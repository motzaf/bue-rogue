#!/usr/bin/python3
import traceback
import random
import curses

class Card(object):
    def __init__(self,coordinates=(0,0)):
        self.coordinates=coordinates
        self.name='card'
    
    def export(self):
        text ='#### ###'
        return text

class Room(object):
    def __init__(self):
        self.cards={}
        self.doors={}
        self.__build__()

    def __build__(self):
        for v in range(3):
            for h in range(3):
                self.cards[(v,h)]=Card((v,h))

    def export(self):
        text=''
        for c in self.cards:
            text+='{}'.format(self.cards[c].coordinates)
        return text

class Level(object):
    def __init__(self):
        self.rooms={}

def main(main_screen):
    r=Room()
    for c in r.cards:
        v=c[0]*5+1
        h=c[1]*8+1
        screen=curses.newwin(5,8,v,h)
        screen.addstr(2,1,'{}'.format(c))
        #screen.box()
        screen.refresh()
        screen.getch()

if __name__=='__main__':
    try:
        main_screen=curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
        curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLUE)
        curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
        
        main(main_screen)

        curses.echo()
        curses.nocbreak()
        curses.endwin()
    except:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()
    finally:
        pass
