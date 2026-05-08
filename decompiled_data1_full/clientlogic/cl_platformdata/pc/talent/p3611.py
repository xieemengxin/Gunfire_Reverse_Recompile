# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3611.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3611.pyc
# Source Generated with Decompyle++
# File: p3611.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.talent.customaction import CustomAction3611 as CustomAction
from . import CTalent as CCustomPerform
from cl_commondefines import PF_SUBMSG_CAREERPF, PF_SUBMSG_CLIENTACTIVE, PICK_INKBEAD, PICK_SPECIALINKBEAD
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3611, 'SpecialCreate', 0, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1325, 'AddStateTime', 0, 400)
    cl_action.CommonChangeInkBeadNum(oWarrior, oLifeCycle, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 2, 0, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3611, 'SpecialCreate', 0, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1325, 'AddStateTime', 0, 800)
    cl_action.CommonChangeInkBeadNum(oWarrior, oLifeCycle, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 2, 0, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 3611, 'SpecialCreate', 0, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1325, 'AddStateTime', 0, 1200)
    cl_action.CommonChangeInkBeadNum(oWarrior, oLifeCycle, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CLIENTACTIVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 2, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_SPECIALINKBEAD, 3, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORECREATEINKBEAD, -1, 6, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1325: 1,
        12029: 1 }, 1, 1):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DoubleEffect', (lambda *a: max(Func361(*a, **{
'sid': 3611,
'sArgs': 'DoubleEffect' }), 0) + 1))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SpecialCreate', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Times', 2)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1325: 1,
        12029: 1 }, 1, 1):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'DoubleEffect', (lambda *a: max(Func361(*a, **{
'sid': 3611,
'sArgs': 'DoubleEffect' }), 0) + 2))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'SpecialCreate', 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Times', 2)


def DoCallBackAction2(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DoubleEffect') == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DoubleEffect', -1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Times', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DoubleEffect') > 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DoubleEffect', -1)
        cl_evact.EventChangeInkBeadReward(oWarrior, oEventCB, 0, 10000)


def DoCallBackAction3(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('DoubleEffect') == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'DoubleEffect', -1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Times', 1)
    cl_action.CommonPickUpAllInkBead(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction6(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 3611
    m_Name = '珠连墨续'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 117

