# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season5/t1033.pyc
# RelativePath: clientlogic/cl_season/pc/season5/t1033.pyc
# Source Generated with Decompyle++
# File: t1033.pyc (Python 3.6)

from cl_commondefines import SEASONSUBTASK_TYPE_ADD, SEASONTASK_EXTINFO_TYPE_WAND, VIRTUAL_ITEM_WAND, WAND_QUALITY_TALE, WAND_SUBMSG_ADD, WAND_SUBMSG_UPGRADE
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from branch import *
from ...mobject import CSeasonTask as CCustom

def RewardAction(oTarget, sReason):
    pass


def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_UPGRADE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBCheckItemQuality(oListener, oEventCB, WAND_QUALITY_TALE, VIRTUAL_ITEM_WAND):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_WAND, 0, 1, SEASONSUBTASK_TYPE_ADD, 1)
        if cl_evcon.CheckInPointWand(oListener, oEventCB, {
            1002: 1 }):
            cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_WAND, 1008, 1, SEASONSUBTASK_TYPE_ADD, 0)
        elif cl_evcon.CheckInPointWand(oListener, oEventCB, {
            1010: 1 }):
            cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_WAND, 1009, 1, SEASONSUBTASK_TYPE_ADD, 0)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckInPointWand(oListener, oEventCB, {
        1002: 1 }):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_WAND, 1008, 1, SEASONSUBTASK_TYPE_ADD, 0)
    elif cl_evcon.CheckInPointWand(oListener, oEventCB, {
        1010: 1 }):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_WAND, 1009, 1, SEASONSUBTASK_TYPE_ADD, 0)


def DoCallBackAction2(oEventCB, oListener):
    if cl_evcon.CheckInPointWand(oListener, oEventCB, {
        1010: 1 }):
        cl_evact.CBAddWarSeasonSonTaskValue(oListener, oEventCB, SEASONTASK_EXTINFO_TYPE_WAND, 1009, 1, SEASONSUBTASK_TYPE_ADD, 0)


class CSeasonTask(CCustom):
    m_SID = 1033
    m_TargetValue = 16
    m_TaskValue = 1000
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_WarExtInfoType = [
        SEASONTASK_EXTINFO_TYPE_WAND]
    m_SubTaskInfo = {
        SEASONTASK_EXTINFO_TYPE_WAND: {
            1002: 1,
            1003: 1,
            1005: 1,
            1006: 1,
            1007: 1,
            1008: 1,
            1009: 1,
            1010: 1,
            1011: 1,
            1012: 1,
            1013: 1,
            1015: 1,
            1016: 1,
            1018: 1,
            1019: 1,
            1020: 1 } }

