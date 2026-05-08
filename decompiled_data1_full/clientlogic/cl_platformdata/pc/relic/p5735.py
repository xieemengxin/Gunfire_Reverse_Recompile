# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5735.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5735.pyc
# Source Generated with Decompyle++
# File: p5735.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_FILLBULLET, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func505

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        1: 3333,
        4: 6667 }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveReduceFillBulletUse(oWarrior, oEventCB)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1397, 0, { }, 1, 1, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.CBTriggerGroup(oWarrior, oEventCB, {
        3: 3333,
        4: 6667 }, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveReduceFillBulletUse(oWarrior, oEventCB)
    cl_evact.EventCBAddSourceWeaponBagBullet(oWarrior, oEventCB, (lambda *a: Func505(*a)))
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1397, 0, { }, 1, 1, None)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 1397, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 5735
    m_Name = '魔术弹夹'
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
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

