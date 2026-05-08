# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st8069.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st8069.pyc
# Source Generated with Decompyle++
# File: st8069.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ENEMY, PLAYMODE_NEWSURVIVOR, PLAYMODE_SURVIVOR, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func430

def StateRemoveAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func430(*a, **{
'sid': 8069 }))) == 0:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckWarPlayMode(oTarget, oEventCB, PLAYMODE_SURVIVOR) or cl_evcon.CheckWarPlayMode(oTarget, oEventCB, PLAYMODE_NEWSURVIVOR):
        cl_action.CommonSuperMonster(oTarget, oEventCB.GetCBLifeCycle(), {
            6151: 10,
            6152: 10,
            6153: 10,
            6154: 5,
            6155: 10,
            6156: 10,
            6157: 5,
            6158: 10,
            6159: 10,
            6160: 10,
            6161: 5,
            6165: 10 }, {
            6251: 10,
            6252: 10,
            6253: 10,
            6254: 10 })
    else:
        cl_action.CommonSuperMonster(oTarget, oEventCB.GetCBLifeCycle(), {
            6101: 10,
            6102: 10,
            6103: 10,
            6104: 5,
            6105: 10,
            6106: 10,
            6107: 5,
            6108: 10,
            6109: 10,
            6110: 10,
            6111: 5,
            6115: 10 }, {
            6201: 10,
            6202: 10,
            6203: 10,
            6204: 10 })


class CState(cl_state.CState):
    m_SID = 8069
    m_Name = '#NT#奉献强化'
    m_DieRemove = 1
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_ENEMY
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
    m_Action = (None, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

