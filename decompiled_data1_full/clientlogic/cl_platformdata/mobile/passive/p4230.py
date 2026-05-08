# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4230.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4230.pyc
# Source Generated with Decompyle++
# File: p4230.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF
from cl_newformula import Func340, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 20, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32564, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'Att', 0, 60000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonRecordMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'pf4230')
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'pf4230' }))) >= 1 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'pf4230' }))) <= 8:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32565, (lambda *a: Func361(*a, **{
'sid': 4230,
'sArgs': 'FullEnergyTime' })), {
            'StateCount': (lambda *a: Func340(*a, **{
'sKey': 'pf4230' })) }, 1, -1, None)
        cl_action.CommonChangeMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'pf4230', (lambda *a: -Func340(*a, **{
'sKey': 'pf4230' })))
    else:
        cl_action.CommonChangeMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'pf4230', (lambda *a: -Func340(*a, **{
'sKey': 'pf4230' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1314, -1, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32563) == 0:
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1314)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1314, -1, None) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32563) == 1:
        cl_evact.EventCBSetCurPerformCD(oWarrior, oEventCB, 0)


class CPerform(CCustomPerform):
    m_SID = 4230
    m_Name = '卫士被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = {
        'FullEnergyTime': 200,
        'FullEnergyRatio': 500 }
    m_DieDisable = 0

