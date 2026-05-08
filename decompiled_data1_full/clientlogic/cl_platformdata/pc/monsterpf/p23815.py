# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p23815.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p23815.pyc
# Source Generated with Decompyle++
# File: p23815.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import MonsterDashCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, OBJ_ALL, STATE_EFF_DEBAR

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 90, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon13(MonsterDashCartoon):
    m_SID = 13
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 7112, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, cl_action.CrtArgCustomPos(skill, cartoon), 12, 0, 20, True, False, True, checkDis = 1, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(MonsterDashCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 180)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7112, bSameItem = False)
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)
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
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 12, 0, 2, True, False, True, checkDis = 1, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

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
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(MonsterDashCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 180)

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
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 12, 0, 5, True, False, True, checkDis = 1, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(TimerCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon10.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(MonsterDashCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 180)

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
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 12, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 12, 0, 10, True, False, True, checkDis = 1, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(TimerCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(MonsterDashCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.MonsterAttackerFacePos(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 16, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 180)

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
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterTurnDirPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 16, 120 if cl_action.CountDistance3D(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgTargetPos(skill, notContainDying = False)) >= 7 else 10, 20), 12, 0, 20, True, False, True, checkDis = 1, start = (0, 0, 0), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False, targettype = OBJ_ALL, Collision = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon13.Init(skill, cartoon, casting = 1, index = 0)

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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 5)

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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetCustomPos(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False))
        cartoon = { }
        CCartoon12.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 60, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


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
    m_SID = 23815
    m_Name = '骑乘怪-坐骑冲撞'
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
        'ColdTime': 1200,
        'AttDistance': 15,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 1038
    m_CacheAttr = [
        'DebuffProb']

