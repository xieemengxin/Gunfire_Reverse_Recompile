# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/deviceelement.pyc
# RelativePath: clientlogic/cl_warmgr/deviceelement.pyc
# Source Generated with Decompyle++
# File: deviceelement.pyc (Python 3.6)

from cl_only import ShufferList, ChooseKey, Functor, Time2Frame
from cl_commondecorator import ChooseRewardEnd
from cl_object.logging import DeviceLog
from cl_warmgr.mobject import CSeasonElement
from cl_warmgr.device import devicechallengemgr
from cl_cscommondef import QUALITY_TYPE_HIGH, QUALITY_TYPE_NORMAL, QUALITY_TYPE_LOW
from cl_commondefines import LEVEL_TYPE_BOSS, WARRIOR_BOSS, NPC_CB_VALUE, NWARRIOR_DROP_DEVICECOMP, NWARRIOR_DROP_RELIC, VIRTUAL_ITEM_DROP, VIRTUAL_ITEM_DEVICECOMP, FAKEMG_RELICTALENT, NWARRIOR_NPC_PASSBOX, CHALLENGE_BOXMONSTER, CHALLENGE_EXTRAELITE, WARRIOR_HERO, WARRIOR_MONSTER, NWARRIOR_DROP_TRIGGER, DROP_REASON_NPCREWARD, LEVEL_TYPE_FIGHT, DEVICECOMP_TYPE_HERO
from cl_warmgr.bigdataanalyse import CDeviceAnalyseCom
from cl_wardata.compreward import GetCompRewardConfig
import cl_msgcenter
import cl_snetwar as warnet
import cl_npc.net as npcnet
import cl_reward
import cl_perform
import cl_notify
SUPPLEMENT_PERFROM = 1809

