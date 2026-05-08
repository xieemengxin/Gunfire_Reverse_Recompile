# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/careerpf/p1326.pyc
# RelativePath: clientlogic/cl_platformdata/pc/careerpf/p1326.pyc
# Source Generated with Decompyle++
# File: p1326.pyc (Python 3.6)

from cl_commondefines import SKILLRET_FAIL, DEBUG_STATUS_NOPFCD
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_state
from cl_perform.cartoon.defines import DirectPosCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, INK_DAMAGE, OBJ_ENEMY

class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.PerformThumpMonster(skill, 10000, 150, 1)
        cl_action.SetSkillServerCache(skill, 'ExShowTips', [
            INK_DAMAGE][0])
        cl_action.PerformDamage(skill, {
            'Att': skill.m_Cache['Att'] })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgSelfPos(skill), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetAttackerPerformAttr(skill, 1326, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgSelfPos(skill), (0, 0, 0), [
                cl_action.GetAttackerPerformAttr(skill, 1326, 'Radius')], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = True, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

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
        cartoon = { }
        CCartoon3.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 20, 1)
        else:
            cls.EnableCtrl(skill, 20, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

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
            cls.EnableShow(skill, 30, 1)
        else:
            cls.EnableCtrl(skill, 30, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.careerpf import CPFBulletPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1326
    m_Name = '浊墨爆炸'
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
        'MaxCover': 1,
        'UseInterval': 35,
        'AddStateTime': 200,
        'Att': 45000,
        'CrazyEff': 10000,
        'BulletSpeed': 70,
        'DebuffProb': 3300,
        'ExplodeDelay': 0,
        'Radius': 5,
        'BulletVerticalAcc': 18,
        'ThumpProb': 0,
        'DamInterval': 0,
        'Pierce': 0,
        'MinUseEnergy': 0,
        'MaxPFBullet': 999,
        'PFBulletUse': 15,
        'PFBulletRecover': 1,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'State_Time': 500,
        'CheckHeroState': 33044,
        'CostFramePer': 20 }
    m_AIPerformDam = 600
    
    def CanUse(self, oWarrior, dInfo):
        oState = oWarrior.m_State.GetItemBySID(self.GetArgValue('CheckHeroState'))
        if not oState:
            return SKILLRET_FAIL
        iRemainFrame = oState.GetRemainTime()
        if iRemainFrame <= 0:
            return SKILLRET_FAIL
        dInfo['NoPFBulletUse'] = 1
        return super().CanUse(oWarrior, dInfo)

    
    def UsePerform(self, oWarrior, oSkill):
        if oWarrior.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD != DEBUG_STATUS_NOPFCD:
            oWarrior.m_Perform.AddColdTime(self.m_SID, self.GetCDTime(oWarrior), iActNum = oSkill.m_Base['ActNum'])
        oWarrior.m_Perform.AddUseInterval(self.m_SID, self.GetUseInterval(oWarrior))
        self.SendUseMsg(oWarrior, oSkill)
        iPFBulletUse = self.CalAttr('PFBulletUse')
        if self.m_CurPFBullet < iPFBulletUse:
            oState = oWarrior.m_State.GetItemBySID(self.GetArgValue('CheckHeroState'))
            if oState:
                iExtra = iPFBulletUse - self.m_CurPFBullet
                cl_state.AddTime(oState, oWarrior, -self.GetArgValue('CostFramePer', 10) * iExtra, oState.GetTime())
        oWarrior.m_InkCon.ModifyInkValue(-iPFBulletUse, 'From1326')
        self.DoAction(oSkill)


