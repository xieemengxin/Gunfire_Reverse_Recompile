# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/commonative/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/commonative/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_only import Time2Frame, ShufferList
from cl_commondefines import STATE_TIME_LIMIT, TOXIC_FOG
from cl_object.logging import DeviceLog
from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON
import cl_object
import cl_state
import cl_msgcenter
import cl_item.load
import cl_action

def CommonAddToxicCount(oTarget, iAttack, dCustomData):
    if not oTarget:
        return None
    oGame = oTarget.m_Game
    oAttack = oGame.GetObject(iAttack)
    if not oAttack:
        return None
    oPerform = oAttack.GetPerform(TOXIC_FOG)
    if not oPerform:
        return None
    iToxicStateSID = dCustomData['ToxicStateSID'] if 'ToxicStateSID' in dCustomData else oPerform.GetArgValue('ToxicStateSID', 0)
    iToxicTime = dCustomData['ToxicTime'] if 'ToxicTime' in dCustomData else oPerform.GetArgValue('ToxicTime', 0)
    iAddCount = dCustomData['AddCount'] if 'AddCount' in dCustomData else oPerform.GetArgValue('AddCount', 0)
    iFrame = Time2Frame(iToxicTime)
    dInfo = {
        'VID': oTarget.m_ID,
        'AddCount': iAddCount }
    oTargetState = oTarget.m_State.GetItemBySource(iToxicStateSID, iAttack)
    if not oTargetState:
        dStateData = {
            'AID': iAttack,
            'RS': cl_object.reason.CStrReason('PF7204-AddToxicCount'),
            'arg': { } }
        oTargetState = cl_state.AddState(oTarget, iToxicStateSID, STATE_TIME_LIMIT, iFrame, dStateData)
        if not oTargetState:
            lstAllPerform = oTarget.m_Perform.GetAllPerformSID()
            lstAllState = oTarget.m_State.GetAllStateSID()
            DeviceLog.Alert('%s %s Not ToxicState %s, AllPerform: %s, AllState: %s' % (oGame.m_ID, oTarget.m_SID, iToxicStateSID, lstAllPerform, lstAllState))
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, oAttack, dInfo, oGame = oGame)
        iAddCount = dInfo['AddCount']
        oTargetState.AddCount(oTarget, iAddCount, iFrame)
        oTargetState.Enable(oTarget)
        if oTarget.IsDead():
            return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_TOXICSTATE_COUNT, oAttack, dInfo, oGame = oGame)
    iAddCount = dInfo['AddCount']
    iNowCount = oTargetState.GetCount()
    iMaxCount = dCustomData['MaxCount'] if 'MaxCount' in dCustomData else oPerform.CalAttr('CommonMaxCount')
    if iNowCount >= iMaxCount:
        oTargetState.AddLimitCount(oTarget, iAddCount, iFrame, iAddCount)
    else:
        iCanAddCount = iMaxCount - iNowCount
        iRefreshCount = iAddCount - iCanAddCount
        if iCanAddCount < iAddCount:
            iAddCount = iCanAddCount
        oTargetState.AddCount(oTarget, iAddCount, iFrame)
        if iRefreshCount > 0:
            oTargetState.AddLimitCount(oTarget, iRefreshCount, iFrame, iRefreshCount)
    dMsgInfo = {
        'VID': oTarget.m_ID,
        'AddCount': iAddCount,
        'CurHitPos': dCustomData['CurHitPos'] if 'CurHitPos' in dCustomData else oTarget.GetPos() }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_AFTER_ADD_TOXICSTATECOUNT, oAttack, dMsgInfo, oGame = oGame)
    if oTarget.IsDead():
        return None
    iNeedAddEasilyInjure = dCustomData['NeedAddEasilyInjure'] if 'NeedAddEasilyInjure' in dCustomData else oPerform.GetArgValue('NeedAddEasilyInjure', 0)
    if iNeedAddEasilyInjure:
        iEasilyInjureStateSID = oPerform.GetArgValue('EasilyInjureState', 0)
        dArgs = {
            'AID': iAttack,
            'RS': cl_object.reason.CStrReason('PF7204-AddToxicCount-EasilyInjureState'),
            'arg': {
                'ToxicCount': oTargetState.GetCount() } }
        cl_state.AddFollowState(oTarget, oTargetState, iEasilyInjureStateSID, STATE_TIME_LIMIT, iFrame, dArgs)


def Custom1910CostBullet(oWarrior, oSkill, oWeapon):
    iCurBulletType = 0
    if oWeapon.m_Type != EQUIP_TYPE_FUNDAMENTALWEAPON:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if oBulletCom:
            iCurBulletType = oBulletCom.m_BulletType
    oComPerform = oWeapon.GetComponent('Perform')
    oAttPerfom = oComPerform.GetPerform(oComPerform.GetAttPerform())
    if not oAttPerfom:
        return None
    sKey = oSkill.m_Base['PFKey']
    oBulletCon = oWarrior.m_BulletCon
    iCostBullet = oAttPerfom.m_BulletUse
    tAllBulletType = cl_item.load.GetAllWeaponBulletType()
    for iBulletType in ShufferList(oWarrior.m_Game, tAllBulletType):
        if iBulletType == iCurBulletType:
            continue
        iHasBullet = oBulletCon.Bullet(iBulletType)
        if iHasBullet:
            iTrueCost = iCostBullet if iHasBullet >= iCostBullet else iHasBullet
            oBulletCon.BulletModify(iBulletType, -iTrueCost, sKey)
            iCostBullet -= iTrueCost
        if iCostBullet <= 0:
            break
    
    if iCurBulletType:
        iHasBullet = oBulletCon.Bullet(iCurBulletType)
        if iHasBullet < iCostBullet:
            iCostBullet = iHasBullet
        oBulletCon.BulletModify(iCurBulletType, -iCostBullet, sKey)


def Custom50101Dam(oSkill):
    oDevice = oSkill.GetAttack()
    if not oDevice:
        return None
    iResultCount = oDevice.Query('AllTocixCount')
    iBaseDam = oDevice.QueryAttr('Att')
    dArgs = {
        'Att': iBaseDam * iResultCount }
    cl_action.PerformDamage(oSkill, dArgs)

