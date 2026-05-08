# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25778.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25778.pyc
# Source Generated with Decompyle++
# File: p25778.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 3000, 0, -1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 1000, 1000, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'RefreshStepLastPos', 0)
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1951, -1, { })


class CPerform(CCustomPerform):
    m_SID = 25778
    m_Name = '刷步神器'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5778
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

