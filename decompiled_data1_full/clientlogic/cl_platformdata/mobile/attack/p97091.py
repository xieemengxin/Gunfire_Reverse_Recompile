# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p97091.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p97091.pyc
# Source Generated with Decompyle++
# File: p97091.pyc (Python 3.6)

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

class CPerform(CCustomPerform):
    m_SID = 97091
    m_Name = '#NT#聚能法杖右键'
    m_ExtPerform = (5306,)
    m_HaltInfo = {
        40108: 1,
        30108: 1,
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
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0,
        'MaxPFBullet': 16000,
        'PFBulletUse': 16000,
        'PFBulletRecover': 1000,
        'CostPFBulletDuringUse': 1,
        'PFBulletRecoverMul': 10000,
        'PFBulletCostMul': 10000 }
    m_ClassifyTag = (2,)
    m_BulletUse = 0
    m_IsMinor = 1
    m_ForbidRule = 1099
    m_CheckForbid = 1019

