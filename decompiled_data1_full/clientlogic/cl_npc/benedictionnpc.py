# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/benedictionnpc.pyc
# RelativePath: clientlogic/cl_npc/benedictionnpc.pyc
# Source Generated with Decompyle++
# File: benedictionnpc.pyc (Python 3.6)

from cl_commondefines import NPC_CB_VALUE, NPC_OPTION_COST_GSCASH, NPC_OPTION_REWARD_BENEDICTION, INTERACT_TYPE_ALLOW, INTERACT_TYPE_FORBID, INTERACT_STATUS_PEND, INTERACT_STATUS_DONE, BENEDRULE_RANDOMFREE, NPC_CB_LIST, MODE_SNOWMOUNTAINS, BENE_SOURCE_LAYER, NPC_ACTION_SELECTBENE, NPC_ACTION_REPLACEBENE, NPC_ACTION_NONE
from cl_only import ChooseKey, ShufferList, CopyDict
from cl_object.logging import WarnpcLog
import math
import cl_perform
import cl_perform.load
import cl_msgcenter
import cl_formula
from . import mobject
from . import net
MAX_BENE_CNT = 3
REPLACEBENE_MODETYPE = [
    MODE_SNOWMOUNTAINS]

class CBenedictionNPC(mobject.CNPC):
    m_ChooseNum = 3
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_ChooseData = { }
        self.m_MaxRefreshTimes = 0
        self.m_HeroRefreshCostInfo = { }
        self.m_ArgData['OldBenedOp'] = { }
        self.m_BuyCostFactor = 100

    
    def Release(self):
        self.m_ChooseData = { }
        super().Release()

    
    def ValidInteract(self, oHero):
        oGame = oHero.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
        lstBenediction = oHero.m_BenedictionCon.GetBenediction(BENE_SOURCE_LAYER)
        iHasCnt = len(lstBenediction)
        if iHasCnt >= iLayer:
            return False
        if iHasCnt >= MAX_BENE_CNT and not self.ValidReplace(oHero):
            return False
        if iLayer == 4 and MODE_SNOWMOUNTAINS not in oGame.m_WarMgr.m_ModeType:
            return False
        for oBenediction in lstBenediction:
            if oBenediction.m_Layer == iLayer:
                return False
        
        return super().ValidInteract(oHero)

    
    def ValidReplace(self, oHero):
        oGame = oHero.m_Game
        if oGame.m_WarMgr.GetEndlessElement():
            return True
        for iModeType in REPLACEBENE_MODETYPE:
            if iModeType not in oGame.m_WarMgr.m_ModeType:
                continue
            return True
        
        return False

    
    def OnInteract(self, oHero):
        self.SendChoose(oHero)

    
    def SetInitInteract(self, iType):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
        for pid in oWarMgr.GetAllPlayer():
            oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            bInteracted = self.CheckInteracted(oWarMgr, oHero, iLayer)
            if bInteracted:
                iType = INTERACT_TYPE_FORBID
                iStatus = INTERACT_STATUS_DONE
            else:
                iType = self.CheckForbid(oWarMgr, iLayer, INTERACT_TYPE_ALLOW)
                iStatus = INTERACT_STATUS_PEND
            self.m_PlayerInteractStatus[pid] = iStatus
            self.m_PlayerInteractType[pid] = iType
            self.m_PlayerAssignInteractType[pid] = NPC_ACTION_NONE
        

    
    def CheckForbid(self, oWarMgr, iLayer, iOriginalType):
        if iLayer == 4 and MODE_SNOWMOUNTAINS not in oWarMgr.m_ModeType:
            return INTERACT_TYPE_FORBID
        return iOriginalType

    
    def CheckInteracted(self, oWarMgr, oHero, iLayer):
        lstBenediction = oHero.m_BenedictionCon.GetBenediction(BENE_SOURCE_LAYER)
        iHasCnt = len(lstBenediction)
        bResult = False
        if oWarMgr.IsEndless() or iLayer > MAX_BENE_CNT:
            for oBene in lstBenediction:
                if oBene.m_Layer == iLayer:
                    bResult = True
                    break
            
        elif iHasCnt >= iLayer:
            bResult = True
        return bResult

    
    def GetPlayerAssignInteractType(self, pid):
        if pid not in self.m_PlayerAssignInteractType:
            return NPC_ACTION_NONE
        if self.m_PlayerAssignInteractType[pid] in (NPC_ACTION_SELECTBENE, NPC_ACTION_REPLACEBENE):
            return self.m_PlayerAssignInteractType[pid]
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            lstBenediction = oHero.m_BenedictionCon.GetBenediction(BENE_SOURCE_LAYER)
            iHasCnt = len(lstBenediction)
            if iHasCnt < MAX_BENE_CNT:
                iAssignInteractType = NPC_ACTION_SELECTBENE
            else:
                iAssignInteractType = NPC_ACTION_REPLACEBENE
            self.m_PlayerAssignInteractType[pid] = iAssignInteractType
            return self.m_PlayerAssignInteractType[pid]
        return NPC_ACTION_NONE

    
    def SendChoose(self, oHero):
        if not self.ValidInteract(oHero):
            return None
        iHero = oHero.m_ID
        dChoose = self.m_ChooseData.setdefault(iHero, { })
        dPrice = cl_perform.load.GetBenedictionPrice()
        oGame = oHero.m_Game
        if not dChoose:
            lstHas = oHero.m_BenedictionCon.GetAllPerformSID()
            dAllWeight = CopyDict(cl_perform.load.GetBenedictionLibrary())
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GEN_BEFOR_BENED, oHero, {
                'BeneWeight': dAllWeight })
            dWeight = { }
            lstOldBenedOp = self.m_ArgData['OldBenedOp'].setdefault(iHero, [])
            dWeight = DealBeneWeight(oHero, dAllWeight, lstExclude = lstOldBenedOp)
            for i in range(self.m_ChooseNum):
                if not dWeight:
                    WarnpcLog.Alert('%s no enough bened %s %s' % (self.m_SID, lstHas, dChoose))
                    break
                iSID = ChooseKey(oGame, dWeight)
                dWeight.pop(iSID)
                dChoose[iSID] = math.ceil(dPrice[iSID] * cl_formula.GetFormulaResult(oHero, self.m_BuyCostFactor, { }) / 100)
            
            if not dChoose:
                WarnpcLog.Debug('%s no choose %s %s %s %s' % (oGame.m_ID, oHero.m_PlayerID, self.m_SID, lstHas, dWeight))
                return None
            self.m_ArgData['OldBenedOp'][iHero] = list(dChoose)
            dInfo = {
                'BenedOp': dChoose }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_OPEN_BEFOR_BENED, oHero, dInfo)
            lstRule = dInfo['RuleInfo'] if 'RuleInfo' in dInfo else []
            for iRule, iValue in lstRule:
                func = g_RuleFunc[iRule]
                func(oHero, dChoose, iValue)
            
        lstAllOption = []
        for i, (iSID, iCost) in enumerate(dChoose.items()):
            iValidChoose = 1 if oHero.m_WarGSCash >= iCost else 0
            lstOption = [
                i,
                iValidChoose,
                '\x00',
                NPC_OPTION_COST_GSCASH,
                '\x00',
                0,
                iCost,
                NPC_OPTION_REWARD_BENEDICTION,
                '\x00',
                iSID,
                {
                    'Attr': [] },
                1]
            lstAllOption.append(lstOption)
        
        net.GS2CNpcEvent(oHero, self.m_ID, '\x00', lstAllOption)
        lstBenediction = oHero.m_BenedictionCon.GetBenediction(BENE_SOURCE_LAYER)
        iHasCnt = len(lstBenediction)
        if iHasCnt >= MAX_BENE_CNT or self.ValidReplace(oHero):
            net.SetNpcUICallBackFunction(oHero, NPC_CB_LIST, self.PlayerChoose, self)
        else:
            net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.PlayerChoose, self)
        self.SetNpcRefreshCallBackFunction(oHero)

    
    def PlayerChoose(self, oHero, iAnswer, iReplace = 0):
        iHero = oHero.m_ID
        if iHero not in self.m_ChooseData:
            return None
        dChoose = self.m_ChooseData[iHero]
        if iAnswer not in dChoose:
            WarnpcLog.Alert('%s bened invalid ans %s %s' % (self.m_SID, iAnswer, dChoose))
            return None
        lstAllHas = oHero.m_BenedictionCon.GetAllPerformSID()
        if iAnswer in lstAllHas:
            WarnpcLog.Alert('%s bened repeat ans %s %s' % (self.m_SID, iAnswer, lstAllHas))
            return None
        iCost = dChoose[iAnswer]
        if oHero.m_WarGSCash < iCost:
            WarnpcLog.Alert('%s bened no gscash %s %s' % (self.m_SID, oHero.m_WarGSCash, iCost))
            return None
        if HasTeamOnlyBene(oHero, iAnswer):
            net.GS2CBeneNpcResult(self, oHero, 2346, iAnswer, 0)
            return None
        dInfo = {
            'Bene': iAnswer }
        lstHas = oHero.m_BenedictionCon.GetBenedictionSID(BENE_SOURCE_LAYER)
        if len(lstHas) < MAX_BENE_CNT:
            sReason = 'npc%s %s' % (self.m_SID, iAnswer)
        elif iReplace not in lstHas or not self.ValidReplace(oHero):
            WarnpcLog.Alert('%s bened replace invalid ans %s %s %s' % (self.m_SID, iAnswer, iReplace, lstHas))
            return None
        sReason = 'npc%s %s replace %d' % (self.m_SID, iAnswer, iReplace)
        oReplace = oHero.m_BenedictionCon.GetPerform(iReplace)
        if oReplace:
            dInfo['ReplaceInfo'] = (iReplace, oReplace.m_Layer)
        oHero.m_BenedictionCon.RemoveBenediction(iReplace)
        oHero.ConsumeGSCash(iCost, sReason)
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
            oHero.m_PlayerID])
        oHero.m_BenedictionCon.AddBenediction(iAnswer, 1, sReason, iReplaceSID = iReplace)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHOOSEBENED, oHero, dInfo)

    
    def Refresh(self, oHero):
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
        if iTimes + 1 > self.m_MaxRefreshTimes:
            return None
        iCost = self.GetRefreshCost(oHero)
        if iCost > oHero.m_WarGSCash:
            return None
        oHero.ConsumeGSCash(iCost, 'BeneRefreshCost')
        dTimes[oHero.m_ID] = iTimes + 1
        self.Set('HeroRefreshTimes', dTimes)
        net.GS2CNpcRefreshInfo(self, oHero)
        self.m_ChooseData.pop(oHero.m_ID)
        self.SendChoose(oHero)

    
    def SetRefreshCost(self, tCost):
        self.m_RefreshCost = tCost

    
    def SetBuyCostFactor(self, tFactor):
        self.m_BuyCostFactor = tFactor

    
    def SetRefreshTimes(self, iTimes):
        self.m_MaxRefreshTimes = iTimes

    
    def GetRefreshCost(self, oHero):
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes[oHero.m_ID] if oHero.m_ID in dTimes else 0
        (iCurTimes, iCost) = self.m_HeroRefreshCostInfo[oHero.m_ID] if oHero.m_ID in self.m_HeroRefreshCostInfo else (-1, 0)
        if iCurTimes == -1 or iCurTimes != iTimes:
            dInfo = {
                cl_formula.FML_ARG_VID: oHero.m_ID }
            iCost = cl_formula.GetFormulaResult(self, self.m_RefreshCost, dInfo)
            self.m_HeroRefreshCostInfo[oHero.m_ID] = (iTimes, iCost)
        return iCost

    
    def GetRefreshInfo(self, oHero):
        iMaxRefreshTimes = self.m_MaxRefreshTimes
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes[oHero.m_ID] if oHero.m_ID in dTimes else 0
        iRefreshTimes = iMaxRefreshTimes - iTimes
        return (iMaxRefreshTimes, iRefreshTimes)



