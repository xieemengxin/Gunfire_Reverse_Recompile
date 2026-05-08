# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25841.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25841.pyc
# Source Generated with Decompyle++
# File: p25841.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_NORMAL

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetHeroTarget(oWarrior, oEventCB, 1, 1, 0, 1)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33389, 0, { }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 25841
    m_Name = '来者不拒'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5841
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

