# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25861.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25861.pyc
# Source Generated with Decompyle++
# File: p25861.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_USE_ARMOR, OBJ_VICTIM, QUALITY_TYPE_NORMAL, WARRIOR_HERO

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKARMOR, -1, 0, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BREAKSHIELD, -1, 0, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUREED, -1, 2, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckDamFromSelf(oWarrior, oEventCB, 0) and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_HERO):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1011, 50, {
            'MoveSpeedMul': -5000 }, 1, 1, 0)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33337, 500, { }, 1, 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1801: 1,
        1604: 1 }, 0, 0):
        cl_evact.EventCBChangeCureLimit(oWarrior, oEventCB, DAM_USE_ARMOR, 0)


class CPerform(CCustomPerform):
    m_SID = 25861
    m_Name = '慑敌之威'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5861
    m_Quality = QUALITY_TYPE_NORMAL
    m_ExcludeRelic = ()

