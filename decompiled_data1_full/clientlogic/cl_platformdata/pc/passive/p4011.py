# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4011.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4011.pyc
# Source Generated with Decompyle++
# File: p4011.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
            cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Stability', 200, 0, 0, { })
        else:
            cl_evact.PassiveCBChangeWeaponAttr(oWarrior, oEventCB, 'Stability', 0, 0, 0, { })


class CPerform(CCustomPerform):
    m_SID = 4011
    m_Name = '开镜加稳定性'
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

