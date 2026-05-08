# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13733.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13733.pyc
# Source Generated with Decompyle++
# File: p13733.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_newformula import Func201, Func598, Func717
from cl_commondefines import ATTACKERSUBMSG_NORMAL, OBJ_VICTIM, WARRIOR_BOSS

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, 'PF13733RewardCrystal'):
        cl_action.CommonSetSavedData(oWarrior, oLifeCycle, 'PF13733RewardCrystal', 1)
        cl_action.CommonRewardS7Crystal(oWarrior, oLifeCycle, 1, {
            1163: 1,
            1164: 1 }, 1)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func598(*a, **{
'sKey': 'PF13733HadAddTime' }))) < oLifeCycle.m_Owner.GetArgValue('MaxAddPointTime'):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'PF13733HadAddTime', (lambda *a: min(int(Func201(*a) - 1), int(Func717(*a, **{
'sArg': 'MaxAddPointTime' })))), 1)
    cl_evact.EventCBAddS7CrystalPoint(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'PF13733HadAddTime' }) * Func717(*a, **{
'sArg': 'AddPointPerTime' })), 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func598(*a, **{
'sKey': 'PF13733HadAddTime' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxAddPointTime'):
        cl_evact.EventCBDoneEvent(oWarrior, oEventCB, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL)
    else:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS) and cl_evcon.CheackTargetFightTypeIsRealit(oWarrior, oEventCB):
            cl_evact.EventCBAddSavedData(oWarrior, oEventCB, 'PF13733HadAddTime', 3, 0)
            cl_evact.EventCBAddS7CrystalPoint(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'AddPointPerTime' })), 1)


class CPerform(CCustomPerform):
    m_SID = 13733
    m_Name = '#NT#S7-水晶'
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
    m_BaseArgData = {
        'MaxAddPointTime': 4,
        'AddPointPerTime': 1 }
    m_DieDisable = 0
    m_Career = None

