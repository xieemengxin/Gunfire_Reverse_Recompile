# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1920.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1920.pyc
# Source Generated with Decompyle++
# File: p1920.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import MONSTER_PART_UNTAGGED, SKILLCACHE_LSTINT

def Action(skill):
    cl_action.ApplyStateTransDamFactor(skill, 33044)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillCustomData(skill, 'LockTarget'))
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1]))
        for i2 in range(0, cl_action.GetTargetStateCount(skill, 33272, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1], False, True), 1):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) }, dArgs = { })
        
    


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
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1920
    m_Name = '#NT#通用浊墨伤害'
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
        'AttDistance': 99,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 10000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
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
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0

