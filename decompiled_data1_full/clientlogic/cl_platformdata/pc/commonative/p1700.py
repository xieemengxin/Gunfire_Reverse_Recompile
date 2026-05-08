# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1700.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1700.pyc
# Source Generated with Decompyle++
# File: p1700.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import DAM_TYPE_FIRE, DAM_TYPE_TRUE
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
        cl_action.PerformDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'PerformAtt') })

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
                (0, 2, -0.2)][cl_action.GetRandomInRange(skill, 0, 5)]), cl_action.CrtArgBodyPos(skill, 0, 0, 0, 0), 10, 15, 10, 15, False), 1, 70, 50, 330, 0.7, targettype = OBJ_ENEMY, pierceblock = True, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 1, hittarger = False)

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
from cl_commondefines import DAM_TYPE_FIRE

class CPerform(CCustomPerform):
    m_SID = 1700
    m_Name = '燃烧子弹'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_FIRE
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    
    def UsePerform(self, oWarrior, oSkill):
        self.m_ElementType = DAM_TYPE_FIRE | DAM_TYPE_TRUE
        oSkill.m_Cache['DebuffProb'] = oSkill.m_Custom['DebuffProb']
        super().UsePerform(oWarrior, oSkill)


