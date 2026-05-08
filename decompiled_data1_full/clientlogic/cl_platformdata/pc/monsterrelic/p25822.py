# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25822.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25822.pyc
# Source Generated with Decompyle++
# File: p25822.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import LEVEL_TYPE_BOSS, OBJ_SELF, QUALITY_TYPE_LOW, WARRIOR_ELITE
from cl_newformula import Func204

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 0, 0, 0)
    cl_action.CommonAttentionOwnerRoomGoalCallBack(oWarrior, oLifeCycle, 2)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if not cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        3165: 1,
        3299: 1,
        2341: 1,
        2342: 1,
        2343: 1,
        2344: 1,
        2345: 1,
        2346: 1,
        2004: 1,
        3004: 1 }) or cl_evcon.CheckTargetHasAfPF(oWarrior, oEventCB, 6114) or cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 50, 0, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
        cl_evact.EventCBCreateRandomNumMonster(oWarrior, oEventCB, 3, {
            2: 10 }, 0, 0, 0, 1, {
            24011: 1,
            34011: 1,
            32822: 1,
            32824: 1 }, {
            'Disable': {
                25822: 1,
                25823: 1 } }, {
            'HP': {
                'Mul': -9000 },
            'Shield': {
                'Mul': -9000 },
            'Armor': {
                'Mul': -9000 } }, 0, (lambda *a: Func204(*a) * 2))
    else:
        cl_evact.EventCBCreateRandomNumMonster(oWarrior, oEventCB, 3, {
            2: 10 }, 0, 0, 0, 1, {
            24011: 1,
            34011: 1,
            32822: 1,
            32824: 1 }, {
            'Disable': {
                25822: 1,
                25823: 1 } }, {
            'HP': {
                'Mul': -5000 },
            'Shield': {
                'Mul': -5000 },
            'Armor': {
                'Mul': -5000 } }, 0, (lambda *a: Func204(*a) * 2))


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.PassiveCBDisableSelf(oWarrior, oEventCB)
    cl_action.CommonKillAllMonster(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 25822
    m_Name = '有效分裂'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = 0
    m_HeroRelic = 5822
    m_Quality = QUALITY_TYPE_LOW
    m_ExcludeRelic = ()

