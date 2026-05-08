# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1670.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1670.pyc
# Source Generated with Decompyle++
# File: p1670.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_perform
from cl_commondefines import SKILLCACHE_LSTINT

def Action(skill):
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1670
    m_Name = '游侠雷击'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_THUNDER
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 80000,
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
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'Thunder': 1 }
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 1000
    
    def UsePerform(self, oWarrior, oSkill):
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, SKILLCACHE_LSTINT, oSkill.m_Custom['LockTarget'])
        oSkill.m_Collect['CareerPf'] = oSkill.m_Custom['CareerPf'] if 'CareerPf' in oSkill.m_Custom else 0
        super().UsePerform(oWarrior, oSkill)


