# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5702.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5702.pyc
# Source Generated with Decompyle++
# File: p5702.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1610, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 15, None, None):
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, 9000, 0, '')
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -9000, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1610, 0, None):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.GetMainHoldWeaponPos(oWarrior, oEventCB) == 1:
            if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 15, None, None):
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, 9000, 0, '')
            else:
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -9000, 0, '')
        if cl_evcon.GetMainHoldWeaponPos(oWarrior, oEventCB) == 2:
            if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 15, None, None):
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -9000, 0, '')
            else:
                cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, 9000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 5702
    m_Name = '偏折护盾'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

