# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16077.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16077.pyc
# Source Generated with Decompyle++
# File: p16077.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import EQUIP_SMG

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetForceReplaceWeaponReward(oWarrior, oLifeCycle, EQUIP_SMG)


class CPerform(CCustomPerform):
    m_SID = 16077
    m_Name = '拾荒冲锋'
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

