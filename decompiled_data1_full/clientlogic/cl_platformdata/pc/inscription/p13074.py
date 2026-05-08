# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p13074.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p13074.pyc
# Source Generated with Decompyle++
# File: p13074.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import EQUIP_TYPE_FUNDAMENTALWEAPON, INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH
from cl_item.defines import MSG_ITEM_REFRESHATTRIBUTE
from cl_newformula import Func606

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetLinkAttr(oWarrior, oLifeCycle, 'MaxBullet', 200)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1866, 0, { }, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oWarrior, oLifeCycle, MSG_ITEM_REFRESHATTRIBUTE, 1, 0, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckSwitchWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_action.PassiveCloseLinkPerform(oWarrior, oEventCB.GetCBLifeCycle())
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func606(*a, **{
'sAttr': 'MaxBullet' }))) > 0:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1869, 0, { }, 1, 1, None)
        cl_evact.PassiveSetStateCount(oWarrior, oEventCB, 1869, (lambda *a: Func606(*a, **{
'sAttr': 'MaxBullet' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckItemRefreshAttribute(oWarrior, oEventCB, 'MaxBullet'):
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func606(*a, **{
'sAttr': 'MaxBullet' }))) > 0:
            if not cl_condition.HasState(oWarrior, oEventCB.GetCBLifeCycle(), 1869):
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 1869, 0, { }, 1, 1, None)
            cl_action.CommonSetStateCount(oWarrior, oEventCB.GetCBLifeCycle(), 1869, (lambda *a: Func606(*a, **{
'sAttr': 'MaxBullet' })), None)
        else:
            cl_action.CommonRemoveState(oWarrior, oEventCB.GetCBLifeCycle(), 1869)


class CPerform(CCustomPerform):
    m_SID = 13074
    m_Name = '弹夹连结（层数）'
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
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((10,), (4878,), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

