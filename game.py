#!/usr/bin/python3

import creature
import world
import curses

def main():
    
    world.World.loadFiles(world.World.filenames)
    menuscreen=curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    while True:
        h=creature.Human()
        world.World.creatures[h.number]=h
        menuscreen.addstr(12,0,h.export())
        q=menuscreen.getch()
        
        if q==ord('q'):
            break
        
    curses.endwin()

if __name__=='__main__':
    main()
