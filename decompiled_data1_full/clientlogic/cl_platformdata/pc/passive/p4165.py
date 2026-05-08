# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4165.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4165.pyc
# Source Generated with Decompyle++
# File: p4165.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetRefreshMonsterTimeInterval(oWarrior, oEventCB) >= 500:
        if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 7 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                16: 10,
                17: 10,
                18: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                12: 10,
                13: 10 }, {
                1: 10 }, 0, -1)
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                19: 10,
                20: 10,
                21: 10 }, {
                1: 10 }, 200, 0)
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        else:
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4165
    m_Name = '三幕宝箱怪刷怪-阶段2'
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
    m_DieDisable = 1

