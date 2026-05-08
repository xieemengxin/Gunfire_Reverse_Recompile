# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1311.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1311.pyc
# Source Generated with Decompyle++
# File: p1311.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import SKILL_TYPE_THROW

def Action(skill):
    if cl_action.CheckPointSkillIsEnable(skill, 1417):
        cl_action.SwitchHeroPerform(skill, 1417, 1418, SKILL_TYPE_THROW)
        cl_action.AttackerAddState(skill, 32424, 0, 0, { })
    else:
        cl_action.SwitchHeroPerform(skill, 1418, 1417, SKILL_TYPE_THROW)
        cl_action.AttackerRemoveState(skill, 32424)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1311
    m_Name = '妖星'
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
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 0
    
    def CanUse(self, oWarrior, dInfo):
        if oWarrior.m_State.GetItemBySID(32424):
            return 1
        return super(CPerform, self).CanUse(oWarrior, dInfo)


