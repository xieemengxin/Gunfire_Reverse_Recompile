# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4371.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4371.pyc
# Source Generated with Decompyle++
# File: p4371.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func578
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_ATTACK

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_CMD_SWITCHSNIPE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddSourceWeaponSpecialAttrBase(oWarrior, oEventCB.GetCBLifeCycle(), 'EnergyBar', (lambda *a: -Func578(*a, **{
'sAttr': 'EnergyBar' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        if cl_evcon.CheckShootStatus(oWarrior, oEventCB):
            cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 0, 10, 2)
            cl_action.CommonListenSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
        else:
            cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())
            cl_action.CommonDoneSnapshotMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0:
        cl_action.CommonAddSourceWeaponSpecialAttrBase(oWarrior, oEventCB.GetCBLifeCycle(), 'EnergyBar', -1)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 10)
    cl_action.CommonAddSourceWeaponSpecialAttrBase(oWarrior, oEventCB.GetCBLifeCycle(), 'EnergyBar', 10)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func578(*a, **{
'sAttr': 'EnergyBar' }) * 50), 0, '')


class CPerform(CCustomPerform):
    m_SID = 4371
    m_Name = '啄木鸟能量增伤'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

