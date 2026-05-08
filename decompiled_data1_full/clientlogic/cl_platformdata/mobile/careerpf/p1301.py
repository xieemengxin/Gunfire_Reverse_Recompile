# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1301.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1301.pyc
# Source Generated with Decompyle++
# File: p1301.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_item

def Action(skill):
    cl_action.AttackerAddState(skill, 32004, skill.m_Cache['AddStateTime'], 0, { })


def GetSkillCacheIndex():
    return []


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1301
    m_Name = '精英双持'
    m_ExtPerform = (1644,)
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
        'ColdTime': 4000,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 2000,
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
    m_ForbidRule = 1031
    m_CheckForbid = 1013
    m_AIPerformDam = 8000
    
    def CanUse(self, oWarrior, dInfo):
        if not oWarrior.ValidOpenDualWield():
            return 0
        return super(CPerform, self).CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        self.DoAction(oSkill)


