# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25781.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25781.pyc
# Source Generated with Decompyle++
# File: p25781.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_FIRE, OBJ_VICTIM, QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetDamageType(oWarrior, oEventCB, DAM_TYPE_FIRE)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, -1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, -3000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 25781
    m_Name = '火焰碎片'
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
    m_HeroRelic = 5781
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

