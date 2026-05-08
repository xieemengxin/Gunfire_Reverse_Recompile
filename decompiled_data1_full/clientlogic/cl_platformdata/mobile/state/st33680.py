# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33680.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33680.pyc
# Source Generated with Decompyle++
# File: st33680.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import LEVEL_TYPE_BOSS, OBJ_SELF, STATE_ADD_LONGORSYNC, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_ELITE, WARRIOR_MONSTER, WARRIOR_NORMAL
from cl_newformula import Func404, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 4, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 4, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 0, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonChangeAttr(oTarget, oLifeCycle, 'HPMax', 0, (lambda *a: Func404(*a) * 100), 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_SELF)
    cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CheckDistance'), WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0)
    cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, '33680AdditionValue', 0)
    cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)
    cl_evact.StateSetSelfCount(oTarget, oEventCB, (lambda *a: cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, '33680AdditionValue') + Func437(*a, **{
'sKey': 'BossAddition' })))


def CallBack2(oEventCB, oTarget):
    if cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_NORMAL):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('NormalValue'), '33680AdditionValue')
    elif cl_evcon.CheckFightType(oTarget, oEventCB, WARRIOR_ELITE) and cl_evcon.CheckTargetIsSummon(oTarget, oEventCB) == 0:
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('EliteValue'), '33680AdditionValue')


def CallBack4(oEventCB, oTarget):
    if cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'BossAddition', oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('BossValue'))
    else:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'BossAddition', 0)


class CState(cl_state.CState):
    m_SID = 33680
    m_Name = '#NT#生命上限词条'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_LONGORSYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 0
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_DelayAction = {
        'action': DelayAction,
        'delay': 50 }
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        4: CallBack4 }

