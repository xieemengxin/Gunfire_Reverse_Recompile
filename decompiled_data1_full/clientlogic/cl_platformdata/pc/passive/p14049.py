# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14049.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14049.pyc
# Source Generated with Decompyle++
# File: p14049.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetMonsterAIPFGroupCnt(oWarrior, oLifeCycle, 1001, 21641, 1, 1)
    cl_action.CommonSetMonsterDodgeCD(oWarrior, oLifeCycle, 50)


class CPerform(CCustomPerform):
    m_SID = 14049
    m_Name = '轮回9-幽冥猎手连续攻击次数下限降低且闪避频率增加'
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

