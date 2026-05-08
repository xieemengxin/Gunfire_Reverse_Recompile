# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/weaponstoreelement.pyc
# RelativePath: clientlogic/cl_warmgr/weaponstoreelement.pyc
# Source Generated with Decompyle++
# File: weaponstoreelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_cscommondef.cs_fight import LEVEL_TYPE_HIDE, LEVEL_TYPE_BOSS, NWARRIOR_NPC_WEAPONSTORE
from cl_only import DeepCopy
from cl_object.logging import WeaponstoreLog
from cl_commondefines import BAG_TYPE_WEAPONSTORE, LAYER_CHOOSE_HIDE, BAG_TYPE_WIELD, BAG_TYPE_EXWEAPON, ROUND_EXTRULE_HIDELEVEL_APPEARCHALLENGE, NWARRIOR_DROP_EQUIP, LINK_QUIT, LINK_DISCONNECT, LINK_ONLINE
from cl_warmgr.bigdataanalyse import CWeaponStoreAnalyseCom
from cl_cscommondef.cs_itemdef import EQUIP_TYPE_MAINWEAPON
from cl_npc.net import GS2CWeaponAnimaInfo
import cl_msgcenter
import cl_item.defines as itemdef
import cl_netattr
NPC_HIDELEVEL_NUM = 1
DEFAULT_ADDINSCRIPTION_TIMES = 1
SETTLE_WEAPON_LAYER = 4

class CWeaponStoreElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CWeaponStoreElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_CallFlag = 'WeaponStoreElement'
        self.m_ReplaceNpc = self.m_Data.m_Config.get('ReplaceNpc', { })
        self.m_FilterHideLevel = self.m_Data.m_Config.get('FilterHideLevel', ())
        self.m_FilterChallenge = self.m_Data.m_Config.get('FilterChallenge', ())
        self.m_LimitChallengeType = self.m_Data.m_Config.get('LimitChallengeType', ())
        self.m_RefreshNpcLayer = self.m_Data.m_Config.get('RefreshNpcLayer', ())
        self.m_LimitHideLevelType = self.m_Data.m_Config.get('LimitHideLevelType', ())
        self.m_AnimaCost = self.m_Data.m_Config.get('AnimaCost', 0)
        self.m_MaxAnimaNum = self.m_Data.m_Config.get('MaxAnimaNum', 0)
        self.m_SettleWeaponInfo = { }
        self.m_ExchangeWeaponInfo = []
        self.m_UnWarWeapon = []
        self.m_InjectAnimaInfo = { }
        self.m_WaitCreateNpc = []
        self.m_InitWeaponInfo = { }
        self.m_InjectAnimaWeaponCache = { }
        self.m_LoadLevelSavePosInfo = { }
        self.m_InjectAnimaWeaponDropInfo = { }

    
    def Init(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        self.InitFilterHideLevel()
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.OnCreateNpc, 'ReplaceNpc' + self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CHOOSECNT, self.OnChooseCnt, 'ChooseCnt' + self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.InitData, 'InitData' + self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelNodeGoalOk, 'LevelNodeGoalOk' + self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, 'LevelNodeFinish' + self.m_CallFlag, -1, 0)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDWEAPONCOM, self.OnAddWeaponCom, 'AddWeaponCom' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDWEAPON, self.OnAddWeapon, 'AddWeapon' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OnChangePlayerLinkStatus, 'ChangePlayerLinkStatus' + self.m_CallFlag)
        self.m_WarMgr.AddRoundExtRule(ROUND_EXTRULE_HIDELEVEL_APPEARCHALLENGE, {
            'LimitChallengeType': self.m_LimitChallengeType }, self.m_CallFlag)

    
    def Release(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, 'ReplaceNpc' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CHOOSECNT, 'ChooseCnt' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'InitData' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'LevelNodeGoalOk' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'LevelNodeFinish' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDWEAPONCOM, 'AddWeaponCom' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDWEAPON, 'AddWeapon' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, 'ChangePlayerLinkStatus' + self.m_CallFlag)
        super(CWeaponStoreElement, self).Release()
        self.m_WarMgr = None

    
    def Save(self):
        dData = { }
        dData['IA'] = DeepCopy(self.m_InjectAnimaInfo)
        dData['IW'] = DeepCopy(self.m_InitWeaponInfo)
        dData['LSP'] = self.GetLevelSavePosInfo()
        dData['IAWC'] = self.m_InjectAnimaWeaponCache
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_InjectAnimaInfo = dData['IA']
        self.m_InitWeaponInfo = dData.get('IW', { })
        self.m_LoadLevelSavePosInfo = dData.get('LSP', { })
        self.m_InjectAnimaWeaponCache = dData.get('IAWC', { })

    
    def GetLevelSavePosInfo(self):
        LevelSavePosInfo = { }
        for iHero in self.m_WarMgr.GetRoomHero():
            oHero = self.m_WarMgr.m_Game.GetObject(iHero)
            if not oHero:
                continue
            oWeaponStoreCom = oHero.m_WeaponStoreCon
            LevelSavePosInfo[oHero.m_PlayerID] = DeepCopy(oWeaponStoreCom.m_LevelSavePos)
        
        return LevelSavePosInfo

    
    def SetLevelSavePosInfo(self, dData):
        for pid, lstLevelSavePos in dData.items():
            oHero = self.m_WarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            oWeaponStoreCom = oHero.m_WeaponStoreCon
            oWeaponStoreCom.m_LevelSavePos = lstLevelSavePos
        

    
    def OnAddWeaponCom(self, oWarMgr, oTarget, dInfo):
        oWeapon = dInfo['Weapon']
        iBagType = dInfo['BagType']
        self.DealAnimaSavePosInfo(oTarget, oWeapon, iBagType)
        if iBagType != BAG_TYPE_WEAPONSTORE:
            return None
        if oTarget.m_WeaponStoreCon.m_LoadFlag and oWeapon.m_ID not in self.m_ExchangeWeaponInfo:
            self.m_ExchangeWeaponInfo.append(oWeapon.m_ID)
        if oTarget.m_PlayerID not in self.m_InjectAnimaInfo:
            return None
        dInjectAnimaInfo = self.m_InjectAnimaInfo[oTarget.m_PlayerID]
        if oWeapon.m_ID in dInjectAnimaInfo:
            dInjectAnimaInfo[oWeapon.m_ID] = oWeapon.m_Pos
            self.RefreshAnimaWeaponInfo(oTarget.m_PlayerID)

    
    def OnAddWeapon(self, oWarMgr, oTarget, dInfo):
        oWeapon = dInfo['Weapon']
        self.DealAnimaSavePosInfo(oTarget, oWeapon, BAG_TYPE_WIELD)

    
    def OnChangePlayerLinkStatus(self, oWarMgr, oTarget, dInfo):
        iNewStatus = dInfo.get('LinkStatus', None)
        if iNewStatus != LINK_QUIT:
            return None
        if oTarget.m_PlayerID not in self.m_InjectAnimaInfo:
            return None
        dSaveData = self.DealLevelWeaponAnimaInfo(oTarget.m_PlayerID)
        oTarget.m_WeaponStoreCon.SaveWeaponToPlayerInfo(dSaveData)

    
    def DealAnimaSavePosInfo(self, oHero, oWeapon, iBagType):
        iInjectOwner = oWeapon.Query('InjectOwner', 0)
        if iInjectOwner in self.m_InjectAnimaInfo and iInjectOwner == oHero.m_PlayerID:
            dInjectAnimaInfo = self.m_InjectAnimaInfo[iInjectOwner]
            if oWeapon.m_ID not in dInjectAnimaInfo:
                return None
            if iBagType == BAG_TYPE_WIELD:
                oContainer = oHero.m_WieldCon
            elif iBagType == BAG_TYPE_EXWEAPON:
                oContainer = oHero.m_ExWeaponCon
            elif iBagType == BAG_TYPE_WEAPONSTORE:
                oContainer = oHero.m_WeaponStoreCon
            else:
                return None
            if self.CheckInjectDataChange(oWeapon, oContainer):
                iSavePos = dInjectAnimaInfo[oWeapon.m_ID]
                self.InjectSave(oHero, oContainer, iSavePos, oWeapon)
            self.ClearInjectAnimaWeaponCache(oHero.m_PlayerID, oWeapon.m_ID)
        if oWeapon.m_ID in self.m_InjectAnimaWeaponDropInfo:
            self.m_InjectAnimaWeaponDropInfo.pop(oWeapon.m_ID)

    
    def OnLevelNodeFinish(self, oWarMgr, dInfo):
        self.m_SettleWeaponInfo = { }
        self.m_InjectAnimaWeaponDropInfo = { }

    
    def DealLevelWeaponAnimaInfo(self, pid):
        oHero = self.m_WarMgr.GetHeroByPlayer(pid)
        if pid not in self.m_InjectAnimaInfo:
            return { }
        dWeaponInjectInfo = self.m_InjectAnimaInfo[pid]
        dLevelSaveData = { }
        for iWeapon, iPos in dWeaponInjectInfo.items():
            oContainer = self.GetContainerByWeaponID(oHero, iWeapon)
            if not oContainer:
                continue
            oWeapon = oContainer.GetItemByID(iWeapon)
            if self.CheckInjectDataChange(oWeapon, oContainer):
                dSaveData = oContainer.GetWeaponItemSaveInfo(oWeapon)
                dLevelSaveData[iPos] = dSaveData
                oWeapon.Set('LastInjectSaveData', dSaveData)
        
        return dLevelSaveData

    
    def CheckInjectDataChange(self, oWeapon, oContainer):
        dLastInjectSaveData = oWeapon.Query('LastInjectSaveData', { })
        dSaveData = oContainer.GetWeaponItemSaveInfo(oWeapon)
        if dLastInjectSaveData and dLastInjectSaveData != dSaveData:
            return True
        return False

    
    def GetContainerByWeaponID(self, oHero, iWeapon):
        oContainer = None
        if iWeapon in oHero.m_WieldCon.m_ItemID:
            oContainer = oHero.m_WieldCon
        elif iWeapon in oHero.m_ExWeaponCon.m_ItemID:
            oContainer = oHero.m_ExWeaponCon
        elif iWeapon in oHero.m_WeaponStoreCon.m_ItemID:
            oContainer = oHero.m_WeaponStoreCon
        return oContainer

    
    def InitData(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetAllHero():
            oHero = oWarMgr.m_Game.GetObject(iHero)
            if not oHero:
                continue
            self.InitExWeaponCon(oHero)
            self.SetInitWeapon(oHero.m_PlayerID, oHero.m_WeaponStoreCon)
            oHero.AddMapLoadOKCbFun(self.m_CallFlag, self.OnMapLoadOK)
        
        oBigdataMgr = self.m_WarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CWeaponStoreAnalyseCom(self.m_Game)
            oBigdataMgr.SetCom('WeaponStore', oAnalyseCom)
        if self.m_LoadLevelSavePosInfo:
            self.SetLevelSavePosInfo(self.m_LoadLevelSavePosInfo)

    
    def OnMapLoadOK(self, oHero, dMsgInfo):
        if oHero.m_PlayerID in self.m_InjectAnimaInfo:
            self.RefreshAnimaWeaponInfo(oHero.m_PlayerID)
        return True

    
    def GetWeaponStoreChangeWeapon(self, oHero, lstWeapon):
        dChangeWeapon = { }
        lstChangeWeapon = []
        if oHero.m_PlayerID in self.m_SettleWeaponInfo:
            dWeaponInfo = self.m_SettleWeaponInfo[oHero.m_PlayerID]
            for oWeapon in oHero.m_WeaponStoreCon.m_Item.values():
                if oWeapon.m_ID in dWeaponInfo:
                    iPos = dWeaponInfo[oWeapon.m_ID]
                    dChangeWeapon[iPos] = oWeapon
            
        tPos = oHero.m_WieldCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
        for iPos in tPos:
            if iPos in dChangeWeapon:
                lstChangeWeapon.append(dChangeWeapon[iPos])
                continue
            if len(lstWeapon) >= iPos:
                oWeapon = lstWeapon[iPos - 1]
                lstChangeWeapon.append(oWeapon)
        
        return lstChangeWeapon

    
    def GetInjectAnimaWeaponDropID(self, iWeapon):
        if iWeapon in self.m_InjectAnimaWeaponDropInfo:
            return self.m_InjectAnimaWeaponDropInfo[iWeapon]
        return 0

    
    def OnLevelNodeGoalOk(self, oWarMgr, dInfo):
        if dInfo['LevelType'] != LEVEL_TYPE_BOSS:
            return None
        if self.m_WaitCreateNpc:
            self.CreateWaitNpc(dInfo['Scene'])
        if dInfo['Layer'] < SETTLE_WEAPON_LAYER:
            return None
        for iHero in oWarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            oWieldCon = oHero.m_WieldCon
            lstWeapon = oWieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
            self.m_SettleWeaponInfo[oHero.m_PlayerID] = { }
            for oWeapon in lstWeapon:
                self.m_SettleWeaponInfo[oHero.m_PlayerID][oWeapon.m_ID] = oWeapon.m_Pos
            
        

    
    def CreateWaitNpc(self, iScene):
        for dNpcInfo in self.m_WaitCreateNpc:
            iNpcSID = dNpcInfo['SID']
            self.m_Game.m_ResMgr.CreateNpc(iScene, iNpcSID, dNpcInfo, dNpcInfo['LineIdx'])
        
        self.m_WaitCreateNpc = []

    
    def InitExWeaponCon(self, oHero):
        if oHero.m_WeaponStoreCon.m_LoadFlag:
            return None
        dWeaponData = oHero.Query('WeaponStore')
        WeaponstoreLog.Debug('%d weaponstoreinfo: %s' % (oHero.m_PlayerID, dWeaponData))
        oHero.m_WeaponStoreCon.LoadEquip(dWeaponData, bInit = True)
        self.SetUnWarWeapon(oHero.m_WeaponStoreCon)
        for oWeapon in oHero.m_WeaponStoreCon.m_Item.values():
            oWeapon.Set('UnWarWeapon', 1)
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            oInscriptionCom.m_ExtraInscriptionTimes = DEFAULT_ADDINSCRIPTION_TIMES
            oWeapon.GS2CItemPropChange('AddInscriptionTimes')
        

    
    def SetUnWarWeapon(self, oCon):
        for oEquip in oCon.m_Item.values():
            self.m_UnWarWeapon.append(oEquip.m_ID)
        

    
    def SetInitWeapon(self, iPlayerID, oCon):
        if iPlayerID in self.m_InitWeaponInfo:
            return None
        self.m_InitWeaponInfo[iPlayerID] = []
        for oEquip in oCon.m_Item.values():
            oEquip.Set('HistoryInjectAnimaWeapon', iPlayerID)
            self.m_InitWeaponInfo[iPlayerID].append(oEquip.m_ID)
        

    
    def GetExchangeWeaponInfo(self):
        lstWeapon = []
        for iWeapon in self.m_ExchangeWeaponInfo:
            if iWeapon in self.m_UnWarWeapon:
                continue
            lstWeapon.append(iWeapon)
        
        return lstWeapon

    
    def DealWeaponStoreInfo(self, oWeapon, iOwner, iDrop):
        iInjectOwner = oWeapon.Query('InjectOwner', 0)
        oOwner = self.m_WarMgr.GetHeroByPlayer(iInjectOwner)
        if iInjectOwner and oOwner and oOwner.m_ID == iOwner:
            if oWeapon.m_ID in self.m_InjectAnimaInfo.get(iInjectOwner, { }):
                dInjectAnimaInfo = self.m_InjectAnimaInfo[iInjectOwner]
                iSavePos = dInjectAnimaInfo[oWeapon.m_ID]
                self.InjectSave(oOwner, oOwner.m_WieldCon, iSavePos, oWeapon)
                self.SaveInjectAnimaWeaponCache(iInjectOwner, oWeapon)
                self.m_InjectAnimaWeaponDropInfo[oWeapon.m_ID] = iDrop
            else:
                oWeapon.Set('InjectOwner', 0)
        else:
            (iPlayer, iPos) = oWeapon.Query('WeaponStoreSourcePos', (0, -1))
            if iPlayer and iPos != -1:
                oHero = self.m_WarMgr.GetHeroByPlayer(iPlayer)
                if not oHero:
                    return None
                dSaveData = oHero.m_WeaponStoreCon.GetWeaponSaveInfo([
                    iPos])
                oHero.m_WeaponStoreCon.SaveWeaponToPlayerInfo(dSaveData)
                if iPos in oHero.m_WeaponStoreCon.m_LevelSavePos:
                    oHero.m_WeaponStoreCon.m_LevelSavePos.remove(iPos)
        oWeapon.Set('WeaponStoreSourcePos', (0, -1))

    
    def InjectSave(self, oHero, oContainer, iSavePos, oWeapon):
        dSaveData = oContainer.GetWeaponItemSaveInfo(oWeapon)
        oWeapon.Set('LastInjectSaveData', dSaveData)
        oHero.m_WeaponStoreCon.SaveWeaponToPlayerInfo({
            iSavePos: dSaveData })

    
    def SaveInjectAnimaWeaponCache(self, iPlayerID, oWeapon):
        dInfo = cl_netattr.MakeItemAddPacket(oWeapon)
        self.m_InjectAnimaWeaponCache[oWeapon.m_ID] = dInfo
        self.RefreshAnimaWeaponInfo(iPlayerID)

    
    def ClearInjectAnimaWeaponCache(self, iPlayerID, iWeapon):
        if iWeapon not in self.m_InjectAnimaWeaponCache:
            return None
        self.m_InjectAnimaWeaponCache.pop(iWeapon)
        self.RefreshAnimaWeaponInfo(iPlayerID)

    
    def OnCreateNpc(self, oLevelCtrl, dInfo):
        oLevelNode = dInfo['LevelNode']
        if oLevelNode.m_LevelType == LEVEL_TYPE_HIDE and oLevelNode.m_LayerNum in self.m_RefreshNpcLayer:
            dWarData = oLevelCtrl.m_LevelCtrlConf
            dLayerData = dWarData[oLevelNode.m_LayerNum]
            iMaxLevel = dLayerData['CtrlSize']
            if oLevelNode.m_LevelNum == iMaxLevel:
                dInfo['NPC'] = self.m_ReplaceNpc
            elif oLevelNode.m_LevelType == LEVEL_TYPE_BOSS and 'NPCInfo' in dInfo:
                clsNpcData = self.m_Game.m_WarData.GetNpcData(dInfo['NPC'])
                if clsNpcData.m_FightType == NWARRIOR_NPC_WEAPONSTORE:
                    dInfo['DelayCreate'] = 1
                    dWaitNpcInfo = dInfo['NPCInfo']
                    dWaitNpcInfo['LineIdx'] = dInfo['LineIdx']
                    self.m_WaitCreateNpc.append(dWaitNpcInfo)

    
    def OnChooseCnt(self, oLevelCtrl, dInfo):
        iCurLayerNum = dInfo['Layer']
        if iCurLayerNum not in self.m_RefreshNpcLayer:
            return None
        if dInfo['Type'] != LAYER_CHOOSE_HIDE:
            return None
        dChooseData = dInfo['ChooseData']
        dChooseData['Expect'] -= NPC_HIDELEVEL_NUM
        iMaxLevel = oLevelCtrl.m_LevelCtrlConf[iCurLayerNum]['CtrlSize']
        dChooseData['LevelBaseCnt'] = {
            iMaxLevel: NPC_HIDELEVEL_NUM }

    
    def InitFilterHideLevel(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        tFilterLevel = oLevelCtrl.m_FilterHideLevel
        oLevelCtrl.m_FilterHideLevel = tuple(set(tFilterLevel) | set(self.m_FilterHideLevel))

    
    def GetUnAnimaPos(self, pid, lstPos):
        dInjectAnimaInfo = self.m_InjectAnimaInfo[pid] if pid in self.m_InjectAnimaInfo else { }
        lstUnAnimaPos = []
        for iPos in lstPos:
            if iPos in dInjectAnimaInfo.values():
                continue
            lstUnAnimaPos.append(iPos)
        
        return lstUnAnimaPos

    
    def GetHideLevelByLimitType(self, oLevelCtrl, dWeight):
        dWarData = oLevelCtrl.m_LevelCtrlConf
        dLayerData = dWarData[oLevelCtrl.m_LayerNum]
        iMaxLevel = dLayerData['CtrlSize']
        if oLevelCtrl.m_LevelNum != iMaxLevel or oLevelCtrl.m_LayerNum not in self.m_RefreshNpcLayer:
            return dWeight
        dNewWeight = { }
        for (iLevel, iType, iLabel), iWeight in dWeight.items():
            if iType not in self.m_LimitHideLevelType:
                dNewWeight[(iLevel, iType, iLabel)] = iWeight
        
        return dNewWeight

    
    def GetInjectWeaponInfo(self, pid):
        if pid not in self.m_InjectAnimaInfo:
            return { }
        dInjectAnimaInfo = self.m_InjectAnimaInfo[pid]
        oHero = self.m_WarMgr.GetHeroByPlayer(pid)
        dSaveInfo = { }
        for iWeapon, iPos in dInjectAnimaInfo.items():
            oContainer = self.GetContainerByWeaponID(oHero, iWeapon)
            if not oContainer:
                continue
            oWeapon = oContainer.GetItemByID(iWeapon)
            dWeaponData = oContainer.GetWeaponItemSaveInfo(oWeapon)
            dSaveInfo[iPos] = dWeaponData
        
        return dSaveInfo

    
    def GetValidInjectPos(self, oHero):
        lstEmptyPos = oHero.m_WeaponStoreCon.GetEmptyPos()
        lstChoosePos = []
        dInjectAnimaInfo = self.m_InjectAnimaInfo[oHero.m_PlayerID] if oHero.m_PlayerID in self.m_InjectAnimaInfo else { }
        for iPos in lstEmptyPos:
            if iPos in dInjectAnimaInfo.values():
                continue
            lstChoosePos.append(iPos)
        
        return lstChoosePos

    
    def RefreshAnimaWeaponInfo(self, pid):
        lstWeaponAnimaInfo = []
        for iWeapon, iPos in self.m_InjectAnimaInfo[pid].items():
            if iWeapon in self.m_InjectAnimaWeaponCache:
                dWeaponCache = self.m_InjectAnimaWeaponCache[iWeapon]
            else:
                dWeaponCache = {
                    'Attr': [] }
            lstWeaponAnimaInfo.append((iWeapon, iPos, dWeaponCache))
        
        GS2CWeaponAnimaInfo(pid, lstWeaponAnimaInfo)

    
    def GetInjectAnimaWeaponNoInStoreCon(self, oHero):
        iPlayerID = oHero.m_PlayerID
        dInjectAnimaInfo = self.m_InjectAnimaInfo[iPlayerID] if iPlayerID in self.m_InjectAnimaInfo else []
        lstResult = []
        for iWeapon in dInjectAnimaInfo:
            if iWeapon in oHero.m_WieldCon.m_ItemID:
                oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
                lstResult.append(oWeapon)
                continue
            if iWeapon in oHero.m_ExWeaponCon.m_ItemID:
                oWeapon = oHero.m_ExWeaponCon.GetItemByID(iWeapon)
                lstResult.append(oWeapon)
        
        return lstResult

    
    def GetNewWeaponFromWeaponStore(self, oHero, bNeedInject = False):
        iPlayerID = oHero.m_PlayerID
        oWeaponStoreCon = oHero.m_WeaponStoreCon
        lstNewWeapon = []
        lstInitWeapon = self.m_InitWeaponInfo[iPlayerID]
        for oWeapon in oWeaponStoreCon.GetAllItem():
            if not oWeapon:
                continue
            if oWeapon.m_ID not in lstInitWeapon:
                lstNewWeapon.append(oWeapon)
        
        if not bNeedInject:
            return lstNewWeapon
        lstWeaponNoInStore = self.GetInjectAnimaWeaponNoInStoreCon(oHero)
        for oWeapon in lstWeaponNoInStore:
            if oWeapon.m_ID not in lstInitWeapon and oWeapon not in lstNewWeapon:
                lstNewWeapon.append(oWeapon)
        
        return lstNewWeapon

    
    def GetNotOperateWeapon(self, oTarget):
        lstWeapon = []
        lstWeapon.extend(oTarget.m_WieldCon.m_Item.values())
        lstWeapon.extend(oTarget.m_ExWeaponCon.m_Item.values())
        lstResult = []
        for oWeapon in lstWeapon:
            if not self.CheckWeaponInfo(oWeapon, oTarget.m_PlayerID, 'notoperate'):
                lstResult.append(oWeapon.m_ID)
        
        return lstResult

    
    def CheckWeaponInfo(self, oWeapon, iPlayerID, sReason):
        if not oWeapon:
            return False
        iInjectOwner = oWeapon.Query('InjectOwner', 0)
        if oWeapon.m_ID not in self.m_InjectAnimaInfo.get(iInjectOwner, []):
            iInjectOwner = 0
            oWeapon.Set('InjectOwner', iInjectOwner)
        if iInjectOwner not in (0, iPlayerID):
            WeaponstoreLog.Debug('%d %d %d injectanmia ownererr %d %s' % (iPlayerID, oWeapon.m_ID, oWeapon.m_SID, iInjectOwner, sReason))
            return False
        return True



def GetComponentClass(oMgrManager):
    return CWeaponStoreElement

