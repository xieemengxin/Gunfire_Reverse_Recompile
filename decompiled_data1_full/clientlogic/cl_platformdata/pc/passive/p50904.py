# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p50904.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p50904.pyc
# Source Generated with Decompyle++
# File: p50904.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HALL, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL
from cl_newformula import Func201

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenLevelCtrlMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREREWARD_RELICLOTTERY, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'NPC') == 1069:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func201(*a))) != 1 or cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_HALL) == 0:
            cl_evact.EventCBReplaceCreateNpc(oWarrior, oEventCB, 30011071)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckInputRelicLotteryQuality(oWarrior, oEventCB, QUALITY_TYPE_LOW):
        cl_evact.EventCBModifyInputRelicLotteryQuality(oWarrior, oEventCB, QUALITY_TYPE_NORMAL)


class CPerform(CCustomPerform):
    m_SID = 50904
    m_Name = '#NT#卡包-局内合成调整'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

