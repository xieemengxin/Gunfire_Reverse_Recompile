# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/mainlevelnode.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/mainlevelnode.pyc
# Source Generated with Decompyle++
# File: mainlevelnode.pyc (Python 3.6)

from cl_cscommondef.cs_fight import LEVEL_TYPE_HALL, GAMETYPE_CONVOY, GAMETYPE_ASSASSINATE, LEVEL_TYPE_BOSS, WARRIOR_MONSTER, GAMETYPE_DEFEND, GAMETYPE_LIMITDEFEND, LEVEL_TYPE_FIGHT, LAYER_CHOOSE_GSCASHSHOP, LAYER_CHOOSE_EVENTNPC, LAYER_CHOOSE_CRAFTSMAN, LAYER_CHOOSE_SHOP, LEVEL_STATUS_WAIT, GAMETYPE_NONE, LAYER_CHOOSE_TASKNPC, LAYER_CHOOSE_PETSHOP, LAYER_CHOOSE_REGROUPRELIC, LAYER_CHOOSE_RELICLOTTERY, LAYER_CHOOSE_WANDSHOP, LAYER_CHOOSE_DICESHOP, LAYER_CHOOSE_S7SHOP, LAYER_CHOOSE_S8SHOP
from cl_cscommondef.cs_playmode import PLAYMODE_DAYLY_TRIAL, GetWarNo, PLAYMODE_ROGUELIKE, PLAYMODE_SURVIVOR, PLAYMODE_NEWSURVIVOR
from cl_cscommondef import SETTLE_FINISHWAR, MG_SOURCE_KILLMONSTEREXT, SETTLE_LOSEWAR
from cl_commondefines import PASS_BOSS_LEVEL_WUDI_PF
from cl_only import Functor, PY_FLAG_DEAD, ChooseKey, DeepCopy, SendAlert
from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON
import cl_msgcenter
import cl_item
import cl_perform
import cl_random
import cl_formula
import cl_object.reason
import cl_reward
import cllib.lib_flag
import cl_betree
from . import baselevelnode
from . import levelspawnaction
LevelLog = baselevelnode.LevelLog
DEFAULT_WEAPON_WEIGHT = 10
WEIGHT_ALERT_PLAYMODE = {
    PLAYMODE_ROGUELIKE,
    PLAYMODE_DAYLY_TRIAL,
    PLAYMODE_SURVIVOR,
    PLAYMODE_NEWSURVIVOR}
LAST_EVENT_NPC = ('petshop', 'regrouprelic', 'reliclottery', 'wandshop', 'diceshop', 's7shop', 's8shop')
PUT_NPC = {
    'PutPetShop': 'petshop',
    'PutRegroupRelicNpc': 'regrouprelic',
    'PutRelicLotteryNpc': 'reliclottery',
    'PutWandNpc': 'wandshop',
    'PutDiceNpc': 'diceshop',
    'PutS7ShopNpc': 's7shop',
    'PutS8ShopNpc': 's8shop' }

