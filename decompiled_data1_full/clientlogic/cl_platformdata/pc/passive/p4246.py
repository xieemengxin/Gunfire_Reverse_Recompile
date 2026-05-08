# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4246.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4246.pyc
# Source Generated with Decompyle++
# File: p4246.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_only import Functor
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK, PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 3, 1):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1400, 0, { }, 1, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1401, None, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1402, None, None, None)
    elif cl_evcon.CheckRandom(oWarrior, oEventCB, 2, 1):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1401, 0, { }, 1, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1400, None, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1402, None, None, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1402, 0, { }, 1, None, None)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1401, None, None, None)
        cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1400, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 4246
    m_Name = '元素失效'
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

