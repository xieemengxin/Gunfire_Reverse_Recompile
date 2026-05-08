# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/pc/season3/t1027.pyc
# RelativePath: clientlogic/cl_season/pc/season3/t1027.pyc
# Source Generated with Decompyle++
# File: t1027.pyc (Python 3.6)

from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW, PF_TYPE_CAREERPF, PF_TYPE_THROW
from cl_newformula import Func336
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
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, PF_SUBMSG_CAREERPF, 1, 0, 0)
    if cl_condition.CheckHero(oListener, oLifeCycle, 217):
        cl_action.CommonListenServantMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_NORMAL, 2)
        cl_action.CommonListenServantMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, -1, 3)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.CheckPerformType(oListener, oEventCB, PF_TYPE_CAREERPF, 0) or cl_evcon.CheckPerformType(oListener, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.EventCBAddCollectInfo(oListener, oEventCB, 't1027_Kill', 1, 0)


def DoCallBackAction1(oEventCB, oListener):
    if cl_evcon.CheckSkillCollectInfo(oListener, oEventCB, 't1027_Kill', 0) > cl_evcon.SeasonTaskCBGetWarValue(oListener, oEventCB):
        cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 't1027_Kill' })))
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 15):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


def DoCallBackAction2(oEventCB, oListener):
    cl_evact.EventCBAddCollectInfo(oListener, oEventCB, 't1027_ServantKill', 1, 0)


def DoCallBackAction3(oEventCB, oListener):
    if cl_evcon.CheckSkillCollectInfo(oListener, oEventCB, 't1027_ServantKill', 0) > cl_evcon.SeasonTaskCBGetWarValue(oListener, oEventCB):
        cl_evact.CBSetWarSeasonTaskValue(oListener, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 't1027_ServantKill' })))
    if cl_evcon.SeasonTaskCBCheckWarValue(oListener, oEventCB, 15):
        cl_evact.CBAddSeasonTaskValue(oListener, oEventCB, 1)


class CSeasonTask(CCustom):
    m_SID = 1027
    m_TargetValue = 1
    m_TaskValue = 1000
    m_ShowTotalValue = 15
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_SubTaskExtProcess = 0
    m_Reward = RewardAction
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_WarExtInfoType = []
    m_SubTaskInfo = { }

