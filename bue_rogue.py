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
    tiles={}
    roomtypes = [] 
    #quantityWords={0.0:'not a all',0.2:'a litte',0.4:'somewhat',0.6:'quite',0.8:'much'}
    #approvalWords={-0.7:'hates',0.0:'ignores',0.7:'loves'}

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
    
    def __init__(self, roomnumber=0):
        self.number=Creature.number
        Creature.number+=1
        World.creatures[self.number]=self    ##put instance in world dictionary    
        self.roomnumber=roomnumber
    
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

    def __init__(self,roomnumber=0):
        Creature.__init__(self,roomnumber=0)
        self.name=self.create_name()
        self.profession=''
        self.boss=-1    #creature.number

    def create_name(self):
        if self.sex=='m':
            fn=random.choice(World.firstnamesm)
        else:
            fn=random.choice(World.firstnamesf)
        ln=random.choice(World.lastnames)
        return fn[:-1]+' '+ln[:-1]

    def export(self):
        text=''
        text+='Name: {} \nSex: '.format(self.name)
        if self.sex=='m':
            text+='Male'
        else:
            text+='Female'
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
        self.maxrooms=4
        self.rooms=0
        World.levels[self.number]=self
        self.safe_lobby()  # motz safe room

        #self.generate_rooms(self.lobby_nr, 2,4)
        #self.generate_rooms2() # motz funktionsaufruf
        
        #self.bathroom_counter=random.randint(1,3)
        #self.corridor_counter=random.randint(3,6)
    
    def safe_lobby(self):
        '''safe and static to test other features'''
        Lobby(self.number)
 
    def generate_rooms(self,startroomnumber,minRooms=1,maxRooms=4):
        """recursive function to generate an start room (can be the lobby)
           and some other rooms connected to this startroom"""
        roomtypeslist = World.roomtypes[:]
        if "Lobby" in roomtypeslist:
            roomtypeslist.remove("Lobby") # remove Lobby
            
        for r in range(0,random.randint(minRooms,maxRooms+1)): 
            if self.maxrooms<self.rooms:
                break
            if startroomnumber==-1:
                #tmp_room=Room(self.number,'lobby')
                tmp_room=Lobby(self.number)
                #self.lobby_nr=tmp_room.number      # set the level-wide lobby-nr
                startroomnumber = tmp_room.number  # set the startroomnumber
            else:
                #rt=random.choice(Room.roomtypes)       ##create non-lobby room
                rt=random.choice(roomtypeslist)       ##create non-lobby room
                #roomtypes=['Corridor','Office','Cantina','Storage'] 
                ###lobby fehlt absichtlich
                ######getattr####WE MISS YOU!!!!!#########
                #print("i create a ", rt)
                #print("vars is", vars(__main__))
                x = "{}({})".format(rt,self.number) # room name and level number
                tmp_room = eval(x)
                #tmp_room = vars()[rt]() # the same as Cantina() if rt == "Cantina"
                
                #if rt=='Corridor':
                #    tmp_room=Corridor(self.number)
                    #tmp_room.x_backdoor=r
                    #create door to start rooom
                    #Door(self.number,startroomnumber,tmp_room.number) 
                #elif rt=='Office':
                #    tmp_room=Office(self.number)
                #elif rt=='Cantina':
                #    tmp_room=Cantina(self.number)
                #elif rt=='Storage':
                #    tmp_room=Storage(self.number)
                tmp_room.x_backdoor=r
                Door(self.number,startroomnumber,tmp_room.number) #create door to start rooom

                if rt=='Corridor':
                    if self.corridors < self.maxcorridors:        #avoid stack-overvlow
                        self.generate_rooms(tmp_room.number)      # recursion    

    def motz_generate_rooms2(self,connect_room_to=0):
        for i in range(3,7):
            if self.is_lobby:
                room=Room(self.number,'lobby')
                self.is_lobby=False
                room=Room(self.number,'corridor')
                Door(self.number,room.number,connect_room_to)
                connect_room_to=room.number

            else:
                room=Room(self.number,random.choice(Room.roomtypes))
                Door(self.number,room.number,connect_room_to)
                if room.roomtype=='corridor':
                    self.generate_rooms2(room.number) 

    def export(self):
        text='\nLevel: {}\n'.format(self.number)
        for r in World.rooms:

            if World.rooms[r].level == self.number:
                text+=World.rooms[r].export()
        text+='\n************+\n'
        return text

