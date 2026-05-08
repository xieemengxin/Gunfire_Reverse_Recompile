# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/backpackcon.pyc
# RelativePath: clientlogic/cl_container/backpackcon.pyc
# Source Generated with Decompyle++
# File: backpackcon.pyc (Python 3.6)

from cl_only import ChooseKey, SendAlert, ShufferList, ChooseMulKeys
from cl_cscommondef import MODULE_MASK, CRYSTAL_MASK
from cl_commondefines import CRTSTAL_RAWMATERIAL, S7_ALL_PERFORM_ENABLE, S7_MODULE_POINT_CHANGE, S7_AUTO_EQUIP, S7CRYSTAL_ADD, S7MODULE_ADD, S7MODULE_ENHANCE, S7MODULE_AUTOENHANCE, S7MODULE_DECREASE, S7_AUTO_UNEQUIP, S7CRYSTAL_REMOVE, S7MODULE_REMOVE, S7_SIMULATE_MODULE_SID, S7ITEM_REFRESH
from cl_object.logging import BackpackLog
from cl_container.mobject import CBaseSeasonContainer, ATTR_GET, FUNC_GET, CONFUNC_GET
from cl_platformdata import GetS7CostPoint, GetS7ModuleByTag, GetModuleTag, GetModuleEquipNumMax, GetS7CrystalType, GetS7Module, GetS7Crystal, GetExclusionCrystal
import cl_seasonplay.season7 as clseason7
import cl_seasonplay.net as seasonplaynet
import cl_msgcenter
import cl_drop
import cl_notify
import cllib.lib_flag
BACKPACKCON_EMPTY_POS = (0, 0)
ENHANCEMODULE_ADD_POINT = 1
AUTOEQUIP_MAX_MODULE = 8
CRYSTAL_RAWMATERIAL_SID = 1001
OVERCHARGE_BENE_SID = 13734
ENHANCEMODULE_COMMONNOTIFY = 2544
ENHANCEMODULE = 1
AUTO_ENHANCEMODULE = 2
GET_EQUIP_POS_HASPOINT = 1
GET_EQUIP_POS_HASNOTPOINT = 2
EQUIP_STATUS = 1
UNEQUIP_STATUS = 2
DELAY_ENABLE_MODULE = 1
NOW_ENABLE_MODULE = 2
NEAR_OFFSET = {
    (0, 1),
    (0, -1),
    (1, 0),
    (1, 1),
    (1, -1),
    (-1, 0),
    (-1, 1),
    (-1, -1)}

