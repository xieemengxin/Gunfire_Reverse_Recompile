# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_passive.pyc
# RelativePath: clientlogic/cl_action/ac_passive.pyc
# Source Generated with Decompyle++
# File: ac_passive.pyc (Python 3.6)

from cl_only import Time2Frame, SendAlert, Functor
from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER, TYPE_PASSIVE_TIME_CD
from cl_commondefines import PF_TYPE_INSCRIPTION, INSCRIPTION_TYPE_GEMINI, DISABLE_TYPE_STATE, DISABLE_TYPE_BULLET, SUIT_HANDLE_DAMAGEFACTOR, WAND_COMP_TYPE_CONDITION
import cl_formula
import cl_state
import cl_item.defines as itemdef
import cl_object.linkattr as linkattr
import cl_snetwar

def PassiveAddState(oTarget, oLifeCycle, iState, iTime, dArgs, iCloseRemove):
    dData = {
        'LifeCycle': oLifeCycle }
    dRet = cl_formula.CalArgsFormula(oTarget, dArgs, dData)
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        if not iCloseRemove:
            SendAlert('err', f'''{oLifeCycle}被动销毁仍添加非跟随对象的状态''')
        return None
    dArgs = {
        'AID': oTarget.m_ID,
        'RS': oTarget.AttReason(pfobj, 0),
        'pfid': pfobj.m_SID,
        'PFLV': pfobj.GetLifeCycleLevel(),
        'arg': dRet }
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oTarget, iTime, dData)
    else:
        iTimeType = STATE_TIME_FOREVER
    oState = cl_state.AddState(oTarget, iState, iTimeType, Time2Frame(iTime), dArgs)
    if not oState:
        return None
    oState.Enable(oTarget)
    if iCloseRemove:
        oLifeCycle.AddDisableType(DISABLE_TYPE_STATE, {
            oTarget.m_ID: oState.m_ID })


def PassiveChangeSourceWeaponAttr(oTarget, oLifeCycle, sAttr, iAdd, iMul):
    pfobj = oLifeCycle.GetObject()
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData, { }, {
        'Weapon': oWeapon })
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData, { }, {
        'Weapon': oWeapon })
    if iMul or iAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey)
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
    elif (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
        oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
    oWeapon.AttrClear(sAttr, sKey)


def PassiveChangeSourceWeaponPerformAttr(oTarget, oLifeCycle, iPerform, sAttr, iAdd, iMul):
    
    def ClearChange(oTarget, oLifeCycle):
        oPerform.AttrClear(sAttr, sKey)

    pfobj = oLifeCycle.GetObject()
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return None
    sKey = oLifeCycle.Key()
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData)
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData)
    if iMul or iAdd:
        oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
        oLifeCycle.AddDisableFunc(ClearChange)
    else:
        oPerform.AttrClear(sAttr, sKey)


def PassiveSubSourceWeaponPointPerformColdTime(oTarget, oLifeCycle, iPerform, iTime, iPercent):
    pfobj = oLifeCycle.GetObject()
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerformCon = oPerformCom.m_Perform
    if not oPerformCon:
        return None
    iColdTimeFrame = oPerformCon.GetTotalColdTime(iPerform)
    if not iColdTimeFrame:
        return None
    iFrame = Time2Frame(iTime)
    if iPercent:
        iMaxColdTimeFrame = oPerformCon.GetMaxColdTime(iPerform)
        iFrame += iMaxColdTimeFrame * iPercent // 100
    oPerformCon.ModifyColdTime(iPerform, -iFrame)
    oPerform.ModifyNextAttackFrame(-iFrame)


def PassiveSetSelfColdTime(oTarget, oLifeCycle, iCDTime):
    iTime = cl_formula.GetResultByData(oTarget, iCDTime, {
        'LifeCycle': oLifeCycle })
    iFrame = Time2Frame(iTime)
    if iFrame > 0:
        pfobj = oLifeCycle.GetObject()
        pfobj.SetCDTime(oTarget, iFrame)


def PassiveSubSelfColdTime(oTarget, oLifeCycle, iCDTime):
    pfobj = oLifeCycle.GetObject()
    if not pfobj.InColdTime():
        return None
    iTime = cl_formula.GetResultByData(oTarget, iCDTime, {
        'LifeCycle': oLifeCycle })
    iFrame = Time2Frame(iTime)
    if iFrame > 0:
        pfobj.ModifyColdTime(oTarget, -iFrame)


