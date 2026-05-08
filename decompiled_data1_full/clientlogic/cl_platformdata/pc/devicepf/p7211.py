# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicepf/p7211.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicepf/p7211.pyc
# Source Generated with Decompyle++
# File: p7211.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import MONSTER_PART_UNTAGGED

def Action(skill):
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    cl_action.ModifySkillHitPos(skill, cl_action.CrtArgHitPos(skill))
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.PerformDamage(skill, {
        'Att': cl_action.ToInt(skill, cl_action.GetAttackerAttr(skill, 'Att') * 120 / 100) })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CDeviceActive as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 7211
    m_Name = '屏障专属1-附加装置伤害'
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
        'AttDistance': 10,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'EnergyCost': 0,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = (0,)
    m_ForbidRule = 0

