# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/__init__.pyc
# RelativePath: clientlogic/cl_container/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)


def GetPlayers(oGame, iWarrior):
    oWarrior = oGame.GetObject(iWarrior)
    if not oWarrior:
        return { }
    oScene = oGame.m_SceneMgr.GetScene(oWarrior.m_Scene)
    dScenePlayer = dict(oScene.GetPlayers()) if oScene else { }
    if iWarrior in oGame.GetRealPlayers():
        dScenePlayer[iWarrior] = 1
    return dScenePlayer


class CListContainer(object):
    m_BagType = 0
    m_CheckItemUpdate = False
    
    def __init__(self, iOwner):
        self.m_Owner = iOwner
        self.m_bUpdated = False
        self.m_Item = { }

    
    def Release(self):
        pass

    
    def GetType(self):
        return self.m_BagType

    
    def Update(self):
        self.m_bUpdated = True

    
    def ClearUpdate(self):
        for oItem in self.m_Item.values():
            oItem.ClearUpdate()
        
        self.m_bUpdated = False

    
    def Updated(self):
        if self.m_CheckItemUpdate:
            for oItem in self.m_Item.values():
                if not hasattr(oItem, 'm_bUpdated'):
                    self.m_CheckItemUpdate = False
                    break
                if oItem.Updated():
                    self.m_bUpdated = True
                    break
            
        return self.m_bUpdated

    
    def Load(self, dData):
        self.m_Item = { }
        if not dData:
            return None
        dItem = dData['Item']
        for iKey, dInfo in dItem.items():
            oItem = self.LoadItem(iKey, dInfo)
            if not oItem:
                continue
            self.LoadItemToList(oItem)
            self.OnItemLoad(oItem)
        

    
    def Save(self):
        dData = { }
        dItem = { }
        for iKey, oItem in self.m_Item.items():
            dInfo = oItem.Save()
            if dInfo:
                dItem[iKey] = dInfo
        
        dData['Item'] = dItem
        return dData

    
    def Keys(self):
        return list(self.m_Item.keys())

    
    def Values(self):
        return list(self.m_Item.values())

    
    def Items(self):
        return list(self.m_Item.items())

    
    def ItemList(self):
        return self.Values()

    
    def Size(self):
        return len(self.m_Item)

    
    def AddItem(self, oItem):
        self.LoadItemToList(oItem)
        oItem = self.OnAddItem(oItem)
        if oItem:
            self.GS2CItemAdd(oItem)
        return oItem

    
    def RemoveItem(self, iItem):
        if iItem in self.m_Item:
            oItem = self.m_Item.pop(iItem)
            self.GS2CItemDel(oItem)
            self.OnRemoveItem(oItem)

    
    def DelItem(self, iItem):
        if iItem in self.m_Item:
            oItem = self.m_Item.pop(iItem)
            self.OnRemoveItem(oItem)

    
    def GetItem(self, iItem):
        if iItem in self.m_Item:
            return self.m_Item[iItem]

    
    def Refresh(self, dPlayer = None):
        for oItem in self.m_Item.values():
            self.GS2CItemAdd(oItem, dPlayer)
        

    
    def LoadItemToList(self, oItem):
        self.m_Item[oItem.m_ID] = oItem

    
    def LoadItem(self, iKey, dData):
        pass

    
    def OnItemLoad(self, oItem):
        pass

    
    def GS2CItemAdd(self, oItem, dPlayer = None):
        pass

    
    def GS2CItemDel(self, oItem):
        pass

    
    def OnAddItem(self, oItem):
        pass

    
    def OnRemoveItem(self, oItem):
        pass


