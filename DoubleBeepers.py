"""
File: DoubleBeepers.py
Name: Winson Pei
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    put_beeper_back()
    karel_goes_home()


def double_beepers():
    while on_beeper():
        # old beepers, facing East
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        # new beepers, facing East
        turn_around()
        move()
        # old beepers, facing West
        turn_around()


def turn_around():
    for i in range(2):
        turn_left()


def put_beeper_back():
    move()
    while on_beeper():
        # old beepers, facing West
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        # new beepers, facing West
        turn_around()
        move()
        # old beepers, facing East


def karel_goes_home():
    turn_around()
    move()
    move()
    turn_around()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #


if __name__ == '__main__':
    execute_karel_task(main)
