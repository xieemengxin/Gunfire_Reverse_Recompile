# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1699.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1699.pyc
# Source Generated with Decompyle++
# File: p1699.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_pxlayer import PXMASK_SKILLBLK
from cl_perform.cartoon.defines import ExternalDriveCartoon, RayCastCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_POS

class CCartoon1(RayCastCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'StartPos'), cl_action.GetSkillVarCache(skill, 'StartPos'), cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), 999, cl_math.CalDistance3D(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetSkillVarCache(skill, 'StartPos')), cl_math.CalDistance3D(cl_action.GetSkillCacheData(skill, SKILLCACHE_POS), cl_action.GetSkillVarCache(skill, 'StartPos')) / 0.3, targettype = OBJ_ENEMY, effect = 0, liveTime = 0.1, trailEffect = None, effectLiveTime = 0, radius = 0.8, flyoverdis = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(ExternalDriveCartoon):
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
        cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_action.GetSkillVarCache(skill, 'HitPos'))
        cl_action.ServerSendSkillCache(skill, [
            SKILLCACHE_POS])
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 0, 'default', 3)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_POS, cl_math.Vec3Add(cl_action.SkillStartPos(skill), (1, 2, 0)))
    cl_action.ServerSendSkillCache(skill, [
        SKILLCACHE_POS])
    cl_action.SetSkillVarCache(skill, 'StartPos', cl_action.GetSkillCacheData(skill, SKILLCACHE_POS))
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_POS]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE

class CPerform(CCustomPerform):
    m_SID = 1699
    m_Name = '青鸾铭刻'
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
        'AttDistance': 99,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    m_IgnoreLayer = (PXMASK_SKILLBLK,)
    
    def UsePerform(self, oWarrior, oSkill):
        oWarrior.Set('pf1699', oSkill.m_Base['ActNum'])
        super(CPerform, self).UsePerform(oWarrior, oSkill)


