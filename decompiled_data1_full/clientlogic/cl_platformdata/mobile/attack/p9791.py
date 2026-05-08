# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9791.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9791.pyc
# Source Generated with Decompyle++
# File: p9791.pyc (Python 3.6)

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
    m_SID = 9791
    m_Name = '#NT#s标记法杖'
    m_ExtPerform = (4383, 5303, 12026, 1722)
    m_HaltInfo = {
        40108: 1,
        10149: 1,
        143: 1 }
    m_IgnoreHalt = { }
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
        'PFBulletUse': 2400,
        'PFBulletRecover': 2400,
        'CostPFBulletDuringUse': 0,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_DPSubMsg = DPSUBMSG_NOFIRE
    m_ClassifyTag = (4,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1079
    m_PassRule = {
        1012: 1,
        1064: 1,
        1051: 1 }
    m_CheckForbid = 1019
    
    def CanUse(self, oWarrior, dData):
        if self.CurPFBullet() < self.MaxPFBullet():
            return False
        return super(CPerform, self).CanUse(oWarrior, dData)


