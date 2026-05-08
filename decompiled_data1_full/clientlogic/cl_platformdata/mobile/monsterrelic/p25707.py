# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25707.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25707.pyc
# Source Generated with Decompyle++
# File: p25707.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, OBJ_SELF, OBJ_VICTIM, QUALITY_TYPE_NORMAL
from cl_newformula import Func374

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 1700):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.CheckTargetIsSelf(oWarrior, oEventCB):
            cl_evact.EventTargetSputterDamage(oWarrior, oEventCB, 50, 0, 0, 0, 0, 1, 0, 1, 0, None)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func374(*a) * 5 / 100), DAM_TYPE_WEAPON | DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 0, 0, 0, -1, 0, 0, None, None, None)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1700, 100, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25707
    m_Name = '浸血弹药'
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
    m_HeroRelic = 5707
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

