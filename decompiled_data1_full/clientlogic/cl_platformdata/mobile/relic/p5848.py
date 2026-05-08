# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5848.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5848.pyc
# Source Generated with Decompyle++
# File: p5848.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1530, 0, { }, 1)
    if cl_condition.HasState(oWarrior, oLifeCycle, 33500):
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 1530, (lambda *a: Func410(*a, **{
'sid': 33500 })), None)
    else:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33500, 0, { }, 0)
        cl_action.CommonSetStateCount(oWarrior, oLifeCycle, 33500, (lambda *a: Func410(*a, **{
'sid': 1530 })), None)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1555, 0, { }, 1)


class CPerform(CCustomPerform):
    m_SID = 5848
    m_Name = '琉璃瞄具'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5524
    m_ValidRemove = 0
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

