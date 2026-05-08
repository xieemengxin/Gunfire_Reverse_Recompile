# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/commonative/p1695.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/commonative/p1695.pyc
# Source Generated with Decompyle++
# File: p1695.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
from cl_only import SendAlert
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_UNTAGGED

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
        cl_action.SetDirectHitInfo(skill, cl_action.GetSkillVID(skill))
        cl_action.CustomPerformAction(skill, 1695, 'CalDamage', { })
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_UNTAGGED)
        cl_action.ModifySkillCache(skill, 'Att', cl_action.GetSkillVarCache(skill, 'Damage'))
        cl_action.ModifySkillCache(skill, 'LuckyHit', -1000)
        cl_action.ModifySkillCache(skill, 'ElementType', 2048)
        cl_action.WeaponDamage(skill, {
            'Att': 100 }, {
            'ForbidModifyType': 1 }, sendPFMsg = False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon0.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1695
    m_Name = '二相孢子爆炸'
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


def CalDamage(oSkill, *args):
    oAttack = oSkill.GetAttack()
    lstWeapon = oAttack.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    if len(lstWeapon) < 2:
        SendAlert('err', 'pf1695 weapon num %d' % len(lstWeapon))
        oSkill.m_VarCache['Damage'] = 0
        return None
    oWeapon1 = lstWeapon[0]
    oWeapon2 = lstWeapon[1]
    iAtt1 = oWeapon1.QueryAttr('Att')
    iAtt2 = oWeapon2.QueryAttr('Att')
    iTrajectory1 = oWeapon1.QueryAttr('Trajectory')
    iTrajectory2 = oWeapon2.QueryAttr('Trajectory')
    iDamage = ((iAtt1 * iTrajectory1 + iAtt2 * iTrajectory2) // (iTrajectory1 + iTrajectory2)) * oSkill.m_Custom['SporeNum']
    oSkill.m_VarCache['Damage'] = iDamage

