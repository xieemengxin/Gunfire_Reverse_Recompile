# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2079.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2079.pyc
# Source Generated with Decompyle++
# File: wc2079.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDCOMP_RARITY_TALE, WANDTAG_OTHER, WAND_COMP_TYPE_ACTION

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)


def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.WandCompAddOwnerState(oWarrior, oLifeCycle, 33532, 0, { }, 1)


class CWandComp(CBaseComp):
    m_SID = 2079
    m_Name = '附武器伤二'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_OTHER,)
    m_ActionInfo = {
        1: (Action1, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1 }
    m_CBFuncAction = { }
    m_Rarity = WANDCOMP_RARITY_TALE

