# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p22822.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p22822.pyc
# Source Generated with Decompyle++
# File: p22822.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import WARRIOR_SUMMON

def Action(skill):
    cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSummonPosByBoxSplit(skill, 6, 4, cl_action.GetWarriorModelRadius(skill, WARRIOR_SUMMON, 1020, 'NavMesh'), True, {
        cl_action.GetPerformArgValue(skill, 'ExtSummonNum') + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) + 2: 70,
        1 + cl_action.GetPerformArgValue(skill, 'ExtSummonNum') + cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True): 30 }, { }, False), WARRIOR_SUMMON, {
        1020: 10 }, {
        'SameGrade': 1 })


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
    m_SID = 22822
    m_Name = '【第三幕】召唤法师怪-死亡召唤'
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
        'ColdTime': 500,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 1.5
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

