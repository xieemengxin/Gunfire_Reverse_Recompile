# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/comperform.pyc
# RelativePath: clientlogic/cl_item/component/comperform.pyc
# Source Generated with Decompyle++
# File: comperform.pyc (Python 3.6)

from cl_only import GAME_FRAME_TIME
from cl_container.performcon import CEquipPerformContainer
from cl_commondefines import BAG_TYPE_WIELD, PF_SUBMSG_FILLBULLET, FORBID_SWITCHWEAPONATTPF
from .mobject import CItemComponent
import cl_item.defines as itemdef
import cl_msgcenter

class CPerformComponent(CItemComponent):
    
    def __init__(self, oItem, dParser):
        super(CPerformComponent, self).__init__(oItem, dParser)
        self.m_Perform = CEquipPerformContainer(self.m_Item)
        self.m_AllAttPerform = dParser['AttPerform'] if 'AttPerform' in dParser else { }
        self.m_AttPerformIdx = 0
        self.m_AttPerform = 0
        self.m_RepeatCnt = 0
        self.m_RepeatCold = 0
        self.m_FireCnt = 0
        self.m_TempFireCnt = 0
        self.m_HaltRepeatFrame = 0
        self.m_MinorPeform = dParser['MinorPerform'] if 'MinorPerform' in dParser else 0
        self.m_MinorRepeatCnt = dParser['MinorRepeatCnt'] if 'MinorRepeatCnt' in dParser else 0
        self.m_MinorRepeatCold = dParser['MinorRepeatCold'] if 'MinorRepeatCold' in dParser else 0
        self.m_MinorTempFireCnt = 0
        self.m_OpPerform = dParser['OpPerform'] if 'OpPerform' in dParser else 0
        self.m_TransEvt = { }
        self.m_Item.AddAttention(itemdef.MSG_ITEM_ADD, self.InitPerform, 'PerformCom')
        self.m_Item.AddAttention(itemdef.MSG_ITEM_HOLD, self.OnHold, 'PerformCom')
        self.m_Item.AddAttention(itemdef.MSG_ITEM_UNHOLD, self.OnUnHold, 'PerformCom')
        self.m_Item.AddAttention(itemdef.MSG_ITEM_REMOVE, self.DisableAllPerform, 'PerformCom')

    
    def Release(self):
        self.m_Perform.Release()
        super(CPerformComponent, self).Release()

    
    def Refresh(self):
        self.m_Perform.Refresh()

    
    def AddPerform(self, iPerform, iLevel, iEnable = 1, iAttPerformIdx = 255, iNotify = 0):
        oOwner = self.m_Item.GetOwner()
        return self.m_Perform.AddPerform(oOwner, iPerform, iLevel, iEnable, self.m_Item.m_ID, iAttPerformIdx, iNotify)

    
    def GetPerform(self, iPerform):
        return self.m_Perform.GetPerform(iPerform)

    
    def InitPerform(self, oItem, oWarrior):
        self.m_Perform.SetOwner(oWarrior)
        oCon = oItem.GetItemContainer()
        if oCon.m_BagType == BAG_TYPE_WIELD:
            for iIdx, (iPerform, iRepeatCnt, iRepeatCold, iElementType) in self.m_AllAttPerform.items():
                self.AddPerform(iPerform, 1, 0, iIdx)
                if iIdx == 0:
                    self.m_AttPerform = iPerform
                    self.m_RepeatCnt = iRepeatCnt
                    self.m_RepeatCold = iRepeatCold
                    if iElementType:
                        oItem.m_ElementTypeObj.SetModify('AttPerformIdx', iElementType)
            
            if self.m_MinorPeform:
                self.AddPerform(self.m_MinorPeform, 1, iEnable = 0)
            if self.m_OpPerform:
                self.AddPerform(self.m_OpPerform, 1, iEnable = 0)

    
    def GetAttPerformIdx(self):
        return self.m_AttPerformIdx

    
    def SetAttPerformIdx(self, iPerformIdx):
        self.m_AttPerformIdx = iPerformIdx
        self.m_Item.GS2CItemPropChange('AttPerformIdx', iPerformIdx)

    
    def SyncWeaponModeIdx(self, oWarrior):
        (iAttMode, iCliMode) = oWarrior.GetWeaponMode(self.m_Item.m_SID)
        if iAttMode != -1 and iAttMode != self.m_AttPerformIdx:
            self.SwitchAttPerform(oWarrior, iAttMode)
        if iCliMode != -1:
            self.m_Item.GS2CItemPropChange('CliModeIdx', iCliMode)

    
    def SwitchAttPerform(self, oWarrior, iPerformIdx):
        if oWarrior.IsForbid(FORBID_SWITCHWEAPONATTPF) or iPerformIdx not in self.m_AllAttPerform:
            return 0
        (iPerform, iRepeatCnt, iRepeatCold, iElementType) = self.m_AllAttPerform[iPerformIdx]
        if iPerform != self.m_AttPerform:
            oCurPerform = self.m_Perform.GetPerform(self.m_AttPerform)
            oCurPerform.Disable(oWarrior)
            oNewPerform = self.m_Perform.GetPerform(iPerform)
            oNewPerform.Enable(oWarrior)
            self.m_AttPerform = iPerform
        if iElementType:
            self.m_Item.m_ElementTypeObj.SetModify('AttPerformIdx', iElementType)
        self.m_RepeatCnt = iRepeatCnt
        self.m_RepeatCold = iRepeatCold
        self.SetAttPerformIdx(iPerformIdx)
        oWarrior.SaveWeaponAttMode(self.m_Item.m_SID, iPerformIdx)
        self.ClearFireCnt()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SWITCH_ATT_PERFORM, oWarrior, {
            'pfid': iPerform })
        return 1

    
    def SwitchNextAttPerform(self, oWarrior):
        iNextIdx = self.m_AttPerformIdx + 1
        if iNextIdx not in self.m_AllAttPerform:
            iNextIdx = 0
        self.SwitchAttPerform(oWarrior, iNextIdx)

    
    def ResetAttPerform(self, oWarrior):
        self.SwitchAttPerform(oWarrior, 0)

    
    def GetAllAttPerform(self):
        lstAll = []
        for iPerform, _, _, _ in self.m_AllAttPerform.values():
            if iPerform not in lstAll:
                lstAll.append(iPerform)
        
        return lstAll

    
    def GetAttPerform(self):
        return self.m_AttPerform

    
    def GetMinorPerform(self):
        return self.m_MinorPeform

    
    def AttrCache(self):
        dCache = {
            'MinorTempFireCnt': self.m_MinorTempFireCnt,
            'MinorRepeatCnt': self.m_MinorRepeatCnt,
            'TempFireCnt': self.m_TempFireCnt,
            'RepeatCnt': self.m_RepeatCnt,
            'FireCnt': self.m_FireCnt,
            'AttPerform': self.m_AttPerform,
            'MinorPerform': self.m_MinorPeform }
        return dCache

    
    def GetSteadyAttCD(self, iIsMinor = 0):
        if iIsMinor:
            self.m_MinorTempFireCnt += 1
            if self.m_MinorRepeatCnt > 1 and self.m_MinorTempFireCnt % self.m_MinorRepeatCnt != 0:
                return self.m_MinorRepeatCold
            return -1
        (_, iRepeatCnt, iRepeatCold) = self.m_Item.QueryTmp('RepeatInfo', ('', self.m_RepeatCnt, self.m_RepeatCold))
        self.m_FireCnt += 1
        self.m_TempFireCnt += 1
        if iRepeatCnt > 1 and self.m_TempFireCnt % iRepeatCnt != 0:
            return iRepeatCold
        return 100 * (10000 // self.m_Item.QueryAttr('AttSpeed') * GAME_FRAME_TIME)

    
    def GetSteadyAttCDNoFire(self, iIsMinor):
        if iIsMinor:
            if self.m_MinorRepeatCnt > 1 and self.m_MinorTempFireCnt % self.m_MinorRepeatCnt != 0:
                return self.m_MinorRepeatCold
            return -1
        (_, iRepeatCnt, iRepeatCold) = self.m_Item.QueryTmp('RepeatInfo', ('', self.m_RepeatCnt, self.m_RepeatCold))
        if iRepeatCnt > 1 and self.m_TempFireCnt % iRepeatCnt != 0:
            return iRepeatCold
        return 100 * (10000 // self.m_Item.QueryAttr('AttSpeed') * GAME_FRAME_TIME)

    
    def AddTransEvent(self, iMsgKey, func, sKey, iOnce = 1, iPriority = 0):
        if iMsgKey not in self.m_TransEvt:
            self.m_TransEvt[iMsgKey] = { }
        self.m_TransEvt[iMsgKey][sKey] = (func, iOnce, iPriority)

    
    def RemoveTransEvent(self, iMsgKey, sKey):
        if iMsgKey not in self.m_TransEvt:
            return None
        if sKey not in self.m_TransEvt[iMsgKey]:
            return None
        self.m_TransEvt[iMsgKey].pop(sKey)

    
    def OnHold(self, oItem, oWarrior):
        self.ClearFireCnt()
        self.m_Perform.AllPerformChangeEnableByHold(oItem.GetComponent('Hold').HoldPos())
        for iAttPerform in self.GetAllAttPerform():
            if iAttPerform != self.m_AttPerform:
                oPerform = self.m_Perform.GetPerform(iAttPerform)
                if not oPerform:
                    continue
                oPerform.Disable(oWarrior)
        
        self.SyncWeaponModeIdx(oWarrior)
        cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_PERFORM_START, FillBulletClearFireCnt, 'ClearFireCnt', PF_SUBMSG_FILLBULLET, 0)

    
    def OnUnHold(self, oItem, oWarrior):
        self.m_Perform.AllPerformChangeEnableByHold(iHoldPos = 0)
        cl_msgcenter.DoneEvent(oWarrior, cl_msgcenter.MSG_WAR_PERFORM_START, 'ClearFireCnt', PF_SUBMSG_FILLBULLET)

    
    def DisableAllPerform(self, oItem, oWarrior):
        oCon = oItem.GetItemContainer()
        if oCon and oCon.m_BagType == BAG_TYPE_WIELD:
            self.m_Perform.AllPerformDisable(iNotify = 1)
        self.m_AttPerformIdx = 0
        self.m_AttPerform = 0
        self.m_Perform.SetOwner(None)

    
    def ClearFireCnt(self):
        self.m_FireCnt = 0
        self.m_TempFireCnt = 0
        self.m_MinorTempFireCnt = 0

    
    def EventCache(self):
        return self.m_TransEvt

    
    def GetPerformSIDByType(self, iType):
        return self.m_Perform.GetPerformSIDByType(iType)

    
    def CheckRepeat(self):
        (_, iRepeatCnt, _) = self.m_Item.QueryTmp('RepeatInfo', ('', self.m_RepeatCnt, self.m_RepeatCold))
        if iRepeatCnt <= 1:
            return False
        return self.m_TempFireCnt % iRepeatCnt



def FillBulletClearFireCnt(oWarrior, dInfo):
    oSkill = dInfo['Skill']
    iWeapon = oSkill.m_Base['Weapon']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    oPerformCom.ClearFireCnt()

