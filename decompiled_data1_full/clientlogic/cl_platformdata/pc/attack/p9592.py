# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9592.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9592.pyc
# Source Generated with Decompyle++
# File: p9592.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, QTECartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, BRIGHTEN_DAMAGE, CRT_CHECK_SERVER, CRT_EXTCHECK_LASERWEAPON, MONSTER_PART_SHIELD, MONSTER_PART_UNTAGGED, MONSTER_PART_WEAKNESS, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT

class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'curTarget', cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCartoonLoopID(skill, 7))))
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVarCache(skill, 'curTarget'))
        if cl_action.GetSkillVarCache(skill, 'curTarget') == cl_action.GetSkillServerCache(skill, 'HitWeaknessTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)
        else:
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)

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
        cl_action.SetSkillVarCache(skill, 'curTarget', cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCartoonLoopID(skill, 7))))
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVarCache(skill, 'curTarget'))
        if cl_action.GetSkillVarCache(skill, 'curTarget') == cl_action.GetSkillServerCache(skill, 'HitWeaknessTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)
        else:
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, cl_action.ToInt(skill, (skill.m_Cache['MultipleExplodeCnt'] + 1) * 3 - 1))

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(TimerCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'curTarget', cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCartoonLoopID(skill, 8))))
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVarCache(skill, 'curTarget'))
        if cl_action.GetSkillVarCache(skill, 'curTarget') == cl_action.GetSkillServerCache(skill, 'HitWeaknessTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)
        else:
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)

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
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'curTarget', cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCartoonLoopID(skill, 8))))
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVarCache(skill, 'curTarget'))
        if cl_action.GetSkillVarCache(skill, 'curTarget') == cl_action.GetSkillServerCache(skill, 'HitWeaknessTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)
        else:
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)

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
        cl_action.SetSkillVarCache(skill, 'curTarget', cl_action.GetSkillVarCache(skill, cl_action.IntToString(skill, cl_action.GetCartoonLoopID(skill, 8))))
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVarCache(skill, 'curTarget'))
        if cl_action.GetSkillVarCache(skill, 'curTarget') == cl_action.GetSkillServerCache(skill, 'HitWeaknessTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)
        else:
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillVarCache(skill, 'curTarget')))
            cl_action.WeaponDamage(skill, {
                'Att': 60 if cl_action.CheckHasInscription(skill, 13128) else 100 }, { }, sendPFMsg = True)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, skill.m_Cache['MultipleExplodeCnt'])

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
        for i1 in range(cl_action.ToInt(skill, cl_action.GetTimerCartoonCurTimes(skill, 6) - 1), len(cl_action.GetSkillVarCache(skill, 'HitTarget')) if cl_action.GetTimerCartoonCurTimes(skill, 6) >= cl_action.GetSkillVarCache(skill, 'LoopTimes') else cl_action.GetTimerCartoonCurTimes(skill, 6), 1):
            if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVarCache(skill, 'HitTarget')[i1]):
                cl_action.SetSkillVarCache(skill, cl_action.IntToString(skill, i1), cl_action.GetSkillVarCache(skill, 'HitTarget')[i1])
                if cl_action.CheckHasInscription(skill, 13128):
                    cartoon = { }
                    CCartoon7.Init(skill, cartoon, casting = 0, index = i1)
                    continue
                if skill.m_Cache['MultipleExplodeCnt'] == 0:
                    cartoon = { }
                    CCartoon8.Init(skill, cartoon, casting = 0, index = i1)
                    continue
                cartoon = { }
                CCartoon2.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, cl_action.GetSkillVarCache(skill, 'LoopTimes'))

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(QTECartoon):
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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')
        if cl_action.CheckHasInscription(skill, 13069):
            cl_action.AddAttackerStateCount(skill, 1857, 1, iTime = 0, bFromAttack = False, bFromWeapon = False)
            if cl_action.CheckHasSkillVarCache(skill, 'HitTarget'):
                cl_action.SetSkillVarCache(skill, 'LoopTimes', cl_action.ToInt(skill, min(10, len(cl_action.GetSkillVarCache(skill, 'HitTarget')))))
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
            elif cl_action.CheckHasSkillVarCache(skill, 'HitTarget'):
                cl_action.SetSkillVarCache(skill, 'LoopTimes', cl_action.ToInt(skill, min(10, len(cl_action.GetSkillVarCache(skill, 'HitTarget')))))
                cartoon = { }
                CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0], cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[1], cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[2])

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.SetSkillServerCache(skill, 'HitWeaknessTarget', cl_action.GetCurVID(skill) if cl_action.CheckHitWeakness(skill) else 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PushVictim(skill, cl_action.GetEndPositionInCrt(skill, 4), 20, 5, 8000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0, iFace2Dir = False)
        if cl_action.GetCurVID(skill) == cl_action.GetSkillServerCache(skill, 'HitWeaknessTarget'):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
            if not cl_action.CheckHasSkillVarCache(skill, 'HitTarget') or cl_action.CheckNumberinList(skill, cl_action.GetCurVID(skill), cl_action.GetSkillVarCache(skill, 'HitTarget')):
                cl_action.AddSkillVarCacheList(skill, 'HitTarget', cl_action.GetCurVID(skill))
            else:
                cl_action.AddSkillVarCacheList(skill, 'HitTarget', cl_action.GetCurVID(skill))
        else:
            cl_action.WeaponDamage(skill, {
                'Att': 100 }, { }, sendPFMsg = True)
            if not cl_action.CheckHasSkillVarCache(skill, 'HitTarget') or cl_action.CheckNumberinList(skill, cl_action.GetCurVID(skill), cl_action.GetSkillVarCache(skill, 'HitTarget')):
                cl_action.AddSkillVarCacheList(skill, 'HitTarget', cl_action.GetCurVID(skill))
            else:
                cl_action.AddSkillVarCacheList(skill, 'HitTarget', cl_action.GetCurVID(skill))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgHitPos(skill) if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) <= 1 else cl_action.GetTargetCenterPos(skill, cl_action.GetCartoonHitTargetInOrder(skill, 5)), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(RayCastCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_SHIELD):
            cl_action.SetSkillServerCache(skill, 'ExShowTips', [
                BRIGHTEN_DAMAGE][0])
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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, 1, cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, radius = 0.8, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_LASERWEAPON)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'EnergyBarNum', skill.m_Cache['EnergyBar'])
    cl_action.SetSkillVarCache(skill, 'EnergyBar', -1)
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    cl_action.UpdateSkillWeaponSpecialAttr(skill, 'EnergyBar', cl_action.GetSkillVarCache(skill, 'EnergyBar'))


def End(skill):
    cl_action.UpdateSkillWeaponSpecialAttr(skill, 'EnergyBar', 0 if cl_action.CheckHasState(skill, 32004) and cl_action.GetSkillServerCache(skill, 'PerformMode') == 0 else cl_action.GetSkillVarCache(skill, 'EnergyBar'))
    if not cl_action.CheckHasInscription(skill, 13069) and cl_action.GetSkillVarCache(skill, 'EnergyBar') == 1:
        cl_action.SetAttackerStateCount(skill, 1857, 0)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform
from cl_commondefines import DPSUBMSG_DEFAULT

class CPerform(CCustomPerform):
    m_SID = 9592
    m_Name = '#NT#龙息QTE'
    m_ExtPerform = (4378,)
    m_HaltInfo = {
        40108: 1,
        10149: 1,
        20149: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 30,
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_DPSubMsg = DPSUBMSG_DEFAULT
    m_ClassifyTag = ()
    m_BulletUse = 1
    m_IsMinor = 1
    m_ForbidRule = 1086
    m_CheckForbid = 1028

