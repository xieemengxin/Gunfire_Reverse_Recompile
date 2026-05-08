# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/levellinenode.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/levellinenode.pyc
# Source Generated with Decompyle++
# File: levellinenode.pyc (Python 3.6)

from cl_commondefines import TRANSFER_DIRTO_NEXT, TRANSFER_DIRTO_MAIN, TRANSFER_DIRTO_PASS, TRANSFER_DIRTO_LAYER, LEVEL_TYPE_HIDE, LEVEL_TYPE_FIGHT, SPAWN_TRIGGERGATE
from cl_only import Functor, ShufferList, SendAlert
import cl_snetwar
import cl_msgcenter
from . import linemonsterctrl
from . import linespawnaction
from . import linenewmonsterctrl
from . import survivormonsterctrl

class CBaseLevelLine(object):
    
    def __init__(self, oLevelNode, iIndexInLevel, iIndexInRoom, sLineName):
        self.m_IndexInLevel = iIndexInLevel
        self.m_IndexInRoom = iIndexInRoom
        self.m_Name = sLineName
        self.m_Game = oLevelNode.m_CtrlMgr.m_Game
        self.m_LevelNode = oLevelNode
        self.m_MonsterCtrl = None
        self.m_GoalFlag = 0
        self.m_Reward = []
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        self.m_Area = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, self.m_Name, 'area')
        self.CreateMonsterCtrl()

    
    def CreateMonsterCtrl(self):
        if self.m_LevelNode.m_LevelType == LEVEL_TYPE_FIGHT:
            oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
            oNewSurvivorElement = self.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
            if oSurvivorElement:
                self.m_MonsterCtrl = survivormonsterctrl.CSurvivorMonsterCtrl(self, oSurvivorElement)
                return None
            if oNewSurvivorElement:
                self.m_MonsterCtrl = survivormonsterctrl.CNewSurvivorMonsterCtrl(self, oNewSurvivorElement)
                return None
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        newconfig = oLevelConfData.GetMapConfig(self.m_LevelNode.m_Level, 'newconfig')
        if newconfig:
            iNotify = oLevelConfData.GetLevelConfig(self.m_LevelNode.m_Level, 'ShowNotify', default = 0)
            tExtAmount = oLevelConfData.GetLevelConfig(self.m_LevelNode.m_Level, 'ExtAmount', default = 0)
            self.m_MonsterCtrl = linenewmonsterctrl.CLineMonsterCtrl(self)
            self.m_MonsterCtrl.SetNotify(iNotify)
            self.m_MonsterCtrl.SetExtAmount(tExtAmount)
        else:
            self.m_MonsterCtrl = linemonsterctrl.CLineMonsterCtrl(self)

    
    def Release(self):
        self.m_MonsterCtrl.Release()
        self.m_LevelNode = None
        self.m_Game = None

    
    def GetLineIdx(self):
        return (self.m_LevelNode.m_Level, self.m_IndexInLevel, self.m_IndexInRoom)

    
    def IsGoal(self):
        return self.m_GoalFlag

    
    def LineTargetGoal(self, *args):
        self.m_GoalFlag = 1
        self.m_LevelNode.LineGoal(self.m_IndexInLevel)

    
    def LineTargetReward(self):
        lstReward = self.m_Reward
        self.m_Reward = []
        for dAction in lstReward:
            func = dAction['func']
            if isinstance(func, int):
                func = linespawnaction.GetSpawnFunc(func)
            tParam = dAction['param']
            func(self, tParam)
        

    
    def LineInit(self):
        iRound = self.m_Game.m_WarMgr.m_Round
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        lstSpawnRule = oLevelConfData.GetLineSpawnRule(self.m_LevelNode.m_Level, self.m_Name, iRound)
        bCloseAutoSuper = False
        for dSpawn in lstSpawnRule:
            tAction = dSpawn['Action']
            for dAction in tAction:
                if dAction['type'] in ('Monster', 'AreaMonster'):
                    self.m_MonsterCtrl.AddSpawnInfo(dAction['param'])
                    continue
                if dAction['type'] == 'AreaMonsterChoose':
                    self.m_MonsterCtrl.AddSpawnInfoByChooseArea(dAction['param'])
                    continue
                if dAction['type'] == 'SuperMonster':
                    tParam = dAction['param']
                    self.m_MonsterCtrl.AddSpawnInfo(tParam[:-2])
                    bCloseAutoSuper = True
                    continue
                if dAction['type'] == 'AreaNumberChoose':
                    self.m_MonsterCtrl.AddSpawnInfoByChooseAreaAndNumber(dAction['param'])
            
        
        if bCloseAutoSuper:
            oMonsterSp = self.m_Game.m_WarMgr.GetComponent('MonsterSuper')
            if oMonsterSp:
                oMonsterSp.CloseLevelAutoSuper(self.m_LevelNode.m_Level)
        self.CreateInitNpc()
        self.CreateInitSummon()
        self.CreateInitBuild()
        self.CreateInitTransfer()
        self.CreateInitHookRopeNpc()

    
    def LineStart(self):
        iRound = self.m_Game.m_WarMgr.m_Round
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        dLineGoalRule = oLevelConfData.GetLineSpawnGoal(self.m_LevelNode.m_Level, self.m_Name, iRound)
        self.m_Reward = dLineGoalRule['Action']
        if dLineGoalRule['Cond']:
            self.m_LevelNode.m_CtrlMgr.m_LevelTrigger.LineAttention(self.LineTargetGoal, self, dLineGoalRule['Cond'])
        else:
            self.LineTargetGoal(None)
        oLevelTrigger = self.m_LevelNode.m_CtrlMgr.m_LevelTrigger
        lstSpawnRule = oLevelConfData.GetLineSpawnRule(self.m_LevelNode.m_Level, self.m_Name, iRound)
        for dSpawn in lstSpawnRule:
            oCondition = dSpawn['Cond']
            tAction = dSpawn['Action']
            cbFunc = Functor(self.DownSpawn, tAction)
            oLevelTrigger.LineAttention(cbFunc, self, oCondition)
        

    
    def GetBornPos(self):
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        for sElement in ('SurvivorElement', 'NewSurvivorElement'):
            oSurvivorElement = self.m_Game.m_WarMgr.GetComponent(sElement)
            if oSurvivorElement:
                dHeroBorn = oSurvivorElement.m_BornCtrl.GetBornPos()
                if dHeroBorn:
                    return dHeroBorn
        
        return oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, self.m_Name, 'bornpos')

    
    def GetRelifePos(self):
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        dConfig = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, self.m_Name, 'relifepos')
        if not dConfig:
            dConfig = self.GetBornPos()
        return dConfig

    
    def CreateInitNpc(self):
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        oGame = self.m_LevelNode.m_Game
        iScene = self.m_LevelNode.m_Scene
        lstNpcConfig = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, self.m_Name, 'scenenpc', 'npc')
        tLineIdx = self.GetLineIdx()
        for dNpcInfo in lstNpcConfig:
            iNpcSID = dNpcInfo['SID']
            dMsgInfo = {
                'NPC': iNpcSID,
                'LevelNode': self.m_LevelNode,
                'NPCInfo': dNpcInfo,
                'LineIdx': tLineIdx,
                'Scene': iScene }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.m_LevelNode.m_CtrlMgr, dMsgInfo)
            if not dMsgInfo['NPC'] or 'DelayCreate' in dMsgInfo:
                continue
            oGame.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dNpcInfo, tLineIdx)
        

    
    def CreateInitSummon(self):
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        oGame = self.m_LevelNode.m_Game
        iScene = self.m_LevelNode.m_Scene
        dSummonConfig = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, self.m_Name, 'scenesummon')
        for _, lstConfig in dSummonConfig.items():
            for dSummonInfo in lstConfig:
                iSummonSID = dSummonInfo['SID']
                oGame.m_ResMgr.CreateSummon(iScene, iSummonSID, dSummonInfo, self.GetLineIdx())
            
        

    
    def CreateInitTransfer(self):
        oLevelNode = self.m_LevelNode
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        oGame = oLevelNode.m_Game
        oLevelCtrl = oLevelNode.m_CtrlMgr
        iScene = oLevelNode.m_Scene
        tNpcConfig = oLevelConfData.GetLineConfig(oLevelNode.m_Level, self.m_Name, 'scenenpc', 'transfer')
        if not tNpcConfig:
            return None
        iTranferDir = self.GetTransferDir()
        iLevelType = oLevelNode.m_LevelType
        if iLevelType == LEVEL_TYPE_HIDE or oLevelCtrl.CheckFinishWar():
            tNpcConfig = ShufferList(oGame, tNpcConfig)
            for dNpcInfo in tNpcConfig:
                iNpc = dNpcInfo['SID']
                dNpcInfo['TransferDir'] = iTranferDir
                oNpc = oGame.m_ResMgr.CreateNpc(iScene, iNpc, dNpcInfo, self.GetLineIdx())
            
        else:
            dTransfer = oLevelNode.m_CtrlMgr.m_CurTransfer
            iDifficulty = oLevelNode.m_Difficulty
            lstTransfer = list(dTransfer.values())
            iLen = min(len(tNpcConfig), len(lstTransfer))
            for idx in range(iLen):
                dNextLevel = lstTransfer[idx]
                dNpcInfo = tNpcConfig[idx]
                dMsgInfo = {
                    'NPC': dNpcInfo['SID'],
                    'LevelNode': oLevelNode,
                    'NPCInfo': dNpcInfo,
                    'Scene': iScene }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelCtrl, dMsgInfo)
                if not dMsgInfo['NPC']:
                    continue
                iNpc = dMsgInfo['NPC']
                dNpcInfo['TransferDir'] = iTranferDir
                oNpc = oGame.m_ResMgr.CreateNpc(iScene, iNpc, dNpcInfo, self.GetLineIdx())
                if oNpc:
                    oNpc.Set('Transfer', dNextLevel)
                    cl_snetwar.GS2CAddTransferInfo(oGame, iScene, iNpc, dNextLevel, iDifficulty)
                    continue
                SendAlert('err', '战场%s 关卡%s NPC-%s创建失败' % (oGame.GetWarMgr().m_SID, oLevelNode.m_Level, iNpc))
            

    
    def CreateInitBuild(self):
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        oGame = self.m_LevelNode.m_Game
        iScene = self.m_LevelNode.m_Scene
        dObstacle = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, self.m_Name, 'lineob')
        tLineIdx = self.GetLineIdx()
        for _, dInfo in dObstacle.items():
            dMsgInfo = {
                'Scene': iScene,
                'Line': tLineIdx }
            dMsgInfo.update(dInfo)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_BEFORE_CREATEINITOBSTACLE, self.m_LevelNode.m_CtrlMgr, dMsgInfo)
            if 'Halt' in dMsgInfo:
                continue
            iObstacleSID = dInfo['SID']
            oGame.m_ResMgr.CreateBuild(iScene, iObstacleSID, dInfo, tLineIdx)
        
        lstBuild = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, self.m_Name, 'initbuild')
        for dInfo in lstBuild:
            iBuildSID = dInfo['SID']
            oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dInfo, tLineIdx)
        

    
    def CreateInitHookRopeNpc(self):
        oLevelNode = self.m_LevelNode
        oLevelCtrl = oLevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        iCurLevel = oLevelNode.m_Level
        dHookRopeConfig = oLevelConfData.GetLineConfig(iCurLevel, self.m_Name, 'hookropenpc')
        if not dHookRopeConfig:
            return None
        oGame = oLevelNode.m_Game
        iScene = oLevelNode.m_Scene
        tLineIdx = self.GetLineIdx()
        iFirstNpc = 0
        for sGroup in dHookRopeConfig:
            if len(dHookRopeConfig[sGroup]) != 2:
                SendAlert('err', '战场%s 关卡%s %s组 钩索配置个数不为2，请检查' % (oGame.GetWarMgr().m_SID, iCurLevel, sGroup))
                continue
            for dNpcInfo in dHookRopeConfig[sGroup]:
                oNpc = oGame.m_ResMgr.CreateNpc(iScene, dNpcInfo['SID'], dNpcInfo, tLineIdx)
                if not oNpc:
                    continue
                if iFirstNpc:
                    oFirstNpc = oGame.GetObject(iFirstNpc)
                    if oFirstNpc:
                        oNpc.BindTargetHookRopeNpc(oFirstNpc)
                        oFirstNpc.BindTargetHookRopeNpc(oNpc)
                    iFirstNpc = 0
                    continue
                iFirstNpc = oNpc.m_ID
            
        

    
    def DownSpawn(self, tAction, oTarget):
        for dAction in tAction:
            func = dAction['func']
            bNeedTarget = func == SPAWN_TRIGGERGATE
            if isinstance(func, int):
                func = linespawnaction.GetSpawnFunc(func)
            if not func:
                continue
            param = dAction['param']
            if bNeedTarget:
                func(self, param, oTarget)
                continue
            func(self, param)
        

    
    def GetCurScene(self):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        return oScene

    
    def GetTransferDir(self):
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        iLType = self.m_LevelNode.m_LevelType
        if iLType == LEVEL_TYPE_HIDE:
            return TRANSFER_DIRTO_MAIN
        if oLevelCtrl.CheckFinishWar():
            return TRANSFER_DIRTO_PASS
        if oLevelCtrl.CheckLayerEndLevel():
            return TRANSFER_DIRTO_LAYER
        return TRANSFER_DIRTO_NEXT

    
    def GetMonsterSpawnInfo(self):
        return self.m_MonsterCtrl.GetMonsterSpawnInfo()



def CreateLineList(oLevelNode, lstRoom):
    lstRoomInLevel = []
    for iIndexInLevel, lstLine in enumerate(lstRoom):
        lstLineInRoom = []
        for iIndexInRoom, sLine in enumerate(lstLine):
            oLine = CBaseLevelLine(oLevelNode, iIndexInLevel, iIndexInRoom, sLine)
            lstLineInRoom.append(oLine)
        
        lstRoomInLevel.append(lstLineInRoom)
    
    return lstRoomInLevel

