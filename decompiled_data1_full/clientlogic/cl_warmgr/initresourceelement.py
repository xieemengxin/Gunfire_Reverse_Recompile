# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/initresourceelement.pyc
# RelativePath: clientlogic/cl_warmgr/initresourceelement.pyc
# Source Generated with Decompyle++
# File: initresourceelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
import cl_msgcenter

class CInitResourceElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CInitResourceElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_BulletData = self.m_Data.m_Config.get('INITBULLET', [])

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.InitPlayer, 'InitResource', -1, 0)

    
    def InitPlayer(self, oWarMgr, dInfo):
        iHero = dInfo['Hero']
        oHero = oWarMgr.m_Game.GetObject(iHero)
        for lstBullet in self.m_BulletData:
            (iBulletSID, iCnt) = lstBullet
            oHero.m_BulletCon.BulletModify(iBulletSID, iCnt, 'INITBULLET')
        

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'InitResource')
        self.m_WarMgr = None
        super(CInitResourceElement, self).Release()



def GetComponentClass(oMgrManager):
    return CInitResourceElement

