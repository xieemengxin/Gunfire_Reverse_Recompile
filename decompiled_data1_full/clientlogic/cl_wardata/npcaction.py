# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/npcaction.pyc
# RelativePath: clientlogic/cl_wardata/npcaction.pyc
# Source Generated with Decompyle++
# File: npcaction.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_NPC_SMITH, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, NWARRIOR_NPC_REFRESH, NPC_CON_CYCLEWAR, NPC_CON_UNLOCK4LAYER, NWARRIOR_NPC_CAR, VIRTUAL_ITEM_RELIC, MG_RELIC, NWARRIOR_NPC_EVENT, NWARRIOR_DROP_KEYITEM, PF_TYPE_PASSIVE, VIRTUAL_ITEM_RELIFETEAM, VIRTUAL_ITEM_EQUIP, MG_EQUIP, OBTAIN_WARCASH, INTERACT_TYPE_FORBID, LEVEL_TYPE_HIDE, STATE_TIME_FOREVER, STATE_TIME_LIMIT, MG_SOURCE_NPCREWARD, DROP_REASON_NPCREWARD, INTERACT_STATUS_PEND, NWARRIOR_NPC_TRANSFERPOS, NWARRIOR_NPC_BENEDICTION, VOTE_CONTINUE, VOTE_QUIT, NWARRIOR_NPC_TRANSFER, PLAYMODE_ROGUELIKE, LEVEL_TYPE_BOSS, NPC_CON_ALWAYSFALSE, NPC_CON_CHECKHERO, TYPE_RELIFE_GSCASH, UPDATE_RECORD_HERO, RELIC_SUBMSG_GENERATE_GOOD, VOTE_TYPE_NORMAL, ATT_SHAPE_SPHERE, DAM_TYPE_SCENE, DAM_USE_HP, MG_RAREITEM, VIRTUAL_ITEM_RAREITEM, NPC_CON_CHECKMODE, NPC_CON_CHECKENDLESS, NPC_CON_CHECKLAYERBOSS, NPC_CON_CHECKENDLESSELEMENT, NWARRIOR_NPC_RELICLOTTERY, NPC_CON_CHECKREGROUPRELICELEMENT, NWARRIOR_NPC_DICESHOP, NWARRIOR_NPC_WANDSHOP, NWARRIOR_NPC_S7SHOP, NWARRIOR_NPC_S8SHOP
from cl_cscommondef import QUALITY_FACTOR, ITEM_SOURCE_GOOD, QUALITY_TYPE_HIGH, QUALITY_TYPE_NORMAL, QUALITY_TYPE_LOW
from cl_only import Time2Frame, Functor, ChooseKey, PY_FLAG_DEAD, Frame2Time
from cl_npc import GetNpcEventData
from cl_object.logging import WarnpcLog, WarobjLog
from cl_pxlayer import PXMASK_MONSTER, PXMASK_STATIC, PXMASK_IMPENETRABLE, PXMASK_PETROCHEMICAL_OUTER, PXMASK_DOOR
from cl_platformdata import GetRareItmeLimitPlayType
import cl_formula
import cl_state
import cl_object.reason
import cl_minigame
import cl_math
import cl_shop
import cl_item
import cl_perform
import cl_notify
import cl_reward
import cl_npc.net as npcnet
import cl_snetwar
import cl_msgcenter
import cllib.lib_server
import cli_player
import cllib.lib_flag as lib_flag
import cl_action
import cl_gamedebug as debug

def NpcSetArgValue(oNpc, sKey, value):
    oNpc.SetArgValue(sKey, value)


def NpcGetArgValue(oNpc, sKey):
    return oNpc.GetArgValue(sKey)


def NpcWeightRewardGroup(oNpc, who, dRoundWeightGroup, iDelay, dExtInfo):
    if not dRoundWeightGroup:
        return None
    iRound = who.m_Game.m_WarMgr.m_Round
    if iRound not in dRoundWeightGroup:
        WarnpcLog.Alert('未配置战场%dNPC%s周目%d权重奖励组' % (oNpc.m_Game.m_WarMgr.m_SID, oNpc.m_SID, iRound))
        iRound = sorted(dRoundWeightGroup)[0]
    iGroup = dRoundWeightGroup[iRound]
    dChoose = { }
    dGroup = oNpc.m_Game.m_WarData.GetWeightRewardGroup(iGroup)
    dNewExtInfo = {
        'DropReason': DROP_REASON_NPCREWARD }
    dNewExtInfo.update(dExtInfo)
    for iMiniGame, (iWeight, _) in dGroup.items():
        clsData = oNpc.m_Game.m_WarData.GetMiniGameData(iMiniGame)
        if not clsData:
            continue
        if not cl_reward.NeedCheckGoldenCup(clsData, dNewExtInfo) and cl_reward.ValidExtraGoldenCup(oNpc.m_Game):
            continue
        dChoose[iMiniGame] = iWeight
    
    iChoose = ChooseKey(oNpc.m_Game, dChoose)
    if iChoose is None:
        return None
    clsData = oNpc.m_Game.m_WarData.GetMiniGameData(iChoose)
    if cl_reward.NeedCheckGoldenCup(clsData, dNewExtInfo):
        cl_reward.AddExtraGoldenCup(oNpc.m_Game)
    dReward = {
        iChoose: (10000, dGroup[iChoose][1]) }
    sKey = 'NpcWeightRewardGroup'
    if not iDelay:
        cl_reward.RewardItemByMiniGame(oNpc, who.m_ID, dReward, sKey, MG_SOURCE_NPCREWARD, dExtInfo = dNewExtInfo)
    else:
        oNpc.Call_Out(Functor(cl_reward.RewardItemByMiniGame, oNpc, who.m_ID, dReward, sKey, MG_SOURCE_NPCREWARD, dNewExtInfo), Time2Frame(iDelay), sKey)


def NpcRewardGroup(oNpc, who, dRoundGroup, iDelay, dExtInfo):
    if not dRoundGroup:
        return None
    iRound = who.m_Game.m_WarMgr.m_Round
    if iRound not in dRoundGroup:
        WarnpcLog.Alert('未配置战场%dNPC%s周目%d奖励组' % (oNpc.m_Game.m_WarMgr.m_SID, oNpc.m_SID, iRound))
        iRound = sorted(dRoundGroup)[0]
    iGroup = dRoundGroup[iRound]
    dGroup = oNpc.m_Game.m_WarData.GetRewardGroup(iGroup)
    sKey = 'NpcRewardGroup'
    dNewExtInfo = {
        'DropReason': DROP_REASON_NPCREWARD }
    dNewExtInfo.update(dExtInfo)
    if not iDelay:
        cl_reward.RewardItemByMiniGame(oNpc, who.m_ID, dGroup, sKey, MG_SOURCE_NPCREWARD, dExtInfo = dNewExtInfo)
    else:
        oNpc.Call_Out(Functor(cl_reward.RewardItemByMiniGame, oNpc, who.m_ID, dGroup, sKey, MG_SOURCE_NPCREWARD, dNewExtInfo), Time2Frame(iDelay), sKey)


def NpcRewardItemListByPhase(oNpc, who, dPhaseMiniGame, iDelay):
    if not dPhaseMiniGame:
        return None
    iDifficulty = oNpc.Query('Difficulty')
    if iDifficulty not in dPhaseMiniGame:
        WarnpcLog.Alert('未配置战场%dNPC%s难度%d掉落' % (oNpc.m_Game.m_WarMgr.m_SID, oNpc.m_SID, iDifficulty))
        iDifficulty = sorted(dPhaseMiniGame)[0]
    dMiniGame = dPhaseMiniGame[iDifficulty]
    if not dMiniGame:
        return None
    dReward = { }
    for iMiniGame, dInfo in dMiniGame.items():
        dReward[iMiniGame] = (dInfo['Prop'], dInfo['Times'])
    
    iHero = who.m_ID
    sKey = 'NpcRewardItemList'
    dExtInfo = {
        'CalOffset': 1,
        'CheckGoldenCup': 1,
        'DropReason': DROP_REASON_NPCREWARD }
    if not iDelay:
        cl_reward.RewardItemByMiniGame(oNpc, iHero, dReward, sKey, MG_SOURCE_NPCREWARD, dExtInfo)
    else:
        oNpc.Call_Out(Functor(cl_reward.RewardItemByMiniGame, oNpc, iHero, dReward, sKey, MG_SOURCE_NPCREWARD, dExtInfo), Time2Frame(iDelay), sKey)


