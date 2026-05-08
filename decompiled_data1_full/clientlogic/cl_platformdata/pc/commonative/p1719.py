# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1719.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1719.pyc
# Source Generated with Decompyle++
# File: p1719.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import DPSUBMSG_DEFAULT
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED, SKILLCACHE_EXTRATRAJECTORY

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
        cl_action.SetCurVictim(skill, cl_action.GetSkillVID(skill))
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.ModifySkillHitPos(skill, cl_action.CrtArgHitPos(skill))
        cl_action.SetCurCartoonCurPos(skill, 0, cl_action.CrtArgHitPos(skill))
        cl_action.SetSkillVarCache(skill, '1719_trajectory', 10 if cl_action.GetTrajectory(skill) > 10 else cl_action.GetTrajectory(skill))
        cl_action.SetSkillVarCache(skill, '1719_damageratio', cl_action.FloatToIntFloor(skill, cl_action.GetTrajectory(skill) * 100 / 10) if cl_action.GetTrajectory(skill) > 10 else 100)
        for i1 in range(0, cl_action.GetSkillVarCache(skill, '1719_trajectory'), 1):
            cl_action.WeaponDamage(skill, {
                'Att': cl_action.GetSkillVarCache(skill, '1719_damageratio') }, { }, sendPFMsg = False)
        

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_EXTRATRAJECTORY]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1719
    m_Name = '祝福战斗核心'
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
    m_UseCurWeapon = 1
    m_ForbidRule = 0
    
    def SendUseMsg(self, oWarrior, oSkill):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DP, oWarrior, {
            'Skill': oSkill }, iSub = DPSUBMSG_DEFAULT)


