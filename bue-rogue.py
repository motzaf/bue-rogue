#!/usr/bin/python3

import traceback
import curses
import random
import os

class World(object):
    ''' contains dictionary and lists containing instances '''

    #Dictionaries
    creatures={}
    rooms={}
    levels={}
    doors={}
    items={}
    quests={}
    quantityWords={0.0:'not a all',0.2:'a litte',0.4:'somewhat',0.6:'quite',0.8:'much'}
    approvalWords={-0.7:'hates',0.0:'ignores',0.7:'loves'}

    #Lists
    colornames=[]
    firstnamesf=[]
    firstnamesm=[]
    lastnames=[]
    traitnames=[]

    #Filelist
    filenames=['colornames.txt','firstnamesf.txt','firstnamesm.txt','lastnames.txt','traitnames.csv']

    
    def load_files(self,filenames=[]):
        ''' loads all files into dictionaries and lists '''
        text='Loading Files:'
        lines=[]
        for f in World.filenames:
            fo=open(os.path.join('data',f))
            lines=fo.readlines()
            fo.close()

            if f[:-4] in World.__dict__.keys():
                text+=f
                World.__dict__[f[:-4]].extend(lines)
        text+='done'
        return text

class Creature(object):
    ''' default creature '''
    number = 0
    
    def __init__(self, roomnumber=1):
        self.number=Creature.number
        Creature.number+=1
        World.creatures[self.number]=self    ##put instance in world dictionary    
    
        self.sex=random.choice(['m','f'])
        
        #General Attibutes
        self.intelligence=0.0
        self.vitality=0.0
        self.charisma=0.0
        self.emphathy=0.0
        self.thirst=0.0
        self.hunger=0.0
        
        self.memory=[]
        self.flaw=[]
        self.trait=[]
        self.skills=[]
        
class Human(Creature):
    ''' humanoid '''

    def __init__(self):
        Creature.__init__(self)
        self.name=self.create_name()        

    def create_name(self):
        if self.sex=='m':
            fn=random.choice(World.firstnamesm)
        else:
            fn=random.choice(World.firstnamesf)
        ln=random.choice(World.lastnames)
        return fn[:-1]+' '+ln[:-1]

    def export(self):
        text='--------------------\n'
        text+='Name: {} \nSex: '.format(self.name)
        if self.sex=='m':
            text+='Male'
        else:
            text+='Female'
        text+='\n--------------------\n'
        return text

class Level(object):
    counter=0
    #self.rooms=[]
    #### other options ueber alle raeume iterieren und schaun welches level ihm gehoert
    def __init__(self):
        self.is_lobby=True
        self.number=Level.counter
        Level.counter+=1
        self.lobby_nr=-1
        self.corridor_nr=-1
        self.corridors = 0     # number of corridors in this level
        self.maxcorridors = 25 # avoid stack overvlow with recursive function
        World.levels[self.number]=self
        self.generate_rooms(self.lobby_nr, 3,9)
        #self.generate_rooms2() # motz funktionsaufruf
        
        
        #self.bathroom_counter=random.randint(1,3)
        #self.corridor_counter=random.randint(3,6)
    

    def generate_rooms2(self,connect_room_to=0):
        for i in range(3,7):
            if self.is_lobby:
                room=Room(self.number,'lobby')
                self.is_lobby=False
                room=Room(self.number,'corridor')
                #corridor_counter-=1
                Door(self.number,room.number,connect_room_to)
                connect_room_to=room.number

            else:
                room=Room(self.number,random.choice(Room.roomtypes))
                Door(self.number,room.number,connect_room_to)
                if room.roomtype=='corridor':
                    self.generate_rooms2(room.number) 


    def generate_rooms(self,startroomnumber,minRooms=3,maxRooms=9):
        """recursive function to generate an start room (can be the lobby)
           and some other rooms connected to this startroom"""
        
        for r in range(0,random.randint(minRooms,maxRooms+1)): 
            if startroomnumber==-1:
                #  
                tmp_room=Room(self.number,'lobby')
                self.lobby_nr=tmp_room.number      # set the level-wide lobby-nr
                startroomnumber = tmp_room.number  # set the startroomnumber
            else:
                tmp_room = Room(self.number)                      #create non-lobby-room
                Door(self.number,startroomnumber,tmp_room.number) #create door to start rooom
                if tmp_room.roomtype == 'corridor':
                    self.corridors += 1            # increase level-wide corridorcounter
                    if self.corridors < self.maxcorridors:        #avoid stack-overvlow
                        self.generate_rooms(tmp_room.number)      # recursion
                

    def export(self):
        text='\nLevel: {}\n'.format(self.number)
        for r in World.rooms:

            if World.rooms[r].level == self.number:
                text+=World.rooms[r].export()
        text+='\n************+\n'
        return text

