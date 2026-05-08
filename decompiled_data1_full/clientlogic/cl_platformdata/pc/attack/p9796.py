# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/attack/p9796.pyc
# RelativePath: clientlogic/cl_platformdata/pc/attack/p9796.pyc
# Source Generated with Decompyle++
# File: p9796.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerRangeCheckCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_ALL_PLAYER

class CCartoon1(TimerRangeCheckCartoon):
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
            cls.EnableShow(skill, 40000, cl_action.GetHeroTrans(skill) if cl_action.IsHeroCtrl(skill) else 0, 20, OBJ_ALL_PLAYER, isCloseGround = True)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.IsHeroCtrl(skill):
        cl_action.AttackerAddState(skill, 39753, 0, 1, { })
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.attack import CPerform as CCustomPerform
from cl_commondefines import DPSUBMSG_NOFIRE

class CPerform(CCustomPerform):
    m_SID = 9796
    m_Name = '#NT#召唤法杖'
    m_ExtPerform = (7021, 7356, 7357)
    m_HaltInfo = {
        40108: 1,
        10149: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 80,
        'AttDistance': 0,
        'ChargeTime': 1000,
        'MaxPFBullet': 40000,
        'PFBulletUse': 30000,
        'PFBulletRecover': 2000,
        'CostPFBulletDuringUse': 0,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = (4,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1079
    m_PassRule = {
        1012: 1,
        1064: 1,
        1051: 1 }
    m_CheckForbid = 1019
    
    def CanUse(self, oWarrior, dData):
        if self.CurPFBullet() < self.MaxPFBullet():
            return False
        return super(CPerform, self).CanUse(oWarrior, dData)