def NpcRewardItemList(oNpc, who, dRoundMiniGame, iDelay):
    if not dRoundMiniGame:
        return None
    iRound = who.m_Game.m_WarMgr.m_Round
    if iRound not in dRoundMiniGame:
        WarnpcLog.Alert('未配置战场%dNPC%s周目%d掉落' % (oNpc.m_Game.m_WarMgr.m_SID, oNpc.m_SID, iRound))
        iRound = sorted(dRoundMiniGame)[0]
    dMiniGame = dRoundMiniGame[iRound]
    if not dMiniGame:
        return None
    dReward = { }
    for iMiniGame, dInfo in dMiniGame.items():
        dReward[iMiniGame] = (dInfo['Prop'], dInfo['Times'])
    
    iHero = who.m_ID
    sKey = 'NpcRewardItemList'
    dExtInfo = {
        'CalOffset': 1,
        'CheckGoldenCup': 1,
        'DropReason': DROP_REASON_NPCREWARD }
    if not iDelay:
        cl_reward.RewardItemByMiniGame(oNpc, iHero, dReward, sKey, MG_SOURCE_NPCREWARD, dExtInfo)
    else:
        oNpc.Call_Out(Functor(cl_reward.RewardItemByMiniGame, oNpc, iHero, dReward, sKey, MG_SOURCE_NPCREWARD, dExtInfo), Time2Frame(iDelay), sKey)


def NpcDelayRemove(oNpc, who, iDelay):
    oNpc.Remove_Call_Out('NpcDelayRemove')
    oNpc.Call_Out(oNpc.Remove, Time2Frame(iDelay), 'NpcDelayRemove')


def NpcAddSelfState(oNpc, who, iState, iTime):
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetFormulaResult(oNpc, iTime)
    else:
        iTimeType = STATE_TIME_FOREVER
    dData = {
        'AID': oNpc.m_ID,
        'RS': cl_object.reason.CStrReason('NpcAdd') }
    oState = cl_state.AddState(oNpc, iState, iTimeType, Time2Frame(iTime), dData)
    if not oState:
        return None
    oState.Enable(oNpc)


def NpcAddTargetState(oNpc, who, iState, iTime):
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = cl_formula.GetFormulaResult(who, iTime)
    else:
        iTimeType = STATE_TIME_FOREVER
    dData = {
        'AID': who.m_ID,
        'RS': cl_object.reason.CStrReason('NpcAdd') }
    oState = cl_state.AddState(who, iState, iTimeType, Time2Frame(iTime), dData)
    if not oState:
        return None
    oState.Enable(who)


def NpcCommonNotify(oNpc, who, iChat):
    cl_notify.SendCommonNotify(who.m_Game, [
        who.m_PlayerID], iChat, { })


def NpcSaveWarRecord(oNpc, who):
    oSave = who.m_Game.m_WarMgr.GetComponent('SaveElement')
    if oSave:
        oSave.ManualSave()


def NpcRewardByPhase(oNpc, who, dMiniGame, iDelay, dExtInfo):
    if not dMiniGame:
        return None
    iDifficulty = oNpc.Query('Difficulty')
    if iDifficulty not in dMiniGame:
        WarnpcLog.Alert('未配置战场%dNPC%s难度%d掉落' % (oNpc.m_Game.m_WarMgr.m_SID, oNpc.m_SID, iDifficulty))
        iDifficulty = sorted(dMiniGame)[0]
    iMiniGame = dMiniGame[iDifficulty]
    clsMiniGame = oNpc.m_Game.m_WarData.GetMiniGameData(iMiniGame)
    if not clsMiniGame:
        return None
    dNewExtInfo = {
        'DropReason': DROP_REASON_NPCREWARD }
    dNewExtInfo.update(dExtInfo)
    if cl_reward.NeedCheckGoldenCup(clsMiniGame, dNewExtInfo):
        if cl_reward.ValidExtraGoldenCup(oNpc.m_Game):
            cl_reward.AddExtraGoldenCup(oNpc.m_Game)
        else:
            return None
    lstHero = oNpc.m_Game.m_WarMgr.GetLiveHero() if clsMiniGame.m_Type not in cl_reward.ONCE_MG_TYPE else [
        who.m_ID]
    if iDelay and not oNpc.Query('DebugMulChoose'):
        oNpc.Call_Out(Functor(DelayNpcStartMiniGame, oNpc, lstHero, iMiniGame, dNewExtInfo), Time2Frame(iDelay), 'DelayNpcStartMiniGame')
    else:
        DelayNpcStartMiniGame(oNpc, lstHero, iMiniGame, dNewExtInfo)


def NpcStartMiniGame(oNpc, who, dRoundMiniGame, iDelay, dExtInfo):
    if not dRoundMiniGame:
        return None
    iRound = who.m_Game.m_WarMgr.m_Round
    if iRound not in dRoundMiniGame:
        WarnpcLog.Alert('未配置战场%dNPC%s周目%d掉落' % (oNpc.m_Game.m_WarMgr.m_SID, oNpc.m_SID, iRound))
        iRound = sorted(dRoundMiniGame)[0]
    iMiniGame = dRoundMiniGame[iRound]
    clsMiniGame = oNpc.m_Game.m_WarData.GetMiniGameData(iMiniGame)
    if not clsMiniGame:
        WarnpcLog.Alert('未配置战场%dNPC%d抽取%d' % (oNpc.m_Game.m_WarMgr.m_SID, oNpc.m_SID, iMiniGame))
        return None
    dNewExtInfo = {
        'DropReason': DROP_REASON_NPCREWARD,
        'Abandoner': oNpc.m_ID }
    dNewExtInfo.update(dExtInfo)
    if oNpc.GetArgValue('LimitTaskInfo'):
        dNewExtInfo['LimitTaskInfo'] = oNpc.GetArgValue('LimitTaskInfo')
    if cl_reward.NeedCheckGoldenCup(clsMiniGame, dNewExtInfo):
        if cl_reward.ValidExtraGoldenCup(oNpc.m_Game):
            cl_reward.AddExtraGoldenCup(oNpc.m_Game)
        else:
            return None
    lstHero = oNpc.m_Game.m_WarMgr.GetLiveHero() if clsMiniGame.m_Type not in cl_reward.ONCE_MG_TYPE else [
        who.m_ID]
    if iDelay and not oNpc.Query('DebugMulChoose'):
        oNpc.Call_Out(Functor(DelayNpcStartMiniGame, oNpc, lstHero, iMiniGame, dNewExtInfo), Time2Frame(iDelay), 'DelayNpcStartMiniGame')
    else:
        DelayNpcStartMiniGame(oNpc, lstHero, iMiniGame, dNewExtInfo)


def DelayNpcStartMiniGame(oNpc, lstHero, iMiniGame, dExtInfo):
    for iHero in lstHero:
        sKey = 'NpcReward%d_%d' % (iMiniGame, iHero)
        if oNpc.Query(sKey) and not oNpc.Query('DebugMulChoose'):
            oMiniGame = oNpc.m_Game.m_MiniGameMgr.GetPlayerMiniGameByOwner(oNpc.m_ID, iHero)
        else:
            oNpc.Set(sKey, 1)
            oNpc.Set('dExtInfo', dExtInfo)
            oNpc.Set('iMiniGame', iMiniGame)
            oMiniGame = cl_minigame.NewMiniGame(oNpc.m_Game, iMiniGame, oNpc.m_ID, iHero, dExtInfo)
        if oMiniGame:
            oMiniGame.Start()
    


def NpcTriggerChooseItem(oNpc, who, dRoundMiniGame, iAll, dChooseWeight, iDelayTime):
    oGame = oNpc.m_Game
    iRound = oGame.m_WarMgr.m_Round
    if not dRoundMiniGame:
        return None
    if iRound not in dRoundMiniGame:
        if not oNpc.Query('GmClone', 0):
            WarnpcLog.Alert('npc-%s多选一没有周目%s配置' % (oNpc.m_SID, iRound))
        iRound = sorted(dRoundMiniGame)[0]
    iMiniGame = dRoundMiniGame[iRound]
    lstHero = oGame.m_WarMgr.GetLiveHero() if iAll else [
        who.m_ID]
    if iDelayTime and not oNpc.Query('DebugMulChoose'):
        func = Functor(DelayNpcTriggerChooseItem, oNpc, lstHero, iMiniGame, dChooseWeight)
        oNpc.Call_Out(func, Time2Frame(iDelayTime), 'DelayTriggerChooseItem')
    else:
        DelayNpcTriggerChooseItem(oNpc, lstHero, iMiniGame, dChooseWeight)


def DelayNpcTriggerChooseItem(oNpc, lstHero, iMiniGame, dChooseWeight):
    for iHero in lstHero:
        sKey = 'NpcReward%d_%d' % (iMiniGame, iHero)
        if not not oNpc.Query(sKey):
            if oNpc.Query('DebugMulChoose'):
                oNpc.Set(sKey, 1)
                oMiniGame = cl_minigame.NewMiniGame(oNpc.m_Game, iMiniGame, oNpc.m_ID, iHero, {
                    'ChooseCnt': dChooseWeight })
                if oMiniGame:
                    oMiniGame.Start()
                    oMiniGame.AddEndCallBack(Functor(NpcNoteMiniGameEnd, oNpc.m_ID, iHero))
                    continue
                continue
    


def NpcNoteMiniGameEnd(iNpc, iHero, oMiniGame):
    oNpc = oMiniGame.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.MiniGameEnd(oMiniGame, iHero)


