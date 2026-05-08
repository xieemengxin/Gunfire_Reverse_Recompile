# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_dice/mobject.pyc
# RelativePath: clientlogic/cl_dice/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_item.baseitem import CBaseItem
from cl_cscommondef import DICE_MASK, REFRESH_DICE_CANROLLTIME, REFRESH_DICE_POINT, REFRESH_DICE_ATTACKTIMES
from cl_only import ShufferList, DeepCopy, ChooseMulKeys
from cl_object.logging import DiceLog
import cl_dice.net as dicenet
import cl_perform

class CDiceData(object):
    m_SID = 1001
    m_Name = '骰子'
    m_Type = DICE_MASK
    
    def Create(cls, oGame, oDiceCon, dDiceInfo, iPointID = 0, dTmp = None):
        oDice = CDice(oGame, 0, iPointID, dTmp)
        oDice.m_Type = cls.m_Type
        if oDiceCon:
            oDice.AddToContainer(oDiceCon)
        if dDiceInfo:
            oDice.Load(dDiceInfo)
        oDice.Init()
        return oDice

    Create = classmethod(Create)


class CDice(CBaseItem):
    m_Quality = 0
    m_PointRange = { }
    m_RollPoint = 0
    m_GetTime = 0
    m_AssemblePos = 0
    m_CanRollTimes = 1
    m_DiceAttackTimes = 0
    m_RedDot = False
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super().__init__(oGame, iTemp, iPointID, dTmp)
        self.m_Enable = 0
        self.m_GameID = oGame.m_ID
        self.m_PlayerID = 0

    
    def __str__(self):
        return '%s-%s-dice%s-%s-%s' % (self.m_GameID, self.m_PlayerID, self.m_SID, self.m_ID, self.m_Quality)

    
    def __repr__(self):
        return '%s-%s-dice%s-%s-%s' % (self.m_GameID, self.m_PlayerID, self.m_SID, self.m_ID, self.m_Quality)

    
    def Save(self):
        dData = super().Save()
        dData['SID'] = self.m_SID
        dData['QL'] = self.m_Quality
        dData['PR'] = self.m_PointRange
        dData['RP'] = self.m_RollPoint
        dData['AP'] = self.m_AssemblePos
        dData['CRT'] = self.m_CanRollTimes
        dData['DAT'] = self.m_DiceAttackTimes
        dData['RD'] = self.m_RedDot
        return dData

    
    def Load(self, dData):
        super().Load(dData)
        self.m_SID = dData['SID']
        self.m_Quality = dData.get('QL', 0)
        self.m_PointRange = dData.get('PR', { })
        self.m_RollPoint = dData.get('RP', 0)
        self.m_AssemblePos = dData.get('AP', 0)
        self.m_CanRollTimes = dData.get('CRT', 1)
        self.m_DiceAttackTimes = dData.get('DAT', 0)
        self.m_RedDot = dData.get('RD', False)
        self.InitName()

    
    def InitName(self):
        clsDiceAbility = cl_perform.GetPerformModule(self.m_SID)
        if not clsDiceAbility:
            DiceLog.Debug('%s dice init name err %s' % (self.m_GameID, self.m_SID))
            return None
        self.m_Name = clsDiceAbility.m_Name

    
    def Name(self):
        return self.m_Name

    
    def AddToContainer(self, oContainer):
        if not self.m_ID:
            return None
        super().AddToContainer(oContainer)
        oOwner = self.GetOwner()
        if oOwner:
            self.m_PlayerID = oOwner.m_PlayerID

    
    def SetDiceGetTime(self, iTime):
        if not (self.m_GetTime) and iTime:
            self.m_GetTime = iTime

    
    def ClearDiceGetTime(self):
        self.m_GetTime = 0

    
    def SetDiceAssemblePos(self, iPos):
        if iPos < 0:
            return None
        self.m_AssemblePos = iPos

    
    def GetDiceAssemblePos(self):
        return self.m_AssemblePos

    
    def RollPoint(self, oHero, iResultNum, dResultPoint, dExcludePoints = None, iUseBaseWeight = 0):
        oGame = self.m_Game
        if self.m_CanRollTimes <= 0:
            DiceLog.Debug('%s %s %s %s can not roll' % (oGame.m_ID, self.m_PlayerID, self.m_ID, self.m_SID))
            return []
        self.AddCanRollTimes(-1, 'RollPoint')
        lstPointWeight = self.GatPointRange()
        setResultPoint = set(dResultPoint)
        if dExcludePoints is None:
            dExcludePoints = { }
        iAnchoringPoint = oHero.m_DiceCon.GetAnchoringPoint()
        (iLastTimePoint, iRealPoint) = oHero.m_DiceCon.GetLastTimeActivePoint()
        if iRealPoint:
            oHero.m_DiceCon.SetLastTimeWaitClear()
        iGuaranteed = max(iAnchoringPoint, iLastTimePoint)
        iMaxPoint = self.GetMaxPoint()
        if iGuaranteed:
            iGuaranteed = min(iGuaranteed, iMaxPoint - 1)
            for iPoint in range(1, iGuaranteed + 1):
                dExcludePoints[iPoint] = 1
            
        if dExcludePoints:
            setExcludePoints = set(dExcludePoints)
            lstPointWeight = list(set(lstPointWeight) - setExcludePoints)
        if setResultPoint:
            lstPointRange = list(set(lstPointWeight) & setResultPoint)
        else:
            lstPointRange = lstPointWeight
        if self.m_RollPoint and self.m_RollPoint in lstPointRange:
            lstPointRange.remove(self.m_RollPoint)
        iSupplementNum = iResultNum - len(lstPointRange)
        if iSupplementNum > 0 and iGuaranteed:
            lstResult = lstPointRange
            lstResult.extend([
                iMaxPoint] * iSupplementNum)
        else:
            oDiceElement = oGame.m_WarMgr.GetDiceElement()
            if oDiceElement:
                if iUseBaseWeight:
                    dWeight = oDiceElement.GetBaseRollPointWeight(iMaxPoint)
                else:
                    dWeight = oDiceElement.GetHeroRollPointWeight(oHero.m_PlayerID, iMaxPoint)
                dChooseWeight = { dWeight[iPoint]: iPoint for iPoint in lstPointRange if iPoint in dWeight }
                lstResult = ChooseMulKeys(oGame, dChooseWeight, iResultNum)
            else:
                DiceLog.Debug('%s %s %s %s dice element not exist' % (oGame.m_ID, self.m_PlayerID, self.m_ID, self.m_SID))
                lstResult = []
        if not lstResult:
            DiceLog.Debug('%s %s %s %s not enough point to roll %s %s' % (oGame.m_ID, self.m_PlayerID, self.m_ID, self.m_SID, dResultPoint, dExcludePoints))
            if self.m_RollPoint:
                iResult = self.m_RollPoint + 1 if self.m_RollPoint < iMaxPoint else self.m_RollPoint - 1
                lstResult = [
                    iResult]
        DiceLog.Debug('%s %s %s %s %s roll point old:%s new:%s' % (oGame.m_ID, self.m_PlayerID, self.m_ID, self.m_SID, self.m_Quality, self.m_RollPoint, lstResult))
        return lstResult

    
    def GetPointRangeByWeight(self, lstPointRange, dResultPoint):
        for iPoint in list(lstPointRange):
            iWeight = dResultPoint.get(iPoint, 0)
            if iWeight > 1:
                lstPointRange.extend([
                    iPoint] * (dResultPoint[iPoint] - 1))
        
        return lstPointRange

    
    def GatPointRange(self):
        lstPointWeight = []
        for lstRange in self.m_PointRange.values():
            lstPointWeight.extend(lstRange)
        
        return lstPointWeight

    
    def GetMaxPoint(self):
        lstPointWeight = self.GatPointRange()
        if lstPointWeight:
            return max(lstPointWeight)
        return 0

    
    def AddCanRollTimes(self, iTimes, sReason):
        DiceLog.Debug('%s %s %s %s addrolltimes %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_ID, self.m_SID, self.m_CanRollTimes, iTimes, sReason))
        self.m_CanRollTimes += iTimes
        dicenet.GS2CRefreshDiceInfo(self.m_Game, [
            self], [
            self.m_PlayerID], iReason = REFRESH_DICE_CANROLLTIME)

    
    def ClearPoints(self, sReason):
        self.AddCanRollTimes(1, sReason)
        self.SetPoint(0, sReason)

    
    def SetPoint(self, iPoint, sReason):
        lstPointWeight = self.GatPointRange()
        if iPoint and iPoint not in lstPointWeight:
            return self.m_RollPoint
        DiceLog.Debug('%s %s %s %s set point old:%s new:%s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_ID, self.m_SID, self.m_RollPoint, iPoint, sReason))
        self.m_RollPoint = iPoint
        dicenet.GS2CRefreshDiceInfo(self.m_Game, [
            self], [
            self.m_PlayerID], iReason = REFRESH_DICE_POINT)
        return self.m_RollPoint

    
    def GetDiceAbilityQuality(self):
        iCurPoint = self.m_RollPoint
        for iQuality, lstRange in self.m_PointRange.items():
            if iCurPoint in lstRange:
                return iQuality
        
        return 0

    
    def GetCanRollTimes(self):
        return self.m_CanRollTimes

    
    def GetRollType(self):
        if self.m_RollPoint:
            return 1
        return 0

    
    def GetPointRange(self):
        return self.m_PointRange

    
    def GetStrPointRange(self):
        dStrPointRange = { }
        for iQuality, lstRange in self.m_PointRange.items():
            dStrPointRange[str(iQuality)] = lstRange
        
        return dStrPointRange

    
    def SetRedDot(self, bState):
        self.m_RedDot = bState

    
    def GetRedDot(self):
        return self.m_RedDot

    
    def GetDiceInfo(self):
        dDiceInfo = {
            'SID': self.m_SID,
            'QL': self.m_Quality,
            'PR': DeepCopy(self.m_PointRange) }
        return dDiceInfo

    
    def GetDiceAttackTimes(self):
        return self.m_DiceAttackTimes

    
    def SetDiceAttackTimes(self, iTimes):
        self.m_DiceAttackTimes = iTimes
        self.SyncDiceAttackTimes()

    
    def ClearDiceAttackTimes(self):
        self.m_DiceAttackTimes = 0
        self.SyncDiceAttackTimes()

    
    def SyncDiceAttackTimes(self):
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        dicenet.GS2CRefreshDiceInfo(self.m_Game, [
            self], lstPlayer, iReason = REFRESH_DICE_ATTACKTIMES)


