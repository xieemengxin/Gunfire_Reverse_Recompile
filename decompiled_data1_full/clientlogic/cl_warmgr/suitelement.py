# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/suitelement.pyc
# RelativePath: clientlogic/cl_warmgr/suitelement.pyc
# Source Generated with Decompyle++
# File: suitelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_object.logging import SuitLog
from cl_platformdata import GetSuitCls, GetAllSuit, GetGameExcludeSuit, GetLimitShow, GetSuitExclude
from cl_commondefines import SUIT_RELIC, SUIT_WEAPONDAMAGE, SUIT_WEAPONTYPE, SUIT_TALENT, RELIC_TYPE_CURSE, SUIT_RELICTYPE, SUIT_BENEDICTION, ALL_SUIT_TYPE, WEAPON_ELEMENTREFRESH_SET, WEAPON_ELEMENTREFRESH_REMOVE, DAM_TYPE_NORMAL
from cl_item.defines import DEPUTY_HOLD, MAIN_HOLD
from cl_only import DeepCopy
import cl_item.defines as itemdef
import cl_msgcenter
import cl_perform
import cl_snetwar
import cl_hero
import cl_notify

class CSuitElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CSuitElement, self).__init__(oGame, nid, oData)
        self.m_CallFlag = 'SuitElement'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_OldElementType = { }
        self.m_Condtion = { }
        self.m_CurSituate = { }
        self.m_Enable = { }
        self.m_CondInfo = { }
        self.m_SuitMap = { }
        self.m_SuitShow = { }
        self.m_PrioritySuit = { }
        self.m_LimiteBene = self.m_Data.m_Config.get('LimiteBene', { })
        self.m_LimitBeneLayer = self.m_Data.m_Config.get('LimitBeneLayer', ())
        self.m_ForbidSuit = { }
        self.m_ForbidSuitCon = { }
        self.m_SuitCon = { }
        self.m_ForeverCondtionInfo = { }

    
    def InitCondtion(self):
        dSuit = GetAllSuit()
        dExcludeSuit = GetGameExcludeSuit(self.m_WarMgr.GetPlayType())
        for iSuit in dSuit:
            if iSuit in dExcludeSuit:
                continue
            if iSuit in self.m_ForbidSuit:
                continue
            clsSuit = GetSuitCls(iSuit)
            self.m_CondInfo[iSuit] = (list(clsSuit.m_CondInfo)[0], dict(list(clsSuit.m_CondInfo.values())[0]))
            lstForbidCon = self.m_ForbidSuitCon.get(iSuit, [])
            for iConSID in lstForbidCon:
                self.m_CondInfo[iSuit][1].pop(iConSID, 0)
            
            self.m_SuitCon[iSuit] = { }
            dSuitCon = self.m_SuitCon[iSuit]
            for iConSID, (iConditionType, iConArgs) in clsSuit.m_Condition.items():
                if iConSID in lstForbidCon:
                    continue
                dSuitCon[iConSID] = (iConditionType, iConArgs)
                dType = self.m_Condtion.setdefault(iConditionType, { })
                tSuitInfo = (iSuit, iConSID)
                if iConArgs not in dType:
                    dType[iConArgs] = []
                dType[iConArgs].append(tSuitInfo)
                self.m_Condtion[iConditionType] = dType
            
        

    
    def InitSuitMap(self):
        dSuit = GetAllSuit()
        dExcludeSuit = GetGameExcludeSuit(self.m_WarMgr.GetPlayType())
        for iType in ALL_SUIT_TYPE:
            self.m_SuitMap[iType] = { }
        
        for iSuit in dSuit:
            if iSuit in dExcludeSuit:
                continue
            if iSuit in self.m_ForbidSuit:
                continue
            clsSuit = GetSuitCls(iSuit)
            lstForbidCon = self.m_ForbidSuitCon.get(iSuit, [])
            for iConSID, (iType, args) in clsSuit.m_Condition.items():
                if iConSID in lstForbidCon:
                    continue
                dMap = self.m_SuitMap[iType]
                if iType in (SUIT_RELIC, SUIT_WEAPONTYPE, SUIT_WEAPONDAMAGE, SUIT_BENEDICTION):
                    if args not in dMap:
                        dMap[args] = []
                    dMap[args].append(iSuit)
                    continue
                if iType == SUIT_TALENT:
                    iTalent = args[0]
                    if iTalent not in dMap:
                        dMap[iTalent] = []
                    dMap[iTalent].append(iSuit)
                    continue
                if iType == SUIT_RELICTYPE:
                    iRelicType = args[0]
                    if iRelicType not in dMap:
                        dMap[iRelicType] = []
                    dMap[iRelicType].append(iSuit)
            
        

    
    def GetSuitMap(self, iType):
        return self.m_SuitMap[iType]

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEHERO, self.OnCreateHero, 'CreateHero' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, self.OnAddRelicPerform, 'AddRelicPerform' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVERELIC, self.OnRemoveRelic, 'RemoveRelic' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, self.OnUnholdWeapon, 'UnholdWeapon' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.OnChangeWeapon, 'ChangeWeapon' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, self.OnWeaponEleRefreshSet, 'OnWeaponEleRefreshSet' + self.m_CallFlag, WEAPON_ELEMENTREFRESH_SET)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, self.OnWeaponEleRefreshRemove, 'OnWeaponEleRefreshRemove' + self.m_CallFlag, WEAPON_ELEMENTREFRESH_REMOVE)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDTALENT, self.OnAddTalent, 'AddTalent' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVETALENT, self.OnRemoveTalent, 'RemoveTalent' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.OnPlayerLogin, 'PlayerLogin' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDWEAPON, self.OnAddWeapon, 'AddWeapon' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDBENED, self.OnAddBennd, 'AddBennd' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVEBENED, self.OnRemoveBened, 'RemoveBened' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GEN_BEFOR_BENED, self.OnGenBened, 'GenBened' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_BEFOREREMOVEWEAPON, self.OnBeforeRemoveWeapon, 'BeforeRemoveWeapon' + self.m_CallFlag)

    
    def InitAfter(self):
        self.InitCondtion()
        self.InitSuitMap()

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEHERO, 'CreateHero' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, 'AddRelicPerform' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVERELIC, 'RemoveRelic' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_BEFOREUNHOLDWEAPON, 'UnholdWeapon' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, 'ChangeWeapon' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, 'OnWeaponEleRefreshSet' + self.m_CallFlag, WEAPON_ELEMENTREFRESH_SET)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, 'OnWeaponEleRefreshRemove' + self.m_CallFlag, WEAPON_ELEMENTREFRESH_REMOVE)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDTALENT, 'AddTalent' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, 'PlayerLogin' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDWEAPON, 'AddWeapon' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDBENED, 'AddBennd' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVEBENED, 'RemoveBened' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GEN_BEFOR_BENED, 'GenBened' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_BEFOREREMOVEWEAPON, 'BeforeRemoveWeapon' + self.m_CallFlag)
        super(CSuitElement, self).Release()
        self.m_WarMgr = None
        self.m_Game = None

    
    def Save(self):
        dData = { }
        dData['FC'] = DeepCopy(self.m_ForeverCondtionInfo)
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ForeverCondtionInfo = dData['FC']
        self.DealForeverCondtion()

    
    def SaveSeed(self, oHero):
        dData = {
            'PID': oHero.m_PlayerID,
            'FC': DeepCopy(self.m_ForeverCondtionInfo.get(oHero.m_PlayerID, { })) }
        return dData

    
    def LoadSeed(self, dData):
        if not dData:
            return None
        iPlayer = dData['PID']
        oHero = self.m_WarMgr.GetHeroByPlayer(iPlayer)
        if not oHero:
            return None
        self.OnCreateHero(self.m_WarMgr, oHero, {
            'HeroSID': oHero.m_SID })
        self.OnPlayerLogin(self.m_WarMgr, oHero, { })
        self.m_ForeverCondtionInfo[iPlayer] = dData['FC']
        self.DealForeverCondtion()

    
    def DealForeverCondtion(self):
        for iPlayer, dInfo in list(self.m_ForeverCondtionInfo.items()):
            oHero = self.m_WarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                continue
            for iSuit, iConSID in list(dInfo):
                clsSuit = GetSuitCls(iSuit)
                if not clsSuit:
                    continue
                if iConSID not in clsSuit.m_Condition:
                    SuitLog.Alert('%d %d error forevercondition %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iSuit, iConSID))
                    continue
                (iType, Key) = clsSuit.m_Condition[iConSID]
                self.AddCheckSuitCondtion(oHero, iType, Key)
            
        

    
    def OnHalfOpen(self):
        for iHero in self.m_WarMgr.GetAllHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            self.OnCreateHero(self.m_WarMgr, oHero, {
                'HeroSID': oHero.m_SID })
            oWeapon = oHero.m_WieldCon.GetCurWeapon()
            self.OnChangeWeapon(self.m_WarMgr, oHero, {
                'ItemID': oWeapon.m_ID })
            for iRelic in oHero.m_RelicCon.GetAllRelicSID():
                self.OnAddRelicPerform(self.m_WarMgr, oHero, {
                    'iPerform': iRelic })
            
            dTalent = oHero.m_TalentCon.GetAllTalentLevel()
            for iTalent, iLevel in dTalent.items():
                self.OnAddTalent(self.m_WarMgr, oHero, {
                    'iPerform': iTalent,
                    'Level': iLevel })
            
            for iBenediction in oHero.m_BenedictionCon.GetBenedictionSID():
                self.OnAddBennd(self.m_WarMgr, oHero, {
                    'Bene': iBenediction })
            
        

    
    def OnGenBened(self, oWarMgr, oTarget, dInfo):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_LayerNum not in self.m_LimitBeneLayer:
            return None
        dExtBeneInfo = self.m_LimiteBene
        dAllWeight = dInfo['BeneWeight']
        for iBene, iWeight in dExtBeneInfo.items():
            dAllWeight[iBene] = iWeight
        

    
    def OnCreateHero(self, oWarMgr, oTarget, dInfo):
        ID = oTarget.m_ID
        iHeroSID = dInfo['HeroSID']
        clsHero = cl_hero.GetHeroData(iHeroSID)
        iCareer = clsHero.m_Career
        self.m_CurSituate[ID] = { }
        self.m_Enable[ID] = { }
        self.m_SuitShow[ID] = { }
        dSuit = GetAllSuit()
        dExcludeSuit = GetGameExcludeSuit(self.m_WarMgr.GetPlayType())
        for iSuit in dSuit:
            if iSuit in dExcludeSuit:
                continue
            if iSuit in self.m_ForbidSuit:
                continue
            clsSuit = GetSuitCls(iSuit)
            if clsSuit.m_Career and iCareer != clsSuit.m_Career:
                continue
            lstForbidCon = self.m_ForbidSuitCon.get(iSuit, [])
            self.m_CurSituate[ID][iSuit] = { }
            self.m_Enable[ID][iSuit] = 0
            self.m_SuitShow[ID][iSuit] = 0
            for iConSID in clsSuit.m_Condition:
                if iConSID in lstForbidCon:
                    continue
                self.m_CurSituate[ID][iSuit][iConSID] = 0
            
        
        self.m_PrioritySuit[ID] = { }

    
    def OnPlayerLogin(self, oWarMgr, oTarget, dInfo):
        cl_snetwar.GS2CSuitMap(self, {
            oTarget.m_PlayerID: 1 })
        if oTarget.m_ID not in self.m_CurSituate:
            return None
        dContion = self.m_CurSituate[oTarget.m_ID]
        if dContion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, [
                dContion], { }, self.m_CondInfo)
        dPlayer = self.m_Game.GetRealPlayers()
        for iPlayer in dPlayer:
            if iPlayer == oTarget.m_PlayerID:
                continue
            oHero = oWarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                continue
            if oHero.m_ID not in self.m_CurSituate:
                continue
            dTempContion = self.m_CurSituate[oHero.m_ID]
            if dTempContion:
                cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oHero.m_ID, [
                    dTempContion], {
                    oTarget.m_PlayerID: 1 }, self.m_CondInfo)
        
        cl_snetwar.GS2CUpdatePrioritySuit(oTarget.m_PlayerID, list(self.m_PrioritySuit[oTarget.m_ID]))

    
    def OnAddTalent(self, oWarMgr, oTarget, dInfo):
        iLevel = dInfo['Level']
        iPerform = dInfo['iPerform']
        tKey = (iPerform, iLevel)
        for iTempPerform, iTempLevel in self.m_Condtion[SUIT_TALENT]:
            if iTempPerform == iPerform and iTempLevel <= iLevel:
                self.AddCheckSuitCondtion(oTarget, SUIT_TALENT, (iTempPerform, iTempLevel))
        
        self.CheckReduceTalentLevel(oTarget, SUIT_TALENT, tKey)

    
    def CheckReduceTalentLevel(self, oTarget, iType, tKey):
        if iType in self.m_Condtion:
            for iPerform, iLevel in self.m_Condtion[iType]:
                if iPerform == tKey[0] and tKey[1] < iLevel:
                    self.RemoveCheckSuitCondtion(oTarget, SUIT_TALENT, (iPerform, iLevel))
            

    
    def OnRemoveTalent(self, oWarMgr, oTarget, dInfo):
        iPerform = dInfo['iPerform']
        pfobj = oTarget.GetPerform(iPerform)
        if not pfobj:
            return None
        iLevel = pfobj.m_Level
        tKey = (iPerform, iLevel)
        self.RemoveCheckSuitCondtion(oTarget, SUIT_TALENT, tKey)

    
    def OnAddRelicPerform(self, oWarMgr, oTarget, dInfo):
        lstCondtion = []
        iSID = dInfo['iPerform']
        dContion = self.AddCheckSuitCondtion(oTarget, SUIT_RELIC, iSID, 0)
        if dContion:
            lstCondtion.append(dContion)
        clsRelic = cl_perform.GetPerformModule(iSID)
        if clsRelic.m_RelicType == RELIC_TYPE_CURSE:
            iCurseNum = oTarget.m_RelicCon.GetNumByRelicType(RELIC_TYPE_CURSE)
            dContion2 = self.AddCheckSuitCondtion(oTarget, SUIT_RELICTYPE, (RELIC_TYPE_CURSE, iCurseNum), 0)
            if dContion2:
                lstCondtion.append(dContion2)
        if lstCondtion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, lstCondtion, { }, self.m_CondInfo)

    
    def OnUnholdWeapon(self, oWarMgr, oTarget, dInfo):
        oWieldCon = oTarget.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['ItemID'])
        if oWeapon in oTarget.m_WieldCon.GetWeapons(DEPUTY_HOLD):
            return None
        if oTarget.m_ID not in self.m_OldElementType:
            return None
        iOldElementType = self.m_OldElementType[oTarget.m_ID]
        lstCondtion = []
        dContion = self.RemoveCheckSuitCondtion(oTarget, SUIT_WEAPONDAMAGE, iOldElementType, 0)
        if dContion:
            lstCondtion.append(dContion)
        if oWeapon.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
            iType = itemdef.EQUIP_HANDGUN
        else:
            iType = oWeapon.m_Type
        dContion2 = self.RemoveCheckSuitCondtion(oTarget, SUIT_WEAPONTYPE, iType, 0)
        if dContion2:
            lstCondtion.append(dContion2)
        if lstCondtion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, lstCondtion, { }, self.m_CondInfo)

    
    def OnChangeWeapon(self, oWarMgr, oTarget, dInfo):
        oWieldCon = oTarget.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['ItemID'])
        if oWeapon in oTarget.m_WieldCon.GetWeapons(DEPUTY_HOLD):
            return None
        iElementType = oWeapon.m_ElementType
        self.m_OldElementType[oTarget.m_ID] = iElementType
        lstCondtion = []
        dContion = self.AddCheckSuitCondtion(oTarget, SUIT_WEAPONDAMAGE, iElementType, 0)
        if dContion:
            lstCondtion.append(dContion)
        if oWeapon.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
            iType = itemdef.EQUIP_HANDGUN
        else:
            iType = oWeapon.m_Type
        SuitLog.Debug('%d %d onchangeweapon sid:%d type:%d' % (self.m_Game.m_ID, oTarget.m_PlayerID, oWeapon.m_SID, iType))
        dContion2 = self.AddCheckSuitCondtion(oTarget, SUIT_WEAPONTYPE, iType, 0)
        if dContion2:
            lstCondtion.append(dContion2)
        if lstCondtion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, lstCondtion, { }, self.m_CondInfo)

    
    def OnWeaponEleRefreshSet(self, oWarMgr, oTarget, dInfo):
        if 'suit' in dInfo['Reason'] or dInfo['RefreshElementType'] == DAM_TYPE_NORMAL:
            return None
        oWieldCon = oTarget.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['Weapon'])
        if oWeapon not in oTarget.m_WieldCon.GetWeapons(MAIN_HOLD):
            return None
        if oTarget.m_ID not in self.m_OldElementType:
            return None
        iOldElementType = self.m_OldElementType[oTarget.m_ID]
        dContion = self.RemoveCheckSuitCondtion(oTarget, SUIT_WEAPONDAMAGE, iOldElementType, 0)
        if dContion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, [
                dContion], { }, self.m_CondInfo)

    
    def OnWeaponEleRefreshRemove(self, oWarMgr, oTarget, dInfo):
        if 'suit' in dInfo['Reason'] or dInfo['RefreshElementType'] == DAM_TYPE_NORMAL:
            return None
        oWieldCon = oTarget.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['Weapon'])
        if oWeapon not in oTarget.m_WieldCon.GetWeapons(MAIN_HOLD):
            return None
        iElementType = oWeapon.m_ElementType
        self.m_OldElementType[oTarget.m_ID] = iElementType
        dContion = self.AddCheckSuitCondtion(oTarget, SUIT_WEAPONDAMAGE, iElementType, 0)
        if dContion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, [
                dContion], { }, self.m_CondInfo)

    
    def OnInscriptionEnableElementType(self, oWarMgr, oTarget, dInfo):
        oWieldCon = oTarget.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['ItemID'])
        if oWeapon not in oTarget.m_WieldCon.GetWeapons(MAIN_HOLD):
            return None
        if oTarget.m_ID not in self.m_OldElementType:
            return None
        iOldElementType = self.m_OldElementType[oTarget.m_ID]
        dContion = self.RemoveCheckSuitCondtion(oTarget, SUIT_WEAPONDAMAGE, iOldElementType, 0)
        if dContion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, [
                dContion], { }, self.m_CondInfo)

    
    def OnInscriptionDisableElementType(self, oWarMgr, oTarget, dInfo):
        oWieldCon = oTarget.m_WieldCon
        oWeapon = oWieldCon.GetItemByID(dInfo['ItemID'])
        if oWeapon not in oTarget.m_WieldCon.GetWeapons(MAIN_HOLD):
            return None
        iElementType = oWeapon.m_ElementType
        self.m_OldElementType[oTarget.m_ID] = iElementType
        dContion = self.AddCheckSuitCondtion(oTarget, SUIT_WEAPONDAMAGE, iElementType, 0)
        if dContion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, [
                dContion], { }, self.m_CondInfo)

    
    def OnRemoveRelic(self, oWarMgr, oTarget, dInfo):
        lstCondtion = []
        iSID = dInfo['iPerform']
        dContion = self.RemoveCheckSuitCondtion(oTarget, SUIT_RELIC, iSID, 0)
        if dContion:
            lstCondtion.append(dContion)
        clsRelic = cl_perform.GetPerformModule(iSID)
        if clsRelic.m_RelicType == RELIC_TYPE_CURSE:
            iRemovePreNum = oTarget.m_RelicCon.GetNumByRelicType(RELIC_TYPE_CURSE) + 1
            dContion2 = self.RemoveCheckSuitCondtion(oTarget, SUIT_RELICTYPE, (RELIC_TYPE_CURSE, iRemovePreNum), 0)
            if dContion2:
                lstCondtion.append(dContion2)
        if lstCondtion:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, oTarget.m_ID, lstCondtion, { }, self.m_CondInfo)

    
    def OnAddWeapon(self, oWarMgr, oTarget, dInfo):
        iTarget = oTarget.m_ID
        iItemID = dInfo['ItemID']
        oWeapon = oTarget.m_WieldCon.GetItemByID(iItemID)
        self.RefreshSuitShow(iTarget, SUIT_WEAPONDAMAGE, oWeapon.m_ElementType)
        self.RefreshSuitShow(iTarget, SUIT_WEAPONTYPE, oWeapon.m_Type)

    
    def OnBeforeRemoveWeapon(self, oWarMgr, oTarget, dInfo):
        iTarget = oTarget.m_ID
        if iTarget not in self.m_OldElementType:
            return None
        iItemID = dInfo['ItemID']
        oWeapon = oTarget.m_WieldCon.GetItemByID(iItemID)
        iOldElementType = self.m_OldElementType[iTarget]
        self.RefreshSuitShow(iTarget, SUIT_WEAPONDAMAGE, iOldElementType, iValue = -1)
        self.RefreshSuitShow(iTarget, SUIT_WEAPONTYPE, oWeapon.m_Type, iValue = -1)

    
    def OnAddBennd(self, oWarMgr, oTarget, dInfo):
        iSID = dInfo['Bene']
        self.AddCheckSuitCondtion(oTarget, SUIT_BENEDICTION, iSID)

    
    def OnRemoveBened(self, oWarMgr, oTarget, dInfo):
        iSID = dInfo['Bene']
        self.RemoveCheckSuitCondtion(oTarget, SUIT_BENEDICTION, iSID)

    
    def RefreshSuitShow(self, iTarget, iType, key, iValue = 0):
        if iType in self.m_Condtion and key in self.m_Condtion[iType]:
            for iSuit, _ in self.m_Condtion[iType][key]:
                if self.m_SuitShow[iTarget][iSuit]:
                    self.m_SuitShow[iTarget][iSuit] = iValue
            

    
    def AddCheckSuitCondtion(self, oTarget, iType, key, iSend = 1):
        dContion = { }
        iTarget = oTarget.m_ID
        dLimitShow = GetLimitShow()
        if iType in self.m_Condtion and key in self.m_Condtion[iType]:
            for iSuit, iConSID in self.m_Condtion[iType][key]:
                if iSuit not in self.m_CurSituate[iTarget]:
                    continue
                if self.m_CurSituate[iTarget][iSuit][iConSID]:
                    continue
                self.m_CurSituate[iTarget][iSuit][iConSID] = 1
                if iSuit not in dContion:
                    dContion[iSuit] = { }
                if iSuit >= 15004 and iSuit <= 15011:
                    SuitLog.Debug('%d %d addsuitcondition %d %d %s' % (self.m_Game.m_ID, oTarget.m_PlayerID, iSuit, iConSID, self.m_CurSituate[iTarget][iSuit]))
                dContion[iSuit][iConSID] = 1
                clsSuit = GetSuitCls(iSuit)
                if iConSID in clsSuit.m_ForeverCondition:
                    self.SetForeverCondtionInfo(oTarget, iSuit, iConSID)
                if not self.m_Enable[iTarget][iSuit]:
                    if self.MeetConditions(clsSuit, iTarget, iSuit):
                        self.UpdateSuitShowFlag(iTarget, iSuit)
                        if not self.m_SuitShow[iTarget][iSuit]:
                            bLog = True
                            if iSuit in dLimitShow:
                                self.m_SuitShow[iTarget][iSuit] = 1
                            cl_notify.SendCommonNotify(self.m_Game, [
                                oTarget.m_PlayerID], 9320, {
                                '$suitname': clsSuit.m_Name })
                            if iSuit in (15012,):
                                SendNotify2Other(oTarget, self.m_WarMgr, clsSuit)
                            else:
                                bLog = False
                        bChange = None.CheckChangeSuitNum(iTarget, iSuit)
                        self.m_Enable[iTarget][iSuit] = 1
                        if self.ChangePrioritySuit(oTarget, iSuit):
                            clsSuit.m_Action(oTarget)
                        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDSUIT, oTarget, {
                            'SuitID': iSuit,
                            'Change': bChange })
                        if bLog:
                            SuitLog.Debug('%d %d addsuit %s' % (self.m_Game.m_ID, oTarget.m_PlayerID, iSuit))
                            continue
                        continue
            
        if dContion and iSend:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, iTarget, [
                dContion], { }, self.m_CondInfo)
        return dContion

    
    def SetForeverCondtionInfo(self, oTarget, iSuit, iConSID):
        iPlayer = oTarget.m_PlayerID
        if iPlayer not in self.m_ForeverCondtionInfo:
            self.m_ForeverCondtionInfo[iPlayer] = { }
            self.m_ForeverCondtionInfo[iPlayer][(iSuit, iConSID)] = 1
        elif (iSuit, iConSID) not in self.m_ForeverCondtionInfo[iPlayer]:
            self.m_ForeverCondtionInfo[iPlayer][(iSuit, iConSID)] = 1

    
    def CheckForeverCondtionInfo(self, iPlayer, iSuit, iConSID):
        if iPlayer not in self.m_ForeverCondtionInfo:
            return False
        dForeverCondtionInfo = self.m_ForeverCondtionInfo[iPlayer]
        if (iSuit, iConSID) not in dForeverCondtionInfo:
            return False
        return True

    
    def UpdateSuitShowFlag(self, iTarget, iSuit):
        iSuitFlag = self.m_SuitShow[iTarget][iSuit]
        if iSuitFlag == -1:
            self.m_SuitShow[iTarget][iSuit] = 1

    
    def RemoveCheckSuitCondtion(self, oTarget, iType, key, iSend = 1):
        dContion = { }
        iTarget = oTarget.m_ID
        if iType in self.m_Condtion and key in self.m_Condtion[iType]:
            for iSuit, iConSID in self.m_Condtion[iType][key]:
                if iSuit not in self.m_CurSituate[iTarget]:
                    continue
                if not self.m_CurSituate[iTarget][iSuit][iConSID]:
                    continue
                if self.CheckForeverCondtionInfo(oTarget.m_PlayerID, iSuit, iConSID):
                    continue
                self.m_CurSituate[iTarget][iSuit][iConSID] = 0
                if iSuit not in dContion:
                    dContion[iSuit] = { }
                dContion[iSuit][iConSID] = 0
                clsSuit = GetSuitCls(iSuit)
                if self.m_Enable[iTarget][iSuit] and not self.MeetConditions(clsSuit, iTarget, iSuit):
                    self.m_Enable[iTarget][iSuit] = 0
                    clsSuit.m_RemoveAction(oTarget)
                    if iSuit in self.m_PrioritySuit[iTarget]:
                        lstExcludeSuit = self.RemovePrioritySuit(oTarget, iSuit)
                        for iExcludeSuit in lstExcludeSuit:
                            self.ChangePrioritySuit(oTarget, iExcludeSuit)
                        
                bChange = self.CheckChangeSuitNum(iTarget, iSuit)
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVESUIT, oTarget, {
                    'SuitID': iSuit,
                    'Change': bChange })
                if self.m_SuitShow[iTarget][iSuit] != 1:
                    SuitLog.Debug('%d %d removesuit %s' % (self.m_Game.m_ID, oTarget.m_PlayerID, iSuit))
            
        if dContion and iSend:
            cl_snetwar.GS2CUpdateSuitCondtion(self.m_Game, iTarget, [
                dContion], { }, self.m_CondInfo)
        return dContion

    
    def CheckChangeSuitNum(self, iTarget, iSuit):
        if self.m_Enable[iTarget][iSuit]:
            return False
        lstCheckSuit = GetSuitExclude(iSuit)
        for iCheckSuit in lstCheckSuit:
            if self.m_Enable[iTarget][iCheckSuit]:
                return False
        
        return True

    
    def MeetConditions(self, clsSuit, iTarget, iSuit):
        if clsSuit.m_CondFunc(self, iTarget, iSuit):
            return 1
        return 0

    
    def GetSuitByID(self, iTarget):
        if iTarget not in self.m_Enable:
            return []
        lstSuit = [ iSuit for iSuit, iEnable in self.m_Enable[iTarget].items() if iEnable ]
        return lstSuit

    
    def GetEffectiveSuitInfo(self, iTarget):
        dCondtion = self.m_CurSituate[iTarget]
        lstSuitInfo = []
        for iSuit in dCondtion:
            if not self.m_Enable[iTarget][iSuit]:
                continue
            lstSuitInfo.append(iSuit)
        
        return lstSuitInfo

    
    def SetPrioritySuit(self, oTarget, iSuit):
        iTarget = oTarget.m_ID
        if iSuit not in self.m_Enable[iTarget]:
            return None
        dPrioritySuit = oTarget.QuerySavedData('PrioritySuit', { })
        if iSuit not in self.m_PrioritySuit[iTarget]:
            lstRemove = GetSuitExclude(iSuit)
            for iRemove in lstRemove:
                self.RemovePrioritySuit(oTarget, iRemove, 0)
                dPrioritySuit.pop(iRemove, 0)
            
            self.AddPrioritySuit(oTarget, iSuit)
            dPrioritySuit[iSuit] = 1
        oTarget.SetSavedData('PrioritySuit', dPrioritySuit)

    
    def AddPrioritySuit(self, oTarget, iSuit):
        iTarget = oTarget.m_ID
        if not self.m_Enable[iTarget][iSuit]:
            return None
        lstSuitExclude = GetSuitExclude(iSuit)
        if not lstSuitExclude:
            return None
        self.m_PrioritySuit[iTarget][iSuit] = lstSuitExclude[:]
        for iExcludeSuit in lstSuitExclude:
            if not self.m_Enable[iTarget][iExcludeSuit]:
                continue
            clsSuit = GetSuitCls(iExcludeSuit)
            clsSuit.m_RemoveAction(oTarget)
        
        cl_snetwar.GS2CUpdatePrioritySuit(oTarget.m_PlayerID, list(self.m_PrioritySuit[iTarget]))

    
    def RemovePrioritySuit(self, oTarget, iSuit, iSend = 1):
        iTarget = oTarget.m_ID
        if iSuit not in self.m_PrioritySuit[iTarget]:
            return []
        for iExcludeSuit in self.m_PrioritySuit[iTarget][iSuit]:
            if not self.m_Enable[iTarget][iExcludeSuit]:
                continue
            clsSuit = GetSuitCls(iExcludeSuit)
            clsSuit.m_Action(oTarget)
        
        lstExcludeSuit = self.m_PrioritySuit[iTarget].pop(iSuit, [])
        if iSend:
            cl_snetwar.GS2CUpdatePrioritySuit(oTarget.m_PlayerID, list(self.m_PrioritySuit[iTarget]))
        return lstExcludeSuit

    
    def ChangePrioritySuit(self, oTarget, iSuit):
        iTarget = oTarget.m_ID
        lstRemove = []
        dPrioritySuit = oTarget.QuerySavedData('PrioritySuit', { })
        for iPrioritySuit, lstSuitExclude in self.m_PrioritySuit[iTarget].items():
            if iSuit in lstSuitExclude or iPrioritySuit in dPrioritySuit:
                return False
            if iSuit in dPrioritySuit or iSuit < iPrioritySuit:
                lstRemove.append(iPrioritySuit)
        else:
            return True
        if lstRemove:
            for iRemove in lstRemove:
                self.RemovePrioritySuit(oTarget, iRemove)
            
            self.AddPrioritySuit(oTarget, iSuit)
            return True
        return False

    
    def AddForbidSuit(self, iSuit):
        self.m_ForbidSuit[iSuit] = 1

    
    def AddForbidSuitCon(self, iType, args):
        dSuit = GetAllSuit()
        dExcludeSuit = GetGameExcludeSuit(self.m_WarMgr.GetPlayType())
        for iSuit in dSuit:
            if iSuit in dExcludeSuit:
                continue
            if iSuit in self.m_ForbidSuit:
                continue
            clsSuit = GetSuitCls(iSuit)
            if not clsSuit:
                continue
            iForbidCon = 0
            for iConSID, (iConditionType, iConArgs) in clsSuit.m_Condition.items():
                if iConditionType == iType and iConArgs == args:
                    iForbidCon = iConSID
                    break
            
            if iForbidCon:
                lstCon = self.m_ForbidSuitCon.setdefault(iSuit, { })
                lstCon[iForbidCon] = 1
        

    
    def AddConditionReduceNum(self, iTarget, iSuit, iReduce, sReason):
        pass

    
    def GetConditionReduceNumByReason(self, iTarget, iSuit, sReason):
        return 0

    
    def GetConditionReduceNum(self, iTarget, iSuit):
        return 0

    
    def GetEnableSuitNum(self, iHeroID):
        if iHeroID not in self.m_Enable:
            return 0
        dSuitEnable = self.m_Enable[iHeroID]
        iNum = 0
        for iEnable in dSuitEnable.values():
            if iEnable:
                iNum += 1
        
        return iNum

    
    def GetAllSuitGrade(self, iHeroID):
        if iHeroID not in self.m_Enable:
            return 0
        return sum(self.m_Enable[iHeroID].values())



def GetComponentClass(oMgrManager):
    return CSuitElement


def SendNotify2Other(oTarget, oWarMgr, clsSuit):
    lstPlayer = oWarMgr.GetRoomPlayer()
    if oTarget.m_PlayerID in lstPlayer:
        lstPlayer.remove(oTarget.m_PlayerID)
    if lstPlayer:
        cl_notify.SendCommonNotify(oTarget.m_Game, lstPlayer, 9323, {
            '$suitname': clsSuit.m_Name,
            '$$name': oTarget.m_OwnerName })

