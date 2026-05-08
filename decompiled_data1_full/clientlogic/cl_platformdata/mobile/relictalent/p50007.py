# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50007.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50007.pyc
# Source Generated with Decompyle++
# File: p50007.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import OBJ_SELF, PF_SUBMSG_CAREERPF, WARRIOR_MONSTER
from cl_newformula import Func361, Func600

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1914)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1911)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33017, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33018, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 6, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, -1, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 6, 0, 0)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33033, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 205):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33053, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33049, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 206):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33054, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 212):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33050, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33051, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33057, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33056, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33055, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33052, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 218):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33641, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33642, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 220):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33871, 0, { }, 1)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 221):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33874, 0, { }, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1914, 'Att', (lambda *a: 10000 * Func600(*a) + 30000), None)
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1911, 'Att', (lambda *a: 50000 * Func600(*a) + 150000), None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1310, 1, 0):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventTargetGetRangeTargetByFightType(oWarrior, oEventCB, (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'EnemySearchRange' })), WARRIOR_MONSTER, 1, 0, (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'TargetCount' }) + Func361(*a, **{
'sid': 50007,
'sArgs': 'ExtraTargetCount' })), 0, 1, None, None)
        cl_evact.EventSplitTargetExecCBFuncAction(oWarrior, oEventCB, 4)


def DoCallBackAction4(oEventCB, oWarrior):
    cl_evact.EventCBUsePerform(oWarrior, oEventCB, 1914, 0, { })


def DoCallBackAction5(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventCBSetTargetStateMaxCount(oWarrior, oEventCB, 33017, (lambda *a: Func361(*a, **{
'sid': 50007,
'sArgs': 'MoveDistance' })), 0, None)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301002) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403004) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403003) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301003):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnemySearchRange', 50)
    else:
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'EnemySearchRange', 25)


class CPerform(CCustomPerform):
    m_SID = 50007
    m_Name = '步步惊雷'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6 }
    m_BaseArgData = {
        'MoveDistance': 160,
        'EnemySearchRange': 25,
        'ExtraThunderNum': 0,
        'ExtraTargetCount': 0,
        'TargetCount': 2,
        'ThunderNum': 1,
        'UseThunderCount': 1 }
    m_DieDisable = 0
    m_GrowPF = [
        50001,
        50003,
        50002,
        50004,
        50005,
        50006]
    m_DamagePF = [
        1914,
        1911]

