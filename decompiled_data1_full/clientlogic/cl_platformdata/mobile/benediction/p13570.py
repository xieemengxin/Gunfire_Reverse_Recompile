# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13570.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13570.pyc
# Source Generated with Decompyle++
# File: p13570.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import DROP_REASON_NPCREWARD, LEVEL_TYPE_BOSS, OBJECT_SERVANT, SENDREWARD_XIAOJIU_MODIFY, SENDREWARD_XIAOJIU_UPGRADE
from cl_newformula import Func304, Func332, Func634, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ADDTALENT, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBackFromOwnByAttr(oWarrior, oLifeCycle, 'HPMax', 1, OBJECT_SERVANT)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, -1, 2)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangeServantAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func332(*a) * 10000 + Func717(*a, **{
'sArg': 'ExtraHPMax' })), 1)
    if cl_evcon.CheckDropReason(oWarrior, oEventCB, DROP_REASON_NPCREWARD):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExtraHPMax', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2))
        cl_action.CommonChangeServantAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func332(*a) * 10000 + Func717(*a, **{
'sArg': 'ExtraHPMax' })), 1)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', 0)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstUpgradeHP') and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstUpgradeTimes'):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FirstUpgradeTimes', -1)
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', 1)
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HadUpgradeTimes') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanUpgradeTimes') and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstUpgradeHP' })) // Func717(*a, **{
'sArg': 'UpgradePerHP' }))) > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HadUpgradeTimes'):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', (lambda *a: min((Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstUpgradeHP' })) // Func717(*a, **{
'sArg': 'UpgradePerHP' }) - Func717(*a, **{
'sArg': 'HadUpgradeTimes' }), Func717(*a, **{
'sArg': 'CanUpgradeTimes' }) - Func717(*a, **{
'sArg': 'HadUpgradeTimes' }))))
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardUpgradeTimes'):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HadUpgradeTimes', (lambda *a: Func717(*a, **{
'sArg': 'RewardUpgradeTimes' })))
            cl_action.CommonSendRandomPassiveReward(oWarrior, oEventCB.GetCBLifeCycle(), {
                5362: 1,
                5363: 1,
                5364: 1,
                5365: 1,
                5366: 1 }, 0, 'b13570Upgrade', 0, 1, SENDREWARD_XIAOJIU_UPGRADE, (lambda *a: Func717(*a, **{
'sArg': 'RewardUpgradeTimes' })), 8)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', 0)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstModifyHP') and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstModifyTimes'):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FirstModifyTimes', -1)
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', 1)
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstModifyHP' })) // Func717(*a, **{
'sArg': 'ModifyPerHP' }))) > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HadModifyTimes'):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstModifyHP' })) // Func717(*a, **{
'sArg': 'ModifyPerHP' }) - Func717(*a, **{
'sArg': 'HadModifyTimes' })))
        if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardModifyTimes'):
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HadModifyTimes', (lambda *a: Func717(*a, **{
'sArg': 'RewardModifyTimes' })))
            cl_action.CommonSendRandomPassiveReward(oWarrior, oEventCB.GetCBLifeCycle(), {
                5358: 1,
                5359: 1,
                5360: 1,
                5361: 1 }, 0, 'b13570Modify', 2, 0, SENDREWARD_XIAOJIU_MODIFY, (lambda *a: Func717(*a, **{
'sArg': 'RewardModifyTimes' })), 8)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstUpgradeHP'):
        cl_action.CommonResetHistoryRewardPassive(oWarrior, oEventCB.GetCBLifeCycle(), 'b13570Upgrade', (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstUpgradeHP' })) // Func717(*a, **{
'sArg': 'UpgradePerHP' }) + 1))
    else:
        cl_action.CommonResetHistoryRewardPassive(oWarrior, oEventCB.GetCBLifeCycle(), 'b13570Upgrade', 0)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstModifyHP'):
        cl_action.CommonResetHistoryRewardPassive(oWarrior, oEventCB.GetCBLifeCycle(), 'b13570Modify', (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstModifyHP' })) // Func717(*a, **{
'sArg': 'ModifyPerHP' }) + 1))
    else:
        cl_action.CommonResetHistoryRewardPassive(oWarrior, oEventCB.GetCBLifeCycle(), 'b13570Modify', 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExtraHPMax', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2))
        cl_action.CommonChangeServantAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func332(*a) * 10000 + Func717(*a, **{
'sArg': 'ExtraHPMax' })), 1)
        cl_evact.DelayTriggerGroup(oWarrior, oEventCB, 6, 1, 100, 0, 0, { })


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ExtraHPMax', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 2))
    cl_action.CommonChangeServantAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', 0, (lambda *a: Func332(*a) * 10000 + Func717(*a, **{
