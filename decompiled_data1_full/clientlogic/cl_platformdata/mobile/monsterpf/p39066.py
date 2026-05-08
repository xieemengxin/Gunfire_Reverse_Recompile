# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39066.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39066.pyc
# Source Generated with Decompyle++
# File: p39066.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import SKILLCACHE_BALLISTICTYPE

def Action(skill):
    cl_action.SummonAreaMonster(skill, 98, {
        1: 100,
        2: 100 }, {
        (1 if cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 2 else 0) + (1 if cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 3 else 0) + (1 if cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) >= 4 else 0) + cl_action.GetSkillCacheData(skill, SKILLCACHE_BALLISTICTYPE): 10 })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_BALLISTICTYPE]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, NONE_DISTANCE
from cl_newformula import Func205

class CPerform(CCustomPerform):
    m_SID = 39066
    m_Name = '海船-召唤近战小兵'
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
        'ColdTime': (lambda *a: 2200 - Func205(*a) * 200),
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

