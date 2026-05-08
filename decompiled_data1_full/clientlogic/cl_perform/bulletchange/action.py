# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/action.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/action.pyc
# Source Generated with Decompyle++
# File: action.pyc (Python 3.6)

from cl_commondefines import BULLET_CBMETHOD_COSTWEAPONBULLET, BULLET_CBMETHOD_COSTBAGBULLET, STATE_TIME_LIMIT, STATE_TIME_FOREVER, BULLET_CBMETHOD_REVERT, OBJ_ATTACK, BULLET_CBMETHOD_SRVSTATE, OBJ_VICTIM, BULLET_CBMETHOD_TRIGROUP, BULLET_CBMETHOD_SETCOLLECT, BULLET_CBMETHOD_EXTUSE, BULLET_CBMETHOD_FILL, BULLET_CBMETHOD_SRVSTATECNT, BULLET_CBMETHOD_REVERTBAG, PF_TYPE_CHARGE, BULLET_CBMETHOD_SRVSTATE, BULLET_CBMETHOD_INFINITEFIRE, BULLET_CBMETHOD_REVERTPFBULLET, BULLET_CBMETHOD_COSTPFBULLET, PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, REASON_COSTBULLET_BULLETCHANGE
from cl_only import Time2Frame
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
import cl_formula
import cl_object
import cl_snetwar
import cl_state
import cl_item.defines as itemdef
import cl_hero

def CheckBulletRevert(oWarrior, oWeapon, iFillValue):
    if not oWeapon:
        return False
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return False
    iMaxBullet = oBulletCom.MaxBullet()
    iNowBullet = oBulletCom.Bullet()
    if iNowBullet >= iMaxBullet:
        return False
    return iFillValue > 0


def CheckBulletFill(oWarrior, oWeapon, iFillValue):
    if not oWeapon:
        return False
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return False
    iMaxBullet = oBulletCom.MaxBullet()
    iNowBullet = oBulletCom.Bullet()
    iBulletSID = oBulletCom.BulletType()
    iBagBullet = oWarrior.m_BulletCon.Bullet(iBulletSID)
    if iFillValue > iBagBullet or iFillValue > iMaxBullet - iNowBullet:
        return False
    return True


def BulletChangeFillSourceWeaponBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowFillValue):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_FILL)
    if tkey not in dClientInfo:
        return None
    if 'ItemID' not in dClientInfo[tkey] or 'BulletVal' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iFillValue = dClientInfo[tkey]['BulletVal']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not CheckBulletFill(oWarrior, oWeapon, iFillValue):
        if oWeapon:
            oBulletCom = oWeapon.GetComponent('Bullet')
            oBulletCom.RefreshCurBullet()
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    iBulletSID = oBulletCom.BulletType()
    oWarrior.m_BulletCon.BulletModify(iBulletSID, -iFillValue, 'fillbullet')
    oBulletCom.BulletModify(iFillValue, 1)


def BulletChangeExtBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowExtBulletUse):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_EXTUSE)
    if tkey not in dClientInfo:
        return None
    if 'BulletVal' not in dClientInfo[tkey]:
        return None
    iExtBulletUse = dClientInfo[tkey]['BulletVal']
    if 'ExtBulletUse' not in oSkill.m_Collect:
        oSkill.m_Collect['ExtBulletUse'] = 0
    oSkill.m_Collect['ExtBulletUse'] += iExtBulletUse


def BulletChangeReduceBulletUse(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowBehavior):
    oSkill.m_Collect['NoBulletUse'] = 1


def BulletChangeSetCollectInfo(oWarrior, pfBulletChange, oSkill, dClientInfo, sShowAttr, iShowAdd, iShowMul):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_SETCOLLECT)
    if tkey not in dClientInfo:
        return None
    for sAttr, iVal in dClientInfo[tkey].items():
        oSkill.m_Collect[sAttr] = iVal
    


def BulletChangeWeaponInfiniteFire(oWarrior, pfBulletChange, oSkill, dClientInfo):
    lstWeapon = oWarrior.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        oComPerform = oWeapon.GetComponent('Perform')
        iMinorPerformSID = oComPerform.GetMinorPerform()
        pfobj = oComPerform.GetPerform(iMinorPerformSID)
        if pfobj and pfobj.m_PFType == PF_TYPE_CHARGE:
            oWeapon.SetTmp('InfiniteFire', 1)
    
    pfBulletChange.AddExtDisableFunc(BULLET_CBMETHOD_INFINITEFIRE)


def BulletChangeRevertBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowFillVal, iShowBehavior):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_REVERT)
    if tkey not in dClientInfo:
        return None
    if 'BulletVal' not in dClientInfo[tkey] or 'ItemID' not in dClientInfo[tkey]:
        return None
    iFill = dClientInfo[tkey]['BulletVal']
    iItemID = dClientInfo[tkey]['ItemID']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not CheckBulletRevert(oWarrior, oWeapon, iFill):
        if oWeapon:
            oBulletCom = oWeapon.GetComponent('Bullet')
            oBulletCom.RefreshCurBullet()
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    oBulletCom.BulletModify(iFill, 0)


def BulletChangeFillBullet(oWarrior, pfBulletChange, oSkill, dClientInfo):
    sKey = pfBulletChange.Key()
    oBulletCon = oWarrior.m_BulletCon
    lstWeapon = oWarrior.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        iBulletSID = oBulletCom.BulletType()
        iAmount = oBulletCom.MaxBullet() - oBulletCom.Bullet()
        iHasBullet = oBulletCon.Bullet(iBulletSID)
        iAmount = min(iAmount, iHasBullet)
        oBulletCon.BulletModify(iBulletSID, -iAmount, sKey)
        oBulletCom.BulletModify(iAmount, 0)
    


def BulletChangeCBAddClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowStateSID, iShowTime, iShowCount, iShowMove):
    pass


def BulletChangeCBDelClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowStateSID):
    pass


def BulletChangeCBTriggerGroup(oWarrior, pfBulletChange, oSkill, dClientInfo, dShowWeight):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_TRIGROUP)
    if tkey not in dClientInfo:
        return None
    if 'Seed' not in dClientInfo[tkey]:
        return None
    iSeed = dClientInfo[tkey]['Seed']
    for iGroup, iWeight in dShowWeight.items():
        if iSeed >= iWeight:
            continue
        dCBFunc = pfBulletChange.m_CBFuncAction
        func = dCBFunc[iGroup] if iGroup in dCBFunc else None
        if func:
            func(oWarrior, pfBulletChange, oSkill, dClientInfo)
    


def BulletChangeCBAddStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, iStateSID, iCount):
    pass


def BulletChangeCBOwnerDamage(oWarrior, pfBulletChange, oSkill, dClientInfo, iValue, iDamType, iShowTips, iSendMsg, iPlaySound = 1):
    iAttack = oWarrior.m_ID
    iDamage = cl_formula.GetResultByData(oWarrior, iValue, { }, {
        'AID': iAttack })
    oReason = cl_object.reason.CPerformReason(pfBulletChange.m_SID, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, {
        'ShowTips': iShowTips,
        'DamType': iDamType,
        'ExInfo': iPlaySound })
    lstDam = [
        (iDamage, oReason)]
    dDamage = {
        'AID': iAttack,
        'CurVID': iAttack,
        'MainDam': lstDam,
        'FlowDam': [],
        'RS': oReason,
        'DamFactor': {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } } }
    oWarrior.ReceiveDamage(iAttack, dDamage, iSendMsg)


def BulletChangeCBOwnerCure(oWarrior, pfBulletChange, oSkill, dClientInfo, iValue, iCurType, iShowTips):
    iCure = cl_formula.GetResultByData(oWarrior, iValue, { })
    if not iCure:
        return None
    oReason = cl_object.reason.CPerformReason(pfBulletChange.m_SID, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, {
        'ShowTips': iShowTips,
        'DamType': iCurType })
    lstCure = [
        [
            iCure,
            oReason]]
    dCure = {
        'MainCure': lstCure,
        'FlowCure': [],
        'RS': oReason }
    oWarrior.ReceiveCure(oWarrior.m_ID, dCure)


