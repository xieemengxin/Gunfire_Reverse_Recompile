# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_snetwar.pyc
# RelativePath: clientlogic/cl_snetwar.pyc
# Source Generated with Decompyle++
# File: cl_snetwar.pyc (Python 3.6)

from cl_only import CRplStr, TraceLog, SendAlert
from cl_commondefines import GetPlayMode, ALL_SUIT_TYPE
from cl_animatorconfig import GetAnimatorConfig
import cl_duonet.dn_cl_cnetwar as warnet
import cl_gamedebug as debug

def GS2CNowSeed(oHero):
    sSeed = debug.CreateLogSeed(oHero)
    debug.SeedDebug(oHero.m_Game, oHero.m_PlayerID, sSeed)


def GS2CDie(oVictim, iAttack, iFinalDam):
    iFinalDam = iFinalDam // 100 if oVictim.m_PlayerID else 0
    warnet.DN_GS2CDie(iAttack, oVictim.m_ID, iFinalDam, oVictim.m_Game, oVictim.m_Scene)


def GS2CWStatusHP(oVictim, oSkill, iTargetPlayer, iAttack, iActNum, iHP, iDamType, iTriggerAbnormal, iBreakShield, iWeaked, iLuckyHitEff, iExInfo):
    oGame = oVictim.m_Game
    iHP = 1 if iHP < 100 else iHP // 100
    if oSkill:
        oSkill.SendBuffer(warnet.DN_GS2CWStatusHP, iAttack, iActNum, oVictim.m_ID, iDamType, iHP, iTriggerAbnormal, iBreakShield, iWeaked, iLuckyHitEff, iExInfo, oGame, iTargetPlayer)
    else:
        warnet.DN_GS2CWStatusHP(iAttack, iActNum, oVictim.m_ID, iDamType, iHP, iTriggerAbnormal, iBreakShield, iWeaked, iLuckyHitEff, iExInfo, oGame, iTargetPlayer)


def GS2CImmunity(oVictim, oSkill, iAttack, iActNum, iType):
    oGame = oVictim.m_Game
    if oSkill:
        oSkill.SendBuffer(warnet.DN_GS2CImmunity, iAttack, iActNum, oVictim.m_ID, iType, oGame, oVictim.m_Scene)
    else:
        warnet.DN_GS2CImmunity(iAttack, iActNum, oVictim.m_ID, iType, oGame, oVictim.m_Scene)


def GS2CStruckMonster(oVictim, iType, iHitPart):
    warnet.DN_GS2CStruckMonster(oVictim.m_ID, iType, iHitPart, oVictim.m_Game, oVictim.m_Scene)


def GS2CMonsterActionSM(oVictim, iType, sArgsName, fArgsValue):
    warnet.DN_GS2CMonsterActionSM(oVictim.m_ID, iType, sArgsName, fArgsValue, oVictim.m_Game, oVictim.m_Scene)


def GS2CRelife(oVictim, iType):
    warnet.DN_GS2CRelife(oVictim.m_ID, iType, oVictim.m_Game)


def GS2CHatch(oVictim, iStatus, iHatchTime):
    warnet.DN_GS2CHatch(oVictim.m_ID, iStatus, iHatchTime, oVictim.m_Game)


def GS2CTriggerBehavior(oGame, iOwner, iBehavior, dPlayer, iStop = 0, iItemID = 0):
    warnet.DN_GS2CTriggerBehavior(iOwner, iItemID, iBehavior, iStop, oGame, dPlayer)


def GS2CRelifeConfirm(oGame, pid, iRelifeIdx, iLeftTimes, iMaxTimes, iType, iRemainTime, iCost):
    warnet.DN_GS2CRelifeConfirm(iRelifeIdx, iLeftTimes, iMaxTimes, iType, iRemainTime, iCost, oGame, pid)


def GS2CLevelNodeLoadOk(oGame, iScene, pid, iLevelID):
    warnet.DN_GS2CLevelNodeLoadOk(iScene, iLevelID, oGame, pid)


def GS2CLevelNodeGoalOk(oGame, iScene, dLevelInfo):
    warnet.DN_GS2CLevelNodeGoalOk(iScene, oGame)


