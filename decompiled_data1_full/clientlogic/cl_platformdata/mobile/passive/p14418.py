# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p14418.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p14418.pyc
# Source Generated with Decompyle++
# File: p14418.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ARMOR_RADIO_SUB, HP_RADIO_SUB, OBJ_SELF
from cl_newformula import Func361, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 39143)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 4055,
'sArgs': 'Threshold1' })), ARMOR_RADIO_SUB, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 4055,
'sArgs': 'Threshold2' })), ARMOR_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 4055,
'sArgs': 'Threshold3' })), HP_RADIO_SUB, 3)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 4, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 39143)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (0, 0, 0),
        2: (100, 0, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (100, 0, 0),
        2: (0, 0, 0),
        3: (0, 0, 0) })
    cl_evact.EventCBSaveMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu')
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (0, 0, 0),
        3: (100, 0, 0) })
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7074, 0, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (50, 0, 0),
        2: (50, -50, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (140, -70, 0),
        3: (30, -30, 0) })
    cl_evact.EventCBSaveMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu')
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (0, 0, 0),
        3: (100, 0, 0) })
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 7074, None, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (100, 0, 0),
        2: (0, 0, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (30, -30, 0),
        2: (70, -70, 0),
        3: (10000, -10000, 0) })
    cl_evact.EventCBSaveMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu')
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (0, 0, 0),
        3: (100, 0, 0) })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (100, 0, 0),
        2: (0, 0, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (100, -100, 0),
        3: (10000, -10000, 0) })
    cl_evact.EventCBSaveMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu')
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (0, 0, 0),
        3: (100, 0, 0) })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        39132: 1 }, 1, 0):
        cl_evact.EventCBRecoverMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu')


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 39132, 1, 0) and cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'SkillVID'):
        cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'SkillVID' })))
        cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 39143, { }, None)


class CPerform(CCustomPerform):
    m_SID = 14418
    m_Name = '轮回10-鱼龙'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0

