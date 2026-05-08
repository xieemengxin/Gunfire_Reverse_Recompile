# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5799.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5799.pyc
# Source Generated with Decompyle++
# File: p5799.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_THROW, PF_TYPE_CAREERPF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func343, Func420, Func421, Func530

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 3, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, -1, 9, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckThrowBullet(oWarrior, oEventCB) or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func420(*a) - Func421(*a))) <= 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1330, 0, { }, 1, 0, None)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1331, 0)
    elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))) == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1330, 0, { }, 1, 0, None)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1331, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))) > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1330, 0, 0, None):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1331, 1200, { }, 1, 0, None)
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1330, 0)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1330, 0, { }, 1, 0, None)
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1331, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))) == 0 or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func530(*a))):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))) == 0:
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1331, 0)
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1330, 0, { }, 1, 0, None)
        else:
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1489, 35, { }, 0)
    elif cl_evcon.CheckHasState(oWarrior, oEventCB, 1330):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1330, 0)
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1331, 2000, { }, 1)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))) == 0 or cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func530(*a))):
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func343(*a, **{
'sid': 4508 }))) == 0:
                cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1331, 0)
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1330, 0, { }, 1, 0, None)
            else:
                cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1489, 35, { }, 0)
        elif cl_evcon.CheckHasState(oWarrior, oEventCB, 1330):
            cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1330, 0)
            cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 1331, 2000, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 5799
    m_Name = '背水之战'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3,
        6: DoCallBackAction6,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

