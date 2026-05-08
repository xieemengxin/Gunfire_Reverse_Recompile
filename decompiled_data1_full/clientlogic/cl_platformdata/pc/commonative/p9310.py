# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p9310.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p9310.pyc
# Source Generated with Decompyle++
# File: p9310.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_ELEMENTTYPE

class CCartoon5(TraceCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, { }, sendPFMsg = False)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, -0.2, 1))):
                return None
            cls.EnableShow(skill, skill.m_Cache['Pierce'], cl_action.GetWeaponAttDis(skill), skill.m_Cache['BulletSpeed'], targettype = OBJ_ENEMY, effect = cl_action.ObjectBranchBySkillElementType(skill, None, None, None, None), liveTime = 0, trailEffect = None, effectLiveTime = 0, lineDistance = 1, angle = 2 if cl_math.CalDistance3D(cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, -0.2, 1)), cl_action.GetSceneCenterPosition(skill, cartoon)) > 8 else 180, lockWeakness = True, lockAngle = 18, lockDis = 50, IgnoreDefalutDis = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.CheckHasInscription(skill, 13033):
        cl_action.AddSkillCacheData(skill, SKILLCACHE_ELEMENTTYPE)
        cl_action.ModifySkillCache(skill, 'ElementType', cl_action.GetElementType(skill))
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
    else:
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_ELEMENTTYPE]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 9310
    m_Name = '如律令专属铭刻'
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
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_ForbidRule = 0

