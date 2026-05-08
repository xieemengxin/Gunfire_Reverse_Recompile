# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14412.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14412.pyc
# Source Generated with Decompyle++
# File: p14412.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 39098)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39091, 'ChangeStoneNumFactor', 2, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39096, 'ChangeStoneNumFactor', 2, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 39098)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39091: 1,
        39096: 1 }, 1, 0):
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 39098, -1, {
            'StoneNum': (lambda *a: Func651(*a, **{
'sKey': 'StoneNum' }) // 2) })


class CPerform(CCustomPerform):
    m_SID = 14412
    m_Name = '轮回10-连城'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

