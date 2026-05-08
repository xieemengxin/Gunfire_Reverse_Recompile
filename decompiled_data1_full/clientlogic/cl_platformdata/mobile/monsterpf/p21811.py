# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p21811.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p21811.pyc
# Source Generated with Decompyle++
# File: p21811.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, EntityParabolaCartoon, MonsterPushHeroCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, OBJ_ALLNOSELF, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY, WARRIOR_HERO, WARRIOR_MONSTER, WARRIOR_SUMMON

class CCartoon8(TimerCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetSkillSummonCreate(skill)[0], 4)
        cl_action.UnlockMonsterAttackerFace(skill)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.UnlockMonsterAttackerFace(skill)

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
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(EntityParabolaCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALLNOSELF):
            cl_action.PushVictim(skill, cl_action.GetCartoonCurPos(skill, 4), 10, 3, 10000, angle = 315)
        elif not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALLNOSELF) and cl_action.GetSkillVarCache(skill, 'pushhero') == cl_action.GetCurVID(skill):
            cl_action.PushHeroVictim(skill, cl_action.GetCartoonCurPos(skill, 4), 10, 3, 10000, downSpeed = 0, fGravaty = 9.8, angle = 315)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_math.Vec3Minus(cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5)), cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0])), 50, 0.4, (0, 18, 0), (0, 0), (0, 0), 500, False, False, 0, False, cl_action.GetSkillSummonCreate(skill)[0], 0, targetType = OBJ_ALLNOSELF, maxDistance = cl_math.CalDistance3D(cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0]), cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))) + 0.01, hitHeroOver = False, forceSpeed = True, innerRadius = 0.1, scale = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
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
            cls.EnableCtrl(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 160 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 12, 3, 10000, downSpeed = 3, fGravaty = 9.8, angle = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.GetCartoonEnd(skill, 5), [
                6.5,
                3,
                120], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        cl_action.SetSummonLifeTime(skill, cl_action.GetSkillSummonCreate(skill)[0], 4)
        cl_action.UnlockMonsterAttackerFace(skill)

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
        cl_action.TargetRemoveState(skill, 1047, cl_action.GetSkillVarCache(skill, 'pushhero'))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(MonsterPushHeroCartoon):
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.CalDistance3D(cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2)), cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0])) / 0.12, cl_math.Vec3MulV(cl_math.Vec3Minus(cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2)), cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0])), (1, 0, 1)), cl_math.CalDistance3D(cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2)), cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0])) if cl_math.CalDistance3D(cl_action.CrtArgSelfPos(skill), cl_action.GetSceneObjPos(skill, cl_action.GetSkillVarCache(skill, 'pushhero'))) > 2.6 else 0, attachSummon = 0, targetType = OBJ_ENEMY, lockTarget = cl_action.GetSkillVarCache(skill, 'pushhero'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon12(TimerCartoon):
    m_SID = 12
    
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
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 0)

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
        cl_action.SetSkillVarCache(skill, 'pushoverflag', cl_action.GetSkillVarCache(skill, 'pushoverflag') + 1)
        if cl_action.GetSkillVarCache(skill, 'pushoverflag') == 2:
            cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), True, 0, (0, 0, 0), parentName = '')
            if cl_math.CalDistance3D(cl_action.CrtArgSelfPos(skill), cl_action.GetCartoonEnd(skill, 5)) > 6.5:
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 44, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(MonsterPushHeroCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'pushoverflag', cl_action.GetSkillVarCache(skill, 'pushoverflag') + 1)
        if cl_action.GetSkillVarCache(skill, 'pushoverflag') == 2:
            cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), True, 0, (0, 0, 0), parentName = '')
            if cl_math.CalDistance3D(cl_action.CrtArgSelfPos(skill), cl_action.GetCartoonEnd(skill, 5)) > 6.5:
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
            else:
                cartoon = { }
                CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALLNOSELF):
            cl_action.PushVictim(skill, cl_action.GetCartoonCurPos(skill, 5), 10, 3, 10000, angle = 315)
        elif cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALLNOSELF):
            cl_action.PushHeroVictim(skill, cl_action.GetCartoonCurPos(skill, 5), 10, 3, 10000, downSpeed = 0, fGravaty = 9.8, angle = 315)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (cl_math.CalDistance3D(cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0]), cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))) + 0.3) / 0.4, cl_math.Vec3MulV(cl_math.Vec3Minus(cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5)), cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0])), (1, 0, 1)), cl_math.CalDistance3D(cl_action.GetSceneObjPos(skill, cl_action.GetSkillSummonCreate(skill)[0]), cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))) + 0.3 if cl_math.CalDistance3D(cl_action.CrtArgSelfPos(skill), cl_action.GetSceneObjPos(skill, cl_action.GetSkillVarCache(skill, 'pushhero'))) > 2.6 else 0, attachSummon = cl_action.GetSkillSummonCreate(skill)[0], targetType = OBJ_ALLNOSELF, lockTarget = cl_action.GetSkillVarCache(skill, 'pushhero'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(TimerCartoon):
    m_SID = 13
    
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
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 75, 1)

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
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(EntityParabolaCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALLNOSELF):
            cl_action.PushVictim(skill, cl_action.GetCartoonCurPos(skill, 3), 10, 3, 10000, angle = 45)
        elif cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALLNOSELF):
            cl_action.VictimAddState(skill, 1047, 0, 1, { })
            cl_action.WeaponDamage(skill, {
                'Att': 70 }, { }, sendPFMsg = False)
            cl_action.SetSkillVarCache(skill, 'pushhero', cl_action.GetCurVID(skill))
            cl_action.SummonAttachHitTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY), False, cl_action.GetSkillVarCache(skill, 'pushhero'), (0, 0.5, 0), parentName = '')
            cl_action.SetSkillVarCache(skill, 'pushoverflag', 0)
            cartoon = { }
            CCartoon13.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 70 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_math.Vec3Minus(cl_math.Vec3Add(cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 1.2, 0)), cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))), 25 + 5 * cl_action.GetPlayRound(skill), 0.4, (0, 18, 0), (0, 0), (0, 0), 75, False, True, 0, False, cl_action.GetSkillSummonCreate(skill)[0], 0, targetType = OBJ_ALLNOSELF, maxDistance = 0, hitHeroOver = True, forceSpeed = True, innerRadius = 0.1, scale = 1)

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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

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
        cl_action.LockMonsterAttackerFace(skill)
        cl_action.CreateRandomNumWarriorAtPointPos(skill, [
            cl_action.GetMonsterMuzzlePos(skill, (0, 1, -2.5))], WARRIOR_SUMMON, {
            1025: 10 }, {
            'Radius': 0.4 })
        cl_action.SetSkillVarCache(skill, 'pushhero', 0)
        cl_action.SetSkillCacheExtraTrajectory(skill, cl_action.GetSkillSummonCreate(skill)[0])
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_EXTRATRAJECTORY])
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 43, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AttackerUsePerform(skill, 21812, {
        'summoncreate': cl_action.GetSkillSummonCreate(skill)[0] if len(cl_action.GetSkillSummonCreate(skill)) > 0 else 0 }, 4)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 21811
    m_Name = '【第三幕】重型锁链兵-丢锁链'
    m_ExtPerform = ()
    m_HaltInfo = {
        198: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 500,
        'AttDistance': 20,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_UseHeight = 2
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 1050
    m_CacheAttr = [
        'DebuffProb']