def PassiveAddSourceWeaponBagBullet(oTarget, oLifeCycle, iAmount):
    pfobj = oLifeCycle.GetObject()
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    sKey = oLifeCycle.Key()
    iAmount = cl_formula.GetResultByData(oTarget, iAmount, {
        'LifeCycle': oLifeCycle })
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iBulletSID = oBulletCom.BulletType()
    oTarget.m_BulletCon.BulletModify(iBulletSID, iAmount, sKey)


def PassiveSetLinkAttr(oTarget, oLifeCycle, sAttr, fMaxValue = 0):
    
    def ClearLinkAttr(oTarget, oLifeCycle):
        pfobj = oLifeCycle.GetObject()
        oWeapon = pfobj.GetMyItem()
        oOtherWeapon = None
        oCon = oTarget.m_WieldCon
        lstPos = oCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
        for iPos in lstPos:
            oOtherWeapon = oCon.GetItem(iPos)
            if oOtherWeapon and oOtherWeapon.m_ID != oWeapon.m_ID:
                break
        
        oLinkAttr = oWeapon.GetItemAttr(sAttr)
        oSelfAttr = oLinkAttr.DelLink(oWeapon.m_ID)
        oConnectAttr = oLinkAttr.DelLink(oOtherWeapon.m_ID)
        oWeapon.DirectSetAttr(sAttr, oSelfAttr)
        oOtherWeapon.DirectSetAttr(sAttr, oConnectAttr)

    pfobj = oLifeCycle.GetObject()
    if pfobj.m_PFType != PF_TYPE_INSCRIPTION or pfobj.m_InscriptionType != INSCRIPTION_TYPE_GEMINI:
        return None
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oOtherWeapon = None
    oCon = oTarget.m_WieldCon
    lstPos = oCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
    for iPos in lstPos:
        oOtherWeapon = oCon.GetItem(iPos)
        if oOtherWeapon and oOtherWeapon.m_ID != oWeapon.m_ID:
            break
    
    if not oOtherWeapon:
        return None
    oSelfAttr = oWeapon.GetItemAttr(sAttr)
    oConnectAttr = oOtherWeapon.GetItemAttr(sAttr)
    if oSelfAttr and oConnectAttr and oSelfAttr.m_Type != 'Link' and oConnectAttr.m_Type != 'Link':
        oLinkAttr = linkattr.CLinkAttr()
        oLinkAttr.AddLink(oWeapon.m_ID, oSelfAttr)
        oLinkAttr.AddLink(oOtherWeapon.m_ID, oConnectAttr)
        if fMaxValue:
            oLinkAttr.SetMaxValue(fMaxValue)
        oWeapon.DirectSetAttr(sAttr, oLinkAttr)
        oOtherWeapon.DirectSetAttr(sAttr, oLinkAttr)
        oLifeCycle.AddDisableFunc(ClearLinkAttr)


def PassiveSetLinkPFBulletAttr(oTarget, oLifeCycle, iLinkMul):
    
    def ClearLinkAttr(dLinkPerform, oTarget, oLifeCycle):
        for iWeapon, iPerform in dLinkPerform.items():
            oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
            if not oWeapon:
                continue
            oPerformCom = oWeapon.GetComponent('Perform')
            if not oPerformCom:
                continue
            oPerform = oPerformCom.GetPerform(iPerform)
            if not oPerform:
                continue
            oLinkAttr = oPerform.GetAttr(sAttr)
            if oLinkAttr.m_Type == 'Link':
                oAttr = oLinkAttr.DelLink(oPerform.m_ID)
                oPerform.DirectSetAttr(sAttr, oAttr)
        

    pfobj = oLifeCycle.GetObject()
    if pfobj.m_PFType != PF_TYPE_INSCRIPTION or pfobj.m_InscriptionType != INSCRIPTION_TYPE_GEMINI:
        return None
    oCurWeapon = pfobj.GetMyItem()
    if not oCurWeapon or not (oCurWeapon.Type() & itemdef.EQUIP_TYPE_MAINWEAPON):
        return None
    sAttr = 'MaxPFBullet'
    dLinkPerform = { }
    dLinkPerformAttr = { }
    for oWeapon in oTarget.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON):
        oPerform = oWeapon.GetPFBulletPerform()
        if not oPerform:
            return None
        oAttr = oPerform.GetAttr(sAttr)
        if oAttr.m_Type == 'Link':
            return None
        dLinkPerformAttr[oWeapon.m_ID] = (oPerform, oAttr)
        dLinkPerform[oWeapon.m_ID] = oPerform.m_SID
    
    oLinkAttr = linkattr.CLinkPFAttr()
    if iLinkMul:
        oLinkAttr.SetLinkMul(iLinkMul)
    for iWeapon, (oPerform, oAttr) in dLinkPerformAttr.items():
        oLinkAttr.AddLink(oPerform.m_ID, oAttr, tKey = (iWeapon, oPerform.m_SID))
    
    for oPerform, _ in dLinkPerformAttr.values():
        oPerform.DirectSetAttr(sAttr, oLinkAttr)
    
    oClearFunc = Functor(ClearLinkAttr, dLinkPerform)
    oLifeCycle.AddDisableFunc(oClearFunc)


