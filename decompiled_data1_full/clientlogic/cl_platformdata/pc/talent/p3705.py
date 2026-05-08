# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p3705.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p3705.pyc
# Source Generated with Decompyle++
# File: p3705.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_newformula import Func369, Func537, Func589, Func717
from cl_commondefines import OBJ_SELF

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 3)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CumulativeDamRatio', 3500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReEnergyThreshold', 4000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 2, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 6)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CumulativeDamRatio', 2500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReEnergyThreshold', 3000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 2, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangeMaxBullet(oWarrior, oLifeCycle, 4508, 0, 9)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CumulativeDamRatio', 1500)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ReEnergyThreshold', 2000)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REVTOTALDAM, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADD_ENERGY, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurDamRatio', (lambda *a: Func369(*a) * 10000 // Func589(*a)))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurDamRatio') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CumulativeDamRatio'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AdditionCount', (lambda *a: Func717(*a, **{
'sArg': 'CurDamRatio' }) // max(Func717(*a, **{
'sArg': 'CumulativeDamRatio' }), 1)))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurDamRatio', (lambda *a: -Func717(*a, **{
'sArg': 'AdditionCount' }) * Func717(*a, **{
'sArg': 'CumulativeDamRatio' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AdditionCount'))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurReEnergy', (lambda *a: Func537(*a)))
    if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CurReEnergy') >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ReEnergyThreshold'):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'CurReEnergy' }) // max(Func717(*a, **{
'sArg': 'ReEnergyThreshold' }), 1)))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'CurReEnergy', (lambda *a: -Func717(*a, **{
'sArg': 'AddCount' }) * Func717(*a, **{
'sArg': 'ReEnergyThreshold' })))
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBTargetAddThrowBagBullet(oWarrior, oEventCB, cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddCount'))


class CPerform(CCustomPerform):
    m_SID = 3705
    m_Name = '精元返生'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 2
    m_IsRareTalent = 0
    m_Career = 118

