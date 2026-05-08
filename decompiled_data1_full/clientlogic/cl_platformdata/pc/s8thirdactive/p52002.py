# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s8thirdactive/p52002.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s8thirdactive/p52002.pyc
# Source Generated with Decompyle++
# File: p52002.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ENEMY, WARRIOR_MONSTER

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckMonsterType(skill, WARRIOR_MONSTER, cl_action.GetCurVID(skill)) and cl_action.CheckWarriorHasState(skill, cl_action.GetCurVID(skill), 39748):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerCustomData(skill, 'PF52002_att', iDefault = 40000) })
            cl_action.PushMoveVictim(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), 10, 2, cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), (0, 0, 0), baseHorizontal = True), iCartoonSID = -1, bKnockBack = True)
            cl_action.TargetAddState(skill, 39748, 20, 1, { }, cl_action.GetCurVID(skill))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                2], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
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
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 10, cl_action.ToInt(skill, (skill.m_Cache['AddStateTime'] if False else 700) / 10))

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.S8ThirdActiveAddState(skill, cl_action.GetSkillAID(skill), 39747, { })
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

from cl_perform.s8thirdactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 52002
    m_Name = '超级蘑菇'
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
        'ColdTime': 300,
        'AttDistance': 0,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 0,
        'Radius': 0,
        'AddStateTime': 700 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = (0,)
    m_ForbidRule = 0

