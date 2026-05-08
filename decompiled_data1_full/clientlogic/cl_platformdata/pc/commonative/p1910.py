# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1910.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1910.pyc
# Source Generated with Decompyle++
# File: p1910.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.commonative.customaction import Custom1910CostBullet as CostBullet
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_WEAKNESS, SKILLCACHE_EXTRATRAJECTORY

class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cl_action.SetCurVictim(skill, cl_action.GetSkillVID(skill))
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
        cl_action.ModifySkillHitPos(skill, cl_action.CrtArgHitPos(skill))
        cl_action.SetCurCartoonCurPos(skill, 4, cl_action.CrtArgHitPos(skill))
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetTrajectory(skill) * 100 }, { }, sendPFMsg = False)

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
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ConsumeWeaponBagBullet(skill, 1)
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 0, index = 0)


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
from cl_pxlayer import PXMASK_BARRIER
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1910
    m_Name = '#NT致命装置-炮台专属一'
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
        'AttDistance': 25,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 1
    m_IgnoreLayer = (PXMASK_BARRIER,)
    m_ForbidRule = 0
    
    def UsePerform(self, oWarrior, oSkill):
        oSkill.m_Collect['BaseBullet'] = 0
        oWeapon = oWarrior.m_WieldCon.GetCurWeapon()
        if oWeapon:
            oSkill.m_Collect['TriggerWeaponID'] = oWeapon.m_ID
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DP, oWarrior, {
                'Skill': oSkill,
                'ItemID': oWeapon.m_ID,
                'UnCrtByOwnerSign': 1 })
            oBulletCom = oWeapon.GetComponent('Bullet')
            if oBulletCom:
                oSkill.m_Collect['CurBullet'] = oBulletCom.Bullet()
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COSTBULLET, oWarrior, {
                    'Skill': oSkill,
                    'ItemID': oWeapon.m_ID })
                oSkill.m_Collect['BulletUse'] = 0
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPONFIRE, oWarrior, {
                'Skill': oSkill })
            CostBullet(oWarrior, oSkill, oWeapon)
        super().UsePerform(oWarrior, oSkill)


