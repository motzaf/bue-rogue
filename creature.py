import world
import random

class Creature(object):
    ''' default creature '''
    number = 0
    
    def __init__(self, roomnumber=1):
        self.__creatureCounter__()
        self.sex=random.choice(['m','f'])

    def __creatureCounter__(self):
        self.number=Creature.number
        Creature.number+=1
        world.World.creatures[self.number]=self    ##put instance in world dictionary    
    
class Human(Creature):
    ''' humanoid '''

    def __init__(self):
        Creature.__init__(self)
        self.name='text'
