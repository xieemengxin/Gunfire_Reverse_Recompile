# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33764.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33764.pyc
# Source Generated with Decompyle++
# File: st33764.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import NWARRIOR_DROP_DICE, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_RECYCLEDROP, -1, 0, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventRecycleDropType(oTarget, oEventCB, NWARRIOR_DROP_DICE) and cl_evcon.CheckRandom(oTarget, oEventCB, 100, 50):
        cl_action.CommonChangeDiceEnergy(oTarget, oEventCB.GetCBLifeCycle(), (lambda *a: Func429(*a, **{
'sArg': 'Reward' })), 'st33764')
        cl_action.CommonSendMessage(oTarget, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_USEDICESPECIALITEM, -1, {
            'SpecialItemSID': (lambda *a: Func429(*a, **{
'sArg': 'SpecialItemSID' })) })


class CState(cl_state.CState):
    m_SID = 33764
    m_Name = '#NT#强化分解双倍骰子'
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
    m_CBFuncAction = {
        0: CallBack0 }

