# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33498.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33498.pyc
# Source Generated with Decompyle++
# File: st33498.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import OBJ_SELF, STATE_ADD_SYNC, STATE_CLS_HELP, STATE_EFF_NONE, TRANSFER_DIRTO_NEXT
from cl_newformula import Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WARMGR_INTERACTTRANSFER, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 1, 1)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckTransferType(oTarget, oEventCB, TRANSFER_DIRTO_NEXT):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBRecorvyInscriptionAndGrade(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'TaskID' })), (lambda *a: Func429(*a, **{
'sArg': 'WeaponGrade' })))
    if cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func429(*a, **{
'sArg': 'ClearPunishEnd' }))):
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33498
    m_Name = '#NT#清除武器锻造任务惩罚'
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_SYNC
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 0
    m_StartCount = 0
    m_PerCountTime = 0
    m_SyncMax = 0
    m_OnlyShowTarget = ()
    m_SaveToRecord = 1
    m_ClientData = { }
    m_Desc = '0'
    m_ShowStateCnt = 1
    m_Action = (StateActAction, None)
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1 }

