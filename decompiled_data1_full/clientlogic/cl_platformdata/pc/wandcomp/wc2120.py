# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2120.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2120.pyc
# Source Generated with Decompyle++
# File: wc2120.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func780

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33611, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), {
        'StatusEffect': 2 }, 1)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33611, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), {
        'StatusEffect': 3 }, 1)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2120
    m_Name = '腐蚀秘法'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        2: (None, None),
        3: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