def GS2CAddTransferInfo(oGame, iScene, iNpc, dInfo, iDiff):
    iTrick = dInfo['LevelID']
    warnet.DN_GS2CAddTransferInfo(iScene, iNpc, iTrick, iDiff, oGame)


def GS2CQuitGame(oGame, pid):
    warnet.DN_GS2CQuitGame(pid, oGame)


def GS2CDisconnected(oGame, pid):
    warnet.DN_GS2CDisconnected(pid, oGame)


def GS2CPickUp(oGame, iScene, iHero, iDrop):
    warnet.DN_GS2CPickUp(iHero, iDrop, oGame, iScene)


def GS2CPickFail(oGame, iScene, pid, iDrop):
    warnet.DN_GS2CPickFail(pid, iDrop, oGame, iScene)


def GS2CTriggerBehaviorStatus(oGame, iOwner, iBehavior, iStep, dPlayer):
    warnet.DN_GS2CTriggerBehaviorStatus(iOwner, iBehavior, iStep, oGame, dPlayer)


def GS2CTeamDamage(oGame, pid, lstHeroDamage):
    warnet.DN_GS2CTeamDamage(lstHeroDamage, oGame, pid)


def GS2CCWarPauseStat(oGame, pid, iPaused):
    warnet.DN_GS2CWarPaused(iPaused, oGame, pid)


def GS2CAddEffect(oGame, iScene, iEffectID, iShape, tPos, dPlayer, vFace = None, vScale = None):
    if not vFace:
        vFace = (0, 0, 0)
    if not vScale:
        vScale = (0, 0, 0)
    warnet.DN_GS2CAddEffect(iScene, iEffectID, iShape, tPos, vFace, vScale, oGame, dPlayer)


def GS2CDeleteEffect(oGame, iScene, iEffectID, dPlayer):
    warnet.DN_GS2CDeleteEffect(iScene, iEffectID, oGame, dPlayer)


def GS2CEnterWatch(oGame, iWatch, iFocus, dPlayer):
    warnet.DN_GS2CEnterWatch(iWatch, iFocus, oGame, dPlayer)


def GS2CWarStatus(oGame, iStatus, iFrame, dPlayer):
    warnet.DN_GS2CWarStatus(iStatus, iFrame, oGame, dPlayer)


def GS2CUpdateLevelRoomPos(oGame, iScene, iRoomPos, lstLineName):
    warnet.DN_GS2CUpdateLevelRoomPos(iScene, iRoomPos, lstLineName, oGame)


def GS2CTriggerDestroyEffect(oGame, iOwner, vPos, vFace, dPlayer):
    warnet.DN_GS2CTriggerDestroyEffect(iOwner, vPos, vFace, oGame, dPlayer)


def GS2CFace(oGame, iScene, iTarget, vFace, iTurnTime):
    oTarget = oGame.GetObject(iTarget)
    (dx, dy, dz) = vFace
    warnet.DN_GS2CFace(iTarget, dx, dy, dz, iTurnTime, oGame, iScene, oTarget.m_PlayerID)


def GS2CFaceTarget(oGame, iScene, iTarget, iVictim, iTurnTime, dPlayer = None):
    if not dPlayer:
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        dPlayer = oScene.GetPlayers()
    warnet.DN_GS2CFaceTarget(iTarget, iVictim, iTurnTime, dPlayer)


def GS2CConstantFaceTarget(oGame, iScene, iTarget, iVictim, iTurnSpeed, dPlayer = None):
    if not dPlayer:
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        dPlayer = oScene.GetPlayers()
    warnet.DN_GS2CConstantFaceTarget(iTarget, iVictim, iTurnSpeed, dPlayer)


def GS2CDoubleHPBarUI(oGame, lstWarrior, iState, dPlayer):
    warnet.DN_GS2CDoubleHPBarUI(lstWarrior, iState, oGame, dPlayer)


def GS2CCircleSummonEffect(oGame, iSummon, lstPrefab, iState, dPlayer):
    warnet.DN_GS2CCircleSummonEffect(iSummon, lstPrefab, iState, oGame, dPlayer)


def GS2CMapBuildSimMask(oGame, iBuild, iMask, dPlayer):
    warnet.DN_GS2CMapBuildSimMask(iBuild, iMask, oGame, dPlayer)


