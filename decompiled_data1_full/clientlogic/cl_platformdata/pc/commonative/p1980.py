# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1980.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1980.pyc
# Source Generated with Decompyle++
# File: p1980.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon, TraceCartoon
from cl_commondefines import CRT_CHECK_SERVER, MONSTER_PART_WEAKNESS, NWARRIOR_DROP, OBJ_ENEMY, SKILLCACHE_LSTINT

class CCartoon2(TraceCartoon):
    m_SID = 2
    
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
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.GetMuzzlePosition(skill, cartoon), (0, 0, 0), 1, 70, 30, showstart = (0, 0, 0), targettype = OBJ_ENEMY, liveTime = 0, lineDistance = 1, angle = 180, lockWeakness = False, lockAngle = 360, canDesAngle = 10, lockDis = 50, IgnoreDefalutDis = 9999, IgnoreSummon = False, iIgnoreMonsterID = 0, FilterDie = True, lockFromCartoon = True, isMultipleBeacon = False, targetOffset = (0, 0, 0), arriveDoTrigger = False, accelerated = 15, lockSumm = True, lockCanDestroy = False, lockHideDoor = False, isBlocked = True, isMonsterFirst = True, lockExplode = False, traceTimes = 1, maskFightType = NWARRIOR_DROP, noTargetOver = True, searchByDistance = True)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) > 0:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

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
        cl_action.ModifySkillHitArea(skill, MONSTER_PART_WEAKNESS)
        cl_action.ModifySkillHitPos(skill, cl_action.CrtArgHitPos(skill))
        cl_action.SetCurCartoonCurPos(skill, 4, cl_action.CrtArgHitPos(skill))
        cl_action.SetCrtValue(skill, 4, 'CopyTimes', iDefault = cl_action.GetSkillCustomData(skill, 'CopyTimes', defaultValue = 0))
        cl_action.WeaponDamage(skill, {
            'Att': cl_action.GetSkillCustomData(skill, 'Dam', defaultValue = 100) * cl_action.CalTrajectory(skill, 1) }, { }, sendPFMsg = False)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 4, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.ModifySkillCache(skill, 'LuckyHit', skill.m_Cache['LuckyHit'] + cl_action.GetSkillCustomData(skill, 'AddLuckyHit', defaultValue = 100))
    cartoon = { }
    CCartoon4.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_LSTINT]


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1980
    m_Name = '耗弹自瞄-手持弹道'
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
        'AttDistance': 99,
        'ChargeTime': 0,
        'Att': 100 }
    m_ClientNeed = 0
    m_UseCurWeapon = 1
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
        super().UsePerform(oWarrior, oSkill)


