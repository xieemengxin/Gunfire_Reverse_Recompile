# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/benedictionnpc.pyc
# RelativePath: clientlogic/cl_npc/benedictionnpc.pyc
# Source Generated with Decompyle++
# File: benedictionnpc.pyc (Python 3.6)

# 单个 灵佑 NPC 可以重复打开，刷新次数不再受上限限制，每个关卡最多拿 2 个 灵佑
# 去除灵佑的选择限制 模式限制 赛季限制 队伍唯一限制 单人模式排除 赛季天赋投放限制

from cl_commondefines import NPC_CB_VALUE, NPC_OPTION_COST_GSCASH, NPC_OPTION_REWARD_BENEDICTION, INTERACT_TYPE_ALLOW, INTERACT_TYPE_FORBID, INTERACT_STATUS_PEND, INTERACT_STATUS_DONE, BENEDRULE_RANDOMFREE, NPC_CB_LIST, MODE_SNOWMOUNTAINS, BENE_SOURCE_LAYER, NPC_ACTION_SELECTBENE, NPC_ACTION_REPLACEBENE, NPC_ACTION_NONE
from cl_only import ChooseKey, ShufferList, CopyDict
from cl_object.logging import WarnpcLog
import math
import cl_perform
import cl_perform.load
import cl_msgcenter
import cl_formula
import cl_test as cl_customconfig
from . import mobject
from . import net
MAX_BENE_CNT = 999999
BENE_PER_LAYER_CNT = 2
UNLIMITED_REFRESH_TIMES = 999999
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

    
    def GetCurLayer(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        return oLevelCtrl.m_LayerNum if oLevelCtrl else 0

    
    def GetLayerBeneCount(self, oHero, iLayer = None):
        if iLayer is None:
            iLayer = self.GetCurLayer()
        iCount = 0
        for oBenediction in oHero.m_BenedictionCon.GetBenediction(BENE_SOURCE_LAYER):
            if oBenediction.m_Layer == iLayer:
                iCount += 1
        return iCount

    
    def ValidInteract(self, oHero):
        iLayer = self.GetCurLayer()
        if self.GetLayerBeneCount(oHero, iLayer) >= BENE_PER_LAYER_CNT:
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
        return iOriginalType

    
    def CheckInteracted(self, oWarMgr, oHero, iLayer):
        return self.GetLayerBeneCount(oHero, iLayer) >= BENE_PER_LAYER_CNT

    
    def GetPlayerAssignInteractType(self, pid):
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            self.m_PlayerAssignInteractType[pid] = NPC_ACTION_SELECTBENE
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
        iLayer = self.GetCurLayer()
        if self.GetLayerBeneCount(oHero, iLayer) >= BENE_PER_LAYER_CNT:
            WarnpcLog.Alert('%s bened layer limit %s %s' % (self.m_SID, iAnswer, iLayer))
            return None
        sReason = 'npc%s %s' % (self.m_SID, iAnswer)
        oHero.ConsumeGSCash(iCost, sReason)
        dChoose.pop(iAnswer, None)
        oHero.m_BenedictionCon.AddBenediction(iAnswer, 1, sReason, iReplaceSID = iReplace)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHOOSEBENED, oHero, dInfo)

    
    def Refresh(self, oHero):
        dTimes = self.Query('HeroRefreshTimes', { })
        iTimes = dTimes.setdefault(oHero.m_ID, 0)
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
        self.m_MaxRefreshTimes = UNLIMITED_REFRESH_TIMES

    
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
        return (UNLIMITED_REFRESH_TIMES, UNLIMITED_REFRESH_TIMES)



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
    # 先构造一个排除集合，来源有三类：
    # 1. 调用方额外传进来的排除列表（通常是这个 NPC 之前已经刷出来过的项）
    # 2. 角色自己已经拥有的灵佑
    # 3. 配表里按人数/队伍规则禁止出现的灵佑
    # setExcludeBened = set(lstExclude) | set(oHero.m_BenedictionCon.GetAllPerformSID())
    setExcludeBened = set(oHero.m_BenedictionCon.GetAllPerformSID())
    # setExcludeBened |= set(cl_perform.load.GetGameExcludeBened(oWarMgr.GetAllPlayerCnt()))
    lstTeamOnly = cl_perform.load.GetTeamOnlyBened()
    # 队伍唯一灵佑：如果队友已经拿过，同一局里就不再进入候选池
    # setExcludeBened |= { iSID for iSID in lstTeamOnly if HasTeamOnlyBene(oHero, iSID) }
    # 模式限制也是做减法：当前激活的每个模式都会贡献一份禁用列表
    # for iModeType in oWarMgr.m_ModeType:
    #     setExcludeBened |= set(cl_perform.load.GetLimitModeBened(iModeType))
    
    # 赛季限制有两种：
    # 1. 只允许在指定赛季出现
    # 2. 在指定赛季里强制锁掉
    # dLimitSeason = cl_perform.load.GetLimitSeasonBened()
    # iCheckSeason = oWarMgr.m_SeasonNum
    # for iLimitBened, lstLimitSeason in dLimitSeason.items():
    #     if iCheckSeason not in lstLimitSeason:
    #         setExcludeBened.add(iLimitBened)
    
    # dLimitSeasonLock = cl_perform.load.GetLimitSeasonBenedLock()
    # for iLimitBened, lstLimitSeason in dLimitSeasonLock.items():
    #     if iCheckSeason in lstLimitSeason:
    #         setExcludeBened.add(iLimitBened)
    
    # 这里仍然要把候选池真正填出来，否则 dWeight 会一直是空的，
    # NPC 打开后就会出现“没有任何可选灵佑”的硬错误。
    # 当前版本保留“已拥有灵佑不重复出”的基础限制，
    # 但不再按模式/赛季去裁剪列表。
    for iSID, iWeight in dAllWeight.items():
        if not iWeight:
            continue
        if iSID in setExcludeBened:
            continue
        clsPerform = cl_perform.GetPerformModule(iSID)
        if not clsPerform:
            continue
        # 仍然保留职业限制，避免给完全不兼容的职业专属灵佑。
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
