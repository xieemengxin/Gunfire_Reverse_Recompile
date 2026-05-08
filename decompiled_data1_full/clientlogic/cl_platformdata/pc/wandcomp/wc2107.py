# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2107.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2107.pyc
# Source Generated with Decompyle++
# File: wc2107.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_COMP_TYPE_ACTION
from cl_newformula import Func747

def Action3(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'WeakenCount', 10)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EnhanceCount', 30)
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33595, 0, {
        'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2107,
'sKey': 'WeakenCount' })) }, 0)
    cl_action.CommonStateStatistics(oWarrior, oLifeCycle, 33595, (lambda *a: Func747(*a, **{
'iWandSID': 2107,
'sKey': 'WeakenCount' })), 'WeakenCount')


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'WeakenCount', -10)
    cl_action.WandCompSetArgValue(oWarrior, oLifeCycle, 'EnhanceCount', -30)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' }))) <= 0:
        cl_action.CommonRemoveOwnerState(oWarrior, oLifeCycle, 33595, 0)
    else:
        cl_action.CommonTriggerStateRefreshBehavior(oWarrior, oLifeCycle, 33595, {
            'StateCount': (lambda *a: Func747(*a, **{
'iWandSID': 2045,
'sKey': 'WeakenCount' })) })


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33595, 30, 0)


class CWandComp(CBaseComp):
    m_SID = 2107
    m_Name = 'Q伤模块三'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        3: (Action3, DisableAction3) }
    m_TriggerActionInfo = {
        3: TriggerAction3 }
    m_CBFuncAction = { }

