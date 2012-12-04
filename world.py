class World(object):
    ''' contains dictionary and lists containing instances '''
    creatures={}
    rooms={}
    items={}
    quests={}
    quantityWords={0.0:'not a all',0.2:'a litte',0.4:'somewhat',0.6:'quite',0.8:'much'}
    approvalWords={-0.7:'hates',0.0:'ignores',0.7:'loves'}
