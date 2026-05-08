# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1753.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1753.pyc
# Source Generated with Decompyle++
# File: p1753.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import CHALLENGE_COUNT_MUTANTMONSTER
from cl_perform.cartoon.defines import LockTargetCartoon, TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon2(LockTargetCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.CustomPerformAction(skill, 1753, 'MonsterMutant', { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SkillHaltSelf(skill)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), cl_action.CrtArgSelfCenterPos(skill), cl_action.GetSkillVID(skill), 999, 12, liveTime = 0, isLockCenter = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVID(skill)):
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.CustomPerformAction(skill, 1753, 'RecordLineIdx', { })
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    if cl_action.CheckTargetAlive(skill, cl_action.GetSkillVID(skill)):
        cl_action.CustomPerformAction(skill, 1753, 'MonsterMutant', { })


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1753
    m_Name = '异化传播（房间挑战）'
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


def RecordLineIdx(oSkill, *args):
    iAttack = oSkill.m_Base['AID']
    oAttack = oSkill.m_Game.GetObject(iAttack)
    if not oAttack or not (oAttack.m_LineIdx):
        return None
    oSkill.m_Custom['MutantLineIdx'] = oAttack.m_LineIdx


def MonsterMutant(oSkill, *args):
    oGame = oSkill.m_Game
    if not oGame or oGame.m_ReleaseFlag:
        return None
    dCustom = oSkill.m_Custom
    if 'MutantLineIdx' not in dCustom:
        return None
    tLineIdx = dCustom['MutantLineIdx']
    if not tLineIdx:
        return None
    iTarget = oSkill.m_Base['VID']
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    oCtrlMgr = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oChallenge = oCtrlMgr.m_RoomChallenge.GetChallenge(tLineIdx)
    if not oChallenge or oChallenge.m_Type != CHALLENGE_COUNT_MUTANTMONSTER:
        return None
    oChallenge.MonsterMutant(oTarget)

