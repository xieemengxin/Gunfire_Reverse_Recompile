# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/throw/p1435.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/throw/p1435.pyc
# Source Generated with Decompyle++
# File: p1435.pyc (Python 3.6)

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


