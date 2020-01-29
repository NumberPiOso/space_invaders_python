import numpy as np
import curses
from entities import space_ship

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

print(sh, sw)
player = space_ship(sw//4, sh//2)

key = curses.KEY_RIGHT

w.addch(sh//2, sw//2, curses.ACS_PI)

while True:
    next_key = w.get_wch()
    key = key if next_key == -1 else next_key

    if next_key in [curses.KEY_F0]:
        curses.endwin()
        quit()
 
    if key == curses.KEY_RIGHT:
        player.turn_rigth
    if key == curses.KEY_LEFT:
        player.turn_left
    if key == curses.KEY_UP:
        player.incr_vel
    if key == curses.KEY_DOWN:
        player.decr_vel

    w.addch(player.x, player.y, curses.ACS_CKBOARD)