def GS2CMonsterSuperInfo(oGame, iMonsterAf, iAttrPlus, iMonsterID, dPlayer):
    warnet.DN_GS2CMonsterSuperInfo(iMonsterID, iMonsterAf, iAttrPlus, oGame, dPlayer)


def GS2CMonsterAdditionInfo(oGame, oMonster, lstAffiliateID):
    warnet.DN_GS2CMonsterAdditionInfo(oMonster.m_ID, lstAffiliateID, oGame, oMonster.m_Scene)


def GS2CReceivedDamRecord(oGame, oMonster, dInfo):
    warnet.DN_GS2CReceivedDamRecord(oMonster.m_ID, dInfo['TotalDam'], dInfo['Dps'], dInfo['MaxDam'], oGame)


def GS2CUpdateMiniMapPos(oGame, iLevel, iOperate, lstPos, dPlayer):
    warnet.DN_GS2CUpdateMiniMapPos(iLevel, iOperate, lstPos, oGame, dPlayer)


def GS2CUpdateSceneIcon(oGame, dPlayer, iLevel, iOperate, lstIcon):
    warnet.DN_GS2CUpdateSceneIcon(iLevel, iOperate, lstIcon, oGame, dPlayer)


def GS2CMonsterUseRelic(oGame, iMonsterID, lstRelic, dPlayer):
    warnet.DN_GS2CMonsterUseRelic(iMonsterID, lstRelic, oGame, dPlayer)


def GS2CRealDie(oVictim):
    warnet.DN_GS2CRealDie(oVictim.m_Game, oVictim.m_PlayerID)


def GS2CBreakShield(oVictim, iAttack):
    warnet.DN_GS2CBreakShield(iAttack, oVictim.m_ID, oVictim.m_Game, oVictim.m_Scene)


def GS2CBreakArmor(oVictim, iAttack):
    warnet.DN_GS2CBreakArmor(iAttack, oVictim.m_ID, oVictim.m_Game, oVictim.m_Scene)


def GS2CTeamInfo(oGame, lstMember, dPlayer):
    lstMemberInfo = []
    for iHero in lstMember:
        oHero = oGame.GetObject(iHero)
        if oHero:
            (dx, dy, dz) = oHero.GetNetFacing()
            lstMemberInfo.append((iHero, oHero.GetPos(), dx, dy, dz))
    
    warnet.DN_GS2CTeamInfo(lstMemberInfo, oGame, dPlayer)


def GS2CPlayType(oGame, pid):
    oWarMgr = oGame.m_WarMgr
    iPlayType = oWarMgr.GetPlayType(bCheckAIMember = False)
    iPlayMode = GetPlayMode(oWarMgr.m_SID)
    warnet.DN_GS2CPlayType(iPlayType, oWarMgr.m_Round, iPlayMode, oWarMgr.m_Cycle, oWarMgr.m_ModeType, oWarMgr.m_ExtraInfo, oWarMgr.m_SeasonNum, pid)


def GS2CPlayTime(oGame, pid, iFrame, iCounting):
    warnet.DN_GS2CPlayTime(iFrame, iCounting, pid)


def GS2CNowInfo(oGame, pid, sInfo):
    warnet.DN_GS2CNowInfo(sInfo.encode('utf-8'), pid)


def GS2CMainCtrl(oGame, iHero, pid, dPlayer):
    warnet.DN_GS2CMainCtrl(iHero, pid, dPlayer, pid)


def GS2CNotifyStartSkill(oGame, pid, iPerformSID, iPerformID, iItemID, dArgs = None):
    if not dArgs:
        dArgs = { }
    warnet.DN_GS2CNotifyStartSkill(iPerformSID, iPerformID, iItemID, dArgs, oGame, pid)


def GS2CLimitConvoy(oGame, iChallenge, sRplMsg, dReplace, iRemainTime, iTotalTime, iNpc, iCurPathIndex, lstPathPos, dPlayer):
    if dReplace:
        sNotify = CRplStr(sRplMsg, dReplace)
    else:
        sNotify = CRplStr(sRplMsg)
    warnet.DN_GS2CLimitConvoy(sNotify, iRemainTime, iTotalTime, iNpc, iChallenge, iCurPathIndex, lstPathPos, oGame, dPlayer)


