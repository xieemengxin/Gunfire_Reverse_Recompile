# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/newbieelement.pyc
# RelativePath: clientlogic/cl_warmgr/newbieelement.pyc
# Source Generated with Decompyle++
# File: newbieelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import FIGHT_KEY_WUDI
import cl_msgcenter

class CNewbieElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CNewbieElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_BulletData = self.m_Data.m_Config.get('INITBULLET', [])
        self.m_PerformData = self.m_Data.m_Config.get('INITPERFORM', [])

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.InitPlayer, 'NewbieInit', -1, 0)

    
    def InitPlayer(self, oWarMgr, dInfo):
        iHero = dInfo['Hero']
        oHero = oWarMgr.m_Game.GetObject(iHero)
        if self.m_BulletData:
            for lstBullet in self.m_BulletData:
                (iBulletSID, iCnt) = lstBullet
                oHero.m_BulletCon.BulletModify(iBulletSID, iCnt, 'NewbieElement')
            
        for iPerform in self.m_PerformData:
            oHero.AddPerform(iPerform, 1)
        

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'NewbieInit')
        self.m_WarMgr = None
        super(CNewbieElement, self).Release()



def GetComponentClass(oMgrManager):
    return CNewbieElement

