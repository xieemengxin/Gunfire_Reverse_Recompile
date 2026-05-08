# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/clientactive/p12028.pyc
# RelativePath: clientlogic/cl_platformdata/pc/clientactive/p12028.pyc
# Source Generated with Decompyle++
# File: p12028.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon1(TraceCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 33088, 0, 0, { })
        cl_action.WeaponDamage(skill, {
            'Att': 175 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = 'Att002')) if cl_action.GetSkillVarCache(skill, 'index') % 2 == 1 else cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = 'Att001'))):
                return None
            if cl_action.IsHeroCtrl(skill):
                if cl_action.GetSkillVarCache(skill, 'index') % 2 == 1:
                    pass
                
            
            skill(skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 70, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = 'Att001')), showstart = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = 'muzzle')), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 0, angle = 15, lockDis = 80, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 100)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
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
        CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetSkillVarCache(skill, 'index'))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if not cl_action.CheckHasInscription(skill, 13085) and cl_action.CheckHasInscription(skill, 13070) and cl_action.GetRandomInRange(skill, 1, 100) >= 80:
        for i1 in range(0, 1, 1):
            cl_action.SetSkillVarCache(skill, 'index', i1)
            if cl_action.GetSkillVarCache(skill, 'index') % 2 == 1:
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetSkillVarCache(skill, 'index'))
                continue
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
        
    else:
        for i2 in range(0, 1, 1):
            cl_action.SetSkillVarCache(skill, 'index', i2)
            if cl_action.GetSkillVarCache(skill, 'index') % 2 == 1:
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = cl_action.GetSkillVarCache(skill, 'index'))
                continue
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
        


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12028
    m_Name = '#NT#追踪步枪特殊弹道'
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
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_UseCurWeapon = 0
    m_ForbidRule = 0

