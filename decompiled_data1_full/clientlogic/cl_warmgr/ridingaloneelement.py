# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/ridingaloneelement.pyc
# RelativePath: clientlogic/cl_warmgr/ridingaloneelement.pyc
# Source Generated with Decompyle++
# File: ridingaloneelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_object.logging import WarobjLog
from cl_commondefines import BENE_SOURCE_RIDINGALONE, RIDING_ALONE
import cl_msgcenter

class CRidingAloneElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_SpawnCnt = 1
        self.m_Bene = 0
        self.m_AttrAdjust = self.m_Data.m_Config.get('AttrAdjust', { })

    
    def IsValidData(self):
        if RIDING_ALONE not in self.m_WarMgr.m_ExtraInfo or not self.m_WarMgr.m_ExtraInfo[RIDING_ALONE]:
            return False
        dData = self.m_WarMgr.m_ExtraInfo[RIDING_ALONE]
        if 'SpawnCnt' not in dData or not dData['SpawnCnt']:
            return False
        if dData['SpawnCnt'] > 4 or dData['SpawnCnt'] < 2:
            return False
        if 'Bene' not in dData:
            return False
        return True

    
    def Init(self):
        if not self.IsValidData():
            WarobjLog.Alert(f'''{self.m_Game.m_ID} ridingalone data illegal {self.m_WarMgr.m_ExtraInfo}''')
            return None
        dData = self.m_WarMgr.m_ExtraInfo[RIDING_ALONE]
        self.m_SpawnCnt = dData['SpawnCnt']
        self.m_Bene = dData['Bene']
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, 'RidingAloneElement')

    
    def OnAddPlayer(self, oListener, oWarMgr, dMsgInfo):
        iHero = dMsgInfo['Hero']
        oHero = self.m_Game.GetObject(iHero)
        oHero.m_BenedictionCon.AddBenediction(self.m_Bene, 1, 'ridingalone', iSource = BENE_SOURCE_RIDINGALONE)

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'RidingAloneElement')
        self.m_WarMgr = None
        super().Release()



def GetComponentClass(oMgrManager):
    return CRidingAloneElement

