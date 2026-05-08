# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_dice/net.pyc
# RelativePath: clientlogic/cl_dice/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

import cl_duonet.dn_cl_dice_net as dicenet
from cl_cscommondef.cs_other import REFRESH_DICE_COM, REFRESH_DICE_ASSEMBLYINFO, REFRESH_DICE_CANROLLTIME, REFRESH_DICE_POINT, REFRESH_DICE_ATTACKTIMES

def GetStrPointRange(oDice):
    return oDice.GetStrPointRange()


def GetDiceAssemblePos(oDice):
    return oDice.GetDiceAssemblePos()


def GetRedDot(oDice):
    return oDice.GetRedDot()


def GetCanRollTimes(oDice):
    return oDice.GetCanRollTimes()


def GetOwner(oDice):
    oOwner = oDice.GetOwner()
    if oOwner:
        return oOwner.m_ID
    return 0

DICE_NETDATA_GET = {
    'ID': None,
    'Quality': None,
    'SID': None,
    'PointRange': GetStrPointRange,
    'RollPoint': None,
    'GetTime': None,
    'DiceAttackTimes': None,
    'Pos': GetDiceAssemblePos,
    'RedDot': GetRedDot,
    'CanRollTime': GetCanRollTimes,
    'Warrior': GetOwner }
DICE_REFRESH_REASON = {
    REFRESH_DICE_ATTACKTIMES: [
        'ID',
        'DiceAttackTimes'],
    REFRESH_DICE_POINT: [
        'ID',
        'RollPoint'],
    REFRESH_DICE_CANROLLTIME: [
        'ID',
        'CanRollTime'],
    REFRESH_DICE_ASSEMBLYINFO: [
        'Warrior',
        'ID',
        'Quality',
        'SID',
        'PointRange',
        'RollPoint',
        'Pos'],
    REFRESH_DICE_COM: [
        'ID',
        'Quality',
        'SID',
        'PointRange',
        'RollPoint',
        'Pos',
        'GetTime',
        'RedDot',
        'CanRollTime'] }

def GS2CRefreshDiceInfo(oGame, lstDice, dPlayer, iReason = 0):
    if iReason not in DICE_REFRESH_REASON:
        return None
    lstNetData = DICE_REFRESH_REASON[iReason]
    lstDiceInfo = []
    for oDice in lstDice:
        dDiceInfo = { }
        for sKey in lstNetData:
            oFunc = DICE_NETDATA_GET[sKey]
            if not oFunc:
                value = getattr(oDice, 'm_%s' % sKey)
            else:
                value = oFunc(oDice)
            dDiceInfo[sKey] = value
        
        lstDiceInfo.append(dDiceInfo)
    
    if not lstDiceInfo:
        return None
    netData = {
        'oGame': oGame,
        'iReason': iReason,
        'lstDiceInfo': lstDiceInfo,
        'dPlayer': dPlayer }
    dicenet.DN_GS2CRefreshDiceInfo(netData)


def GS2CAddDice(pid, oDice):
    if not oDice:
        return None
    netData = {
        'pid': pid,
        'iDiceID': oDice.m_ID,
        'iQuality': oDice.m_Quality,
        'iDiceAbilitySID': oDice.m_SID,
        'dPointsRange': oDice.m_PointRange,
        'iRollPoint': oDice.m_RollPoint,
        'iTime': oDice.m_GetTime,
        'bRetDot': oDice.GetRedDot(),
        'iCanRollTime': oDice.GetCanRollTimes() }
    dicenet.DN_GS2CAddDice(netData)


def GS2CRemoveDice(pid, iDiceID):
    netData = {
        'pid': pid,
        'iDiceID': iDiceID }
    dicenet.DN_GS2CRemoveDice(netData)


def GS2CRefreshMaxDiceAssemblyNum(pid, iNum, iExtraNum):
    netData = {
        'pid': pid,
        'iNum': iNum,
        'iExtraNum': iExtraNum }
    dicenet.DN_GS2CRefreshMaxDiceAssemblyNum(netData)


def GS2CSyncActiveDiceSpecialItem(pid, iSpecialItem, iCanUseTimes, iActiveCurDiceEnergy, iTriggerEnergy):
    iActiveCurDiceEnergy = iActiveCurDiceEnergy // 100
    iTriggerEnergy = iTriggerEnergy // 100
    netData = {
        'pid': pid,
        'iSpecialItem': iSpecialItem,
        'iCanUseTimes': iCanUseTimes,
        'iCurDiceEnergy': iActiveCurDiceEnergy,
        'iTriggerEnergy': iTriggerEnergy }
    dicenet.DN_GS2CSyncActiveDiceSpecialItem(netData)


def GS2CDiceSpecialItemInfo(pid, dSpecialItem):
    netData = {
        'pid': pid,
        'dSpecialItem': dSpecialItem }
    dicenet.DN_GS2CDiceSpecialItemInfo(netData)


