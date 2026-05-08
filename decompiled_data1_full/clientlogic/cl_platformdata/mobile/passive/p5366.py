# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5366.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5366.pyc
# Source Generated with Decompyle++
# File: p5366.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJECT_SERVANT
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttrFromOwn(oWarrior, oLifeCycle, 7144, 'Pierce', (lambda *a: Func717(*a, **{
'sArg': 'PierceNum' })), 0, OBJECT_SERVANT, None)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1426, 'Pierce', 0, (lambda *a: Func717(*a, **{
'sArg': 'PierceNum' })))


class CPerform(CCustomPerform):
    m_SID = 5366
    m_Name = '#NT#小玖升级5'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'PierceNum': 1 }
    m_DieDisable = 0

