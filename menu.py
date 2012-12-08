#!/usr/bin/python
import traceback
import curses
import creature
import world

class Menu(object):
    def __init__(self):
        menuItems=[]
        
    def menuItem(self):
        pass

def mainMenu():
    pass

def printmenu():
    text='Welcome'
    return text

def printtext():
    text='asdf\nasfd\nasfd'
    return text

def main(mainScreen):
    ###lets instance a world
    w=world.World()
    #menuscr.addstr(2,3,printmenu())
    #menuScr.hline(3,3,'*',10)
    #statusscr=curses.newwin(15,15,5,20)
    #curses.textpad.rectangle(menuScr,4,4,15,15)

    mainScreen.refresh()
    
    exportScreen=curses.newwin(6,80,17,0)
    #exportScreen.border(' ',' ',0,0,' ',' ',' ',' ')
    exportScreen.refresh()

    mainmenuScreen=curses.newwin(10,10,0,69)
    mainmenuScreen.border(' ',' ',' ',' ',' ','?',' ',' ')
    mainmenuScreen.refresh()

    roomScreen=curses.newwin(15,40,2,2,)
    roomScreen.box()
    roomScreen.refresh()

    ###loading Files
    status=w.loadFiles(w.filenames)
    #mainScreen.addstr(status)

    while True:
        key=mainScreen.getch()
        
        if key==ord('q'):
            break
        elif key==ord('a'):
            mainScreen.addstr(3,12,'asdf')
        elif key==ord('?'):
            mainmenuScreen.addstr(2,0,'(?)elp\n(q)uit\n(t)ext\n(c)reate\n(l)ist')
        elif key==ord('t'):
            exportScreen.addstr(1,0,printtext())
        elif key==ord('c'):
            h=creature.Human()
            exportScreen.addstr(1,0,h.export())
        elif key==ord('l'):
            for h in world.World.creatures:
                mainScreen.addstr(1,0,world.World.creatures[h].export())
                tmp=mainScreen.getch()
        mainScreen.refresh()
        mainmenuScreen.refresh()
        exportScreen.refresh()

if __name__=='__main__':
    try:
        mainscr=curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        ############
        main(mainscr)
        ############
        curses.echo()
        curses.nocbreak()
        curses.endwin() 
    except:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()
    finally:    #durchlesen und checken
        pass
