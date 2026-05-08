# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39099.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39099.pyc
# Source Generated with Decompyle++
# File: p39099.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateThrowCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, FIGHT3_KEY_IGNORETHUMP, OBJ_ENEMY, WARRIOR_HERO

class CCartoon11(TimerCartoon):
    m_SID = 11
    
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
        cl_action.SetSkillVarCache(skill, 'RPos', cl_action.CrtArgTargetPosGroudPos(skill, cl_math.Vec3Minus(cl_action.CalTargetPosInRectangle(skill, (-7, 0, -9), (70, 0, 50)), (7, 0, 0.5))))
        cl_action.AddClientEffect(skill, 1015, cl_action.CrtArgTargetPosGroudPos(skill, cl_math.Vec3Minus(cl_action.CalTargetPosInRectangle(skill, (-7, 0, -9), (70, 0, 50)), (7, 0, 0.5))), 0, (0, 0, 0))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon16(DirectPosCartoon):
    m_SID = 16
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 60 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 6), (0, 0, 0), [
                9], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DelegateThrowCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.DeleteClientEffect(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ENEMY):
            cl_action.WeaponDamage(skill, {
                'Att': 80 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon16.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-10, 20, -18)), cl_action.CrtArgSetParabolaSpeed(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (-10, 20, -18)), cl_action.GetSkillVarCache(skill, 'RPos'), 40, 0, 0.5), 40, 3.71, (0, 0, 0), (1, 1), 300, True, liveTime = 0, innerRadius = 0.5, pierce = 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon15(TimerCartoon):
    m_SID = 15
    
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
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(DirectPosCartoon):
    m_SID = 13
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 60 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 14), (0, 0, 0), [
                9], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(DelegateThrowCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ENEMY):
            cartoon = { }
            CCartoon13.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 80 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon13.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (10, 20, -18)), cl_action.CrtArgSetParabolaSpeed(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (10, 20, -18)), cl_action.GetSkillVarCache(skill, 'LPos'), 40, 0, 0.5), 40, 3.71, (0, 0, 0), (1, 1), 300, True, liveTime = 0, innerRadius = 0.5, pierce = 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon17(TimerCartoon):
    m_SID = 17
    
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
        CCartoon14.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'LPos', cl_action.CrtArgTargetPosGroudPos(skill, cl_math.Vec3Add(cl_action.CalTargetPosInRectangle(skill, (-7, 0, -9), (70, 0, 50)), (7, 0, -0.5))))
        cl_action.AddClientEffect(skill, 1015, cl_action.CrtArgTargetPosGroudPos(skill, cl_math.Vec3Add(cl_action.CalTargetPosInRectangle(skill, (-7, 0, -9), (70, 0, 50)), (7, 0, -0.5))), 0, (0, 0, 0))
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon17.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.MonsterFaceTarget(skill, 0, 100, 1)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cartoon = { }
    CCartoon9.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39099
    m_Name = '轮回10-石巨人拳头'
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
        'ColdTime': 1,
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

