# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p6952.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p6952.pyc
# Source Generated with Decompyle++
# File: p6952.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction6952 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'Perform': 1604 })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventPlayerIsLiveFirst(oWarrior, oEventCB) and cl_evcon.CheckTriggerDrop(oWarrior, oEventCB, 1801):
        cl_action.CommonGetSteamedStuffedBunRecover(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_BEFOREINTERACTSHOP, -1, 0, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DROPTRIGGER, -1, 1, 1)


class CPerform(CCustomPerform):
    m_SID = 6952
    m_Name = '队友AI商店包子'
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

