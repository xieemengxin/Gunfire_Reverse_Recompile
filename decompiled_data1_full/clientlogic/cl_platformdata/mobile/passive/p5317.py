# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5317.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5317.pyc
# Source Generated with Decompyle++
# File: p5317.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction5317InitAttr
from cl_platformdata.custom.passive.customaction import CustomAction5317ChangeCount
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, DAM_USE_ARMOR, DAM_USE_HP, DAM_USE_SHIELD, DOUBLE_SHOOT_SETTLE_DAMAGE, OBJ_VICTIM, WARRIOR_MONSTER
from cl_newformula import Func369, Func425, Func651, Func717, Func780

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CommonCheckItemTmpData(oWarrior, oLifeCycle, '5317HasInitAttr') == 0:
        cl_action.CommonSetSourceItemTmpData(oWarrior, oLifeCycle, '5317HasInitAttr', 1)
        CustomAction5317InitAttr(oWarrior, oLifeCycle, {
            'MaxCount': 10,
            'Perform': 9020 })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAM, ATTACKERSUBMSG_NORMAL, 4, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 7, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, -1, 9, 0, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9020, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'EnhanceShoot') == 0 or cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'AddCountFlag', 0) == 0:
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'AddCountFlag', 1, 0)
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddDam', (lambda *a: Func369(*a) * max(50, Func780(*a, **{
'sKey': 'RecordDamRatio' })) // 100))
        cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'StoreDam', (lambda *a: Func780(*a, **{
'sKey': 'StoreDam' }) + Func717(*a, **{
'sArg': 'AddDam' })))
    elif cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1315: 1,
        8505: 1,
        1319: 1 }, 1, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddDam', (lambda *a: Func369(*a) * max(50, Func780(*a, **{
'sKey': 'RecordDamRatio' })) // 100))
        cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'StoreDam', (lambda *a: Func780(*a, **{
'sKey': 'StoreDam' }) + Func717(*a, **{
'sArg': 'AddDam' })))
        CustomAction5317ChangeCount(oWarrior, oEventCB.GetCBLifeCycle(), {
            'Perform': 9020 })


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9020, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'EnhanceShoot') == 1:
        CustomAction5317ChangeCount(oWarrior, oEventCB.GetCBLifeCycle(), {
            'ClearCount': 1,
            'Perform': 9020 })
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33570, 50, { }, 1, 1, 0)
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
            cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, 10, WARRIOR_MONSTER, 1, 0, 0, 0, 0, 0, 0)
            if cl_evcon.GetTargetNum(oWarrior, oEventCB) > 0:
                cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func780(*a, **{
'sKey': 'StoreDam' }) + Func425(*a)) // cl_evcon.GetTargetNum(oWarrior, oEventCB)), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_HP | DAM_USE_SHIELD | DAM_USE_ARMOR | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, DOUBLE_SHOOT_SETTLE_DAMAGE, 0, None)
                cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 33561, 50, {
                    'OriginMonster': (lambda *a: Func651(*a, **{
'sKey': 'VID' })) }, 1, 1, 0)
        cl_evact.EventCBSetDamShowTipsType(oWarrior, oEventCB, DOUBLE_SHOOT_SETTLE_DAMAGE)
        cl_evact.EventCBAdditionDamage(oWarrior, oEventCB, (lambda *a: Func780(*a, **{
'sKey': 'StoreDam' })))
        cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'StoreDam', 0)


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB) and cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9020, 1, 0) and cl_evcon.EventCBGetSkillCustomInfo(oWarrior, oEventCB, 'EnhanceShoot') == 1:
        CustomAction5317ChangeCount(oWarrior, oEventCB.GetCBLifeCycle(), {
            'ClearCount': 1,
            'Perform': 9020 })
        cl_action.CommonSetSourceItemTmpData(oWarrior, oEventCB.GetCBLifeCycle(), 'StoreDam', 0)


def DoCallBackAction9(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        CustomAction5317ChangeCount(oWarrior, oEventCB.GetCBLifeCycle(), {
            'Perform': 9020 })


class CPerform(CCustomPerform):
    m_SID = 5317
    m_Name = '#NT双发步枪被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2,
        4: DoCallBackAction4,
        7: DoCallBackAction7,
        9: DoCallBackAction9 }
    m_BaseArgData = { }
    m_DieDisable = 0

