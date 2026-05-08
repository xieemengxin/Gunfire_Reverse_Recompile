# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/state/st33441.pyc
# RelativePath: clientlogic/cl_platformdata/pc/state/st33441.pyc
# Source Generated with Decompyle++
# File: st33441.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import DEPUTY_HOLD, MAIN_HOLD, OBJ_SELF, PF_SUBMSG_FILLBULLET, STATE_ADD_EXCLUDE, STATE_CLS_ABNORMAL, STATE_EFF_NONE, WUDI_START
from cl_newformula import Func507

def StateActAction(oTarget, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_AUTOFILLBULLET, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEWEAPON, -1, 5, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_WUDI, WUDI_START, 6, 0, 0)


def StateCountAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    if cl_evcon.CheckEventWeaponHoldType(oTarget, oEventCB, MAIN_HOLD):
        cl_action.CommonSetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 0, 33441, '', MAIN_HOLD)
        cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MaxBullet', 0, 0, MAIN_HOLD)
        cl_evact.EventSetSkillCache(oTarget, oEventCB, 'MaxBullet', (lambda *a: Func507(*a)))
        cl_action.CommonSetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 0, 33441, '', MAIN_HOLD)
        if cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 1) == 0 and cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 2) == 0 and cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 3) == 0:
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_action.CommonSetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 0, 33441, '', DEPUTY_HOLD)
            cl_action.CommonChangeWeaponAttr(oTarget, oEventCB.GetCBLifeCycle(), 'MaxBullet', 0, 0, DEPUTY_HOLD)
            cl_evact.EventSetSkillCache(oTarget, oEventCB, 'MaxBullet', (lambda *a: Func507(*a)))
            cl_action.CommonSetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 0, 33441, '', DEPUTY_HOLD)
            if cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 1) == 0 and cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 2) == 0 and cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 3) == 0:
                cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack1(oEventCB, oTarget):
    if cl_condition.CheckDualSate(oTarget, oEventCB.GetCBLifeCycle()):
        cl_action.CommonAddStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), -2500, 33441, '', 0)
        if cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, None) < -10000:
            cl_action.CommonSetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), -10000, 33441, '', MAIN_HOLD)
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MaxBullet', 0, cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, None), MAIN_HOLD)
        else:
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MaxBullet', 0, cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, None), MAIN_HOLD)
        if cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', DEPUTY_HOLD, None) < -10000:
            cl_action.CommonSetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), -10000, 33441, '', DEPUTY_HOLD)
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MaxBullet', 0, cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', DEPUTY_HOLD, None), DEPUTY_HOLD)
        else:
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MaxBullet', 0, cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', DEPUTY_HOLD, None), DEPUTY_HOLD)
    else:
        cl_action.CommonAddStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), -2500, 33441, '', MAIN_HOLD)
        if cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, None) < -10000:
            cl_action.CommonSetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), -10000, 33441, '', MAIN_HOLD)
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MaxBullet', 0, cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, None), MAIN_HOLD)
        else:
            cl_evact.StateCBChangeWeaponAttr(oTarget, oEventCB, 'MaxBullet', 0, cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, None), MAIN_HOLD)


def CallBack5(oEventCB, oTarget):
    CustomAction(oTarget, oEventCB, {
        'Statis': 0,
        'StateSID': 33441 })
    if cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 1) == 0 and cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 2) == 0 and cl_action.CommonGetStateStatisticsKeyItemID(oTarget, oEventCB.GetCBLifeCycle(), 33441, '', MAIN_HOLD, 3) == 0:
        cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack6(oEventCB, oTarget):
    cl_evact.StateCBSelfRemove(oTarget, oEventCB)


class CState(cl_state.CState):
    m_SID = 33441
    m_Name = '军火商人（怪物）'
    m_IsShow = 1
    m_Type = STATE_CLS_ABNORMAL
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
    m_ShowStateCnt = 0
    m_Action = (StateActAction, None)
    m_CountFunc = {
        'action': StateCountAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        5: CallBack5,
        6: CallBack6 }


def CustomAction(oTarget, oEventCB, dArgs):
    if 'Statis' not in dArgs or 'StateSID' not in dArgs:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    cl_action.CommonStateStatistics(oTarget, oEventCB.GetCBLifeCycle(), dArgs['StateSID'], dArgs['Statis'], str(dMsgInfo['ItemID']))