def NpcTransferLevel(oNpc, who):
    if not who:
        return None
    oGame = oNpc.m_Game
    if oNpc.m_LineIdx:
        (iLevel, _, _) = oNpc.m_LineIdx
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode.m_LevelType == LEVEL_TYPE_HIDE:
            oLevelCtrl.m_CurNode.TryHeroEnterLevel([
                who.m_ID])
        else:
            dTransfer = oNpc.Query('Transfer')
            oLevelNode.TryTriggerPassLevel([
                who.m_ID], dTransfer)


def NpcTransferHideLevel(oNpc, who):
    if not who:
        return None
    oGame = oNpc.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    iBaseLevel = oNpc.Query('HideLevel')
    iLevel = oLevelCtrl.GetHeroHideLevel(iBaseLevel, who.m_ID)
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    if not oLevelNode:
        oLevelNode = oLevelCtrl.CreateHideLevel(iBaseLevel, iLevel)
    if oLevelNode:
        oLevelNode.TryHeroEnterLevel([
            who.m_ID])


def NpcVoteNextLayer(oNpc, oHero, iContinue, iCountTime, iChangeCountTime = 500):
    if not oHero:
        return None
    oGame = oNpc.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    iCurNpc = oLevelCtrl.GetCurTransferNpc()
    if not iCurNpc:
        oLevelCtrl.SetCurTransferNpc(oNpc.m_ID)
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    pid = oHero.m_PlayerID
    if pid in dReady and iContinue == dReady[pid]:
        PlayerCancelVote(oNpc, oHero)
    else:
        PlayerVote(oNpc, oHero, iContinue, iCountTime, iChangeCountTime)


def PlayerVote(oNpc, oHero, iContinue, iCountTime, iChangeCountTime):
    oGame = oHero.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    lstVotingPlayer = oGame.m_WarMgr.GetRoomPlayer(iCalAI = 0)
    if oLevelCtrl.CheckFinishWar():
        lstVotingPlayer = oGame.m_WarMgr.GetLivePlayer(iCalAI = 0)
    pid = oHero.m_PlayerID
    WarnpcLog.Info('%d %s %s vote %s ready:%s' % (oGame.m_ID, oNpc.m_SID, pid, iContinue, dReady))
    dReady[pid] = iContinue
    npcnet.GS2CVoteStat(oGame, dReady, VOTE_TYPE_NORMAL)
    if len(lstVotingPlayer) <= 1:
        VoteTimeout(oLevelCtrl)
        return None
    if len(dReady) == 1:
        iWaitFrame = Time2Frame(iCountTime)
        oLevelCtrl.SetTranserReadyFrame(iWaitFrame)
        oGame.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, Functor(OnVoteRemovePlayer, iChangeCountTime), 'VoteNextLayer')
        oLevelCtrl.Call_Out(Functor(AllPlayerVoted, oLevelCtrl, iChangeCountTime), iWaitFrame, 'VoteNextLayer')
    NotifyVoteCountdown(oLevelCtrl, dReady)
    for iPlayer in lstVotingPlayer:
        if iPlayer not in dReady:
            break
    


def OnVoteRemovePlayer(iChangeCountTime, oLevelCtrl, oWarMgr, dInfo):
    pid = dInfo['pid']
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    WarnpcLog.Info('%d %s voteremove ready:%s' % (oWarMgr.m_Game.m_ID, pid, dReady))
    if pid in dReady:
        dReady.pop(pid)
    if dReady:
        if lib_flag.g_IsStandaloneClient:
            who = cli_player.GetPlayer(pid)
            if not who or who.m_WarMaster:
                return None
        lstPlayer = oWarMgr.GetLivePlayer(iCalAI = 0)
        for iPlayer in lstPlayer:
            if iPlayer not in dReady:
                return None
        
        AllPlayerVoted(oLevelCtrl, iChangeCountTime)
    else:
        AllPlayerCancelVote(oLevelCtrl)


def PlayerCancelVote(oNpc, oHero):
    oGame = oHero.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    pid = oHero.m_PlayerID
    WarnpcLog.Info('%d %s %s cancelvote ready:%s' % (oGame.m_ID, oNpc.m_SID, pid, dReady))
    dReady.pop(pid)
    npcnet.GS2CVoteStat(oGame, dReady, VOTE_TYPE_NORMAL)
    if not dReady:
        AllPlayerCancelVote(oLevelCtrl)


def AllPlayerCancelVote(oLevelCtrl):
    oGame = oLevelCtrl.m_Game
    lstVotingPlayer = oGame.m_WarMgr.GetRoomPlayer(iCalAI = 0)
    WarnpcLog.Info('%d %s allcancelvote' % (oGame.m_ID, lstVotingPlayer))
    oLevelCtrl.Remove_Call_Out('VoteNextLayer')
    cl_notify.ClearCommonNotify(oGame, lstVotingPlayer, 2002)
    cl_notify.ClearCommonNotify(oGame, lstVotingPlayer, 2028)
    oGame.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, 'VoteNextLayer')
    oLevelCtrl.SetTranserReadyFrame(0)


def AllPlayerVoted(oLevelCtrl, iChangeCountTime):
    oGame = oLevelCtrl.m_Game
    lstVotingPlayer = oGame.m_WarMgr.GetRoomPlayer(iCalAI = 0)
    WarnpcLog.Info('%d %s allvoted' % (oGame.m_ID, lstVotingPlayer))
    oLevelCtrl.Remove_Call_Out('VoteNextLayer')
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    tVote = set(dReady.values())
    if VOTE_CONTINUE in tVote and VOTE_QUIT in tVote:
        iCountFrame = Time2Frame(iChangeCountTime)
        oLevelCtrl.SetTranserReadyFrame(iCountFrame)
        NotifyVoteCountdown(oLevelCtrl, dReady)
        oLevelCtrl.Call_Out(Functor(VoteTimeout, oLevelCtrl), iCountFrame, 'VoteNextLayer')
    else:
        VoteTimeout(oLevelCtrl)


def VoteTimeout(oLevelCtrl):
    oGame = oLevelCtrl.m_Game
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    lstVotingPlayer = oGame.m_WarMgr.GetRoomPlayer(iCalAI = 0)
    WarnpcLog.Info('%d votetimeout %s %s' % (oGame.m_ID, lstVotingPlayer, dReady))
    oGame.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERSETTLE, 'VoteNextLayer')
    iDefault = VOTE_QUIT if oLevelCtrl.CheckFinishWar() else VOTE_CONTINUE
    for iPlayer in lstVotingPlayer:
        if iPlayer not in dReady:
            dReady[iPlayer] = iDefault
    
    oGame.m_WarMgr.HandleVote(dReady)


def NotifyVoteCountdown(oLevelCtrl, dVote):
    oGame = oLevelCtrl.m_Game
    dContinue = { }
    dQuit = { }
    iDefaultQuit = 1 if oLevelCtrl.CheckFinishWar() else 0
    lstVotingPlayer = oGame.m_WarMgr.GetRoomPlayer(iCalAI = 0)
    for pid in lstVotingPlayer:
        if iDefaultQuit and pid not in dVote:
            dQuit[pid] = 1
            continue
        if pid in dVote and dVote[pid] == VOTE_QUIT:
            dQuit[pid] = 1
            continue
        dContinue[pid] = 1
    
    iEndFrame = oLevelCtrl.GetTransferReadyFrame()
    iCurFrame = oGame.GetFrameNum()
    iRemainFrame = iEndFrame - iCurFrame
    iRemainTime = Frame2Time(iRemainFrame)
    sTime = str(iRemainTime)
    cl_notify.ClearCommonNotify(oGame, lstVotingPlayer, 2002)
    cl_notify.ClearCommonNotify(oGame, lstVotingPlayer, 2028)
    cl_notify.SendCommonNotify(oGame, dQuit, 2028, {
        '$time': sTime })
    cl_notify.SendCommonNotify(oGame, dContinue, 2002, {
        '$time': sTime })


def NeedToVote(oNpc):
    iMaxLayer = 4
    dTransfer = oNpc.Query('Transfer')
    if dTransfer and dTransfer['LayerNum'] == iMaxLayer and dTransfer['LevelNum'] == 0:
        return 1
    return 0