def BulletChangeCBOwnerClientBehavior(oWarrior, pfBulletChange, oSkill, dClientInfo, iBehavior, iStop = 0):
    iAttack = oWarrior.m_ID
    iPlayer = oWarrior.m_PlayerID
    cl_snetwar.GS2CTriggerBehavior(oWarrior.m_Game, iAttack, iBehavior, [
        iPlayer], iStop)


def BulletChangeCBResetClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, iStateSID):
    pass


def BulletChangeCBSummaryFireInfo(oWarrior, pfBulletChange, oSkill, dClientInfo):
    pass


def BulletChangeAddServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, iStateSID, iTime, iCloseRemove, iCount = 0):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_SRVSTATE)
    if tkey not in dClientInfo:
        return None
    if 'Seed' in dClientInfo[tkey]:
        iCount = dClientInfo[tkey]['Seed']
    oReason = cl_object.reason.CPerformReason(pfBulletChange.m_SID, oWarrior.m_ID, oWarrior.m_SID, oWarrior.m_FightType, None, { })
    dArgs = {
        'AID': oWarrior.m_ID,
        'RS': oReason,
        'pfid': pfBulletChange.m_SID,
        'PFLV': pfBulletChange.m_Level,
        'arg': { } }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oWarrior, iTime, { })
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oWarrior, iStateSID, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    if iCount:
        oState.SetCount(oWarrior, iCount)
    oState.Enable(oWarrior)
    if iCloseRemove:
        iStateID = oState.m_ID
        pfBulletChange.AddExtDisableFunc(BULLET_CBMETHOD_SRVSTATE, iStateID)


def BulletChangeAddServerStateCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, iStateSID, iAdd, iTime):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_SRVSTATECNT)
    if tkey not in dClientInfo:
        return None
    iAddCount = cl_formula.GetResultByData(oWarrior, iAdd, { })
    iTime = cl_formula.GetResultByData(oWarrior, iTime, { })
    oState = oWarrior.m_State.GetItemBySID(iStateSID)
    if oState:
        oState.AddCount(oWarrior, iAddCount)
        if iTime:
            cl_state.AddTime(oState, oWarrior, Time2Frame(iTime), Time2Frame(iTime))


def BulletChangeCBCostBagBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowExtBulletUse):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_COSTBAGBULLET)
    if tkey not in dClientInfo:
        return None
    if 'ItemID' not in dClientInfo[tkey] or 'BulletVal' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iCostValue = dClientInfo[tkey]['BulletVal']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oBulletCon = oWarrior.m_BulletCon
    iBulletSID = oWeapon.GetBulletType()
    iHasBullet = oBulletCon.Bullet(iBulletSID)
    iAmount = iHasBullet if iCostValue > iHasBullet else iCostValue
    if 'ExtShootBulletUse' in oSkill.m_Collect:
        oSkill.m_Collect['ExtShootBulletUse'] += iAmount
    else:
        oSkill.m_Collect['ExtShootBulletUse'] = iAmount
    oBulletCon.BulletModify(iBulletSID, -iAmount, REASON_COSTBULLET_BULLETCHANGE, 1, 0, oWeapon.IsInitWeapon())


def BulletChangeRevertBulletBag(oWarrior, pfBulletChange, oSkill, dClientInfo):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_REVERTBAG)
    if tkey not in dClientInfo:
        return None
    if 'ItemID' not in dClientInfo[tkey] or 'BulletVal' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iFill = dClientInfo[tkey]['BulletVal']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oBulletCon = oWarrior.m_BulletCon
    iBulletSID = oWeapon.GetBulletType()
    oBulletCon.BulletModify(iBulletSID, iFill, REASON_COSTBULLET_BULLETCHANGE, 1, 0)


def BulletChangeCBCostWeaponBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iShowExtBulletUse):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_COSTWEAPONBULLET)
    if tkey not in dClientInfo:
        return None
    if 'ItemID' not in dClientInfo[tkey] or 'BulletVal' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iCostValue = dClientInfo[tkey]['BulletVal']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if 'ExtShootBulletUse' in oSkill.m_Collect:
        oSkill.m_Collect['ExtShootBulletUse'] += iCostValue
    else:
        oSkill.m_Collect['ExtShootBulletUse'] = iCostValue
    oBulletCom.BulletModify(-iCostValue, 0)


