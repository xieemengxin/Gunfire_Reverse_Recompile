# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4357.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4357.pyc
# Source Generated with Decompyle++
# File: p4357.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import GAMETYPE_JUMP

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_LEAVESCENE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101006):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0, {
            'Att': 1 }, 1)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101009):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0, {
            'Att': 2 }, 1)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301003):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0, {
            'Att': 3 }, 1)
    if cl_evcon.CheckLevelGameType(oWarrior, oEventCB, GAMETYPE_JUMP):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0, {
            'Att': 4 }, 1)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1101007) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403003) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403004) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 7101007):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0, {
            'Att': 5 }, 1)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301002):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0, {
            'Att': 6 }, 1)
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403001) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403002):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0, {
            'Att': 7 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32870, 0)


class CPerform(CCustomPerform):
    m_SID = 4357
    m_Name = '御灵师仆从专属行为'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

