# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_cnetwar.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_cnetwar.pyc
# Source Generated with Decompyle++
# File: dn_cl_cnetwar.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_cnetwar

def DN_GS2CDie(iAttack, iVictim, iFinalDam, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(iAttack, 4)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.PacketAddI(iFinalDam, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CWStatusHP(iAttack, iActNum, iVictim, iType, iHP, iAbnormal, iBreakShield, iWeaked, iLuckyHitEff, iExInfo, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(iAttack, 4)
    cl_duonet.netfunc.PacketAddI(iActNum, 2)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.PacketAddI(iType, 4)
    cl_duonet.netfunc.PacketVarLong(iHP)
    cl_duonet.netfunc.PacketAddI(iAbnormal, 2)
    cl_duonet.netfunc.PacketAddI(iBreakShield, 1)
    cl_duonet.netfunc.PacketAddI(iWeaked, 1)
    cl_duonet.netfunc.PacketAddI(iLuckyHitEff, 1)
    cl_duonet.netfunc.PacketAddI(iExInfo, 2)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CImmunity(iAttack, iActNum, iVictim, iType, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(iAttack, 4)
    cl_duonet.netfunc.PacketAddI(iActNum, 2)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CStruckMonster(iVictim, iType, iHitPart, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddI(iHitPart, 1)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CRelife(iVictim, iType, oGame):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.DGameBroadCast(oGame)


def DN_GS2CMonsterActionSM(iMonster, iType, sArgsName, fArgsValue, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(9, 1)
    cl_duonet.netfunc.PacketAddI(iMonster, 4)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddSL(sArgsName, 1)
    cl_duonet.netfunc.PacketFloat(fArgsValue, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CRealDie(oGame, pid):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CBreakShield(iAttack, iVictim, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(11, 1)
    cl_duonet.netfunc.PacketAddI(iAttack, 4)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CBreakArmor(iAttack, iVictim, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(iAttack, 4)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CHatch(iVictim, iStatus, iHatchTime, oGame):
    cl_duonet.netfunc.PacketPrepare(52)
    cl_duonet.netfunc.PacketAddI(13, 1)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.PacketAddI(iStatus, 1)
    cl_duonet.netfunc.PacketAddI(iHatchTime, 2)
    cl_duonet.netfunc.DGameBroadCast(oGame)


def DN_GS2CTriggerBehavior(Owner, iItemID, iBehavior, iStop, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(Owner, 4)
    cl_duonet.netfunc.PacketAddI(iItemID, 4)
    cl_duonet.netfunc.PacketAddI(iBehavior, 4)
    cl_duonet.netfunc.PacketAddI(iStop, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CLevelNodeLoadOk(iScene, LevelID, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(iScene, 4)
    cl_duonet.netfunc.PacketAddI(LevelID, 4)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CLevelNodeGoalOk(iScene, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(iScene, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CAddTransferInfo(iScene, iNpc, iTrick, Difficult, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(iScene, 4)
    cl_duonet.netfunc.PacketAddI(iNpc, 4)
    cl_duonet.netfunc.PacketAddI(iTrick, 4)
    cl_duonet.netfunc.PacketAddI(Difficult, 1)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CRelifeConfirm(iRelifeIdx, iLeftTimes, iMaxTimes, iType, iRemainTime, iCost, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(iRelifeIdx, 4)
    cl_duonet.netfunc.PacketAddI(iLeftTimes, 1)
    cl_duonet.netfunc.PacketAddI(iMaxTimes, 1)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.PacketAddI(iCost, 2)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CQuitGame(pid, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(pid, 4)
    cl_duonet.netfunc.DGameBroadCast(oGame)


def DN_GS2CDisconnected(pid, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(7, 1)
    cl_duonet.netfunc.PacketAddI(pid, 4)
    cl_duonet.netfunc.DGameBroadCast(oGame)


def DN_GS2CPickUp(HeroID, iDrop, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(9, 1)
    cl_duonet.netfunc.PacketAddI(HeroID, 4)
    cl_duonet.netfunc.PacketAddI(iDrop, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CWarPaused(iPaused, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.PacketAddI(iPaused, 1)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CAddEffect(iScene, iEffectID, iShape, pos, vFace, vScale, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(11, 1)
    cl_duonet.netfunc.PacketAddI(iScene, 4)
    cl_duonet.netfunc.PacketAddI(iEffectID, 4)
    cl_duonet.netfunc.PacketAddI(iShape, 2)
    cl_duonet.netfunc.PacketPosFloat(pos)
    cl_duonet.netfunc.PacketPosFloat(vFace)
    cl_duonet.netfunc.PacketPosFloat(vScale)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CDeleteEffect(iScene, iEffectID, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(iScene, 4)
    cl_duonet.netfunc.PacketAddI(iEffectID, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CEnterWatch(HeroID, focus, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(13, 1)
    cl_duonet.netfunc.PacketAddI(HeroID, 4)
    cl_duonet.netfunc.PacketAddI(focus, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CWarStatus(iStatus, iFrame, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(14, 1)
    cl_duonet.netfunc.PacketAddI(iStatus, 1)
    cl_duonet.netfunc.PacketAddI(iFrame, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CDoubleHPBarUI(lstWarrior, iState, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(15, 1)
    cl_duonet.netfunc.PacketAddI(len(lstWarrior), 1)
    for iWarrior in lstWarrior:
        cl_duonet.netfunc.PacketAddI(iWarrior, 4)
    
    cl_duonet.netfunc.PacketAddI(iState, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CCircleSummonEffect(iSummon, lstPrefab, iState, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(16, 1)
    cl_duonet.netfunc.PacketAddI(iSummon, 4)
    cl_duonet.netfunc.PacketAddI(len(lstPrefab), 1)
    for iPrefab in lstPrefab:
        cl_duonet.netfunc.PacketAddI(iPrefab, 4)
    
    cl_duonet.netfunc.PacketAddI(iState, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CMapBuildSimMask(iBuild, iSimMark, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(17, 1)
    cl_duonet.netfunc.PacketAddI(iBuild, 4)
    cl_duonet.netfunc.PacketAddI(iSimMark, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CMonsterSuperInfo(iMonsterID, iMonsterAf, iAttrPlus, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(18, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketAddI(iMonsterAf, 4)
    cl_duonet.netfunc.PacketAddI(iAttrPlus, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CUpdateMiniMapPos(iLevel, iOperate, lstPos, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(19, 1)
    cl_duonet.netfunc.PacketAddI(iLevel, 4)
    cl_duonet.netfunc.PacketAddI(iOperate, 1)
    cl_duonet.netfunc.PacketAddI(len(lstPos), 1)
    for ID, iType, iShowMode, Pos in lstPos:
        cl_duonet.netfunc.PacketAddI(ID, 2)
        cl_duonet.netfunc.PacketAddI(iType, 1)
        cl_duonet.netfunc.PacketAddI(iShowMode, 1)
        cl_duonet.netfunc.PacketPosFloat(Pos)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CTeamInfo(lstMember, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(20, 1)
    cl_duonet.netfunc.PacketAddI(len(lstMember), 1)
    for HeroID, vPos, dx, dy, dz in lstMember:
        cl_duonet.netfunc.PacketAddI(HeroID, 4)
        cl_duonet.netfunc.PacketPosFloat(vPos)
        cl_duonet.netfunc.PacketAddI(dx, 1)
        cl_duonet.netfunc.PacketAddI(dy, 1)
        cl_duonet.netfunc.PacketAddI(dz, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CPlayType(iPlayType, iRound, iPlayMode, iCycle, lstMode, sExtraInfo, iSeasonNum, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(21, 1)
    cl_duonet.netfunc.PacketAddI(iPlayType, 1)
    cl_duonet.netfunc.PacketAddI(iRound, 1)
    cl_duonet.netfunc.PacketAddI(iPlayMode, 2)
    cl_duonet.netfunc.PacketAddI(iCycle, 1)
    cl_duonet.netfunc.PacketAddI(len(lstMode), 1)
    for iMode in lstMode:
        cl_duonet.netfunc.PacketAddI(iMode, 2)
    
    cl_duonet.netfunc.PacketMarshal(sExtraInfo, 2)
    cl_duonet.netfunc.PacketAddI(iSeasonNum, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CPlayTime(iFrame, iCounting, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(22, 1)
    cl_duonet.netfunc.PacketAddI(iFrame, 4)
    cl_duonet.netfunc.PacketAddI(iCounting, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateLevelRoomPos(iScene, RoomPos, lstLine, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(23, 1)
    cl_duonet.netfunc.PacketAddI(iScene, 4)
    cl_duonet.netfunc.PacketAddI(RoomPos, 1)
    cl_duonet.netfunc.PacketAddI(len(lstLine), 1)
    for sLine in lstLine:
        cl_duonet.netfunc.PacketAddSL(sLine, 1)
    
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CTriggerDestroyEffect(Owner, vPos, vFace, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(24, 1)
    cl_duonet.netfunc.PacketAddI(Owner, 4)
    cl_duonet.netfunc.PacketPosFloat(vPos)
    cl_duonet.netfunc.PacketPosFloat(vFace)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CNowInfo(sInfo, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(25, 1)
    cl_duonet.netfunc.PacketAddBinaryS(sInfo, 0)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMainCtrl(Hero, WarPlayer, PlayerCtrl, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(26, 1)
    cl_duonet.netfunc.PacketAddI(Hero, 4)
    cl_duonet.netfunc.PacketAddI(WarPlayer, 4)
    cl_duonet.netfunc.PacketAddI(len(PlayerCtrl), 1)
    for Player, Hero in PlayerCtrl.items():
        cl_duonet.netfunc.PacketAddLong(Player, 4)
        cl_duonet.netfunc.PacketAddI(Hero, 4)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CNotifyStartSkill(iPerformSID, iPerformID, iItemID, Args, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(27, 1)
    cl_duonet.netfunc.PacketAddI(iPerformSID, 2)
    cl_duonet.netfunc.PacketAddI(iPerformID, 4)
    cl_duonet.netfunc.PacketAddI(iItemID, 4)
    cl_duonet.netfunc.PacketAddI(len(Args), 1)
    for sKey, iVal in Args.items():
        cl_duonet.netfunc.PacketAddSL(sKey, 1)
        cl_duonet.netfunc.PacketAddI(iVal, 4)
    
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CLimitConvoy(sNotify, iRemainTime, iTotalTime, iNpc, iChallenge, iCurPathIndex, lstPathPos, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(28, 1)
    cl_duonet.netfunc.PacketAddPSL(sNotify, 1)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.PacketAddI(iTotalTime, 4)
    cl_duonet.netfunc.PacketAddI(iNpc, 4)
    cl_duonet.netfunc.PacketAddI(iChallenge, 1)
    cl_duonet.netfunc.PacketAddI(iCurPathIndex, 1)
    cl_duonet.netfunc.PacketAddI(len(lstPathPos), 1)
    for vPos in lstPathPos:
        cl_duonet.netfunc.PacketPosFloat(vPos)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CMonsterNotify(sNotify, iTime, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(29, 1)
    cl_duonet.netfunc.PacketAddPSL(sNotify, 1)
    cl_duonet.netfunc.PacketAddI(iTime, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CClearChallengeUI(iChallenge, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(30, 1)
    cl_duonet.netfunc.PacketAddI(iChallenge, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CLimitDefend(iChallenge, sNotify, iRemainTime, iTotalTime, iNpc, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(31, 1)
    cl_duonet.netfunc.PacketAddI(iChallenge, 1)
    cl_duonet.netfunc.PacketAddPSL(sNotify, 1)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.PacketAddI(iTotalTime, 4)
    cl_duonet.netfunc.PacketAddI(iNpc, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CTargetDefend(iChallenge, sNotify, iNow, iTotal, iNpc, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(32, 1)
    cl_duonet.netfunc.PacketAddI(iChallenge, 1)
    cl_duonet.netfunc.PacketAddPSL(sNotify, 1)
    cl_duonet.netfunc.PacketAddI(iNow, 4)
    cl_duonet.netfunc.PacketAddI(iTotal, 4)
    cl_duonet.netfunc.PacketAddI(iNpc, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CRelifeInfo(lstHeroInfo, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(33, 1)
    cl_duonet.netfunc.PacketAddI(len(lstHeroInfo), 1)
    for iHero, lstAllInfo in lstHeroInfo:
        cl_duonet.netfunc.PacketAddI(iHero, 4)
        cl_duonet.netfunc.PacketAddI(len(lstAllInfo), 1)
        for iType, iRestTimes, iTotalTimes in lstAllInfo:
            cl_duonet.netfunc.PacketAddI(iType, 1)
            cl_duonet.netfunc.PacketAddI(iRestTimes, 1)
            cl_duonet.netfunc.PacketAddI(iTotalTimes, 1)
        
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CStartChallenge(iChallenge, sNotify, iRemainTime, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(34, 1)
    cl_duonet.netfunc.PacketAddI(iChallenge, 1)
    cl_duonet.netfunc.PacketAddPSL(sNotify, 1)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CMainCtrlFace(dx, dy, dz, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(35, 1)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CPickFail(iPicker, iDrop, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(36, 1)
    cl_duonet.netfunc.PacketAddI(iPicker, 4)
    cl_duonet.netfunc.PacketAddI(iDrop, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CTriggerBehaviorStatus(Owner, iBehavior, iStep, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(37, 1)
    cl_duonet.netfunc.PacketAddI(Owner, 4)
    cl_duonet.netfunc.PacketAddI(iBehavior, 4)
    cl_duonet.netfunc.PacketAddI(iStep, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CTeamDamage(lstHeroDamage, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(38, 1)
    cl_duonet.netfunc.PacketAddI(len(lstHeroDamage), 1)
    for iHero, iDamage, iSeasonDamage, dType in lstHeroDamage:
        cl_duonet.netfunc.PacketAddI(iHero, 4)
        cl_duonet.netfunc.PacketAddLong(iDamage, 8)
        cl_duonet.netfunc.PacketAddLong(iSeasonDamage, 8)
        cl_duonet.netfunc.PacketAddI(len(dType), 1)
        for iType, dArgs in dType.items():
            cl_duonet.netfunc.PacketAddI(iType, 1)
            cl_duonet.netfunc.PacketAddI(len(dArgs), 1)
            for iKey, iValue in dArgs.items():
                cl_duonet.netfunc.PacketAddI(iKey, 2)
                cl_duonet.netfunc.PacketAddLong(iValue, 8)
            
        
    
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CStartRescue(iRescuer, iTarget, iTime, iStartFrame, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(39, 1)
    cl_duonet.netfunc.PacketAddI(iRescuer, 4)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iTime, 2)
    cl_duonet.netfunc.PacketAddI(iStartFrame, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CStopRescue(iRescuer, iTarget, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(40, 1)
    cl_duonet.netfunc.PacketAddI(iRescuer, 4)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CBreakRescue(iRescuer, iTarget, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(41, 1)
    cl_duonet.netfunc.PacketAddI(iRescuer, 4)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CDayTrialItemInfo(lstItem, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(42, 1)
    cl_duonet.netfunc.PacketAddI(len(lstItem), 1)
    for iItem, lstArgs in lstItem:
        cl_duonet.netfunc.PacketAddI(iItem, 2)
        cl_duonet.netfunc.PacketAddI(len(lstArgs), 1)
        for iArgs in lstArgs:
            cl_duonet.netfunc.PacketAddI(iArgs, 4)
        
    
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CDayTrialInfo(iThem, iGood, iBad, lstTheme, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(43, 1)
    cl_duonet.netfunc.PacketAddI(iThem, 2)
    cl_duonet.netfunc.PacketAddI(iGood, 2)
    cl_duonet.netfunc.PacketAddI(iBad, 2)
    cl_duonet.netfunc.PacketAddI(len(lstTheme), 1)
    for iItem in lstTheme:
        cl_duonet.netfunc.PacketAddI(iItem, 2)
    
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CEliteCreateTip(iScene, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(44, 1)
    cl_duonet.netfunc.PacketAddI(iScene, 4)
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CJumpFigure(iReason, iTarget, iCnt, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(46, 1)
    cl_duonet.netfunc.PacketAddI(iReason, 2)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iCnt, 4)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CUpdateChallenge(iContinueTime, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(47, 1)
    cl_duonet.netfunc.PacketAddI(iContinueTime, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CForbidRule(iRule, sKey, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(48, 1)
    cl_duonet.netfunc.PacketAddI(iRule, 2)
    cl_duonet.netfunc.PacketAddSL(sKey, 2)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUnForbidRule(iRule, sKey, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(49, 1)
    cl_duonet.netfunc.PacketAddI(iRule, 2)
    cl_duonet.netfunc.PacketAddSL(sKey, 2)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CSightPhaseTime(iPhase, iRemainTime, sTitle, dOption, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(50, 1)
    cl_duonet.netfunc.PacketAddI(iPhase, 1)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.PacketAddPSL(sTitle, 2)
    cl_duonet.netfunc.PacketAddI(len(dOption), 1)
    for iOption, sOption in dOption.items():
        cl_duonet.netfunc.PacketAddI(iOption, 1)
        cl_duonet.netfunc.PacketAddPSL(sOption, 2)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CRecycleDropInfo(lstDropType, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(51, 1)
    cl_duonet.netfunc.PacketAddI(len(lstDropType), 1)
    for iType in lstDropType:
        cl_duonet.netfunc.PacketAddI(iType, 4)
    
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CRecycleDropResult(iTarget, iResult, iCashType, iPrice, iHero, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(52, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iResult, 1)
    cl_duonet.netfunc.PacketAddI(iCashType, 1)
    cl_duonet.netfunc.PacketAddI(iPrice, 4)
    cl_duonet.netfunc.PacketAddI(iHero, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CCallForHelp(iHero, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(53, 1)
    cl_duonet.netfunc.PacketAddI(iHero, 4)
    cl_duonet.netfunc.DGameBroadCast(oGame)


def DN_GS2CPerformanceInfo(iFlag, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(54, 1)
    cl_duonet.netfunc.PacketAddI(iFlag, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CConfirmFunc(iConfirm, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(55, 1)
    cl_duonet.netfunc.PacketAddI(iConfirm, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CFightInfo(sWarMask, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(56, 1)
    cl_duonet.netfunc.PacketAddSL(sWarMask, 2)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CSightScore(iScore, iCurScore, iHitCnt, iVictim, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(57, 1)
    cl_duonet.netfunc.PacketAddI(iScore, 2)
    cl_duonet.netfunc.PacketAddI(iCurScore, 2)
    cl_duonet.netfunc.PacketAddI(iHitCnt, 2)
    cl_duonet.netfunc.PacketAddI(iVictim, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CMonsterAdditionInfo(iMonsterID, lstAffiliateID, oGame, iScene):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(58, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketAddI(len(lstAffiliateID), 1)
    for iAffiliateID in lstAffiliateID:
        cl_duonet.netfunc.PacketAddI(iAffiliateID, 4)
    
    cl_duonet.netfunc.DGameSceneBroadCast(oGame, iScene)


def DN_GS2CReceivedDamRecord(iMonsterID, iTotal, iDps, iMaxDam, oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(59, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketAddLong(iTotal, 8)
    cl_duonet.netfunc.PacketAddLong(iDps, 8)
    cl_duonet.netfunc.PacketAddLong(iMaxDam, 8)
    cl_duonet.netfunc.DGameBroadCast(oGame)


def DN_GS2CSightConfig(dRewardConfig, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(60, 1)
    cl_duonet.netfunc.PacketAddI(len(dRewardConfig), 1)
    for iScore, iLevel in dRewardConfig.items():
        cl_duonet.netfunc.PacketAddI(iScore, 2)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CSkipCG(iHero, iBehavior, iSkip, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(61, 1)
    cl_duonet.netfunc.PacketAddI(iHero, 4)
    cl_duonet.netfunc.PacketAddI(iBehavior, 4)
    cl_duonet.netfunc.PacketAddI(iSkip, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CTriggerCG(Owner, iCanSkip, iBehavior, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(62, 1)
    cl_duonet.netfunc.PacketAddI(Owner, 4)
    cl_duonet.netfunc.PacketAddI(iCanSkip, 1)
    cl_duonet.netfunc.PacketAddI(iBehavior, 4)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CRefreshItemChecked(iItemID, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(63, 1)
    cl_duonet.netfunc.PacketAddI(iItemID, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CTransferHideLevelInfo(iLevel, iLeftTimes, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(65, 1)
    cl_duonet.netfunc.PacketAddI(iLevel, 4)
    cl_duonet.netfunc.PacketAddI(iLeftTimes, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateSuitCondtion(iTarget, lstSuit, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(66, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(len(lstSuit), 1)
    for iSuit, lstCondtion, iNum in lstSuit:
        cl_duonet.netfunc.PacketAddI(iSuit, 4)
        cl_duonet.netfunc.PacketAddI(len(lstCondtion), 1)
        for iCondtion, iMeet, iMain in lstCondtion:
            cl_duonet.netfunc.PacketAddI(iCondtion, 2)
            cl_duonet.netfunc.PacketAddI(iMeet, 1)
            cl_duonet.netfunc.PacketAddI(iMain, 1)
        
        cl_duonet.netfunc.PacketAddI(iNum, 2)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CSuitMap(lstMap, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(67, 1)
    cl_duonet.netfunc.PacketAddI(len(lstMap), 1)
    for iCondType, dInfo in lstMap:
        cl_duonet.netfunc.PacketAddI(iCondType, 1)
        cl_duonet.netfunc.PacketAddI(len(dInfo), 1)
        for iKey, lstSuit in dInfo.items():
            cl_duonet.netfunc.PacketAddI(iKey, 4)
            cl_duonet.netfunc.PacketAddI(len(lstSuit), 1)
            for iSuit in lstSuit:
                cl_duonet.netfunc.PacketAddI(iSuit, 2)
            
        
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CLastActionNum(iLastActNum, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(68, 1)
    cl_duonet.netfunc.PacketAddI(iLastActNum, 2)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CHeroUpGradeInfoRefresh(iGrade, iExperience, iSkillpoint, iUpNeed, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(69, 1)
    cl_duonet.netfunc.PacketAddI(iGrade, 2)
    cl_duonet.netfunc.PacketAddI(iExperience, 4)
    cl_duonet.netfunc.PacketAddI(iSkillpoint, 2)
    cl_duonet.netfunc.PacketAddI(iUpNeed, 4)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CChooseRewardItem(iMenuIdx, iItemtype, lstItem, dExtraOption, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(70, 1)
    cl_duonet.netfunc.PacketAddI(iMenuIdx, 2)
    cl_duonet.netfunc.PacketAddI(iItemtype, 1)
    cl_duonet.netfunc.PacketAddI(len(lstItem), 1)
    for attr in lstItem:
        cl_duonet.netfunc.PacketAttr(attr)
    
    cl_duonet.netfunc.PacketAddI(len(dExtraOption), 1)
    for iOption, iValue in dExtraOption.items():
        cl_duonet.netfunc.PacketAddI(iOption, 1)
        cl_duonet.netfunc.PacketAddI(iValue, 4)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CTriggerArea(Owner, iType, vPos, vHalfExt, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(71, 1)
    cl_duonet.netfunc.PacketAddI(Owner, 4)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketPosFloat(vPos)
    cl_duonet.netfunc.PacketPosFloat(vHalfExt)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CPhaseInfo(iPhase, iIsFinish, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(72, 1)
    cl_duonet.netfunc.PacketAddI(iPhase, 2)
    cl_duonet.netfunc.PacketAddI(iIsFinish, 1)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CTriggerAnimator(iTarget, iType, sArgsName, fArgsValue, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(73, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddSL(sArgsName, 1)
    cl_duonet.netfunc.PacketFloat(fArgsValue, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CPreviewUpgradeWeaponInfo(iWeapon, arr, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(74, 1)
    cl_duonet.netfunc.PacketAddI(iWeapon, 4)
    cl_duonet.netfunc.PacketAttr(arr)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CPrepareTimeInfo(iRemainTime, iTotalTime, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(75, 1)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 4)
    cl_duonet.netfunc.PacketAddI(iTotalTime, 4)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CUpdateSceneIcon(iLevel, iOperate, lstIcon, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(76, 1)
    cl_duonet.netfunc.PacketAddI(iLevel, 4)
    cl_duonet.netfunc.PacketAddI(iOperate, 1)
    cl_duonet.netfunc.PacketAddI(len(lstIcon), 1)
    for iIcon, iType, vPos, lstArgs in lstIcon:
        cl_duonet.netfunc.PacketAddI(iIcon, 4)
        cl_duonet.netfunc.PacketAddI(iType, 1)
        cl_duonet.netfunc.PacketPosFloat(vPos)
        cl_duonet.netfunc.PacketAddI(len(lstArgs), 1)
        for sArgsName, iValue in lstArgs:
            cl_duonet.netfunc.PacketAddSL(sArgsName, 1)
            cl_duonet.netfunc.PacketAddI(iValue, 2)
        
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CUpdatePrioritySuit(lstPrioritySuit, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(77, 1)
    cl_duonet.netfunc.PacketAddI(len(lstPrioritySuit), 1)
    for iSuit in lstPrioritySuit:
        cl_duonet.netfunc.PacketAddI(iSuit, 4)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMonsterUseRelic(iMonsterID, lstRelic, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(78, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketAddI(len(lstRelic), 1)
    for iRelicSID in lstRelic:
        cl_duonet.netfunc.PacketAddI(iRelicSID, 2)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CUpdateQuality(iMaxCnt, iSkillClearFlag, lstQuality, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(79, 1)
    cl_duonet.netfunc.PacketAddI(iMaxCnt, 1)
    cl_duonet.netfunc.PacketAddI(iSkillClearFlag, 1)
    cl_duonet.netfunc.PacketAddI(len(lstQuality), 1)
    for iID, iQuality in lstQuality:
        cl_duonet.netfunc.PacketAddI(iID, 2)
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMonsterRelicRefreshCnt(iMonsterID, iRelicSID, iCount, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(80, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketAddI(iRelicSID, 2)
    cl_duonet.netfunc.PacketAddI(iCount, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CUpdateQualityProb(lstQualityProb, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(81, 1)
    cl_duonet.netfunc.PacketAddI(len(lstQualityProb), 1)
    for iQuality, iProb in lstQualityProb:
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
        cl_duonet.netfunc.PacketAddI(iProb, 2)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMonsterSpawnFlaw(lstFlaw, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(82, 1)
    cl_duonet.netfunc.PacketAddI(len(lstFlaw), 1)
    for iMonsterID, iFlawID, iTime, iHitCnt, iSize, iIsWeakness in lstFlaw:
        cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
        cl_duonet.netfunc.PacketAddI(iFlawID, 1)
        cl_duonet.netfunc.PacketAddI(iTime, 2)
        cl_duonet.netfunc.PacketAddI(iHitCnt, 1)
        cl_duonet.netfunc.PacketAddI(iSize, 2)
        cl_duonet.netfunc.PacketAddI(iIsWeakness, 1)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMonsterClearFlaw(iMonsterID, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(83, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMonsterKillLine(lstKillLine, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(84, 1)
    cl_duonet.netfunc.PacketAddI(len(lstKillLine), 1)
    for iMonsterID, iBaseKillLine, iUnbalanceKillLine, iMaxKillLine in lstKillLine:
        cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
        cl_duonet.netfunc.PacketAddI(iBaseKillLine, 2)
        cl_duonet.netfunc.PacketAddI(iUnbalanceKillLine, 2)
        cl_duonet.netfunc.PacketAddI(iMaxKillLine, 2)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CHeroKillLine(iBaseKillLine, iUnbalanceKillLine, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(85, 1)
    cl_duonet.netfunc.PacketAddI(iBaseKillLine, 4)
    cl_duonet.netfunc.PacketAddI(iUnbalanceKillLine, 4)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CSeasonTaskData(dTask, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(86, 1)
    cl_duonet.netfunc.PacketAddI(len(dTask), 1)
    for SID, lstTaskInfo in dTask.items():
        cl_duonet.netfunc.PacketAddI(SID, 2)
        cl_duonet.netfunc.PacketAddI(len(lstTaskInfo), 1)
        for iCurValue, iTotalValue, lstExtInfo in lstTaskInfo:
            cl_duonet.netfunc.PacketAddI(iCurValue, 4)
            cl_duonet.netfunc.PacketAddI(iTotalValue, 4)
            cl_duonet.netfunc.PacketAddI(len(lstExtInfo), 1)
            for iType, lstVal in lstExtInfo:
                cl_duonet.netfunc.PacketAddI(iType, 1)
                cl_duonet.netfunc.PacketAddI(len(lstVal), 1)
                for iVal, iCurVal, iMaxVal in lstVal:
                    cl_duonet.netfunc.PacketAddI(iVal, 4)
                    cl_duonet.netfunc.PacketAddI(iCurVal, 4)
                    cl_duonet.netfunc.PacketAddI(iMaxVal, 4)
                
            
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMonsterKillLineAddition(iMonsterID, iKillLineAddition, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(87, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketAddLong(iKillLineAddition, 8)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CEndlessInfo(iCurLevelNum, iPassLevelNum, iKillBossNum, iResistance, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(88, 1)
    cl_duonet.netfunc.CustomPacketAddI(iCurLevelNum, 2)
    cl_duonet.netfunc.CustomPacketAddI(iPassLevelNum, 2)
    cl_duonet.netfunc.CustomPacketAddI(iKillBossNum, 2)
    cl_duonet.netfunc.PacketAddI(iResistance, 2)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CEndlessTime(iStatus, iOverFrame, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(89, 1)
    cl_duonet.netfunc.PacketAddI(iStatus, 1)
    cl_duonet.netfunc.PacketVarInt(iOverFrame)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CEndlessChangeTime(iTime, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(90, 1)
    cl_duonet.netfunc.PacketAddI(iTime, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CChooseRelicTalent(iMenuIdx, iType, lstPerform, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(91, 1)
    cl_duonet.netfunc.PacketAddI(iMenuIdx, 2)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddI(len(lstPerform), 1)
    for iPerform in lstPerform:
        cl_duonet.netfunc.PacketAddI(iPerform, 2)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CAddRelicTalent(iType, iPerform, iLevel, iHero, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(92, 1)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddI(iPerform, 2)
    cl_duonet.netfunc.PacketAddI(iLevel, 1)
    cl_duonet.netfunc.PacketAddI(iHero, 4)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CMonsterRemoveFlaw(iMonsterID, iFlawID, iEffect, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(93, 1)
    cl_duonet.netfunc.PacketAddI(iMonsterID, 4)
    cl_duonet.netfunc.PacketAddI(iFlawID, 1)
    cl_duonet.netfunc.PacketAddI(iEffect, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CSeasonTaskDone(lstTask, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(94, 1)
    cl_duonet.netfunc.PacketAddI(len(lstTask), 1)
    for SID, iShowValue in lstTask:
        cl_duonet.netfunc.PacketAddI(SID, 2)
        cl_duonet.netfunc.PacketAddI(iShowValue, 4)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CChangeExtraPickUpRule(lstRule, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(95, 1)
    cl_duonet.netfunc.PacketAddI(len(lstRule), 1)
    for iRule in lstRule:
        cl_duonet.netfunc.PacketAddI(iRule, 1)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateDeviceCompLevel(iSID, iLevel, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(96, 1)
    cl_duonet.netfunc.PacketAddI(iSID, 2)
    cl_duonet.netfunc.PacketAddI(iLevel, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateDeviceCompPos(iSID, iPos, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(97, 1)
    cl_duonet.netfunc.PacketAddI(iSID, 2)
    cl_duonet.netfunc.PacketAddI(iPos, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CDeviceCompMaxPos(iMaxPos, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(98, 1)
    cl_duonet.netfunc.PacketAddI(iMaxPos, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CChooseDevice(iMenuIdx, lstDevice, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(99, 1)
    cl_duonet.netfunc.PacketAddI(iMenuIdx, 2)
    cl_duonet.netfunc.PacketAddI(len(lstDevice), 1)
    for iSID in lstDevice:
        cl_duonet.netfunc.PacketAddI(iSID, 2)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CAddDevice(iHero, iSID, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(100, 1)
    cl_duonet.netfunc.PacketAddI(iHero, 4)
    cl_duonet.netfunc.PacketAddI(iSID, 2)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CSendThunderStageInfo(iStage, iTime, iRemainTime, lstPos, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(102, 1)
    cl_duonet.netfunc.PacketAddI(iStage, 1)
    cl_duonet.netfunc.PacketAddI(iTime, 2)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 2)
    cl_duonet.netfunc.PacketAddI(len(lstPos), 1)
    for vPos, fRadius in lstPos:
        cl_duonet.netfunc.PacketPosFloat(vPos)
        cl_duonet.netfunc.PacketFloat(fRadius, 4)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CSwitchFuncMode(lstMode, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(103, 1)
    cl_duonet.netfunc.PacketAddI(len(lstMode), 1)
    for iMode, dInfo in lstMode:
        cl_duonet.netfunc.PacketAddI(iMode, 1)
        cl_duonet.netfunc.PacketAddI(len(dInfo), 1)
        for sKey, iVal in dInfo.items():
            cl_duonet.netfunc.PacketAddSL(sKey, 1)
            cl_duonet.netfunc.PacketAddI(iVal, 4)
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateAllDeviceCompInfo(dDeviceCompInfo, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(104, 1)
    cl_duonet.netfunc.PacketAddI(len(dDeviceCompInfo), 1)
    for iSID, lstInfo in dDeviceCompInfo.items():
        cl_duonet.netfunc.PacketAddI(iSID, 2)
        cl_duonet.netfunc.PacketAddI(len(lstInfo), 1)
        for iLevel, iPos in lstInfo:
            cl_duonet.netfunc.PacketAddI(iLevel, 1)
            cl_duonet.netfunc.PacketAddI(iPos, 1)
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CConquerState(iStage, iConqueror, iTarget, iTotalProgress, iCurProgress, iConquerRate, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(105, 1)
    cl_duonet.netfunc.PacketAddI(iStage, 1)
    cl_duonet.netfunc.PacketAddI(iConqueror, 4)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iTotalProgress, 2)
    cl_duonet.netfunc.PacketAddI(iCurProgress, 2)
    cl_duonet.netfunc.PacketAddI(iConquerRate, 2)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CMonsterWeakInfo(iTarget, iTotalTime, iRemainTime, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(106, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iTotalTime, 2)
    cl_duonet.netfunc.PacketAddI(iRemainTime, 2)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CConquerChallengeInfo(iStage, iTarget, iPlus, iPerform, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(107, 1)
    cl_duonet.netfunc.PacketAddI(iStage, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(iPlus, 1)
    cl_duonet.netfunc.PacketAddI(iPerform, 2)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CCustomPerformData(dPerform, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(108, 1)
    cl_duonet.netfunc.PacketAddI(len(dPerform), 1)
    for iPerformID, dData in dPerform.items():
        cl_duonet.netfunc.PacketAddI(iPerformID, 2)
        cl_duonet.netfunc.PacketAddI(len(dData), 1)
        for sKey, iVal in dData.items():
            cl_duonet.netfunc.PacketAddSL(sKey, 1)
            cl_duonet.netfunc.PacketAddI(iVal, 4)
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CIsFirstCycle(iIsFirstCycle, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(109, 1)
    cl_duonet.netfunc.PacketAddI(iIsFirstCycle, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateDataUI(iType, ExInfo, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(110, 1)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketMarshal(ExInfo, 2)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CSeasonFunc(lstFunc, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(111, 1)
    cl_duonet.netfunc.PacketAddI(len(lstFunc), 1)
    for iFunc in lstFunc:
        cl_duonet.netfunc.PacketAddI(iFunc, 1)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CCustomReconnetion(oGame):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(112, 1)
    cl_duonet.netfunc.DGameBroadCast(oGame)


def DN_GS2CObstacleAlienationRoundInfo(iRoundMax, iCurrentRound, iRoundTime, lstInfo, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(113, 1)
    cl_duonet.netfunc.PacketAddI(iRoundMax, 1)
    cl_duonet.netfunc.PacketAddI(iCurrentRound, 1)
    cl_duonet.netfunc.PacketAddI(iRoundTime, 2)
    cl_duonet.netfunc.PacketAddI(len(lstInfo), 1)
    for iObstacle in lstInfo:
        cl_duonet.netfunc.PacketAddI(iObstacle, 4)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CUpdateSeasonSuitCondtion(iTarget, lstSuit, iClearData, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(114, 1)
    cl_duonet.netfunc.PacketAddI(iTarget, 4)
    cl_duonet.netfunc.PacketAddI(len(lstSuit), 1)
    for iSuit, lstCondtion, iNum, iGrade, iFusedTimes in lstSuit:
        cl_duonet.netfunc.PacketAddI(iSuit, 4)
        cl_duonet.netfunc.PacketAddI(len(lstCondtion), 1)
        for iCondtion, iMeet, iMain in lstCondtion:
            cl_duonet.netfunc.PacketAddI(iCondtion, 2)
            cl_duonet.netfunc.PacketAddI(iMeet, 1)
            cl_duonet.netfunc.PacketAddI(iMain, 1)
        
        cl_duonet.netfunc.PacketAddI(iNum, 2)
        cl_duonet.netfunc.PacketAddI(iGrade, 1)
        cl_duonet.netfunc.PacketAddI(iFusedTimes, 1)
    
    cl_duonet.netfunc.PacketAddI(iClearData, 1)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CSeasonSuitMap(lstMap, dGradeInfo, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(115, 1)
    cl_duonet.netfunc.PacketAddI(len(lstMap), 1)
    for iCondType, dInfo in lstMap:
        cl_duonet.netfunc.PacketAddI(iCondType, 1)
        cl_duonet.netfunc.PacketAddI(len(dInfo), 1)
        for iKey, lstSuit in dInfo.items():
            cl_duonet.netfunc.PacketAddI(iKey, 4)
            cl_duonet.netfunc.PacketAddI(len(lstSuit), 1)
            for iSuit in lstSuit:
                cl_duonet.netfunc.PacketAddI(iSuit, 2)
            
        
    
    cl_duonet.netfunc.PacketAddI(len(dGradeInfo), 1)
    for iSuit, dGradeInfo in dGradeInfo.items():
        cl_duonet.netfunc.PacketAddI(iSuit, 2)
        cl_duonet.netfunc.PacketAddI(len(dGradeInfo), 1)
        for iGrade, iNum in dGradeInfo.items():
            cl_duonet.netfunc.PacketAddI(iGrade, 1)
            cl_duonet.netfunc.PacketAddI(iNum, 1)
        
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CSeasonSuitOptionInfo(iOption, iHeroID, lstResult, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(116, 1)
    cl_duonet.netfunc.PacketAddI(iOption, 1)
    cl_duonet.netfunc.PacketAddI(iHeroID, 4)
    cl_duonet.netfunc.PacketAddI(len(lstResult), 1)
    for iResult in lstResult:
        cl_duonet.netfunc.PacketAddI(iResult, 4)
    
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CShowDamageInfo(lstInfo, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(117, 1)
    cl_duonet.netfunc.PacketAddI(len(lstInfo), 1)
    for lstDamInfo in lstInfo:
        cl_duonet.netfunc.PacketAddI(len(lstDamInfo), 1)
        for iValue in lstDamInfo:
            cl_duonet.netfunc.PacketAddI(iValue, 4)
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateSignRelic(lstSignRelic, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(118, 1)
    cl_duonet.netfunc.PacketAddI(len(lstSignRelic), 1)
    for iRelicSID in lstSignRelic:
        cl_duonet.netfunc.PacketAddI(iRelicSID, 2)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CMarkSeasonSuit(dMarkSuit, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(119, 1)
    cl_duonet.netfunc.PacketAddI(len(dMarkSuit), 1)
    for iSID, iVal in dMarkSuit.items():
        cl_duonet.netfunc.PacketAddI(iSID, 2)
        cl_duonet.netfunc.PacketAddI(iVal, 1)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateSeasonSuitFusedTimes(iSuit, iFusedTimes, iGrade, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(120, 1)
    cl_duonet.netfunc.PacketAddI(iSuit, 2)
    cl_duonet.netfunc.PacketAddI(iFusedTimes, 1)
    cl_duonet.netfunc.PacketAddI(iGrade, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateSeasonSuitReduceInfo(dSuitReduceInfo, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(121, 1)
    cl_duonet.netfunc.PacketAddI(len(dSuitReduceInfo), 1)
    for iTriggerSuit, iReduceSuit in dSuitReduceInfo.items():
        cl_duonet.netfunc.PacketAddI(iTriggerSuit, 2)
        cl_duonet.netfunc.PacketAddI(iReduceSuit, 2)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CSeasonSuitPerformStart(iSID, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(122, 1)
    cl_duonet.netfunc.PacketAddI(iSID, 2)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CShowSuitTempList(iCurSuitTemp, lstSuitTemp, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(123, 1)
    cl_duonet.netfunc.PacketAddI(iCurSuitTemp, 2)
    cl_duonet.netfunc.PacketAddI(len(lstSuitTemp), 1)
    for iSuitTemp, iCardPackID, lstSuitTemp in lstSuitTemp:
        cl_duonet.netfunc.PacketAddI(iSuitTemp, 2)
        cl_duonet.netfunc.PacketAddI(iCardPackID, 2)
        cl_duonet.netfunc.PacketAddI(len(lstSuitTemp), 1)
        for iSuit in lstSuitTemp:
            cl_duonet.netfunc.PacketAddI(iSuit, 2)
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CSetSuitTempResult(iSuitTemp, iResult, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(124, 1)
    cl_duonet.netfunc.PacketAddI(iSuitTemp, 2)
    cl_duonet.netfunc.PacketAddI(iResult, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CRealDiedRelifeConfirm(iCost, oGame, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(125, 1)
    cl_duonet.netfunc.PacketAddI(iCost, 2)
    cl_duonet.netfunc.DGamePacketSend(oGame, pid)


def DN_GS2CMonsterMaxCreateCnt(iCount, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(126, 1)
    cl_duonet.netfunc.PacketAddI(iCount, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CUpdateUI(iType, iOperate, sMsg, ExInfo, oGame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(127, 1)
    cl_duonet.netfunc.PacketAddI(iType, 1)
    cl_duonet.netfunc.PacketAddI(iOperate, 1)
    cl_duonet.netfunc.PacketAddPSL(sMsg, 1)
    cl_duonet.netfunc.PacketMarshal(ExInfo, 2)
    cl_duonet.netfunc.DGameSendToPlayers(oGame, dPlayer)


def DN_GS2CShowDetailDam(lstDetailDam, pid):
    cl_duonet.netfunc.PacketPrepare(53)
    cl_duonet.netfunc.PacketAddI(128, 1)
    cl_duonet.netfunc.PacketAddI(len(lstDetailDam), 1)
    for iType, iTotalDam, iDps, lstInfo in lstDetailDam:
        cl_duonet.netfunc.PacketAddI(iType, 1)
        cl_duonet.netfunc.PacketAddLong(iTotalDam, 8)
        cl_duonet.netfunc.PacketAddLong(iDps, 8)
        cl_duonet.netfunc.PacketAddI(len(lstInfo), 1)
        for sPerform, iDam in lstInfo:
            cl_duonet.netfunc.PacketAddSL(sPerform, 1)
            cl_duonet.netfunc.PacketAddLong(iDam, 8)
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CFace(Target, dx, dy, dz, Time, oGame, iScene, pid):
    cl_duonet.netfunc.PacketPrepare(54)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketAddI(dx, 1)
    cl_duonet.netfunc.PacketAddI(dy, 1)
    cl_duonet.netfunc.PacketAddI(dz, 1)
    cl_duonet.netfunc.PacketAddI(Time, 2)
    cl_duonet.netfunc.DGameSceneBroadCastExclude(oGame, iScene, pid)


def DN_GS2CFaceTarget(Target, Victim, Time, dPlayer):
    cl_duonet.netfunc.PacketPrepare(55)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketAddI(Victim, 4)
    cl_duonet.netfunc.PacketAddI(Time, 2)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CConstantFaceTarget(Target, Victim, TurnSpeed, dPlayer):
    cl_duonet.netfunc.PacketPrepare(55)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(Target, 4)
    cl_duonet.netfunc.PacketAddI(Victim, 4)
    cl_duonet.netfunc.PacketAddI(TurnSpeed, 2)
    cl_duonet.netfunc.SendToPlayers(dPlayer)


def DN_GS2CWarNewPing(iPingIdx, pid):
    cl_duonet.netfunc.PacketPrepare(57)
    cl_duonet.netfunc.PacketAddI(iPingIdx, 1)
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CTaskStatus(lstTask, pid):
    cl_duonet.netfunc.PacketPrepare(58)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(len(lstTask), 1)
    for iID, iSID, iTargetSID, iStatu in lstTask:
        cl_duonet.netfunc.PacketAddI(iID, 4)
        cl_duonet.netfunc.PacketAddI(iSID, 2)
        cl_duonet.netfunc.PacketAddI(iTargetSID, 2)
        cl_duonet.netfunc.PacketAddI(iStatu, 1)
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_GS2CTaskStat(lstTask, pid):
    cl_duonet.netfunc.PacketPrepare(58)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(len(lstTask), 1)
    for iID, lstStats in lstTask:
        cl_duonet.netfunc.PacketAddI(iID, 4)
        cl_duonet.netfunc.PacketAddI(len(lstStats), 1)
        for iIdx, iCurValue in lstStats:
            cl_duonet.netfunc.PacketAddI(iIdx, 1)
            cl_duonet.netfunc.PacketAddI(iCurValue, 1)
        
    
    cl_duonet.netfunc.PacketSend(pid)


def DN_C2GSPickUp(who):
    iDrop = cl_duonet.netfunc.UnpackInt(4)
    iPos = cl_duonet.netfunc.UnpackInt(1)
    iPickType = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSPickUp(who, iDrop, iPos, iPickType)


def DN_C2GSResetSpoolup(who):
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSResetSpoolup(who, iWeapon)


def DN_C2GSSnipe(who):
    iOpen = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSSnipe(who, iOpen)


def DN_C2GSHaltAction(who):
    iActNum = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSHaltAction(who, iActNum)


def DN_C2GSRelifeAnswer(who):
    iRelifeIdx = cl_duonet.netfunc.UnpackInt(4)
    iAnswer = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSRelifeAnswer(who, iRelifeIdx, iAnswer)


def DN_C2GSEnterWatch(who):
    iConfirm = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSEnterWatch(who, iConfirm)


def DN_C2GSSwitchWeaponAttPF(who):
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    iPerformIdx = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSSwitchWeaponAttPF(who, iWeapon, iPerformIdx)


def DN_C2GSRemoveBeaconSummon(who):
    iSummon = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSRemoveBeaconSummon(who, iSummon)


def DN_C2GSTriggerBehavior(who):
    iBehavior = cl_duonet.netfunc.UnpackInt(4)
    iStop = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSTriggerBehavior(who, iBehavior, iStop)


def DN_C2GSTriggerCartoonList(who):
    lstCartoon = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iActNum = cl_duonet.netfunc.UnpackInt(2)
        iCartoonID = cl_duonet.netfunc.UnpackInt(2)
        lstCartoon.append((iActNum, iCartoonID))
    
    cl_cnetwar.C2GSTriggerCartoonList(who, lstCartoon)


def DN_C2GSReplaceWeapon(who):
    iDrop = cl_duonet.netfunc.UnpackInt(4)
    iFromPos = cl_duonet.netfunc.UnpackInt(1)
    iToPos = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSReplaceWeapon(who, iDrop, iFromPos, iToPos)


def DN_C2GSSwitchWatch(who):
    iTarger = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSSwitchWatch(who, iTarger)


def DN_C2GSNowInfo(who):
    cl_cnetwar.C2GSNowInfo(who)


def DN_C2GSWeaponLockTarget(who):
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    iKey = cl_duonet.netfunc.UnpackInt(4)
    lstTarget = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iTarget = cl_duonet.netfunc.UnpackInt(4)
        lstTarget.append(iTarget)
    
    cl_cnetwar.C2GSWeaponLockTarget(who, iWeapon, iKey, lstTarget)


def DN_C2GSTeamDamage(who):
    cl_cnetwar.C2GSTeamDamage(who)


def DN_C2GSStartRescue(who):
    iTarget = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSStartRescue(who, iTarget)


def DN_C2GSBreakRescue(who):
    iRescuer = cl_duonet.netfunc.UnpackInt(4)
    iTarget = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSBreakRescue(who, iRescuer, iTarget)


def DN_C2GSSaveInfo(who):
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    iReset = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSSaveInfo(who, iWeapon, iReset)


def DN_C2GSRelifeSetPhase(who):
    iTarget = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSRelifeSetPhase(who, iTarget)


def DN_C2GSChooseOption(who):
    iOption = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSChooseOption(who, iOption)


def DN_C2GSCallForHelp(who):
    cl_cnetwar.C2GSCallForHelp(who)


def DN_C2GSReportFPS(who):
    iLevel = cl_duonet.netfunc.UnpackInt(4)
    iAve = cl_duonet.netfunc.UnpackInt(1)
    iBelowLowRatio = cl_duonet.netfunc.UnpackInt(2)
    iLowRatio = cl_duonet.netfunc.UnpackInt(2)
    iMidRatio = cl_duonet.netfunc.UnpackInt(2)
    iHighRatio = cl_duonet.netfunc.UnpackInt(2)
    iAboveHighRatio = cl_duonet.netfunc.UnpackInt(2)
    iGear = cl_duonet.netfunc.UnpackInt(1)
    iMemoryUsage = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSReportFPS(who, iLevel, iAve, iBelowLowRatio, iLowRatio, iMidRatio, iHighRatio, iAboveHighRatio, iGear, iMemoryUsage)


def DN_C2GSRecycleDrop(who):
    iDrop = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSRecycleDrop(who, iDrop)


def DN_C2GSCheckImmortal(who):
    iImmortal = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSCheckImmortal(who, iImmortal)


def DN_C2GSClientEvent(who):
    iType = cl_duonet.netfunc.UnpackInt(1)
    lstKey = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iButton = cl_duonet.netfunc.UnpackInt(2)
        lstKey.append(iButton)
    
    cl_cnetwar.C2GSClientEvent(who, iType, lstKey)


def DN_C2GSSkipCG(who):
    iBehavior = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSSkipCG(who, iBehavior)


def DN_C2GSSetTeamPF(who):
    iOpen = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSSetTeamPF(who, iOpen)


def DN_C2GSRefreshItemChecked(who):
    iDrop = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSRefreshItemChecked(who, iDrop)


def DN_C2GSCGState(who):
    iBehavior = cl_duonet.netfunc.UnpackInt(4)
    iState = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSCGState(who, iBehavior, iState)


def DN_C2GSUpdateSealedInscription(who):
    iType = cl_duonet.netfunc.UnpackInt(2)
    iOpen = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSUpdateSealedInscription(who, iType, iOpen)


def DN_C2GSChooseReward(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    iAnswer = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSChooseReward(who, iMenuIdx, iAnswer)


def DN_C2GSPreviewUpgradeWeapon(who):
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSPreviewUpgradeWeapon(who, iWeapon)


def DN_C2GSUpdateChooseRewardStatus(who):
    iFrame = cl_duonet.netfunc.UnpackInt(4)
    iStatus = cl_duonet.netfunc.UnpackInt(1)
    iType = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSUpdateChooseRewardStatus(who, iFrame, iStatus, iType)


def DN_C2GSUpdateVoteStatus(who):
    iStatus = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSUpdateVoteStatus(who, iStatus)


def DN_C2GSChangeHeroName(who):
    iTargetHero = cl_duonet.netfunc.UnpackInt(4)
    sName = cl_duonet.netfunc.UnpackSL(2)
    cl_cnetwar.C2GSChangeHeroName(who, iTargetHero, sName)


def DN_C2GSSetPrioritySuit(who):
    iSuit = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSSetPrioritySuit(who, iSuit)


def DN_C2GSRollRelic(who):
    iID = cl_duonet.netfunc.UnpackInt(4)
    iPerformSID = cl_duonet.netfunc.UnpackInt(2)
    iRollType = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSRollRelic(who, iID, iPerformSID, iRollType)


def DN_C2GSSetRelicUpgradeType(who):
    iUpgradeType = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSSetRelicUpgradeType(who, iUpgradeType)


def DN_C2GSViewSeasonTask(who):
    cl_cnetwar.C2GSViewSeasonTask(who)


def DN_C2GSRecycleGoldenCup(who):
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSRecycleGoldenCup(who, iNpc)


def DN_C2GSRecycleUnDrop(who):
    iType = cl_duonet.netfunc.UnpackInt(1)
    iID = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSRecycleUnDrop(who, iType, iID)


def DN_C2GSTalentLevelUp(who):
    iTalentSID = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSTalentLevelUp(who, iTalentSID)


def DN_C2GSStartConquer(who):
    iTarget = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSStartConquer(who, iTarget)


def DN_C2GSHaltConquer(who):
    iTarget = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSHaltConquer(who, iTarget)


def DN_C2GSModeAnswer(who):
    iMode = cl_duonet.netfunc.UnpackInt(1)
    iSID = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSModeAnswer(who, iMode, iSID)


def DN_C2GSHaltRepeatShoot(who):
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSHaltRepeatShoot(who, iWeapon)


def DN_C2GSUpdateDeviceCompLevel(who):
    iSID = cl_duonet.netfunc.UnpackInt(2)
    iLevel = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSUpdateDeviceCompLevel(who, iSID, iLevel)


def DN_C2GSUpdateDeviceCompPos(who):
    iSID = cl_duonet.netfunc.UnpackInt(2)
    iPos = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSUpdateDeviceCompPos(who, iSID, iPos)


def DN_C2GSIceMoveDistance(who):
    iDis = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSIceMoveDistance(who, iDis)


def DN_C2GSSeasonSuitOption(who):
    iOption = cl_duonet.netfunc.UnpackInt(1)
    lstResult = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iResult = cl_duonet.netfunc.UnpackInt(4)
        lstResult.append(iResult)
    
    cl_cnetwar.C2GSSeasonSuitOption(who, iOption, lstResult)


def DN_C2GSSignRelic(who):
    iRelicSID = cl_duonet.netfunc.UnpackInt(2)
    iSign = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSSignRelic(who, iRelicSID, iSign)


def DN_C2GSMarkSeasonSuit(who):
    dMarkSuit = { }
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iSID = cl_duonet.netfunc.UnpackInt(2)
        iVal = cl_duonet.netfunc.UnpackInt(1)
        dMarkSuit[iSID] = iVal
    
    cl_cnetwar.C2GSMarkSeasonSuit(who, dMarkSuit)


def DN_C2GSSetSuitTemp(who):
    iSuitTempID = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSSetSuitTemp(who, iSuitTempID)


def DN_C2GSSwitchWeaponCliMode(who):
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    iCliMode = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSSwitchWeaponCliMode(who, iWeapon, iCliMode)


def DN_C2GSRealDiedRelife(who):
    cl_cnetwar.C2GSRealDiedRelife(who)


def DN_C2GSUpdateSkillCounter(who):
    iPerformSID = cl_duonet.netfunc.UnpackInt(2)
    iCount = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSUpdateSkillCounter(who, iPerformSID, iCount)


def DN_C2GSPickSeed(who):
    iSeedID = cl_duonet.netfunc.UnpackInt(4)
    cl_cnetwar.C2GSPickSeed(who, iSeedID)


def DN_C2GSFace(who):
    dx = cl_duonet.netfunc.UnpackInt(1)
    dy = cl_duonet.netfunc.UnpackInt(1)
    dz = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSFace(who, dx, dy, dz)


def DN_C2GSWarPing(who):
    iPing = cl_duonet.netfunc.UnpackInt(2)
    cl_cnetwar.C2GSWarPing(who, iPing)


def DN_C2GSEarphone(who):
    sName = cl_duonet.netfunc.UnpackSL(1)
    cl_cnetwar.C2GSEarphone(who, sName)


def DN_C2GSWarNewPing(who):
    iPingIdx = cl_duonet.netfunc.UnpackInt(1)
    cl_cnetwar.C2GSWarNewPing(who, iPingIdx)

