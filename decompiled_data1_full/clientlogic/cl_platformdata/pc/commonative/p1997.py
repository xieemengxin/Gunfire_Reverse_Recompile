# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1997.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1997.pyc
# Source Generated with Decompyle++
# File: p1997.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.MonsterPauseAgent(skill)
    cl_action.TeleportToNearestSpacePosByPos(skill, cl_action.GetSkillCustomData(skill, 'vStart', defaultValue = (0, 0, 0)))
    cl_action.MonsterResumeAgent(skill)


def Halt(skill):
    cl_action.SkillForbid(skill, False, 1085)


def End(skill):
    cl_action.SkillForbid(skill, False, 1085)


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 1997
    m_Name = '#NT#迭代小玖机甲空降身边'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = 0
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

