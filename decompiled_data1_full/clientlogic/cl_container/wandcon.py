# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/wandcon.pyc
# RelativePath: clientlogic/cl_container/wandcon.pyc
# Source Generated with Decompyle++
# File: wandcon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_WAND, S5_ITEM_TYPE_WAND, S5_ITEM_TYPE_COMP, WAND_SUBMSG_ADD, WAND_SUBMSG_REMOVE, WAND_COMP_TYPE_ACTION, WAND_COMP_TYPE_CONDITION
from cl_commondefines import WAND_REMOVE, WAND_EQUIP, WAND_UNEQUIP, WAND_EQUIPCOMP, WAND_UNEQUIPCOMP, WANDCOMP_REMOVE, WAND_RECYCLE, WANDCOMP_RECYCLE, NWARRIOR_DROP_WANDCOMP, CURRENCY_CASH, WANDCOMP_SUBMSG_ADDCOMP_TO_CONTAINER, WANDCOMP_SUBMSG_REMOVECOMP_FROM_CONTAINER, RECYCLE_UNDROP, WAND_QUALITY_NORMAL, WAND_QUALITY_RARE, WAND_QUALITY_TALE, ROLLABILITY_OPTION, STATE_TIME_FOREVER, MGRSTATE_ADDEXTCONCOMP, MGRSTATE_ADDEXTACTCOMP, WANDABILITY_ADDEXTCONCOMP, WANDABILITY_ADDEXTACTCOMP, PAIR_WAND, PAIR_WAND_MGRSTATE
from cl_object.logging import WandLog
from cl_platformdata import GetWandCompType, GetWandDropInfo, GetWandRecycleInfo, GetWandCompRecycleInfo, GetWandCompDropInfo
from cl_only import DeepCopy, SendAlert
from cl_container.mobject import CBaseSeasonContainer
import cl_wand
import cl_drop
import cl_snetwar
import cl_wand.net as wandnet
import cl_msgcenter
import cl_object
import cl_state
COMP_ONELEVEL_MAX = 99
NOTIFY_TYPE_WAND = 0
NOTIFY_TYPE_WANDCOMP = 1
WAND_MAX = 50
WAND_UPGRADE_TIMES = 3
QUICK_ADDCOMP_QUALITY = (WAND_QUALITY_TALE, WAND_QUALITY_RARE, WAND_QUALITY_NORMAL)

