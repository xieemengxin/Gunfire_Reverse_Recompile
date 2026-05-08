# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33310.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33310.pyc
# Source Generated with Decompyle++
# File: st33310.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK, OBJ_SELF, STATE_ADD_EXCLUDE, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func385, Func386, Func404, Func437

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def CallBack1(oEventCB, oTarget):
    cl_evact.StateCBAddSelfStateStatistics(oTarget, oEventCB, (lambda *a: Func385(*a)), 'PFBulletCost')
    if cl_condition.StateCheckStatistics(oTarget, oEventCB.GetCBLifeCycle(), 'PFBulletCost') >= 0.05 * cl_evcon.GetEventWeaponPerformMaxPFBullet(oTarget, oEventCB) and cl_evcon.GetFormula(oTarget, oEventCB, (lambda *a: Func386(*a, **{
'sAttr': 'MaxPFBullet' }))) > 0:
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'AddCount', (lambda *a: Func437(*a, **{
'sKey': 'PFBulletCost' }) // 0.05 * Func386(*a, **{
'sAttr': 'MaxPFBullet' })))
        cl_evact.StateCBSetSelfStateStatistics(oTarget, oEventCB, 'PFBulletCost', (lambda *a: Func437(*a, **{
'sKey': 'PFBulletCost' }) - 0.05 * Func437(*a, **{
'sKey': 'AddCount' }) * Func386(*a, **{
'sAttr': 'MaxPFBullet' })))
        cl_action.CommonAddStateCount(oTarget, oEventCB.GetCBLifeCycle(), 33310, (lambda *a: Func437(*a, **{
'sKey': 'AddCount' }) * 6), 1500)


def CallBack3(oEventCB, oTarget):
    if cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()) > 0:
        cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func404(*a) * 100), DAM_TYPE_WEAPON, '')


class CState(cl_state.CState):
    m_SID = 33310
    m_Name = '双子铭刻'
    m_IsShow = 1
    m_Type = STATE_CLS_HELP
    m_EffType = STATE_EFF_NONE
    m_AddType = STATE_ADD_EXCLUDE
    m_TargetType = OBJ_SELF
    m_MinCount = 0
    m_MaxCount = 150
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
        1: CallBack1,
        3: CallBack3 }

