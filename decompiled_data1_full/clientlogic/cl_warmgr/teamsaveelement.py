# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/teamsaveelement.pyc
# RelativePath: clientlogic/cl_warmgr/teamsaveelement.pyc
# Source Generated with Decompyle++
# File: teamsaveelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from .saveelement import CBasePlayerSave
from cl_commondefines import LEVEL_TYPE_FIGHT
from cl_object.logging import FightserverLog
import cl_msgcenter
import cli_player
import cllib.lib_flag as lib_flag

class TeamPlayerSave(CBasePlayerSave):
    
    def __init__(self, oGame, pid, *args):
        super().__init__(oGame, pid, args)
        self.m_PlayerID = pid

    
    def ValidSaveLoad(self):
        return 1

    
    def SaveCurRecord(self, dInfo):
        self.SaveHeroInfo()
        self.SaveLevelInfo(dInfo)
        self.SaveWarReport()
        self.SaveWarMgrInfo()

    
    def SaveLevelInfo(self, dInfo):
        if 'Transfer' not in dInfo:
            return None
        dLevel = { }
        dLevel.update(dInfo['Transfer'])
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        dLevel.update(oLevelCtrl.Save())
        self.m_Data['Level'] = dLevel



class CTeamSaveElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_PlayerData = { }
        self.m_TeamLoaded = 0

    
    def Init(self):
        if not lib_flag.g_IsStandaloneClient:
            return None
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, OnAddPlayer, 'TeamRecord')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, OnRemovePlayer, 'TeamRecord')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, OnLevelNodeFinish, 'TeamRecord')

    
    def Release(self):
        if lib_flag.g_IsStandaloneClient:
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'TeamRecord')
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, 'TeamRecord')
            self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'TeamRecord')
        self.m_WarMgr = None
        for oSave in self.m_PlayerData.values():
            oSave.Release()
        
        self.m_PlayerData = { }
        super().Release()

    
    def ValidLoad(self):
        if not self.m_WarMgr.IsTransferGame():
            return 0
        return 1

    
    def ValidSave(self):
        if self.m_WarMgr.IsSingleGame():
            return 0
        return 1

    
    def AddPlayer(self, pid, dData):
        self.m_PlayerData[pid] = TeamPlayerSave(self.m_Game, pid)
        self.Load(pid, dData)
        who = cli_player.GetPlayer(pid)
        if who and who.m_WarMaster:
            self.RemovePlayer(pid)

    
    def Load(self, pid, dData):
        if not dData:
            return False
        if dData['WarNo'] != self.m_WarMgr.m_SID:
            return False
        if dData['Round'] != self.m_WarMgr.m_Round:
            return False
        if not self.ValidLoad():
            FightserverLog.Alert('%s %s invalidload' % (self.m_Game.m_ID, pid))
            return False
        if self.m_TeamLoaded == 0:
            self.m_TeamLoaded = 1
            iLoaded = 0
        else:
            iLoaded = 1
        self.m_PlayerData[pid].Load(dData, iLoaded)
        return True

    
    def Save(self, pid):
        if pid not in self.m_PlayerData:
            return { }
        dRecord = self.m_PlayerData[pid].Save()
        if not dRecord:
            return { }
        oWarMgr = self.m_WarMgr
        oHero = oWarMgr.GetHeroByPlayer(pid)
        dRecord['FightIndex'] = oHero.Query('FightIndex')
        dRecord['Round'] = oWarMgr.m_Round
        dRecord['WarNo'] = oWarMgr.m_SID
        dRecord['Cycle'] = oWarMgr.m_Cycle
        dRecord['MaxLayer'] = oWarMgr.m_MaxLayer
        return dRecord

    
    def SaveCurRecord(self, dInfo):
        for oSave in self.m_PlayerData.values():
            oSave.SaveCurRecord(dInfo)
        

    
    def RemovePlayer(self, pid):
        if self.m_WarMgr.GetComponent('TeammateAI'):
            return None
        if pid in self.m_PlayerData:
            oSave = self.m_PlayerData.pop(pid)
            oSave.Release()



