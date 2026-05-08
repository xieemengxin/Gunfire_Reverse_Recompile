# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wand/net.pyc
# RelativePath: clientlogic/cl_wand/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

import cl_duonet.dn_cl_wand_net as wandnet

def GS2CWandOption(oGame, pid, iOption, iWandID):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iOption': iOption,
        'iWandID': iWandID }
    wandnet.DN_GS2CWandOption(netData)


def GS2CAddWand(oGame, iHero, dPlayer, oWand, bSyncOtherPlayer = False):
    (iLevel, iColdTime, iConditionCompNum, iActionCompNum, lstComInfo, lstAbilities) = oWand.GetWandShowInfo()
    netData = {
        'oGame': oGame,
        'iWarrior': iHero,
        'iWandID': oWand.m_ID,
        'iWandSID': oWand.m_SID,
        'iCD': iColdTime,
        'iRareLevel': iLevel,
        'iConditionGrooveNum': iConditionCompNum,
        'iBehaviorGrooveNum': iActionCompNum,
        'lstComp': lstComInfo,
        'dPlayer': dPlayer,
        'bRetDot': oWand.GetRedDot(),
        'bSyncOtherPlayer': bSyncOtherPlayer,
        'lstAbilities': lstAbilities,
        'lstLockWandAbility': oWand.GetLockWandAbility(),
        'lstCarryAbility': oWand.m_CarryWandAbility }
    wandnet.DN_GS2CAddWand(netData)


def GS2CUpdateWandComp(oGame, iHero, dPlayer, oWand):
    netData = {
        'oGame': oGame,
        'iWarrior': iHero,
        'iWandID': oWand.m_ID,
        'lstComp': oWand.GetCompInfo(),
        'dPlayer': dPlayer }
    wandnet.DN_GS2CUpdateWandComp(netData)


def GS2CUpdateBagComp(oGame, pid, lstCompInfo):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'WandComp': lstCompInfo }
    wandnet.DN_GS2CUpdateBagComp(netData)


def GS2CWandGroupSendOption(oGame, iHero, dPlayer, iOption, iWand):
    netData = {
        'oGame': oGame,
        'iWarrior': iHero,
        'iWandID': iWand,
        'iOption': iOption,
        'dPlayer': dPlayer }
    wandnet.DN_GS2CWandGroupSendOption(netData)


def GS2CWandCastingConditions(oGame, pid, iWand, iCDDownFrame, iCD, lstComp):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iWandID': iWand,
        'iCDDownFrame': iCDDownFrame,
        'iCD': iCD,
        'lstComp': lstComp }
    wandnet.DN_GS2CWandCastingConditions(netData)


def GS2CWandConditionCompCountChange(oGame, pid, iWand, iComp, iCount):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iWandID': iWand,
        'iComp': iComp,
        'iCount': iCount }
    wandnet.DN_GS2CWandConditionCompCountChange(netData)


def GS2CWandCountChange(oGame, pid, iWand, iCount):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iWandID': iWand,
        'iCount': iCount }
    wandnet.DN_GS2CWandCountChange(netData)


def GS2CWandCountInfo(oGame, pid, iWand, iCount, iMaxCount):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iWandID': iWand,
        'iCurCount': iCount,
        'iMaxCount': iMaxCount }
    wandnet.DN_GS2CWandCountInfo(netData)


def GS2CAddWandNotify(oGame, pid, iType, iSID, iLevel, iUpgrade):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iType': iType,
        'iSID': iSID,
        'iLevel': iLevel,
        'iUpgrade': iUpgrade }
    wandnet.DN_GS2CAddWandNotify(netData)


def GS2CWandPropChange(oGame, pid, iWand, iScene, dPropInfo, dPlayer):
    netData = {
        'oGame': oGame,
        'iWarrior': pid,
        'iTarget': iWand,
        'iScene': iScene,
        'dPropInfo': dPropInfo,
        'dPlayer': dPlayer }
    wandnet.DN_GS2CWandPropChange(netData)


def GS2CS5PackSignInfo(oGame, pid, dSignInfo):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'dSign': dSignInfo }
    wandnet.DN_GS2CS5PackSignInfo(netData)


def GS2CWandActCompTrigger(oGame, pid, iWand, iCompPos, iNeedCount, iCount, iEndFrame, iTime):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iWandID': iWand,
        'iCompPos': iCompPos,
        'iNeedCount': iNeedCount,
        'iCount': iCount,
        'iEndFrame': iEndFrame,
        'iTime': iTime }
    wandnet.DN_GS2CWandActCompTrigger(netData)


def GS2CWandActCompInstantTrigger(oGame, pid, iWand, iCompPos):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iWandID': iWand,
        'iCompPos': iCompPos }
    wandnet.DN_GS2CWandActCompInstantTrigger(netData)


def GS2CDropWandAbilities(oGame, iDrop, lstAbilities, dPlayer):
    netData = {
        'oGame': oGame,
        'dPlayer': dPlayer,
        'iWandDropID': iDrop,
        'lstAbilities': lstAbilities }
    wandnet.DN_GS2CDropWandAbilities(netData)


def C2GSWandOption(who, iOption, iWandID):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.ChooseOption(iOption, iWandID)


def C2GSWandCompOption(who, iOption, iWandID, iCompPos, iComp, iLevel):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.ChooseOption(iOption, iWandID, iCompPos, iComp, iLevel)


def C2GSBagCompOption(who, iOption, iComp, iLevel):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.ChooseOption(iOption, iComp, iLevel)


def C2GSClearWandRedDot(who, iWand):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.ClearWandRedDot(iWand)


def C2GSClearCompRedDot(who, iComp, iLevel):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.ClearCompRedDot(iComp, iLevel)


def C2GSBatchRecycleBagComp(who, lstComp):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.BatchRecycleComp(lstComp)


def C2GSAddS5Sign(who, iType, iSID):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.AddSign(iType, iSID)


def C2GSDelS5Sign(who, iType, iSID):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.DelSign(iType, iSID)


def C2GSQuickAddComp(who, iWandID, lstComp):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.QuickAddWandComp(iWandID, lstComp)


def C2GSLockWandAbility(who, iWandID, iAbility, iLock):
    oWandCon = who.m_WandCon
    if not oWandCon:
        return None
    oWandCon.LockWandAbility(iWandID, iAbility, iLock)

