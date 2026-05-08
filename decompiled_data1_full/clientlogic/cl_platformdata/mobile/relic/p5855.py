# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5855.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5855.pyc
# Source Generated with Decompyle++
# File: p5855.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_LOW, RELIC_TYPE_NORMAL
from cl_newformula import Func239

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, None)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 0, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEWEAPON, -1, 0, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 1, 1)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, -1, 1, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 4, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, 0, None)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_AFTERADDWEAPON, -1, 2, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEWEAPON, -1, 2, 0)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE, -1, 3, 1)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 2, 1)
    cl_action.CommonListenAllHeroMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERLEAVEGAME, -1, 3, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVERELIC, -1, 5, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.CalTeamSameWeaponInfo(oWarrior, oEventCB, 0)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'Att', 0, (lambda *a: Func239(*a, **{
'iType': 0 }) * 1000 + Func239(*a, **{
'iType': 2 }) * 1000), 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.RemoveTeamSameWeaponInfo(oWarrior, oEventCB)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'Att', 0, (lambda *a: Func239(*a, **{
'iType': 0 }) * 1000 + Func239(*a, **{
'iType': 2 }) * 1000), 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.CalTeamSameWeaponInfo(oWarrior, oEventCB, 1)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'Att', 0, (lambda *a: Func239(*a, **{
'iType': 1 }) * 1000), 0)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'LuckyHit', (lambda *a: Func239(*a, **{
'iType': 0 }) * 10), 0, 0)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func239(*a, **{
'iType': 2 }) * 2000), 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_evact.RemoveTeamSameWeaponInfo(oWarrior, oEventCB)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'Att', 0, (lambda *a: Func239(*a, **{
'iType': 1 }) * 1000), 0)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'LuckyHit', (lambda *a: Func239(*a, **{
'iType': 0 }) * 10), 0, 0)
    cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func239(*a, **{
'iType': 2 }) * 2000), 0, 0)


def DoCallBackAction4(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5855):
        cl_evact.RemoveTeamSameWeaponInfo(oWarrior, oEventCB)
        cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'Att', 0, (lambda *a: Func239(*a, **{
'iType': 0 }) * 1000 + Func239(*a, **{
'iType': 2 }) * 1000), 0)


def DoCallBackAction5(oEventCB, oWarrior):
    if cl_evcon.CheckPointRelic(oWarrior, oEventCB, 5855):
        cl_evact.RemoveTeamSameWeaponInfo(oWarrior, oEventCB)
        cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'Att', 0, (lambda *a: Func239(*a, **{
'iType': 1 }) * 1000), 0)
        cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'LuckyHit', (lambda *a: Func239(*a, **{
'iType': 0 }) * 10), 0, 0)
        cl_evact.EventCBChangeAllWeaponAttr(oWarrior, oEventCB, 'CrazyEff', (lambda *a: Func239(*a, **{
'iType': 2 }) * 2000), 0, 0)


class CPerform(CCustomPerform):
    m_SID = 5855
    m_Name = '心意相通'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4,
        5: DoCallBackAction5 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5523
    m_ValidRemove = 1
    m_BasePrice = 80
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_LOW

