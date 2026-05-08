# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2041.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2041.pyc
# Source Generated with Decompyle++
# File: wc2041.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func780

def TriggerAction2(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33579):
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33579, 0, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33579, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def TriggerAction3(oWarrior, oLifeCycle):
    if not cl_condition.HasState(oWarrior, oLifeCycle, 33581):
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33581, 0, { }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 33581, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 1, 1, (lambda *a: 500 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2041
    m_Name = '暴击增幅'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        2: (None, None),
        3: (None, None) }
    m_TriggerActionInfo = {
        2: TriggerAction2,
        3: TriggerAction3 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_CONTINUE

