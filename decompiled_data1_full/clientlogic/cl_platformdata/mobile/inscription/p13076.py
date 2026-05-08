# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13076.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13076.pyc
# Source Generated with Decompyle++
# File: p13076.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import DPSUBMSG_NOFIRE, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD
from cl_newformula import Func666

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_NOFIRE, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK_END, DPSUBMSG_NOFIRE, 1, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_HALT, -1, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 0)
    cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COSTPFBULLET, -1)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func666(*a, **{
'iPerform': 9793,
'sKey': 'EnergyCost' }) * 1.5)) >= 15000 and cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COSTPFBULLET, -1)
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: min(15000, Func666(*a, **{
'iPerform': 9793,
'sKey': 'EnergyCost' }) * 1.5)))
    else:
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, (lambda *a: min(15000, Func666(*a, **{
'iPerform': 9793,
'sKey': 'EnergyCost' }) * 1.5)))


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9793, 0, 0):
        cl_evact.PassiveCBChangeSourceWeaponAttr(oWarrior, oEventCB, 'AttSpeed', 0, 0)
        cl_action.CommonDoneEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_COSTPFBULLET, -1)


class CPerform(CCustomPerform):
    m_SID = 13076
    m_Name = '璇玑2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1703,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

