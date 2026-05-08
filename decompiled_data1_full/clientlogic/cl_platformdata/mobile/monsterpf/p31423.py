# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p31423.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p31423.pyc
# Source Generated with Decompyle++
# File: p31423.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    cl_action.SetMonsterAttackerPhase(skill, 2)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 31423
    m_Name = '【第二幕】精英中型远程-隐身远程怪-隐身'
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
        'ColdTime': 1000,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

