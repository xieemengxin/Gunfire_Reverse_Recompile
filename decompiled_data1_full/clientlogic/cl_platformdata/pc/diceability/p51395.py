# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51395.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51395.pyc
# Source Generated with Decompyle++
# File: p51395.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import CREATE_PLANT, DICETAG_PERFORM, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM, PET_ENTER_BATTLE
from cl_newformula import Func308, Func651

def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 1, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 1, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 1, 0, 0)


def DisableAction4(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 1, 0, 0)


def DisableAction5(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetAllSummonAsTarget(oWarrior, oEventCB)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
        cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 7020, (lambda *a: Func308(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 7020, (lambda *a: Func308(*a)))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBSetTargetByID(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'TargetPet' })))
    cl_evact.EventCBTargetAddPerform(oWarrior, oEventCB, 7020, (lambda *a: Func308(*a)))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetAllSummonAsTarget(oWarrior, oEventCB)
    if cl_evcon.GetThisTargetNum(oWarrior, oEventCB):
        cl_evact.EventCBTargetRemovePerform(oWarrior, oEventCB, 7020)


class CPerform(CCustomPerform):
    m_SID = 51395
    m_Name = '灵力附着'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = {
        2: DisableAction2,
        3: DisableAction3,
        4: DisableAction4,
        5: DisableAction5 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_PERFORM,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

