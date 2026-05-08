# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4227.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4227.pyc
# Source Generated with Decompyle++
# File: p4227.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 4)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
        if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 4 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                911: 10,
                912: 10,
                913: 10,
                914: 10,
                1011: 10,
                1012: 10,
                1013: 10,
                1014: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                1111: 10,
                1112: 10,
                1113: 10,
                1114: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        else:
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetRefreshMonsterTimeInterval(oWarrior, oEventCB) >= 500:
        if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 4 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                911: 10,
                912: 10,
                913: 10,
                914: 10,
                1011: 10,
                1012: 10,
                1013: 10,
                1014: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                1111: 10,
                1112: 10,
                1113: 10,
                1114: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        else:
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
        if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 4 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                911: 10,
                912: 10,
                913: 10,
                914: 10,
                1011: 10,
                1012: 10,
                1013: 10,
                1014: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                1111: 10,
                1112: 10,
                1113: 10,
                1114: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        else:
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
    if cl_evcon.GetRefreshMonsterTimeInterval(oWarrior, oEventCB) >= 500:
        if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 4 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                911: 10,
                912: 10,
                913: 10,
                914: 10,
                1011: 10,
                1012: 10,
                1013: 10,
                1014: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 6, {
                1111: 10,
                1112: 10,
                1113: 10,
                1114: 10 }, {
                1: 10 }, 0, 0)
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        else:
            cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4227
    m_Name = '一幕宝箱怪刷怪-阶段2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 1

