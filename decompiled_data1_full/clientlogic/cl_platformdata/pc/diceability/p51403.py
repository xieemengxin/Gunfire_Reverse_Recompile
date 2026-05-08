# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/diceability/p51403.pyc
# RelativePath: clientlogic/cl_platformdata/pc/diceability/p51403.pyc
# Source Generated with Decompyle++
# File: p51403.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.diceability import CDiceAbility as CCustomPerform
from cl_commondefines import DICETAG_WEAPON, DICE_PUTOUT_POLL_TWO, EQUIP_TYPE_FUNDAMENTALWEAPON, EQUIP_TYPE_MAINWEAPON
from cl_newformula import Func717, Func834, Func835

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 2)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Accuracy', 50, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Stability', 50, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })


def Action2(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 3)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Stability', 50, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Accuracy', 50, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })


def Action3(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 4)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Stability', 50, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Accuracy', 50, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })


def Action4(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 5)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonAddFundamentalInscription(oWarrior, oLifeCycle, {
        4890: 1,
        4889: 1,
        13086: 1,
        4820: 1,
        4849: 1,
        4891: 1,
        4880: 1 }, 1)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Stability', 100, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Accuracy', 100, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })


def Action5(oWarrior, oLifeCycle):
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddLuckyHit', 7)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonAddFundamentalInscription(oWarrior, oLifeCycle, {
        4890: 1,
        4889: 1,
        13086: 1,
        4820: 1,
        4849: 1,
        4891: 1,
        4880: 1 }, 2)
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Accuracy', 100, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })
    cl_action.CommonChangeTargetWeaponAttr(oWarrior, oLifeCycle, 'Stability', 100, 0, {
        EQUIP_TYPE_MAINWEAPON: 1 }, { })


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonListenMsgCallBack(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CHANGE_WEAPONGRADE, -1, 1, 0, 0)
    cl_action.CommonReplaceFundamentalLevelFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func834(*a) * 2))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_evact.EventCBChangeWeaponAttr(oWarrior, oEventCB, 'LuckyHit', (lambda *a: Func717(*a, **{
'sArg': 'AddLuckyHit' }) * Func835(*a, **{
'sAttr': 'Grade' })), 0)


class CPerform(CCustomPerform):
    m_SID = 51403
    m_Name = '熔炉觉醒'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Tag = (DICETAG_WEAPON,)
    m_PutOutPoolType = DICE_PUTOUT_POLL_TWO

