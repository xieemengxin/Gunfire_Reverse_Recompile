# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8031.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8031.pyc
# Source Generated with Decompyle++
# File: st8031.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
from cl_object.logging import CgLog
import cl_state
from cl_commondefines import FIGHT_KEY_WUDI, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func432

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)
    cl_action.CommonHalt(oTarget, oLifeCycle, { }, { })
    cl_action.CommonPauseMonsterOwnerAgent(oTarget, oLifeCycle)
    cl_action.CommonPausePlayerStateCounter(oTarget, oLifeCycle, (lambda *a: Func432(*a)), 1005)
    cl_action.CommonPausePlayerStateCounter(oTarget, oLifeCycle, (lambda *a: Func432(*a)), 20026)
    cl_action.CommonAddSpecialKey(oTarget, oLifeCycle, FIGHT_KEY_WUDI, None)


def StateRemoveAction(oTarget, oLifeCycle):
    CustomAction(oTarget, oLifeCycle, { })
    cl_action.StateAddState(oTarget, oLifeCycle, 1042, 0, { }, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBAddSelfTime(oTarget, oEventCB, 2000, 6000)


class CState(cl_state.CState):
    m_SID = 8031
    m_Name = '#NT#boss播放CG期间'
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }


def CustomAction(oTarget, oLifeCycle, dInfo):
    CgLog.Debug(f'''monster {oTarget.m_SID} cg end''')

