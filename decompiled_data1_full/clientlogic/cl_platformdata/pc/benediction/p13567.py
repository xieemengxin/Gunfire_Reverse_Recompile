# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13567.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13567.pyc
# Source Generated with Decompyle++
# File: p13567.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func598, Func717
from cl_commondefines import OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33878, 0, {
        'DamRatio': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })),
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33881, 0, {
        'MaxTotalDamCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxTotalDamCount' })) }, 1)
    cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33881, (lambda *a: Func598(*a, **{
'sKey': 'CauseCorrisionNum' }) // 9), 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckTargetAddState(oWarrior, oEventCB, 20027):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'p13567_CauseCorrision', 1)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 33878, 1, (lambda *a: Func717(*a, **{
'sArg': 'DamTime' })))
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'p13567_CauseCorrision') >= 4:
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'p13567_CauseCorrision', 0)
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33880, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })), { }, 1, 0, 0)
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33879, (lambda *a: Func717(*a, **{
'sArg': 'EffectTime' })), {
                'MoveSpeedMul': (lambda *a: Func717(*a, **{
'sArg': 'MoveSpeedMul' })) }, 0, 0, 0)
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'CauseCorrisionNum' }) % 9)) == 0:
            cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 33881, (lambda *a: Func598(*a, **{
'sKey': 'CauseCorrisionNum' }) // 9))


class CPerform(CCustomPerform):
    m_SID = 13567
    m_Name = '腐蚀凋零'
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
        'DamRatio': 2000,
        'DamTime': 1000,
        'MaxCount': 10,
        'MoveSpeedMul': 5000,
        'EffectTime': 200,
        'MaxTotalDamCount': 80 }
    m_DieDisable = 0
    m_Career = 119

