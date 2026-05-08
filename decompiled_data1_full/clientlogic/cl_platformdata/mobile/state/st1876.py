# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st1876.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st1876.pyc
# Source Generated with Decompyle++
# File: st1876.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import LEVEL_TYPE_HIDE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_SPECIAL, STATE_EFF_NONE
from cl_newformula import Func240, Func410, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_TALENT_CHOOSE_END, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 4)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEGOLDENCUP, -1, 6, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    if cl_condition.StateGetSelfCount(oTarget, oLifeCycle) == 1:
        cl_action.CommonStateStatistics(oTarget, oLifeCycle, 1876, 0, 'SecondTime')
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'NpcID') != 0:
        cl_action.CommonRemoveNpc(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'NpcID', cl_action.CommonCreateNpc(oTarget, oEventCB.GetCBLifeCycle(), 30011067, 1, { }))
        cl_action.CommonNpcSetShare(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
        cl_action.CommonGoldenCupNpcSetTimes(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), (lambda *a: Func410(*a, **{
'sid': 1875 })))
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'SecondTime') == 0:
            cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1, 8, 0, 0)
            cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 8, 0, 0)
            if cl_condition.CheckHasAllTalent(oTarget, oEventCB.GetCBLifeCycle()):
                cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
            else:
                cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
        else:
            cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1)
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'NpcID', cl_action.CommonCreateNpc(oTarget, oEventCB.GetCBLifeCycle(), 30011067, 1, { }))
        cl_action.CommonNpcSetShare(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
        cl_action.CommonGoldenCupNpcSetTimes(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), (lambda *a: Func410(*a, **{
'sid': 1875 })))
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'SecondTime') == 0:
            cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1, 8, 0, 0)
            cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 8, 0, 0)
            if cl_condition.CheckHasAllTalent(oTarget, oEventCB.GetCBLifeCycle()):
                cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
            else:
                cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
        else:
            cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1)
            cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1)


def CallBack2(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func240(*a))) == cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'NpcID'):
        cl_action.CommonSetStateCount(oTarget, oEventCB.GetCBLifeCycle(), 1875, (lambda *a: Func410(*a, **{
'sid': 1875 }) - 1), None)


def CallBack3(oEventCB, oTarget):
    if cl_evcon.CheckEnterNewSecne(oTarget, oEventCB) and cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE) == 0:
        if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'NpcID') != 0:
            cl_action.CommonRemoveNpc(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })))
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'NpcID', cl_action.CommonCreateNpc(oTarget, oEventCB.GetCBLifeCycle(), 30011067, 1, { }))
            cl_action.CommonNpcSetShare(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
            cl_action.CommonGoldenCupNpcSetTimes(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), (lambda *a: Func410(*a, **{
'sid': 1875 })))
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'SecondTime') == 0:
                cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1, 8, 0, 0)
                cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 8, 0, 0)
                if cl_condition.CheckHasAllTalent(oTarget, oEventCB.GetCBLifeCycle()):
                    cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
                else:
                    cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
            else:
                cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
                cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1)
                cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1)
        else:
            cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'NpcID', cl_action.CommonCreateNpc(oTarget, oEventCB.GetCBLifeCycle(), 30011067, 1, { }))
            cl_action.CommonNpcSetShare(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
            cl_action.CommonGoldenCupNpcSetTimes(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), (lambda *a: Func410(*a, **{
'sid': 1875 })))
            cl_evact.StateSetSelfCount(oTarget, oEventCB, 0)
            if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'SecondTime') == 0:
                cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1, 8, 0, 0)
                cl_action.CommonListenMsgCallBack(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 8, 0, 0)
                if cl_condition.CheckHasAllTalent(oTarget, oEventCB.GetCBLifeCycle()):
                    cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
                else:
                    cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)
            else:
                cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
                cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ADDTALENT, -1)
                cl_action.CommonDoneEvent(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1)


def CallBack4(oEventCB, oTarget):
    if cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'SecondTime'):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 1875, 0)
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'SecondTime', 1)


def CallBack6(oEventCB, oTarget):
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func240(*a))) == cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'NpcID'):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        cl_action.CommonRemoveOwnerState(oTarget, oEventCB.GetCBLifeCycle(), 1875, 0)


def CallBack8(oEventCB, oTarget):
    if cl_condition.CheckHasAllTalent(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 1)
    else:
        cl_action.CommonGoldenCupNpcSetAutoRecycle(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func437(*a, **{
'sKey': 'NpcID' })), 0)


class CState(cl_state.CState):
    m_SID = 1876
    m_Name = '否极泰来'
    m_Type = STATE_CLS_SPECIAL
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3,
        4: CallBack4,
        6: CallBack6,
        8: CallBack8 }

