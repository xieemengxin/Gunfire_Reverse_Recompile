# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2013.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2013.pyc
# Source Generated with Decompyle++
# File: wc2013.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_OTHER, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

def TriggerAction1(oWarrior, oLifeCycle):
    if cl_condition.CheckSceneFightMonster(oWarrior, oLifeCycle):
        cl_action.CommonAddWarCash(oWarrior, oLifeCycle, 20)
    else:
        cl_action.CommonAddWarCash(oWarrior, oLifeCycle, 2)


def TriggerAction2(oWarrior, oLifeCycle):
    if cl_condition.CheckSceneFightMonster(oWarrior, oLifeCycle):
        cl_action.CommonAddWarCash(oWarrior, oLifeCycle, 40)
    else:
        cl_action.CommonAddWarCash(oWarrior, oLifeCycle, 4)


class CWandComp(CBaseComp):
    m_SID = 2013
    m_Name = '获得铜币'
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

