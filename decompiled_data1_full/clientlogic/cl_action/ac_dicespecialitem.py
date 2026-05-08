# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_action/ac_dicespecialitem.pyc
# RelativePath: clientlogic/cl_action/ac_dicespecialitem.pyc
# Source Generated with Decompyle++
# File: ac_dicespecialitem.pyc (Python 3.6)

from cl_only import ChooseKey, ShufferList
import cl_dice.net as dicenet
import cl_formula
import cl_state
import cl_object
from cl_only import SendAlert, Functor, Time2Frame
from cl_object.logging import OtherLog
from cl_commondefines import STATE_TIME_LIMIT, STATE_TIME_FOREVER

def SendSpecialItemResult(oOwner, iDice, iItem, dPoint = None):
    if dPoint is None:
        dPoint = { }
    dicenet.GS2CDiceSpecialItemResult(oOwner, iDice, [
        iItem], dPoint)


def SpecialItemClearDicePoints(oOwner, lstDice, dInfo):
    if not lstDice:
        return None
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = lstDice[0]
    oDiceCon.ClearDicePoints(iDice, 'Clear-%d' % dInfo['Item'])
    SendSpecialItemResult(oOwner, iDice, dInfo['Item'])


def SpecialItemReThrowDicePoints(oOwner, lstDice, dInfo):
    
    def MarDice(oOwner, iPoints):
        SendSpecialItemResult(oOwner, iReThrowDice, iSpecialItem, {
            0: iPoints })

    if not lstDice:
        return None
    iSpecialItem = dInfo['Item']
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iReThrowDice = lstDice[0]
    if not oDiceCon.CheckDiceRoll(iReThrowDice):
        OtherLog.Debug('%s %s dice no roll %s' % (oOwner.m_Game.m_ID, oOwner.m_PlayerID, iReThrowDice))
        return None
    oDiceCon.ReThrowDice(iReThrowDice, sReason = 'ReThrow-%d' % iSpecialItem, cbfunc = Functor(MarDice, oOwner), iDirectSpItem = iSpecialItem)


def SpecialItemProcessDice(oOwner, lstDice, dInfo, iPointRange):
    if not lstDice:
        return None
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = lstDice[0]
    iAddPoints = oOwner.m_Game.Random(iPointRange) + 1
    oDiceCon.AddDicePoints(iDice, iAddPoints, sReason = 'Process-%d' % dInfo['Item'], iDirectSpItem = dInfo['Item'])
    SendSpecialItemResult(oOwner, iDice, dInfo['Item'], dPoint = {
        0: iAddPoints })


def SpecialItemAddThrowResultNum(oOwner, lstDice, dInfo, iAddResultNum):
    if 'ExtraResultNum' in dInfo:
        dInfo['ExtraResultNum'] += iAddResultNum
    else:
        dInfo['ExtraResultNum'] = iAddResultNum


def SpecialItemCopyDice(oOwner, lstDice, dInfo, iCopyNum):
    if not lstDice:
        return None
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = lstDice[0]
    oDiceCon.CopyDice(iDice, iCopyNum, sReason = 'Copy-%d' % dInfo['Item'])
    SendSpecialItemResult(oOwner, iDice, dInfo['Item'])


def SpecialItemChangeRollWeightByMul(oOwner, lstDice, dInfo, dData):
    oDiceElement = oOwner.m_Game.m_WarMgr.GetDiceElement()
    if not oDiceElement:
        return None
    for iMaxPointRange, dInfo in dData.items():
        lstPoint = []
        for iLeastCommonMultiple, iChangeRatio in dInfo.items():
            if iLeastCommonMultiple in lstPoint:
                SendAlert('err', '【特殊道具根据倍数修改点数权重】配置的最大公约数区间重复，请检查')
                return None
            dChangeInfo = { iChangeRatio: iPoint for iPoint in range(iLeastCommonMultiple, iMaxPointRange + 1, iLeastCommonMultiple) }
            oDiceElement.ChangeHeroRollPointWeight(oOwner.m_PlayerID, iMaxPointRange, dChangeInfo)
        
    


