# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p50903.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p50903.pyc
# Source Generated with Decompyle++
# File: p50903.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction50903 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSwitchMode(oWarrior, oLifeCycle, FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE, 0, { }, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ACTIVE_SEASONSUIT, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 50903
    m_Name = '#NT#卡包-获得额外套装'
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

