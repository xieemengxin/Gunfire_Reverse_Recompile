# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p50706.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p50706.pyc
# Source Generated with Decompyle++
# File: p50706.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PET_ENTER_BATTLE, PET_HANDLE_ACTIVEABILITY
from cl_newformula import Func304, Func701, Func702

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'HPMax', -1, 3, 0, 0)
    cl_action.CommonSetMiniCloneNum(oWarrior, oLifeCycle, 3)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_CURPET, PET_ENTER_BATTLE, 5)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MINICLONE_DIE, -1, 5)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_MINICLONE, -1, 6)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33404, 0, { }, 1)
    cl_action.CommonListenOwnerMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_HANDLE_PET, PET_HANDLE_ACTIVEABILITY, 9)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33208, (lambda *a: Func304(*a, **{
'sAttr': 'RelifeTime' })), { }, 0, 0, None)
    cl_action.PassiveCloseCDExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33208, 0)
    cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'RelifeTime' })))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveChangeAttr(oWarrior, oEventCB, 'RHP', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 10 / 100), 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func702(*a) - Func701(*a))) > 0:
        cl_action.CommonCreateClone(oWarrior, oEventCB.GetCBLifeCycle())
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func702(*a) - Func701(*a))) > 0:
            cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'RelifeTime' })))
        if cl_evcon.CheckReason(oWarrior, oEventCB, 'EnterBattle', 0) == 0:
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33404, (lambda *a: max(Func701(*a) - 1, 0)), None)
            cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
            cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 7)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func702(*a) - Func701(*a))) > 0:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'RelifeTime' })))
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'EnterBattle', 0) == 0:
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33404, (lambda *a: max(Func701(*a) - 1, 0)), None)
        cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 7)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckReason(oWarrior, oEventCB, 'EnterBattle', 0) == 0:
        cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33404, (lambda *a: max(Func701(*a) - 1, 0)), None)
        cl_evact.EventCBGetClonePet(oWarrior, oEventCB)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 7)


def DoCallBackAction7(oEventCB, oWarrior):
    if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33404, 0, 1, 0, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33404, 0, { }, 1, 0, 0)
    cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 33404, (lambda *a: max(Func701(*a) - 1, 0)), 1)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0) == 0 and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func702(*a) - Func701(*a))) > 0:
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'RelifeTime' })))


class CPerform(CCustomPerform):
    m_SID = 50706
    m_Name = '#NT#MINI妖灵召唤'
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
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0

