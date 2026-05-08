# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5954.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5954.pyc
# Source Generated with Decompyle++
# File: p5954.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE
from cl_newformula import Func304, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1533, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ArmorMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1533):
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1533, (lambda *a: min(int(int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) / 1500)), 20)))
        cl_evact.EventCBRefreshStateArgs(oWarrior, oEventCB, 1011, {
            'MoveSpeedMul': (lambda *a: -100 * Func410(*a, **{
'sid': 1533 })) })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1533, (lambda *a: min(int(int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) / 1500)), 20)))
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1011, 0, {
        'MoveSpeedMul': (lambda *a: -100 * Func410(*a, **{
'sid': 1533 })) }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5954
    m_Name = '负重前行'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = {
        'StateSID': 33361 }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

