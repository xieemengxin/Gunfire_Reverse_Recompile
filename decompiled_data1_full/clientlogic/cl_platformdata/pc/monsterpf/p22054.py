# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p22054.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p22054.pyc
# Source Generated with Decompyle++
# File: p22054.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP, OBJ_ALL, OBJ_ALLNOSELF, OBJ_ENEMY, WARRIOR_HERO, WARRIOR_PROTEGE, WARRIOR_SERVANT

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.SelfDamage(skill, skill.m_Cache['HPMax'], DAM_TYPE_PERFORM, DAM_USE_HP, DAM_TYPE_TRUE, 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ENEMY):
            if not cl_action.CheckVictimType(skill, WARRIOR_PROTEGE, OBJ_ALLNOSELF) or cl_action.CheckVictimType(skill, WARRIOR_SERVANT, OBJ_ENEMY):
                cl_action.WeaponDamage(skill, {
                    'Att': cl_action.GetPlayRound(skill) * 6000 + 24000 + (cl_action.GetGamePlayerCnt(skill) - 1) * 9000 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 2, 1.4)), (0, 0, 0), [
                7.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_THUNDER, MONSTERPF_TYPE_ATTACK, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 22054
    m_Name = '【新第二幕】喷电怪-电桶爆炸'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 5000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_THUNDER
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

