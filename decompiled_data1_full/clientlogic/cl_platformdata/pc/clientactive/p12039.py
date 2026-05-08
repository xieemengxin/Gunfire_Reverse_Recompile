# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12039.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12039.pyc
# Source Generated with Decompyle++
# File: p12039.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_LSTINT

class CCartoon1(TraceCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[2] * 100 }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])):
                return None
            cls.EnableShow(skill, 999, 70, 15, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 180, lockDis = 10, IgnoreDefalutDis = 9999, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[3], maskFightType = NWARRIOR_DROP, noTargetOver = True, searchByDistance = True, canLockMoreTimes = True, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE

class CPerform(CCustomPerform):
    m_SID = 12039
    m_Name = '#NT#小玖弹射飞弹'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_TRUE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0

