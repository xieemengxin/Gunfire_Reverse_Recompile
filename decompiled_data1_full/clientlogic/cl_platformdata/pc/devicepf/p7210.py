# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicepf/p7210.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicepf/p7210.pyc
# Source Generated with Decompyle++
# File: p7210.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateCollidedTriggerCartoon
from cl_commondefines import ATT_SHAPE_RECTANGLE, CRT_CHECK_SERVER, OBJ_ENEMY, PUSH_TYPE_MOVE_STAND, SKILLCACHE_INT

class CCartoon0(DelegateCollidedTriggerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetAttackerAttr(skill, 'Att')) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetMuzzlePos(skill), (0, 0, 0), 30, 100, 25, 0.3, [
                5.4,
                4,
                3], attshape = ATT_SHAPE_RECTANGLE, targettype = OBJ_ENEMY, pushtype = PUSH_TYPE_MOVE_STAND, liveTime = 0, standtime = cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), summonsid = 1084)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetPerformArgValue(skill, 'StandTime', iDefault = 400))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.deviceactive import CDeviceActive as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 7210
    m_Name = '屏障专属3-发射屏障'
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
        'AttDistance': 10,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1,
        'EnergyCost': 0,
        'Radius': 0 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = (0,)
    m_ForbidRule = 0
    m_BaseArgData = {
        'StandTime': 400 }

