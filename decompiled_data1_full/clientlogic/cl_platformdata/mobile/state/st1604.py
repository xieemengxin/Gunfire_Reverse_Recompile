# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1604.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1604.pyc
# Source Generated with Decompyle++
# File: st1604.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_HP, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304, Func347

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 5:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, None, None)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 20 / 100 + 0), CURE_TYPE_PERFORM | DAM_USE_HP, -1, -1, None)
    cl_evact.EventAddBagBullet(oTarget, oEventCB, 4502, (lambda *a: Func347(*a, **{
'sid': 4502 }) * 20 / 100))
    cl_evact.EventAddBagBullet(oTarget, oEventCB, 4503, (lambda *a: Func347(*a, **{
'sid': 4503 }) * 20 / 100))
    cl_evact.EventAddBagBullet(oTarget, oEventCB, 4504, (lambda *a: Func347(*a, **{
'sid': 4504 }) * 20 / 100))
    cl_evact.StateAddSelfCount(oTarget, oEventCB, -5, None)


class CState(cl_state.CState):
    m_SID = 1604
    m_Name = '#NT#补给专家'
    m_Type = STATE_CLS_HELP
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

