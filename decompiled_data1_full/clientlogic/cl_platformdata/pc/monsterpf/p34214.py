# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p34214.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p34214.pyc
# Source Generated with Decompyle++
# File: p34214.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateThrowCartoon, DirectPosCartoon, SceneEventCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, FIGHT3_KEY_IGNOREIMMOBILIZE, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTPOS, SKILLCACHE_PERFORMMODE, WARRIOR_MONSTER
from cl_only import PY_FLAG_EXCLUDEMONSTERHATE

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
        cl_action.CreateMonsterAtPos(skill, 24231, cl_action.GetEndPositionInCrt(skill, 5), 0, False, 'elitespider', bLineGoal = True)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(ThrowByPowerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

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
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfTopPos(skill), cl_action.CrtArgSetParabolaSpeed(skill, cartoon, cl_action.CrtArgSelfTopPos(skill), cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[i1], 9, -9, 0), 9, 1, (0, 9, 0), (1, 1), 0, False, True, 0, innerRadius = 0, pierce = 99, ignoreMonster = True, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 1, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(DirectPosCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 1003, 100, 0, {
            'MoveSpeedMul': -6500 })
        cl_action.WeaponDamage(skill, {
            'Att': 75 }, {
            'MoveSpeedMul': -6500 }, sendPFMsg = False)

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
                1.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(DirectPosCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 1003, 100, 0, {
            'MoveSpeedMul': -6500 })

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
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 8)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(DirectPosCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon12.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 6), (0, 0, 0), [
                1], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DelegateThrowCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i3, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0.1, 1.5, -2)), cl_action.CrtArgSetParabolaSpeed(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0.1, 1.5, -2)), cl_action.CrtArgShiftAngle(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0.1, 1.5, -2)), cl_action.GetSkillCustomData(skill, 'NetPos', defaultValue = [])[cl_action.GetTimerCartoonCurTimes(skill, 11)], i3 * 30 + -30, 0), 15, -15, 0) if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 2 else cl_action.CrtArgSetParabolaSpeed(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0.1, 1.5, -2)), cl_action.GetSkillCustomData(skill, 'NetPos', defaultValue = [])[cl_action.GetTimerCartoonCurTimes(skill, 11)], 15, -15, 0), 15, 2, (1, 5, 0), (0.5, 0.5), 500, True, liveTime = 0, innerRadius = 0.15, pierce = 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        cl_action.SetSkillCustomDataV3List(skill, 'NetPos', cl_action.GetSummonPosByBoxSplit(skill, 16, 4, 2, False, {
            cl_action.ToInt(skill, cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) * cl_action.GetSkillVarCache(skill, 'KillSummon') / 4 + 6) / 2 + 1): 10 }, {
            'IgnoreTargetPos': 1 }, True, iAngle = 0))

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.StartBackSwing(skill, 62)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        if cl_action.GetTimerCartoonCurTimes(skill, 11) == cl_action.ToInt(skill, cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) * cl_action.GetSkillVarCache(skill, 'KillSummon') / 4 + 6) / 2 + 1):
            cl_action.SetSkillVictim(skill, cl_action.GetRandomLivePlayer(skill, 180, bNotContainDying = True, fMaxDis = 0, bSkillVIDSecond = True, iFlag = PY_FLAG_EXCLUDEMONSTERHATE, bResetVID = True))
            cl_action.ExtendSkillCustomDataV3List(skill, 'NetPos', cl_action.GetSummonPosByBoxSplit(skill, 16, 4, 2, False, {
                cl_action.ToInt(skill, cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) * cl_action.GetSkillVarCache(skill, 'KillSummon') / 4 + 6) / 2 + 1): 10 }, {
                'IgnoreTargetPos': 1 }, True, iAngle = 0))
        if not len(cl_action.GetSkillCustomData(skill, 'NetPos', defaultValue = [])) > cl_action.GetTimerCartoonCurTimes(skill, 11):
            cl_action.SkillHaltSelf(skill)
        for i3 in range(0, 3 if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 2 else 1, 1):
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = i3)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, cl_action.ToInt(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) * cl_action.GetSkillVarCache(skill, 'KillSummon') / 4 + 6))

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(TimerCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.UnlockMonsterAttackerFace(skill)
        cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREIMMOBILIZE)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 75, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
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
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 4), (0, 0, 0), [
                1.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(ThrowByPowerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.CrtArgHitPos(skill), (0, 2, 0)), cl_action.CrtArgGetCustomDir(skill, (0, 0, 0), cl_math.Vec3Normalize(cl_math.Vec3Add(cl_math.Vec3Normalize(cl_math.Vec3Minus(cl_action.CrtArgHitPos(skill), cl_action.CrtArgSelfPos(skill))), (0, 0.25, 0))), (0, (cl_action.GetSkillVarCache(skill, 'angleIndex') - 1) * cl_action.CrtArgRandomNum(skill, 1, 10), 0), baseHorizontal = False), 25, 1, (0, 0, 0), (1, 1), 0, False, True, 0, innerRadius = 0, pierce = 99, ignoreMonster = True, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 1, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(SceneEventCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 8119, 0, 1, { })
        cl_action.SetSkillVarCache(skill, 'KillSummon', 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 8119, bSameItem = False)
        for i2 in range(0, len(cl_action.GetSkillSummonCreate(skill)), 1):
            cl_action.TargetRemoveState(skill, 33193, cl_action.GetSkillSummonCreate(skill)[i2])
        
        cartoon = { }
        CCartoon14.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.AssignWarriorDie(skill, cl_action.GetCurVID(skill))
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) >= 2:
            for i4 in range(0, 3, 2):
                cl_action.SetSkillVarCache(skill, 'angleIndex', i4)
                cl_action.AddSkillVarCache(skill, 'KillSummon', 1)
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
            
        else:
            cl_action.SetSkillVarCache(skill, 'angleIndex', 1)
            cl_action.AddSkillVarCache(skill, 'KillSummon', 1)
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.ToInt(skill, 400 / cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE)), 1, {
                'Radius': 3 }, iFightType = WARRIOR_MONSTER, iHitOver = False, funcCheckTar = cl_action.GetFuncCheckVictimCreatedBySkill(skill))

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        for i1 in range(0, len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)), 1):
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = i1)
        

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.LockMonsterAttackerFace(skill)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 68, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREIMMOBILIZE)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, cl_action.GetPerformArgValue(skill, 'Mode', iDefault = 1))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetGamePlayerCnt(skill))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_LSTPOS, cl_action.GetSummonPosByBoxSplit(skill, 28, 6, 2, True, {
        cl_action.GetRoomPlayerCnt(skill) * 2 + 8: 10 }, {
        'MinDis': 6 }, False, iAngle = 70))
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTPOS,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 34214
    m_Name = '【新二幕】精英蜘蛛怪-召唤'
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
        'ColdTime': 750,
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

