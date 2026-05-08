# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9795.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9795.pyc
# Source Generated with Decompyle++
# File: p9795.pyc (Python 3.6)

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

from cl_perform.attack import CChargePerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 9795
    m_Name = 's速射弓'
    m_ExtPerform = (5315, 5340)
    m_HaltInfo = {
        40108: 1,
        143: 1 }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 43,
        'AttDistance': 0,
        'ChargeTime': 40,
        'MaxPFBullet': 30000,
        'PFBulletUse': 30000,
        'PFBulletRecover': 1500,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000,
        'TriggerTimes': 1 }
    m_ClassifyTag = (2,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1045
    m_CheckForbid = 1019

