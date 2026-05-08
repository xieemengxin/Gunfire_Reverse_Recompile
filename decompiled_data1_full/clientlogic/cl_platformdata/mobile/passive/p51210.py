# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p51210.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p51210.pyc
# Source Generated with Decompyle++
# File: p51210.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF, WAND_SUBMSG_TRIGGERACTION

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 1, 0, 0)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 5)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 1, 0, 0)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 10)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'MaxCover', 0, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_TRIGGERACTION, 1, 0, 0)
    cl_action.CommonSetWandMaxCount(oWarrior, oLifeCycle, 15)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 0, 0):
        cl_evact.EventCBAddWandCount(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CommonCheckItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'ClearCount'):
        cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'ClearCount', 0)
        cl_evact.EventCBSetWandCount(oWarrior, oEventCB, 0)


class CPerform(CCustomPerform):
    m_SID = 51210
    m_Name = '#NT#流星法杖被动'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