def NpcDelayTransferLevel(oNpc, oHero, iTime):
    if NeedToVote(oNpc):
        NpcVoteNextLayer(oNpc, oHero, iContinue = 0, iCountTime = iTime)
        return None
    if not oHero:
        return None
    if not oNpc.CheckTransferLevel(oHero):
        return None
    oGame = oNpc.m_Game
    iNpc = oNpc.m_ID
    pid = oHero.m_PlayerID
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    if not oLevelCtrl.GetCurTransferNpc():
        oLevelCtrl.SetCurTransferNpc(iNpc)
    lstPlayer = oGame.m_WarMgr.GetLivePlayer(iCalAI = 0)
    dPlayer = oGame.GetRealPlayers()
    if pid not in dReady:
        if not dReady and len(lstPlayer) > 1:
            func = Functor(AllPlayerReadyToTransefer, oNpc)
            iWaitFrame = Time2Frame(iTime)
            oNpc.Call_Out(func, iWaitFrame, 'TranserReady')
            oLevelCtrl.SetTranserReadyFrame(iWaitFrame)
            cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2002, {
                '$time': str(iTime) })
            cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2208, { })
            oGame.AddGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_PLAYERSETTLE, Functor(UpdateReadyPlayer, False), 'RemoveLivePlayer')
            oGame.AddGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_TAKEOVERHERO, Functor(UpdateReadyPlayer, False), 'TakeOverHero')
            oGame.AddGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_HANDOVERHERO, Functor(UpdateReadyPlayer, True), 'HandOverHero')
            RefreshAIReadyStat(oGame, iNpc, dReady)
        WarnpcLog.Info('%d %s transefer %s ready:%s liveplayer:%s' % (oGame.m_ID, oNpc.m_SID, pid, dReady, lstPlayer))
        dReady[pid] = 1
        npcnet.GS2CTransferReadyStat(oHero, iNpc, 1, dPlayer)
        for iPlayer in lstPlayer:
            if iPlayer not in dReady:
                break
        
    else:
        WarnpcLog.Info('%d %s transefer %s unready:%s liveplayer:%s' % (oGame.m_ID, oNpc.m_SID, pid, dReady, lstPlayer))
        dReady.pop(pid)
        npcnet.GS2CTransferReadyStat(oHero, iNpc, 0, dPlayer)
        if not dReady:
            RefreshAIReadyStat(oGame, iNpc, dReady)
            AllPlayerCancelReady(oNpc)


def UpdateReadyPlayer(bCancelReady, oNpc, _oSender, dInfo):
    pid = dInfo['pid']
    oGame = oNpc.m_Game
    oWarMgr = oGame.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    dReady = oLevelCtrl.GetReadyTransferPlayer()
    if pid in dReady:
        dReady.pop(pid)
    if bCancelReady:
        oHero = oWarMgr.GetHeroByPlayer(pid)
        if oHero:
            npcnet.GS2CTransferReadyStat(oHero, oNpc.m_ID, 0, oGame.GetRealPlayers())
    RefreshAIReadyStat(oGame, oNpc.m_ID, dReady)
    if dReady:
        if lib_flag.g_IsStandaloneClient:
            who = cli_player.GetPlayer(pid)
            if not who:
                return None
            if who.m_WarMaster:
                return None
        lstPlayer = oWarMgr.GetLivePlayer(iCalAI = 0)
        for iPlayer in lstPlayer:
            if iPlayer not in dReady:
                return None
        
        AllPlayerReadyToTransefer(oNpc)
    else:
        AllPlayerCancelReady(oNpc)


def RefreshAIReadyStat(oGame, iNpc, dReady):
    lstAIHero = oGame.m_WarMgr.GetAllAIHero()
    if not lstAIHero:
        return None
    iReady = 1 if dReady else 0
    dPlayer = oGame.GetRealPlayers()
    for iHero in lstAIHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        npcnet.GS2CTransferReadyStat(oHero, iNpc, iReady, dPlayer)
    


def AllPlayerCancelReady(oNpc):
    oGame = oNpc.m_Game
    iNpc = oNpc.m_ID
    cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2290, { })
    cl_notify.ClearCommonNotify(oGame, oGame.GetRealPlayers(), 2002)
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_PLAYERSETTLE, 'RemoveLivePlayer')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_TAKEOVERHERO, 'TakeOverHero')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_HANDOVERHERO, 'HandOverHero')
    oNpc.Remove_Call_Out('TranserReady')
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelCtrl.SetTranserReadyFrame(0)


def AllPlayerReadyToTransefer(oNpc):
    oGame = oNpc.m_Game
    iNpc = oNpc.m_ID
    lstPlayer = oGame.m_WarMgr.GetLivePlayer(iCalAI = 0)
    WarnpcLog.Info('%d transefer all ready:%s liveplayer:%s' % (oGame.m_ID, oNpc.Query('TranserReady', { }), lstPlayer))
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_PLAYERSETTLE, 'RemoveLivePlayer')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_TAKEOVERHERO, 'TakeOverHero')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_HANDOVERHERO, 'HandOverHero')
    oNpc.Remove_Call_Out('TranserReady')
    oNpc.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)
    (iLevel, _, _) = oNpc.m_LineIdx
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    lstHero = oGame.m_WarMgr.GetLiveHero()
    if oLevelNode.m_LevelType == LEVEL_TYPE_HIDE:
        oLevelCtrl.m_CurNode.TryHeroEnterLevel(lstHero)
    else:
        dTransfer = oNpc.Query('Transfer')
        oLevelNode.TryTriggerPassLevel(lstHero, dTransfer)


def NpcDelayTransferPos(oNpc, who, iTime, iBehavior, iCG, iCanSkip):
    if oNpc.m_FightType != NWARRIOR_NPC_TRANSFERPOS:
        WarnpcLog.Alert('npc%s 不是传送位置npc' % oNpc.m_SID)
        return None
    oGame = oNpc.m_Game
    iNpc = oNpc.m_ID
    lstPlayer = oGame.m_WarMgr.GetLivePlayer(iCalAI = 0)
    dReady = oNpc.m_Ready
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl.GetCurTransferNpc():
        oLevelCtrl.SetCurTransferNpc(iNpc)
    dPlayer = oGame.GetRealPlayers()
    if who.m_PlayerID not in dReady:
        if not dReady and len(lstPlayer) > 1:
            func = Functor(TransferPos, oNpc, iBehavior, iCG, iCanSkip)
            oNpc.Call_Out(func, Time2Frame(iTime), 'TranserPos')
            cl_notify.SendCommonNotify(oGame, dPlayer, 2347, {
                '$time': str(iTime) })
            oGame.AddGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_PLAYERSETTLE, Functor(UpdateTransferPlayer, False, iBehavior, iCG, iCanSkip), 'RemoveTransferPlayer')
            oGame.AddGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_TAKEOVERHERO, Functor(UpdateTransferPlayer, False, iBehavior, iCG, iCanSkip), 'TakeOverHero')
            oGame.AddGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_HANDOVERHERO, Functor(UpdateTransferPlayer, True, iBehavior, iCG, iCanSkip), 'HandOverHero')
            RefreshAIReadyStat(oGame, iNpc, dReady)
        dReady[who.m_PlayerID] = 1
        npcnet.GS2CTransferReadyStat(who, iNpc, 1, dPlayer)
        for iPlayer in lstPlayer:
            if iPlayer not in dReady:
                break
        
    else:
        dReady.pop(who.m_PlayerID)
        npcnet.GS2CTransferReadyStat(who, iNpc, 0, dPlayer)
        if not dReady:
            RefreshAIReadyStat(oGame, iNpc, dReady)
            CancelTransferPos(oNpc)
            oLevelCtrl.SetCurTransferNpc(0)


def TransferPos(oNpc, iBehavior, iCG, iCanSkip):
    oGame = oNpc.m_Game
    iNpc = oNpc.m_ID
    dRealPlayer = oGame.GetRealPlayers()
    cl_notify.ClearCommonNotify(oGame, dRealPlayer, 2347)
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_PLAYERSETTLE, 'RemoveTransferPlayer')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_TAKEOVERHERO, 'TakeOverHero')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_HANDOVERHERO, 'HandOverHero')
    oNpc.Remove_Call_Out('TranserPos')
    oNpc.m_Ready = { }
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelCtrl.CleanTranserInfo()
    for pid in oGame.m_WarMgr.GetRoomPlayer():
        oNpc.m_PlayerInteractStatus[pid] = INTERACT_STATUS_PEND
        oNpc.NotifyInteractInfo(pid)
    
    (iLevel, _, _) = oNpc.m_LineIdx
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
    oLineNode = oLevelCtrl.GetLineNode(oNpc.m_LineIdx)
    lstPosInfo = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'transferpos')
    lstHero = oNpc.m_Game.m_WarMgr.GetLiveHero()
    if iBehavior:
        cl_snetwar.GS2CTriggerBehavior(oGame, iNpc, iBehavior, dRealPlayer)
    if iCG:
        cl_action.CommonTriggerCG(oGame, iCG, iCanSkip)
    for idx, iHero in enumerate(lstHero):
        dTransferInfo = lstPosInfo[idx]
        oHero = oGame.GetObject(iHero)
        tTransferPos = dTransferInfo['Pos']
        tFace = dTransferInfo['Facing']
        oHero.Stop()
        oHero.WalkTo(tTransferPos)
        npcnet.GS2CTransferFace(oNpc, (int(tFace[0] * 127) + 128, int(tFace[1] * 127) + 128, int(tFace[2] * 127) + 128), oHero.m_PlayerID)
    
    for iPlayer in dRealPlayer:
        oHero = oGame.m_WarMgr.GetHeroByPlayer(iPlayer)
        if oHero and oHero.IsRealDied():
            npcnet.GS2CTransferFace(oNpc, (0, 0, 0), iPlayer)
    


