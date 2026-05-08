# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25877.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25877.pyc
# Source Generated with Decompyle++
# File: p25877.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_PERSISTENCE, DAM_TYPE_TRUE, DAM_USE_ALL, NORMAL_DAMAGE, OBJ_VICTIM, QUALITY_TYPE_LOW, WARRIOR_HERO
from cl_newformula import Func334

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_PERSISTENCE) == 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func334(*a) * 0.5), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, 1, 0, 0, NORMAL_DAMAGE, None, None)


class CPerform(CCustomPerform):
    m_SID = 25877
    m_Name = '火中取栗'
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
    m_HeroRelic = 5877
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

