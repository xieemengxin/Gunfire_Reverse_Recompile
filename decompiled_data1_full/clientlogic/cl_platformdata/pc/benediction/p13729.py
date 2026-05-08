# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13729.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13729.pyc
# Source Generated with Decompyle++
# File: p13729.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import VIRTUAL_ITEM_WANDCOMP, WAND_SUBMSG_ADD, WAND_SUBMSG_REMOVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetAllWandExtActionCompNum(oWarrior, oLifeCycle, 1, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_ADD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCHANGE, WAND_SUBMSG_REMOVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEBENED_BEFORE, -1, 3, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDPLAYER, -1, 4)
    if not cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, 'BeneReward13729'):
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'BeneReward13729', 1)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetWandExtActionCompNum(oWarrior, oEventCB, 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetWandExtActionCompNum(oWarrior, oEventCB, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBWandItemInBag(oWarrior, oEventCB, 1021, 2, 1, VIRTUAL_ITEM_WANDCOMP)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'BeneReward13729', 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.CommonSetAllWandExtActionCompNum(oWarrior, oEventCB.GetCBLifeCycle(), 1, 0)


class CPerform(CCustomPerform):
    m_SID = 13729
    m_Name = '灵玉拓位'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

