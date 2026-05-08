# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/careerpf/p1310.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/careerpf/p1310.pyc
# Source Generated with Decompyle++
# File: p1310.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon, WinkPosCartoon
from cl_commondefines import ATT_SHAPE_LINE, ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, FIGHT3_KEY_IGNOREKNOCKBACK, OBJ_ENEMY, SKILLCACHE_PERFORMMODE, WARRIOR_BUILD, WARRIOR_MONSTER, WARRIOR_OBSTACLE_NORMAL

class CCartoon1(WinkPosCartoon):
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
            cls.EnableShow(skill, 0, 20, [], [], dashshape = ATT_SHAPE_LINE, acceleration = 1, decrease = 2, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
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
            cls.EnableShow(skill, 18, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(TimerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ENEMY) and cl_action.GetVictimAttr(skill, 'DefKnockBack') < 10000:
            if cl_action.CheckVictimInStruckCD(skill):
                cl_action.PushMoveVictim(skill, cl_action.GetCartoonCurPos(skill, 2), 20, 4, iCartoonSID = -1, bKnockBack = False)
            else:
                cl_action.PushVictim(skill, cl_action.GetCartoonCurPos(skill, 2), 20, 4, 20000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)

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
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] + ((cl_action.GetTalentLevel(skill, 2903) * 0.2 + 0.1) * skill.m_Cache['AttDistance'] * 2 if cl_action.GetSkillServerCache(skill, 'MoveDistance') < (cl_action.GetTalentLevel(skill, 2903) * 0.2 + 0.1) * skill.m_Cache['AttDistance'] * 2 else cl_action.GetSkillServerCache(skill, 'MoveDistance')) * 0.2 * 70000 if cl_action.CheckHasTalent(skill, 2903) else skill.m_Cache['Att'] })
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgCameraCenterPos(skill, cartoon), end = cl_action.CrtArgSightCentrePos(skill, cartoon)):
                return None
            cls.EnableShow(skill, [
                5,
                1.5,
                90], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(WinkPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillServerCache(skill, 'MoveDistance', cl_action.FloatToIntFloor(skill, cl_action.CountDistance(skill, cl_action.GetCartoonStart(skill, 3), cl_action.GetCartoonEnd(skill, 3))))
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_BUILD, OBJ_ENEMY):
            cl_action.PerformDamage(skill, {
                'Att': 1000 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 0, 30, [
                3,
                2,
                180], [
                WARRIOR_OBSTACLE_NORMAL], dashshape = ATT_SHAPE_SECTOR, acceleration = 100, decrease = 100, targettype = OBJ_ENEMY, hitOver = True, bWaitOverTime = False, upSpeed = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREKNOCKBACK)
        cl_action.SetSkillServerCache(skill, 'DashTag', 1)
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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetPerformMode(skill) <= 0:
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1310
    m_Name = '冲刺'
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
        'ColdTime': 250,
        'AttDistance': 6,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 70000,
        'CrazyEff': 0,
        'BulletSpeed': 5000,
        'DebuffProb': 4000,
        'ExplodeDelay': 0,
        'Radius': 14,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1044
    m_CheckForbid = 1022
    m_AIPerformDam = 0

