# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/s8con.pyc
# RelativePath: clientlogic/cl_container/s8con.pyc
# Source Generated with Decompyle++
# File: s8con.pyc (Python 3.6)

from cl_cscommondef import GEMITEM_MASK, THIRDITEM_MASK
from cl_container.mobject import CBaseSeasonContainer, CONFUNC_GET, ATTR_GET, QUERY_GET, FUNC_GET
from cl_object.logging import SeasoneightLog
from cl_only import SendAlert
from cl_seasonplay.season8 import GetS8GemItemDataCls, GetS8ThirdItemCls, CreateS8ThirdItem, CreateS8GemItem
from cl_commondefines import S8_THIRDITEM_ENABLE, S8_THIRDITEM_DISABLE, S8_THIRDITEM_REMOVE
import cl_seasonplay.net as seasonplaynet
import cl_msgcenter
GEM_COMBINE_NUM = 2
MAX_THIRD_QUALITY = 3
MAX_GEM_QUALITY = 3
g_ThirdActiveAttr = {
    'Radius': 1,
    'AddStateTime': 1 }

class CS8Container(CBaseSeasonContainer):
    m_SeasonNum = 8
    m_GemItemCanEquipNum = 6
    m_ItemAttr = {
        'Pos': CONFUNC_GET,
        'Energy': ATTR_GET,
        'MaxEnergy': QUERY_GET,
        'EnergyCost': QUERY_GET,
        'RecoverInterval': QUERY_GET,
        'RecoverValue': QUERY_GET,
        'AllTime': FUNC_GET,
        'RemainTime': FUNC_GET }
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_ThirdItem = { }
        self.m_GemItem = { }
        self.m_EquipThirdItem = 0
        self.m_EquipGemItem = { }
        self.m_EnablePassivePerform = { }
        self.m_ThirdGrooveAttr = { }
        self.Init()

    
    def Init(self):
        oGame = self.m_Game
        if not oGame:
            return None
        for iPos in range(1, self.m_GemItemCanEquipNum + 1):
            self.m_EquipGemItem[iPos] = 0
        

    
    def Release(self):
        for oPerform in list(self.m_EnablePassivePerform.values()):
            oPerform.Release()
        
        for oModule in list(self.m_ThirdItem.values()):
            oModule.Release()
        
        for oCrystal in list(self.m_GemItem.values()):
            oCrystal.Release()
        
        self.m_ThirdItem = { }
        self.m_GemItem = { }
        self.m_EquipGemItem = { }
        self.m_EnablePassivePerform = { }

    
    def Load(self, dData):
        if not dData:
            return None
        lstThirdItem = dData.get('TI', [])
        lstGemItem = dData.get('GI', [])
        self.LoadThirdItem(lstThirdItem)
        self.LoadGemItem(lstGemItem)

    
    def LoadThirdItem(self, lstThirdItem):
        oGame = self.m_Game
        for iEquip, dItem in lstThirdItem:
            iSID = dItem['SID']
            clsItem = GetS8ThirdItemCls(iSID)
            if not clsItem:
                continue
            oItem = clsItem.Load(oGame, dItem)
            self.AddThirdItem(oItem, sReason = 'load')
            if iEquip:
                self.EquipThirdItem(oItem.m_ID)
        

    
    def LoadGemItem(self, lstGemItem):
        oGame = self.m_Game
        for iPos, dItem in lstGemItem:
            iSID = dItem['SID']
            clsItem = GetS8GemItemDataCls(iSID)
            if not clsItem:
                continue
            oItem = clsItem.Load(oGame, dItem)
            self.AddGemItem(oItem, sReason = 'load')
            if iPos:
                self.EquipGemItem(oItem.m_ID, iPos)
        

    
    def Save(self):
        dData = { }
        lstThirdItem = []
        lstGemItem = []
        for oItem in self.m_ThirdItem.values():
            iEquip = 1 if oItem.m_ID == self.m_EquipThirdItem else 0
            lstThirdItem.append((iEquip, oItem.Save()))
        
        for oItem in self.m_GemItem.values():
            iPos = self.GetPos(oItem.m_ID)
            lstGemItem.append((iPos, oItem.Save()))
        
        dData['TI'] = lstThirdItem
        dData['GI'] = lstGemItem
        return dData

    
    def Refresh(self, dPlayer):
        for oThird in self.m_ThirdItem.values():
            self.GS2CAddS8ThirdItem(oThird, dPlayer)
        
        for oGem in self.m_GemItem.values():
            self.GS2CAddS8GemItem(oGem, dPlayer)
        

    
    def GetItemByID(self, iItem):
        if iItem in self.m_ThirdItem:
            return self.m_ThirdItem[iItem]
        if iItem in self.m_GemItem:
            return self.m_GemItem[iItem]

    
    def AllPerformDisable(self, iNotify = 0):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iEquipThirdItem = self.m_EquipThirdItem
        if iEquipThirdItem:
            self.DisableThirdItem(iEquipThirdItem)
        for iItem in list(self.m_EquipGemItem.values()):
            if not iItem:
                continue
            self.DisableGemItem(iItem)
        
        if self.m_EnablePassivePerform:
            SendAlert('err', '%d %d s8 allperformdisable err %s %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_EnablePassivePerform, self.m_EquipThirdItem, self.m_ThirdItem, self.m_EquipGemItem, self.m_GemItem))
            for oPerform in dict(self.m_EnablePassivePerform).values():
                oPerform.Disable(oOwner)
                oPerform.Release()
            
            self.m_EnablePassivePerform = { }

    
    def GetPerform(self, iPerformSID, iItem):
        tKey = (iPerformSID, iItem)
        if tKey not in self.m_EnablePassivePerform:
            return None
        return self.m_EnablePassivePerform[tKey]

    
    def GetPos(self, iItem):
        for iPos, iTmpItem in self.m_EquipGemItem.items():
            if iTmpItem == iItem:
                return iPos
        
        return 0

    
    def GetEquipThirdItem(self):
        iEquipThirdItem = self.m_EquipThirdItem
        if iEquipThirdItem in self.m_ThirdItem:
            return self.m_ThirdItem[iEquipThirdItem]

    
    def AddThirdItem(self, oItem, sReason):
        if not oItem:
            return None
        iItemID = oItem.m_ID
        iItemType = oItem.m_Type
        if iItemType != THIRDITEM_MASK:
            return None
        for iItem in list(self.m_ThirdItem.keys()):
            self.RemoveS8Item(iItem, iDrop = 1)
        
        SeasoneightLog.Debug('%s %s addthirditem %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oItem, sReason))
        self.m_ThirdItem[iItemID] = oItem
        oItem.AddToContainer(self)
        self.GS2CAddS8ThirdItem(oItem)
        self.EquipThirdItem(iItemID)

    
    def AddGemItem(self, oItem, sReason, iTryCombine = 1):
        if not oItem:
            return None
        iItemID = oItem.m_ID
        iItemType = oItem.m_Type
        if iItemType != GEMITEM_MASK:
            return None
        SeasoneightLog.Debug('%s %s addgemitem %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oItem, sReason))
        self.m_GemItem[iItemID] = oItem
        oItem.AddToContainer(self)
        self.GS2CAddS8GemItem(oItem)
        if iTryCombine:
            self.TryCombineGem(oItem)

    
    def TryCombineGem(self, oItem):
        iEquipPos = 0
        for _ in range(MAX_GEM_QUALITY - 1):
            if not oItem:
                break
            iQuality = oItem.m_Quality
            if iQuality >= MAX_GEM_QUALITY:
                break
            iSID = oItem.m_SID
            lstSameGem = []
            for iGemItem, oTmpItem in self.m_GemItem.items():
                if (oTmpItem.m_SID, oTmpItem.m_Quality) == (iSID, iQuality):
                    lstSameGem.append(iGemItem)
            
            if len(lstSameGem) < GEM_COMBINE_NUM:
                break
            for iGemItem in lstSameGem[:GEM_COMBINE_NUM]:
                iPos = self.GetPos(iGemItem)
                if iPos:
                    iEquipPos = min(iEquipPos, iPos) if iEquipPos else iPos
                self.RemoveS8Item(iGemItem)
            
            iNewQuality = iQuality + 1
            dGemData = {
                'SID': iSID,
                'QL': iNewQuality }
            oItem = self.RewardGemItem(dGemData, 'combine', iTryCombine = 0)
        
        if not oItem or not iEquipPos:
            return None
        self.EquipGemItem(oItem.m_ID, iEquipPos)

    
    def RewardThirdItem(self, dThirdData, sReason = ''):
        iSID = dThirdData.get('SID', 0)
        iQuality = dThirdData.get('QL', 0)
        oThirdItem = CreateS8ThirdItem(self.m_Game, iSID, iQuality, { })
        if not oThirdItem:
            SendAlert('err', '%s %s not third item %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iQuality, sReason))
            return None
        self.AddThirdItem(oThirdItem, sReason)
        return oThirdItem

    
    def RewardGemItem(self, dGemData, sReason = '', iTryCombine = 1):
        iSID = dGemData.get('SID', 0)
        iQuality = dGemData.get('QL', 0)
        oGemItem = CreateS8GemItem(self.m_Game, iSID, iQuality, { })
        if not oGemItem:
            SendAlert('err', '%s %s not gem item %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iQuality, sReason))
            return None
        self.AddGemItem(oGemItem, sReason, iTryCombine)
        return oGemItem

    
    def RemoveS8Item(self, iItem, iDrop = 0):
        oItem = None
        if iItem in self.m_ThirdItem:
            if self.CheckItemEquip(iItem, THIRDITEM_MASK):
                self.UnEquipThirdItem()
            oItem = self.m_ThirdItem.pop(iItem, 0)
        elif iItem in self.m_GemItem:
            if self.CheckItemEquip(iItem, GEMITEM_MASK):
                self.UnEquipGemItem(self.GetPos(iItem))
            oItem = self.m_GemItem.pop(iItem, 0)
        else:
            return None
        self.GS2CRemoveS8Item(iItem, self.GetPlayers())
        self.OnRemoveItem(oItem, iDrop)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, self.GetOwner(), { }, iSub = S8_THIRDITEM_REMOVE)

    
    def UnEquipThirdItem(self):
        iItem = self.m_EquipThirdItem
        if not iItem or not self.CheckItemEquip(iItem, THIRDITEM_MASK):
            return None
        self.DisableThirdItem(iItem)
        self.m_EquipThirdItem = 0

    
    def UnEquipGemItemByID(self, iItem):
        iPos = self.GetPos(iItem)
        if iPos:
            self.UnEquipGemItem(iPos)

    
    def UnEquipGemItem(self, iPos):
        if iPos not in self.m_EquipGemItem or not self.m_EquipGemItem[iPos]:
            return None
        iItem = self.m_EquipGemItem[iPos]
        if iItem not in self.m_GemItem:
            return None
        self.DisableGemItem(iItem)
        self.m_EquipGemItem[iPos] = 0
        self.GS2CRefreshItemAttr(iItem, [
            'Pos'])

    
    def EquipThirdItem(self, iItem):
        if not iItem or iItem not in self.m_ThirdItem or iItem == self.m_EquipThirdItem:
            SendAlert('err', '%d %d s8 equipthirditem err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iItem, self.m_EquipThirdItem, self.m_ThirdItem))
            return None
        self.UnEquipThirdItem()
        self.m_EquipThirdItem = iItem
        self.EnableThirdItem(iItem)

    
    def EquipGemItem(self, iItem, iPos):
        if not iItem or iItem not in self.m_GemItem or iPos not in self.m_EquipGemItem or self.m_EquipGemItem[iPos] == iItem:
            SendAlert('err', '%d %d s8 equipgemitem err %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iItem, iPos, self.m_EquipGemItem, self.m_GemItem))
            return None
        self.UnEquipGemItem(iPos)
        self.m_EquipGemItem[iPos] = iItem
        self.EnableGemItem(iItem)
        self.GS2CRefreshItemAttr(iItem, [
            'Pos'])

    
    def CheckItemEquip(self, iItem, iItemType):
        if iItemType == THIRDITEM_MASK:
            if iItem and iItem == self.m_EquipThirdItem:
                pass
            return iItem in self.m_ThirdItem
        if iItemType == GEMITEM_MASK:
            if iItem and iItem in self.m_EquipGemItem.values():
                pass
            return iItem in self.m_GemItem
        return 0

    
    def AddThirdGrooveAttr(self, sKey, sAttr, iMul, iAdd):
        tAttrKey = (sKey, sAttr)
        self.m_ThirdGrooveAttr[tAttrKey] = [
            iMul,
            iAdd]
        self.ThirdGrooveAttrChange(sKey, sAttr, iMul, iAdd)

    
    def ClearThirdGrooveAttr(self, sKey, sAttr):
        self.m_ThirdGrooveAttr.pop((sKey, sAttr), None)
        self.ThirdGrooveAttrClear(sKey, sAttr)

    
    def EnableAllThirdGrooveAttr(self):
        for (sKey, sAttr), (iMul, iAdd) in self.m_ThirdGrooveAttr.items():
            self.ThirdGrooveAttrChange(sKey, sAttr, iMul, iAdd)
        

    
    def DisableAllThirdGrooveAttr(self):
        for sKey, sAttr in self.m_ThirdGrooveAttr:
            self.ThirdGrooveAttrClear(sKey, sAttr)
        

    
    def ThirdGrooveAttrChange(self, sKey, sAttr, iMul, iAdd):
        oOwner = self.GetOwner()
        oEquipItem = self.GetEquipThirdItem()
        if not oOwner or not oEquipItem:
            return None
        if sAttr in g_ThirdActiveAttr:
            iActivePerform = oEquipItem.m_ActivePerform
            oActivePerform = oOwner.GetPerform(iActivePerform, oEquipItem.m_ID)
            if not oActivePerform or not oActivePerform.GetAttr(sAttr):
                return None
            oActivePerform.AttrChange(sAttr, sKey, iMul, iAdd)
        else:
            oEquipItem.AttrChange(sAttr, iMul, iAdd, sKey)

    
    def ThirdGrooveAttrClear(self, sKey, sAttr):
        oOwner = self.GetOwner()
        oEquipItem = self.GetEquipThirdItem()
        if not oOwner or not oEquipItem:
            return None
        if sAttr in g_ThirdActiveAttr:
            iActivePerform = oEquipItem.m_ActivePerform
            oActivePerform = oOwner.GetPerform(iActivePerform, oEquipItem.m_ID)
            if not oActivePerform or not oActivePerform.GetAttr(sAttr):
                return None
            oActivePerform.AttrClear(sAttr, sKey)
        else:
            oEquipItem.AttrClear(sAttr, sKey)

    
    def EnablePassivePerform(self, oItem, iPerformSID, iLv):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iItem = oItem.m_ID
        if (iPerformSID, iItem) in self.m_EnablePassivePerform:
            SendAlert('err', '%d %d s8 enableperform err %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oItem, iPerformSID, iLv, self.m_EnablePassivePerform))
            return None
        oPerform = oOwner.m_Game.m_ResMgr.NewPerform(iPerformSID, oOwner, iLv)
        if not oPerform:
            return None
        oPerform.m_Item = iItem
        self.m_EnablePassivePerform[(iPerformSID, iItem)] = oPerform
        oPerform.Enable(oOwner)

    
    def DisablePassivePerform(self, oItem, iPerformSID):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iItem = oItem.m_ID
        if (iPerformSID, iItem) not in self.m_EnablePassivePerform:
            SendAlert('err', '%d %d s8 disableperform err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, oItem, iPerformSID, self.m_EnablePassivePerform))
            return None
        oPerform = self.m_EnablePassivePerform.pop((iPerformSID, iItem))
        oPerform.Disable(oOwner)
        oPerform.Release()

    
    def EnableThirdItem(self, iItem):
        if not self.CheckItemEquip(iItem, THIRDITEM_MASK):
            SendAlert('err', '%d %d s8 enablethirditem err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iItem, self.m_EquipThirdItem, self.m_ThirdItem))
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oItem = self.m_ThirdItem[iItem]
        if not oItem:
            return None
        iActivePerform = oItem.m_ActivePerform
        if iActivePerform:
            oOwner.AddPerform(iActivePerform, 1, iItem = iItem)
        self.EnablePassivePerform(oItem, oItem.m_PassivePerform, oItem.m_Quality)
        for iAbility, iAbilityLv in oItem.m_Ability.items():
            self.EnablePassivePerform(oItem, iAbility, iAbilityLv)
        
        self.EnableAllThirdGrooveAttr()
        oItem.Enable()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, self.GetOwner(), { }, iSub = S8_THIRDITEM_ENABLE)

    
    def EnableGemItem(self, iItem):
        if not self.CheckItemEquip(iItem, GEMITEM_MASK):
            SendAlert('err', '%d %d s8 enablegemitem err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iItem, self.m_EquipGemItem, self.m_GemItem))
            return None
        oItem = self.m_GemItem[iItem]
        self.EnablePassivePerform(oItem, oItem.m_PassivePerform, oItem.m_Quality)

    
    def DisableThirdItem(self, iItem):
        oOwner = self.GetOwner()
        if not oOwner or iItem not in self.m_ThirdItem:
            return None
        oItem = self.m_ThirdItem[iItem]
        if not oItem:
            return None
        oItem.Disable()
        self.DisableAllThirdGrooveAttr()
        for iPerformSID, iTmpItem in list(self.m_EnablePassivePerform):
            if iTmpItem == iItem:
                self.DisablePassivePerform(oItem, iPerformSID)
        
        iActivePerform = oItem.m_ActivePerform
        if iActivePerform:
            oSkillMgr = self.m_Game.m_SkillMgr
            if oSkillMgr:
                lstSkill = oSkillMgr.GetSkillBySID(iActivePerform)
                for oSkill in lstSkill:
                    oSkillMgr.TryHaltSkill(oSkill)
                
            oOwner.RemovePerform(iActivePerform)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, self.GetOwner(), { }, iSub = S8_THIRDITEM_DISABLE)

    
    def DisableGemItem(self, iItem):
        if iItem not in self.m_GemItem:
            return None
        oItem = self.m_GemItem[iItem]
        for iPerformSID, iTmpItem in list(self.m_EnablePassivePerform):
            if iTmpItem == iItem:
                self.DisablePassivePerform(oItem, iPerformSID)
        

    
    def GS2CAddS8ThirdItem(self, oItem, dPlayer = None):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if not dPlayer:
            dPlayer = self.GetPlayers()
        seasonplaynet.GS2CAddS8ThirdItem(oOwner, oItem, dPlayer)

    
    def GS2CAddS8GemItem(self, oItem, dPlayer = None):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if not dPlayer:
            dPlayer = self.GetPlayers()
        seasonplaynet.GS2CAddS8GemItem(oOwner, oItem, dPlayer)

    
    def GS2CRemoveS8Item(self, iItem, dPlayer = None):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if not dPlayer:
            dPlayer = self.GetPlayers()
        seasonplaynet.GS2CRemoveS8Item(oOwner, iItem, dPlayer)


