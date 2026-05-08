# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25727.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25727.pyc
# Source Generated with Decompyle++
# File: p25727.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, JUMPFIGURE_BUYGOODS, OBJ_VICTIM, QUALITY_TYPE_LOW
from cl_newformula import Func369

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func369(*a))) > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1700, -1, -1, None) < 1:
            cl_evact.EventCBAddTargetCash(oWarrior, oEventCB, -10, 0, JUMPFIGURE_BUYGOODS, 0, 0)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1700, 100, { }, -1, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25727
    m_Name = '魔鬼契约'
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
    m_HeroRelic = 5727
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

