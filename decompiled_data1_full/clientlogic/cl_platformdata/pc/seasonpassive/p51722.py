# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51722.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51722.pyc
# Source Generated with Decompyle++
# File: p51722.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S8THIRDACTIVE_ENERGY_CHANGE_ADD
from cl_newformula import Func537, Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, S8THIRDACTIVE_ENERGY_CHANGE_ADD, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AddEnergy', (lambda *a: Func537(*a)))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'EnergyRecovery' }))) and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'AddEnergy') >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func859(*a, **{
'sAttr': 'EnergyRecovery' }))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCount', (lambda *a: Func717(*a, **{
'sArg': 'AddEnergy' }) // Func859(*a, **{
'sAttr': 'EnergyRecovery' })))
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'AddEnergy', (lambda *a: -Func717(*a, **{
'sArg': 'AddCount' }) * Func859(*a, **{
'sAttr': 'EnergyRecovery' })))
        cl_evact.EventCBAddWeaponPFBulletByHoldType(oWarrior, oEventCB, 0, (lambda *a: Func717(*a, **{
'sArg': 'AddCount' }) * Func859(*a, **{
'sAttr': 'AddCountMul' }) * 1000), 0)


class CPerform(CCustomPerform):
    m_SID = 51722
    m_Name = '武器资源回复效率'
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
    m_BaseLevelArgData = {
        1: {
            'EnergyRecovery': 3,
            'AddCountMul': 1 },
        2: {
            'EnergyRecovery': 1,
            'AddCountMul': 1 },
        3: {
            'EnergyRecovery': 1,
            'AddCountMul': 3 } }