def OnAddPlayer(oWarMgr, oTarget, dInfo):
    pid = dInfo['pid']
    oSaveElement = oWarMgr.GetComponent('TeamSaveElement')
    oSaveElement.AddPlayer(pid, dInfo['CreateInfo'].get('TransferRecord', { }))


def OnRemovePlayer(oWarMgr, oTarget, dInfo):
    pid = dInfo['pid']
    oSaveElement = oWarMgr.GetComponent('TeamSaveElement')
    oSaveElement.RemovePlayer(pid)


def OnLevelNodeFinish(oWarMgr, oTarget, dInfo):
    if not dInfo.get('Transfer', { }):
        return None
    iPassAll = dInfo.get('PassAll', 0)
    if not iPassAll:
        oSaveElement = oWarMgr.GetComponent('TeamSaveElement')
        if oSaveElement.ValidSave():
            oSaveElement.SaveCurRecord(dInfo)


class CSurvivorTeamSaveElement(CTeamSaveElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_LoadFlag = True
        self.m_SurvivorData = { }

    
    def ValidSave(self):
        if self.m_WarMgr.IsSingleGame():
            return 0
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_CurNode.m_LevelType != LEVEL_TYPE_FIGHT:
            return 0
        return 1

    
    def SaveCurRecord(self, dInfo):
        super().SaveCurRecord(dInfo)
        self.SaveSurvivorData()

    
    def Save(self, pid):
        dRecord = { }
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if self.ValidSave():
            dInfo = { }
            dInfo['Transfer'] = {
                'LevelID': oLevelCtrl.m_CurNode.m_Level,
                'LayerNum': oLevelCtrl.m_LayerNum,
                'LevelNum': oLevelCtrl.m_LevelNum }
            self.SaveCurRecord(dInfo)
        dRecord['Survivor'] = self.m_SurvivorData
        dRecord.update(super().Save(pid))
        return dRecord

    
    def Load(self, pid, dData):
        if not super().Load(pid, dData):
            return False
        if 'Hero' in dData and 'GSCH' in dData['Hero']:
            oHero = self.m_WarMgr.GetHeroByPlayer(pid)
            oHero.m_WarGSCash = dData['Hero']['GSCH']
        if 'Survivor' in dData and self.m_LoadFlag:
            self.m_LoadFlag = False
            self.m_SurvivorData = dData['Survivor']
            self.LoadSurvivorInfo(dData)
        self.LoadUpgrade(pid, dData)
        return True

    
    def SaveSurvivorData(self):
        oSurvivorElement = self.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return None
        dSurvivorData = oSurvivorElement.Save()
        dUpgradeMgr = { }
        for pid in self.m_PlayerData:
            oHero = self.m_WarMgr.GetHeroByPlayer(pid)
            dData = oSurvivorElement.m_UpgradeMgr.Save(oHero.m_ID)
            dUpgradeMgr[pid] = dData
        
        dSurvivorData['UP'] = dUpgradeMgr
        self.m_SurvivorData = dSurvivorData

    
    def LoadSurvivorInfo(self, dData):
        oSurvivorElement = self.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return None
        oSurvivorElement.Load(dData['Survivor'])

    
    def LoadUpgrade(self, pid, dData):
        oSurvivorElement = self.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return None
        if 'Survivor' not in dData:
            return None
        dSurvivor = dData['Survivor']
        if 'UP' not in dSurvivor:
            return None
        if pid not in dSurvivor['UP']:
            return None
        oHero = self.m_WarMgr.GetHeroByPlayer(pid)
        oSurvivorElement.m_UpgradeMgr.Load(oHero.m_ID, dSurvivor['UP'][pid])



def GetComponentClass(oWarMgr):
    if 'SurvivorElement' in oWarMgr.m_ComponentCls:
        return CSurvivorTeamSaveElement
    return CTeamSaveElement

