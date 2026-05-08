# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4332.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4332.pyc
# Source Generated with Decompyle++
# File: p4332.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM, PATHMODE_COLLISIONLESS, WARRIOR_BUILD_TRAP
from cl_newformula import Func362, Func852

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddCustomValueWithReason(oWarrior, oLifeCycle, '4332RobotRelife', 2000)
    cl_action.CommonSetDyingSecond(oWarrior, oLifeCycle, 12)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32758, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 5)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 2, 1, 0)
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'AttSpeed', -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIEDIST, -1, 0, 0, 0)
    cl_action.CommonSetServantBronPosInfo(oWarrior, oLifeCycle, 7, 10, 35, 75)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'AddSkillSpeed', 60)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_condition.CheckHasPerform(oWarrior, oEventCB.GetCBLifeCycle(), 4353):
        cl_evact.EventCBGetTargetByBelongs(oWarrior, oEventCB)
        if not cl_evcon.EventCBCheckTargetRealDead(oWarrior, oEventCB) or cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 33946, 0, 0, 0):
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 32744, (lambda *a: max(10, Func852(*a, **{
'sKey': '4332RobotRelife' }))), { }, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_ATTACK)
    if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BUILD_TRAP) or cl_evcon.CheckTargetPointBaseSummon(oWarrior, oEventCB, 1060):
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
    elif cl_evcon.CheckTargetPointBaseMonsters(oWarrior, oEventCB, {
        2004: 1,
        2221: 1,
        2222: 1,
        2223: 1,
        2224: 1,
        2201: 1,
        3083: 1,
        3201: 1,
        2381: 1,
        2382: 1,
        2385: 1,
        3381: 1,
        3382: 1,
        3384: 1 }):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -5000, 0, '')


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.SwitchTargetPathMode(oWarrior, oEventCB.GetCBLifeCycle(), PATHMODE_COLLISIONLESS)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 7141, 'ColdTime', (lambda *a: -Func362(*a, **{
'sAttr': 'AttSpeed' }) * 10000 / (100 + Func362(*a, **{
'sAttr': 'AttSpeed' }))), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 7148, 'ColdTime', (lambda *a: -Func362(*a, **{
'sAttr': 'AttSpeed' }) * 10000 / (100 + Func362(*a, **{
'sAttr': 'AttSpeed' }))), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 7143, 'ColdTime', (lambda *a: -Func362(*a, **{
'sAttr': 'AttSpeed' }) * 10000 / (100 + Func362(*a, **{
'sAttr': 'AttSpeed' }))), 0)
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 7144, 'ColdTime', (lambda *a: -Func362(*a, **{
'sAttr': 'AttSpeed' }) * 10000 / (100 + Func362(*a, **{
'sAttr': 'AttSpeed' }))), 0)


class CPerform(CCustomPerform):
    m_SID = 4332
    m_Name = '御灵师机甲被动'
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
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

