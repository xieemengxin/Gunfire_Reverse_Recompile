# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season7/t1020.pyc
# RelativePath: clientlogic/cl_season/pc/season7/t1020.pyc
# Source Generated with Decompyle++
# File: t1020.pyc (Python 3.6)

from cl_commondefines import CRTSTAL_RAWMATERIAL, S7CRYSTAL_ADD
from cl_newformula import Func651
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, S7CRYSTAL_ADD, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if not cl_evcon.EventCBCrystalType(oListener, oEventCB, CRTSTAL_RAWMATERIAL) and cl_evcon.SeasonTaskCBGetWarDictData(oListener, oEventCB, 'CrystalID', (lambda *a: Func651(*a, **{
'sKey': 'S7Item' }))):
        cl_evact.CBAddWarSeasonTaskDictData(oListener, oEventCB, 'CrystalID', (lambda *a: Func651(*a, **{
'sKey': 'S7Item' })), 1)
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction1(oEventCB, oListener):
    if not cl_evcon.SeasonTaskCBGetWarDictData(oListener, oEventCB, 'CrystalID', (lambda *a: Func651(*a, **{
'sKey': 'S7Item' }))):
        cl_evact.CBAddWarSeasonTaskDictData(oListener, oEventCB, 'CrystalID', (lambda *a: Func651(*a, **{
'sKey': 'S7Item' })), 1)
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1020
    m_TargetValue = 15
    m_TaskValue = 500
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

