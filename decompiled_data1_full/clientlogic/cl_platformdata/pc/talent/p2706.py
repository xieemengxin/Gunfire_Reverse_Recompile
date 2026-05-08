# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2706.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2706.pyc
# Source Generated with Decompyle++
# File: p2706.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform
from cl_commondefines import OBJ_SELF
from cl_newformula import Func331, Func428

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)


def DisableAction3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateMaxCount(oWarrior, oEventCB, 32506, (lambda *a: Func331(*a, **{
'sid': 2706 })))
    cl_evact.EventCBAddTargetStateMaxCount(oWarrior, oEventCB, 32505, (lambda *a: Func331(*a, **{
'sid': 2706 })))
    if cl_evcon.GetTargetStateCount(oWarrior, oEventCB, 32505, None, None) < cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func428(*a, **{
'sid': 32506 }))):
        cl_evact.EventCBSetTargetStateCount(oWarrior, oEventCB, 32505, (lambda *a: Func428(*a, **{
'sid': 32506 })), -1)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func331(*a, **{
'sid': 2706 }))) == 3:
        cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 32504, 10, -1, None)
    else:
        cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 32504, 15, None, None)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBAddTargetStateMaxCount(oWarrior, oEventCB, 32505, (lambda *a: -Func331(*a, **{
'sid': 2706 })))
    cl_evact.EventCBAddTargetStateMaxCount(oWarrior, oEventCB, 32506, (lambda *a: -Func331(*a, **{
'sid': 2706 })))


class CPerform(CCustomPerform):
    m_SID = 2706
    m_Name = '通明剑心'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = {
        1: DisableAction1,
        2: DisableAction2,
        3: DisableAction3 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 2
    m_TalentType = 3
    m_IsRareTalent = 0
    m_Career = 109

