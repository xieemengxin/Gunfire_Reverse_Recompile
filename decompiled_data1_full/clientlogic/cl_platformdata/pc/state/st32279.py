# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st32279.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st32279.pyc
# Source Generated with Decompyle++
# File: st32279.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CONSHOOT, STATE_ADD_REPLACE, STATE_CLS_HELP, STATE_EFF_NONE, WARRIOR_MONSTER
from cl_newformula import Func336, Func404

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DelayAction(oTarget, oLifeCycle):
    cl_action.StateAddSelfCount(oTarget, oLifeCycle, 1, None)


def CallBack0(oEventCB, oTarget):
    if not cl_evcon.CheckPerformType(oTarget, oEventCB, PF_TYPE_CONSHOOT, None) or cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'state32279', None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 10000), 0, DAM_TYPE_WEAPON, '')
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'state32279', 1)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_MONSTER, 1, 1, 0, 0, -1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    elif cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'state32279', None):
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'state32279' })), 0, DAM_TYPE_WEAPON, None, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_MONSTER, 1, 1, 0, 0, -1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)
    else:
        cl_evact.StateCBAddSkillCollectInfo(oTarget, oEventCB, 'state32279', (lambda *a: Func404(*a) * 10000))
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_ATTACK)
        cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * 10000), 0, DAM_TYPE_WEAPON, None, 0)
        cl_evact.EventGetTargetByType(oTarget, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oTarget, oEventCB, 10, WARRIOR_MONSTER, 1, 1, 0, 0, -1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oTarget, oEventCB, 2)
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack2(oEventCB, oTarget):
    cl_evact.EventTargetSputterDamage(oTarget, oEventCB, 100, 1, 0, -1, -1, -1, -1, 1, 1, None)


class CState(cl_state.CState):
    m_SID = 32279
    m_Name = '#NT#耐心猎手'
    m_DieRemove = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_REPLACE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 10
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
        'delay': 100,
        'firsttime': 100 }
    m_CBFuncAction = {
        0: CallBack0,
        2: CallBack2 }

