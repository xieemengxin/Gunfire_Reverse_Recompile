# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p16096.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p16096.pyc
# Source Generated with Decompyle++
# File: p16096.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import SMITHNPCSUBMSG_UPGRADE

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_BEFORESMITHNPC, SMITHNPCSUBMSG_UPGRADE, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'MaxCnt': 5,
        'ExtraLevel': 1 })


class CPerform(CCustomPerform):
    m_SID = 16096
    m_Name = '强五送一'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

from cl_commondefines import WARRIOR_HERO

def CustomAction(oListener, oEventCB, dInfo):
    if not oListener.m_FightType & WARRIOR_HERO:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo or 'NpcID' not in dMsgInfo or 'MaxCnt' not in dInfo or 'ExtraLevel' not in dInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iPerform = dEventInfo['pfid']
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return None
    iWeapon = dMsgInfo['ItemID']
    iNpc = dMsgInfo['NpcID']
    if iWeapon and iNpc:
        dWeaponInfo = {
            iWeapon: oPerform.GetArgValue(iNpc, { }).get(iWeapon, 0) + 1 }
        UpdateNpcInfo(oPerform, iNpc, dWeaponInfo)
        iMaxCnt = dInfo['MaxCnt']
        iExtraLevel = dInfo['ExtraLevel']
        if iMaxCnt and oPerform.GetArgValue(iNpc, { }).get(iWeapon, 0) >= iMaxCnt:
            UpdateNpcInfo(oPerform, iNpc, {
                iWeapon: 0 })
            cl_evact.EventCBAddWeaponUpgradeLevel(oListener, oEventCB, iExtraLevel)


def UpdateNpcInfo(oPerform, iNpc, dUpdate):
    dNpcInfo = oPerform.GetArgValue(iNpc, { })
    dNpcInfo.update(dUpdate)
    oPerform.SetArgValue(iNpc, dNpcInfo)

