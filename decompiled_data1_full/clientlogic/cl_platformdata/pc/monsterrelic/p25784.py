# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25784.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25784.pyc
# Source Generated with Decompyle++
# File: p25784.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_ATTACK, OBJ_VICTIM, QUALITY_TYPE_HIGH

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1708, 1000, { }, 1, -1, None)
    if cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 25):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, -10000, 0, '')
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, 100, DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_TYPE_NORMAL | DAM_USE_ALL, 1, 0, 0, 0, -1, -1, -1, -1, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 25784
    m_Name = '门板重盾'
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
    m_HeroRelic = 5784
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

