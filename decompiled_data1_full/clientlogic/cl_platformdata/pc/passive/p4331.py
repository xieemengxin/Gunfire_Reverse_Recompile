# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4331.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4331.pyc
# Source Generated with Decompyle++
# File: p4331.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction4331 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PLAYMODE_NEWSURVIVOR, PLAYMODE_SURVIVOR, TYPE_RELIFE_RESCUE
from cl_newformula import Func567

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonCreateServant(oWarrior, oLifeCycle, 301, 1, 10, 0, 180)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERONREADY, -1, 2, 0, 0)
    cl_action.CommonDisablePF(oWarrior, oLifeCycle, 1322, 1)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'MoveSpeed', -1, 4, 0, 0)
    if cl_condition.CheckWarPlayMode(oWarrior, oLifeCycle, PLAYMODE_SURVIVOR) or cl_condition.CheckWarPlayMode(oWarrior, oLifeCycle, PLAYMODE_NEWSURVIVOR):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 32881, 0, { }, 0)
    if cl_condition.CheckOpenElement(oWarrior, oLifeCycle, {
        'EndlessElement': 1,
        'RealEndlessElement': 1 }):
        cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTENDLESS, -1, 5)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckRelifeType(oWarrior, oEventCB, TYPE_RELIFE_RESCUE):
        cl_action.CommonRelifeServant(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckReenter(oWarrior, oEventCB):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func567(*a))) == 1:
            cl_action.CommonSwitchPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1321)
        else:
            cl_action.CommonSwitchPerform(oWarrior, oEventCB.GetCBLifeCycle(), 1322)


def DoCallBackAction4(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33029, 0, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 4331
    m_Name = '御灵师被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

