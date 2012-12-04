import world

class Creature(object):
    ''' default creature '''
    number = 0
    
    def __init__(self, roomnumber=1):
        self.creatureCounter()

    def creatureCounter(self):
        self.number=Creature.number
        Creature.number+=1
        world.World.creatures[self.number]=self    ##put instance in world dictionary    
    
class Human(Creature):
    ''' humanoid '''

    def __init__(self):
        self.creatureCounter()
        self.name='text'
