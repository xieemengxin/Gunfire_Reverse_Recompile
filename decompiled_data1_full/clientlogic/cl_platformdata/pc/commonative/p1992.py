# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1992.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1992.pyc
# Source Generated with Decompyle++
# File: p1992.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import COMMON_SEASON_DAMEAGE, MONSTER_PART_UNTAGGED

def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        COMMON_SEASON_DAMEAGE][0])
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    cl_action.ModifySkillCache(skill, 'Att', cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0))
    cl_action.WeaponDamage(skill, {
        'Att': 100 }, { }, sendPFMsg = True)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1992
    m_Name = '#NT#毒雾装置毒气技能'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'DebuffProb': 3000,
        'Att': 60000,
        'CrazyEff': 10000 }
    m_ClientNeed = 1
    m_UseCurWeapon = 0
    m_ForbidRule = 0