def GS2CS6PackSignInfo(pid, dSignInfo):
    netData = {
        'pid': pid,
        'dSign': dSignInfo }
    dicenet.DN_GS2CS6PackSignInfo(netData)


def GS2CDiceSpecialItemResult(oOwner, iDiceID, lstSPItem, dPoint):
    dResultPoint = { }
    for iPos, iPoint in dPoint.items():
        dResultPoint[str(iPos)] = iPoint
    
    dDiceInfo = {
        'PointInfo': dResultPoint }
    oDice = oOwner.m_DiceCon.GetDiceByID(iDiceID)
    if oDice:
        dDiceInfo['DiceQuality'] = oDice.m_Quality
    netData = {
        'pid': oOwner.m_PlayerID,
        'iDiceID': iDiceID,
        'lstSPItem': lstSPItem,
        'sDiceInfo': dDiceInfo }
    dicenet.DN_GS2CDiceSpecialItemResult(netData)


def GS2CDiceSelectionPacketInfo(oHero, iQuality, dDice, dPointRange):
    netData = {
        'pid': oHero.m_PlayerID,
        'dDice': dDice,
        'iQuality': iQuality,
        'dPointRange': dPointRange,
        'iMenuIdx': oHero.m_NpcUIMenuIdx }
    dicenet.DN_GS2CDiceSelectionPacketInfo(netData)


def GS2CUpdateUnLockAbilityDesc(pid, dAbilityDesc):
    netData = {
        'pid': pid,
        'dAbilityDesc': { list(dQuality): iAbilitySID for iAbilitySID, dQuality in dAbilityDesc.items() } }
    dicenet.DN_GS2CUpdateUnLockAbilityDesc(netData)


def GS2CDiceSpecialItemGrooveInfo(pid, lstSpecialItem):
    netData = {
        'pid': pid,
        'lstSpecialItem': lstSpecialItem }
    dicenet.DN_GS2CDiceSpecialItemGrooveInfo(netData)


def GS2CDiceEnergy(pid, iEnergy, iChangeReason):
    netData = {
        'pid': pid,
        'iEnergy': iEnergy,
        'iChangeReason': iChangeReason }
    dicenet.DN_GS2CDiceEnergy(netData)


def GS2CDiceDropRollInfo(pid, iDropID, iPoint):
    netData = {
        'pid': pid,
        'iDropID': iDropID,
        'iPoint': iPoint }
    dicenet.DN_GS2CDiceDropRollInfo(netData)


def GS2CUpdateAddUpPoint(pid, iRollPoint):
    netData = {
        'pid': pid,
        'iRollPoint': iRollPoint }
    dicenet.DN_GS2CUpdateAddUpPoint(netData)


def C2GSRollDice(who, iDiceID, iOption):
    oDiceCon = who.m_DiceCon
    if oDiceCon:
        oDiceCon.RollDice(iDiceID, sReason = 'Roll')


def C2GSAssembleDice(who, iDiceID, iPos, iOption):
    oDiceCon = who.m_DiceCon
    if oDiceCon:
        oDiceCon.AssembleDice(iDiceID, iPos, iOption)


def C2GSDropDice(who, iDiceID):
    oDiceCon = who.m_DiceCon
    if oDiceCon:
        oDiceCon.RemoveDice(iDiceID)


def C2GSClearDiceRedDot(who, iDice):
    oDiceCon = who.m_DiceCon
    if oDiceCon:
        oDiceCon.ClearDiceRedDot(iDice)


def C2GSRecycleBagDice(who, iDice):
    oDiceCon = who.m_DiceCon
    if oDiceCon:
        oDiceCon.RecycleDice(iDice)


def C2GSChooseDiceResult(who, iDice, iPos, iSpecialItem):
    oDiceCon = who.m_DiceCon
    if not oDiceCon:
        return None
    oDiceCon.ChooseDiceResult(who, iDice, iPos, iSpecialItem)


def C2GSUseDiceSpecialItem(who, iPos, iSpecialItem, lstDice):
    oDiceCon = who.m_DiceCon
    if not oDiceCon:
        return None
    oDiceCon.UseDiceSpecialItem(who, iPos, iSpecialItem, lstDice)


def C2GSAddS6Sign(who, iType, iSID):
    oDiceCon = who.m_DiceCon
    if not oDiceCon:
        return None
    oDiceCon.AddSign(iType, iSID, iRefresh = 1)


def C2GSDelS6Sign(who, iType, iSID):
    oDiceCon = who.m_DiceCon
    if not oDiceCon:
        return None
    oDiceCon.DelSign(iType, iSID, iRefresh = 1)


def C2GSUpdateUnLockAbilityDesc(who, iDiceAbilitySID, iMaxUnlockQuality):
    oDiceCon = who.m_DiceCon
    if not oDiceCon:
        return None
    oDiceCon.UnLockAbilityQuality(iDiceAbilitySID, iMaxUnlockQuality)

