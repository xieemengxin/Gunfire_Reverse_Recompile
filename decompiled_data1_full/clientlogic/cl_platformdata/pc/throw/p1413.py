# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1413.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1413.pyc
# Source Generated with Decompyle++
# File: p1413.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, LightningChainCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_PERFORMMODE

class CCartoon0(LightningChainCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, skill.m_Cache['DamInterval'], skill.m_Cache['Radius'], skill.m_Cache['BulletSpeed'], cl_action.GetSkillAID(skill) if cl_action.GetSkillCustomArg(skill, 'Target') == 0 else cl_action.GetSkillCustomArg(skill, 'Target'), '', 1, False)
        elif cl_action.GetSkillCustomArg(skill, 'Target') == 0:
            pass
        
        skill(False, True, cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraDirPos(skill, 0), (0, -0.5, 0)), skill.m_Cache['DamInterval'], skill.m_Cache['Radius'], skill.m_Cache['BulletSpeed'], 0 if cl_action.GetSkillCustomArg(skill, 'Target') == 0 else 30, 0 if cl_action.GetSkillCustomArg(skill, 'Target') == 0 else skill.m_Cache['Radius'], 0 if cl_action.GetSkillCustomArg(skill, 'Target') == 0 else 60, 0.2, True, [], cl_action.GetSkillAID(skill) if cl_action.GetSkillCustomArg(skill, 'Target') == 0 else cl_action.GetSkillCustomArg(skill, 'Target'), '', 1, False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[2]), (0, 0.2, 0)), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[2]), (0, 0.2, 0)), (0, 0, 0), [
                5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    cl_action.AddSkillCacheData(skill, SKILLCACHE_PERFORMMODE)
    cl_action.SetSkillCustomDataInt(skill, 'TriggerOrigin', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
        cl_action.SendUseThrowPFMsg(skill)
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[0] == 0:
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cl_action.AddIgnoreTarget(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[2])
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.throw import CUseCountPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1413
    m_Name = '连环闪电触发'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_THUNDER
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 60000,
        'CrazyEff': 10000,
        'BulletSpeed': 50,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 7,
        'BulletVerticalAcc': 0,
        'AddStateTime': 0,
        'KeepTime': 0,
        'DamInterval': 3,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