class CBackpackContainer(CBaseSeasonContainer):
    m_SeasonNum = 7
    m_ItemAttr = {
        'EffGrid': FUNC_GET,
        'Pos': CONFUNC_GET,
        'Point': FUNC_GET,
        'Lock': FUNC_GET,
        'SimModule': CONFUNC_GET }
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_RowNum = 0
        self.m_ColNum = 0
        self.m_UnlockRowNum = 0
        self.m_UnlockColNum = 0
        self.m_UnLockModule = { }
        self.m_UnLockCrystal = { }
        self.m_Module = { }
        self.m_Crystal = { }
        self.m_EquipMap = { }
        self.m_Item2Pos = { }
        self.m_PointMap = { }
        self.m_Perform = { }
        self.m_CrystalEffInfo = { }
        self.m_NeedEnableModule = 0
        self.m_ModuleEquipNum = { }
        self.m_ExtraPoint = { }
        self.m_ExtraPointInfo = { }
        self.m_BeneCrystal = 0
        self.m_SignModuleInfo = { }
        self.m_SimulateInfo = (0, 0, 0)
        self.m_SpecialPassive = None
        self.Init()

    
    def Init(self):
        oGame = self.m_Game
        if not oGame:
            return None
        oOwner = self.GetOwner()
        if oOwner:
            cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, 'BackpackCon', -1, 0)

    
    def OnMapLoadOK(self, oHero, dMsgInfo):
        self.AllPerformEnable()
        self.GS2CS7SignItem()

    
    def Release(self):
        oOwner = self.GetOwner()
        if oOwner:
            cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'BackpackCon')
        for dPerform in dict(self.m_Perform).values():
            for _, oPerform in dPerform.values():
                oPerform.Release()
            
        
        for oModule in list(self.m_Module.values()):
            oModule.Release()
        
        for oCrystal in list(self.m_Crystal.values()):
            oCrystal.Release()
        
        oSpecialPassive = self.GetSpecialPassive()
        if oSpecialPassive:
            oSpecialPassive.Release()
        self.m_SpecialPassive = None
        self.m_Module = { }
        self.m_Crystal = { }
        self.m_EquipMap = { }
        self.m_PointMap = { }
        self.m_Perform = { }
        self.m_CrystalEffInfo = { }
        self.m_ModuleEquipNum = { }
        self.m_Game = None

    
    def Load(self, dData):
        if not dData:
            return None
        (iRowNum, iColNum) = dData.get('BS', [
            0,
            0])
        self.SetEquipAreaMaxSize(iRowNum, iColNum, sReason = 'load', iSync = 0)
        (iUnlockRow, iUnlockCol) = dData.get('UL', [
            0,
            0])
        self.UnlockEquipAreaSize(iUnlockRow, iUnlockCol, sReason = 'load', iSync = 0)
        lstModuleInfo = dData.get('MD', { })
        for tPos, dModule in lstModuleInfo:
            oModule = clseason7.CreateModule(self.m_Game, oModuleDataCon = self, dData = dModule)
            if not oModule:
                continue
            self.m_Module[oModule.m_ID] = oModule
            if tPos != BACKPACKCON_EMPTY_POS:
                self.EquipS7Item(*tPos, oModule.m_ID, **{
                    'iSync': 0 })
        
        lstCrystalInfo = dData.get('CS', { })
        for tPos, dCrystal in lstCrystalInfo:
            oCrystal = clseason7.CreateCrystal(self.m_Game, oCrystalCon = self, dData = dCrystal)
            if not oCrystal:
                continue
            self.m_Crystal[oCrystal.m_ID] = oCrystal
            if 'BM' in dCrystal:
                self.m_BeneCrystal = oCrystal.m_ID
            if tPos != BACKPACKCON_EMPTY_POS:
                self.EquipS7Item(*tPos, oCrystal.m_ID, **{
                    'iSync': 0 })
        
        self.m_UnLockModule = dData.get('ULM', { })
        self.m_UnLockCrystal = dData.get('ULC', { })
        self.m_SignModuleInfo = dData.get('SMI', { })
        if 'SP' in dData:
            self.SetSpecialPassive(dData['SP'])

    
    def Save(self):
        dData = { }
        lstModule = []
        lstCrystal = []
        for iModule, oModule in self.m_Module.items():
            tPos = self.GetPos(iModule)
            lstModule.append([
                tPos,
                oModule.Save()])
        
        for iCrystal, oCrystal in self.m_Crystal.items():
            tPos = self.GetPos(iCrystal)
            dCrystal = oCrystal.Save()
            if iCrystal == self.m_BeneCrystal:
                dCrystal['BM'] = 1
            lstCrystal.append([
                tPos,
                dCrystal])
        
        dData['MD'] = lstModule
        dData['CS'] = lstCrystal
        dData['BS'] = [
            self.m_RowNum,
            self.m_ColNum]
        dData['UL'] = [
            self.m_UnlockRowNum,
            self.m_UnlockColNum]
        dData['ULM'] = self.m_UnLockModule
        dData['ULC'] = self.m_UnLockCrystal
        dData['SMI'] = self.m_SignModuleInfo
        oSpecialPassive = self.GetSpecialPassive()
        if oSpecialPassive:
            dData['SP'] = oSpecialPassive.m_SID
        return dData

    
    def ClearAll(self):
        for iModule in list(self.m_Module):
            self.RemoveS7Item(iModule, sReason = 'useseed')
        
        for iCrystal in list(self.m_Crystal):
            self.RemoveS7Item(iCrystal, sReason = 'useseed')
        
        self.AllPerformDisable()
        self.m_RowNum = 0
        self.m_ColNum = 0
        self.m_UnlockRowNum = 0
        self.m_UnlockColNum = 0
        self.m_Module = { }
        self.m_Crystal = { }
        self.m_EquipMap = { }
        self.m_Item2Pos = { }
        self.m_Perform = { }
        self.m_CrystalEffInfo = { }
        self.m_ModuleEquipNum = { }
        self.Refresh({
            self.m_PlayerID: 1 })

    
    def Refresh(self, dPlayer):
        if self.m_PlayerID in dPlayer:
            self.GS2CBackpackConInfo()
        for oModule in self.m_Module.values():
            dExtInfo = self.GetModuleExtInfo(oModule)
            self.GS2CAddModule(oModule, dPlayer, dExtInfo)
        
        for oCrystal in self.m_Crystal.values():
            dExtInfo = self.GetCrystalExtInfo(oCrystal)
            self.GS2CAddCrystal(oCrystal, dPlayer, dExtInfo = dExtInfo)
        
        self.GS2CRefreshPosPoint(dPlayer = dPlayer)

    
    def RefreshS7Item(self, oS7Item, iEffPoint = 0, iUnEffPoint = 0, iSync = 1, iNeedEnableModule = DELAY_ENABLE_MODULE, lstSyncAttr = None):
        if not oS7Item:
            return None
        iS7Item = oS7Item.m_ID
        if iNeedEnableModule:
            self.m_NeedEnableModule = 1
            if iNeedEnableModule == NOW_ENABLE_MODULE:
                self.AllPerformEnable()
        if oS7Item.m_Type == CRYSTAL_MASK:
            if iUnEffPoint:
                self.UnEffectCrystalPoint(iS7Item)
            if iEffPoint:
                self.EffectCrystalPoint(iS7Item)
        dMsgInfo = {
            'S7Item': iS7Item,
            'Type': oS7Item.m_Type,
            'Sync': iSync }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.GetOwner(), dMsgInfo, iSub = S7ITEM_REFRESH)
        if iSync:
            self.GS2CRefreshItemAttr(iS7Item, lstSyncAttr)

    
    def GetCrystalExtInfo(self, oCrystal):
        dExtInfo = { }
        if oCrystal.m_ID == self.m_BeneCrystal:
            dExtInfo['BeneMark'] = 1
        dExtInfo['Lock'] = oCrystal.Query('Lock')
        return dExtInfo

    
    def GetModuleExtInfo(self, oModule):
        dExtInfo = {
            'Lock': oModule.Query('Lock') }
        if oModule.m_SID == S7_SIMULATE_MODULE_SID:
            dExtInfo['SimModule'] = self.m_SimulateInfo[1]
        return dExtInfo

    
    def SetBeneCrystal(self, oCrystal):
        if not oCrystal:
            return None
        self.m_BeneCrystal = oCrystal.m_ID

    
    def GetBeneCrystal(self):
        return self.m_BeneCrystal

    
    def SetEquipAreaMaxSize(self, iRow, iCol, sReason, iSync = 1):
        if self.m_RowNum or self.m_ColNum:
            SendAlert('err', '%d %d already set equiparea size %d %d %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iRow, iCol, self.m_UnlockRowNum, self.m_UnlockColNum, sReason))
            return None
        self.m_RowNum = iRow
        self.m_ColNum = iCol
        BackpackLog.Debug('%s %s setequipareamaxsize %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iRow, iCol, sReason))
        self.InitPointMap(iSync = iSync)

    
    def UnlockEquipAreaSize(self, iRow, iCol, sReason, iSync = 1):
        if iRow < self.m_UnlockRowNum or iCol < self.m_UnlockColNum:
            SendAlert('err', '%d %d unlockequipareasize err %d %d %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iRow, iCol, self.m_UnlockRowNum, self.m_UnlockColNum, sReason))
            return None
        if (iRow, iCol) == (self.m_UnlockRowNum, self.m_UnlockColNum):
            return None
        self.m_UnlockRowNum = iRow
        self.m_UnlockColNum = iCol
        BackpackLog.Debug('%s %s unlockequipareasize %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iRow, iCol, sReason))
        if iSync:
            self.GS2CBackpackConInfo()
            self.GS2CRefreshPosPoint()

    
    def InitPointMap(self, iSync = 1):
        self.m_CrystalEffInfo = { }
        self.m_PointMap = { }
        for x in range(1, self.m_ColNum + 1):
            for y in range(1, self.m_RowNum + 1):
                self.m_PointMap[(x, y)] = 0
            
        
        if iSync:
            self.GS2CRefreshPosPoint()

    
    def GetModule(self, iModule):
        if iModule not in self.m_Module:
            return None
        return self.m_Module[iModule]

    
    def GetEquipModuleInfo(self, iCheckSID, iCheckTag, iCheckFullPoint = 0, iCheckHasExtraPoint = 0, iCheckEnhanceTimes = 0, iCheckEquip = 0, iGetNum = 0, iGetPoint = 0):
        iResult = 0
        for iModule, oModule in self.m_Module.items():
            if not self.IsEquip(iModule):
                continue
            iModuleSID = oModule.m_SID
            if iCheckSID and iModuleSID != iCheckSID:
                continue
            if iCheckTag:
                dModuleTag = GetModuleTag(iModuleSID)
                if iCheckTag not in dModuleTag:
                    continue
                continue
            if iCheckFullPoint:
                iCurPoint = self.GetModulePoint(iModule)
                iMaxPoint = oModule.GetPointMax()
                if iCurPoint < iMaxPoint:
                    continue
                continue
            if iCheckHasExtraPoint:
                tPos = self.GetPos(iModule)
                if tPos not in self.m_ExtraPoint:
                    continue
                continue
            if iCheckEnhanceTimes and oModule.m_Point < iCheckEnhanceTimes:
                continue
            if iCheckEquip:
                iIsEquip = self.IsEquip(iModule)
                if (iCheckEquip == EQUIP_STATUS or not iIsEquip or iCheckEquip == UNEQUIP_STATUS) and iIsEquip:
                    continue
                continue
            if iGetNum:
                iResult += 1
                continue
            if iGetPoint:
                iResult += self.GetModulePoint(iModule)
                continue
            SendAlert('err', '%d %d 获取装配s7组件未传入Get参数' % (self.m_Game.m_ID, self.m_PlayerID))
            return 0
        
        return iResult

    
    def GetReachedPointsNum(self, iTargetPoint, iExcludeOverflow = 1):
        iNum = 0
        for iModule in self.m_Module.keys():
            if self.GetModulePoint(iModule, iExcludeOverflow = iExcludeOverflow) >= iTargetPoint:
                iNum += 1
        
        return iNum

    
    def GetFullyActModuleCnt(self, iTargetPoint, iExcludeOverflow = 1):
        iNum = 0
        for iModule, oModule in self.m_Module.items():
            if self.GetModulePoint(iModule, iExcludeOverflow = iExcludeOverflow) >= iTargetPoint and iTargetPoint >= oModule.GetPointMax():
                iNum += 1
        
        return iNum

    
    def GetCrystal(self, iCrystal):
        if iCrystal not in self.m_Crystal:
            return None
        return self.m_Crystal[iCrystal]

    
    def GetItemByID(self, iItem):
        if iItem in self.m_Module:
            return self.m_Module[iItem]
        if iItem in self.m_Crystal:
            return self.m_Crystal[iItem]

    
    def CustomGetModule(self, iCheckEquip = 0, iCheckCanEquip = 0):
        lstModule = []
        for oItem in self.m_Module.values():
            if not oItem:
                continue
            if iCheckEquip:
                iIsEquip = self.IsEquip(oItem.m_ID)
                if (iCheckEquip == EQUIP_STATUS or not iIsEquip or iCheckEquip == UNEQUIP_STATUS) and iIsEquip:
                    continue
                continue
            if iCheckCanEquip:
                iModuleSID = oItem.m_SID
                iCurEquipNum = self.m_ModuleEquipNum.get(iModuleSID, 0)
                iEquipNumMax = GetModuleEquipNumMax(iModuleSID)
                if iCurEquipNum >= iEquipNumMax:
                    continue
                continue
            lstModule.append(oItem)
        
        return lstModule

    
    def CustomGetCrystal(self, iCheckEquip = 0, iIgnoreType = 0):
        lstCrystal = []
        for oItem in self.m_Crystal.values():
            if not oItem:
                continue
            if iCheckEquip:
                iIsEquip = self.IsEquip(oItem.m_ID)
                if (iCheckEquip == EQUIP_STATUS or not iIsEquip or iCheckEquip == UNEQUIP_STATUS) and iIsEquip:
                    continue
                continue
            if iIgnoreType and GetS7CrystalType(oItem.m_SID) == iIgnoreType:
                continue
            lstCrystal.append(oItem)
        
        return lstCrystal

    
    def GetPerform(self, iPerform, iItem):
        if iItem not in self.m_Perform or iPerform not in self.m_Perform[iItem]:
            oSpecialPassive = self.GetSpecialPassive()
            if oSpecialPassive and oSpecialPassive.m_SID == iPerform:
                return oSpecialPassive
            return None
        (_, oPerform) = self.m_Perform[iItem][iPerform]
        return oPerform

    
    def GetPosPoint(self, x, y):
        tPos = (x, y)
        iPosPoint = self.m_PointMap[tPos] if tPos in self.m_PointMap else 0
        iExtraPoint = self.m_ExtraPoint[tPos] if tPos in self.m_ExtraPoint else 0
        return iPosPoint + iExtraPoint

    
    def GetModulePoint(self, iModule, iExcludeOverflow = 0):
        oModule = self.GetModule(iModule)
        if not oModule:
            return 0
        tPos = self.GetPos(iModule)
        iPosPoint = self.GetPosPoint(*tPos)
        iModulePoint = iPosPoint + oModule.GetPoint()
        if iExcludeOverflow:
            return min(oModule.GetPointMax(), iModulePoint)
        return iModulePoint

    
    def GetMaxModule(self):
        dResult = { }
        dNowModule = { }
        for oModule in self.m_Module.values():
            iModuleSID = oModule.m_SID
            if iModuleSID not in dNowModule:
                dNowModule[iModuleSID] = 1
            else:
                dNowModule[iModuleSID] += 1
            iEquipNumMax = GetModuleEquipNumMax(iModuleSID)
            if dNowModule[iModuleSID] < iEquipNumMax:
                continue
            for iQuality in oModule.m_QualityConfig:
                dResult[(iModuleSID, iQuality)] = 1
            
        
        return dResult

    
    def CheckModuleEquipNumMax(self, iModuleSID):
        iCurEquipNum = self.m_ModuleEquipNum.get(iModuleSID, 0)
        iEquipNumMax = GetModuleEquipNumMax(iModuleSID)
        if iCurEquipNum >= iEquipNumMax:
            return 1
        return 0

    
    def GetSameTagModule(self, iModuleSID):
        dTag = GetModuleTag(iModuleSID)
        if not dTag:
            return { }
        dSameTagModule = { }
        dResult = { }
        for iTag in dTag:
            dModule = GetS7ModuleByTag(iTag)
            dSameTagModule.update(dModule)
        
        for oModule in self.m_Module.values():
            iModuleSID = oModule.m_SID
            if iModuleSID in dSameTagModule:
                dResult[oModule.m_ID] = 1
        
        return dResult

    
    def GetModuleData(self):
        lstModules = []
        for iItemID in self.m_EquipMap.values():
            if iItemID not in self.m_Module:
                continue
            oModule = self.m_Module[iItemID]
            (x, y) = self.GetPos(oModule.m_ID)
            dModule = {
                'id': oModule.m_ID,
                'quality': oModule.GetQuality(),
                'sid': oModule.m_SID,
                'x': x,
                'y': y,
                'point': oModule.GetPoint() }
            lstModules.append(dModule)
        
        return lstModules

    
    def GetCrystalData(self):
        lstCrystals = []
        for iItemID in self.m_EquipMap.values():
            if iItemID not in self.m_Crystal:
                continue
            oItem = self.m_Crystal[iItemID]
            (x, y) = self.GetPos(oItem.m_ID)
            lstEffPoints = [ {
'x': t[0],
'y': t[1],
'point': t[2] } for t in oItem.GetEffGrid() ]
            dCrystal = {
                'effPoints': lstEffPoints,
                'rotate': oItem.GetRotate(),
                'sid': oItem.m_SID,
                'x': x,
                'y': y }
            lstCrystals.append(dCrystal)
        
        return lstCrystals

    
    def GetExtraFlagData(self):
        lstExtraFlag = []
        if not self.m_ExtraPoint:
            return lstExtraFlag
        for tPos, iPoint in self.m_ExtraPoint.items():
            lstExtraFlag.append({
                'x': tPos[0],
                'y': tPos[1],
                'point': iPoint })
        
        return lstExtraFlag

    
    def GetBackPackData(self):
        dData = {
            'Crystals': self.GetCrystalData(),
            'Modules': self.GetModuleData(),
            'ExtraFlag': self.GetExtraFlagData() }
        (iMaxRowNum, iMaxColNum) = self.GetMaxRowAndColNum()
        dData['SimModuleID'] = self.m_SimulateInfo[0]
        dData['SimID'] = self.m_SimulateInfo[1]
        dData['MaxRowNum'] = iMaxRowNum
        dData['MaxColNum'] = iMaxColNum
        return dData

    
    def GetAllEquipModulePoint(self, dCheckModuleTag = None, iCheckExcludeOverflow = 1):
        iAllEffPoint = 0
        setCheckModuleTag = set(dCheckModuleTag) if dCheckModuleTag else set()
        for iModule, oModule in self.m_Module.items():
            if not self.IsEquip(iModule):
                continue
            if setCheckModuleTag:
                dModuleTag = GetModuleTag(oModule.m_SID)
                if not setCheckModuleTag & set(dModuleTag):
                    continue
                continue
            iAllEffPoint += self.GetModulePoint(iModule, iExcludeOverflow = iCheckExcludeOverflow)
        
        return iAllEffPoint

    
    def GetLockPos(self):
        oWarMgr = self.m_Game.m_WarMgr
        oBackpackElement = oWarMgr.GetBackpackElement()
        if not oBackpackElement:
            return { }
        iMaxRow = self.m_RowNum
        iMaxCol = self.m_ColNum
        iUnlockRow = self.m_UnlockRowNum
        iUnlockCol = self.m_UnlockColNum
        (iNextUnlockRow, iNextUnLockCol) = (0, 0)
        dUnlockInfo = oBackpackElement.m_KillLayerBossUnlockConEquipAreaSize
        lstUnlockLayer = sorted(dUnlockInfo)
        for iLayer in lstUnlockLayer:
            if dUnlockInfo[iLayer] > (iUnlockRow, iUnlockCol):
                (iNextUnlockRow, iNextUnLockCol) = dUnlockInfo[iLayer]
                break
        
        dLockPos = { }
        for x in range(1, iMaxCol + 1):
            for y in range(1, iMaxRow + 1):
                if x <= iUnlockCol and y <= iUnlockRow:
                    continue
                iIsNextUnlock = 1 if x <= iNextUnLockCol and y <= iNextUnlockRow else 0
                dLockPos[(x, y)] = iIsNextUnlock
            
        
        return dLockPos

    
    def RewardModule(self, dModuleData, sReason = ''):
        oModule = clseason7.CreateModule(self.m_Game, oModuleDataCon = None, dData = dModuleData)
        if not oModule:
            return None
        self.AddS7Item(oModule, sReason)
        return oModule

    
    def RewardCrystal(self, dCrystalData, sReason = '', dExtInfo = None):
        oCrystal = clseason7.CreateCrystal(self.m_Game, oCrystalCon = None, dData = dCrystalData)
        if not oCrystal:
            return None
        if dExtInfo:
            iBeneMark = dExtInfo['BeneMark'] if 'BeneMark' in dExtInfo else 0
            if iBeneMark:
                self.SetBeneCrystal(oCrystal)
        self.AddS7Item(oCrystal, sReason, dExtInfo)
        return oCrystal

    
    def AddS7Item(self, oS7Item, sReason = '', dExtInfo = None):
        if not oS7Item:
            return None
        iType = oS7Item.m_Type
        iS7Item = oS7Item.m_ID
        if iType == MODULE_MASK:
            if iS7Item in self.m_Module:
                return None
            self.m_Module[iS7Item] = oS7Item
            iSubMsg = S7MODULE_ADD
            dExtInfo = self.GetModuleExtInfo(oS7Item)
            self.GS2CAddModule(oS7Item, dExtInfo = dExtInfo)
            dMsgInfo = {
                'S7Item': iS7Item,
                'ModuleSID': oS7Item.m_SID }
        elif iType == CRYSTAL_MASK:
            if iS7Item in self.m_Crystal:
                return None
            self.m_Crystal[iS7Item] = oS7Item
            iSubMsg = S7CRYSTAL_ADD
            if sReason == 'warshopbuy' and oS7Item.IsExtPointEffect():
                cl_notify.SendCommonNotify(self.m_Game, {
                    self.m_PlayerID: 1 }, 2545, { })
            if not dExtInfo:
                dExtInfo = self.GetCrystalExtInfo(oS7Item)
            self.GS2CAddCrystal(oS7Item, dPlayer = None, dExtInfo = dExtInfo)
            dMsgInfo = {
                'S7Item': iS7Item,
                'CrystalSID': oS7Item.m_SID,
                'TotalPoint': oS7Item.GetNowTotalPoint() }
        else:
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.GetOwner(), dMsgInfo, iSub = iSubMsg)
        oS7Item.AddToContainer(self)
        if self.m_Game.m_WarMgr.IsAIHero(self.m_Owner):
            self.AutoEquip()
            self.AutoEnhanceModules()
            self.AllPerformEnable()
        BackpackLog.Debug('%s %s adds7item %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oS7Item, sReason))

    
    def RemoveS7Item(self, iS7Item, sReason = '', iDrop = 0):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if iDrop and iS7Item == self.m_BeneCrystal:
            return None
        self.UnEquipS7ItemByID(iS7Item)
        oS7Item = None
        if iS7Item in self.m_Module:
            oS7Item = self.m_Module[iS7Item]
            if oS7Item.m_Point:
                self.DecreaseModules([
                    (iS7Item, oS7Item.m_Point)])
            oS7Item = self.m_Module.pop(iS7Item)
            iSubMsg = S7MODULE_REMOVE
            dMsgInfo = {
                'S7Item': iS7Item,
                'ModuleSID': oS7Item.m_SID,
                'Drop': iDrop }
        elif iS7Item in self.m_Crystal:
            oS7Item = self.m_Crystal.pop(iS7Item)
            iSubMsg = S7CRYSTAL_REMOVE
            dMsgInfo = {
                'S7Item': iS7Item,
                'CrystalSID': oS7Item.m_SID,
                'Drop': iDrop }
        if not oS7Item:
            SendAlert('err', '%d %d removes7item err %d %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iS7Item, self.m_Module, self.m_Crystal))
            return None
        self.GS2CRemoveS7Item(iS7Item)
        BackpackLog.Debug('%s %s removes7item %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oS7Item, sReason))
        if not iDrop:
            oS7Item.Release()
        else:
            oS7Item.RemoveFromContainer(sReason)
            oS7Item.m_Source = oOwner.m_PlayerID
            cl_drop.DropItem(oOwner, oS7Item, bFly = True)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.GetOwner(), dMsgInfo, iSub = iSubMsg)

    
    def GetPos(self, iS7Item):
        if iS7Item not in self.m_Item2Pos:
            return BACKPACKCON_EMPTY_POS
        return self.m_Item2Pos[iS7Item]

    
    def SetPos(self, iS7Item, x, y):
        tNewPos = (x, y)
        if not self.ValidEquip(x, y) and tNewPos != BACKPACKCON_EMPTY_POS:
            return None
        if not self.HandleModuleEquipNum(iS7Item, tNewPos):
            return None
        tOldPos = self.m_Item2Pos.get(iS7Item, BACKPACKCON_EMPTY_POS)
        self.m_EquipMap.pop(tOldPos, None)
        self.m_Item2Pos.pop(iS7Item, None)
        if tNewPos != BACKPACKCON_EMPTY_POS:
            self.m_EquipMap[tNewPos] = iS7Item
            self.m_Item2Pos[iS7Item] = tNewPos

    
    def HandleModuleEquipNum(self, iS7Item, tPos):
        oModule = self.GetModule(iS7Item)
        if not oModule:
            return 1
        iModuleSID = oModule.m_SID
        iEquipNum = self.m_ModuleEquipNum[iModuleSID] if iModuleSID in self.m_ModuleEquipNum else 0
        if tPos != BACKPACKCON_EMPTY_POS:
            if iEquipNum >= oModule.m_EquipNumMax:
                return 0
            self.m_ModuleEquipNum[iModuleSID] = iEquipNum + 1
        else:
            self.m_ModuleEquipNum[iModuleSID] = iEquipNum - 1
        return 1

    
    def IsEquip(self, iS7Item):
        return iS7Item in self.m_Item2Pos

    
    def ValidPos(self, x, y):
        return (x, y) in self.m_PointMap

    
    def ValidEquip(self, x, y):
        if not self.ValidPos(x, y):
            return 0
        if x > self.m_UnlockColNum or y > self.m_UnlockRowNum:
            return 0
        return 1

    
    def EquipS7Item(self, x, y, iS7Item, iSync = 1):
        (iOldX, iOldY) = self.GetPos(iS7Item)
        if iOldX == x and iOldY == y:
            return None
        if not self.ValidEquip(x, y):
            return None
        iNewPosS7Item = 0
        if (x, y) in self.m_EquipMap:
            iNewPosS7Item = self.m_EquipMap[(x, y)]
            self.UnEquipS7Item(x, y, iSync = iSync)
        if (iOldX, iOldY) in self.m_EquipMap:
            self.UnEquipS7ItemByID(iS7Item, iSync = iSync)
        self.SimpleEquipS7Item(x, y, iS7Item, iSync = iSync)
        if self.ValidEquip(iOldX, iOldY):
            self.SimpleEquipS7Item(iOldX, iOldY, iNewPosS7Item, iSync = iSync)

    
    def SimpleEquipS7Item(self, x, y, iS7Item, iSync):
        if (x, y) in self.m_EquipMap or iS7Item in self.m_Item2Pos or not self.ValidEquip(x, y):
            SendAlert('err', '%s %s simpleequips7item err %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, (x, y), iS7Item, self.m_EquipMap, self.m_Item2Pos))
            return False
        oS7Item = self.GetItemByID(iS7Item)
        if not oS7Item:
            return False
        self.SetPos(iS7Item, x, y)
        if iSync and oS7Item.m_Type == MODULE_MASK and oS7Item.m_SID == S7_SIMULATE_MODULE_SID:
            iNeedEnableType = NOW_ENABLE_MODULE
        else:
            iNeedEnableType = DELAY_ENABLE_MODULE
        self.RefreshS7Item(oS7Item, iEffPoint = 1, iUnEffPoint = 0, iSync = iSync, iNeedEnableModule = iNeedEnableType, lstSyncAttr = [
            'Pos'])
        BackpackLog.Debug('%s %s equips7item %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oS7Item, x, y))
        return True

    
    def UnEquipS7Item(self, x, y, iS7Item = 0, iSync = 1):
        if (x, y) not in self.m_EquipMap:
            return False
        iTrueS7Item = self.m_EquipMap[(x, y)]
        if iS7Item and iS7Item != iTrueS7Item:
            return False
        oS7Item = self.GetItemByID(iTrueS7Item)
        if not oS7Item:
            return False
        self.SetPos(iTrueS7Item, *BACKPACKCON_EMPTY_POS)
        if oS7Item.m_Type == MODULE_MASK and oS7Item.m_SID == S7_SIMULATE_MODULE_SID:
            iNeedEnableType = NOW_ENABLE_MODULE
        else:
            iNeedEnableType = DELAY_ENABLE_MODULE
        self.RefreshS7Item(oS7Item, iEffPoint = 0, iUnEffPoint = 1, iSync = iSync, iNeedEnableModule = iNeedEnableType, lstSyncAttr = [
            'Pos'])
        BackpackLog.Debug('%s %s unequips7item %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oS7Item, x, y))
        return True

    
    def UnEquipS7ItemByID(self, iS7Item, iSync = 1):
        tPos = self.GetPos(iS7Item)
        return self.UnEquipS7Item(*tPos, iS7Item, **{
            'iSync': iSync })

    
    def RotateCrystal(self, iCrystal, iRotate = 1):
        oCrystal = self.GetCrystal(iCrystal)
        if not oCrystal:
            return None
        oCrystal.Rotate(iRotate)
        self.RefreshS7Item(oCrystal, iEffPoint = 1, iUnEffPoint = 1, iSync = 1, iNeedEnableModule = DELAY_ENABLE_MODULE, lstSyncAttr = [
            'EffGrid'])

    
    def EffectCrystalPoint(self, iCrystal, iSync = 1):
        oCrystal = self.GetCrystal(iCrystal)
        if not oCrystal:
            return None
        if iCrystal in self.m_CrystalEffInfo:
            return None
        (x, y) = self.GetPos(iCrystal)
        if not self.ValidEquip(x, y):
            return None
        dEffGridInfo = { }
        self.m_CrystalEffInfo[iCrystal] = dEffGridInfo
        dPointAddInfo = oCrystal.GetPointInfo()
        dChangePoint = { }
        for (iOffsetX, iOffsetY), iPoint in dPointAddInfo.items():
            iEffX = x + iOffsetX
            iEffY = y + iOffsetY
            if not self.ValidPos(iEffX, iEffY):
                continue
            self.m_PointMap[(iEffX, iEffY)] += iPoint
            dEffGridInfo[(iEffX, iEffY)] = iPoint
            dChangePoint[(iEffX, iEffY)] = self.m_PointMap[(iEffX, iEffY)]
        
        if iSync:
            self.GS2CRefreshPosPoint(dChangePoint)

    
    def UnEffectCrystalPoint(self, iCrystal, iSync = 1):
        oCrystal = self.GetCrystal(iCrystal)
        if not oCrystal:
            return None
        if iCrystal not in self.m_CrystalEffInfo:
            return None
        dEffGridInfo = self.m_CrystalEffInfo[iCrystal]
        dChangePoint = { }
        for (iEffX, iEffY), iPoint in dEffGridInfo.items():
            if not self.ValidPos(iEffX, iEffY):
                continue
            self.m_PointMap[(iEffX, iEffY)] -= iPoint
            dChangePoint[(iEffX, iEffY)] = self.m_PointMap[(iEffX, iEffY)]
        
        self.m_CrystalEffInfo.pop(iCrystal, None)
        if iSync:
            self.GS2CRefreshPosPoint(dChangePoint)

    
    def AllPerformDisable(self, iNotify = 0):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        for dPerform in dict(self.m_Perform).values():
            for _, oPerform in list(dPerform.values()):
                if oPerform.m_ID == self.m_SimulateInfo[-1]:
                    continue
                oPerform.Disable(oOwner)
                oPerform.Release()
            
        
        self.m_Perform = { }
        self.DisableSpecialPassive()

    
    def AllPerformEnable(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.GetOwner(), { }, iSub = S7_MODULE_POINT_CHANGE)
        if not self.m_NeedEnableModule:
            return None
        self.m_NeedEnableModule = 0
        (setNeedDisablePf, setNeedEnablePf) = self.GetNeedEnableAndDisablePf()
        if not setNeedEnablePf and not setNeedDisablePf:
            return None
        for iModule, iPerform, iLv in setNeedDisablePf:
            if iModule not in self.m_Perform or iPerform not in self.m_Perform[iModule]:
                continue
            dModulePf = self.m_Perform[iModule]
            (_, oPf) = dModulePf[iPerform]
            oPf.Disable(oOwner)
            oPf.Release()
            dModulePf.pop(iPerform, 0)
            if not dModulePf:
                self.m_Perform.pop(iModule, 0)
        
        for iModule, iPerform, iLv in setNeedEnablePf:
            dModulePf = self.m_Perform.setdefault(iModule, { })
            if iPerform in dModulePf:
                BackpackLog.TraceAlert('%s %s repeat enable %s' % (self.m_Game.m_ID, self.m_PlayerID, iPerform))
                continue
            oPerform = oOwner.m_Game.m_ResMgr.NewPerform(iPerform, oOwner, iLv)
            if not oPerform:
                continue
            oPerform.m_Item = iModule
            dModulePf[iPerform] = (iLv, oPerform)
            oPerform.Enable(oOwner)
        
        self.EnableSpecialPassive()
        BackpackLog.Debug('%s %s enableperform %s %s' % (self.m_Game.m_ID, self.m_PlayerID, setNeedDisablePf, setNeedEnablePf))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.GetOwner(), { }, iSub = S7_ALL_PERFORM_ENABLE)

    
    def GetNeedEnableAndDisablePf(self):
        setOldPerform = set()
        for iModule, dPerform in self.m_Perform.items():
            for iPerform, (iLv, oPerform) in dPerform.items():
                if oPerform.m_ID == self.m_SimulateInfo[-1]:
                    continue
                setOldPerform.add((iModule, iPerform, iLv))
            
        
        lstAIMoudleWhite = self.GetAIMoudleWhite()
        setCurPerform = set()
        for oModule in self.CustomGetModule(iCheckEquip = EQUIP_STATUS):
            if lstAIMoudleWhite and oModule.m_SID not in lstAIMoudleWhite:
                continue
            iModule = oModule.m_ID
            iPoint = self.GetModulePoint(iModule)
            dAbility = oModule.GetAbilityByPoint(iPoint)
            for iPerform, iLv in dAbility.items():
                setCurPerform.add((iModule, iPerform, iLv))
            
        
        return (setOldPerform - setCurPerform, setCurPerform - setOldPerform)

    
    def GetAIMoudleWhite(self):
        oWarMgr = self.m_Game.m_WarMgr
        lstAIMoudleWhite = []
        if oWarMgr.IsAIHero(self.m_Owner):
            oBackpackElement = oWarMgr.GetBackpackElement()
            if oBackpackElement:
                lstAIMoudleWhite = oBackpackElement.GetAIMoudleWhite()
        return lstAIMoudleWhite

    
    def LockCrystal(self, iS7Item, iLock):
        oS7Item = self.GetItemByID(iS7Item)
        if not oS7Item:
            BackpackLog.Alert('%s %s lock crystal err  %s' % (self.m_Game, self.m_Owner, iS7Item))
            return None
        oS7Item.Set('Lock', iLock)
        self.GS2CRefreshItemAttr(iS7Item, [
            'Lock'])

    
    def GS2CAddCrystal(self, oCrystal, dPlayer = None, dExtInfo = None):
        if not oCrystal:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if not dPlayer:
            dPlayer = self.GetPlayers()
        seasonplaynet.GS2CAddS7Crystal(oOwner, oCrystal, dPlayer, dExtInfo)

    
    def GS2CAddModule(self, oModule, dPlayer = None, dExtInfo = None):
        if not oModule:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if not dPlayer:
            dPlayer = self.GetPlayers()
        if dExtInfo is None:
            dExtInfo = { }
        dExtInfo['DefaultPoint'] = oModule.m_DefaultPoint
        seasonplaynet.GS2CAddS7Module(oOwner, oModule, dPlayer, dExtInfo)

    
    def GS2CRemoveS7Item(self, iS7Item):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        lstPlayers = self.GetPlayers()
        seasonplaynet.GS2CRemoveS7Item(oOwner, iS7Item, lstPlayers)

    
    def GS2CRefreshPosPoint(self, dPointMap = None, dPlayer = None):
        if not dPointMap:
            dPointMap = self.m_PointMap
        lstPosPoint = []
        for (x, y), _ in dPointMap.items():
            iExtraFlag = 1 if self.ValidEquip(x, y) or (x, y) in self.m_ExtraPoint else 0
            lstPosPoint.append([
                x,
                y,
                self.GetPosPoint(x, y),
                iExtraFlag])
        
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if not dPlayer:
            dPlayer = self.GetPlayers()
        seasonplaynet.GS2CRefreshPosPoint(oOwner, lstPosPoint, dPlayer)

    
    def GS2CBackpackConInfo(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        dLockPos = self.GetLockPos()
        lstLockPos = [ (x, y, iIsNextUnlock) for (x, y), iIsNextUnlock in dLockPos.items() ]
        seasonplaynet.GS2CBackpackConInfo(oOwner, self.m_RowNum, self.m_ColNum, lstLockPos, {
            oOwner.m_PlayerID: 1 })

    
    def GS2CS7SignItem(self):
        seasonplaynet.GS2CS7InWarSignInfo(self.m_PlayerID, self.m_SignModuleInfo)

    
    def ComCrystal(self, iMainCrystalID, lCostCrystalID):
        dCrystal = self.m_Crystal
        oGameID = self.m_Game.m_ID
        iPlayerID = self.m_PlayerID
        iTotalAddPoint = 0
        if iMainCrystalID not in dCrystal or all((iCostCrystalID == 0 for iCostCrystalID in lCostCrystalID)):
            BackpackLog.Alert('%s %s com crystal err %s %s' % (oGameID, iPlayerID, iMainCrystalID, iMainCrystalID in dCrystal))
            return None
        oMainCrystal = dCrystal[iMainCrystalID]
        if oMainCrystal.IsFull():
            BackpackLog.Alert('%s %s main crystal is full %s ' % (oGameID, iPlayerID, iMainCrystalID))
            return None
        for iCostCrystalID in lCostCrystalID:
            if not iCostCrystalID:
                continue
            iTotalAddPoint += self._ComCrystal(dCrystal, oGameID, iPlayerID, iMainCrystalID, iCostCrystalID)
        
        if not iTotalAddPoint:
            BackpackLog.Alert('%s %s total add point is zero %s %s' % (oGameID, iPlayerID, iMainCrystalID, str(lCostCrystalID)))
            return None
        seasonplaynet.GS2CCComCrystalResult(self.m_PlayerID, iMainCrystalID, iTotalAddPoint)

    
    def _ComCrystal(self, dCrystal, oGameID, iPlayerID, iMainCrystalID, iCostCrystalID):
        oMainCrystal = dCrystal[iMainCrystalID]
        if oMainCrystal.IsFull():
            BackpackLog.Info('%s %s main crystal is full 2 %s ' % (oGameID, iPlayerID, iMainCrystalID))
            return 0
        iMainCrystalSID = oMainCrystal.m_SID
        oCostCrystal = dCrystal[iCostCrystalID]
        iCostCrystalSID = oCostCrystal.m_SID
        lstCanAddPointGrid = oMainCrystal.GetCanAddPointGrid()
        iCostPoint = oCostCrystal.GetNowTotalPoint()
        dCostPoint = GetS7CostPoint(iCostPoint)
        if not dCostPoint:
            BackpackLog.Alert('%s %s not cost point %s' % (oGameID, iPlayerID, iCostPoint))
            return 0
        iAddPoint = ChooseKey(self.m_Game, dCostPoint)
        self.RemoveS7Item(iCostCrystalID, 'ComCrystal')
        if iMainCrystalID not in dCrystal:
            BackpackLog.Alert('%s %s not main crystal %s %s' % (oGameID, iPlayerID, iMainCrystalSID, iCostCrystalSID))
            return 0
        self.AddCrystalPoint(iMainCrystalID, iAddPoint, lstCanAddPointGrid)
        BackpackLog.Info('%s %s com crystal %s %s %s' % (oGameID, iPlayerID, iMainCrystalSID, iCostCrystalSID, iAddPoint))
        return iAddPoint

    
    def AddCrystalPoint(self, iCrystalID, iPoint, lstGrid, iRandomDir = 0):
        dCrystal = self.m_Crystal
        if iCrystalID not in dCrystal:
            BackpackLog.Alert('%s %s not crystal %s' % (self.m_Game.m_ID, self.m_PlayerID, iCrystalID))
            return None
        oCrystal = dCrystal[iCrystalID]
        if not oCrystal:
            return None
        if iRandomDir:
            lstGrid = oCrystal.GetCanAddPointGrid()
        oCrystal.AddPoint(iPoint, lstGrid)
        self.RefreshS7Item(oCrystal, iEffPoint = 1, iUnEffPoint = 1, iSync = 1, iNeedEnableModule = NOW_ENABLE_MODULE, lstSyncAttr = [
            'EffGrid'])

    
    def AddCrystalExtPoint(self, sKey, iCrystalID, iPoint, iMaxPoint):
        dCrystal = self.m_Crystal
        if iCrystalID and iCrystalID not in dCrystal:
            BackpackLog.Alert('%s %s not crystal2 %s' % (self.m_Game.m_ID, self.m_PlayerID, iCrystalID))
            return None
        if iCrystalID:
            lstCrystal = [
                dCrystal[iCrystalID]]
        else:
            lstCrystal = list(dCrystal.values())
        for oCrystal in lstCrystal:
            if not oCrystal:
                continue
            lstGrid = oCrystal.GetCanAddPointGrid(iMaxPoint)
            if not lstGrid:
                continue
            oCrystal.AddExtPoint(sKey, iPoint, lstGrid, iMaxPoint)
            self.RefreshS7Item(oCrystal, iEffPoint = 1, iUnEffPoint = 1, iSync = 1, iNeedEnableModule = NOW_ENABLE_MODULE, lstSyncAttr = [
                'EffGrid'])
        

    
    def ClearExtPoint(self, sKey, iCrystalID, iRemove):
        dCrystal = self.m_Crystal
        if iCrystalID and iCrystalID not in dCrystal:
            BackpackLog.Alert('%s %s not crystal3 %s' % (self.m_Game.m_ID, self.m_PlayerID, iCrystalID))
            return None
        if iCrystalID:
            lstCrystal = [
                dCrystal[iCrystalID]]
        else:
            lstCrystal = list(dCrystal.values())
        for oCrystal in lstCrystal:
            if not oCrystal:
                continue
            oCrystal.ClearExtPoint(sKey, iRemove)
            self.RefreshS7Item(oCrystal, iEffPoint = 1, iUnEffPoint = 1, iSync = 1, iNeedEnableModule = NOW_ENABLE_MODULE, lstSyncAttr = [
                'EffGrid'])
        

    
    def ReEnableExtPointEffect(self, sKey, iCrystalID):
        dCrystal = self.m_Crystal
        if iCrystalID not in dCrystal:
            BackpackLog.Alert('%s %s not crystal4 %s' % (self.m_Game.m_ID, self.m_PlayerID, iCrystalID))
            return None
        oCrystal = dCrystal[iCrystalID]
        if not oCrystal:
            return None
        oCrystal.ReEnableExtPointEffect(sKey)
        self.RefreshS7Item(oCrystal, iEffPoint = 1, iUnEffPoint = 1, iSync = 1, iNeedEnableModule = NOW_ENABLE_MODULE, lstSyncAttr = [
            'EffGrid'])

    
    def GetRawMaterialCrystalAndPoint(self):
        iCrystalAddPoint = 0
        lstRawMaterialCrystal = []
        for iCrystal, oCrystal in self.m_Crystal.items():
            if not oCrystal:
                BackpackLog.Alert('%s %s rawmaterial nocrystal %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iCrystal, self.m_Crystal))
                continue
            iCrystalType = GetS7CrystalType(oCrystal.m_SID)
            if iCrystalType == CRTSTAL_RAWMATERIAL:
                iCrystalAddPoint += ENHANCEMODULE_ADD_POINT
                lstRawMaterialCrystal.append(iCrystal)
        
        return (lstRawMaterialCrystal, iCrystalAddPoint)

    
    def EnhanceModule(self, iModule, iAddPoint, iOp):
        oModule = self.GetModule(iModule)
        if not oModule:
            return None
        oModule.AddPoint(iAddPoint)
        dMsgInfo = {
            'AddPoint': iAddPoint }
        if iOp == ENHANCEMODULE:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.GetOwner(), dMsgInfo, iSub = S7MODULE_ENHANCE)
        elif iOp == AUTO_ENHANCEMODULE:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.GetOwner(), dMsgInfo, iSub = S7MODULE_AUTOENHANCE)
        BackpackLog.Debug('%s %s enhancemodule %s %d %d' % (self.m_Game.m_ID, self.m_PlayerID, oModule, iAddPoint, oModule.m_Point))
        self.RefreshS7Item(oModule, iEffPoint = 0, iUnEffPoint = 0, iSync = 1, iNeedEnableModule = DELAY_ENABLE_MODULE, lstSyncAttr = [
            'Point'])

    
    def EnhanceModules(self, lstItem, iOp):
        iTotalNum = 0
        for _, iNum in lstItem:
            iTotalNum += iNum
        
        (lstRawMaterialCrystal, iTotalAddPoint) = self.GetRawMaterialCrystalAndPoint()
        oGame = self.m_Game
        iPlayerID = self.m_PlayerID
        if iTotalNum > iTotalAddPoint:
            BackpackLog.Debug('%s %s erraddpoint %s %s' % (oGame.m_ID, iPlayerID, iTotalNum, iTotalAddPoint))
            return None
        for iModule, iNum in lstItem:
            oModule = self.GetModule(iModule)
            if not oModule:
                return None
        
        for iModule, iNum in lstItem:
            iCrystalNum = iNum // ENHANCEMODULE_ADD_POINT
            lstCostCrystal = list(lstRawMaterialCrystal)
            for iCrystal in lstCostCrystal:
                if iCrystalNum <= 0:
                    break
                iCrystalNum -= 1
                lstRawMaterialCrystal.remove(iCrystal)
                self.RemoveS7Item(iCrystal, sReason = 'enhancemodule')
            
            self.EnhanceModule(iModule, iNum, iOp)
        
        if iOp == AUTO_ENHANCEMODULE:
            cl_notify.SendCommonNotify(oGame, {
                iPlayerID: 1 }, ENHANCEMODULE_COMMONNOTIFY, { })

    
    def AutoEnhanceModules(self):
        (_, iTotalAddPoint) = self.GetRawMaterialCrystalAndPoint()
        if not iTotalAddPoint:
            return None
        lstModules = []
        for iItem in self.m_EquipMap.values():
            oModule = self.GetModule(iItem)
            if not oModule:
                continue
            iLackPoint = oModule.GetPointMax() - self.GetModulePoint(iItem)
            if iLackPoint <= 0:
                continue
            iAddPoint = min(iLackPoint, iTotalAddPoint)
            iTotalAddPoint -= iAddPoint
            lstModules.append((iItem, iAddPoint))
            if not iTotalAddPoint:
                break
        
        self.EnhanceModules(lstModules, AUTO_ENHANCEMODULE)

    
    def ValidDecreaseModules(self, lstItem):
        for iModule, iNum in lstItem:
            oModule = self.GetModule(iModule)
            if not oModule:
                BackpackLog.Debug('%d %d no decreasemodule %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iModule, self.m_Module))
                return 0
            if oModule.m_Point < iNum:
                BackpackLog.Debug('%d %d %d no enoughpoint %d %d' % (self.m_Game.m_ID, self.m_PlayerID, iModule, oModule.m_Point, iNum))
                return 0
        
        return 1

    
    def DecreaseModules(self, lstItem):
        if not self.ValidDecreaseModules(lstItem):
            return None
        for iModule, iNum in lstItem:
            oModule = self.GetModule(iModule)
            oModule.SubPoint(iNum)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.GetOwner(), {
                'SubPoint': iNum }, iSub = S7MODULE_DECREASE)
            iCrystalNum = iNum // ENHANCEMODULE_ADD_POINT
            for _ in range(iCrystalNum):
                clsCrystalData = clseason7.GetCrystalPerformCls(CRYSTAL_RAWMATERIAL_SID)
                iChoosePoint = ChooseKey(self.m_Game, clsCrystalData.m_CanChoosePoint)
                dData = {
                    'SID': CRYSTAL_RAWMATERIAL_SID,
                    'TP': iChoosePoint }
                oCrystal = clseason7.CreateCrystal(self.m_Game, oCrystalCon = self, dData = dData)
                if not oCrystal:
                    continue
                self.m_Crystal[oCrystal.m_ID] = oCrystal
                self.GS2CAddCrystal(oCrystal, dPlayer = None, dExtInfo = {
                    'NoShowNew': 1 })
            
            BackpackLog.Debug('%s %s decreasemodule %s %d %d' % (self.m_Game.m_ID, self.m_PlayerID, oModule, ENHANCEMODULE_ADD_POINT, oModule.m_Point))
            self.RefreshS7Item(oModule, iEffPoint = 0, iUnEffPoint = 0, iSync = 1, iNeedEnableModule = DELAY_ENABLE_MODULE, lstSyncAttr = [
                'Point'])
        

    
    def GetAllCanEquipPos(self, iCheckHasEquip = 0, iCheckPoint = 0):
        lstAllCanEquipPos = []
        for x in range(1, self.m_UnlockColNum + 1):
            for y in range(1, self.m_UnlockRowNum + 1):
                if iCheckHasEquip and (x, y) in self.m_EquipMap:
                    continue
                if iCheckPoint:
                    iPoint = self.GetPosPoint(x, y)
                    if (iCheckPoint == GET_EQUIP_POS_HASPOINT or not iPoint or iCheckPoint == GET_EQUIP_POS_HASNOTPOINT) and iPoint:
                        continue
                    continue
                lstAllCanEquipPos.append((x, y))
            
        
        return lstAllCanEquipPos

    
    def IsEffPoint(self, x, y):
        if not self.ValidEquip(x, y):
            return 0
        if (x, y) in self.m_EquipMap:
            iPosItem = self.m_EquipMap[(x, y)]
            if iPosItem in self.m_Crystal:
                return 0
        return 1

    
    def GetHighEffectRotate(self, iCrystal, x, y):
        oCrystal = self.GetCrystal(iCrystal)
        if not oCrystal:
            return 0
        iChooseRatate = 0
        (iMaxEffectPoint, iMaxSupplyModulePoint, iMaxSupplyGridPoint) = (0, 0, 0)
        for iRotate in range(oCrystal.m_RotateLimit):
            dPointAddInfo = oCrystal.GetEffPointByRotate(iRotate)
            (iCurEffectPoint, iCurSupplyModulePoint, iCurSupplyGridPoint) = (0, 0, 0)
            for (iOffsetX, iOffsetY), iPoint in dPointAddInfo.items():
                iEffX = x + iOffsetX
                iEffY = y + iOffsetY
                if not self.ValidPos(iEffX, iEffY):
                    continue
                if (iEffX, iEffY) not in self.m_EquipMap:
                    iCurEffectPoint += iPoint
                    iCurSupplyGridPoint += iPoint
                    continue
                iPosItem = self.m_EquipMap[(iEffX, iEffY)]
                if iPosItem in self.m_Module:
                    oModule = self.m_Module[iPosItem]
                    iMaxPoint = oModule.GetPointMax()
                    iCurPoint = self.GetModulePoint(iPosItem)
                    iAddPoint = min(iPoint, iMaxPoint - iCurPoint)
                    iCurEffectPoint += iAddPoint
                    iCurSupplyModulePoint += iAddPoint
            
            if (iCurEffectPoint, iCurSupplyModulePoint, iCurSupplyGridPoint) > (iMaxEffectPoint, iMaxSupplyModulePoint, iMaxSupplyGridPoint):
                iMaxEffectPoint = iCurEffectPoint
                iMaxSupplyModulePoint = iCurSupplyModulePoint
                iMaxSupplyGridPoint = iCurSupplyGridPoint
                iChooseRatate = iRotate
        
        return (iChooseRatate, (iMaxEffectPoint, iMaxSupplyModulePoint, iMaxSupplyGridPoint))

    
    def AutoEquipModule(self):
        iEquipNum = self.GetEquipModuleInfo(iCheckSID = 0, iCheckTag = 0, iGetNum = 1)
        if iEquipNum >= AUTOEQUIP_MAX_MODULE:
            return 0
        oGame = self.m_Game
        lstModule = self.CustomGetModule(iCheckEquip = UNEQUIP_STATUS, iCheckCanEquip = 1)
        lstModule = [ oModule for oModule in lstModule if oModule.Query('Lock') == 0 ]
        if not lstModule:
            return 0
        lstChooseModule = ShufferList(oGame, lstModule)
        lstChooseModule = sorted(lstChooseModule, key = (lambda oModule: oModule.GetPoint()), reverse = True)
        lstAllHasPointPos = self.GetAllCanEquipPos(iCheckHasEquip = 1, iCheckPoint = GET_EQUIP_POS_HASPOINT)
        iHasEquip = 0
        for x, y in sorted(lstAllHasPointPos, key = (lambda tPos: self.GetPosPoint(*tPos)), reverse = True):
            if not lstChooseModule:
                break
            oModule = lstChooseModule.pop(0)
            if self.SimpleEquipS7Item(x, y, oModule.m_ID, iSync = 1):
                iHasEquip = 1
        
        return iHasEquip

    
    def AutoEquipCrystal(self, iEquipNum, iEquipNotPointPos):
        oGame = self.m_Game
        lstCrystal = self.CustomGetCrystal(iCheckEquip = UNEQUIP_STATUS, iIgnoreType = CRTSTAL_RAWMATERIAL)
        lstChooseCrystal = sorted(lstCrystal, key = (lambda oCrystal: oCrystal.m_TotalPoint), reverse = True)
        lstChooseCrystal = [ oCrystal for oCrystal in lstChooseCrystal if oCrystal.Query('Lock') == 0 ]
        if iEquipNum:
            lstChooseCrystal = lstChooseCrystal[:iEquipNum]
        if not lstChooseCrystal:
            return 0
        iCheckPoint = GET_EQUIP_POS_HASNOTPOINT if iEquipNotPointPos else 0
        lstEquipPos = self.GetAllCanEquipPos(iCheckHasEquip = 1, iCheckPoint = iCheckPoint)
        dNearModuleNum = { }
        for x, y in lstEquipPos:
            iNearModuleNum = 0
            for iOffsetX, iOffsetY in NEAR_OFFSET:
                tNewX = x + iOffsetX
                tNewY = y + iOffsetY
                if (tNewX, tNewY) not in self.m_EquipMap:
                    continue
                iItem = self.m_EquipMap[(tNewX, tNewY)]
                oModule = self.GetModule(iItem)
                if not oModule:
                    continue
                iNearModuleNum += 1
            
            dNearModuleNum[(x, y)] = iNearModuleNum
        
        lstEquipPos = sorted(dNearModuleNum.keys(), key = (lambda tPos: dNearModuleNum[tPos]), reverse = True)
        if not lstEquipPos:
            return 0
        iHasEquip = 0
        for oChooseCrystal in lstChooseCrystal:
            if not lstEquipPos:
                break
            iChooseCrystal = oChooseCrystal.m_ID
            lstChoosePosAndRotate = []
            tMaxEffPoint = (-1, 0, 0)
            for x, y in lstEquipPos[:10]:
                (iRotate, tEffPoint) = self.GetHighEffectRotate(iChooseCrystal, x, y)
                if tEffPoint > tMaxEffPoint:
                    lstChoosePosAndRotate = [
                        ((x, y), iRotate)]
                    tMaxEffPoint = tEffPoint
                    continue
                if tEffPoint == tMaxEffPoint:
                    lstChoosePosAndRotate.append(((x, y), iRotate))
            
            if lstChoosePosAndRotate:
                iRandIdx = oGame.Random(len(lstChoosePosAndRotate))
                (tChoosePos, iChooseRotate) = lstChoosePosAndRotate[iRandIdx]
                lstEquipPos.remove(tChoosePos)
                self.RotateCrystal(iChooseCrystal, iChooseRotate)
                if self.SimpleEquipS7Item(*tChoosePos, iChooseCrystal, **{
                    'iSync': 1 }):
                    iHasEquip = 1
        
        return iHasEquip

    
    def AutoEquip(self):
        lstModule = self.CustomGetModule(iCheckEquip = UNEQUIP_STATUS, iCheckCanEquip = 1)
        lstCrystal = self.CustomGetCrystal(iCheckEquip = UNEQUIP_STATUS, iIgnoreType = CRTSTAL_RAWMATERIAL)
        if not lstModule and not lstCrystal:
            return None
        if not self.GetAllCanEquipPos(iCheckHasEquip = 1):
            return None
        (iCanEquipModule, iCanEquipCrystal) = (1, 1)
        for _ in range(10):
            if not iCanEquipModule and not iCanEquipCrystal:
                break
            iCanEquipModule = self.AutoEquipModule()
            iCanEquipCrystal = self.AutoEquipCrystal(iEquipNum = 1, iEquipNotPointPos = 1)
        
        self.AutoEquipCrystal(iEquipNum = 0, iEquipNotPointPos = 0)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.GetOwner(), { }, iSub = S7_AUTO_EQUIP)

    
    def AutoUnEquip(self):
        if not self.m_EquipMap:
            return None
        lstNeedUnEquip = []
        for tPos, iItemID in self.m_EquipMap.items():
            oItem = self.GetItemByID(iItemID)
            if not oItem.Query('Lock'):
                lstNeedUnEquip.append(tPos)
        
        for x, y in lstNeedUnEquip:
            self.UnEquipS7Item(x, y, iSync = 1)
        
        lstModule = []
        for iModule, oModule in self.m_Module.items():
            dModuleExtInfo = self.GetModuleExtInfo(oModule)
            if dModuleExtInfo['Lock']:
                continue
            lstModule.append((iModule, oModule.m_Point))
        
        self.DecreaseModules(lstModule)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.GetOwner(), { }, iSub = S7_AUTO_UNEQUIP)

    
    def SetUnLockModule(self, dModule):
        dAllS7Module = GetS7Module()
        for iModule, iUnLock in dModule.items():
            if not iUnLock or iModule not in dAllS7Module:
                continue
            self.m_UnLockModule[iModule] = iUnLock
        

    
    def SetUnLockCrystal(self, dCrystal):
        dAllS7Crystal = GetS7Crystal()
        for iCrystal, iUnLock in dCrystal.items():
            if not iUnLock or iCrystal not in dAllS7Crystal:
                continue
            self.m_UnLockCrystal[iCrystal] = iUnLock
        

    
    def GetUnLockModule(self):
        return self.m_UnLockModule

    
    def GetUnLockCrystal(self):
        return self.m_UnLockCrystal

    
    def GetMaxRowAndColNum(self):
        return (self.m_RowNum, self.m_ColNum)

    
    def RandomAddExtraPoint(self, sKey, iRandNum, iAddPoint):
        lstAllEquipPos = self.GetAllCanEquipPos()
        lstChoosePos = ChooseMulKeys(self.m_Game, dict.fromkeys(lstAllEquipPos, 1), iRandNum)
        return self.AddExtraPoint(sKey, dict.fromkeys(lstChoosePos, 1))

    
    def AddExtraPoint(self, sKey, dSetExtraPoint):
        dExtraPoint = { }
        for tPos, iAddPoint in dSetExtraPoint.items():
            if not self.ValidEquip(*tPos):
                return None
            dExtraPoint[tPos] = iAddPoint
        
        self.m_ExtraPointInfo[sKey] = dExtraPoint
        self.RefreshExtraPoint()
        return dExtraPoint

    
    def ClearExtraPoint(self, sKey):
        if sKey not in self.m_ExtraPointInfo:
            return None
        self.m_ExtraPointInfo.pop(sKey)
        self.RefreshExtraPoint()

    
    def RefreshExtraPoint(self):
        dNewExtraPoint = { }
        for dPoint in self.m_ExtraPointInfo.values():
            for tPos, iAddPoint in dPoint.items():
                if tPos not in dNewExtraPoint:
                    dNewExtraPoint[tPos] = 0
                dNewExtraPoint[tPos] += iAddPoint
            
        
        self.m_ExtraPoint = dNewExtraPoint
        self.GS2CRefreshPosPoint()
        self.AllPerformEnable()

    
    def GetModuleOverflowPoint(self, iModule):
        iPoint = self.GetModulePoint(iModule)
        oModule = self.GetModule(iModule)
        iMaxPoint = oModule.GetPointMax()
        if not iMaxPoint:
            return 0
        if iPoint <= iMaxPoint:
            return 0
        return iPoint - iMaxPoint

    
    def GetOverflowPoint(self):
        iOverflowPoint = 0
        for oModule in self.CustomGetModule(iCheckEquip = EQUIP_STATUS):
            iOverflowPoint += self.GetModuleOverflowPoint(oModule.m_ID)
        
        return iOverflowPoint

    
    def GetExclusionCrystal(self):
        dExclusionCrystal = { }
        for oCrystal in self.m_Crystal.values():
            iCrystalSID = oCrystal.m_SID
            dCurExclusion = GetExclusionCrystal(iCrystalSID)
            dExclusionCrystal.update(dCurExclusion)
        
        return dExclusionCrystal

    
    def GetDiffMaxPointModuleNum(self):
        setDiff = set()
        for iModule, oModule in self.m_Module.items():
            if not self.IsEquip(iModule):
                continue
            iPoint = self.GetModulePoint(iModule)
            iPointMax = oModule.GetPointMax()
            if iPointMax <= iPoint:
                setDiff.add(iPointMax)
        
        return len(setDiff)

    
    def GetEffectMaxPointModuleNum(self):
        iNum = 0
        for iModule, oModule in self.m_Module.items():
            iIsEquip = self.IsEquip(iModule)
            if not iIsEquip:
                continue
            iPoint = self.GetModulePoint(iModule)
            if oModule.GetPointMax() <= iPoint:
                iNum += 1
        
        return iNum

    
    def GetAllEquipModuleSIDAndPoint(self, iCheckExcludeOverflow = 1):
        lstModuleInfo = []
        for iModule, oModule in self.m_Module.items():
            if not self.IsEquip(iModule):
                continue
            iModuleSID = oModule.m_SID
            iPoint = self.GetModulePoint(iModule, iExcludeOverflow = iCheckExcludeOverflow)
            lstModuleInfo.append((iModuleSID, iPoint))
        
        return lstModuleInfo

    
    def GetAllEquipCrystalSIDAndPoint(self):
        lstCrystalInfo = []
        for iCrystal, oCrystal in self.m_Crystal.items():
            if not self.IsEquip(iCrystal):
                continue
            iCrystalSID = oCrystal.m_SID
            iPoint = oCrystal.GetNowTotalPoint()
            lstCrystalInfo.append((iCrystalSID, iPoint))
        
        return lstCrystalInfo

    
    def GetAllEquipModuleEnhancePoint(self):
        iAllEnhancePoint = 0
        for iModule, oModule in self.m_Module.items():
            if not self.IsEquip(iModule):
                continue
            iAllEnhancePoint += oModule.GetPoint()
        
        return iAllEnhancePoint

    
    def GetAllEquipCrystalPoint(self):
        iAllEquipPoint = 0
        for iCrystal, oCrystal in self.m_Crystal.items():
            if not self.IsEquip(iCrystal):
                continue
            iAllEquipPoint += oCrystal.GetNowTotalPoint()
        
        return iAllEquipPoint

    
    def GetEffPointAndUnEffPoint(self):
        iAllEquipPoint = self.GetAllEquipCrystalPoint() + self.GetAllEquipModuleEnhancePoint()
        iEffPoint = self.GetAllEquipModulePoint()
        oOwner = self.GetOwner()
        if oOwner and oOwner.m_BenedictionCon.HasBenediction(OVERCHARGE_BENE_SID):
            iOverflowPoint = self.GetOverflowPoint()
            return (iEffPoint, iAllEquipPoint - iEffPoint - iOverflowPoint)
        return (iEffPoint, iAllEquipPoint - iEffPoint)

    
    def GetLegalSignModuleInfo(self, dSignModule):
        if not dSignModule:
            return { }
        dResult = { }
        dLegalModule = GetS7Module()
        for iPos, iModuleSID in dSignModule.items():
            if iModuleSID not in dLegalModule:
                BackpackLog.Debug('%d %d illlegal signmodule %s' % (self.m_Game.m_ID, self.m_PlayerID, iModuleSID))
                continue
            dResult[iPos] = iModuleSID
        
        return dResult

    
    def UpdateSignModuleInfo(self, dSignModuleInfo):
        BackpackLog.Debug('%s %s signmodule %s' % (self.m_Game.m_ID, self.m_PlayerID, dSignModuleInfo))
        dLegalInfo = self.GetLegalSignModuleInfo(dSignModuleInfo)
        self.m_SignModuleInfo = dLegalInfo
        self.GS2CS7SignItem()

    
    def GetSimModule(self, iItem):
        return self.m_SimulateInfo[1]

    
    def EnableSimPerform(self, iModule, iTarModule, iPerform, iLv):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        dModulePf = self.m_Perform.setdefault(iModule, { })
        if iPerform in dModulePf:
            BackpackLog.Alert('%s %s repeat enable %s' % (self.m_Game.m_ID, self.m_PlayerID, iPerform))
            return None
        if self.m_SimulateInfo != (0, 0, 0):
            BackpackLog.Alert('%s %s repeat simulate %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iTarModule, iPerform, self.m_SimulateInfo))
            return None
        oPf = oOwner.m_Game.m_ResMgr.NewPerform(iPerform, oOwner, iLv)
        if not oPf:
            return None
        oPf.m_Item = iModule
        dModulePf[iPerform] = (iLv, oPf)
        oPf.Enable(oOwner)
        self.m_SimulateInfo = (iModule, iTarModule, oPf.m_ID)
        BackpackLog.Debug('%s %s enable perform %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iModule, iPerform, oPf.m_ID))
        self.GS2CRefreshItemAttr(iModule, [
            'Pos',
            'SimModule'])

    
    def DisableSimPerform(self, iModule, iPerform):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if iModule not in self.m_Perform or iPerform not in self.m_Perform[iModule]:
            return None
        dModulePf = self.m_Perform[iModule]
        (_, oPf) = dModulePf[iPerform]
        oPf.Disable(oOwner)
        oPf.Release()
        dModulePf.pop(iPerform, 0)
        self.m_SimulateInfo = (0, 0, 0)
        if not dModulePf:
            self.m_Perform.pop(iModule, 0)
        BackpackLog.Debug('%s %s disenable perform %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iModule, iPerform, oPf.m_ID))
        if oOwner.m_OnGame:
            self.GS2CRefreshItemAttr(iModule, [
                'Pos',
                'SimModule'])

    
    def ValidOpenSpecialPF(self):
        if not cllib.lib_flag.g_IsInternalRun:
            return False
        return True

    
    def SetSpecialPassive(self, iPassive):
        if not self.ValidOpenSpecialPF():
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oSpecialPassive = oOwner.m_Game.m_ResMgr.NewPerform(iPassive, oOwner, 1)
        if not oSpecialPassive:
            return None
        BackpackLog.Debug('%s %s set sp pf %s' % (self.m_Game.m_ID, self.m_PlayerID, iPassive))
        self.m_SpecialPassive = oSpecialPassive
        self.EnableSpecialPassive()

    
    def EnableSpecialPassive(self):
        if not self.ValidOpenSpecialPF():
            return None
        if not self.m_SpecialPassive:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        BackpackLog.Debug('%s %s enable sp pf' % (self.m_Game.m_ID, self.m_PlayerID))
        self.m_SpecialPassive.Enable(oOwner)

    
    def DisableSpecialPassive(self):
        if not self.ValidOpenSpecialPF():
            return None
        if not self.m_SpecialPassive:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        BackpackLog.Debug('%s %s disable sp pf' % (self.m_Game.m_ID, self.m_PlayerID))
        self.m_SpecialPassive.Disable(oOwner)

    
    def GetSpecialPassive(self):
        if not self.ValidOpenSpecialPF():
            return None
        return self.m_SpecialPassive


