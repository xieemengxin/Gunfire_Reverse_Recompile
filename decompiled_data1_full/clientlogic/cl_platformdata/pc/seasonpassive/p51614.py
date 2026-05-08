# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51614.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51614.pyc
# Source Generated with Decompyle++
# File: p51614.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 1000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'DamRatio', 2000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'Count', 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1998, 1, 0):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'Count', 1)
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Count') >= 3:
        if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 39670):
            cl_evact.PassiveCBAddState(oWarrior, oEventCB, 39670, 500, {
                'DamRatio': (lambda *a: Func717(*a, **{
'sArg': 'DamRatio' })) }, 1, 1, 0)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', 0)
        cl_action.CommonAddStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39670, 1, 500)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', 0)


class CPerform(CCustomPerform):
    m_SID = 51614
    m_Name = '莲花-次数转技能伤害'
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