def SpecialItemRollAllGoodsDice(oOwner, lstDice, dInfo):
    if 'ShopNpc' not in dInfo:
        return None
    iNpc = dInfo['ShopNpc']
    oNpc = oOwner.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    oNpc.RollAllGoodsDice(oOwner)


def SpecialItemFuseDice(oOwner, lstDice, dInfo):
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = oDiceCon.FuseDice(lstDice, sReason = 'FuseDice-%d' % dInfo['Item'])
    if iDice:
        SendSpecialItemResult(oOwner, iDice, dInfo['Item'])


def SpecialItemProcessDiceQuality(oOwner, lstDice, dInfo):
    if 'ShopNpc' not in dInfo:
        return None
    iNpcID = dInfo['ShopNpc']
    oNpc = oOwner.m_Game.GetObject(iNpcID)
    if not oNpc:
        return None
    oNpc.UpgradeDiceGood(oOwner)


def SpecialItemExtractThrowExcludePoints(oOwner, lstDice, dInfo, dExtractPoints, dAdditionPoints):
    if not lstDice:
        return None
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = lstDice[0]
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return None
    lstUnExcludePoints = list(dInfo['ResultPoint'])
    lstUnExcludePoints.append(oDiceCon.GetRollPointMin())
    for iUnExcludePoints in lstUnExcludePoints:
        if iUnExcludePoints in dExtractPoints:
            dExtractPoints.pop(iUnExcludePoints)
        for iAdditionPoints in dAdditionPoints:
            iPoint = iUnExcludePoints - iAdditionPoints
            if iPoint in dExtractPoints:
                dExtractPoints.pop(iPoint)
        
    
    iExcludePoints = ChooseKey(oOwner.m_Game, dExtractPoints)
    iDicePointMax = oDice.GetMaxPoint()
    if iExcludePoints > iDicePointMax:
        return None
    dTrueExcludePoints = {
        iExcludePoints: 1 }
    for iAdditionPoints in dAdditionPoints:
        iPoints = iExcludePoints + iAdditionPoints
        if iPoints > iDicePointMax:
            continue
        dTrueExcludePoints[iPoints] = 1
    
    dExcludePoints = dInfo['ExcludePoints']
    dExcludePoints.update(dTrueExcludePoints)
    SendSpecialItemResult(oOwner, iDice, dInfo['Item'], dTrueExcludePoints)


def SpecialItemTransferChooseDice(oOwner, lstDice, dInfo, iChooseNum):
    if not lstDice:
        return None
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = lstDice[0]
    sReason = 'TransferItem-%d' % dInfo['Item']
    dResult = oDiceCon.GetTransferDiceSID(iDice, dInfo['Item'], sReason, iChooseNum)
    if dResult:
        SendSpecialItemResult(oOwner, iDice, dInfo['Item'], dResult)


def SpecialItemPassiveAddState(oOwner, dInfo, iState, iTime, dArgs):
    dData = { }
    dRet = cl_formula.CalArgsFormula(oOwner, dArgs, dData)
    if iTime:
        iTimeType = STATE_TIME_LIMIT
        iTime = Time2Frame(iTime)
    else:
        iTimeType = STATE_TIME_FOREVER
    dArgs = {
        'AID': oOwner.m_ID,
        'RS': cl_object.reason.CStrReason('dicespecialitem %d passiveaddState %d' % (dInfo['Item'], iState)),
        'arg': dRet }
    oState = cl_state.AddState(oOwner, iState, iTimeType, iTime, dArgs)
    if not oState:
        return None
    oState.Enable(oOwner)


