# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5762.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5762.pyc
# Source Generated with Decompyle++
# File: p5762.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DROP_BULLETPICK_CHANGE, NWARRIOR_DROP_BULLET, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetBulletPickModule(oWarrior, oLifeCycle, DROP_BULLETPICK_CHANGE)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 0, 0, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonSetBulletPickModule(oWarrior, oLifeCycle, DROP_BULLETPICK_CHANGE)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, -1, 1, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_BULLET):
        cl_evact.PassiveCBChangeBulletWieldType(oWarrior, oEventCB)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPickType(oWarrior, oEventCB, NWARRIOR_DROP_BULLET):
        cl_evact.PassiveCBChangeBulletWieldType(oWarrior, oEventCB)
        cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), 3)


class CPerform(CCustomPerform):
    m_SID = 5762
    m_Name = '子弹银行'
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
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

