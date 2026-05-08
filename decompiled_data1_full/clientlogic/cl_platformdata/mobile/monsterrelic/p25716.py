# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterrelic/p25716.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterrelic/p25716.pyc
# Source Generated with Decompyle++
# File: p25716.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import OBJ_SELF, QUALITY_TYPE_NORMAL, TYPE_RELIFE_PASSIVE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetRelifeAttr(oWarrior, oLifeCycle, TYPE_RELIFE_PASSIVE, 230, 1, 1, {
        'Elite': 10,
        'Normal': 50 }, None, None)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'HPMax', -4000, 0, -1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ShieldMax', -4000, 0, 1)
    cl_action.CommonChangeAttr(oWarrior, oLifeCycle, 'ArmorMax', -4000, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COSTRELIFES, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1256, 230, { }, 1, 0, None)


class CPerform(CCustomPerform):
    m_SID = 25716
    m_Name = '三重轮回'
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
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5716
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

