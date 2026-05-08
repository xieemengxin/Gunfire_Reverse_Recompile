# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1751.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1751.pyc
# Source Generated with Decompyle++
# File: p1751.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, NWARRIOR_DROP, OBJ_ENEMY, S6_DICE_DAMAGE

class CCartoon2(TraceCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetCameraDirPos(skill, 0), cl_action.CrtArgTargetPos(skill, notContainDying = False), 1, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, targetID = 0, liveTime = 0, lineDistance = 1, angle = 180, lockWeakness = False, lockAngle = 360, canDesAngle = 10, lockDis = 50, IgnoreDefalutDis = 9999, IgnoreSummon = False, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, lockSumm = True, lockCanDestroy = False, lockHideDoor = False, isBlocked = True, isMonsterFirst = True, lockExplode = False, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = True, searchByDistance = True, canLockMoreTimes = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'S6DiceSkill', 1)
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        S6_DICE_DAMAGE][0])
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


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
    m_SID = 1751
    m_Name = '弹射骰子（队友AI）'
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
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'Radius': 10 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'AIPerformDam': 200 }

