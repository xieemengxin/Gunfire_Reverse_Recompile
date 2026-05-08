# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suitactive/p8607.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suitactive/p8607.pyc
# Source Generated with Decompyle++
# File: p8607.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_LSTINT

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.ModifySkillCache(skill, 'DebuffProb', cl_action.GetSkillCustomData(skill, 'ElementExceptionRatio', defaultValue = 2000))
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[cl_action.GetCartoonLoopID(skill, 10)]), (0, 0, 0), [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 46, 1)

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
        CCartoon10.Init(skill, cartoon, casting = 0, index = cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 0) - 1))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, cl_action.GetRangeTargetByPointTarget(skill, cl_action.GetSkillAID(skill), 30, True, cl_action.GetSkillCustomData(skill, 'Cnt', defaultValue = 2), bSort = True))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_LSTINT])
    if not len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) == 0:
        cl_action.SetSkillVarCache(skill, 'TempTargetList', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT))
        if len(cl_action.GetSkillVarCache(skill, 'TempTargetList')) < cl_action.GetSkillCustomData(skill, 'Cnt', defaultValue = 2):
            for i1 in range(0, cl_action.GetSkillCustomData(skill, 'Cnt', defaultValue = 2) - len(cl_action.GetSkillVarCache(skill, 'TempTargetList')), 1):
                cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT).append(cl_action.GetSkillVarCache(skill, 'TempTargetList')[cl_action.CrtArgRandomNum(skill, 0, len(cl_action.GetSkillVarCache(skill, 'TempTargetList')) - 1)])
            
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.suitactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, SUIT_PERFORM_POS_NOTCONTROL

class CPerform(CCustomPerform):
    m_SID = 8607
    m_Name = '迅影流星'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_FIRE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 25,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'Att': 0,
        'Radius': 2,
        'MaxCover': 1 }
    m_SourceSuit = 15124
    m_Pos = SUIT_PERFORM_POS_NOTCONTROL
    m_ForbidRule = 0
    m_BaseArgData = {
        'AIPerformDam': 500 }

