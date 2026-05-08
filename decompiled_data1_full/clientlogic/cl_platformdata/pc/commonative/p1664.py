# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1664.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1664.pyc
# Source Generated with Decompyle++
# File: p1664.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, WARRIOR_HERO
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'idx', cl_action.GetSkillVarCache(skill, 'idx') + 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'ComAtt': 60 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'idx'))), (0, 0, 0), [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.AddClientEffect(skill, 1018 if cl_action.GetNowLayer(skill) == 2 else 1017, cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop'))), 200, (0, 0, 0))
        cl_action.AddSceneEventForState(skill, cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop'))), 200, 1, {
            'Radius': 2 }, 32248, 200, 1, iFightType = WARRIOR_HERO, iLeaveSetTime = -1)

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 200, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'idx', cl_action.GetSkillVarCache(skill, 'idx') + 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'ComAtt': 60 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'idx'))), (0, 0, 0), [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.AddClientEffect(skill, 1018 if cl_action.GetNowLayer(skill) == 2 else 1017, cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop'))), 200, (0, 0, 0))
        cl_action.AddSceneEventForState(skill, cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop'))), 200, 1, {
            'Radius': 2 }, 32248, 200, 1, iFightType = WARRIOR_HERO, iLeaveSetTime = -1)

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
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 200, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'loop', 1 + cl_action.GetSkillVarCache(skill, 'loop'))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.CheckHasPlayerInRange(skill, 12, iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cl_action.SetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop')), cl_action.CrtPlayerOffsetPosInRange(skill, 15, (6, 0, 6), iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE))
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop')), cl_action.CrtPlayerOffsetPosInRange(skill, 15, (20, 0, 20), iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

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
        cl_action.SetSkillVarCache(skill, 'loop', 1 + cl_action.GetSkillVarCache(skill, 'loop'))
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.CheckHasPlayerInRange(skill, 12, iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cl_action.SetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop')), cl_action.CrtPlayerOffsetPosInRange(skill, 15, (6, 0, 6), iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE))
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.SetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetSkillVarCache(skill, 'loop')), cl_action.CrtPlayerOffsetPosInRange(skill, 15, (20, 0, 20), iPyFlag = PY_FLAG_EXCLUDEMONSTERHATE))
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 56 - cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = False) * 6), cl_action.ToInt(skill, cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = False) * 3))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'loop', 0)
    cl_action.SetSkillVarCache(skill, 'idx', 1)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1664
    m_Name = '怪物强化词条-雷霆'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_THUNDER
    m_BaseAttrData = {
        'ColdTime': 1,
        'AttDistance': 15,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 10000 }

