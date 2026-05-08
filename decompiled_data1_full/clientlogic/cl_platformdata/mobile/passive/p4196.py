# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4196.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4196.pyc
# Source Generated with Decompyle++
# File: p4196.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_BARRIER
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVESUMMON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByMsgInfoSummonID(oWarrior, oEventCB)
    if cl_evcon.GetSummonAttr(oWarrior, oEventCB, 'HP') <= 0 and cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BARRIER):
        cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), 1, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckTalentLevel(oWarrior, oEventCB, 2502) < 3:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32383, 0, {
            'KeepTime': 1000 }, 0, 0, None)
    else:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32383, 0, {
            'KeepTime': 500 }, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonChangeEnergy(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' })), None)


class CPerform(CCustomPerform):
    m_SID = 4196
    m_Name = '卫士被动(旧)'
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

