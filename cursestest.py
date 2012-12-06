#!/usr/bin/python
import curses
import curses.textpad

def printmenu():
    text='Welcome'
    return text

def printtext():
    text='asdf\nasfd\nasfd'
    return text

def main():
    menuScr=curses.initscr()
    curses.noecho()
    curses.cbreak()

    ##colors
    curses.start_color()
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)

    curses.curs_set(0)
    
    menuScr.addstr(2,3,printmenu())
    #menuScr.hline(3,3,'*',10)

    ##initialize some windows
    statusScr=curses.newwin(15,15,5,20)
    testScr=curses.newwin(5,5,22,5)


    curses.textpad.rectangle(menuScr,4,4,15,15)
    

    while True:
        
        key=menuScr.getch()
        
        if key==ord('q'):
            break
        elif key==ord('a'):
            menuScr.addstr(3,12,'asdf')            
        elif key==ord('t'):
            ###output in other window
            statusScr.addstr(0,0,printtext(),curses.color_pair(1))
            statusScr.refresh()
        elif key==ord('c'):
            ##make some colorful output
            testScr.addstr(0,0,printtext(),curses.color_pair(2))
            testScr.refresh()

            
    curses.nocbreak()        
    curses.endwin()




if __name__=='__main__':
    main()
