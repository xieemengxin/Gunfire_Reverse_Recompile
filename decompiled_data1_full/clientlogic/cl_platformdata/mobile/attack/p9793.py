# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9793.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9793.pyc
# Source Generated with Decompyle++
# File: p9793.pyc (Python 3.6)

from cl_cscommondef import DEPUTY_HOLD, MAIN_HOLD
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon

def Action(skill):
    pass


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCache():
    return []

from cl_perform.attack import CPerform as CCustomPerform
from cl_commondefines import DPSUBMSG_NOFIRE

class CPerform(CCustomPerform):
    m_SID = 9793
    m_Name = '#NT#浮游炮右键'
    m_ExtPerform = (4386, 5302)
    m_HaltInfo = {
        40108: 1,
        10214: 1,
        143: 1 }
    m_IgnoreHalt = {
        1310: 1,
        1801: 1 }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 80,
        'AttDistance': 0,
        'ChargeTime': 1000,
        'MaxPFBullet': 24000,
        'PFBulletUse': 300,
        'PFBulletRecover': 600,
        'CostPFBulletDuringUse': 0,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = (3,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_PassRule = {
        1012: 1,
        1051: 1,
        1062: 1,
        1064: 1,
        1065: 1,
        1005: 1,
        1085: 1 }
    m_CheckForbid = 1019
    
    def CanUse(self, oWarrior, dData):
        if self.m_Game.m_SkillMgr.GetSkillBySource(self.m_SID, self.m_Owner, self.m_Item):
            return False
        if oWarrior.Query('DualState'):
            oMyWeapon = self.GetMyItem()
            iOtherHold = MAIN_HOLD if oMyWeapon.GetComponent('Hold').HoldPos() == DEPUTY_HOLD else DEPUTY_HOLD
            oOtherWeapon = oWarrior.m_WieldCon.GetCurWeapon(iOtherHold)
            if oMyWeapon.m_SID == oOtherWeapon.m_SID and self.m_Game.m_SkillMgr.GetSkillBySource(self.m_SID, self.m_Owner, oOtherWeapon.m_ID):
                return True
        if self.CurPFBullet() < self.MaxPFBullet():
            return False
        return super(CPerform, self).CanUse(oWarrior, dData)