def GetRevertPFBulletByFightType(oWarrior, oSkill, oPerform):
    oEquip = oPerform.m_Container.m_Equip
    iAddValue = 0
    if oEquip and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        for dCartoon in oSkill.m_Cartoon.values():
            dClient = oSkill.m_NetReceive.get(dCartoon.get('ID', 0), { })
            lstRay = dClient.get('Ray', [])
            if lstRay:
                break
        
        oGame = oWarrior.m_Game
        for _, _, iVictim, _ in lstRay:
            oVictim = oGame.GetObject(iVictim)
            if not oVictim:
                continue
            for iType, iCnt in oEquip.m_RevertPFBullet.items():
                if oVictim.m_FightType & iType == iType:
                    iAddValue += iCnt
            
        
    return iAddValue


def BulletChangeCBRevertPFBulletByFightType(oWarrior, pfBulletChange, oSkill, dClientInfo, iTimes):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_REVERTPFBULLET)
    if tkey not in dClientInfo or 'ItemID' not in dClientInfo[tkey] or 'PerformSID' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iPerformSID = dClientInfo[tkey]['PerformSID']
    oPerform = oWarrior.GetPerform(iPerformSID, iItemID)
    if not oPerform:
        return None
    iAddValue = GetRevertPFBulletByFightType(oWarrior, oSkill, oPerform)
    oPerform.AddPFBullet(iAddValue * iTimes, 0)


def BulletChangeCBRevertPFBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iAdd, iTimes):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_REVERTPFBULLET)
    if tkey not in dClientInfo or 'ItemID' not in dClientInfo[tkey] or 'PerformSID' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iPerformSID = dClientInfo[tkey]['PerformSID']
    oPerform = oWarrior.GetPerform(iPerformSID, iItemID)
    if oPerform and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        iAddValue = cl_formula.GetResultByData(oWarrior, iAdd, { })
        oPerform.AddPFBullet(iAddValue * iTimes, 0)


def BulletChangeCBCostPFBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iCost):
    oSkill.m_Collect['Sync'] = 0


def AddDualPFBullet(oWarrior, iPerform, iAddValue):
    oItemCon = oWarrior.m_WieldCon
    lstItem = oItemCon.GetHoldWeapon()
    for tItem in lstItem:
        (oItem, _) = tItem
        oPerformCom = oItem.GetComponent('Perform')
        if not oPerformCom:
            continue
        oCurPerform = oPerformCom.GetPerform(iPerform)
        if not oCurPerform:
            continue
        oCurPerform.AddPFBullet(iAddValue, 0)
    


def BulletChangeCBRevertDualPFBulletByFightType(oWarrior, pfBulletChange, oSkill, dClientInfo, iTimes):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_REVERTPFBULLET)
    if tkey not in dClientInfo or 'ItemID' not in dClientInfo[tkey] or 'PerformSID' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iPerformSID = dClientInfo[tkey]['PerformSID']
    oPerform = oWarrior.GetPerform(iPerformSID, iItemID)
    if not oPerform:
        return None
    iAddValue = GetRevertPFBulletByFightType(oWarrior, oSkill, oPerform) * iTimes
    AddDualPFBullet(oWarrior, iPerformSID, iAddValue)


def BulletChangeCBRevertDualPFBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iAdd, iTimes):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_REVERTPFBULLET)
    if tkey not in dClientInfo or 'PerformSID' not in dClientInfo[tkey]:
        return None
    iPerformSID = dClientInfo[tkey]['PerformSID']
    iAddValue = cl_formula.GetResultByData(oWarrior, iAdd, { }) * iTimes
    AddDualPFBullet(oWarrior, iPerformSID, iAddValue)


def BulletChangeCBCostDualPFBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iCost):
    oSkill.m_Collect['Sync'] = 0
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBMETHOD_COSTPFBULLET)
    if tkey not in dClientInfo or 'ItemID' not in dClientInfo[tkey] or 'PerformSID' not in dClientInfo[tkey]:
        return None
    iItemID = dClientInfo[tkey]['ItemID']
    iPerformSID = dClientInfo[tkey]['PerformSID']
    oItemCon = oWarrior.m_WieldCon
    oCurItem = oItemCon.GetItemByID(iItemID)
    lstItem = oItemCon.GetHoldWeapon()
    for tItem in lstItem:
        (oItem, _) = tItem
        if oItem.m_ID == oCurItem.m_ID:
            continue
        oPerformCom = oItem.GetComponent('Perform')
        if not oPerformCom:
            continue
        oCurPerform = oPerformCom.GetPerform(iPerformSID)
        if not oCurPerform:
            continue
        if 'PFBulletUse' in oCurPerform.m_Attr:
            iCostValue = oCurPerform.CalAttr('PFBulletUse')
        oCurPerform.CostPFBullet(iCostValue, 0)
    


