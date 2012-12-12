#!/usr/bin/python
import traceback
import curses
import creature
import world
import level

class Menu(object):
    def __init__(self):
        menuItems=[]
        
    def menuItem(self):
        pass

def mainMenu():
    pass

def draw_room(room):
    ''' drawing rooms and doors '''
    door_dict={}    ##will be returned
    #print(room.check_doors())
    door_list=room.check_doors()
    #room variables
    room_height=15
    room_width=40
    room_pos_h=2
    room_pos_v=2
    #door variables
    door_pos_h=5
    #drawing room
    room_screen=curses.newwin(room_height,room_width,room_pos_v,room_pos_h)
    room_screen.box()
    room_screen.refresh()
    #drawing static doors
    #door_screen=curses.newwin(3,3,1,20)
    #door_screen.box()
    #drawing label in center
    label_screen=curses.newwin(3,20,8,15)
    #label_screen.addstr(room.export())
    label_screen.refresh()
    ##drawing the doors
    ## 'a' = 97
    key=97
    for d in door_list:
        ##writing the dict
        door_dict[key]=d        
        ##the drawing stuff
        door_screen=curses.newwin(3,3,1,door_pos_h)
        door_screen.box()
        door_pos_h+=4
        door_screen.addstr(1,1,chr(key))
        key+=1
        door_screen.refresh()
        
    return door_dict

def printmenu():
    text='Welcome'
    return text

def generate_menu_items(tmp_list):    
    return item_list    #integer for keyprocessing

def main(main_screen):
    ###lets instance a world
    w=world.World()

    ##instance some screens
    main_screen.refresh()
    export_screen=curses.newwin(6,80,17,0)
    export_screen.refresh()
    export_screen.idlok(1)    ###for scrolling
    export_screen.scrollok(1)

    ###loading Files
    status=w.loadFiles(w.filenames)
    export_screen.addstr(' \n [s] to start\n [q] to quit ')
    export_screen.refresh()

    #generating level
    l=level.Level()
    #print(l.export())
            
    ###always start in room 0
    room=(world.World.rooms[0])
    
    while True:
        key=main_screen.getch()
        t=1
        
        if key==ord('q'):
            break
        if key==ord('t'):
            t+=1
            export_screen.addstr('asdfasfdasfd{}\n'.format(t))
        if key==ord('s'):
            
            while True:
                #main_screen.clear()
                door_dict=draw_room(room)
                export_screen.addstr('{} \n'.format(room.export()))
                export_screen.refresh()
                key=main_screen.getch()
                if key==ord('q'):
                    break
                if key in door_dict.keys():
                    d=world.World.doors[door_dict[key]]
                    for i in d.door_tupel:
                        if i!=room.number:
                            room=world.World.rooms[i]
                            break
                main_screen.erase()
                main_screen.refresh()                    

        main_screen.refresh()
        export_screen.refresh()

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
