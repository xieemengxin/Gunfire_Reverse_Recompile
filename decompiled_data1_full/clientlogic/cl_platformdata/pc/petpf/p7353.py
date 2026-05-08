# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/petpf/p7353.pyc
# RelativePath: clientlogic/cl_platformdata/pc/petpf/p7353.pyc
# Source Generated with Decompyle++
# File: p7353.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        if cl_action.GetSkillVarCache(skill, 'ElementENum') == 1:
            cl_action.ModifySkillCache(skill, 'ElementType', 1024)
        elif cl_action.GetSkillVarCache(skill, 'ElementENum') == 2:
            cl_action.ModifySkillCache(skill, 'ElementType', 512)
        elif cl_action.GetSkillVarCache(skill, 'ElementENum') == 3:
            cl_action.ModifySkillCache(skill, 'ElementType', 256)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': int(skill.m_Cache['Att'] * 0.75) }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVID(skill)), cl_action.CrtArgWarriorPos(skill, cl_action.GetSkillVID(skill)), [
                cl_action.GetAttackerPerformAttr(skill, 7353, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = True, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillVarCache(skill, 'ElementENum', cl_action.GetRandomInRange(skill, 1, 3))
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.petactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, PETPF_ACTIVE_ATTACK

class CPerform(CCustomPerform):
    m_SID = 7353
    m_Name = '妖灵随机元素爆炸'
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
        'ColdTime': 50,
        'AttDistance': 999,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1,
        'Radius': 5 }
    m_ElementType = DAM_TYPE_NORMAL
    m_ClientNeed = 0
    m_PFSubType = PETPF_ACTIVE_ATTACK
    m_SpellPower = 0
    m_NeedTarget = 0
    m_ForbidRule = 0

