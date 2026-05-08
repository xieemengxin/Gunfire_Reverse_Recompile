# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2106.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2106.pyc
# Source Generated with Decompyle++
# File: wc2106.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EnhanceCount', 18)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'WeakenCount', 6)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33595, 0, {
        'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2106,
'sKey': 'WeakenCount' })) }, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2106,
'sKey': 'WeakenCount' })), 'WeakenCount')


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'WeakenCount', -6)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EnhanceCount', -18)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33595, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' })) })


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33595, 18, 0)


class CWandComp(CBaseComp):
    m_SID = 2106
    m_Name = 'Q伤模块二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        2: (Action2, DisableAction2) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }

