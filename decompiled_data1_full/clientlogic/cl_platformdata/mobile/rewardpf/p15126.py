# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15126.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15126.pyc
# Source Generated with Decompyle++
# File: p15126.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_PERSISTENCE, DAM_TYPE_THUNDER, OBJ_VICTIM, SUITEXPORT_PFSPECIALTAG
from cl_newformula import Func223, Func303, Func308, Func358, Func620, Func703, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8609)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, -1, 7, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 13, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, -1, 8, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSTATE, -1, 11, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 12, 0, 0)
    cl_action.CommonSetPerformSpecialTag(oWarrior, oLifeCycle, SUITEXPORT_PFSPECIALTAG, {
        1631: 1,
        1627: 1,
        1623: 1 })
    cl_action.CommonEnableSeasonSuitDamSummary(oWarrior, oLifeCycle, 15126, {
        1631: 0,
        1627: 0,
        1623: 0 })
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15126)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 8609, 1, 0) == 0:
            if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0 and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_condition.CheckHasOrderRelicNum(oWarrior, oEventCB.GetCBLifeCycle(), {
                5779: 1,
                5780: 1,
                5752: 1 }, 0):
                cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 400)
                cl_evact.EventCBSetUsePerformData(oWarrior, oEventCB, 'vEnd', cl_evact.EventCBGetHitPos(oWarrior, oEventCB), 1, 1)
                cl_evact.EventCBCustomUsePerform(oWarrior, oEventCB, 8609, { }, {
                    'Element': (lambda *a: Func703(*a)),
                    'TargetID': (lambda *a: Func620(*a)),
                    'ExtraElement': (lambda *a: Func717(*a, **{
'sArg': 'RelicNum' }) - 1) }, 0)
        elif cl_evcon.GetSkillCacheValue(oWarrior, oEventCB, 'ElementType') == 1024:
            if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5780):
                cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, (lambda *a: Func303(*a, **{
'sAttr': 'DebuffProb' })), 0)
            if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5752):
                cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, (lambda *a: Func303(*a, **{
'sAttr': 'DebuffProb' })), 0)
        elif cl_evcon.GetSkillCacheValue(oWarrior, oEventCB, 'ElementType') == 512:
            if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5779):
                cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, (lambda *a: Func303(*a, **{
'sAttr': 'DebuffProb' })), 0)
            if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5752):
                cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_THUNDER, (lambda *a: Func303(*a, **{
'sAttr': 'DebuffProb' })), 0)
        elif cl_evcon.GetSkillCacheValue(oWarrior, oEventCB, 'ElementType') == 256:
            if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5779):
                cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_FIRE, (lambda *a: Func303(*a, **{
'sAttr': 'DebuffProb' })), 0)
            if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5780):
                cl_evact.EventCBAddEleAbnormalTrigger(oWarrior, oEventCB, DAM_TYPE_CORRISION, (lambda *a: Func303(*a, **{
'sAttr': 'DebuffProb' })), 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 8609, 'Att', 0, (lambda *a: 10000 * Func223(*a) + 70000 * (Func308(*a) - 1)))


def DoCallBackAction8(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5779):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5779, -7500, 0)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1631, 'Att', 0, (lambda *a: Func358(*a, **{
'sid': 1631,
'sKey': 'Att' }) * 3))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RelicNum', 1)
    elif cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5780):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5780, -7500, 0)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1627, 'Att', 0, (lambda *a: Func358(*a, **{
'sid': 1627,
'sKey': 'Att' }) * 3))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RelicNum', 1)
    elif cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5752):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5752, -7500, 0)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1623, 'Att', 0, (lambda *a: Func358(*a, **{
'sid': 1623,
'sKey': 'Att' }) * 3))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RelicNum', 1)


def DoCallBackAction11(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 1002):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5779, -7500, 0)
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 1627, -7500, 0)
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5752, -7500, 0)


def DoCallBackAction12(oEventCB, oWarrior):
    if cl_evcon.CheckInPointRelic(oWarrior, oEventCB, {
        5779: 1,
        5780: 1,
        5752: 1 }):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RelicNum', -1)


def DoCallBackAction13(oEventCB, oWarrior):
    if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5779):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5779, -7500, 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RelicNum', 1)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1631, 'Att', 0, (lambda *a: Func358(*a, **{
'sid': 1631,
'sKey': 'Att' }) * 3))
    if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5780):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5780, -7500, 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RelicNum', 1)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1627, 'Att', 0, (lambda *a: Func358(*a, **{
'sid': 1627,
'sKey': 'Att' }) * 3))
    if cl_condition.CheckHasRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5752):
        cl_action.CommonChangePassiveCycleExecCBFuncTime(oWarrior, oEventCB.GetCBLifeCycle(), 5752, -7500, 0)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RelicNum', 1)
        cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1623, 'Att', 0, (lambda *a: Func358(*a, **{
'sid': 1623,
'sKey': 'Att' }) * 3))
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 8609, 'Att', 0, (lambda *a: Func358(*a, **{
'sid': 8609,
'sKey': 'Att' }) * 3))


class CPerform(CCustomPerform):
    m_SID = 15126
    m_Name = '元素新星'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        11: DoCallBackAction11,
        12: DoCallBackAction12,
        13: DoCallBackAction13 }
    m_BaseArgData = { }
    m_DieDisable = 0