def GS2CMonsterNotify(oGame, sRplMsg, dReplace, iTime, dPlayer):
    if dReplace:
        sNotify = CRplStr(sRplMsg, dReplace)
    else:
        sNotify = CRplStr(sRplMsg)
    warnet.DN_GS2CMonsterNotify(sNotify, iTime, oGame, dPlayer)


def GS2CClearChallengeUI(oGame, iChallenge, dPlayer):
    warnet.DN_GS2CClearChallengeUI(iChallenge, oGame, dPlayer)


def GS2CLimitDefend(oGame, iChallenge, iNpc, iRemainTime, iTotalTime, sRplMsg, dReplace, dPlayer):
    if dReplace:
        sNotify = CRplStr(sRplMsg, dReplace)
    else:
        sNotify = CRplStr(sRplMsg)
    warnet.DN_GS2CLimitDefend(iChallenge, sNotify, iRemainTime, iTotalTime, iNpc, oGame, dPlayer)


def GS2CTargetDefend(oGame, iChallenge, iNpc, iNow, iTotal, sRplMsg, dReplace, dPlayer):
    if dReplace:
        sNotify = CRplStr(sRplMsg, dReplace)
    else:
        sNotify = CRplStr(sRplMsg)
    warnet.DN_GS2CTargetDefend(iChallenge, sNotify, iNow, iTotal, iNpc, oGame, dPlayer)


def GS2CRelifeInfo(oGame, lstHeroInfo, lstPlayer):
    warnet.DN_GS2CRelifeInfo(lstHeroInfo, oGame, lstPlayer)


def GS2CStartChallenge(oGame, iChallenge, iRemainTime, sRplMsg, dReplace, dPlayer):
    if dReplace:
        sNotify = CRplStr(sRplMsg, dReplace)
    else:
        sNotify = CRplStr(sRplMsg)
    warnet.DN_GS2CStartChallenge(iChallenge, sNotify, iRemainTime, oGame, dPlayer)


def GS2CMainCtrlFace(oTarget):
    (dx, dy, dz) = oTarget.GetNetFacing()
    warnet.DN_GS2CMainCtrlFace(dx, dy, dz, oTarget.m_PlayerID)


def GS2CStartRescue(oWarrior, oTarget, iRescueTime, iStartFrame, dPlayer):
    warnet.DN_GS2CStartRescue(oWarrior.m_ID, oTarget.m_ID, iRescueTime, iStartFrame, oWarrior.m_Game, dPlayer)


def GS2CStopRescue(oWarrior, oTarget, dPlayer):
    warnet.DN_GS2CStopRescue(oWarrior.m_ID, oTarget.m_ID, oWarrior.m_Game, dPlayer)


def GS2CBreakRescue(oWarrior, oTarget, dPlayer):
    warnet.DN_GS2CBreakRescue(oWarrior.m_ID, oTarget.m_ID, oWarrior.m_Game, dPlayer)


def GS2CDayTrialItemInfo(oHero, lstInfo):
    warnet.DN_GS2CDayTrialItemInfo(lstInfo, oHero.m_Game, oHero.m_PlayerID)


def GS2CDayTrialInfo(oHero, iTheme, lstTheme, iGood, iBad):
    warnet.DN_GS2CDayTrialInfo(iTheme, iGood, iBad, lstTheme, oHero.m_Game, oHero.m_PlayerID)


def GS2CEliteCreateTip(oGame, iScene):
    warnet.DN_GS2CEliteCreateTip(iScene, oGame)


def GS2CJumpFigure(oHero, iReason, iTarget, iCnt):
    warnet.DN_GS2CJumpFigure(iReason, iTarget, iCnt, oHero.m_Game, oHero.m_PlayerID)


def GS2CUpdateChallenge(oGame, dPlayer, iContinueTime):
    warnet.DN_GS2CUpdateChallenge(iContinueTime, oGame, dPlayer)


def GS2CForbidRule(oHero, iRule, sKey):
    warnet.DN_GS2CForbidRule(iRule, sKey, oHero.m_PlayerID)


def GS2CUnForbidRule(oHero, iRule, sKey):
    warnet.DN_GS2CUnForbidRule(iRule, sKey, oHero.m_PlayerID)


