# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8012.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8012.pyc
# Source Generated with Decompyle++
# File: p8012.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateDirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon2(DelegateDirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.UseExtraThrowPerform(skill, {
            'UseFacePos': cl_action.GetSkillCustomData(skill, 'UseFacePos', defaultValue = 0) }, 30, 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetAttackerPerformAttr(skill, 1411, 'Att') })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.StartAndEndAtSameHeight(skill, cl_action.CrtArgCustomPos(skill, cartoon), cl_action.CrtArgDestPosDirPlane(skill, cl_action.CrtArgCustomPos(skill, cartoon), cl_math.Vec3Minus(cl_action.CrtArgSelfPos(skill), cl_action.CrtArgCustomPos(skill, cartoon)), 3, 0)), cl_action.CrtArgCustomPos(skill, cartoon), [
                cl_action.GetAttackerPerformAttr(skill, 1411, 'Radius'),
                1.8,
                180], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, useclientpos = False)

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
        if cl_action.GetSkillCustomData(skill, 'UseFacePos', defaultValue = 0) == 1:
            cl_action.SetCustomPos(skill, cl_action.GetCameraDirPos(skill, 1.5))
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        else:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetSkillCustomData(skill, 'ThrowMsg', defaultValue = 0) == 1:
        cl_action.SendUseThrowPFMsg(skill)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8012
    m_Name = '秘卷觉醒挥砍'
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
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 10000,
        'BulletSpeed': 35,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 7,
        'BulletVerticalAcc': 0,
        'AddStateTime': 0,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