def UpdateTransferPlayer(bCancelReady, iBehavior, iCG, iCanSkip, oNpc, _oSender, dInfo):
    oGame = oNpc.m_Game
    pid = dInfo['pid']
    oWarMgr = oGame.m_WarMgr
    dReady = oNpc.m_Ready
    if pid in dReady:
        dReady.pop(pid)
    if bCancelReady:
        oHero = oWarMgr.GetHeroByPlayer(pid)
        if oHero:
            npcnet.GS2CTransferReadyStat(oHero, oNpc.m_ID, 0, oGame.GetRealPlayers())
    RefreshAIReadyStat(oGame, oNpc.m_ID, dReady)
    if dReady:
        lstPlayer = oWarMgr.GetLivePlayer(iCalAI = 0)
        for iPlayer in lstPlayer:
            if iPlayer not in dReady:
                return None
        
        TransferPos(oNpc, iBehavior, iCG, iCanSkip)
    else:
        CancelTransferPos(oNpc)


def CancelTransferPos(oNpc):
    oGame = oNpc.m_Game
    iNpc = oNpc.m_ID
    cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 2290, { })
    cl_notify.ClearCommonNotify(oGame, oGame.GetRealPlayers(), 2347)
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_PLAYERSETTLE, 'RemoveTransferPlayer')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_TAKEOVERHERO, 'TakeOverHero')
    oGame.DoneGlobalAttention(iNpc, cl_msgcenter.MSG_WAR_HANDOVERHERO, 'HandOverHero')
    oNpc.Remove_Call_Out('TranserPos')


def NpcCancelCheckDistance(oNpc, who, iOnlyTeam):
    oGame = who.m_Game
    lstPlayer = oGame.m_WarMgr.GetLivePlayer()
    if iOnlyTeam or len(lstPlayer) > 1:
        oNpc.m_CheckInteractDistance = False
        oNpc.m_CheckInteractScene = False
    else:
        oNpc.m_CheckInteractDistance = False
        oNpc.m_CheckInteractScene = False


def NpcGoodsConfig(oNpc, oHero, iPos, iWeight, iBuyNum, iCashType, iCash, iSID, iHide = 0, dInfo = None):
    if not oNpc.ValidAction(oHero, dInfo):
        return None
    iCash = cl_formula.GetFormulaResult(oHero, iCash, {
        'Npc': oNpc.m_ID })
    oGoods = cl_shop.CreateGoodsByConfig(iSID, iCash, iCashType, iBuyNum, iHide)
    oNpc.SetGoods(iPos, iWeight, oGoods)


def ChooseWeapon(oHero, iMiniGame, iEnhance, lstExclude):
    oGame = oHero.m_Game
    clsMiniGame = oHero.m_Game.m_WarData.GetMiniGameData(iMiniGame)
    if clsMiniGame.m_Type != MG_EQUIP:
        return None
    lstWeapon = list(clsMiniGame.GetChooseWeight(oHero))
    lstAllUnlockItem = oHero.Query('Illus')['Weapon']
    lstAllCanSellItem = cl_item.GetAllCanSellWeapon(oGame)
    lstAllItem = list(set(lstAllUnlockItem) & set(lstAllCanSellItem) & set(lstWeapon))
    for iItem in lstExclude:
        if iItem in lstAllItem:
            lstAllItem.remove(iItem)
    
    if not lstAllItem:
        return None
    iReward = oGame.m_RandomMgr.ChooseKey('weapon%d' % oHero.m_ID, {
        'Select': lstAllItem })
    iGrade = cl_reward.GetWeaponRewardGrade(oGame)
    oEquip = cl_item.CreateEquip(oGame, iReward, iGrade, oOwner = oHero, iSource = ITEM_SOURCE_GOOD)
    if not oEquip:
        return None
    if oEquip.Type() & cl_item.EQUIP_TYPE_MAINWEAPON:
        oBulletcom = oEquip.GetComponent('Bullet')
        if oBulletcom:
            oBulletcom.BulletModify(oBulletcom.MaxBullet())
    if iEnhance:
        oEquip.AddEnhance(iEnhance, 'shop')
    return oEquip


def NpcGoodsEquip(oNpc, oHero, iPos, iWeight, iBuyNum, iCash, dRoundMiniGame, iHide = 0, iCashType = OBTAIN_WARCASH, iEnhance = 0, dInfo = None):
    if not oNpc.ValidAction(oHero, dInfo):
        return None
    if not dRoundMiniGame:
        return None
    oGame = oHero.m_Game
    iRound = oGame.m_WarMgr.m_Round
    if iRound not in dRoundMiniGame:
        if not oNpc.Query('GmClone', 0):
            WarnpcLog.Alert('npc-%s武器商品没有周目%s配置' % (oNpc.m_SID, iRound))
        iRound = sorted(dRoundMiniGame)[0]
    iMiniGame = dRoundMiniGame[iRound]
    lstExclude = oNpc.GetGoodsCacheData(VIRTUAL_ITEM_EQUIP, oHero.m_ID)
    oEquip = ChooseWeapon(oHero, iMiniGame, iEnhance, lstExclude)
    if not oEquip:
        return None
    iCash = cl_formula.GetFormulaResult(oHero, iCash, {
        'Npc': oNpc.m_ID })
    dGoods = {
        'item': VIRTUAL_ITEM_EQUIP,
        'info': {
            'sid': oEquip.m_SID,
            'item': oEquip,
            'data': { } } }
    if not iCashType:
        iCashType = OBTAIN_WARCASH
    oGoods = cl_shop.CreateGoodsByData(oEquip.m_SID, VIRTUAL_ITEM_EQUIP, iCash, iCashType, iBuyNum, [
        dGoods], iHide)
    oNpc.SetGoods(iPos, iWeight, oGoods)


def ChooseRelic(oHero, iMiniGame, iLevel, iNoCheckSell, lstExclude = None):
    oGame = oHero.m_Game
    clsMiniGame = oGame.m_WarData.GetMiniGameData(iMiniGame)
    if clsMiniGame.m_Type != MG_RELIC:
        return 0
    setRelic = set(clsMiniGame.m_ChooseWeight)
    if not iNoCheckSell:
        lstAllCanSellRelic = cl_perform.GetAllCanSellRelic(oGame)
        setRelic = setRelic & set(lstAllCanSellRelic)
    if lstExclude:
        setRelic = setRelic - set(lstExclude)
    oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
    oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(oHero.m_ID)
    if oChoosePool:
        setRelic = setRelic - set(oChoosePool.m_PreLoadData['Relic'])
    lstAllRelic = oHero.m_RelicCon.GetChooseRelicSet(setRelic, iLevel)
    if not lstAllRelic:
        return 0
    iReward = oGame.m_RandomMgr.ChooseKey('relic%d' % oHero.m_ID, {
        'Select': lstAllRelic })
    return iReward


def NpcGoodsRelic(oNpc, oHero, iPos, iWeight, iBuyNum, iCashType, iCash, dRoundMiniGame, iHide = 0, iLevel = 1, dInfo = None, iNoCheckSell = 0):
    if not oNpc.ValidAction(oHero, dInfo):
        return None
    oGame = oNpc.m_Game
    iRound = oGame.m_WarMgr.m_Round
    if not dRoundMiniGame:
        return None
    if not iLevel:
        iLevel = 1
    if iRound not in dRoundMiniGame:
        if not oNpc.Query('GmClone', 0):
            WarnpcLog.Alert('npc-%s遗物商品没有周目%s配置' % (oNpc.m_SID, iRound))
        iRound = sorted(dRoundMiniGame)[0]
    iMiniGame = dRoundMiniGame[iRound]
    lstExclude = oNpc.GetGoodsCacheData(VIRTUAL_ITEM_RELIC, oHero.m_ID)
    iReward = ChooseRelic(oHero, iMiniGame, iLevel, iNoCheckSell, lstExclude)
    clsRelic = cl_perform.GetPerformModule(iReward)
    if not clsRelic:
        return None
    iQuality = clsRelic.m_Quality
    dArgs = {
        'RelicSID': iReward,
        'QualityCoff': QUALITY_FACTOR[iQuality],
        'Npc': oNpc.m_ID }
    iCash = cl_formula.GetFormulaResult(oHero, iCash, dArgs)
    dGoods = {
        'item': VIRTUAL_ITEM_RELIC,
        'info': {
            'sid': iReward,
            'data': { },
            'level': iLevel } }
    dMsgInfo = {
        'Relic': iReward,
        'Level': iLevel }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oHero, dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_GOOD)
    if 'RelicDropLevel' in dMsgInfo:
        dGoods['info']['level'] = dMsgInfo['RelicDropLevel']
        iLevel = dMsgInfo['RelicDropLevel']
    if 'ReplaceRelicInfo' in dMsgInfo:
        iCanRepeat = dMsgInfo['RelicCanRepeat']
        iUseOldLevel = dMsgInfo['RelicUseOldLevel']
        for iReplaceRelic, iReplaceLevel in dMsgInfo['ReplaceRelicInfo']:
            if not iCanRepeat and iReplaceRelic in oNpc.GetGoodsCacheData(VIRTUAL_ITEM_RELIC, oHero.m_ID):
                continue
            dGoods['info']['sid'] = iReplaceRelic
            dGoods['info']['level'] = iReplaceLevel
            if iUseOldLevel:
                clsPerform = cl_perform.GetPerformModule(iReplaceRelic)
                if clsPerform.m_MaxLevel >= iLevel:
                    dGoods['info']['level'] = iLevel
            iReward = iReplaceRelic
        
    oGoods = cl_shop.CreateGoodsByData(iReward, VIRTUAL_ITEM_RELIC, iCash, iCashType, iBuyNum, [
        dGoods], iHide)
    oNpc.SetGoods(iPos, iWeight, oGoods)


def NpcGoodsEquipOrRelic(oNpc, oHero, iPos, iWeight, iBuyNum, iEquipCash, dEquipRoundMiniGame, iRelicCash, dRelicRoundMiniGame, iCashType = OBTAIN_WARCASH, iHide = 0, iEnhance = 0, iLevel = 1):
    if oHero.Query('ChangeGSCashShopGoods', 0):
        NpcGoodsRelic(oNpc, oHero, iPos, iWeight, iBuyNum, iCashType, iRelicCash, dRelicRoundMiniGame, iHide, iLevel)
    else:
        NpcGoodsEquip(oNpc, oHero, iPos, iWeight, iBuyNum, iEquipCash, dEquipRoundMiniGame, iHide, iCashType, iEnhance)


def NpcRandomPlusGoodsEquipOrRelic(oNpc, oHero, iPos, iWeight, iBuyNum, iEquipCash, iPlusEquipCash, dEquipRoundMiniGame, iRelicCash, iPlusRelicCash, dRelicRoundMiniGame, iCashType, iPlusCashType, iHide, iEnhance, iLevel, iPlusRandom, dTypeWeight, dPlusTypeWeight):
    dMsgInfo = {
        'PlusRandom': iPlusRandom }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GOODSPOSINITBEFORE, oHero, dMsgInfo)
    oGame = oHero.m_Game
    iPlusRandom = dMsgInfo['PlusRandom']
    iRandom = oGame.Random(10000)
    if iRandom < iPlusRandom:
        iPlus = 1
        iGoodsType = ChooseKey(oGame, dPlusTypeWeight)
    else:
        iPlus = 0
        iEnhance = 0
        iLevel = 1
        iGoodsType = ChooseKey(oGame, dTypeWeight)
    if iGoodsType == MG_EQUIP:
        if iPlus:
            NpcGoodsEquip(oNpc, oHero, iPos, iWeight, iBuyNum, iPlusEquipCash, dEquipRoundMiniGame, iHide, iPlusCashType, iEnhance)
        else:
            NpcGoodsEquip(oNpc, oHero, iPos, iWeight, iBuyNum, iEquipCash, dEquipRoundMiniGame, iHide, iCashType, iEnhance)
    elif iPlus:
        NpcGoodsRelic(oNpc, oHero, iPos, iWeight, iBuyNum, iPlusCashType, iPlusRelicCash, dRelicRoundMiniGame, iHide, iLevel)
    else:
        NpcGoodsRelic(oNpc, oHero, iPos, iWeight, iBuyNum, iCashType, iRelicCash, dRelicRoundMiniGame, iHide, iLevel)


def NpcGoodsRelife(oNpc, oHero, iPos, iWeight, iBuyNum, iCashType, iCash):
    oGame = oHero.m_Game
    lstHero = oGame.m_WarMgr.GetAllHero()
    lstPosHero = []
    for iTarget in lstHero:
        if iTarget == oHero.m_ID:
            continue
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        iTeamPos = oTarget.Query('TeamPos')
        lstPosHero.append((iTeamPos, iTarget))
    
    lstPosHero.sort()
    iIdx = len(oNpc.GetGoodsCacheData(VIRTUAL_ITEM_RELIFETEAM))
    if iIdx >= len(lstPosHero):
        return None
    iTargetPlayer = lstPosHero[iIdx][1]
    oGoods = cl_shop.CreateRelifeGoods(oHero.m_Game, oNpc.m_ID, oHero.m_ID, iCash, iCashType, iBuyNum, iTargetPlayer)
    oNpc.SetGoods(iPos, iWeight, oGoods)


def NpcGoodsRareItem(oNpc, oHero, iPos, iWeight, iBuyNum, iCashType, iCash, iMiniGame, iHide = 0):
    oGame = oNpc.m_Game
    oWarMgr = oGame.m_WarMgr
    dChooseWeight = { }
    clsMiniGame = oGame.m_WarData.GetMiniGameData(iMiniGame)
    if clsMiniGame.m_Type != MG_RAREITEM:
        WarnpcLog.Alert('战场%dnpc-%s抽取%d不是稀有道具抽取类型' % (oWarMgr.m_SID, oNpc.m_SID, iMiniGame))
        return None
    oSurvivorElement = oWarMgr.GetSurvivorElement()
    if not oSurvivorElement:
        WarnpcLog.Alert('非幸存者模式战场%dnpc-%s配置了稀有道具商品' % (oWarMgr.m_SID, oNpc.m_SID))
        return None
    dExcludeRareItem = oSurvivorElement.m_RareItemMgr.m_ExcludeRareItem
    dRareItmeLimit = GetRareItmeLimitPlayType(oWarMgr.GetPlayType())
    for iRareItem, iWeight in clsMiniGame.m_ChooseWeight.items():
        if iRareItem not in dRareItmeLimit:
            continue
        dChooseWeight[iRareItem] = iWeight
    
    if not dChooseWeight:
        WarnpcLog.Alert('战场%dnpc-%s稀有道具商品抽取不足' % (oWarMgr.m_SID, oNpc.m_SID))
        return None
    for iRareItem in dExcludeRareItem:
        dChooseWeight.pop(iRareItem, 0)
    
    for iItem in oNpc.GetGoodsCacheData(VIRTUAL_ITEM_RAREITEM, oHero.m_ID):
        if iItem in dChooseWeight:
            dChooseWeight.pop(iItem, 0)
    
    if not dChooseWeight:
        WarnpcLog.Info('%d %d %s not enough rareitem %s' % (oGame.m_ID, oWarMgr.m_SID, oNpc.m_SID, oHero.m_PlayerID))
        return None
    iReward = ChooseKey(oGame, dChooseWeight)
    oItem = cl_item.CreateRareItem(oGame, iReward)
    if not oItem:
        WarnpcLog.Alert('战场%dnpc-%s稀有道具商品%d不存在' % (oWarMgr.m_SID, oNpc.m_SID, iReward))
        return None
    iCash = cl_formula.GetFormulaResult(oHero, iCash)
    dGoods = {
        'item': VIRTUAL_ITEM_RAREITEM,
        'info': {
            'sid': oItem.m_SID,
            'item': oItem,
            'data': { } } }
    oGoods = cl_shop.CreateGoodsByData(iReward, VIRTUAL_ITEM_RAREITEM, iCash, iCashType, iBuyNum, [
        dGoods], iHide)
    oNpc.SetGoods(iPos, iWeight, oGoods)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RAREITEMGOODS, oHero, {
        'Item': oItem })


def NpcGoodsPet(oNpc, oHero, iNum, iCashType, iCash, dQualityCoff):
    oNpc.InitGoodsInfo(oHero, iNum, iCashType, iCash, dQualityCoff)


def NpcGoodsWandShopCardPack(oNpc, oHero, dLevel, iWandCash, dWandQualityWeight, dCompQualityWeight, iExtraWandNum, iExtraWandCash, iExtraWandCompNum, iExtraCompCash, dQuality, iGuarantee):
    dInfo = oNpc.m_FormulaLimit
    iWandCash = cl_formula.GetFormulaResult(oHero, iWandCash, dInfo)
    iExtraWandCash = cl_formula.GetFormulaResult(oHero, iExtraWandCash, dInfo)
    iExtraCompCash = cl_formula.GetFormulaResult(oHero, iExtraCompCash, dInfo)
    iGuarantee = cl_formula.GetFormulaResult(oHero, iGuarantee, dInfo)
    oNpc.InitGoodsInfo(oHero, dLevel, iWandCash, dWandQualityWeight, dCompQualityWeight, iExtraWandNum, iExtraWandCash, iExtraWandCompNum, iExtraCompCash, dQuality, iGuarantee)


def NpcWandShopAbilityRollInfo(oNpc, oHero, dRollInfo):
    oNpc.InitAbilityRollInfo(dRollInfo)


def NpcSetBuyRelicRewardGoods(oNpc, oHero, iBuyType, iRewardCnt):
    lstGoods = oNpc.GetGoods(iBuyType)
    for oGoods in lstGoods:
        oGoods.SetRewardRelic(iRewardCnt)
    


def NpcChangeWeaponGrade(oNpc, oHero, iMul, iAdd):
    iMul = cl_formula.GetResultByData(oHero, iMul, { })
    iAdd = cl_formula.GetResultByData(oHero, iAdd, { })
    lstGoods = oNpc.GetGoods(VIRTUAL_ITEM_EQUIP)
    for oGoods in lstGoods:
        for dItem in oGoods.m_Items:
            oEquip = dItem['info'].get('item', None)
            if oEquip:
                oEquip.m_Grade += oEquip.m_Grade * iMul // 10000 + iAdd
                oInscriptionCom = oEquip.GetComponent('Inscription')
                oInscriptionCom.ResetInscription()
        
    


