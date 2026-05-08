# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p7013.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p7013.pyc
# Source Generated with Decompyle++
# File: p7013.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI, HATEMETHOD_HERODIS, LEVEL_TYPE_BOSS, OBJECT_OWNER, PATHMODE_STAYSTATUS

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, 0)
    cl_action.CommonSetServantBronPosInfo(oWarrior, oLifeCycle, 2, 4, 35, 75)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 1, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 1)
    cl_action.CommonReplaceOwnObjHateMethod(oWarrior, oLifeCycle, OBJECT_OWNER, HATEMETHOD_HERODIS)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.SwitchTargetPathMode(oWarrior, oEventCB.GetCBLifeCycle(), PATHMODE_STAYSTATUS)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33132, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 7013
    m_Name = '致命装置-炮台被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

