# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1710.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1710.pyc
# Source Generated with Decompyle++
# File: p1710.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import WARRIOR_ENTITYEFFECT, WARRIOR_SUMMON

def Action(skill):
    cl_action.AssignSummonDie(skill, cl_action.GetAttackSummon(skill, WARRIOR_ENTITYEFFECT), 0)
    cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.ChooseBoxGemSummonPos(skill, cl_action.ToInt(skill, 11 - cl_action.GetPlayRound(skill) - cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = False) * 0.5) if cl_action.CheckCurLevel(skill, 1301213) or cl_action.CheckCurLevel(skill, 1301212) else cl_action.ToInt(skill, 8 - cl_action.GetPlayRound(skill) - cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = False) * 0.5)), WARRIOR_SUMMON, {
        1062: 10 }, {
        'Radius': 2 }, (0, 0, 0))
    for i1 in range(0, len(cl_action.GetSkillSummonCreate(skill)), 1):
        cl_action.TargetAddState(skill, 1009, 0, 0, { }, cl_action.GetSkillSummonCreate(skill)[i1])
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1710
    m_Name = '宝箱怪召唤宝石'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