def NpcSetBuyGoodsGenCash(oNpc, oHero):
    lstGoods = oNpc.GetGoods()
    for oGoods in lstGoods:
        oGoods.m_Cash = -(oGoods.m_Cash)
    


def NpcGoodsSelloff(oNpc, oHero, iWeight, iPos, iSelloff):
    if iWeight < oHero.m_Game.Random(100):
        return None
    iPos = cl_formula.GetFormulaResult(oHero, iPos)
    iSelloff = cl_formula.GetFormulaResult(oHero, iSelloff)
    oNpc.SetSelloff(oHero, iPos, iSelloff)


def NpcForbidInteract(oNpc, oHero, iAll):
    oGame = oNpc.m_Game
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer() if iAll else [
        oHero.m_PlayerID]
    oNpc.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)


def NpcSetInteractDone(oNpc, oHero, iNotify, iForbid, iAll):
    oGame = oNpc.m_Game
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer() if iAll else [
        oHero.m_PlayerID]
    for pid in lstPlayer:
        oNpc.SetHeroInteractStatus(pid, iNotify)
    
    if iForbid:
        oNpc.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)


def NpcTriggerClientBehavior(oNpc, oHero, iBehavior, iTrigger = 0, iBroadcast = 1):
    oGame = oNpc.m_Game
    iOwner = oHero.m_ID if iTrigger else oNpc.m_ID
    if iBroadcast:
        oScene = oNpc.m_Game.m_SceneMgr.GetScene(oNpc.m_Scene)
        lstPlayer = list(oScene.GetPlayers())
    else:
        lstPlayer = [
            oHero.m_PlayerID]
    cl_snetwar.GS2CTriggerBehavior(oGame, iOwner, iBehavior, lstPlayer)


