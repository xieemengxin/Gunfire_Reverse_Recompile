# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_npc_net.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_npc_net.pyc
# Source Generated with Decompyle++
# File: dn_cl_npc_net.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_npc.net

def DN_GS2CSystemAsk(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(1, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iTimeOut'], 2)
    cl_duonet.netfunc.PacketAddPSL(netdata['Title'], 1)
    cl_duonet.netfunc.PacketAddPSL(netdata['Text'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstAnswer']), 1)
    for Answer in netdata['lstAnswer']:
        cl_duonet.netfunc.PacketAddSL(Answer, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcShop(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(2, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstGoods']), 1)
    for pos, sid, goodstype, canbuy, hasbuy, cashtype, cash, isLock, allattr in netdata['lstGoods']:
        cl_duonet.netfunc.PacketAddI(pos, 1)
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(goodstype, 1)
        cl_duonet.netfunc.PacketAddI(canbuy, 1)
        cl_duonet.netfunc.PacketAddI(hasbuy, 1)
        cl_duonet.netfunc.PacketAddI(cashtype, 1)
        cl_duonet.netfunc.PacketAddI(cash, 4)
        cl_duonet.netfunc.PacketAddI(isLock, 1)
        cl_duonet.netfunc.PacketAddI(len(allattr), 1)
        for attr in allattr:
            cl_duonet.netfunc.PacketAttr(attr)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcShopSingleChange(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(3, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['pos'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['sid'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['goodstype'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['canbuy'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['hasbuy'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['cashtype'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['cash'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['isLock'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['allattr']), 1)
    for attr in netdata['allattr']:
        cl_duonet.netfunc.PacketAttr(attr)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcShopInteractResult(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(4, 1)
    cl_duonet.netfunc.PacketAddI(netdata['pos'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['sid'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['buy'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dExtraInfo']), 1)
    for sKey, iValue in netdata['dExtraInfo'].items():
        cl_duonet.netfunc.PacketAddSL(sKey, 1)
        cl_duonet.netfunc.PacketAddI(iValue, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcChooseTalent(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(5, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iTimeOutTime'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTalent']), 1)
    for sid, iLevel, sSubDesc in netdata['lstTalent']:
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
        cl_duonet.netfunc.PacketAddPSL(sSubDesc, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcReplaceTalent(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(6, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iTimeOutTime'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iSelectedTalent'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iTalentLevel'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTalent']), 1)
    for sid, iLevel in netdata['lstTalent']:
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcOpenCost(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(8, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstCost']), 1)
    for iType, sid, iNum in netdata['lstCost']:
        cl_duonet.netfunc.PacketAddI(iType, 1)
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(iNum, 2)
    
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CNpcItemInteract(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(9, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstItem']), 1)
    for iItem, lstOptionCost in netdata['lstItem']:
        cl_duonet.netfunc.PacketAddI(iItem, 4)
        cl_duonet.netfunc.PacketAddI(len(lstOptionCost), 1)
        for iOption, iCashType, iCost, iOptionStatus in lstOptionCost:
            cl_duonet.netfunc.PacketAddI(iOption, 1)
            cl_duonet.netfunc.PacketAddI(iCashType, 1)
            cl_duonet.netfunc.PacketAddI(iCost, 4)
            cl_duonet.netfunc.PacketAddI(iOptionStatus, 1)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcItemResult(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(10, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iItem'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iResult'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcInteractState(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(11, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iState'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iAssignInteractType'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CTransferDir(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(12, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iDir'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHideType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iHideLevel'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CNpcChooseReward(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(13, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMiniGame'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iSubOp'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstItem']), 1)
    for iItem, iType, pos, desc in netdata['lstItem']:
        cl_duonet.netfunc.PacketAddI(iItem, 2)
        cl_duonet.netfunc.PacketAddI(iType, 1)
        cl_duonet.netfunc.PacketPosFloat(pos)
        cl_duonet.netfunc.PacketAttr(desc)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcChooseMultiTalent(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(14, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iTimeOutTime'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstQue']), 1)
    for idx, lstTalent in netdata['lstQue']:
        cl_duonet.netfunc.PacketAddI(idx, 1)
        cl_duonet.netfunc.PacketAddI(len(lstTalent), 1)
        for sid, iLevel in lstTalent:
            cl_duonet.netfunc.PacketAddI(sid, 2)
            cl_duonet.netfunc.PacketAddI(iLevel, 1)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcEvent(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(15, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddPSL(netdata['sTitle'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstOption']), 1)
    for iOp, iValid, sOpTitle, iCostType, sCostTitle, iCostSID, iCostAmount, iRewardType, sRewardTitle, iRewardSID, attr, iRewardAmount in netdata['lstOption']:
        cl_duonet.netfunc.PacketAddI(iOp, 1)
        cl_duonet.netfunc.PacketAddI(iValid, 1)
        cl_duonet.netfunc.PacketAddPSL(sOpTitle, 1)
        cl_duonet.netfunc.PacketAddI(iCostType, 1)
        cl_duonet.netfunc.PacketAddPSL(sCostTitle, 1)
        cl_duonet.netfunc.PacketAddI(iCostSID, 2)
        cl_duonet.netfunc.PacketAddI(iCostAmount, 4)
        cl_duonet.netfunc.PacketAddI(iRewardType, 1)
        cl_duonet.netfunc.PacketAddPSL(sRewardTitle, 1)
        cl_duonet.netfunc.PacketAddI(iRewardSID, 2)
        cl_duonet.netfunc.PacketAttr(attr)
        cl_duonet.netfunc.PacketAddI(iRewardAmount, 4)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcChallengeStatus(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(16, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iStatus'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CTransferReadyStat(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(17, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iHero'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iIsReady'], 1)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CNPCEventChoose(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(18, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iCount'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstItem']), 1)
    for iItem in netdata['lstItem']:
        cl_duonet.netfunc.PacketAddI(iItem, 2)
    
    cl_duonet.netfunc.PacketAddI(netdata['iEventType'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CRefreshNPC(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(19, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iRewardType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iRewardSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iCost'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iLevel'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCostType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iLimit'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCount'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CSmithInteractInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(20, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iInteractTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxUpTimes'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstItem']), 1)
    for iItem, attr, iRecastTimes, iMaxRecastTimes, GeminiExcludeInfo in netdata['lstItem']:
        cl_duonet.netfunc.PacketAddI(iItem, 4)
        cl_duonet.netfunc.PacketAttr(attr)
        cl_duonet.netfunc.PacketAddI(iRecastTimes, 1)
        cl_duonet.netfunc.PacketAddI(iMaxRecastTimes, 1)
        cl_duonet.netfunc.PacketAddI(len(GeminiExcludeInfo), 1)
        for iType, iInscription in GeminiExcludeInfo:
            cl_duonet.netfunc.PacketAddI(iType, 1)
            cl_duonet.netfunc.PacketAddI(iInscription, 4)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcAnimator(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(21, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['Animator'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CRandomRewardpf(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(22, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstRewardpf']), 1)
    for iRewardpf in netdata['lstRewardpf']:
        cl_duonet.netfunc.PacketAddI(iRewardpf, 4)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CTransferScale(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(23, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['sx'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['sy'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['sz'], 4)
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CNpcRefreshInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(24, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCanRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxChooseAllTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCanChooseAllTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCost'], 4)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CBeneNpcResult(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(25, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iChat'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iBeneSID'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iResult'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CTransferFace(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(26, 1)
    cl_duonet.netfunc.PacketAddI(netdata['dx'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['dy'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['dz'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNPCEventWeaponAction(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(27, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iActionType'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpcType'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstInfo']), 1)
    for lstWeapon, iUpgradeLevel in netdata['lstInfo']:
        cl_duonet.netfunc.PacketAddI(len(lstWeapon), 1)
        for iWeapon, iPos, iValid, attr in lstWeapon:
            cl_duonet.netfunc.PacketAddI(iWeapon, 4)
            cl_duonet.netfunc.PacketAddI(iPos, 1)
            cl_duonet.netfunc.PacketAddI(iValid, 1)
            cl_duonet.netfunc.PacketAttr(attr)
        
        cl_duonet.netfunc.PacketAddI(iUpgradeLevel, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CVoteStat(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(28, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iVoteType'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstVote']), 1)
    for iHero, iStat in netdata['lstVote']:
        cl_duonet.netfunc.PacketAddI(iHero, 4)
        cl_duonet.netfunc.PacketAddI(iStat, 1)
    
    cl_duonet.netfunc.DGameBroadCast(netdata['oGame'])


def DN_GS2CRandomChoose(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(29, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iChoose'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstOption']), 1)
    for iOption, iOptionValue in netdata['lstOption']:
        cl_duonet.netfunc.PacketAddI(iOption, 4)
        cl_duonet.netfunc.PacketAddI(iOptionValue, 4)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CChoosePerform(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(30, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstPerform']), 1)
    for iPerform, iLevel in netdata['lstPerform']:
        cl_duonet.netfunc.PacketAddI(iPerform, 4)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CChosenRelicList(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(31, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstRelic']), 1)
    for iRelic in netdata['lstRelic']:
        cl_duonet.netfunc.PacketAddI(iRelic, 2)
    
    cl_duonet.netfunc.DGameSendToPlayers(netdata['oGame'], netdata['dPlayer'])


def DN_GS2CNpcModifyItem(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(32, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iTotalNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iUseNum'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNPCOpenWeaponStoreUI(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(33, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iAnimaCost'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstNotOperateWeapon']), 1)
    for iWeapon in netdata['lstNotOperateWeapon']:
        cl_duonet.netfunc.PacketAddI(iWeapon, 4)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CCommonTalentChoose(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(34, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTalent']), 1)
    for sid in netdata['lstTalent']:
        cl_duonet.netfunc.PacketAddI(sid, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CCommonTalentChosen(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(35, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTalent']), 1)
    for sid in netdata['lstTalent']:
        cl_duonet.netfunc.PacketAddI(sid, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcTask(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(36, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iCanRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTask']), 1)
    for Idx, SID, iEnable, iTargetSID in netdata['lstTask']:
        cl_duonet.netfunc.PacketAddI(Idx, 1)
        cl_duonet.netfunc.PacketAddI(SID, 2)
        cl_duonet.netfunc.PacketAddI(iEnable, 1)
        cl_duonet.netfunc.PacketAddI(iTargetSID, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CPhaseGoldenCount(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(37, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCount'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CWeaponAnimaInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(38, 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstWeaponInfo']), 1)
    for iWeapon, iPos, dInfo in netdata['lstWeaponInfo']:
        cl_duonet.netfunc.PacketAddI(iWeapon, 4)
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAttr(dInfo)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CWeaponInjectAnimaInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(39, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iWeapon'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iPos'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iResult'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CExchangeNpcChooseTalent(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(40, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstTalent']), 1)
    for sid, iLevel, sSubDesc in netdata['lstTalent']:
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
        cl_duonet.netfunc.PacketAddPSL(sSubDesc, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CNpcChooseEnable(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(41, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iEnable'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CPetShop(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(42, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstPetGoods']), 1)
    for pos, sid, canbuy, hasbuy, cashtype, cash, dOffset, attr, lstAbility in netdata['lstPetGoods']:
        cl_duonet.netfunc.PacketAddI(pos, 1)
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(canbuy, 1)
        cl_duonet.netfunc.PacketAddI(hasbuy, 1)
        cl_duonet.netfunc.PacketAddI(cashtype, 1)
        cl_duonet.netfunc.PacketAddI(cash, 4)
        cl_duonet.netfunc.PacketAttrOffset(dOffset)
        cl_duonet.netfunc.PacketAttr(attr)
        cl_duonet.netfunc.PacketAddI(len(lstAbility), 1)
        for iPerform in lstAbility:
            cl_duonet.netfunc.PacketAddI(iPerform, 2)
        
    
    cl_duonet.netfunc.PacketAddI(netdata['iMaxRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iCanRefreshTimes'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CPetSellPrice(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(43, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['dPetPrice']), 1)
    for iPet, iPrice in netdata['dPetPrice'].items():
        cl_duonet.netfunc.PacketAddI(iPet, 4)
        cl_duonet.netfunc.PacketAddI(iPrice, 4)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CCheckFusePoint(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(44, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCheckFusePoint'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CRefreshRollNpcData(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(45, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMode'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['dRelic']), 1)
    for iRelic, isPick in netdata['dRelic'].items():
        cl_duonet.netfunc.PacketAddI(iRelic, 2)
        cl_duonet.netfunc.PacketAddI(isPick, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CSyncFuseCount(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(46, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iCount'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2COpenReduceSuitTakeEffectAmountUI(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(47, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iNum'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iUI'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstSuit']), 1)
    for iSuit in netdata['lstSuit']:
        cl_duonet.netfunc.PacketAddI(iSuit, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CUpdateCheckReduceSuitResult(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(48, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iSuit'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iResult'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CRelicLotteryNpcData(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(49, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstBefore']), 1)
    for iQuality, iRelic, iLevel in netdata['lstBefore']:
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
        cl_duonet.netfunc.PacketAddI(iRelic, 2)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
    
    cl_duonet.netfunc.PacketAddI(netdata['iReInteractProb'], 1)
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CWandShop(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(50, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iCanRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstGoods']), 1)
    for pos, type, sid, cash, sellout, level, reason in netdata['lstGoods']:
        cl_duonet.netfunc.PacketAddI(pos, 1)
        cl_duonet.netfunc.PacketAddI(type, 1)
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(cash, 2)
        cl_duonet.netfunc.PacketAddI(sellout, 1)
        cl_duonet.netfunc.PacketAddI(level, 1)
        cl_duonet.netfunc.PacketAddI(reason, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CWandShopCardPackInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(51, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iType'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstCardPack']), 1)
    for pos, sid, iLevel in netdata['lstCardPack']:
        cl_duonet.netfunc.PacketAddI(pos, 1)
        cl_duonet.netfunc.PacketAddI(sid, 2)
        cl_duonet.netfunc.PacketAddI(iLevel, 1)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CWandShopRollInfo(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(52, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iWandID'], 4)
    cl_duonet.netfunc.PacketAddI(len(netdata['dInfo']), 1)
    for iOption, lstAbilities in netdata['dInfo'].items():
        cl_duonet.netfunc.PacketAddI(iOption, 1)
        cl_duonet.netfunc.PacketAddI(len(lstAbilities), 1)
        for iSID, iQuality, iFloatingRange in lstAbilities:
            cl_duonet.netfunc.PacketAddI(iSID, 2)
            cl_duonet.netfunc.PacketAddI(iQuality, 1)
            cl_duonet.netfunc.PacketAddI(iFloatingRange, 1)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceShop(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(53, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iCanRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(netdata['iMaxRefreshTimes'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstGoods']), 1)
    for iPos, iAbilitySID, dAbility, iDiceQuality, iCostEnergy, iSellout, iCurPoint in netdata['lstGoods']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iAbilitySID, 2)
        cl_duonet.netfunc.PacketAddI(len(dAbility), 1)
        for iQuality, lstPointRange in dAbility.items():
            cl_duonet.netfunc.PacketAddI(iQuality, 1)
            cl_duonet.netfunc.PacketAddI(len(lstPointRange), 1)
            for iPoint in lstPointRange:
                cl_duonet.netfunc.PacketAddI(iPoint, 1)
            
        
        cl_duonet.netfunc.PacketAddI(iDiceQuality, 1)
        cl_duonet.netfunc.PacketAddI(iCostEnergy, 2)
        cl_duonet.netfunc.PacketAddI(iSellout, 1)
        cl_duonet.netfunc.PacketAddI(iCurPoint, 1)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstDicePacket']), 1)
    for iPos, iQuality, iCostEnergy, iSellout, iNextTimePacketCash in netdata['lstDicePacket']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iQuality, 1)
        cl_duonet.netfunc.PacketAddI(iCostEnergy, 2)
        cl_duonet.netfunc.PacketAddI(iSellout, 1)
        cl_duonet.netfunc.PacketAddI(iNextTimePacketCash, 2)
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CDiceShopRecycleDiceCnt(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(55, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iRecycleDiceCnt'], 1)
    cl_duonet.netfunc.DGamePacketSend(netdata['oGame'], netdata['pid'])


def DN_GS2CS7Shop(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(56, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iFullUpdate'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstModulePacket']), 1)
    for iPos, iSellout, iCost, iRefreshTimes, iMaxRefreshTimes, lstModulePacketGoods in netdata['lstModulePacket']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iSellout, 1)
        cl_duonet.netfunc.PacketAddI(iCost, 2)
        cl_duonet.netfunc.PacketAddI(iRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(iMaxRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(len(lstModulePacketGoods), 1)
        for iSID, iQuality in lstModulePacketGoods:
            cl_duonet.netfunc.PacketAddI(iSID, 2)
            cl_duonet.netfunc.PacketAddI(iQuality, 1)
        
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstCrystalGoods']), 1)
    for iPos, iSID, lstGoodsPoint, iSellout, iCost in netdata['lstCrystalGoods']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iSID, 2)
        cl_duonet.netfunc.PacketAddI(len(lstGoodsPoint), 1)
        for iEffX, iEffY, iPoint in lstGoodsPoint:
            cl_duonet.netfunc.PacketAddI(iEffX, 4)
            cl_duonet.netfunc.PacketAddI(iEffY, 4)
            cl_duonet.netfunc.PacketAddI(iPoint, 1)
        
        cl_duonet.netfunc.PacketAddI(iSellout, 1)
        cl_duonet.netfunc.PacketAddI(iCost, 2)
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstCrystalPacket']), 1)
    for iPos, iSellout, iCost, iRefreshTimes, iMaxRefreshTimes, iMaxPoint, lstCrystalPacketGoods in netdata['lstCrystalPacket']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iSellout, 1)
        cl_duonet.netfunc.PacketAddI(iCost, 2)
        cl_duonet.netfunc.PacketAddI(iRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(iMaxRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(iMaxPoint, 1)
        cl_duonet.netfunc.PacketAddI(len(lstCrystalPacketGoods), 1)
        for iPos, iSID, lstPacketPoint in lstCrystalPacketGoods:
            cl_duonet.netfunc.PacketAddI(iPos, 1)
            cl_duonet.netfunc.PacketAddI(iSID, 2)
            cl_duonet.netfunc.PacketAddI(len(lstPacketPoint), 1)
            for iEffX, iEffY, iPoint in lstPacketPoint:
                cl_duonet.netfunc.PacketAddI(iEffX, 4)
                cl_duonet.netfunc.PacketAddI(iEffY, 4)
                cl_duonet.netfunc.PacketAddI(iPoint, 1)
            
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_GS2CS8Shop(netdata):
    cl_duonet.netfunc.PacketPrepare(80)
    cl_duonet.netfunc.PacketAddI(57, 1)
    cl_duonet.netfunc.PacketAddI(netdata['iNpc'], 4)
    cl_duonet.netfunc.PacketAddI(netdata['iMenuIdx'], 2)
    cl_duonet.netfunc.PacketAddI(netdata['iFullUpdate'], 1)
    cl_duonet.netfunc.PacketAddI(len(netdata['lstThirdPFPacket']), 1)
    for iPos, iSellout, iCost, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes, lstThirdPFPacketGoods in netdata['lstThirdPFPacket']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iSellout, 1)
        cl_duonet.netfunc.PacketAddI(iCost, 2)
        cl_duonet.netfunc.PacketAddI(iBaseRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(iExtraRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(iMaxRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(len(lstThirdPFPacketGoods), 1)
        for iSID, iQuality, dAbility in lstThirdPFPacketGoods:
            cl_duonet.netfunc.PacketAddI(iSID, 2)
            cl_duonet.netfunc.PacketAddI(iQuality, 1)
            cl_duonet.netfunc.PacketAddI(len(dAbility), 1)
            for iAbilitySID, iQuality in dAbility.items():
                cl_duonet.netfunc.PacketAddI(iAbilitySID, 2)
                cl_duonet.netfunc.PacketAddI(iQuality, 1)
            
        
    
    cl_duonet.netfunc.PacketAddI(len(netdata['lstGemPacket']), 1)
    for iPos, iSellout, iCost, iBaseRefreshTimes, iExtraRefreshTimes, iMaxRefreshTimes, lstGemPacketGoods in netdata['lstGemPacket']:
        cl_duonet.netfunc.PacketAddI(iPos, 1)
        cl_duonet.netfunc.PacketAddI(iSellout, 1)
        cl_duonet.netfunc.PacketAddI(iCost, 2)
        cl_duonet.netfunc.PacketAddI(iBaseRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(iExtraRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(iMaxRefreshTimes, 1)
        cl_duonet.netfunc.PacketAddI(len(lstGemPacketGoods), 1)
        for iSID, iQuality in lstGemPacketGoods:
            cl_duonet.netfunc.PacketAddI(iSID, 2)
            cl_duonet.netfunc.PacketAddI(iQuality, 1)
        
    
    cl_duonet.netfunc.PacketSend(netdata['pid'])


def DN_C2GSNPCInteract(who):
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    iType = cl_duonet.netfunc.UnpackInt(1)
    cl_npc.net.C2GSNPCInteract(who, iNpc, iType)


def DN_C2GSAnswerList(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    iAnswer = cl_duonet.netfunc.UnpackInt(2)
    iPos = cl_duonet.netfunc.UnpackInt(2)
    cl_npc.net.C2GSAnswerList(who, iMenuIdx, iAnswer, iPos)


def DN_C2GSNpcRefresh(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    cl_npc.net.C2GSNpcRefresh(who, iMenuIdx)


def DN_C2GSAnswerValue(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    iAnswer = cl_duonet.netfunc.UnpackInt(4)
    cl_npc.net.C2GSAnswerValue(who, iMenuIdx, iAnswer)


def DN_C2GSNpcItemInteract(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    iItem = cl_duonet.netfunc.UnpackInt(4)
    iOption = cl_duonet.netfunc.UnpackInt(1)
    cl_npc.net.C2GSNpcItemInteract(who, iMenuIdx, iItem, iOption)


def DN_C2GSNPCClientStopInteract(who):
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    cl_npc.net.C2GSNPCClientStopInteract(who, iNpc)


def DN_C2GSAnswerDict(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    lstQue = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        ikey = cl_duonet.netfunc.UnpackInt(2)
        iAnswer = cl_duonet.netfunc.UnpackInt(4)
        lstQue.append((ikey, iAnswer))
    
    cl_npc.net.C2GSAnswerDict(who, iMenuIdx, lstQue)


def DN_C2GSAnswerValueList(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    lstAnswer = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iAnswer = cl_duonet.netfunc.UnpackInt(4)
        lstAnswer.append(iAnswer)
    
    cl_npc.net.C2GSAnswerValueList(who, iMenuIdx, lstAnswer)


def DN_C2GSRandomRewardpf(who):
    iChoosepf = cl_duonet.netfunc.UnpackInt(4)
    cl_npc.net.C2GSRandomRewardpf(who, iChoosepf)


def DN_C2GSFarTransferLevel(who):
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    cl_npc.net.C2GSFarTransferLevel(who, iNpc)


def DN_C2GSNPCItemConInteract(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    iFromContainer = cl_duonet.netfunc.UnpackInt(1)
    iToContainer = cl_duonet.netfunc.UnpackInt(1)
    iTarget = cl_duonet.netfunc.UnpackInt(4)
    iFromInfo = cl_duonet.netfunc.UnpackInt(4)
    iToInfo = cl_duonet.netfunc.UnpackInt(4)
    cl_npc.net.C2GSNPCItemConInteract(who, iMenuIdx, iNpc, iFromContainer, iToContainer, iTarget, iFromInfo, iToInfo)


def DN_C2GSChooseAll(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    cl_npc.net.C2GSChooseAll(who, iMenuIdx)


def DN_C2GSNpcLockGoods(who):
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    pos = cl_duonet.netfunc.UnpackInt(1)
    isLock = cl_duonet.netfunc.UnpackInt(1)
    cl_npc.net.C2GSNpcLockGoods(who, iNpc, pos, isLock)


def DN_C2GSNPCInjectAnimaOperation(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    iContainer = cl_duonet.netfunc.UnpackInt(1)
    iWeapon = cl_duonet.netfunc.UnpackInt(4)
    isInject = cl_duonet.netfunc.UnpackInt(1)
    iPos = cl_duonet.netfunc.UnpackInt(1)
    cl_npc.net.C2GSNPCInjectAnimaOperation(who, iMenuIdx, iNpc, iContainer, iWeapon, isInject, iPos)


def DN_C2GSNpcChooseRelicByFuse(who):
    iNpc = cl_duonet.netfunc.UnpackInt(4)
    iSuit = cl_duonet.netfunc.UnpackInt(2)
    lstRelicInfo = []
    for _ in range(cl_duonet.netfunc.UnpackInt(1)):
        iRelic = cl_duonet.netfunc.UnpackInt(2)
        lstRelicInfo.append(iRelic)
    
    cl_npc.net.C2GSNpcChooseRelicByFuse(who, iNpc, iSuit, lstRelicInfo)


def DN_C2GSXiaoJiuModifyAnswerValue(who):
    iMenuIdx = cl_duonet.netfunc.UnpackInt(2)
    iAnswer = cl_duonet.netfunc.UnpackInt(4)
    cl_npc.net.C2GSXiaoJiuModifyAnswerValue(who, iMenuIdx, iAnswer)

