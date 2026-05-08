# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/comenhance.pyc
# RelativePath: clientlogic/cl_item/component/comenhance.pyc
# Source Generated with Decompyle++
# File: comenhance.pyc (Python 3.6)

from cl_only import ChooseKey, DeepCopy, Functor
from cl_commondefines import BAG_TYPE_WIELD, ITEMPERFORM_ENABLE_HOLD, ITEMPERFORM_ENABLE_UNHOLD, ITEMPERFORM_ENABLE_MAINHOLD
from cl_perform.load import GetWeaponEnhanceLib
from cl_object.logging import WarrewardLog
from cl_item.defines import MAIN_HOLD
import cl_item.defines as itemdef
import cl_perform
import cl_netattr
from .mobject import CItemComponent
MAX_ENHANCE_NUM = 1

class CEnhanceComponent(CItemComponent):
    
    def __init__(self, oItem, dParser):
        super().__init__(oItem, dParser)
        self.m_Enhance = { }
        self.m_TempEnhance = []
        self.m_TempEnhanceInfo = { }
        self.m_Item.AddAttention(itemdef.MSG_ITEM_ADD, self.OnItemAddToContainer, 'EnhanceCom')
        self.m_Item.AddAttention(itemdef.MSG_ITEM_REMOVE, self.OnItemRemoveFromContainer, 'EnhanceCom')

    
    def Save(self):
        dData = { }
        dData['EH'] = DeepCopy(self.m_Enhance)
        dData['TEHI'] = DeepCopy(self.m_TempEnhanceInfo)
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        for iSID, dAttr in dData['EH'].items():
            self.m_Enhance[iSID] = dAttr
            self._ApplyEnhance(iSID)
        
        if 'TEHI' in dData:
            for sKey, tData in dData['TEHI'].items():
                self.m_TempEnhanceInfo[sKey] = tData
            

    
    def GetAllEnhanceSID(self):
        return list(self.m_Enhance.keys())

    
    def GetAllEnhance(self):
        lstReturn = []
        for iSID, dAttr in self.m_Enhance.items():
            lstTmp = [
                iSID]
            for sAttr, lstVal in dAttr.items():
                (idx, _, _, _, _) = cl_netattr.INFO_PROP_NAME[sAttr]
                lstTmp.append(idx)
                lstTmp.extend(lstVal)
            
            lstReturn.append(lstTmp)
        
        if not lstReturn:
            for _, tData in self.m_TempEnhanceInfo.items():
                (iSID, dAttr) = tData
                if iSID in self.m_TempEnhance:
                    lstTmp = [
                        iSID]
                    for sAttr, lstVal in dAttr.items():
                        (idx, _, _, _, _) = cl_netattr.INFO_PROP_NAME[sAttr]
                        lstTmp.append(idx)
                        lstTmp.extend(lstVal)
                    
                lstReturn.append(lstTmp)
            
        return lstReturn

    
    def TraceName(self):
        return (self.m_Enhance, self.m_TempEnhanceInfo)

    
    def AddEnhance(self, iNum, sReason, lstExcludeSID = None):
        if lstExcludeSID is None:
            lstExcludeSID = []
        oItem = self.m_Item
        iNum = min(iNum, MAX_ENHANCE_NUM - len(self.m_Enhance))
        dAll = GetWeaponEnhanceLib()
        dWeight = { }
        for iSID, iWeight in dAll.items():
            if iSID in self.m_Enhance:
                continue
            if iSID in lstExcludeSID:
                continue
            clsPerform = cl_perform.GetPerformModule(iSID)
            if not clsPerform or not clsPerform.CheckValidItem(oItem, self.m_Enhance):
                continue
            dWeight[iSID] = iWeight
        
        for _ in range(iNum):
            if not dWeight:
                WarrewardLog.Alert('%s %s no enhance %s' % (self.m_Item.m_SID, self.m_Enhance, sReason))
                break
            iSID = ChooseKey(self.m_Item.m_Game, dWeight)
            if not self.CanEnhance(iSID, sReason):
                break
            self._ApplyEnhance(iSID)
            dWeight.pop(iSID)
        
        self.m_Item.GS2CItemPropChange('Enhance', self.GetAllEnhance())

    
    def AddEnhanceBySID(self, iSID, sReason):
        dAll = GetWeaponEnhanceLib()
        if iSID not in dAll:
            return None
        if not self.CanEnhance(iSID, sReason):
            return None
        self._ApplyEnhance(iSID)
        self.m_Item.GS2CItemPropChange('Enhance', self.GetAllEnhance())

    
    def _ApplyEnhance(self, iSID):
        dAttr = self.m_Enhance.setdefault(iSID, { })
        dApplyAttr = self.ApplyEnhanceAttr('EnhanceCom', iSID, dAttr)
        self.m_Enhance[iSID] = dApplyAttr

    
    def DisableItemEnhance(self):
        for iSID in self.m_Enhance:
            dAllAttr = cl_perform.GetPerformClassAttr(iSID, 'm_EnhanceAttr')
            for sAttr in dict(dAllAttr):
                self.m_Item.AttrClear(sAttr, 'EnhanceCom%s' % iSID)
            
        

    
    def CanEnhance(self, iSID, sReason):
        if len(self.m_Enhance) >= MAX_ENHANCE_NUM:
            WarrewardLog.Alert('game:%d reason:%s %s %s %s max enhance' % (self.m_Item.m_Game.m_ID, sReason, self.m_Item.m_SID, self.m_Enhance, iSID))
            return False
        return True

    
    def EnablePerform(self, iSID):
        oItem = self.m_Item
        oPerformCom = oItem.GetComponent('Perform')
        if oPerformCom:
            pfobj = oPerformCom.GetPerform(iSID)
            if not pfobj:
                clsPerform = cl_perform.GetPerformModule(iSID)
                iItemEnableType = clsPerform.m_ItemEnableType
                oHoldComp = oItem.GetComponent('Hold')
                iHoldPos = oHoldComp.HoldPos()
                iEnable = 0
                if not iItemEnableType & ITEMPERFORM_ENABLE_HOLD or iHoldPos:
                    if (iItemEnableType & ITEMPERFORM_ENABLE_UNHOLD or not iHoldPos or iItemEnableType & ITEMPERFORM_ENABLE_MAINHOLD) and iHoldPos == MAIN_HOLD:
                        iEnable = 1
                None.AddPerform(iSID, 1, iEnable)

    
    def OnItemAddToContainer(self, oItem, oOwner):
        oCon = oItem.GetItemContainer()
        if oCon.m_BagType != BAG_TYPE_WIELD:
            return None
        for iSID in self.m_Enhance:
            self.EnablePerform(iSID)
        

    
    def OnItemRemoveFromContainer(self, oItem, oOwner):
        oTarget = self.m_Item
        oPerformCom = oTarget.GetComponent('Perform')
        for iSID in self.m_Enhance:
            oPerformCom.m_Perform.RemovePerform(oOwner, iSID)
        

    
    def RemoveEnhance(self, iNum):
        dEnhance = self.m_Enhance
        if len(dEnhance) < iNum:
            return []
        iRemovedCnt = 0
        lstEnhance = []
        for iSID in list(dEnhance.keys()):
            if iRemovedCnt >= iNum:
                break
            iRemovedCnt += 1
            dAttr = dEnhance.pop(iSID)
            lstEnhance.append(iSID)
            if not dAttr:
                continue
            sAttr = list(dAttr.keys())[0]
            self.m_Item.AttrClear(sAttr, 'EnhanceCom%s' % iSID)
        
        self.m_Item.GS2CItemPropChange('Enhance', self.GetAllEnhance())
        return lstEnhance

    
    def GetEnhanceNum(self):
        return len(self.m_Enhance)

    
    def AddTempEnhance(self, sKey, iMaxAttr = 0, lstExcludeSID = None):
        if self.m_Enhance or self.GetEnhanceNum() >= MAX_ENHANCE_NUM:
            return None
        if lstExcludeSID is None:
            lstExcludeSID = []
        oItem = self.m_Item
        if sKey not in self.m_TempEnhanceInfo:
            iSID = self.ChooseEnhance(sKey, lstExcludeSID)
            if not iSID:
                return None
            dAttr = { }
            self.m_TempEnhanceInfo[sKey] = (iSID, dAttr)
        self.ApplyTempEnhance(sKey, iMaxAttr)
        oItem.AddAttention(itemdef.MSG_ITEM_REMOVE, Functor(self.OnClearTempDisableEnhance, sKey), sKey)
        oItem.GS2CItemPropChange('Enhance', self.GetAllEnhance())

    
    def OnClearTempDisableEnhance(self, sKey, oItem, oOwner):
        self.ClearTempEnhance(sKey)
        oItem.DoneAttention(itemdef.MSG_ITEM_REMOVE, sKey)

    
    def ClearTempEnhance(self, sKey):
        if sKey not in self.m_TempEnhanceInfo:
            return None
        (iSID, dAttr) = self.m_TempEnhanceInfo[sKey]
        if not dAttr:
            return None
        if iSID in self.m_TempEnhance:
            self.m_TempEnhance.remove(iSID)
            sAttr = list(dAttr)[0]
            self.m_Item.AttrClear(sAttr, 'TempEnhance%s' % iSID)
            self.m_Item.GS2CItemPropChange('Enhance', self.GetAllEnhance())

    
    def ApplyTempEnhance(self, sKey, iMaxAttr = 0):
        (iSID, dAttr) = self.m_TempEnhanceInfo[sKey]
        if iSID not in self.m_TempEnhance:
            self.m_TempEnhance.append(iSID)
        dAttr = self.ApplyEnhanceAttr('TempEnhance', iSID, dAttr, iMaxAttr)
        self.m_TempEnhanceInfo[sKey] = (iSID, dAttr)

    
    def ChooseEnhance(self, sReason, lstExcludeSID = None):
        if lstExcludeSID is None:
            lstExcludeSID = []
        oItem = self.m_Item
        dAll = GetWeaponEnhanceLib()
        dWeight = { }
        for iSID, iWeight in dAll.items():
            if iSID in self.m_Enhance:
                continue
            if iSID in lstExcludeSID:
                continue
            clsPerform = cl_perform.GetPerformModule(iSID)
            if not clsPerform or not clsPerform.CheckValidItem(oItem, self.m_Enhance):
                continue
            dWeight[iSID] = iWeight
        
        if not dWeight:
            WarrewardLog.Alert('%s %s no enhance %s' % (self.m_Item.m_SID, self.m_Enhance, sReason))
            return None
        return ChooseKey(oItem.m_Game, dWeight)

    
    def ApplyEnhanceAttr(self, sKey, iSID, dAttr = None, iMaxAttr = 0):
        if dAttr is None:
            dAttr = { }
        oGame = self.m_Item.m_Game
        dAllAttr = cl_perform.GetPerformClassAttr(iSID, 'm_EnhanceAttr')
        for sAttr, (iMulMin, iMulMax, iAddMin, iAddMax) in dAllAttr.items():
            if sAttr in dAttr:
                (iMul, iAdd) = dAttr[sAttr]
            else:
                iMul = 0
                if iMulMin < iMulMax:
                    iMul = oGame.Random((iMulMax - iMulMin) + 1) + iMulMin
                    iMul = (iMul // 100) * 100
                iAdd = 0
                if iAddMin < iAddMax:
                    iAdd = oGame.Random((iAddMax - iAddMin) + 1) + iAddMin
                dAttr[sAttr] = (iMul, iAdd)
            if iMaxAttr:
                iMul = iMulMax
                iAdd = iAddMax
            self.m_Item.AttrChange(sAttr, iMul, iAdd, sKey + '%s' % iSID)
        
        return dAttr


