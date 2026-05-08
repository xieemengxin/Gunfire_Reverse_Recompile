# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13564.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13564.pyc
# Source Generated with Decompyle++
# File: p13564.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ENERGY_RS_LIONENHANCETHROW, OBJ_SELF
from cl_newformula import Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1439, 'MinUseEnergy', 6000)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1439, 'CostAllEnergy', 1, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckChangeEnergyReason(oWarrior, oEventCB, ENERGY_RS_LIONENHANCETHROW):
        if cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 15305):
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' }))) >= 18000:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33771, 2400, {
                    'StateCount': (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' }) // 100) }, 1, 0, 0)
            elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' }))) >= 12000:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33771, 1800, {
                    'StateCount': (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' }) // 100) }, 1, 0, 0)
            else:
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33771, 1200, {
                    'StateCount': (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' }) // 100) }, 1, 0, 0)
        else:
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33771, 1200, {
                'StateCount': (lambda *a: Func651(*a, **{
'sKey': 'TrueEnergyChange' }) // 100) }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if (cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 8155) or cl_evcon.EventCBCheckFromPointState(oWarrior, oEventCB, 8156)) and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TransFlag') == 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, (lambda *a: (Func651(*a, **{
'sKey': 'RemainTime' }) // 100) * 500))


class CPerform(CCustomPerform):
    m_SID = 13564
    m_Name = '焚元化劫'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 118

