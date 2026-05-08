# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5364.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5364.pyc
# Source Generated with Decompyle++
# File: p5364.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func311, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DYING, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    if cl_evcon.EventCBCheckTriggerOwner(oWarrior, oEventCB):
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: Func311(*a) - 100))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33936, 0, {
        'DamReduceMul': (lambda *a: Func717(*a, **{
'sArg': 'DamReduceMul' }) * 100),
        'SpeedMul': (lambda *a: Func717(*a, **{
'sArg': 'SpeedMul' }) * 100),
        'RescueReduceMul': (lambda *a: Func717(*a, **{
'sArg': 'RescueReduceMul' }) * 100) }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5364
    m_Name = '#NT#小玖升级3'
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
    m_BaseArgData = {
        'DamReduceMul': 30,
        'SpeedMul': 50,
        'RescueReduceMul': 50 }
    m_DieDisable = 0

