class World(object):
    ''' contains dictionary and lists containing instances '''

    #Dictionaries
    creatures={}
    rooms={}
    items={}
    quests={}
    quantityWords={0.0:'not a all',0.2:'a litte',0.4:'somewhat',0.6:'quite',0.8:'much'}
    approvalWords={-0.7:'hates',0.0:'ignores',0.7:'loves'}

    #Lists
    colornames=[]
    firstnamesf=[]
    firstnamesm=[]
    lastnames=[]
    traitnames=[]


    #Filelist
    files=['data/colornames.txt','data/firstnamesf.txt','data/firstnamesm.txt','data/lastnames.txt','data/traitnames.csv']


    
    def loadFiles(self,files=[]):
        for file in files:
            print(file)

        #file=open('color.txt')
        #self.colors=file.readlines()
        #file.close()

    #self.loadFiles()

