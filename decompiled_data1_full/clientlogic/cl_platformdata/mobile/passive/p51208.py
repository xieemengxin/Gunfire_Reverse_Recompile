# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51208.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51208.pyc
# Source Generated with Decompyle++
# File: p51208.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CHANGEWARCASHSUBMSG_COST
from cl_newformula import Func364, Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_COST, 0, 0, 0)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 2000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_COST, 0, 0, 0)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 2000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDCASH, CHANGEWARCASHSUBMSG_COST, 0, 0, 0)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 2000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBAddSavedData(oWarrior, oEventCB, '51208_Count', (lambda *a: -Func364(*a)), 1)
    cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': '51208_Count' })))
    if cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) >= 2000:
        cl_evact.PassiveCBReplaceSourceWand(oWarrior, oEventCB, 1002)
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '51208_Count', 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetWandCount(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': '51208_Count' })))
    if cl_condition.CommonGetSourceWandCount(oWarrior, oEventCB.GetCBLifeCycle()) >= 2000:
        cl_evact.PassiveCBReplaceSourceWand(oWarrior, oEventCB, 1002)
        cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), '51208_Count', 0)


class CPerform(CCustomPerform):
    m_SID = 51208
    m_Name = '初始钱龙被动'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

