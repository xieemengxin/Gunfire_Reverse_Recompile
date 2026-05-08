# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51676.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51676.pyc
# Source Generated with Decompyle++
# File: p51676.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import COST_BAGBULLET_THROW, OBJ_SELF
from cl_newformula import Func308, Func651, Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39764, 0, {
        'DamRate': (lambda *a: Func859(*a, **{
'sAttr': 'DamRate' })),
        'SrcLV': (lambda *a: Func308(*a)) }, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39764, 0, {
        'DamRate': (lambda *a: Func859(*a, **{
'sAttr': 'DamRate' })),
        'SrcLV': (lambda *a: Func308(*a)) }, 1)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39764, 0, {
        'DamRate': (lambda *a: Func859(*a, **{
'sAttr': 'DamRate' })),
        'ThrowRate': (lambda *a: Func859(*a, **{
'sAttr': 'ThrowRate' })),
        'SrcLV': (lambda *a: Func308(*a)) }, 1)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETCHANGE, COST_BAGBULLET_THROW, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 39764, 0, {
        'DamRate': (lambda *a: Func859(*a, **{
'sAttr': 'DamRate' })),
        'ThrowRate': (lambda *a: Func859(*a, **{
'sAttr': 'ThrowRate' })),
        'SrcLV': (lambda *a: Func308(*a)) }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBGetMsgInfo(oWarrior, oEventCB, 'Amount') > 0:
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 39764, (lambda *a: Func651(*a, **{
'sKey': 'Amount' })), 1, 1, None)


class CPerform(CCustomPerform):
    m_SID = 51676
    m_Name = '次要技能-韬光养晦'
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
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'DamRate': 2 },
        2: {
            'DamRate': 4 },
        3: {
            'DamRate': 6,
            'ThrowRate': 6 },
        4: {
            'DamRate': 8,
            'ThrowRate': 8 } }

