# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1307.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1307.pyc
# Source Generated with Decompyle++
# File: p1307.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import RayCastCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL, WARRIOR_BARRIER, WARRIOR_SUMMON

class CCartoon0(RayCastCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.SetAttackerCustomPos(skill, 'BarriarPos', [
            cl_action.GetStartPositionInCrt(skill, 0)][0])
        if cl_action.GetTalentLevel(skill, 2503) == 1:
            if cl_action.CheckHasTalent(skill, 2505):
                cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1049)
                cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                    cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                    cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                    'Box': 0 })
                cl_action.AttackerAddState(skill, 32372, 0, 0, { })
                cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
            else:
                cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1046)
                cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                    cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                    cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                    'Box': 0 })
                cl_action.AttackerAddState(skill, 32372, 0, 0, { })
                cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
        elif cl_action.GetTalentLevel(skill, 2503) == 2:
            if cl_action.CheckHasTalent(skill, 2505):
                cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1050)
                cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                    cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                    cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                    'Box': 0 })
                cl_action.AttackerAddState(skill, 32372, 0, 0, { })
                cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
            else:
                cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1047)
                cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                    cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                    cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                    'Box': 0 })
                cl_action.AttackerAddState(skill, 32372, 0, 0, { })
                cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
        elif cl_action.GetTalentLevel(skill, 2503) == 3:
            if cl_action.CheckHasTalent(skill, 2505):
                cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1051)
                cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                    cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                    cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                    'Box': 0 })
                cl_action.AttackerAddState(skill, 32372, 0, 0, { })
                cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
            else:
                cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1048)
                cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                    cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                    cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                    'Box': 0 })
                cl_action.AttackerAddState(skill, 32372, 0, 0, { })
                cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
        elif cl_action.CheckHasTalent(skill, 2505):
            cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1052)
            cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                'Box': 0 })
            cl_action.AttackerAddState(skill, 32372, 0, 0, { })
            cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
        else:
            cl_action.SetSkillVarCache(skill, 'BarrierModelId', 1044)
            cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                cl_action.GetStartPositionInCrt(skill, 0)], WARRIOR_SUMMON, {
                cl_action.GetSkillVarCache(skill, 'BarrierModelId'): 1 }, {
                'Box': 0 })
            cl_action.AttackerAddState(skill, 32372, 0, 0, { })
            cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.SetBarriarPos(skill, 3, 1)):
                return None
            cls.EnableShow(skill, 0, 1, 1, targettype = OBJ_ALL, effect = None, liveTime = 0, trailEffect = None, effectLiveTime = 0, radius = 0, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
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
        if not cl_action.CheckHasState(skill, 32383):
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 25, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasState(skill, 32372):
        cl_action.AttackerRemoveState(skill, 32372)
        if len(cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)) > 0:
            cl_action.AddClientEffect(skill, 1010, cl_action.CrtArgWarriorPos(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER)[0]), time = 4)
            cl_action.ChangeAttackerEnergy(skill, cl_action.ToInt(skill, 0 - cl_action.GetAttackerAttr(skill, 'Energy') / 4))
            cl_action.DestroyAssignSummon(skill, cl_action.GetAttackSummon(skill, WARRIOR_BARRIER), 0)
        else:
            cartoon = { }
            CCartoon4.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1307
    m_Name = '力场屏障'
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
        'ColdTime': 100,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 80,
        'AddStateTime': 0,
        'Att': 0,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 0

