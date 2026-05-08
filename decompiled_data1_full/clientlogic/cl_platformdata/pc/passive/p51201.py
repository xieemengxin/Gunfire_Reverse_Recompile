# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p51201.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p51201.pyc
# Source Generated with Decompyle++
# File: p51201.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CHANGEWARCASHSUBMSG_COST
from cl_newformula import Func364, Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33536, 0, { }, 1)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33536, (lambda *a: Func598(*a, **{
'sKey': '51201_Count' }) // 100), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_COST, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33536, 0, { }, 1)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33536, (lambda *a: Func598(*a, **{
'sKey': '51201_Count' }) // 100), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_COST, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33536, 0, { }, 1)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33536, (lambda *a: Func598(*a, **{
'sKey': '51201_Count' }) // 100), None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_COST, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddSavedData(oWarrior, oEventCB, '51201_Count', (lambda *a: -Func364(*a)), 1)
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33536, (lambda *a: Func598(*a, **{
'sKey': '51201_Count' }) // 100))


class CPerform(CCustomPerform):
    m_SID = 51201
    m_Name = '#NT#钱龙杖被动'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

