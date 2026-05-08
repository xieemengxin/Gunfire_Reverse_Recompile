# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/teaminfoelement.pyc
# RelativePath: clientlogic/cl_warmgr/teaminfoelement.pyc
# Source Generated with Decompyle++
# File: teaminfoelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_container.keycon import CKeyContainer
import cl_msgcenter

class CTeamInfoElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CTeamInfoElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_KeyCon = CKeyContainer(oGame, self.m_ID)

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, OnPlayerReady, 'TeamInfoRefresh')

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'TeamInfoRefresh')
        self.m_WarMgr = None
        self.m_KeyCon.Release()
        self.m_KeyCon = None
        super(CTeamInfoElement, self).Release()

    
    def OnPlayerReady(self, oHero, dInfo):
        self.m_KeyCon.Refresh(oHero)

    
    def Refresh(self):
        self.m_KeyCon.Refresh()



def OnPlayerReady(oWarMgr, oTarget, dInfo):
    oTeamInfoElement = oWarMgr.GetComponent('TeamInfo')
    oTeamInfoElement.OnPlayerReady(oTarget, dInfo)


def GetComponentClass(oWarMgr):
    return CTeamInfoElement

