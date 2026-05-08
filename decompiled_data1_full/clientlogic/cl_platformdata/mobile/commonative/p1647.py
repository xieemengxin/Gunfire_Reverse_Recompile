# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1647.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1647.pyc
# Source Generated with Decompyle++
# File: p1647.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import EntityCurveCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon6(EntityCurveCartoon):
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, (0, 0, 0), cl_math.Vec3Add(cl_action.CrtArgTargetPos(skill), (0, 1, 0)), 0, 0, 150, 10, 0, 1, targettype = OBJ_ENEMY, summonID = cl_action.GetSkillAID(skill))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AttackerAddState(skill, 7947, 0, 1, { })
    cartoon = { }
    CCartoon6.Init(skill, cartoon, casting = 1, index = 0)


def GetSkillCacheIndex():
    return []


def Halt(skill):
    pass


def End(skill):
    pass

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1647
    m_Name = '龙卷风追踪伤害'
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
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

