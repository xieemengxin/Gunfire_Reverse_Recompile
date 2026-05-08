# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14046.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14046.pyc
# Source Generated with Decompyle++
# File: p14046.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ACCURACY_TYPE_HIGH, MISSING_DIS_HARD
from cl_newformula import Func367

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetMonsterAccuracyFactor(oWarrior, oLifeCycle, ACCURACY_TYPE_HIGH)
    cl_action.CommonSetMonsterMissingDisTypeByRound(oWarrior, oLifeCycle, {
        1: MISSING_DIS_HARD,
        2: MISSING_DIS_HARD,
        3: MISSING_DIS_HARD })
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'AccuracyProb', 0, (lambda *a: 60 - Func367(*a, **{
'sAttr': 'AccuracyProb' })), -1)


class CPerform(CCustomPerform):
    m_SID = 14046
    m_Name = '轮回9-魔化左弩兵'
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

