# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25829.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25829.pyc
# Source Generated with Decompyle++
# File: p25829.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK, QUALITY_TYPE_HIGH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 10, 8):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 15000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 25829
    m_Name = '合理幸运'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5829
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