def GS2CRecycleDropInfo(oHero, lstDropType):
    warnet.DN_GS2CRecycleDropInfo(lstDropType, oHero.m_Game, oHero.m_PlayerID)


def GS2CRecycleDropResult(oGame, iTarget, iHero, iResult, iCashType, iPrice, dPlayer):
    warnet.DN_GS2CRecycleDropResult(iTarget, iResult, iCashType, iPrice, iHero, oGame, dPlayer)


def GS2CCallForHelp(oGame, iHero):
    warnet.DN_GS2CCallForHelp(iHero, oGame)


def GS2CPerformanceInfo(pid, iFlag):
    warnet.DN_GS2CPerformanceInfo(iFlag, pid)


def GS2CConfirmCheat(pid, iConfirm):
    warnet.DN_GS2CConfirmFunc(iConfirm, pid)


def GS2CFightInfo(pid, sWarMask):
    warnet.DN_GS2CFightInfo(sWarMask, pid)


def GS2CSightPhaseTime(oGame, dPlayer, iPhase, sTitle, dOption, iRemainTime):
    warnet.DN_GS2CSightPhaseTime(iPhase, iRemainTime, sTitle, dOption, oGame, dPlayer)


def GS2CSightScore(oGame, dPlayer, iScore, iCurScore, iHitCnt, iVictim):
    warnet.DN_GS2CSightScore(iScore, iCurScore, iHitCnt, iVictim, oGame, dPlayer)


def GS2CSightConfig(oGame, dPlayer, dRewardConfig):
    warnet.DN_GS2CSightConfig(dRewardConfig, oGame, dPlayer)


def GS2CSkipCG(oGame, dPlayer, iHero, iBehavior, iSkip):
    warnet.DN_GS2CSkipCG(iHero, iBehavior, iSkip, oGame, dPlayer)


def GS2CTriggerCG(oGame, pid, iOwner, iBehavior, iCanSkip):
    warnet.DN_GS2CTriggerCG(iOwner, iCanSkip, iBehavior, pid)


def GS2CRefreshItemChecked(oGame, dPlayer, iItemID):
    warnet.DN_GS2CRefreshItemChecked(iItemID, oGame, dPlayer)


def GS2CTransferHideLevelInfo(oGame, pid, iLevel, iLeftTimes):
    warnet.DN_GS2CTransferHideLevelInfo(iLevel, iLeftTimes, pid)


def GS2CUpdateSuitCondtion(oGame, iTarget, lstCond, dPlayer, dCondInfo):
    if not dPlayer:
        dPlayer = oGame.GetRealPlayers()
    lstSuit = []
    for dCondtion in lstCond:
        for iSuit, dCond in dCondtion.items():
            if iSuit not in dCondInfo:
                continue
            lstCondtion = []
            dInfo = dCondInfo[iSuit][1]
            iNum = dCondInfo[iSuit][0]
            for iCondtion, iMeet in dCond.items():
                lstCondtion.append((iCondtion, iMeet, dInfo[iCondtion]))
            
            lstSuit.append((iSuit, lstCondtion, iNum))
        
    
    warnet.DN_GS2CUpdateSuitCondtion(iTarget, lstSuit, oGame, dPlayer)


def GS2CSuitMap(oSuitElement, dPlayer = None):
    oGame = oSuitElement.m_Game
    if not dPlayer:
        dPlayer = oGame.GetRealPlayers()
    lstMap = []
    for iCondition in ALL_SUIT_TYPE:
        lstMap.append((iCondition, oSuitElement.GetSuitMap(iCondition)))
    
    warnet.DN_GS2CSuitMap(lstMap, oGame, dPlayer)


def GS2CLastActionNum(pid, iLastActNum):
    warnet.DN_GS2CLastActionNum(iLastActNum, pid)


def GS2CHeroUpGradeInfoRefresh(pid, iExperience, iGrade, iSkillpoint, iUpNeed):
    warnet.DN_GS2CHeroUpGradeInfoRefresh(iGrade, iExperience, iSkillpoint, iUpNeed, pid)


def GS2CChooseRewardItem(pid, iMenuIdx, iItemType, lstItem, dExtraOption):
    warnet.DN_GS2CChooseRewardItem(iMenuIdx, iItemType, lstItem, dExtraOption, pid)


