# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51396.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51396.pyc
# Source Generated with Decompyle++
# File: p51396.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import CREATE_PLANT, DICETAG_OTHER, DICE_PUTOUT_POLL_TWO, OBJ_VICTIM, PET_ENTER_BATTLE

def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 6, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 9, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPRatio', 5000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHPAddRatio', 500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ModelScaleRatio', 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 10, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 3, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPRatio', 8000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHPAddRatio', 600)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ModelScaleRatio', 6)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 10, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 3, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPRatio', 12000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraHPAddRatio', 800)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ModelScaleRatio', 8)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_SET_HEROSIDEPET, PET_ENTER_BATTLE, 1, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 10, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, CREATE_PLANT, 3, 0, 0)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 4, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBGetEventPet(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
        'TalentLevel': 0,
        'HPMax': 3000 }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBGetEventPet(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
        'TalentLevel': 1,
        'StatusEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraHPAddRatio'),
        'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ModelScaleRatio'),
        'HPMax': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHPRatio') }, 1, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    if cl_evcon.EventCBCheckLoading(oWarrior, oEventCB) == 0:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
            'TalentLevel': 1,
            'StatusEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraHPAddRatio'),
            'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ModelScaleRatio'),
            'HPMax': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHPRatio') }, 1, 0, 0)
    else:
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33907, 0, {
            'TalentLevel': 1,
            'StatusEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraHPAddRatio'),
            'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ModelScaleRatio'),
            'HPMax': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHPRatio') }, 1, 1, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
        'TalentLevel': 1,
        'StatusEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraHPAddRatio'),
        'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ModelScaleRatio'),
        'HPMax': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHPRatio') }, 1, 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventGetTargetByPlants(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
        'TalentLevel': 1,
        'StatusEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraHPAddRatio'),
        'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ModelScaleRatio'),
        'HPMax': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHPRatio') }, 1, 0, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByServant(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
        'TalentLevel': 0,
        'HPMax': 3000 }, 1, 0, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
        'TalentLevel': 0,
        'HPMax': 3000 }, 1, 0, 0)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_evact.EventGetTargetByPlants(oWarrior, oEventCB)
    cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
        'TalentLevel': 0,
        'HPMax': 3000 }, 1, 0, 0)


def DoCallBackAction9(oEventCB, oWarrior):
    cl_evact.EventGetAllSummonAsTarget(oWarrior, oEventCB)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 11)


def DoCallBackAction10(oEventCB, oWarrior):
    cl_evact.EventGetAllSummonAsTarget(oWarrior, oEventCB)
    cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 12)


def DoCallBackAction11(oEventCB, oWarrior):
    if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33906, 0, 0, 0, 0) or cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33907, 0, 0, 0, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
            'TalentLevel': 0,
            'HPMax': 3000 }, 1, 0, 0)


def DoCallBackAction12(oEventCB, oWarrior):
    if not cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33906, 0, 0, 0, 0) or cl_evcon.CheckTargetHasState(oWarrior, oEventCB, 33907, 0, 0, 0, 0):
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33906, 0, {
            'TalentLevel': 1,
            'StatusEffect': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ExtraHPAddRatio'),
            'StateCount': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ModelScaleRatio'),
            'HPMax': cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddHPRatio') }, 1, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 51396
    m_Name = '巨化仆从'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        9: DoCallBackAction9,
        10: DoCallBackAction10,
        11: DoCallBackAction11,
        12: DoCallBackAction12 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_OTHER,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

