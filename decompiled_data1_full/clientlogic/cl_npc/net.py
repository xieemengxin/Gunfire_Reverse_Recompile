# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/net.pyc
# RelativePath: clientlogic/cl_npc/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_NPC_TRANSFERPOS, NPC_CB_ITEMCONOP, NWARRIOR_NPC_WEAPONSTORE, NPC_CB_DICT, NPC_CB_ITEM, NPC_CB_VALUELIST, NPC_CB_REFRESH, NPC_CB_VALUE, NPC_CB_LIST, NWARRIOR_NPC, NWARRIOR_NPC_TRANSFER, TRANSFER_DIRTO_HIDE, NPC_CB_CHOOSEALL, NWARRIOR_NPC_SHOP, NWARRIOR_NPC_PHASESHOP, NPC_CB_INJECT
from cl_object.logging import WarnpcLog
import cl_duonet.dn_cl_npc_net as npcnet

def SetNpcUICallBackFunction(oHero, iCBType, cbfunc, npcobj = None):
    iTarget = 0
    if npcobj:
        iTarget = npcobj.m_ID
    iMenuIdx = oHero.m_NpcUIMenuIdx
    if oHero.m_NpcUICallBack:
        (iWaitMenuIdx, iWaitTarget, cbDict) = oHero.m_NpcUICallBack
        if iWaitMenuIdx == iMenuIdx:
            if iWaitTarget != iTarget:
                WarnpcLog.Alert('the same idx %s but different npc %s %s' % (iWaitMenuIdx, iTarget, iWaitTarget))
                return 0
            cbDict[iCBType] = cbfunc
            return iMenuIdx
    oHero.m_NpcUICallBack = (iMenuIdx, iTarget, {
        iCBType: cbfunc })
    return iMenuIdx


def DelNpcUICallBackFunction(oHero, iMenuIdx, iCBType, npcobj = None):
    if not oHero.m_NpcUICallBack:
        return None
    iTarget = 0
    if npcobj:
        iTarget = npcobj.m_ID
    (iWaitMenuIdx, iWaitTarget, cbDict) = oHero.m_NpcUICallBack
    if iWaitMenuIdx != iMenuIdx or iTarget != iWaitTarget:
        return None
    cbDict.pop(iCBType, None)


def ValidNpcUICallBack(oHero, iMenuIdx, iCBType):
    if not oHero.m_NpcUICallBack:
        WarnpcLog.Debug('%s %s no callback' % (oHero.m_PlayerID, iCBType))
        return False
    (iCallIdx, iNpc, _) = oHero.m_NpcUICallBack
    if iMenuIdx != iCallIdx:
        WarnpcLog.Debug('%s %s %s different idx %s %s' % (oHero.m_PlayerID, iCBType, iNpc, iCallIdx, iMenuIdx))
        return False
    if iNpc:
        oNpc = oHero.m_Game.GetObject(iNpc)
        if not oNpc or not oNpc.ValidInteract(oHero):
            WarnpcLog.Debug('%s %s invalid' % (oHero.m_PlayerID, iCBType))
            return False
    return True


def GS2CSystemAskList(oHero, sTitle, sText, sAnsList, iTimeOut = 0):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iTimeOut': iTimeOut,
        'Title': sTitle,
        'Text': sText,
        'lstAnswer': sAnsList,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CSystemAsk(netData)


def GS2CNpcShop(oHero, iShopNpc, lstMenu):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': iShopNpc,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstGoods': lstMenu,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcShop(netData)


def GS2CNpcShopSingleChange(oHero, iShopNpc, oGoods, iPos):
    oHero.IncMenuIdx()
    (pos, sid, goodstype, num, hasbuy, cashtype, cash, isLock, allattr) = oHero.m_BuyMgr.GetGoodsShow(iPos, oGoods, iShopNpc)
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'pos': pos,
        'sid': sid,
        'goodstype': goodstype,
        'canbuy': num,
        'hasbuy': hasbuy,
        'cashtype': cashtype,
        'cash': cash,
        'allattr': allattr,
        'pid': oHero.m_PlayerID,
        'isLock': isLock }
    npcnet.DN_GS2CNpcShopSingleChange(netData)


