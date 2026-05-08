# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/inkwallsummon.pyc
# RelativePath: clientlogic/cl_summon/inkwallsummon.pyc
# Source Generated with Decompyle++
# File: inkwallsummon.pyc (Python 3.6)

from cl_commondefines import SIDE_TYPE_HERO, WARRIOR_INKWALL, FIGHT_KEY_WUDI
from cl_resmgr.resdata import CSummonData
import cl_msgcenter
from . import mobject

class CInkWallSummon(mobject.CBaseSummon):
    m_Side = SIDE_TYPE_HERO
    m_FightType = WARRIOR_INKWALL
    m_ValidShowTips = 0
    
    def OnInitAttr(self, clsData, dAddData):
        self.m_Shape = dAddData['ObjShape']
        self.m_ClientOwner = dAddData['ClientOwner']
        self.AddBitAttr('SpecialKey', 'InkWallSummon', FIGHT_KEY_WUDI)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_RECEIVEDAMED, OnReceiveDam, 'InkWallReceiveDam')

    
    def Remove(self, sReason):
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_RECEIVEDAMED, 'InkWallReceiveDam')
        super().Remove(sReason)

    
    def OnContact(self, iTarget, dArgs):
        pass

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)



class CInkWallSummonData(CSummonData):
    m_SID = 1001
    m_Side = SIDE_TYPE_HERO
    m_Name = '墨墻召唤物'
    m_Shape = 0
    m_FightType = WARRIOR_INKWALL


def OnReceiveDam(oSummon, dMsgInfo):
    oOwner = oSummon.GetOwner()
    dInfo = { }
    if 'Skill' in dMsgInfo:
        dInfo['Skill'] = dMsgInfo['Skill']
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INKWALL_BLOCK, oOwner, dInfo)