class CMainLevelNode(baselevelnode.CBaseLevelNode):
    m_LevelType = LEVEL_TYPE_FIGHT
    m_GameType = GAMETYPE_NONE
    m_TargetName = ''
    
    def __init__(self, oCtrlMgr, iLevel):
        super(CMainLevelNode, self).__init__(oCtrlMgr, iLevel)
        self.m_RewardNpcPos = { }
        self.m_LastMainLevelInfo = { }
        self.m_LevelAnalysisParam = {
            'shop': LAYER_CHOOSE_SHOP,
            'craftsman': LAYER_CHOOSE_CRAFTSMAN,
            'event': LAYER_CHOOSE_EVENTNPC,
            'gscashshop': LAYER_CHOOSE_GSCASHSHOP,
            'tasknpc': LAYER_CHOOSE_TASKNPC,
            'petshop': LAYER_CHOOSE_PETSHOP,
            'regrouprelic': LAYER_CHOOSE_REGROUPRELIC,
            'reliclottery': LAYER_CHOOSE_RELICLOTTERY,
            'wandshop': LAYER_CHOOSE_WANDSHOP,
            'diceshop': LAYER_CHOOSE_DICESHOP,
            's7shop': LAYER_CHOOSE_S7SHOP,
            's8shop': LAYER_CHOOSE_S8SHOP }

    
    def OnRelease(self):
        self.m_Game.DoneGlobalAttention(self.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE_BEFORE, 'GroupChooseDrop')
        self.m_Game.DoneGlobalAttention(self.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE_BEFORE, 'GroupChooseGoldenCup')
        if cllib.lib_flag.g_AutoDelBetree:
            cl_betree.ClearBetree()

    
    def OnLevelInit(self):
        self.CreateHideTransfer()
        self.SetRandomChoose()
        self.ChooseMonsterDrop()
        self.SetPlayerInitCash()
        oWarMgr = self.m_Game.m_WarMgr
        self.ChooseNpc('shop')
        for sPutKey, sNpcType in PUT_NPC.items():
            if oWarMgr.Query(sPutKey, 0):
                self.ChooseNpc(sNpcType)
        
        self.ChooseNpc('event')
        self.ChooseNpc('craftsman')
        if oWarMgr.m_PlayMode == PLAYMODE_ROGUELIKE and oWarMgr.IsCycleWar():
            self.ChooseNpc('gscashshop')
        if oWarMgr.GetComponent('TaskElement'):
            self.ChooseNpc('tasknpc')
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        oScene.m_ScenePreLoad.InitPreLoadData(self.m_LastMainLevelInfo.get('PreLoad', { }))

    
    def OnLevelGoal(self, dTrigger):
        levelspawnaction.SpawnPassLevelNotify(self)

    
    def OnPassLevel(self, lstPlayer, dTransfer):
        oCtrlMgr = self.m_CtrlMgr
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        iPassAll = oCtrlMgr.CheckFinishWar()
        dData = {
            'LevelType': self.m_LevelType,
            'LevelID': self.m_Level,
            'PassAll': iPassAll,
            'FinishLevel': max(0, oCtrlMgr.m_LevelNum - 1),
            'Layer': oCtrlMgr.m_LayerNum,
            'Level': oCtrlMgr.m_LevelNum,
            'Transfer': dTransfer,
            'Scene': self.m_Scene }
        cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, oWarMgr, dData)
        cl_msgcenter.SendCoreMsg(cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, oWarMgr, dData)
        if self.IsPassLevel():
            oWarMgr.OnFinishLevel(SETTLE_FINISHWAR)
            oWarMgr.UpdateHeroLevelRecord(self.m_Level)
        else:
            oWarMgr.OnFinishLevel(SETTLE_LOSEWAR)
        if iPassAll:
            LevelLog.Info('%s players%s finishwar mapid:%d levelid:%d' % (oGame.m_ID, lstPlayer, self.m_Map, self.m_Level))
            oWarMgr.OnFinishWar()
        else:
            oCtrlMgr.NextLevel(dTransfer)

    
    def CheckAllPlayerReady(self):
        if self.m_Status != LEVEL_STATUS_WAIT:
            return False
        if not self.IsSceneLoaded():
            return False
        oGame = self.m_CtrlMgr.m_Game
        dPlayers = oGame.GetRealPlayers()
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        dReadyPlayer = oScene.GetPlayers()
        for pid in dPlayers.keys():
            if pid not in dReadyPlayer:
                return False
        
        return True

    
    def CheckLevelHidePoints(self, iArea):
        oCtrlMgr = self.m_CtrlMgr
        iLayer = oCtrlMgr.m_LayerNum
        iLevel = oCtrlMgr.m_LevelNum
        dLevelLineInfo = self.GetLevelLineInfo()
        if (oCtrlMgr.m_Game.m_WarMgr.m_SID != GetWarNo(PLAYMODE_DAYLY_TRIAL) or iLayer == 1) and iLevel == 1:
            lstLevelLine = list(dLevelLineInfo.keys())
            if lstLevelLine[0] == iArea:
                return 1
            if iLevel == 1:
                lstLevelLine = list(dLevelLineInfo.keys())
                if lstLevelLine[0] == iArea:
                    return 1
        return 0

    
    def CreateHideTransfer(self):
        oLevelConfData = self.m_CtrlMgr.m_LevelConfData
        dLevel = self.m_CtrlMgr.m_HideLevelLib
        if not dLevel:
            return None
        dObstacle = oLevelConfData.GetMapConfig(self.m_Level, 'hideob')
        if not dObstacle:
            return None
        dHideObstacle = { }
        lstHideObstacle = []
        dLevelLine = oLevelConfData.GetLevelConfig(self.m_Level, 'arealine')
        for iArea, _ in dLevelLine.items():
            if iArea not in dObstacle:
                continue
            if self.CheckLevelHidePoints(iArea):
                continue
            for dInfo in dObstacle[iArea]:
                iPrefab = dInfo['Prefab']
                tKey = (iArea, iPrefab)
                dHideObstacle[tKey] = dInfo
                lstHideObstacle.append(tKey)
            
        
        lstHideObstacle = list(set(lstHideObstacle))
        for iLevel in dLevel.keys():
            iLen = len(lstHideObstacle)
            if iLen < 1:
                break
            idx = self.m_Game.Random(iLen)
            tKey = lstHideObstacle[idx]
            dInfo = dHideObstacle[tKey]
            (iArea, iPrefab) = tKey
            tLineIdx = self.GetLineIdxByArea(iArea)
            iObstacleSID = dInfo['SID']
            oObstacle = self.m_Game.m_ResMgr.CreateBuild(self.m_Scene, iObstacleSID, dInfo, tLineIdx)
            oObstacle.Set('HideLevel', iLevel)
            lstHideObstacle.remove(tKey)
            lstMutex = dInfo['Other'].get('MutexIdx', [])
            for lstIndex in lstMutex:
                tIndex = tuple(lstIndex)
                if tIndex not in lstHideObstacle:
                    continue
                lstHideObstacle.remove(tIndex)
            
        

    
    def ChooseRewardNpcPos(self, tLineIdx, iAmount):
        iLevelCnt = self.m_CtrlMgr.m_LevelNum
        iLimit = self.m_CtrlMgr.m_LayerChoose.GetMainLevelScrollCnt(iLevelCnt)
        iCnt = min(iLimit, iAmount)
        return self.GetLineConfigPos(tLineIdx, 'reward', iCnt)

    
    def ChooseNpc(self, sType):
        iLevelNum = self.m_CtrlMgr.m_LevelNum
        iCnt = 0
        oLevelNode = self.m_CtrlMgr.m_CurNode
        if sType not in self.m_LevelAnalysisParam:
            return None
        iType = self.m_LevelAnalysisParam[sType]
        iCnt = self.m_CtrlMgr.m_LayerChoose.GetMainLevelCnt(iType, iLevelNum)
        if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
            iCnt += self.m_CtrlMgr.m_LayerChoose.GetBossLevelCnt(iType)
        if not iCnt:
            return None
        if sType in ('craftsman', 'gscashshop', 'tasknpc'):
            lstNpcPos = self.GetSceneConfigPos('shop', iCnt)
        elif sType in LAST_EVENT_NPC:
            lstNpcPos = self.ChooseLastEventNpcPos(iCnt)
        else:
            lstNpcPos = self.GetSceneConfigPos(sType, iCnt)
        if 'DebugJudgeToLevel' in oLevelNode.m_CustomData and oLevelNode.m_CustomData['DebugJudgeToLevel'] and len(lstNpcPos) < iCnt:
            return None
        dMsgInfo = {
            'Type': sType,
            'NpcWeight': dict(self.GetRefreshNpcWeight(sType)),
            'LevelNum': iLevelNum,
            'LayerNum': self.m_CtrlMgr.m_LayerNum }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CHOOSENPC_PRE, self.m_CtrlMgr, dMsgInfo)
        dNpcWeight = dMsgInfo['NpcWeight']
        if not dNpcWeight:
            return None
        dNpcInfo = self.m_Game.m_WarData.GetNpcChooseInfo()
        iRound = self.m_Game.m_WarMgr.m_Round
        iCycle = self.m_Game.m_WarMgr.m_Cycle
        for iNpc in list(dNpcWeight):
            if not cl_reward.ValidExtraGoldenCup(self.m_Game, {
                'NPC': iNpc }):
                dNpcWeight.pop(iNpc)
                continue
            if iNpc in dNpcInfo:
                (iMinRound, iMinCycle, iMaxRound, iMaxCycle) = dNpcInfo[iNpc]
                if not iRound < iMinRound or iRound > iMaxRound:
                    if not iRound == iMinRound or iCycle < iMinCycle:
                        if iRound == iMaxRound and iCycle > iMaxCycle:
                            dNpcWeight.pop(iNpc)
                            continue
        
        if len(lstNpcPos) < iCnt:
            LevelLog.Alert('%s %s no enough %s npc pos' % (self.m_Map, self.m_Level, sType))
        lstNpcPos = DeepCopy(lstNpcPos)
        for dPos in lstNpcPos:
            iNpc = ChooseKey(self.m_Game, dNpcWeight)
            if not iNpc:
                return None
            iArea = dPos['Area']
            oLineNode = self.GetLineNodeByArea(iArea)
            if not oLineNode:
                LevelLog.Alert('%s %s node err by area %s' % (self.m_Map, self.m_Level, iArea))
                continue
            dMsgInfo = {
                'NPC': iNpc,
                'LevelNode': self,
                'NPCInfo': dPos,
                'Scene': self.m_Scene }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.m_CtrlMgr, dMsgInfo)
            if not dMsgInfo['NPC']:
                continue
            self.m_Game.m_ResMgr.CreateNpc(self.m_Scene, dMsgInfo['NPC'], dPos, oLineNode.GetLineIdx())
        

    
    def SetRandomChoose(self, iAssignHero = 0):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oRandomMgr = oGame.m_RandomMgr
        if iAssignHero:
            lstHero = [
                iAssignHero]
        else:
            lstHero = oWarMgr.GetRoomHero()
        dWeightConfig = oGame.m_WarData.GetRewardWeightConf()
        dRelicConfig = dWeightConfig['Relic'] if 'Relic' in dWeightConfig else { }
        dWeaponConfig = dWeightConfig['Equip'] if 'Equip' in dWeightConfig else {
            'Common': { } }
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            lstWeapon = oHero.Query('Illus')['Weapon']
            dHeroWeaponConfig = dWeaponConfig[oHero.m_SID] if oHero.m_SID in dWeaponConfig else { }
            dCommonWeaponConfig = dWeaponConfig['Common']
            dWeapon = { }
            for iWeapon in lstWeapon:
                clsWeapon = cl_item.GetItemCls(iWeapon)
                if not clsWeapon:
                    continue
                if clsWeapon.m_Type == EQUIP_TYPE_FUNDAMENTALWEAPON:
                    continue
                if iWeapon in dCommonWeaponConfig:
                    iWeight = cl_formula.GetFormulaResult(self, dCommonWeaponConfig[iWeapon])
                    if iWeight < 0 and oWarMgr.m_PlayMode in WEIGHT_ALERT_PLAYMODE:
                        SendAlert('err', '战场: %s 装备%s 通用奖励权重必须>=0' % (oWarMgr.m_SID, iWeapon))
                    else:
                        iWeight = DEFAULT_WEAPON_WEIGHT
                        if oWarMgr.m_PlayMode in WEIGHT_ALERT_PLAYMODE:
                            SendAlert('err', '战场: %s 装备%s 未配置通用奖励权重' % (oWarMgr.m_SID, iWeapon))
                if None in dHeroWeaponConfig:
                    iWeight += cl_formula.GetFormulaResult(self, dHeroWeaponConfig[iWeapon])
                dWeapon[iWeapon] = iWeight
            
            sWeaponKey = 'weapon%d' % iHero
            if not oRandomMgr.ValidRandom(sWeaponKey):
                oRandomMgr.InitRandom(cl_random.RANDOM_NORMAL, sWeaponKey, dWeapon)
            else:
                oRandomMgr.SetChoose(sWeaponKey, dWeapon)
            setRelic = oHero.Query('Illus')['Relic']
            dRelic = { }
            for iRelic in setRelic:
                clsRelic = cl_perform.GetPerformModule(iRelic)
                if not clsRelic:
                    continue
                if iRelic in dRelicConfig:
                    iWeight = dRelicConfig[iRelic]
                else:
                    iWeight = 1
                    if oWarMgr.m_PlayMode in WEIGHT_ALERT_PLAYMODE:
                        SendAlert('err', '战场: %s 遗物%s 未配置奖励权重' % (oWarMgr.m_SID, iRelic))
                dRelic[iRelic] = cl_formula.GetFormulaResult(self, iWeight)
            
            sRelicKey = 'relic%d' % iHero
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_LEVELINIT_INITRELICDROPPROB, oHero, dRelic)
            if not oRandomMgr.ValidRandom(sRelicKey):
                oRandomMgr.InitRandom(cl_random.RANDOM_NORMAL, sRelicKey, dRelic)
                continue
            oRandomMgr.SetChoose(sRelicKey, dRelic)
        

    
    def ChooseMonsterDrop(self):
        oGame = self.m_Game
        dLevelCtrlConf = self.m_CtrlMgr.m_LevelCtrlConf
        iLayerNum = self.m_CtrlMgr.m_LayerNum
        iLevelNum = self.m_CtrlMgr.m_LevelNum
        if iLayerNum not in dLevelCtrlConf:
            return None
        iChooseItem = dLevelCtrlConf[iLayerNum]['ItemChoose']
        dAllChooseItem = self.m_CtrlMgr.m_ChooseItem
        if iChooseItem not in dAllChooseItem:
            return None
        tLevelKey = (iLayerNum, iLevelNum)
        if tLevelKey not in dAllChooseItem[iChooseItem]:
            iBaseLayer = self.m_Game.m_WarMgr.GetBaseLayer(iLayerNum)
            tLevelKey = (iBaseLayer, iLevelNum)
            if tLevelKey not in dAllChooseItem[iChooseItem]:
                return None
        dLineCnt = self.GetAllLineMonsterCnt()
        dChoose = { }
        for tLineIdx, iCnt in dLineCnt.items():
            for idx in range(iCnt):
                dChoose[(tLineIdx, idx)] = 1
            
        
        if not dChoose:
            return None
        dChooseItem = dAllChooseItem[iChooseItem][tLevelKey]
        dSource = { }
        dSource['WeaponChoose'] = dChooseItem['WeaponChoose'] if 'WeaponChoose' in dChooseItem else { }
        dSource['GoldenCupChoose'] = dChooseItem['GoldenCupChoose'] if 'GoldenCupChoose' in dChooseItem else { }
        dSource['RelicChoose'] = dChooseItem['RelicChoose'] if 'RelicChoose' in dChooseItem else { }
        dNewChooseItem = DeepCopy(dSource)
        dMsgInfo = {
            'iLayerNum': iLayerNum,
            'iLevelNum': iLevelNum,
            'ChooseData': dNewChooseItem }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CHOOSEITEM, self.m_CtrlMgr, dMsgInfo)
        oRandomMgr = oGame.m_RandomMgr
        if 'WeaponChoose' in dNewChooseItem:
            (iExcept, iSigma, iMiniGame) = dNewChooseItem['WeaponChoose']
            iExcept = cl_formula.GetFormulaResult(self, iExcept)
            iSigma = cl_formula.GetFormulaResult(self, iSigma)
            if not oRandomMgr.ValidRandom('groupdrop'):
                oRandomMgr.InitRandom(cl_random.RANDOM_LEVEL, 'groupdrop', dChoose)
            else:
                oRandomMgr.SetChoose('groupdrop', dChoose)
            dMonsterChoose = oRandomMgr.ChooseKey('groupdrop', {
                'Expect': iExcept,
                'Sigma': iSigma,
                'Game': oGame })
            if dMonsterChoose:
                oGame.AddGlobalAttention(self.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, Functor(OnMonsterDie, { }, dMonsterChoose, iMiniGame, 'WeaponChoose'), 'GroupChooseDrop')
        if 'GoldenCupChoose' in dNewChooseItem:
            (iExcept, iSigma, iMiniGame) = dNewChooseItem['GoldenCupChoose']
            iExcept = cl_formula.GetFormulaResult(self, iExcept)
            iSigma = cl_formula.GetFormulaResult(self, iSigma)
            if not oRandomMgr.ValidRandom('groupgoldencup'):
                oRandomMgr.InitRandom(cl_random.RANDOM_LEVEL, 'groupgoldencup', dChoose)
            else:
                oRandomMgr.SetChoose('groupgoldencup', dChoose)
            dMonsterChoose = oRandomMgr.ChooseKey('groupgoldencup', {
                'Expect': iExcept,
                'Sigma': iSigma,
                'Game': oGame })
            if dMonsterChoose:
                oGame.AddGlobalAttention(self.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, Functor(OnMonsterDie, { }, dMonsterChoose, iMiniGame, 'GoldenCupChoose'), 'GroupChooseGoldenCup')
        if 'RelicChoose' in dNewChooseItem:
            (iExcept, iSigma, iMiniGame) = dNewChooseItem['RelicChoose']
            iExcept = cl_formula.GetFormulaResult(self, iExcept)
            iSigma = cl_formula.GetFormulaResult(self, iSigma)
            if not oRandomMgr.ValidRandom('grouprelic'):
                oRandomMgr.InitRandom(cl_random.RANDOM_LEVEL, 'grouprelic', dChoose)
            else:
                oRandomMgr.SetChoose('grouprelic', dChoose)
            dMonsterChoose = oRandomMgr.ChooseKey('grouprelic', {
                'Expect': iExcept,
                'Sigma': iSigma,
                'Game': oGame })
            if dMonsterChoose:
                oGame.AddGlobalAttention(self.m_CtrlMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, Functor(OnMonsterDie, { }, dMonsterChoose, iMiniGame, 'RelicChoose'), 'GroupChooseRelic')

    
    def SetLastLevelInfo(self, dLastLevelInfo):
        self.m_LastMainLevelInfo = dLastLevelInfo

    
    def GetPassToNextLevelInfo(self):
        dData = { }
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        dData['PreLoad'] = oScene.m_ScenePreLoad.GetPassPreLoadData()
        return dData

    
    def SetPlayerInitCash(self):
        oCtrlMgr = self.m_CtrlMgr
        if oCtrlMgr.m_LevelNum == 0 and oCtrlMgr.m_LayerNum == 1:
            oGame = self.m_Game
            for iHero in oGame.m_WarMgr.GetAllHero():
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                oHero.Set('InitCash', oHero.m_WarCash)
            



