# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p21332.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p21332.pyc
# Source Generated with Decompyle++
# File: p21332.pyc (Python 3.6)

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
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK

class CPerform(CCustomPerform):
    m_SID = 21332
    m_Name = '鲨鱼怪浪鳍-两段普攻'
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
        'ColdTime': 200,
        'AttDistance': 4,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = CLOSE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1038
    m_BaseArgData = {
        'MovingCast': 1 }
    m_CacheAttr = [
        'DebuffProb']

