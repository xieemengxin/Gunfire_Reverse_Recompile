# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4018.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4018.pyc
# Source Generated with Decompyle++
# File: p4018.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import itertools
from cl_commondefines import OBJ_VICTIM, DAM_TYPE_TRUE
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'MaxRadio': 5000,
        'BulletConversion': 100 })


class CPerform(CCustomPerform):
    m_SID = 4018
    m_Name = '1007扣弹减伤'
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


def CustomAction(oWarrior, oEventCB, dArg):
    iMaxRadio = dArg['MaxRadio']
    iBulletConversion = dArg['BulletConversion']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'MainDam' not in dMsgInfo or 'FlowDam' not in dMsgInfo:
        return None
    iItemID = dEventInfo['ItemID']
    if not iItemID:
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    iBulletSID = oBulletCom.BulletType()
    iHasBullet = oWarrior.m_BulletCon.Bullet(iBulletSID)
    if not iHasBullet:
        return None
    iTotalDam = 0
    for iDam, oReason in itertools.chain(dMsgInfo['MainDam'], dMsgInfo['FlowDam']):
        iDamType = oReason.Query('DamType', 0)
        if iDamType & DAM_TYPE_TRUE:
            continue
        iTotalDam += iDam
    
    iReduceDam = iHasBullet * iBulletConversion
    iMaxDam = iTotalDam * iMaxRadio // 10000
    if iReduceDam > iMaxDam:
        iReduceDam = iMaxDam
        iReduceRadio = iMaxRadio
    else:
        iReduceRadio = iReduceDam * 10000 // iTotalDam
    oWarrior.m_BulletCon.BulletModify(iBulletSID, -(iReduceDam // iBulletConversion), dEventInfo['PFKey'])
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -iReduceRadio, 0)