def OnMonsterDie(dMonsterCnt, dMonsterChoose, iMiniGame, sKey, oListener, oSender, dMsgInfo):
    if oSender.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    tLineIdx = oSender.m_LineIdx
    oLineNode = oListener.GetLineNode(tLineIdx)
    if not oLineNode:
        return None
    tBelong = oLineNode.m_MonsterCtrl.GetMonsterBelong(oSender)
    if not tBelong[0] or not tBelong[1]:
        return None
    iGroupCnt = dMonsterCnt.setdefault(tLineIdx, 0)
    dMonsterCnt[tLineIdx] = iGroupCnt + 1
    tKey = (tLineIdx, iGroupCnt)
    if tKey not in dMonsterChoose:
        return None
    iTimes = dMonsterChoose[tKey]
    dMiniGameExtInfo = {
        'UrgentDrop': 0,
        'CalOffset': 0,
        'Abandoner': oSender.m_ID }
    cl_reward.RewardItemByMiniGame(oSender, dMsgInfo['AID'], {
        iMiniGame: (10000, iTimes) }, 'KillMonster%d %s' % (iGroupCnt, sKey), MG_SOURCE_KILLMONSTEREXT, dMiniGameExtInfo)


class CHallLevelNode(CMainLevelNode):
    m_LevelType = LEVEL_TYPE_HALL
    m_GameType = GAMETYPE_NONE
    m_TargetName = ''


