# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5795.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5795.pyc
# Source Generated with Decompyle++
# File: p5795.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, CURE_TYPE_PERFORM, DAM_TYPE_FIRE, DAM_USE_HP, OBJ_ATTACK, OBJ_SELF, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func213, Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20026):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20026, (lambda *a: Func213(*a) * 100 / 100 + 0), {
            'AbnormalSourceDam': 2500 }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, None) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 20026, 0, None, None) and cl_evcon.CheckAttackIsVictim(oWarrior, oEventCB) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 20 // 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 4)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20026):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 20026, (lambda *a: Func213(*a) * 100 / 100 + 0), {
            'AbnormalSourceDam': 2500 }, 1, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckEleDamType(oWarrior, oEventCB, DAM_TYPE_FIRE, None) and cl_evcon.CheckAttackIsVictim(oWarrior, oEventCB) == 0:
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: (Func304(*a, **{
'sAttr': 'HPMax' }) - Func304(*a, **{
'sAttr': 'HP' })) * 20 // 100), CURE_TYPE_PERFORM | DAM_USE_HP, 0, 0, 4)


class CPerform(CCustomPerform):
    m_SID = 5795
    m_Name = '火焰狂热'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 40
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

