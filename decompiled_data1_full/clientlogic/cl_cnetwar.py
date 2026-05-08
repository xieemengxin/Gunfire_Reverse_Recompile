# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_cnetwar.pyc
# RelativePath: clientlogic/cl_cnetwar.pyc
# Source Generated with Decompyle++
# File: cl_cnetwar.pyc (Python 3.6)

from cl_commondefines import WARRIOR_BEACON, NWARRIOR_DROP_EQUIP, CHALLENGE_SIGHT, CG_STATUS_END, SEALED_MONKEY, TALENT_ANCIENT_ETCHING, CHOOSE_REWARD_CLOSE, CHOOSE_REWARD_OPEN, CHOOSE_REWARD_UPDATE, PLAY_TYPE_SINGLE, LEVEL_TYPE_BOSS, STATE_CHOOSEREWARD, WARRIOR_HERO, INTERACT_PROTECT_REWARD, INTERACT_PROTECT_IGNORETEAM, INTERACT_ALL_TPYE
from cl_commondefines import NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, FUNCMODE_TYPE_TALENTLEVELUP, FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE, VIRTUAL_ITEM_TALENT, ALL_SUIT_HANDLE, NWARRIOR_DROP_DICE, NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_WANDCOMP, GARDENER_HERO, FUNCMODE_TYPE_ADDNEWTALENT
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
from cl_object.logging import CgLog, SurvivorLog, WarobjLog, DeviceLog
import cl_action
import cl_snetwar
import cl_gamedebug
import cl_notify
import cl_msgcenter
import cl_netattr
import cl_reward
import cl_item.defines as itemdef

def C2GSFace(oHero, dx, dy, dz):
    if oHero.IsDead():
        return None
    oScene = oHero.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
    if not oScene:
        return None
    if oHero.m_ID not in oScene.GetHeros():
        return None
    dx -= 128
    dy -= 128
    dz -= 128
    if not dx and not dy and not dz:
        return None
    oHero.SetFacing((dx, dy, dz))


def C2GSPickUp(oHero, iDrop, iPos, iPickType):
    oGame = oHero.m_Game
    oDrop = oGame.GetObject(iDrop)
    if not oDrop:
        return None
    oDrop.DelayPick(oHero, iPos, iPickType)


def C2GSReplaceWeapon(oHero, iDrop, iFromPos, iToPos):
    oDrop = oHero.m_Game.GetObject(iDrop)
    if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_EQUIP:
        return None
    oDrop.ReplaceWeapon(oHero, iFromPos, iToPos)


def C2GSResetSpoolup(oHero, iWeapon):
    oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oComSpoolup = oWeapon.GetComponent('Spoolup')
    if oComSpoolup:
        oComSpoolup.ResetSpoolupCnt()


def C2GSSnipe(oHero, iOpen):
    if not oHero.SwitchSnipe(iOpen):
        oHero.SyncSnipeChange()


def C2GSRelifeAnswer(oHero, iRelifeIdx, iAnswer):
    oWarMgr = oHero.m_Game.m_WarMgr
    oDieElement = oWarMgr.GetComponent('PVEDieElement')
    oDieElement.AnswerRelife(oHero, iRelifeIdx, iAnswer)


def C2GSWarPing(oHero, iPing):
    oHero.m_Game.m_WarKeep.WarKeepHeartBeat(oHero)


def C2GSWarNewPing(oHero, iPingIdx):
    oHero.m_Game.m_WarKeep.WarKeepHeartBeat(oHero)
    cl_snetwar.GS2CWarNewPing(oHero.m_PlayerID, iPingIdx)


def C2GSEarphone(oHero, sName):
    if not sName:
        return None
    lstEarphones = oHero.QuerySavedData('Earphones', [])
    if sName not in lstEarphones:
        lstEarphones.append(sName)
        oHero.SetSavedData('Earphones', lstEarphones)


def C2GSHaltAction(oHero, iActNum):
    cl_action.HaltCasting(oHero, iActNum, '主动打断')


