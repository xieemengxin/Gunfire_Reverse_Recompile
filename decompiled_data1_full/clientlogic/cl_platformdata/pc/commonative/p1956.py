# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1956.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1956.pyc
# Source Generated with Decompyle++
# File: p1956.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    cl_action.PerformDamage(skill, {
        'Att': skill.m_Cache['Att'] })
    cl_action.PushHeroVictim(skill, (0, 0, 0), 25, 7, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)


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
    m_SID = 1956
    m_Name = '首领秘卷龙卷风击退'
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
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

