# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p50703.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p50703.pyc
# Source Generated with Decompyle++
# File: p50703.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func555, Func585, Func593, Func617

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetFlawData(oWarrior, oLifeCycle, (lambda *a: Func593(*a) ** 1.1 * min(2, Func555(*a, **{
'sAttr': 'Att' }) / 8000) * 500 * 0.8 * (1 - (Func617(*a, **{
'iSID': 218 }) - 2) * 0.2)), 300, 99, 300, 300, 1000, (lambda *a: Func585(*a) * 2), 450, 5, 1, 0, 120, 850, 1, 0, 10000)


class CPerform(CCustomPerform):
    m_SID = 50703
    m_Name = '#NT#妖化怪被动'
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

