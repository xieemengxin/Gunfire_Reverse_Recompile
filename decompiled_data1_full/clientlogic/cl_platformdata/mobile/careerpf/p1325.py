# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1325.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1325.pyc
# Source Generated with Decompyle++
# File: p1325.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    pass


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1325
    m_Name = '灵墨化形'
    m_ExtPerform = (1326, 1918, 1920, 1921)
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
        'ColdTime': 1500,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 1600,
        'Att': 60000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3300,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_BaseArgData = {
        'DamReduceRatio': 6000,
        'ShieldRecoverAdd': 1000,
        'AddStateThresholdValue': 15 }
    m_AIPerformDam = 600
    
    def UsePerform(self, oWarrior, oSkill):
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        self.DoAction(oSkill)


