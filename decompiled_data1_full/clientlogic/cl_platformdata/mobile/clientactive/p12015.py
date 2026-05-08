# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/clientactive/p12015.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/clientactive/p12015.pyc
# Source Generated with Decompyle++
# File: p12015.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_perform
from cl_commondefines import PF_PER_SKILL
from cl_only import Functor
from cl_perform.cartoon.defines import ChargeCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon6(ChargeCartoon):
    m_SID = 6
    
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
            cls.EnableShow(skill, 0, 0, 0, False, True, effect = None, halfEnd = False, offsetTime = 0, breaktips = True)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon6.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.clientactive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 12015
    m_Name = '职业技能蓄力前置'
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
    m_UseCurWeapon = 0
    m_ForbidRule = 1070
    m_CheckForbid = 1013
    m_SubMsg = PF_PER_SKILL
    
    def UsePerform(self, oWarrior, oSkill):
        super().UsePerform(oWarrior, oSkill)
        oCareerpf = oWarrior.GetCareerPerform()
        oCareerpf.m_CheckForbid = 0
        oSkill.AddEndFunc(Functor(ReSetCheckForbidType, oWarrior.m_ID))

    
    def CanUse(self, oWarrior, dInfo):
        self.m_CanUseCount = 1
        return super().CanUse(oWarrior, dInfo)



def ReSetCheckForbidType(iWarrior, oSkill):
    oWarrior = oSkill.m_Game.GetObject(iWarrior)
    if not oWarrior:
        return None
    clsPerform = cl_perform.GetPerformModule(oWarrior.GetCareerPerformID())
    oCareerpf = oWarrior.GetCareerPerform()
    oCareerpf.m_CheckForbid = clsPerform.m_CheckForbid

