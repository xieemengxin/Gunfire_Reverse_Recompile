# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25740.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25740.pyc
# Source Generated with Decompyle++
# File: p25740.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GOTDEBUFF, -1, 2, 0, 0)
    cl_action.PassiveSetSelfColdTime(oWarrior, oLifeCycle, 1000)


def CDAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckHasLockEnemy(oWarrior, oEventCB.GetCBLifeCycle()):
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1000)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('25740Cover'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25740Cover', 0)
            cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1)
        cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
            3: 3333,
            4: 3333,
            5: 3334 }, 1)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25740Cover', 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 1000)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('25740Cover'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, '25740Cover', 0)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_MONSTER_START_HATE, -1)
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        3: 3333,
        4: 3333,
        5: 3334 }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveSubSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 50)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1962, 0, { })


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1963, 0, { })


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1964, 0, { })


class CPerform(CCustomPerform):
    m_SID = 25740
    m_Name = '元素汇流'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = {
        1: CDAction1 }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5740
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