def C2GSEnterWatch(oHero, iConfirm):
    pass


def C2GSSwitchWeaponAttPF(oHero, iWeapon, iPerformIdx):
    oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oComPerform = oWeapon.GetComponent('Perform')
    if not oComPerform:
        return None
    oComPerform.SwitchAttPerform(oHero, iPerformIdx)


def C2GSSwitchWeaponCliMode(oHero, iWeapon, iCliMode):
    oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    iWeaponSID = oWeapon.m_SID
    oHero.SaveWeaponCliMode(iWeaponSID, iCliMode)
    oWeapon.GS2CItemPropChange('CliModeIdx', iCliMode)


def C2GSRealDiedRelife(oHero):
    oWatchElement = oHero.m_Game.m_WarMgr.GetComponent('WatchElement')
    if not oWatchElement:
        return None
    oWatchElement.RealDiedRelife(oHero)


def C2GSUpdateSkillCounter(oHero, iPerformSID, iCount):
    oPerform = oHero.GetPerform(iPerformSID)
    if not oPerform:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPDATESKILLCOUNT, oHero, {
        'pfid': iPerformSID,
        'SkillCount': iCount })


def C2GSPickSeed(oHero, iSeed):
    if oHero.m_SID != GARDENER_HERO:
        return None
    oHero.m_GardenerCon.PickSeed(iSeed)


def C2GSRemoveBeaconSummon(oHero, iSummon):
    if iSummon not in oHero.m_SummonDict:
        return None
    oSummon = oHero.m_Game.GetObject(iSummon)
    if not oSummon or oSummon.m_FightType != WARRIOR_BEACON:
        return None
    oSummon.Remove('ClientRemove')


def C2GSTriggerBehavior(oHero, iBehavior, iStop):
    oGame = oHero.m_Game
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    iOwner = oHero.m_PlayerID
    if iOwner in lstPlayer:
        lstPlayer.remove(iOwner)
    cl_snetwar.GS2CTriggerBehavior(oGame, oHero.m_ID, iBehavior, lstPlayer, iStop)


def C2GSTriggerCartoonList(oHero, lstCartoon):
    iTriggerNum = 0
    lstSkill = []
    oGame = oHero.m_Game
    for iActNum, iCartoonID in lstCartoon:
        oSkill = oGame.m_SkillMgr.GetSkill(oHero.m_ID, iActNum)
        if oSkill and iCartoonID in oSkill.m_Cartoon:
            iTriggerNum += 1
            lstSkill.append(oSkill)
    
    for oSkill in lstSkill:
        dMsg = {
            'TriggerNum': iTriggerNum }
        oSkill.SendSkillTriggerMsg(dMsg)
    


def C2GSSwitchWatch(oHero, iTarget):
    oWarMgr = oHero.m_Game.m_WarMgr
    oWatchElement = oWarMgr.GetComponent('WatchElement')
    if oWatchElement:
        oWatchElement.SwitchWatch(oHero.m_ID, iTarget)


def C2GSNowInfo(oHero):
    sInfo = cl_gamedebug.GameNowInfo(oHero)
    cl_snetwar.GS2CNowInfo(oHero.m_Game, oHero.m_PlayerID, sInfo)
    cl_snetwar.GS2CNowInfo(oHero.m_Game, oHero.m_PlayerID, '<日志结束>')
    cl_snetwar.GS2CNowSeed(oHero)


def C2GSWeaponLockTarget(who, iWeapon, iKey, lstTarget):
    oWeapon = who.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    sKey = 'LockTarget%d' % iKey
    oWeapon.SetTmp(sKey, lstTarget)


def C2GSTeamDamage(oHero):
    oGame = oHero.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    dPlayer = {
        oHero.m_PlayerID: 1 }
    for iHero in lstHero:
        if oHero.m_ID == iHero:
            continue
        oTeamer = oGame.GetObject(iHero)
        if not oTeamer:
            continue
        lstWeapon = oTeamer.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
        for oWeapon in lstWeapon:
            cl_netattr.SyncWeaponProp(oWeapon, dPlayer)
        
    
    oReport = oGame.m_WarMgr.GetComponent('Warreport')
    if oReport:
        lstDamage = oReport.GetAllTotalDamage()
        cl_snetwar.GS2CTeamDamage(oGame, oHero.m_PlayerID, lstDamage)


def C2GSStartRescue(who, iTarget):
    WarobjLog.Debug('gameid %d receive c2gsstartrescue %d %d %d' % (who.m_Game.m_ID, who.m_PlayerID, who.m_ID, iTarget))
    oRescueElement = who.m_Game.m_WarMgr.GetComponent('RescueElement')
    if not oRescueElement:
        return None
    oRescueElement.StartRescue(who, iTarget)


def C2GSBreakRescue(who, iRescuer, iTarget):
    oRescueElement = who.m_Game.m_WarMgr.GetComponent('RescueElement')
    if not oRescueElement:
        return None
    oWarrior = who.m_Game.GetObject(iRescuer)
    if not oWarrior:
        return None
    oRescueElement.HaltRescue(oWarrior, { })


def C2GSSaveInfo(oHero, iWeapon, iReset):
    oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oWeapon.GetSaveInfo(oHero, iWeapon, iReset)


def C2GSRelifeSetPhase(who, iTarget):
    pass


def C2GSChooseOption(oHero, iOption):
    tLineIdx = oHero.Query('SightCurLevel')
    if not tLineIdx:
        return None
    oLevelCtrl = oHero.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return None
    oChallenge = oLevelCtrl.m_RoomChallenge.GetChallenge(tLineIdx)
    if not oChallenge or oChallenge.m_Type != CHALLENGE_SIGHT:
        return None
    if iOption not in oChallenge.m_OptionFunc:
        return None
    oChallenge.m_OptionFunc[iOption]()


def C2GSCallForHelp(oHero):
    oGame = oHero.m_Game
    lstPlayer = oGame.m_WarMgr.GetLivePlayer()
    cl_notify.SendCommonNotify(oGame, lstPlayer, 12010, {
        '$$playername': oHero.Name() })
    cl_snetwar.GS2CCallForHelp(oGame, oHero.m_ID)


def C2GSReportFPS(oHero, iScene, iAve, iBelowLowRatio, iLowRatio, iMidRatio, iHighRatio, iAboveHighRatio, iGear, iMemoryUsage):
    oReport = oHero.m_Game.m_WarMgr.GetComponent('Warreport')
    if oReport:
        oReport.OnReportFPS(oHero, iScene, iAve, iBelowLowRatio, iLowRatio, iMidRatio, iHighRatio, iAboveHighRatio, iGear, iMemoryUsage)


def C2GSRecycleDrop(oHero, iDrop):
    oGame = oHero.m_Game
    oDrop = oGame.GetObject(iDrop)
    if not oDrop:
        return None
    sReason = 'ActiveRecycle'
    oWarMgr = oGame.m_WarMgr
    oSeasonElement = None
    if oDrop.m_FightType in (NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_WANDCOMP):
        oSeasonElement = oWarMgr.GetWandElement()
    elif oDrop.m_FightType == NWARRIOR_DROP_DICE:
        oSeasonElement = oWarMgr.GetDiceElement()
    if oSeasonElement:
        oSeasonElement.RecycleDrop(oHero, oDrop, sReason)
        return None
    oRecycleDropElement = oWarMgr.GetComponent('RecycleDropElement')
    if not oRecycleDropElement:
        return None
    oRecycleDropElement.RecycleDrop(oHero, iDrop)


def C2GSRecycleUnDrop(oHero, iType, iSID):
    oRecycleDropElement = oHero.m_Game.m_WarMgr.GetComponent('RecycleDropElement')
    if not oRecycleDropElement:
        return None
    oRecycleDropElement.RecycleUnDrop(oHero, iType, iSID)


