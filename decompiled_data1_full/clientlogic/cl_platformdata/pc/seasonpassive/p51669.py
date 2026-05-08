# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51669.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51669.pyc
# Source Generated with Decompyle++
# File: p51669.pyc (Python 3.6)

from cl_platformdata.custom.seasonpassive.customaction import CustomAction51669 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM
from cl_newformula import Func372, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCnt', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCnt', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EnemyCnt', 1)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpreadCnt', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 3, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'pf51669Cnt', 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCnt', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 5)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EnemyCnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpreadCnt', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 3, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'pf51669Cnt', 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCnt', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EnemyCnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpreadCnt', 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PurpleCnt', 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 3, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'pf51669Cnt', 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1960)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddCnt', 2)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCnt', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 6000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Distance', 7)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'EnemyCnt', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'SpreadCnt', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'PurpleCnt', 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATECOUNTCHANGE, -1, 3, 0, 0)
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'pf51669Cnt', 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTriggerLuckyHit(oWarrior, oEventCB) and cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '51669', 1) == 0:
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 39735, 0, 1, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 39735, 0, {
                'MaxCnt': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxCnt') }, 0, 0, 0)
        cl_evact.EventCBSetTargetStateArgVal(oWarrior, oEventCB, 39735, 'LuckyHitEff', (lambda *a: Func372(*a)), 1)
        cl_evact.EventCBSetTargetStateArgVal(oWarrior, oEventCB, 39735, 'CrazyEff', (lambda *a: Func651(*a, **{
'sKey': 'CrazyEff' })), 1)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39735, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCnt'), 1, 0, 0)
        if cl_evcon.GetTriggerLuckyHit(oWarrior, oEventCB) >= 3 and oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('PurpleCnt') > 0 and cl_evcon.EventCBCheckTargetCDByMark(oWarrior, oEventCB, '51669', 1) == 0:
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39735, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'PurpleCnt'), 1, 0, None)


def DoCallBackAction3(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'StateSID': 39735 })


class CPerform(CCustomPerform):
    m_SID = 51669
    m_Name = '武器-幸运七星'
    m_MaxLevel = 4
    m_MaxStack = 2
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

