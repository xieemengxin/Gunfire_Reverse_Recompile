# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5330.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5330.pyc
# Source Generated with Decompyle++
# File: p5330.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7170)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7171)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7172)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 7174)
    cl_action.CommonSwitchAttPerform(oWarrior, oLifeCycle, 7170)
    cl_action.CommonSetShape(oWarrior, oLifeCycle, 1104, 0)
    cl_action.CommonSetPlantCanTransferState(oWarrior, oLifeCycle, {
        33733: 1 })
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33668, 0, {
        'DotDam': (lambda *a: Func717(*a, **{
'sArg': 'DotDam' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 5330
    m_Name = '园丁巨树被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'DotDam': 1000 }
    m_DieDisable = 0