def GS2CNpcShopInteractResult(oHero, oGoods, iPos, bBuy):
    iBuy = 0
    if bBuy:
        iBuy = 1
    netData = {
        'pos': iPos,
        'sid': oGoods.m_SID,
        'buy': iBuy,
        'pid': oHero.m_PlayerID,
        'dExtraInfo': oGoods.GetExtraInfo() }
    npcnet.DN_GS2CNpcShopInteractResult(netData)


def GS2CNpcChooseTalent(oHero, lstTalent, iNpc, iTimeOutTime = 0):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': iNpc,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iTimeOutTime': iTimeOutTime,
        'lstTalent': lstTalent,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcChooseTalent(netData)


def GS2CNpcReplaceTalent(oHero, iSelectedTalent, iTalentLevel, lstTalent, iTimeOutTime):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iTimeOutTime': iTimeOutTime,
        'lstTalent': lstTalent,
        'iTalentLevel': iTalentLevel,
        'iSelectedTalent': iSelectedTalent,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcReplaceTalent(netData)


def GS2CNpcOpenCost(oHero, oNpc, dCost):
    lstCost = []
    for iType, dInfo in dCost.items():
        for iSID, iNum in dInfo.items():
            lstCost.append((iType, iSID, iNum))
        
    
    netData = {
        'lstCost': lstCost,
        'iNpc': oNpc.m_ID,
        'oGame': oNpc.m_Game,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcOpenCost(netData)


def GS2CNpcItemInteract(oHero, oNpc, dItem):
    oHero.IncMenuIdx()
    lstItem = []
    for iItem, dOption in dItem.items():
        lstOp = []
        for iOp, (iCashType, iCost, iOptionStatus) in dOption.items():
            lstOp.append((iOp, iCashType, iCost, iOptionStatus))
        
        lstItem.append((iItem, lstOp))
    
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstItem': lstItem,
        'iNpc': oNpc.m_ID,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcItemInteract(netData)


def GS2CNpcItemResult(oHero, oNpc, iItem, iResult):
    netData = {
        'iResult': iResult,
        'iItem': iItem,
        'iNpc': oNpc.m_ID,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcItemResult(netData)


def GS2CNpcInteractState(oNpc, pid):
    iStatus = oNpc.GetHeroInteractStatus(pid)
    iType = oNpc.GetPlayerInteractType(pid)
    iAssignInteractType = oNpc.GetPlayerAssignInteractType(pid)
    netData = {
        'iState': iStatus | iType,
        'iAssignInteractType': iAssignInteractType,
        'iNpc': oNpc.m_ID,
        'pid': pid }
    npcnet.DN_GS2CNpcInteractState(netData)


def GS2CTransferDir(oGame, dPlayer, iNpc, iDir, iHideType, iHideLevel):
    netData = {
        'oGame': oGame,
        'iDir': iDir,
        'iNpc': iNpc,
        'dPlayer': dPlayer,
        'iHideType': iHideType,
        'iHideLevel': iHideLevel }
    npcnet.DN_GS2CTransferDir(netData)


def GS2CNpcChooseReward(oHero, iNpc, lstReward, iMiniGame, iOp):
    lstItem = []
    for iReward, dOption in lstReward:
        tPos = dOption['Pos']
        lstAtt = dOption['Attr']
        iType = dOption['Type']
        lstItem.append((iReward, iType, tPos, {
            'Attr': lstAtt }))
    
    netData = {
        'iMiniGame': iMiniGame,
        'iSubOp': iOp,
        'lstItem': lstItem,
        'iNpc': iNpc,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcChooseReward(netData)


def GS2CNpcChooseMultiTalent(oHero, dTalent, iTimeOutTime = 0):
    oHero.IncMenuIdx()
    lstQue = []
    for idx, dQue in dTalent.items():
        lstTalent = []
        for iSID, iLevel in dQue.items():
            lstTalent.append((iSID, iLevel))
        
        lstQue.append((idx, lstTalent))
    
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iTimeOutTime': iTimeOutTime,
        'lstQue': lstQue,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcChooseMultiTalent(netData)


def GS2CNpcModifyItem(oHero, iNpc, iTotalNum, iUseNum):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iNpc': iNpc,
        'iTotalNum': iTotalNum,
        'iUseNum': iUseNum,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcModifyItem(netData)


def GS2CNpcEvent(oHero, iNpc, sTitle, lstAllOption):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'sTitle': sTitle,
        'iNpc': iNpc,
        'lstOption': lstAllOption,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CNpcEvent(netData)


def GS2CNpcChallengeStatus(iHero, iNpc, iStatus):
    netData = {
        'iStatus': iStatus,
        'iNpc': iNpc,
        'pid': iHero }
    npcnet.DN_GS2CNpcChallengeStatus(netData)


def GS2CTransferReadyStat(oHero, iNpc, iIsReady, dPlayer):
    netData = {
        'oGame': oHero.m_Game,
        'iHero': oHero.m_ID,
        'iIsReady': iIsReady,
        'dPlayer': dPlayer,
        'iNpc': iNpc }
    npcnet.DN_GS2CTransferReadyStat(netData)


def GS2CNPCEventChoose(oHero, iType, iCount, lstItem, iEventType):
    oHero.IncMenuIdx()
    netData = {
        'oGame': oHero.m_Game,
        'pid': oHero.m_PlayerID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iType': iType,
        'iCount': iCount,
        'lstItem': lstItem,
        'iEventType': iEventType }
    npcnet.DN_GS2CNPCEventChoose(netData)


def GS2CNPCEventWeaponAction(oHero, iActionType, iNpcType, lstInfo):
    oHero.IncMenuIdx()
    netData = {
        'oGame': oHero.m_Game,
        'pid': oHero.m_PlayerID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iActionType': iActionType,
        'iNpcType': iNpcType,
        'lstInfo': lstInfo }
    npcnet.DN_GS2CNPCEventWeaponAction(netData)


def GS2CNpcTask(oHero, iTaskNpc, lstTaskInfo, iCanRefreshTimes):
    oHero.IncMenuIdx()
    dNetData = {
        'pid': oHero.m_PlayerID,
        'iNpc': iTaskNpc,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstTask': lstTaskInfo,
        'iCanRefreshTimes': iCanRefreshTimes }
    npcnet.DN_GS2CNpcTask(dNetData)


def GS2CRefreshNPC(oHero, iRewardType, iRewardSID, iCost, iLevel, iCostType, iLimit, iCount):
    oHero.IncMenuIdx()
    netData = {
        'oGame': oHero.m_Game,
        'pid': oHero.m_PlayerID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iRewardType': iRewardType,
        'iRewardSID': iRewardSID,
        'iCost': iCost,
        'iLevel': iLevel,
        'iCostType': iCostType,
        'iLimit': iLimit,
        'iCount': iCount }
    npcnet.DN_GS2CRefreshNPC(netData)


def GS2CSmithInteractInfo(oHero, iUpTimes, iMaxUpTimes, lstWeaponInfo):
    netData = {
        'oGame': oHero.m_Game,
        'pid': oHero.m_PlayerID,
        'iInteractTimes': iUpTimes,
        'iMaxUpTimes': iMaxUpTimes,
        'lstItem': lstWeaponInfo }
    npcnet.DN_GS2CSmithInteractInfo(netData)


def GS2CNpcAnimator(oNpc, pid, iAnimator):
    netData = {
        'oGame': oNpc.m_Game,
        'iNpc': oNpc.m_ID,
        'Animator': iAnimator,
        'pid': pid }
    npcnet.DN_GS2CNpcAnimator(netData)


def GS2CRandomRewardpf(who, lstRewardpf):
    who.IncMenuIdx()
    netData = {
        'pid': who.m_PlayerID,
        'iMenuIdx': who.m_NpcUIMenuIdx,
        'lstRewardpf': lstRewardpf }
    npcnet.DN_GS2CRandomRewardpf(netData)


def GS2CRandomChoose(pid, iChoose, dOption):
    lstOption = []
    for iOption, iValue in dOption.items():
        lstOption.append((iOption, iValue))
    
    netData = {
        'pid': pid,
        'iChoose': iChoose,
        'lstOption': lstOption }
    npcnet.DN_GS2CRandomChoose(netData)


def GS2CChoosePerform(who, lstPerform, iType):
    who.IncMenuIdx()
    netData = {
        'pid': who.m_PlayerID,
        'iMenuIdx': who.m_NpcUIMenuIdx,
        'lstPerform': lstPerform,
        'iType': iType }
    npcnet.DN_GS2CChoosePerform(netData)


def GS2CChosenRelicList(oGame, lstRelic, dPlayer):
    netData = {
        'oGame': oGame,
        'dPlayer': dPlayer,
        'lstRelic': lstRelic }
    npcnet.DN_GS2CChosenRelicList(netData)


def GS2CTransferScale(oGame, dPlayer, oNpc, tSacle):
    (sx, sy, sz) = tSacle
    netData = {
        'oGame': oGame,
        'dPlayer': dPlayer,
        'iNpc': oNpc.m_ID,
        'sx': sx,
        'sy': sy,
        'sz': sz }
    npcnet.DN_GS2CTransferScale(netData)


def GS2CNpcRefreshInfo(oNpc, oHero):
    (iMaxRefreshTimes, iCanRefreshTimes) = oNpc.GetRefreshInfo(oHero)
    (iMaxChooseAllTimes, iCanChooseAllTimes) = oNpc.GetChooseAllInfo(oHero)
    iCost = oNpc.GetRefreshCost(oHero)
    netData = {
        'iNpc': oNpc.m_ID,
        'iMaxRefreshTimes': iMaxRefreshTimes,
        'iCanRefreshTimes': iCanRefreshTimes,
        'iMaxChooseAllTimes': iMaxChooseAllTimes,
        'iCanChooseAllTimes': iCanChooseAllTimes,
        'pid': oHero.m_PlayerID,
        'iCost': iCost }
    npcnet.DN_GS2CNpcRefreshInfo(netData)


def GS2CBeneNpcResult(oNpc, oHero, iChat, iBeneSID, iResult):
    netData = {
        'iNpc': oNpc.m_ID,
        'iChat': iChat,
        'iBeneSID': iBeneSID,
        'iResult': iResult,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CBeneNpcResult(netData)


def GS2CTransferFace(oNpc, tPos, pid):
    netData = {
        'dx': tPos[0],
        'dy': tPos[1],
        'dz': tPos[2],
        'pid': pid }
    npcnet.DN_GS2CTransferFace(netData)


def GS2CVoteStat(oGame, dStat, iVoteType):
    lstVote = []
    for pid, iStat in dStat.items():
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        if not oHero:
            continue
        lstVote.append((oHero.m_ID, iStat))
    
    netData = {
        'oGame': oGame,
        'lstVote': lstVote,
        'iVoteType': iVoteType }
    npcnet.DN_GS2CVoteStat(netData)


def GS2CNPCOpenWeaponStoreUI(oNpc, oHero, iAnimaCost, lstNotOperateWeapon):
    oHero.IncMenuIdx()
    netData = {
        'pid': oHero.m_PlayerID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iNpc': oNpc.m_ID,
        'iAnimaCost': iAnimaCost,
        'lstNotOperateWeapon': lstNotOperateWeapon }
    npcnet.DN_GS2CNPCOpenWeaponStoreUI(netData)


def GS2CCommonTalentChoose(oHero, lstTalent):
    oHero.IncMenuIdx()
    netData = {
        'pid': oHero.m_PlayerID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstTalent': lstTalent }
    npcnet.DN_GS2CCommonTalentChoose(netData)


def GS2CCommonTalentChosen(oHero, lstTalent):
    netData = {
        'pid': oHero.m_PlayerID,
        'lstTalent': lstTalent }
    npcnet.DN_GS2CCommonTalentChosen(netData)


def GS2CPhaseGoldenCount(pid, iCount):
    netData = {
        'pid': pid,
        'iCount': iCount }
    npcnet.DN_GS2CPhaseGoldenCount(netData)


def GS2CWeaponAnimaInfo(pid, lstWeaponInfo):
    netData = {
        'pid': pid,
        'lstWeaponInfo': lstWeaponInfo }
    npcnet.DN_GS2CWeaponAnimaInfo(netData)


def GS2CWeaponInjectAnimaInfo(pid, iNpc, iWeapon, iPos, iResult):
    netData = {
        'pid': pid,
        'iNpc': iNpc,
        'iWeapon': iWeapon,
        'iPos': iPos,
        'iResult': iResult }
    npcnet.DN_GS2CWeaponInjectAnimaInfo(netData)


def GS2CExchangeNpcChooseTalent(oHero, lstTalent, iNpc):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': iNpc,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstTalent': lstTalent,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CExchangeNpcChooseTalent(netData)


def GS2CNpcChooseEnable(pid, iNpc, iEnable):
    netData = {
        'iNpc': iNpc,
        'iEnable': iEnable,
        'pid': pid }
    npcnet.DN_GS2CNpcChooseEnable(netData)


def GS2CPetShop(oHero, iNPC, lstPetGoods, iMaxRefreshTimes, iCanRefreshTimes):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': iNPC,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstPetGoods': lstPetGoods,
        'pid': oHero.m_PlayerID,
        'iMaxRefreshTimes': iMaxRefreshTimes,
        'iCanRefreshTimes': iCanRefreshTimes }
    npcnet.DN_GS2CPetShop(netData)


def GS2CPetSellPrice(oHero, iNpc, dPetPrice):
    netData = {
        'iNpc': iNpc,
        'dPetPrice': dPetPrice,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CPetSellPrice(netData)


def GS2CCheckFusePoint(oHero, iNpc, iCheckFusePoint):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': iNpc,
        'iCheckFusePoint': iCheckFusePoint,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CCheckFusePoint(netData)


def GS2CRefreshRollNpcData(oHero, iNpc, iMode, dRelic):
    netData = {
        'iNpc': iNpc,
        'iMode': iMode,
        'dRelic': dRelic,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CRefreshRollNpcData(netData)


def GS2CSyncFuseCount(oHero, iNpc, iCount):
    netData = {
        'iNpc': iNpc,
        'iCount': iCount,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CSyncFuseCount(netData)


def GS2COpenReduceSuitTakeEffectAmountUI(oHero, lstSuit, iNum, iUI):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iNum': iNum,
        'lstSuit': lstSuit,
        'iUI': iUI,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2COpenReduceSuitTakeEffectAmountUI(netData)


def GS2CUpdateCheckReduceSuitResult(oHero, iSuit, iResult):
    netData = {
        'iSuit': iSuit,
        'iResult': iResult,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CUpdateCheckReduceSuitResult(netData)


def GS2CRelicLotteryNpcData(oHero, lstBefore, iReInteractProb):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstBefore': lstBefore,
        'iReInteractProb': iReInteractProb,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CRelicLotteryNpcData(netData)


def GS2CWandShop(oHero, iNPC, lstGoods, iCanRefreshTimes, iMaxRefreshTimes):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': iNPC,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstGoods': lstGoods,
        'pid': oHero.m_PlayerID,
        'iCanRefreshTimes': iCanRefreshTimes,
        'iMaxRefreshTimes': iMaxRefreshTimes }
    npcnet.DN_GS2CWandShop(netData)


def GS2CWandShopCardPackInfo(oHero, iType, lstCardPack):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iType': iType,
        'lstCardPack': lstCardPack,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CWandShopCardPackInfo(netData)


def GS2CWandShopRollInfo(oHero, iWand, dAbility):
    netData = {
        'iWandID': iWand,
        'dInfo': dAbility,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CWandShopRollInfo(netData)


def GS2CDiceShop(oHero, iNPC, lstGoods, iCanRefreshTimes, iMaxRefreshTimes, lstDicePacket):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': iNPC,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'lstGoods': lstGoods,
        'pid': oHero.m_PlayerID,
        'iCanRefreshTimes': iCanRefreshTimes,
        'iMaxRefreshTimes': iMaxRefreshTimes,
        'lstDicePacket': lstDicePacket }
    npcnet.DN_GS2CDiceShop(netData)


def GS2CDiceShopRecycleDiceCnt(oHero, iNPC, iRecycleDiceCnt):
    netData = {
        'iNpc': iNPC,
        'pid': oHero.m_PlayerID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iRecycleDiceCnt': iRecycleDiceCnt,
        'oGame': oHero.m_Game }
    npcnet.DN_GS2CDiceShopRecycleDiceCnt(netData)


def GS2CS7Shop(oHero, oNPC, lstModulePacket, lstCrystalGoods, lstCrystalPacket, iFullUpdate):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': oNPC.m_ID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iFullUpdate': iFullUpdate,
        'lstModulePacket': lstModulePacket,
        'lstCrystalGoods': lstCrystalGoods,
        'lstCrystalPacket': lstCrystalPacket,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CS7Shop(netData)


def GS2CS8Shop(oHero, oNPC, lstThirdPFPacket, lstGemPacket, iFullUpdate):
    oHero.IncMenuIdx()
    netData = {
        'iNpc': oNPC.m_ID,
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'iFullUpdate': iFullUpdate,
        'lstThirdPFPacket': lstThirdPFPacket,
        'lstGemPacket': lstGemPacket,
        'pid': oHero.m_PlayerID }
    npcnet.DN_GS2CS8Shop(netData)


def C2GSNPCInteract(oHero, iNpc, iType):
    oGame = oHero.m_Game
    oNpc = oGame.GetObject(iNpc)
    if not oNpc or oNpc.m_FightType & NWARRIOR_NPC != NWARRIOR_NPC:
        WarnpcLog.Debug('%s %s npc invalid' % (oGame.m_ID, oHero.m_PlayerID))
        return None
    WarnpcLog.Debug('%s %s npc%s interact %s' % (oGame.m_ID, oHero.m_PlayerID, oNpc.m_SID, iType))
    oNpc.Interact(oHero, iType)


def C2GSAnswerList(oHero, iMenuIdx, iAnswer, iPos):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_LIST):
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_LIST not in cbDict:
        WarnpcLog.Debug('%s %s %s list invalid' % (oHero.m_PlayerID, NPC_CB_LIST, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_LIST]
    cbfunc(oHero, iAnswer, iPos)


def C2GSAnswerValue(oHero, iMenuIdx, iAnswer):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_VALUE):
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_VALUE not in cbDict:
        WarnpcLog.Debug('%s %s %s value invalid' % (oHero.m_PlayerID, NPC_CB_VALUE, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_VALUE]
    cbfunc(oHero, iAnswer)


def C2GSChooseAll(oHero, iMenuIdx):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_CHOOSEALL):
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_CHOOSEALL not in cbDict:
        WarnpcLog.Debug('%s %s %s chooseall invalid' % (oHero.m_PlayerID, NPC_CB_CHOOSEALL, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_CHOOSEALL]
    cbfunc(oHero)


def C2GSNpcLockGoods(oHero, iNpc, pos, isLock):
    oGame = oHero.m_Game
    oNpc = oGame.GetObject(iNpc)
    if not oNpc or oNpc.m_FightType not in (NWARRIOR_NPC_SHOP, NWARRIOR_NPC_PHASESHOP):
        return None
    oNpc.LockGoods(oHero, pos, isLock)


def C2GSNPCInjectAnimaOperation(oHero, iMenuIdx, iNpc, iContainer, iTarget, isInject, iPos):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_INJECT):
        return None
    oGame = oHero.m_Game
    oNpc = oGame.GetObject(iNpc)
    if not oNpc or oNpc.m_FightType != NWARRIOR_NPC_WEAPONSTORE:
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_INJECT not in cbDict:
        WarnpcLog.Debug('%s %s %s iteminject invalid' % (oHero.m_PlayerID, NPC_CB_INJECT, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_INJECT]
    cbfunc(oHero, iContainer, iTarget, isInject, iPos)


def C2GSNpcRefresh(oHero, iMenuIdx):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_REFRESH):
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_REFRESH not in cbDict:
        WarnpcLog.Debug('%s %s %s refresh invalid' % (oHero.m_PlayerID, NPC_CB_REFRESH, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_REFRESH]
    cbfunc(oHero)


def C2GSAnswerValueList(oHero, iMenuIdx, lstAnswer):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_VALUELIST):
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_VALUELIST not in cbDict:
        WarnpcLog.Debug('%s %s %s valuelist invalid' % (oHero.m_PlayerID, NPC_CB_VALUELIST, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_VALUELIST]
    cbfunc(oHero, lstAnswer)


def C2GSNpcItemInteract(oHero, iMenuIdx, iItem, iAnswer):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_ITEM):
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_ITEM not in cbDict:
        WarnpcLog.Debug('%s %s %s item invalid' % (oHero.m_PlayerID, NPC_CB_ITEM, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_ITEM]
    cbfunc(oHero, iItem, iAnswer)


def C2GSNPCItemConInteract(oHero, iMenuIdx, iNpc, iFromContainer, iToContainer, iTarget, iFromInfo, iToInfo):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_ITEMCONOP):
        return None
    oGame = oHero.m_Game
    oNpc = oGame.GetObject(iNpc)
    if not oNpc or oNpc.m_FightType != NWARRIOR_NPC_WEAPONSTORE:
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_ITEMCONOP not in cbDict:
        WarnpcLog.Debug('%s %s %s itemconop invalid' % (oHero.m_PlayerID, NPC_CB_ITEMCONOP, cbDict))
        return None
    cbfunc = cbDict[NPC_CB_ITEMCONOP]
    cbfunc(oHero, iFromContainer, iToContainer, iTarget, iFromInfo, iToInfo)


def C2GSNPCClientStopInteract(oHero, iNpc):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.StopInteract(oHero)


def C2GSAnswerDict(oHero, iMenuIdx, lstQue):
    if not ValidNpcUICallBack(oHero, iMenuIdx, NPC_CB_DICT):
        return None
    (_, _, cbDict) = oHero.m_NpcUICallBack
    if NPC_CB_DICT not in cbDict:
        WarnpcLog.Debug('%s %s %s dict invalid' % (oHero.m_PlayerID, NPC_CB_DICT, cbDict))
        return None
    dQue = { }
    for key, val in lstQue:
        dQue[key] = val
    
    cbfunc = cbDict[NPC_CB_DICT]
    cbfunc(oHero, dQue)


def C2GSRandomRewardpf(who, iChoosepf):
    if who.QuerySavedData('RandomRewardFlag'):
        return None
    lstRewardpf = who.QuerySavedData('lstRewardpf', [])
    if iChoosepf in lstRewardpf:
        who.SetSavedData('RandomRewardFlag', iChoosepf)
        who.AddPerform(iChoosepf, 1)


def C2GSFarTransferLevel(who, iNpc):
    oGame = who.m_Game
    oNpc = oGame.GetObject(iNpc)
    if not oNpc or oNpc.m_FightType not in (NWARRIOR_NPC_TRANSFER, NWARRIOR_NPC_TRANSFERPOS):
        WarnpcLog.Alert('%s %s fartransfernpc invalid %s' % (oGame.m_ID, who.m_PlayerID, iNpc))
        return None
    iType = oNpc.m_TransferDir
    if iType == TRANSFER_DIRTO_HIDE:
        iLevel = oNpc.Query('HideLevel')
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oHideLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        WarnpcLog.Debug(f'''{oGame.m_ID} {who.m_PlayerID} tryfartransfer:{iLevel}''')
        if not oHideLevelNode:
            WarnpcLog.Debug(f'''{oGame.m_ID} {who.m_PlayerID} {who.m_Scene} nohidelevel {iLevel}''')
            return None
        if not oHideLevelNode.ValidTransfer(who):
            return None
        oHideLevelNode.AddTransferHero(who)
    iTemp = oNpc.m_CheckInteractDistance
    oNpc.m_CheckInteractDistance = False
    WarnpcLog.Debug('%s %s fartransfernpc%s interact %s' % (oGame.m_ID, who.m_PlayerID, oNpc.m_SID, iType))
    oNpc.Interact(who)
    oNpc.m_CheckInteractDistance = iTemp


def C2GSNpcChooseRelicByFuse(oHero, iNpc, iSuit, lstRelicInfo):
    oGame = oHero.m_Game
    oNpc = oGame.GetObject(iNpc)
    if not oNpc or not lstRelicInfo:
        return None
    oSeasonSuitElement = oGame.m_WarMgr.GetSeasonSuitElement()
    if oSeasonSuitElement:
        dCurSituate = oSeasonSuitElement.GetCurSituate(oHero)
        if iSuit not in dCurSituate:
            WarnpcLog.Debug('%s %s %s choose err no suit %s' % (oGame.m_ID, oHero.m_PlayerID, oNpc.m_SID, iSuit))
            return None
    oNpc.FuseBySubMode(oHero, lstRelicInfo, iSuit)


def C2GSXiaoJiuModifyAnswerValue(oHero, iMenuIdx, iAnswer):
    cbFunc = oHero.Query('ModifyChooseCallback')
    if not cbFunc:
        return None
    cbFunc(oHero, iMenuIdx, iAnswer)

