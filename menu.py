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
    curses.curs_set(0)
    
    menuScr.addstr(2,3,printmenu())
    #menuScr.hline(3,3,'*',10)

    statusScr=curses.newwin(15,15,5,20)
    curses.textpad.rectangle(menuScr,4,4,15,15)

    while True:
        
        key=menuScr.getch()
        
        if key==ord('q'):
            break
        elif key==ord('a'):
            menuScr.addstr(3,12,'asdf')            
        elif key==ord('t'):
            statusScr.addstr(0,0,printtext())
            statusScr.refresh()
            
    curses.endwin()