def PassiveCloseLinkPerform(oTarger, oLifeCycle):
    oWieldCon = oTarger.m_WieldCon
    lstPos = oWieldCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
    pfobj = oLifeCycle.GetObject()
    if pfobj.m_PFType != PF_TYPE_INSCRIPTION or pfobj.m_InscriptionType != INSCRIPTION_TYPE_GEMINI:
        return None
    iPerform = pfobj.m_SID
    for iPos in lstPos:
        oWeapon = oWieldCon.GetItem(iPos)
        oPerformCom = oWeapon.GetComponent('Perform')
        oPerform = oPerformCom.GetPerform(iPerform)
        if not oPerform:
            continue
        oPerform.Disable(oTarger)
    


def PassiveCycleExecCBFuncAction(oTarget, oLifeCycle, iFirstTime, iCycleTime, iGroup):
    pfobj = oLifeCycle.GetObject()
    if iGroup not in pfobj.m_EventCB.m_CBFuncAction:
        return None
    dData = {
        'LifeCycle': oLifeCycle }
    iFirstTime = cl_formula.GetResultByData(oTarget, iFirstTime, dData)
    iCycleTime = cl_formula.GetResultByData(oTarget, iCycleTime, dData)
    iFirstFrame = Time2Frame(iFirstTime)
    iBaseCycleFrame = Time2Frame(iCycleTime)
    iCycleFrame = pfobj.GetCycleTimeChange(iBaseCycleFrame)
    if iBaseCycleFrame and iCycleFrame <= 0:
        SendAlert('err', f'''game:{oTarget.m_Game.m_ID} CycleTime is negative {pfobj.m_FactorInfo}, Perform:{pfobj.m_SID}''')
        return None
    pfobj.SetCycleTime(oTarget, iFirstFrame, iCycleFrame, iBaseCycleFrame, iGroup)


def PassiveChangeCurCycleTime(oTarget, oLifeCycle, iChange):
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        return None
    iChange = cl_formula.GetResultByData(oTarget, iChange, {
        'LifeCycle': oLifeCycle })
    iChangeFrame = Time2Frame(iChange)
    pfobj.UpdateCurCycleTime(oTarget, iChangeFrame)


def PassiveCloseCycleExecCBFuncAction(oTarget, oLifeCycle):
    pfobj = oLifeCycle.GetObject()
    pfobj.DelCycleTime(oTarget)


def PassiveCloseCDExecCBFuncAction(oTarget, oLifeCycle):
    pfobj = oLifeCycle.GetObject()
    pfobj.DelPassTime(oTarget, TYPE_PASSIVE_TIME_CD)


def PassiveEnableBulletChangeRule(oTarget, oLifeCycle, iPerform, iLevel):
    pfobj = oLifeCycle.GetObject()
    iOwnPfid = pfobj.m_ID
    oTarget.m_BulletChangeCon.AddPerform(oTarget, iOwnPfid, iPerform, iLevel, 1, pfobj.m_Item)
    oLifeCycle.AddDisableType(DISABLE_TYPE_BULLET, iPerform, iOwnPfid)


def PassiveDisableBulletChangeRule(oTarget, oLifeCycle, iPerform):
    pfobj = oLifeCycle.GetObject()
    iOwnPfid = pfobj.m_ID
    oTarget.m_BulletChangeCon.RemovePerform(oTarget, iOwnPfid, iPerform)


def PassiveLinkBaseGrade(oTarget, oLifeCycle, iGroup):
    
    def ClearExtGrade(oTarget, oLifeCycle):
        oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oWeapon.ClearExtGrade(sKey)

    pfobj = oLifeCycle.GetObject()
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oOtherWeapon = None
    oCon = oTarget.m_WieldCon
    lstPos = oCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
    iWeapon = oWeapon.m_ID
    for iPos in lstPos:
        oOtherWeapon = oCon.GetItem(iPos)
        if oOtherWeapon and oOtherWeapon.m_ID != iWeapon:
            break
    
    if not oOtherWeapon:
        return None
    sKey = oLifeCycle.Key()
    oWeapon.AddExtGrade(sKey, iGroup, oOtherWeapon.m_BaseGrade)
    oLifeCycle.AddDisableFunc(ClearExtGrade)


