# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2017.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2017.pyc
# Source Generated with Decompyle++
# File: wc2017.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import OBJ_SELF, WANDTAG_WEAPON, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func742, Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2017Num', 5)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'WC2017Count', 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddArgValue(oWarrior, oLifeCycle, 'WC2017Num', -5)
    if cl_condition.WandCompGetArgValue(oWarrior, oLifeCycle, 'WC2017Count'):
        cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33532, (lambda *a: -Func742(*a, **{
'sArg': 'WC2017Count' })), 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2017,
'sKey': 'WC2017Num' }))) == 0:
        cl_action.CommonRemoveState(oWarrior, oLifeCycle, 33532)


def TriggerAction2(oWarrior, oLifeCycle):
    if cl_condition.HasState(oWarrior, oLifeCycle, 33532) == 0:
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33532, 0, { }, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.WandCompGetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'WC2017Count') < 5:
        cl_action.WandCompAddArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'WC2017Count', 1)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33532, 1, 0, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 33532):
        cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'WC2017Count', 0)


class CWandComp(CBaseComp):
    m_SID = 2017
    m_Name = '融兵打击'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

