# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33225.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33225.pyc
# Source Generated with Decompyle++
# File: st33225.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import LEVEL_TYPE_HIDE, OBJECT_CURPET, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func207, Func661

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func661(*a, **{
'iAbility': 50558,
'sKey': 'AddRecord' })))
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 10)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonSetPetAbilityInheritInfo(oTarget, oLifeCycle, 50558, 'AddRecord', cl_action.StateGetSelfCount(oTarget, oLifeCycle))
    cl_action.CommonChangeOwnerObjectAttr(oTarget, oLifeCycle, OBJECT_CURPET, 'Att', 800 * cl_action.StateGetSelfCount(oTarget, oLifeCycle), 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEnterNewSecne(oTarget, oEventCB) and cl_evcon.CheckLevelType(oTarget, oEventCB, LEVEL_TYPE_HIDE) == 0 and cl_condition.CalFormula(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func207(*a))) >= 100:
        cl_action.CommonAddWarCash(oTarget, oEventCB.GetCBLifeCycle(), -100)
        cl_action.StateAddSelfCount(oTarget, oEventCB.GetCBLifeCycle(), 1, None)


class CState(cl_state.CState):
    m_SID = 33225
    m_Name = '#NT#词条50558'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
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
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0 }

