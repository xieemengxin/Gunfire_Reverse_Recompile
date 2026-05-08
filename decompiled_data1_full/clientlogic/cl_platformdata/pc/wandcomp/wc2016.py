# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2016.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2016.pyc
# Source Generated with Decompyle++
# File: wc2016.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WAND_COMP_TYPE_ACTION, WAND_SUBMSG_TRIGGERACTION
from cl_newformula import Func304, Func742

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HP_CHANGE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SHIELDFINSH, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.WandCompAddArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'HPChange', cl_evact.EventCBGetTotalHPChangeByCureRatio(oWarrior, oEventCB, 1))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, 100, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 2, 1, 100, 0, 0)
    cl_action.WandCompAddArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'HPChange', (lambda *a: Func304(*a, **{
'sAttr': 'RShield' }) * 100))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.RemoveDelayTriggerGroup(oWarrior, oEventCB)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.WandCompAddArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Cnt', (lambda *a: min(Func742(*a, **{
'sArg': 'HPChange' }) // 5000, 25)))
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'HPChange', 0)
    cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33520, 500, {
        'StateCount': (lambda *a: Func742(*a, **{
'sArg': 'Cnt' })) }, 0)
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Cnt', 0)


class CWandComp(CBaseComp):
    m_SID = 2016
    m_Name = '生命变化'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (4,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }

