# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/npcrefreshmgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/npcrefreshmgr.pyc
# Source Generated with Decompyle++
# File: npcrefreshmgr.pyc (Python 3.6)

from cl_commondefines import NPC_INTERVAL_REFRESH, NPC_PHASE_REFRESH, NPC_RESIDENT, SURVIVOR_NPC_SHOP, SURVIVOR_NPC_CRAFTSMAN, NPC_TYPE_SHOP, NPC_TYPE_CRAFTSMAN, NPCMGR_MOBILESURVIVOR, NPCMGR_SURVIVOR, NPC_NOENTITY_REFRESH, NWARRIOR_NPC_PHASESHOP, NWARRIOR_NPC_PHASESMITH, NWARRIOR_NPC_PHASEGOLDENCUP, NWARRIOR_NPC_EVENT, NWARRIOR_NPC_REFRESH, INTERACT_STATUS_DONE
from cl_only import SendAlert, ShufferList, Time2Frame, Functor, ChooseKey, GAME_FRAME
from cl_object.logging import SurvivorLog
import cllib.lib_flag
import cl_msgcenter
import cl_math
import cl_snetwar
import cl_notify
import cl_scene
NpcPosMap = {
    NPC_NOENTITY_REFRESH: 'intervalpos',
    NPC_RESIDENT: 'staypos',
    NPC_PHASE_REFRESH: 'supplypos',
    NPC_INTERVAL_REFRESH: 'intervalpos' }

def IntervalRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule):
    iStartTime = dRefreshRule['StartTime']
    iStartFrame = Time2Frame(iStartTime)
    if not iStartFrame:
        RealIntervalRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule)
    else:
        func = Functor(RealIntervalRefresh, oNpcRefreshMgr, dChooseRule, dRefreshRule)
        oNpcRefreshMgr.Npc_Remove_Call_Out('IntervalRefresh')
        oNpcRefreshMgr.Npc_Call_Out(func, iStartFrame, 'IntervalRefresh')


def RealIntervalRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule):
    if oNpcRefreshMgr.m_Survivor.m_CallFlag == 'SurvivorElement':
        oTarget = oNpcRefreshMgr.m_Survivor.GetMaxDamageTarget()
    else:
        lstHero = ShufferList(oNpcRefreshMgr.m_Game, oNpcRefreshMgr.m_Game.m_WarMgr.GetLiveHero())
        for iHero in lstHero:
            oHero = oNpcRefreshMgr.m_Game.GetObject(iHero)
            if not oHero:
                continue
            oTarget = oHero
        else:
            return None
    if not oTarget:
        oLevelCtrl = oNpcRefreshMgr.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        SendAlert('err', 'game:%d %s没有刷怪玩家无法刷新NPC' % (oNpcRefreshMgr.m_Game.m_ID, oLevelCtrl.m_CurNode.m_Level))
        return None
    vTarget = oTarget.GetPos()
    lstAvailablePos = GetAvailablePos(oNpcRefreshMgr, dRefreshRule['MinDistance'], dRefreshRule['MaxDistance'], vTarget, NPC_INTERVAL_REFRESH, [])
    dSecondaryPut = dRefreshRule['PutWeight']
    sType = 'IntervalRefresh'
    iDuration = dRefreshRule['Duration']
    dDuration = {
        'Duration': iDuration,
        'Type': sType } if iDuration else { }
    CreateSurvivorNpc(oNpcRefreshMgr, lstAvailablePos, dChooseRule, dSecondaryPut, dDuration, vTarget, sType, NPC_CHANGEPOS)


def PhaseRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule):
    iStartTime = dRefreshRule['StartTime']
    iStartFrame = Time2Frame(iStartTime)
    if not iStartFrame:
        RealPhaseRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule)
    else:
        func = Functor(RealPhaseRefresh, oNpcRefreshMgr, dChooseRule, dRefreshRule)
        oNpcRefreshMgr.Npc_Remove_Call_Out('PhaseRefresh')
        oNpcRefreshMgr.Npc_Call_Out(func, iStartFrame, 'PhaseRefresh')


def RealPhaseRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule):
    oTarget = oNpcRefreshMgr.m_Survivor.GetMaxDamageTarget()
    if not oTarget:
        oLevelCtrl = oNpcRefreshMgr.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        SendAlert('err', 'game:%d %s没有刷怪玩家无法刷新NPC' % (oNpcRefreshMgr.m_Game.m_ID, oLevelCtrl.m_CurNode.m_Level))
        return None
    vTarget = oTarget.GetPos()
    lstAvailablePos = GetAvailablePos(oNpcRefreshMgr, dRefreshRule['MinDistance'], dRefreshRule['MaxDistance'], vTarget, NPC_PHASE_REFRESH, [])
    dSecondaryPut = dRefreshRule['PutWeight']
    sType = 'IntervalRefresh'
    iDuration = dRefreshRule['Duration']
    dDuration = {
        'Duration': iDuration,
        'Type': sType } if iDuration else { }
    CreateSurvivorNpc(oNpcRefreshMgr, lstAvailablePos, dChooseRule, dSecondaryPut, dDuration, vTarget, sType, NPC_APPEAR)


def ResidentRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule, bFirst = True):
    oNpcRefreshMgr.Npc_Remove_Call_Out('ResidentRefresh')
    func = Functor(ResidentRefresh, oNpcRefreshMgr, dChooseRule, dRefreshRule, False)
    iFrame = Time2Frame(dRefreshRule['IntervalRefershTime'])
    oNpcRefreshMgr.Npc_Call_Out(func, iFrame, 'ResidentRefresh')
    oTarget = oNpcRefreshMgr.m_Survivor.GetMaxDamageTarget()
    if not oTarget:
        oLevelCtrl = oNpcRefreshMgr.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        SendAlert('err', 'game:%d %s没有刷怪玩家无法刷新NPC' % (oNpcRefreshMgr.m_Game.m_ID, oLevelCtrl.m_CurNode.m_Level))
        return None
    vTarget = oTarget.GetPos()
    lstAvailablePos = GetAvailablePos(oNpcRefreshMgr, dRefreshRule['MinDistance'], dRefreshRule['MaxDistance'], vTarget, NPC_RESIDENT, oNpcRefreshMgr.m_LastNpcPos)
    dSecondaryPut = dRefreshRule['PutWeight']
    iDuration = dRefreshRule['Duration']
    sType = 'ResidentRefresh'
    dDuration = {
        'Duration': iDuration,
        'Type': sType } if iDuration else { }
    iDialogue = NPC_APPEAR if bFirst else NPC_CHANGEPOS
    CreateSurvivorNpc(oNpcRefreshMgr, lstAvailablePos, dChooseRule, dSecondaryPut, dDuration, vTarget, sType, iDialogue)


def NoEntityRefresh(oNpcRefreshMgr, dChooseRule, dRefreshRule):
    lstAvailablePos = GetPosByType(oNpcRefreshMgr, NPC_NOENTITY_REFRESH)
    dSecondaryPut = dRefreshRule['PutWeight']
    sType = 'NoEntityRefresh'
    iDuration = dRefreshRule['Duration']
    dDuration = {
        'Duration': iDuration,
        'Type': sType } if iDuration else { }
    iRemoveOnFight = dRefreshRule['RemoveOnFight']
    CreateSurvivorNpc(oNpcRefreshMgr, lstAvailablePos, dChooseRule, dSecondaryPut, dDuration, None, sType, NPC_PHASEREWARD, iRemoveOnFight, iEffect = 0, iDelay = 0)


