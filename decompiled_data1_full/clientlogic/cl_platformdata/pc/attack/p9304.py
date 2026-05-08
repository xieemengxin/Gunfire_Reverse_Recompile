# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9304.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9304.pyc
# Source Generated with Decompyle++
# File: p9304.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ExternalDriveCartoon, RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, QINGLUAN_PUSH_DAMAGE, SKILLCACHE_EXTRATRAJECTORY

class CCartoon3(ExternalDriveCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        if cl_action.CheckVictimInStruckCD(skill):
            cl_action.PushMoveVictim(skill, (0, 0, 0), 40, 6.4, (0, 0, 0), iCartoonSID = 3, bKnockBack = True)
        else:
            cl_action.PushVictim(skill, (0, 0, 0), 40, 6.4, 10000, angle = 0, iCartoonSID = 3, iIgnoreStruckCD = 0, iClient = 1)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            QINGLUAN_PUSH_DAMAGE][0])
        for i2 in range(0, cl_action.GetHitTimesAtpointTarget(skill, cl_action.GetCurVID(skill)), 1):
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.ToInt(skill, (6.4 - cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetEndPositionInCrt(skill, 3)) if 6.4 - cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetEndPositionInCrt(skill, 3)) > 0 else 0) / 0.064) if cl_action.ToInt(skill, (6.4 - cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetEndPositionInCrt(skill, 3)) if 6.4 - cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 3), cl_action.GetEndPositionInCrt(skill, 3)) > 0 else 0) / 0.064) >= 20 else 20 }, { }, sendPFMsg = False)
        

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetCurVID(skill), cl_action.GetSkillHitArea(skill), 3)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if not cl_math.CalDistance3D(cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), cl_action.GetSkillVarCache(skill, 'SkillStart')) >= (20 if cl_action.CheckHasInscription(skill, 4918) else 10):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), cl_math.Vec3Add(((0.1 - (skill.m_Cache['Accuracy'] + 1) / 8000) * (cl_action.GetTrajectory(skill) / -2.3), 0, 0), (i1 * (0.1 - (skill.m_Cache['Accuracy'] + 1) / 8000), 0, 0)))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], 40, skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)
        if not cl_math.CalDistance3D(cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), cl_action.GetSkillVarCache(skill, 'SkillStart')) >= (20 if cl_action.CheckHasInscription(skill, 4918) else 10):
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i3, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), cl_math.Vec3Add((-0.9, 0.25, 0), (i3 * 0.3, 0, 0)))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(RayCastCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        for i1 in range(0, cl_action.GetTrajectory(skill), 1):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = i1)
        
        if not True:
            for i3 in range(0, 6, 1):
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = i3)
            

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
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon)):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], 40, skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, liveTime = 0, radius = 0, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'SkillStart', cl_action.GetMuzzlePos(skill))
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


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
    m_SID = 9304
    m_Name = '青鸾'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001

