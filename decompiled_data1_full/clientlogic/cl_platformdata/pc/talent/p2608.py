# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/talent/p2608.pyc
# RelativePath: clientlogic/cl_platformdata/pc/talent/p2608.pyc
# Source Generated with Decompyle++
# File: p2608.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CTalent as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'AttDistance', 0, 1)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1330, 'EnergyRecoverL3', 500, 1)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1330, 'EnergyRecoverL4', 200, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'AddStateTime', 0, 200)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1330, 'L4Mul', 0.8, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1330, 'L4EndMul', 4.5, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'AttDistance', 0, 1)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1330, 'EnergyRecoverL3', 1000, 1)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1330, 'EnergyRecoverL4', 300, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1330, 'L4Mul', 1.2, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1330, 'L4EndMul', 6, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'AddStateTime', 0, 400)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'AttDistance', 0, 1)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1330, 'EnergyRecoverL3', 2000, 1)
    cl_action.CommonAddPerformArgsValue(oWarrior, oLifeCycle, 1330, 'EnergyRecoverL4', 400, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1330, 'L4Mul', 2, 1)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 1330, 'L4EndMul', 7.5, 1)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'AddStateTime', 0, 100000)


class CPerform(CCustomPerform):
    m_SID = 2608
    m_Name = '#NT#觉醒占位'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_MaxUpgradeTimes = 0
    m_TalentType = 1
    m_IsRareTalent = 0
    m_Career = 121

