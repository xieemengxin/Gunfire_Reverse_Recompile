# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1015.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1015.pyc
# Source Generated with Decompyle++
# File: wc1015.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_COMP_TYPE_CONDITION
from cl_newformula import Func651, Func742, Func749

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 0, 0, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oLifeCycle, (lambda *a: 16 - 2 * Func749(*a)))


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'RealCost' }))) >= 1000:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'RealCost' }))) >= 10000:
            cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, 10)
        else:
            cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'RealCost' }) // 1000))
    else:
        cl_evact.WandCompCBAddArgValue(oWarrior, oEventCB, 'RecordCost', (lambda *a: Func651(*a, **{
'sKey': 'RealCost' })))
        if cl_condition.WandCompGetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'RecordCost') >= 1000:
            cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'Count', (lambda *a: Func742(*a, **{
'sArg': 'RecordCost' }) // 1000))
            cl_action.WandCompAddArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'RecordCost', (lambda *a: -Func742(*a, **{
'sArg': 'Count' }) * 1000))
            cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: Func742(*a, **{
'sArg': 'Count' })))


class CWandComp(CBaseComp):
    m_SID = 1015
    m_Name = '武器技能资源'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }

