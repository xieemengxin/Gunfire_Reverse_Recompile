# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32707.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32707.pyc
# Source Generated with Decompyle++
# File: st32707.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from . import statedata
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1316, 'Att', (0, None, ((404,), (lambda a0: 1500 * a0))), 0)
    cl_action.CommonChangePerformAttr(oTarget, oLifeCycle, 1318, 'Att', (0, None, ((404,), (lambda a0: 1500 * a0))), 0)
    cl_action.CommonSendStateCountChangeMessage(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1316, 0, 0) and cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'pf13529', None) == 0:
        cl_evact.StateAddSelfCount(oTarget, oEventCB, -10)


class CState(statedata.CStateData):
    m_SID = 32707
    m_Name = '怒焰奔腾'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 30
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

