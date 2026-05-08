# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51627.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51627.pyc
# Source Generated with Decompyle++
# File: p51627.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import EQUIP_TYPE_FUNDAMENTALWEAPON, EQUIP_TYPE_MAINWEAPON, S7_MODULE_POINT_CHANGE
from cl_newformula import Func717, Func746, Func839

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 6000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 12000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'CrazyRatio', 18000)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraCrazyRatio', 1000)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39692, 0, {
        'ExtraCrazyRatio': (lambda *a: Func717(*a, **{
'sArg': 'ExtraCrazyRatio' })) }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, S7_MODULE_POINT_CHANGE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func717(*a, **{
'sArg': 'CrazyRatio' })), 0, EQUIP_TYPE_MAINWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func717(*a, **{
'sArg': 'CrazyRatio' })), 0, EQUIP_TYPE_FUNDAMENTALWEAPON)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 39692, (lambda *a: Func839(*a) // 5), 1)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func717(*a, **{
'sArg': 'CrazyRatio' }) + Func746(*a, **{
'iStateSID': 39692 }) * Func717(*a, **{
'sArg': 'ExtraCrazyRatio' })), 0, EQUIP_TYPE_MAINWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func717(*a, **{
'sArg': 'CrazyRatio' }) + Func746(*a, **{
'iStateSID': 39692 }) * Func717(*a, **{
'sArg': 'ExtraCrazyRatio' })), 0, EQUIP_TYPE_FUNDAMENTALWEAPON)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func717(*a, **{
'sArg': 'CrazyRatio' }) + Func746(*a, **{
'iStateSID': 39692 }) * Func717(*a, **{
'sArg': 'ExtraCrazyRatio' })), 0, EQUIP_TYPE_MAINWEAPON)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func717(*a, **{
'sArg': 'CrazyRatio' }) + Func746(*a, **{
'iStateSID': 39692 }) * Func717(*a, **{
'sArg': 'ExtraCrazyRatio' })), 0, EQUIP_TYPE_FUNDAMENTALWEAPON)


class CPerform(CCustomPerform):
    m_SID = 51627
    m_Name = '暴击倍率'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

