# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13724.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13724.pyc
# Source Generated with Decompyle++
# File: p13724.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func598

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'benediction13724' }))):
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'benediction13724', 1)
        cl_action.CommonAddBlankRelic(oWarrior, oLifeCycle, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEBENED_BEFORE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33432, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CBCheckFromBenediction(oWarrior, oEventCB, 13724):
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'benediction13724', 0)


class CPerform(CCustomPerform):
    m_SID = 13724
    m_Name = '无为自化'
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
    m_Career = None

