# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5885.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5885.pyc
# Source Generated with Decompyle++
# File: p5885.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DROP_REASON_UNLOCK, NWARRIOR_NPC_EVENT, QUALITY_TYPE_HIGH, RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_DROP, RELIC_SUBMSG_GENERATE_GOOD, RELIC_SUBMSG_GENERATE_LOTTERY, RELIC_TYPE_NORMAL, REMOVE_RELIC_EXTEND, REMOVE_RELIC_FOURSEASON_ROLLRELIC
from cl_newformula import Func201, Func244, Func245, Func248, Func518, Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5885)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func518(*a, **{
'sAttr': 'PF5885_First' }))) > 0:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREADDRELIC, -1, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_DROP, 5, 0, -99)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_GOOD, 3, 0, -99)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_CHOOSE, 3, 0, -99)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, RELIC_SUBMSG_GENERATE_LOTTERY, 3, 0, -99)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_EVENTNPC_REWARD_RELIC, -1, 3, 0, -99)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_REMOVE_RELIC_DROP, REMOVE_RELIC_EXTEND, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORE_REMOVE_RELIC_DROP, REMOVE_RELIC_FOURSEASON_ROLLRELIC, 6, 0, 0)
    if cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, 'PF5885_Level') == 0:
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'PF5885_Level', (lambda *a: Func244(*a) + Func245(*a)))


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddFilterRelic(oWarrior, oLifeCycle, 5885)
    cl_action.CommonCreateNpc(oWarrior, oLifeCycle, 30011027, 1, {
        'SelectedTalent': 1,
        'BanReplace': 1 })
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5885, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5885_First', 0)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func248(*a))) and cl_condition.CheckTalentCanUpgrade(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func248(*a))):
        cl_action.CommonAddTalentLevel(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func248(*a)), 0, 1)
    else:
        cl_action.CommonCreateNpc(oWarrior, oEventCB.GetCBLifeCycle(), 30011027, 1, {
            'BanReplace': 1 })
    cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5885, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5885) and cl_evcon.EventCBGetRelicLevel(oWarrior, oEventCB, None) < 2:
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5885_First', 1)
        cl_evact.EventCBRemoveRelic(oWarrior, oEventCB, 5885, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'PF5885_Layer' }))) != cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func201(*a))) and cl_condition.CheckHasExtendRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5885) == 0 and cl_condition.CheckHasTempRemoveRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5885) == 0 and cl_evcon.EventCBGetRelicLevel(oWarrior, oEventCB, 1) == 1 and cl_evcon.CheckRelicQuality(oWarrior, oEventCB, QUALITY_TYPE_HIGH) and cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_NORMAL) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: 10 + (Func244(*a) + Func245(*a) - Func598(*a, **{
'sKey': 'PF5885_Level' })) * 4)):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5885_Layer', (lambda *a: Func201(*a)))
        cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
            5885: 1 }, 1, 0, 1)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckNPCType(oWarrior, oEventCB, NWARRIOR_NPC_EVENT) == 0 and cl_evcon.CheckDropReason(oWarrior, oEventCB, DROP_REASON_UNLOCK) == 0 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'PF5885_Layer' }))) != cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func201(*a))) and cl_condition.CheckHasExtendRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5885) == 0 and cl_condition.CheckHasTempRemoveRelic(oWarrior, oEventCB.GetCBLifeCycle(), 5885) == 0 and cl_evcon.EventCBGetRelicLevel(oWarrior, oEventCB, 1) == 1 and cl_evcon.CheckRelicQuality(oWarrior, oEventCB, QUALITY_TYPE_HIGH) and cl_evcon.CheckRelicType(oWarrior, oEventCB, RELIC_TYPE_NORMAL) and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, (lambda *a: 10 + (Func244(*a) + Func245(*a) - Func598(*a, **{
'sKey': 'PF5885_Level' })) * 4)):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5885_Layer', (lambda *a: Func201(*a)))
        cl_evact.EventReplaceRelicReward(oWarrior, oEventCB, {
            5885: 1 }, 1, 0, 1)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5885):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'PF5885_Layer', (lambda *a: Func201(*a)))


class CPerform(CCustomPerform):
    m_SID = 5885
    m_Name = '好事成双'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_HIGH

