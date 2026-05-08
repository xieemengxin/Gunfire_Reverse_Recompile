# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/smithnpc.pyc
# RelativePath: clientlogic/cl_npc/smithnpc.pyc
# Source Generated with Decompyle++
# File: smithnpc.pyc (Python 3.6)

from cl_commondefines import INTERACT_STATUS_DONE, OBTAIN_WARCASH, NPC_CB_ITEM, SMITH_RECAST_COST, INTERACT_RULE_SMITHUPGRADE, SMITHNPCSUBMSG_UPGRADE, SMITHNPCSUBMSG_RECAST, SMITHNPCSUBMSG_ADD_INSCRIPTION, SMITHNPCSUBMSG_RECAST_INSCRIPTION, SMITHNPCSUBMSG_INTERACT, OPTION_STATUS_SHOW, OPTION_STATUS_HIDE, OPTION_STATUS_NOINTERACT
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
from cl_only import Functor
import cl_msgcenter
import cl_netattr
from . import mobject
from . import net

def CheckUpgrade(oNpc, oHero, oItem):
    pid = oHero.m_PlayerID
    if pid not in oNpc.m_PlayerInteractStatus:
        return OPTION_STATUS_NOINTERACT
    oRule = oNpc.GetRule()
    if oRule and not oRule.ValidUpgrade(oHero.m_ID):
        return OPTION_STATUS_NOINTERACT
    if oItem.CanUpgrade():
        return OPTION_STATUS_SHOW
    return OPTION_STATUS_NOINTERACT


def CheckRecastGemini(oNpc, oHero, oItem):
    if oItem.CanRecastGemini():
        return OPTION_STATUS_SHOW
    return OPTION_STATUS_NOINTERACT


def CheckExtraInscription(oNpc, oHero, oItem):
    if not oItem.CanExtraInscription():
        return OPTION_STATUS_HIDE
    oInscriptionCom = oItem.GetComponent('Inscription')
    if not oInscriptionCom:
        return OPTION_STATUS_NOINTERACT
    if oHero.Query('SuitExtraInscription', 0):
        if oItem.CheckHasMaxInscriptionNum():
            return OPTION_STATUS_NOINTERACT
        return OPTION_STATUS_SHOW
    if oHero.Query('ExtraInscription', 0):
        if oInscriptionCom.GetExtraInscriptionTimes() or oItem.CheckHasMaxInscriptionNum():
            return OPTION_STATUS_NOINTERACT
        return OPTION_STATUS_SHOW
    return OPTION_STATUS_HIDE


def CheckRecastInscription(oNpc, oHero, oItem):
    if not oHero:
        return OPTION_STATUS_HIDE
    if not oHero.Query('RecastInscription', 0):
        return OPTION_STATUS_HIDE
    if oItem.CanRecast():
        return OPTION_STATUS_SHOW
    return OPTION_STATUS_NOINTERACT


