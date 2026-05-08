# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14006.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14006.pyc
# Source Generated with Decompyle++
# File: p14006.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MONSTER_PART_SHIELD, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACKED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATEMONSTER, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckHitPart(oWarrior, oEventCB, MONSTER_PART_SHIELD) and cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) and cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 200)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.PassiveCBUsePerform2EvtTarget(oWarrior, oEventCB, 1721, None, { }, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 8110, 3, None, None)


class CPerform(CCustomPerform):
    m_SID = 14006
    m_Name = '轮回9-命中盾牌反弹攻击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

