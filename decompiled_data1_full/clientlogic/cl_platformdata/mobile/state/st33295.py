# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33295.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33295.pyc
# Source Generated with Decompyle++
# File: st33295.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import COST_BAGBULLET_WEAPON, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func208, Func215, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0)
    cl_action.CommonListenOwnerMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 1)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 3, 1, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'RelifeTime', (lambda *a: -Func404(*a) * 1000), 0, 0)
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) >= 9:
        cl_action.CommonDoneOwnerEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1)
        cl_action.CommonDoneOwnerEvent(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func208(*a)), 'ConsumeBullet')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ConsumeBullet') >= 5:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddCount', cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ConsumeBullet') // 5)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddCount') * 5, 'ConsumeBullet')
        cl_evact.StateAddSelfCount(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddCount'), None)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func215(*a)), 'ConsumeBullet')
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ConsumeBullet') >= 5:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddCount', cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'ConsumeBullet') // 5)
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddCount') * 5, 'ConsumeBullet')
        cl_evact.StateAddSelfCount(oTarget, oEventCB, cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'AddCount'), None)


def CallBack3(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33295
    m_Name = '#NT#词条50615'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 9
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3 }

