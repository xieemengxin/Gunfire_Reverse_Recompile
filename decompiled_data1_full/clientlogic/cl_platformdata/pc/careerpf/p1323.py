# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1323.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1323.pyc
# Source Generated with Decompyle++
# File: p1323.pyc (Python 3.6)

from cl_commondefines import STATA_QIANSUISHIELD
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_war
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER, SKILLCACHE_PERFORMMODE

class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cl_action.AttackerRemoveState(skill, 32774, bSameItem = False)

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
            cls.EnableShow(skill, 50, 1)
        else:
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cl_action.AttackerAddState(skill, 32774, skill.m_Cache['AddStateTime'], 0, { })

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
            cls.EnableShow(skill, 10, 1)
        else:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    if cl_action.GetSkillCacheData(skill, SKILLCACHE_PERFORMMODE) == 1 or cl_action.IsHeroCtrl(skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)
    else:
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return [
        SKILLCACHE_PERFORMMODE]


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1323
    m_Name = '潮汐之盾'
    m_ExtPerform = (1428,)
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
        'ColdTime': 1400,
        'AttDistance': 0,
        'MaxCover': 1,
        'UseInterval': 20,
        'AddStateTime': 500,
        'Att': 70000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 4000,
        'ExplodeDelay': 0,
        'Radius': 0,
        'BulletVerticalAcc': 0,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0 }
    m_ForbidRule = 1012
    m_CheckForbid = 1013
    m_AIPerformDam = 2800
    
    def UsePerform(self, oWarrior, oSkill):
        iCancelShield = 0
        if oSkill.m_CheckType == CRT_CHECK_SERVER and 'CancelShield' in oSkill.m_Custom:
            iCancelShield = 1
            if oWarrior.m_State.GetItemBySID(STATA_QIANSUISHIELD):
                cl_action.SetSkillCacheData(oSkill, SKILLCACHE_PERFORMMODE, 1)
            else:
                oSkill.Halt('noshield')
                return None
        super().UsePerform(oWarrior, oSkill)
        if iCancelShield:
            oPerform = oWarrior.GetPerform(1428)
            if not oPerform:
                return None
            if not oWarrior.m_Agent:
                return None
            vCur = oWarrior.GetPos()
            oTarget = oWarrior.m_Agent.GetLockTarget()
            if oTarget:
                vTarget = oTarget.GetPos()
            else:
                vTarget = cl_math.Vec3DisplaceDir(vCur, oWarrior.GetFacing(), 1)
            dData = {
                'Custom': {
                    'CameraCenterPos': cl_math.Vec3Add(vCur, (0, 0.1, 0)) },
                'vEnd': vTarget }
            oPerform.AddCanUseCount(1)
            cl_war.UsePerform(oWarrior, oPerform, dData)


