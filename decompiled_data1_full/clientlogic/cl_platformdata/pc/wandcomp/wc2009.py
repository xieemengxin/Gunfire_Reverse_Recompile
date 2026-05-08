# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2009.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2009.pyc
# Source Generated with Decompyle++
# File: wc2009.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

def TriggerAction1(oWarrior, oLifeCycle):
    if cl_condition.RandomTrigger(oWarrior, oLifeCycle, 100, 50):
        cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33524, 0, { }, 1)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33524, 0, { }, 1)


class CWandComp(CBaseComp):
    m_SID = 2009
    m_Name = '元素附着'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (None, None),
        2: (None, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

