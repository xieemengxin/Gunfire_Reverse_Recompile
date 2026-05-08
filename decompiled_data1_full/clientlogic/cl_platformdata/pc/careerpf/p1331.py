# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1331.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1331.pyc
# Source Generated with Decompyle++
# File: p1331.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import ChargeCartoon, DirectPosCartoon, RayCastCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, 20), cl_action.ToInt(skill, 5))
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 20), cl_action.ToInt(skill, 5))

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillServerCache(skill, 'SkillAtt') })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 4), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = False, explosionDelay = 0)
        else:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 4), (0, 0, 0), [
                3], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(RayCastCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillServerCache(skill, 'SkillAtt', skill.m_Cache['Att'] * ((cl_action.GetCartoonChargeLevel(skill, 0) * 0.6 if cl_action.GetChargeCartoonTime(skill, 0) >= 20 else 0) + 1))
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSkillServerCache(skill, 'SkillAtt', skill.m_Cache['Att'] * ((cl_action.GetCartoonChargeLevel(skill, 0) * 0.6 if cl_action.GetChargeCartoonTime(skill, 0) >= 20 else 0) + 1))
        cartoon = { }
        CCartoon6.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgTpsTransform(skill, 'Bip001 R Hand'))):
                return None
            cls.EnableShow(skill, 1, 100, 150, targettype = OBJ_ENEMY, liveTime = 0, radius = cl_action.GetChargeCartoonTime(skill, 0) / 100, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgTpsTransform(skill, 'Bip001 R Hand')), cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgTpsTransform(skill, 'Bip001 R Hand')), cl_action.GetSceneCenterPosition(skill, cartoon), 1, 100, 150, targettype = OBJ_ENEMY, liveTime = 0, radius = cl_action.GetChargeCartoonTime(skill, 0) / 100, flyoverdis = 0, passid = 0, extCheck = CRT_EXTCHECK_NONE)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ChargeCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, sSubMsgKey = '')

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SkillForbid(skill, True, 1100)
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.ToInt(skill, cl_action.ToInt(skill, 20) / (1 if cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100 == 0 else cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100)), cl_action.ToInt(skill, 5), 0, False, True, halfEnd = False, offsetTime = 0, breaktips = True, allowMaxChargeLowAmmo = True)
        elif cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100 == 0:
            pass
        
        skill(cl_action.ToInt, skill(cl_action.ToInt(skill, 20), 1 / cl_action.GetAttackerAttr(skill, 'ChargeSpeed') / 100), cl_action.ToInt(skill, 5), 0, False, True, halfEnd = False, offsetTime = 0, breaktips = True, scanAngle = 0, scanDistance = 0, maxScanNum = 0, prepareTime = 30, hasLv0 = True, allowMaxChargeLowAmmo = True, minLevel = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ApplyStateTransDamFactor(skill, 33604)
    cl_action.AttackerAddState(skill, 33761, 0, 1, { })
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    cl_action.SkillForbid(skill, False, 1100)


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1331
    m_Name = '#NT#蓄力远程'
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
        'ColdTime': 4,
        'AttDistance': 6,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 200,
        'Att': 30000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 4000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 600

