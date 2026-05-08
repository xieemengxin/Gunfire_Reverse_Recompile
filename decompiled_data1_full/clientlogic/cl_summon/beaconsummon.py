# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/beaconsummon.pyc
# RelativePath: clientlogic/cl_summon/beaconsummon.pyc
# Source Generated with Decompyle++
# File: beaconsummon.pyc (Python 3.6)

from cl_only import Functor
import cl_msgcenter
from . import mobject

class CBeaconSummon(mobject.CBaseSummon):
    
    def OnInitAttr(self, clsData, dAddData):
        self.m_AttachTarget = dAddData['Victim']
        self.m_AttachPart = dAddData['AttachPart']
        self.m_MaxTriggerCnt = dAddData['MaxTriggerCnt']
        cl_msgcenter.AddAttentionFunc(self, dAddData['Victim'], cl_msgcenter.MSG_WAR_DIE, Functor(DieRemoveBeacon), 'VictimDie')
        cl_msgcenter.AddAttentionFunc(self, dAddData['Victim'], cl_msgcenter.MSG_WAR_REMOVEOBJ, Functor(DieRemoveBeacon), 'VictimDie')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, Functor(DieRemoveBeacon), 'LeaveScene')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_ACREMOVEWEAPON, Functor(OnRemoveWeapon), 'RemoveWeapon')

    
    def TriggerSummon(self, dTrigger):
        if not self.m_MaxTriggerCnt:
            return None
        iTriggerCnt = dTrigger['TriggerCnt']
        self.m_MaxTriggerCnt -= iTriggerCnt
        if self.m_MaxTriggerCnt <= 0:
            self.Remove('TriggerRemove')

    
    def Remove(self, sReason):
        cl_msgcenter.DoneAttention(self, self.m_AttachTarget, cl_msgcenter.MSG_WAR_DIE, 'VictimDie')
        cl_msgcenter.DoneAttention(self, self.m_AttachTarget, cl_msgcenter.MSG_WAR_REMOVEOBJ, 'VictimDie')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, 'LeaveScene')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_ACREMOVEWEAPON, 'RemoveWeapon')
        super(CBeaconSummon, self).Remove(sReason)



def DieRemoveBeacon(oSummon, oWarrior, dMsgInfo):
    oSummon.Remove('VictimDie')


def OnRemoveWeapon(oSummon, oWarrior, dMsgInfo):
    iWeapon = dMsgInfo['ItemID']
    if oSummon.m_SrcWeapon == iWeapon:
        oSummon.Remove('RemoveWeapon')

