# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/suitactive/p8605.pyc
# RelativePath: clientlogic/cl_platformdata/pc/suitactive/p8605.pyc
# Source Generated with Decompyle++
# File: p8605.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon1(CurveCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, '1946Att', defaultValue = 0) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgRandomAngle(skill, cartoon, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 15, 20, 15, 20, False), 1, 50, 25, 330, 0.7, targettype = OBJ_ENEMY, pierceblock = True, liveTime = 0, hittarger = False, iVictim = 0, lockPos = (0, 0, 0), bLockDeadPos = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        for i1 in range(0, 1, 1):
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 0, index = 0)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.suitactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION, SUIT_PERFORM_POS_NOTCONTROL

class CPerform(CCustomPerform):
    m_SID = 8605
    m_Name = '荆棘外壳套装等级1'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 0,
        'Radius': 0,
        'MaxCover': 1 }
    m_SourceSuit = 15107
    m_Pos = SUIT_PERFORM_POS_NOTCONTROL
    m_ForbidRule = 0
    m_BaseArgData = {
        'DebuffProb': 1000 }

