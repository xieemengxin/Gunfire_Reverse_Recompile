# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/explorelevelctrl.pyc
# RelativePath: clientlogic/cl_warmgr/explorelevelctrl.pyc
# Source Generated with Decompyle++
# File: explorelevelctrl.pyc (Python 3.6)

from cl_cscommondef.cs_fight import LEVEL_TYPE_FIGHT, LEVEL_DIFF_NORMAL, GAMETYPE_DESTROY
from cl_cscommondef import PLAYMODE_MOBILE_DEMO
import cl_msgcenter
from . import levelctrl

class CExploreLevelCtrlElement(levelctrl.CLevelCtrlElement):
    
    def __init__(self, oGame, nid, oData):
        super(CExploreLevelCtrlElement, self).__init__(oGame, nid, oData)
        self.m_LevelNum = 1
        self.m_CurLType = LEVEL_TYPE_FIGHT
        self.m_CurTType = GAMETYPE_DESTROY
        self.m_DemoFirstLevel = 1

    
    def InitLevelNode(self):
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, 'LevelCtrlPlayerLogin', -1)
        dLayerData = self.m_LevelCtrlConf[self.m_LayerNum]
        iLevelID = dLayerData['CtrlInfo'][self.m_LevelNum]['NormalStore'][0]
        self.CreateMainLevel(iLevelID, self.m_LayerNum, self.m_LevelNum, self.m_CurLType, self.m_CurTType, True)

    
    def GetTransferInfo(self, iNowLevelDiff = LEVEL_DIFF_NORMAL):
        if self.m_DemoFirstLevel:
            return { }
        return super().GetTransferInfo(iNowLevelDiff)

    
    def Save(self):
        return { }

    
    def Load(self, dData):
        pass

    
    def NextLevel(self, dTransfer):
        if self.m_Game.m_WarMgr.m_PlayMode != PLAYMODE_MOBILE_DEMO:
            return None
        dTransfer = super().GetTransferInfo()
        dTransfer = list(dTransfer.values())[0]
        super().NextLevel(dTransfer)



def GetComponentClass(oMgrManager):
    return CExploreLevelCtrlElement

