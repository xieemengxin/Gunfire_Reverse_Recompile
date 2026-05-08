# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1432.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1432.pyc
# Source Generated with Decompyle++
# File: p1432.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, OBJ_ENEMY, OBJ_FRIEND, WARRIOR_MONSTER

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimSideType(skill, OBJ_ENEMY):
            if cl_action.CheckMonsterType(skill, WARRIOR_MONSTER, cl_action.GetCurVID(skill)):
                cl_action.VictimAddState(skill, 1860, cl_action.GetSpecificPerformArgValue(skill, 1429, 'SlowDownTime', iDefault = 200), 0, { })
                cl_action.PerformDamage(skill, {
                    'Att': cl_action.GetAttackerPerformAttr(skill, 1429, 'Att') * 0.5 if cl_action.GetSkillCustomData(skill, '3516SureNothrow', defaultValue = False) else cl_action.GetAttackerPerformAttr(skill, 1429, 'Att') })
            elif cl_action.GetSkillCustomData(skill, '3516SureNothrow', defaultValue = False):
                pass
            
            skill('Att', {
                cl_action.GetAttackerPerformAttr(skill, 1429, 'Att') * 0.5: cl_action.GetAttackerPerformAttr(skill, 1429, 'Att') })
        elif cl_action.GetSkillCustomData(skill, 'HasP3518', defaultValue = False) and cl_action.CheckVictimSideType(skill, OBJ_FRIEND):
            cl_action.VictimAddState(skill, 33041, 500, 0, {
                'TalentLevel': cl_action.GetSkillCustomData(skill, '3518PFLV', defaultValue = 1) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = (0, 0, 0), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = True, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, (0, 0, 0), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = True, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
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

from cl_perform.throw import CUseCountPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1432
    m_Name = '#NT#3514破绽爆炸'
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
        'ColdTime': 15,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 0,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 45,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 300,
        'KeepTime': 300,
        'DamInterval': 100,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000

