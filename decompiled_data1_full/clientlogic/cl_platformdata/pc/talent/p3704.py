# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3704.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3704.pyc
# Source Generated with Decompyle++
# File: p3704.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_VICTIM
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'BulletVerticalAcc', 2000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'AddStateTime', 2000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'BulletVerticalAcc', 2000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'AddStateTime', 2000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'KeepTime', 2000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceAtt', 3000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'BulletVerticalAcc', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'AddStateTime', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'BulletVerticalAcc', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'AddStateTime', 4000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'KeepTime', 4000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceAtt', 4500)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'BulletVerticalAcc', 6000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1434, 'AddStateTime', 6000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'BulletVerticalAcc', 6000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'AddStateTime', 6000, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1439, 'KeepTime', 6000, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReduceAtt', 6000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATE_START, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckInPointState(oWarrior, oEventCB, {
        8155: 1,
        8156: 1 }):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if not cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33829, 0, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33829, 0, {
                'ReduceAtt': (lambda *a: Func717(*a, **{
'sArg': 'ReduceAtt' })) }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckInPointState(oWarrior, oEventCB, {
        8155: 1,
        8156: 1 }):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33829, 0, 0, 0) and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8155, 0, 0, 0) == 0 and cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 8156, 0, 0, 0) == 0:
            cl_evact.PassiveCBRemoveTargetState(oWarrior, oEventCB, 33829, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 3704
    m_Name = '天印延衍'
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
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 118

