# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5360.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5360.pyc
# Source Generated with Decompyle++
# File: p5360.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'MoveSpeed', (lambda *a: Func717(*a, **{
'sArg': 'SpeedMul' }) * 100), 0, 0)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, (lambda *a: Func717(*a, **{
'sArg': 'ResistanceAdd' }) * 100), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 5360
    m_Name = '#NT#小玖改装3'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'SpeedMul': 10,
        'ResistanceAdd': 10 }
    m_DieDisable = 0

