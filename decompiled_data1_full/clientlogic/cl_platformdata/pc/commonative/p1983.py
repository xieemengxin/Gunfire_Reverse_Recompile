# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1983.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1983.pyc
# Source Generated with Decompyle++
# File: p1983.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import MONSTER_PART_UNTAGGED, S6_DICE_DAMAGE

def Action(skill):
    cl_action.SetSkillServerCache(skill, 'S6DiceSkill', 1)
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        S6_DICE_DAMAGE][0])
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCustomData(skill, 'LockTrigger', defaultValue = 0))
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCustomData(skill, 'LockTrigger', defaultValue = 0)))
    cl_action.PerformDamage(skill, {
        'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) }, dArgs = { })


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
    m_SID = 1983
    m_Name = '控制骰子-额外伤害'
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
        'ChargeTime': 0,
        'Radius': 5 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

