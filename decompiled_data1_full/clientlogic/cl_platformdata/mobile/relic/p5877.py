# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5877.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5877.pyc
# Source Generated with Decompyle++
# File: p5877.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import LEVEL_TYPE_HIDE, QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func304, Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 1, 0, -1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, -1, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 3, 0, -1)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsCost', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEnterNewSecne(oWarrior, oEventCB) and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsCost'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsCost', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCash', (lambda *a: max(0, Func304(*a, **{
'sAttr': 'HP' }) // 100 - 1) * 3))
        cl_action.CommonHPModify(oWarrior, oEventCB.GetCBLifeCycle(), 'HP', 100, None)
        cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 5877,
'sArgs': 'AddCash' })))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCash', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsCost', 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckEnterNewSecne(oWarrior, oEventCB) and cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_HIDE) == 0 and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'IsCost'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'IsCost', 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCash', (lambda *a: max(0, Func304(*a, **{
'sAttr': 'HP' }) // 100 - 1) * 6))
        cl_action.CommonHPModify(oWarrior, oEventCB.GetCBLifeCycle(), 'HP', 100, None)
        cl_action.CommonAddWarCash(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func361(*a, **{
'sid': 5877,
'sArgs': 'AddCash' })))
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCash', 0)


class CPerform(CCustomPerform):
    m_SID = 5877
    m_Name = '火中取栗'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 1
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

