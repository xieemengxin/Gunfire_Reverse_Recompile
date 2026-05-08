# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/state/st33577.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/state/st33577.pyc
# Source Generated with Decompyle++
# File: st33577.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_formula
import cl_evact
import cl_evcon
import cl_state
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, DPSUBMSG_DEFAULT, EQUIP_LASER, OBJ_ATTACK, OBJ_SELF, STATE_ADD_LONGORSYNC, STATE_CLS_HELP, STATE_EFF_NONE
from cl_newformula import Func404, Func429

def StateActAction(oTarget, oLifeCycle):
    cl_action.StateSetSelfCount(oTarget, oLifeCycle, (lambda *a: Func429(*a, **{
'sArg': 'StateCount' }) * 10))
    cl_action.CommonListenSnapshotMsg(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_DEFAULT, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oTarget, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def CallBack0(oEventCB, oTarget):
    cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'ST33577', 1, 0)


def CallBack1(oEventCB, oTarget):
    if cl_evcon.CheckSkillCollectInfo(oTarget, oEventCB, 'ST33577', 0):
        cl_evact.EventCBSetCollectInfo(oTarget, oEventCB, 'ST33577', 0, 0)
        if cl_evcon.CheckEventWeaponType(oTarget, oEventCB, EQUIP_LASER) or cl_evcon.CheckFromPointPerform(oTarget, oEventCB, 9415, 1, 0):
            cl_evact.EventChangeDamFactor(oTarget, oEventCB, OBJ_ATTACK, (lambda *a: Func404(*a) * 100), 0, 0, '')
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)
        else:
            cl_evact.StateCBChangeSkillDamFactor(oTarget, oEventCB, (lambda *a: Func404(*a) * 100), 0, DAM_TYPE_WEAPON, 0, 0)
            cl_evact.StateCBSelfRemove(oTarget, oEventCB)


def CallBack3(oEventCB, oTarget):
    if 10 * cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'NewAdditionCount') >= cl_condition.StateGetSelfCount(oTarget, oEventCB.GetCBLifeCycle()):
        cl_evact.StateSetSelfCount(oTarget, oEventCB, 10 * cl_evact.StateCBGetSelfStateStatistics(oTarget, oEventCB, 'NewAdditionCount'))


def StateRefreshAction(oTarget, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oTarget, oLifeCycle, 3, 0, 0)


class CState(cl_state.CState):
    m_SID = 33577
    m_Name = '压缩弹夹'
    m_IsShow = 1
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
    m_RefreshFunc = {
        'action': StateRefreshAction }
    m_CBFuncAction = {
        0: CallBack0,
        1: CallBack1,
        3: CallBack3 }