def RandomFree(oHero, dBenedIndo, iValue):
    if not dBenedIndo:
        return None
    lstBened = list(dBenedIndo)
    lstBened = ShufferList(oHero.m_Game, lstBened)
    for _ in range(iValue):
        dBenedIndo[lstBened.pop()] = 0
    

g_RuleFunc = {
    BENEDRULE_RANDOMFREE: RandomFree }

def DealBeneWeight(oHero, dAllWeight, lstExclude):
    dWeight = { }
    oGame = oHero.m_Game
    oWarMgr = oGame.m_WarMgr
    setExcludeBened = set(lstExclude) | set(oHero.m_BenedictionCon.GetAllPerformSID())
    setExcludeBened |= set(cl_perform.load.GetGameExcludeBened(oWarMgr.GetAllPlayerCnt()))
    lstTeamOnly = cl_perform.load.GetTeamOnlyBened()
    setExcludeBened |= { iSID for iSID in lstTeamOnly if HasTeamOnlyBene(oHero, iSID) }
    for iModeType in oWarMgr.m_ModeType:
        setExcludeBened |= set(cl_perform.load.GetLimitModeBened(iModeType))
    
    dLimitSeason = cl_perform.load.GetLimitSeasonBened()
    iCheckSeason = oWarMgr.m_SeasonNum
    for iLimitBened, lstLimitSeason in dLimitSeason.items():
        if iCheckSeason not in lstLimitSeason:
            setExcludeBened.add(iLimitBened)
    
    dLimitSeasonLock = cl_perform.load.GetLimitSeasonBenedLock()
    for iLimitBened, lstLimitSeason in dLimitSeasonLock.items():
        if iCheckSeason in lstLimitSeason:
            setExcludeBened.add(iLimitBened)
    
    dLimitSeasonTalentPut = cl_perform.load.GetLimitSeasonTalentPut()
    for iSID, iWeight in dAllWeight.items():
        if not iWeight:
            continue
        if iSID in setExcludeBened:
            continue
        if not iSID in dLimitSeasonTalentPut and oHero.HasSeasonTalent(dLimitSeasonTalentPut[iSID]):
            continue
        clsPerform = cl_perform.GetPerformModule(iSID)
        if not clsPerform:
            continue
        iLimitCareer = clsPerform.m_Career
        if iLimitCareer and iLimitCareer != oHero.m_Career:
            continue
        dWeight[iSID] = iWeight
    
    return dWeight


def HasTeamOnlyBene(oHero, iBenediction):
    lstTeamOnly = cl_perform.load.GetTeamOnlyBened()
    if iBenediction in lstTeamOnly:
        oGame = oHero.m_Game
        lstHero = oGame.m_WarMgr.GetAllHero()
        for iHero in lstHero:
            if iHero == oHero.m_ID:
                continue
            oTmpHero = oGame.GetObject(iHero)
            if not oTmpHero:
                continue
            if iBenediction in oTmpHero.m_BenedictionCon.GetBenedictionSID():
                return True
        
    return False

