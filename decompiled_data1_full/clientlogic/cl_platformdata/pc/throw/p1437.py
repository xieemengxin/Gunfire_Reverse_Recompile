# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1437.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1437.pyc
# Source Generated with Decompyle++
# File: p1437.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurGroundFlyCartoon, SendDataCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL, OBJ_FRIEND, SKILLCACHE_INT, SKILLCACHE_POS, WARRIOR_SUMMON_SEED

class CCartoon2(SendDataCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillServerCache(skill, 'CreatePlant') > 0 and cl_action.GetSkillServerCache(skill, 'FirstDam') != 1:
            if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
                for i1 in range(0, cl_action.GetSkillServerCache(skill, 'CreatePlant'), 1):
                    cl_action.CreatePlantByPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), i1, (1, 0, 0))
                
            else:
                for i2 in range(1, cl_action.GetSkillServerCache(skill, 'CreatePlant') + 1, 1):
                    cl_action.CreatePlantByPos(skill, cl_action.GetEndPositionInCrt(skill, 1), cl_action.GetSpecificPerformArgValue(skill, 1436, 'ShiftDis', iDefault = 0), cl_math.Vec3Add(cl_action.CrtArgSelfHeroCtrlToTargetFace(skill, cl_action.GetEndPositionInCrt(skill, 1)), (i2, 0, 0)))
                

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
            cls.EnableShow(skill)
        else:
            cls.EnableCtrl(skill)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(CurGroundFlyCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckVictimType(skill, WARRIOR_SUMMON_SEED, OBJ_ALL):
            cl_action.HatchVictimGardenerSeed(skill)
        elif not cl_action.CheckVictimSideType(skill, OBJ_FRIEND):
            if cl_action.CheckHasTalent(skill, 3812):
                cl_action.PerformDamage(skill, {
                    'Att': cl_action.ToInt(skill, cl_action.GetAttackerPerformAttr(skill, 1436, 'Att') * 0.7) })
            else:
                cl_action.PerformDamage(skill, {
                    'Att': cl_action.GetAttackerPerformAttr(skill, 1436, 'Att') })
            cl_action.VictimAddState(skill, 33593, cl_action.GetSpecificPerformArgValue(skill, 1436, 'ImmobilizeTime', iDefault = 0), 0, { })
            if cl_action.GetSkillServerCache(skill, 'CreatePlant') > 0 and cl_action.GetSkillServerCache(skill, 'FirstDam') != 1:
                cl_action.SetSkillServerCache(skill, 'FirstDam', 1)
                for i3 in range(1, cl_action.GetSkillServerCache(skill, 'CreatePlant') + 1, 1):
                    cl_action.CreatePlantByPos(skill, cl_action.CrtArgHitPos(skill), i3, (1, 0, 0))
                

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, cl_action.GetAttackerPerformAttr(skill, 1436, 'BulletSpeed'), cl_action.GetAttackerPerformAttr(skill, 1436, 'KeepTime'), 50, (cl_action.GetAttackerPerformAttr(skill, 1436, 'Radius'), 2, 2), (cl_action.GetAttackerPerformAttr(skill, 1436, 'Radius') + 1, 2, 2), upDis = 0.5, downDis = 2, climbHeight = 5)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), cl_action.CrtArgSelfFace(skill), cl_action.GetAttackerPerformAttr(skill, 1436, 'BulletSpeed'), cl_action.GetAttackerPerformAttr(skill, 1436, 'KeepTime'), 50, (cl_action.GetAttackerPerformAttr(skill, 1436, 'Radius'), 2, 2), (cl_action.GetAttackerPerformAttr(skill, 1436, 'Radius') + 1, 2, 2), upDis = 0.5, downDis = 2, climbHeight = 5)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'CreatePlant', cl_action.GetSkillServerCache(skill, 'CreatePlant'))
    cl_action.SetSkillServerCache(skill, 'FirstDam', 0)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.throw import CUseCountPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1437
    m_Name = '#NT#藤蔓冲击触发'
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
        'BulletSID': 0,
        'Att': 60000,
        'CrazyEff': 0,
        'BulletSpeed': 20,
        'DebuffProb': 0,
        'ExplodeDelay': 0,
        'Radius': 2,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 75,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 2000

