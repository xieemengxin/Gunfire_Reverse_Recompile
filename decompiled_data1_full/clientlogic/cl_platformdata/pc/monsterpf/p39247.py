# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39247.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39247.pyc
# Source Generated with Decompyle++
# File: p39247.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, FlyingMuzzleCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, CRT_ROTATE_FORATT, FIGHT3_KEY_IGNOREKNOCKBACK, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon8(TimerCartoon):
    m_SID = 8
    
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
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 106, 1)

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
        cl_action.AttackerAddState(skill, 8027, 0, 0, { })

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 110, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cl_action.StartBackSwing(skill, 140)
        cl_action.AttackerRemoveState(skill, 8012, bSameItem = False)
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(RayCastCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 40 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), 5, cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 1) - 1) * 7 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) + cl_action.ToInt(skill, i1 * 36 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))), cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), 5, cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 1) - 1) * 7 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) + cl_action.ToInt(skill, i1 * 36 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))), cl_action.StartAndEndAtSameHeight(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), 99, cl_action.ToInt(skill, (cl_action.GetTimerCartoonCurTimes(skill, 1) - 1) * 7 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) + cl_action.ToInt(skill, i1 * 36 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)))), 99, 35, cl_action.GetPlayRound(skill) + 7, targettype = OBJ_ENEMY, liveTime = 0, radius = 0.65, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
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
        for i1 in range(0, 10, 1):
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -1 + 29), 30)

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
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(FlyingMuzzleCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 0, index = 0)

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
    
    def InitSuccess(cls, skill, i2, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), 5, cl_action.ToInt(skill, i2 * 36 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))), cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1.2, 0)), 5, cl_action.ToInt(skill, i2 * 36 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))), 60 + cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -1 + 29) - 0, (0, 0, 0), 60, 60 + cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -1 + 29), 30, cl_action.ToInt(skill, cl_action.GetPlayRound(skill) * -1 + 29), 7 * cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 5, 0, CRT_ROTATE_FORATT, (0, 0, 0), (0, 0, 0))

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        for i2 in range(0, 10, 1):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = i2)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 94, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PushHeroVictim(skill, cl_action.CrtArgSelfCenterPos(skill), (4 if cl_action.ToInt(skill, cl_action.GetDistanceByAttackerAndTarget(skill) * -1 + 15) < 4 else cl_action.ToInt(skill, cl_action.GetDistanceByAttackerAndTarget(skill) * -1 + 15)) / 0.3, 4 if cl_action.ToInt(skill, cl_action.GetDistanceByAttackerAndTarget(skill) * -1 + 15) < 4 else cl_action.ToInt(skill, cl_action.GetDistanceByAttackerAndTarget(skill) * -1 + 15), 10000, downSpeed = 1.47, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), (0, 0, 0), [
                15], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'Relic': 1 })

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 106, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, 1 if cl_action.CrtArgRandomNum(skill, 0, 100) > 50 else -1)
    if cl_action.GetAttackSID(skill) == 39251:
        cl_action.AttackerAddState(skill, 8079, 0, 1, { })
        cl_action.AttackerAddState(skill, 8012, 0, 1, { })
        cl_action.LockMonsterAttackerFace(skill)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 1)
    else:
        cl_action.AttackerAddState(skill, 8012, 0, 1, { })
        cl_action.LockMonsterAttackerFace(skill)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 1)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39247
    m_Name = '妖王-妖气释放'
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
        'ColdTime': 3500,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_BaseArgData = {
        'DamReduce': -5000 }
    m_CacheAttr = [
        'DebuffProb']

