# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4841.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4841.pyc
# Source Generated with Decompyle++
# File: p4841.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.inscription.customaction import CustomAction4841 as CustomAction
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, EQUIP_TYPE_FUNDAMENTALWEAPON, INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_BOTH, OBJ_VICTIM

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAIN_ATTACK, ATTACKERSUBMSG_NORMAL, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 2001, 1, None, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 5, 0, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p4841IsShow', 0)
    cl_action.CommonSetCustomData(oWarrior, oLifeCycle, 'p4841OpenMsg', 0)
    cl_action.CommonTriggerClientBehavior(oWarrior, oLifeCycle, 2002, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1695, 1, 0):
        cl_evact.EventCBForbidCrazy(oWarrior, oEventCB)
        cl_evact.EventCBSetLuckyHitEff(oWarrior, oEventCB, 1)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1695, 1, 0) or cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        CustomAction(oWarrior, oEventCB, {
            'TriggerNum': 30 })


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    cl_evact.EventCBUsePerformEvtTarget(oWarrior, oEventCB, 1695, {
        'SporeNum': 20 }, None)
    cl_evact.EventClientBehavior(oWarrior, oEventCB, 2003, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'p4841IsShow', 0)
        cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 2002, 0, None, None)
    elif not cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'p4841IsShow'):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'p4841IsShow', 1)
        cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 2001, 1, None, None)


def DoCallBackAction5(oEventCB, oWarrior):
    if not cl_evact.EventCBGetCustomData(oWarrior, oEventCB, 'p4841OpenMsg'):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'p4841OpenMsg', 1)
        cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 4, 0, 0)


class CPerform(CCustomPerform):
    m_SID = 4841
    m_Name = '二相孢子'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_BOTH

