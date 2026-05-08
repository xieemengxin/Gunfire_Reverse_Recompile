# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39065.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39065.pyc
# Source Generated with Decompyle++
# File: p39065.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    if skill.m_Cache['Phase'] == 2 or cl_action.GetPerformArgValue(skill, 'Summon') > 0:
        cl_action.SummonAreaMonster(skill, 99, {
            5: 100,
            6: 100 }, {
            1: 10 })
    elif skill.m_Cache['Phase'] == 4 or cl_action.GetPerformArgValue(skill, 'Summon') > 0:
        cl_action.SummonAreaMonster(skill, 99, {
            5: 100,
            6: 100 }, {
            1: 10 })
    elif skill.m_Cache['Phase'] == 6 and cl_action.GetPerformArgValue(skill, 'Summon') > 0:
        cl_action.SummonAreaMonster(skill, 99, {
            5: 100,
            6: 100 }, {
            1: 10 })


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39065
    m_Name = '海船-转阶段总控技能'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_BaseArgData = {
        'Summon': 1 }
    m_CacheAttr = [
        'DebuffProb']

