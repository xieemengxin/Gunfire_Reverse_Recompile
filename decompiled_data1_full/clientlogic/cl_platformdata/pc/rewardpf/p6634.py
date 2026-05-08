# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6634.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6634.pyc
# Source Generated with Decompyle++
# File: p6634.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSeasonShopNpcRefreshTimes(oWarrior, oLifeCycle, 1, 'ModulePacketRefreshTimes')
    cl_action.CommonAddSeasonShopNpcRefreshTimes(oWarrior, oLifeCycle, 1, 'CrystalPacketRefreshTimes')


class CPerform(CCustomPerform):
    m_SID = 6634
    m_Name = '赛季7天赋30级'
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

