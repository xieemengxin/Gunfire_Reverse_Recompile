# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/monsteraf/p6110.pyc
# RelativePath: clientlogic/cl_perform/monsteraf/p6110.pyc
# Source Generated with Decompyle++
# File: p6110.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsteraf import CPerform as CCustomPerform
from cl_commondefines import DEFEND_TREND_ARMOR, MAF_TYPE_FIRE
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', 0, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 1.5), 0)
    else:
        cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', 0, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 1.5), 0)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'HPMax', 100)


class CPerform(CCustomPerform):
    m_SID = 6110
    m_Name = '披甲的'
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
    m_MonsterAfType = MAF_TYPE_FIRE