def C2GSTalentLevelUp(oHero, iTalent):
    oTalentCon = oHero.m_TalentCon
    if not oTalentCon:
        return None
    oGame = oHero.m_Game
    dAllBanTalent = oTalentCon.GetAllBanTalent()
    if iTalent in dAllBanTalent:
        WarobjLog.Alert('%d %d talentlvup ban err %d' % (oGame.m_ID, oHero.m_PlayerID, iTalent))
        return None
    dHasTalent = oTalentCon.m_Perform
    if iTalent in dHasTalent:
        TalentLevelUp(oHero, iTalent)
    else:
        AddNewTalent(oHero, iTalent)


def TalentLevelUp(oHero, iTalent):
    oGame = oHero.m_Game
    dFuncModeInfo = oHero.GetFuncMode()
    if FUNCMODE_TYPE_TALENTLEVELUP not in dFuncModeInfo or not dFuncModeInfo[FUNCMODE_TYPE_TALENTLEVELUP]:
        return None
    oTalentCon = oHero.m_TalentCon
    dAllTalent = oTalentCon.GetAllTalentLevel()
    if iTalent not in dAllTalent or dAllTalent[iTalent] < 1:
        WarobjLog.Alert('%d %d talentlvup err %d' % (oGame.m_ID, oHero.m_PlayerID, iTalent))
        return None
    oTalent = oTalentCon.GetPerform(iTalent)
    if dAllTalent[iTalent] >= oTalent.m_MaxLevel:
        WarobjLog.Alert('%d %d talentlvup level err %d' % (oGame.m_ID, oHero.m_PlayerID, iTalent))
        return None
    oHero.CostFuncModeTimes(FUNCMODE_TYPE_TALENTLEVELUP, 1)
    dReward = {
        'item': VIRTUAL_ITEM_TALENT,
        'info': {
            'sid': iTalent,
            'amount': 1 } }
    cl_reward.RewardItem(oGame, oHero, [
        dReward], 'C2GSTalentLevelUp')


def AddNewTalent(oHero, iTalent):
    oGame = oHero.m_Game
    dFuncModeInfo = oHero.GetFuncMode()
    if FUNCMODE_TYPE_ADDNEWTALENT not in dFuncModeInfo or not dFuncModeInfo[FUNCMODE_TYPE_ADDNEWTALENT]:
        return None
    oHero.CostFuncModeTimes(FUNCMODE_TYPE_ADDNEWTALENT, 1)
    dReward = {
        'item': VIRTUAL_ITEM_TALENT,
        'info': {
            'sid': iTalent,
            'amount': 1 } }
    cl_reward.RewardItem(oGame, oHero, [
        dReward], 'C2GSAddNewTalent')


def C2GSStartConquer(oHero, iTarget):
    oConquerElement = oHero.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        return None
    oConquerElement.m_ConquerchallengeMgr.StartConquer(oHero, iTarget)


def C2GSHaltConquer(oHero, iTarget):
    oConquerElement = oHero.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        return None
    oConquerElement.m_ConquerchallengeMgr.HaltConquer(oHero, iTarget)


def C2GSModeAnswer(oHero, iMode, iSID):
    dFuncModeInfo = oHero.GetFuncMode()
    if iMode not in dFuncModeInfo or not dFuncModeInfo[iMode]:
        WarobjLog.Debug('mode:%s do not have available times' % iMode)
        return None
    if iMode not in g_FuncMode or not g_FuncMode[iMode]:
        WarobjLog.Debug('mode:%s do not have callback func' % iMode)
        return None
    g_FuncMode[iMode](oHero, iSID)


def C2GSHaltRepeatShoot(oHero, iWeapon):
    
    def DelayClearWeaponFireCnt():
        oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oPerformCon = oWeapon.GetComponent('Perform')
        if not oPerformCon:
            return None
        oPerformCon.ClearFireCnt()
        oWeapon.SendMsg(itemdef.MSG_ITEM_REPEAT_END)

    oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oPerformCon = oWeapon.GetComponent('Perform')
    if oPerformCon:
        iNowFrame = oHero.m_Game.GetFrameNum()
        if oPerformCon.m_RepeatCnt > 1 and oPerformCon.m_HaltRepeatFrame < iNowFrame:
            oPerformCon.m_HaltRepeatFrame = iNowFrame + oPerformCon.m_RepeatCnt * oPerformCon.m_RepeatCold * 7 // 1000
            lstAttackCache = oHero.m_WeaponWaitingSkill.get(iWeapon, [])
            if lstAttackCache:
                iDelayFrame = len(lstAttackCache) * oPerformCon.m_RepeatCold // 100
                oHero.Call_Out(DelayClearWeaponFireCnt, iDelayFrame, 'DelayClearWeaponFireCnt')
            else:
                oPerformCon.ClearFireCnt()
                oWeapon.SendMsg(itemdef.MSG_ITEM_REPEAT_END)


def C2GSRollRelic(oHero, iID, iPerformSID, iRollType):
    oRollRelicElement = oHero.m_Game.m_WarMgr.GetComponent('RollRelicElement')
    if not oRollRelicElement:
        return None
    oRollRelicElement.RollRelic(oHero, iID, iPerformSID, iRollType)


def C2GSSetRelicUpgradeType(oHero, iUpgradeType):
    if not oHero.m_GamblerCon:
        return None
    oHero.m_GamblerCon.SetUpgradeRelicType(iUpgradeType)


def C2GSCheckImmortal(oHero, iImmortal):
    if not iImmortal:
        return None
    oCheckCheatElement = oHero.m_Game.m_WarMgr.GetComponent('CheckCheatElement')
    if not oCheckCheatElement:
        return None
    oCheckCheatElement.UsePlugin(oHero)


def C2GSClientEvent(who, iType, lstClientKey):
    if iType == 1:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_UNSEND_CLIENTBUTTON, who, {
            'lstClientKey': lstClientKey })
    elif iType == 2:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_UNSEND_CGEVENT, who, { })


def C2GSSkipCG(oHero, iBehavior):
    oGame = oHero.m_Game
    dPlayer = oGame.GetRealPlayers()
    oLevelNode = oGame.m_WarMgr.GetComponent('LevelCtrl').m_CurNode
    dSkip = oLevelNode.m_SkipCGPlayer.setdefault(iBehavior, { })
    dSkip[oHero.m_PlayerID] = 1
    iSkip = 0
    CgLog.Debug('%s skipcg %d %s %d %s %s' % (oGame.m_ID, oHero.m_PlayerID, dSkip, iBehavior, dPlayer, oLevelNode.m_CustomData))
    if len(dSkip) >= len(dPlayer):
        iSkip = 1
        sKey = 'BehaviorEnd-%d' % iBehavior
        if sKey not in oLevelNode.m_CustomData:
            oLevelNode.m_CustomData[sKey] = 1
            CgLog.Debug('%s cgend %s' % (oGame.m_ID, iBehavior))
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CG_END, oGame.m_WarMgr, {
                'Behavior': iBehavior })
    cl_snetwar.GS2CSkipCG(oGame, dPlayer, oHero.m_ID, iBehavior, iSkip)


def C2GSCGState(oHero, iBehavior, iState):
    oGame = oHero.m_Game
    oLevelNode = oGame.m_WarMgr.GetComponent('LevelCtrl').m_CurNode
    CgLog.Debug('%s cgstate %d %d %d %s ' % (oGame.m_ID, oHero.m_PlayerID, iState, iBehavior, oLevelNode.m_CustomData))
    if iState == CG_STATUS_END:
        sKey = 'BehaviorEnd-%d' % iBehavior
        if sKey not in oLevelNode.m_CustomData:
            oLevelNode.m_CustomData[sKey] = 1
            CgLog.Debug('%s cgend %s' % (oGame.m_ID, iBehavior))
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CG_END, oGame.m_WarMgr, {
                'Behavior': iBehavior })


def C2GSSetTeamPF(oHero, iOpen):
    if oHero:
        oHero.SetTeamPF(iOpen)


def C2GSRefreshItemChecked(oHero, iDrop):
    oGame = oHero.m_Game
    oDrop = oGame.GetObject(iDrop)
    if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_EQUIP:
        return None
    oDrop.SetCheckedPlayer(oHero)


def C2GSUpdateSealedInscription(oHero, iType, iOpen):
    oGame = oHero.m_Game
    if not oGame.m_WarMgr.IsUseSealedInscription():
        return None
    iLv = 0
    if iType == SEALED_MONKEY:
        oTalent = oHero.m_TalentCon.GetPerform(TALENT_ANCIENT_ETCHING)
        iLv = oTalent.m_Level if oTalent else 0
    if not iLv:
        return None
    lstWeapon = oHero.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
    if not lstWeapon:
        return None
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        if iOpen:
            oInscriptionCom.EnableSealedInscription(iLv)
            continue
        oInscriptionCom.DisableSealedInscription(iLv)
    


def C2GSChooseReward(oHero, iMenuIdx, iAnswer):
    if not oHero.m_Game.m_WarMgr.IsInRoom(oHero.m_PlayerID):
        return None
    oSurvivorElement = oHero.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if oSurvivorElement:
        oSurvivorElement.m_UpgradeMgr.ChooseReward(oHero, iMenuIdx, iAnswer)
    else:
        oSurvivorElement = oHero.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if oSurvivorElement and oSurvivorElement.m_RewardMgr.ValidChooseReward(oHero):
            oSurvivorElement.m_RewardMgr.ChooseReward(oHero, iMenuIdx, iAnswer)


def C2GSPreviewUpgradeWeapon(oHero, iWeapon):
    oSurvivorElement = oHero.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if not oSurvivorElement:
        return None
    oSurvivorElement.m_UpgradeMgr.QueryPreviewUpgradeWeapon(oHero, iWeapon)


def C2GSUpdateChooseRewardStatus(oHero, iFrame, iStatus, iType):
    SurvivorLog.Debug('game:%d updatestatus %s %s %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iStatus, iType))
    if iType not in INTERACT_ALL_TPYE:
        return None
    oWarMgr = oHero.m_Game.m_WarMgr
    if iType != INTERACT_PROTECT_IGNORETEAM and oWarMgr.GetPlayType(bCheckAIMember = False) == PLAY_TYPE_SINGLE:
        return None
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    if oLevelCtrl and oLevelCtrl.m_CurNode and oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_BOSS:
        return None
    oSurvivorElement = oHero.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if not oSurvivorElement:
        return None
    if iStatus == CHOOSE_REWARD_OPEN:
        oUpgradeMgr = oSurvivorElement.m_UpgradeMgr
        if iType == INTERACT_PROTECT_REWARD:
            if oHero.m_ID not in oUpgradeMgr.m_CurRewardInfo or not oUpgradeMgr.m_CurRewardInfo[oHero.m_ID]:
                return None
        if oHero.m_State.GetItemBySID(STATE_CHOOSEREWARD):
            return None
        oSurvivorElement.OpenChooseReward(oHero, iFrame)
    elif iStatus == CHOOSE_REWARD_CLOSE:
        oSurvivorElement.CloseChooseReward(oHero, iFrame)
    elif iStatus == CHOOSE_REWARD_UPDATE:
        iCurFrame = oHero.m_Game.GetFrameNum()
        oSurvivorElement.m_ChooseRewardUpdateFrame[oHero.m_ID] = iCurFrame


def C2GSUpdateVoteStatus(oHero, iStatus):
    oSurvivorElement = oHero.m_Game.m_WarMgr.GetSurvivorElement()
    if not oSurvivorElement:
        return None
    oSurvivorElement.UpdateVoteStatus(oHero, iStatus)


def C2GSChangeHeroName(oHero, iTargetHero, sName):
    oTarget = oHero.m_Game.GetObject(iTargetHero)
    if not oTarget or oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    if oTarget:
        oTarget.SetName(sName)


def C2GSSetPrioritySuit(oHero, iSuit):
    oSuitElement = oHero.m_Game.m_WarMgr.GetComponent('SuitElement')
    if not oSuitElement:
        return None
    oSuitElement.SetPrioritySuit(oHero, iSuit)


def C2GSViewSeasonTask(oHero):
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_CMD_OPENSEASONPANEL, oHero, { })
    oHero.m_SeasonTaskMgr.UpdateExtShowInfo()
    dTaskData = oHero.m_SeasonTaskMgr.GetAllSeasonTaskData()
    cl_snetwar.GS2CSeasonTaskData(oHero.m_PlayerID, dTaskData)


