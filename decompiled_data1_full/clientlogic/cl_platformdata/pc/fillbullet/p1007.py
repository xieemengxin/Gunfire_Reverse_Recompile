# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/fillbullet/p1007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/fillbullet/p1007.pyc
# Source Generated with Decompyle++
# File: p1007.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL

class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.FillBullet(skill, cl_action.GetWeaponIntAttr(skill, 'MaxBullet'), 1)

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
            cls.EnableShow(skill, cl_action.GetWeaponIntAttr(skill, 'FillTime'), 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 1, index = 0)

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
            cls.EnableShow(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SelfDamage(skill, skill.m_Cache['HPConsumption'], DAM_TYPE_PERFORM, DAM_USE_ALL, DAM_TYPE_TRUE, 1)
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

from cl_perform.fillbullet import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 1007
    m_Name = '1007换弹'
    m_ExtPerform = ()
    m_HaltInfo = {
        40108: 1,
        10149: 1,
        20149: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'HPConsumption': 3000 }
    m_ForbidRule = 1003
    
    def CanUse(self, oWarrior, dInfo):
        if not super(CPerform, self).CanUse(oWarrior, dInfo):
            return 0
        oWeapon = self.GetMyItem()
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        if oBulletCom.Bullet() >= oBulletCom.MaxBullet():
            return 0
        if oWarrior.HP() + oWarrior.Shield() + oWarrior.Armor() < self.CalAttr('HPConsumption'):
            return 0
        return 1


