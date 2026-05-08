# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2105.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2105.pyc
# Source Generated with Decompyle++
# File: wc2105.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action1(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'WeakenCount', 3)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EnhanceCount', 9)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33595, 0, {
        'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2105,
'sKey': 'WeakenCount' })) }, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2105,
'sKey': 'WeakenCount' })), 'WeakenCount')


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'WeakenCount', -3)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EnhanceCount', -9)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33595, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' })) })


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33595, 9, 0)


class CWandComp(CBaseComp):
    m_SID = 2105
    m_Name = 'Q伤模块一'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        1: (Action1, DisableAction1) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = { }

