# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_state.pyc
# RelativePath: clientlogic/cl_action/ac_state.pyc
# Source Generated with Decompyle++
# File: ac_state.pyc (Python 3.6)

from cl_only import Functor, Time2Frame, PY_FLAG_DEAD
from cl_commondefines import STATUS_PUSH, WARRIOR_MONSTER, MOVE_TYPE_NORMAL, FIGHT3_KEY_IGNOREKNOCKBACK, STATE_TIME_LIMIT, STATE_TIME_FOREVER, DEBUG_STATUS_NOPFCD, CURE_TYPE_PERFORM, DAM_USE_ARMOR, DAM_USE_SHIELD, DAM_USE_ALL, DAM_TYPE_PERSISTENCE, DISABLE_TYPE_BULLET
from cl_pxlayer import PXMASK_LIVEOBJ, PXMASK_STATIC
from cl_object.logging import ErrLog
from cl_propdata import BASIC_PROP_NAME
import cl_formula
import cl_action
import cl_msgcenter
import cl_snetwar
import cl_math
import cl_state
import cl_war
import cl_object
import cl_forbid
import cl_item.defines as itemdef

def StateCureByAtive(oTarget, oLifeCycle, iBaseVal, iShowTips, iCurType):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iType = CURE_TYPE_PERFORM | iCurType
    oReason = oState.Reason().ExtInfo({
        'DamType': iType,
        'ShowTips': iShowTips,
        'SourceState': oState.m_SID })
    iVal = cl_formula.GetResultByData(oTarget, iBaseVal, {
        'LifeCycle': oLifeCycle })
    lstMainCure = [
        [
            iVal,
            oReason]]
    dCure = {
        'MainCure': lstMainCure,
        'FlowCure': [],
        'RS': oReason }
    oTarget.ReceiveCure(oState.m_StateInfo['AID'], dCure)


def StateCureStateAttacker(oTarget, oLifeCycle, iBaseVal, iShowTips, iCurType):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oAttacker = oTarget.m_Game.GetObject(oState.m_Attacker)
    if not oAttacker:
        return 0
    StateCureByAtive(oAttacker, oLifeCycle, iBaseVal, iShowTips, iCurType)


def StateReceiveDam(oTarget, oLifeCycle, iDamVal, iElementType, iShowTips, iIgnoreShield = 0, iIgnoreArmor = 0, iPlaySound = 1, iExShowTipsType = 0):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iAttack = oState.m_StateInfo['AID']
    iDamType = iElementType | DAM_TYPE_PERSISTENCE | DAM_USE_ALL
    if iIgnoreShield:
        iDamType &= ~DAM_USE_SHIELD
    if iIgnoreArmor:
        iDamType &= ~DAM_USE_ARMOR
    dReason = {
        'DamType': iDamType,
        'ShowTips': iShowTips,
        'ActNum': 0,
        'ExInfo': iPlaySound,
        'SourceState': oState.m_SID }
    if iExShowTipsType:
        dReason['ExInfo'] = iPlaySound | iExShowTipsType if iPlaySound else iExShowTipsType
    oReason = oState.Reason().ExtInfo(dReason)
    iVal = cl_formula.GetResultByData(oTarget, iDamVal, {
        'LifeCycle': oLifeCycle })
    lstMainDam = [
        [
            iVal,
            oReason]]
    dDamFactor = oState.GetEventDamFactor()
    dState = {
        'MainDam': lstMainDam,
        'RS': oReason,
        'DamFactor': dDamFactor }
    oTarget.ReceiveState(iAttack, dState)


def StateSetPerformColdTime(oTarget, oLifeCycle, iCDTime):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iPerform = oState.GetPerformID()
    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    iTime = cl_formula.GetResultByData(oTarget, iCDTime, {
        'LifeCycle': oLifeCycle })
    iFrame = Time2Frame(iTime)
    if iFrame > 0:
        pfobj.SetCDTime(oTarget, iFrame)


def StatePerformAddColdTime(oTarget, oLifeCycle):
    if oTarget.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD == DEBUG_STATUS_NOPFCD:
        return None
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iPerform = oState.GetPerformID()
    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    oTarget.m_Perform.AddColdTime(iPerform, pfobj.GetCDTime(oTarget))


def StatePerformPauseColdDown(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iPerform = oState.GetPerformID()
    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    oTarget.m_Perform.PauseColdDown(iPerform)


def StatePerformRestartColdDown(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iPerform = oState.GetPerformID()
    pfobj = oTarget.GetPerform(iPerform)
    if not pfobj:
        return None
    oTarget.m_Perform.ReStartColdDown(iPerform)


def StateAddSelfCount(oTarget, oLifeCycle, iAddCount, iCountTime = 0):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iAddCount = cl_formula.GetResultByData(oTarget, iAddCount, {
        'LifeCycle': oLifeCycle })
    if iCountTime:
        iCountTime = cl_formula.GetResultByData(oTarget, iCountTime, {
            'LifeCycle': oLifeCycle })
        oState.AddCount(oTarget, iAddCount, Time2Frame(iCountTime))
    else:
        oState.AddCount(oTarget, iAddCount)


def StateSetSelfCount(oTarget, oLifeCycle, iCount):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iFormulaCount = cl_formula.GetResultByData(oTarget, iCount, {
        'LifeCycle': oLifeCycle })
    iNowCount = oState.GetCount()
    iAddCount = iFormulaCount - iNowCount
    oState.AddCount(oTarget, iAddCount)


def StateGetSelfCount(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return 0
    return oState.GetCount()


def StateListenAttackerMsg(oTarget, oLifeCycle, iMsg, iSub, iGroup):
    
    def ClearOtherEvent(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, iAttacker, iMsg, sKey, iSub)

    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iAttacker = oState.m_StateInfo['AID']
    oAttacker = oTarget.m_Game.GetObject(iAttacker)
    if not oAttacker:
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    sKey = oLifeCycle.Key()
    func = Functor(EventCBAttentionFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iAttacker, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableFunc(ClearOtherEvent)


def EventCBAttentionFunc(oEventCB, iGroup, dEvent, oTarget, oSender, dMsgInfo):
    oEventCB.CBFuncAction(oTarget, iGroup, dEvent, dMsgInfo)


def StateListenAttackerCallBackByAttr(oTarget, oLifeCycle, sAttr, iGroup):
    
    def ClearOtherEvent(oTarget, oLifeCycle):
        cl_msgcenter.DoneAttention(oTarget, iAttacker, iMsg, sKey, iSub)

    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iAttacker = oState.m_StateInfo['AID']
    oAttacker = oTarget.m_Game.GetObject(iAttacker)
    if not oAttacker:
        return None
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    iMsg = cl_msgcenter.MSG_WAR_ATTR_CHANGE
    iSub = BASIC_PROP_NAME[sAttr][0]
    oAttacker.AddRefreshAttr(sAttr)
    sKey = oLifeCycle.Key()
    func = Functor(EventCBAttentionFunc, oLifeCycle.GetObject().m_EventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oTarget, iAttacker, iMsg, func, sKey, iSub)
    oLifeCycle.AddDisableFunc(ClearOtherEvent)


def StateAddState(oTarget, oLifeCycle, iState, iTime, dArgs, iCount = 0):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetResultByData(oTarget, iTime, {
            'LifeCycle': oLifeCycle })
    else:
        iTimeType = STATE_TIME_FOREVER
    dStateArg = { }
    if 'arg' in oState.m_StateInfo:
        dStateArg.update(oState.m_StateInfo['arg'])
    dArgs = cl_formula.CalArgsFormula(oTarget, dArgs, {
        'LifeCycle': oLifeCycle })
    dStateArg.update(dArgs)
    dData = {
        'AID': oState.m_StateInfo['AID'],
        'RS': oState.Reason(),
        'pfid': oState.GetPerformID(),
        'arg': dStateArg }
    oAddState = cl_state.AddState(oTarget, iState, iTimeType, Time2Frame(iTime), dData)
    if not oAddState:
        return None
    oAddState.Enable(oTarget)
    if iCount:
        iCount = cl_formula.GetResultByData(oTarget, iCount, {
            'LifeCycle': oLifeCycle })
        oAddState.AddCount(oTarget, iCount)


def StateChangeSourceWeaponAttr(oTarget, oLifeCycle, sAttr, iAdd, iMul):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    dArgs = {
        'Weapon': oWeapon }
    dData = {
        'LifeCycle': oLifeCycle }
    iMul = cl_formula.GetResultByData(oTarget, iMul, dData, { }, dArgs)
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dData, { }, dArgs)
    sKey = oLifeCycle.Key()
    if iMul or iAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey)
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
    elif (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
        oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
    oWeapon.AttrClear(sAttr, sKey)


def StateChangeSourceWeaponForceAttr(oTarget, oLifeCycle, sAttr, iValue):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iWeapon = oState.m_Item
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle }, { }, {
        'Weapon': oWeapon })
    sKey = oState.Key()
    oLifeCycle.m_ItemApply[(iWeapon, sAttr)] = 1
    oWeapon.ItemAttrForceSet(sAttr, iValue, sKey)


def StateFillSourceWeaponBullet(oTarget, oLifeCycle, iFillValue):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iFillValue = cl_formula.GetResultByData(oTarget, iFillValue, {
        'LifeCycle': oLifeCycle })
    iMaxBullet = oBulletCom.MaxBullet()
    iNowBullet = oBulletCom.Bullet()
    iBulletSID = oBulletCom.BulletType()
    iBagBullet = oTarget.m_BulletCon.Bullet(iBulletSID)
    iFillValue = min(iFillValue, iBagBullet, iMaxBullet - iNowBullet)
    if iFillValue <= 0:
        return None
    oTarget.m_BulletCon.BulletModify(iBulletSID, -iFillValue, oReason.GetStrReason())
    oBulletCom.BulletModify(iFillValue)


def StatePullOwnerToPos(oTarget, oLifeCycle, iSpeed, fMaxDis, fStopDis = 0.5, iUseAttackPos = 0):
    
    def StopPulling(oTarget, oLifeCycle):
        if oTarget.m_MoveCtrl and oTarget.m_MoveCtrl.m_CurStatus == STATUS_PUSH:
            oTarget.m_MoveCtrl.Stop(oTarget)

    if not (oTarget.m_MoveCtrl) or not (oTarget.m_FightType & WARRIOR_MONSTER):
        return None
    if not oTarget.m_MoveMode & MOVE_TYPE_NORMAL:
        return None
    if oTarget.CheckLogicKey(FIGHT3_KEY_IGNOREKNOCKBACK):
        return None
    oGame = oTarget.m_Game
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    vStart = oTarget.GetPos()
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    if iUseAttackPos:
        oAttacker = oGame.GetObject(oState.m_Attacker)
        if not oAttacker:
            return None
        vTar = oAttacker.GetPos()
    else:
        vTar = oState.GetArgValue('Pos')
    tRetPos = oGame.Scene_RaycastSingle(iScene, vTar, (vTar[0], vTar[1] - 10, vTar[2]), PXMASK_STATIC)
    if tRetPos[0] != -1:
        vEnd = tRetPos[1]
    else:
        vEnd = vTar
    if cl_math.CheckDistance3D(vEnd, vStart, fStopDis):
        return None
    fHeightDiff = abs(vStart[1] - vEnd[1])
    if fHeightDiff > 3:
        return None
    fCurDis = cl_math.CalDistance3D(vStart, vEnd)
    fDis = min(fCurDis, fMaxDis)
    iSpeed = cl_formula.GetResultByData(oTarget, iSpeed, {
        'LifeCycle': oLifeCycle })
    fSpeed = iSpeed / 100
    fSecondOut = fDis / fSpeed
    vDir = cl_math.Vec3Minus(vEnd, vStart)
    oTarget.m_MoveCtrl.PushMove(oTarget, vDir, fSpeed, fSecondOut, iClientAni = 0)
    oLifeCycle.AddDisableFunc(StopPulling)


def StateLockShield(oTarget, oLifeCycle):
    
    def ClearStateLockShield(oTarget, oLifeCycle):
        oState = oLifeCycle.GetObject()
        oTarget.HPDirectModify('Shield', oState.m_Attacker, iShield, oReason)
        oTarget.UnForbid(cl_forbid.SHIELDLOCK_RULE, sKey)

    iShield = oTarget.Shield()
    iChange = -iShield
    oReason = cl_object.reason.CStrReason('状态锁定护盾')
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oTarget.HPDirectModify('Shield', oState.m_Attacker, iChange, oReason)
    sKey = oLifeCycle.Key()
    oTarget.Forbid(cl_forbid.SHIELDLOCK_RULE, sKey)
    oLifeCycle.AddDisableFunc(ClearStateLockShield)


def StateSwitchAttPerform(oTarget, oLifeCycle, iIdx = -1):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oComPerform = oWeapon.GetComponent('Perform')
    if not oComPerform:
        return None
    if iIdx != -1:
        oComPerform.SwitchAttPerform(oTarget, iIdx)
    else:
        oComPerform.SwitchNextAttPerform(oTarget)


def StateResetAttPerform(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    oComPerform = oWeapon.GetComponent('Perform')
    if not oComPerform:
        return None
    oComPerform.ResetAttPerform(oTarget)


def StateTriggerClientBehavior(oTarget, oLifeCycle, iBehavior):
    oGame = oTarget.m_Game
    oState = oLifeCycle.GetObject()
    if 'AID' not in oState.m_StateInfo:
        ErrLog.Alert('%s stateinfo err %s %s %s %s %s' % (oGame.m_ID, oTarget.m_PlayerID, oTarget.m_SID, oState.m_SID, oTarget.m_Perform.GetAllPerformSID(), oState.m_StateInfo))
        return None
    oAttack = oGame.GetObject(oState.m_StateInfo['AID'])
    dPlayer = {
        oTarget.m_PlayerID: 1 }
    if oAttack:
        dPlayer[oAttack.m_PlayerID] = 1
    cl_snetwar.GS2CTriggerBehavior(oGame, oTarget.m_ID, iBehavior, dPlayer, iStop = 0)


def StateShareTreasureRelicRoomCnt(oTarget, oLifeCycle, iMsg, iSub):
    
    def CancelListenMsg(oTarget, oLifeCycle):
        oMonsterRelicElement.MonsterCancelListenMsg(iTarget, iMsg, iSub)

    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oMonsterRelicElement = oTarget.m_Game.m_WarMgr.GetComponent('MonsterRelicElement')
    if not oMonsterRelicElement:
        return None
    iStateSID = oState.m_SID
    iTarget = oTarget.m_ID
    oMonsterRelicElement.MonsterListenMsg(iTarget, iMsg, iSub, iStateSID)
    iCount = oMonsterRelicElement.GetRoomStateCount(iTarget, iStateSID)
    if iCount:
        oState.AddCount(oTarget, iCount)
    oLifeCycle.AddDisableFunc(CancelListenMsg)


def StateRefreshMonsterRelicCnt(oTarget, oLifeCycle, iRelicSID):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    oMonsterRelicElement = oTarget.m_Game.m_WarMgr.GetComponent('MonsterRelicElement')
    if not oMonsterRelicElement:
        return None
    oMonsterRelicElement.SetRefreshRelic(oTarget.m_ID, iRelicSID, oState.m_SID)
    oScene = oTarget.m_Game.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return None
    dPlayers = oScene.GetPlayers()
    if not dPlayers:
        return None
    iCount = oState.GetCount()
    cl_snetwar.GS2CMonsterRelicRefreshCnt(oTarget.m_Game, oTarget.m_ID, iRelicSID, iCount, dPlayers)


def StateChangeStateDelayInfo(oTarget, oLifeCycle, iFirstTime, iDelay, iCount):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dTempDelayAction = oState.m_DelayAction
    if not dTempDelayAction:
        return None
    dDelayAction = { }
    dDelayAction.update(dTempDelayAction)
    dData = {
        'LifeCycle': oLifeCycle }
    if iFirstTime:
        iFirstTime = cl_formula.GetResultByData(oTarget, iFirstTime, dData)
        dDelayAction['firsttime'] = iFirstTime
    if iDelay:
        iDelay = cl_formula.GetResultByData(oTarget, iDelay, dData)
        dDelayAction['delay'] = iDelay
    if iCount:
        iCount = cl_formula.GetResultByData(oTarget, iCount, dData)
        dDelayAction['cnt'] = iCount
    oState.m_DelayAction = dDelayAction


def StateHaltFromSkill(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dStateInfo = oState.m_StateInfo
    iActNum = dStateInfo['ActNum']
    if not iActNum:
        return None
    cl_action.HaltCasting(oTarget, iActNum, oLifeCycle.Key())


def StateSetLiteCD(oTarget, oLifeCycle, iTime):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    iTime = cl_formula.GetResultByData(oTarget, iTime, {
        'LifeCycle': oLifeCycle })
    oState.SetLiteCD(iTime)


def StateTriggerStateDelayBehavior(oTarget, oLifeCycle, iSameFrame):
    oState = oLifeCycle.GetObject()
    idx = oState.GetDelayIdx()
    dIdx2Frame = oTarget.m_StateTimeUnit.m_Idx2Frame
    if idx not in dIdx2Frame:
        return None
    if iSameFrame:
        iCallFrame = dIdx2Frame[idx]
        iFrame = oTarget.m_Game.GetFrameNum()
        if iCallFrame != iFrame:
            return None
    oState.m_LifeCycle.CallFunc('Delay', oTarget)


def StateGetAttackerDis(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    oAttacker = oTarget.m_Game.GetObject(oState.m_Attacker)
    if not oAttacker:
        return 0
    return cl_math.CalDistance3D(oTarget.GetPos(), oAttacker.GetPos())


def StateAddFromSkillCollectInfo(oTarget, oLifeCycle, sAttr, iAdd, iAddExtInfo):
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dStateInfo = oState.m_StateInfo
    iActNum = dStateInfo['ActNum']
    if not iActNum:
        return None
    if iAddExtInfo:
        sAttr = '%s%s' % (oLifeCycle.Key(), sAttr)
    oGame = oTarget.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oTarget.m_ID, iActNum)
    if not oSkill:
        return None
    iOldValue = oSkill.m_Collect[sAttr] if sAttr in oSkill.m_Collect else 0
    iValue = cl_formula.GetResultByData(oTarget, iAdd, {
        'LifeCycle': oLifeCycle })
    oSkill.m_Collect[sAttr] = iOldValue + iValue


def StateGetSelfTransDamFactor(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    if not oState:
        return { }
    return oState.GetArgValue('TransDamFactor', { })


def StateEnableBulletChangeRule(oTarget, oLifeCycle, iPerform, iLevel):
    oState = oLifeCycle.GetObject()
    iOwnStateID = oState.m_ID
    iLevel = cl_formula.GetResultByData(oTarget, iLevel, {
        'LifeCycle': oLifeCycle })
    oTarget.m_BulletChangeCon.AddPerform(oTarget, iOwnStateID, iPerform, iLevel, 1, oState.m_Item)
    oLifeCycle.AddDisableType(DISABLE_TYPE_BULLET, iPerform, iOwnStateID)


def StateDisableBulletChangeRule(oTarget, oLifeCycle, iPerform):
    oState = oLifeCycle.GetObject()
    iOwnStateID = oState.m_ID
    oTarget.m_BulletChangeCon.RemovePerform(oTarget, iOwnStateID, iPerform)


def StateSyncToClient(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    oTarget.m_State.GS2CItemAdd(oState)


def StateGetFromSkillActNum(oTarget, oLifeCycle):
    oState = oLifeCycle.GetObject()
    oReason = oState.Reason()
    return oReason.Query('ActNum', 0)


def StateSetArgValue(oTarget, oLifeCycle, sKey, iValue):
    oState = oLifeCycle.GetObject()
    iValue = cl_formula.GetResultByData(oTarget, iValue, {
        'LifeCycle': oLifeCycle })
    return oState.SetArgValue(sKey, iValue)


def StateRefreshStateExtraInfo(oTarget, oLifeCycle, dInfo):
    oGame = oTarget.m_Game
    oState = oLifeCycle.GetObject()
    if not oState:
        return None
    dRet = cl_formula.CalArgsFormula(oTarget, dInfo, {
        'LifeCycle': oLifeCycle })
    oState.SetArgValue('StateExtraInfo', dRet)
    if not oTarget.m_PlayerID:
        oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
        dPlayer = dict(oScene.GetPlayers()) if oScene else { }
    else:
        dPlayer = {
            oTarget.m_PlayerID: 1 }
    cl_action.GS2CStateRefreshExtraInfo(oTarget, oState, dRet, dPlayer)

