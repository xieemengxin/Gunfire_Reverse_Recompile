# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15148.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15148.pyc
# Source Generated with Decompyle++
# File: p15148.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func208, Func3, Func361, Func505, Func651
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33461, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgsValue(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ItemID' })), (lambda *a: Func208(*a)))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 5 * cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, Func651(*a, **{
'sKey': 'ItemID' })))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a))):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Temp', (lambda *a: cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, Func651(*a, **{
'sKey': 'ItemID' }))))
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 33461, (lambda *a: Func361(*a, **{
'sid': 15148,
'sArgs': 'Temp' }) * 5 // Func505(*a)), 0, 0, 500)
        cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ItemID' })), (lambda *a: Func3(*a, **{
'a': int(Func361(*a, **{
'sid': 15148,
'sArgs': 'Temp' }) * 5),
'b': int(Func505(*a)) }) // 5))


class CPerform(CCustomPerform):
    m_SID = 15148
    m_Name = '充能弹丸'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

