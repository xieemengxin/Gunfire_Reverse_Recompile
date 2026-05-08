# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/dicecon.pyc
# RelativePath: clientlogic/cl_container/dicecon.pyc
# Source Generated with Decompyle++
# File: dicecon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_DICE, DICE_SUBMSG_ADD, DICE_SUBMSG_REMOVE, TYPE_ASSEMBLE, CURRENCY_CASH, DICESPECIAL_ACTIVE_TAKEEFFECT, DICESPECIAL_PASSIVE_TAKEEFFECT, DICESPECIAL_PASSIVE_INIT_TAKEEFFECT, DICE_QUALITY_TALE, TYPE_DISASSEMBLE, RECYCLE_UNDROP, NWARRIOR_DROP_DICE, DICE_SUBMSG_ASSEMBLE, DICE_SUBMSG_DISASSEMBLE, DICE_SUBMSG_SWITCHASSEMBLE, REFRESH_DICE_COM, REFRESH_DICE_ASSEMBLYINFO, DICETAG_AI, AUTOFILL_EXCLUDEDICESPECIAL
from cl_commondefines import NPC_CB_VALUE, NWARRIOR_DROP_DICESELECTIONPACKET, DICEABILITY_LOCKDESC_QUALITY, S6_SIGN_ITEM_DICE, ADD_DICEENERGY, COST_DICEENERGY, ASSEMBLE_DICE_SUMADD, ASSEMBLE_DICE_SUMSUB, S6_ENERGY_CHANGE_REASON_DEFAULT, S6_ENERGY_CHANGE_REASON_ROLLPOINT
from cl_commondefines import DICESPECIAL_ACTIVE_IMITATORS, DICESPECIAL_PASSIVE_IMITATORS, DICESPECIAL_CARRYMAX_DEFAULT, DICESPECIAL_CARRYMAX_ACTIVE, DICESPECIAL_CARRYMAX_PASSIVE
from cl_object.logging import DiceLog
from cl_only import Frame2Time, Functor, ChooseKey, ShufferList, ChooseMulKeys
from cl_platformdata import GetDiceSpecialTypeList, GetAllDiceAbility, GetExcludeDiceQuality, GetDiceTagListInfo, GetDicePointMaxSameAssemblyNum, GetDiceSpecialItemTriggerEnergy, GetAIDice
from cl_npc import net as npcnet
from cl_container.mobject import CBaseSeasonContainer
import cl_dice
import cl_msgcenter
import cl_dice.net as dicenet
import cl_drop
import cl_snetwar
import cl_notify
MAX_ASSEMBLY_NUM = 6
FUSEDICE_NUM = 3
ASSEMBLY_DEFAULT_NUM = 3
SIGN_LEGAL_DATA_SOURCE = {
    S6_SIGN_ITEM_DICE: GetAllDiceAbility }
MAX_SAME_ASSEMBLY_NUM = 1
COMMON_NOTIFY_NUM = 2503
PACKETSHOWCNT_MAX = 200
MAX_DICE_ENERGY = 999
ADD_DICEENERGY_SPECIAL = [
    1004]
SPECIAL_ITEM_1022_ACTIVE = 1
SPECIAL_ITEM_1022_INACTIVE = 0
SPECIAL_ITEM_1022_WAIT_CLEAR = 2

