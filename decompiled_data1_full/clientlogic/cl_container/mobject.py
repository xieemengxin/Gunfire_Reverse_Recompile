# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/mobject.pyc
# RelativePath: clientlogic/cl_container/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import SendAlert
import cl_seasonplay.net as seasonplaynet
import cl_drop
ATTR_GET = 0
FUNC_GET = 1
CONFUNC_GET = 2
QUERY_GET = 3

class CBaseSeasonContainer(object):
    m_SeasonNum = 0
    m_ItemAttr = { }
    
    def __init__(self, oWarrior):
        self.m_Owner = oWarrior.m_ID
        self.m_PlayerID = oWarrior.m_PlayerID
        self.m_Game = oWarrior.m_Game

    
    def GetOwner(self):
        if not self.m_Game:
            return None
        return self.m_Game.GetObject(self.m_Owner)

    
    def Load(self, dData):
        pass

    
    def Save(self):
        return { }

    
    def Release(self):
        pass

    
    def AllPerformDisable(self, iNotify = 0):
        pass

    
    def SelfRefresh(self):
        pass

    
    def Refresh(self, dPlayer):
        pass

    
    def NeedCreateSeed(self):
        return 1

    
    def GetItemByID(self, iItem):
        pass

    
    def GetPerform(self, iPerform, iItem = 0):
        pass

    
    def GetPlayers(self):
        return self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)

    
    def GS2CRefreshItemAttr(self, iItem, lstAttr):
        if not lstAttr:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oItem = self.GetItemByID(iItem)
        if not oItem:
            return None
        oItemCls = oItem.__class__
        oConCls = self.__class__
        dItemAttr = oItem.__dict__
        dItemClsAttr = oItemCls.__dict__
        dConClsAttr = oConCls.__dict__
        dAttrValue = { }
        dItemAttrGet = self.m_ItemAttr
        for sAttr in lstAttr:
            if sAttr not in dItemAttrGet:
                SendAlert('err', '%d %d refreshseasonitem notattr %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oItem, sAttr))
                continue
            iGetMode = dItemAttrGet[sAttr]
            if iGetMode == ATTR_GET:
                iValue = dItemAttr['m_%s' % sAttr]
            elif iGetMode == FUNC_GET:
                func = dItemClsAttr['Get%s' % sAttr]
                iValue = func(oItem)
            elif iGetMode == CONFUNC_GET:
                func = dConClsAttr['Get%s' % sAttr]
                iValue = func(self, iItem)
            elif iGetMode == QUERY_GET:
                iValue = oItem.QueryAttr(sAttr)
            dAttrValue[sAttr] = iValue
        
        lstPlayers = self.GetPlayers()
        seasonplaynet.GS2CRefreshSeasonItemAttr(oOwner, oItem, dAttrValue, lstPlayers)

    
    def AutoEquip(self):
        pass

    
    def AutoUnEquip(self):
        pass

    
    def OnRemoveItem(self, oItem, iDrop = 0):
        if not oItem:
            return None
        if not iDrop:
            oItem.Release()
        else:
            oOwner = self.GetOwner()
            if not oOwner:
                return None
            oItem.RemoveFromContainer()
            oItem.m_Source = oOwner.m_PlayerID
            cl_drop.DropItem(oOwner, oItem, bFly = True)


