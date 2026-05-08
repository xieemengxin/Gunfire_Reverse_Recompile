# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4172.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4172.pyc
# Source Generated with Decompyle++
# File: p4172.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetAllMonsterByTargetScene(oWarrior, oEventCB, 1, None, None)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 7101, 100, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 4172
    m_Name = '石巨人开场锁定'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

