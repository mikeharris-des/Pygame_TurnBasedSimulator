NAME:
	MICHAEL ANASTASAKIS
	mikeharris.des@gmail.com

TURN BASED SIMULATOR APPLICATION:

    This program simulates a turn based board game for two users. Each User rolls a pair of dice and the
    result sum of the roll determines the number of tiles they move. The first one to reach the last tile
    wins this game known as Blocco. The program handles idle and active user sprites for a given turn with
    interface update/refresh inside a simple game loop.

    Requires user interaction in the event of mouse clicks to watch each turn die roll event and user moves.
    NOTE: repeated mouse clicks in close succession may cause latency issues or undefined behaviour of the
    program

REQUIREMENTS:
    pycharm library (comes default installed on Ubuntu 22.04 for LINUX OS)

TESTED:
    on Ubuntu 22.04 Linux VM (Virtual Box)

ACKNOWLEDGEMENTS:
    I would like to express my gratitude to Professor Robert Collier for providing the initial outline and
    specifications for several Python assignments during my time at University. These assignments served as
    the foundation for the project for this class presented here.
---------------------------------------------------------------------------------------------------------------

LAUNCH INSTRUCTIONS:
   * Ensure the 4 png images are in the directory containing the python file main.py:
	   user1.png
	   user2.png
	   user1idle.png
       user2idle.png

   * in console navigate to directory containing main.py file and enter:
       python3 main.py

TEST INSTRUCTIONS:

   repeatedly click the pygame interface window in succession at a pace of 1-2 clicks per second to watch the
   pieces simulate movement in a turn pace game

   CTRL+C in the console to quit or use the 'x' button on the window to quit
