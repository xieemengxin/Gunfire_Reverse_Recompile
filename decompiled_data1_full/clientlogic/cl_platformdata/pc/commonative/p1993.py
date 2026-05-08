# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1993.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1993.pyc
# Source Generated with Decompyle++
# File: p1993.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_CYLINDER, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ALL, WARRIOR_HERO, WARRIOR_MONSTER

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL):
            cl_action.PerformDamage(skill, {
                'Att': skill.m_Cache['Att'] })
        elif cl_action.CheckVictimType(skill, WARRIOR_MONSTER, OBJ_ALL):
            cl_action.PerformDamage(skill, {
                'Att': cl_action.GetPerformArgValue(skill, 'DamagetoMonster', iDefault = 0) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                1,
                3], attshape = ATT_SHAPE_CYLINDER, targettype = OBJ_ALL, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER

class CPerform(CCustomPerform):
    m_SID = 1993
    m_Name = '临时电柱'
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
        'ChargeTime': 0,
        'DebuffProb': 1000,
        'Att': 6000 }
    m_ClientNeed = 1
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'DamagetoMonster': 6000 }

