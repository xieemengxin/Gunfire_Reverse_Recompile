# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5328.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5328.pyc
# Source Generated with Decompyle++
# File: p5328.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction5328 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'SharkChaseHPLimit', (lambda *a: Func717(*a, **{
'sArg': 'ChaseHPLimit' })))
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'DefaultCanChaseSharkNum', (lambda *a: Func717(*a, **{
'sArg': 'DefaultCanChaseSharkNum' })))
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'HighCycleCanChaseSharkNum', (lambda *a: Func717(*a, **{
'sArg': 'HighCycleCanChaseSharkNum' })))
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 200, 200, 0)
    cl_action.CommonSetAgentInfo(oWarrior, oLifeCycle, 'CurPerformUseDis', 5)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 5328
    m_Name = '#NT#鲨鱼怪被动'
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
        'ChaseHPLimit': 15,
        'DefaultCanChaseSharkNum': 1,
        'HighCycleCanChaseSharkNum': 3 }
    m_DieDisable = 1

