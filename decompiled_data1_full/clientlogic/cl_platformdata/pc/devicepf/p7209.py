# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicepf/p7209.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicepf/p7209.pyc
# Source Generated with Decompyle++
# File: p7209.pyc (Python 3.6)

from cl_platformdata.custom.commonative.customaction import Custom50101Dam
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
    if cl_action.GetSkillCustomData(skill, 'PF50101', defaultValue = 0) == 0:
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetTargetStateCount(skill, cl_action.GetSkillCustomData(skill, 'ToxicStateSID', defaultValue = 0), cl_action.GetSkillVID(skill), False, True) * skill.m_Cache['Att'] })
    else:
        cl_action.CustomPerformAction(skill, 7209, 'PF50101Dam', {
            'TargetID': cl_action.GetSkillVID(skill) })


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
    m_SID = 7209
    m_Name = '毒气装置-毒气伤害'
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


def PF50101Dam(oSkill, *args):
    Custom50101Dam(oSkill)

