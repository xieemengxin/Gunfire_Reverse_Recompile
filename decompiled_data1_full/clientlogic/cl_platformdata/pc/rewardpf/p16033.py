# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16033.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16033.pyc
# Source Generated with Decompyle++
# File: p16033.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB) and cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '16033', None) == 0:
        cl_evact.EventCBGetTargetByDyingHero(oWarrior, oEventCB, 25, 1)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) == 1:
            cl_evact.EventCBRelifeDyingTarget(oWarrior, oEventCB)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, '16033', 1500, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1315, -1, -1) and cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '16033', None) == 0:
        cl_evact.EventCBGetTargetByDyingHero(oWarrior, oEventCB, 25, 1)
        if cl_evcon.GetThisTargetNum(oWarrior, oEventCB) == 1:
            cl_evact.EventCBRelifeDyingTarget(oWarrior, oEventCB)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventCBAddTargetCDByMark(oWarrior, oEventCB, '16033', 1500, None)


class CPerform(CCustomPerform):
    m_SID = 16033
    m_Name = '心脏起搏'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

