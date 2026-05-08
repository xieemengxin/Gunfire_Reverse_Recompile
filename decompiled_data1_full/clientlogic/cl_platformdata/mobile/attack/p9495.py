# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9495.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9495.pyc
# Source Generated with Decompyle++
# File: p9495.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHasState(skill, 1511):
            cl_action.AttackerAddState(skill, 1511, 0, 1, { })
            cl_action.CreateBeaconSummon(skill, 1017, cl_action.GetCartoonHitFirstTargetPos(skill, 1), 1500, 1, 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        if not cl_action.CheckHasState(skill, 1511):
            cl_action.AttackerAddState(skill, 1511, 0, 1, { })
            cl_action.CreateBeaconSummon(skill, 1017, cl_action.GetCartoonHitFirstTargetPos(skill, 1), 1500, 1, 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgCameraCenterPos(skill, cartoon)):
                return None
            cls.EnableShow(skill, 1, cl_action.GetWeaponAttackDis(skill), 100, targettype = OBJ_ENEMY, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    for i1 in range(0, 1, 1):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform
from cl_commondefines import DPSUBMSG_NOFIRE

class CPerform(CCustomPerform):
    m_SID = 9495
    m_Name = 's彩虹'
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
        'ColdTime': 50,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1019

