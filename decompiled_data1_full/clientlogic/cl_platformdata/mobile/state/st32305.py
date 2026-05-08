# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st32305.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st32305.pyc
# Source Generated with Decompyle++
# File: st32305.pyc (Python 3.6)

import cl_object.reason
import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_ATTACK, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func304

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 1306, 0, None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        if cl_condition.HasState(oTarget, oEventCB.GetCBLifeCycle(), 32473):
            if oTarget.HP() > cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * (0.3 + cl_evcon.CheckTalentLevel(oTarget, oEventCB, 2401) / 10))):
                cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.3 + Func304(*a, **{
'sAttr': 'HPMax' }) * cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2401) / 10))
                CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
                    'iChange': (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 0.3 + Func304(*a, **{
'sAttr': 'HPMax' }) * cl_action.CommonGetTalentLevel(oTarget, oEventCB.GetCBLifeCycle(), 2401) / 10) })
            else:
                cl_action.CommonHaltPointPerform(oTarget, oEventCB.GetCBLifeCycle(), 1306)
        else:
            cl_evact.StateCBAddVictimState(oTarget, oEventCB, 32477, 1000, 0, {
                'Damage': (lambda *a: 0.1 * Func304(*a, **{
'sAttr': 'HP' })) }, 0, None, None)
            cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HP' }) * 0.1))
            CustomAction(oTarget, oEventCB.GetCBLifeCycle(), {
                'iChange': (lambda *a: Func304(*a, **{
'sAttr': 'HP' }) * 0.1) })


class CState(cl_state.CState):
    m_SID = 32305
    m_Name = '#NT#吸血和耗血'
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
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        1: CallBack1 }


def CustomAction(oWarrior, oLifeCycle, dArgs):
    iChaneg = dArgs['iChange']
    iChange = cl_formula.GetResultByData(oWarrior, iChaneg, { })
    if iChange:
        oReason = cl_object.reason.CStrReason('自身技能消耗')
        oWarrior.HPDirectModify('HP', oWarrior.m_ID, -iChange, oReason)

