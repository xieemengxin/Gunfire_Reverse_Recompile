# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8014.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8014.pyc
# Source Generated with Decompyle++
# File: p8014.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DelegateDirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SECTOR, CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_PERFORMMODE, SKILLCACHE_POS

class CCartoon11(TimerCartoon):
    m_SID = 11
    
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
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(DelegateDirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetAttackerStateCount(skill, 32775) < 16:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1427, 'Att') })
        elif cl_action.GetAttackerStateCount(skill, 32775) < 32:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 64)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1427, 'Att') })
        else:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 80)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1427, 'Att') })

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
                cl_action.GetAttackerPerformAttr(skill, 1427, 'Radius'),
                2,
                45], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, useclientpos = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 8, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DelegateDirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.GetAttackerStateCount(skill, 32775) < 16:
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1427, 'Att') * 0.5 })
        elif cl_action.GetAttackerStateCount(skill, 32775) < 32:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 64)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1427, 'Att') * 0.5 })
        else:
            cl_action.SetSkillServerCache(skill, 'ExShowTips', 80)
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetAttackerPerformAttr(skill, 1427, 'Att') * 0.5 })

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
                skill.m_Cache['Radius'],
                2,
                45], attshape = ATT_SHAPE_SECTOR, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, useclientpos = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

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
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 8, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) // 8 if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) // 8 < 6 else 5)

    InitSuccess = classmethod(InitSuccess)


class CCartoon25(TimerCartoon):
    m_SID = 25
    
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
        if (cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) // 8 if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) // 8 < 6 else 5) == 0:
            cartoon = { }
            CCartoon1.Init(skill, cartoon, casting = 1, index = 0)
        else:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableCtrl(skill, 55, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    if cl_action.GetSkillCustomData(skill, 'ThrowMsg', defaultValue = 0) == 1:
        cl_action.SendUseThrowPFMsg(skill)
    cl_action.UseExtraThrowPerform(skill, {
        'UseFacePos': cl_action.GetSkillCustomData(skill, 'UseFacePos', defaultValue = 0) }, 20, 0)
    if cl_action.GetSkillCustomData(skill, 'UseFacePos', defaultValue = 0) == 1:
        cl_action.SetCustomPos(skill, cl_action.GetCameraDirPos(skill, 1.5))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'vEnd', defaultValue = (0, 0, 0)))
    cl_action.SetSkillCacheData(skill, SKILLCACHE_PERFORMMODE, 1 if cl_action.GetSkillCustomData(skill, 'SingleHit', defaultValue = 0) == 0 and cl_action.CheckHasTalent(skill, 2908) else 0)
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_INT])
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1:
        cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetSpecificPerformArgValue(skill, 4347, 'BaseEnergyNum', iDefault = 1))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_INT])
        cartoon = { }
        CCartoon25.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_PERFORMMODE,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8014
    m_Name = '秘卷觉醒冲拳'
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
        'Att': 70000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 1500,
        'ExplodeDelay': 0,
        'Radius': 7,
        'BulletVerticalAcc': 0,
        'AddStateTime': 200,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

