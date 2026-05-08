# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p33812.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p33812.pyc
# Source Generated with Decompyle++
# File: p33812.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import MonsterDashCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, STATE_EFF_DEBAR

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
        cl_action.AttackerUsePerform(skill, 33813, { }, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 6)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(MonsterDashCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7130)
        cl_action.UnlockMonsterAttackerFace(skill)
        cl_action.MonsterFaceTarget(skill, cl_action.GetSkillVID(skill), 20, 1)
        cl_action.AttackerAddState(skill, 7125, 40, 0, { })

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
            cls.EnableCtrl(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 96, 25, 20, True, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 16, StopDis = 0.4, CheckHalt = True)

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
        cl_action.AttackerUsePerform(skill, 33813, { }, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 6)

    InitSuccess = classmethod(InitSuccess)


class CCartoon12(MonsterDashCartoon):
    m_SID = 12
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon13.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7130)
        cl_action.UnlockMonsterAttackerFace(skill)
        cl_action.MonsterFaceTarget(skill, cl_action.GetSkillVID(skill), 20, 1)
        cl_action.AttackerAddState(skill, 7125, 40, 0, { })

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
            cls.EnableCtrl(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 96, 25, 20, True, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 16, StopDis = 0.4, CheckHalt = True)

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
        cl_action.AttackerUsePerform(skill, 33813, { }, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(MonsterDashCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7130)

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
            cls.EnableCtrl(skill, cl_action.CrtArgTargetPos(skill, notContainDying = False), 28, 25, 20, True, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 16, StopDis = 0.4, CheckHalt = True)

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
        cl_action.AttackerUsePerform(skill, 33813, { }, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(MonsterDashCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon9.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7130)

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
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_action.CrtArgGetCustomDir(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillVarCache(skill, 'end'), (0, 0, 0)), 35, 0), 28, 25, 20, True, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 16, StopDis = 0.2, CheckHalt = True)

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
        cl_action.AttackerUsePerform(skill, 33813, { }, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon15(MonsterDashCartoon):
    m_SID = 15
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7130)
        cl_action.StartBackSwing(skill, 52)

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
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_action.CrtArgGetCustomDir(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillVarCache(skill, 'end'), (0, 0, 0)), 35, 0), 28, 25, 12, True, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False)

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
        cl_action.AttackerUsePerform(skill, 33813, { }, 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 16, 2)

    InitSuccess = classmethod(InitSuccess)


class CCartoon18(MonsterDashCartoon):
    m_SID = 18
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon17.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 7130)
        cl_action.UnlockMonsterAttackerFace(skill)
        cl_action.RemoveIgnoreStateEffect(skill, STATE_EFF_DEBAR)
        cl_action.AttackerRemoveState(skill, 7124)
        cl_action.StartBackSwing(skill, 52)

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
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_action.CrtArgGetCustomDir(skill, cl_action.GetSkillVarCache(skill, 'start'), cl_action.GetSkillVarCache(skill, 'end'), (0, 0, 0)), 35, 0), 28, 25, 4, True, False, False, checkDis = 0, start = cl_action.CrtArgSelfPos(skill), offSetY = 0, staticbreak = False, CheckTime = 0, StopDis = 0, CheckHalt = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon16(TimerCartoon):
    m_SID = 16
    
    def Active(cls, skill):
        cl_action.LockMonsterAttackerFace(skill)
        cl_action.AttackerAddState(skill, 7130, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon15.Init(skill, cartoon, casting = 1, index = 0)

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
        cl_action.AttackerAddState(skill, 7130, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon18.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 32, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon10(TimerCartoon):
    m_SID = 10
    
    def Active(cls, skill):
        cl_action.LockMonsterAttackerFace(skill)
        cl_action.AttackerAddState(skill, 7130, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon16.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 32, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(TimerCartoon):
    m_SID = 14
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'end', cl_action.CrtArgTargetPos(skill, notContainDying = False))
        cl_action.SetSkillVarCache(skill, 'start', cl_action.CrtArgSelfPos(skill))
        cl_action.LockMonsterAttackerFace(skill)
        cl_action.AttackerAddState(skill, 7130, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 32, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.LockMonsterAttackerFace(skill)
        cl_action.AttackerAddState(skill, 7130, 0, 1, {
            'Cache': 1 })
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
        CCartoon14.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 128, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.LockMonsterAttackerFace(skill)
        cl_action.AttackerAddState(skill, 7130, 0, 1, {
            'Cache': 1 })
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 128, 1)

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
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AttackerAddState(skill, 7124, 0, 0, { })
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.AttackerAddState(skill, 7126, 40, 0, { })
    cl_action.AttackerRemoveState(skill, 7124)
    cl_action.StartBackSwing(skill, 52)


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_FIRE, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 33812
    m_Name = '精英骑乘怪-燃烧路径'
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
        'AttDistance': 25,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

