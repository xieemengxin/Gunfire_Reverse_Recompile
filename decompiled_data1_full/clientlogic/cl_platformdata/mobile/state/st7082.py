# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st7082.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st7082.pyc
# Source Generated with Decompyle++
# File: st7082.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import MONSTER_PART_RIGHTGUN, OBJ_SELF, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func403, Func423, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 0)


def StateRemoveAction(oTarget, oLifeCycle):
    cl_action.StateAddState(oTarget, oLifeCycle, 7083, 500, { }, None)
    if not cl_condition.HasState(oTarget, oLifeCycle, 7079):
        cl_action.CommonHaltPointPerform(oTarget, oLifeCycle, 22031)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckHitPart(oTarget, oEventCB, MONSTER_PART_RIGHTGUN) and cl_evcon.CheckAttackInShield(oTarget, oEventCB):
        cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func423(*a) // 100), 'RightGunDamage')
        if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func437(*a, **{
'sKey': 'RightGunDamage' }))) >= 0.01 * cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func403(*a, **{
'sAttr': 'HPMax' }) * 11 / 100 + 1)):
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 7082
    m_Name = '#NT#火箭炮兵-右炮筒-可用'
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
    m_Action = (StateActAction, StateRemoveAction)
    m_CBFuncAction = {
        0: CallBack0 }

