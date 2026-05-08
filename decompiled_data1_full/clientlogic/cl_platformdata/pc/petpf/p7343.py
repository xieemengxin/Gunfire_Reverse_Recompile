# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petpf/p7343.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petpf/p7343.pyc
# Source Generated with Decompyle++
# File: p7343.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import MONSTER_PART_UNTAGGED, SKILLCACHE_LSTINT

def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetSkillCustomData(skill, 'LockTarget'))
    for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)), 1):
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1])
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[i1]))
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] }, dArgs = { })
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.petactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, PETPF_ACTIVE_ATTACK

class CPerform(CCustomPerform):
    m_SID = 7343
    m_Name = '通用妖灵额外普攻'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 5,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_ATTACK
    m_SpellPower = 0
    m_NeedTarget = 0
    m_ForbidRule = 0