def SpecialItemSplitThrowDicePoints(oOwner, lstDice, dInfo, iSplitPoints):
    if not lstDice:
        return None
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = lstDice[0]
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return None
    iMaxPoint = oDice.GetMaxPoint()
    if iSplitPoints > iMaxPoint:
        return None
    iThrowCnt = iMaxPoint // iSplitPoints
    dPoints = { }
    iAllPoints = 0
    for idx in range(iThrowCnt):
        iPoints = oOwner.m_Game.Random(iSplitPoints) + 1
        iAllPoints += iPoints
        dPoints[idx] = iPoints
    
    if iAllPoints in dInfo['ExcludePoints']:
        for idx, iPoints in list(dPoints.items()):
            if iPoints == iSplitPoints:
                continue
            dPoints[idx] = iPoints + 1
            iAllPoints += 1
        
    iAnchoringPoint = oDiceCon.GetRollPointMin()
    iDifference = iAnchoringPoint - iAllPoints
    if iDifference > 0:
        lstPoints = []
        for iPoints in dPoints.values():
            if iDifference:
                iAddPoints = min(iDifference, iMaxPoint - iPoints)
                iDifference -= iAddPoints
                lstPoints.append(iPoints + iAddPoints)
                iAllPoints += iAddPoints
                continue
            lstPoints.append(iPoints)
        
        lstPoints = ShufferList(oOwner.m_Game, lstPoints)
        dPoints = { }
        for idx, iPoints in enumerate(lstPoints):
            dPoints[idx] = iPoints
        
    dInfo['ResultPoint'] = {
        iAllPoints: 1 }
    SendSpecialItemResult(oOwner, iDice, dInfo['Item'], dPoints)


def SpecialItemAddDicePacketPointsShowCnt(oOwner, _lstDice, _dInfo, iShowCnt):
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    oDiceCon.ChangeDicePacketPointsShowCnt(iShowCnt)


def SpecialItemAddDiceRandomPoints(oOwner, lstDice, dInfo, iMaxAddPoint, dEffectPoints):
    
    def BeforeSetPointFunc(oTarget, iDice, iSpecialItem, iMaxAddPoint, dEffectPoints, dPointResult):
        if not oTarget:
            return None
        if not dPointResult or len(dPointResult) > 1:
            return None
        iRollPoint = dPointResult[0]
        if iRollPoint not in dEffectPoints:
            return None
        iMaxPoint = dEffectPoints[iRollPoint]
        iRandomAddPoint = oTarget.m_Game.Random(iMaxAddPoint) + 1
        iResultPoint = iRandomAddPoint + iRollPoint
        oDice = oTarget.m_DiceCon.GetDiceByID(iDice) if oTarget.m_DiceCon else None
        if not oDice:
            return None
        if iResultPoint > iMaxPoint:
            SendAlert('err', '【特殊道具增加骰子随机点数】增加数值超出阈值，请检查配置 %s %s %s' % (iRollPoint, iRandomAddPoint, iMaxPoint))
            iResultPoint = iMaxPoint
            iRandomAddPoint = iResultPoint - iRollPoint
        SendSpecialItemResult(oTarget, iDice, iSpecialItem, {
            0: iRollPoint,
            1: iRandomAddPoint })
        dPointResult[0] = iResultPoint

    if not lstDice:
        return None
    dInfo['BeforeSetPointFunc'] = Functor(BeforeSetPointFunc, oOwner, lstDice[0], dInfo['Item'], iMaxAddPoint, dEffectPoints)


def SpecialItemAddDiceMaxAssembly(oOwner, lstDice, dInfo, iAdd, dData):
    oDiceCon = oOwner.m_DiceCon
    oDiceElement = oOwner.m_Game.m_WarMgr.GetDiceElement()
    if not oDiceCon or not oDiceElement:
        return None
    for iMaxPointRange, dChange in dData.items():
        oDiceElement.ChangeHeroRollPointWeight(oOwner.m_PlayerID, iMaxPointRange, dChange)
    
    if not oOwner.QuerySavedData('SpecialItemMaxAssembleNum', 0):
        oOwner.SetSavedData('SpecialItemMaxAssembleNum', 1)
        oDiceCon.AddExtraMaxAssembleNum(iAdd)


def SpecialItemSendLastTimePoint(oOwner, lstDice, dInfo, iDelta):
    oDiceCon = oOwner.m_DiceCon
    if not oDiceCon:
        return None
    iDice = lstDice[0] if lstDice else 0
    oDiceCon.SetLastTimeActive()
    oDiceCon.SetDelta(iDelta)
    (iLastTimePoint, _iRealPoint) = oDiceCon.GetLastTimeActivePoint()
    SendSpecialItemResult(oOwner, iDice, dInfo['Item'], {
        0: iLastTimePoint })

