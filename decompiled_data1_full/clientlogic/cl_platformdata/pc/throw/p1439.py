# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1439.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1439.pyc
# Source Generated with Decompyle++
# File: p1439.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, LockTargetCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, WARRIOR_ELITE

class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 0), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 0), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(LockTargetCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.LionAddLockStateToTarget(skill, cl_action.GetCurVID(skill), cl_action.ToInt(skill, skill.m_Cache['AddStateTime'] * ((cl_action.GetSkillServerCache(skill, 'AddKeepTimeRatio') + 100) / 100 if cl_action.CheckHasSkillCollect(skill, 'AddKeepTimeRatio') else 1)), True, { })
        cl_action.TargetAddState(skill, 8153, cl_action.ToInt(skill, ((cl_action.GetSkillServerCache(skill, 'AddKeepTimeRatio') + 100) / 100 if cl_action.CheckHasSkillCollect(skill, 'AddKeepTimeRatio') else 1) * (skill.m_Cache['KeepTime'] / 3 if cl_action.CheckMonsterType(skill, WARRIOR_ELITE, cl_action.GetCurVID(skill)) else skill.m_Cache['KeepTime'])), 0, { }, cl_action.GetCurVID(skill))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgSelfPos(skill), (-1.2, 0, 3.3))):
                return None
            cls.EnableShow(skill, cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgSelfPos(skill), (-1.2, 0, 3.3)), cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgSelfPos(skill), (-1.2, 0, 3.3)), cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 999, 40, liveTime = 0, isLockCenter = True)
        else:
            cls.EnableCtrl(skill, cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgSelfPos(skill), (-1.2, 0, 3.3)), cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgSelfPos(skill), (-1.2, 0, 3.3)), cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 999, 40, liveTime = 0, isLockCenter = True)

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
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 16, 1)
        else:
            cls.EnableCtrl(skill, 16, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ChangeAttackerEnergy(skill, 0 - cl_action.GetAttackEnergy(skill) if cl_action.GetPerformArgValue(skill, 'CostAllEnergy', iDefault = 0) == 1 else -12000, iReason = 5)
    cl_action.SendUseThrowPFMsg(skill)
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.throw import CEnergyPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1439
    m_Name = '#NT#强化锁云诀'
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
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 60000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 3,
        'BulletVerticalAcc': 150,
        'AddStateTime': 600,
        'KeepTime': 600,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 12000 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 2000

