# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25820.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25820.pyc
# Source Generated with Decompyle++
# File: p25820.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_HERO
from cl_newformula import Func374

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckVictimFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 20026) == 0 and cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 1689) == 0 and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1765, 0, 1, None) == 0:
            cl_evact.EventClientBehavior(oWarrior, oEventCB, 25820, 0)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1765, 300, { }, 1, 1, None)
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 5, WARRIOR_HERO, 0, 0, 0, 0, 0, None, None)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 10 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, 1, 0, -1, None, None, None)


class CPerform(CCustomPerform):
    m_SID = 25820
    m_Name = '爆破子弹'
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
    m_HeroRelic = 5820
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

