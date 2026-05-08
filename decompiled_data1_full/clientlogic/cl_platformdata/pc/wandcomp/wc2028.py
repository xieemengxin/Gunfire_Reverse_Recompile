# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2028.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2028.pyc
# Source Generated with Decompyle++
# File: wc2028.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func361

def TriggerAction2(oWarrior, oLifeCycle):
    if cl_condition.CheckHasPerform(oWarrior, oLifeCycle, 51213):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if not oWarrior.IsDying():
        cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33556, 0, {
            'Speed': 3000,
            'Dam': (lambda *a: Func361(*a, **{
'sid': 51213,
'sArgs': 'DamAdd' })) }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    if not oWarrior.IsDying():
        cl_action.WandCompAddOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33556, 0, {
            'Speed': 3000 }, 1)


class CWandComp(CBaseComp):
    m_SID = 2028
    m_Name = '隐身'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_TriggerType = WAND_ACTCOMP_INSTANT

