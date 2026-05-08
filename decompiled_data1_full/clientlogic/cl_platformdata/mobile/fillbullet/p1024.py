# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/fillbullet/p1024.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/fillbullet/p1024.pyc
# Source Generated with Decompyle++
# File: p1024.pyc (Python 3.6)

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

from cl_perform.fillbullet import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_SID = 1024
    m_Name = '浮游炮换弹'
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
        'HPConsumption': 0 }
    m_ForbidRule = 1010
    m_PassRule = {
        1012: 1,
        1051: 1,
        1062: 1,
        1064: 1,
        1065: 1,
        1085: 1 }

