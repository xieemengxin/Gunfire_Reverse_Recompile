# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5959.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5959.pyc
# Source Generated with Decompyle++
# File: p5959.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_BUILD, OBJ_ATTACK, OBJ_VICTIM, OBSTACLE_JAR, QUALITY_TYPE_CURSE, RELIC_TYPE_CURSE
from cl_newformula import Func207

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_KILL, ATTACKERSUBMSG_BUILD, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetIsPointClasses(oWarrior, oEventCB, OBSTACLE_JAR):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func207(*a))) >= 5:
            cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), -5)


class CPerform(CCustomPerform):
    m_SID = 5959
    m_Name = '蹑手蹑脚'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'StateSID': 33366 }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_CURSE
    m_DropShape = 5531
    m_ValidRemove = 0
    m_BasePrice = 0
    m_bCanSell = 0
    m_Quality = QUALITY_TYPE_CURSE

