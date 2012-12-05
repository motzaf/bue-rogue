import mensch
#import random

def checkSympath(human1, human2):
    text='\n'
    text+=human1.getName()+'   vs   '+human2.getName()+'\n\n'
    apprWord=''
    human2ApprTrait=round(human1.trait1.intensity*human2.trait1.approvalForeign,1)
    if human2ApprTrait <= -.5:
        apprWord='hates'
    elif human2ApprTrait >= .5:
        apprWord='loves'
    else:
        apprWord='ignores'
    text+='intensity:     {}    {}\n'.format(round(human1.trait1.intensity,2), (round(human2.trait1.intensity,2)))
    text+='approval:      {}    {}\n'.format(round(human1.trait1.approvalForeign,2),(round(human2.trait1.approvalForeign,2)))
    text+='{} {} {}'.format(human2.getName(), apprWord, human1.getName())
    print(human2ApprTrait)
    #print(human1.trait1.approvalForeign+'  '+human2.trait1.approvalForeign)
    #print(human1.trait1.approvalSelf+'  '+human2.trait1.approvalSelf)
    return text

### interaktionen in zeit
#### z.b name rausgeben kurz, wegfragen, hinweisen, ausborgen

def battle(h1, h2, textSwitch=True):
    text=''
    #text+=h1.exportVerbose()
    word=''
    energy1=0.0

    for i in h1.traits:
        #text+='{} is {}'.format(h1.name,i)
        if i in h2.traits.keys():
            text+='### {} haben beide\n'.format(i[:-1])
            if h1.traits[i].approvalForeign < -0.5:
                word='hates'
            elif h1.traits[i].approvalForeign > 0.5:
                word='likes'
            else:
                word='ignores'
            text+='Approval: {} {} {} for being {} \n'.format(h1.name, word, h2.name, i)
            result=h1.traits[i].approvalForeign*h2.traits[i].intensity
            text+='Result: {} = appr {} * intens {}\n'.format(round(result,2),round(h1.traits[i].approvalForeign,2),round(h2.traits[i].intensity,2))
            text+='{} loses energy: {}\n'.format(h1.name,round(result,2))
            energy1+=result
        #if energy1 != 0.0:
            text+='* TotalEnergy: {}\n'.format(round(energy1,2))

        
    #    print(h1[i])
    text+='...............................'
    if textSwitch:
        return text
    else:
        return energy1

    
def main():
    ''' die sympathie zwischen zwei menschen und deren eigensympathie wird ausgetragen '''
    mensch.loadVariables()
    arena=mensch.Room()
    while True:
        print('--------------------------')
        h1=mensch.Creature()
        h2=mensch.Creature()
        #print(h1.export())
        #print(h2.export())
        print(battle(h1, h2))
        print(battle(h2, h1))
        x=input()
        if x == 'q':
            break
    
### wenn manuell ausgefuehrt wird main() funktion ausgefuehrt
### wenn als modul importiert, dann wird main() nicht ausgefuehrt
if __name__=='__main__':
    main()
