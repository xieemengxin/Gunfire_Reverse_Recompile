# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25705.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25705.pyc
# Source Generated with Decompyle++
# File: p25705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_USE_HP, OBJ_SELF, QUALITY_TYPE_NORMAL
from cl_newformula import Func378

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func378(*a))) <= 0:
        cl_action.CommonRemovePerform(oWarrior, oEventCB.GetCBLifeCycle(), 25705)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeDefValue(oWarrior, oEventCB, 100, DAM_USE_HP, None)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1656, 100, { }, 0, -1, None)


class CPerform(CCustomPerform):
    m_SID = 25705
    m_Name = '救命稻草'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_RelicType = 0
    m_HeroRelic = 5705
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

