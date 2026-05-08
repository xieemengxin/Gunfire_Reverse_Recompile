# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9707.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9707.pyc
# Source Generated with Decompyle++
# File: p9707.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED, MONSTER_PART_WEAKNESS, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon5(TraceCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHitPointArea(skill, MONSTER_PART_WEAKNESS):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
            cl_action.WeaponDamage(skill, {
                'Att': 50 if cl_action.CheckHasInscription(skill, 13095) else 100 }, { }, sendPFMsg = True)
        elif cl_action.CheckHasInscription(skill, 13095):
            pass
        
        skill('Att', {
            50: 100 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = 'R_Att'))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), 25, showstart = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = 'R_Att')), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 360 if cl_math.CalDistance3D(cl_action.GetCameraCenterPosition(skill, cartoon), cl_action.GetSceneObjPos(skill, 0)) <= 5 else 5, lockDis = 70, IgnoreDefalutDis = 0, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = False, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 150)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

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
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, int(12 / (3 if skill.m_Cache['AttSpeed'] / 220 > 3 else skill.m_Cache['AttSpeed'] / 220)), cl_action.GetTrajectory(skill) - 1)

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
        cl_action.SendCurCartoonTriggerMsg(skill)
        if cl_action.GetTrajectory(skill) >= 2:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, int(50 / (3 if skill.m_Cache['AttSpeed'] / 220 > 3 else skill.m_Cache['AttSpeed'] / 220)), 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9707
    m_Name = '#聚能法杖 -4'
    m_ExtPerform = ()
    m_HaltInfo = {
        108: 1,
        10214: 1,
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
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001