def C2GSRecycleGoldenCup(oHero, iNpcID):
    oNpc = oHero.m_Game.GetObject(iNpcID)
    if oNpc and oNpc.m_FightType in (NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP):
        oNpc.Recycle(oHero.m_PlayerID)


def C2GSUpdateDeviceCompLevel(oHero, iSID, iLevel):
    if iLevel < 0:
        return None
    oPerformCon = oHero.m_DevicePerformCon
    oDeviceComp = oPerformCon.GetComponent(iSID)
    if not oDeviceComp:
        return None
    iCurLevel = oDeviceComp.m_Level
    if iLevel >= iCurLevel:
        DeviceLog.Debug('%s %s devicecomp %s level:%s cur:%s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iSID, iLevel, iCurLevel))
        return None
    iDropCnt = iCurLevel - iLevel
    for _ in range(iDropCnt):
        oPerformCon.DegradeComponent(iSID)
    


def C2GSUpdateDeviceCompPos(oHero, iSID, iPos):
    oHero.m_DevicePerformCon.UpdateComponentPos(iSID, iPos)


def C2GSIceMoveDistance(oHero, iDis):
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ICE_MOVE, oHero, {
        'Distance': iDis })


def C2GSSeasonSuitOption(oHero, iOption, lstResult):
    if iOption not in ALL_SUIT_HANDLE:
        return None
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, oHero, {
        'Result': lstResult }, iSub = iOption)


def C2GSSignRelic(oHero, iRelicSID, iSign):
    if oHero.m_GamblerCon:
        oHero.m_GamblerCon.SignRelic(iRelicSID, iSign)
    else:
        oRegroupRelicElement = oHero.m_Game.m_WarMgr.GetComponent('RegroupRelicElement')
        if oRegroupRelicElement:
            oRegroupRelicElement.SignRelic(oHero.m_PlayerID, iRelicSID, iSign)


def C2GSMarkSeasonSuit(oHero, dMarkSuit):
    oSeasonSuitElement = oHero.m_Game.m_WarMgr.GetSeasonSuitElement()
    if oSeasonSuitElement:
        oSeasonSuitElement.SetMarkSuit(oHero, dMarkSuit)


def C2GSSetSuitTemp(oHero, iSuitTempID):
    oSeasonSuitElement = oHero.m_Game.m_WarMgr.GetSeasonSuitElement()
    if oSeasonSuitElement:
        oSeasonSuitElement.ChangeSuitTemp(oHero, iSuitTempID)


def OnShowCardPackSuitChoose(oHero, iSID):
    oWarMgr = oHero.m_Game.m_WarMgr
    oSeasonSuitElement = oWarMgr.GetSeasonSuitElement()
    if oSeasonSuitElement:
        oSeasonSuitElement.OnShowMultiChoose(oHero)

g_FuncMode = {
    FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE: OnShowCardPackSuitChoose,
    FUNCMODE_TYPE_TALENTLEVELUP: None }
