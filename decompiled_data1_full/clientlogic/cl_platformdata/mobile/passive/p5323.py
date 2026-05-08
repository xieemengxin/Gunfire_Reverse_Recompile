# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5323.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5323.pyc
# Source Generated with Decompyle++
# File: p5323.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ARMOR_RADIO_SUB, HP_RADIO_SUB, OBJ_SELF
from cl_newformula import Func361

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 4055,
'sArgs': 'Threshold1' })), ARMOR_RADIO_SUB, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 4055,
'sArgs': 'Threshold2' })), ARMOR_RADIO_SUB, 2)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, (lambda *a: Func361(*a, **{
'sid': 4055,
'sArgs': 'Threshold3' })), HP_RADIO_SUB, 3)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (0, 0, 0),
        2: (100, 0, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (100, 0, 0),
        2: (0, 0, 0),
        3: (0, 0, 0) })
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 7074, 0, { }, 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (50, 0, 0),
        2: (50, -50, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (100, 0, 0),
        3: (0, 0, 0) })
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


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (100, 0, 0),
        2: (0, 0, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (100, -100, 0),
        3: (10000, -10000, 0) })


class CPerform(CCustomPerform):
    m_SID = 5323
    m_Name = '低轮回鱼龙切阶段'
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

