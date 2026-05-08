# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p8019.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p8019.pyc
# Source Generated with Decompyle++
# File: p8019.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, GARDENER_THROW_DAMAGE, OBJ_ENEMY

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'VID': cl_action.GetCurVID(skill),
            'GardenThrowHit': 1 })
        if cl_action.GetSkillCustomData(skill, 'NoAddParasiticState', defaultValue = 0) == 0:
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'])
        cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetSpecificPerformArgValue(skill, 1436, 'ParasiticMul', iDefault = 3), cl_action.GetTransDamFactor(skill), skill.m_Cache['DamInterval'])

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.CrtArgTargetPos(skill, notContainDying = False), (0, 0.1, 0)), (0, 0, 0), [
                cl_action.GetAttackerPerformAttr(skill, 1436, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = True, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ModifySkillCache(skill, 'DamInterval', cl_action.GetAttackerPerformAttr(skill, 1436, 'DamInterval'))
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        GARDENER_THROW_DAMAGE][0])
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 8019
    m_Name = '被动藤蔓冲击'
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
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 40000,
        'CrazyEff': 0,
        'BulletSpeed': 20,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 4,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 80,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