class CSmithNpc(mobject.CNPC):
    m_LimitInteract = 1
    m_Msgs = {
        0: cl_msgcenter.MSG_WAR_UPGRADEWEAPON,
        1: cl_msgcenter.MSG_WAR_RECASTWEAPON,
        2: cl_msgcenter.MSG_WAR_ADD_INSCRIPTION }
    m_BeforeSUBMsgs = {
        0: SMITHNPCSUBMSG_UPGRADE,
        1: SMITHNPCSUBMSG_RECAST,
        2: SMITHNPCSUBMSG_ADD_INSCRIPTION,
        3: SMITHNPCSUBMSG_RECAST_INSCRIPTION }
    
    def Release(self):
        self.m_Options = { }
        super().Release()

    
    def __init__(self, *args):
        super(CSmithNpc, self).__init__(*args)
        self.AddRule()
        self.m_Options = {
            0: [
                CheckUpgrade,
                OBTAIN_WARCASH,
                (lambda oItem: self.GetExtraUpgradeCost(oItem) + oItem.GetWeaponUpgradeCost()),
                (lambda oItem, dArgs: oItem.Upgrade(dArgs['UpgradeLevel']))],
            1: [
                CheckRecastGemini,
                OBTAIN_WARCASH,
                (lambda oItem: SMITH_RECAST_COST),
                (lambda oItem, dArgs: oItem.RecastGemini())],
            2: [
                CheckExtraInscription,
                OBTAIN_WARCASH,
                (lambda oItem: oItem.GetWeaponExtraInscriptionCost()),
                (lambda oItem, dArgs: oItem.ExtraInscription())],
            3: [
                CheckRecastInscription,
                OBTAIN_WARCASH,
                (lambda oItem: self.GetRecastCost(oItem)),
                (lambda oItem, dArgs: self.Recast(oItem))] }
        self.m_WeaponRecastList = { }

    
    def AddRule(self):
        self.AddExtraInteractRule(INTERACT_RULE_SMITHUPGRADE, {
            'Times': 2 })

    
    def GetRule(self):
        return self.GetExtraInteractRule(INTERACT_RULE_SMITHUPGRADE)

    
    def SetHeroInteractStatus(self, pid, iNotify = 1):
        self.SetPlayerInteractStatus(pid, INTERACT_STATUS_DONE)

    
    def SetPlayerInteractStatus(self, pid, iStatus, iNotify = 1):
        if pid not in self.m_PlayerInteractStatus:
            return None
        iOldStatus = self.m_PlayerInteractStatus[pid] & 14
        if iOldStatus & iStatus == iStatus:
            return None
        self.m_PlayerInteractStatus[pid] = iOldStatus | iStatus
        if iNotify:
            self.NotifyInteractInfo(pid)

    
    def RefreshOption(self, oHero):
        oCon = oHero.m_WieldCon
        lstWeapon = oCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
        dItem = { }
        for oWeapon in lstWeapon:
            dItem[oWeapon.m_ID] = { }
            for iOp, (validFunc, iCashType, costFunc, _) in self.m_Options.items():
                iOptionStatus = validFunc(self, oHero, oWeapon)
                iCostCash = 0 if oHero.Query('SmithNoCashCost', 0) else costFunc(oWeapon)
                dItem[oWeapon.m_ID][iOp] = (iCashType, iCostCash, iOptionStatus)
            
        
        iMaxRecastedTimes = oHero.Query('RecastInscription', 0)
        if self.m_LimitInteract:
            (iRestUpTimes, iMaxUpTimes) = (0, 0)
            oRule = self.GetRule()
            if oRule:
                (iRestUpTimes, iMaxUpTimes) = oRule.GetUpgradeTimes(oHero.m_ID)
            else:
                (iRestUpTimes, iMaxUpTimes) = (-1, -1)
        lstWeaponInfo = []
        for oWeapon in lstWeapon:
            lstAttr = []
            iRecastedTimes = 0
            dAttr = {
                'Attr': lstAttr }
            dPreview = oWeapon.PreviewWeaponUpgradeAttr()
            for sAttr, iValue in dPreview.items():
                (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME[sAttr]
                lstAttr.append((iIdx, iType, iLen, iValue))
            
            if oWeapon.m_ID in self.m_WeaponRecastList:
                iRecastedTimes = self.m_WeaponRecastList[oWeapon.m_ID]
            iRecastTimes = iMaxRecastedTimes - iRecastedTimes if iRecastedTimes < iMaxRecastedTimes else 0
            lstGeminiExcludeInfo = oWeapon.GetGeminiExcludeInfo()
            lstWeaponInfo.append((oWeapon.m_ID, dAttr, iRecastTimes, iMaxRecastedTimes, lstGeminiExcludeInfo))
        
        net.GS2CSmithInteractInfo(oHero, iRestUpTimes, iMaxUpTimes, lstWeaponInfo)
        net.GS2CNpcItemInteract(oHero, self, dItem)
        net.SetNpcUICallBackFunction(oHero, NPC_CB_ITEM, Functor(ItemInteract, self.m_ID), self)

    
    def ItemInteract(self, oHero, iItem, iOption):
        if not self.ValidInteract(oHero):
            return 0
        if iOption not in self.m_Options:
            return 0
        oWeapon = oHero.m_WieldCon.GetItemByID(iItem)
        if not oWeapon:
            return 0
        (validFunc, iCashType, costFunc, rewardFunc) = self.m_Options[iOption]
        if validFunc(self, oHero, oWeapon) != OPTION_STATUS_SHOW:
            return 0
        iCost = costFunc(oWeapon)
        if oHero.Query('SmithNoCashCost', 0):
            iCost = 0
        sReason = self.GetActionKey(iOption, oWeapon.m_SID)
        if iCashType == OBTAIN_WARCASH:
            if oHero.m_WarCash < iCost:
                return 0
            oHero.AddCash(-iCost, sReason)
            iUpgradeLevel = 1
            dArgs = {
                'UpgradeLevel': iUpgradeLevel }
            if iOption in self.m_BeforeSUBMsgs:
                iSubMSG = self.m_BeforeSUBMsgs[iOption]
                dMsgInfo = {
                    'Cost': iCost,
                    'ItemID': iItem,
                    'NpcID': self.m_ID,
                    'Args': dArgs }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORESMITHNPC, oHero, dMsgInfo, iSub = iSubMSG)
            rewardFunc(oWeapon, dArgs)
            if iOption in self.m_Msgs:
                iMsg = self.m_Msgs[iOption]
                dMsgInfo = {
                    'Cost': iCost,
                    'ItemID': iItem,
                    'NpcID': self.m_ID }
                cl_msgcenter.SendMsg(iMsg, oHero, dMsgInfo)
            return 1
        return 0

    
    def GetActionKey(self, iOption, iWeapon):
        if iOption == 0:
            return 'NPC-%d-upgrade-weapon-%d' % (self.m_SID, iWeapon)
        if iOption == 1:
            return 'NPC-%d-reforge-weapon-%d' % (self.m_SID, iWeapon)
        if iOption == 2:
            return 'NPC-%d-addInscription-weapon-%d' % (self.m_SID, iWeapon)
        if iOption == 3:
            return 'NPC-%d-RecastInscription-weapon-%d' % (self.m_SID, iWeapon)
        return 'NPC-%d-unknown-weapon-%d' % (self.m_SID, iWeapon)

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORESMITHNPC, oHero, {
            'InteractStatus': self.m_PlayerInteractStatus[pid],
            'NpcID': self.m_ID }, iSub = SMITHNPCSUBMSG_INTERACT)
        self.SetHeroInteractStatus(pid)
        if self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        self.RefreshOption(oHero)

    
    def SetIntactAction(self, iType, iCash):
        if iType not in self.m_Options:
            return None
        
        self.m_Options[iType][2] = lambda oItem: iCash

    
    def Recast(self, oWeapon):
        if oWeapon.m_ID not in self.m_WeaponRecastList:
            self.m_WeaponRecastList[oWeapon.m_ID] = 1
        else:
            self.m_WeaponRecastList[oWeapon.m_ID] += 1
        oWeapon.Recast()

    
    def GetRecastCost(self, oWeapon):
        oHero = oWeapon.GetOwner()
        if oHero.Query('RecastInscriptionNoCost', 0):
            return 0
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            return None
        iNum = oInscriptionCom.m_InscriptionNum
        iGrade = oWeapon.m_BaseGrade
        iRecastedTimes = 0
        if oWeapon.m_ID in self.m_WeaponRecastList:
            iRecastedTimes = self.m_WeaponRecastList[oWeapon.m_ID]
        iCost = int(iGrade * iNum * 20 * (1 + iRecastedTimes * 0.3) // 1)
        return iCost

    
    def GetExtraUpgradeCost(self, oWeapon):
        oHero = oWeapon.GetOwner()
        iEnable = oHero.Query('WeaponExtraUpgradeCostEnable', 0)
        if not iEnable:
            return 0
        dCost = oHero.Query('WeaponExtraUpgradeCost', { })
        if not dCost:
            return 0
        if self.m_ID in dCost:
            return dCost[self.m_ID]
        return 0



def ItemInteract(iNpc, oHero, iItem, iOption):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    iResult = oNpc.ItemInteract(oHero, iItem, iOption)
    net.GS2CNpcItemResult(oHero, oNpc, iItem, iResult)
    oNpc.RefreshOption(oHero)


class CPhaseSmithNpc(CSmithNpc):
    m_CheckInteractDistance = False
    m_LimitInteract = 0
    
    def AddRule(self):
        pass

    
    def GetRule(self):
        pass


