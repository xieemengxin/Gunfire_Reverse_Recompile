# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5747.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5747.pyc
# Source Generated with Decompyle++
# File: p5747.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL, WARRIOR_MONSTER, WARRIOR_OBSTACLE, WARRIOR_SUMMON

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, -1, 0, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11044, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, -1, 1, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11044, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_OBSTACLE) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_SUMMON):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1129, 200, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_MONSTER) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_OBSTACLE) or cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_SUMMON):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1129, 400, { }, 1, None, None)


class CPerform(CCustomPerform):
    m_SID = 5747
    m_Name = '妙手空空'
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
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

