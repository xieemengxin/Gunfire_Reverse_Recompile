# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51671.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51671.pyc
# Source Generated with Decompyle++
# File: p51671.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_ALL, OBJ_SELF, PF_SUBMSG_CAREERPF
from cl_newformula import Func374, Func717, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39750, 0, {
        'MaxRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxRate' }) // 100) }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 2)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39750, 0, {
        'MaxRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxRate' }) // 100) }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 3)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39750, 0, {
        'MaxRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxRate' }) // 100) }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 1, 0, 4)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39750, 0, {
        'MaxRate': (lambda *a: Func859(*a, **{
'sAttr': 'MaxRate' }) // 100) }, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromCareerPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Dam', (lambda *a: 25 * Func374(*a) // 10000))
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func717(*a, **{
'sArg': 'Dam' }))):
            cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Count', (lambda *a: Func717(*a, **{
'sArg': 'Dam' }) * Func859(*a, **{
'sAttr': 'Rate' })))
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func717(*a, **{
'sArg': 'Dam' }) * 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, None)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39750, (lambda *a: Func717(*a, **{
'sArg': 'Count' }) // 100), 0, 1, (lambda *a: Func859(*a, **{
'sAttr': 'Time' }) * 100))


class CPerform(CCustomPerform):
    m_SID = 51671
    m_Name = '主要技能-恶魔契约'
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
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'MaxRate': 5000,
            'Time': 10,
            'Rate': 16 },
        2: {
            'MaxRate': 10000,
            'Time': 10,
            'Rate': 20 },
        3: {
            'MaxRate': 15000,
            'Time': 15,
            'Rate': 24 },
        4: {
            'MaxRate': 25000,
            'Time': 15,
            'Rate': 32 } }

