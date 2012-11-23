#!/usr/bin/python3
import random

##TODO Kommentar
### file to list als eigenes modul
### 
### winning condition??
### losing condition??
### time/turns

### (c)pickle for writing binarys to file


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
            

            

class Mensch(object):
        ''' der standard mitarbeiteter '''
        ### selfawareness per property
        ### instant (love/hate) first impression
        ### interaction between humans
        ### energylevel for opposing aggression
                
        nummer = 0 #Klassenattribut gehoert der gesamten Menschheit
        ## Listen als Klassenattribute (spart file-IO)        
        farben=[]
        vornamenf=[]
        vornamenm=[]
        nachnamen=[]
        
        def __init__(self,roomnumber=1):
            ''' konstruktoirorr oder so'''
            self.geschlecht=random.choice(['m','w'])
            self.haarfarbe=self.getColor()
            self.groesse=random.randint(150,210)
            self.gewicht=random.randint(50,150)
            Mensch.nummer+=1
            self.nummer=Mensch.nummer
            self.name=self.getName()
            self.roomnumber=roomnumber
                
        def getName(self):
            if self.geschlecht=='m':
                vn=random.choice(Mensch.vornamenm)
            else:
                vn=random.choice(Mensch.vornamenf)
            nn=random.choice(Mensch.nachnamen)
            return vn[:-1]+' '+nn[:-1]
                            
        def getColor(self):
            return random.choice(Mensch.farben)[:-1]
                
class Menschheit(object):
    menschen={}
    ## eine vergleichsmethode zweier zufaelliger menschen

#menschheit=[]

def main():

    ## reading files into lists
    ## may use 'for' in future
    
    file=open('color.txt')
    Mensch.farben=file.readlines()
    file.close()
    file=open('vorname.f.txt')
    Mensch.vornamenf=file.readlines()
    file.close()
    file=open('vorname.m.txt')
    Mensch.vornamenm=file.readlines()
    file.close()
    file=open('nachname.txt')
    Mensch.nachnamen=file.readlines()
    file.close()
    
    while True:
        menschling=Mensch()
        #print(menschling.nummer)
        Menschheit.menschen[menschling.nummer]=menschling
        #menschheit.append(menschling)

        print(menschling.__dict__)

        eingabe=input()
        if eingabe=="q":
            break

if __name__=='__main__':
    main()
