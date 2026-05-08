# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15185.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15185.pyc
# Source Generated with Decompyle++
# File: p15185.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DUAL_STATE_END, PF_SUBMSG_CAREERPF, PF_SUBMSG_THROW

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfColdTime(oWarrior, oLifeCycle, 1000)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 205) or cl_condition.CheckHero(oWarrior, oLifeCycle, 206) or cl_condition.CheckHero(oWarrior, oLifeCycle, 215) or cl_condition.CheckHero(oWarrior, oLifeCycle, 216) or cl_condition.CheckHero(oWarrior, oLifeCycle, 218) or cl_condition.CheckHero(oWarrior, oLifeCycle, 214) or cl_condition.CheckHero(oWarrior, oLifeCycle, 212):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 1, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_THUNDEROVER, -1, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_THROW, 3, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_CAREERPF, 4, 0, 0)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15185)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33485, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33493, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33493, 0)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CD') == 1:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1000)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33485, 0)
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33493, 0)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CD') == 1:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1000)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1428, 1, 0):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33485, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33493, 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CD') == 1:
            cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1000)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1325, 1, 0):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33485, 0)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33493, 0)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CD') == 1:
            cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1000)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'CD', 1)


class CPerform(CCustomPerform):
    m_SID = 15185
    m_Name = '#NT#寸步难移套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