def GS2CTriggerArea(oGame, iOwner, iType, vPos, vHalfExt, dPlayer):
    warnet.DN_GS2CTriggerArea(iOwner, iType, vPos, vHalfExt, oGame, dPlayer)


def GS2CPhaseInfo(dPlayer, iPhase, iIsFinish):
    warnet.DN_GS2CPhaseInfo(iPhase, iIsFinish, dPlayer)


def GS2CTriggerAnimator(oGame, dPlayer, iTarget, iConfig):
    (_, iType, sArgsName, fArgsValue) = GetAnimatorConfig(iConfig)
    warnet.DN_GS2CTriggerAnimator(iTarget, iType, sArgsName, fArgsValue, oGame, dPlayer)


def GS2CPreviewUpgradeWeaponInfo(pid, iWeapon, dAttr):
    warnet.DN_GS2CPreviewUpgradeWeaponInfo(iWeapon, dAttr, pid)


def GS2CPrepareTimeInfo(dPlayer, iRemainTime, iTotalTime):
    warnet.DN_GS2CPrepareTimeInfo(iRemainTime, iTotalTime, dPlayer)


def GS2CUpdatePrioritySuit(pid, lstPrioritySuit):
    warnet.DN_GS2CUpdatePrioritySuit(lstPrioritySuit, pid)


def GS2CUpdateQuality(pid, iMaxCnt, lstQuality, iSkillClearFlag):
    warnet.DN_GS2CUpdateQuality(iMaxCnt, iSkillClearFlag, lstQuality, pid)


def GS2CUpdateQualityProb(pid, lstQualityProb):
    warnet.DN_GS2CUpdateQualityProb(lstQualityProb, pid)


def GS2CUpdateSignRelic(pid, lstSignRelic):
    warnet.DN_GS2CUpdateSignRelic(lstSignRelic, pid)


def GS2CUpdateSeasonSuitFusedTimes(pid, iSuit, iFusedTimes, iCurGrade):
    warnet.DN_GS2CUpdateSeasonSuitFusedTimes(iSuit, iFusedTimes, iCurGrade, pid)


def GS2CWarNewPing(pid, iPingIdx):
    warnet.DN_GS2CWarNewPing(iPingIdx, pid)


def GS2CMonsterRelicRefreshCnt(oGame, iMonsterID, iRelicSID, iCount, dPlayer):
    warnet.DN_GS2CMonsterRelicRefreshCnt(iMonsterID, iRelicSID, iCount, oGame, dPlayer)


def GS2CTaskStatus(pid, lstTaskStatusInfo):
    warnet.DN_GS2CTaskStatus(lstTaskStatusInfo, pid)


def GS2CTaskStat(pid, lstTaskStatInfo):
    warnet.DN_GS2CTaskStat(lstTaskStatInfo, pid)


def GS2CMonsterSpawnFlaw(pid, lstFlaw):
    warnet.DN_GS2CMonsterSpawnFlaw(lstFlaw, pid)


def GS2CMonsterClearFlaw(pid, iMonsterID):
    warnet.DN_GS2CMonsterClearFlaw(iMonsterID, pid)


def GS2CMonsterKillLine(pid, lstKillLine):
    warnet.DN_GS2CMonsterKillLine(lstKillLine, pid)


def GS2CHeroKillLine(pid, iBaseKillLine, iUnbalanceKillLine):
    warnet.DN_GS2CHeroKillLine(iBaseKillLine, iUnbalanceKillLine, pid)


def GS2CSeasonTaskData(pid, dTaskData):
    warnet.DN_GS2CSeasonTaskData(dTaskData, pid)


def GS2CMonsterKillLineAddition(pid, iMonster, iKillLineAddition):
    warnet.DN_GS2CMonsterKillLineAddition(iMonster, iKillLineAddition, pid)


def GS2CEndlessInfo(oGame, iCurLevelNum, iPassLevelNum, iKillBossNum, iResistance, dPlayer):
    warnet.DN_GS2CEndlessInfo(iCurLevelNum, iPassLevelNum, iKillBossNum, iResistance, oGame, dPlayer)


def GS2CEndlessTime(oGame, iStatus, iOverFrame, dPlayer):
    warnet.DN_GS2CEndlessTime(iStatus, iOverFrame, oGame, dPlayer)


