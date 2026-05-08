# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandability/p51276.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandability/p51276.pyc
# Source Generated with Decompyle++
# File: p51276.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.wandability import CWandAbility as CCustomPerform
from cl_commondefines import ABILITY_QUALITY_FOUR, ABILITY_TYPE_POSITIVE, WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE, WAND_SUBMSG_EXTACTIONSLOT, WAND_SUBTYPE_COPY
from cl_newformula import Func651, Func717, Func750, Func788, Func789

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonFillWandEmptyActionCompSlot(oWarrior, oLifeCycle, (lambda *a: Func788(*a, **{
'iPos': 1 })), (lambda *a: Func789(*a, **{
'iPos': 1 })), WAND_SUBTYPE_COPY, {
        2047: 1,
        2109: 1,
        2121: 1 }, (lambda *a: Func717(*a, **{
'sArg': 'SlotNum' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_REMOVE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, WANDCOMP_SUBMSG_ADD, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WAND, WAND_SUBMSG_EXTACTIONSLOT, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Wand' }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func750(*a))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompType' }))) == 1 and cl_evcon.CheckKeyInReason(oWarrior, oEventCB, '51276') == 0:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompPos' }))) == 1:
            cl_action.ClearWandEmptyActionCompSlot(oWarrior, oEventCB.GetCBLifeCycle())
        elif cl_evcon.CheckKeyInReason(oWarrior, oEventCB, '-syncrmcomp') == 0 and cl_evcon.CheckKeyInReason(oWarrior, oEventCB, 'refreshactioncomp') == 0:
            cl_action.CommonFillWandEmptyActionCompSlot(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func788(*a, **{
'iPos': 1 })), (lambda *a: Func789(*a, **{
'iPos': 1 })), WAND_SUBTYPE_COPY, {
                2047: 1,
                2109: 1,
                2121: 1 }, (lambda *a: Func717(*a, **{
'sArg': 'SlotNum' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Wand' }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func750(*a))) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'CompType' }))) == 1 and cl_evcon.CheckKeyInReason(oWarrior, oEventCB, '51276') == 0:
        cl_action.CommonFillWandEmptyActionCompSlot(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func788(*a, **{
'iPos': 1 })), (lambda *a: Func789(*a, **{
'iPos': 1 })), WAND_SUBTYPE_COPY, {
            2047: 1,
            2109: 1,
            2121: 1 }, (lambda *a: Func717(*a, **{
'sArg': 'SlotNum' })))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'Wand' }))) == cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func750(*a))):
        cl_action.CommonFillWandEmptyActionCompSlot(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func788(*a, **{
'iPos': 1 })), (lambda *a: Func789(*a, **{
'iPos': 1 })), WAND_SUBTYPE_COPY, {
            2047: 1,
            2109: 1,
            2121: 1 }, (lambda *a: Func717(*a, **{
'sArg': 'SlotNum' })))


class CPerform(CCustomPerform):
    m_SID = 51276
    m_Name = '强化复制'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3 }
    m_BaseArgData = {
        'SlotNum': 2 }
    m_DieDisable = 0
    m_QualityValue = {
        ABILITY_QUALITY_FOUR: 1 }
    m_AbilityType = ABILITY_TYPE_POSITIVE
    m_BaseValue = 0
    m_IsReverseFloting = 0

