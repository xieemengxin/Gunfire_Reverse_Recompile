# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1987.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1987.pyc
# Source Generated with Decompyle++
# File: p1987.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MAGIC_WAND_DAMAGE, OBJ_ENEMY, SKILLCACHE_INT

class CCartoon5(CurveCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'Att', defaultValue = 0) }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetSkillCustomData(skill, 'vStart', defaultValue = (0, 0, 0)), cl_action.CrtArgRandomAngle(skill, cartoon, cl_action.CrtArgMonsterMuzzlePos(skill, cartoon, (0, 2, -1)), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 0, 0, 0, 0, False), 1, 50, cl_action.GetSkillCacheData(skill, SKILLCACHE_INT), 330, 0.7, targettype = OBJ_ENEMY, pierceblock = True, liveTime = 0, hittarger = True, iVictim = 0, lockPos = (0, 0, 0), bLockDeadPos = False)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
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
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillCacheData(skill, SKILLCACHE_INT, cl_action.GetPerformArgValue(skill, 'FlySpeed', iDefault = 10))
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        MAGIC_WAND_DAMAGE][0])
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_TRUE

class CPerform(CCustomPerform):
    m_SID = 1987
    m_Name = '锦上添花弹射'
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
        'AttDistance': 10,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0

