# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p5431.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p5431.pyc
# Source Generated with Decompyle++
# File: p5431.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 4000, DAM_TYPE_CORRISION, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 8000, DAM_TYPE_CORRISION, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, 12000, DAM_TYPE_CORRISION, 1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'CorrisionAbnormalFactor', 0, 60, 0)


class CPerform(CCustomPerform):
    m_SID = 5431
    m_Name = '深度腐蚀'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 119

