# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p16073.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p16073.pyc
# Source Generated with Decompyle++
# File: p16073.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import EQUIP_ROCKET_LAUNCHER

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetForceReplaceWeaponReward(oWarrior, oLifeCycle, EQUIP_ROCKET_LAUNCHER)


class CPerform(CCustomPerform):
    m_SID = 16073
    m_Name = '拾荒火炮'
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

