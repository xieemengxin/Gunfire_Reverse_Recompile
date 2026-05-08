# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4259.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4259.pyc
# Source Generated with Decompyle++
# File: p4259.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import WARRIOR_MONSTER

def Action1(oWarrior, oLifeCycle):
    CustomAction(oWarrior, oLifeCycle, {
        'Type': 'TypeWeight',
        20891: 0.3,
        23611: 0.3,
        23811: 2,
        23812: 1,
        23813: 0.5,
        21281: 1.5,
        23851: 1,
        21081: 1.2,
        21091: 1,
        21101: 1.2,
        20651: 1,
        21641: 1,
        21651: 1 })
    CustomAction(oWarrior, oLifeCycle, {
        'Type': 'LifeWeight',
        100: 0.2,
        80: 1,
        50: 1.5,
        0: 2 })
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'LifeRange', 15)
    CustomAction(oWarrior, oLifeCycle, {
        'Type': 'SuperWeight',
        20891: 0.3,
        23611: 0.3,
        23811: 2,
        23812: 1,
        23813: 1,
        21281: 1.5,
        23851: 1,
        21081: 1.2,
        21091: 1.2,
        21101: 1.2,
        20651: 1,
        21641: 1.5,
        21651: 1.5 })
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'SuperRange', 15)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, -1, 0, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'LifeRange', 10)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'SuperRange', 10)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 31261, 0, None):
        cl_evact.EventGetRangeTargetByFightType(oWarrior, oEventCB, 50, WARRIOR_MONSTER, 1, 0, 1, 0, 0, { }, None, None, None, None, None)
        cl_evact.EventCBTargetUsePerform(oWarrior, oEventCB, 1, {
            24014: 0 })


class CPerform(CCustomPerform):
    m_SID = 4259
    m_Name = '巨型召唤怪被动-怪物权重'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0


def CustomAction(oWarrior, oLifeCycle, dInfo):
    sType = dInfo.pop('Type')
    if sType == 'LifeWeight':
        dInfo = sorted(dInfo.items(), key = (lambda item: item[0]), reverse = True)
    oWarrior.Set(sType, dInfo)

