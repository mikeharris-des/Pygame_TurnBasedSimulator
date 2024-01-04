# *******************************************
# Requires LINUX OS Library pygame 
# *******************************************

import pygame
import random
import os
os.environ['SDL_AUDIODRIVER'] = 'dummy' #disable audio (issues related with my vm audio)

# ******************** CONSTANTS ***********************

width, height = 1200, 600
rows, columns = 12, 6
# each image 64px

# rgb
red = (255, 0, 0)
white = (50, 50, 50)
black = (0, 0, 0)
green = (173, 255, 5)

fps = 60
cellsize = 100
# Turn at 0, game hasn't started
turn = 0



# ******************** INITIALIZE **********************
# INIT PYGAME
pygame.init()

# TITLE CAPTION
pygame.display.set_caption('BLOCCO') #name of the game

# INITIALIZE USER1 PIECE
user1idle = pygame.image.load('user1idle.png')
user1 = pygame.image.load('user1.png')
# USER1 STARTING CELL
user1_xpos = 0
user1_ypos = 0

# INITIALIZE USER2 PIECE
user2idle = pygame.image.load('user2idle.png')
user2 = pygame.image.load('user2.png')
# USER2 STARTING CELL
user2_xpos = 0
user2_ypos = 0

# WINDOW
window = pygame.display.set_mode((width, height))
window.fill((127, 127, 127))

# ******************** FUNCTIONS **********************

# FUNCTION FOR CONVERTING PXL TO CELL SQUARE (TILE, SPACE)
# y is rows
# x is columns
def cell2pxl(x,y):
    cell_x = cellsize*x + cellsize//2
    cell_y = cellsize*y + cellsize//2
    return [cell_x, cell_y]

# FUNCTION FOR DRAWING GRID FROM CHECKER PATTERN TUTORIAL
def drawgrid():
    current_colour = white
    window.fill(white)

    for i in range(0, rows):
        for j in range(0, columns):
            pygame.draw.rect(window, current_colour, (i * cellsize, j * cellsize, cellsize, cellsize))

            if current_colour == white:
                current_colour = black
            else:
                current_colour = white
        if current_colour == white:
            current_colour = black
        else:
            current_colour = white

#IMAGE USED DETERMINED BY TURN
# ARGUMENTS ARE CELL VALUE X,Y USING CELL2PXL
def drawuserone(x1, y1, t):
    # CELLCOORD LIST
    # ACCESS LIST VIA INDEXES
    cell_coord = cell2pxl(x1, y1)
    # VAR EXIST ONLY IN FUNC
    p_x = cell_coord[0]
    p_y = cell_coord[1]

    offset = 0
    # COMPARE ==
    # ASSIGN =
    if user1_xpos == user2_xpos and user1_ypos == user2_ypos:
        offset = 10
    # BY DEFAULT DISPLAY USER 1
    img = user1
    # t will be turn variable with values 0,1,2
    # != is mot
    if t != 1:
        # IF IT IS NOT USER1TURN
        img = user1idle
    # screen.blit draws image at coordinate on screen at (x1,y1) upon update
    # screen.blit(image,x_coord,y_coord) (set as x1,y1 redifined)
    # p_x-32 -> correction for image centering
    window.blit(img, (p_x-32-offset, p_y-32))


#IMAGE USED DETERMINED BY TURN
# ARGUMENTS ARE CELL VALUE X,Y USING CELL2PXL
def drawusertwo(x2, y2, t):
    # CELLCOORD LIST
    # ACCESS LIST VIA INDEXES
    cell_coord = cell2pxl(x2, y2)
    # VAR EXIST ONLY IN FUNC
    p_x = cell_coord[0]
    p_y = cell_coord[1]

    offset = 0
    if user1_xpos == user2_xpos and user1_ypos == user2_ypos:
        offset = 10
    # BY DEFAULT DISPLAY USER 1
    img = user2
    # t will be turn variable with values 0,1,2
    # != is not
    if t != 2:
        # IF IT IS NOT USER1TURN
        img = user2idle

    # screen.blit draws image at coordinate on screen at (x1,y1) upon update
    # screen.blit(image,x_coord,y_coord) (set as x1,y1 redifined)
    # p_x-32 -> correction for image centering
    window.blit(img, (p_x-32+offset, p_y-32))


# FUNCTION FOR RAN DICE 6 SIDED DI ROLL - ONLY 1 ARG - BUT CALLING TWICE
def diceroll():
    d1 = random.randint(1, 6)
   # d2 = random.randint(1, 6)
    return d1

# userrollstr = str(diceroll())
# TEXT TO SCREEN FOR  - INSTRUCTIONS, TURN, DICE ROLL, VICTORY
# THREE ARGs: str message, & xyCOORDINATES TO DISPLAY
def texttoscreen(text,x,y):
#   USING SYSTEM FONT
    font = pygame.font.Font(None, 24)
    text_user1turn = font.render(text, False, green)
#   textsurface = font.render("text", False, color)  # "text", antialias, color
#   surface.blit(textsurface, (x, y))
    window.blit(text_user1turn, (x, y))

# TEXT TO SCREEN BUT LARGE FONT!
def bannertoscreen(text,x,y):
    font = pygame.font.Font(None, 50)
    banner = font.render(text, False, green)
    window.blit(banner, (x, y))

# FUNC FOR UPDATING USER ONE LOCATION X Y
# TAKE IN result OF diceroll()
# MOVE ONCE
# user1 = 0,0
# check to see if at border cell
    # FUNC FOR USER2 MOVEMENT
    # IF USER PIECE REACHES FINISH LINE CELL[11,0]
    # DONT MOVE
