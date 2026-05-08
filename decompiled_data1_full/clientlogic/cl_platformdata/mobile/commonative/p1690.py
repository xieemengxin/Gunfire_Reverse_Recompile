# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1690.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1690.pyc
# Source Generated with Decompyle++
# File: p1690.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import CurveCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ENEMY, SKILLCACHE_RANDOM

class CCartoon1(CurveCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckHasTalent(skill, 2902):
            if cl_action.GetTalentLevel(skill, 2902) == 1:
                pass
            elif cl_action.GetTalentLevel(skill, 2902) == 2:
                pass
            
        
        if 30000 > 10000 and cl_action.CheckHasTalent(skill, 2902):
            if cl_action.GetTalentLevel(skill, 2902) == 1:
                pass
            elif cl_action.GetTalentLevel(skill, 2902) == 2:
                pass
            
        
        cl_action.CalAttenuationByDis(skill, {
            cl_action.GetCartoonStart(skill, 1): cl_action.GetSkillCustomData(skill, 'PerformAtt')(cl_action.GetSkillCustomData(skill, 'PerformAtt'), 30000, 10000, 10000, 50, 10) })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), [
                (0, 1, 0.5),
                (0, 1, -0.5),
                (0, 1.5, 0.5),
                (0, 1.5, -0.5),
                (0, 2, 0.2),
                (0, 2, -0.2)][cl_action.GetRandomInRange(skill, 0, 5)]), cl_action.CrtArgRandomAngle(skill, cartoon, cl_math.Vec3Add(cl_action.CrtArgSelfPos(skill), [
                (0, 1, 0.5),
                (0, 1, -0.5),
                (0, 1.5, 0.5),
                (0, 1.5, -0.5),
                (0, 2, 0.2),
                (0, 2, -0.2)][cl_action.GetRandomInRange(skill, 0, 5)]), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 10, 15, 10, 15, False), 1, 70, 100 if cl_action.CheckTargetSID(skill, 39211) else 50, 330, 0.7, targettype = OBJ_ENEMY, pierceblock = True, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 1, hittarger = False, iVictim = 0)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetSkillCustomDataInt(skill, 'ChooseSelf', 1)

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
        CCartoon1.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon2.Init(skill, cartoon, casting = 1, index = 0)


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
    m_SID = 1690
    m_Name = '荆棘盾牌反弹'
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
    m_UseCurWeapon = 0
    m_ForbidRule = 0

