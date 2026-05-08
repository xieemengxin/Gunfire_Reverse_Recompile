# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5881.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5881.pyc
# Source Generated with Decompyle++
# File: p5881.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, MG_SOURCE_RELIC, QUALITY_TYPE_HIGH, RELIC_TYPE_CURSE, RELIC_TYPE_NORMAL
from cl_newformula import Func210

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5881)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 6, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5881)
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDRELIC, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 6, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if (cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) or cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS)) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func210(*a))) > 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
        cl_evact.EventCBRemoveRandomCurseRelic(oWarrior, oEventCB, 0)
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2423, {
            1: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RelicName') != 0:
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 2429, {
                '$name1': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurseName'),
                '$name2': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RelicName') })
        else:
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 9688, {
                '$name': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurseName') })
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RelicName', 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurseRewarded') == 0:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CurseRewarded', 1)
        if cl_evcon.EventCBCheckLoading(oWarrior, oEventCB) == 0:
            cl_evact.EventCBGetRandomCurseRelic(oWarrior, oEventCB, 3)


def DoCallBackAction3(oEventCB, oWarrior):
    if (cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_FIGHT) or cl_evcon.CheckEventLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS)) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func210(*a))) > 0:
        cl_evact.EventCBRemoveRandomCurseRelic(oWarrior, oEventCB, 0)
        cl_action.CommonSetWeightDropGoods(oWarrior, oEventCB.GetCBLifeCycle(), 2423, {
            1: 100 }, MG_SOURCE_RELIC, 1, 1, 1, None)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RelicName') != 0:
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 2429, {
                '$name1': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurseName'),
                '$name2': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'RelicName') })
        else:
            cl_action.CommonSendNotify(oWarrior, oEventCB.GetCBLifeCycle(), 1, 9688, {
                '$name': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurseName') })
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RelicName', 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_RELIC) and cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'MiniGame2423'):
        cl_evact.PassiveCBSetPFArgsNoFormula(oWarrior, oEventCB, 'RelicName', cl_evact.EventCBGetRelicName(oWarrior, oEventCB))


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_CURSE) and cl_evcon.CheckReason(oWarrior, oEventCB, 'eventRemoveRelic', 0):
        cl_evact.PassiveCBSetPFArgsNoFormula(oWarrior, oEventCB, 'CurseName', cl_evact.EventCBGetRelicName(oWarrior, oEventCB))


class CPerform(CCustomPerform):
    m_SID = 5881
    m_Name = '先苦后甜'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 0
    m_BasePrice = 100
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_HIGH

