# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p2008.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p2008.pyc
# Source Generated with Decompyle++
# File: p2008.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, COMMON_SEASON_DAMEAGE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, SKILLCACHE_EXTRATRAJECTORY

class CCartoon0(DirectPosCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0)) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'vStart', defaultValue = cl_action.SkillStartPos(skill)), (0, 0, 0), [
                cl_action.GetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY) / 100], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        COMMON_SEASON_DAMEAGE][0])
    cl_action.SetSkillCacheData(skill, SKILLCACHE_EXTRATRAJECTORY, cl_action.GetSkillCustomData(skill, 'Radius', defaultValue = cl_action.GetAttackerCustomValue(skill, 'BaseRadius', iDefault = 100)))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_EXTRATRAJECTORY])
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE

class CPerform(CCustomPerform):
    m_SID = 2008
    m_Name = '#NT#S7组件莲花单次绽放'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_TRUE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_BaseArgData = {
        'AIPerformDam': 200 }

