# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1961.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1961.pyc
# Source Generated with Decompyle++
# File: p1961.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon7(RayCastCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetSummonOwnerAttr(skill, 'Att') * 0.1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgDestPosDirPlane(skill, cl_math.Vec3Add(cl_action.CrtTargeFloorPos(skill, cl_action.GetSkillAID(skill)), (0, 1.2, 0)), cl_action.CrtArgDestPosDirPlane(skill, cl_math.Vec3Add(cl_action.CrtTargeFloorPos(skill, cl_action.GetSkillAID(skill)), (0, 1.2, 0)), cl_action.CrtArgSelfModelDirection(skill), 99, cl_action.ToInt(skill, -75 if cl_action.GetTimerCartoonCurTimes(skill, 1) % 2 == 1 else -60)), 5, cl_action.ToInt(skill, i1 * 30)), cl_action.CrtArgDestPosDirPlane(skill, cl_math.Vec3Add(cl_action.CrtTargeFloorPos(skill, cl_action.GetSkillAID(skill)), (0, 1.2, 0)), cl_action.CrtArgDestPosDirPlane(skill, cl_math.Vec3Add(cl_action.CrtTargeFloorPos(skill, cl_action.GetSkillAID(skill)), (0, 1.2, 0)), cl_action.CrtArgSelfModelDirection(skill), 99, cl_action.ToInt(skill, -75 if cl_action.GetTimerCartoonCurTimes(skill, 1) % 2 == 1 else -60)), 5, cl_action.ToInt(skill, i1 * 30)), cl_action.StartAndEndAtSameHeight(skill, cl_math.Vec3Add(cl_action.CrtTargeFloorPos(skill, cl_action.GetSkillAID(skill)), (0, 1.2, 0)), cl_action.CrtArgDestPosDirPlane(skill, cl_math.Vec3Add(cl_action.CrtTargeFloorPos(skill, cl_action.GetSkillAID(skill)), (0, 1.2, 0)), cl_action.CrtArgDestPosDirPlane(skill, cl_math.Vec3Add(cl_action.CrtTargeFloorPos(skill, cl_action.GetSkillAID(skill)), (0, 1.2, 0)), cl_action.CrtArgSelfModelDirection(skill), 99, cl_action.ToInt(skill, -75 if cl_action.GetTimerCartoonCurTimes(skill, 1) % 2 == 1 else -60)), 99, cl_action.ToInt(skill, i1 * 30))), 99, 99, 10, targettype = OBJ_ENEMY, liveTime = 0, radius = 0.65, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

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
        for i1 in range(0, 5, 1):
            cartoon = { }
            CCartoon7.Init(skill, cartoon, casting = 0, index = i1)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 150, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.PerformAddArgValue(skill, '1961_UseCnt', 1)
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetPerformArgValue(skill, '1961_UseCnt', iDefault = 1) * 1 if cl_action.GetPerformArgValue(skill, '1961_UseCnt', iDefault = 1) < 3 else 3)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1961
    m_Name = '首领遗物-妖王'
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
        'AttDistance': 99,
        'ChargeTime': 0 }
    m_ClientNeed = 1
    m_UseCurWeapon = 0
    m_ForbidRule = 0

