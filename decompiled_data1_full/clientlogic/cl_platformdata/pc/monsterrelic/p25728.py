# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25728.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25728.pyc
# Source Generated with Decompyle++
# File: p25728.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETDROP, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 1, 0, 0)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, -1, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBRemoveBulletDropMiniGameBySID(oWarrior, oEventCB, {
        4502: 0,
        4503: 0,
        4504: 0 })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByMsgInfoSummon(oWarrior, oEventCB)
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 25728, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBGetTargetByEventMonster(oWarrior, oEventCB)
    if cl_evcon.CheckTargetIsSelfSummon(oWarrior, oEventCB, WARRIOR_MONSTER):
        cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 25728, 1)


class CPerform(CCustomPerform):
    m_SID = 25728
    m_Name = '弹药腰带'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5728
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

