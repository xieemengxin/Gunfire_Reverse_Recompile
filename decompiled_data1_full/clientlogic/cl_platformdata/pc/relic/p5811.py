# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5811.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5811.pyc
# Source Generated with Decompyle++
# File: p5811.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import BOX_TREBLE_DAMAGE, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_ATTACK, PF_SUBMSG_THROW, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func374, Func420, Func421

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11137, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 0, 0, -1)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11137, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func420(*a) - Func421(*a))) >= 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min((Func421(*a) - Func420(*a)) * Func374(*a) * 15 / 100, Func374(*a) - 100)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 1, 0, -1, -1, -1, 0, BOX_TREBLE_DAMAGE, None, None)
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32719):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32719, 100, { }, -1, -1, None)
            cl_evact.EventClientBehavior(oWarrior, oEventCB, 1080, -1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func420(*a) - Func421(*a))) >= 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
        cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: min((Func421(*a) - Func420(*a)) * Func374(*a) * 15 / 100, Func374(*a) - 100)), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 1, 0, -1, -1, -1, 0, BOX_TREBLE_DAMAGE, None, None)
        if not cl_evcon.CheckHasState(oWarrior, oEventCB, 32719):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32719, 100, { }, -1, -1, None)
            cl_evact.EventClientBehavior(oWarrior, oEventCB, 1080, -1)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1410, 500, { }, 1, -1, None)
        cl_evact.PassiveCBAddTargetStateCount(oWarrior, oEventCB, 1410, 1, -1)


class CPerform(CCustomPerform):
    m_SID = 5811
    m_Name = '能力透支'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