class CBossLevelNode(CMainLevelNode):
    m_LevelType = LEVEL_TYPE_BOSS
    m_GameType = GAMETYPE_ASSASSINATE
    m_TargetName = '击败boss'
    
    def OnLevelGoal(self, dTrigger):
        super().OnLevelGoal(dTrigger)
        oGame = self.m_Game
        lstLiveHero = oGame.m_WarMgr.GetLiveHero()
        for iHero in lstLiveHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oHero.AddPerform(PASS_BOSS_LEVEL_WUDI_PF, 1)
        

    
    def OnPassLevel(self, lstPlayer, dTransfer):
        oGame = self.m_Game
        lstLiveHero = oGame.m_WarMgr.GetLiveHero()
        for iHero in lstLiveHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oHero.m_Perform.RemovePerform(oHero, PASS_BOSS_LEVEL_WUDI_PF)
        
        super().OnPassLevel(lstPlayer, dTransfer)



class CConvoyLevelNode(CMainLevelNode):
    m_LevelType = LEVEL_TYPE_FIGHT
    m_GameType = GAMETYPE_CONVOY
    m_TargetName = '护送目标到指定地点'
    
    def OnLevelInit(self):
        super().OnLevelInit()
        cl_msgcenter.AddFunction(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnChallengeTrigger, 'ChallengeConvoyLevel', -1, 0)

    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, 'ChallengeConvoyLevel')

    
    def OnChallengeTrigger(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        iRlt = dMsgInfo['Rlt']
        if self.m_Level != iLevel:
            return None
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, 'ChallengeConvoyLevel')
        if not iRlt:
            oGame = self.m_Game
            oReason = cl_object.reason.CStrReason('挑战失败')
            for iHero in oGame.m_WarMgr.GetLiveHero():
                oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
                if not oHero:
                    continue
                oHero.HPDirectModify('Shield', 0, -oHero.Shield(), oReason)
                oHero.HPDirectModify('HP', 0, -oHero.HP(), oReason)
            
            self.LevelGoal({ })



