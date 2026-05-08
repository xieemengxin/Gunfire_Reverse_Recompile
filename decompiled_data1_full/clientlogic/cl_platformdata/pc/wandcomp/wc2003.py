# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2003.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2003.pyc
# Source Generated with Decompyle++
# File: wc2003.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_WEAPON, WAND_ACTCOMP_CONTINUE, WAND_COMP_TYPE_ACTION
from cl_newformula import Func780

def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33525, (lambda *a: 200 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), {
        'StateCount': 60 }, 1)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 200 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


def TriggerAction3(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33525, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })), {
        'StateCount': 100 }, 1)
    cl_action.WandActCompTrigger(oWarrior, oLifeCycle, 0, 0, (lambda *a: 300 + Func780(*a, **{
'sKey': 'AbilityAddLast' })))


class CWandComp(CBaseComp):
    m_SID = 2003
    m_Name = '暴击转化'
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

