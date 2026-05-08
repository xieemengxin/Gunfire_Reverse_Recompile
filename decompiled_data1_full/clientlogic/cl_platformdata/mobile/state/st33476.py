# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33476.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33476.pyc
# Source Generated with Decompyle++
# File: st33476.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_platformdata.custom.state.customaction import CustomAction33476 as CustomAction
import cl_state
from cl_commondefines import LEVEL_TYPE_FIGHT, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func736

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventLevelType(oTarget, oEventCB, LEVEL_TYPE_FIGHT):
        cl_evact.EventCBAddCustomInfo(oTarget, oEventCB, 'st33476-num', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('StateCount'))
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
            'SID': 1067,
            'ForceNum': (lambda *a: max(1, int(min(Func736(*a, **{
'sKey': 'st33476-num' }), 3)))),
            'Radius': 3,
            'OffsetY': 2 })


class CState(cl_state.CState):
    m_SID = 33476
    m_Name = '#NT#灵力奔涌金爵'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0 }

