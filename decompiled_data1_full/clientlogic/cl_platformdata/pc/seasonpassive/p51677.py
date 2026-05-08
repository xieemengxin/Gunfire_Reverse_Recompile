# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51677.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51677.pyc
# Source Generated with Decompyle++
# File: p51677.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.seasonpassive.customaction import CustomAction51677 as CustomAction
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, MG_SOURCE_SEASONMODULE
from cl_newformula import Func859

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Cash', (lambda *a: Func859(*a, **{
'sAttr': 'CashRatioAdd' }) + Func859(*a, **{
'sAttr': 'ExtraRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Trigger', (lambda *a: Func859(*a, **{
'sAttr': 'TriggerRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Bullet', (lambda *a: Func859(*a, **{
'sAttr': 'BulletRatioAdd' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Cash', (lambda *a: Func859(*a, **{
'sAttr': 'CashRatioAdd' }) + Func859(*a, **{
'sAttr': 'ExtraRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Trigger', (lambda *a: Func859(*a, **{
'sAttr': 'TriggerRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Bullet', (lambda *a: Func859(*a, **{
'sAttr': 'BulletRatioAdd' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Cash', (lambda *a: Func859(*a, **{
'sAttr': 'CashRatioAdd' }) + Func859(*a, **{
'sAttr': 'ExtraRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Trigger', (lambda *a: Func859(*a, **{
'sAttr': 'TriggerRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Bullet', (lambda *a: Func859(*a, **{
'sAttr': 'BulletRatioAdd' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETDROP_PLAYER, -1, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Cash', (lambda *a: Func859(*a, **{
'sAttr': 'CashRatioAdd' }) + Func859(*a, **{
'sAttr': 'ExtraRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Trigger', (lambda *a: Func859(*a, **{
'sAttr': 'TriggerRatioAdd' })))
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, 'PF51677Bullet', (lambda *a: Func859(*a, **{
'sAttr': 'BulletRatioAdd' })))
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ASSISTKILL, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BULLETDROP_PLAYER, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckMiniGameSource(oWarrior, oEventCB, MG_SOURCE_SEASONMODULE):
        cl_evact.EventCBChangeBulletDropMiniGameChooseWeight(oWarrior, oEventCB, 4508, 0, (lambda *a: Func859(*a, **{
'sAttr': 'ExtraRatioAdd' }) // 100))


class CPerform(CCustomPerform):
    m_SID = 51677
    m_Name = '次要技能-额外补给'
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
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'CashRatioAdd': 2000,
            'TriggerRatioAdd': 2000,
            'BulletRatioAdd': 2000 },
        2: {
            'CashRatioAdd': 2500,
            'TriggerRatioAdd': 2500,
            'BulletRatioAdd': 2500 },
        3: {
            'CashRatioAdd': 3000,
            'TriggerRatioAdd': 3000,
            'BulletRatioAdd': 3000,
            'ExtraRatioAdd': 1000 },
        4: {
            'CashRatioAdd': 4000,
            'TriggerRatioAdd': 4000,
            'BulletRatioAdd': 4000,
            'ExtraRatioAdd': 2000 } }

