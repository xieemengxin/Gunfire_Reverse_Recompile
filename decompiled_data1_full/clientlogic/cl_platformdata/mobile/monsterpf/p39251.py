# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39251.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39251.pyc
# Source Generated with Decompyle++
# File: p39251.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, SKILLCACHE_POS

class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'end', cl_action.CrtArgTargetPos(skill, notContainDying = False))

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(DirectPosCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SwitchAttackerPhyAble(skill, True)
        cl_action.AttackerUsePerform(skill, 39242, { }, 0, 0)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 1009, cl_action.ToInt(skill, (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / (20 + cl_action.GetPlayRound(skill) * 8)) * 100 + 4), 1, { })

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
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / (20 + cl_action.GetPlayRound(skill) * 8)) * 100 + 4), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        cl_action.MonsterTeleportToPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 3)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SwitchAttackerPhyAble(skill, False)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.AttackerUsePerform(skill, 39250, {
            'vPos': cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_math.Vec3Minus(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetSkillVarCache(skill, 'start')), (cl_action.GetTimerCartoonCurTimes(skill, 2) - 1) * 2, 0),
            'end': cl_action.GetSkillCacheData(skill, SKILLCACHE_POS) }, 10, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.ToInt(skill, (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / (20 + cl_action.GetPlayRound(skill) * 8)) * 100 + 4) / (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 2 + 1)) if cl_action.ToInt(skill, cl_action.ToInt(skill, (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / (20 + cl_action.GetPlayRound(skill) * 8)) * 100 + 4) / (cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 2 + 1)) > 4 else 4, cl_action.ToInt(skill, cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS)) / 2 + 1))

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

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
        if 39247 == 39247:
            cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillVarCache(skill, 'end'))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_POS])
            if cl_action.CheckHasState(skill, 7998):
                cartoon = { }
                CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cl_action.SwitchAttackerPhyAble(skill, False)
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
        elif 39244 == 39247:
            cl_action.SetSkillVarCache(skill, 'target', cl_action.CrtArgTargetPos(skill, notContainDying = False))
            if cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillVarCache(skill, 'target')) > 18:
                cl_action.SetSkillVarCache(skill, 'end', cl_action.DemonKingRoamingSiteSelection(skill, 39247, {
                    'angle1': 45,
                    'distance1': 8,
                    'angle2': 45,
                    'distance2': 12,
                    'randius1': 14,
                    'randius2': 18,
                    'winkangle1': 105,
                    'winkangle2': 150 }))
                cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillVarCache(skill, 'end'))
                cl_action.ServerSendSkillCache(skill, [
                    SKILLCACHE_POS])
                if cl_action.CheckHasState(skill, 7998):
                    cartoon = { }
                    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cl_action.SwitchAttackerPhyAble(skill, False)
                    cartoon = { }
                    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cl_action.SetSkillVarCache(skill, 'end', cl_action.GetMonsterWinkPos(skill, 10, 14, 150, 179))
                cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillVarCache(skill, 'end'))
                cl_action.ServerSendSkillCache(skill, [
                    SKILLCACHE_POS])
                if cl_action.CheckHasState(skill, 7998):
                    cartoon = { }
                    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
                else:
                    cl_action.SwitchAttackerPhyAble(skill, False)
                    cartoon = { }
                    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.SetSkillVarCache(skill, 'end', cl_action.DemonKingRoamingSiteSelection(skill, 39247, {
                'angle1': 45,
                'distance1': 8,
                'angle2': 45,
                'distance2': 12,
                'randius1': 14,
                'randius2': 18,
                'winkangle1': 105,
                'winkangle2': 150 }))
            cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillVarCache(skill, 'end'))
            cl_action.ServerSendSkillCache(skill, [
                SKILLCACHE_POS])
            if cl_action.CheckHasState(skill, 7998):
                cartoon = { }
                CCartoon2.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cl_action.SwitchAttackerPhyAble(skill, False)
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'start', cl_action.CrtArgSelfPos(skill))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39251
    m_Name = '美术测试-妖王-妖气漫游'
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
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

