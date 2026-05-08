# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/taskelement.pyc
# RelativePath: clientlogic/cl_warmgr/taskelement.pyc
# Source Generated with Decompyle++
# File: taskelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_warmgr.bigdataanalyse import CGreatTaskAnalyseCom
from cl_commondefines import NWARRIOR_NPC_TASKNPC
import cl_msgcenter

class CTaskElement(CBaseElement):
    m_CallFlag = 'TaskElement'
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'WarMgr.TaskElement'
        self.m_MaxRunningTask = oData.m_Config.get('MaxRunningTask', 0)
        self.m_MaxTeamRunningTaskCnt = oData.m_Config.get('MaxTeamRunningTaskCnt', ())
        self.m_TaskNum = 0

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateNpc, self.m_CallFlag)

    
    def Save(self):
        dData = { }
        dData['TN'] = self.m_TaskNum
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_TaskNum = dData['TN']

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_CallFlag)
        super().Release()
        self.m_Game = None

    
    def InitAfter(self):
        oBigdataMgr = self.m_Game.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CGreatTaskAnalyseCom(self.m_Game)
            oBigdataMgr.SetCom('GreatTask', oAnalyseCom)

    
    def GetTeamExcludeTask(self):
        if not self.m_MaxTeamRunningTaskCnt:
            return { }
        dTeamExcludeTask = { }
        lstHero = []
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                lstHero.append(oHero)
        
        for tSID, iMaxCnt in self.m_MaxTeamRunningTaskCnt:
            iCnt = 0
            for oHero in lstHero:
                iCnt += oHero.m_TaskCon.GetRunningTaskCntBySID(tSID)
            
            if iCnt >= iMaxCnt:
                for iSID in tSID:
                    dTeamExcludeTask[iSID] = 1
                
        
        return dTeamExcludeTask

    
    def OnCreateNpc(self, _oLinstener, oNpc, dMsgInfo):
        if oNpc.m_FightType == NWARRIOR_NPC_TASKNPC:
            self.m_TaskNum += 1



def GetComponentClass(oWarManager):
    return CTaskElement