def GS2CEndlessChangeTime(oGame, iChangeTime, dPlayer):
    warnet.DN_GS2CEndlessChangeTime(iChangeTime, oGame, dPlayer)


def GS2CChooseRelicTalent(oHero, iType, lstPerform):
    oHero.IncMenuIdx()
    warnet.DN_GS2CChooseRelicTalent(oHero.m_NpcUIMenuIdx, iType, lstPerform, oHero.m_PlayerID)


def GS2CAddRelicTalent(oGame, iType, iPerform, iLevel, iHero, dPlayer):
    warnet.DN_GS2CAddRelicTalent(iType, iPerform, iLevel, iHero, oGame, dPlayer)


def GS2CMonsterRemoveFlaw(pid, iMonster, iFlaw, iEffect):
    warnet.DN_GS2CMonsterRemoveFlaw(iMonster, iFlaw, iEffect, pid)


def GS2CSeasonTaskDone(lstTask, pid):
    warnet.DN_GS2CSeasonTaskDone(lstTask, pid)


def GS2CChangeExtraPickUpRule(pid, lstRule):
    warnet.DN_GS2CChangeExtraPickUpRule(lstRule, pid)


def GS2CUpdateAllDeviceCompInfo(pid, dDeviceCompInfo):
    warnet.DN_GS2CUpdateAllDeviceCompInfo(dDeviceCompInfo, pid)


def GS2CConquerState(oGame, iType, iConqueror, iTarget, iTotalProgress, iCurProgress, iConquerRate, dPlayer):
    warnet.DN_GS2CConquerState(iType, iConqueror, iTarget, iTotalProgress, iCurProgress, iConquerRate, oGame, dPlayer)


def GS2CMonsterWeakInfo(oGame, iTarget, iTotalTime, iRemainTime, dPlayer):
    warnet.DN_GS2CMonsterWeakInfo(iTarget, iTotalTime, iRemainTime, oGame, dPlayer)


def GS2CConquerChallengeInfo(oGame, iState, iTarget, iPlus, iPerform, dPlayer):
    warnet.DN_GS2CConquerChallengeInfo(iState, iTarget, iPlus, iPerform, oGame, dPlayer)


def GS2CObstacleAlienationRoundInfo(oGame, iRoundMax, iCurrentRound, iRoundTime, lstInfo, dPlayer):
    warnet.DN_GS2CObstacleAlienationRoundInfo(iRoundMax, iCurrentRound, iRoundTime, lstInfo, oGame, dPlayer)


def GS2CUpdateDeviceCompLevel(pid, iSID, iLevel):
    warnet.DN_GS2CUpdateDeviceCompLevel(iSID, iLevel, pid)


def GS2CUpdateDeviceCompPos(pid, iSID, iPos):
    warnet.DN_GS2CUpdateDeviceCompPos(iSID, iPos, pid)


def GS2CDeviceCompMaxPos(pid, iMaxPos):
    warnet.DN_GS2CDeviceCompMaxPos(iMaxPos, pid)


def GS2CChooseDevice(oHero, lstDevice):
    oHero.IncMenuIdx()
    warnet.DN_GS2CChooseDevice(oHero.m_NpcUIMenuIdx, lstDevice, oHero.m_PlayerID)


def GS2CAddDevice(oGame, iHero, iDeviceSID, dPlayer):
    warnet.DN_GS2CAddDevice(iHero, iDeviceSID, oGame, dPlayer)


def GS2CSendThunderStageInfo(oGame, iStage, iTime, iRemainTime, lstPos, dPlayer):
    warnet.DN_GS2CSendThunderStageInfo(iStage, iTime, iRemainTime, lstPos, oGame, dPlayer)


def GS2CSwitchFuncMode(pid, iMode, dNetInfo):
    warnet.DN_GS2CSwitchFuncMode([
        [
            iMode,
            dNetInfo]], pid)


def GS2CIsFirstCycle(pid, iIsFirstCycle):
    warnet.DN_GS2CIsFirstCycle(iIsFirstCycle, pid)


def GS2CSeasonFunc(pid, lstFunc):
    warnet.DN_GS2CSeasonFunc(lstFunc, pid)


