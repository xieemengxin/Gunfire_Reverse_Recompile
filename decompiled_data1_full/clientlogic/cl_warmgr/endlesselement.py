# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/endlesselement.pyc
# RelativePath: clientlogic/cl_warmgr/endlesselement.pyc
# Source Generated with Decompyle++
# File: endlesselement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_only import ChooseKey, DeepCopy, Time2Frame
from cl_commondefines import NWARRIOR_NPC_BENEDICTION, DAM_MASK_CLASS, DAM_MASK_ELEMENT, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, MG_CASH, MG_GSCASH, WARRIOR_BOSS, NWARRIOR_NPC_PASSBOX, ENDLESS_TIME_STATUS_PAUSE, ENDLESS_TIME_STATUS_RUNNING, ENDLESS_TIME_STATUS_OVER, LEVEL_TYPE_HALL, NWARRIOR_DROP_CASH, NWARRIOR_DROP_GSCASH, MAX_GSCASH, ENDLESS_BASE, ENDLESS_TIME, WARRIOR_NORMAL, WARRIOR_ELITE, NWARRIOR_NPC_ALL_GOLDENCUP
from cl_object.logging import EndlessLog
import cl_msgcenter
import cl_formula
import cl_snetwar as net
import cl_extraattr
NEED_CLEAR_MGSID = [
    4001]

