# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/seasonsuitelement.pyc
# RelativePath: clientlogic/cl_warmgr/seasonsuitelement.pyc
# Source Generated with Decompyle++
# File: seasonsuitelement.pyc (Python 3.6)

from itertools import chain
from .suitelement import CSuitElement
from cl_commondecorator import ChooseRewardEnd
from cl_platformdata import GetSeasonSuit, GetMinorSeasonSuit, GetSeasonSuitCls, GetGameExcludeSeasonSuit, GetSeasonSuitExclude, GetCommonSeasonSuit, GetSeasonSuitTemplate, GetCardPackMaxSuitNum, GetClassicCardPack, GetTempCardPackPerform, GetActiveSourceSuitMap, GetSeasonSuitMain2Sub, GetSeasonSuitNotMain, GetSeasonSuitSub2Main
from cl_commondefines import SUIT_RELIC, SUIT_WEAPONDAMAGE, SUIT_WEAPONTYPE, SUIT_TALENT, RELIC_TYPE_CURSE, SUIT_RELICTYPE, SUIT_BENEDICTION, ALL_SUIT_TYPE, SUIT_ELEMENT, SUIT_HANDLE_OPENSUIT, SUIT_HANDLE_CLOSESUIT, THUNDERSTEP_CONDUCT_DAMAGE, FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE
from cl_commondefines import SUIT_HANDLE_ELEMENT, ALL_ELEMENT_SUIT, ATTACKERSUBMSG_NORMAL, PF_TYPE_SUITACTIVE, NPC_CB_VALUE, NPC_CB_VALUELIST, NORMAL_REDUCENUM_UI, RECYCLE_DROP, NWARRIOR_DROP_EQUIP, SUIT_HANDLE_SETTLEACCOUNTSSUIT, PF_SUBMSG_COMMON, PERFORMCHOOSE_TYPE_S4CARDPACKSUIT
from cl_only import DeepCopy, PythonError, ChooseKey, ChooseMulKeys
from cl_object.logging import SeasonsuitLog
from cl_npc import net as npcnet
from cllib import lib_flag
from cl_warmgr.bigdataanalyse import CSeasonSuitAnalyseCom
import cl_msgcenter
import cl_perform
import cl_snetwar
import cl_notify
import cl_formula
EXCLUDE_FUSESUIT = [
    15123]
BENE_REDUCESUITNUM = {
    13726: 3 }
CARDPACKCHOOSENUM = 3

