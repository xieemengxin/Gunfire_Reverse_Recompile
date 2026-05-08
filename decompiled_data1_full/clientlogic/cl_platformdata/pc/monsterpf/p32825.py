# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p32825.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p32825.pyc
# Source Generated with Decompyle++
# File: p32825.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_RECTANGLE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT

class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.MonsterFaceTarget(skill, cl_action.GetSkillVID(skill), 35, 0)

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
        cl_action.LockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 100)

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
        cl_action.UnlockMonsterAttackerFace(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
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
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'Interval') + 175) * (cl_action.GetSkillVarCache(skill, 'AllNum') - cl_action.GetSkillVarCache(skill, 'CurNum'))), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 0.5, 0)), cl_action.CrtArgSkillEndPos(skill), [
                60,
                2,
                2], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'Interval') + 175) * (cl_action.GetSkillVarCache(skill, 'AllNum') - cl_action.GetSkillVarCache(skill, 'CurNum'))) == 0:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 80, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgSelfPos(skill), cl_math.Vec3Minus(cl_action.CrtArgTargetPos(skill, notContainDying = False), cl_action.CrtArgSelfPos(skill)), 3, 0), cl_action.CrtArgTargetPos(skill, notContainDying = False), [
                1,
                1,
                1], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
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
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'Interval') * (cl_action.GetSkillVarCache(skill, 'CurNum') - 1)), 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTINT, [
        cl_action.GetSkillCustomData(skill, 'Interval', defaultValue = 0),
        cl_action.GetSkillCustomData(skill, 'AllNum', defaultValue = 0),
        cl_action.GetSkillCustomData(skill, 'CurNum', defaultValue = 0)])
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_INT])
    cl_action.SetSkillVarCache(skill, 'Interval', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0])
    cl_action.SetSkillVarCache(skill, 'AllNum', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[1])
    cl_action.SetSkillVarCache(skill, 'CurNum', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[2])
    if cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'Interval') * (cl_action.GetSkillVarCache(skill, 'CurNum') - 1)) == 0:
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 32825
    m_Name = '【第三幕】精英召唤法师怪-连携射线'
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
        'ColdTime': 500,
        'AttDistance': 45,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 1.5
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1050
    m_CacheAttr = [
        'DebuffProb']

