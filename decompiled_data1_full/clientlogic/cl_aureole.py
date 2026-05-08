# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_aureole.pyc
# RelativePath: clientlogic/cl_aureole.pyc
# Source Generated with Decompyle++
# File: cl_aureole.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD
import cl_world
import cl_msgcenter

class CAureoleManager(cl_world.CEventObject):
    
    def __init__(self, oGame, nid):
        super(CAureoleManager, self).__init__(oGame, nid)
        self.m_MonsterAureole = { }
        self.m_MonsterAureoleOwner = { }

    
    def Release(self):
        oGame = self.m_Game
        cl_msgcenter.DoneAttention(self, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, 'MonsterAureole')
        super().Release()

    
    def OnCreateMonster(self, _oLinster, _oWarMgr, dMsgInfo):
        iMonster = dMsgInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            return None
        for iAureole in self.m_MonsterAureole.values():
            oMonster.AddPerform(iAureole, 1)
        

    
    def AddMonsterAureole(self, iOwner, sKey, iAureole, sSourceKey = ''):
        dAureoleOwner = self.m_MonsterAureoleOwner.setdefault(sKey, { })
        dOwnerKeyInfo = dAureoleOwner.setdefault(iOwner, { })
        dOwnerKeyInfo[sSourceKey] = 1
        if sKey in self.m_MonsterAureole:
            return None
        self.m_MonsterAureole[sKey] = iAureole
        oGame = self.m_Game
        for iMonster in oGame.m_SceneMgr.GetAllSceneObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            oMonster.AddPerform(iAureole, 1)
        
        if len(self.m_MonsterAureole) == 1:
            cl_msgcenter.AddAttentionFunc(self, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, 'MonsterAureole')

    
    def RemoveMonsterAureole(self, iOwner, sKey, sSourceKey = ''):
        if sKey not in self.m_MonsterAureole:
            return None
        if sKey not in self.m_MonsterAureoleOwner:
            return None
        dAureoleOwner = self.m_MonsterAureoleOwner[sKey]
        if iOwner not in dAureoleOwner:
            return None
        dOwnerKeyInfo = dAureoleOwner[iOwner]
        if sSourceKey not in dOwnerKeyInfo:
            return None
        dOwnerKeyInfo.pop(sSourceKey, 0)
        if not dOwnerKeyInfo:
            dAureoleOwner.pop(iOwner, { })
        if not dAureoleOwner:
            iAureole = self.m_MonsterAureole.pop(sKey)
            oGame = self.m_Game
            for iMonster in oGame.m_SceneMgr.GetAllSceneObjectsByType('Monster'):
                oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
                if not oMonster:
                    continue
                oMonster.RemovePerform(iAureole)
            
            if not self.m_MonsterAureole:
                cl_msgcenter.DoneAttention(self, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, 'MonsterAureole')

    
    def GetAureoleOwner(self, sKey):
        if sKey in self.m_MonsterAureoleOwner:
            return self.m_MonsterAureoleOwner[sKey]
        return []



def NewAureoleMgr(oGame):
    iID = oGame.NewNPCID()
    obj = CAureoleManager(oGame, iID)
    oGame.CreateObject(iID, obj)
    return obj

