# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12038.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12038.pyc
# Source Generated with Decompyle++
# File: p12038.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_WEAKNESS, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_LSTINT

class CCartoon2(TraceCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetMuzzlePos(skill)):
                return None
            cls.EnableShow(skill, 1, 70, 50, showstart = cl_action.GetMuzzlePos(skill), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 30, lockDis = 50, IgnoreDefalutDis = 9999, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = True, searchByDistance = True, canLockMoreTimes = False, scale = 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


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
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12038
    m_Name = 'S7射速自瞄弹道'
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
    m_UseCurWeapon = 1
    m_ForbidRule = 0

