# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14414.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14414.pyc
# Source Generated with Decompyle++
# File: p14414.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import NWARRIOR_DROP_KEYITEM
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonRemoveState(oWarrior, oLifeCycle, 7139)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7158, 0, { }, 1)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 39068)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SWITCH_PHASE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckMonsterPhase(oWarrior, oEventCB, 6):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'EnablePf39054', 1)
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DROP, -1, 2)
        cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_LEVEL_STARTSPAWN, -1, 3)
    elif cl_evcon.CheckMonsterPhase(oWarrior, oEventCB, 7):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7157, 1500, { }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_KEYITEM):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'EnablePf39054', 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'GroupID' }))) == 99:
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'EnablePf39054', 1)


class CPerform(CCustomPerform):
    m_SID = 14414
    m_Name = '轮回10-夜姬丸'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

