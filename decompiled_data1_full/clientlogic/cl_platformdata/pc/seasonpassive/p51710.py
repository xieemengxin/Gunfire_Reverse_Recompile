# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51710.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51710.pyc
# Source Generated with Decompyle++
# File: p51710.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S8THIRDACTIVE_STATE_ALLEND, S8THIRDACTIVE_STATE_START
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_START, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_START, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_START, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, S8THIRDACTIVE_STATE_ALLEND, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckHasState(oWarrior, oEventCB, 39771):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39771, 0, { }, 0)
    if not cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Effect'):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39771, (lambda *a: Func859(*a, **{
'sAttr': 'BulletNum' })), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Effect', 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 39771) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Effect'):
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39771, (lambda *a: -Func859(*a, **{
'sAttr': 'BulletNum' })), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Effect', 0)


class CPerform(CCustomPerform):
    m_SID = 51710
    m_Name = '持续爆射'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'BulletNum': 2 },
        2: {
            'BulletNum': 4 },
        3: {
            'BulletNum': 8 } }

