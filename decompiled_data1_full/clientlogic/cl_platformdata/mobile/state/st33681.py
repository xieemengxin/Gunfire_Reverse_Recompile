# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33681.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33681.pyc
# Source Generated with Decompyle++
# File: st33681.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DAM_MASK_ELEMENT, OBJ_SELF, QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, STATE_ADD_REFRESH, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func216, Func226, Func227, Func404, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 4, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oTarget, oLifeCycle, 0, (lambda *a: Func404(*a) * 50), DAM_MASK_ELEMENT, 1)


def CallBack0(oEventCB, oTarget):
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'LowRelicNum', (lambda *a: Func227(*a)))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'NormalRelicNum', (lambda *a: Func226(*a)))
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'HighRelicNum', (lambda *a: Func216(*a)))


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckRelicQuality(oTarget, oEventCB, QUALITY_TYPE_LOW):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'LowRelicNum')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', 0, 0) * Func437(*a, **{
'sKey': 'LowRelicNum' }) + Func437(*a, **{
'sKey': 'NormalRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', 0, 0) + Func437(*a, **{
'sKey': 'HighRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', 0, 0)))
    elif cl_evcon.CheckRelicQuality(oTarget, oEventCB, QUALITY_TYPE_NORMAL):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'NormalRelicNum')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', 0, 0) * Func437(*a, **{
'sKey': 'LowRelicNum' }) + Func437(*a, **{
'sKey': 'NormalRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', 0, 0) + Func437(*a, **{
'sKey': 'HighRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', 0, 0)))
    elif cl_evcon.CheckRelicQuality(oTarget, oEventCB, QUALITY_TYPE_HIGH):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, 1, 'HighRelicNum')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', 0, 0) * Func437(*a, **{
'sKey': 'LowRelicNum' }) + Func437(*a, **{
'sKey': 'NormalRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', 0, 0) + Func437(*a, **{
'sKey': 'HighRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', 0, 0)))


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckRelicQuality(oTarget, oEventCB, QUALITY_TYPE_LOW):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'LowRelicNum')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', 0, 0) * Func437(*a, **{
'sKey': 'LowRelicNum' }) + Func437(*a, **{
'sKey': 'NormalRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', 0, 0) + Func437(*a, **{
'sKey': 'HighRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', 0, 0)))
    elif cl_evcon.CheckRelicQuality(oTarget, oEventCB, QUALITY_TYPE_NORMAL):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'NormalRelicNum')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', 0, 0) * Func437(*a, **{
'sKey': 'LowRelicNum' }) + Func437(*a, **{
'sKey': 'NormalRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', 0, 0) + Func437(*a, **{
'sKey': 'HighRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', 0, 0)))
    elif cl_evcon.CheckRelicQuality(oTarget, oEventCB, QUALITY_TYPE_HIGH):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, -1, 'HighRelicNum')
        cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', 0, 0) * Func437(*a, **{
'sKey': 'LowRelicNum' }) + Func437(*a, **{
'sKey': 'NormalRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', 0, 0) + Func437(*a, **{
'sKey': 'HighRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', 0, 0)))


def CallBack8(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack9(oEventCB, oTarget):
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'LowAdditionCount', 0, 0) * Func437(*a, **{
'sKey': 'LowRelicNum' }) + Func437(*a, **{
'sKey': 'NormalRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'NormalAdditionCount', 0, 0) + Func437(*a, **{
'sKey': 'HighRelicNum' }) * cl_action.CommonGetStateArgsDictSum(oTarget, oEventCB.GetCBLifeCycle(), 33681, 'HighAdditionCount', 0, 0)))


def StateRefreshAction(oTarget, oLifeCycle):
    if cl_condition.CommonCheckStateArgsDict(oTarget, oLifeCycle, 33681, 'LowAdditionCount', 0, 0):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 9, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 8, 0, 0)


class CState(cl_state.CState):
    m_SID = 33681
    m_Name = '秘能魔匣（增伤）'
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
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        4: CallBack4,
        8: CallBack8,
        9: CallBack9 }

