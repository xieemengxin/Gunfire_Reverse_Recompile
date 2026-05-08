# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5357.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5357.pyc
# Source Generated with Decompyle++
# File: p5357.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ARMOR_RADIO_ADD, ARMOR_RADIO_SUB, DAM_MASK_CLASS, DAM_MASK_ELEMENT

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 1, ARMOR_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 1, ARMOR_RADIO_ADD, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if oWarrior.Armor() > 0:
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 5000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 0)
    else:
        cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 0, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 5000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), 0, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 0)


class CPerform(CCustomPerform):
    m_SID = 5357
    m_Name = '#NT#精英冲锋怪护甲增加抗性'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

