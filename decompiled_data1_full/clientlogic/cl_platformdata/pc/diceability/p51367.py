# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51367.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51367.pyc
# Source Generated with Decompyle++
# File: p51367.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_PERFORM, DICE_PUTOUT_POLL_ONE, INKVALUE_SUB, OBJECT_OWNER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 10)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 12)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 24)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 15)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 30)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 20)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 40)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COST_ENERGY, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_INKVALUE, INKVALUE_SUB, 1, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MinRatio', 35)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatio', 60)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'MaxRatioCost', 9000)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, min(int(max(((cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TrueEnergyChange') - 1000) / (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatioCost') - 1000)) * 100, 0)), 100) * (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatio') - cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')) / 100 + cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')):
        cl_evact.EventGetTargetByOwnObj(oWarrior, oEventCB, OBJECT_OWNER)
        cl_evact.EventChangeEnergy(oWarrior, oEventCB, cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'TrueEnergyChange'))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') < 0 and cl_evcon.CheckRandom(oWarrior, oEventCB, 100, min(int(max(((-cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange') * 100 - 1000) / (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatioCost') - 1000)) * 100, 0)), 100) * (cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MaxRatio') - cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')) / 100 + cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'MinRatio')):
        cl_action.CommonModifyInkValue(oWarrior, oEventCB.GetCBLifeCycle(), -cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'RealChange'), '', {
            'Fixed': 1 })


class CPerform(CCustomPerform):
    m_SID = 51367
    m_Name = '内力流转'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_ONE

