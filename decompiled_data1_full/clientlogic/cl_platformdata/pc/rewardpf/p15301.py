# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15301.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15301.pyc
# Source Generated with Decompyle++
# File: p15301.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1329, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1331, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1335, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1336, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1435, 'Att', 4000, 0)
    cl_action.CommonAddCustomIntData(oWarrior, oLifeCycle, 'PunchAttAdd', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1332, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1334, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1337, 'Att', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1310, 'Att', 4000, 0)


class CPerform(CCustomPerform):
    m_SID = 15301
    m_Name = '破岳罡劲'
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