class CSeasonSuitElement(CSuitElement):
    m_IsInheritSeasonElement = False
    
    def __init__(self, oGame, nid, oData):
        super(CSeasonSuitElement, self).__init__(oGame, nid, oData)
        self.m_CallFlag = 'SeasonSuitElement'
        self.m_AllSuitGradeInfo = { }
        self.m_AllSuitMaxGrade = { }
        self.m_MarkSuitInfo = { }
        self.m_SuitOpenStatus = { }
        self.m_SavedOpenStatus = { }
        self.m_SuitArg = { }
        self.m_ConditionReduceNumInfo = { }
        self.m_SavedSuitArg = { }
        self.m_SuitTemp = { }
        self.m_CanChangeSuitTemp = { }
        self.m_CanChangeCardPackTemp = { }
        self.m_ChosenInitSuit = { }
        self.m_SuitCanReduceConditionNum = { }
        dConfig = self.m_Data.m_Config
        self.m_InitChooseSuit = dConfig.get('InitChooseSuit', [])
        self.m_InitChooseSuitNum = dConfig.get('InitChooseSuitNum', 1)
        self.m_InitChooseSuitReduceNum = dConfig.get('InitChooseSuitReduceNum', 1)
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_ElementFlag = 'Element'
        self.m_SeasonSuitReduceMap = { }
        self.m_BeneTakeEffectSuit = dConfig.get('BeneTakeEffectSuit', { })
        self.m_RecycleWeaponInfo = { }
        self.m_SettleAccountsSuitInfo = { }
        self.m_SuitDamSummary = { }
        self.m_CurCardPackPerform = { }
        self.m_ExtraSeasonSuit = { }
        self.m_LastTimeOptions = { }
        self.m_PlayerMinorSuitPut = { }
        self.m_NoCarryMinorSuit = { }

    
    def Init(self):
        if not self.CheckEnable():
            return None
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnAddPlayerInfo, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, self.OnAddRelicPerform, 'AddRelicPerform' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVERELIC, self.OnRemoveRelic, 'RemoveRelic' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_INSCRIPTION_ENABLE_ELEMENTTYPE, self.OnInscriptionEnableElementType, 'InscriptionEnableElementType' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDTALENT, self.OnAddTalent, 'AddTalent' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVETALENT, self.OnRemoveTalent, 'RemoveTalent' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.OnPlayerLogin, 'PlayerLogin' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDBENED, self.OnAddBennd, 'AddBennd' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVEBENED, self.OnRemoveBened, 'RemoveBened' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnReady, 'OnRead' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, self.OpenSuit, 'OpenSuit' + self.m_CallFlag, iSub = SUIT_HANDLE_OPENSUIT)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, self.CloseSuit, 'CloseSuit' + self.m_CallFlag, iSub = SUIT_HANDLE_CLOSESUIT)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GEN_BEFOR_BENED, self.OnGenBened, 'GenBened' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RECYCLEDROP, self.OnRecycle, 'Recycle' + self.m_CallFlag, iSub = RECYCLE_DROP)

    
    def InitAfter(self):
        if not self.CheckEnable():
            return None
        oBigdataMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CSeasonSuitAnalyseCom(self.m_Game)
            oBigdataMgr.SetCom('SeasonSuit', oAnalyseCom)
        self.InitCondtion()
        self.InitSuitMap()

    
    def Release(self):
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, 'AddRelicPerform' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVERELIC, 'RemoveRelic' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_INSCRIPTION_ENABLE_ELEMENTTYPE, 'InscriptionEnableElementType' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDTALENT, 'AddTalent' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVETALENT, 'RemoveTalent' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERLOGIN, 'PlayerLogin' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDBENED, 'AddBennd' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVEBENED, 'RemoveBened' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'OnRead' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, 'OpenSuit' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CONTROL_SEASONSUIT, 'CloseSuit' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GEN_BEFOR_BENED, 'GenBened' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RECYCLEDROP, 'Recycle' + self.m_CallFlag)
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_PERFORM_START, self.m_CallFlag, iSub = PF_SUBMSG_COMMON)
        
        self.m_WarMgr = None
        self.m_Game = None

    
    def Save(self):
        dData = { }
        dData['FC'] = DeepCopy(self.m_ForeverCondtionInfo)
        dData['MSI'] = DeepCopy(self.m_MarkSuitInfo)
        dData['OS'] = DeepCopy(self.m_SuitOpenStatus)
        dData['CRN'] = DeepCopy(self.m_ConditionReduceNumInfo)
        dData['SSA'] = DeepCopy(self.m_SavedSuitArg)
        dData['ESS'] = DeepCopy(self.m_ExtraSeasonSuit)
        dData['ST'] = DeepCopy(self.m_SuitTemp)
        dData['CIS'] = dict(self.m_ChosenInitSuit)
        dData['SSRM'] = DeepCopy(self.m_SeasonSuitReduceMap)
        dData['RWI'] = dict(self.m_RecycleWeaponInfo)
        dData['SASI'] = dict(self.m_SettleAccountsSuitInfo)
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        if not self.ValidLoad(dData):
            return None
        self.m_SuitTemp = dData.get('ST', { })
        self.m_ForeverCondtionInfo = dData['FC']
        self.m_MarkSuitInfo = dData['MSI']
        self.m_SavedOpenStatus = dData.get('OS', { })
        self.m_ConditionReduceNumInfo = dData.get('CRN', { })
        self.m_SavedSuitArg = dData.get('SSA', { })
        self.m_ExtraSeasonSuit = dData.get('ESS', { })
        self.m_ChosenInitSuit = dData.get('CIS', { })
        self.m_SeasonSuitReduceMap = dData.get('SSRM', { })
        self.m_RecycleWeaponInfo = dData.get('RWI', { })
        self.m_SettleAccountsSuitInfo = dData.get('SASI', { })
        for iPlayer in self.m_SuitTemp:
            oHero = self.m_WarMgr.GetHeroByPlayer(iPlayer)
            if oHero:
                self.LoadHero(oHero)
        

    
    def ValidLoad(self, dData):
        dSuitTemp = dData.get('ST', { })
        if not dSuitTemp:
            return 0
        lstAllPlayer = self.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        if not set(lstAllPlayer) & set(dSuitTemp):
            return 0
        return 1

    
    def LoadHero(self, oHero):
        iPlayer = oHero.m_PlayerID
        self.InitEnableSuit(oHero)
        if iPlayer in self.m_SuitTemp:
            iCurSuitTemp = self.GetCurSuitTemp(iPlayer)
            iCardPack = self.GetCardPackByTempID(iPlayer, iCurSuitTemp)
            self.OnChangeCardPackPerform(oHero, iCardPack)
            self.SyncNoCarryMinorSuit(iPlayer, self.m_SuitTemp[iPlayer])
        if iPlayer in self.m_ForeverCondtionInfo:
            for iSuit, iConSID in list(self.m_ForeverCondtionInfo[iPlayer]):
                clsSuit = GetSeasonSuitCls(iSuit)
                if not clsSuit:
                    continue
                if iConSID not in clsSuit.m_Condition:
                    SeasonsuitLog.Alert('%d %d error forevercondition %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iSuit, iConSID))
                    continue
                (iType, Key) = clsSuit.m_Condition[iConSID]
                self.AddCheckSuitCondtion(oHero, iType, Key)
            
        dConditionReduceNumInfo = self.m_ConditionReduceNumInfo.get(iPlayer, { })
        if dConditionReduceNumInfo:
            self.m_ConditionReduceNumInfo[iPlayer] = { }
            for iSuit, dReduce in dConditionReduceNumInfo.items():
                self.m_ConditionReduceNumInfo[iPlayer][iSuit] = dReduce
                if iSuit not in self.m_Enable[oHero.m_ID]:
                    SeasonsuitLog.Debug('%d %d suitreduce loaderr %d' % (self.m_Game.m_ID, iPlayer, iSuit))
                    continue
                self.UpdateSuitGrade(oHero, iSuit)
            
        if iPlayer in self.m_ExtraSeasonSuit and self.m_ExtraSeasonSuit[iPlayer]:
            self.ChangeSuitTemp(oHero)

    
    def InitCondtion(self):
        dSuit = GetSeasonSuitNotMain()
        dExcludeSuit = GetGameExcludeSeasonSuit(self.m_WarMgr.GetPlayType())
        for iType in ALL_SUIT_TYPE:
            self.m_Condtion[iType] = { }
        
        for iSuit in dSuit:
            if iSuit in dExcludeSuit:
                continue
            if iSuit in self.m_ForbidSuit:
                continue
            clsSuit = GetSeasonSuitCls(iSuit)
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
                dType = self.m_Condtion[iConditionType]
                tSuitInfo = (iSuit, iConSID)
                if iConArgs not in dType:
                    dType[iConArgs] = []
                dType[iConArgs].append(tSuitInfo)
                self.m_Condtion[iConditionType] = dType
            
        

    
    def InitSuitMap(self):
        dSuit = GetSeasonSuitNotMain()
        dExcludeSuit = GetGameExcludeSeasonSuit(self.m_WarMgr.GetPlayType())
        for iType in ALL_SUIT_TYPE:
            self.m_SuitMap[iType] = { }
        
        for iSuit in dSuit:
            if iSuit in dExcludeSuit:
                continue
            if iSuit in self.m_ForbidSuit:
                continue
            clsSuit = GetSeasonSuitCls(iSuit)
            self.m_AllSuitGradeInfo[iSuit] = clsSuit.m_GradeInfo
            iMaxGrade = clsSuit.m_MaxGrade
            self.m_AllSuitMaxGrade[iSuit] = iMaxGrade
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
            
            iNeedConditionNum = 0
            for iNeed in self.m_CondInfo[iSuit][1].values():
                if iNeed:
                    iNeedConditionNum += 1
            
            self.m_SuitCanReduceConditionNum[iSuit] = self.m_AllSuitGradeInfo[iSuit][iMaxGrade] - iNeedConditionNum
        

    
    def OnAddPlayerInfo(self, _oListener, oWarMgr, dInfo):
        oHero = dInfo['Hero']
        dPlayerInfo = dInfo['Info']
        iHero = oHero.m_ID
        iPlayerID = oHero.m_PlayerID
        if iPlayerID not in self.m_SuitOpenStatus:
            self.m_SuitOpenStatus[iPlayerID] = { }
        if iPlayerID not in self.m_SuitArg:
            self.m_SuitArg[iPlayerID] = { }
        self.SetPlayerMinorSuitPut(oHero)
        dSeasonSuit = dPlayerInfo.get('SeasonSuit', { })
        if iPlayerID not in self.m_SuitTemp:
            (lstSuitTemp, iExtraNum) = self.GetFilterSuitTemp(dSeasonSuit.get('SuitTemp', []))
            iCardPack = dSeasonSuit.get('CardPack', GetClassicCardPack())
            self.InitCardPackPerform(oHero, iCardPack)
            self.SetSuitTemp(iPlayerID, dSeasonSuit.get('CurTemp', 0), iCardPack, lstSuitTemp, dSeasonSuit.get('ForceTemp', 0), iExtraNum)
            self.InitEnableSuit(oHero)
        else:
            self.LoadHero(oHero)
        self.SetCanChangeSuitTemp(iPlayerID, dSeasonSuit.get('CustomSuitTemp', { }), dSeasonSuit.get('CustomCardPackTemp', { }))
        self.m_PrioritySuit[iHero] = { }
        if iPlayerID not in self.m_MarkSuitInfo:
            self.m_MarkSuitInfo[iPlayerID] = { }
        if iPlayerID not in self.m_SavedSuitArg:
            self.m_SavedSuitArg[iPlayerID] = { }
        if iPlayerID not in self.m_ExtraSeasonSuit:
            self.m_ExtraSeasonSuit[iPlayerID] = { }

    
    def GetFilterSuitTemp(self, lstSuitTemp):
        dMain2Sub = GetSeasonSuitMain2Sub()
        dSub2Main = GetSeasonSuitSub2Main()
        lstNewSuitTemp = []
        iExtraNum = 0
        lstCountMain = []
        for iSuit in lstSuitTemp:
            if iSuit in dMain2Sub:
                lstNewSuitTemp.extend(dMain2Sub[iSuit])
                iExtraNum += len(dMain2Sub[iSuit]) - 1
                continue
            if iSuit in dSub2Main:
                iMainSuit = dSub2Main[iSuit]
                if iMainSuit in lstCountMain:
                    continue
                if iMainSuit not in dMain2Sub:
                    continue
                lstCountMain.append(iMainSuit)
                lstNewSuitTemp.extend(dMain2Sub[iMainSuit])
                iExtraNum += len(dMain2Sub[iMainSuit]) - 1
                continue
            lstNewSuitTemp.append(iSuit)
        
        return (lstNewSuitTemp, iExtraNum)

    
    def SetSuitTemp(self, pid, iCurTemp, iCardPack, lstSuitTemp, iForceTemp, iExtraNum):
        oGame = self.m_Game
        dSeasonSuit = GetSeasonSuitNotMain()
        if pid in self.m_ExtraSeasonSuit and self.m_ExtraSeasonSuit[pid]:
            iExtraNum += len(self.m_ExtraSeasonSuit[pid])
        if not iCardPack:
            iCardPack = GetClassicCardPack()
        iTempSuitNum = GetCardPackMaxSuitNum(iCardPack) + iExtraNum
        for iSuit in lstSuitTemp:
            if iSuit not in dSeasonSuit:
                SeasonsuitLog.Alert('%s %s seasonsuit %s not put %s' % (oGame.m_ID, pid, iSuit, lstSuitTemp))
                lstSuitTemp = []
                break
        
        if len(lstSuitTemp) != iTempSuitNum:
            if lstSuitTemp:
                SeasonsuitLog.Alert('%s %s suitemp %s %s invalid' % (oGame.m_ID, pid, iCurTemp, lstSuitTemp))
            dSeasonSuitTemp = GetSeasonSuitTemplate()
            dChooseWeight = dict.fromkeys(list(dSeasonSuitTemp), 10)
            iCurTemp = ChooseKey(oGame, dChooseWeight)
            lstSuitTemp = dSeasonSuitTemp[iCurTemp]
            (lstSuitTemp, _) = self.GetFilterSuitTemp(lstSuitTemp)
            oHero = self.m_WarMgr.GetHeroByPlayer(pid)
            if oHero:
                self.OnChangeCardPackPerform(oHero, GetClassicCardPack())
        SeasonsuitLog.Debug('%s %s setsuittemp %s %s %s' % (oGame.m_ID, pid, iCurTemp, iCardPack, lstSuitTemp))
        dSuitTempInfo = {
            iCurTemp: list(lstSuitTemp) }
        self.m_SuitTemp[pid] = dSuitTempInfo
        self.SyncNoCarryMinorSuit(pid, dSuitTempInfo)

    
    def SyncNoCarryMinorSuit(self, iPlayerID, dSuitTempInfo):
        dMinorSuit = self.m_PlayerMinorSuitPut[iPlayerID] if iPlayerID in self.m_PlayerMinorSuitPut else { }
        dSeasonSuitSub2Main = GetSeasonSuitSub2Main()
        lstSuitTemp = list(dSuitTempInfo.values())[0]
        for iSuit in lstSuitTemp:
            if iSuit in dSeasonSuitSub2Main and dSeasonSuitSub2Main[iSuit] in dMinorSuit:
                dMinorSuit.pop(dSeasonSuitSub2Main[iSuit])
            if iSuit in dMinorSuit:
                dMinorSuit.pop(iSuit)
        
        self.m_NoCarryMinorSuit[iPlayerID] = dMinorSuit

    
    def ChangeSuitTemp(self, oHero, iCurTemp = 0):
        iPlayerID = oHero.m_PlayerID
        if not iCurTemp:
            iCurTemp = self.GetCurSuitTemp(iPlayerID)
        iCardPack = self.GetCardPackByTempID(iPlayerID, iCurTemp)
        if iPlayerID not in self.m_CanChangeSuitTemp:
            cl_snetwar.GS2CSetSuitTempResult(iPlayerID, iCurTemp, iResult = 0)
            return None
        dCanChangeSuitTemp = self.m_CanChangeSuitTemp[iPlayerID]
        if iCurTemp not in dCanChangeSuitTemp:
            cl_snetwar.GS2CSetSuitTempResult(iPlayerID, iCurTemp, iResult = 0)
            return None
        lstNewSuit = dCanChangeSuitTemp[iCurTemp]
        self.OnChangeSuitTemp(oHero, iCurTemp, iCardPack, lstNewSuit)

    
    def OnChangeSuitTemp(self, oHero, iCurTemp, iCardPack, lstNewSuit):
        iHero = oHero.m_ID
        iPlayerID = oHero.m_PlayerID
        iOldSuitTemp = self.GetCurSuitTemp(iPlayerID)
        lstOldSuit = self.m_SuitTemp[iPlayerID][iOldSuitTemp]
        dEnableSuit = self.m_Enable[iHero]
        dCurSituate = self.m_CurSituate[iHero]
        if iPlayerID in self.m_ExtraSeasonSuit and self.m_ExtraSeasonSuit[iPlayerID]:
            for iExtra in self.m_ExtraSeasonSuit[iPlayerID]:
                if iExtra not in lstNewSuit:
                    lstNewSuit.append(iExtra)
            
        (lstNewSuit, iExtraNum) = self.GetFilterSuitTemp(lstNewSuit)
        iForceTemp = 0
        lstKeepSuit = []
        dMarkSuitInfo = self.m_MarkSuitInfo[iPlayerID]
        dSuitOpenStatus = self.m_SuitOpenStatus[iPlayerID]
        for iSuit in lstOldSuit:
            if iSuit in lstNewSuit:
                lstKeepSuit.append(iSuit)
                continue
            if iSuit in dEnableSuit:
                iSuitGrade = dEnableSuit.pop(iSuit)
                if iSuitGrade:
                    dSuitOpenStatus.pop(iSuit, 0)
                    clsSuit = GetSeasonSuitCls(iSuit)
                    self.RemoveAction(clsSuit, oHero, iSuitGrade)
            if iSuit in dCurSituate:
                dCurSituate.pop(iSuit)
            if iSuit in dMarkSuitInfo:
                dMarkSuitInfo.pop(iSuit)
        
        iCareer = oHero.m_Career
        dExcludeSuit = GetGameExcludeSeasonSuit(self.m_WarMgr.GetPlayType())
        for iSuit in lstNewSuit:
            if iSuit not in dMarkSuitInfo:
                dMarkSuitInfo[iSuit] = 1
            if iSuit in lstKeepSuit:
                continue
            self.InitSuitCurSituate(iHero, iSuit, dExcludeSuit, iCareer)
            self.UpdateSuitGrade(oHero, iSuit, iSend = 0)
        
        if iCurTemp != self.GetCurSuitTemp(iPlayerID):
            self.OnChangeCardPackPerform(oHero, iCardPack)
        self.SetSuitTemp(iPlayerID, iCurTemp, iCardPack, lstNewSuit, iForceTemp, iExtraNum)
        cl_snetwar.GS2CSetSuitTempResult(iPlayerID, iCurTemp, iResult = 1)
        self.SyncSuitCondtion(oHero)
        self.RefreshSuitOpenStatus(oHero)
        lstHasRelic = oHero.m_RelicCon.GetAllRelicSID()
        oWarMgr = self.m_WarMgr
        for iRelic in lstHasRelic:
            self.OnAddRelicPerform(oWarMgr, oHero, {
                'iPerform': iRelic })
        
        cl_snetwar.GS2CMarkSeasonSuit(iPlayerID, self.m_MarkSuitInfo[iPlayerID])

    
    def OnAddSuitTempExtraSeasonSuit(self, oHero, iNewSuit):
        iPlayerID = oHero.m_PlayerID
        iCurTemp = self.GetCurSuitTemp(iPlayerID)
        iCardPack = self.GetCardPackByTempID(iPlayerID, iCurTemp)
        iOldSuitTemp = self.GetCurSuitTemp(iPlayerID)
        lstOldSuit = self.m_SuitTemp[iPlayerID][iOldSuitTemp]
        if lstOldSuit:
            lstNewSuit = list(lstOldSuit)
            lstNewSuit.append(iNewSuit)
        else:
            lstNewSuit = [
                iNewSuit]
        (lstNewSuit, iExtraNum) = self.GetFilterSuitTemp(lstNewSuit)
        dMain2Sub = GetSeasonSuitMain2Sub()
        if iNewSuit in dMain2Sub:
            self.TrueAddSuitTempExtraSuit(oHero, dMain2Sub[iNewSuit])
        else:
            self.TrueAddSuitTempExtraSuit(oHero, [
                iNewSuit])
        self.SetSuitTemp(iPlayerID, iCurTemp, iCardPack, lstNewSuit, 1, iExtraNum)
        cl_snetwar.GS2CSetSuitTempResult(iPlayerID, iCurTemp, iResult = 1)
        self.SyncSuitCondtion(oHero, iNewSuit)
        lstHasRelic = oHero.m_RelicCon.GetAllRelicSID()
        oWarMgr = self.m_WarMgr
        for iRelic in lstHasRelic:
            self.OnAddRelicPerform(oWarMgr, oHero, {
                'iPerform': iRelic })
        
        cl_snetwar.GS2CMarkSeasonSuit(iPlayerID, self.m_MarkSuitInfo[iPlayerID])

    
    def TrueAddSuitTempExtraSuit(self, oHero, lstNewSuit):
        iHero = oHero.m_ID
        iCareer = oHero.m_Career
        dExcludeSuit = GetGameExcludeSeasonSuit(self.m_WarMgr.GetPlayType())
        for iNewSuit in lstNewSuit:
            self.InitSuitCurSituate(iHero, iNewSuit, dExcludeSuit, iCareer)
            self.UpdateSuitGrade(oHero, iNewSuit)
        

    
    def SetCanChangeSuitTemp(self, iPlayerID, dSuitTemp, dCardPackTemp):
        self.m_CanChangeSuitTemp[iPlayerID] = { }
        self.m_CanChangeCardPackTemp[iPlayerID] = { }
        for iTempID, dSuit in dSuitTemp.items():
            lstSuit = []
            for lstTempSuit in dSuit.values():
                lstSuit.extend(lstTempSuit)
            
            self.m_CanChangeSuitTemp[iPlayerID][iTempID] = lstSuit
        
        for iTempID, iCardPack in dCardPackTemp.items():
            self.m_CanChangeCardPackTemp[iPlayerID][iTempID] = iCardPack
        
        dSeasonSuitTemp = GetSeasonSuitTemplate()
        for iTempID, lstSuit in dSeasonSuitTemp.items():
            self.m_CanChangeSuitTemp[iPlayerID][iTempID] = list(lstSuit)
            self.m_CanChangeCardPackTemp[iPlayerID][iTempID] = GetClassicCardPack()
        

    
    def SetPlayerMinorSuitPut(self, oHero):
        iPlayerID = oHero.m_PlayerID
        dExcludeSuit = GetGameExcludeSeasonSuit(self.m_WarMgr.GetPlayType())
        dMinorSuit = GetMinorSeasonSuit()
        dCommonSuit = GetCommonSeasonSuit()
        dSeasonSuitSub2Main = GetSeasonSuitSub2Main()
        for iSuitSub in dSeasonSuitSub2Main:
            if iSuitSub in dMinorSuit:
                dMinorSuit.pop(iSuitSub)
        
        dPlayerMinorSuitPut = { }
        for iMinor in dMinorSuit:
            if iMinor in EXCLUDE_FUSESUIT:
                continue
            if iMinor in dExcludeSuit or iMinor in dCommonSuit:
                continue
            clsSuit = GetSeasonSuitCls(iMinor)
            if clsSuit and clsSuit.m_Career:
                continue
            dPlayerMinorSuitPut[iMinor] = 1
        
        self.m_PlayerMinorSuitPut[iPlayerID] = dPlayerMinorSuitPut

    
    def GetChangeSuitTempInfo(self, iPlayerID):
        if iPlayerID in self.m_CanChangeSuitTemp:
            return self.m_CanChangeSuitTemp[iPlayerID]
        return { }

    
    def GetCardPackByTempID(self, iPlayerID, iTempID):
        if iPlayerID in self.m_CanChangeCardPackTemp and iTempID in self.m_CanChangeCardPackTemp[iPlayerID]:
            return self.m_CanChangeCardPackTemp[iPlayerID][iTempID]
        return 0

    
    def AddExtraSeasonSuit(self, iPlayerID, iExtra):
        if iPlayerID not in self.m_ExtraSeasonSuit or iExtra not in GetSeasonSuit():
            return None
        self.m_ExtraSeasonSuit[iPlayerID][iExtra] = 1

    
    def OnShowMultiChoose(self, oHero):
        iPlayer = oHero.m_PlayerID
        oGame = self.m_Game
        iGame = oGame.m_ID
        if iPlayer in self.m_LastTimeOptions and self.m_LastTimeOptions[iPlayer]:
            dOptionSuit = self.m_LastTimeOptions[iPlayer]
        elif iPlayer not in self.m_NoCarryMinorSuit:
            SeasonsuitLog.Debug('%s %d get minorsuit fail' % (iGame, iPlayer))
            return None
        dNoCarryMinorSuit = self.m_NoCarryMinorSuit[iPlayer]
        if not dNoCarryMinorSuit:
            cl_notify.SendCommonNotify(oGame, [
                iPlayer], 2431, { })
            return None
        lstOptionSuit = ChooseMulKeys(oGame, dNoCarryMinorSuit, CARDPACKCHOOSENUM)
        dOptionSuit = dict.fromkeys(lstOptionSuit, 1)
        self.m_LastTimeOptions[iPlayer] = dOptionSuit
        SeasonsuitLog.Info('%s %d cardpack suit reward %s' % (iGame, iPlayer, dOptionSuit))
        npcnet.GS2CChoosePerform(oHero, list(dOptionSuit.items()), PERFORMCHOOSE_TYPE_S4CARDPACKSUIT)
        npcnet.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.OnChooseOption)

    
    def OnChooseOption(self, oHero, iSuitSID):
        iPlayer = oHero.m_PlayerID
        iGame = self.m_Game.m_ID
        SeasonsuitLog.Debug('%s %d cardpackpassive choose reward %s' % (iGame, iPlayer, iSuitSID))
        if iSuitSID not in GetSeasonSuit():
            SeasonsuitLog.Debug('%s %d %s not exist' % (iGame, iPlayer, iSuitSID))
            return None
        if iSuitSID in list(self.GetSuitTemp(iPlayer).values())[0]:
            SeasonsuitLog.Debug('%s %d %s allready in cardpack' % (iGame, iPlayer, iSuitSID))
            return None
        oHero.CostFuncModeTimes(FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE, 1)
        self.m_LastTimeOptions[iPlayer] = { }
        self.AddExtraSeasonSuit(iPlayer, iSuitSID)
        self.OnAddSuitTempExtraSeasonSuit(oHero, iSuitSID)
        if oHero.GetFuncModeTimes(FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE):
            self.OnShowMultiChoose(oHero)

    
    def OnAddAllPlayer(self, _oListener, oWarMgr, dInfo):
        for pid in self.m_SuitOpenStatus:
            if pid not in self.m_SavedOpenStatus:
                continue
            oHero = oWarMgr.GetHeroByPlayer(pid)
            if oHero:
                self.ChangeSuitOpenStatus(oHero, self.m_SavedOpenStatus[pid])
        
        if not (oWarMgr.m_IsUseRecord) and not oWarMgr.IsTransferGame():
            for pid, dTempInfo in self.m_SuitTemp.items():
                oHero = oWarMgr.GetHeroByPlayer(pid)
                if oHero:
                    for lstTemp in dTempInfo.values():
                        self.SetMarkSuit(oHero, dict.fromkeys(lstTemp, 1))
                    
            

    
    def OnAddPlayer(self, _oListener, oWarMgr, dInfo):
        oHero = dInfo['oCtrlHero']
        if oHero.m_PlayerID not in self.m_ChosenInitSuit:
            cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.AutoChooseInitSuit, self.m_CallFlag)
            oHero.AddMapLoadOKCbFun(self.m_CallFlag, self.SendInitReduceSuit, iPriority = 1, iOnce = 1)

    
    def SendInitReduceSuit(self, oHero, dMsgInfo):
        if self.m_InitChooseSuitNum <= 0:
            return 1
        if oHero.m_PlayerID in self.m_ChosenInitSuit:
            return 1
        lstSuit = []
        iHero = oHero.m_ID
        for iSuit in self.m_InitChooseSuit:
            if iSuit in self.m_Enable[iHero] and self.CheckCondiReduce(iHero, iSuit):
                lstSuit.append(iSuit)
        
        if not lstSuit:
            return 1
        npcnet.GS2COpenReduceSuitTakeEffectAmountUI(oHero, lstSuit, self.m_InitChooseSuitNum, NORMAL_REDUCENUM_UI)
        npcnet.SetNpcUICallBackFunction(oHero, NPC_CB_VALUELIST, self.PlayerChooseInitSuit)
        npcnet.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, CheckCondiReduce)
        return 0

    
    def PlayerChooseInitSuit(self, oHero, lstAnswer):
        iPlayerID = oHero.m_PlayerID
        if iPlayerID in self.m_ChosenInitSuit:
            return 1
        iHero = oHero.m_ID
        for iSuit in lstAnswer:
            if iSuit not in self.m_Enable[iHero] or iSuit not in self.m_InitChooseSuit:
                SeasonsuitLog.Debug('%s %s initchosen %s err' % (self.m_Game.m_ID, iPlayerID, iSuit))
                return 0
            if not self.CheckCondiReduce(iPlayerID, iSuit):
                SeasonsuitLog.Debug('%s %s chosen %s cant reduce' % (self.m_Game.m_ID, iPlayerID, iSuit))
                return 0
        
        SeasonsuitLog.Debug('%s %s initchosen %s %s' % (self.m_Game.m_ID, iPlayerID, lstAnswer, self.m_InitChooseSuitNum))
        lstSuit = lstAnswer[:self.m_InitChooseSuitNum]
        self.m_ChosenInitSuit[iPlayerID] = lstSuit
        if not lstSuit:
            return 1
        for iSuit in lstSuit:
            clsSuit = GetSeasonSuitCls(iSuit)
            self.SuitCondiReduce(oHero, clsSuit, self.m_InitChooseSuitReduceNum, 'InitChosen')
        
        return 1

    PlayerChooseInitSuit = ChooseRewardEnd(PlayerChooseInitSuit)
    
    def AutoChooseInitSuit(self, oListener, oWarMgr, dMsgInfo):
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_CallFlag)
        oGame = self.m_Game
        for iHero in oWarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHero)
            if oHero and oHero.m_PlayerID not in self.m_ChosenInitSuit:
                oHero.RemoveMapLoadOKCbFun(self.m_CallFlag, iPriority = 1)
                self.m_ChosenInitSuit[oHero.m_PlayerID] = []
        

    
    def EnableSuitDamSummary(self, iHero, iSuit, lstPerform):
        dSummary = self.m_SuitDamSummary.setdefault(iHero, { })
        if not dSummary:
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnPerformStart, self.m_CallFlag, iSub = PF_SUBMSG_COMMON)
        for iPerform in lstPerform:
            dSummary[iPerform] = iSuit
        

    
    def DisableSuitDamSummary(self, iHero, iDisableSuit):
        if iHero not in self.m_SuitDamSummary:
            return None
        dSummary = { }
        for iPerform, iSuit in self.m_SuitDamSummary[iHero].items():
            if iDisableSuit == iSuit:
                continue
            dSummary[iPerform] = iSuit
        
        self.m_SuitDamSummary[iHero] = dSummary
        if not dSummary:
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_PERFORM_START, self.m_CallFlag, iSub = PF_SUBMSG_COMMON)

    
    def OnPerformStart(self, _oListener, oHero, dMsgInfo):
        iHeroID = oHero.m_ID
        if iHeroID not in self.m_SuitDamSummary or 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        iPerformSID = oSkill.m_Base['pfid']
        dSummary = self.m_SuitDamSummary[iHeroID]
        if iPerformSID not in dSummary:
            return None
        oSkill.m_Collect['ExShowTips'] = THUNDERSTEP_CONDUCT_DAMAGE

    
    def GetDamageSourceSuit(self, iHero, oSkill):
        iPerform = oSkill.m_Base['pfid']
        iSuit = 0
        if oSkill.m_Base['PFType'] == PF_TYPE_SUITACTIVE:
            dSuitMap = GetActiveSourceSuitMap()
            if iPerform in dSuitMap:
                iSuit = dSuitMap[iPerform]
            elif iHero in self.m_SuitDamSummary and iPerform in self.m_SuitDamSummary[iHero]:
                iSuit = self.m_SuitDamSummary[iHero][iPerform]

    
    def InitCardPackPerform(self, oHero, iCardPack):
        lstInitPerform = GetTempCardPackPerform(iCardPack)
        if lstInitPerform:
            self.m_CurCardPackPerform[oHero.m_PlayerID] = lstInitPerform
            for iPerform in lstInitPerform:
                oHero.AddPerform(iPerform, 1)
            

    
    def OnChangeCardPackPerform(self, oHero, iNewCardPack):
        iPlayerID = oHero.m_PlayerID
        if iPlayerID in self.m_CurCardPackPerform:
            for iPerform in self.m_CurCardPackPerform[iPlayerID]:
                oHero.RemovePerform(iPerform)
            
            self.m_CurCardPackPerform.pop(iPlayerID)
        self.InitCardPackPerform(oHero, iNewCardPack)

    
    def GetCurCardPackPerform(self, iPlayer):
        if iPlayer not in self.m_CurCardPackPerform:
            return []
        return self.m_CurCardPackPerform[iPlayer]

    
    def InitEnableSuit(self, oHero):
        iHero = oHero.m_ID
        iCareer = oHero.m_Career
        iPlayerID = oHero.m_PlayerID
        self.m_Enable[iHero] = { }
        self.m_CurSituate[iHero] = { }
        dExcludeSuit = GetGameExcludeSeasonSuit(self.m_WarMgr.GetPlayType())
        dCommonSuit = GetCommonSeasonSuit()
        if iPlayerID in self.m_SuitTemp:
            dSuitTempInfo = self.m_SuitTemp[iPlayerID]
            lstSuitTemp = list(dSuitTempInfo.values())[0]
        else:
            lstSuitTemp = []
        (lstSuitTemp, _) = self.GetFilterSuitTemp(lstSuitTemp)
        SeasonsuitLog.Debug('%s %s suittemp %s' % (self.m_Game.m_ID, iPlayerID, lstSuitTemp))
        for iSuit in chain(dCommonSuit, lstSuitTemp):
            self.InitSuitCurSituate(iHero, iSuit, dExcludeSuit, iCareer)
        
        self.SyncSuitCondtion(oHero)

    
    def InitSuitCurSituate(self, iHero, iSuit, dExcludeSuit, iCareer):
        if iSuit in dExcludeSuit:
            return None
        if iSuit in self.m_ForbidSuit:
            return None
        clsSuit = GetSeasonSuitCls(iSuit)
        if clsSuit.m_Career and iCareer != clsSuit.m_Career:
            return None
        lstForbidCon = self.m_ForbidSuitCon.get(iSuit, [])
        self.m_CurSituate[iHero][iSuit] = { }
        self.m_Enable[iHero][iSuit] = 0
        for iConSID in clsSuit.m_Condition:
            if iConSID in lstForbidCon:
                continue
            self.m_CurSituate[iHero][iSuit][iConSID] = 0
        

    
    def OnPlayerLogin(self, oWarMgr, oTarget, dInfo):
        
        try:
            cl_snetwar.GS2CSeasonSuitMap(self, oTarget.m_PlayerID)
            self.SyncSuitCondtion(oTarget)
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
                    cl_snetwar.GS2CUpdateSeasonSuitCondtion(self.m_Game, self, oHero.m_ID, [
                        dTempContion], {
                        oTarget.m_PlayerID: 1 }, self.m_CondInfo)
            
        except:
            PythonError()


    
    def SyncSuitCondtion(self, oTarget, iSuit = 0):
        
        try:
            iTarget = oTarget.m_ID
            self.ShowSuitTempList(oTarget.m_PlayerID)
            if iTarget not in self.m_CurSituate:
                return None
            dContion = { }
            if iSuit:
                dMain2Sub = GetSeasonSuitMain2Sub()
                if iSuit in dMain2Sub:
                    for iSubSuit in dMain2Sub[iSuit]:
                        dContion[iSubSuit] = self.m_CurSituate[iTarget].get(iSubSuit, { })
                    
                else:
                    dContion[iSuit] = self.m_CurSituate[iTarget].get(iSuit, { })
                iClearData = 0
            else:
                dContion = self.m_CurSituate[iTarget]
                iClearData = 1
            if dContion:
                cl_snetwar.GS2CUpdateSeasonSuitCondtion(self.m_Game, self, iTarget, [
                    dContion], { }, self.m_CondInfo, iClearData = iClearData)
        except:
            PythonError()


    
    def OnReady(self, oWarMgr, oTarget, dInfo):
        
        try:
            iPlayerID = oTarget.m_PlayerID
            dMarkSuitInfo = self.m_MarkSuitInfo
            if iPlayerID not in dMarkSuitInfo:
                dMarkSuitInfo[iPlayerID] = { }
                SeasonsuitLog.Debug('%s %s ready err %s' % (self.m_Game.m_ID, iPlayerID, dMarkSuitInfo))
            cl_snetwar.GS2CMarkSeasonSuit(oTarget.m_PlayerID, dMarkSuitInfo[iPlayerID])
            self.RefreshSuitOpenStatus(oTarget)
            self.RefreshAllSuitElement(oTarget)
            self.UpdateSeasonSuitReduceInfo(iPlayerID)
            self.UpdateSettleAccountsSuitInfo(oTarget)
        except:
            PythonError()


    
    def SetMarkSuit(self, oHero, dMarkSuit):
        dNewMarkSuit = { }
        dCurSituate = self.m_CurSituate[oHero.m_ID]
        for iSuit, iVal in dMarkSuit.items():
            if iSuit not in dCurSituate:
                continue
            dNewMarkSuit[iSuit] = iVal
        
        iPlayerID = oHero.m_PlayerID
        self.m_MarkSuitInfo[iPlayerID] = dNewMarkSuit
        cl_snetwar.GS2CMarkSeasonSuit(iPlayerID, dNewMarkSuit)

    
    def OpenSuit(self, oWarMgr, oHero, dMsgInfo):
        lstOpenSuit = dMsgInfo['Result']
        SeasonsuitLog.Debug('%s %s opensuit %s' % (self.m_Game.m_ID, oHero.m_PlayerID, lstOpenSuit))
        self.ChangeSuitOpenStatus(oHero, dict.fromkeys(lstOpenSuit, 1))

    
    def CloseSuit(self, oWarMgr, oHero, dMsgInfo):
        lstOpenSuit = dMsgInfo['Result']
        SeasonsuitLog.Debug('%s %s closesuit %s' % (self.m_Game.m_ID, oHero.m_PlayerID, lstOpenSuit))
        self.ChangeSuitOpenStatus(oHero, dict.fromkeys(lstOpenSuit, 0))

    
    def ChangeSuitOpenStatus(self, oHero, dSuit):
        iHero = oHero.m_ID
        dSuitOpenStatus = self.m_SuitOpenStatus[oHero.m_PlayerID]
        for iSuit, iOpen in dSuit.items():
            if iSuit not in self.m_Enable[iHero] or self.m_Enable[iHero][iSuit] <= 0:
                continue
            if iSuit in dSuitOpenStatus and iOpen == dSuitOpenStatus[iSuit]:
                continue
            self.UpdateSuitOpenStatus(oHero, iSuit, iOpen)
        
        self.RefreshSuitOpenStatus(oHero)

    
    def UpdateSuitOpenStatus(self, oHero, iSuit, iNewOpenStatus):
        iHero = oHero.m_ID
        dSuitOpenStatus = self.m_SuitOpenStatus[oHero.m_PlayerID]
        if iSuit in dSuitOpenStatus and iNewOpenStatus == dSuitOpenStatus[iSuit]:
            return None
        SeasonsuitLog.Debug('%s %s openstatus %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iSuit, iNewOpenStatus))
        dSuitOpenStatus[iSuit] = iNewOpenStatus
        iSuitGrade = self.m_Enable[iHero][iSuit]
        clsSuit = GetSeasonSuitCls(iSuit)
        dSuitArg = self.m_SuitArg[oHero.m_PlayerID]
        if iNewOpenStatus:
            for iExcludeSuit in GetSeasonSuitExclude(iSuit):
                if iExcludeSuit not in self.m_Enable[iHero]:
                    continue
                iExcludeSuitGrade = self.m_Enable[iHero][iExcludeSuit]
                clsExcludeSuit = GetSeasonSuitCls(iExcludeSuit)
                if iExcludeSuitGrade > 0 and dSuitOpenStatus.get(iExcludeSuit, 1):
                    dSuitOpenStatus[iExcludeSuit] = 0
                    dSuitArg.pop(iExcludeSuit, { })
                    self.RemoveAction(clsExcludeSuit, oHero, iExcludeSuitGrade)
            
            self.ActiveAction(clsSuit, oHero, iSuitGrade)
        else:
            dSuitArg.pop(iSuit, { })
            if iSuitGrade > 0:
                self.RemoveAction(clsSuit, oHero, iSuitGrade)

    
    def UpdateSuitGrade(self, oHero, iSuit, iSend = 1):
        iHero = oHero.m_ID
        if iSuit not in self.m_Enable[iHero]:
            return None
        clsSuit = GetSeasonSuitCls(iSuit)
        if not clsSuit:
            return None
        iSuitGrade = self.m_Enable[iHero][iSuit]
        iNewGrade = self.MeetConditions(clsSuit, iHero, iSuit)
        iUpdateSuitOpenStatus = 0
        if iSuitGrade != iNewGrade:
            self.m_Enable[iHero][iSuit] = iNewGrade
            dSuitOpenStatus = self.m_SuitOpenStatus[oHero.m_PlayerID]
            dSuitArg = self.m_SuitArg[oHero.m_PlayerID]
            if iNewGrade <= 0:
                if iSuit in dSuitOpenStatus and dSuitOpenStatus[iSuit]:
                    self.RemoveAction(clsSuit, oHero, iSuitGrade)
                dSuitOpenStatus.pop(iSuit)
                dSuitArg.pop(iSuit, { })
                iUpdateSuitOpenStatus = 1
            elif iSuit not in dSuitOpenStatus:
                for iExcludeSuit in GetSeasonSuitExclude(iSuit):
                    if iExcludeSuit in dSuitOpenStatus and dSuitOpenStatus[iExcludeSuit]:
                        dSuitOpenStatus[iSuit] = 0
                        break
                
                iUpdateSuitOpenStatus = 1
            elif dSuitOpenStatus[iSuit]:
                if iSuitGrade > 0:
                    self.RemoveAction(clsSuit, oHero, iSuitGrade)
                self.ActiveAction(clsSuit, oHero, iNewGrade)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPDATESEASONSUITGRADE, oHero, {
            'Suit': iSuit })
        if iSend and iUpdateSuitOpenStatus:
            self.RefreshSuitOpenStatus(oHero)

    
    def RefreshSuitOpenStatus(self, oHero):
        oGame = self.m_Game
        lstOpenSuit = []
        lstCloseSuit = []
        dSuitOpenStatus = self.m_SuitOpenStatus[oHero.m_PlayerID]
        for iSuit, iOpen in dSuitOpenStatus.items():
            if iOpen:
                lstOpenSuit.append(iSuit)
                continue
            lstCloseSuit.append(iSuit)
        
        cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_OPENSUIT, lstOpenSuit, oGame, oHero)
        cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_CLOSESUIT, lstCloseSuit, oGame, oHero)

    
    def AddCheckSuitCondtion(self, oTarget, iType, key, iSend = 1):
        iTarget = oTarget.m_ID
        if iTarget not in self.m_CurSituate or iType not in self.m_Condtion:
            return { }
        dContion = { }
        if key in self.m_Condtion[iType]:
            for iSuit, iConSID in self.m_Condtion[iType][key]:
                if iSuit not in self.m_CurSituate[iTarget]:
                    continue
                if self.m_CurSituate[iTarget][iSuit][iConSID]:
                    continue
                self.m_CurSituate[iTarget][iSuit][iConSID] = 1
                if iSuit not in dContion:
                    dContion[iSuit] = { }
                dContion[iSuit][iConSID] = 1
                clsSuit = GetSeasonSuitCls(iSuit)
                if iConSID in clsSuit.m_ForeverCondition:
                    self.SetForeverCondtionInfo(oTarget, iSuit, iConSID)
                self.UpdateSuitGrade(oTarget, iSuit)
            
        if dContion and iSend:
            cl_snetwar.GS2CUpdateSeasonSuitCondtion(self.m_Game, self, iTarget, [
                dContion], { }, self.m_CondInfo)
        return dContion

    
    def RemoveCheckSuitCondtion(self, oTarget, iType, key, iSend = 1):
        iTarget = oTarget.m_ID
        if iTarget not in self.m_CurSituate:
            return { }
        dContion = { }
        if key in self.m_Condtion[iType]:
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
                self.UpdateSuitGrade(oTarget, iSuit)
            
        if dContion and iSend:
            cl_snetwar.GS2CUpdateSeasonSuitCondtion(self.m_Game, self, iTarget, [
                dContion], { }, self.m_CondInfo)
        return dContion

    
    def MeetConditions(self, clsSuit, iTarget, iSuit):
        iNewGrade = 0
        for oCondFunc in clsSuit.m_CondFunc.values():
            if oCondFunc(self, iTarget, iSuit):
                iNewGrade += 1
                continue
        
        return iNewGrade

    
    def AddForbidSuitCon(self, iType, args):
        dSuit = GetSeasonSuitNotMain()
        dExcludeSuit = GetGameExcludeSeasonSuit(self.m_WarMgr.GetPlayType())
        for iSuit in dSuit:
            if iSuit in dExcludeSuit:
                continue
            if iSuit in self.m_ForbidSuit:
                continue
            clsSuit = GetSeasonSuitCls(iSuit)
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
            cl_snetwar.GS2CUpdateSeasonSuitCondtion(self.m_Game, self, oTarget.m_ID, lstCondtion, { }, self.m_CondInfo)

    
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
            cl_snetwar.GS2CUpdateSeasonSuitCondtion(self.m_Game, self, oTarget.m_ID, lstCondtion, { }, self.m_CondInfo)

    
    def GetAllSuitGradeInfo(self, iTarget):
        if iTarget not in self.m_Enable:
            return { }
        return self.m_Enable[iTarget]

    
    def GetSuitCurGrade(self, iTarget, iSuit):
        if iTarget not in self.m_Enable or iSuit not in self.m_Enable[iTarget]:
            return 0
        return self.m_Enable[iTarget][iSuit]

    
    def GetSuitTemp(self, iPlayerID):
        if iPlayerID not in self.m_SuitTemp:
            return { }
        return self.m_SuitTemp[iPlayerID]

    
    def GetCurSuitTemp(self, iPlayerID):
        if iPlayerID not in self.m_SuitTemp:
            return 0
        return list(self.m_SuitTemp[iPlayerID])[0]

    
    def GetSuitOpenStatus(self, oHero, iSuit):
        iHero = oHero.m_ID
        if iHero not in self.m_Enable:
            return 0
        dEnableSuit = self.m_Enable[iHero]
        if iSuit not in dEnableSuit or dEnableSuit[iSuit] <= 0:
            return 0
        dSuitOpenStatus = self.m_SuitOpenStatus[oHero.m_PlayerID]
        if iSuit in dSuitOpenStatus and dSuitOpenStatus[iSuit]:
            return 1
        return 0

    
    def SetSuitArg(self, oHero, iSuit, sArg, iVal):
        dSuitArg = self.m_SuitArg[oHero.m_PlayerID]
        if iSuit not in dSuitArg:
            dSuitArg[iSuit] = { }
        dSuitArg[iSuit][sArg] = iVal

    
    def GetSuitArg(self, oHero, iSuit, sArg):
        dSuitArg = self.m_SuitArg[oHero.m_PlayerID]
        if iSuit not in dSuitArg or sArg not in dSuitArg[iSuit]:
            return 0
        return dSuitArg[iSuit][sArg]

    
    def SetSavedSuitArg(self, oHero, iSuit, sArg, iVal):
        dSavedSuitArg = self.m_SavedSuitArg[oHero.m_PlayerID]
        if iSuit not in dSavedSuitArg:
            dSavedSuitArg[iSuit] = { }
        dSavedSuitArg[iSuit][sArg] = iVal

    
    def GetSavedSuitArg(self, oHero, iSuit, sArg):
        dSavedSuitArg = self.m_SavedSuitArg[oHero.m_PlayerID]
        if iSuit not in dSavedSuitArg or sArg not in dSavedSuitArg[iSuit]:
            return 0
        return dSavedSuitArg[iSuit][sArg]

    
    def GetCurSituate(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_CurSituate:
            return { }
        return self.m_CurSituate[iHero]

    
    def ActiveAction(self, clsSuit, oHero, iGrade):
        dInfo = {
            'SeasonSuit': clsSuit.m_SID,
            'Grade': iGrade }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ACTIVE_SEASONSUIT, oHero, dInfo)
        iEnable = dInfo.get('Enable', 1)
        if iEnable:
            oActionFunc = clsSuit.GetAction(iGrade)
            oActionFunc(oHero)

    
    def RemoveAction(self, clsSuit, oHero, iGrade):
        oRemoveActionFunc = clsSuit.GetRemoveAction(iGrade)
        oRemoveActionFunc(oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVE_SEASONSUIT, oHero, {
            'SeasonSuit': clsSuit.m_SID,
            'Grade': iGrade })

    
    def AddConditionReduceNum(self, iTarget, iSuit, iReduce, sReason):
        if not iReduce:
            return None
        iPlayer = self.m_Game.m_WarMgr.GetPlayerIDByHeroID(iTarget)
        if iPlayer not in self.m_ConditionReduceNumInfo:
            self.m_ConditionReduceNumInfo[iPlayer] = {
                iSuit: {
                    sReason: iReduce } }
        elif iSuit not in self.m_ConditionReduceNumInfo[iPlayer]:
            self.m_ConditionReduceNumInfo[iPlayer][iSuit] = {
                sReason: iReduce }
        else:
            dInfo = self.m_ConditionReduceNumInfo[iPlayer][iSuit]
            if sReason not in dInfo:
                dInfo[sReason] = iReduce
            else:
                dInfo[sReason] += iReduce

    
    def GetAllCanConditionReduceSuit(self, iHero):
        if iHero not in self.m_Enable:
            return []
        lstResult = []
        for iSuit in self.m_Enable[iHero]:
            if self.CheckCondiReduce(iHero, iSuit):
                lstResult.append(iSuit)
        
        return lstResult

    
    def GetConditionReduceNumByReason(self, iTarget, iSuit, sReason):
        iPlayer = self.m_Game.m_WarMgr.GetPlayerIDByHeroID(iTarget)
        if iPlayer not in self.m_ConditionReduceNumInfo or iSuit not in self.m_ConditionReduceNumInfo[iPlayer]:
            return 0
        dInfo = self.m_ConditionReduceNumInfo[iPlayer][iSuit]
        if sReason not in dInfo:
            return 0
        return dInfo[sReason]

    
    def GetConditionReduceNum(self, iTarget, iSuit):
        iPlayer = self.m_Game.m_WarMgr.GetPlayerIDByHeroID(iTarget)
        if iPlayer not in self.m_ConditionReduceNumInfo or iSuit not in self.m_ConditionReduceNumInfo[iPlayer]:
            return 0
        iCanReduceNum = self.GetSuitCanReduceNum(iSuit)
        iReduceNum = sum(self.m_ConditionReduceNumInfo[iPlayer][iSuit].values())
        return min(iCanReduceNum, iReduceNum)

    
    def GetSuitCanReduceNum(self, iSuit):
        if iSuit not in self.m_SuitCanReduceConditionNum:
            return 0
        return self.m_SuitCanReduceConditionNum[iSuit]

    
    def CheckCondiReduce(self, iHero, iSuit):
        if iSuit in EXCLUDE_FUSESUIT:
            return False
        clsSuit = GetSeasonSuitCls(iSuit)
        if not clsSuit:
            return False
        for iType, _ in clsSuit.m_Condition.values():
            if iType in (SUIT_RELIC, SUIT_RELICTYPE):
                break
        else:
            return False
        iCanReduceNum = self.GetSuitCanReduceNum(iSuit)
        if self.GetConditionReduceNum(iHero, iSuit) >= iCanReduceNum:
            return False
        return True

    
    def SuitCondiReduce(self, oHero, clsSuit, iReduceNum, sReason, iFromSeasonSuit = 0):
        iSuit = clsSuit.m_SID
        iHero = oHero.m_ID
        if not self.CheckCondiReduce(iHero, iSuit):
            return None
        self.AddConditionReduceNum(iHero, iSuit, iReduceNum, sReason)
        self.UpdateSuitGrade(oHero, iSuit)
        self.UpdateSeasonSuitFusedTimes(oHero, clsSuit)
        iPlayerID = oHero.m_PlayerID
        if iFromSeasonSuit:
            if iPlayerID not in self.m_SeasonSuitReduceMap:
                self.m_SeasonSuitReduceMap[iPlayerID] = { }
            if iFromSeasonSuit in self.m_SeasonSuitReduceMap[iPlayerID]:
                SeasonsuitLog.Alert('%d %d suit reduceerr %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iFromSeasonSuit, iSuit))
                return None
            self.m_SeasonSuitReduceMap[iPlayerID][iFromSeasonSuit] = iSuit
            self.UpdateSeasonSuitReduceInfo(iPlayerID)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REDUCE_SUITCONDITION, oHero, {
            'Suit': iSuit,
            'Reason': sReason })
        self.SyncSuitCondtion(oHero, iSuit)

    
    def UpdateSeasonSuitFusedTimes(self, oHero, clsSuit):
        iHero = oHero.m_ID
        iSuit = clsSuit.m_SID
        iRequire = self.GetConditionReduceNum(iHero, iSuit)
        cl_snetwar.GS2CUpdateSeasonSuitFusedTimes(oHero.m_PlayerID, iSuit, iRequire, self.MeetConditions(clsSuit, iHero, iSuit))

    
    def GetSuitElement(self, oHero, iSuit):
        return self.GetSavedSuitArg(oHero, iSuit, self.m_ElementFlag)

    
    def ChangeSuitElement(self, oHero, iSuit):
        iNowElement = self.GetSavedSuitArg(oHero, iSuit, self.m_ElementFlag)
        if not iNowElement:
            iResultElement = SUIT_ELEMENT[0]
        elif iNowElement in SUIT_ELEMENT:
            iNowIndex = SUIT_ELEMENT.index(iNowElement)
            iResultIndex = (iNowIndex + 1) % 3
            iResultElement = SUIT_ELEMENT[iResultIndex]
        else:
            return None
        self.SetSavedSuitArg(oHero, iSuit, self.m_ElementFlag, iResultElement)
        cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_ELEMENT, [
            iSuit,
            iResultElement], self.m_Game, oHero)

    
    def RefreshAllSuitElement(self, oHero):
        dSuitOpenStatus = self.m_SuitOpenStatus[oHero.m_PlayerID]
        dSavedSuitArg = self.m_SavedSuitArg[oHero.m_PlayerID]
        for iSuit in ALL_ELEMENT_SUIT:
            if iSuit not in dSuitOpenStatus:
                continue
            iNowElement = dSavedSuitArg[iSuit][self.m_ElementFlag]
            cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_ELEMENT, [
                iSuit,
                iNowElement], self.m_Game, oHero)
        

    
    def RefreshSuitElement(self, oHero, iSuit):
        if iSuit not in ALL_ELEMENT_SUIT:
            return None
        iNowElement = self.GetSuitElement(oHero, iSuit)
        if not iNowElement:
            self.ChangeSuitElement(oHero, iSuit)
        else:
            cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_ELEMENT, [
                iSuit,
                iNowElement], self.m_Game, oHero)

    
    def GetSuitMaxGrade(self, iSuit):
        if iSuit not in self.m_AllSuitMaxGrade:
            SeasonsuitLog.Alert('%d suitmaxgrade err %d' % (self.m_Game.m_ID, iSuit))
            clsSuit = GetSeasonSuitCls(iSuit)
            if clsSuit:
                return clsSuit.m_MaxGrade
            return 0
        return self.m_AllSuitMaxGrade[iSuit]

    
    def GetSeasonSuitData(self, iHero):
        if iHero not in self.m_Enable:
            return None
        dSuitInfo = { }
        for iSuit, iGrade in self.m_Enable[iHero].items():
            if not iGrade:
                continue
            iMaxGrade = self.GetSuitMaxGrade(iSuit)
            dSuitInfo[str(iSuit)] = [
                iGrade,
                iMaxGrade]
        
        return dSuitInfo

    
    def UpdateSeasonSuitReduceInfo(self, iPlayerID):
        if iPlayerID not in self.m_SeasonSuitReduceMap:
            return None
        cl_snetwar.GS2CUpdateSeasonSuitReduceInfo(self.m_SeasonSuitReduceMap[iPlayerID], iPlayerID)

    
    def GetSuitConditionNum(self, iTarget, iSuit):
        iNum = self.GetConditionReduceNum(iTarget, iSuit)
        if iTarget in self.m_CurSituate and iSuit in self.m_CurSituate[iTarget]:
            for _, iHas in self.m_CurSituate[iTarget][iSuit].items():
                if not iHas:
                    continue
                iNum += 1
            
        return iNum

    
    def OnGenBened(self, oWarMgr, oTarget, dInfo):
        iHero = oTarget.m_ID
        iCanReduceSuitNum = len(self.GetAllCanConditionReduceSuit(iHero))
        dAllWeight = dInfo['BeneWeight']
        for iBene, iNum in BENE_REDUCESUITNUM.items():
            if iBene not in dAllWeight:
                continue
            if iNum > iCanReduceSuitNum:
                dAllWeight.pop(iBene)
        
        if iHero not in self.m_CurSituate:
            return None
        dCurSituate = self.m_CurSituate[iHero]
        for iBene, lstSuit in self.m_BeneTakeEffectSuit.items():
            if iBene not in dAllWeight:
                continue
            for iSuit in lstSuit:
                if iSuit in dCurSituate:
                    bHasSuit = True
                    break
            else:
                bHasSuit = False
            if not bHasSuit:
                dAllWeight.pop(iBene)
        

    
    def OnRecycle(self, oWarMgr, oHero, dMsgInfo):
        if 'RecycleDropType' not in dMsgInfo:
            return None
        if dMsgInfo['RecycleDropType'] != NWARRIOR_DROP_EQUIP:
            return None
        iPlayerID = oHero.m_PlayerID
        if iPlayerID in self.m_RecycleWeaponInfo:
            self.m_RecycleWeaponInfo[iPlayerID] += 1
        else:
            self.m_RecycleWeaponInfo[iPlayerID] = 1

    
    def GetAllLackRelic(self, oHero):
        if oHero.m_ID not in self.m_CurSituate:
            return { }
        oRelicCon = oHero.m_RelicCon
        dRelic = { }
        for iSuit in self.m_CurSituate[oHero.m_ID]:
            for iType, iRelic in self.m_SuitCon[iSuit].values():
                if iType != SUIT_RELIC:
                    continue
                if oRelicCon.CheckHasRelic(iRelic):
                    continue
                dRelic[iRelic] = 1
            
        
        return dRelic

    
    def GetAllCoreSuitID(self, oHero):
        if oHero.m_ID not in self.m_CurSituate:
            return []
        lstCoreSuit = []
        for iSuit in self.m_CurSituate[oHero.m_ID]:
            clsSuit = GetSeasonSuitCls(iSuit)
            if clsSuit.m_MaxGrade > 1:
                lstCoreSuit.append(iSuit)
        
        return lstCoreSuit

    
    def GetCoreSuitLackRelic(self, oHero):
        lstCoreSuit = self.GetAllCoreSuitID(oHero)
        if not lstCoreSuit:
            return { }
        dRelic = { }
        oRelicCon = oHero.m_RelicCon
        for iCoreSuit in lstCoreSuit:
            if iCoreSuit not in self.m_SuitCon:
                continue
            for iType, iRelic in self.m_SuitCon[iCoreSuit].values():
                if iType != SUIT_RELIC:
                    continue
                if oRelicCon.CheckHasRelic(iRelic):
                    continue
                dRelic[iRelic] = 1
            
        
        return dRelic

    
    def GetRecycleWeaponNum(self, iPlayerID):
        if iPlayerID not in self.m_RecycleWeaponInfo:
            return 0
        return self.m_RecycleWeaponInfo[iPlayerID]

    
    def SettleAccountsSeasonSuit(self, oTarget, iSuit):
        iPlayerID = oTarget.m_PlayerID
        if iPlayerID not in self.m_SettleAccountsSuitInfo:
            self.m_SettleAccountsSuitInfo[iPlayerID] = []
        lstSettleAccountsSuitInfo = self.m_SettleAccountsSuitInfo[iPlayerID]
        if iSuit in lstSettleAccountsSuitInfo:
            return None
        lstSettleAccountsSuitInfo.append(iSuit)
        self.UpdateSettleAccountsSuitInfo(oTarget)
        clsSuit = GetSeasonSuitCls(iSuit)
        for iConSID, (iConditionType, iConArgs) in clsSuit.m_Condition.items():
            if iConditionType != SUIT_RELIC:
                continue
            if not oTarget.m_RelicCon.IsEnabled(iConArgs):
                continue
            self.SetForeverCondtionInfo(oTarget, iSuit, iConSID)
            oTarget.m_RelicCon.RemoveRelic(iConArgs, 'settleaccounts %d' % iSuit, 1)
        

    
    def UpdateSettleAccountsSuitInfo(self, oTarget):
        iPlayerID = oTarget.m_PlayerID
        if iPlayerID not in self.m_SettleAccountsSuitInfo:
            return None
        cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_SETTLEACCOUNTSSUIT, self.m_SettleAccountsSuitInfo[iPlayerID], self.m_Game, oTarget)

    
    def GS2CSeasonSuitPerformStart(self, iSID, pid):
        cl_snetwar.GS2CSeasonSuitPerformStart(iSID, pid)

    
    def GetSuitConditionSpillNum(self, iTarget, iSuit):
        iSuitConditionNum = self.GetSuitConditionNum(iTarget, iSuit)
        if iSuit not in self.m_CondInfo:
            return 0
        iMaxLvNeedNum = self.m_CondInfo[iSuit][0]
        return max(0, iSuitConditionNum - iMaxLvNeedNum)

    
    def CheckCoreSuitAndGetGrade(self, iSuit):
        iMaxGrade = 0
        clsSuit = GetSeasonSuitCls(iSuit)
        if clsSuit:
            iMaxGrade = clsSuit.m_MaxGrade
            if iMaxGrade > 1:
                return (1, iMaxGrade)
        return (0, iMaxGrade)

    
    def CheckCoreSuitReachMaxGrade(self, iHero, iCoreSuit):
        (iRet, iMaxGrade) = self.CheckCoreSuitAndGetGrade(iCoreSuit)
        if iRet:
            iGrade = self.GetSuitCurGrade(iHero, iCoreSuit)
            if iGrade == iMaxGrade:
                return True
        return False

    
    def CheckEnable(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return False
        return True

    
    def ShowSuitTempList(self, iPlayerID):
        iCurSuitTemp = self.GetCurSuitTemp(iPlayerID)
        dSuitTemp = self.GetChangeSuitTempInfo(iPlayerID)
        lstSuitTemp = []
        for iTempID, lstSuit in dSuitTemp.items():
            iCardPack = self.GetCardPackByTempID(iPlayerID, iTempID)
            lstSuitTemp.append([
                iTempID,
                iCardPack,
                lstSuit])
        
        cl_snetwar.GS2CShowSuitTempList(iCurSuitTemp, lstSuitTemp, iPlayerID)

    
    def SaveSeed(self, oHero):
        if not self.CheckEnable():
            return { }
        iPlayerID = oHero.m_PlayerID
        dSaveInfo = self.Save()
        if not dSaveInfo:
            return { }
        dData = { }
        for sKey, dValue in dSaveInfo.items():
            if iPlayerID not in dValue:
                continue
            dData[sKey] = dValue[iPlayerID]
        
        iCurTemp = self.GetCurSuitTemp(iPlayerID)
        dData['PID'] = oHero.m_PlayerID
        dData['CardPack'] = self.GetCardPackByTempID(iPlayerID, iCurTemp)
        return dData

    
    def LoadSeed(self, dData):
        if not dData or not self.CheckEnable():
            return None
        iPlayerID = dData.get('PID', 0)
        oHero = self.m_WarMgr.GetHeroByPlayer(iPlayerID)
        if not oHero:
            return None
        dSuitTemp = dData.get('ST', { })
        if dSuitTemp:
            lstSuitTemp = list(dSuitTemp.values())[0]
            self.m_SuitTemp[iPlayerID] = {
                0: lstSuitTemp }
        self.m_MarkSuitInfo[iPlayerID] = dData.get('MSI', { })
        self.m_ForeverCondtionInfo[iPlayerID] = dData.get('FC', { })
        self.m_ConditionReduceNumInfo[iPlayerID] = dData.get('CRN', { })
        self.m_SeasonSuitReduceMap[iPlayerID] = dData.get('SSRM', { })
        self.m_SavedSuitArg[iPlayerID] = dData.get('SSA', { })
        if 'RWI' in dData:
            self.m_RecycleWeaponInfo[iPlayerID] = dData['RWI']
        if 'SASI' in dData:
            self.m_SettleAccountsSuitInfo[iPlayerID] = dData['SASI']
        self.m_SuitOpenStatus[iPlayerID] = dData.get('OS', { })
        self.LoadHero(oHero)
        self.ChangeSuitTemp(oHero)
        if 'CardPack' in dData:
            self.OnChangeCardPackPerform(oHero, dData['CardPack'])

    
    def GetSuitRelicCondition(self, iSuit):
        if iSuit not in self.m_SuitCon:
            return { }
        dRelic = { }
        dCondition = self.m_SuitCon[iSuit]
        for iConditionType, iSID in dCondition.values():
            if iConditionType != SUIT_RELIC:
                continue
            dRelic[iSID] = 1
        
        return dRelic

    
    def GetSuitRelicGradeInfo(self, iSuit):
        if iSuit not in self.m_AllSuitGradeInfo:
            return { }
        return self.m_AllSuitGradeInfo[iSuit]



def CheckCondiReduce(oHero, iSuit):
    oSuitElement = oHero.m_Game.m_WarMgr.GetSeasonSuitElement()
    iResult = 0 if not oSuitElement or not oSuitElement.CheckCondiReduce(oHero.m_ID, iSuit) else 1
    npcnet.GS2CUpdateCheckReduceSuitResult(oHero, iSuit, iResult)


def GetComponentClass(oMgrManager):
    return CSeasonSuitElement

