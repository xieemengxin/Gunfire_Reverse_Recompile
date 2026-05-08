# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/fillbullet/p1022.pyc
# RelativePath: clientlogic/cl_platformdata/pc/fillbullet/p1022.pyc
# Source Generated with Decompyle++
# File: p1022.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import MeleeWeaponCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_USE_ARMOR, DAM_USE_SHIELD, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.FillBullet(skill, cl_action.GetWeaponIntAttr(skill, 'MaxBullet'), 0)

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
            cls.EnableShow(skill, skill.m_Cache['FillTime'], 1)

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
            cls.EnableShow(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(MeleeWeaponCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillServerCache(skill, 'HitTimes') >= cl_action.GetTrajectory(skill):
            cl_action.AttackerAddState(skill, 1591, 0, 0, { })

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHasInscription(skill, 13047):
            cl_action.BreakVictimProtection(skill, DAM_USE_SHIELD, True, True)
            cl_action.BreakVictimProtection(skill, DAM_USE_ARMOR, True, True)
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetSkillServerCache(skill, 'AttBuff') * 150 }, { }, sendPFMsg = False)
            cl_action.SetSkillServerCache(skill, 'HitTimes', cl_action.FloatToIntFloor(skill, cl_action.GetSkillServerCache(skill, 'HitTimes') + 1))
        else:
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetSkillServerCache(skill, 'AttBuff') * 150 }, { }, sendPFMsg = False)
            cl_action.SetSkillServerCache(skill, 'HitTimes', cl_action.FloatToIntFloor(skill, cl_action.GetSkillServerCache(skill, 'HitTimes') + 1))

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
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                1,
                40,
                0], meshCount = 1, totalTime = 4, targettype = OBJ_ENEMY, pierceStatic = False, left2right = False, center2around = True)

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
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 6, cl_action.GetTrajectory(skill))

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon6.Init(skill, cartoon, casting = 1, index = 0)
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SkillForbid(skill, True, 1076)
    cl_action.SetSkillServerCache(skill, 'HitTimes', 0)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    cl_action.SkillForbid(skill, False, 1076)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.fillbullet import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 1022
    m_Name = '手喷换弹'
    m_ExtPerform = ()
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
        'ColdTime': 0,
        'AttDistance': 0,
        'HPConsumption': 0 }
    m_ForbidRule = 0
    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['AttBuff'] = 1
        super().UsePerform(oWarrior, oSkill)


