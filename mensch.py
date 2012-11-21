#!/usr/bin/python3
import random

##TODO Kommentar
### file to list als eigenes modul
### 

class Mensch(object):
        ''' der standard mitarbeiteter '''
        nummer = 0 #Klassenattribut gehoert der gesamten Menschheit
        ## Listen als Klassenattribute (spart file-IO)        
        farben=[]
        vornamenf=[]
        vornamenm=[]
        nachnamen=[]
        
        def __init__(self):
            ''' konstruktoirorr oder so'''
            self.geschlecht=random.choice(['m','w'])
            self.haarfarbe=self.getColor()
            self.groesse=random.randint(150,210)
            self.gewicht=random.randint(50,150)
            Mensch.nummer+=1
            self.nummer=Mensch.nummer
            self.name=self.getName()
                
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
