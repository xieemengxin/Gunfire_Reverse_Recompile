# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1340.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1340.pyc
# Source Generated with Decompyle++
# File: p1340.pyc (Python 3.6)

from cl_commondefines import TYPE_RELIFE_PASSIVE
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.SetCartoonDependState(skill, 1, 39731)
        cl_action.CustomPerformAction(skill, 1340, 'SpareEnterScene', { })

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.AttackerRemoveState(skill, 39731, bSameItem = False)
        cl_action.CustomPerformAction(skill, 1340, 'SpareLeaveScene', { })

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
            cls.EnableShow(skill, 200, 45)
        else:
            cls.EnableCtrl(skill, 200, 45)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseCareerPFMsg(skill)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    cl_action.CustomPerformAction(skill, 1340, 'SpareLeaveScene', { })
    cl_action.AttackerRemoveState(skill, 39731, bSameItem = False)


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1340
    m_Name = '#NT#灵体状态'
    m_ExtPerform = (2003, 12043, 1341)
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
        'ColdTime': 1500,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 0,
        'AddStateTime': 1500,
        'Att': 40000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 10000,
        'ExplodeDelay': 280,
        'Radius': 3,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 0
    m_CheckForbid = 1013
    m_AIPerformDam = 3000
    
    def UsePerform(self, oWarrior, oSkill):
        cl_action.AttackerAddState(oSkill, 39731, oSkill.m_Cache.get('AddStateTime', 1000), 0, {
            'TransDamFactor': cl_action.GetTransDamFactor(oSkill) })
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        self.DoAction(oSkill)



def SpareEnterScene(oSkill, dInfo, *arg):
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_Servant):
        return None
    oSpare = oAttack.m_Game.GetObject(oAttack.m_Servant)
    if oSpare.IsDead():
        dReason = {
            'Type': TYPE_RELIFE_PASSIVE }
        oSpare.Relife(dReason)
    sKey = 'pf1340'
    iHPMax = max(100, oAttack.QueryAttr('HPMax') + oAttack.QueryAttr('ShieldMax'))
    oSpare.AttrForceSet('HPMax', iHPMax, sKey)
    iHPMax = oSpare.QueryAttr('HPMax')
    oSpare.HPDirectModify('HP', 0, iHPMax - oSpare.HP(), sKey)
    oSpare.Goto(oAttack.m_Scene, oAttack.GetPos())


def SpareLeaveScene(oSkill, dInfo, *arg):
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_Servant):
        return None
    oSpare = oAttack.m_Game.GetObject(oAttack.m_Servant)
    if not oSpare:
        return None
    vPos = oSpare.GetPos()
    oSpare.LeaveScene(0)
    if not oAttack.Query('1340NoBack', []):
        oAttack.WalkTo(vPos)

