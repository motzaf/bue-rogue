import mensch
#import random

def checkSympath(human1, human2):
    text='\n'
    text+=human1.getName()+'   vs   '+human2.getName()+'\n\n'
    text+='intensity:     {}    {}\n'.format(round(human1.trait1.intensity,2), (round(human2.trait1.intensity,2)))
    text+='approval:      {}    {}\n'.format(round(human1.trait1.approvalForeign,2),(round(human2.trait1.approvalForeign,2)))



    #print(human1.trait1.approvalForeign+'  '+human2.trait1.approvalForeign)
    #print(human1.trait1.approvalSelf+'  '+human2.trait1.approvalSelf)
    return text


    
def main():
    ''' die sympathie zwischen zwei menschen und deren eigensympathie wird ausgetragen '''
    mensch.loadVariables()
    arena=mensch.Room()
    while True:
        h1=mensch.Human()
        h2=mensch.Human()
        #print(h1.export())
        #print(h2.export())
        print(checkSympath(h1, h2))
        input()

    
    

### wenn manuell ausgefuehrt wird main() funktion ausgefuehrt
### wenn als modul importiert, dann wird main() nicht ausgefuehrt
if __name__=='__main__':
    main()
