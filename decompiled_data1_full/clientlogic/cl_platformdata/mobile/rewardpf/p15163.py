# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p15163.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p15163.pyc
# Source Generated with Decompyle++
# File: p15163.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_PERFORM, DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_ALL, INK_DAMAGE, OBJ_VICTIM, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL
from cl_newformula import Func208, Func3, Func361, Func505, Func557, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 6, 0, 0)
    cl_action.CommonAddNeedSubCDPerform(oWarrior, oLifeCycle, 15163)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckSrcDamType(oWarrior, oEventCB, DAM_TYPE_SCENE) == 0 and cl_evcon.EventCBCheckVictimForSelf(oWarrior, oEventCB) == 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, '15163CrazyHit', 0) == 0:
        cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '15163Count', 1)
        if cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, '15163Count') >= 10:
            cl_evact.PassiveCBAddPFArgs(oWarrior, oEventCB, '15163Count', -10)
            cl_action.PassiveSubSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 10)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 0) == 0 and cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
        cl_action.PassiveSetSelfColdTime(oWarrior, oEventCB.GetCBLifeCycle(), 500)
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, '15163CrazyHit', 1, 0)
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_NORMAL):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func557(*a) * 10 // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, INK_DAMAGE, 0, None)
        elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_ELITE):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func557(*a) * 5 // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, INK_DAMAGE, 0, None)
        elif cl_evcon.CheckFightType(oWarrior, oEventCB, WARRIOR_BOSS):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: Func557(*a) * 2 // 100), DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, 1, 0, 0, INK_DAMAGE, 0, None)


def DoCallBackAction6(oEventCB, oWarrior):
    cl_evact.PassiveCBAddPFArgsValue(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ItemID' })), (lambda *a: Func208(*a)))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: 10 * cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, Func651(*a, **{
'sKey': 'ItemID' })))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func505(*a))):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Temp', (lambda *a: cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, Func651(*a, **{
'sKey': 'ItemID' }))))
        cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'ItemID' })), (lambda *a: Func3(*a, **{
'a': int(Func361(*a, **{
'sid': 15148,
'sArgs': 'Temp' }) * 10),
'b': int(Func505(*a)) }) // 10))
        cl_evact.PassiveSubPerformCD(oWarrior, oEventCB, 15163, (lambda *a: 10 * Func361(*a, **{
'sid': 15148,
'sArgs': 'Temp' }) * 10 // Func505(*a)))


class CPerform(CCustomPerform):
    m_SID = 15163
    m_Name = '灵犀一击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2,
        6: DoCallBackAction6 }
    m_BaseArgData = { }
    m_DieDisable = 0

