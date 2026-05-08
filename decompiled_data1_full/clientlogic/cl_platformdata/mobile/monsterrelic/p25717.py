# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25717.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25717.pyc
# Source Generated with Decompyle++
# File: p25717.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_ELITE
from cl_newformula import Func305

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', 5000, 0, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, 5000, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        if cl_condition.CheckTargetFightType(oWarrior, oEventCB.GetCBLifeCycle(), WARRIOR_ELITE):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 0.6 / 100 + 0))
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
        else:
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
            cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func305(*a, **{
'sAttr': 'HPMax' }) * 3 / 100 + 0))
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1717, 100, { }, -1, -1, None)
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 100)


class CPerform(CCustomPerform):
    m_SID = 25717
    m_Name = '鲜血圣物'
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
    m_RelicType = 0
    m_HeroRelic = 5717
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

