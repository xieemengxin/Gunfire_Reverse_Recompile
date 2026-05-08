# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_servant/spare.pyc
# RelativePath: clientlogic/cl_servant/spare.pyc
# Source Generated with Decompyle++
# File: spare.pyc (Python 3.6)

from cl_commondefines import WARRIOR_MONSTER
from cl_betree.monsteragent import DamHateVal
from . import mobject
import cl_msgcenter

class CSpareServant(mobject.CServant):
    m_HateFactor = 1.5
    m_OwnerAttentionKey = 'SpareServant'
    
    def OwnerDieDist(self, _oServant, _oOwner, _dMsgInfo):
        pass

    
    def OwnerLeaveScene(self, _oServant, _oOwner, _dMsgInfo):
        pass

    
    def InitAttention(self):
        super().InitAttention()
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnOwnerDealTotalDam, self.m_OwnerAttentionKey)

    
    def ReleaseAttention(self):
        super().ReleaseAttention()
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_OwnerAttentionKey)

    
    def OnOwnerDealTotalDam(self, _oServant, _oOwner, dMsgInfo):
        if not self.m_Scene:
            return None
        if dMsgInfo['OriginAID'] == self.m_ID:
            return None
        iTarget = dMsgInfo['CurVID']
        oTarget = self.m_Game.GetObject(iTarget)
        if not oTarget or not (oTarget.m_Agent) or not (oTarget.m_FightType & WARRIOR_MONSTER):
            return None
        dFakeMsgInfo = {
            'AID': self.m_ID,
            'TotalDam': dMsgInfo['TotalDam'] }
        DamHateVal(oTarget, dFakeMsgInfo)


