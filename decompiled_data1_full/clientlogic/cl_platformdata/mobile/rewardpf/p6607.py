# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6607.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6607.pyc
# Source Generated with Decompyle++
# File: p6607.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, 'pf6607') == 0:
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'pf6607', 1)
        cl_action.CommonGetPetEggs(oWarrior, oLifeCycle, {
            1: 1,
            2: 1 })


class CPerform(CCustomPerform):
    m_SID = 6607
    m_Name = '赛季天赋1008'
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

