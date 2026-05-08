# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1915.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1915.pyc
# Source Generated with Decompyle++
# File: p1915.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import MONSTER_PART_FLAW

def Action(skill):
    cl_action.SetSkillServerCache(skill, '1915Flaw', cl_action.GetTargetFlaw(skill, cl_action.GetSkillVID(skill), False))
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    cl_action.ModifySkillHitPos(skill, cl_action.CrtArgHitPos(skill))
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_FLAW)
    for i1 in range(0, len(cl_action.GetSkillServerCache(skill, '1915Flaw')), 1):
        if not cl_action.GetSkillCustomData(skill, 'Flaw', defaultValue = 0) == cl_action.GetSkillServerCache(skill, '1915Flaw')[i1]:
            cl_action.SetHitFlaw(skill, cl_action.GetSkillServerCache(skill, '1915Flaw')[i1], iBreakFlaw = 0)
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.ToInt(skill, cl_action.GetPerformArgValue(skill, 'Att', iDefault = 100) / 2) }, { }, sendPFMsg = False)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1915
    m_Name = '#NT#破绽伤害'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 1
    m_ForbidRule = 0
    m_BaseArgData = {
        'Att': 100 }

