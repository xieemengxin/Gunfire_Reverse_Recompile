# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st8150.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st8150.pyc
# Source Generated with Decompyle++
# File: st8150.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MONSTER_PART_S6CHALLENGEPFSHIELD, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_NORMAL
from cl_newformula import Func374, Func423, Func429, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)
    if cl_condition.CheckTargetFightType(oTarget, oLifeCycle, WARRIOR_NORMAL):
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 2, 0, 0)
    else:
        cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_S6CHALLENGEPFSHIELD) or cl_evcon.CheckDamIsExplosion(oTarget, oEventCB):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func423(*a)), 'PredictPartDamage')
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'PredictPartDamage' }))) >= oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('Shield'):
            cl_action.CommonSendStateMessage(oTarget, oEventCB.GetCBLifeCycle(), 0, { })
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'Shield', (lambda *a: Func374(*a) * Func429(*a, **{
'sArg': 'MinorVal' }) * 100 // 10000))


def CallBack3(oEventCB, oTarget):
    cl_action.StateSetArgValue(oTarget, oEventCB.GetCBLifeCycle(), 'Shield', (lambda *a: Func374(*a) * Func429(*a, **{
'sArg': 'MinorVal' }) * 50 // 10000))


class CState(cl_state.CState):
    m_SID = 8150
    m_Name = '#NT#s6挑战技能2'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2,
        3: CallBack3 }

