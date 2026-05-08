# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13702.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13702.pyc
# Source Generated with Decompyle++
# File: p13702.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 300, 300, 0)
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 10000, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0)


class CPerform(CCustomPerform):
    m_SID = 13702
    m_Name = '无限火力'
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
    m_DieDisable = 1
    m_Career = None

