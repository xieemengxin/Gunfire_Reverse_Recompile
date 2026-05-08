# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6510.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6510.pyc
# Source Generated with Decompyle++
# File: p6510.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 300, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 600, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 900, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 1200, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, 1500, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 6510
    m_Name = '伤害抵抗'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

