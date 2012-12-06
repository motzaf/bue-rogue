import world
import random

class Creature(object):
    ''' default creature '''
    number = 0
    
    def __init__(self, roomnumber=1):
        self.number=Creature.number
        Creature.number+=1
        world.World.creatures[self.number]=self    ##put instance in world dictionary    
    
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
        self.name=self.createName()        

    def createName(self):
        if self.sex=='m':
            fn=random.choice(world.World.firstnamesm)
        else:
            fn=random.choice(world.World.firstnamesf)
        ln=random.choice(world.World.lastnames)
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
