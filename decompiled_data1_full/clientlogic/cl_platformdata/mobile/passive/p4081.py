# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4081.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4081.pyc
# Source Generated with Decompyle++
# File: p4081.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ARMOR_RADIO_SUB, FIGHT3_KEY_IGNOREIMMOBILIZE, FIGHT3_KEY_IGNOREKNOCKBACK, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREUNBALANCE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREKNOCKBACK)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNORETHUMP)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREUNBALANCE)
    cl_action.CommonAddLogicKey(oWarrior, oLifeCycle, FIGHT3_KEY_IGNOREIMMOBILIZE)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 60, ARMOR_RADIO_SUB, 1)
    cl_action.CommonListenHPThreshold(oWarrior, oLifeCycle, 20, ARMOR_RADIO_SUB, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (0, 0, 0),
        2: (100, 0, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (100, 0, 0),
        2: (0, 0, 0),
        3: (0, 0, 0) })


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (30, 0, 0),
        2: (60, -30, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (0, 0, 0),
        2: (100, -20, 0),
        3: (20, 0, 0) })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'qianxing', {
        1: (80, 0, 0),
        2: (20, -20, 0) })
    cl_evact.EventCBSetMonsterStatePolicy(oWarrior, oEventCB, 'zuanchu', {
        1: (20, 0, 0),
        2: (20, 0, 0),
        3: (60, -20, 0) })


class CPerform(CCustomPerform):
    m_SID = 4081
    m_Name = '二幕Boss血量切权重'
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

