# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5792.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5792.pyc
# Source Generated with Decompyle++
# File: p5792.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import PF_SUBMSG_SWITCHWEAPON, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_SWITCHWEAPON, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_END, PF_SUBMSG_SWITCHWEAPON, 1, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11048, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBFillBullet(oWarrior, oEventCB)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1396, 300, { }, 1, 1, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 1434):
        cl_evact.PassiveCBFillBullet(oWarrior, oEventCB)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1396, 300, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1434, 3)
    else:
        cl_evact.PassiveCBFillBullet(oWarrior, oEventCB)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1396, 300, { }, 1, 1, None)
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1434, 0, { }, 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 5792
    m_Name = '快速装填'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

