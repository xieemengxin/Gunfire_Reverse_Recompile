# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1424.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1424.pyc
# Source Generated with Decompyle++
# File: p1424.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_LSTINT, SKILLCACHE_RANDOM

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
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTINT)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT,
        SKILLCACHE_RANDOM]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1424
    m_Name = '占星'
    m_ExtPerform = (1425,)
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
        'ColdTime': 80,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 50000,
        'CrazyEff': 0,
        'BulletSpeed': 100,
        'DebuffProb': 3000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 1,
        'TriggerTimes': 1,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_AIPerformDam = 2000
    
    def UsePerform(self, oWarrior, oSkill):
        iCardCnt = cl_action.GetSkillCacheData(oSkill, SKILLCACHE_LSTINT)[0]
        oSkill.m_Collect['CardCnt'] = iCardCnt
        super().UsePerform(oWarrior, oSkill)


