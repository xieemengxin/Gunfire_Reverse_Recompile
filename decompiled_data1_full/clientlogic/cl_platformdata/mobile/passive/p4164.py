# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4164.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4164.pyc
# Source Generated with Decompyle++
# File: p4164.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 10)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 50, HP_RADIO_SUB, 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, -1, 9, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 2 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 70:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 50:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetRefreshMonsterTimeInterval(oWarrior, oEventCB) >= 800:
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 2 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 70:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 50:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)
    cl_evact.CommonCBAddPerform(oWarrior, oEventCB, 4165)


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)


def DoCallBackAction10(oEventCB, oWarrior):
    if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 2 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 70:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 50:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
    if cl_evcon.GetRefreshMonsterTimeInterval(oWarrior, oEventCB) >= 800:
        if cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 90:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 2 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 3, {
                    101: 10,
                    102: 10,
                    103: 10,
                    104: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 70:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 3 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 4, {
                    201: 10,
                    202: 10,
                    203: 10,
                    204: 10 }, {
                    0: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
        elif cl_evcon.GetListenerHPRatio(oWarrior, oEventCB) >= 50:
            if cl_evcon.GetSceneMonsterCnt(oWarrior, oEventCB, 1) <= 5 + 0.5 * (cl_evcon.GetRoomPlayerCnt(oWarrior, oEventCB) - 1):
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 0, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 50, 0)
                cl_evact.EventCBSummonAreaMonster(oWarrior, oEventCB, 5, {
                    301: 10,
                    302: 10,
                    303: 10,
                    304: 10,
                    401: 5,
                    402: 5,
                    403: 5,
                    404: 5 }, {
                    1: 10 }, 100, 1)
            else:
                cl_evact.CommonCBSetRefreshMonsterTime(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4164
    m_Name = '三幕宝箱怪刷怪-阶段1'
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
    m_DieDisable = 0

