#!/usr/bin/python3
# a rogue-like game by Motz

#for i in range(10):
#    print('there are {} peas'.format(i))

import os

def credits():
   ''' show the credits '''
   text='''Mehrzeiliger Credittext
Viele Leute:
Alles Spender!
'''
   return text

def options():
   ''' options for your game '''
   name=input('\n Enter Your Name: ')
   return name

def saveOption(saveName='deadmeat'):
   ''' save Options to a file '''
   filename=saveName+'.txt'

   f=open(filename,'w')
   f.write(saveName)
   f.close()

def loadOption():
   ''' load Options (Player Name) from a file '''
   f=open('save.txt')
   o=''

   while True:
      line=f.readline()
      if len(line) == 0:
         break
      else:
         o=line
   f.close()
   return o

def listFiles():
   '''  '''
   myFiles=[]
   for p,dirs,files in os.walk(os.path.abspath('.')):
      for f in files:
         if f[-4:] == '.txt':
            myFiles.append(f)
      break
   return myFiles



def genLoadMenu():
   ''' generates the Load Menu '''
   fileList=listFiles()
   loadMenu=''
   menuItems=''
   #print(fileList)
   loadMenu += '\n           Select Savegame\n\n'

   for i in fileList:
      loadMenu += '       ('+chr(97+fileList.index(i))+') '+i[:-4]+'\n'
      menuItems += chr(97+fileList.index(i))

   loadMenu +='       (q) Back to Main'

   while True:
      print(loadMenu)
      eingabe=input('\nEingabe: ')
      if eingabe == '':
        continue
      if eingabe[0] in 'qQ':
        return ''
      elif eingabe[0].lower() in menuItems:
        return fileList[ord(eingabe[0].lower())-97]

        #playerName=fileList[ord(eingabe[0].lower())-97][:-4]
        #break


textmenu = '''
                Generic Menu
       (a) Menu Apply For a Job
       (b) Menu B
       (c) show Credits
       (f) show SaveFiles
       (o) Options
       (s) Save
       (l) Load
       (q) Quit
'''

playerName=''

while True:
    if playerName:
        print('\n                Welcome {}'.format(playerName))
    print(textmenu)    
    eingabe=input('\nEingabe: ')
    if eingabe == '':
        continue
    if eingabe[0] in 'qQ':
        break
    elif eingabe[0] in 'aA':
        print('\n Menu A')
    elif eingabe[0] in 'bB':
        print('\n Menu B')
    elif eingabe[0] in 'cC':
        print(credits())
    elif eingabe[0] in 'fF':
        listFiles()
    elif eingabe[0] in 'sS':
        saveOption(playerName)
    elif eingabe[0] in 'lL':
        saveFile=genLoadMenu()
        #playerName=loadOption()
    elif eingabe[0] in 'oO':
        playerName=options()
    else:
        print('\n Falsche Eingabe')


#Dateioperationen
#
#for p,dirs,files in os.walk(os.path.abspath('.')):
#	for f in files:
#		print(f)
#	break
#
