# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6604.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6604.pyc
# Source Generated with Decompyle++
# File: p6604.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import SEASONFUNC_REFRESH_PETSHOP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPetShopRefreshTimes(oWarrior, oLifeCycle, 1)
    cl_action.CommonAddSeasonFunc(oWarrior, oLifeCycle, SEASONFUNC_REFRESH_PETSHOP)


class CPerform(CCustomPerform):
    m_SID = 6604
    m_Name = '赛季天赋1005'
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