def CreateSurvivorNpc(oNpcRefreshMgr, lstAvailablePos, dChooseRule, dSecondaryPut, dDuration, vTarget, sType, iDialogue, iRemoveOnFight = 0, iEffect = 1, iDelay = 1):
    oGame = oNpcRefreshMgr.m_Game
    lstWaitRefreshNpc = []
    for dRule in dChooseRule.values():
        iPutNumber = dRule['PutNumber']
        dPutWeight = dRule['PutWeight'] if dRule['PutWeight'] else dSecondaryPut
        for _ in range(iPutNumber):
            iNpcSID = ChooseKey(oGame, dPutWeight)
            lstWaitRefreshNpc.append(iNpcSID)
        
    
    iNpcLen = len(lstWaitRefreshNpc)
    if not lstAvailablePos or iNpcLen > len(lstAvailablePos):
        if cllib.lib_flag.g_IsInternalRun:
            oLevelCtrl = oNpcRefreshMgr.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            SendAlert('err', 'game:%d %s没有刷足够的位置刷新NPC %s %s %s %s %s %s' % (oNpcRefreshMgr.m_Game.m_ID, oLevelCtrl.m_CurNode.m_Level, sType, lstWaitRefreshNpc, lstAvailablePos, vTarget, oNpcRefreshMgr.m_UsedPos, oNpcRefreshMgr.m_Survivor.m_Phase))
        if sType == 'ResidentRefresh':
            for tPos in oNpcRefreshMgr.m_LastNpcPos:
                if tPos not in lstAvailablePos:
                    lstAvailablePos.append(tPos)
            
        if not lstAvailablePos:
            return None
    cl_notify.SendCommonNotify(oNpcRefreshMgr.m_Game, oNpcRefreshMgr.m_Game.GetRealPlayers(), iDialogue, { })
    lstAvailablePos = ShufferList(oGame, lstAvailablePos)
    lstNpcConfig = []
    lstEffectID = []
    lstUsePos = []
    lstUsedPos = []
    oScene = oGame.m_SceneMgr.GetScene(oNpcRefreshMgr.m_Scene)
    if not oScene:
        return None
    for idx, (vPos, vFacing) in enumerate(lstAvailablePos):
        iNpcSID = lstWaitRefreshNpc[idx]
        dNpcConfig = { }
        dNpcConfig['Pos'] = vPos
        dNpcConfig['Facing'] = vFacing
        dNpcConfig['SID'] = iNpcSID
        dNpcConfig['RemoveOnFight'] = iRemoveOnFight
        lstNpcConfig.append(dNpcConfig)
        lstUsePos.append((vPos, vFacing))
        lstUsedPos.append(vPos)
        if iEffect:
            iEffectID = oGame.NewNoSceneObjID()
            lstEffectID.append(iEffectID)
            cl_snetwar.GS2CAddEffect(oGame, oNpcRefreshMgr.m_Scene, iEffectID, NPC_APPEAR_EFFECT, vPos, oScene.GetPlayers())
        if idx == iNpcLen - 1:
            break
    
    if sType == 'ResidentRefresh':
        oNpcRefreshMgr.m_LastNpcPos = lstUsePos
    oNpcRefreshMgr.m_UsedPos.extend(lstUsedPos)
    if iDelay:
        func = Functor(DelayCreateSurvivorNpc, oNpcRefreshMgr, lstNpcConfig, dDuration, lstEffectID)
        sCallFlag = 'DelayCreateSurvivorNpc' + sType
        oNpcRefreshMgr.Npc_Remove_Call_Out(sCallFlag)
        oNpcRefreshMgr.Npc_Call_Out(func, REMOVE_EFFECT_FRAME, sCallFlag)
    else:
        DelayCreateSurvivorNpc(oNpcRefreshMgr, lstNpcConfig, dDuration, lstEffectID)


def DelayCreateSurvivorNpc(oNpcRefreshMgr, lstNpcConfig, dDuration, lstEffectID):
    oNpcRefreshMgr.CreateWaitRefreshNpc(lstNpcConfig, dDuration)
    oNpcRefreshMgr.DelayRemoveEffect(lstEffectID)


