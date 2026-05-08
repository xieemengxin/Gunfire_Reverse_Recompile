# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1335.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1335.pyc
# Source Generated with Decompyle++
# File: p1335.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, FIGHT3_KEY_IGNOREKNOCKBACK, OBJ_ENEMY, WARRIOR_NORMAL

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
        cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)
        else:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * (cl_action.GetPerformArgValue(skill, 'PowerEndMul', iDefault = 1) if cl_action.GetSkillServerCache(skill, 'TotalCost') >= cl_action.GetPerformArgValue(skill, 'PowerCost', iDefault = 6000) else cl_action.GetPerformArgValue(skill, 'EndMul', iDefault = 1)) })
        cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 40, 2, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.GetSceneCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                8,
                4,
                120,
                0], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.GetSceneCenterPosition(skill, cartoon), [
                8,
                4,
                120,
                0], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

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
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

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
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * cl_action.GetPerformArgValue(skill, 'NormalMul', iDefault = 1) })
        if cl_action.CheckMonsterType(skill, WARRIOR_NORMAL, cl_action.GetCurVID(skill)):
            cl_action.PushMoveVictim(skill, cl_action.CrtArgSelfCenterPos(skill), 10, 0.5, (0, 0, 0), iCartoonSID = -1, bKnockBack = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.GetSceneCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                5,
                3,
                60,
                0], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.GetSceneCenterPosition(skill, cartoon), [
                5,
                3,
                60,
                0], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

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
        cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)
        else:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(DirectPosCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] * (cl_action.GetPerformArgValue(skill, 'PowerEndMul', iDefault = 1) if cl_action.GetSkillServerCache(skill, 'TotalCost') >= cl_action.GetPerformArgValue(skill, 'PowerCost', iDefault = 6000) else cl_action.GetPerformArgValue(skill, 'EndMul', iDefault = 1)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = cl_action.GetSceneCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                5,
                3,
                60,
                0], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.GetSceneCenterPosition(skill, cartoon), [
                5,
                3,
                60,
                0], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

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
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 42, 1)
        else:
            cls.EnableCtrl(skill, 42, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(TimerCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetTimerCartoonCurTimes(skill, 7) > 0:
            cl_action.SetSkillServerCache(skill, 'TotalCost', cl_action.GetPerformArgValue(skill, 'EnergyCost', iDefault = 1) * cl_action.GetTimerCartoonCurTimes(skill, 7))
            cl_action.SetSkillServerCache(skill, 'EndPF1335', 1)
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
        if cl_action.GetSkillVarCache(skill, 'SkillHalt') == 0:
            if cl_action.GetAttackEnergy(skill) > 0:
                cl_action.ChangeAttackerEnergy(skill, 0 - cl_action.GetPerformArgValue(skill, 'EnergyCost', iDefault = 1), iReason = 0)
                cl_action.AddAttackerStateCount(skill, 33759, cl_action.GetPerformArgValue(skill, 'EnergyCost', iDefault = 1) / 100, iTime = 0)
                cartoon = { }
                CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
            else:
                cl_action.SetSkillVarCache(skill, 'SkillHalt', 1)
                cl_action.SetSkillServerCache(skill, 'TotalCost', cl_action.GetPerformArgValue(skill, 'EnergyCost', iDefault = 1) * (cl_action.GetTimerCartoonCurTimes(skill, 7) - 1))
                cl_action.SetSkillServerCache(skill, 'EndPF1335', 1)
                cartoon = { }
                CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetSkillVarCache(skill, 'WaitTime'), 1000)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'WaitTime'), 1000)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(TimerCartoon):
    m_SID = 8
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'SkillHalt', 0)
        cl_action.SetSkillVarCache(skill, 'WaitTime', cl_action.ToInt(skill, 30 * ((100 - skill.m_Cache['ExplodeDelay']) / 100)))
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 4, 1)
        else:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyStateTransDamFactor(skill, 33604)
    cartoon = { }
    CCartoon8.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPFEnergyPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1335
    m_Name = '#NT#连续拳（废弃）'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 4,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 30000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 100 }
    m_ForbidRule = 0
    m_CheckForbid = 1013
    m_AIPerformDam = 1000
    
    def Enable(self, oWarrior, iNotify = 0):
        if not oWarrior.m_TalentCon:
            return None
        if ENABLE_TALENT not in oWarrior.m_TalentCon.m_Perform:
            return None
        super().Enable(oWarrior, iNotify = 1)


ENABLE_TALENT = 3709