def PassiveSetTaskSaveInfo(oTarget, oLifeCycle, sKey, iValue):
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    oTask.SetSaveData(sKey, iValue)


def PassiveAddTaskSaveInfo(oTarget, oLifeCycle, sKey, iAdd):
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    oTask.AddSaveData(sKey, iAdd)


def PassiveGetTaskSaveInfo(oTarget, oLifeCycle, sKey):
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return 0
    return oTask.GetSaveData(sKey)


def PassiveRemoveSelfOnTask(oTarget, oLifeCycle):
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    oTask.RemovePerform(pfobj.m_SID)


def PassiveClearTaskTempDisableInsciption(oWarrior, oLifeCycle):
    pfobj = oLifeCycle.GetObject()
    oTask = pfobj.GetOwnerTask()
    if not oTask:
        return None
    iTask = oTask.m_ID
    lstWeapon = oWarrior.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        sKey = 'DisableInscription-%s-%s' % (iTask, oWeapon.m_ID)
        oInscriptionCom.RemoveTempDisbleInscription(sKey, iRefresh = 1)
    


def PassiveChangeConquerProbability(oTarget, oLifeCycle, iMul):
    
    def ClearChange(oTarget, oLifeCycle):
        oConquerElement.m_ConquerchallengeMgr.ClearConquerProbabilityChanged()

    oConquerElement = oTarget.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        return None
    oConquerElement.m_ConquerchallengeMgr.ChangeConquerProbability(iMul)
    oLifeCycle.AddDisableFunc(ClearChange)


def PassiveSetConquerExtraAttr(oTarget, oLifeCycle, sAttr, iValue, iCommon):
    
    def ClearChange(oTarget, oLifeCycle):
        oConquerElement.m_ConquerchallengeMgr.ClearExtraAttr(sAttr, sKey)

    oConquerElement = oTarget.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        return None
    if iCommon:
        sKey = 'Common'
    else:
        sKey = oLifeCycle.Key()
    oConquerElement.m_ConquerchallengeMgr.SetExtraAttr(sAttr, sKey, iValue)
    oLifeCycle.AddDisableFunc(ClearChange)


def PassiveGetLiteCDRemainTime(oTarget, oLifeCycle):
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        return 0
    return pfobj.GetRemainLiteCD()


def PassiveSendSuitDamageFactor(oTarget, oLifeCycle, iDamageFactor):
    iDamageFactor = cl_formula.GetResultByData(oTarget, iDamageFactor, {
        'LifeCycle': oLifeCycle })
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_DAMAGEFACTOR, [
        iDamageFactor], oTarget.m_Game, oTarget)


def PassiveAddSurvivorExtraReward(oTarget, oLifeCycle, iMiniGame, iChooseCnt):
    oSurvivorElement = oTarget.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if not oSurvivorElement:
        return None
    sKey = oLifeCycle.Key()
    oSurvivorElement.m_UpgradeMgr.AddExtraReward(oTarget, iMiniGame, iChooseCnt, sKey)


def PassiveSetSurvivorChooseAllCnt(oTarget, oLifeCycle, iItemType, iCnt):
    
    def ClearFunc(oTarget, oLifeCycle):
        oSurvivorElement.m_UpgradeMgr.ClearChooseAllCnt(oTarget, iItemType, sKey)

    oSurvivorElement = oTarget.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if not oSurvivorElement:
        return None
    sKey = oLifeCycle.Key()
    oSurvivorElement.m_UpgradeMgr.SetChooseAllCnt(oTarget, iItemType, iCnt, sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def PassiveSetForceReplaceWeaponReward(oTarget, oLifeCycle, iType):
    
    def ClearFunc(oTarget, oLifeCycle):
        dReplaceType[iType].remove(sKey)
        if not dReplaceType:
            dReplaceType.pop(iType)

    dReplaceType = oTarget.SetDefault('ForceReplaceEquip', { })
    if iType not in dReplaceType:
        dReplaceType[iType] = []
    sKey = oLifeCycle.Key()
    dReplaceType[iType].append(sKey)
    oLifeCycle.AddDisableFunc(ClearFunc)


def PassiveSubWandCD(oTarget, oLifeCycle, iTime, iMinLastTime):
    pfobj = oLifeCycle.GetObject()
    oWand = oTarget.m_WandCon.GetWandByID(pfobj.m_Item)
    if not oWand:
        return None
    oWand.SubSpellCD(Time2Frame(iTime), Time2Frame(iMinLastTime))


def PassiveSetSelfArgValue(oTarget, oLifeCycle, sKey, iValue):
    pfobj = oLifeCycle.GetObject()
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    pfobj.SetArgValue(sKey, iValue)

