# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/testlevelctrl.pyc
# RelativePath: clientlogic/cl_warmgr/testlevelctrl.pyc
# Source Generated with Decompyle++
# File: testlevelctrl.pyc (Python 3.6)

from cl_cscommondef.cs_fight import LEVEL_TYPE_FIGHT, LEVEL_DIFF_NORMAL, GAMETYPE_DESTROY
from cl_cscommondef import DEBUG_STATUS_NODIE
import cl_msgcenter
from . import levelctrl

class CTestLevelCtrlElement(levelctrl.CLevelCtrlElement):
    
    def __init__(self, oGame, nid, oData):
        super(CTestLevelCtrlElement, self).__init__(oGame, nid, oData)
        self.m_LevelNum = 1
        self.m_CurLType = LEVEL_TYPE_FIGHT
        self.m_CurTType = GAMETYPE_DESTROY
        self.m_NextTransferInfo = { }

    
    def InitLevelNode(self):
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, 'LevelCtrlPlayerLogin', -1)
        dLayerData = self.m_LevelCtrlConf[self.m_LayerNum]
        iLevelID = dLayerData['CtrlInfo'][self.m_LevelNum]['NormalStore'][0]
        self.CreateMainLevel(iLevelID, self.m_LayerNum, self.m_LevelNum, self.m_CurLType, self.m_CurTType, True)
        for iHero in self.m_Game.m_WarMgr.GetAllHero():
            oHero = self.m_Game.GetObject(iHero)
            iStatus = oHero.Query('DebugStatus', 0)
            oHero.Set('DebugStatus', iStatus | DEBUG_STATUS_NODIE)
            oHero.GS2CPropChange('DebugStatus')
        

    
    def Save(self):
        return { }

    
    def Load(self, dData):
        pass

    
    def SetTransferInfo(self, dTransfer):
        self.m_NextTransferInfo = dTransfer

    
    def GetTransferInfo(self, iNowLevelDiff = LEVEL_DIFF_NORMAL):
        return self.m_NextTransferInfo

    
    def GetMaxLevel(self):
        return 1

    
    def CheckFinishWar(self):
        return False



def GetComponentClass(oMgrManager):
    return CTestLevelCtrlElement