def GetAvailablePos(oNpcRefreshMgr, iMinDistance, iMaxDistance, vTarget, iType, lstExcludePos):
    sPosKey = NpcPosMap[iType]
    if iType == NPC_PHASE_REFRESH:
        dPosInfo = oNpcRefreshMgr.m_NpcPos[sPosKey]
        for lstPos in dPosInfo.values():
            bFlag = True
            for tPos in lstPos:
                if tPos[0] in oNpcRefreshMgr.m_UsedPos:
                    bFlag = False
                    break
            
            if not bFlag:
                continue
            for tPos in lstPos:
                vPos = tPos[0]
                fDistance = cl_math.CalDistance(vPos, vTarget)
                if fDistance >= iMinDistance and fDistance <= iMaxDistance:
                    return lstPos
            
        
    else:
        lstAvailablePos = []
        lstPosInfo = oNpcRefreshMgr.m_NpcPos[sPosKey]
        for vPos, vFacing in lstPosInfo:
            if (vPos, vFacing) in lstExcludePos:
                continue
            if vPos in oNpcRefreshMgr.m_UsedPos:
                continue
            fDistance = cl_math.CalDistance(vPos, vTarget)
            if fDistance >= iMinDistance and fDistance <= iMaxDistance:
                lstAvailablePos.append((vPos, vFacing))
        
        return lstAvailablePos
    return []


def GetPosByType(oNpcRefreshMgr, iType):
    sPosKey = NpcPosMap[iType]
    lstPosInfo = oNpcRefreshMgr.m_NpcPos[sPosKey]
    return lstPosInfo

g_RefreshFunc = {
    NPC_NOENTITY_REFRESH: NoEntityRefresh,
    NPC_RESIDENT: ResidentRefresh,
    NPC_PHASE_REFRESH: PhaseRefresh,
    NPC_INTERVAL_REFRESH: IntervalRefresh }

def GetSpawnFunc(idx):
    if idx in g_RefreshFunc:
        return g_RefreshFunc[idx]

NPC_APPEAR = 9334
NPC_DISAPPEAR = 9335
NPC_CHANGEPOS = 9336
NPC_PHASEREWARD = 17158
NPC_APPEAR_EFFECT = 1028
NPC_DISAPPEAR_EFFECT = 1029
REMOVE_EFFECT_FRAME = 50

