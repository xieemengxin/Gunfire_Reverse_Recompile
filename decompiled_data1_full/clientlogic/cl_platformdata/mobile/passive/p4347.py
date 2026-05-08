# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4347.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4347.pyc
# Source Generated with Decompyle++
# File: p4347.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func340, Func361, Func410, Func430

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 4, 21, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32775, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDPERFORMCD, -1, 2, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12013)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 12)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECEIVE, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonRecordMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'pf4347')
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'pf4347' }))) >= 1 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func340(*a, **{
'sKey': 'pf4347' }))) <= 8:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32854):
            cl_evact.EventCBSetStateStatistics(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 32775 })), 32854, 'LastNum')
        if cl_evcon.CheckHasState(oWarrior, oEventCB, 32853):
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32775, (lambda *a: Func340(*a, **{
'sKey': 'pf4347' })), (lambda *a: Func430(*a, **{
'sid': 32853 }) + Func361(*a, **{
'sid': 4347,
'sArgs': 'FullEnergyTime' })), -1)
            cl_action.CommonChangeMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'pf4347', (lambda *a: -Func340(*a, **{
'sKey': 'pf4347' })))
        else:
            cl_evact.EventCBAddTargetStateCountAndEffectiveTime(oWarrior, oEventCB, 32775, (lambda *a: Func340(*a, **{
'sKey': 'pf4347' })), (lambda *a: Func361(*a, **{
'sid': 4347,
'sArgs': 'FullEnergyTime' })), -1)
            cl_action.CommonChangeMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'pf4347', (lambda *a: -Func340(*a, **{
'sKey': 'pf4347' })))
    else:
        cl_action.CommonChangeMoveDis(oWarrior, oEventCB.GetCBLifeCycle(), 'pf4347', (lambda *a: -Func340(*a, **{
'sKey': 'pf4347' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1323, -1, -1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774) == 0:
        cl_evact.EventCBRefreshPerformColdTime(oWarrior, oEventCB, 1323)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1323, -1, -1) and cl_evcon.CheckHasState(oWarrior, oEventCB, 32774) == 1:
        cl_evact.EventCBSetCurPerformCD(oWarrior, oEventCB, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Smash_IsCrazy', None):
        cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_WEAKNESS)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventCBStartThrowSkill(oWarrior, oEventCB, 1428, None, { })


class CPerform(CCustomPerform):
    m_SID = 4347
    m_Name = '新卫士被动'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        6: DoCallBackAction6 }
    m_BaseArgData = {
        'FullEnergyTime': 200,
        'FullEnergyRatio': 500,
        'BaseEnergyNum': 0 }
    m_DieDisable = 0

