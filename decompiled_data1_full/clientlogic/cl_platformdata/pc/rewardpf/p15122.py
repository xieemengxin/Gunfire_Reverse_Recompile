# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15122.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15122.pyc
# Source Generated with Decompyle++
# File: p15122.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, 'SuitExtraInscription', 1, None)
    cl_action.CommonSetOwnerWeaponExtraEtchingCost(oWarrior, oLifeCycle, {
        0: 0,
        1: 800,
        2: 900,
        3: 1000,
        4: 1250,
        5: 1500,
        6: 1500 })


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, 'SuitExtraInscription', 0, None)


class CPerform(CCustomPerform):
    m_SID = 15122
    m_Name = '#NT#精雕细琢'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