class CWandContainer(CBaseSeasonContainer):
    m_SeasonNum = 5
    m_BagType = BAG_TYPE_WAND
    m_Flag = 'WandCon'
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_Wand = { }
        self.m_CurWand = 0
        self.m_Comp = { }
        self.m_Options = {
            WANDCOMP_REMOVE: (self.RemoveComp, 2),
            WANDCOMP_RECYCLE: (self.RecycleComp, 2),
            WAND_RECYCLE: (self.RecycleWand, 1),
            WAND_UNEQUIPCOMP: (self.RemoveWandComp, 4),
            WAND_EQUIPCOMP: (self.AddWandComp, 4),
            WAND_UNEQUIP: (self.UnEquipWand, 1),
            WAND_EQUIP: (self.SetCurWand, 1),
            WAND_REMOVE: (self.RemoveWand, 1) }
        self.m_CompRedDot = { }
        self.m_Sign = {
            S5_ITEM_TYPE_COMP: [],
            S5_ITEM_TYPE_WAND: [] }
        self.m_SortedBagComp = {
            WAND_COMP_TYPE_ACTION: { },
            WAND_COMP_TYPE_CONDITION: { } }
        for dTypeInfo in self.m_SortedBagComp.values():
            for iLevel in QUICK_ADDCOMP_QUALITY:
                dTypeInfo[iLevel] = []
            
        
        cl_msgcenter.AddFunction(self.m_Game.GetWarMgr(), cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnAddPlayer, 'WandConAddPlayer', iOnce = 0)

    
    def Save(self):
        dData = { }
        lstWand = []
        for oWand in self.m_Wand.values():
            dWand = oWand.Save()
            if oWand.m_ID == self.m_CurWand:
                dWand['IsCurWand'] = 1
            lstWand.append(dWand)
        
        dData['Wand'] = lstWand
        dData['Comp'] = DeepCopy(self.m_Comp)
        dData['CRD'] = self.m_CompRedDot
        dData['WSN'] = self.m_Sign
        dData['SBC'] = self.m_SortedBagComp
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        if not self.CheckElementIsEnable():
            return None
        iCurWand = 0
        self.m_Comp = dData['Comp']
        lstWand = dData['Wand']
        for dWand in lstWand:
            oWand = self.CreateWand(dWand['SID'], dWand['Grade'], 'Load', dWand)
            if not oWand:
                continue
            self.m_Wand[oWand.m_ID] = oWand
            wandnet.GS2CAddWand(self.m_Game, self.m_Owner, {
                self.m_PlayerID: 1 }, oWand)
            if 'IsCurWand' in dWand:
                iCurWand = oWand.m_ID
        
        if iCurWand:
            self.SetCurWand(iCurWand)
        self.m_CompRedDot = dData['CRD']
        self.m_Sign = dData['WSN']
        if 'SBC' in dData:
            self.m_SortedBagComp = dData['SBC']
        self.AfterLoad()

    
    def AfterLoad(self):
        dConWandInfo = { }
        for oWand in self.m_Wand.values():
            if oWand.m_SID == PAIR_WAND:
                self.AddPairWandMgrState()
            if oWand.HasWandAbility(WANDABILITY_ADDEXTCONCOMP):
                dConWandInfo[oWand.m_ID] = 1
        
        if dConWandInfo:
            dArg = {
                'WandInfo': dConWandInfo,
                'Loading': 1 }
            self.AddExtConCompMgrState(dArg)

    
    def AddPairWandMgrState(self, dArg = None):
        oHero = self.GetOwner()
        if not oHero:
            return None
        if oHero.m_State.GetItemBySID(PAIR_WAND_MGRSTATE):
            return None
        iTimeType = STATE_TIME_FOREVER
        dArgs = {
            'AID': oHero.m_ID,
            'RS': cl_object.reason.CStrReason('AddPairWandMgrState'),
            'arg': dArg if dArg else { } }
        oState = cl_state.AddState(oHero, PAIR_WAND_MGRSTATE, iTimeType, 0, dArgs)
        if not oState:
            return None
        oState.Enable(oHero)

    
    def AddExtConCompMgrState(self, dArg):
        oHero = self.GetOwner()
        if not oHero:
            return None
        if oHero.m_State.GetItemBySID(MGRSTATE_ADDEXTCONCOMP):
            return None
        iTimeType = STATE_TIME_FOREVER
        dArgs = {
            'AID': oHero.m_ID,
            'RS': cl_object.reason.CStrReason('AddExtConCompAbility'),
            'arg': dArg }
        oState = cl_state.AddState(oHero, MGRSTATE_ADDEXTCONCOMP, iTimeType, 0, dArgs)
        if not oState:
            return None
        oState.Enable(oHero)

    
    def AddExtActCompMgrState(self, dArg):
        oHero = self.GetOwner()
        if not oHero:
            return None
        if oHero.m_State.GetItemBySID(MGRSTATE_ADDEXTACTCOMP):
            return None
        iTimeType = STATE_TIME_FOREVER
        dArgs = {
            'AID': oHero.m_ID,
            'RS': cl_object.reason.CStrReason('AddExtActCompAbility'),
            'arg': dArg }
        oState = cl_state.AddState(oHero, MGRSTATE_ADDEXTACTCOMP, iTimeType, 0, dArgs)
        if not oState:
            return None
        oState.Enable(oHero)

    
    def OnAddPlayer(self, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['Hero'] if 'Hero' in dMsgInfo else None
        if not oHero or oHero.m_ID != self.m_Owner:
            return None
        dPlayerInfo = dMsgInfo['Info']
        if 'SeasonWand' not in dPlayerInfo:
            return None
        dSeasonWand = dPlayerInfo['SeasonWand']
        if not dSeasonWand:
            return None
        iWandSID = dSeasonWand['WandSID']
        lstComp = dSeasonWand['WandComp']
        clsWandData = cl_wand.GetWandDataCls(iWandSID)
        if not clsWandData:
            SendAlert('err', '获取预设模板法杖配置异常 %d' % iWandSID)
            return None
        iMaxLevel = max(clsWandData.m_LevelInfo)
        (_, lstConditionComp, _, lstActionComp) = clsWandData.m_LevelInfo[iMaxLevel][:4]
        dPersetComp = { iDismantleStatus: iCompSID for iCompSID, _, iDismantleStatus in lstConditionComp + lstActionComp }
        for _, iCompSID in lstComp:
            if iCompSID in dPersetComp and not dPersetComp[iCompSID]:
                continue
            self.AddSign(S5_ITEM_TYPE_COMP, iCompSID, 0)
        
        self.AddSign(S5_ITEM_TYPE_WAND, iWandSID, 0)
        self.RefreshAllSign()

    
    def CheckElementIsEnable(self):
        oWandElement = self.m_Game.m_WarMgr.GetComponent('WandElement')
        if not oWandElement or not (oWandElement.m_Enable):
            return False
        return True

    
    def AllPerformDisable(self, iNotify = 0):
        for oWand in list(self.m_Wand.values()):
            oWand.Disable()
        

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_Game.GetWarMgr(), cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, 'WandConAddPlayer')
        self.m_CurWand = 0
        for oWand in self.m_Wand.values():
            oWand.Release()
        
        self.m_Wand = { }
        self.m_Comp = { }
        self.m_Options = { }
        self.m_CompRedDot = { }
        self.m_Game = None

    
    def ClearAll(self):
        for iWandID in list(self.m_Wand):
            self.RemoveWand(iWandID, 'ClearAll', iDrop = 0)
        
        self.m_Comp = { }
        self.m_CompRedDot = { }
        self.SelfRefresh()

    
    def Refresh(self, dPlayer):
        if not self.CheckElementIsEnable():
            return None
        if self.m_CurWand:
            oWand = self.m_Wand[self.m_CurWand]
            wandnet.GS2CAddWand(self.m_Game, self.m_Owner, dPlayer, oWand, bSyncOtherPlayer = True)
            oWand.SelfRefresh()
        self.RefreshAllSign()

    
    def SelfRefresh(self):
        if not self.CheckElementIsEnable():
            return None
        if self.m_Comp:
            dCompInfo = self.GetCompInfo(self.m_Comp)
            wandnet.GS2CUpdateBagComp(self.m_Game, self.m_PlayerID, dCompInfo)
        for oWand in self.m_Wand.values():
            if oWand.m_ID == self.m_CurWand:
                wandnet.GS2CWandOption(self.m_Game, self.m_PlayerID, WAND_EQUIP, self.m_CurWand)
                oWand.SelfRefresh()
                continue
            wandnet.GS2CAddWand(self.m_Game, self.m_Owner, {
                self.m_PlayerID: 1 }, oWand)
        

    
    def ChooseOption(self, iOption, *args):
        if iOption not in self.m_Options:
            WandLog.Alert('%s %s op err %s' % (self.m_Game.m_ID, self.m_PlayerID, iOption))
            return None
        (func, iMinLen) = self.m_Options[iOption]
        if len(args) < iMinLen:
            WandLog.Alert('%s %s res err %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iOption, args))
            return None
        func(*args)

    
    def SetCurWand(self, iWand):
        if self.m_CurWand == iWand:
            return None
        if iWand and iWand not in self.m_Wand:
            WandLog.Error('%s %s setcurwand %s invalid' % (self.m_Game.m_ID, self.m_PlayerID, iWand))
            return None
        oWand = self.m_Wand[iWand] if iWand else None
        sWandInfo = '%s-%s-%s' % (iWand, oWand.m_SID, oWand.m_Grade) if oWand else '0'
        WandLog.Debug('%s %s setcurwand %s' % (self.m_Game.m_ID, self.m_PlayerID, sWandInfo))
        oCurWand = self.m_Wand.get(self.m_CurWand, None)
        iDisableWandSID = 0
        if oCurWand:
            iDisableWandSID = oCurWand.m_SID
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDDISABLE, self.GetOwner(), {
                'WandSID': iDisableWandSID }, oGame = self.m_Game)
            oCurWand.Disable()
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        if self.m_CurWand:
            wandnet.GS2CWandGroupSendOption(self.m_Game, self.m_Owner, lstPlayer, WAND_UNEQUIP, self.m_CurWand)
        self.m_CurWand = iWand
        wandnet.GS2CWandOption(self.m_Game, self.m_PlayerID, WAND_EQUIP, iWand)
        if not oWand:
            return None
        if not self.m_Game.m_WarMgr.IsAIHero(self.m_Owner):
            oWand.Enable()
        oWand.GS2CCountChange(bComp = True, bWandCnt = True)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDENABLE, self.GetOwner(), {
            'Wand': oWand.m_ID,
            'WandSID': oWand.m_SID,
            'LastWand': iDisableWandSID,
            'WandTag': list(oWand.m_Tag) }, oGame = self.m_Game)
        dPlayer = { }
        for iPlayer in lstPlayer:
            if iPlayer == self.m_PlayerID:
                continue
            dPlayer[iPlayer] = 1
        
        if dPlayer:
            wandnet.GS2CAddWand(self.m_Game, self.m_Owner, dPlayer, oWand, bSyncOtherPlayer = True)

    
    def GetCurWand(self):
        if not self.m_CurWand:
            return None
        return self.m_Wand[self.m_CurWand]

    
    def UnEquipWand(self, iWand):
        if not self.m_CurWand:
            return None
        if self.m_CurWand != iWand:
            return None
        self.SetCurWand(0)

    
    def AddWandToContainer(self, oWand, sReason):
        if not oWand:
            return None
        oGame = self.m_Game
        if not self.ValidAddWand():
            WandLog.Debug('%s %s addwand to container valid %s %s' % (oGame.m_ID, self.m_PlayerID, oWand.m_SID, sReason))
            return None
        oWand.SetRedDot(True)
        oWand.AddToContainer(self)
        oWand.Init(oWand.m_Grade)
        oWand.OnSetGrade()
        self.AddWand(oWand, sReason = sReason)

    
    def SyncWandCompByPriority(self, oNewWand):
        lstSameWand = self.GetSameWand(oNewWand)
        if len(lstSameWand) <= 1:
            return None
        lstTmpWand = []
        oTmpWand = None
        for oWand in lstSameWand:
            if oWand.CheckEquipComp():
                lstTmpWand.append(oWand)
                if not oTmpWand and oWand.m_ID != oNewWand.m_ID:
                    oTmpWand = oWand
        
        if not lstTmpWand:
            return None
        if len(lstTmpWand) > 1:
            oCurWand = self.GetCurWand()
            if oCurWand in lstTmpWand:
                oTmpWand = oCurWand
            else:
                oTmpWand = lstTmpWand[0]
            for oWand in lstSameWand:
                if oWand.m_ID == oTmpWand.m_ID:
                    continue
                self.SyncWandComp(oWand, oTmpWand)
            

    
    def SyncWandComp(self, oWand, oTmpWand = None):
        from cl_wand.mobject import WAND_EMPTY_COMP
        if not oTmpWand:
            lstSameWand = self.GetSameWand(oWand)
            if not lstSameWand:
                return None
            oTmpWand = lstSameWand[0]
        dTmpCompInfo = DeepCopy(oTmpWand.m_CompTemp)
        for iType, dComp in oWand.m_CompTemp.items():
            for iPos, tComp in dComp.items():
                if not oTmpWand.IsFromConEquip(iType, iPos):
                    continue
                if iPos not in dTmpCompInfo[iType] or dTmpCompInfo[iType][iPos] == WAND_EMPTY_COMP:
                    oWand.RemoveComp(iType, iPos, 'syncwandcomp1', bSyncSameWand = False)
                    continue
                if tComp != WAND_EMPTY_COMP:
                    oWand.RemoveComp(iType, iPos, 'syncwandcomp2', bSyncSameWand = False)
                (iCompSID, iCompLevel) = dTmpCompInfo[iType][iPos]
                if not self.CheckBagComp(oWand, iType, iCompSID, iCompLevel):
                    continue
                oWand.AddCustomComp(iType, iPos, iCompSID, iCompLevel, sReason = 'syncwandcomp3', bSyncSameWand = False)
            
            wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, [
                self.GetOwner().m_PlayerID], oWand)
        

    
    def AddWand(self, oWand, iSetCurWand = 0, iNotify = 1, sReason = ''):
        self.SyncWandComp(oWand)
        self.m_Wand[oWand.m_ID] = oWand
        WandLog.Debug('%s %s addwand %s-%s-%s-%s' % (self.m_Game.m_ID, self.m_PlayerID, oWand.m_ID, oWand.m_SID, oWand.m_Grade, sReason))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCHANGE, self.GetOwner(), {
            'Wand': oWand.m_ID,
            'WandSID': oWand.m_SID,
            'Reason': sReason,
            'Quality': oWand.GetWandQuality() }, oGame = self.m_Game, iSub = WAND_SUBMSG_ADD)
        wandnet.GS2CAddWand(self.m_Game, self.m_Owner, {
            self.m_PlayerID: 1 }, oWand)
        if iSetCurWand or len(self.m_Wand) == 1:
            self.SetCurWand(oWand.m_ID)
        if iNotify:
            iOldGrade = oWand.m_Grade
            oNewWand = self.TryUpgradeWand(oWand)
            iUpgrade = 1 if oNewWand.m_Grade > iOldGrade else 0
            wandnet.GS2CAddWandNotify(self.m_Game, self.m_PlayerID, NOTIFY_TYPE_WAND, oNewWand.m_SID, oNewWand.m_Grade, iUpgrade)
        else:
            self.TryUpgradeWand(oWand)

    
    def RewardWand(self, iWandSID, iLevel, sReason, iNotify = 1):
        oWand = self.CreateWand(iWandSID, iLevel, sReason)
        if not oWand:
            return None
        self.AddWand(oWand, iNotify = iNotify, sReason = sReason)
        return oWand

    
    def TryUpgradeWand(self, oWand):
        iCurGrade = oWand.m_Grade
        if iCurGrade + 1 not in oWand.GetWandLevelInfo():
            return oWand
        dSameWand = { }
        iWandSID = oWand.m_SID
        iMaxGrade = oWand.m_MaxGrade
        for oOtherWand in self.m_Wand.values():
            if oOtherWand.m_ID == oWand.m_ID:
                continue
            if not oOtherWand.m_SID == iWandSID or oOtherWand.m_EvolutionTarget == iWandSID:
                if oOtherWand.m_SID == oWand.m_EvolutionTarget:
                    iOtherGrade = oOtherWand.m_Grade
                    if iOtherGrade != iMaxGrade or iOtherGrade not in dSameWand:
                        dSameWand[iOtherGrade] = [
                            oOtherWand]
                        continue
                    dSameWand[iOtherGrade].append(oOtherWand)
                    continue
        
        if iCurGrade not in dSameWand or len(dSameWand[iCurGrade]) < WAND_UPGRADE_TIMES - 1:
            return oWand
        sReason = 'Upgrade'
        oUpgradeWand = oWand
        for iGrade in range(iCurGrade, iMaxGrade):
            if iGrade not in dSameWand or len(dSameWand[iGrade]) < WAND_UPGRADE_TIMES - 1:
                break
            lstSameWand = dSameWand[iGrade]
            lstCarryAbility = []
            for oSameWand in lstSameWand + [
                oUpgradeWand]:
                oSameWand.SetTmp('WandUpgrade', 1)
            
            for oSameWand in lstSameWand:
                if (oSameWand.m_EvolutionTarget == oUpgradeWand.m_SID or oUpgradeWand.m_ID == self.m_CurWand) and oUpgradeWand.m_EvolutionTarget != oSameWand.m_SID:
                    if oSameWand.m_CarryWandAbility:
                        lstCarryAbility = oSameWand.m_CarryWandAbility
                    self.RemoveWand(oSameWand.m_ID, sReason, iDrop = 0)
                    continue
                if oUpgradeWand.m_ID == self.m_CurWand:
                    self.SetCurWand(oSameWand.m_ID)
                if oUpgradeWand.m_CarryWandAbility:
                    lstCarryAbility = oUpgradeWand.m_CarryWandAbility
                self.RemoveWand(oUpgradeWand.m_ID, sReason, iDrop = 0)
                oUpgradeWand = oSameWand
            
            if lstCarryAbility:
                oUpgradeWand.SetCarryAbility(lstCarryAbility)
            oUpgradeWand.Upgrade()
            oUpgradeWand.RemoveTmp('WandUpgrade')
        
        dPlayer = self.GetSendPlayer(oUpgradeWand.m_ID)
        wandnet.GS2CAddWand(self.m_Game, self.m_Owner, dPlayer, oUpgradeWand, bSyncOtherPlayer = True)
        oUpgradeWand.SelfRefresh()
        return oUpgradeWand

    
    def CreateWand(self, iWand, iLevel, sReason, dWand = None):
        oGame = self.m_Game
        if not self.ValidAddWand():
            WandLog.Debug('%s %s createwand valid %s-%s-%s' % (oGame.m_ID, self.m_PlayerID, iWand, iLevel, sReason))
            return None
        oWand = cl_wand.CreateWand(oGame, self, iWand, iLevel, dWand, dTmp = {
            'Reason': sReason })
        if not oWand:
            WandLog.Alert('%s %s createwand nowand %s-%s-%s' % (oGame.m_ID, self.m_PlayerID, iWand, iLevel, sReason))
            return None
        WandLog.Debug('%s %s createwand %s-%s %s' % (oGame.m_ID, self.m_PlayerID, iWand, iLevel, sReason))
        return oWand

    
    def CheckWandMax(self):
        if len(self.m_Wand) >= WAND_MAX:
            return 0
        return 1

    
    def ValidAddWand(self):
        if not self.CheckWandMax():
            return 0
        return 1

    
    def GetAllWand(self):
        return self.m_Wand

    
    def GetAllBagComp(self):
        return self.m_Comp

    
    def RemoveWand(self, iWand, sReason = 'Remove', iDrop = 1):
        if iWand not in self.m_Wand:
            return None
        oWand = self.m_Wand[iWand]
        iWandSID = oWand.m_SID
        if iDrop and not GetWandDropInfo(iWandSID):
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCHANGE, self.GetOwner(), {
            'Wand': iWand }, oGame = self.m_Game, iSub = WAND_SUBMSG_REMOVE)
        WandLog.Debug('%s %s removewand %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iWandSID, sReason))
        if iWand == self.m_CurWand:
            self.SetCurWand(0)
        self.m_Wand.pop(iWand)
        dPlayer = self.GetSendPlayer(iWand)
        wandnet.GS2CWandGroupSendOption(self.m_Game, self.m_Owner, dPlayer, WAND_REMOVE, iWand)
        if not iDrop:
            oWand.Release()
        else:
            oWand.RemoveFromContainer(sReason)
            oOwner = self.GetOwner()
            if oOwner:
                oWand.m_Source = oOwner.m_PlayerID
                cl_drop.DropItem(oOwner, oWand, bFly = True)

    
    def ReplaceWand(self, iWandID, iNewSID):
        if iWandID not in self.m_Wand:
            return None
        oGame = self.m_Game
        oOldWand = self.m_Wand[iWandID]
        iIsEvolution = 0
        dTmp = { }
        if iNewSID == oOldWand.m_EvolutionTarget:
            iIsEvolution = 1
            dTmp['BanInitAbility'] = 1
        oNewWand = cl_wand.CreateWand(oGame, self, iNewSID, oOldWand.m_Grade, { }, 0, dTmp)
        if not oNewWand:
            WandLog.Alert('%s %s replacewand nowand %s-%s' % (oGame.m_ID, self.m_PlayerID, iNewSID, oOldWand.m_Grade))
            return None
        dAllComp = oOldWand.GetAllDismantleComp()
        for iType, lstComp in dAllComp.items():
            for iCompSID, iCompLevel in lstComp:
                iPos = oNewWand.GetEmptyPosByType(iType)
                oNewWand.AddCustomComp(iType, iPos, iCompSID, iCompLevel)
            
        
        iSetCurWand = 1 if self.m_CurWand == iWandID else 0
        if iIsEvolution:
            oNewWand.RemoveTmp('BanInitAbility')
            lstCarryAbility = oOldWand.m_CarryWandAbility
            oNewWand.SetCarryAbility(lstCarryAbility)
            if oNewWand.GetWandQuality() == WAND_QUALITY_TALE:
                if oOldWand.Query('UseCarryWandAbility'):
                    oNewWand.InitWandAbility('replace')
                else:
                    lstAbility = oOldWand.GetWandAbilityInfo()
                    oNewWand.SetWandAbility(lstAbility, 'replace')
        self.RemoveWand(iWandID, 'Replace', iDrop = 0)
        self.AddWand(oNewWand, iSetCurWand, sReason = 'replace')

    
    def GetWandByID(self, iWand):
        if iWand not in self.m_Wand:
            return None
        return self.m_Wand[iWand]

    
    def GetWand(self, iWandSID, iQuality = 1):
        for oWand in self.m_Wand.values():
            if oWand.m_SID == iWandSID and oWand.m_Quality == iQuality:
                return oWand
        

    
    def ValidAddComp(self, iComp, iLevel, sReason):
        clsWandComp = cl_wand.GetWandCompCls(iComp)
        if not clsWandComp or iLevel not in clsWandComp.m_ActionInfo:
            WandLog.Alert('%s %s nocomp %s-%s-%s' % (self.m_Game.m_ID, self.m_PlayerID, iComp, iLevel, sReason))
            return 0
        if iComp in self.m_Comp:
            dCompNum = self.m_Comp[iComp]
            if iLevel in dCompNum and dCompNum[iLevel] >= COMP_ONELEVEL_MAX:
                return 0
        return 1

    
    def AddBagComp(self, iComp, iLevel, iNum, sReason, iNotify = 1):
        if not self.ValidAddComp(iComp, iLevel, sReason):
            return 0
        WandLog.Debug('%d %d addbagcomp %d %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iComp, iLevel, iNum, sReason))
        if iComp not in self.m_Comp:
            self.m_Comp[iComp] = { }
        dCompNum = self.m_Comp[iComp]
        if iLevel in dCompNum:
            dCompNum[iLevel] += iNum
        else:
            dCompNum[iLevel] = iNum
        iType = GetWandCompType(iComp)
        self.AddSortedBagComp(iComp, iType, iLevel)
        if iType == WAND_COMP_TYPE_ACTION and sReason != 'wandinit' and self.m_CurWand and iLevel > min(dCompNum):
            oCurWand = self.m_Wand[self.m_CurWand]
            lstWand = self.GetSameWand(oCurWand)
            for oWand in lstWand:
                bResult = False
                for _ in range(iNum):
                    if not oWand.AutoUpdateComp(iType, iComp, iLevel):
                        break
                    bResult = True
                
                if bResult:
                    dPlayer = self.GetSendPlayer(oWand.m_ID)
                    wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, dPlayer, oWand)
            
        if sReason != 'initial':
            self.AddCompRedDot(iComp, iLevel)
        dCompInfo = self.GetCompInfo({
            iComp: dCompNum })
        wandnet.GS2CUpdateBagComp(self.m_Game, self.m_PlayerID, dCompInfo)
        if iNotify:
            wandnet.GS2CAddWandNotify(self.m_Game, self.m_PlayerID, NOTIFY_TYPE_WANDCOMP, iComp, iLevel, 0)
        oOwner = self.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, oOwner, {
                'CompSID': iComp,
                'Quality': iLevel }, iSub = WANDCOMP_SUBMSG_ADDCOMP_TO_CONTAINER)
        return iLevel

    
    def GetCompInfo(self, dComp):
        dCompInfo = { }
        for iComp, dCompNum in dComp.items():
            dCompInfo[iComp] = []
            for iLevel, iNum in dCompNum.items():
                if (iComp, iLevel) in self.m_CompRedDot:
                    bRedDot = True
                else:
                    bRedDot = False
                dCompInfo[iComp].append((iLevel, iNum, bRedDot))
            
        
        return dCompInfo

    
    def GetBagCompNum(self, iComp, iLevel):
        if iComp not in self.m_Comp:
            return 0
        dCompNum = self.m_Comp[iComp]
        if iLevel not in dCompNum:
            return 0
        return dCompNum[iLevel]

    
    def GetSameWand(self, oSourceWand):
        iQuality = oSourceWand.m_Quality
        if iQuality == WAND_QUALITY_TALE:
            return [
                oSourceWand]
        iWandSID = oSourceWand.m_SID
        return [ oWand for oWand in self.m_Wand.values() if oWand.m_Quality == iQuality ]

    
    def AddWandComp(self, iWandID, iCompPos, iComp, iLevel):
        if iWandID not in self.m_Wand:
            return 0
        oWand = self.m_Wand[iWandID]
        if not oWand:
            return 0
        return self.AddCompToWand(oWand, iCompPos, iComp, iLevel)

    
    def AddCompToWand(self, oWand, iCompPos, iComp, iLevel):
        iType = GetWandCompType(iComp)
        if iType is None:
            return 0
        if not self.CheckBagComp(oWand, iType, iComp, iLevel):
            return 0
        iCompID = oWand.AddCustomComp(iType, iCompPos, iComp, iLevel)
        if not iCompID:
            return 0
        dPlayer = self.GetSendPlayer(oWand.m_ID)
        wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, dPlayer, oWand)
        oWand.GS2CWandConditionCompCountChange([
            iCompID])
        return 1

    
    def CheckBagComp(self, oWand, iType, iComp, iLevel):
        if oWand.GetEquipCompNum(iType, iComp, iLevel) >= self.GetBagCompNum(iComp, iLevel):
            return 0
        return 1

    
    def RemoveWandComp(self, iWandID, iCompPos, iComp, _iLevel):
        if iWandID not in self.m_Wand:
            return None
        iType = GetWandCompType(iComp)
        if iType is None:
            return None
        oWand = self.m_Wand[iWandID]
        if not oWand.CheckRemoveComp(iType, iCompPos):
            oOwner = self.GetOwner()
            WandLog.Alert('%s %s illegal remove %s %s %s ' % (self.m_Game.m_ID, oOwner.m_PlayerID, oWand.m_SID, iType, iCompPos))
            return None
        if oWand.RemoveCustomComp(iType, iCompPos):
            dPlayer = self.GetSendPlayer(iWandID)
            wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, dPlayer, oWand)

    
    def RecycleWand(self, iWandID):
        if iWandID not in self.m_Wand:
            return None
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        if not oWandElement:
            return None
        oHero = self.GetOwner()
        if oHero.IsDead():
            return None
        oWand = self.m_Wand[iWandID]
        if not GetWandRecycleInfo(oWand.m_SID):
            return None
        iPrice = oWandElement.CalRecycleWandPrice(oWand)
        self.RemoveWand(iWandID, iDrop = 0)
        iPrice = oHero.AddCash(iPrice, 'RecycleWand')
        cl_snetwar.GS2CRecycleDropResult(self.m_Game, 0, oHero.m_ID, 1, CURRENCY_CASH, iPrice, {
            self.m_PlayerID: 1 })

    
    def RecycleComp(self, iComp, iLevel):
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        if not oWandElement:
            return None
        oHero = self.GetOwner()
        if oHero.IsDead():
            return None
        if not GetWandCompRecycleInfo(iComp):
            return None
        if not self.RemoveComp(iComp, iLevel, iNum = 1, sReason = 'Recycle', iDrop = 0):
            return None
        iPrice = oWandElement.CalRecycleWandCompPrice(iComp, iLevel)
        iPrice = oHero.AddCash(iPrice, 'RecycleComp')
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEDROP, oHero, {
            'RecycleDropType': NWARRIOR_DROP_WANDCOMP }, iSub = RECYCLE_UNDROP)
        cl_snetwar.GS2CRecycleDropResult(self.m_Game, 0, oHero.m_ID, 1, CURRENCY_CASH, iPrice, {
            self.m_PlayerID: 1 })

    
    def GetCompHasNum(self, iComp, iLevel):
        if iComp not in self.m_Comp or iLevel not in self.m_Comp[iComp]:
            return 0
        return self.m_Comp[iComp][iLevel]

    
    def BatchRecycleComp(self, lstComp):
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        if not oWandElement:
            return None
        oHero = self.GetOwner()
        if oHero.IsDead():
            return None
        iAllPrice = 0
        for iComp, iLevel in lstComp:
            iNum = self.GetCompHasNum(iComp, iLevel)
            if not iNum or not GetWandCompRecycleInfo(iComp) or not self.RemoveComp(iComp, iLevel, iNum, sReason = 'BatchRecycle', iDrop = 0):
                continue
            iAllPrice += oWandElement.CalRecycleWandCompPrice(iComp, iLevel) * iNum
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEDROP, oHero, {
                'RecycleDropType': NWARRIOR_DROP_WANDCOMP }, iSub = RECYCLE_UNDROP)
        
        if not iAllPrice:
            return None
        iAllPrice = oHero.AddCash(iAllPrice, 'BatchRecycleComp')
        cl_snetwar.GS2CRecycleDropResult(self.m_Game, 0, oHero.m_ID, 1, CURRENCY_CASH, iAllPrice, {
            self.m_PlayerID: 1 })

    
    def RemoveComp(self, iComp, iLevel, iNum = 1, sReason = 'Remove', iDrop = 1):
        if iComp not in self.m_Comp:
            return 0
        dComp = self.m_Comp[iComp]
        if iLevel not in dComp:
            return 0
        if iDrop and not GetWandCompDropInfo(iComp):
            return 0
        iCurNum = dComp[iLevel]
        if iNum > iCurNum:
            WandLog.Alert('%s %s removecomp %d %d %d>%d %s' % (self.m_Game.m_ID, self.m_PlayerID, iComp, iLevel, iNum, iCurNum, sReason))
            iNum = iCurNum
        WandLog.Debug('%s %s removecomp %d %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iComp, iLevel, iNum, sReason))
        dComp[iLevel] -= iNum
        if dComp[iLevel] <= 0:
            dComp.pop(iLevel)
        iType = GetWandCompType(iComp)
        self.RemoveSortedBagComp(iComp, iType, iLevel)
        self.OnChangeBagCompNum(iComp)
        if iDrop:
            for _ in range(iNum):
                self.DropComp(iComp, iLevel)
            
        oOwner = self.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, oOwner, {
                'CompSID': iComp,
                'Quality': iLevel,
                'RemoveNum': iNum }, iSub = WANDCOMP_SUBMSG_REMOVECOMP_FROM_CONTAINER)
        return 1

    
    def DropComp(self, iComp, iLevel):
        iHero = self.m_Owner
        oGame = self.m_Game
        oHero = self.GetOwner()
        iScene = oHero.m_Scene
        dExtraInfo = {
            'Abandoner': iHero }
        dStaticInfo = {
            'DropSource': oHero.m_PlayerID }
        oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_WANDCOMP, oHero.GetPos(), [
            {
                'WandCompSID': iComp,
                'WandCompLevel': iLevel }], dExtraInfo, dStaticInfo, iOwner = 0)

    
    def OnChangeBagCompNum(self, iComp):
        dCompNum = {
            iComp: self.m_Comp[iComp] }
        dCompInfo = self.GetCompInfo(dCompNum)
        wandnet.GS2CUpdateBagComp(self.m_Game, self.m_PlayerID, dCompInfo)
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        for iWand, oWand in self.m_Wand.items():
            oWand.OnChangeCompNum(dCompNum)
            if iWand == self.m_CurWand:
                wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, lstPlayer, oWand)
                continue
            wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, {
                self.m_PlayerID: 1 }, oWand)
        

    
    def AddSortedBagComp(self, iComp, iType, iLevel):
        if iType not in self.m_SortedBagComp or iLevel not in self.m_SortedBagComp[iType]:
            return None
        lstSortedComp = self.m_SortedBagComp[iType][iLevel]
        lstSortedComp.append(iComp)
        lstSortedComp.sort()

    
    def RemoveSortedBagComp(self, iComp, iType, iLevel):
        if iType not in self.m_SortedBagComp or iLevel not in self.m_SortedBagComp[iType]:
            return None
        lstSortedComp = self.m_SortedBagComp[iType][iLevel]
        if iComp in lstSortedComp:
            lstSortedComp.remove(iComp)

    
    def QuickAddWandComp(self, iWandID, lstComp):
        from cl_wand.mobject import WAND_EMPTY_COMP
        if not (self.m_Comp) or iWandID not in self.m_Wand:
            return None
        WandLog.Debug('%s %s quickadd wand:%s complist:%s' % (self.m_Game.m_ID, self.m_PlayerID, iWandID, lstComp))
        dSortedBagComp = DeepCopy(self.m_SortedBagComp)
        for iCompPos, iComp, iLevel in lstComp:
            if self.AddWandComp(iWandID, iCompPos, iComp, iLevel):
                iType = GetWandCompType(iComp)
                if iType not in dSortedBagComp or iLevel not in dSortedBagComp[iType]:
                    continue
                dInfo = dSortedBagComp[iType][iLevel]
                if iComp in dInfo:
                    dInfo.remove(iComp)
        
        lstGuaranteeAdd = []
        oTmpWand = self.m_Wand[iWandID]
        dCompTemp = oTmpWand.GetCompTemp()
        for iType, dPosInfo in dCompTemp.items():
            if iType not in dSortedBagComp:
                continue
            for iPos, (iCompSID, iCompLevel) in dPosInfo.items():
                if (iCompSID, iCompLevel) != WAND_EMPTY_COMP:
                    continue
                for iLevel, lstSortedBagComp in dSortedBagComp[iType].items():
                    if not lstSortedBagComp:
                        continue
                    iAddComp = lstSortedBagComp.pop(0)
                    lstGuaranteeAdd.append((iPos, iAddComp, iLevel))
                    self.AddWandComp(iWandID, iPos, iAddComp, iLevel)
                
            
        
        if lstGuaranteeAdd:
            WandLog.Debug('%s %s quickadd guarantee wand:%s compinfo:%s' % (self.m_Game.m_ID, self.m_PlayerID, iWandID, lstGuaranteeAdd))

    
    def GetCurWandData(self):
        if not self.m_CurWand:
            return { }
        oWand = self.m_Wand[self.m_CurWand]
        (iLevel, iColdTime, iConditionCompNum, iActionCompNum, lstComInfo, lstAbilities) = oWand.GetWandShowInfo()
        dWandInfo = {
            'iWandSID': oWand.m_SID,
            'iRareLevel': iLevel,
            'iCD': iColdTime,
            'iConditionGrooveNum': iConditionCompNum,
            'iBehaviorGrooveNum': iActionCompNum,
            'lstComp': lstComInfo,
            'lstAbilities': lstAbilities }
        return dWandInfo

    
    def GetSendPlayer(self, iWandID):
        if iWandID == self.m_CurWand:
            lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
            return dict.fromkeys(lstPlayer, 1)
        return {
            self.m_PlayerID: 1 }

    
    def ProcessCntCache(self, iWand, lstComp, bWandCnt):
        if iWand != self.m_CurWand:
            return None
        oWand = self.m_Wand[iWand]
        bComp = True if lstComp else False
        oWand.GS2CCountChange(bComp, bWandCnt, lstComp)

    
    def ClearWandRedDot(self, iWand):
        if iWand:
            if iWand in self.m_Wand:
                oWand = self.m_Wand[iWand]
                oWand.SetRedDot(False)
            return None
        for oWand in self.m_Wand.values():
            oWand.SetRedDot(False)
        

    
    def AddCompRedDot(self, iComp, iLevel):
        self.m_CompRedDot[(iComp, iLevel)] = 1

    
    def ClearCompRedDot(self, iComp, iLevel):
        if not iComp:
            self.m_CompRedDot = { }
            return None
        tComp = (iComp, iLevel)
        if tComp not in self.m_CompRedDot:
            return None
        self.m_CompRedDot.pop(tComp)

    
    def AddSign(self, iType, iSID, iRefresh = 1):
        if iType not in self.m_Sign or iSID in self.m_Sign[iType]:
            return None
        self.m_Sign[iType].append(iSID)
        if iRefresh:
            self.RefreshAllSign()

    
    def DelSign(self, iType, iSID, iRefresh = 1):
        if iType not in self.m_Sign or iSID not in self.m_Sign[iType]:
            return None
        self.m_Sign[iType].remove(iSID)
        if iRefresh:
            self.RefreshAllSign()

    
    def RefreshAllSign(self):
        wandnet.GS2CS5PackSignInfo(self.m_Game, self.m_PlayerID, self.m_Sign)

    
    def GetSignByItemType(self, iType):
        if iType in self.m_Sign:
            return self.m_Sign[iType]
        return []

    
    def AddWandAbility(self, iWand, iAbility, iQuality = 0, iFloatingRange = 0, sReason = ''):
        if iWand not in self.m_Wand:
            return 0
        oWand = self.m_Wand[iWand]
        if oWand.AddWandAbility(iAbility, iQuality, iFloatingRange, sReason):
            dPlayer = self.GetSendPlayer(oWand.m_ID)
            wandnet.GS2CAddWand(self.m_Game, self.m_Owner, dPlayer, oWand, bSyncOtherPlayer = True)
            return 1
        return 0

    
    def RemoveWandAbility(self, iWand, iAbility, sReason):
        if iWand not in self.m_Wand:
            return 0
        oWand = self.m_Wand[iWand]
        if oWand.RemoveWandAbility(iAbility, sReason):
            dPlayer = self.GetSendPlayer(oWand.m_ID)
            wandnet.GS2CAddWand(self.m_Game, self.m_Owner, dPlayer, oWand, bSyncOtherPlayer = True)
            return 1
        return 0

    
    def GetWandRollAbility(self, iWand, iOptionNum, iNegativeRatio, dHasNegativeyWeight, dNotNegativeyWeight, dCertainlyQuality, iPointAbilityWeight, dLockAppointWeight):
        if iWand not in self.m_Wand:
            return { }
        oWand = self.m_Wand[iWand]
        dAllAbility = { }
        iOptionInit = ROLLABILITY_OPTION + 1
        for iOption in range(iOptionInit, iOptionNum + iOptionInit):
            lstAbility = oWand.ChooseWandAbility(iNegativeRatio, dHasNegativeyWeight, dNotNegativeyWeight, dCertainlyQuality, sReason = 'Roll', iRetainLockWandAbility = 1, iPointAbilityWeight = iPointAbilityWeight, dLockAppointWeight = dLockAppointWeight)
            if lstAbility:
                dAllAbility[iOption] = lstAbility
        
        return dAllAbility

    
    def SetWandAbility(self, iWand, lstAbility, sReason):
        if iWand not in self.m_Wand:
            return None
        oWand = self.m_Wand[iWand]
        oWand.SetWandAbility(lstAbility, sReason)
        dPlayer = self.GetSendPlayer(oWand.m_ID)
        wandnet.GS2CAddWand(self.m_Game, self.m_Owner, dPlayer, oWand, bSyncOtherPlayer = True)
        oWand.SelfRefresh()

    
    def LockWandAbility(self, iWand, iAbility, iLock):
        if iWand not in self.m_Wand:
            return None
        oWand = self.m_Wand[iWand]
        oWand.LockWandAbility(iAbility, iLock)
        dPlayer = self.GetSendPlayer(oWand.m_ID)
        wandnet.GS2CAddWand(self.m_Game, self.m_Owner, dPlayer, oWand, bSyncOtherPlayer = True)

    
    def RefreshWand(self, oWand):
        dPlayer = self.GetSendPlayer(oWand.m_ID)
        wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, dPlayer, oWand)


