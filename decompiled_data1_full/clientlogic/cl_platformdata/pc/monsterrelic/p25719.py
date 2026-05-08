# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25719.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25719.pyc
# Source Generated with Decompyle++
# File: p25719.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_LOW, STATE_CLS_ABNORMAL
from cl_newformula import Func304, Func311, Func326, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1713, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1713, (lambda *a: Func326(*a) * 100 // (Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' }))), -1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func410(*a, **{
'sid': 1713 }))) >= 20 and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func311(*a))) > 1:
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1713, -20, -1)
        cl_action.CommonRemoveAllStateByType(oWarrior, oEventCB.GetCBLifeCycle(), STATE_CLS_ABNORMAL)


class CPerform(CCustomPerform):
    m_SID = 25719
    m_Name = '回光返照'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5719
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