'sArg': 'ExtraHPMax' })), 1)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', 0)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstUpgradeHP') and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstUpgradeTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FirstUpgradeTimes', -1)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HadUpgradeTimes') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanUpgradeTimes') and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstUpgradeHP' })) // Func717(*a, **{
'sArg': 'UpgradePerHP' }))) > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HadUpgradeTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', (lambda *a: min((Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstUpgradeHP' })) // Func717(*a, **{
'sArg': 'UpgradePerHP' }) - Func717(*a, **{
'sArg': 'HadUpgradeTimes' }), Func717(*a, **{
'sArg': 'CanUpgradeTimes' }) - Func717(*a, **{
'sArg': 'HadUpgradeTimes' }))))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardUpgradeTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HadUpgradeTimes', (lambda *a: Func717(*a, **{
'sArg': 'RewardUpgradeTimes' })))
        cl_action.CommonSendRandomPassiveReward(oWarrior, oEventCB.GetCBLifeCycle(), {
            5362: 1,
            5363: 1,
            5364: 1,
            5365: 1,
            5366: 1 }, 0, 'b13570Upgrade', 0, 1, SENDREWARD_XIAOJIU_UPGRADE, (lambda *a: Func717(*a, **{
'sArg': 'RewardUpgradeTimes' })), 8)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', 0)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstModifyHP') and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstModifyTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FirstModifyTimes', -1)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', 1)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstModifyHP' })) // Func717(*a, **{
'sArg': 'ModifyPerHP' }))) > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HadModifyTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstModifyHP' })) // Func717(*a, **{
'sArg': 'ModifyPerHP' }) - Func717(*a, **{
'sArg': 'HadModifyTimes' })))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardModifyTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HadModifyTimes', (lambda *a: Func717(*a, **{
'sArg': 'RewardModifyTimes' })))
        cl_action.CommonSendRandomPassiveReward(oWarrior, oEventCB.GetCBLifeCycle(), {
            5358: 1,
            5359: 1,
            5360: 1,
            5361: 1 }, 0, 'b13570Modify', 2, 0, SENDREWARD_XIAOJIU_MODIFY, (lambda *a: Func717(*a, **{
'sArg': 'RewardModifyTimes' })), 8)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', 0)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstUpgradeHP') and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstUpgradeTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FirstUpgradeTimes', -1)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', 1)
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('HadUpgradeTimes') < oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('CanUpgradeTimes') and cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstUpgradeHP' })) // Func717(*a, **{
'sArg': 'UpgradePerHP' }))) > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HadUpgradeTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardUpgradeTimes', (lambda *a: min((Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstUpgradeHP' })) // Func717(*a, **{
'sArg': 'UpgradePerHP' }) - Func717(*a, **{
'sArg': 'HadUpgradeTimes' }), Func717(*a, **{
'sArg': 'CanUpgradeTimes' }) - Func717(*a, **{
'sArg': 'HadUpgradeTimes' }))))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardUpgradeTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HadUpgradeTimes', (lambda *a: Func717(*a, **{
'sArg': 'RewardUpgradeTimes' })))
        cl_action.CommonSendRandomPassiveReward(oWarrior, oEventCB.GetCBLifeCycle(), {
            5362: 1,
            5363: 1,
            5364: 1,
            5365: 1,
            5366: 1 }, 0, 'b13570Upgrade', 0, 1, SENDREWARD_XIAOJIU_UPGRADE, (lambda *a: Func717(*a, **{
'sArg': 'RewardUpgradeTimes' })), 8)
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', 0)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func634(*a, **{
'sAttr': 'HPMax' }))) >= cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstModifyHP') and cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'FirstModifyTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'FirstModifyTimes', -1)
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', 1)
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstModifyHP' })) // Func717(*a, **{
'sArg': 'ModifyPerHP' }))) > cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'HadModifyTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'RewardModifyTimes', (lambda *a: (Func634(*a, **{
'sAttr': 'HPMax' }) - Func717(*a, **{
'sArg': 'FirstModifyHP' })) // Func717(*a, **{
'sArg': 'ModifyPerHP' }) - Func717(*a, **{
'sArg': 'HadModifyTimes' })))
    if oEventCB.GetCBLifeCycle().m_Owner.GetArgValue('RewardModifyTimes'):
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, 'HadModifyTimes', (lambda *a: Func717(*a, **{
'sArg': 'RewardModifyTimes' })))
        cl_action.CommonSendRandomPassiveReward(oWarrior, oEventCB.GetCBLifeCycle(), {
            5358: 1,
            5359: 1,
            5360: 1,
            5361: 1 }, 0, 'b13570Modify', 2, 0, SENDREWARD_XIAOJIU_MODIFY, (lambda *a: Func717(*a, **{
'sArg': 'RewardModifyTimes' })), 8)


class CPerform(CCustomPerform):
    m_SID = 13570
    m_Name = '#NT#战斗核心'
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
        2: DoCallBackAction2,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = {
        'CanUpgradeTimes': 2,
        'HadModifyTimes': 0,
        'ExtraHPMax': 0,
        'RewardModifyTimes': 0,
        'UpgradePerHP': 200000,
        'ModifyPerHP': 50000,
        'FirstModifyHP': 50000,
        'FirstModifyTimes': 1,
        'FirstUpgradeHP': 0,
        'FirstUpgradeTimes': 1,
        'CanModifyTimes': -1,
        'HadUpgradeTimes': 0,
        'RewardUpgradeTimes': 0 }
    m_DieDisable = 0
    m_Career = 120