class Tile(object):
    '''each room has nine tiles
        -------
        |0|1|2|
        --+-+--
        |3|4|5|
        --+-+--
        |6|7|8|
        -------
    room is a set of 3x3 tiles'''

    number=0
    def __init__(self,roomnumber,pos):
        self.number=Tile.number
        Tile.number+=1
        self.roomnumber=roomnumber
        self.pos=pos
        World.tiles[self.number]=self
        has_door=True


class Room(object):
    '''room is a set of 3x3 tiles'''
    counter=0
    #roomtypes=['Corridor','Office','Cantina','Storage'] ###lobby fehlt absichtlich
    def __init__(self,level):
        self.level=level
        self.number=Room.counter
        Room.counter+=1 ### sind alle ids
        World.levels[self.level].rooms+=1 ###zaehl wieviele raeume ein level hat
        x_backdoor=-1
        World.rooms[self.number]=self
        #if roomtype=='':
        #    self.roomtype=random.choice(Room.roomtypes)
        #else:
        #    self.roomtype=roomtype
        #self.lobby=False
        #self.bathroom=False
        #self.corridor=False
        #self.doors=[]

    def place_doors(self,level):
        doorlist=check_doors(self)
        

    def creature_name_list(self):
        creature_name_list=[]
        for c in World.creatures:
            if World.creatures[c].roomnumber==self.number:
                creature_name_list.append(World.creatures[c].name)
        return creature_name_list

    def creature_list(self): ####test ob kopie oder pointer
        creature_list=[]
        for c in World.creatures:
            if World.creatures[c].roomnumber==self.number:
                creature_list.append(World.creatures[c])
        return creature_list

    def item_list(self): ####test ob kopie oder pointer
        item_list=[]
        for i in World.items:
            if World.items[i].roomnumber==self.number:
                item_list.append(World.items[i])
        return item_list
        
    def check_creatures(self):
        '''number of creatures in this room'''
        count=0
        for c in World.creatures:
            if World.creatures[c].roomnumber==self.number:
                count+=1
        return count

    def check_items(self):
        '''number of items in room returned'''
        count=0
        for i in World.items:
            if World.items[i].roomnumber==self.number:
                count+=1
        return count

    def check_doors(self,tupel_index=0):
        '''gibt obere oder untere tueren zurueck, tupel_index=0 fuer unten 1 fuer oben'''
        doorlist=[]
        for d in World.doors:
            if World.doors[d].level == self.level:
                if self.number == World.doors[d].door_tupel[tupel_index]:
                    doorlist.append(World.doors[d].number)        
        return doorlist

    def export(self):
        #roomname=repr(self)                           # very ugly code from Horst
        #roomname=roomname.split(".")[1].split(' ')[0] # very ugly code from Horst
        roomname = self.__class__.__name__             # found at Stackoverflow
        text='\nRoomnumber: {} {}\n'.format(self.number,roomname)
        text+='Number of Doors: {} \n'.format(len(self.check_doors()))   
        text+='Number of Creatures: {} \n'.format(self.check_creatures())
        text+='Number of Items: {}\n'.format(self.check_items())
        return text

class Office(Room):
    def __init__(self,level):
        Room.__init__(self,level)

class Lobby(Room):
    def __init__(self,level):
        Room.__init__(self,level)    
        World.levels[self.level].lobby_nr=self.number # set the level-wide lobby-nr
        for r in range(0,random.randint(10,20)):
            Human(self.number)
        for r in range(0,random.randint(10,20)):
            Item(self.number)
          
class Corridor(Room):
    def __init__(self,level):
        Room.__init__(self,level)    
        World.levels[self.level].corridors+=1   # increase level-wide corridorcounter
        #self.corridors += 1            

class Storage(Room):
    def __init__(self,level):
        Room.__init__(self,level)    

class Cantina(Room):
    def __init__(self,level):
        Room.__init__(self,level)    

class Door(object):
    number=0
    compass={'n':'s','s':'n','e':'w','w':'e'}

    def __init__(self,level,room1nr,room2nr,room1_facing):
        self.facing=room1_facing  ###direction of door from room 1 (N,S,E,W)
        self.counter_facing=Door.compass[self.facing]
        self.level=level
        self.number=Door.number
        Door.number+=1
        World.doors[self.number]=self
        self.locked=False
        self.forbidden=False
        self.door_tupel=(room1nr,room2nr)

    def export(self):
        text='Doornumber: {} \n'.format(self.number)
        text+='connecting: {} with {} \n'.format(self.door_tupel[0],self.door_tupel[1])
        text+='heading {} (counter {})'.format(self.facing,self.counter_facing)
        return text

class Item(object):
    ###epic liste von eigenschaftsworten gewisse wschl. bez. eigenschaft
    adj=['org','ur','episch','leiwand','viech','voi','fett']
    nom=['bleistift','zeichenblock','kugelschreiber','bürogueklammer','tischlampe','blumentopf']
    number=0

    def __init__(self,roomnumber=0):
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

    def export(self):
        return 'ItemetI'

class Menu(object):
    def __init__(self):
        self.screen=curses.newwin(24,50,0,0)
        self.export=curses.newwin(20,30,0,30)
        self.screen.keypad(1)
        self.screen.idlok(1)    ###for scrolling
        self.screen.scrollok(1)

        self.up_keys=(259,ord('k'))
        self.down_keys=(258,ord('j'))

    def run(self,menu_items):
        counter=0
        for m in menu_items:
            self.screen.addstr(menu_items.index(m),0,m.name)
        while True:
            pos=counter%len(menu_items)
            self.screen.addstr(pos,0,menu_items[pos].name,curses.color_pair(3))
            self.screen.refresh()
            self.export.addstr(0,0,menu_items[pos].export())
            self.export.refresh()
            key=self.screen.getch()
            self.export.erase()
            if key in self.down_keys:
                pos_old=counter%len(menu_items)
                counter+=1
                pos=counter%len(menu_items)
                self.screen.addstr(pos,0,menu_items[pos].name,curses.color_pair(3))
                self.screen.addstr(pos_old,0,menu_items[pos_old].name)

            if key in self.up_keys:
                pos_old=counter%len(menu_items)
                counter-=1
                pos=counter%len(menu_items)
                self.screen.addstr(pos,0,menu_items[pos].name,curses.color_pair(3))
                self.screen.addstr(pos_old,0,menu_items[pos_old].name)

            if key==ord('q'):
                self.screen.erase()
                break

#def get_roomtypelist():
#        """browses all subclasses of Room and returns
#        a list with the class names.
#        Assumes that first char of a classname is correctly uppercase."""
#        roomtypeslist = []
#        print('da muss er herkommen',vars().keys())
#        for classname in [thing for thing in dir() if thing[0].isupper() ]:
#            for basename in vars()[classname].__bases__:
#                print(classname,basename)
#                if ".Room" in str(b):  # the current class is based on Room class
#                    roomtypeslist.append(classname)
#        return roomtypeslist

def main_menu():
    screen=curses.newwin(10,5,5,30)
    screen.keypad(1)
    menu_items=[('play','s'),('test','t'),('reset','r'),('quit','q')]
    #screen.addstr('asdf',curses.color_pair(1))
    counter=0
    for m in menu_items:
        screen.addstr(menu_items.index(m),0,m[0])
    screen.addstr(0,0,menu_items[0][0],curses.color_pair(2))
    while True:
        key=screen.getch()
        #if key==258 and item < len(menu_items)-1:  ###key_down
        #    item+=1
        #    screen.addstr(item,0,menu_items[item],curses.color_pair(2))
        #    screen.addstr(item-1,0,menu_items[item-1])
        #if key==259 and item > 0:  ###key_up
        #    item-=1
        #    screen.addstr(item,0,menu_items[item],curses.color_pair(2))
        #    screen.addstr(item+1,0,menu_items[item+1])

        if key==258:
            pos_old=counter%len(menu_items)
            counter+=1
            pos=counter%len(menu_items)
            screen.addstr(pos,0,menu_items[pos][0],curses.color_pair(2))
            screen.addstr(pos_old,0,menu_items[pos_old][0])

        if key==259:
            pos_old=counter%len(menu_items)
            counter-=1
            pos=counter%len(menu_items)
            screen.addstr(pos,0,menu_items[pos][0],curses.color_pair(2))
            screen.addstr(pos_old,0,menu_items[pos_old][0])

        if key in (curses.KEY_ENTER, curses.KEY_RIGHT, curses.KEY_LEFT):
            screen.erase()
            pos=counter%len(menu_items)
            return ord(menu_items[pos][1])

        if key==ord('q'):
            screen.erase()
            return ord('q')
        
    #m=Menu()
    #for item in menu_items:
    #return 's'

def draw_room2(room):
    #room variables
    room_height=15
    room_width=40
    room_pos_h=2
    room_pos_v=2
    #door variables #### roemischen sind da drin
    #door_pos_h=5
    #door_pos_v=1 # oder 17
    #drawing room
    room_screen=curses.newwin(room_height,room_width,room_pos_v,room_pos_h)
    room_screen.box()
    room_screen.refresh()
    
    door_dict={}
    key=97
    for w in [0,1]:
    #for w in [0]:
        door_list=room.check_doors(w)
        #print("doorlist,w",door_list,w)
        for d in door_list: # türnummern
            ##writing the dict
            door_dict[key]=d        
            ##the drawing stuff
            if w==0: 
                door_pos_v=1
            else:
                door_pos_v=15
                
            up_room_number=World.doors[d].door_tupel[1]    
            for r in World.rooms:
                # suche jenen Raum, dessen Raumnummer die 2. Raumnummer 
                #der aktuellen türe ist(doortuple)
                #nimm von diesem Raumdie  xbackdoor koordinate
                if World.rooms[r].number==up_room_number:
                    door_pos_h=World.rooms[r].x_backdoor
                    break
            door_screen=curses.newwin(3,3,door_pos_v,door_pos_h*3+3)
            door_screen.box()
            door_screen.addstr(1,1,chr(key))
            key+=1
            door_screen.refresh()
        
    return door_dict

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
    export_screen=curses.newwin(5,80,18,0)
    export_screen.refresh()
    export_screen.idlok(1)    ###for scrolling
    export_screen.scrollok(1)

    ###loading Files
    status=w.load_files(w.filenames)
    #export_screen.addstr(' \n [s] to start\n [q] to quit ')
    export_screen.refresh()

    #generating level
    l=Level()
    #print(l.export())
            
    ###always start in room 0
    room=(World.rooms[0])
    
    while True:
        key=main_menu()
        
        #key=main_screen.getch()
        if key==ord('q'):
            break

        if key==ord('t'):
            h=Human()
            export_screen.addstr(h.export())
        if key==ord('r'):
            pass    ##TODO##

        if key==ord('s'):
            
            while True:
                #main_screen.clear()
                door_dict=draw_room2(room)
                export_screen.addstr('{} \n'.format(room.export()))
                export_screen.refresh()
                key=main_screen.getch()
                if key==ord('q'):
                    break
                if key==ord('z'):
                    m=Menu()
                    m.run(room.creature_list())
                if key==ord('x'):
                    m=Menu()
                    m.run(room.item_list())
                if key in door_dict.keys():
                    d=World.doors[door_dict[key]]
                    for i in d.door_tupel:
                        if i!=room.number:
                            room=World.rooms[i]
                            break
                main_screen.erase()
                main_screen.refresh()                    

        main_screen.erase()
        main_screen.refresh()
        export_screen.erase()
        export_screen.refresh()

if __name__=='__main__':
    # generate dynamic roomtypes list over all child classes of class Room
    # Assumes that first char of a classname is correctly uppercase.
    # Motz will kill this code because of ugliness and replace it with a
    # static list of roomtypes. This makes Horst a very sad Panda
    #print('da muss er herkommen',vars().keys())
    for classname in [thing for thing in dir() if thing[0].isupper() ]:
            for basename in vars()[classname].__bases__:
                if ".Room" in str(basename):  # the current class is based on Room class
                    World.roomtypes.append(classname)

    try:
        mainscr=curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
        curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLUE)
        curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
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
