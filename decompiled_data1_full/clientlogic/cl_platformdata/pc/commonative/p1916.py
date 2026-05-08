# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1916.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1916.pyc
# Source Generated with Decompyle++
# File: p1916.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import SectorDiffuseCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED, OBJ_ENEMY, SKILLCACHE_RANDOM, WARRIOR_BUILD

class CCartoon4(SectorDiffuseCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if not cl_action.CheckHitPointArea(skill, MONSTER_PART_UNTAGGED):
            cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'overflow', defaultValue = 10000) * (cl_action.CountDistance(skill, cl_action.GetStartPositionInCrt(skill, 0), cl_action.CrtArgHitPos(skill)) / 50) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, i1, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetSceneObjPos(skill, cl_action.GetSkillCustomData(skill, 'Target', defaultValue = 0)), (0, 0.1, 0)), cl_action.CrtArgDestPosDirPlane(skill, cl_math.Vec3Add(cl_action.GetSceneObjPos(skill, cl_action.GetSkillCustomData(skill, 'Target', defaultValue = 0)), (0, 0.1, 0)), cl_action.CrtArgSelfFace(skill), 1, (cl_action.GetCartoonLoopID(skill, 4) + 1) * 120 + cl_action.GetSkillCacheData(skill, SKILLCACHE_RANDOM)), 0, skill.m_Cache['AttDistance'], 1, 40, 1.5, 45, targettype = OBJ_ENEMY, effect = 0, isOverByFightType = False, fightType = WARRIOR_BUILD, isUseSector = True)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
    cl_action.ModifySkillHitPos(skill, cl_action.GetTargetCenterPos(skill, cl_action.GetSkillCustomData(skill, 'Target', defaultValue = 0)))
    cl_action.SetDirectHitInfo(skill, cl_action.GetSkillCustomData(skill, 'Target', defaultValue = 0))
    for i1 in range(0, 3, 1):
        cl_action.SetSkillVarCache(skill, 'isHitStatic', False)
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 0, index = i1)
    


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1916
    m_Name = '#NT#失衡冲击波'
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
        'AttDistance': 50,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