class Room(object):
    counter=0
    roomtypes=['corridor','storeroom','office','bathroom','cantina']
    def __init__(self,level,roomtype=''):
        self.level=level
        self.number=Room.counter
        Room.counter+=1
        World.rooms[self.number]=self
        if roomtype=='':
            self.roomtype=random.choice(Room.roomtypes)
        else:
            self.roomtype=roomtype
            
        #self.lobby=False
        #self.bathroom=False
        #self.corridor=False
        #self.doors=[]

    def check_doors(self):
        doorlist=[]
        for d in World.doors:
            if World.doors[d].level == self.level:
                if self.number in World.doors[d].door_tupel:
                    doorlist.append(World.doors[d].number)        
        return doorlist

    def export(self):
        text='\nRoomnumber: {} {}\n'.format(self.number,self.roomtype)
        text+='Number of Doors: {} \n'.format(len(self.check_doors()))   
        return text
       
class Door(object):
    number=0

    def __init__(self,level,room1nr,room2nr):
        self.level=level
        self.number=Door.number
        Door.number+=1
        World.doors[self.number]=self
        self.locked=False
        self.forbidden=False
        self.door_tupel=(room1nr,room2nr)

    def export(self):
        text='\nDoornumber: {} \n'.format(self.number)
        text+='connecting: {} with {} \n'.format(self.door_tupel[0],self.door_tupel[1])
        return text


class Item(object):
    ###epic liste von eigenschaftsworten gewisse wschl. bez. eigenschaft
    adj=['org','ur','episch','leiwand','viech','voi','fett']
    nom=['bleistift','zeichenblock','kugelschreiber','bürogueklammer','tischlampe','blumentopf']
    number=0

    def __init__(self,roomnumber=-1):
        self.roomnumber=roomnumber
        self.number=Item.number
        Item.number+=1
        World.items[self.number]=self
        self.name=self.name_generator()

    def name_generator(self,name=''):
        if name=='':
            name=random.choice(Item.nom)
        
        if random.random()<0.3:
            tmpadj=Item.adj[:]  # full copy
            adj=random.choice(tmpadj)
            for myadj in Item.adj:
                if myadj in name:
                    tmpadj.remove(myadj)
            if len(tmpadj)>0:
                name=random.choice(tmpadj)+' '+name
                return self.name_generator(name)
            else:
                return name

        else:
            return name

class Menu(object):
    def __init__(self):
        pass

def main_menu():
    screen=curses.newwin(10,5,5,30)
    screen.keypad(1)
    menu_items=['play','test','quit']
    #screen.addstr('asdf',curses.color_pair(1))
    item=0
    for m in menu_items:
        screen.addstr(menu_items.index(m),0,m)
    screen.addstr(item,0,menu_items[item],curses.color_pair(1))
    while True:
        key=screen.getch()
        if key==258:  ###key_up
            item+=1
            screen.addstr(item,0,menu_items[item],curses.color_pair(1))
            
        if key==ord('q'):
            break
        
    #m=Menu()
    #for item in menu_items:
    #return 's'

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

def generate_menu_items(tmp_list):    
    return item_list    #integer for keyprocessing

def main(main_screen):
    ###lets instance a world
    w=World()

    ##instance some screens
    main_screen.refresh()
    export_screen=curses.newwin(6,80,17,0)
    export_screen.refresh()
    export_screen.idlok(1)    ###for scrolling
    export_screen.scrollok(1)

    ###loading Files
    status=w.load_files(w.filenames)
    export_screen.addstr(' \n [s] to start\n [q] to quit ')
    export_screen.refresh()

    #generating level
    l=Level()
    #print(l.export())
            
    ###always start in room 0
    room=(World.rooms[0])
    
    while True:
        main_menu()
        
        key=main_screen.getch()
        if key==ord('q'):
            break

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
                    d=World.doors[door_dict[key]]
                    for i in d.door_tupel:
                        if i!=room.number:
                            room=World.rooms[i]
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
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
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
