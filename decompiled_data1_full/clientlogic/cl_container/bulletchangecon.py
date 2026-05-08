# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/bulletchangecon.pyc
# RelativePath: clientlogic/cl_container/bulletchangecon.pyc
# Source Generated with Decompyle++
# File: bulletchangecon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_BULLETCHANGE
import weakref

class CBulletChangeContainer(object):
    m_BagType = BAG_TYPE_BULLETCHANGE
    
    def __init__(self, oWarrior):
        self.m_Owner = oWarrior.m_ID
        self.m_PlayerID = oWarrior.m_PlayerID
        self.m_Game = oWarrior.m_Game
        self.m_Perform = { }
        self.m_Pfid2Key = { }

    
    def SetOwner(self, oOwner):
        if oOwner:
            self.m_Owner = oOwner.m_ID
            self.m_PlayerID = oOwner.m_PlayerID
        else:
            self.m_Owner = 0
            self.m_PlayerID = 0

    
    def GetOwnerID(self):
        return self.m_Owner

    
    def AddPerform(self, oOwner, iOwnPfid, iPerform, iLevel, iEnable, iItem):
        tKey = (iOwnPfid, iPerform)
        if tKey in self.m_Perform:
            oPerform = self.m_Perform[tKey]
            if oPerform.m_Owner == oOwner.m_ID:
                oPerform.SetLevel(oOwner, iLevel)
                if iEnable and not (oPerform.m_Enable):
                    oPerform.Enable(oOwner)
                return oPerform
        oPerform = oOwner.m_Game.m_ResMgr.NewPerform(iPerform, oOwner, iLevel)
        if not oPerform:
            return None
        self.m_Perform[tKey] = oPerform
        self.m_Pfid2Key[oPerform.m_ID] = tKey
        oPerform.m_Container = weakref.proxy(self)
        oPerform.m_Item = iItem
        oPerform.SetOwnPerfom(iOwnPfid)
        if iEnable:
            oPerform.Enable(oOwner)
        return oPerform

    
    def RemovePerform(self, oOwner, iOwnPfid, iPerform):
        tKey = (iOwnPfid, iPerform)
        if tKey not in self.m_Perform:
            return None
        oPerform = self.m_Perform[tKey]
        oPerform.Disable(oOwner)
        oPerform.m_Container = None
        oPerform.Release()
        self.m_Perform.pop(tKey)

    
    def GetPerform(self, iOwnPfid, iPerform):
        tKey = (iOwnPfid, iPerform)
        if tKey not in self.m_Perform:
            return None
        return self.m_Perform[tKey]

    
    def GetPerformByID(self, iPerformID):
        if iPerformID not in self.m_Pfid2Key:
            return None
        key = self.m_Pfid2Key[iPerformID]
        if key not in self.m_Perform:
            return None
        return self.m_Perform[key]

    
    def AllPerformEnable(self):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        for oPerform in self.m_Perform.values():
            oPerform.Enable(oOwner)
        

    
    def AllPerformDisable(self, iNotify = 0):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        for oPerform in list(self.m_Perform.values()):
            oPerform.Disable(oOwner, iNotify)
        

    
    def GetAllPerform(self):
        return self.m_Perform.values()

    
    def GetAllPerformLevel(self):
        dLevel = { }
        for oPerform in self.m_Perform.values():
            dLevel[oPerform.m_SID] = oPerform.Level()
        
        return dLevel

    
    def Release(self):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        if oOwner and oOwner.m_ReleaseFlag:
            oOwner = None
        for oPerform in self.m_Perform.values():
            if oOwner:
                oPerform.Disable(oOwner)
            oPerform.m_Container = None
            oPerform.Release()
        
        self.m_Pfid2Key = { }
        self.m_Perform = { }
        self.m_Game = None

    
    def Save(self):
        dData = { }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None

    
    def Refresh(self, dPlayer = None):
        for oPerform in self.m_Perform.values():
            oPerform.Refresh()
        

    
    def TriggerBulletChange(self, oSkill, dData):
        for iPerfom, dMethod in dData.items():
            if iPerfom not in self.m_Pfid2Key:
                continue
            key = self.m_Pfid2Key[iPerfom]
            if key not in self.m_Perform:
                continue
            oPerform = self.m_Perform[key]
            oPerform.TriggerRule(oSkill, dMethod)
        


