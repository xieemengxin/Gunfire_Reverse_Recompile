# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15195.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15195.pyc
# Source Generated with Decompyle++
# File: p15195.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_THROW
from cl_newformula import Func361, Func385, Func386, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTPFBULLET, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1) == 0 and cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 50)
        cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, 0, 0, 10)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgsValue(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ItemID' })), (lambda *a: Func385(*a)))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 2 * cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, Func651(*a, **{
'sKey': 'ItemID' })))) >= cl_evcon.GetEventWeaponPerformMaxPFBullet(oWarrior, oEventCB):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Temp', (lambda *a: cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, Func651(*a, **{
'sKey': 'ItemID' }))))
        cl_evact.PassiveCBAddPFArgsValue(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ItemID' })), (lambda *a: -((2 * Func361(*a, **{
'sid': 15195,
'sArgs': 'Temp' }) // Func386(*a, **{
'sAttr': 'MaxPFBullet' })) * Func386(*a, **{
'sAttr': 'MaxPFBullet' }) // 2)))
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: 2 * Func361(*a, **{
'sid': 15195,
'sArgs': 'Temp' }) // cl_evcon.GetEventWeaponPerformMaxPFBullet(oWarrior, oEventCB)), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ItemID' })), 0)


class CPerform(CCustomPerform):
    m_SID = 15195
    m_Name = '灵力补给'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