def GS2CCustomReconnetion(oGame):
    warnet.DN_GS2CCustomReconnetion(oGame)


def GS2CUpdateSeasonSuitCondtion(oGame, oSuitElement, iTarget, lstCond, dPlayer, dCondInfo, iClearData = 0):
    if not dPlayer:
        dPlayer = oGame.GetRealPlayers()
    lstSuit = []
    dGrade = oSuitElement.GetAllSuitGradeInfo(iTarget)
    for dCondtion in lstCond:
        for iSuit, dCond in dCondtion.items():
            if iSuit not in dCondInfo:
                continue
            lstCondtion = []
            dInfo = dCondInfo[iSuit][1]
            iNum = dCondInfo[iSuit][0]
            iGrade = dGrade[iSuit]
            iFusedTimes = oSuitElement.GetConditionReduceNum(iTarget, iSuit)
            for iCondtion, iMeet in dCond.items():
                lstCondtion.append((iCondtion, iMeet, dInfo[iCondtion]))
            
            lstSuit.append((iSuit, lstCondtion, iNum, iGrade, iFusedTimes))
        
    
    warnet.DN_GS2CUpdateSeasonSuitCondtion(iTarget, lstSuit, iClearData, oGame, dPlayer)


def GS2CSeasonSuitMap(oSuitElement, pid):
    oGame = oSuitElement.m_Game
    lstMap = []
    for iCondition in ALL_SUIT_TYPE:
        lstMap.append((iCondition, oSuitElement.GetSuitMap(iCondition)))
    
    warnet.DN_GS2CSeasonSuitMap(lstMap, oSuitElement.m_AllSuitGradeInfo, oGame, {
        pid: 1 })


def GS2CSeasonSuitOptionInfo(iOption, lstResult, oGame, oHero, iSendAll = 0):
    dPlayer = oGame.GetRealPlayers() if iSendAll else {
        oHero.m_PlayerID: 1 }
    warnet.DN_GS2CSeasonSuitOptionInfo(iOption, oHero.m_ID, lstResult, oGame, dPlayer)


def GS2CUpdateSeasonSuitReduceInfo(dSuitReduceInfo, pid):
    warnet.DN_GS2CUpdateSeasonSuitReduceInfo(dSuitReduceInfo, pid)


def GS2CShowDamageInfo(lstInfo, pid):
    warnet.DN_GS2CShowDamageInfo(lstInfo, pid)


def GS2CMarkSeasonSuit(pid, dMarkSuit):
    warnet.DN_GS2CMarkSeasonSuit(dMarkSuit, pid)


def GS2CSeasonSuitPerformStart(iSID, pid):
    warnet.DN_GS2CSeasonSuitPerformStart(iSID, pid)


def GS2CShowSuitTempList(iCurSuitTemp, lstSuitTemp, pid):
    warnet.DN_GS2CShowSuitTempList(iCurSuitTemp, lstSuitTemp, pid)


def GS2CSetSuitTempResult(pid, iSuitTemp, iResult):
    warnet.DN_GS2CSetSuitTempResult(iSuitTemp, iResult, pid)


def GS2CRealDiedRelifeConfirm(pid, oGame, iCost):
    warnet.DN_GS2CRealDiedRelifeConfirm(iCost, oGame, pid)


def GS2CMonsterMaxCreateCnt(pid, iCount):
    warnet.DN_GS2CMonsterMaxCreateCnt(iCount, pid)


def GS2CUpdateUI(oGame, iType, iOperate, sRplMsg, dReplace, dExtInfo, dPlayer):
    if dReplace:
        sMsg = CRplStr(sRplMsg, dReplace)
    else:
        sMsg = CRplStr(sRplMsg)
    warnet.DN_GS2CUpdateUI(iType, iOperate, sMsg, dExtInfo, oGame, dPlayer)


def GS2CUpdateDataUI(oGame, pid, iType, dExtInfo):
    warnet.DN_GS2CUpdateDataUI(iType, dExtInfo, oGame, pid)


def GS2CShowDetailDam(lstDetailDam, pid):
    warnet.DN_GS2CShowDetailDam(lstDetailDam, pid)


def GS2CCustomPerformData(dPerform, pid):
    warnet.DN_GS2CCustomPerformData(dPerform, pid)

