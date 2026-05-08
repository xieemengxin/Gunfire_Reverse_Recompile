# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p22014.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p22014.pyc
# Source Generated with Decompyle++
# File: p22014.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP, OBJ_ALL, OBJ_ALLNOSELF, OBJ_ENEMY, WARRIOR_HERO, WARRIOR_PROTEGE

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.SelfDamage(skill, skill.m_Cache['HPMax'], DAM_TYPE_PERFORM, DAM_USE_HP, DAM_TYPE_TRUE, 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ENEMY) or cl_action.CheckVictimType(skill, WARRIOR_PROTEGE, OBJ_ALLNOSELF):
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetPlayRound(skill) * 4000 + 16000 + (cl_action.GetGamePlayerCnt(skill) - 1) * 9000 }, { }, sendPFMsg = True)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 1.7, 1.4)), (0, 0, 0), [
                7.5], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False)

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

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import CLOSE_DISTANCE, DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 22014
    m_Name = '【第二幕】喷火怪-燃料罐爆炸'
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
    m_ElementType = DAM_TYPE_FIRE
    m_SkillShotType = CLOSE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