class CDiceContainer(CBaseSeasonContainer):
    m_SeasonNum = 6
    m_BagType = BAG_TYPE_DICE
    m_Flag = 'DiceCon'
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_Perform = { }
        self.m_Dice = { }
        self.m_AssembleDice = { }
        self.m_MaxAssemblyNum = ASSEMBLY_DEFAULT_NUM
        self.m_ExtraAssembleNum = 0
        self.m_NextThrowItemCache = { }
        self.m_TempResult = { }
        self.m_CopyDiceAbility = { }
        self.m_UnLockAbilityDesc = { }
        self.m_SpecialItemInfo = { }
        self.m_DiceEnergy = 0
        self.m_SignInfo = {
            S6_SIGN_ITEM_DICE: [] }
        self.m_AssembleNum = { }
        self.m_DicePacketPointsShowCnt = 0
        self.m_AccumulatedRollPoint = 0
        self.m_AnchoringPoint = 0
        self.m_SpecItemTriggerEnergy = { }
        self.m_ActiveCurDiceEnergy = 0
        self.m_ChargeEnergyMul = 0
        self.m_AssembleDiceSumThreshold = {
            ASSEMBLE_DICE_SUMSUB: [],
            ASSEMBLE_DICE_SUMADD: [] }
        self.m_AssembleDiceSumPoint = 0
        self.m_TriggerEnergyMul = 100
        self.m_SpecItemUseEnergy = { }
        self.m_LastTimePointInfo = [
            SPECIAL_ITEM_1022_INACTIVE,
            0,
            0]

    
    def Release(self):
        self.m_Game = None
        oOwner = self.GetOwner()
        for oPerform in self.m_Perform.values():
            if oOwner:
                oPerform.Disable(oOwner)
            oPerform.Release()
        
        for oDice in self.m_Dice.values():
            oDice.Release()
        
        self.m_Dice = { }
        self.m_TempResult = { }

    
    def Save(self):
        dData = { }
        lstDice = []
        for oDice in self.m_Dice.values():
            dDice = oDice.Save()
            lstDice.append(dDice)
        
        dData['Dice'] = lstDice
        dData['MAN'] = self.m_MaxAssemblyNum
        dData['EMAN'] = self.m_ExtraAssembleNum
        dData['ULAD'] = self.m_UnLockAbilityDesc
        dData['SPIF'] = self.m_SpecialItemInfo
        dData['DE'] = self.m_DiceEnergy
        dData['DSNI'] = self.m_SignInfo
        dData['DPPS'] = self.m_DicePacketPointsShowCnt
        dData['ARP'] = self.m_AccumulatedRollPoint
        dData['STE'] = self.m_SpecItemTriggerEnergy
        dData['ADE'] = self.m_ActiveCurDiceEnergy
        dData['LTPF'] = self.m_LastTimePointInfo
        dData['SIE'] = self.m_SpecItemUseEnergy
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        if not self.m_Game.m_WarMgr.GetDiceElement():
            return None
        self.m_MaxAssemblyNum = dData['MAN']
        self.m_ExtraAssembleNum = dData.get('EMAN', 0)
        dicenet.GS2CRefreshMaxDiceAssemblyNum(self.m_PlayerID, self.GetMaxAssemblyNum(), self.m_ExtraAssembleNum)
        for dDice in dData['Dice']:
            oDice = self.CreateDice(dDice, 'Load')
            if not oDice:
                continue
            self.m_Dice[oDice.m_ID] = oDice
            dicenet.GS2CAddDice(self.m_PlayerID, oDice)
            iAssemblePos = oDice.GetDiceAssemblePos()
            if iAssemblePos:
                self.AssembleDice(oDice.m_ID, iAssemblePos, TYPE_ASSEMBLE, sReason = 'Load')
        
        self.m_UnLockAbilityDesc = dData.get('ULAD', { })
        self.m_SpecialItemInfo = dData.get('SPIF', { })
        self.m_DiceEnergy = dData.get('DE', 0)
        self.m_SignInfo = dData.get('DSNI', {
            S6_SIGN_ITEM_DICE: [] })
        self.m_DicePacketPointsShowCnt = dData.get('DPPS', 0)
        self.m_AccumulatedRollPoint = dData.get('ARP', 0)
        self.m_SpecItemTriggerEnergy = dData.get('STE', { })
        self.m_ActiveCurDiceEnergy = dData.get('ADE', 0)
        self.m_LastTimePointInfo = dData.get('LTPF', [
            SPECIAL_ITEM_1022_INACTIVE,
            0,
            0])
        self.m_SpecItemUseEnergy = dData.get('SIE', { })
        self.EffectSpecialItem()

    
    def ClearAll(self):
        lstDice = [ iDice for iDice in self.m_Dice ]
        for iDice in lstDice:
            self.RemoveDice(iDice, iDrop = 0, sReason = 'ClearAll')
        
        self.m_Dice = { }
        self.m_AssembleDice = { }
        self.m_MaxAssemblyNum = ASSEMBLY_DEFAULT_NUM
        self.m_NextThrowItemCache = { }
        self.m_UnLockAbilityDesc = { }
        self.SelfRefresh()

    
    def SelfRefresh(self):
        if not self.m_Game.m_WarMgr.GetDiceElement():
            return None
        self.SyncConDiceAttackTimes()
        dicenet.GS2CRefreshDiceInfo(self.m_Game, self.m_Dice.values(), [
            self.m_PlayerID], iReason = REFRESH_DICE_COM)
        dicenet.GS2CRefreshMaxDiceAssemblyNum(self.m_PlayerID, self.GetMaxAssemblyNum(), self.m_ExtraAssembleNum)
        dicenet.GS2CDiceSpecialItemInfo(self.m_PlayerID, self.m_NextThrowItemCache)
        dicenet.GS2CUpdateUnLockAbilityDesc(self.m_PlayerID, self.m_UnLockAbilityDesc)
        dicenet.GS2CDiceEnergy(self.m_PlayerID, self.m_DiceEnergy, S6_ENERGY_CHANGE_REASON_DEFAULT)
        oOwner = self.GetOwner()
        if oOwner:
            self.GS2CDiceSpecialItemGrooveInfo(oOwner)
        dicenet.GS2CS6PackSignInfo(self.m_PlayerID, self.m_SignInfo)
        self.GS2CSyncActiveDiceSpecialItem()

    
    def Refresh(self, dPlayer = None):
        if not self.m_Game.m_WarMgr.GetDiceElement():
            return None
        if not self.m_AssembleDice:
            return None
        for iDiceID in self.m_AssembleDice.values():
            if iDiceID not in self.m_Dice:
                continue
            oDice = self.m_Dice[iDiceID]
            dicenet.GS2CRefreshDiceInfo(self.m_Game, [
                oDice], dPlayer, iReason = REFRESH_DICE_ASSEMBLYINFO)
        
        self.SyncConDiceAttackTimes()

    
    def SyncConDiceAttackTimes(self):
        lstDice = self.m_Dice.values()
        for oDice in lstDice:
            if not oDice:
                continue
            oDice.SyncDiceAttackTimes()
        

    
    def UpdateSignInfo(self, dSignInfo):
        DiceLog.Debug('%s %s carry signinfo %s' % (self.m_Game.m_ID, self.m_PlayerID, dSignInfo))
        for iType, lstSign in dSignInfo.items():
            if iType not in SIGN_LEGAL_DATA_SOURCE:
                continue
            lstLegalSign = self.GetLegalSignInfo(iType, lstSign)
            self.m_SignInfo[iType] = lstLegalSign
        

    
    def RefreshAllSign(self):
        dicenet.GS2CS6PackSignInfo(self.m_PlayerID, self.m_SignInfo)

    
    def AddSign(self, iType, iSID, iRefresh = 1):
        if iType not in SIGN_LEGAL_DATA_SOURCE:
            return None
        dLegalInfo = SIGN_LEGAL_DATA_SOURCE[iType]()
        if iSID not in dLegalInfo:
            return None
        lstSign = self.m_SignInfo.setdefault(iType, [])
        if iSID in lstSign:
            return None
        lstSign.append(iSID)
        if iRefresh:
            self.RefreshAllSign()

    
    def DelSign(self, iType, iSID, iRefresh = 1):
        if iType not in self.m_SignInfo or iSID not in self.m_SignInfo[iType]:
            return None
        self.m_SignInfo[iType].remove(iSID)
        if iRefresh:
            self.RefreshAllSign()

    
    def GetLegalSignInfo(self, iType, lstSign = None):
        lstResult = []
        dLegalInfo = SIGN_LEGAL_DATA_SOURCE[iType]()
        for iSignSID in lstSign:
            if iSignSID not in dLegalInfo:
                continue
            lstResult.append(iSignSID)
        
        return lstResult

    
    def CheckAssembleSameDice(self, iSID, iPos):
        if iPos in self.m_AssembleDice:
            iOldDice = self.m_AssembleDice[iPos]
            oOldDice = self.m_Dice[iOldDice]
            if oOldDice.m_SID == iSID:
                return True
        return False

    
    def AddAssembleNum(self, iSID):
        iAssembleNum = self.m_AssembleNum.setdefault(iSID, 0)
        iDiceMaxNum = GetDicePointMaxSameAssemblyNum(iSID)
        if not iDiceMaxNum:
            iDiceMaxNum = MAX_SAME_ASSEMBLY_NUM
        if iAssembleNum >= iDiceMaxNum:
            cl_notify.SendCommonNotify(self.m_Game, [
                self.m_PlayerID], COMMON_NOTIFY_NUM, {
                '$num': str(iDiceMaxNum) })
            DiceLog.Debug('%s %s out of maxnum %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iAssembleNum, iDiceMaxNum, iSID))
            return False
        self.m_AssembleNum[iSID] += 1
        return True

    
    def SubAssembleNum(self, iSID):
        if iSID not in self.m_AssembleNum:
            return None
        self.m_AssembleNum[iSID] -= 1
        if self.m_AssembleNum[iSID] <= 0:
            self.m_AssembleNum.pop(iSID)

    
    def RewardDice(self, dDiceInfo, sReason, bAccumulatedRollPoint = False):
        oDice = self.CreateDice(dDiceInfo, sReason)
        if not oDice:
            return None
        if bAccumulatedRollPoint:
            self.AddAccumulatedRollPoint(oDice.m_RollPoint)
        self.AddDice(oDice, sReason = sReason)
        if 'RewardEnergy' in dDiceInfo:
            iDiceQuality = oDice.GetDiceAbilityQuality()
            self.AddEnergyWithSetDicePoint(iDiceQuality)
        return oDice

    
    def GetDiceData(self):
        lstDiceData = []
        dData = {
            'MaxAssemblyNum': self.GetMaxAssemblyNum(),
            'ExtraAssemblyNum': self.m_ExtraAssembleNum,
            'DiceData': lstDiceData,
            'SpecItem': list(self.m_SpecialItemInfo.values()) }
        for iDice in self.m_AssembleDice.values():
            if iDice not in self.m_Dice:
                continue
            oDice = self.m_Dice[iDice]
            dDiceData = {
                'SID': oDice.m_SID,
                'Quality': oDice.m_Quality,
                'RollPoint': oDice.m_RollPoint,
                'AssemblePos': oDice.m_AssemblePos,
                'PointRange': { lstValue: str(iKey) for iKey, lstValue in oDice.m_PointRange.items() } }
            lstDiceData.append(dDiceData)
        
        return dData

    
    def CreateDice(self, dDiceInfo, sReason):
        oGame = self.m_Game
        if not self.ValidAddDice():
            DiceLog.Debug('%s %s createdice invalid %s-%s' % (oGame.m_ID, self.m_PlayerID, dDiceInfo, sReason))
            return None
        oDice = cl_dice.CreateDice(oGame, self, dDiceInfo)
        if not oDice:
            DiceLog.Alert('%s %s createdice no dice %s-%s' % (oGame.m_ID, self.m_PlayerID, dDiceInfo, sReason))
            return None
        DiceLog.Debug('%s %s createdice %s-%s' % (oGame.m_ID, self.m_PlayerID, dDiceInfo, sReason))
        return oDice

    
    def AddDice(self, oDice, sReason):
        self.m_Dice[oDice.m_ID] = oDice
        oDice.SetRedDot(True)
        oGame = self.m_Game
        DiceLog.Debug('%s %s adddice %s-%s-%s' % (oGame.m_ID, self.m_PlayerID, oDice.m_ID, oDice.m_SID, sReason))
        iPoint = oDice.m_RollPoint
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICECHANGE, self.GetOwner(), {
            'Dice': oDice.m_ID,
            'DiceSID': oDice.m_SID,
            'Point': iPoint,
            'Reason': sReason }, oGame, iSub = DICE_SUBMSG_ADD)
        oDice.SetDiceGetTime(Frame2Time(oGame.GetFrameNum()))
        dicenet.GS2CAddDice(self.m_PlayerID, oDice)
        if iPoint:
            self.UnLockAbilityQuality(oDice.m_SID, oDice.GetDiceAbilityQuality())

    
    def RemoveDice(self, iDice, iDrop = 1, sReason = 'Remove'):
        if iDice not in self.m_Dice:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oGame = self.m_Game
        oDice = self.m_Dice[iDice]
        if not oDice:
            DiceLog.Debug('%s %s remove nonedice %s-%s' % (oGame.m_ID, self.m_PlayerID, iDice, sReason))
            return None
        if iDrop:
            iNewDice = self.AutoChooseDiceResult(oOwner, iDice, 'RemoveTemp')
            if iNewDice:
                self.RemoveDice(iNewDice, iDrop = 1, sReason = sReason)
                return None
        DiceLog.Debug('%s %s removedice %s-%s-%s' % (oGame.m_ID, self.m_PlayerID, iDice, oDice.m_SID, sReason))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICECHANGE, oOwner, {
            'Dice': oDice.m_ID,
            'DiceSID': oDice.m_SID,
            'Reason': sReason }, oGame, iSub = DICE_SUBMSG_REMOVE)
        iAssemblePos = oDice.GetDiceAssemblePos()
        if iAssemblePos:
            self.OnDisAssembleDice(oOwner, iAssemblePos, iDisAssembleDice = iDice, sReason = sReason)
        self.m_Dice.pop(iDice, None)
        dicenet.GS2CRemoveDice(self.m_PlayerID, iDice)
        if not iDrop:
            oDice.Release()
        else:
            oDice.ClearDiceGetTime()
            oDice.RemoveFromContainer(sReason)
            oDice.m_Source = oOwner.m_PlayerID
            cl_drop.DropItem(oOwner, oDice, bFly = True)

    
    def AddDiceToContainer(self, oDice, sReason):
        if not oDice:
            return None
        oGame = self.m_Game
        if not self.ValidAddDice():
            DiceLog.Debug('%s %s add dice to container invalid %s %s' % (oGame.m_ID, self.m_PlayerID, oDice.m_SID, sReason))
            return None
        oDice.AddToContainer(self)
        self.AddDice(oDice, sReason = sReason)

    
    def ValidAddDice(self):
        return 1

    
    def AddMaxAssemblyNum(self, iAdd):
        if not iAdd or self.m_MaxAssemblyNum == MAX_ASSEMBLY_NUM:
            return None
        oGame = self.m_Game
        iTempNum = self.m_MaxAssemblyNum + iAdd
        if iTempNum < 0:
            DiceLog.Debug('%s %s maxassemblynum < 0 %s %s' % (oGame.m_ID, self.m_PlayerID, self.m_MaxAssemblyNum, iAdd))
            self.m_MaxAssemblyNum = 0
        elif iTempNum > MAX_ASSEMBLY_NUM:
            DiceLog.Debug('%s %s maxassemblynum > %s %s %s' % (oGame.m_ID, self.m_PlayerID, MAX_ASSEMBLY_NUM, iTempNum, iAdd))
            self.m_MaxAssemblyNum = MAX_ASSEMBLY_NUM
        else:
            self.m_MaxAssemblyNum = iTempNum
        DiceLog.Debug('%s %s maxassemblynum %s' % (oGame.m_ID, self.m_PlayerID, self.m_MaxAssemblyNum))
        dicenet.GS2CRefreshMaxDiceAssemblyNum(self.m_PlayerID, self.GetMaxAssemblyNum(), self.m_ExtraAssembleNum)

    
    def AddExtraMaxAssembleNum(self, iAdd):
        if not iAdd:
            return None
        iTempNum = self.m_ExtraAssembleNum + iAdd
        if iTempNum < 0:
            DiceLog.Debug('%s %s extraassemblynum < 0 %s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_ExtraAssembleNum, iAdd))
            self.m_ExtraAssembleNum = 0
        self.m_ExtraAssembleNum = iTempNum
        dicenet.GS2CRefreshMaxDiceAssemblyNum(self.m_PlayerID, self.GetMaxAssemblyNum(), self.m_ExtraAssembleNum)

    
    def GetMaxAssemblyNum(self):
        return self.m_MaxAssemblyNum + self.m_ExtraAssembleNum

    
    def GetAssembleDice(self):
        return self.m_AssembleDice

    
    def GetNextCanAssemblePos(self):
        for iPos in range(1, self.GetMaxAssemblyNum() + 1):
            if not iPos not in self.m_AssembleDice:
                if not self.m_AssembleDice[iPos]:
                    return iPos
        
        return 0

    
    def AssembleDice(self, iDice, iPos, iOption, sReason = ''):
        iMaxAssemblyNum = self.GetMaxAssemblyNum()
        if not iPos or iPos > iMaxAssemblyNum:
            DiceLog.Debug('%s %s assemble invalid pos %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iPos, iMaxAssemblyNum))
            return None
        if iDice not in self.m_Dice:
            return None
        if not self.CheckDiceRoll(iDice):
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oDice = self.m_Dice[iDice]
        if iOption == TYPE_ASSEMBLE:
            bResult = self.OnAssembleDice(oOwner, oDice, iPos, sReason = sReason)
        elif iOption == TYPE_DISASSEMBLE:
            bResult = self.OnDisAssembleDice(oOwner, iPos, iDisAssembleDice = iDice, sReason = sReason)
        else:
            bResult = self.OnSwitchAssembleDice(oOwner, oDice, iPos, sReason = sReason)
        if bResult:
            dPlayer = self.GetSendPlayer()
            dicenet.GS2CRefreshDiceInfo(self.m_Game, [
                oDice], dPlayer, iReason = REFRESH_DICE_ASSEMBLYINFO)

    
    def GetSendPlayer(self):
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        return dict.fromkeys(lstPlayer, 1)

    
    def OnAssembleDice(self, oOwner, oDice, iPos, sReason = ''):
        iDiceAbilitySID = oDice.m_SID
        bAssembleSame = self.CheckAssembleSameDice(iDiceAbilitySID, iPos)
        if not bAssembleSame and not self.AddAssembleNum(iDiceAbilitySID):
            return False
        oGame = self.m_Game
        iAbilityQuality = oDice.GetDiceAbilityQuality()
        if not iAbilityQuality:
            DiceLog.Debug('%s %s assemble dice %s %s %s fail %s' % (oGame.m_ID, self.m_PlayerID, iPos, iDiceAbilitySID, iAbilityQuality, sReason))
            return False
        if iPos in self.m_AssembleDice:
            if bAssembleSame:
                sDisAssembleReason = 'ReplaceSame'
            else:
                sDisAssembleReason = 'Replace'
            bDisAssemble = self.OnDisAssembleDice(oOwner, iPos, sReason = sDisAssembleReason)
            if not bDisAssemble:
                return False
        iDice = oDice.m_ID
        oDice.SetDiceAssemblePos(iPos = iPos)
        self.m_AssembleDice[iPos] = iDice
        DiceLog.Debug('%s %s assemble dice %s %s %s %s %s' % (oGame.m_ID, self.m_PlayerID, iPos, iDice, iDiceAbilitySID, iAbilityQuality, sReason))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICECHANGE, oOwner, {
            'Dice': iDice,
            'AbilitySID': iDiceAbilitySID,
            'AbilityQuality': iAbilityQuality }, oGame, iSub = DICE_SUBMSG_ASSEMBLE)
        self.ChangeAssembleDiceSumPoint(oOwner, oDice.m_RollPoint, iDirect = ASSEMBLE_DICE_SUMADD)
        self.AddPerform(oOwner, iDiceAbilitySID, iAbilityQuality, iItem = iDice, iEnable = 1, sReason = sReason)
        return True

    
    def OnDisAssembleDice(self, oOwner, iPos, iDisAssembleDice = 0, sReason = ''):
        oGame = self.m_Game
        if iPos not in self.m_AssembleDice:
            DiceLog.Debug('%s %s disassemble pos %s fail %s %s' % (oGame.m_ID, self.m_PlayerID, iPos, self.m_AssembleDice, sReason))
            return False
        iDice = self.m_AssembleDice[iPos]
        if iDice not in self.m_Dice:
            DiceLog.Debug('%s %s disassemble no dice %s %s %s' % (oGame.m_ID, self.m_PlayerID, iPos, iDice, sReason))
            return False
        if iDisAssembleDice and iDisAssembleDice != iDice:
            DiceLog.Debug('%s %s disassemble err dice %s %s %s %s' % (oGame.m_ID, self.m_PlayerID, iPos, iDisAssembleDice, iDice, sReason))
            return False
        self.m_AssembleDice.pop(iPos)
        oDice = self.m_Dice[iDice]
        iDiceAbilitySID = oDice.m_SID
        DiceLog.Debug('%s %s disassemble dice %s %s %s %s' % (oGame.m_ID, self.m_PlayerID, iPos, iDice, iDiceAbilitySID, sReason))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICECHANGE, oOwner, {
            'Dice': iDice,
            'AbilitySID': iDiceAbilitySID,
            'AbilityQuality': oDice.GetDiceAbilityQuality() }, oGame, iSub = DICE_SUBMSG_DISASSEMBLE)
        oDice.SetDiceAssemblePos(iPos = 0)
        self.ChangeAssembleDiceSumPoint(oOwner, oDice.m_RollPoint, iDirect = ASSEMBLE_DICE_SUMSUB)
        self.RemovePerform(oOwner, iDice, iDiceAbilitySID)
        if sReason != 'ReplaceSame':
            self.SubAssembleNum(iDiceAbilitySID)
        return True

    
    def OnSwitchAssembleDice(self, oOwner, oDice, iPos, sReason = ''):
        oGame = self.m_Game
        iAssemblePos = oDice.GetDiceAssemblePos()
        if iPos not in self.m_AssembleDice:
            DiceLog.Debug('%s %s %s change pos old:%s new:%s %s' % (oGame.m_ID, self.m_PlayerID, oDice.m_ID, iAssemblePos, iPos, sReason))
            self.ChangeDicePos(oDice, iAssemblePos, iPos)
            return True
        iTargetDice = self.m_AssembleDice[iPos]
        if iTargetDice not in self.m_Dice:
            DiceLog.Debug('%s %s switchassemble no dice %s %s %s %s' % (oGame.m_ID, self.m_PlayerID, iPos, oDice.m_ID, iTargetDice, sReason))
            return False
        oTargetDice = self.m_Dice[iTargetDice]
        DiceLog.Debug('%s %s %s switch pos old:%s new:%s %s' % (oGame.m_ID, self.m_PlayerID, oDice.m_ID, iAssemblePos, iPos, sReason))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DICECHANGE, oOwner, { }, oGame, iSub = DICE_SUBMSG_SWITCHASSEMBLE)
        self.ChangeDicePos(oTargetDice, 0, iAssemblePos)
        dicenet.GS2CRefreshDiceInfo(oGame, [
            oTargetDice], self.GetSendPlayer(), iReason = REFRESH_DICE_ASSEMBLYINFO)
        self.ChangeDicePos(oDice, 0, iPos)
        return True

    
    def RemoveAIDice(self):
        for iDice, oDice in dict(self.m_Dice).items():
            if DICETAG_AI in GetDiceTagListInfo(oDice.m_SID):
                self.RemoveDice(iDice, iDrop = 0, sReason = 'RemoveAIDice')
        

    
    def CheckAndReplaceAssembleDice(self, oDice):
        if oDice.m_ID not in self.m_Dice:
            return None
        dReplaceInfo = { }
        if oDice.GetRollType() and oDice.m_SID in self.m_AssembleNum:
            for iPos, iDice in self.m_AssembleDice.items():
                if iDice not in self.m_Dice:
                    continue
                oAssembleDice = self.m_Dice[iDice]
                if oAssembleDice.m_SID == oDice.m_SID and oAssembleDice.m_RollPoint < oDice.m_RollPoint:
                    dReplaceInfo[oAssembleDice.m_RollPoint] = iPos
            
            if dReplaceInfo:
                iPos = dReplaceInfo[min(dReplaceInfo)]
                self.AssembleDice(oDice.m_ID, iPos, TYPE_ASSEMBLE, sReason = 'CheckAndReplaceAssembleDice')

    
    def ChangeDicePos(self, oDice, iOldPos, iNewPos):
        oDice.SetDiceAssemblePos(iPos = iNewPos)
        if iOldPos:
            self.m_AssembleDice.pop(iOldPos)
        if iNewPos:
            self.m_AssembleDice[iNewPos] = oDice.m_ID

    
    def ChangeAssembleDiceSumPoint(self, oOwner, iPoint, iDirect):
        iOld = self.m_AssembleDiceSumPoint
        DiceLog.Debug('%s %s assemble sumpoint %s %s %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, iPoint, iOld, iDirect))
        if iPoint <= 0:
            return None
        if iDirect == ASSEMBLE_DICE_SUMADD:
            self.m_AssembleDiceSumPoint += iPoint
        else:
            self.m_AssembleDiceSumPoint -= iPoint
        if self.m_AssembleDiceSumPoint < 0:
            DiceLog.Alert('%s %s assemble sumpoint err %s %s %s %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, iPoint, iOld, self.m_AssembleDiceSumPoint, iDirect))
            self.m_AssembleDiceSumPoint = 0
        self.RefreshAssembleDiceSumThreshold(iOld, self.m_AssembleDiceSumPoint, iDirect)

    
    def RefreshAssembleDiceSumThreshold(self, iOldVal, iNowVal, iDirect):
        oOwner = self.GetOwner()
        for iThreshold, _, func in self.m_AssembleDiceSumThreshold[iDirect]:
            if iDirect == ASSEMBLE_DICE_SUMADD:
                if iOldVal >= iThreshold or iNowVal < iThreshold:
                    continue
                continue
            if iDirect == ASSEMBLE_DICE_SUMSUB:
                if iNowVal >= iThreshold or iOldVal < iThreshold:
                    continue
                continue
            func(oOwner, {
                'Threshold': iThreshold,
                'Direct': iDirect,
                'OldVal': iOldVal,
                'NowVal': iNowVal })
        

    
    def AddAssembleDiceSumThreshold(self, iThreshold, iDirect, sKey, func, iUnique):
        if iDirect not in self.m_AssembleDiceSumThreshold:
            return None
        if iUnique:
            lstAssembleDiceSumThreshold = []
            for iCheckThreshold, sCheckKey, fCheckFunc in self.m_AssembleDiceSumThreshold[iDirect]:
                if sCheckKey == sKey:
                    continue
                lstAssembleDiceSumThreshold.append((iCheckThreshold, sCheckKey, fCheckFunc))
            
            self.m_AssembleDiceSumThreshold[iDirect] = lstAssembleDiceSumThreshold
        self.m_AssembleDiceSumThreshold[iDirect].append((iThreshold, sKey, func))

    
    def ClearAssembleDiceSumThreshold(self, iClearThreshold, iDirect, sClearKey):
        if iDirect not in self.m_AssembleDiceSumThreshold:
            return None
        lstAssembleDiceSumThreshold = []
        for iThreshold, sKey, func in self.m_AssembleDiceSumThreshold[iDirect]:
            if iClearThreshold == iThreshold and sClearKey == sKey:
                continue
            lstAssembleDiceSumThreshold.append((iThreshold, sKey, func))
        
        self.m_AssembleDiceSumThreshold[iDirect] = lstAssembleDiceSumThreshold

    
    def RollDice(self, iDice, sReason, cbfunc = None, iDirectSpItem = 0, dExcludePoints = None, dExtraInfo = None):
        oOwner = self.GetOwner()
        if not oOwner:
            return { }
        if iDice not in self.m_Dice:
            return { }
        oDice = self.m_Dice[iDice]
        if not oDice:
            return { }
        lstSpItem = []
        dInfo = {
            'ResultPoint': { },
            'ExcludePoints': { } }
        if iDice != oOwner.Query('CurUseItemDice', 0):
            oOwner.Set('CurUseItemDice', iDice)
            for iSpecialItem in list(self.m_NextThrowItemCache):
                lstSpItem.append(iSpecialItem)
                self.UseSpecialItem(oOwner, iSpecialItem, [
                    iDice], dInfo)
            
            oOwner.Set('CurUseItemDice', 0)
        iResultNum = 1 + dInfo['ExtraResultNum'] if dInfo and 'ExtraResultNum' in dInfo else 1
        dResultPoint = dInfo['ResultPoint']
        dAllExcludePoints = { }
        dAllExcludePoints.update(dInfo['ExcludePoints'])
        if dExcludePoints:
            dAllExcludePoints.update(dExcludePoints)
        lstResult = oDice.RollPoint(oOwner, iResultNum, dResultPoint, dAllExcludePoints)
        if not lstResult:
            return { }
        dResult = { }
        for iPos, iResult in enumerate(lstResult):
            dResult[iPos] = iResult
        
        if iDirectSpItem:
            lstSpItem.append(iDirectSpItem)
        if 'BeforeSetPointFunc' in dInfo:
            func = dInfo['BeforeSetPointFunc']
            func(dResult)
        if len(lstResult) > 1:
            if dExtraInfo and dExtraInfo.get('LongPressSkipChoose', 0):
                return dResult
            dicenet.GS2CDiceSpecialItemResult(oOwner, iDice, [], dResult)
            cbFuncSetPoint = Functor(self.SetDicePoint, iDice)
            cbFuncRemoveDice = Functor(self.ApplyTempPoint, iDice)
            self.m_TempResult[iDice] = (dResult, cbFuncSetPoint, cbFuncRemoveDice, lstSpItem)
            cbAutoChooseDicePoint = Functor(self.AutoChoosePoint, iDice, sReason)
            sKey = 'ChooseDiceResult-%s' % iDice
            oOwner.AddMapLoadOKCbFun(sKey, cbAutoChooseDicePoint)
        else:
            self.SetDicePoint(iDice, dResult[0], sReason, cbfunc, lstSpItem, bAddDiceEnergy = True, bLastTimeFlag = True)
        return dResult

    
    def SetDicePoint(self, iDice, iPoint, sReason, cbfunc = None, lstSpItem = None, bAddDiceEnergy = False, bLastTimeFlag = False):
        if iDice not in self.m_Dice:
            return None
        oDice = self.m_Dice[iDice]
        if not oDice:
            return None
        sReason = 'SetDicePoint'
        iAssemblePos = oDice.GetDiceAssemblePos()
        if iAssemblePos in self.m_AssembleDice:
            bAssemble = True
            self.AssembleDice(iDice, iAssemblePos, TYPE_DISASSEMBLE, sReason = sReason)
        else:
            bAssemble = False
        if iDice in self.m_TempResult:
            self.m_TempResult.pop(iDice)
        iPoint = oDice.SetPoint(iPoint, sReason)
        if bLastTimeFlag:
            self.SetLastTimePoint(iPoint)
        if cbfunc:
            cbfunc(iPoint)
        if iDice not in self.m_Dice:
            return None
        if lstSpItem is None:
            lstSpItem = []
        self.AddAccumulatedRollPoint(iPoint)
        iDiceQuality = oDice.GetDiceAbilityQuality()
        if bAddDiceEnergy:
            self.AddEnergyWithSetDicePoint(iDiceQuality)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, self.GetOwner(), {
            'Dice': iDice,
            'Point': iPoint,
            'RS': sReason,
            'UsedSpi': lstSpItem,
            'QL': oDice.m_Quality,
            'DiceSID': oDice.m_SID })
        self.UnLockAbilityQuality(oDice.m_SID, iDiceQuality)
        if bAssemble:
            self.AssembleDice(iDice, iAssemblePos, TYPE_ASSEMBLE, sReason = sReason)

    
    def AddEnergyWithSetDicePoint(self, iDiceQuality):
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if oDiceElement:
            iDiceEnergy = oDiceElement.GetAddEnergyByDiceQuality(iDiceQuality)
            self.ChangeDiceEnergy(iDiceEnergy, 'SetDicePoint', S6_ENERGY_CHANGE_REASON_ROLLPOINT)

    
    def AddAccumulatedRollPoint(self, iPoint):
        self.m_AccumulatedRollPoint += iPoint

    
    def GetAccumulatedRollPoint(self):
        return self.m_AccumulatedRollPoint

    
    def SetAnchoringPoint(self, iPoint):
        self.m_AnchoringPoint = iPoint

    
    def GetAnchoringPoint(self):
        return self.m_AnchoringPoint

    
    def GetRollPointMin(self):
        (iActivePoint, _) = self.GetLastTimeActivePoint()
        if not (self.m_AnchoringPoint) and not iActivePoint:
            return 0
        return max(self.m_AnchoringPoint, iActivePoint) + 1

    
    def UnLockAbilityQuality(self, iDiceAbilitySID, iMaxQuality):
        dAllDice = GetAllDiceAbility()
        if iDiceAbilitySID not in dAllDice or iMaxQuality not in DICEABILITY_LOCKDESC_QUALITY:
            return None
        dUnLockQuality = self.m_UnLockAbilityDesc.setdefault(iDiceAbilitySID, { })
        if iMaxQuality in dUnLockQuality:
            return None
        for iQuality in DICEABILITY_LOCKDESC_QUALITY:
            if iQuality <= iMaxQuality:
                dUnLockQuality[iQuality] = 1
        
        DiceLog.Debug('%s %s unlockdicedesc %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iDiceAbilitySID, dUnLockQuality))
        dicenet.GS2CUpdateUnLockAbilityDesc(self.m_PlayerID, {
            iDiceAbilitySID: dUnLockQuality })

    
    def ChooseDiceResult(self, oHero, iDice, iPos, iSpecialItem):
        sKey = 'ChooseDiceResult-%s' % iDice
        oHero.RemoveMapLoadOKCbFun(sKey)
        if iDice not in self.m_TempResult:
            return None
        (dResult, cbfunc, _, lstSpItem) = self.m_TempResult.pop(iDice)
        if iPos not in dResult:
            return None
        if not lstSpItem:
            return None
        iSpecialItemSID = lstSpItem[0]
        if iSpecialItemSID not in self.m_SpecialItemInfo.values():
            return None
        if cbfunc:
            bAddDiceEnergy = True if iSpecialItem in ADD_DICEENERGY_SPECIAL else False
            cbfunc(dResult[iPos], 'ChooseResult-%s' % iSpecialItemSID, None, lstSpItem, bAddDiceEnergy)

    
    def AutoChooseDiceResult(self, oHero, iDice, sReason):
        sKey = 'ChooseDiceResult-%s' % iDice
        oHero.RemoveMapLoadOKCbFun(sKey)
        if iDice not in self.m_TempResult:
            return 0
        cbfuncRemoveDice = self.m_TempResult[iDice][2]
        if cbfuncRemoveDice:
            return cbfuncRemoveDice(sReason)
        return 0

    
    def AutoChoosePoint(self, iDice, sReason, oHero, _dMsgInfo):
        self.ApplyTempPoint(iDice, 'Auto-' + sReason)
        return 1

    
    def ApplyTempPoint(self, iDice, sReason):
        if iDice not in self.m_TempResult:
            return 0
        (dResult, cbfunc, _, lstSpItem) = self.m_TempResult.pop(iDice)
        iTempPoint = max(dResult.values())
        self.SetDicePoint(iDice, iTempPoint, sReason, cbfunc, lstSpItem, bAddDiceEnergy = True)
        return iDice

    
    def AutoChooseAbility(self, iDice, sReason, oHero, _dMsgInfo):
        self.ApplyTempAbility(iDice, 'Auto-' + sReason)
        return 1

    
    def ApplyTempAbility(self, iDice, sReason):
        if iDice not in self.m_TempResult:
            return 0
        (dResult, _, _, _) = self.m_TempResult.pop(iDice)
        dChooseDice = { 1: iDiceSID for iDiceSID in dResult.values() }
        iTransferDiceSID = ChooseKey(self.m_Game, dChooseDice)
        return self.TransferDice(iDice, iTransferDiceSID, sReason, None, None)

    
    def AddPerform(self, oOwner, iPerformSID, iLevel, iItem, iEnable, sReason = ''):
        if iEnable and sReason != 'gm' and self.m_Game.m_WarMgr.IsAIHero(oOwner.m_ID) and iPerformSID not in GetAIDice():
            iEnable = 0
        tKey = (iItem, iPerformSID)
        if tKey in self.m_Perform:
            oPerform = self.m_Perform[tKey]
            if oPerform.m_Owner == oOwner.m_ID:
                oPerform.SetLevel(oOwner, iLevel)
                if iEnable and not (oPerform.m_Enable):
                    oPerform.Enable(oOwner)
                return oPerform
        oPerform = oOwner.m_Game.m_ResMgr.NewPerform(iPerformSID, oOwner, iLevel)
        if not oPerform:
            return None
        self.m_Perform[tKey] = oPerform
        oPerform.m_Item = iItem
        if iEnable:
            oPerform.Enable(oOwner)
        return oPerform

    
    def RemovePerform(self, oOwner, iItem, iPerformSID):
        tKey = (iItem, iPerformSID)
        if tKey not in self.m_Perform:
            return None
        oPerform = self.m_Perform[tKey]
        oPerform.Disable(oOwner)
        oPerform.Release()
        return self.m_Perform.pop(tKey)

    
    def AllPerformEnable(self, iNotify = 0):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        for oPerform in list(self.m_Perform.values()):
            if oPerform.m_Enable:
                continue
            oPerform.Enable(oOwner, iNotify)
        

    
    def AllPerformDisable(self, iNotify = 0):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        for oPerform in list(self.m_Perform.values()):
            oPerform.Disable(oOwner, iNotify)
        

    
    def GetPerform(self, iPerform, iItem):
        tKey = (iItem, iPerform)
        if tKey not in self.m_Perform:
            return None
        return self.m_Perform[tKey]

    
    def ClearDiceRedDot(self, iDice):
        if iDice:
            if iDice in self.m_Dice:
                oDice = self.m_Dice[iDice]
                oDice.SetRedDot(False)
            return None
        for oDice in self.m_Dice.values():
            oDice.SetRedDot(False)
        

    
    def GetDiceByID(self, iDice):
        if iDice not in self.m_Dice:
            return None
        return self.m_Dice[iDice]

    
    def GetDiceBySID(self, iDiceSID, bAssemble = False):
        if not self.m_Dice:
            return 0
        for iDiceID, oDice in self.m_Dice.items():
            if oDice.m_SID != iDiceSID:
                continue
            if bAssemble and oDice.GetDiceAssemblePos():
                return iDiceID
            if not bAssemble and not oDice.GetDiceAssemblePos():
                return iDiceID
        
        return 0

    
    def RecycleDice(self, iDice):
        oHero = self.GetOwner()
        if iDice not in self.m_Dice:
            return None
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return None
        if oHero.IsDead():
            return None
        oDice = self.m_Dice[iDice]
        sReason = 'RecycleDice'
        dInfo = {
            'Dice': iDice,
            'QL': oDice.m_Quality,
            'RecycleDropType': NWARRIOR_DROP_DICE,
            'CurPoint': oDice.m_RollPoint,
            'Reward': self.GetDiceRecyclePrice(oDice),
            'DiceSID': oDice.m_SID }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEDROP, oHero, dInfo, iSub = RECYCLE_UNDROP)
        self.RemoveDice(iDice, iDrop = 0, sReason = sReason)
        iReward = dInfo['Reward']
        if iReward <= 0:
            return None
        oHero.AddCash(iReward, 'RecycleDice')
        cl_snetwar.GS2CRecycleDropResult(self.m_Game, 0, oHero.m_ID, 1, CURRENCY_CASH, iReward, {
            self.m_PlayerID: 1 })

    
    def GetDiceRecyclePrice(self, oDice):
        if not oDice:
            return 0
        return oDice.m_RollPoint * 10

    
    def RandomCopyAssembleEffect(self, dExclude, iCopyNum, iLast):
        if not (self.m_AssembleDice) or iCopyNum <= 0:
            return { }
        dAssemblePos = { }
        for iPos, iDice in self.m_AssembleDice.items():
            oDice = self.GetDiceByID(iDice)
            iDiceAbility = oDice.m_SID
            if iDiceAbility in dExclude:
                continue
            oDiceAbility = self.GetPerform(iDiceAbility, iDice)
            if not oDiceAbility:
                continue
            dAssemblePos[iPos] = (iDiceAbility, oDiceAbility.m_Level)
        
        if not dAssemblePos:
            return { }
        lstAssemblePos = list(dAssemblePos)
        lstCopyPos = []
        if iLast:
            iMaxPos = max(dAssemblePos.keys())
            lstAssemblePos.remove(iMaxPos)
            lstCopyPos = [
                iMaxPos]
        lstCopyPos.extend(ShufferList(self.m_Game, lstAssemblePos, iCopyNum))
        dCopyResult = { }
        for idx, iPos in enumerate(lstCopyPos):
            dCopyResult[idx] = dAssemblePos[iPos]
        
        return dCopyResult

    
    def EnableCopyDiceAbility(self, oEnableAbility, dExclude, iCopyNum, iLast = 0):
        dEnableAbility = self.RandomCopyAssembleEffect(dExclude, iCopyNum, iLast)
        if not dEnableAbility:
            return None
        iEnableDice = oEnableAbility.m_Item
        for iDiceAbilitySID, iLevel in dEnableAbility.values():
            self.AddCopyPerform(iEnableDice, iDiceAbilitySID, iLevel)
        

    
    def DisableCopyDiceAbility(self, iDisableDice, lstDisableCopyAbility = None):
        if iDisableDice not in self.m_CopyDiceAbility:
            return None
        if not lstDisableCopyAbility:
            lstDisableCopyAbility = self.m_CopyDiceAbility[iDisableDice]
        for iPerformSID in list(lstDisableCopyAbility):
            self.RemoveCopyPerform(iDisableDice, iPerformSID)
        

    
    def AddCopyPerform(self, iEnableDice, iPerformSID, iLevel):
        oOwner = self.GetOwner()
        if oOwner:
            DiceLog.Debug('%s %s %s copyadd %s-%s' % (oOwner.m_Game.m_ID, oOwner.m_PlayerID, iEnableDice, iPerformSID, iLevel))
            oPerform = self.AddPerform(oOwner, iPerformSID, iLevel, iItem = iEnableDice, iEnable = 1, sReason = 'copyadd')
            if oPerform:
                if iEnableDice not in self.m_CopyDiceAbility:
                    self.m_CopyDiceAbility[iEnableDice] = [
                        iPerformSID]
                else:
                    self.m_CopyDiceAbility[iEnableDice].append(iPerformSID)
                return oPerform

    
    def RemoveCopyPerform(self, iDisableDice, iPerformSID):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oPerform = self.GetPerform(iPerformSID, iDisableDice)
        if not oPerform:
            return None
        DiceLog.Debug('%s %s %s copyremove %s-%s' % (oOwner.m_Game.m_ID, oOwner.m_PlayerID, iDisableDice, iPerformSID, oPerform.m_Level))
        self.m_CopyDiceAbility[iDisableDice].remove(iPerformSID)
        if not self.m_CopyDiceAbility[iDisableDice]:
            self.m_CopyDiceAbility.pop(iDisableDice)
        self.RemovePerform(oOwner, iDisableDice, iPerformSID)

    
    def DisableLinkCopyAbility(self, iCheckAbilitySID, iCheckAbilityLevel):
        for iDice, lstCopyAbility in dict(self.m_CopyDiceAbility).items():
            lstDisableLinkCopyAbility = []
            for iPerform in lstCopyAbility:
                oPerform = self.GetPerform(iPerform, iDice)
                if not oPerform:
                    continue
                if iPerform == iCheckAbilitySID and oPerform.m_Level == iCheckAbilityLevel:
                    lstDisableLinkCopyAbility.append(iPerform)
                    break
            
            if lstDisableLinkCopyAbility:
                self.DisableCopyDiceAbility(iDice, lstDisableLinkCopyAbility)
        

    
    def ChangeDiceEnergy(self, iNum, sReason, iSyncChangeReason = S6_ENERGY_CHANGE_REASON_DEFAULT):
        if not iNum:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        DiceLog.Debug('%s %s change dice energy %s %s %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, iNum, self.m_DiceEnergy, sReason))
        iOld = self.m_DiceEnergy
        self.m_DiceEnergy += iNum
        if self.m_DiceEnergy < 0:
            DiceLog.Alert('%s %s change dice energy err %s %s %s' % (oOwner.m_Game.m_ID, oOwner.m_PlayerID, iNum, self.m_DiceEnergy, sReason))
            self.m_DiceEnergy = 0
        if self.m_DiceEnergy > MAX_DICE_ENERGY:
            self.m_DiceEnergy = MAX_DICE_ENERGY
        if iOld == self.m_DiceEnergy:
            return None
        if iOld > self.m_DiceEnergy:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_DICEENERGY, oOwner, {
                'Cost': iOld - self.m_DiceEnergy }, iSub = COST_DICEENERGY)
        else:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_DICEENERGY, oOwner, {
                'AddEnergy': iNum,
                'Reason': sReason }, iSub = ADD_DICEENERGY)
            if self.m_SpecItemTriggerEnergy:
                iChange = (self.m_DiceEnergy - iOld) * 100
                iTotalChange = iChange * (100 + self.m_ChargeEnergyMul) // 100
                self.m_ActiveCurDiceEnergy += iTotalChange
                self.GS2CSyncActiveDiceSpecialItem()
        dicenet.GS2CDiceEnergy(oOwner.m_PlayerID, self.m_DiceEnergy, iSyncChangeReason)

    
    def GetDiceEnergy(self):
        return self.m_DiceEnergy

    
    def AddChargeEnergyMul(self, iMul):
        self.m_ChargeEnergyMul += iMul

    
    def AddCarrySpecItem(self, lstCarryInSpecItem, iIsAI = 0):
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        dUnlockSpecItem = oDiceElement.GetAllUnLockSpecItem(oOwner.m_PlayerID)
        if DICESPECIAL_ACTIVE_IMITATORS in lstCarryInSpecItem:
            (iActiveMax, iPassiveMax) = DICESPECIAL_CARRYMAX_ACTIVE
        elif DICESPECIAL_PASSIVE_IMITATORS in lstCarryInSpecItem:
            (iActiveMax, iPassiveMax) = DICESPECIAL_CARRYMAX_PASSIVE
        else:
            (iActiveMax, iPassiveMax) = DICESPECIAL_CARRYMAX_DEFAULT
        lstActive = GetDiceSpecialTypeList(DICESPECIAL_ACTIVE_TAKEEFFECT)
        lstPassive = GetDiceSpecialTypeList(DICESPECIAL_PASSIVE_TAKEEFFECT)
        dFilterSpecItemInfo = { }
        lstSpecialItemInfo = []
        for iSpecItem in lstCarryInSpecItem:
            if not iSpecItem:
                continue
            if iSpecItem not in dUnlockSpecItem:
                DiceLog.Alert('%s %s carryin specitem unlock %d %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, iSpecItem, dUnlockSpecItem))
                continue
            if iSpecItem in lstActive:
                if not iActiveMax:
                    continue
                iActiveMax -= 1
            elif iSpecItem in lstPassive:
                if not iPassiveMax:
                    continue
                iPassiveMax -= 1
            else:
                DiceLog.Alert('%s %s carryin specitem err type %s %d' % (self.m_Game.m_ID, oOwner.m_PlayerID, lstCarryInSpecItem, iSpecItem))
            lstSpecialItemInfo.append(iSpecItem)
        
        dFillSpecItem = {
            DICESPECIAL_PASSIVE_TAKEEFFECT: iPassiveMax,
            DICESPECIAL_ACTIVE_TAKEEFFECT: iActiveMax }
        for iSpecItemType, iFillNum in dFillSpecItem.items():
            for _ in range(iFillNum):
                if not iFillNum:
                    break
                iFillNum -= 1
                setCanChoose = set(GetDiceSpecialTypeList(iSpecItemType)) & set(dUnlockSpecItem) - set(lstSpecialItemInfo) - AUTOFILL_EXCLUDEDICESPECIAL
                if not setCanChoose:
                    break
                iSpecialItem = ChooseKey(self.m_Game, dict.fromkeys(setCanChoose, 1))
                DiceLog.Debug('%s %s carryin specitem autofill %s %s %d' % (self.m_Game.m_ID, oOwner.m_PlayerID, lstCarryInSpecItem, dFilterSpecItemInfo, iSpecialItem))
                lstSpecialItemInfo.append(iSpecialItem)
            
        
        for iPos, iSpecialItem in enumerate(lstSpecialItemInfo):
            self.m_SpecialItemInfo[iPos] = iSpecialItem
            if iSpecialItem not in self.m_SpecItemUseEnergy:
                self.m_SpecItemUseEnergy[iSpecialItem] = 0
        
        DiceLog.Debug('%s %s carryin specitem %s %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, dFilterSpecItemInfo, self.m_SpecialItemInfo))
        self.GS2CDiceSpecialItemGrooveInfo(oOwner)
        if not iIsAI:
            self.EffectSpecialItem()

    
    def EffectSpecialItem(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if self.m_Game.m_WarMgr.IsAIHero(oOwner.m_ID):
            return None
        lstActive = GetDiceSpecialTypeList(DICESPECIAL_ACTIVE_TAKEEFFECT)
        lstPassiveInit = GetDiceSpecialTypeList(DICESPECIAL_PASSIVE_INIT_TAKEEFFECT)
        for iSpecialItem in self.m_SpecialItemInfo.values():
            if iSpecialItem in lstActive:
                self.m_SpecItemTriggerEnergy[iSpecialItem] = GetDiceSpecialItemTriggerEnergy(iSpecialItem)
                continue
            if iSpecialItem not in lstPassiveInit:
                self.m_NextThrowItemCache[iSpecialItem] = 1
                dicenet.GS2CDiceSpecialItemInfo(self.m_PlayerID, self.m_NextThrowItemCache)
                continue
            self.UseSpecialItem(oOwner, iSpecialItem, None, None, iSendMsg = 0)
        
        self.GS2CSyncActiveDiceSpecialItem()

    
    def GS2CSyncActiveDiceSpecialItem(self):
        for iSpecialItem in self.m_SpecItemTriggerEnergy:
            iTriggerEnergy = self.GetSpItemTriggerEnergy(iSpecialItem)
            (iCanUseCnt, iCanUseEnergy) = self.GetSpecItemCanUseCntAndEnergy(iSpecialItem)
            dicenet.GS2CSyncActiveDiceSpecialItem(self.m_PlayerID, iSpecialItem, iCanUseCnt, iCanUseEnergy, iTriggerEnergy)
        

    
    def GS2CDiceSpecialItemGrooveInfo(self, oHero):
        lstSpecialItemInfo = []
        for iPos, iSpecialItem in self.m_SpecialItemInfo.items():
            lstSpecialItemInfo.append([
                iPos,
                iSpecialItem])
        
        dicenet.GS2CDiceSpecialItemGrooveInfo(oHero.m_PlayerID, lstSpecialItemInfo)

    
    def UseDiceSpecialItem(self, oHero, iPos, iSpecialItem, lstChooseDice):
        if iPos not in self.m_SpecialItemInfo or not self.m_SpecialItemInfo[iPos]:
            DiceLog.Alert('%s %s use notspi %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPos, self.m_SpecialItemInfo))
            return None
        iSpecialItem = self.m_SpecialItemInfo[iPos]
        self.UseSpecialItem(oHero, iSpecialItem, lstChooseDice, dInfo = None)

    
    def UseSpecialItem(self, oHero, iSpecialItem, lstDice, dInfo, iSendMsg = 1):
        clsSpecialItem = cl_dice.GetDiceSpecialCls(iSpecialItem)
        if not clsSpecialItem:
            DiceLog.Alert('%s %s specialitem null %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iSpecialItem))
            return None
        cFunEnableAction = clsSpecialItem.m_EnableActionInfo
        if not cFunEnableAction:
            return None
        if dInfo is None:
            dInfo = { }
        dInfo['Item'] = iSpecialItem
        DiceLog.Debug('%s %s usespecialitem %s %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, lstDice, iSpecialItem))
        if iSpecialItem in GetDiceSpecialTypeList(DICESPECIAL_ACTIVE_TAKEEFFECT):
            (iCanUseCnt, _) = self.GetSpecItemCanUseCntAndEnergy(iSpecialItem)
            if not iCanUseCnt:
                DiceLog.Alert('%s %s active specialitem %s no use times %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iSpecialItem, self.m_ActiveCurDiceEnergy))
                return None
            iEnergy = self.GetSpItemTriggerEnergy(iSpecialItem)
            self.m_SpecItemUseEnergy[iSpecialItem] += iEnergy
            self.GS2CSyncActiveDiceSpecialItem()
        if iSendMsg:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_USEDICESPECIALITEM, oHero, {
                'SpecialItemSID': iSpecialItem })
        cFunEnableAction(oHero, lstDice, dInfo)

    
    def ClearDicePoints(self, iDice, sReason):
        if not self.CheckDiceRoll(iDice):
            return None
        oDice = self.m_Dice[iDice]
        iAssemblePos = oDice.GetDiceAssemblePos()
        if iAssemblePos in self.m_AssembleDice:
            self.AssembleDice(iDice, iAssemblePos, TYPE_DISASSEMBLE, sReason = 'ClearDicePoints')
        oDice.ClearPoints(sReason)

    
    def CheckDiceRoll(self, iDice):
        oDice = self.GetDiceByID(iDice)
        if not oDice or not oDice.GetRollType():
            return False
        return True

    
    def ReThrowDice(self, iDice, sReason, cbfunc, iDirectSpItem = 0, dExcludePoints = None):
        if not self.CheckDiceRoll(iDice):
            return None
        oDice = self.m_Dice[iDice]
        oDice.AddCanRollTimes(1, sReason)
        self.RollDice(iDice, sReason, cbfunc, iDirectSpItem, dExcludePoints)

    
    def AddDicePoints(self, iDice, iAddPoints, sReason, iDirectSpItem = 0):
        if not self.CheckDiceRoll(iDice):
            return None
        oDice = self.m_Dice[iDice]
        iMaxPoint = oDice.GetMaxPoint()
        iPoints = oDice.m_RollPoint + iAddPoints
        if iPoints > iMaxPoint:
            iPoints -= iMaxPoint
        if iDirectSpItem:
            self.SetDicePoint(iDice, iPoints, sReason, None, [
                iDirectSpItem])
        else:
            self.SetDicePoint(iDice, iPoints, sReason)

    
    def CopyDice(self, iDice, iNum, sReason):
        if iDice not in self.m_Dice:
            oOwner = self.GetOwner()
            if oOwner and self.m_Game:
                DiceLog.Alert('%s %s copydice: dice err %s %s %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, iDice, iNum, sReason))
            return None
        oDice = self.m_Dice[iDice]
        for _ in range(iNum):
            dDiceInfo = oDice.GetDiceInfo()
            self.RewardDice(dDiceInfo, sReason)
        

    
    def FuseDice(self, lstDice, sReason):
        if len(lstDice) != FUSEDICE_NUM:
            return 0
        oOwner = self.GetOwner()
        if not oOwner:
            return 0
        iRet = self.CheckPutDice(oOwner, lstDice, sReason)
        if not iRet:
            return 0
        dDiceChoosePool = { }
        iSumPoint = 0
        for iDice in lstDice:
            if iDice not in self.m_Dice:
                continue
            oDice = self.m_Dice[iDice]
            iDiceSID = oDice.m_SID
            if iDiceSID in dDiceChoosePool:
                dDiceChoosePool[iDiceSID] += 1
            else:
                dDiceChoosePool[iDiceSID] = 1
            iDiceQuality = oDice.m_Quality
            iSumPoint += iDiceQuality
            self.RemoveDice(iDice, iDrop = 0, sReason = sReason)
        
        oGame = self.m_Game
        iResultDiceSID = ChooseKey(oGame, dDiceChoosePool)
        fFinalPoint = (iSumPoint + FUSEDICE_NUM) * 100 / FUSEDICE_NUM
        fHighterQualityProb = fFinalPoint % 100
        iBaseQuality = fFinalPoint // 100
        if fHighterQualityProb and self.m_Game.Random(100) < fHighterQualityProb:
            iBaseQuality += 1
        iResultDiceQuality = int(min(iBaseQuality, DICE_QUALITY_TALE))
        DiceLog.Debug('%s %s %s fusedice result %s %s %s' % (oGame.m_ID, oOwner.m_PlayerID, lstDice, iResultDiceSID, iResultDiceQuality, sReason))
        dDiceInfo = self.GetDiceInfo(iResultDiceSID, iResultDiceQuality)
        oResultDice = self.RewardDice(dDiceInfo, sReason)
        return oResultDice.m_ID

    
    def CheckPutDice(self, oOwner, lstDice, sReason):
        oGame = self.m_Game
        lstFinal = []
        for iDice in lstDice:
            if not self.CheckDiceRoll(iDice):
                DiceLog.Debug('%s %s fusedice %s not exist or not roll %s' % (oGame.m_ID, oOwner.m_PlayerID, iDice, sReason))
                return 0
            if iDice in lstFinal:
                DiceLog.Debug('%s %s fusedice %s repeat %s' % (oGame.m_ID, oOwner.m_PlayerID, lstDice, sReason))
                return 0
            lstFinal.append(iDice)
        
        return 1

    
    def GetTransferDiceSID(self, iDice, iSpecialItemSID, sReason, iChooseNum):
        if not self.CheckDiceRoll(iDice):
            return { }
        oOwner = self.GetOwner()
        if not oOwner:
            return { }
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return { }
        dAllDice = oDiceElement.GetAllUnLockDice(oOwner.m_PlayerID)
        oDice = self.m_Dice[iDice]
        dExcludeDice = GetExcludeDiceQuality(oDice.m_Quality)
        dChooseDice = { dAllDice[iDiceSID]: iDiceSID for iDiceSID in dAllDice if iDiceSID not in dExcludeDice }
        dChooseDice.pop(oDice.m_SID, 0)
        lstResult = ChooseMulKeys(self.m_Game, dChooseDice, iChooseNum)
        if not lstResult:
            return { }
        dResult = { }
        for iPos, iResult in enumerate(lstResult):
            dResult[iPos] = iResult
        
        lstSpItem = [
            iSpecialItemSID]
        cbFuncTransferDice = Functor(self.TransferDice, iDice)
        cbFuncRemoveDice = Functor(self.ApplyTempAbility, iDice)
        self.m_TempResult[iDice] = (dResult, cbFuncTransferDice, cbFuncRemoveDice, lstSpItem)
        cbAutoChooseDiceAbility = Functor(self.AutoChooseAbility, iDice, sReason)
        sKey = 'ChooseDiceResult-%s' % iDice
        oOwner.AddMapLoadOKCbFun(sKey, cbAutoChooseDiceAbility)
        return dResult

    
    def TransferDice(self, iDice, iTransferDiceSID, sReason, cbfunc, lstSpItem, bAddDiceEnergy = False):
        if not self.CheckDiceRoll(iDice):
            return 0
        if not self.GetOwner():
            return 0
        oDice = self.m_Dice[iDice]
        dDiceInfo = self.GetDiceInfo(iTransferDiceSID, oDice.m_Quality)
        dDiceInfo['RP'] = oDice.m_RollPoint
        dDiceInfo['CRT'] = oDice.GetCanRollTimes()
        iAssemblePos = oDice.GetDiceAssemblePos()
        self.RemoveDice(iDice, iDrop = 0, sReason = sReason)
        oNewDice = self.RewardDice(dDiceInfo, sReason)
        if oNewDice:
            iNewDice = oNewDice.m_ID
            if iAssemblePos:
                self.AssembleDice(iNewDice, iAssemblePos, TYPE_ASSEMBLE, sReason = 'TransferDice')
            return iNewDice
        return 0

    
    def GetDiceInfo(self, iDiceSID, iDiceQuality):
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return { }
        dDiceInfo = {
            'SID': iDiceSID,
            'QL': iDiceQuality,
            'PR': oDiceElement.GetTempPointRangeByQuality(iDiceQuality) }
        return dDiceInfo

    
    def ChangeDicePacketPointsShowCnt(self, iCnt):
        DiceLog.Debug('%s %s packetshowcnt %s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_DicePacketPointsShowCnt, iCnt))
        self.m_DicePacketPointsShowCnt = min(self.m_DicePacketPointsShowCnt + iCnt, PACKETSHOWCNT_MAX)

    
    def GetDicePacketPointsShowCnt(self):
        return self.m_DicePacketPointsShowCnt

    
    def GetSpecialItemInfo(self):
        return self.m_SpecialItemInfo

    
    def SetLastTimePoint(self, iPoint):
        iEffect = self.m_LastTimePointInfo[0]
        if iEffect == SPECIAL_ITEM_1022_WAIT_CLEAR:
            self.m_LastTimePointInfo[0] = SPECIAL_ITEM_1022_INACTIVE
            self.m_LastTimePointInfo[1] = 0
            iPoint = 0
        else:
            self.m_LastTimePointInfo[1] = iPoint
        dicenet.GS2CUpdateAddUpPoint(self.m_PlayerID, iPoint)
        DiceLog.Debug('%s %s set last time point %s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_LastTimePointInfo[0], self.m_LastTimePointInfo[1]))

    
    def SetLastTimeActive(self):
        self.m_LastTimePointInfo[0] = SPECIAL_ITEM_1022_ACTIVE
        DiceLog.Debug('%s %s set last time active' % (self.m_Game.m_ID, self.m_PlayerID))

    
    def SetLastTimeWaitClear(self):
        self.m_LastTimePointInfo[0] = SPECIAL_ITEM_1022_WAIT_CLEAR
        self.m_LastTimePointInfo[1] = 0
        DiceLog.Debug('%s %s set last time wait clear' % (self.m_Game.m_ID, self.m_PlayerID))

    
    def SetDelta(self, iDelta):
        self.m_LastTimePointInfo[2] = iDelta
        DiceLog.Debug('%s %s set delta %s' % (self.m_Game.m_ID, self.m_PlayerID, iDelta))

    
    def GetLastTimeActivePoint(self):
        (iActive, iPoint, iDelta) = self.m_LastTimePointInfo
        iActivePoint = max(iPoint - iDelta, 0) if iActive == SPECIAL_ITEM_1022_ACTIVE else 0
        iRealPoint = iPoint if iActive == SPECIAL_ITEM_1022_ACTIVE else 0
        return (iActivePoint, iRealPoint)

    
    def RewardDiceSelectionPacket(self, oHero, oDrop, sReason):
        oDiceElement = self.m_Game.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            oDrop.Remove('NotDiceElement')
            return None
        iQuality = oDrop.m_Quality
        dAllDice = oDiceElement.GetAllUnLockDice(oHero.m_PlayerID)
        dExcludeDice = GetExcludeDiceQuality(iQuality)
        lstSelectionDice = list(dAllDice.keys() - dExcludeDice.keys())
        if lstSelectionDice:
            dPointRange = oDiceElement.GetTempPointRangeByQuality(iQuality)
            oHero.IncMenuIdx()
            dicenet.GS2CDiceSelectionPacketInfo(oHero, iQuality, lstSelectionDice, dPointRange)
            npcnet.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, Functor(self.SelectDice, oDrop.m_ID, lstSelectionDice, sReason))
        else:
            oDrop.Remove('NotDice')

    
    def SelectDice(self, iDrop, lstSelectionDice, sReason, oHero, iDiceSID):
        oGame = self.m_Game
        oDrop = self.m_Game.GetObject(iDrop)
        if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_DICESELECTIONPACKET:
            return None
        iQuality = oDrop.m_Quality
        oDrop.Remove('SelectDice')
        if iDiceSID not in lstSelectionDice:
            return None
        DiceLog.Debug('%s %s selectdice result %s %s %s %s' % (oGame.m_ID, oHero.m_PlayerID, iDiceSID, iQuality, lstSelectionDice, sReason))
        dDiceInfo = self.GetDiceInfo(iDiceSID, iQuality)
        self.RewardDice(dDiceInfo, sReason)

    
    def GetSpItemTriggerEnergy(self, iSpItemID):
        if iSpItemID not in self.m_SpecItemTriggerEnergy:
            return 99999
        return (self.m_SpecItemTriggerEnergy[iSpItemID] * self.m_TriggerEnergyMul // 100) * 100

    
    def AddSpecItemTriggerEnergyRatio(self, iMul):
        self.m_TriggerEnergyMul += iMul
        self.GS2CSyncActiveDiceSpecialItem()

    
    def GetSpecItemCanUseCntAndEnergy(self, iSpItemID):
        if iSpItemID not in self.m_SpecItemUseEnergy:
            return (0, 0)
        iEnergy = self.m_ActiveCurDiceEnergy - self.m_SpecItemUseEnergy[iSpItemID]
        iTriggerEnergy = self.GetSpItemTriggerEnergy(iSpItemID)
        iCanUseCnt = iEnergy // iTriggerEnergy
        iCanUseEnergy = iEnergy % iTriggerEnergy
        return (iCanUseCnt, iCanUseEnergy)


