# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4166.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4166.pyc
# Source Generated with Decompyle++
# File: p4166.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MG_SOURCE_KILLMONSTER, PLAYMODE_DAYLY_TRIAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 50:
        cl_evact.CommonCBDropReward(oWarrior, oEventCB, {
            101: 20,
            401: 1 }, {
            101: 10000,
            401: 10000 }, None, MG_SOURCE_KILLMONSTER, None, None)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 23411, 0, { })
    elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 25:
        cl_evact.CommonCBDropReward(oWarrior, oEventCB, {
            101: 25,
            401: 1,
            1001: 1 }, {
            101: 10000,
            401: 10000,
            1001: 10000 }, None, MG_SOURCE_KILLMONSTER, None, None)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 23411, 0, { })
    elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) > 0:
        cl_evact.CommonCBDropReward(oWarrior, oEventCB, {
            101: 30,
            401: 1,
            1001: 1,
            2401: 1 }, {
            101: 10000,
            401: 10000,
            1001: 10000,
            2401: 10000 }, None, MG_SOURCE_KILLMONSTER, None, None)
        cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 23411, 0, { })
    elif cl_condition.CheckWarPlayMode(oWarrior, oEventCB.GetCBLifeCycle(), PLAYMODE_DAYLY_TRIAL):
        cl_evact.CommonCBDropReward(oWarrior, oEventCB, {
            101: 40,
            401: 1,
            1001: 1,
            2401: 2 }, {
            101: 10000,
            401: 10000,
            1001: 10000,
            2401: 10000 }, 225, MG_SOURCE_KILLMONSTER, None, None)
    else:
        cl_evact.CommonCBDropReward(oWarrior, oEventCB, {
            101: 40,
            401: 1,
            1001: 1,
            2401: 2,
            501: 20 }, {
            101: 10000,
            401: 10000,
            1001: 10000,
            2401: 10000,
            501: 10000 }, 225, MG_SOURCE_KILLMONSTER, None, None)


class CPerform(CCustomPerform):
    m_SID = 4166
    m_Name = '宝箱怪掉落奖励'
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

