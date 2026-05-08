# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9790.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9790.pyc
# Source Generated with Decompyle++
# File: p9790.pyc (Python 3.6)

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
from cl_commondefines import DPSUBMSG_DEFAULT

class CPerform(CCustomPerform):
    m_SID = 9790
    m_Name = '#NT#s元素法杖'
    m_ExtPerform = ()
    m_HaltInfo = {
        103: 1,
        108: 1,
        40108: 1,
        10214: 1,
        143: 1,
        286: 1 }
    m_IgnoreHalt = {
        1801: 1,
        1310: 1 }
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
        'MaxPFBullet': 21000,
        'PFBulletUse': 3000,
        'PFBulletRecover': 1000,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_DPSubMsg = DPSUBMSG_DEFAULT
    m_ClassifyTag = ()
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 0
    m_CheckForbid = 1019

