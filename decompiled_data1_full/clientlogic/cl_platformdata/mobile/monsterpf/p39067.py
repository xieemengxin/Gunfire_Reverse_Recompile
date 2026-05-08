# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39067.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39067.pyc
# Source Generated with Decompyle++
# File: p39067.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, OBJ_ALL, SIDE_TYPE_HERO, WARRIOR_HERO, WARRIOR_SUMMON

class CCartoon1(DirectPosCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimSide(skill, WARRIOR_SUMMON, SIDE_TYPE_HERO):
            cl_action.PerformDamage(skill, {
                'Att': 5000 })
        elif cl_action.CheckVictimType(skill, WARRIOR_HERO, OBJ_ALL):
            cl_action.PushHeroVictim(skill, cl_action.GetCartoonEnd(skill, 1), 20, 4, 10000, downSpeed = 0, fGravaty = 9.8, angle = 0)
            cl_action.PerformDamage(skill, {
                'Att': 5000 })
        else:
            cl_action.PushVictim(skill, cl_action.GetCartoonEnd(skill, 1), 20, 8, 10000, angle = 0, iCartoonSID = -1, iIgnoreStruckCD = 0, iClient = 0)
            cl_action.PerformDamage(skill, {
                'Att': 5000 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetKeyItemPos(skill, 6001), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ALL, pierceStatic = False, explosion = False)

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
from cl_commondefines import DAM_TYPE_NORMAL, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39067
    m_Name = '海船-炮弹爆炸'
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
        'AttDistance': 5,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

