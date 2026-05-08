# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5363.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5363.pyc
# Source Generated with Decompyle++
# File: p5363.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39677, 0, {
        'PerAttSpeedMul': (lambda *a: Func717(*a, **{
'sArg': 'PerAttSpeedMul' }) * 100),
        'AttRangeMul': (lambda *a: Func717(*a, **{
'sArg': 'AttRangeMul' }) * 100),
        'ReduceCD': (lambda *a: Func717(*a, **{
'sArg': 'ReduceCD' }) * 100),
        'MaxCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 5363
    m_Name = '#NT#小玖升级2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'ReduceCD': 2,
        'PerAttSpeedMul': 10,
        'AttRangeMul': 50,
        'MaxCount': 10 }
    m_DieDisable = 0