def BulletChangeListenSnapshotMsg(oWarrior, pfBulletChange, iMsg, iSub, iGroup, iOnce, iPriority):
    pfBulletChange.AddCBGroupFunc(iMsg, iSub, iGroup)


def BulletChangeListenMsgCallBack(oWarrior, pfBulletChange, iMsg, iSub, iGroup, iOnce, iPriority):
    pfBulletChange.AddCBGroupFunc(iMsg, iSub, iGroup)


def BulletChangeDirectEventCBFunc(oWarrior, pfBulletChange, iGroup):
    dCBFunc = pfBulletChange.m_CBFuncAction
    func = dCBFunc[iGroup] if iGroup in dCBFunc else None
    if func:
        func(oWarrior, pfBulletChange, None, { })


def BulletChangeAddClientState(oWarrior, pfBulletChange, iShowStateSID, iShowTime, iShowCount, iShowMove):
    pass


def BulletChangeThrowInfiniteFire(oWarrior, pfBulletChange, iOpen):
    dHero2HeroThrow = cl_hero.load.GetHero2HeroThrow()
    for iPerformSID in dHero2HeroThrow[oWarrior.m_SID]:
        oPerform = oWarrior.GetPerform(iPerformSID)
        if not oPerform:
            continue
        oPerform.m_IgnoreBulletJudge = iOpen
    


def BulletChangeCBSetSkillCacheChange(oWarrior, pfBulletChange, oSkill, dClientInfo, sAttr, iAdd, iMul):
    dCache = oSkill.m_Cache
    if sAttr not in dCache:
        return None
    iAdd = cl_formula.GetResultByData(oWarrior, iAdd, { }, {
        'Skill': oSkill })
    iMul = cl_formula.GetResultByData(oWarrior, iMul, { }, {
        'Skill': oSkill })
    sKey = 'CacheChange-%s' % sAttr
    dVarCache = oSkill.m_VarCache
    if sKey not in dVarCache:
        iBaseValue = dCache[sAttr]
        iSumAdd = iAdd
        iSumMul = iMul
    else:
        (iBaseValue, iSumAdd, iSumMul) = dVarCache[sKey]
        iSumAdd += iAdd
        iSumMul += iMul
    dVarCache[sKey] = (iBaseValue, iSumAdd, iSumMul)
    dCache[sAttr] = (iBaseValue + iSumAdd) * (10000 + iSumMul) // 10000


def BulletChangeCBChangeBagBullet(oWarrior, pfBulletChange, oSkill, dClientInfo, iBullet, iAmount):
    iAmount = cl_formula.GetResultByData(oWarrior, iAmount, { }, {
        'Skill': oSkill })
    if iAmount < 0:
        iHasBullet = oWarrior.m_BulletCon.Bullet(iBullet)
        if iHasBullet + iAmount < 0:
            iAmount = 0 - iHasBullet
    oWarrior.m_BulletCon.BulletModify(iBullet, iAmount, pfBulletChange.Key())


def BulletChangeCBChangeSkillDamFactor(oWarrior, pfBulletChange, oSkill, dClientInfo, iAdd, iMul, iMask, iTransmit):
    sKey = pfBulletChange.Key()
    dFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
    dFactor[sKey] = (iAdd, iMul, iMask)
    oSkill.m_Collect['DamFactor'] = dFactor
    if iTransmit == 1:
        dTransFactor = oSkill.m_Custom['TransDamFactor'] if 'TransDamFactor' in oSkill.m_Custom else { }
        dTransFactor[sKey] = (iAdd, iMul, iMask)
        oSkill.m_Custom['TransDamFactor'] = dTransFactor

