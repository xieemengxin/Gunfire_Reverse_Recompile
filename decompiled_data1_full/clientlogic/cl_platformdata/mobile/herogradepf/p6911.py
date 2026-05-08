# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/herogradepf/p6911.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/herogradepf/p6911.pyc
# Source Generated with Decompyle++
# File: p6911.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_newformula import Func3, Func361, Func672

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', 2000, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33251, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'InkValueChange', (lambda *a: abs(Func672(*a, **{
'iIsReal': 1 }))))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 6911,
'sArgs': 'InkValueChange' }))) >= 5:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddLevel', (lambda *a: Func361(*a, **{
'sid': 6911,
'sArgs': 'InkValueChange' }) // 5))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'InkValueChange', (lambda *a: Func3(*a, **{
'a': int(Func361(*a, **{
'sid': 6911,
'sArgs': 'InkValueChange' })),
'b': 5 })))
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33251, (lambda *a: Func361(*a, **{
'sid': 6911,
'sArgs': 'AddLevel' })), 1200)


class CPerform(CCustomPerform):
    m_SID = 6911
    m_Name = '水墨画师lv.1'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'InkValueChange': 0 }
    m_DieDisable = 0

