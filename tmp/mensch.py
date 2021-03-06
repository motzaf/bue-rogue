 #!/usr/bin/python3
import random

##TODO Kommentar
### file to list als eigenes modul
### 
### winning condition??
### losing condition??
### time/turns

### (c)pickle for writing binarys to file

### nummernautomat.. als npc

#schreibe eine methode der klasse raum, welche ueber alle generic items iteriert deren raumnummer chekct
#und wenn raummnummere matched die itemnummer in eine liste (attribut von raum) eintraegt
#mit dieser liste von itemnummern soll eine exportfunktion gemacht werden (text)

class World(object):
        items={}  ###key=itemnumber, value=instance
        creatures={}
        rooms={}
        traits={}
        quests={}
        quantityWords={0.0:'not a all',0.2:'a litte',0.4:'somewhat',0.6:'quite',0.8:'much'}
        

class Trait(object):
        ''' positve and negative attributes of Creatures '''
        number=0
        traitNameList=[]
        
        def __init__(self,name='nothing',randomTrigger=True):
                if name=='nothing':
                        self.name=random.choice((Trait.traitNameList))
                else:
                        self.name=name
                self.number=Trait.number
                Trait.number+=1
                World.traits[self.number]=self
                self.intensity=0.0          ### 0.0 to 1.0
                self.awarenessSelf=0.25     ### 0.0 to 1.0
                self.awarenessForeign=0.0   ### 0.0 to 1.0
                self.visabilty=0.1          ### 0.0 to 1.0  ##verstellfaktor (kosttet energie)
                self.approvalSelf=0.0       ### -1.0 to +1.0 for approval rate
                self.approvalForeign=0.0    ### -1.0 to +1.0 for approval rate
                if randomTrigger:
                        self.randomize()
                        
        def randomize(self):
                ''' randomize all attributes of Traits except number and names
                approval -1.0 to +1.0 all others 0.0 to 1.0'''

                for i in self.__dict__:
                        if i == 'name' or i == 'number':
                                continue
                        if i[0:8] == 'approval':
                                self.__dict__[i]=random.random()*2-1
                        else:
                                self.__dict__[i]=random.random()
                        
                              
                        #print(i, x.__dict__[i])

        def export(self):
                ''' a method for output '''
                text=''
                for i in self.__dict__:
                        text+='    {}: {}\n'.format(i,self.__dict__[i]) # the export is idented by 4 spaces

                return text
        
        def exportVerbose(self,sex):
                ## <he/she> is <quantity traitadj>, which <he/she> is <quantity selfawareness>
                ### which is <quantity visibility> for the world
                ### <he/she> <selfapproval quantity> and <foreignapproval quantity>
                ### <he/she> can detect <trait> in others with <quantity foreignawareness>
                text=''
                quant=self.intensity ##### is 0.35 oder so
                sortKeys=World.quantityWords.keys()
                
                for k in sorted(sortKeys,reverse=True):
                        #print(k,quant)
                        if k < quant:
                                break
                word=World.quantityWords[k]
                
                text+='{} is {} {}'.format(sex[1],word,self.name)
                
                return text
                        
                        
class Quest(object):
        ''' liek get formular or talk to somebody bout something'''
        number = 0
        def __init__(self):
                self.number=Quest.number
                Quest.number+=1
                World.quests[self.number]=self

class GenericItem(object):
        ''' generic item class '''
        number = 0
        
        def __init__(self,roomnumber=-1):
            self.number=GenericItem.number
            GenericItem.number+=1
            World.items[self.number]=self
            if roomnumber==-1:                
                    self.roomnumber=random.randomint(0,2) ###fixme
            else:
                    self.roomnumber=roomnumber   
            self.farbe=random.choice(['rot','blau','gruen'])
            self.eigen=random.choice(['gross','klein','stinkig'])
        def export(self):
            text=''
            text+='{} {}'.format(self.farbe,self.eigen)
            return text

class MovableItem(GenericItem):
        ''' movable Items like paperclip '''
        def __init__(self):
            GenericItem.__init__(self)
            
            self.typ=random.choice(['bierdeckl','bzeroklammer','telefon','schlissel'])
            #print(self.export())
        def export(self):
            text=''
            text+='{} {} {}'.format(self.farbe,self.eigen,self.typ)
            return text


            
class StaticItem(object):
        ''' unmovable objects '''

