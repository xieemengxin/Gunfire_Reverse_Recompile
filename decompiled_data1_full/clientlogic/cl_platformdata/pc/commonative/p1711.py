# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1711.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1711.pyc
# Source Generated with Decompyle++
# File: p1711.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_FRIEND_NOSELF

class CCartoon1(CurveCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 8073, 150 if cl_action.GetTargetPhase(skill, cl_action.GetCurVID(skill)) == 3 else 170 if cl_action.GetTargetPhase(skill, cl_action.GetCurVID(skill)) == 2 else 200, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgRandomAngle(skill, cartoon, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 15, 20, 15, 20, False), 1, 100, 12, 330, 0.3, targettype = OBJ_FRIEND_NOSELF, pierceblock = True, effect = 0, liveTime = 0, trailEffect = 0, effectLiveTime = 1, hittarger = True, iVictim = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVID(skill)):
            if cl_math.CalDistance3D(cl_action.CrtArgSelfPos(skill), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0)) < 0.001:
                cl_action.VictimAddState(skill, 8073, 150 if cl_action.GetTargetPhase(skill, cl_action.GetCurVID(skill)) == 3 else 170 if cl_action.GetTargetPhase(skill, cl_action.GetCurVID(skill)) == 2 else 200, 0, { })
            else:
                cartoon = { }
                CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1711
    m_Name = '宝箱怪宝石主动'
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

