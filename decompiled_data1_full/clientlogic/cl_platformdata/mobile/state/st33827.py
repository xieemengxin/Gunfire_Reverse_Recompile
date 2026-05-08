# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33827.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33827.pyc
# Source Generated with Decompyle++
# File: st33827.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func437

def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.CalFormula(oTarget, oLifeCycle, (lambda *a: Func404(*a) // 10)) >= 6:
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33827, 6, 'HitCount')
    else:
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33827, (lambda *a: Func404(*a) // 10), 'HitCount')
    if cl_condition.GetStateStatistics(oTarget, oLifeCycle, 33827, 'HitCount') != cl_condition.GetStateStatistics(oTarget, oLifeCycle, 33827, 'Cache'):
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 33827, (lambda *a: Func437(*a, **{
'sKey': 'HitCount' })), 'Cache')
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonSendStateCountChangeMessage(oTarget, oLifeCycle)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.CommonSendStateMessage(oTarget, oLifeCycle, 1, {
        'RealHitCount': cl_action.StateGetSelfCount(oTarget, oLifeCycle) })


def CallBack0(oEventCB, oTarget):
    if cl_condition.GetStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), 33827, 'HitCount') >= 6:
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1331, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1335, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1336, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1435, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1332, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1337, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1310, 'Att', 15000, 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1334, 'Att', 15000, 0)
    else:
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1330, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1331, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1335, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1336, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1435, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1332, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1337, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1310, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)
        cl_action.CommonChangePerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 1334, 'Att', (lambda *a: Func437(*a, **{
'sKey': 'HitCount' }) * 2500), 0)


class CState(cl_state.CState):
    m_SID = 33827
    m_Name = '#NT#狮子连击计数'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REFRESH
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
    m_Action = (None, StateRemoveAction)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

