# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/devicecomp/p50122.pyc
# RelativePath: clientlogic/cl_platformdata/pc/devicecomp/p50122.pyc
# Source Generated with Decompyle++
# File: p50122.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.devicecomp.customaction import CustomAction50122 as CustomAction
from cl_perform.devicecomp import CDeviceComp as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, DEVICECOMP_TYPE_DEVICE, OBJ_ATTACK, OBJ_VICTIM, PF_SUBMSG_DEVICEACTIVE, WARRIOR_MONSTER
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50122, 'TimeCostEnergy', 400, 1)
    cl_action.CommonSetDevicePerformIgnoreCostEnergy(oWarrior, oLifeCycle, 7200)
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oLifeCycle, 100, 100, 0)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 2)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_DEVICE_ENERGY, -1, 3, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50122, 'TimeCount', 0, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50122, 'EnergyAddAtt', 0, None)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50122, 'StopRecover', 0, None)
    cl_action.CommonStopDeviceEnergyRecover(oWarrior, oLifeCycle, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TimeCount') < 5:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'TimeCount', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('TimeCount') >= 5:
        cl_evact.EventChangeDeviceEnergy(oWarrior, oEventCB, (lambda *a: min(0, Func304(*a, **{
'sAttr': 'RDeviceEnergy' }) - cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TimeCostEnergy'))), 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TimeCostEnergy', min(2000, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'TimeCostEnergy') + 400))
        if cl_condition.GetDeviceEnergyRatio(oWarrior, oEventCB.GetCBLifeCycle()) <= 10 and not cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StopRecover'):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StopRecover', 1)
            cl_action.CommonStopDeviceEnergyRecover(oWarrior, oEventCB.GetCBLifeCycle(), 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TimeCount', 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'TimeCostEnergy', 400)
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: (Func304(*a, **{
'sAttr': 'DeviceEnergy' }) // 100) * (50 + 30 * cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnergyAddAtt'))), 0, 0, '')
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'StopRecover'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'StopRecover', 0)
        cl_action.CommonStopDeviceEnergyRecover(oWarrior, oEventCB.GetCBLifeCycle(), 0, 1)


def DoCallBackAction3(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'EnergyToGroup': {
            4000: 5,
            8000: 6,
            14000: 7,
            20000: 8 },
        'Action': 'CalGroup' })
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ChangeGroup'):
        cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 0, 0, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyAddAtt', 0)
        cl_action.CommonDoneDeviceEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL)
        cl_action.CommonDoneDeviceEvent(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnergyGroup'):
            cl_action.CommonDirectEventCBFunc(oWarrior, oEventCB.GetCBLifeCycle(), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'EnergyGroup'), 1, 0)


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 5000, 0, 0)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 5000, 0, 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyAddAtt', 1)


def DoCallBackAction7(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 5000, 0, 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyAddAtt', 1)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 9)


def DoCallBackAction8(oEventCB, oWarrior):
    cl_action.CommonChangeDeviceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'AttSpeed', 5000, 0, 0)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnergyAddAtt', 1)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 9)
    cl_action.CommonListenDeviceMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_DEVICEACTIVE, 10)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 7200, 0, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 5, WARRIOR_MONSTER, 0, 0, 1, 0, 0, 0, None)
        cl_evact.EventCBUpdateCustomPosInfo(oWarrior, oEventCB, {
            'ExtraAttack': 1 })
        CustomAction(oWarrior, oEventCB, {
            'Action': 'ExtraAttack',
            'RS': 'ExtraAttack50122',
            'BaseFactor': 100 })


def DoCallBackAction10(oEventCB, oWarrior):
    cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'ElementType', cl_condition.RandomChooseKey(oWarrior, oEventCB.GetCBLifeCycle(), {
        DAM_TYPE_THUNDER: 3334,
        DAM_TYPE_CORRISION: 3333,
        DAM_TYPE_FIRE: 3333 }))
    cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'DebuffProb', 5000)


class CPerform(CCustomPerform):
    m_SID = 50122
    m_Name = '震霆'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        7: DoCallBackAction7,
        8: DoCallBackAction8,
        9: DoCallBackAction9,
        10: DoCallBackAction10 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ExclusiveDevice = (1002,)
    m_ExclusiveHero = ()
    m_ExcludeComp = (50120, 50121)
    m_DropShape = 5560
    m_DeployActive = 1
    m_Type = DEVICECOMP_TYPE_DEVICE
    m_FirstChooseExtWeight = 0

