# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/attack/p9020.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/attack/p9020.pyc
# Source Generated with Decompyle++
# File: p9020.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondecorator import CheckFaultTolerance

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
    m_SID = 9020
    m_Name = '#NT#双发步枪'
    m_ExtPerform = (5317,)
    m_HaltInfo = {
        40108: 1,
        30108: 1,
        10214: 1,
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
        'ChargeTime': 0 }
    m_BulletUse = 1
    m_ForbidRule = 0
    m_CheckForbid = 1001
    
    def Refresh(self):
        for sAttr in ('CommonMaxCount', 'TriggerTimes'):
            if sAttr in self.m_Attr:
                oAttr = self.m_Attr[sAttr]
                oAttr.Refresh(self)
        
        return super(CPerform, self).Refresh()

    Refresh = CheckFaultTolerance(Refresh)

