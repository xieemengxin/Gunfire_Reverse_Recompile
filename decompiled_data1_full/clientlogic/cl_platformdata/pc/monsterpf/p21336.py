# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterpf/p21336.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterpf/p21336.pyc
# Source Generated with Decompyle++
# File: p21336.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_object
import cl_state
from cl_only import PY_FLAG_DEAD
from cl_commondefines import WARRIOR_HERO, STATE_TIME_FOREVER, SHARK_CHASE_STATE, HERO_CHASED_STATE
from cl_platformdata.custom.passive.customaction import CheckHeroCanBeChase
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREVERTIGO, STATE_EFF_DEBAR

class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetCartoonDependState(skill, 2, 33586)

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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 50, 10000)

    InitSuccess = classmethod(InitSuccess)


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
        cl_action.AttackerAddState(skill, 33586, 0, 0, { })
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 35, 1)

    InitSuccess = classmethod(InitSuccess)


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
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 65, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SkillForbid(skill, True, 1006)
    cl_action.StopMove(skill)
    cl_action.CustomPerformAction(skill, 21336, 'AddHeroChasedStateInfo', { })
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNOREVERTIGO)
    cl_action.AddLogicKey(skill, iLogickey = FIGHT3_KEY_IGNORETHUMP)
    cl_action.AddIgnoreStateEffect(skill, STATE_EFF_DEBAR)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.CustomPerformAction(skill, 21336, 'RemoveHeroChasedStateInfo', { })


def End(skill):
    cl_action.CustomPerformAction(skill, 21336, 'RemoveHeroChasedStateInfo', { })


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MIDDLE_DISTANCE, MONSTERPF_TYPE_ATTACK

class CPerform(CCustomPerform):
    m_SID = 21336
    m_Name = '鲨鱼怪浪鳍-潜泳'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 300,
        'AttDistance': 40,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = MIDDLE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_ATTACK
    m_ForbidRule = 0
    m_CacheAttr = [
        'DebuffProb']
    
    def CanUse(self, oWarrior, dData):
        if not dData:
            oEnemy = oWarrior.m_Agent.GetLockEnemy()
        elif 'VID' in dData:
            oEnemy = oWarrior.m_Game.GetObject(dData['VID'], PY_FLAG_DEAD)
        else:
            return 0
        if not oEnemy:
            return 0
        if not oWarrior.m_State.GetItemBySID(SHARK_CHASE_STATE) and not CheckHeroCanBeChase(oWarrior, oEnemy, IsLowHPChase = False):
            return 0
        return super(CPerform, self).CanUse(oWarrior, dData)



def AddHeroChasedStateInfo(oSkill, *args):
    iVID = oSkill.m_Base['VID']
    oTarget = oSkill.m_Game.GetObject(iVID, PY_FLAG_DEAD)
    if not oTarget or not (oTarget.m_FightType & WARRIOR_HERO):
        return None
    oState = oTarget.m_State.GetItemBySID(HERO_CHASED_STATE)
    iShark = oSkill.m_Base['AID']
    if not oState:
        dChasedInfo = {
            'AID': iShark,
            'RS': cl_object.reason.CStrReason('CustomAction5828') }
        oState = cl_state.AddState(oTarget, HERO_CHASED_STATE, STATE_TIME_FOREVER, 0, dChasedInfo)
        if oState:
            oState.Enable(oTarget)
    if 'ChaseShark' not in oState.m_Data:
        oState.m_Data['ChaseShark'] = { }
    if iShark not in oState.m_Data['ChaseShark']:
        oState.AddCount(oTarget, 1)
        oState.m_Data['ChaseShark'][iShark] = 1


def RemoveHeroChasedStateInfo(oSkill, *args):
    iVID = oSkill.m_Base['VID']
    oTarget = oSkill.m_Game.GetObject(iVID)
    if not oTarget or not (oTarget.m_FightType & WARRIOR_HERO):
        return None
    oState = oTarget.m_State.GetItemBySID(HERO_CHASED_STATE)
    if not oState:
        return None
    dStateData = oState.m_Data
    if 'ChaseShark' not in dStateData:
        return None
    iShark = oSkill.m_Base['AID']
    if iShark not in dStateData['ChaseShark']:
        return None
    dStateData['ChaseShark'].pop(iShark)
    oState.AddCount(oTarget, -1)
    if not oState.GetCount():
        oTarget.m_State.RemoveItem(oState.m_ID)
    oShark = oSkill.GetAttack()
    if not oShark:
        return None
    cl_state.RemoveState(oShark, SHARK_CHASE_STATE)

