# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4112.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4112.pyc
# Source Generated with Decompyle++
# File: p4112.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_commondefines import WARRIOR_OBSTACLE_BROKENPILLAR
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import HP_RADIO_SUB, OBJ_ATTACK, OBJ_SELF, WARRIOR_BOSS
from cl_newformula import Func205

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 70, HP_RADIO_SUB, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 40, HP_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 10, HP_RADIO_SUB, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func205(*a) * 100))
    else:
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 56, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 57, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 58, 0)


class CPerform(CCustomPerform):
    m_SID = 4112
    m_Name = '一幕石柱'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oWarrior, oEventCB, dInfo):
    if oWarrior.m_FightType != WARRIOR_OBSTACLE_BROKENPILLAR:
        return None
    if not oWarrior.m_PaModel:
        return None
    oModel = oWarrior.m_PaModel.pop()
    oModel.E_Unstall()

