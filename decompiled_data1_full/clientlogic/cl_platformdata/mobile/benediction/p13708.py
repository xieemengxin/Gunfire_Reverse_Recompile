# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13708.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13708.pyc
# Source Generated with Decompyle++
# File: p13708.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddChangeEvent(oWarrior, oLifeCycle, {
        1: {
            30011002: 1,
            30011034: 1,
            30011060: 1,
            30011163: 1 },
        2: {
            30011089: 1,
            30011147: 1 },
        3: {
            30011090: 1,
            30011157: 1 },
        4: {
            30011091: 1 } })


class CPerform(CCustomPerform):
    m_SID = 13708
    m_Name = '千难万险'
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
    m_Career = None

