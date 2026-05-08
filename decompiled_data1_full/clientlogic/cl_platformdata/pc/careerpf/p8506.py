# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p8506.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p8506.pyc
# Source Generated with Decompyle++
# File: p8506.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_CYLINDER, CRT_CHECK_SERVER, CRT_EXTCHECK_SEEDPLANT, OBJ_ALL, SKILLCACHE_POS, WARRIOR_MONSTER, WARRIOR_PLANT, WARRIOR_SUMMON_SEED

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckMonsterType(skill, WARRIOR_MONSTER, cl_action.GetCurVID(skill)):
            cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
                'P8506_HitMonster': 1,
                'VID': cl_action.GetCurVID(skill),
                'AddStateTime': 50 }, sSubMsgKey = '')
        if cl_action.CheckMonsterType(skill, WARRIOR_SUMMON_SEED, cl_action.GetCurVID(skill)) and cl_action.GetTargetOwnerID(skill, cl_action.GetCurVID(skill)) == cl_action.GetSkillAID(skill):
            cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
                'P8506_HitSeed': 1,
                'VID': cl_action.GetCurVID(skill),
                'AddStateTime': 50 }, sSubMsgKey = '')
            cl_action.UpdateFieldSeedInfo(skill)
        if cl_action.CheckMonsterType(skill, WARRIOR_PLANT, cl_action.GetCurVID(skill)) and cl_action.GetTargetOwnerID(skill, cl_action.GetCurVID(skill)) == cl_action.GetSkillAID(skill):
            cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
                'P8506_HitPlant': 1,
                'VID': cl_action.GetCurVID(skill),
                'AddStateTime': 50 }, sSubMsgKey = '')
        if cl_action.GetCurVID(skill) == cl_action.GetSkillAID(skill):
            cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
                'P8506_HitSelf': 1,
                'VID': cl_action.GetCurVID(skill),
                'AddStateTime': 50 }, sSubMsgKey = '')
            cl_action.VictimAddState(skill, 33780, 58, 0, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), (0, 2, 0)), (0, 0, 0), [
                cl_action.GetAttackerPerformAttr(skill, 1333, 'Radius'),
                2], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_SEEDPLANT, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerUsePerform(skill, 8506, {
            'vStart': cl_action.GetSkillCacheData(skill, SKILLCACHE_POS) }, 4, 0)
        cl_action.SkillHaltSelf(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillCustomData(skill, 'vStart', defaultValue = (0, 0, 0)))
    cl_action.SetAttackerCustomPos(skill, 'FieldCenterPos', cl_action.GetSkillCustomData(skill, 'vStart', defaultValue = (0, 0, 0)))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    cl_action.ClearFieldSeedInfo(skill)


def End(skill):
    cl_action.ClearFieldSeedInfo(skill)


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 8506
    m_Name = '#园丁领域技能'
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
        'UseInterval': 0,
        'AddStateTime': 0,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 3,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 100,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 0

