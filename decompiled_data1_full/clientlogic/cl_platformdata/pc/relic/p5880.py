# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5880.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5880.pyc
# Source Generated with Decompyle++
# File: p5880.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func598

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32373, 0, {
        'StatusEffect': 1 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32373, 0, {
        'StatusEffect': 2 }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 32373, 60, 1, None)
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32373, (lambda *a: Func598(*a, **{
'sKey': 'PF5880' })), None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 32373, 120, 1, None)
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 32373, (lambda *a: Func598(*a, **{
'sKey': 'PF5880' })), None)


class CPerform(CCustomPerform):
    m_SID = 5880
    m_Name = '愈行愈速'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_NORMAL

