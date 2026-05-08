# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/realendlesselement.pyc
# RelativePath: clientlogic/cl_warmgr/realendlesselement.pyc
# Source Generated with Decompyle++
# File: realendlesselement.pyc (Python 3.6)

from .endlesselement import CBaseEndlessElement
from cl_commondefines import NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, DROP_REASON_NPCREWARD, ENDLESS_REAL, WARRIOR_BOSS, LEVEL_TYPE_BOSS
import cl_msgcenter

class CRealEndlessElement(CBaseEndlessElement):
    m_EndlessMode = ENDLESS_REAL
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'RealEndlessElement'
        self.m_BoseLevelRecord = { }
        self.m_GoldenCupConfig = oData.m_Config.get('GoldenCupConfig', { })
        self.m_FilterHideLevelType = oData.m_Config.get('FilterHideLevelType', { })

    
    def Save(self):
        dData = super().Save()
        dData['BLR'] = dict(self.m_BoseLevelRecord)
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        super().Load(dData)
        if 'BLR' in dData:
            self.m_BoseLevelRecord = dData['BLR']

    
    def AddAttention(self):
        super().AddAttention()
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, self.m_CallFlag)

    
    def DoneAttention(self):
        super().DoneAttention()
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_BEFORE_CHOOSEBOSSLEVEL, self.m_CallFlag)

    
    def OnLevelNodeInit(self, oEndlessElement, oWarMgr, dMsgInfo):
        if 'LevelType' not in dMsgInfo or dMsgInfo['LevelType'] != LEVEL_TYPE_BOSS:
            return None
        iLayer = dMsgInfo['Layer']
        self.m_BoseLevelRecord[iLayer] = dMsgInfo['LevelID']

    
    def OnCreateNpc(self, oEndlessElement, oLevelCtrl, dMsgInfo):
        super().OnCreateNpc(oEndlessElement, oLevelCtrl, dMsgInfo)
        if 'NPC' not in dMsgInfo or not (self.m_GoldenCupConfig):
            return None
        iNpc = dMsgInfo['NPC']
        clsNpcData = self.m_Game.m_WarData.GetNpcData(iNpc)
        if not clsNpcData or clsNpcData.m_FightType not in [
            NWARRIOR_NPC_GOLDENCUP,
            NWARRIOR_NPC_LIMITGOLDENCUP,
            NWARRIOR_NPC_EXCHANGEGOLDENCUP]:
            return None
        if 'PassLevel' in self.m_GoldenCupConfig and 'ExtInfo' in dMsgInfo and 'DropReason' in dMsgInfo['ExtInfo'] and dMsgInfo['ExtInfo']['DropReason'] == DROP_REASON_NPCREWARD:
            dMsgInfo['NPC'] = self.m_GoldenCupConfig['PassLevel']
        elif 'Boss' in self.m_GoldenCupConfig and 'Abandoner' in dMsgInfo:
            oAbandoner = self.m_Game.GetObject(dMsgInfo['Abandoner'])
            if oAbandoner and oAbandoner.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
                dMsgInfo['NPC'] = self.m_GoldenCupConfig['Boss']

    
    def StartEndless(self):
        super().StartEndless()
        self.FilterHideLevelByType()
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
        if self.m_BoseLevelRecord:
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_BEFORE_CHOOSEBOSSLEVEL, self.OnBeforeChooseBossLevel, self.m_CallFlag)

    
    def OnBeforeChooseBossLevel(self, oEndlessElement, oLevelCtrl, dMsgInfo):
        if 'FilterLevel' not in dMsgInfo:
            return None
        iBaseLayerNum = self.GetBaseLayer(oLevelCtrl.m_LayerNum)
        if iBaseLayerNum not in self.m_BoseLevelRecord:
            return None
        iLevel = self.m_BoseLevelRecord.pop(iBaseLayerNum)
        dMsgInfo['FilterLevel'][iLevel] = 1
        if not self.m_BoseLevelRecord:
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_BEFORE_CHOOSEBOSSLEVEL, self.m_CallFlag)

    
    def FilterHideLevelByType(self):
        if not self.m_FilterHideLevelType:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oLevelCtrl.m_FilterHideLevelType.update(self.m_FilterHideLevelType)



def GetComponentClass(oMgrManager):
    return CRealEndlessElement

