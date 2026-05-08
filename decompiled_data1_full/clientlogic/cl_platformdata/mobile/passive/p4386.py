# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4386.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4386.pyc
# Source Generated with Decompyle++
# File: p4386.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, PF_TYPE_CAREERPF, PF_TYPE_THROW
from cl_newformula import Func14, Func663, Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 9703, 0, 0):
        cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
    elif cl_evcon.CheckPerformIsInkPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Limit', 2)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) == 0 and cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a) - 3)):
            cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a)), (lambda *a: Func14(*a)))
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
        elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) > 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Limit'):
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
    elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Limit', 8)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) == 0 and cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a) - 3)):
            cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a)), (lambda *a: Func14(*a)))
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
        elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) > 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Limit'):
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, 0):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Limit', 4)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) == 0 and cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a) - 3)):
            cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a)), (lambda *a: Func14(*a)))
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
        elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) > 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Limit'):
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
    elif cl_evcon.CheckPerformIsInkPerform(oWarrior, oEventCB):
        cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Limit', 2)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) == 0 and cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a) - 3)):
            cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a)), (lambda *a: Func14(*a)))
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
        elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) > 0:
            pass
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Limit'):
            cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
        elif cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 0):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'Limit', 8)
            if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) == 0 and cl_evcon.PassiveCBGetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func14(*a) - 3)):
                cl_evact.PassiveCBSetPFArgsByFormulaKey(oWarrior, oEventCB, (lambda *a: Func663(*a)), (lambda *a: Func14(*a)))
                cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
                cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))
            elif cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) > 0 and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1) < cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'Limit'):
                cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'iDamCnt', 1, 1)
                cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9793, (lambda *a: Func686(*a, **{
'iPerform': 9793,
'sAttr': 'PFBulletRecover' })))


class CPerform(CCustomPerform):
    m_SID = 4386
    m_Name = '浮游炮-能量恢复'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 1

