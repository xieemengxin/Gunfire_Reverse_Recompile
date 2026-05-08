# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p39151.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p39151.pyc
# Source Generated with Decompyle++
# File: p39151.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, WARRIOR_SUMMON

class CCartoon0(TimerCartoon):
    m_SID = 0
    
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
        cl_action.CreateRandomNumWarriorAtPointPos(skill, cl_action.GetSkillVarCache(skill, 'lstpos'), WARRIOR_SUMMON, {
            1028: 10 }, {
            'Radius': 2 })
        for i2 in range(0, len(cl_action.GetSkillSummonCreate(skill)), 1):
            cl_action.TargetAddState(skill, 7959, 0, 0, { }, cl_action.GetSkillSummonCreate(skill)[i2])
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetMonsterPhase(skill) > 2:
        cl_action.SetSkillVarCache(skill, 'number', 6 + (1 if cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) > 2 else 0))
        cl_action.SetSkillVarCache(skill, 'total', cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) + 9)
        cl_action.SetSkillVarCache(skill, 'lstpos', cl_action.RemovePointsWithinDistance(skill, cl_action.GetPosByDistanceAndSummon(skill, 6, cl_action.GetSummonByDistance(skill, 200, 1028), cl_action.RemovePointsBeyondDistance(skill, cl_action.CreateRectanglePosList(skill, cl_action.StartAndEndAtSameHeight(skill, (0, 2, 0), cl_action.SkillStartPos(skill)), (130, 0, 130), 120, 5, 0), 29, (134.8, 2, 135.3))), 15, cl_action.GetSkillVarCache(skill, 'number') if cl_action.GetSkillVarCache(skill, 'total') - cl_action.GetSummonCnt(skill, 1028) >= cl_action.GetSkillVarCache(skill, 'number') else cl_action.GetSkillVarCache(skill, 'total') - cl_action.GetSummonCnt(skill, 1028)))
        for i1 in range(0, len(cl_action.GetSkillVarCache(skill, 'lstpos')), 1):
            cl_action.AddClientEffect(skill, 1013, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'lstpos')[i1], (0, 2.3, 0)), 100, (0, 0, 0))
        
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
    elif cl_action.GetMonsterPhase(skill) > 1:
        cl_action.SetSkillVarCache(skill, 'number', 5 + (1 if cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) > 2 else 0))
        cl_action.SetSkillVarCache(skill, 'total', cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) + 8)
        cl_action.SetSkillVarCache(skill, 'lstpos', cl_action.RemovePointsWithinDistance(skill, cl_action.GetPosByDistanceAndSummon(skill, 6, cl_action.GetSummonByDistance(skill, 200, 1028), cl_action.RemovePointsBeyondDistance(skill, cl_action.CreateRectanglePosList(skill, cl_action.StartAndEndAtSameHeight(skill, (0, 2, 0), cl_action.SkillStartPos(skill)), (130, 0, 130), 120, 5, 0), 29, (134.8, 2, 135.3))), 15, cl_action.GetSkillVarCache(skill, 'number') if cl_action.GetSkillVarCache(skill, 'total') - cl_action.GetSummonCnt(skill, 1028) >= cl_action.GetSkillVarCache(skill, 'number') else cl_action.GetSkillVarCache(skill, 'total') - cl_action.GetSummonCnt(skill, 1028)))
        for i3 in range(0, len(cl_action.GetSkillVarCache(skill, 'lstpos')), 1):
            cl_action.AddClientEffect(skill, 1013, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'lstpos')[i3], (0, 2.3, 0)), 100, (0, 0, 0))
        
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
    elif cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) > 2:
        pass
    
    skill('number', 4, 1 + 0)
    cl_action.SetSkillVarCache(skill, 'total', cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = True) + 7)
    cl_action.SetSkillVarCache(skill, 'lstpos', cl_action.RemovePointsWithinDistance(skill, cl_action.GetPosByDistanceAndSummon(skill, 6, cl_action.GetSummonByDistance(skill, 200, 1028), cl_action.RemovePointsBeyondDistance(skill, cl_action.CreateRectanglePosList(skill, cl_action.StartAndEndAtSameHeight(skill, (0, 2, 0), cl_action.SkillStartPos(skill)), (130, 0, 130), 120, 5, 0), 29, (134.8, 2, 135.3))), 15, cl_action.GetSkillVarCache(skill, 'number') if cl_action.GetSkillVarCache(skill, 'total') - cl_action.GetSummonCnt(skill, 1028) >= cl_action.GetSkillVarCache(skill, 'number') else cl_action.GetSkillVarCache(skill, 'total') - cl_action.GetSummonCnt(skill, 1028)))
    for i5 in range(0, len(cl_action.GetSkillVarCache(skill, 'lstpos')), 1):
        cl_action.AddClientEffect(skill, 1013, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'lstpos')[i5], (0, 2.3, 0)), 100, (0, 0, 0))
    
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39151
    m_Name = '风神-召唤气旋'
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
        'ColdTime': 1000,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 0,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']