class CDeviceElement(CSeasonElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'DeviceElement'
        self.m_WarMgr = oGame.m_WarMgr
        dConfig = self.m_Data.m_Config
        self.m_CurRewardConfig = { }
        self.m_EnableRound = dConfig.get('EnableRound', [
            3])
        self.m_DeviceChallengeMgr = devicechallengemgr.NewDeviceChallengeMgr(self, oData)
        self.m_AddExtComponentPosLayer = dConfig.get('AddExtComponentPosLayer', [
            1,
            2,
            3])
        self.m_ChooseDevice = dConfig.get('ChooseDevice', [])
        self.m_MaxComponentPos = dConfig.get('MaxCompPos', 3)
        self.m_Layer2RewardConfigSID = dConfig.get('RewardConfig', {
            1: 1001 })
        self.m_PassBoxRewardDelay = dConfig.get('PassBoxRewardDelay', 150)
        self.m_BossForceDropComp = dConfig.get('BossForceDropComp', { })
        self.m_MinDropHeroExclusiveLayer = dConfig.get('MinDropHeroExclusiveLayer', 0)
        self.m_ExcludeLevelChosenCompNum = dConfig.get('ExcludeLevelChosenCompNum', 0)
        self.m_Enable = 0
        self.m_PlayerChooseInfo = { }
        self.m_RecycleRelicMap = {
            QUALITY_TYPE_HIGH: 'RecycleHighRelic',
            QUALITY_TYPE_NORMAL: 'RecycleNormalRelic',
            QUALITY_TYPE_LOW: 'RecycleLowRelic' }

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        if oWarMgr.m_Round not in self.m_EnableRound:
            return None
        self.m_DeviceChallengeMgr.Init()
        self.m_Enable = 1
        if self.m_ChooseDevice:
            oGame = self.m_Game
            sFlag = self.m_CallFlag
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, sFlag)
            cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, sFlag)
            cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, self.OnLevelNodeFinishBefore, sFlag)
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, self.OnRoomChallengeCreateDemon, sFlag)
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, sFlag)
            oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_RECYCLEDROP, self.OnRecycleDrop, sFlag)
            oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, sFlag)
            oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, sFlag)
            oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DEVICE_INIT, self.OnAddDevice, sFlag)

    
    def InitAfter(self):
        if not self.m_Enable:
            return None
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oBigdataMgr = oWarMgr.GetComponent('BigDataAnalyseMgr')
        if oBigdataMgr:
            oAnalyseCom = CDeviceAnalyseCom(oGame)
            oBigdataMgr.SetCom('Device', oAnalyseCom)

    
    def Release(self):
        self.m_DeviceChallengeMgr.Release()
        self.m_Enable = 0
        self.DoneAttention()
        self.m_WarMgr = None
        super().Release()

    
    def CheckEnable(self):
        return self.m_Enable

    
    def GetDeviceSaveInfo(self):
        dInfo = { }
        oGame = self.m_Game
        for iHero in self.m_WarMgr.GetRoomHero(iCalAI = 0):
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dInfo[oHero.m_PlayerID] = oHero.m_DeviceMgr.Save()
        
        return dInfo

    
    def DoneAttention(self):
        if not self.m_Enable:
            return None
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        sFlag = self.m_CallFlag
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, sFlag)
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, sFlag)
        for iHero in oWarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, sFlag)
        
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, sFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, sFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_RECYCLEDROP, sFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, sFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DIE, sFlag)
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_DEVICE_INIT, sFlag)

    
    def OnAddPlayer(self, oListener, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['oCtrlHero']
        dConfig = {
            'MaxComponentPos': self.m_MaxComponentPos,
            'AddExtComponentPosLayer': self.m_AddExtComponentPosLayer }
        oHero.m_DeviceMgr.Enable(dConfig)
        oHero.m_DevicePerformCon.InitExcludeLevelChosenNum(self.m_ExcludeLevelChosenCompNum)
        if not oHero.GetDeviceSID():
            cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.AutoChooseDevice, self.m_CallFlag)
            oHero.AddMapLoadOKCbFun(self.m_CallFlag, self.SendChooseDevice, iPriority = 1, iOnce = 1)
        cl_msgcenter.AddAttentionFunc(self, oHero.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnHeroEnterScene, self.m_CallFlag)

    
    def SendChooseDevice(self, oHero, dMsgInfo):
        if oHero.GetDeviceSID():
            return None
        warnet.GS2CChooseDevice(oHero, self.m_ChooseDevice)
        iMenuIdx = npcnet.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, self.PlayerChooseDevice)
        oHero.Set('DeviceUIIdx', iMenuIdx)

    
    def PlayerChooseDevice(self, oHero, iAnswer):
        return self._PlayerChooseDevice(oHero, iAnswer)

    PlayerChooseDevice = ChooseRewardEnd(PlayerChooseDevice)
    
    def AutoChooseDevice(self, oListener, oWarMgr, dMsgInfo):
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_CallFlag)
        for iPlayerID in oWarMgr.GetAllPlayer():
            oHero = oWarMgr.GetHeroByPlayer(iPlayerID)
            if oHero and not oHero.GetDeviceSID():
                oHero.RemoveMapLoadOKCbFun(self.m_CallFlag)
                npcnet.DelNpcUICallBackFunction(oHero, oHero.Query('DeviceUIIdx', 0), NPC_CB_VALUE)
                self._PlayerChooseDevice(oHero, iAnswer = 0)
        

    
    def _PlayerChooseDevice(self, oHero, iAnswer):
        iPlayerID = oHero.m_PlayerID
        if oHero.GetDeviceSID():
            return 1
        oGame = self.m_Game
        if iAnswer not in self.m_ChooseDevice:
            if iAnswer:
                DeviceLog.Alert('%d %d choose device %s err %s' % (oGame.m_ID, iPlayerID, iAnswer, self.m_ChooseDevice))
            iAnswer = ShufferList(oGame, self.m_ChooseDevice)[0]
            sReason = 'AutoChoose'
        else:
            sReason = 'PlayerChoose'
        DeviceLog.Info('%d %d choose device %d' % (oGame.m_ID, iPlayerID, iAnswer))
        oHero.m_DeviceMgr.AddDevice(iAnswer, sReason)
        return 1

    
    def GetRewardInfoByType(self, sType):
        if sType not in self.m_CurRewardConfig:
            return { }
        return self.m_CurRewardConfig[sType]

    
    def OnLevelNodeInit(self, oListener, oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_CallFlag)

    
    def OnLevelNodeFinishBefore(self, oListener, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        dPlayer = { }
        dRecycleDrop = { }
        for oNode in oLevelCtrl.m_LevelNodeLib.values():
            oScene = oGame.m_SceneMgr.GetScene(oNode.m_Scene)
            if not oScene:
                continue
            lstDrop = oScene.GetObjectsByType('Drop')
            for iDrop in lstDrop:
                oDrop = oGame.GetObject(iDrop)
                if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_DEVICECOMP or not (oDrop.m_Source):
                    continue
                iSource = oDrop.m_Source
                oHero = oWarMgr.GetRoomHeroByPlayer(iSource)
                if not oHero:
                    continue
                if oHero.m_DevicePerformCon.ValidComponentMaxLevel(oDrop.m_DropInfo[0]):
                    dRecycleDrop[oDrop.m_ID] = oDrop
                    continue
                if oDrop.Pick(oHero.m_ID) and iSource not in dPlayer:
                    dPlayer[iSource] = 1
            
        
        if oWarMgr.IsEndless():
            for oDrop in dRecycleDrop.values():
                oHero = oWarMgr.GetRoomHeroByPlayer(oDrop.m_Source)
                oDrop.Pick(oHero.m_ID)
            
        if dPlayer:
            cl_notify.SendCommonNotify(self.m_Game, dPlayer, 9498, { })

    
    def OnCreateMonster(self, oListener, oWarMgr, dMsgInfo):
        iMonsterID = dMsgInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonsterID)
        if not oMonster or oMonster.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            return None
        if oMonster.m_Owner:
            return None
        cl_msgcenter.AddAttentionFunc(self, iMonsterID, cl_msgcenter.MSG_WAR_DIE, self.OnBossDie, self.m_CallFlag)

    
    def OnBossDie(self, oListener, oMonster, dMsgInfo):
        iMonster = oMonster.m_ID
        cl_msgcenter.DoneAttention(self, iMonster, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        oGame = self.m_Game
        vBasePos = cl_reward.GetDropBasePos(oMonster)
        iScene = oMonster.m_Scene
        vPos = cl_reward.GetDropFixPos(oGame, oMonster, iScene, vBasePos, iMonster)
        dBossDropInfo = self.GetRewardInfoByType('Boss')
        if not dBossDropInfo:
            return None
        lstHero = oGame.m_WarMgr.GetRoomHero(iCalAI = 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iCurLayer = oLevelCtrl.m_LayerNum
        dForceCompConfig = { }
        dBossForceDropComp = self.m_BossForceDropComp
        lstLayer = dBossForceDropComp.get('Layer', [])
        if iCurLayer in lstLayer:
            dForceCompConfig = dBossForceDropComp.get('Config', { })
        dBaseForceNum = dBossDropInfo['ForceNum']
        if iCurLayer == self.m_MinDropHeroExclusiveLayer:
            dBaseForceNum = dict(dBossDropInfo['ForceNum'])
            dBaseForceNum[DEVICECOMP_TYPE_HERO] = 1
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstReward = []
            iDeviceSID = oHero.GetDeviceSID()
            iTotalNum = dBossDropInfo['Num']
            dForceNum = dict(dBaseForceNum)
            dChosen = { }
            oDevicePerformCon = oHero.m_DevicePerformCon
            if iDeviceSID in dForceCompConfig:
                lstExclusiveComp = dForceCompConfig[iDeviceSID]
                dChooseComp = { }
                for iSID in lstExclusiveComp:
                    if not oDevicePerformCon.GetComponent(iSID):
                        dChooseComp[iSID] = 1
                
                if dChooseComp:
                    iSID = ChooseKey(oGame, dChooseComp)
                    clsComponent = cl_perform.GetPerformModule(iSID)
                    if not clsComponent:
                        DeviceLog.Alert('%d %d boss reward %d err %s' % (oGame.m_ID, oHero.m_PlayerID, iSID, lstExclusiveComp))
                    else:
                        iType = clsComponent.m_Type
                        if iType in dForceNum:
                            dForceNum[iType] -= 1
                        iTotalNum -= 1
                        dChosen[iSID] = 1
                        oDevicePerformCon.AddAcquiredComp(iSID)
                        oDevicePerformCon.AddLevelChosenInfo([
                            iSID])
                        dReward = {
                            'item': VIRTUAL_ITEM_DROP,
                            'info': {
                                'DropType': NWARRIOR_DROP_DEVICECOMP,
                                'DropInfo': [
                                    iSID],
                                'DropPos': vPos } }
                        lstReward.append(dReward)
            dRewardConfig = {
                'Weight': dBossDropInfo['Weight'],
                'ForceNum': dForceNum,
                'Num': iTotalNum }
            for iSID in oDevicePerformCon.ChooseComponent(dRewardConfig, dChosen):
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_DEVICECOMP,
                        'DropInfo': [
                            iSID],
                        'DropPos': vPos } }
                lstReward.append(dReward)
            
            cl_reward.RewardItem(oGame, oHero, lstReward, 'BossDrop', {
                'Abandoner': iMonster,
                'Player': iHero })
        

    
    def OnRoomChallengeCreateDemon(self, oListener, oLevelCtrl, dMsgInfo):
        dMGInfo = dMsgInfo['MGInfo']
        if not dMGInfo:
            return None
        oGame = self.m_Game
        dRewardConfig = self.GetRewardInfoByType('RoomChallenge')
        iChallengeType = dMsgInfo['ChallengeType']
        iRemoveRelic = 0 if iChallengeType in (CHALLENGE_BOXMONSTER, CHALLENGE_EXTRAELITE) else 1
        for iHero, dInfo in dMGInfo.items():
            oHero = oGame.GetObject(iHero)
            if not oHero or not (oHero.m_FightType & WARRIOR_HERO):
                continue
            bDropDeviceComp = False
            if iRemoveRelic:
                for _, lstRewardInfo, _ in dInfo.values():
                    for dReward in lstRewardInfo[:]:
                        iRewardItem = dReward['item'] if 'item' in dReward else 0
                        if iRewardItem != VIRTUAL_ITEM_DROP:
                            continue
                        iDropType = dReward['info']['DropType']
                        if iDropType == NWARRIOR_DROP_RELIC:
                            lstRewardInfo.remove(dReward)
                            bDropDeviceComp = True
                    
                
            if not bDropDeviceComp:
                if not iRemoveRelic:
                    lstReward = []
                    vPos = oHero.GetPos()
                    for iSID in oHero.m_DevicePerformCon.ChooseComponent(dRewardConfig):
                        dReward = {
                            'item': VIRTUAL_ITEM_DROP,
                            'info': {
                                'DropType': NWARRIOR_DROP_DEVICECOMP,
                                'DropInfo': [
                                    iSID],
                                'DropPos': vPos } }
                        lstReward.append(dReward)
                    
            dInfo[FAKEMG_RELICTALENT] = (0, lstReward, {
                'Player': oHero.m_ID })
        

    
    def OnLayerStart(self, oListener, oLevelCtrl, dMsgInfo):
        iCurLayer = dMsgInfo['Layer']
        iCurConfig = 0
        for iLayer, iConfig in self.m_Layer2RewardConfigSID.items():
            if iCurLayer < iLayer:
                break
            iCurConfig = iConfig
        
        self.m_CurRewardConfig = GetCompRewardConfig(iCurConfig)

    
    def OnRecycleDrop(self, oListener, oHero, dMsgInfo):
        iRecycleDropType = dMsgInfo['RecycleDropType']
        if iRecycleDropType != NWARRIOR_DROP_RELIC:
            return None
        iRelicSID = dMsgInfo['Relic']
        clsRelic = cl_perform.GetPerformModule(iRelicSID)
        iQuality = clsRelic.m_Quality
        if iQuality not in self.m_RecycleRelicMap:
            return None
        sType = self.m_RecycleRelicMap[iQuality]
        dRewardConfig = self.GetRewardInfoByType(sType)
        oPerformCon = oHero.m_DevicePerformCon
        oGame = self.m_Game
        lstComponent = oPerformCon.ChooseComponent(dRewardConfig)
        if not lstComponent:
            return None
        iRewardSID = lstComponent[0]
        iDrop = 1
        sReason = 'RecycleRelic'
        if 'RecycleDrop' not in dMsgInfo or 'AutoRecycle' in dMsgInfo:
            if oHero.m_DevicePerformCon.ValidPickComponent(iRewardSID, sReason):
                iDrop = 0
            elif 'AutoRecycle' in dMsgInfo:
                lstDelayDropComp = oHero.SetDefaultSavedData('DelayDropComp', [])
                lstDelayDropComp.append(iRewardSID)
                return None
        if iDrop:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_DEVICECOMP,
                    'DropInfo': [
                        iRewardSID],
                    'DropPos': oHero.GetPos() } }
        else:
            dReward = {
                'item': VIRTUAL_ITEM_DEVICECOMP,
                'info': {
                    'SID': iRewardSID } }
        cl_reward.RewardItem(oGame, oHero, [
            dReward], sReason, {
            'Player': oHero.m_ID })

    
    def OnHeroEnterScene(self, oListener, oHero, dMsgInfo):
        lstComponent = oHero.QuerySavedData('DelayDropComp', [])
        if not lstComponent:
            return None
        oHero.DelSavedData('DelayDropComp')
        lstReward = []
        vPos = oHero.GetPos()
        for iSID in lstComponent:
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_DEVICECOMP,
                    'DropInfo': [
                        iSID],
                    'DropPos': vPos } }
            lstReward.append(dReward)
        
        cl_reward.RewardItem(self.m_Game, oHero, lstReward, 'DelayDrop', {
            'Player': oHero.m_ID })

    
    def OnNpcInteract(self, oListener, oHero, dMsgInfo):
        if 'NpcType' not in dMsgInfo:
            return None
        if dMsgInfo['NpcType'] != NWARRIOR_NPC_PASSBOX:
            return None
        oGame = self.m_Game
        iNpc = dMsgInfo['NPC']
        oNpc = oGame.GetObject(iNpc)
        if not oNpc:
            return None
        tLineIdx = oNpc.m_LineIdx
        if not tLineIdx:
            return None
        iLevel = tLineIdx[0]
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode or oLevelNode.m_LevelType not in (LEVEL_TYPE_FIGHT,):
            return None
        vPos = oNpc.GetPos()
        iScene = oNpc.m_Scene
        iDelay = self.m_PassBoxRewardDelay
        if iDelay:
            oNpc.Call_Out(Functor(self.RewardCompByPassBox, iNpc, iScene, vPos), Time2Frame(iDelay), 'PassBoxReward')
        else:
            self.RewardCompByPassBox(iNpc, iScene, vPos)

    
    def RewardCompByPassBox(self, iNpc, iScene, vPos):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        dRewardConfig = self.GetRewardInfoByType('PassBox')
        for iHero in self.m_WarMgr.GetRoomHero(iCalAI = 0):
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstReward = []
            for iSID in oHero.m_DevicePerformCon.ChooseComponent(dRewardConfig):
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_DEVICECOMP,
                        'DropInfo': [
                            iSID],
                        'DropPos': vPos } }
                lstReward.append(dReward)
            
            cl_reward.RewardItem(oGame, oHero, lstReward, 'PassBox', {
                'Player': iHero,
                'Abandoner': iNpc,
                'DropReason': DROP_REASON_NPCREWARD,
                'Scene': iScene })
        

    
    def OnDie(self, oListener, oTarget, dMsgInfo):
        if not oTarget.m_FightType & WARRIOR_MONSTER:
            return None
        oGame = self.m_Game
        clsMonsterData = oGame.m_WarData.GetMonsterData(oTarget.m_SID)
        if not clsMonsterData:
            return None
        dDeviceEnergyPoint = clsMonsterData.m_DeviceEnergyPoint
        if not dDeviceEnergyPoint:
            return None
        iTarget = oTarget.m_ID
        lstHero = self.m_WarMgr.GetLiveHero()
        vPos = cl_reward.GetDropBasePos(oTarget)
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstReward = self.GetDeviceEnergyPointReward(dDeviceEnergyPoint, vPos)
            if not lstReward:
                continue
            cl_reward.RewardItem(oGame, oHero, lstReward, 'MonsterDrop', {
                'Abandoner': iTarget,
                'Player': oHero.m_ID })
        

    
    def GetDeviceEnergyPointReward(self, dWeight, vPos):
        lstReward = []
        iNum = ChooseKey(self.m_Game, dWeight)
        for _ in range(iNum):
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_TRIGGER,
                    'DropInfo': [
                        {
                            SUPPLEMENT_PERFROM: 1 }],
                    'DropPos': vPos } }
            lstReward.append(dReward)
        
        return lstReward

    
    def OnAddDevice(self, oListener, oHero, dMsgInfo):
        iDeviceSID = oHero.GetDeviceSID()
        self.m_PlayerChooseInfo[oHero.m_PlayerID] = iDeviceSID



def GetComponentClass(oWarManager):
    return CDeviceElement

