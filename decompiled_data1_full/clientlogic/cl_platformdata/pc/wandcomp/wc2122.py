# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2122.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2122.pyc
# Source Generated with Decompyle++
# File: wc2122.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION
from cl_newformula import Func780

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33635, (lambda *a: 100 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), { }, 1)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 100 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.CommonSubPointPerformColdTime(oWarrior, oLifeCycle, 1310, 0, 100)


class CWandComp(CBaseComp):
    m_SID = 2122
    m_Name = '无限冲刺'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

