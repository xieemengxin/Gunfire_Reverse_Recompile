# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petpf/p7339.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petpf/p7339.pyc
# Source Generated with Decompyle++
# File: p7339.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import SKILLCACHE_POS

def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_POS)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.CrtArgSelfPos(skill))
    cl_action.TeleportToNearestSpacePosByPos(skill, cl_action.GetTargetNearestSpace(skill, cl_action.GetSkillVID(skill), True, 1))
    cl_action.AttackerAddState(skill, 33259, 0, 0, { })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.petactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, PETPF_ACTIVE_SPELL

class CPerform(CCustomPerform):
    m_SID = 7339
    m_Name = '词条50525'
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
        'AttDistance': 300,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_SPELL
    m_SpellPower = 100
    m_NeedTarget = 0
    m_ForbidRule = 0

