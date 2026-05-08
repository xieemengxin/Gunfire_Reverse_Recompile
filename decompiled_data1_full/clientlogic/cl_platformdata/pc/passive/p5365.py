# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5365.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5365.pyc
# Source Generated with Decompyle++
# File: p5365.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJECT_SERVANT
from cl_newformula import Func634, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBackFromOwnByAttr(oWarrior, oLifeCycle, 'HPMax', 0, OBJECT_SERVANT)
    cl_action.CommonChangeServantAttr(oWarrior, oLifeCycle, 'Att', (lambda *a: (max(Func634(*a, **{
'sAttr': 'HPMax' }), 0) // 50) * Func717(*a, **{
'sArg': 'DamMul' })), 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeServantAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'Att', (lambda *a: (max(Func634(*a, **{
'sAttr': 'HPMax' }), 0) // 50) * Func717(*a, **{
'sArg': 'DamMul' })), 0, 1)


class CPerform(CCustomPerform):
    m_SID = 5365
    m_Name = '#NT#小玖升级4'
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
        'DamMul': 1 }
    m_DieDisable = 0

