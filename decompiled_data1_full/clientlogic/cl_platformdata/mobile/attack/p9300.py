# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9300.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9300.pyc
# Source Generated with Decompyle++
# File: p9300.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon5(TraceCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (0, -0.2, 1))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttackDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = cl_action.ObjectBranchBySkillElementType(skill, None, None, None, None), liveTime = 0, trailEffect = None, effectLiveTime = 0, lineDistance = 1, angle = 2 if cl_math.CalDistance3D(cl_action.VectorShiftForAttDir(skill, cl_action.CrtArgCameraCenterPos(skill, cartoon), (0, -0.2, 1)), cl_action.CrtArgSightCentrePos(skill, cartoon)) > 8 else 180, lockWeakness = True, lockAngle = 18, lockDis = 50, IgnoreDefalutDis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheExtraTrajectory(skill, 1)
    cartoon = { }
    CCartoon5.Init(skill, cartoon, casting = 0, index = cl_action.GetTrajectory(skill))


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]

from cl_perform.attack import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9300
    m_Name = 's元素符咒真实发射'
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
    m_ClassifyTag = (1,)
    m_BulletUse = 1
    m_IsMinor = 1
    m_ForbidRule = 0

