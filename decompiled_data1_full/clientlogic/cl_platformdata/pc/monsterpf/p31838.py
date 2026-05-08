# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p31838.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p31838.pyc
# Source Generated with Decompyle++
# File: p31838.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, MonsterDashCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_RECTANGLE, ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, OBJ_ALL, OBJ_ENEMY, STATE_EFF_DEBAR

class CCartoon7(MonsterDashCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 720)

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
            cls.EnableCtrl(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 0, 13, True, False, False, checkDis = 0, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AttackerRemoveState(skill, 7051, bSameItem = False)
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
        cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)
        cl_action.UnlockMonsterAttackerFace(skill)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 200 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 10, 5, 10000, downSpeed = 5, fGravaty = 9.8, angle = 0, bDirectRotation = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 0.1, -2)), cl_action.CrtArgSelfPos(skill), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7051, bSameItem = False)
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
        cl_action.RemoveLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 200 }, { }, sendPFMsg = False)
        cl_action.PushHeroVictim(skill, (0, 0, 0), 10, 5, 10000, downSpeed = 5, fGravaty = 9.8, angle = 0, bDirectRotation = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 0, 0)), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 0, 0)), cl_action.GetAttackerFacing(skill), 1, 0), [
                8,
                3,
                3], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon12(TimerCartoon):
    m_SID = 12
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


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
        cartoon = { }
        CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 36, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(MonsterDashCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 150 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 5 else 10, 30), 720)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 150 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 5 else 10, 30), 12, 0, 13, True, False, False, checkDis = 0, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(MonsterDashCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 150 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 5 else 10, 30), 720)

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
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 150 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 5 else 10, 30), 12, 0, 13, True, False, False, checkDis = 0, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(TimerCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

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
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 7)

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
        cl_action.AttackerAddState(skill, 7051, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 80, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 31838
    m_Name = '【新三幕】精英蟹先锋-近身追击-转阶段'
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
        'ColdTime': 400,
        'AttDistance': 8,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

