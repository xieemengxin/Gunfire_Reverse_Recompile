# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1419.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1419.pyc
# Source Generated with Decompyle++
# File: p1419.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.CheckSightCentrePosDis(skill, cl_action.GetStartPositionInCrt(skill, 2), 20)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = { })
        cl_action.UseExtraThrowPerform(skill, {
            'DirectPos': 1,
            'vEnd': cl_action.GetStartPositionInCrt(skill, 2) }, 30, 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 32500, skill.m_Cache['AddStateTime'], 0, { })
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'raypos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'raypos'), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 24, 1)
        else:
            cls.EnableCtrl(skill, 24, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 10)

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
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'raypos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'raypos'), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'raypos', cl_action.GetSpherePointByRay(skill, 0.01, 1, 20) if cl_action.GetSkillCustomData(skill, 'UseByAI', defaultValue = 0) == 0 else cl_action.CrtArgTargetPos(skill, notContainDying = True))
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 18, 1)
        else:
            cls.EnableCtrl(skill, 18, 1)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 12, 1)
        else:
            cls.EnableCtrl(skill, 12, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
            cls.EnableShow(skill, 64, 1)
        else:
            cls.EnableCtrl(skill, 64, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1419
    m_Name = '飞花'
    m_ExtPerform = (8004, 8013)
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
        'Att': 40000,
        'CrazyEff': 0,
        'BulletSpeed': 60,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 6,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1062
    m_CheckForbid = 1010
    m_AIPerformDam = 2000
    
    def UsePerform(self, oWarrior, oSkill):
        if oSkill.m_CheckType == CRT_CHECK_SERVER:
            oSkill.m_Custom['UseByAI'] = 1
        super().UsePerform(oWarrior, oSkill)


