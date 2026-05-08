# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13094.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13094.pyc
# Source Generated with Decompyle++
# File: p13094.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH
from cl_item.defines import MSG_ITEM_MAXPFBULLET_CHANGE
from cl_newformula import Func687, Func755, Func811

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetLinkPFBulletAttr(oWarrior, oLifeCycle, 5000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oWarrior, oLifeCycle, MSG_ITEM_MAXPFBULLET_CHANGE, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 4, 0, 0)
    if cl_condition.PassiveCheckFromMainHoldWeapon(oWarrior, oLifeCycle):
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33310, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func687(*a))) >= 0:
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func811(*a, **{
'sAttr': 'MaxPFBullet' }))) < cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func755(*a, **{
'sAttr': 'MaxPFBullet' }))):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ForceSetFlag', 0)
            cl_action.CommonClearSourceWeaponPFBulletPerfomrForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletUse')
        elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ForceSetFlag') and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func811(*a, **{
'sAttr': 'PFBulletUse' }))) > cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func755(*a, **{
'sAttr': 'PFBulletUse' }))):
            cl_action.CommonSetSourceWeaponPFBulletPerfomrForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletUse', (lambda *a: Func755(*a, **{
'sAttr': 'MaxPFBullet' })))
        elif cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func755(*a, **{
'sAttr': 'PFBulletUse' }))) > cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func755(*a, **{
'sAttr': 'MaxPFBullet' }))):
            cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'ForceSetFlag', 1)
            cl_action.CommonSetSourceWeaponPFBulletPerfomrForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletUse', (lambda *a: Func755(*a, **{
'sAttr': 'MaxPFBullet' })))
        elif cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'ForceSetFlag') and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func811(*a, **{
'sAttr': 'PFBulletUse' }))) > cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func755(*a, **{
'sAttr': 'PFBulletUse' }))):
            cl_action.CommonSetSourceWeaponPFBulletPerfomrForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'PFBulletUse', (lambda *a: Func755(*a, **{
'sAttr': 'MaxPFBullet' })))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_action.PassiveAddState(oWarrior, oEventCB.GetCBLifeCycle(), 33310, 0, { }, 1)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33310, 1)


class CPerform(CCustomPerform):
    m_SID = 13094
    m_Name = '法杖双子'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((24,), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