class CNpcRefreshMgr(object):
    m_PosType = ('intervalpos', 'supplypos', 'staypos')
    
    def __init__(self, oSurvivorElement, oData, iType):
        self.m_CallFlag = 'NpcRefresh'
        self.m_Type = iType
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_NpcConfig = oData.m_NpcConfig
        self.m_SID = 0
        self.m_Scene = 0
        self.m_NpcPos = { }
        self.m_LastNpcPos = []
        self.m_UsedPos = []
        self.m_FightRemove = []
        self.m_NpcCustomData = { }

    
    def Release(self):
        self.m_Survivor = None
        self.m_NpcConfig = { }
        self.m_LastNpcPos = []
        self.m_UsedPos = []
        self.m_Game = None
        self.m_NpcCustomData = { }

    
    def SetNpcCustomData(self, sKey, value):
        self.m_NpcCustomData[sKey] = value

    
    def PopNpcCustomData(self, sKey, default = None):
        return self.m_NpcCustomData.pop(sKey, default)

    
    def InitNpcPos(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        self.m_Scene = oLevelCtrl.m_CurNode.m_Scene
        oLevelConfData = oLevelCtrl.m_LevelConfData
        for sPosType in self.m_PosType:
            dPosInfo = oLevelConfData.GetMapConfig(oLevelCtrl.m_CurNode.m_Level, sPosType)
            if sPosType == 'supplypos':
                self.m_NpcPos[sPosType] = { }
                for dPos in dPosInfo.values():
                    dTempPos = { }
                    for iGroup, lstPos in dPos.items():
                        lstTempPos = []
                        for dPosInfo in lstPos:
                            lstTempPos.append((dPosInfo['Pos'], dPosInfo['Facing']))
                        
                        dTempPos[iGroup] = lstTempPos
                    
                    self.m_NpcPos[sPosType].update(dTempPos)
                
            lstTempPos = []
            for lstPos in dPosInfo.values():
                for dPosInfo in lstPos:
                    lstTempPos.append((dPosInfo['Pos'], dPosInfo['Facing']))
                
            
            self.m_NpcPos[sPosType] = lstTempPos
        

    
    def TryNpcRefresh(self, iIntervalStart):
        for iNpcRefreshType in self.m_NpcConfig[self.m_SID]:
            if self.m_Survivor.m_Phase not in self.m_NpcConfig[self.m_SID][iNpcRefreshType]['RefreshRule']:
                continue
            func = GetSpawnFunc(iNpcRefreshType)
            if not func:
                continue
            dRefreshRule = self.m_NpcConfig[self.m_SID][iNpcRefreshType]['RefreshRule'][self.m_Survivor.m_Phase]
            iPhaseIntervalStart = dRefreshRule['PhaseIntervalStart']
            if iIntervalStart ^ iPhaseIntervalStart:
                continue
            lstRemoveNpcType = dRefreshRule['RemoveNpcType']
            self.RemoveNpcByType(lstRemoveNpcType)
            iClearMonster = dRefreshRule['ClearMonster'] if 'ClearMonster' in dRefreshRule else 0
            if iClearMonster:
                self.m_Survivor.SceneMonsterAllDie()
            func(self, self.m_NpcConfig[self.m_SID][iNpcRefreshType]['ChooseRule'], dRefreshRule)
        

    
    def RemoveNpcOnFight(self):
        if not self.m_FightRemove:
            return None
        lstFightRemove = self.m_FightRemove
        self.m_FightRemove = []
        self.RemoveNpcList(lstFightRemove)

    
    def CreateWaitRefreshNpc(self, lstNpcConfig, dDuration):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        lstNpc = []
        lstFightRemove = []
        SurvivorLog.Debug('game:%d %s refreshnpc:%s %s' % (oGame.m_ID, oLevelCtrl.m_CurNode.m_Level, lstNpcConfig, self.m_UsedPos))
        for dNpcInfo in lstNpcConfig:
            iNpcSID = dNpcInfo['SID']
            dMsgInfo = {
                'NPC': iNpcSID,
                'LevelNode': oLevelCtrl.m_CurNode,
                'NPCInfo': dNpcInfo,
                'Scene': self.m_Scene }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelCtrl, dMsgInfo)
            if not dMsgInfo['NPC']:
                continue
            oNpc = oGame.m_ResMgr.CreateNpc(self.m_Scene, dMsgInfo['NPC'], dNpcInfo, self.m_Survivor.m_CurLine.GetLineIdx())
            lstNpc.append(oNpc.m_ID)
            if 'RemoveOnFight' in dNpcInfo and dNpcInfo['RemoveOnFight']:
                lstFightRemove.append(oNpc.m_ID)
        
        if dDuration:
            iFrame = Time2Frame(dDuration['Duration'])
            sType = dDuration['Type']
            iCurFrame = oGame.GetFrameNum()
            sFlag = sType + str(iCurFrame)
            func = Functor(self.RemoveNpcByFlag, lstNpc, sFlag, sType)
            self.Npc_Call_Out(func, iFrame, sFlag)
        self.m_FightRemove.extend(lstFightRemove)

    
    def RemoveNpcByFlag(self, lstNpc, sFlag, sType):
        self.Npc_Remove_Call_Out(sFlag)
        oGame = self.m_Game
        lstEffectID = []
        for iNpcID in lstNpc:
            oNpc = oGame.GetObject(iNpcID)
            if not oNpc:
                continue
            vPos = oNpc.GetPos()
            self.ClearUsedPos(vPos)
            iEffectID = self.AddNpcEffect(oNpc)
            if iEffectID:
                lstEffectID.append(iEffectID)
            oNpc.Remove('TimeOver')
        
        if sType != 'ResidentRefresh':
            cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), NPC_DISAPPEAR, { })
        if lstEffectID:
            func = Functor(self.DelayRemoveEffect, lstEffectID)
            self.Npc_Call_Out(func, REMOVE_EFFECT_FRAME, sFlag)

    
    def DelayRemoveEffect(self, lstEffectID, dPlayer = None):
        for iEffectID in lstEffectID:
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
            if not dPlayer:
                dPlayer = oScene.GetPlayers()
            cl_snetwar.GS2CDeleteEffect(self.m_Game, self.m_Scene, iEffectID, dPlayer)
        

    
    def RemoveNpcByType(self, lstNpcType):
        oGame = self.m_Game
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        lstNPC = oScene.GetObjectsByType('NPC')
        lstEffectID = []
        for iNPCID in lstNPC:
            oNpc = oGame.GetObject(iNPCID)
            if oNpc and oNpc.m_FightType in lstNpcType:
                vPos = oNpc.GetPos()
                self.ClearUsedPos(vPos)
                iEffectID = self.AddNpcEffect(oNpc)
                if iEffectID:
                    lstEffectID.append(iEffectID)
                oNpc.Remove('ClearByType')
        
        if lstEffectID:
            func = Functor(self.DelayRemoveEffect, lstEffectID)
            self.Npc_Call_Out(func, REMOVE_EFFECT_FRAME, 'RemoveNpcByType')

    
    def RemoveNpcList(self, lstNPC):
        oGame = self.m_Game
        lstEffectID = []
        for iNPCID in lstNPC:
            oNpc = oGame.GetObject(iNPCID)
            if not oNpc:
                continue
            vPos = oNpc.GetPos()
            self.ClearUsedPos(vPos)
            iEffectID = self.AddNpcEffect(oNpc)
            if iEffectID:
                lstEffectID.append(iEffectID)
            oNpc.Remove('ClearByList')
        
        if lstEffectID:
            func = Functor(self.DelayRemoveEffect, lstEffectID)
            self.Npc_Call_Out(func, REMOVE_EFFECT_FRAME, 'ClearByList')

    
    def AddNpcEffect(self, oNpc, dPlayer = None):
        if oNpc.m_FightType in [
            NWARRIOR_NPC_PHASESHOP,
            NWARRIOR_NPC_PHASESMITH,
            NWARRIOR_NPC_PHASEGOLDENCUP]:
            return 0
        oGame = self.m_Game
        vPos = oNpc.GetPos()
        iEffectID = oGame.NewNoSceneObjID()
        if not dPlayer:
            oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
            dPlayer = oScene.GetPlayers()
        cl_snetwar.GS2CAddEffect(oGame, self.m_Scene, iEffectID, NPC_DISAPPEAR_EFFECT, vPos, dPlayer)
        return iEffectID

    
    def ClearUsedPos(self, vPos):
        vWaitRemove = None
        for vUesdPos in self.m_UsedPos:
            if cl_math.CalDistance(vPos, vUesdPos) < 0.1:
                vWaitRemove = vUesdPos
                break
        
        if vWaitRemove:
            self.m_UsedPos.remove(vWaitRemove)

    
    def SpawnTransferNpc(self, lstNpc):
        if self.m_Survivor.m_Phase > self.m_Survivor.m_MaxPhase:
            return None
        lstTransferNpc = [
            SURVIVOR_NPC_SHOP,
            SURVIVOR_NPC_CRAFTSMAN]
        for iNpcRefreshType in self.m_NpcConfig[self.m_SID]:
            if self.m_Survivor.m_Phase not in self.m_NpcConfig[self.m_SID][iNpcRefreshType]['RefreshRule']:
                continue
            for iType in self.m_NpcConfig[self.m_SID][iNpcRefreshType]['ChooseRule']:
                if iType == NPC_TYPE_SHOP:
                    lstTransferNpc.remove(SURVIVOR_NPC_SHOP)
                    continue
                if iType == NPC_TYPE_CRAFTSMAN:
                    lstTransferNpc.remove(SURVIVOR_NPC_CRAFTSMAN)
            
        
        if not lstTransferNpc:
            return None
        lstNpcConfig = []
        for dNpcInfo in lstNpc:
            if dNpcInfo['SID'] not in lstTransferNpc:
                continue
            lstNpcConfig.append(dNpcInfo)
        
        if lstNpcConfig:
            self.CreateWaitRefreshNpc(lstNpcConfig, { })

    
    def TryRemoveEventNpc(self):
        oGame = self.m_Game
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        lstNPC = oScene.GetObjectsByType('NPC')
        lstEffectID = []
        for iNPCID in lstNPC:
            dPlayer = { }
            oNpc = oGame.GetObject(iNPCID)
            iRemove = 1
            if oNpc and oNpc.m_FightType in (NWARRIOR_NPC_EVENT, NWARRIOR_NPC_REFRESH):
                for iHero in oGame.m_WarMgr.GetRoomHero():
                    iVisible = 1
                    oHero = oGame.GetObject(iHero)
                    if not oHero:
                        continue
                    if oNpc.m_FightType == NWARRIOR_NPC_REFRESH:
                        iInteractStatus = oNpc.GetHeroInteractStatus(oHero.m_PlayerID)
                        if iInteractStatus == INTERACT_STATUS_DONE and oHero.m_ID not in oNpc.m_Reward:
                            iVisible = 0
                        elif oNpc.m_FightType == NWARRIOR_NPC_EVENT:
                            iCurStage = oNpc.GetCurStage(oHero)
                            if iCurStage == len(oNpc.m_Event):
                                iVisible = 0
                    if not None:
                        dPlayer[oHero.m_PlayerID] = 1
                        oNpc.m_VisiblePlayer[oHero.m_PlayerID] = 0
                        continue
                    oNpc.m_VisiblePlayer[oHero.m_PlayerID] = 1
                    iRemove = 0
                
            if dPlayer:
                cl_scene.GS2CMapDel(oNpc, dPlayer)
                iEffectID = self.AddNpcEffect(oNpc, dPlayer)
                if iEffectID:
                    lstEffectID.append(iEffectID)
            if iRemove:
                vPos = oNpc.GetPos()
                self.ClearUsedPos(vPos)
                func = Functor(oNpc.Remove, 'RemoveEventNpc')
                oNpc.Call_Out(func, GAME_FRAME * 10, 'RemoveEventNpc' + str(oNpc.m_ID))
        
        if lstEffectID:
            func = Functor(self.DelayRemoveEffect, lstEffectID)
            self.Npc_Call_Out(func, REMOVE_EFFECT_FRAME, 'RemoveEventNpc')

    
    def Npc_Call_Out(self, func, iDelay, sFlag):
        if self.m_Type == NPCMGR_SURVIVOR:
            self.m_Survivor.Call_Out_Suspendable(func, iDelay, sFlag)
        elif self.m_Type == NPCMGR_MOBILESURVIVOR:
            self.m_Survivor.Call_Out(func, iDelay, sFlag)
        else:
            SendAlert('err', 'game:%d 定时器类型错误%s' % (self.m_Game.m_ID, self.m_Type))

    
    def Npc_Remove_Call_Out(self, sFlag):
        if self.m_Type == NPCMGR_SURVIVOR:
            self.m_Survivor.Remove_Call_Out_Suspendable(sFlag)
        elif self.m_Type == NPCMGR_MOBILESURVIVOR:
            self.m_Survivor.Remove_Call_Out(sFlag)
        else:
            SendAlert('err', 'game:%d 定时器类型错误%s' % (self.m_Game.m_ID, self.m_Type))



def NewNpcRefreshMgr(oSurvivorElement, oData, iType):
    oNpcRefreshMgr = CNpcRefreshMgr(oSurvivorElement, oData, iType)
    return oNpcRefreshMgr

