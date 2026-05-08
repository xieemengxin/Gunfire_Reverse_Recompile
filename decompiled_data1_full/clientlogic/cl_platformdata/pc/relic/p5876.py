# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5876.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5876.pyc
# Source Generated with Decompyle++
# File: p5876.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import PF_SUBMSG_FILLBULLET, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func335, Func505, Func714

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AUTOFILLBULLET, -1, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_FILLBULLET, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AUTOFILLBULLET, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func335(*a))) == 0:
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'EmptyMagazine', 1, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'EmptyMagazine', 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1873, 600, { }, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func335(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a) * 50 / 100)):
        cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'EmptyMagazine', 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'EmptyMagazine', 0):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1885, 600, { }, 0, 0, None)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func714(*a))) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1873, 600, { }, 0, 0, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func714(*a))) == 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1885, 600, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 5876
    m_Name = '有始有终'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

