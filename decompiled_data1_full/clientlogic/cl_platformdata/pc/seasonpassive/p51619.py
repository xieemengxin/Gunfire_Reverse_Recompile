# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51619.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51619.pyc
# Source Generated with Decompyle++
# File: p51619.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func14, Func308, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 5)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 5)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 5)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 5)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastFireFrame') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFireFrame', (lambda *a: Func14(*a) + 18))
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 39671, 76, {
            'StatusEffect': (lambda *a: max(300, Func308(*a) * 200)),
            'StateCount': (lambda *a: Func717(*a, **{
'sArg': 'MaxCount' })) }, 1)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFireFrame', (lambda *a: Func14(*a) + 18))


class CPerform(CCustomPerform):
    m_SID = 51619
    m_Name = '生存-过荷射击'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

