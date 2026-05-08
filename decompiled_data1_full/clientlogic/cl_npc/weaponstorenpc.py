# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/weaponstorenpc.pyc
# RelativePath: clientlogic/cl_npc/weaponstorenpc.pyc
# Source Generated with Decompyle++
# File: weaponstorenpc.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_DROP_EQUIP, BAG_TYPE_WEAPONSTORE, NPC_CB_ITEMCONOP, BAG_TYPE_WIELD, BAG_TYPE_EXWEAPON, BAG_TYPE_GLOBAL, BAG_TYPE_WEAPONSTORE, NPC_CB_INJECT, NORMAL_QUALITY
from cl_object.logging import WeaponstoreLog
from cl_npc.net import GS2CWeaponInjectAnimaInfo
import cl_item
import cl_reward
import cl_notify
import cl_formula
from . import mobject
from . import net

class CWeaponStoreNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_AnimaInfo = { }
        oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
        self.m_AnimaCost = oWeaponStoreElement.m_AnimaCost if oWeaponStoreElement else 0
        self.m_AllAnimaCost = { }

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        self.SetHeroInteractStatus(oHero.m_PlayerID)
        if self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        self.SendInteractMsg(oHero)
        oHero.m_BuyMgr.SetInteractShopNpc(self.m_ID)
        self.RefreshWeaponGrade(oHero)
        self.RefreshShopUI(oHero)
        self.OnCompensateWeapon(oHero)

    
    def OnStopInteract(self, oHero):
        oHero.m_BuyMgr.SetInteractShopNpc(0)

    
    def RefreshShopUI(self, oHero):
        oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
        if oWeaponStoreElement:
            lstNotOperateWeapon = oWeaponStoreElement.GetNotOperateWeapon(oHero)
        else:
            lstNotOperateWeapon = []
        net.GS2CNPCOpenWeaponStoreUI(self, oHero, cl_formula.GetFormulaResult(oHero, self.GetHeroAnimaCost(oHero), { }), lstNotOperateWeapon)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_ITEMCONOP, self.ItemInteract, self)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_INJECT, self.InjectAnimaOperation, self)

    
    def OnCompensateWeapon(self, oHero):
        lstCompensateWeapon = oHero.QuerySavedData('CompensateWeaponInfo', [])
        if not lstCompensateWeapon:
            return None
        cl_notify.SendWarConfirm(self.m_Game, oHero, 1101, 1, 'None', '', {
            0: self.CompensateWeapon })

    
    def CompensateWeapon(self, oHero):
        lstCompensateWeapon = oHero.QuerySavedData('CompensateWeaponInfo', [])
        if not lstCompensateWeapon:
            return None
        oHero.SetSavedData('CompensateWeaponInfo', [])
        self.m_Game.m_WarMgr.HandlePlayerUnWarSetInfo(oHero.m_PlayerID, {
            'CompensateWeaponInfo': { } })
        iGrade = cl_reward.GetWeaponRewardGrade(oHero.m_Game)
        for dWeappon in lstCompensateWeapon:
            if not dWeappon:
                continue
            oEquip = cl_item.CreateEquip(self.m_Game, dWeappon['SID'], 0, 0)
            oEquip.Load(dWeappon)
            oEquip.SetBaseGrade(iGrade)
            lstDropData = [
                oEquip]
            vDropPos = oHero.GetPos()
            self.m_Game.GetResMgr().CreateDrop(oHero.m_Scene, NWARRIOR_DROP_EQUIP, vDropPos, lstDropData, { }, {
                'DropSource': oHero.m_PlayerID }, oHero.m_ID)
            WeaponstoreLog.Info('%d compensateweapon drop info:%s' % (oHero.m_PlayerID, dWeappon))
        

    
    def ItemInteract(self, oHero, iFromContainer, iToContainer, iTarget, iFromPos, iToPos):
        tKey = (iFromContainer, iToContainer)
        if tKey not in g_NpcItemOPFunc:
            return None
        oToContainer = cl_item.cnet.GetContainer(oHero, iToContainer)
        oFromContainer = cl_item.cnet.GetContainer(oHero, iFromContainer)
        if not self.CheckVaildWeaponOp(oHero, oFromContainer, oToContainer, iFromPos, iToPos):
            return None
        WeaponstoreLog.Debug('%d weaponstorechange form %d %d to %d %d' % (oHero.m_PlayerID, iFromContainer, iFromPos, iToContainer, iToPos))
        g_NpcItemOPFunc[tKey](oHero, oFromContainer, oToContainer, iTarget, iFromPos, iToPos)

    
    def RefreshWeaponGrade(self, oHero):
        oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
        if not oWeaponStoreElement:
            return None
        oCon = oHero.m_WeaponStoreCon
        lstExchangeWeapon = oWeaponStoreElement.GetExchangeWeaponInfo()
        for oEquip in oCon.m_Item.values():
            if oEquip.m_ID in lstExchangeWeapon:
                continue
            iGrade = cl_reward.GetWeaponRewardGrade(oHero.m_Game)
            oEquip.SetBaseGrade(iGrade)
        

    
    def InjectAnimaOperation(self, oHero, iContainer, iWeapon, isInject, iPos):
        oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
        if not oWeaponStoreElement:
            return None
        oContainer = cl_item.cnet.GetContainer(oHero, iContainer)
        oWeapon = oContainer.GetItemByID(iWeapon)
        if not oWeapon and isInject:
            return None
        dInjectAnimaWeapon = oWeaponStoreElement.m_InjectAnimaInfo.setdefault(oHero.m_PlayerID, { })
        if isInject:
            if not oWeaponStoreElement.CheckWeaponInfo(oWeapon, oHero.m_PlayerID, 'injectanima'):
                return None
            WeaponstoreLog.Debug('%d weapon %d %d injectanmia %d' % (oHero.m_PlayerID, iWeapon, oWeapon.m_SID, isInject))
            iAnimaCost = self.GetHeroAnimaCost(oHero)
            if iAnimaCost > oHero.m_WarGSCash:
                WeaponstoreLog.Debug('%d no enoughgscash to injectanima %d %d' % (oHero.m_PlayerID, iAnimaCost, oHero.m_WarGSCash))
                return None
            if len(dInjectAnimaWeapon) >= oWeaponStoreElement.m_MaxAnimaNum:
                WeaponstoreLog.Debug('%d injectanima weapon num too many' % oHero.m_PlayerID)
                return None
            if iWeapon in dInjectAnimaWeapon:
                WeaponstoreLog.Debug('%d weapon %d %d already injectanima' % (oHero.m_PlayerID, iWeapon, oWeapon.m_SID))
                return None
            if oHero.m_PlayerID in self.m_AnimaInfo:
                return None
            lstPos = oWeaponStoreElement.GetValidInjectPos(oHero)
            if oContainer.m_BagType == BAG_TYPE_WEAPONSTORE or iPos != oWeapon.m_Pos:
                WeaponstoreLog.Debug('%d invalid pos %d to injectanima %d %d' % (oHero.m_PlayerID, iPos, iWeapon, oWeapon.m_SID))
                return None
            if iPos not in lstPos:
                WeaponstoreLog.Debug('%d invalid pos %d to injectanima %d %d' % (oHero.m_PlayerID, iPos, iWeapon, oWeapon.m_SID))
                return None
            oHero.ConsumeGSCash(iAnimaCost, 'InjectAnmiaCost')
            dInjectAnimaWeapon[iWeapon] = iPos
            self.m_AnimaInfo[oHero.m_PlayerID] = iWeapon
            oWeapon.Set('InjectOwner', oHero.m_PlayerID)
            oWeaponStoreElement.InjectSave(oHero, oContainer, iPos, oWeapon)
        elif iWeapon not in dInjectAnimaWeapon:
            return None
        iPos = dInjectAnimaWeapon.pop(iWeapon)
        oWeaponStoreElement.ClearInjectAnimaWeaponCache(oHero.m_PlayerID, iWeapon)
        if oWeapon:
            oWeapon.Set('InjectOwner', 0)
        else:
            iDrop = oWeaponStoreElement.GetInjectAnimaWeaponDropID(iWeapon)
            if iDrop:
                oDrop = self.m_Game.GetObject(iDrop)
                if oDrop:
                    oWeapon = oDrop.m_DropInfo[0]
                    oWeapon.Set('InjectOwner', 0)
                    oDrop.m_AnimaDrop = NORMAL_QUALITY
                    oDrop.MapSendPacket({
                        oHero.m_PlayerID: 1 })
                else:
                    for iOwner in self.m_Game.m_WarMgr.GetRoomHero():
                        if iOwner == oHero.m_ID:
                            continue
                        oOwner = self.m_Game.GetObject(iOwner)
                        if not oOwner:
                            continue
                        oWeapon = oOwner.m_WieldCon.GetItemByID(iWeapon)
                        if not oWeapon:
                            oWeapon = oOwner.m_ExWeaponCon.GetItemByID(iWeapon)
                        if oWeapon:
                            oWeapon.Set('InjectOwner', 0)
                            if oOwner.m_BuyMgr.m_InteractShopNpc == self.m_ID:
                                self.RefreshShopUI(oOwner)
                            break
                    
        self.m_AnimaInfo.pop(oHero.m_PlayerID, 0)
        if oContainer.m_BagType != BAG_TYPE_WEAPONSTORE and iPos not in oHero.m_WeaponStoreCon.m_LevelSavePos:
            oHero.m_WeaponStoreCon.m_LevelSavePos.append(iPos)
        iWeaponSID = oWeapon.m_SID if oWeapon else 0
        WeaponstoreLog.Info('%d injectanima success %d %d isinject %d' % (oHero.m_PlayerID, iWeapon, iWeaponSID, isInject))
        GS2CWeaponInjectAnimaInfo(oHero.m_PlayerID, self.m_ID, iWeapon, iPos, isInject)

    
    def CheckVaildWeaponOp(self, oHero, oFromContainer, oToContainer, iFromPos, iToPos):
        oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
        if not oWeaponStoreElement:
            return 0
        if not oFromContainer and oToContainer:
            return 1
        oWeapon = oFromContainer.GetItem(iFromPos)
        if not oWeaponStoreElement.CheckWeaponInfo(oWeapon, oHero.m_PlayerID, 'toweaponstore'):
            return 0
        if oHero.m_PlayerID not in oWeaponStoreElement.m_InjectAnimaInfo:
            return 1
        dInjectAnimaInfo = oWeaponStoreElement.m_InjectAnimaInfo[oHero.m_PlayerID]
        if oToContainer.m_BagType == BAG_TYPE_WEAPONSTORE and iToPos in dInjectAnimaInfo.values():
            oWeapon = oFromContainer.GetItem(iFromPos)
            if oWeapon:
                if oWeapon.m_ID in dInjectAnimaInfo:
                    pass
                if not (dInjectAnimaInfo[oWeapon.m_ID] == iToPos):
                    return 0
        if oFromContainer.m_BagType == BAG_TYPE_WEAPONSTORE and iFromPos in dInjectAnimaInfo.values():
            oWeapon = oToContainer.GetItem(iToPos)
            if oWeapon:
                if oWeapon.m_ID in dInjectAnimaInfo:
                    pass
                if not (dInjectAnimaInfo[oWeapon.m_ID] == iFromPos):
                    return 0
        return 1

    
    def GetHeroAnimaCost(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_AllAnimaCost:
            self.m_AllAnimaCost[iHero] = cl_formula.GetFormulaResult(oHero, self.m_AnimaCost, { })
        return self.m_AllAnimaCost[iHero]


g_NpcItemOPFunc = {
    (BAG_TYPE_WEAPONSTORE, BAG_TYPE_GLOBAL): cl_item.cnet.RemoveWeaponFromWeaponCon,
    (BAG_TYPE_WEAPONSTORE, BAG_TYPE_WEAPONSTORE): cl_item.cnet.ChangeWeaponConEquipPos,
    (BAG_TYPE_WEAPONSTORE, BAG_TYPE_EXWEAPON): cl_item.cnet.ChangeWeaponFromDifferentWeaponCon,
    (BAG_TYPE_WEAPONSTORE, BAG_TYPE_WIELD): cl_item.cnet.ChangeWeaponFromDifferentWeaponCon,
    (BAG_TYPE_EXWEAPON, BAG_TYPE_WEAPONSTORE): cl_item.cnet.ChangeWeaponFromDifferentWeaponCon,
    (BAG_TYPE_WIELD, BAG_TYPE_WEAPONSTORE): cl_item.cnet.ChangeWeaponFromDifferentWeaponCon }
