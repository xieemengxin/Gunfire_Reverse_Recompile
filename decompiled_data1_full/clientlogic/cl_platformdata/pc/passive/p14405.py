# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p14405.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p14405.pyc
# Source Generated with Decompyle++
# File: p14405.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_VICTIM, SKILLCACHE_BALLISTICTYPE

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7142, 0, { }, -1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 7143, 0, { }, -1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CREATESUMMON, -1, 3, 0, 0)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39132, 'Range', 14, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39134, 'Speed', 17, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39135, 'Speed', 17, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39137, 'IgnoreDamage', 1, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 39132, 'Effect', 1034, None)
    cl_action.CommonSetMonsterAgentConfig(oWarrior, oLifeCycle, 'GuerrillaInterval', 400)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 1):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, -5000, 0, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39138, 1, 0):
        cl_evact.EventSetSkillCacheData(oWarrior, oEventCB, SKILLCACHE_BALLISTICTYPE, 3)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39137, 1, 0) and cl_evcon.EventCBGetCurCrtData(oWarrior, oEventCB, 'SummonSID'):
        cl_evact.EventCBTriggerDropBullet(oWarrior, oEventCB, {
            4502: 90,
            4503: 25,
            4504: 8,
            4508: 1 }, {
            4502: 15,
            4503: 15,
            4504: 15,
            4508: 10 }, 1, 1, { })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39137, 1, 0):
        cl_evact.EventGetTargetByMsgInfoSummon(oWarrior, oEventCB)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1009, 0, { }, 0, 0, None)


class CPerform(CCustomPerform):
    m_SID = 14405
    m_Name = '轮回9-鱼龙后裔'
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
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

