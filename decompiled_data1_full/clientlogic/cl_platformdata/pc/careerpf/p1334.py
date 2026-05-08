# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1334.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1334.pyc
# Source Generated with Decompyle++
# File: p1334.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import BIG_LION_STATE
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
            cls.EnableShow(skill, cl_action.ToInt(skill, 16 - 16 * (skill.m_Cache['ExplodeDelay'] / 100)), 1)
        else:
            cls.EnableCtrl(skill, cl_action.ToInt(skill, 16 - 16 * (skill.m_Cache['ExplodeDelay'] / 100)), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AddAttackerStateCount(skill, 33838, -6, iTime = 0)
        cl_action.PerformCure(skill, cl_action.GetAttackerAttr(skill, 'HPMax'), iPointTarget = cl_action.GetSkillAID(skill))
        cl_action.AttackerAddState(skill, 33766, skill.m_Cache['AddStateTime'], 0, {
            'TransDamFactor': cl_action.GetTransDamFactor(skill) })
        if cl_action.CheckHasState(skill, 33605):
            cl_action.SetAttackStateStatistics(skill, 33605, 'KeepBigLion', 1)
            cl_action.AttackerRemoveState(skill, 33605, bSameItem = False)
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 100, 1)
        else:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SkillHaltOther(skill, 1330)
    cl_action.SkillHaltOther(skill, 1336)
    cl_action.SkillHaltOther(skill, 1331)
    cl_action.SendUseCareerPFMsg(skill)
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPFEnergyPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1334
    m_Name = '#NT#无双'
    m_ExtPerform = (1330, 1331, 1335, 1336, 1681, 1337, 1332)
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
        'ColdTime': 100,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 2000,
        'Att': 30000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 6,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 1036
    m_AIPerformDam = 600
    
    def CanUse(self, oWarrior, dInfo):
        oStateCon = oWarrior.m_State
        if not oStateCon.GetItemBySID(BIG_LION_STATE):
            return 0
        oState = oStateCon.GetItemBySID(NEED_STATE)
        iNeedCount = self.CalAttr('Pierce')
        if not oState or oState.m_CurCount < iNeedCount:
            return 0
        return super().CanUse(oWarrior, dInfo)


NEED_STATE = 33838
