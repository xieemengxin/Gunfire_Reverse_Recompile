# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51606.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51606.pyc
# Source Generated with Decompyle++
# File: p51606.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_FILLBULLET

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1015, 0, {
        'MaxCount': 3 }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 1015, 3, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1015, 0, {
        'MaxCount': 6 }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 1015, 6, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1015, 0, {
        'MaxCount': 17 }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 1015, 9, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1015, 0, {
        'MaxCount': 28 }, 1)
    cl_action.CommonAddStateCount(oWarrior, oLifeCycle, 1015, 12, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1015, 1, 500)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1015, 2, 500)


class CPerform(CCustomPerform):
    m_SID = 51606
    m_Name = '#NT#幸运一击'
    m_MaxLevel = 4
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

