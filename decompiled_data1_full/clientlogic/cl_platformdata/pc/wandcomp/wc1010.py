# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wandcomp/wc1010.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wandcomp/wc1010.pyc
# Source Generated with Decompyle++
# File: wc1010.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.wandcomp.customaction import CustomActionCostBullet
from cl_platformdata.custom.wandcomp.customaction import CustomActionCostBagBullet
from cl_wand.mobject import CWandComp as CBaseComp
from cl_commondefines import COST_BAGBULLET_WEAPON, DEPUTY_HOLD, DUAL_STATE_BEGIN, DUAL_STATE_END, MAIN_HOLD, WANDTAG_WEAPON, WAND_COMP_TYPE_CONDITION
from cl_newformula import Func208, Func215, Func517, Func533, Func742, Func758, Func777

def Action2(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 201):
        cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 13, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 12, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBULLETCHANGE, -1, 4, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 6, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 8, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_BEGIN, 5, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DUALSTATE, DUAL_STATE_END, 14, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPERFROM_COSTBULLET, -1, 17, 0, 0)
    else:
        cl_action.CommonSetEventMaxCBCycle(oWarrior, oLifeCycle, 1)
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBULLET, -1, 1, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, COST_BAGBULLET_WEAPON, 2, 0, 0)
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAXBULLETCHANGE, -1, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.WandConditionCompCBSetCount(oWarrior, oEventCB, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: max(1, Func517(*a))))
    cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'LastMaxBullet', (lambda *a: Func517(*a)))


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508):
        cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: Func208(*a)))


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508):
        cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: Func215(*a)))


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.WandConditionCompCBSetCount(oWarrior, oEventCB, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: max(1, Func517(*a))))


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MainAttackNum', 0)
    cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MainHoldMaxBullet', (lambda *a: max(1, Func517(*a))))
    cl_evact.WandConditionCompCBSetCount(oWarrior, oEventCB, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: max(1, Func517(*a))))


def DoCallBackAction5(oEventCB, oWarrior):
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MainAttackNum', (lambda *a: Func777(*a)))
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'DeputyAttackNum', 0)
    cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MainHoldMaxBullet', (lambda *a: max(1, Func517(*a))))
    cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'DeputyHoldMaxBullet', (lambda *a: max(1, Func533(*a))))


def DoCallBackAction6(oEventCB, oWarrior):
    if not cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508):
        if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
            cl_evact.WandCompCBAddArgValue(oWarrior, oEventCB, 'MainAttackNum', (lambda *a: Func208(*a)))
            cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: Func208(*a)))
            cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum', (lambda *a: 100 * Func742(*a, **{
'sArg': 'MainAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'MainHoldMaxBullet' })) + 100 * Func742(*a, **{
'sArg': 'DeputyAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'DeputyHoldMaxBullet' }))))
            if cl_condition.WandCompGetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum') >= 100:
                cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())
            elif cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, DEPUTY_HOLD):
                cl_evact.WandCompCBAddArgValue(oWarrior, oEventCB, 'DeputyAttackNum', (lambda *a: Func208(*a)))
                cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum', (lambda *a: 100 * Func742(*a, **{
'sArg': 'MainAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'MainHoldMaxBullet' })) + 100 * Func742(*a, **{
'sArg': 'DeputyAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'DeputyHoldMaxBullet' }))))
                if cl_condition.WandCompGetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum') >= 100:
                    cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction8(oEventCB, oWarrior):
    if not cl_evcon.CheckCostBulletType(oWarrior, oEventCB, 4508):
        if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, MAIN_HOLD):
            cl_evact.WandCompCBAddArgValue(oWarrior, oEventCB, 'MainAttackNum', (lambda *a: Func215(*a)))
            cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: Func215(*a)))
            cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum', (lambda *a: 100 * Func742(*a, **{
'sArg': 'MainAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'MainHoldMaxBullet' })) + 100 * Func742(*a, **{
'sArg': 'DeputyAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'DeputyHoldMaxBullet' }))))
            if cl_condition.WandCompGetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum') >= 100:
                cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())
            else:
                cl_evact.WandCompCBAddArgValue(oWarrior, oEventCB, 'DeputyAttackNum', (lambda *a: Func215(*a)))
                if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, DEPUTY_HOLD):
                    cl_evact.WandCompCBAddArgValue(oWarrior, oEventCB, 'DeputyAttackNum', (lambda *a: Func215(*a)))
                    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum', (lambda *a: 100 * Func742(*a, **{
'sArg': 'MainAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'MainHoldMaxBullet' })) + 100 * Func742(*a, **{
'sArg': 'DeputyAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'DeputyHoldMaxBullet' }))))
                    if cl_condition.WandCompGetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum') >= 100:
                        cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())


def DoCallBackAction12(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponHoldType(oWarrior, oEventCB, DEPUTY_HOLD) == 0:
        cl_evact.WandConditionCompCBSetCount(oWarrior, oEventCB, 0)
        cl_action.WandConditionCompSetFinishCount(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func517(*a)))
        cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'LastMaxBullet', (lambda *a: max(1, Func517(*a))))
        cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MainHoldMaxBullet', (lambda *a: max(1, Func517(*a))))
        cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'DeputyHoldMaxBullet', (lambda *a: max(1, Func533(*a))))
        cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MainAttackNum', 0)
        cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'DeputyAttackNum', 0)


def DoCallBackAction13(oEventCB, oWarrior):
    cl_evact.WandConditionCompCBSetCount(oWarrior, oEventCB, 0)
    cl_action.WandConditionCompSetFinishCount(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func517(*a)))
    cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'LastMaxBullet', (lambda *a: max(1, Func517(*a))))
    cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'MainHoldMaxBullet', (lambda *a: max(1, Func517(*a))))
    cl_action.WandCompSetKeepValue(oWarrior, oEventCB.GetCBLifeCycle(), 'DeputyHoldMaxBullet', (lambda *a: max(1, Func533(*a))))


def DoCallBackAction14(oEventCB, oWarrior):
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'DeputyAttackNum', 0)


def DoCallBackAction17(oEventCB, oWarrior):
    cl_evact.WandCompCBAddArgValue(oWarrior, oEventCB, 'MainAttackNum', (lambda *a: Func208(*a)))
    cl_evact.WandConditionCompCBAddCount(oWarrior, oEventCB, (lambda *a: Func208(*a)))
    cl_action.WandCompSetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum', (lambda *a: 100 * Func742(*a, **{
'sArg': 'MainAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'MainHoldMaxBullet' })) + 100 * Func742(*a, **{
'sArg': 'DeputyAttackNum' }) / max(1, Func758(*a, **{
'sAttr': 'DeputyHoldMaxBullet' }))))
    if cl_condition.WandCompGetArgValue(oWarrior, oEventCB.GetCBLifeCycle(), 'FinishNum') >= 100:
        cl_action.WandCompFinishCondition(oWarrior, oEventCB.GetCBLifeCycle())


class CWandComp(CBaseComp):
    m_SID = 1010
    m_Name = '消耗弹药'
    m_Type = WAND_COMP_TYPE_CONDITION
    m_Tag = (WANDTAG_WEAPON,)
    m_ActionInfo = {
        2: (Action2, None) }
    m_TriggerActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5,
        6: DoCallBackAction6,
        8: DoCallBackAction8,
        12: DoCallBackAction12,
        13: DoCallBackAction13,
        14: DoCallBackAction14,
        17: DoCallBackAction17 }

