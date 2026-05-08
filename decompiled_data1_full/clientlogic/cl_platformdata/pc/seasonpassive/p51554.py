# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51554.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51554.pyc
# Source Generated with Decompyle++
# File: p51554.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_newformula import Func14

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountAddition', 300)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountAddition', 400)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountAddition', 600)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONFIRE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxCount', 4)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CountAddition', 1200)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'LastFireFrame') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFireFrame', (lambda *a: Func14(*a) + 18))
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33678, 76, {
            'StatusEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CountAddition'),
            'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxCount') }, 1)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'LastFireFrame', (lambda *a: Func14(*a) + 18))


class CPerform(CCustomPerform):
    m_SID = 51554
    m_Name = '#NT#射速升级'
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