class CBaseDefendLevelNode(CMainLevelNode):
    m_LevelType = LEVEL_TYPE_FIGHT
    m_GameType = GAMETYPE_DEFEND
    m_TargetName = '守卫目标'
    m_MsgName = 'ChallengeBaseDefendLevel'
    
    def OnLevelInit(self):
        super().OnLevelInit()
        cl_msgcenter.AddFunction(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnChallengeTrigger, self.m_MsgName, -1, 0)

    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.m_MsgName)

    
    def OnChallengeTrigger(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        iRlt = dMsgInfo['Rlt']
        if self.m_Level != iLevel:
            return None
        if 'Protege' not in dMsgInfo['OtherInfo']:
            SendAlert('err', '守护关%s触发了非守护挑战%s' % (iLevel, dMsgInfo['Key']))
            return None
        iProtege = dMsgInfo['OtherInfo']['Protege']
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.m_MsgName)
        if not iRlt:
            oProtege = self.m_Game.GetObject(iProtege)
            if not oProtege:
                self.OnChallengeFail()
                return None
            iRemoveDelay = oProtege.m_RemoveDelay
            if iRemoveDelay:
                self.m_CtrlMgr.Call_Out(self.OnChallengeFail, iRemoveDelay, 'DefendLevelNode')
            else:
                self.OnChallengeFail()

    
    def OnChallengeFail(self):
        self.m_PassLevel = False
        oReason = cl_object.reason.CStrReason('挑战失败')
        for iHero in self.m_Game.m_WarMgr.GetLiveHero():
            oHero = self.m_Game.GetObject(iHero, PY_FLAG_DEAD)
            if not oHero:
                continue
            oHero.HPDirectModify('Shield', 0, -oHero.Shield(), oReason)
            oHero.HPDirectModify('HP', 0, -oHero.HP(), oReason)
        
        self.LevelGoal({
            'PassLevel': False })



class CDefendLevelNode(CBaseDefendLevelNode):
    m_LevelType = LEVEL_TYPE_FIGHT
    m_GameType = GAMETYPE_DEFEND
    m_TargetName = '守卫目标'
    m_MsgName = 'ChallengeDefendLevel'


class CLimitDefendNode(CBaseDefendLevelNode):
    m_LevelType = LEVEL_TYPE_FIGHT
    m_GameType = GAMETYPE_LIMITDEFEND
    m_TargetName = '限时守卫'
    m_MsgName = 'ChallengeLimitDefendLevel'

