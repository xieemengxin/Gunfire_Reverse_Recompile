# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39203.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39203.pyc
# Source Generated with Decompyle++
# File: p39203.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import WARRIOR_MONSTER

def Action(skill):
    cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.AdjustTentaclePos(skill, cl_action.ChooseSweepTentaclePosNew(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetGroundPos(skill), 55, 30), (1, 0, 0), 3921, 55, 9, 180, 1, lastDirOnly = False, heightOffset = 0), WARRIOR_MONSTER, {
        39211: 1 }, {
        'FollowDie': 1 })
    cl_action.WarriorUsePerform(skill, cl_action.GetSkillSummonCreate(skill)[0], 39213, { }, False)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39203
    m_Name = '海怪-召唤横扫'
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
        'ColdTime': 1500,
        'AttDistance': 200,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