class Room(object):
        ''' Rooms contain Creatures, Furniture and Items '''
        number=0
        ## office
        ## bathroom (m/f/unisex)
        ## corridor
        ## lobby
        ## street
        ## public transport
        ## private car
        ## copy room
        ## cafeteria

        def __init__(self):
            ## first instance of Class Room has to be street (roomnumber 1)
            ## each level has at least one street, corridor, bathroom and elevator (for reaching next level)
            ## the other rooms will be randomized
            ## ppl spawn on street           
            self.number=Room.number
            Room.number+=1
            World.rooms[self.number]=self
            self.maxCapacity=4  #depends on roomtype
            ### self.quality= from -1 to 1
            for i in range(random.randint(1,5)):
                    GenericItem(self.number)
                    #self.itemList.append(self.genItems())            
            
        def checkItems(self):
            itemDict={}    
            for i in World.items: ## iteriert ueber keys
                if World.items[i].roomnumber==self.number:
                        itemDict[i]=World.items[i]
            return itemDict

        def export(self):
            ''' export room properties to text '''
            text='Roomnumber: {}\n Items:\n'.format(self.number)
            tmpDict=self.checkItems()
            for i in tmpDict:
                    text+='{}: {}\n'.format(i,tmpDict[i].export())
            return text
                

class Creature(object):
        ''' der standard mitarbeiteter '''
        ### selfawareness per property
        ### instant (love/hate) first impression
        ### interaction between humans
        ### energylevel for opposing aggression
                
        number = 0 #Klassenattribut gehoert der gesamten Menschheit
        ## Listen als Klassenattribute (spart file-IO)        
        colors=[]
        firstnamesF=[]
        firstnamesM=[]
        lastnames=[]
        
        def __init__(self,roomnumber=1):
            ''' konstruktoirorr oder so'''
            self.number=Creature.number
            Creature.number+=1
            World.creatures[self.number]=self
            self.sex=random.choice(['m','f'])
            self.age=random.randint(20,80)
            self.hairColor=self.getColor()
            #self.groesse=random.randint(150,210)
            #self.gewicht=random.randint(50,150)
            self.name=self.getName()
            self.roomnumber=roomnumber
            self.traits={}
            for i in range(3,7):
                    myTrait=Trait()
                    self.traits[myTrait.name]=myTrait
                    
            #self.trait1=Trait('Trait1')
            #self.trait2=Trait('Trait2')
            #self.trait3=Trait('Trait3')

        def export(self):
                text=''
                for i in self.__dict__:
                #        if i[0:5]=='trait':
                #                text+='{}:\n{}\n'.format(i,self.__dict__[i].export())
                #        else:
                #                text+='{}: {}\n'.format(i,self.__dict__[i])
                        if i!='traits':
                                text+='{}: {}\n'.format(i,self.__dict__[i])
                text += 'Traits: \n'             
                for i in self.traits:
                        text+=self.traits[i].export()
                        
                return text

        def exportVerbose(self):
            ### <name> is a <haicolor> haired, <age> year old <sex>
            text=''
            if self.sex=='m':
                    ######0######1####2######
                    sex=['man','he','him']
            else:
                    sex=['woman','she','her']

            text+='{} is a {} haired, {} year old {}\n'.format(self.getName(),self.hairColor,self.age,sex[0])

            for i in self.traits:
                    text+=self.traits[i].exportVerbose(sex)
            
            return text
                                    
        def getName(self):
            if self.sex=='m':
                vn=random.choice(Creature.firstnamesM)
            else:
                vn=random.choice(Creature.firstnamesF)
            nn=random.choice(Creature.lastnames)
            return vn[:-1]+' '+nn[:-1]
                            
        def getColor(self):
            return random.choice(Creature.colors)[:-1]
                
#class Menschheit(object):
#    menschen={}
    ## eine vergleichsmethode zweier zufaelliger menschen

#menschheit=[]

def loadVariables():
    ## reading files into lists
    ## may use 'for' in future
    file=open('color.txt')
    Creature.colors=file.readlines()
    file.close()
    file=open('vorname.f.txt')
    Creature.firstnamesF=file.readlines()
    file.close()
    file=open('vorname.m.txt')
    Creature.firstnamesM=file.readlines()
    file.close()
    file=open('nachname.txt')
    Creature.lastnames=file.readlines()
    file.close()
    file=open('traits.csv')
    Trait.traitNameList=file.readlines()
    file.close()
    Trait.traitNameList.pop(0)### killt ueberschrift
    return True

def main():
    loadVariables()
    while True:
        menschling=Creature()
        #print(menschling.nummer)
        #Menschheit.menschen[menschling.number]=menschling
        #menschheit.append(menschling)

        ###print(menschling.__dict__)
        ###menschen export bauen
        #print(menschling.export())
        print(menschling.exportVerbose())
        eingabe=input()
        if eingabe=="q":
            break

if __name__=='__main__':
    main()
