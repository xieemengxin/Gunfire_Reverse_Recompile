# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s8thirdactive/p52005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s8thirdactive/p52005.pyc
# Source Generated with Decompyle++
# File: p52005.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, OBJ_ENEMY

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PushVictim(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillAID(skill)), 4, 3, 10000, angle = 180, iCartoonSID = -1, iIgnoreStruckCD = 1, iClient = 0, iFace2Dir = True)
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] }, dArgs = { })
        cl_action.PerformCure(skill, cl_action.ToInt(skill, skill.m_Cache['Att'] * 1 / 100), iPointTarget = cl_action.GetSkillAID(skill))

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetCameraCenterPosition(skill, cartoon), end = cl_action.GetCameraDirPos(skill, 4)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius'],
                4,
                120], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
        if cl_action.GetTimerCartoonCurTimes(skill, 1) > 3:
            cl_action.ChangeS8ThirdItemEnergy(skill, -5)
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
        if cl_action.GetS8ThirdItemEnergy(skill) <= 5:
            cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 100, 99)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(ChargeCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

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
        cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 100, 99, 0, False, True, halfEnd = False, offsetTime = 0, breaktips = True, allowMaxChargeLowAmmo = False)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.TargetAddState(skill, 39773, 0, 1, { }, cl_action.GetSkillAID(skill))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 0, index = 0)


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
    m_SID = 52005
    m_Name = '吞天'
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
        'ChargeTime': 0,
        'DebuffProb': 0,
        'Att': 0,
        'Radius': 15 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = (0,)
    m_ForbidRule = 0

