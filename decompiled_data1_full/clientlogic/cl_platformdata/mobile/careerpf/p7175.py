# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p7175.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p7175.pyc
# Source Generated with Decompyle++
# File: p7175.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import TYPE_RELIFE_PF

def Action(skill):
    pass


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 7175
    m_Name = '#NT#迭代小玖机甲自爆'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 6,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 30000,
        'CrazyEff': 0,
        'BulletSpeed': 5000,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1038
    m_CheckForbid = 0
    m_AIPerformDam = 0
    
    def CanUse(self, oWarrior, dInfo):
        dInfo['IgnoreDie'] = 1
        return super().CanUse(oWarrior, dInfo)



def CustomSkillEnd(oSkill, *args):
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oOwner = oAttack.GetOwner()
    if not oOwner:
        return None
    oState = oOwner.m_State.GetItemBySID(33953)
    if not oState or oState.GetCount() < 1:
        return None
    oState.AddCount(oOwner, -1)
    dReason = {
        'Type': TYPE_RELIFE_PF,
        'ActNum': oSkill.m_Base['ActNum'],
        'AID': oSkill.m_Base['AID'] }
    if args:
        dInfo = args[0]
        if 'RelifePos' in dInfo:
            dReason['RelifePos'] = dInfo['RelifePos']
    oAttack.Relife(dReason)

