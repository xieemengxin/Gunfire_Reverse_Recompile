# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2035.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2035.pyc
# Source Generated with Decompyle++
# File: wc2035.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import DEPUTY_HOLD, MAIN_HOLD, OBJ_SELF, WANDTAG_WEAPON, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func525, Func532, Func742

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'WC2035Temp', 0)
    cl_action.WandCompAddArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'WC2035Temp', (lambda *a: min(int(-(Func525(*a) - 1)), 0)))
    cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: Func742(*a, **{
'sArg': 'WC2035Temp' })), MAIN_HOLD)
    if cl_condition.CheckDualSate(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'WC2035Temp2', (lambda *a: min(int(-(Func532(*a) - 1)), 0)))
        cl_action.WandCompAddArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'WC2035Temp', (lambda *a: Func742(*a, **{
'sArg': 'WC2035Temp2' })))
        cl_evact.EventCBAddHoldWeaponComBullet(oWarrior, oEventCB, (lambda *a: Func742(*a, **{
'sArg': 'WC2035Temp2' })), DEPUTY_HOLD)
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33577, 1, 1, 0, 0):
        cl_evact.EventCBSetTargetStateStatistics(oWarrior, oEventCB, 33577, 'NewAdditionCount', (lambda *a: -Func742(*a, **{
'sArg': 'WC2035Temp' })), 1, 1, 1)
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 33577, { }, 1, 1)
    else:
        cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33577, 0, {
            'StateCount': (lambda *a: -Func742(*a, **{
'sArg': 'WC2035Temp' })) }, 1)


class CWandComp(CBaseComp):
    m_SID = 2035
    m_Name = '压缩弹夹'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

