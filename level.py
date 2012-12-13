import random
import world

class Level(object):
    number=0
    #self.rooms=[]
    #### other options ueber alle raeume iterieren und schaun welches level ihm gehoert
    def __init__(self):
        self.number=Level.number
        Level.number+=1
        world.World.levels[self.number]=self
        self.generate_rooms(3,9)

    def generate_rooms(self,minRooms=3,maxRooms=9):
        corridor_nr=-1
        bathroom_nr=-1
        lobby_nr=-1

        for r in range(0,random.randint(minRooms,maxRooms+1)):
            if lobby_nr==-1:
                tmp_room=Room(self.number,'lobby')
                lobby_nr=tmp_room.number
            elif corridor_nr==-1:
                tmp_room=Room(self.number,'corridor')
                corridor_nr=tmp_room.number
                Door(self.number,lobby_nr,corridor_nr)
            elif bathroom_nr==-1:
                tmp_room=Room(self.number,'bathroom')
                bathroom_nr=tmp_room.number
                Door(self.number,bathroom_nr,random.choice((corridor_nr,lobby_nr)))
            else:
                tmp_room=Room(self.number)
                Door(self.number,tmp_room.number,corridor_nr) 
        
    def room_gen_tmp(self):
        #### alte raumgen methode
        tmpCorridorNumber=-1
        tmpBathroomNumber=-1
        tmpLobbyNumber=-1
    
        for r in range(0,random.randint(minRooms,maxRooms+1)):
            tmpRoom=Room(self.number)
            if r == 0:
                tmpRoom.lobby=True
                tmpLobbyNumber=tmpRoom.number
            elif r == 1:
                tmpRoom.corridor=True
                tmpCorridorNumber=tmpRoom.number
                Door(self.number,tmpCorridorNumber,tmpLobbyNumber)
                #tmpRoom.doors.append(tmpCorridorNumber)
            elif r == 2:
                tmpBathroomNumber=tmpRoom.number
                tmpRoom.bathroom=True
                Door(self.number,tmpCorridorNumber,tmpBathroomNumber)
            else:
                Door(self.number,tmpCorridorNumber,tmpRoom.number)                


    def export(self):
        text='\nLevel: {}\n'.format(self.number)
        for r in world.World.rooms:

            if world.World.rooms[r].level == self.number:
                text+=world.World.rooms[r].export()
        text+='\n************+\n'
        return text

class Room(object):
    number=0
    roomTypes=['corridor','infirmary','office','waitingroom','bathroom','lobby']
    def __init__(self,level,roomtype=''):
        self.level=level
        self.number=Room.number
        Room.number+=1
        world.World.rooms[self.number]=self
        if roomtype=='':
            self.roomtype=random.choice(Room.roomTypes)
        else:
            self.roomtype=roomtype
            
        #self.lobby=False
        #self.bathroom=False
        #self.corridor=False
        #self.doors=[]

    def check_doors(self):
        doorlist=[]
        for d in world.World.doors:
            if world.World.doors[d].level == self.level:
                if self.number in world.World.doors[d].door_tupel:
                    doorlist.append(world.World.doors[d].number)        
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
        world.World.doors[self.number]=self
        self.locked=False
        self.forbidden=False
        self.door_tupel=(room1nr,room2nr)

    def export(self):
        text='\nDoornumber: {} \n'.format(self.number)
        text+='connecting: {} with {} \n'.format(self.door_tupel[0],self.door_tupel[1])
        return text