def NpcKillAroundMonster(oNpc, oHero, fRadius, iFightType):
    oGame = oNpc.m_Game
    lstArgs = [
        oNpc.GetPos(),
        fRadius]
    dMask = {
        'Mask': PXMASK_MONSTER,
        'BlockMask': PXMASK_STATIC | PXMASK_DOOR | PXMASK_PETROCHEMICAL_OUTER | PXMASK_IMPENETRABLE }
    if oGame.m_WarMgr.Query('DebugRay'):
        debug.DebugCircle(oGame, oNpc.GetPos(), fRadius, debug.LINE_TILE)
    lstMonster = cl_math.GetAttackTargetList(oGame, oNpc.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    oReason = cl_object.reason.CStrReason('NpcAction', None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if oMonster.m_FightType & iFightType == iFightType:
            oMonster.HPDirectModify('HP', oHero.m_ID, -oMonster.HP(), oReason)
            if oMonster.m_Part and not oMonster.IsDead():
                oMonster.HPDirectModify('HP', oHero.m_ID, -oMonster.HP(), oReason)
    


def NpcDisableSceneMonsterPassive(oNpc, oHero, iMonsterSID, iPassive, iDelayTime):
    if iDelayTime:
        oNpc.Call_Out(Functor(DelayDisableSceneMonsterPassive, oNpc, iMonsterSID, iPassive), Time2Frame(iDelayTime), 'DelayRemoveMonsterPassive')
    else:
        DelayDisableSceneMonsterPassive(oNpc, iMonsterSID, iPassive)


def DelayDisableSceneMonsterPassive(oNpc, iMonsterSID, iPassive):
    oGame = oNpc.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oNpc.m_Scene)
    for mid in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(mid, PY_FLAG_DEAD)
        if not oMonster or iMonsterSID != oMonster.m_SID:
            continue
        oPerform = oMonster.GetPerform(iPassive)
        if not oPerform or oPerform.m_PFType & PF_TYPE_PASSIVE != PF_TYPE_PASSIVE:
            continue
        oPerform.Disable(oMonster)
    


def NpcPartyReward(oNpc, oHero, iDelay = 130):
    pid = oHero.m_PlayerID
    iLGS = oNpc.m_Game.m_WarMgr.GetPlayerLGS(pid)
    iRewardFrame = oNpc.m_Game.GetFrameNum() + Time2Frame(iDelay)
    cllib.lib_server.L2SPartyReward(iLGS, oNpc.m_Game.m_ID, pid, Functor(CBPartyReward, oNpc.m_Game, oNpc.m_ID, oHero.m_ID, iRewardFrame))


def CBPartyReward(oGame, iNpc, iHero, iRewardFrame, iReward):
    iNow = oGame.GetFrameNum()
    if iRewardFrame <= iNow:
        DelayPartyReward(oGame, iNpc, iHero, iReward)
    else:
        oNpc = oGame.GetObject(iNpc)
        if not oNpc:
            return None
        oNpc.Call_Out(Functor(DelayPartyReward, oGame, iNpc, iHero, iReward), iRewardFrame - iNow, 'DelayPartyReward')


def DelayPartyReward(oGame, iNpc, iHero, iReward):
    oItem = cl_item.GetTemp(iReward)
    if not oItem:
        return None
    oHero = oGame.GetObject(iHero)
    if not oHero:
        return None
    oNpc = oGame.GetObject(iNpc)
    if not oNpc:
        return None
    oResMgr = oGame.GetResMgr()
    lstDropData = [
        oItem]
    oResMgr.CreateDrop(oHero.m_Scene, NWARRIOR_DROP_KEYITEM, oNpc.GetPos(), lstDropData, { }, dStaticInfo = {
        'DropSource': oHero.m_PlayerID }, iOwner = oHero.m_ID)
    dItem2Chat = {
        6002: 2013,
        6003: 2014,
        6004: 2015 }
    iChat = dItem2Chat[iReward] if iReward in dItem2Chat else 2015
    cl_notify.SendCommonNotify(oGame, [
        oHero.m_PlayerID], iChat, { })


def NpcModifySingleGSCostRelifeTimes(oNpc, oHero, iModify, iMaxModify, dLayer):
    oGame = oHero.m_Game
    oWarMgr = oGame.m_WarMgr
    if not oWarMgr.IsSingleGame():
        return None
    if oWarMgr.m_PlayMode not in (PLAYMODE_ROGUELIKE,):
        return None
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    iLayer = oLevelCtrl.m_LayerNum
    if iLayer not in dLayer:
        return None
    dRelifeTransferInfo = oHero.QuerySavedData('RelifeTransferInfo', { })
    if iLayer in dRelifeTransferInfo:
        return None
    iModify = cl_formula.GetFormulaResult(oHero, iModify)
    iMaxModify = cl_formula.GetFormulaResult(oHero, iMaxModify)
    dRelifeTransferInfo[iLayer] = 1
    oHero.SetSavedData('RelifeTransferInfo', dRelifeTransferInfo)
    WarobjLog.Info(f'''game:{oGame.m_ID} pid:{oHero.m_PlayerID} {iLayer} modifyrelifeinfo {iModify} {dRelifeTransferInfo}''')
    iChange = oHero.ModifyRelifeCnt(TYPE_RELIFE_GSCASH, 'WarInit', iModify, iMaxModify)
    oSave = oWarMgr.GetComponent('SaveElement')
    if oSave:
        dRelifeInfo = oHero.Query('RelifeInfo', { })
        oSave.HandleRecord({
            'Hero': {
                'RLF': dRelifeInfo,
                'SET': oHero.Save() } }, UPDATE_RECORD_HERO)
    iChat = 17126 if iChange else 17127
    cl_notify.SendCommonNotify(oGame, [
        oHero.m_PlayerID], iChat, { })


def NpcGoodsDice(oNpc, oHero):
    oNpc.InitGoodsInfo(oHero)


def NpcSetTransferDir(oNpc, iDir, dTargetLayer, iLimitLayer):
    if oNpc.m_FightType != NWARRIOR_NPC_TRANSFER:
        return None
    oWarMgr = oNpc.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    if oLevelCtrl.GetMaxLayer() < iLimitLayer:
        return None
    iLayer = oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
    if iLayer not in dTargetLayer:
        return None
    if oLevelCtrl.m_CurNode and oLevelCtrl.m_CurNode.m_LevelType != LEVEL_TYPE_BOSS:
        return None
    oNpc.SetTransferDir(iDir)


def NpcSetOpenBoxRule(oNpc, iRule, dParam):
    oNpc.SetTriggerRule(iRule, dParam)


def NpcSetOpenCost(oNpc, iType, dParam, iReset):
    dCost = {
        iType: dParam }
    oNpc.SetOpenCost(dCost, iReset)


def NpcSetVisibleCondition(oNpc, iCondition, dParam):
    if iCondition in NPC_CONDITION_FUNC:
        func = Functor(NPC_CONDITION_FUNC[iCondition], dParam)
        oNpc.AddVisibleCondition(func)


def NpcSetEventData(oNpc, iEventDataSID):
    if oNpc.m_FightType != NWARRIOR_NPC_EVENT:
        return None
    clsEventData = GetNpcEventData(iEventDataSID)
    if not clsEventData:
        return None
    oNpc.SetEvent(clsEventData)


def AddExtraInteractRule(oNpc, iRule, dParam):
    oNpc.AddExtraInteractRule(iRule, dParam)


def NpcSetSpeed(oNpc, fSpeed):
    oNpc.SetSpeed(fSpeed)


def NpcSetTriggerRadius(oNpc, fRadius):
    if oNpc.m_FightType != NWARRIOR_NPC_CAR:
        return None
    oNpc.SetTriggerRadius(fRadius)


def NpcSetInitRefreshFormula(oNpc, tCost, iType):
    if oNpc.m_FightType != NWARRIOR_NPC_REFRESH:
        return None
    oNpc.SetInitRefreshCost(tCost, iType)


def NpcSetRefreshFormula(oNpc, tCost):
    if oNpc.m_FightType != NWARRIOR_NPC_REFRESH:
        return None
    oNpc.SetRefreshCost(tCost)


def NpcSetRefreshMG(oNpc, dRoundMiniGame):
    if oNpc.m_FightType != NWARRIOR_NPC_REFRESH:
        return None
    if not dRoundMiniGame:
        return None
    oGame = oNpc.m_Game
    iRound = oGame.m_WarMgr.m_Round
    if iRound not in dRoundMiniGame:
        return None
    iWarMiniGame = dRoundMiniGame[iRound]
    iWarNo = iWarMiniGame // 10000
    if iWarNo != oNpc.m_Game.m_WarMgr.m_SID:
        return None
    iMiniGame = iWarMiniGame % 10000
    oNpc.SetChooseGame(iMiniGame)


def NpcSetRefreshWarMG(oNpc, dRoundMiniGame):
    if oNpc.m_FightType != NWARRIOR_NPC_REFRESH:
        return None
    if not dRoundMiniGame:
        return None
    oGame = oNpc.m_Game
    iRound = oGame.m_WarMgr.m_Round
    if iRound not in dRoundMiniGame:
        return None
    iWarNo = oGame.m_WarMgr.m_SID
    if iWarNo not in dRoundMiniGame[iRound]:
        return None
    iWarMiniGame = dRoundMiniGame[iRound][iWarNo]
    iMiniGame = iWarMiniGame % 10000
    oNpc.SetChooseGame(iMiniGame)


def NpcSetGoldenCupTimes(oNpc, iTimes):
    if oNpc.m_FightType not in [
        NWARRIOR_NPC_GOLDENCUP,
        NWARRIOR_NPC_LIMITGOLDENCUP,
        NWARRIOR_NPC_EXCHANGEGOLDENCUP]:
        return None
    oNpc.SetTimes(iTimes)


def NpcSetSmithAction(oNpc, who, iType, iCash):
    if oNpc.m_FightType != NWARRIOR_NPC_SMITH:
        return None
    oNpc.SetIntactAction(iType, iCash)


def NpcSetFormulaArgsLimit(oNpc, dArgs):
    if oNpc.m_FightType not in (NWARRIOR_NPC_EVENT, NWARRIOR_NPC_REFRESH, NWARRIOR_NPC_DICESHOP, NWARRIOR_NPC_WANDSHOP, NWARRIOR_NPC_S7SHOP, NWARRIOR_NPC_S8SHOP):
        WarnpcLog.Alert('%s 未支持类型SID为%sNPC设置公式参数' % (oNpc.m_Game.m_ID, oNpc.m_SID))
        return None
    oNpc.SetFormulaArgsLimit(dArgs)


def NpcSetRefreshLayer(oNpc, iLayer, iTimes, tCost):
    if oNpc.m_FightType != NWARRIOR_NPC_BENEDICTION:
        return None
    oLevelCtrl = oNpc.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    if oLevelCtrl.m_LayerNum != iLayer:
        oNpc.SetRefreshTimes(0)
    else:
        oNpc.SetRefreshTimes(iTimes)
    oNpc.SetRefreshCost(tCost)


def NpcSetSellPrice(oNpc, iCash, dQualityCoff):
    oNpc.SetSellPrice(iCash, dQualityCoff)


def NpcSetBuyCostFactor(oNpc, tCost):
    if oNpc.m_FightType != NWARRIOR_NPC_BENEDICTION:
        return None
    oNpc.SetBuyCostFactor(tCost)


def NpcSetRelicLotteryInitData(oNpc, dSuper, dHigh, dNormal, dLow, iCloseProb, iMiniGame):
    if oNpc.m_FightType != NWARRIOR_NPC_RELICLOTTERY:
        return None
    dWeight = {
        QUALITY_TYPE_LOW: dLow,
        QUALITY_TYPE_NORMAL: dNormal,
        QUALITY_TYPE_HIGH: dHigh,
        -1: dSuper }
    oNpc.SetInitData(dWeight, iCloseProb, iMiniGame)


def NpcSetDiceShopNpcInitData(oNpc, iBaseDiceGoodsNum, dDiceCashInfo, dDiceQualityProb, iBaseRefreshCount, dDicePacketInfo, dBossDicePacketInfo, dExcludePoints):
    if oNpc.m_FightType != NWARRIOR_NPC_DICESHOP:
        return None
    oNpc.SetInitData(iBaseDiceGoodsNum, dDiceCashInfo, dDiceQualityProb, iBaseRefreshCount, dDicePacketInfo, dBossDicePacketInfo, dExcludePoints)


def NpcSetS7ShopNpcInitData(oNpc, iCrystalGoodNum, iCrystalGoodCost, iCrystalPacketNum, iCrystalPacketCost, iCrystalPacketSize, iCrystalPacketDiff, iModulePacketNum, iModulePacketCost, dCrystalGoodInfo, dCrystalPacketInfo, dModulePacketChoose):
    if oNpc.m_FightType != NWARRIOR_NPC_S7SHOP:
        return None
    oNpc.SetInitData(iCrystalGoodNum, iCrystalGoodCost, iCrystalPacketNum, iCrystalPacketCost, iCrystalPacketSize, iCrystalPacketDiff, iModulePacketNum, iModulePacketCost, dCrystalGoodInfo, dCrystalPacketInfo, dModulePacketChoose)


def NpcSetS8ShopNpcInitData(oNpc, iPFPacketCost, iGemPacketCost, dPFPacketConfigInfo, dGemPacketConfigInfo):
    if oNpc.m_FightType != NWARRIOR_NPC_S8SHOP:
        return None
    oNpc.SetInitData(iPFPacketCost, iGemPacketCost, dPFPacketConfigInfo, dGemPacketConfigInfo)


def NpcCheckCycleWar(dParam, oNpc, oHero):
    return oNpc.m_Game.m_WarMgr.IsCycleWar()


def NpcCheckUnlock4Layer(dParam, oNpc, oHero):
    oGame = oNpc.m_Game
    if oGame.m_WarMgr.m_PlayMode not in (PLAYMODE_ROGUELIKE,):
        return 0
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    return oLevelCtrl.GetMaxLayer() >= 4


def NpcCheckAlwaysFalse(dParam, oNpc, oHero):
    return 0


def NpcCheckAssignHero(dParam, oNpc, oHero):
    if oHero.m_SID == dParam['AssignHero']:
        return 1
    return 0


def NpcCheckMode(dParam, oNpc, oHero):
    iMode = dParam['Mode']
    oGame = oNpc.m_Game
    if iMode in oGame.m_WarMgr.m_ModeType:
        return 1
    return 0


def NPCCheckEndless(dParam, oNpc, oHero):
    if oNpc.m_Game.m_WarMgr.IsEndless() == dParam['Check']:
        return 1
    return 0


def NPCCheckLayerBoss(dParam, oNpc, oHero):
    if not oNpc.m_LineIdx:
        return 0
    oLevelCtrl = oNpc.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    iLevel = oNpc.m_LineIdx[0]
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    if oLevelNode.m_LevelType != LEVEL_TYPE_BOSS:
        return 1
    dLayer = dParam['Layer']
    iCheck = dParam['Check']
    iInLayer = 1 if oLevelCtrl.m_LayerNum in dLayer else 0
    if iInLayer == iCheck:
        return 1
    return 0


def NPCCheckEndlessElement(dParam, oNpc, oHero):
    oEndlessElement = oNpc.m_Game.m_WarMgr.GetEndlessElement()
    iCheck = 1 if oEndlessElement else 0
    if iCheck == dParam['Check']:
        return 1
    return 0


def NPCCheckRegroupRelicElement(dParam, oNpc, oHero):
    oElement = oNpc.m_Game.m_WarMgr.GetComponent('RegroupRelicElement')
    if oElement and oElement.m_Enable:
        return 1
    return 0

NPC_CONDITION_FUNC = {
    NPC_CON_CHECKREGROUPRELICELEMENT: NPCCheckRegroupRelicElement,
    NPC_CON_CHECKENDLESSELEMENT: NPCCheckEndlessElement,
    NPC_CON_CHECKLAYERBOSS: NPCCheckLayerBoss,
    NPC_CON_CHECKENDLESS: NPCCheckEndless,
    NPC_CON_CHECKMODE: NpcCheckMode,
    NPC_CON_CHECKHERO: NpcCheckAssignHero,
    NPC_CON_ALWAYSFALSE: NpcCheckAlwaysFalse,
    NPC_CON_UNLOCK4LAYER: NpcCheckUnlock4Layer,
    NPC_CON_CYCLEWAR: NpcCheckCycleWar }
