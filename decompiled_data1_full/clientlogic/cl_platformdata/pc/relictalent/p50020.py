# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relictalent/p50020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relictalent/p50020.pyc
# Source Generated with Decompyle++
# File: p50020.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_newformula import Func602

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CLIENTACTIVEUSECOUNTCHANGE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33015, 0, {
        'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount6'),
        'StatusEffect': 24 }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33015, 0, {
        'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount6'),
        'StatusEffect': 20 }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33015, 0, {
        'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StateCount6'),
        'StatusEffect': 16 }, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 12019, 0, 0) and cl_condition.RandomTrigger(oWarrior, oEventCB.GetCBLifeCycle(), 100, 5):
        cl_action.CommonAddThrowBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func602(*a) * 0.1), 0)


class CPerform(CCustomPerform):
    m_SID = 50020
    m_Name = '种豆得瓜'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_GrowPF = []
    m_DamagePF = []

