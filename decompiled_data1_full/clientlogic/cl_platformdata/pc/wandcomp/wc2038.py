# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2038.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2038.pyc
# Source Generated with Decompyle++
# File: wc2038.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func780

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33578, (lambda *a: 150 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), { }, 1)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 150 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2038
    m_Name = '无限灵力'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        2: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

