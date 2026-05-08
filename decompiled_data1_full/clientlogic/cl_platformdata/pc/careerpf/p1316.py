# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1316.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1316.pyc
# Source Generated with Decompyle++
# File: p1316.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, DirectPosCartoon, RayCastingPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_RECTANGLE, ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_PERFORMMODE

class CCartoon22(TimerCartoon):
    m_SID = 22
    
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon22.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.StartAttackEnergyRecover(skill, 'pf1316')
        cl_action.AttackerRemoveState(skill, 32661, bSameItem = False)
        cl_action.DelAttackPerformCoverCD(skill, 1316)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 40 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 7, 1)
        else:
            cls.EnableCtrl(skill, 40 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 7, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 90 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 15, 1)
        else:
            cls.EnableCtrl(skill, 90 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 15, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 140 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 23, 1)
        else:
            cls.EnableCtrl(skill, 140 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 23, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon21(TimerCartoon):
    m_SID = 21
    
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 16, 1)
        else:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon20(TimerCartoon):
    m_SID = 20
    
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
        CCartoon21.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon19(RayCastingPosCartoon):
    m_SID = 19
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon20.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 1 * ((cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 19), cl_action.GetCartoonCurPos(skill, 19)) * 0.02 if cl_action.GetTalentLevel(skill, 3113) == 3 else 0) + 1)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 1))):
                return None
            cls.EnableShow(skill, 99, 50, 30, 0, [
                3,
                2.7,
                4], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, liveTime = 0)
        else:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 1)), cl_action.GetSceneCenterPosition(skill, cartoon), 99, 50, 30, 0, [
                3,
                2.7,
                4], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, liveTime = 0)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 16, 1)
        else:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon18(TimerCartoon):
    m_SID = 18
    
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
        CCartoon17.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon16(RayCastingPosCartoon):
    m_SID = 16
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon18.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 2 * ((cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 16), cl_action.GetCartoonCurPos(skill, 16)) * 0.02 if cl_action.GetTalentLevel(skill, 3113) == 3 else 0) + 1)) })
            if cl_action.CheckHasTalent(skill, 3115):
                cl_action.PerformDamage(skill, {
                    'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 2 * ((cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 16), cl_action.GetCartoonCurPos(skill, 16)) * 0.02 if cl_action.GetTalentLevel(skill, 3113) == 3 else 0) + 1) * (cl_action.GetTalentLevel(skill, 3115) * 0.25 + 0.25)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 1))):
                return None
            cls.EnableShow(skill, 99, 50, 30, 0, [
                3,
                5.4,
                4], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, liveTime = 0)
        else:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 1)), cl_action.GetSceneCenterPosition(skill, cartoon), 99, 50, 30, 0, [
                3,
                5.4,
                4], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, liveTime = 0)

    InitSuccess = classmethod(InitSuccess)


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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 18, 14)
        else:
            cls.EnableCtrl(skill, 18, 14)

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
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 3 * ((cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetCartoonCurPos(skill, 3)) * 0.02 if cl_action.GetTalentLevel(skill, 3113) == 3 else 0) + 1) * 0.25) }, dArgs = {
            'AIDamFactor': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetStartPositionInCrt(skill, 11), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetStartPositionInCrt(skill, 11), (0, 0, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        CCartoon13.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 5)
        else:
            cls.EnableCtrl(skill, 50, 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(DirectPosCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon12.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 3 * ((cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetCartoonCurPos(skill, 3)) * 0.02 if cl_action.GetTalentLevel(skill, 3113) == 3 else 0) + 1) * 0.25) }, dArgs = {
            'AIDamFactor': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.CrtArgTargetPosGroudPos(skill, cl_action.GetSkillVarCache(skill, 'bulletpos')), (0, 0.4, 0)), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.CrtArgTargetPosGroudPos(skill, cl_action.GetSkillVarCache(skill, 'bulletpos')), (0, 0.4, 0)), (0, 0, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(TimerCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

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
        if not cl_action.CheckHasSkillVarCache(skill, 'bulletpos') or cl_math.CalDistance3D(cl_action.GetSkillVarCache(skill, 'bulletpos'), cl_action.StartAndEndAtSameHeight(skill, cl_action.GetSkillVarCache(skill, 'bulletpos'), cl_action.GetEndPositionInCrt(skill, 3))) > 3:
            cl_action.SetSkillVarCache(skill, 'bulletpos', cl_action.GetEndPositionInCrt(skill, 3))
            cartoon = { }
            CCartoon11.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, 10)
        else:
            cls.EnableCtrl(skill, 10, 10)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 16, 1)
        else:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        if cl_action.GetTalentLevel(skill, 3115) == 3 and cl_action.GetSkillVarCache(skill, 'UseEnergy') >= 6000:
            cl_action.SetSkillVarCache(skill, 'forward', cl_action.CrtArgSelfFace(skill))
            cartoon = { }
            CCartoon14.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(RayCastingPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 3 * ((cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetCartoonCurPos(skill, 3)) * 0.02 if cl_action.GetTalentLevel(skill, 3113) == 3 else 0) + 1)) })
            if cl_action.CheckHasTalent(skill, 3115):
                cl_action.PerformDamage(skill, {
                    'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 3 * ((cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetCartoonCurPos(skill, 3)) * 0.02 if cl_action.GetTalentLevel(skill, 3113) == 3 else 0) + 1) * (cl_action.GetTalentLevel(skill, 3115) * 0.25 + 0.25)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 1))):
                return None
            cls.EnableShow(skill, 99, 50, 30, 0, [
                3,
                8.1,
                4], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, liveTime = 0.1)
        else:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0, 1)), cl_action.GetSceneCenterPosition(skill, cartoon), 99, 50, 30, 0, [
                3,
                8.1,
                4], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, liveTime = 0.1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'EnergyCost', cl_action.GetSkillVarCache(skill, 'UseEnergy'))
        cl_action.AttackerRemoveState(skill, 32661, bSameItem = False)
        cl_action.ChangeAttackerEnergy(skill, cl_action.GetSkillVarCache(skill, 'UseEnergy') * -1, iReason = 3)
        cl_action.StartAttackEnergyRecover(skill, 'pf1316')
        if (cl_action.GetSkillVarCache(skill, 'UseEnergy') if cl_action.IsHeroCtrl(skill) else cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 3000:
            cartoon = { }
            CCartoon19.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetTalentLevel(skill, 3115) < 2 or (cl_action.GetSkillVarCache(skill, 'UseEnergy') if cl_action.IsHeroCtrl(skill) else cl_action.GetSkillCacheData(skill, SKILLCACHE_INT)) < 6000:
            cartoon = { }
            CCartoon16.Init(skill, cartoon, casting = 0, index = 0)
        else:
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 8, 1)
        else:
            cls.EnableCtrl(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ChargeCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillVarCache(skill, 'IsCharge', 0)
        cl_action.AttackerRemoveState(skill, 32682, bSameItem = False)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
        cl_action.SendUseCareerPFMsg(skill)
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSkillCustomData(skill, 'AIEnergy', defaultValue = 0)(cl_action.ToInt, skill if cl_action.GetSkillCustomData(skill, 'UseByAI', defaultValue = 0) == 1 else cl_action.GetSkillVarCache(skill, 'MaxChargeEnergy') if cl_action.GetSkillVarCache(skill, 'MaxChargeEnergy') < cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 80 + 240) * (cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100)) * cl_action.GetCartoonChargeLevel(skill, 0) + 0 else cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 80 + 240) * (cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100)) * cl_action.GetCartoonChargeLevel(skill, 0) + 0))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])
        cl_action.SetSkillVarCache(skill, 'UseEnergy', cl_action.GetSkillCustomData(skill, 'AIEnergy', defaultValue = 0)(cl_action.ToInt, skill if cl_action.GetSkillCustomData(skill, 'UseByAI', defaultValue = 0) == 1 else cl_action.GetSkillVarCache(skill, 'MaxChargeEnergy') if cl_action.GetSkillVarCache(skill, 'MaxChargeEnergy') < cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 80 + 240) * (cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100)) * cl_action.GetCartoonChargeLevel(skill, 0) + 0 else cl_action.ToInt(skill, (cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 80 + 240) * (cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100)) * cl_action.GetCartoonChargeLevel(skill, 0) + 0))
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetSkillCustomData(skill, 'AIIntervalTime', defaultValue = 4) if cl_action.GetSkillCustomData(skill, 'UseByAI', defaultValue = 0) == 1 else 4, cl_action.GetSkillCustomData(skill, 'AIMaxChargeLevel', defaultValue = 0) if cl_action.GetSkillCustomData(skill, 'UseByAI', defaultValue = 0) == 1 else cl_action.GetSkillVarCache(skill, 'MaxChargeEnergy') / 240 + 1, 0, False, True, halfEnd = False, offsetTime = 0, breaktips = True, allowMaxChargeLowAmmo = False)
        elif cl_action.GetSkillCustomData(skill, 'UseByAI', defaultValue = 0) == 1:
            pass
        
        skill(cl_action.GetSkillCustomData(skill, 'AIIntervalTime', defaultValue = 4), 4, cl_action.GetSkillCustomData(skill, 'AIMaxChargeLevel', defaultValue = 0) if cl_action.GetSkillCustomData(skill, 'UseByAI', defaultValue = 0) == 1 else cl_action.GetSkillVarCache(skill, 'MaxChargeEnergy') / 240 + 1, 0, False, True, halfEnd = False, offsetTime = 0, breaktips = True, scanAngle = 0, scanDistance = 0, maxScanNum = 0, prepareTime = 0, hasLv0 = False, allowMaxChargeLowAmmo = False, minLevel = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        if cl_action.IsHeroCtrl(skill):
            if cl_action.GetAttackEnergy(skill) < 3000:
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
            elif cl_action.GetAttackEnergy(skill) >= 6000 and cl_action.GetTalentLevel(skill, 3115) >= 2:
                cartoon = { }
                CCartoon4.Init(skill, cartoon, casting = 0, index = 0)
            else:
                cartoon = { }
                CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        cl_action.SetSkillVarCache(skill, 'MaxChargeEnergy', cl_action.GetAttackEnergy(skill) - cl_action.GetAttackEnergy(skill) % 3000 if cl_action.GetTalentLevel(skill, 3114) == 3 else cl_action.GetAttackEnergy(skill) - cl_action.GetAttackEnergy(skill) % 3000 if cl_action.GetAttackEnergy(skill) - cl_action.GetAttackEnergy(skill) % 3000 < 6000 else 6000)
        cl_action.AttackerAddState(skill, 32682, 0, 1, { })
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 8, 1)
        else:
            cls.EnableCtrl(skill, 50 - cl_action.GetSkillVarCache(skill, 'ChargeSpeed') * 8, 1)

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
        cl_action.AttackerAddState(skill, 32661, 0, 1, { })
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 0 and cl_action.CheckHasBenediction(skill, 13534):
            cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
            cl_action.SendUseCareerPFMsg(skill)
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.SetSkillVarCache(skill, 'IsCharge', 1)
            cartoon = { }
            CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)
        else:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_PERFORMMODE)
    cl_action.SetSkillVarCache(skill, 'ChargeSpeed', cl_action.ToInt(skill, cl_action.GetAttackerStateCount(skill, 32705, dState = { }) / 1200))
    cl_action.StopAttackEnergyRecover(skill, 'pf1316', 0)
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.StartAttackEnergyRecover(skill, 'pf1316')
    cl_action.AttackerRemoveState(skill, 32661, bSameItem = False)
    cl_action.DelAttackPerformCoverCD(skill, 1316)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1316
    m_Name = '炽炎有灵'
    m_ExtPerform = (1318,)
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
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 35000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3300,
        'ExplodeDelay': 0,
        'Radius': 3,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 2000
    
    def UsePerform(self, oWarrior, oSkill):
        if oSkill.m_CheckType == CRT_CHECK_SERVER:
            cl_action.SetSkillCacheData(oSkill, SKILLCACHE_PERFORMMODE, 1)
            oSkill.m_Custom['UseByAI'] = 1
            oSkill.m_Custom['AIIntervalTime'] = 160
            oSkill.m_Custom['AIMaxChargeLevel'] = 1
            if cl_action.CheckHasTalent(oSkill, 3115):
                oSkill.m_Custom['AIEnergy'] = 6000
            else:
                oSkill.m_Custom['AIEnergy'] = 3000
        super().UsePerform(oWarrior, oSkill)


