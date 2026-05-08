# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p22252.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p22252.pyc
# Source Generated with Decompyle++
# File: p22252.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    pass


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCache():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 22252
    m_Name = '自爆怪-飞行自爆被动爆炸'
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
        'ColdTime': 300,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

