import os

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
    filenames=['colornames.txt','firstnamesf.txt','firstnamesm.txt','lastnames.txt','traitnames.csv']
    
    def loadFiles(self,filenames=[]):
        lines=[]
        for f in filenames:
            fo=open(os.path.join('data',f))
            lines=fo.readlines()
            fo.close()

            if f[:-4] in World.__dict__.keys():
                print(f)
                World.__dict__[f[:-4]].extend(lines)
               
        #file=open('color.txt')
        #self.colors=file.readlines()
        #file.close()

    #self.loadFiles()
