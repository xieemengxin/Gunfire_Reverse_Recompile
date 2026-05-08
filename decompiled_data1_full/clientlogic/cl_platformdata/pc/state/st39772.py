# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st39772.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st39772.pyc
# Source Generated with Decompyle++
# File: st39772.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, S8THIRDACTIVE_REFRESH_MAXENERGY, S8_THIRDITEM_ENABLE, S8_THIRDITEM_REMOVE, STATE_ADD_SAMESOURCE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429, Func862

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    if cl_condition.CheckHero(oTarget, oLifeCycle, 207) or cl_condition.CheckHero(oTarget, oLifeCycle, 214):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_ENABLE, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_REMOVE, 0, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_ENABLE, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_REMOVE, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: min((Func862(*a, **{
'sAttr': 'MaxEnergy' }) // Func429(*a, **{
'sArg': 'PerMax' })) * Func429(*a, **{
'sArg': 'RangeMul' }), Func429(*a, **{
'sArg': 'MaxRangeMul' }))))
    cl_action.CommonChangeThrowPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DamInterval', (lambda *a: Func404(*a)), 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: min((Func862(*a, **{
'sAttr': 'MaxEnergy' }) // Func429(*a, **{
'sArg': 'PerMax' })) * Func429(*a, **{
'sArg': 'RangeMul' }), Func429(*a, **{
'sArg': 'MaxRangeMul' }))))
    cl_action.CommonChangeThrowPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Radius', (lambda *a: Func404(*a)), 0, 1)


def CallBack2(oEventCB, oTarget):
    cl_action.StateSetSelfCount(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: min((Func862(*a, **{
'sAttr': 'MaxEnergy' }) // Func429(*a, **{
'sArg': 'PerMax' })) * Func429(*a, **{
'sArg': 'RangeMul' }), Func429(*a, **{
'sArg': 'MaxRangeMul' }))))


def CallBack3(oEventCB, oTarget):
    cl_action.CommonChangeThrowPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'DamInterval', (lambda *a: Func404(*a)), 0, 0)


def CallBack4(oEventCB, oTarget):
    cl_action.CommonChangeThrowPerformAttr(oTarget, oEventCB.GetCBLifeCycle(), 'Radius', (lambda *a: Func404(*a)), 0, 1)


class CState(cl_state.CState):
    m_SID = 39772
    m_Name = '#NT#次要范围'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SAMESOURCE
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
        0: CallBack0,
        1: CallBack1,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4 }

