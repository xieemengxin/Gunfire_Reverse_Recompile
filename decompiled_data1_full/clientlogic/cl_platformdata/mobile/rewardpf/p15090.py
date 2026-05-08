# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15090.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15090.pyc
# Source Generated with Decompyle++
# File: p15090.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.rewardpf.customaction import CustomAction15090 as CustomAction
from . import CPerform as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HALL, LEVEL_TYPE_HIDE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33158, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33159, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0 and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HALL) == 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 30):
        CustomAction(oWarrior, oEventCB, {
            'IsCurse': 0,
            'Level': 1,
            'Count': 1,
            'StateSID': 33158,
            'Pfid': 15090 })


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'pick', 0) and cl_evcon.EventCBCheckFirstGetRelic(oWarrior, oEventCB) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 5):
        CustomAction(oWarrior, oEventCB, {
            'IsCurse': 1,
            'Level': 1,
            'Count': 1,
            'StateSID': 33159,
            'Pfid': 15090 })


class CPerform(CCustomPerform):
    m_SID = 15090
    m_Name = '#NT#穷达有命'
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

