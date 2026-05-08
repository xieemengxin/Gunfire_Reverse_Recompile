# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5358.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5358.pyc
# Source Generated with Decompyle++
# File: p5358.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.EventCBChangeTargetModel(oWarrior, oEventCB, (lambda *a: min(100 + Func717(*a, **{
'sArg': 'SizeAdd' }), 200)))
    cl_evact.EventCBChangeTargetPerformAttr(oWarrior, oEventCB, 7153, 'Radius', (lambda *a: Func717(*a, **{
'sArg': 'RangeMul' }) * 100), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5358
    m_Name = '#NT#小玖改装1'
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
        'SizeAdd': 15,
        'RangeMul': 15 }
    m_DieDisable = 0

