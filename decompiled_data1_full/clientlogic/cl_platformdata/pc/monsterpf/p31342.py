# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p31342.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p31342.pyc
# Source Generated with Decompyle++
# File: p31342.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import MonsterDashCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, OBJ_ALL, SKILLCACHE_INT, SKILLCACHE_POS, STATE_EFF_CONTROL

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
        cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

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
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 10, 3, cl_math.Vec3MulV(cl_action.CrtArgSelfFace(skill), (-1, -1, -1)), iCartoonSID = -1, bKnockBack = False)
        cl_action.ChangeAttackerArmor(skill, (cl_action.ToInt(skill, cl_action.GetAttackerAttr(skill, 'ArmorMax') * 0.1) if cl_action.GetAttackerAttr(skill, 'Armor') > cl_action.ToInt(skill, cl_action.GetAttackerAttr(skill, 'ArmorMax') * 0.1) else cl_action.GetAttackerAttr(skill, 'Armor')) * -1)
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, 1 if cl_action.GetAttackerAttr(skill, 'Armor') > 0 else 0)
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])
        cl_action.AttackerAddState(skill, 7162, 680, 0, {
            'KeepTime': cl_action.GetPerformArgValue(skill, 'BackSwingTime', iDefault = 640) + 200 })

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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) > 0:
            cl_action.UnlockMonsterAttackerFace(skill)
            cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetWarriorLockEnemy(skill, cl_action.GetSkillAID(skill))), 50)
            cartoon = { }
            CCartoon13.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetPerformArgValue(skill, 'BackSwingTime', iDefault = 640) + 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(MonsterDashCartoon):
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
        cl_action.SetSkillVarCache(skill, 'hitstatic', 1)
        cl_action.SetCurVictim(skill, cl_action.GetSkillAID(skill))
        cl_action.AttackerRemoveState(skill, 7161, bSameItem = False)
        cl_action.AttackerAddState(skill, 7164, cl_action.GetPerformArgValue(skill, 'BackSwingTime', iDefault = 640), 0, { })
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), 64, 0, 5, True, False, False, checkDis = 1, start = (0, 0, 0), offSetY = 2, staticbreak = True, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False, BulletHeightScale = 0.45, BulletRadiusScale = 0.7)

    InitSuccess = classmethod(InitSuccess)


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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.AttackerRemoveState(skill, 7161, bSameItem = False)
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_CONTROL)
        cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
        cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(MonsterDashCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, (0, 0, 0), 16, 20, 5, True, False, False, checkDis = 1, start = (0, 0, 0), offSetY = 2, staticbreak = True, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False, BulletHeightScale = 0.45, BulletRadiusScale = 0.7)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(MonsterDashCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'subspeedend', 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'subspeedend') == 1:
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSkillVarCache(skill, 'subspeedend', 1)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), 26, 44, 15, True, False, False, checkDis = 1, start = (0, 0, 0), offSetY = 2, staticbreak = True, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False, BulletHeightScale = 0.45, BulletRadiusScale = 0.7)

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
        if cl_action.GetSkillVarCache(skill, 'hitstatic') == 0:
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 72, 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(MonsterDashCartoon):
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
        cl_action.SetSkillVarCache(skill, 'hitstatic', 1)
        cl_action.SetCurVictim(skill, cl_action.GetSkillAID(skill))
        cl_action.AttackerRemoveState(skill, 7161, bSameItem = False)
        cl_action.AttackerAddState(skill, 7164, cl_action.GetPerformArgValue(skill, 'BackSwingTime', iDefault = 640), 0, { })
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), 52, 50, 15 + cl_action.GetTimerCartoonCurTimes(skill, 0) * 5, True, False, False, checkDis = 1, start = (0, 0, 0), offSetY = 2, staticbreak = True, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False, BulletHeightScale = 0.45, BulletRadiusScale = 0.7)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'hitstatic') == 0:
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 68, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        if cl_action.GetBallisticType(skill) != 2:
            cl_action.LockMonsterAttackerFace(skill)
            cl_action.SetCustomPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False))

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
        cl_action.AttackerAddState(skill, 7161, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 20, 1)

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
        cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.CrtArgSkillEndPos(skill))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_POS])
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 88, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'hitstatic', 0)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddIgnoreStateEffect(skill, STATE_EFF_CONTROL)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AttackerRemoveState(skill, 7161, bSameItem = False)
    cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_CONTROL)
    cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE
from cl_newformula import Func221

class CPerform(CCustomPerform):
    m_SID = 31342
    m_Name = '【新一幕】精英冲锋兵-冲锋突击'
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
        'ColdTime': 300,
        'AttDistance': 20,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_BaseArgData = {
        'BackSwingTime': (lambda *a: 450 - (min(1, int(Func221(*a))) + Func221(*a) // 9) * 150) }
    m_CacheAttr = [
        'DebuffProb']

