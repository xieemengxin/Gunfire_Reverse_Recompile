# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suitactive/p8603.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suitactive/p8603.pyc
# Source Generated with Decompyle++
# File: p8603.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import SKILLCACHE_LSTINT

def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    cl_action.TargetAddState(skill, 33436, 600, 0, { }, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
    cl_action.TargetAddState(skill, 33437, 600, 0, { }, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.suitactive import CPerform as CCustomPerform
from cl_commondefines import SUIT_PERFORM_POS_NOTCONTROL

class CPerform(CCustomPerform):
    m_SID = 8603
    m_Name = '#NT#测试技能三'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 1000,
        'Radius': 0,
        'MaxCover': 1 }
    m_SourceSuit = 15111
    m_Pos = SUIT_PERFORM_POS_NOTCONTROL
    m_ForbidRule = 0

