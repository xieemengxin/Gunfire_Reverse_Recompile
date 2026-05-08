# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14606.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14606.pyc
# Source Generated with Decompyle++
# File: p14606.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8151, 0, {
        'StateCount': (lambda *a: Func361(*a, **{
'sid': 14606,
'sArgs': 'EffectVal' })) }, 1)


class CPerform(CCustomPerform):
    m_SID = 14606
    m_Name = '骰子挑战1技能'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

