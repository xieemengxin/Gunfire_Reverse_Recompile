# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9796.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9796.pyc
# Source Generated with Decompyle++
# File: p9796.pyc (Python 3.6)

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
    m_SID = 9796
    m_Name = '#NT#召唤法杖'
    m_ExtPerform = (7021, 7356, 7357)
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
        'MaxPFBullet': 40000,
        'PFBulletUse': 30000,
        'PFBulletRecover': 2000,
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

