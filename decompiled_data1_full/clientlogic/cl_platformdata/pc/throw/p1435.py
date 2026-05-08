# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1435.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1435.pyc
# Source Generated with Decompyle++
# File: p1435.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, OBJ_ENEMY, STATE_CLS_ABNORMAL

class CCartoon5(DirectPosCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.VictimAddState(skill, 33752, 150, 0, { })
        cl_action.PerformDamage(skill, {
            'Att': cl_action.ToInt(skill, skill.m_Cache['Att'] * 25 / 100) }, dArgs = { })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfCenterPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfCenterPos(skill), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.RemoveTargetsAllStateByType(skill, [
            cl_action.GetSkillAID(skill)], STATE_CLS_ABNORMAL)
        cl_action.PerformCure(skill, cl_action.ToInt(skill, (cl_action.GetAttackerAttr(skill, 'HPMax') + cl_action.GetAttackerAttr(skill, 'ShieldMax')) * 20 / 100), iPointTarget = cl_action.GetSkillAID(skill))
        cl_action.AttackerAddState(skill, 33751, 300, 0, { })
        if cl_action.CheckHasState(skill, 33605):
            cl_action.SetAttackStateStatistics(skill, 33605, 'KeepBigLion', 1)
            cl_action.AttackerRemoveState(skill, 33605, bSameItem = False)
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 40, 1)
        else:
            cls.EnableCtrl(skill, 40, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SendUseThrowPFMsg(skill)
    cl_action.ApplyStateTransDamFactor(skill, 33604)
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

from cl_perform.throw import CEnergyPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1435
    m_Name = '御势'
    m_ExtPerform = ()
    m_HaltInfo = {
        377: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 30000,
        'CrazyEff': 0,
        'BulletSpeed': 0,
        'DebuffProb': 2000,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 200,
        'KeepTime': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 3000 }
    m_ForbidRule = 1012
    m_CheckForbid = 1010
    m_BaseArgData = {
        'EnergyCost': 3000 }
    m_UnCrtByOwnerSign = 1
    m_AIPerformDam = 2000
    
    def CanUse(self, oWarrior, dInfo):
        oState = oWarrior.m_State.GetItemBySID(33760)
        if oState and oState.m_CurCount > 0:
            dInfo['PerformUseNoCost'] = 1
        return super().CanUse(oWarrior, dInfo)


