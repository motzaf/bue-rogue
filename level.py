import random
import world

class Level(object):
    number=0
    #self.rooms=[]
    #### other options ueber alle raeume iterieren und schaun welches level ihm gehoert
    def __init__(self,minRooms=3,maxRooms=9):
        self.number=Level.number
        Level.number+=1
        world.World.levels[self.number]=self
        tmpCorridorNumber=1
        tmpBathroomNumber=2
        
        for r in range(0,random.randint(minRooms,maxRooms+1)):
            tmpRoom=Room(self.number)
            if r == 0:
                tmpRoom.lobby=True
            if r != tmpCorridorNumber:
                tmpRoom.doors.append(tmpCorridorNumber)
            if r == tmpBathroomNumber:
                tmpRoom.bathroom=True

    def export(self):
        text='\nLevel: {}\n'.format(self.number)
        for r in world.World.rooms:

            if world.World.rooms[r].level == self.number:
                text+=world.World.rooms[r].export()
        text+='\n***********+\n'
        return text


    
class Room(object):
    number=0
    roomTypes=['lobby','corridor','infirmary','office','waitingroom']
    def __init__(self,level):
        self.level=level
        self.number=Room.number
        Room.number+=1
        world.World.rooms[self.number]=self
        self.roomtype=random.choice(Room.roomTypes)
        self.lobby=False
        self.bathroom=False
        self.doors=[]

    def export(self):
        text='\nRoomnumber: {} \n'.format(self.number)
        return text
    
    