class CBaseEndlessElement(CBaseElement):
    m_EndlessMode = ENDLESS_BASE
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'BaseEndlessElement'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_RecordBaseLayer = []
        self.m_StartEndless = False
        self.m_BaseLevelCtrlConf = { }
        self.m_ChooseLayerMap = { }
        self.m_MonsterExtraGrade = { }
        self.m_LayerInitExtraGrade = 0
        self.m_PassLevelNum = 0
        self.m_PassLayerNum = 0
        self.m_KillBossNum = 0
        self.m_CurLevelNum = 0
        self.m_ValidCycle = oData.m_Config.get('ValidCycle', 0)
        self.m_ReplaceNpc = oData.m_Config.get('ReplaceNpc', { })
        self.m_StartLayer = oData.m_Config.get('StartLayer', 0)
        self.m_GapLayer = oData.m_Config.get('GapLayer', 0)
        self.m_FilterLayerCnt = oData.m_Config.get('FilterLayerCnt', 2)
        self.m_MonsterInitPerform = oData.m_Config.get('MonsterInitPerform', { })
        self.m_GivenBaseLayer = oData.m_Config.get('GivenBaseLayer', { })
        self.m_ExcludeCacheMG = oData.m_Config.get('ExcludeCacheMG', [])
        self.m_MonsterTeamFactor = oData.m_Config.get('MonsterTeamFactor', { })
        self.m_LimitMonsterResistance = oData.m_Config.get('LimitMonsterResistance', 9000)
        self.m_LayerConfig = oData.m_LayerConfig
        self.m_InitPassive = oData.m_InitPassive
        self.m_MonsterGrade = oData.m_MonsterGrade
        self.m_MonsterExtraInfo = oData.m_MonsterExtraInfo
        self.m_BossAttrAdjust = oData.m_BossAttrAdjust
        self.m_WeaponGrade = oData.m_WeaponGrade
        self.m_MonsterResistance = oData.m_MonsterResistance
        self.m_MonsterResistanceAdd = oData.m_MonsterResistanceAdd
        self.m_CampFireNpc = oData.m_Config.get('CampFireNpc', { })

    
    def Init(self):
        if not self.ValidOpen():
            return None
        self.AddAttention()
        oMiniGameMgr = self.m_Game.m_MiniGameMgr
        for iSID in self.m_ExcludeCacheMG:
            oMiniGameMgr.AddExcludeCacheMG(iSID)
        

    
    def Release(self):
        self.DoneAttention()
        self.m_WarMgr = None
        super().Release()

    
    def Save(self):
        dData = {
            'LM': DeepCopy(self.m_ChooseLayerMap),
            'CL': self.m_CurLevelNum,
            'PL': self.m_PassLevelNum,
            'KB': self.m_KillBossNum,
            'MR': self.m_MonsterResistance,
            'PY': self.m_PassLayerNum }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ChooseLayerMap = dData['LM']
        self.m_CurLevelNum = dData.get('CL', 0)
        self.m_PassLevelNum = dData.get('PL', 0)
        self.m_KillBossNum = dData.get('KB', 0)
        self.m_MonsterResistance = dData.get('MR', 0)
        self.m_PassLayerNum = dData.get('PY', 0)

    
    def SaveSeed(self, oHero):
        return self.Save()

    
    def LoadSeed(self, dData):
        self.Load(dData)
        self.OnAddAllPlayer(self, self.m_WarMgr, { })
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        self.OnInitLevelCtrl(self, oLevelCtrl, dData)

    
    def ValidOpen(self):
        if self.m_ValidCycle and self.m_WarMgr.m_Cycle < self.m_ValidCycle:
            EndlessLog.Error('%d open %s err cycle:%s<%s' % (self.m_Game.m_ID, self.m_EndlessMode, self.m_WarMgr.m_Cycle, self.m_ValidCycle))
            return False
        return True

    
    def AddAttention(self):
        if not self.m_WarMgr:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self.OnInitLevelCtrl, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, self.OnLevelNodeFinishBefore, self.m_CallFlag)

    
    def StartEndless(self):
        EndlessLog.Info('%d %s startendless %d' % (self.m_Game.m_ID, self.m_WarMgr.GetRoomPlayer(), self.m_EndlessMode))
        self.m_StartEndless = True
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.OnCreateNpc, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.OnCreateMonsterBefore, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelNodeGoalOK, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_WEAPONGRADE, self.OnWeaponGrade, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, self.m_CallFlag)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_STARTENDLESS, self.m_WarMgr, { })

    
    def DoneAttention(self):
        if not self.m_WarMgr:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_WEAPONGRADE, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_WARMGR_LEVELCTRLINIT, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)

    
    def DisableUnlockProgressCon(self):
        for iHero in self.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            oHero.DisableUnlockProgressCon()
        

    
    def OnAddAllPlayer(self, oEndlessElement, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        for iHero in oWarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            for iPerform in self.m_InitPassive:
                oHero.AddPerform(iPerform, 1)
            
        

    
    def OnInitLevelCtrl(self, oEndlessElement, oLevelCtrl, dMsgInfo):
        self.m_BaseLevelCtrlConf = { }
        self.m_BaseLevelCtrlConf.update(oLevelCtrl.m_LevelCtrlConf)
        dLevelCtrlConf = { }
        dLevelCtrlConf.update(oLevelCtrl.m_LevelCtrlConf)
        oLevelCtrl.m_LevelCtrlConf = dLevelCtrlConf
        iMaxLayer = oLevelCtrl.GetMaxLayer()
        self.m_RecordBaseLayer = list(range(1, iMaxLayer + 1))[-(self.m_FilterLayerCnt):]
        self.m_WarMgr.m_MaxLayer = 999999
        self.LoadChooseInfo()

    
    def LoadChooseInfo(self):
        EndlessLog.Debug('%d loadchooseinfo %s' % (self.m_Game.m_ID, self.m_ChooseLayerMap))
        if not self.m_ChooseLayerMap:
            return None
        for iLayer, iBaseLayer in self.m_ChooseLayerMap.items():
            self.AddLayerInfo(iLayer, iBaseLayer)
        

    
    def OnLayerStart(self, oEndlessElement, oLevelCtrl, dMsgInfo):
        iCurLayer = dMsgInfo['Layer']
        iMaxLayer = oLevelCtrl.GetMaxLayer()
        if iCurLayer == iMaxLayer:
            self.ChooseNextLayer(iCurLayer, oLevelCtrl)
        if not (self.m_StartEndless) and iCurLayer in self.m_ChooseLayerMap:
            self.StartEndless()

    
    def ChooseNextLayer(self, iCurLayer, oLevelCtrl):
        dWeight = dict.fromkeys(self.m_BaseLevelCtrlConf, 10)
        iLayer = iCurLayer + 1
        if iLayer in self.m_GivenBaseLayer:
            iBaseLayer = self.m_GivenBaseLayer[iLayer]
        else:
            for iBaseLayer in self.m_RecordBaseLayer:
                dWeight.pop(iBaseLayer, 0)
            
            iBaseLayer = ChooseKey(self.m_Game, dWeight)
        EndlessLog.Info('%d chooselayer:(%s:%s) %s filter:%s' % (self.m_Game.m_ID, iLayer, iBaseLayer, list(dWeight), self.m_RecordBaseLayer))
        self.AddLayerInfo(iLayer, iBaseLayer)

    
    def AddLayerInfo(self, iLayer, iBaseLayer):
        self.m_ChooseLayerMap[iLayer] = iBaseLayer
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        dLevelCtrlConf = oLevelCtrl.m_LevelCtrlConf
        dLevelCtrlConf[iLayer] = { }
        dBaseLevelCtrlConf = self.m_BaseLevelCtrlConf[iBaseLayer]
        dLevelCtrlConf[iLayer].update(dBaseLevelCtrlConf)
        if iBaseLayer in self.m_LayerConfig:
            dLevelCtrlConf[iLayer]['LayerChoose'] = self.m_LayerConfig[iBaseLayer]['LayerChoose']
        self.m_RecordBaseLayer.append(iBaseLayer)
        self.m_RecordBaseLayer = self.m_RecordBaseLayer[-(self.m_FilterLayerCnt):]
        if iLayer in self.m_MonsterExtraGrade:
            return None
        (iLevelAddGrade, iLayerAddGrade) = (0, 0)
        for iLimitLayer, tExtraInfo in self.m_MonsterExtraInfo.items():
            if iLimitLayer > iLayer:
                break
            (iLevelAddGrade, iLayerAddGrade) = tExtraInfo
        
        dData = {
            'Layer': iLayer }
        iLevelAddGrade = cl_formula.GetFormulaResult(self, iLevelAddGrade, dData)
        iLayerAddGrade = cl_formula.GetFormulaResult(self, iLayerAddGrade, dData)
        dMonsterExtraGrade = { }
        iGrade = self.m_LayerInitExtraGrade
        if iLevelAddGrade > 0:
            for iLevelIdx in range(1, dBaseLevelCtrlConf['CtrlSize'] + 2):
                iMinGrade = iGrade
                iGrade += iLevelAddGrade
                dMonsterExtraGrade[iLevelIdx] = (iMinGrade, iGrade - 1)
            
            iGrade -= 1
        self.m_LayerInitExtraGrade = iGrade + iLayerAddGrade
        self.m_MonsterExtraGrade[iLayer] = dMonsterExtraGrade

    
    def OnCreateNpc(self, oEndlessElement, oLevelCtrl, dMsgInfo):
        if not self.IsEndless():
            return None
        if 'NPC' not in dMsgInfo:
            return None
        iNpc = dMsgInfo['NPC']
        iCurLayerNum = oLevelCtrl.m_CurNode.m_LayerNum
        clsNpcData = self.m_Game.m_WarData.GetNpcData(iNpc)
        if not clsNpcData:
            return None
        if clsNpcData.m_FightType == NWARRIOR_NPC_BENEDICTION:
            if iCurLayerNum < self.m_StartLayer or (iCurLayerNum - self.m_StartLayer) % self.m_GapLayer:
                dMsgInfo['NPC'] = 0
        dNpcInfo = dMsgInfo['NPCInfo'] if 'NPCInfo' in dMsgInfo else { }
        iBanReplace = dNpcInfo['BanReplace'] if 'BanReplace' in dNpcInfo else 0
        if not iBanReplace and iNpc in self.m_ReplaceNpc:
            dMsgInfo['NPC'] = self.m_ReplaceNpc[iNpc]

    
    def OnStartFight(self, oEndlessElement, oWarMgr, dMsgInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelType = dMsgInfo['LevelType']
        if iLevelType in [
            LEVEL_TYPE_FIGHT,
            LEVEL_TYPE_BOSS]:
            self.m_CurLevelNum += 1
            EndlessLog.Info('%d players%s levelnum:%s resistance:%s' % (self.m_Game.m_ID, oWarMgr.GetRoomPlayer(), self.m_CurLevelNum, self.m_MonsterResistance))
            self.NotifyEndlessInfo()
        elif iLevelType == LEVEL_TYPE_HALL and oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum) in self.m_CampFireNpc:
            iLevelID = dMsgInfo['LevelID']
            oLevelNode = oLevelCtrl.GetLevelNode(iLevelID)
            dAddInfo = oLevelCtrl.m_LevelConfData.GetMapConfig(iLevelID, 'campfirepos')
            if not dAddInfo:
                return None
            dAddInfo = DeepCopy(dAddInfo)
            iScene = oLevelNode.m_Scene
            dMsgInfo = {
                'NPC': self.m_CampFireNpc[oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)],
                'LevelNode': oLevelNode,
                'NPCInfo': dAddInfo,
                'Scene': iScene }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelCtrl, dMsgInfo)
            if not dMsgInfo['NPC']:
                return None
            self.m_Game.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dAddInfo)

    
    def OnPlayerMapLoadOK(self, oEndlessElement, oHero, dInfo):
        dPlayer = {
            oHero.m_PlayerID: 1 }
        self.NotifyEndlessInfo(dPlayer)

    
    def NotifyEndlessInfo(self, dPlayer = None):
        if dPlayer is None:
            dPlayer = self.m_WarMgr.GetRoomPlayer()
        net.GS2CEndlessInfo(self.m_Game, self.m_CurLevelNum, self.m_PassLevelNum, self.m_KillBossNum, self.m_MonsterResistance, dPlayer)

    
    def OnCreateMonsterBefore(self, oEndlessElement, oWarMgr, dMsgInfo):
        if not self.IsEndless():
            return None
        dMsgInfo['ForceGrade'] = self.m_MonsterGrade

    
    def OnCreateMonster(self, oEndlessElement, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        oMonster = oGame.GetObject(dMsgInfo['Monster'])
        if not oMonster:
            return None
        if 'Default' in self.m_MonsterInitPerform:
            for iPerform in self.m_MonsterInitPerform['Default']:
                oMonster.AddPerform(iPerform, 1)
            
        if oMonster.m_DataSID in self.m_MonsterInitPerform:
            for iPerform in self.m_MonsterInitPerform[oMonster.m_DataSID]:
                oMonster.AddPerform(iPerform, 1)
            
        if not oMonster.m_Resistance:
            oMonster.m_Resistance = cl_extraattr.CResistance('Resistance', 0, iSync = 0)
        oMonster.m_Resistance.SetLimit(self.m_LimitMonsterResistance)
        oMonster.m_Resistance.ModifyResistance(oMonster, self.m_MonsterResistance, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1, self.m_CallFlag)

    
    def OnLevelNodeGoalOK(self, oEndlessElement, oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType in [
            LEVEL_TYPE_FIGHT,
            LEVEL_TYPE_BOSS]:
            self.m_PassLevelNum += 1
            if iLevelType == LEVEL_TYPE_BOSS:
                self.m_PassLayerNum += 1
                self.m_KillBossNum += 1
            self.NotifyEndlessInfo()

    
    def OnLevelNodeFinishBefore(self, oEndlessElement, oWarMgr, dMsgInfo):
        if self.m_StartEndless and self.m_MonsterResistance < self.m_LimitMonsterResistance:
            self.CalMonsterResistance(dMsgInfo)
        self.OnRecycleCup(oWarMgr)

    
    def CalMonsterResistance(self, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType in [
            LEVEL_TYPE_FIGHT,
            LEVEL_TYPE_BOSS]:
            iLayer = dMsgInfo['Layer']
            (iLevelAdd, iLayerAdd) = (0, 0)
            for iLimitLayer, tAddInfo in self.m_MonsterResistanceAdd.items():
                if iLimitLayer > iLayer:
                    break
                (iLevelAdd, iLayerAdd) = tAddInfo
            
            dData = {
                'Layer': iLayer }
            if iLevelType == LEVEL_TYPE_BOSS:
                iAdd = cl_formula.GetFormulaResult(self, iLayerAdd, dData)
            else:
                iAdd = cl_formula.GetFormulaResult(self, iLevelAdd, dData)
            if iAdd:
                self.m_MonsterResistance += iAdd
                if self.m_MonsterResistance >= self.m_LimitMonsterResistance:
                    self.m_MonsterResistance = self.m_LimitMonsterResistance
            self.NotifyEndlessInfo()

    
    def OnRecycleCup(self, oWarMgr):
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        for oNode in oLevelCtrl.m_LevelNodeLib.values():
            oScene = oGame.m_SceneMgr.GetScene(oNode.m_Scene)
            if not oScene:
                continue
            lstNPC = oScene.GetObjectsByType('NPC')
            for pid in self.m_WarMgr.GetLivePlayer(iCalAI = 0):
                for iNPC in lstNPC:
                    oNPC = self.m_Game.GetObject(iNPC)
                    if not oNPC:
                        continue
                    if oNPC.m_FightType not in NWARRIOR_NPC_ALL_GOLDENCUP:
                        continue
                    if not oNPC.IsAutoRecycle():
                        continue
                    oNPC.Recycle(pid)
                
            
        

    
    def OnWeaponGrade(self, oEndlessElement, oWarMgr, dMsgInfo):
        if not self.IsEndless():
            return None
        dMsgInfo['Grade'] = cl_formula.GetFormulaResult(self, self.m_WeaponGrade)

    
    def IsEndless(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iCurLayer = oLevelCtrl.m_LayerNum
        return iCurLayer in self.m_ChooseLayerMap

    
    def GetMonsterExtraGrade(self, iLevel, iRoomPos):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        if not oLevelNode:
            return 0
        if iLevel != oLevelNode.m_Level:
            iRoomPos = 0
        iLayerNum = oLevelCtrl.m_LayerNum
        iLevelNum = oLevelCtrl.m_LevelNum
        if iLayerNum in self.m_MonsterExtraGrade and iLevelNum in self.m_MonsterExtraGrade[iLayerNum]:
            iRoomCnt = len(oLevelNode.m_RoomList)
            (iMinGrade, iMaxGrade) = self.m_MonsterExtraGrade[iLayerNum][iLevelNum]
            return iMinGrade + (iMaxGrade - iMinGrade) * (iRoomPos + 1) // iRoomCnt
        return 0

    
    def GetBaseLayer(self, iLayer):
        if iLayer not in self.m_ChooseLayerMap:
            return iLayer
        return self.m_ChooseLayerMap[iLayer]

    
    def GetEndlessMode(self):
        return self.m_EndlessMode

    
    def GetMonsterTeamFactor(self, oMonster):
        iFightType = oMonster.m_FightType
        if not self.m_StartEndless:
            return 1
        if iFightType & WARRIOR_NORMAL == WARRIOR_NORMAL or oMonster.Query('Demon'):
            sType = 'Normal'
        elif iFightType & WARRIOR_ELITE == WARRIOR_ELITE:
            sType = 'Elite'
        elif iFightType & WARRIOR_BOSS == WARRIOR_BOSS:
            sType = 'Boss'
        else:
            return 1
        if sType in self.m_MonsterTeamFactor:
            return self.m_MonsterTeamFactor[sType]
        return 1

    
    def GetPassLayerNum(self):
        return self.m_PassLayerNum

    
    def GetEndLessStartLayer(self):
        return self.m_StartLayer



class CEndlessElement(CBaseEndlessElement):
    m_EndlessMode = ENDLESS_TIME
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'EndlessElement'
        self.m_ChoseBossLevelRecord = { }
        self.m_BossDropInfo = oData.m_Config.get('BossDropInfo', { })
        self.m_DemonDropInfo = oData.m_Config.get('DemonDropInfo', { })
        self.m_InteractGoldenCupReward = oData.m_Config.get('InteractGoldenCupReward', { })
        self.m_NoSameBossEndLayer = oData.m_Config.get('NoSameBossEndLayer', 0)
        self.m_InitTime = oData.m_Config.get('InitTime', 120000)
        self.m_LevelCountdown = oData.m_LevelCountdown
        self.m_RemainFrame = Time2Frame(self.m_InitTime)
        self.m_LastUpdateFrame = 0
        self.m_TimeStatus = ENDLESS_TIME_STATUS_PAUSE
        self.m_TimeOutFlag = 'EndlessElement_TimeOut'
        self.m_Totaltime = self.m_InitTime
        self.m_CurLevelStartRemainFarme = self.m_RemainFrame
        self.m_CurLevelAddFrame = 0

    
    def Save(self):
        dData = {
            'LM': DeepCopy(self.m_ChooseLayerMap),
            'CL': self.m_CurLevelNum,
            'PL': self.m_PassLevelNum,
            'KB': self.m_KillBossNum,
            'MR': self.m_MonsterResistance,
            'RF': self.m_RemainFrame,
            'TS': self.m_TimeStatus,
            'BL': self.m_ChoseBossLevelRecord,
            'TT': self.m_Totaltime,
            'PY': self.m_PassLayerNum }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ChooseLayerMap = dData['LM']
        self.m_CurLevelNum = dData.get('CL', 0)
        self.m_PassLevelNum = dData.get('PL', 0)
        self.m_KillBossNum = dData.get('KB', 0)
        self.m_MonsterResistance = dData.get('MR', 0)
        self.m_Totaltime = dData.get('TT', 0)
        self.m_PassLayerNum = dData.get('PY', 0)
        if 'RF' in dData:
            self.m_RemainFrame = dData['RF']
        if 'TS' in dData:
            self.m_TimeStatus = dData['TS']
        if 'BL' in dData:
            self.m_ChoseBossLevelRecord = dData['BL']

    
    def AddAttention(self):
        if not self.m_WarMgr:
            return None
        super().AddAttention()
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, self.m_CallFlag)

    
    def StartEndless(self):
        super().StartEndless()
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CG_START, self.OnCGStart, self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CG_END, self.OnCGEnd, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_BEFORECREATEDEMON, self.OnBeforeCreateDemon, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, self.m_CallFlag)
        if oLevelCtrl.m_LayerNum < self.m_NoSameBossEndLayer:
            cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_BEFORE_CHOOSEBOSSLEVEL, self.OnBeforeChooseBossLevel, self.m_CallFlag)

    
    def DoneAttention(self):
        if not self.m_WarMgr:
            return None
        super().DoneAttention()
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CG_START, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CG_END, self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_BEFORE_CHOOSEBOSSLEVEL, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_BEFORECREATEDEMON, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.m_CallFlag)

    
    def IsTimeOut(self):
        return self.m_TimeStatus == ENDLESS_TIME_STATUS_OVER

    
    def TimeOut(self):
        if self.IsTimeOut():
            return None
        self.UpdateRemainTime()
        if self.m_RemainFrame > 0:
            return None
        EndlessLog.Info('%d remaintime timeout' % self.m_Game.m_ID)
        self.m_TimeStatus = ENDLESS_TIME_STATUS_OVER
        self.RefreshTime()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_ENDLESS_TIMEOUT, self.m_WarMgr, { })

    
    def AddRemainTime(self, iTime, sReason):
        if not iTime or self.IsTimeOut():
            return None
        self.UpdateRemainTime()
        iAddFrame = Time2Frame(iTime)
        self.m_RemainFrame += iAddFrame
        if self.m_Totaltime:
            self.m_Totaltime += iTime
            self.m_CurLevelAddFrame += iAddFrame
        EndlessLog.Info('%d addtime %d %d %s' % (self.m_Game.m_ID, iAddFrame, self.m_RemainFrame, sReason))
        self.NotifyChangeTime(iTime)
        self.RefreshTime()
        self.Remove_Call_Out(self.m_TimeOutFlag)
        if self.m_RemainFrame <= 0:
            self.TimeOut()
        elif self.m_TimeStatus == ENDLESS_TIME_STATUS_RUNNING:
            self.Call_Out(self.TimeOut, self.m_RemainFrame, self.m_TimeOutFlag)

    
    def UpdateRemainTime(self):
        if self.m_TimeStatus != ENDLESS_TIME_STATUS_RUNNING:
            return None
        iCurFrame = self.m_Game.GetFrameNum()
        if iCurFrame == self.m_LastUpdateFrame:
            return None
        iRemainFrame = self.m_RemainFrame - iCurFrame - self.m_LastUpdateFrame
        if iRemainFrame < 0:
            iRemainFrame = 0
        self.m_RemainFrame = iRemainFrame
        self.m_LastUpdateFrame = iCurFrame

    
    def Pause(self, sReason):
        self.UpdateRemainTime()
        EndlessLog.Info('%d pause %d %s %s' % (self.m_Game.m_ID, self.m_RemainFrame, self.m_TimeStatus, sReason))
        if self.m_TimeStatus != ENDLESS_TIME_STATUS_RUNNING:
            return None
        self.m_TimeStatus = ENDLESS_TIME_STATUS_PAUSE
        self.Remove_Call_Out(self.m_TimeOutFlag)
        self.RefreshTime()

    
    def Resume(self, sReason):
        EndlessLog.Info('%d resume %d %s %s' % (self.m_Game.m_ID, self.m_RemainFrame, self.m_TimeStatus, sReason))
        if self.m_TimeStatus != ENDLESS_TIME_STATUS_PAUSE:
            return None
        self.m_TimeStatus = ENDLESS_TIME_STATUS_RUNNING
        self.m_LastUpdateFrame = self.m_Game.GetFrameNum()
        self.RefreshTime()
        self.Remove_Call_Out(self.m_TimeOutFlag)
        if self.m_RemainFrame > 0:
            self.Call_Out(self.TimeOut, self.m_RemainFrame, self.m_TimeOutFlag)
        else:
            self.TimeOut()

    
    def NotifyChangeTime(self, iChangeTime):
        net.GS2CEndlessChangeTime(self.m_Game, iChangeTime, self.m_WarMgr.GetRoomPlayer())

    
    def RefreshTime(self):
        self.NotifyRemainTime(self.m_WarMgr.GetRoomPlayer())

    
    def NotifyRemainTime(self, dPlayer):
        self.UpdateRemainTime()
        net.GS2CEndlessTime(self.m_Game, self.m_TimeStatus, self.GetTimeOutFrame(), dPlayer)

    
    def GetTimeOutFrame(self):
        if self.IsTimeOut():
            return 0
        return self.m_Game.GetFrameNum() + self.m_RemainFrame

    
    def OnLevelNodeInit(self, oEndlessElement, oWarMgr, dMsgInfo):
        if self.IsEndless():
            cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_CallFlag)
            return None
        if 'LevelType' not in dMsgInfo or 'LevelID' not in dMsgInfo or 'Layer' not in dMsgInfo:
            return None
        if dMsgInfo['LevelType'] != LEVEL_TYPE_BOSS:
            return None
        iLevel = dMsgInfo['LevelID']
        iLayer = dMsgInfo['Layer']
        if iLevel and iLayer:
            if iLayer not in self.m_ChoseBossLevelRecord:
                self.m_ChoseBossLevelRecord[iLayer] = {
                    iLevel: 1 }
            else:
                self.m_ChoseBossLevelRecord[iLayer][iLevel] = 1

    
    def OnPlayerMapLoadOK(self, oEndlessElement, oHero, dInfo):
        super().OnPlayerMapLoadOK(oEndlessElement, oHero, dInfo)
        self.NotifyRemainTime({
            oHero.m_PlayerID: 1 })

    
    def OnCreateMonster(self, oEndlessElement, oWarMgr, dMsgInfo):
        super().OnCreateMonster(oEndlessElement, oWarMgr, dMsgInfo)
        oGame = self.m_Game
        oMonster = oGame.GetObject(dMsgInfo['Monster'])
        dReward = oMonster.GetDieReward()
        if not oMonster or not dReward:
            return None
        iRound = oGame.m_WarMgr.m_Round
        dNewReward = dict(dReward)
        oWarData = oGame.m_WarData
        dDropInfo = {
            MG_GSCASH: self.m_BossDropInfo['GSCash'],
            MG_CASH: self.m_BossDropInfo['Cash'] }
        for iMiniGame in dReward:
            clsMiniGame = oWarData.GetMiniGameData(iMiniGame)
            iMGType = clsMiniGame.m_Type
            if iMGType in dDropInfo:
                iFightType = oMonster.m_FightType
                if iFightType & WARRIOR_BOSS == WARRIOR_BOSS and WARRIOR_BOSS in clsMiniGame.m_TypeBase:
                    dNewReward[iMiniGame] = (10000, dDropInfo[iMGType] // clsMiniGame.m_TypeBase[WARRIOR_BOSS])
                    continue
                dNewReward.pop(iMiniGame)
        
        oMonster.m_Reward[iRound] = dNewReward

    
    def OnBeforeCreateDemon(self, oEndlessElement, oHero, dMsgInfo):
        if 'Reward' not in dMsgInfo:
            return None
        dInfo = dMsgInfo['Reward']
        iDone = 0
        dDropInfo = {
            NWARRIOR_DROP_GSCASH: [
                {
                    'GSCash': self.m_DemonDropInfo['GSCash'] },
                {
                    'GSCash': 0 }],
            NWARRIOR_DROP_CASH: [
                {
                    'Cash': self.m_DemonDropInfo['Cash'] },
                {
                    'Cash': 0 }] }
        for _, lstInfo in dInfo.items():
            (_, lstReward, _) = lstInfo
            for dReward in lstReward:
                dRewardInfo = dReward['info'] if 'info' in dReward else { }
                if not 'DropType' in dRewardInfo and dRewardInfo['DropType'] in dDropInfo or iDone:
                    dRewardInfo['DropInfo'] = [
                        dDropInfo[dRewardInfo['DropType']][0]]
                    iDone = 1
                    continue
                dRewardInfo['DropInfo'] = [
                    dDropInfo[dRewardInfo['DropType']][1]]
            
        

    
    def OnNpcInteract(self, oEndlessElement, oHero, dMsgInfo):
        if 'NpcType' not in dMsgInfo:
            return None
        if dMsgInfo['NpcType'] != NWARRIOR_NPC_PASSBOX:
            return None
        sReason = 'endless-npcinteract'
        oGame = self.m_Game
        lstHero = oGame.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            self.RewardExtraCash(oHero, sReason)
            self.RewardExtraGSCash(oHero, sReason)
        

    
    def RewardExtraCash(self, oHero, sReason):
        iCash = self.m_InteractGoldenCupReward['Cash']
        iMaxCash = oHero.MaxCash()
        if oHero.m_WarCash + iCash > iMaxCash:
            iCash = iMaxCash - oHero.m_WarCash
        oHero.AddCash(iCash, sReason)

    
    def RewardExtraGSCash(self, oHero, sReason):
        iGSCash = self.m_InteractGoldenCupReward['GSCash']
        if oHero.m_WarGSCash + iGSCash > MAX_GSCASH:
            iGSCash = MAX_GSCASH - oHero.m_WarGSCash
        oHero.AddGSCash(iGSCash, sReason)

    
    def OnLevelNodeGoalOK(self, oEndlessElement, oWarMgr, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType in [
            LEVEL_TYPE_FIGHT,
            LEVEL_TYPE_BOSS]:
            self.m_PassLevelNum += 1
            if iLevelType == LEVEL_TYPE_BOSS:
                self.m_PassLayerNum += 1
                self.m_KillBossNum += 1
            self.NotifyEndlessInfo()
            iAddTime = 0
            iLayer = dMsgInfo['Layer']
            (iLevelAddTime, iLayerAddTime) = (0, 0)
            for iLimitLayer, tExtraInfo in self.m_LevelCountdown.items():
                if iLimitLayer > iLayer:
                    break
                (iLevelAddTime, iLayerAddTime) = tExtraInfo
            
            dData = {
                'Layer': iLayer }
            if iLevelType == LEVEL_TYPE_BOSS:
                iAddTime = cl_formula.GetFormulaResult(self, iLayerAddTime, dData)
            else:
                iAddTime = cl_formula.GetFormulaResult(self, iLevelAddTime, dData)
            self.AddRemainTime(iAddTime, 'LevelNodeGoal')
        if iLevelType in [
            LEVEL_TYPE_FIGHT,
            LEVEL_TYPE_BOSS,
            LEVEL_TYPE_HALL]:
            self.Pause('LevelGoal')

    
    def OnStartFight(self, oEndlessElement, oWarMgr, dMsgInfo):
        super().OnStartFight(oEndlessElement, oWarMgr, dMsgInfo)
        iLevelType = dMsgInfo['LevelType']
        if iLevelType in [
            LEVEL_TYPE_FIGHT,
            LEVEL_TYPE_BOSS]:
            self.m_CurLevelStartRemainFarme = self.m_RemainFrame
            self.m_CurLevelAddFrame = 0
            if iLevelType != LEVEL_TYPE_BOSS:
                self.Resume('StartFight')

    
    def OnCGStart(self, oEndlessElement, oWarMgr, dMsgInfo):
        self.Pause('CGStart')

    
    def OnCGEnd(self, oEndlessElement, oWarMgr, dMsgInfo):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oCurNode = oLevelCtrl.m_CurNode
        if not oCurNode or oCurNode.HasGoaledCurNode():
            return None
        self.Resume('CGEnd')

    
    def OnBeforeChooseBossLevel(self, oEndlessElement, oLevelCtrl, dMsgInfo):
        if 'FilterLevel' not in dMsgInfo:
            return None
        iCurLayer = oLevelCtrl.m_LayerNum
        if iCurLayer not in self.m_ChooseLayerMap:
            return None
        if iCurLayer >= self.m_NoSameBossEndLayer:
            cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_BEFORE_CHOOSEBOSSLEVEL, self.m_CallFlag)
            return None
        dFilterLevel = dMsgInfo['FilterLevel']
        iBaseLayer = self.m_ChooseLayerMap[iCurLayer]
        if iBaseLayer in self.m_ChoseBossLevelRecord:
            for iLevel in self.m_ChoseBossLevelRecord[iBaseLayer]:
                dFilterLevel[iLevel] = 1
            



def GetComponentClass(oMgrManager):
    return CEndlessElement

