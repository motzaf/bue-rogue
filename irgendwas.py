#!/usr/bin/python3
# a rogue-like game by Motz

#for i in range(10):
#    print('there are {} peas'.format(i))
    

textmenu = '''     Generic Menu
       (a) Menu A
       (b) Menu B
       (c) Menu C
       (d) Menu D
       (q) Quit
'''
print(textmenu)

while True:
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
        print('\n Menu C')
    elif eingabe[0] in 'dD':
        print('\n Menu D')
    else:
        print('\n Falsche Eingabe')
        
        

