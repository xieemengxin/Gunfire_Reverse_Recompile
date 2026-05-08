# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51734.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51734.pyc
# Source Generated with Decompyle++
# File: p51734.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import PF_SUBMSG_S8THIRDACTIVE
from cl_newformula import Func852

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, '51734AddSpeed', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, '51734AddSpeed', 4000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, '51734AddSpeed', 8000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_S8THIRDACTIVE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39766, 1000, {
        'MoveSpeedMul': (lambda *a: Func852(*a, **{
'sKey': '51734AddSpeed' })) }, 0)


class CPerform(CCustomPerform):
    m_SID = 51734
    m_Name = '移动速度'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'AddCount': 1 },
        2: {
            'AddCount': 2 },
        3: {
            'AddCount': 3 } }

