# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/daytrialpf/p14682.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/daytrialpf/p14682.pyc
# Source Generated with Decompyle++
# File: p14682.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.daytrial import CPerform as CCustomPerform
from cl_commondefines import MAIN_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1409, 'Radius', -3000, 0)
    cl_action.CommonChangeWeaponAttr(oWarrior, oLifeCycle, 'Radius', 0, -3000, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Radius', 0, -3000, MAIN_HOLD, { })


class CPerform(CCustomPerform):
    m_SID = 14682
    m_Name = '劣质火药'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

