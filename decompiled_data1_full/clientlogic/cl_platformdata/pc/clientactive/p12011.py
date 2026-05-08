# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12011.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12011.pyc
# Source Generated with Decompyle++
# File: p12011.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_PERFORMMODE

class CCartoon0(TraceCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) * 2) }, { }, sendPFMsg = False)
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
            cl_action.WeaponDamage(skill, {
                'Att': 2000 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (cl_action.GetSkillCustomArg(skill, 'X') / 100, cl_action.GetSkillCustomArg(skill, 'Y') / 100, cl_action.GetSkillCustomArg(skill, 'Z') / 100)):
                return None
            cls.EnableShow(skill, 1, 20, 20, showstart = (cl_action.GetSkillCustomArg(skill, 'X') / 100, cl_action.GetSkillCustomArg(skill, 'Y') / 100, cl_action.GetSkillCustomArg(skill, 'Z') / 100), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 20, lockDis = 100, IgnoreDefalutDis = 0, iIgnoreMonsterID = cl_action.GetSkillCustomArg(skill, 'CurVID'), FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerAddState(skill, 1681, 0, 1, {
            'Att': cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) / 100) })
        for i1 in range(0, 10, 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_INT)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_PERFORMMODE)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12011
    m_Name = '无悔散射'
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
    m_BaseArgData = {
        'Att': 10000 }

