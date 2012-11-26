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

class Trait(object):
        ''' positve and negative attributes of Humans '''
        number=0
        def __init__(self,name='TraitX',randomTrigger=True):
                self.name=name
                Trait.number+=1
                self.number=Trait.number
                self.intensity=0.0          ### 0.0 to 1.0
                self.awarenessSelf=0.25     ### 0.0 to 1.0
                self.awarenessForeign=0.0   ### 0.0 to 1.0
                self.visabilty=0.1          ### 0.0 to 1.0
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
                        
                        
                

class Quest(object):
        ''' liek get formular or talk to somebody bout something'''

class Items(object):
        ''' movable Items like paperclip '''

class Furniture(object):
        ''' unmovable objects '''

class Room(object):
        ''' Rooms contain Humans, Furniture and Items '''
        number = 0
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
            
            Room.number+=1
            self.number=Room.number
            self.maxCapacity=4  #depends on roomtype
            ### self.quality= from -1 to 1
            

            

class Human(object):
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
            self.sex=random.choice(['m','w'])
            self.hairColor=self.getColor()
            #self.groesse=random.randint(150,210)
            #self.gewicht=random.randint(50,150)
            Human.number+=1
            self.number=Human.number
            self.name=self.getName()
            self.roomnumber=roomnumber
            self.trait1=Trait('Trait1')
            self.trait2=Trait('Trait2')
            self.trait3=Trait('Trait3')

        def export(self):
                text=''
                for i in self.__dict__:
                        text+='{}: {}\n'.format(i,self.__dict__[i])
                        if i[0:5]=='trait':
                                text+='{}: {}\n'.format(i,self.__dict__[i].export())
                return text


                        
            
        def getName(self):
            if self.sex=='m':
                vn=random.choice(Human.firstnamesM)
            else:
                vn=random.choice(Human.firstnamesF)
            nn=random.choice(Human.lastnames)
            return vn[:-1]+' '+nn[:-1]
                            
        def getColor(self):
            return random.choice(Human.colors)[:-1]
                
class Menschheit(object):
    menschen={}
    ## eine vergleichsmethode zweier zufaelliger menschen

#menschheit=[]

def main():

    ## reading files into lists
    ## may use 'for' in future
    
    file=open('color.txt')
    Human.colors=file.readlines()
    file.close()
    file=open('vorname.f.txt')
    Human.firstnamesF=file.readlines()
    file.close()
    file=open('vorname.m.txt')
    Human.firstnamesM=file.readlines()
    file.close()
    file=open('nachname.txt')
    Human.lastnames=file.readlines()
    file.close()
    
    while True:
        menschling=Human()
        #print(menschling.nummer)
        #Menschheit.menschen[menschling.number]=menschling
        #menschheit.append(menschling)

        ###print(menschling.__dict__)
        ###menschen export bauen
        print(menschling.export())




        eingabe=input()
        if eingabe=="q":
            break

if __name__=='__main__':
    main()
