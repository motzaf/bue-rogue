#!/usr/bin/python3
# a rogue-like game by Motz

#for i in range(10):
#    print('there are {} peas'.format(i))

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

textmenu = '''
                Generic Menu
       (a) Menu Apply For a Job
       (b) Menu B
       (c) show Credits
       (o) Options
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
        #print('\n Menu C')
        print(credits())
    elif eingabe[0] in 'oO':
        playerName=options()
    else:
        print('\n Falsche Eingabe')