def moveuser1():
    # Refer to global var
    global user1_xpos
    global user1_ypos

    if user1_xpos == 11 and user1_ypos == 0:
        return
    if user1_xpos % 2 == 0:
        if user1_ypos < 5:
             user1_ypos = user1_ypos + 1
        else:
            user1_xpos = user1_xpos + 1
    else:
        if user1_ypos > 0:
            user1_ypos = user1_ypos - 1
        else:
            user1_xpos = user1_xpos + 1

# FOR LOOP TO UPDATE USER POS
# CALL MOVEUSER1 FUNC
def moveuser1_cont(roll):
    global user1_xpos
    global user1_ypos
    # DICE ROLL
    for i in range(roll):
        moveuser1()
    print("user1 " + str(user1_xpos) + " " + str(user1_ypos))


    # FUNC FOR USER2 MOVEMENT
    # IF USER PIECE REACHES FINISH LINE CELL[11,0]
    # DONT MOVE
def moveuser2():
    global user2_xpos
    global user2_ypos

    if user2_xpos == 11 and user2_ypos == 0:
        return
    if user2_xpos % 2 == 0:
        if user2_ypos < 5:
             user2_ypos = user2_ypos + 1
        else:
            user2_xpos = user2_xpos + 1
    else:
        if user2_ypos > 0:
            user2_ypos = user2_ypos - 1
        else:
            user2_xpos = user2_xpos + 1

# FOR LOOP TO UPDATE USER POS
# USES ARG ROLL FROM DI ROLL
def moveuser2_cont(roll):
    global user2_xpos
    global user2_ypos
    # DICE ROLL
    for i in range(roll):
        moveuser2()
        # NEED TO CONVERT TO STRING
    print("user2 " + str(user2_xpos) + " " + str(user2_ypos))

# FUNCTION DRAWS TRACEW WHERE PREVIOUS POSITION HELD ON PREVIOUS TURN OF RESPECTED USER
def drawtrace(x,y):
    cell_coord = cell2pxl(x, y)
    # VAR EXIST ONLY IN FUNC
    p_x = cell_coord[0]
    p_y = cell_coord[1]
    #pygame.draw.circle(surface, colour, (x,y), radius)
    pygame.draw.circle(window, green, (p_x, p_y), 8)

# FUNC CHECKS IF USER IS BOARDGAME FINAL CELL [11,0]
# RETURNS INT CORRESPONDING TO BOOLEAN, W. '0' RETURNED IF NOONE WON YET
def checkwinner():
    # GLOBAL CALL
    global user1_xpos
    global user1_ypos
    global user2_xpos
    global user2_ypos

    if user1_xpos == 11 and user1_ypos == 0:
        return 1
    elif user2_xpos == 11 and user2_ypos == 0:
        return 2
    # NO WINNER
    else:
        return 0


# ******************** FUNCTIONS **********************


# MAIN FUNCTION
def main():
    running = True
    turn = 0
    roll1 = 0
    roll2 = 0
    winner = False

    # GLOBAL CALL
    global user1_xpos
    global user1_ypos
    global user2_xpos
    global user2_ypos

    # CONTROL FRAME RATE w. CLOCK
    clock = pygame.time.Clock()

    #DEBUG CELL AS PIXEL VALUE
    #print(cell2pxl(0, 0))

    while running:
        clock.tick(fps)

        # FOR LOOP WILL LOOP CHECK WHICH EVENTS ARE UPDATING
        #  SCREEN DISPLAY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # WHEN EVENT HAPPENS
            # DRAW GRID FIRST, AFTER UPDATING REDRAW SCREEN TO REMOVE LINGERERING EVENT
            drawgrid()
            # UPDATE EVERYTHING AFTER EVENT

            if turn == 0:
                bannertoscreen("CLICK MOUSE-BUTTON TO WATCH A REPLAY", 0, 100)
                bannertoscreen("OF THE 2022 BLOCCO WORLD FINALS",0, 150)
                bannertoscreen("(MOUSECLICK TO SHOW EACH TURN)", 0, 200)
            else:
                texttoscreen("USER "+str(turn)+"'s TURN", 0, 0)


            # KEY INPUT UDPDATES SCREEN
            # CHANGE TURN ON A CLICK
            if event.type == pygame.MOUSEBUTTONDOWN and winner == False:
                if turn == 0:
                    turn = 1
                elif turn == 1:
                    turn = 2
                elif turn == 2:
                    turn = 1


                # only drawing to screen when button is held

                # ROLL FUNCTION CALL
                roll1 = diceroll()
                roll2 = diceroll()

                # MOVE USER FUNCTION CALL
                if turn == 1:
                    moveuser1_cont(roll1+roll2)

                elif turn == 2:
                    moveuser2_cont(roll1+roll2)

                #UPDATE USER MOVEMENT HERE

            texttoscreen("USERS ROLL WAS " + str(roll1) + ", " + str(roll2), 525, 0)

            # CALL CHECK WINNER
            chickendinner = checkwinner()
            if chickendinner > 0:
                bannertoscreen("USER " + str(chickendinner) + " WINS", 400, 200)
                winner = True

            # call user func AT END WHILE LOOP
            if turn == 2:
                drawuserone(user1_xpos, user1_ypos, turn)
                drawusertwo(user2_xpos, user2_ypos, turn)
            else:
                drawusertwo(user2_xpos, user2_ypos, turn)
                drawuserone(user1_xpos, user1_ypos, turn)

        # INSIDE WHILE LOOP
        pygame.display.update()

    # WHILE LOOP EXIT
    pygame.quit()

# ***************************************************************

# CALL MAIN FUNCTION
main()
