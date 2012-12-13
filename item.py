import random
import world

class Item(object):
    ###epic liste von eigenschaftsworten gewisse wschl. bez. eigenschaft
    adj=['org','ur','episch','leiwand','viech','voi','fett']
    nom=['bleistift','zeichenblock','kugelschreiber','bürogueklammer','tischlampe','blumentopf']
    number=0

    def __init__(self,roomnumber=-1):
        self.roomnumber=roomnumber
        self.number=Item.number
        Item.number+=1
        world.World.items[self.number]=self
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
        
