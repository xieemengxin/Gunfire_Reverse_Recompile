# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6557.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6557.pyc
# Source Generated with Decompyle++
# File: p6557.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_item.defines as itemdef
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1855, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 6557
    m_Name = '队友AI伤害'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oWarrior, oEventCB, dArg):
    dEventInfo = oEventCB.GetCBEventInfo()
    iWeaponType = dEventInfo['ItemType']
    dChangeAttr = dArg.get(iWeaponType, { })
    if not dChangeAttr:
        return None
    sAttr = dChangeAttr['Attr']
    iAdd = dChangeAttr['Add']
    iMul = dChangeAttr['Mul']
    cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), sAttr, iAdd, iMul, MAIN_HOLD)
    cl_action.CommonChangeWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), sAttr, iAdd, iMul, -1)

