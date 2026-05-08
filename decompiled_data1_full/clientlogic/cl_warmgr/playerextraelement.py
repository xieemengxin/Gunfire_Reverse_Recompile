# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/playerextraelement.pyc
# RelativePath: clientlogic/cl_warmgr/playerextraelement.pyc
# Source Generated with Decompyle++
# File: playerextraelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
import cl_msgcenter

class CPlayerExtraElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'CPlayerExtraElement'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_ReleaseFlag = 0
        self.m_State = 0

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.AddPassive, sFlag)

    
    def AddPassive(self, *args):
        (oTarget, _oLifeCycle, dInfo) = args
        oCtrlHero = dInfo['oCtrlHero']
        iPassive = self.m_Data.m_Config['SpeedPassive']
        if not iPassive:
            return None
        oCtrlHero.m_Perform.AddPerform(oCtrlHero, iPassive, 1, iEnable = 1, iItem = 0)



def GetComponentClass(_oWarManager):
    return CPlayerExtraElement

