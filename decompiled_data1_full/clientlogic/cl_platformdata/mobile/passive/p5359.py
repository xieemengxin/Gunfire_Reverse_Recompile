# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5359.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5359.pyc
# Source Generated with Decompyle++
# File: p5359.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeServantAttr(oWarrior, oLifeCycle, 'Att', (lambda *a: Func717(*a, **{
'sArg': 'AttMul' }) * 100), 0, 0)
    cl_action.CommonChangeServantAttr(oWarrior, oLifeCycle, 'AttSpeed', (lambda *a: Func717(*a, **{
'sArg': 'AttSpeedMul' }) * 100), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5359
    m_Name = '#NT#小玖改装2'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'AttMul': 25,
        'AttSpeedMul': 10 }
    m_DieDisable = 0

