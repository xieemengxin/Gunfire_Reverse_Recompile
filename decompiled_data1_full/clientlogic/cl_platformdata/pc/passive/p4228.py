# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4228.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4228.pyc
# Source Generated with Decompyle++
# File: p4228.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 10)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 35, HP_RADIO_SUB, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 9, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    305: 10,
                    306: 10 }, {
                    2: 10 }, 0, 2)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 65:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    405: 10,
                    406: 10,
                    407: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    505: 10,
                    506: 10,
                    507: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    705: 10,
                    706: 10,
                    707: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 40:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    805: 10,
                    807: 10,
                    808: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    905: 10,
                    907: 10,
                    908: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    1105: 10,
                    1107: 10,
                    1108: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetRefreshMonsterTimeInterval(oWarrior, oEventCB) >= 850:
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    305: 10,
                    306: 10 }, {
                    2: 10 }, 0, 2)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 65:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    405: 10,
                    406: 10,
                    407: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    505: 10,
                    506: 10,
                    507: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    705: 10,
                    706: 10,
                    707: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 40:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    805: 10,
                    807: 10,
                    808: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    905: 10,
                    907: 10,
                    908: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    1105: 10,
                    1107: 10,
                    1108: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)
    cl_evact.CommonCBAddPerform(oWarrior, oEventCB, 4229)


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    305: 10,
                    306: 10 }, {
                    2: 10 }, 0, 2)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 65:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    405: 10,
                    406: 10,
                    407: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    505: 10,
                    506: 10,
                    507: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    705: 10,
                    706: 10,
                    707: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 40:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    805: 10,
                    807: 10,
                    808: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    905: 10,
                    907: 10,
                    908: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    1105: 10,
                    1107: 10,
                    1108: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
    if cl_evcon.GetRefreshMonsterTimeInterval(oWarrior, oEventCB) >= 850:
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    305: 10,
                    306: 10 }, {
                    2: 10 }, 0, 2)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 65:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    405: 10,
                    406: 10,
                    407: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    505: 10,
                    506: 10,
                    507: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    705: 10,
                    706: 10,
                    707: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 40:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    805: 10,
                    807: 10,
                    808: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    905: 10,
                    907: 10,
                    908: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    1105: 10,
                    1107: 10,
                    1108: 10 }, {
                    1: 10 }, 0, 1)
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4228
    m_Name = '二幕宝箱怪刷怪-阶段1'
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
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 1

