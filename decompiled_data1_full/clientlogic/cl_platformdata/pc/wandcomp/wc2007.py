# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc2007.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc2007.pyc
# Source Generated with Decompyle++
# File: wc2007.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import WANDTAG_PERFORM, WAND_ACTCOMP_INSTANT, WAND_COMP_TYPE_ACTION

def TriggerAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddThrowBagBullet(oWarrior, oLifeCycle, 1, 0)


def TriggerAction2(oWarrior, oLifeCycle):
    cl_action.CommonAddThrowBagBullet(oWarrior, oLifeCycle, 2, 0)


class CWandComp(CBaseComp):
    m_SID = 2007
    m_Name = '灵力回复'
    m_Type = WAND_COMP_TYPE_ACTION
    m_Tag = (WANDTAG_PERFORM,)
    m_ActionInfo = {
        1: (None, None),
        2: (None, None) }
    m_TriggerActionInfo = {
        1: TriggerAction1,
        2: TriggerAction2 }
    m_CBFuncAction = { }
    m_TriggerType = WAND_ACTCOMP_INSTANT

