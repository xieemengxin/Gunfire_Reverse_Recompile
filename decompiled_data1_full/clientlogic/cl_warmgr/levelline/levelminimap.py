# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/levelminimap.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/levelminimap.pyc
# Source Generated with Decompyle++
# File: levelminimap.pyc (Python 3.6)

from cl_commondefines import GOALPOS_TYPE_HIGHLIGHT, GOALPOS_HIGHLIGHT, SCENE_EVT_SHAPE_RECTANGLE, GOALPOS_TYPE_UNHIGHLIGHT, TRIGGER_ROOMGOAL, GOALPOS_TYPE_COMMON, NWARRIOR_NPC_PASSBOX, GOALPOS_TYPE_PASSTRANSFER, MINMAPPPT_TYPE_NORMALTRANS, MINIMAPPT_TYPE_HIDETRANS, MINIMAPPT_OPER_SHOW, MINIMAPPT_OPER_HIDE, MINIMAPPT_TYPE_GOALPOS, MINIMAPPT_TYPE_PASSBOXGOALPOS, GOALPOS_TYPE_PASSBOXNPC, MINIMAPPT_SHOW_SHALLOW, INTERACT_STATUS_DONE, NWARRIOR_NPC_TRANSFER, MINIMAPPT_SHOW_HIGHLIGHT, TRANSFER_DIRTO_HIDE, TRANSFER_DIRTO_NULL, PLAYMODE_SURVIVOR, PLAYMODE_NEWSURVIVOR
from cl_only import WeakProxy
import cl_msgcenter
import cl_snetwar
import cl_math

class CSceneMiniMapMgr(object):
    
    def __init__(self, oLevelCtrl):
        self.m_LevelCtrl = oLevelCtrl
        self.m_Game = oLevelCtrl.m_Game
        self.m_SceneMiniMap = { }
        self.m_Level2Scene = { }
        self.Init()

    
    def Init(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, 'MiniMapLevelInit', -1, 0, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, 'MiniMapLevelFinish', -1, 0, 1)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelNodeGoal, 'MiniGameLevelGoal', -1, 0, 1)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStartFight, 'MiniGameStartFight', -1, 0, 1)
        self.m_Game.AddGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnEnterScene, 'MiniMapEnterScene')
        self.m_Game.AddGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, 'MiniMapNpcInteract')
        self.m_Game.AddGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_FINDHIDELEVEL, self.OnFindHideLevel, 'MiniMapFindHideLevel')
        self.m_Game.AddGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_REMOVENPC, self.OnNpcRemove, 'MiniMapNpcRemove')

    
    def Release(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, 'MiniMapLevelInit')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'MiniMapLevelFinish')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'MiniGameLevelGoal')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, 'MiniGameStartFight')
        self.m_Game.DoneGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'MiniMapEnterScene')
        self.m_Game.DoneGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, 'MiniMapNpcInteract')
        self.m_Game.DoneGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_FINDHIDELEVEL, 'MiniMapFindHideLevel')
        self.m_Game.DoneGlobalAttention(self.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_REMOVENPC, 'MiniMapNpcRemove')
        for _, oMiniMap in self.m_SceneMiniMap.items():
            oMiniMap.Release()
        
        self.m_SceneMiniMap = { }
        self.m_Level2Scene = { }
        self.m_LevelCtrl = None
        self.m_Game = None

    
    def OnLevelNodeInit(self, oWarMgr, dInfo):
        iScene = dInfo['Scene']
        iLevel = dInfo['LevelID']
        if iScene not in self.m_SceneMiniMap:
            oMiniMap = CSceneMiniMap(self, iLevel, iScene)
            self.m_SceneMiniMap[iScene] = oMiniMap
            self.m_Level2Scene[iLevel] = iScene

    
    def OnLevelNodeFinish(self, oWarMgr, dInfo):
        for _, oMiniMap in self.m_SceneMiniMap.items():
            oMiniMap.Release()
        
        self.m_SceneMiniMap = { }
        self.m_Level2Scene = { }

    
    def OnLevelNodeGoal(self, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        oMiniMap = self.GetMiniMap(iLevel)
        if not oMiniMap:
            return None
        iScene = self.m_Level2Scene[iLevel]
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        lstTransfer = oScene.GetObjectsByType('Transfer')
        lstPlayer = oScene.GetPlayers()
        for nid in lstTransfer:
            oNpc = self.m_Game.GetObject(nid)
            if not oNpc:
                continue
            if oNpc.m_TransferDir in (TRANSFER_DIRTO_NULL, TRANSFER_DIRTO_HIDE):
                continue
            for pid in lstPlayer:
                if oNpc.IsVisibleTo(pid):
                    break
            
            dData = {
                'Pos': oNpc.GetPos(),
                'ShowMode': MINIMAPPT_SHOW_HIGHLIGHT }
            oMiniMap.AddTranferPos(oNpc.m_ID, dData)
        

    
    def OnLevelStartFight(self, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        oMiniMap = self.GetMiniMap(iLevel)
        if oMiniMap:
            oMiniMap.SetStartFight()

    
    def OnEnterScene(self, oLevelCtrl, oHero, dInfo):
        iLevel = dInfo['LevelID']
        oMiniMap = self.GetMiniMap(iLevel)
        if oMiniMap:
            oMiniMap.EnterScene(oHero.m_PlayerID)

    
    def OnNpcInteract(self, oLevelCtrl, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_TRANSFER:
            return None
        iTransDir = oNpc.m_TransferDir
        if iTransDir != TRANSFER_DIRTO_HIDE:
            return None
        pid = dInfo['pid']
        iInteractStatus = oNpc.GetHeroInteractStatus(pid)
        if iInteractStatus != INTERACT_STATUS_DONE:
            return None
        iScene = oNpc.m_Scene
        if iScene not in self.m_SceneMiniMap:
            return None
        dData = {
            'Pos': oNpc.GetPos(),
            'ShowMode': MINIMAPPT_SHOW_SHALLOW }
        oMiniMap = self.m_SceneMiniMap[iScene]
        oMiniMap.AddHideTranferPos(pid, oNpc.m_ID, dData)

    
    def OnFindHideLevel(self, oLevelCtrl, oHero, dInfo):
        iNpc = dInfo['iNpc']
        oNpc = self.m_Game.GetObject(iNpc)
        oMiniMap = self.m_SceneMiniMap[oHero.m_Scene]
        lstPlayer = self.m_Game.GetRealPlayers()
        dData = {
            'Pos': oNpc.GetPos(),
            'ShowMode': MINIMAPPT_SHOW_HIGHLIGHT }
        for pid in lstPlayer:
            oMiniMap.AddHideTranferPos(pid, oNpc.m_ID, dData)
        

    
    def OnNpcRemove(self, oLevelCtrl, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_TRANSFER:
            return None
        iTransDir = oNpc.m_TransferDir
        if iTransDir != TRANSFER_DIRTO_HIDE:
            return None
        if oNpc.m_Scene not in self.m_SceneMiniMap:
            return None
        oMiniMap = self.m_SceneMiniMap[oNpc.m_Scene]
        lstPlayer = self.m_Game.GetRealPlayers()
        for pid in lstPlayer:
            oMiniMap.DelHideTranferPos(pid, oNpc.m_ID)
        

    
    def GetMiniMap(self, iLevel):
        if iLevel not in self.m_Level2Scene:
            return None
        iScene = self.m_Level2Scene[iLevel]
        return self.m_SceneMiniMap[iScene]



class CSceneMiniMap(object):
    
    def __init__(self, oMgr, iLevel, iScene):
        self.m_MiniMapMgr = WeakProxy(oMgr)
        self.m_Level = iLevel
        self.m_Scene = iScene
        self.m_GoalPos = { }
        self.m_Transfer = { }
        self.m_HideTransfer = { }
        self.m_PtID = 0
        self.m_StartFight = False
        self.m_LevelGoalPos = CLevelGoalPosMgr(self)

    
    def Release(self):
        self.m_LevelGoalPos.Release()
        self.m_GoalPos = { }
        self.m_Transfer = { }
        self.m_HideTransfer = { }
        self.m_MiniMapMgr = None

    
    def GetScenePlayers(self):
        oGame = self.m_MiniMapMgr.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return []
        lstPlayer = list(oScene.GetPlayers().keys())
        return lstPlayer

    
    def SetStartFight(self):
        self.m_StartFight = True
        lstPlayer = self.GetScenePlayers()
        for pid in lstPlayer:
            self.EnterScene(pid)
        

    
    def AddGoalPos(self, pid, nid, dData):
        tPos = dData['Pos']
        iShowMode = dData['ShowMode']
        iGoalPosType = dData['GoalPosType']
        dGoalPos = self.m_GoalPos.setdefault(pid, { })
        if nid not in dGoalPos:
            ptid = self.NewPtID()
            iType = MINIMAPPT_TYPE_PASSBOXGOALPOS if iGoalPosType == GOALPOS_TYPE_PASSBOXNPC else MINIMAPPT_TYPE_GOALPOS
            oPt = CMiniMapPt(ptid, iType, iShowMode, tPos)
            dGoalPos[nid] = oPt
        else:
            oPt = dGoalPos[nid]
            if oPt.GetShowMode() == iShowMode:
                return None
            oPt.Update(iShowMode)
        self.NetPtListInfo([
            oPt], MINIMAPPT_OPER_SHOW, [
            pid])

    
    def GetCurLevelGoal(self, pid):
        if pid in self.m_GoalPos:
            for idx in self.m_GoalPos[pid]:
                return self.m_LevelGoalPos.m_GoalPosInfo[idx]
            

    
    def DelGoalPos(self, pid, nid):
        if pid not in self.m_GoalPos:
            return None
        oPt = self.m_GoalPos[pid].pop(nid, None)
        if oPt:
            self.NetPtListInfo([
                oPt], MINIMAPPT_OPER_HIDE, [
                pid])

    
    def AddTranferPos(self, nid, dData):
        tPos = dData['Pos']
        iShowMode = dData['ShowMode']
        if nid not in self.m_Transfer:
            ptid = self.NewPtID()
            oPt = CMiniMapPt(ptid, MINMAPPPT_TYPE_NORMALTRANS, iShowMode, tPos)
            self.m_Transfer[nid] = oPt
        else:
            oPt = self.m_Transfer[nid]
            if oPt.GetShowMode() == iShowMode:
                return None
            oPt.Update(iShowMode)
        lstPlayer = self.GetScenePlayers()
        self.NetPtListInfo([
            oPt], MINIMAPPT_OPER_SHOW, lstPlayer)

    
    def DelTranferPos(self, nid, dData):
        if nid not in self.m_Transfer:
            return None
        oPt = self.m_Transfer[nid]
        self.m_Transfer.pop(nid)
        lstPlayer = self.GetScenePlayers()
        self.NetPtListInfo([
            oPt], MINIMAPPT_OPER_HIDE, lstPlayer)

    
    def AddHideTranferPos(self, pid, nid, dData):
        tPos = dData['Pos']
        iShowMode = dData['ShowMode']
        lstTransfer = self.m_HideTransfer.setdefault(pid, { })
        if nid not in lstTransfer:
            ptid = self.NewPtID()
            oPt = CMiniMapPt(ptid, MINIMAPPT_TYPE_HIDETRANS, iShowMode, tPos)
            lstTransfer[nid] = oPt
        else:
            oPt = lstTransfer[nid]
            if oPt.GetShowMode() == iShowMode:
                return None
            oPt.Update(iShowMode)
        self.NetPtListInfo([
            oPt], MINIMAPPT_OPER_SHOW, [
            pid])

    
    def DelHideTranferPos(self, pid, nid):
        if pid not in self.m_HideTransfer:
            return None
        lstTransfer = self.m_HideTransfer[pid]
        if nid not in lstTransfer:
            return None
        oPt = lstTransfer.pop(nid)
        self.NetPtListInfo([
            oPt], MINIMAPPT_OPER_HIDE, [
            pid])

    
    def NewPtID(self):
        self.m_PtID += 1
        if self.m_PtID > 32767:
            self.m_PtID = 1
        return self.m_PtID

    
    def NetPtListInfo(self, lstPt, iOperate, lstPlayer):
        if not lstPlayer or not lstPt:
            return None
        if not self.m_StartFight:
            return None
        lstPosInfo = []
        for pt in lstPt:
            lstPosInfo.append(pt.Desc())
        
        oGame = self.m_MiniMapMgr.m_Game
        cl_snetwar.GS2CUpdateMiniMapPos(oGame, self.m_Level, iOperate, lstPosInfo, lstPlayer)

    
    def EnterScene(self, pid):
        lstPt = []
        lstPt.extend(list(self.m_Transfer.values()))
        if pid in self.m_GoalPos:
            lstPt.extend(list(self.m_GoalPos[pid].values()))
        if pid in self.m_HideTransfer:
            lstPt.extend(list(self.m_HideTransfer[pid].values()))
        return self.NetPtListInfo(lstPt, MINIMAPPT_OPER_SHOW, [
            pid])



class CMiniMapPt(object):
    
    def __init__(self, ptid, iPtType, iShowMode, tPos):
        self.m_ID = ptid
        self.m_PtType = iPtType
        self.m_ShowMode = iShowMode
        self.m_Pos = tPos

    
    def Update(self, iShowMode):
        self.m_ShowMode = iShowMode

    
    def Desc(self):
        return (self.m_ID, self.m_PtType, self.m_ShowMode, self.m_Pos)

    
    def GetShowMode(self):
        return self.m_ShowMode



class CLevelGoalPosMgr(object):
    
    def __init__(self, oSceneMiniMap):
        self.m_SceneMiniMap = WeakProxy(oSceneMiniMap)
        self.m_Game = oSceneMiniMap.m_MiniMapMgr.m_Game
        self.m_GoalPosInfo = { }
        self.m_PlayerGoalPos = { }
        self.m_RoomPos = 0
        if self.m_Game.m_WarMgr.m_PlayMode not in (PLAYMODE_SURVIVOR, PLAYMODE_NEWSURVIVOR):
            self.Init()

    
    def Init(self):
        oLevelCtrl = self.GetLevelCtrl()
        oLevelConfData = oLevelCtrl.m_LevelConfData
        lstGoalPosInfo = oLevelConfData.GetLevelConfig(self.m_SceneMiniMap.m_Level, 'goalpos')
        if not lstGoalPosInfo:
            return None
        dPassBoxNpcConfig = self.GetCurPassBoxNpcConfig()
        iLen = len(lstGoalPosInfo)
        lstGoalPosInfo = sorted(lstGoalPosInfo, key = (lambda x: x['Index']))
        lstGoalPosIdx = []
        for dParam in lstGoalPosInfo:
            if dParam['Index'] == iLen and dPassBoxNpcConfig:
                idx = iLen
                dPassBox = {
                    'Type': GOALPOS_TYPE_PASSBOXNPC,
                    'Pos': (dPassBoxNpcConfig['Pos'][0], dPassBoxNpcConfig['Pos'][1] + 2, dPassBoxNpcConfig['Pos'][2]),
                    'Index': idx,
                    'Facing': dPassBoxNpcConfig['Facing'] }
                oGoal = CreateGoalPos(GOALPOS_TYPE_PASSBOXNPC, self, dPassBox)
                self.m_GoalPosInfo[idx] = oGoal
                lstGoalPosIdx.append(idx)
                idx = iLen + 1
                dPassTransfer = { }
                for k, v in dParam.items():
                    dPassTransfer[k] = v
                
                dPassTransfer['Index'] = idx
                dPassTransfer['Type'] = GOALPOS_TYPE_PASSTRANSFER
                oGoal = CreateGoalPos(GOALPOS_TYPE_PASSTRANSFER, self, dPassTransfer)
                self.m_GoalPosInfo[idx] = oGoal
                lstGoalPosIdx.append(idx)
                break
            iType = dParam['Type']
            oGoal = CreateGoalPos(iType, self, dParam)
            idx = oGoal.m_Index
            self.m_GoalPosInfo[idx] = oGoal
            lstGoalPosIdx.append(idx)
        
        self.m_CurIndex = lstGoalPosIdx[0]
        oWarMgr = self.m_Game.m_WarMgr
        oFirstGoal = self.m_GoalPosInfo[self.m_CurIndex]
        dData = {
            'Pos': oFirstGoal.m_Pos,
            'ShowMode': oFirstGoal.m_InitShowMode,
            'GoalPosType': oFirstGoal.m_Type }
        for iPlayer in oWarMgr.GetRoomPlayer():
            self.m_PlayerGoalPos[iPlayer] = list(lstGoalPosIdx)
            self.m_SceneMiniMap.AddGoalPos(iPlayer, self.m_CurIndex, dData)
        

    
    def Release(self):
        for _, oGoal in self.m_GoalPosInfo.items():
            oGoal.Release()
        
        self.m_GoalPosInfo = { }
        self.m_PlayerGoalPos = { }
        self.m_SceneMiniMap = None

    
    def GetCurScene(self):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_SceneMiniMap.m_Scene)
        return oScene

    
    def GetCurLevel(self):
        iLevel = self.m_SceneMiniMap.m_Level
        oLevelCtrl = self.GetLevelCtrl()
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        return oLevelNode

    
    def GetCurPassBoxNpcConfig(self):
        oLevelNode = self.GetCurLevel()
        oLineNode = oLevelNode.m_RoomList[-1][-1]
        oLevelCtrl = self.GetLevelCtrl()
        oGame = oLevelCtrl.m_Game
        oLevelConfData = oLevelCtrl.m_LevelConfData
        lstNpcConfig = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'scenenpc', 'npc')
        for dData in lstNpcConfig:
            clsData = oGame.m_WarData.GetNpcData(dData['SID'])
            if not clsData:
                continue
            if clsData.m_FightType == NWARRIOR_NPC_PASSBOX:
                return dData
        
        return { }

    
    def GetLevelCtrl(self):
        return self.m_SceneMiniMap.m_MiniMapMgr.m_LevelCtrl

    
    def SetGoalPosHighLight(self, pid, idx):
        oGoal = self.m_GoalPosInfo[idx]
        oGoal.m_InitShowMode = MINIMAPPT_SHOW_HIGHLIGHT
        dData = {
            'Pos': oGoal.m_Pos,
            'ShowMode': oGoal.m_InitShowMode,
            'GoalPosType': oGoal.m_Type }
        self.m_SceneMiniMap.AddGoalPos(pid, idx, dData)

    
    def SetGoalPosDestory(self, pid, idx):
        lstGoalPosIdx = self.m_PlayerGoalPos[pid]
        self.m_SceneMiniMap.DelGoalPos(pid, idx)
        lstGoalPosIdx.remove(idx)
        if lstGoalPosIdx:
            idx = lstGoalPosIdx[0]
            oNextGoal = self.m_GoalPosInfo[idx]
            dData = {
                'Pos': oNextGoal.m_Pos,
                'ShowMode': oNextGoal.m_InitShowMode,
                'GoalPosType': oNextGoal.m_Type }
            self.m_SceneMiniMap.AddGoalPos(pid, oNextGoal.m_Index, dData)



class CBaseGoalPos(object):
    m_InitShowMode = MINIMAPPT_SHOW_SHALLOW
    
    def __init__(self, oGoalPosMgr, dParam):
        self.m_GoalPosMgr = WeakProxy(oGoalPosMgr)
        self.m_Pos = dParam['Pos']
        self.m_Facing = dParam['Facing']
        self.m_Index = dParam['Index']
        self.m_Type = dParam['Type']
        self.Init(dParam)

    
    def Release(self):
        self.m_GoalPosMgr = None

    
    def Init(self, dParam):
        self.CreateHighLightRule(dParam)
        self.CreateDestroyRule(dParam)

    
    def CreateHighLightRule(self, dParam):
        pass

    
    def CreateDestroyRule(self, dParam):
        pass

    
    def ValidTrigger(self, pid):
        dGoalPos = self.m_GoalPosMgr.m_PlayerGoalPos
        if pid not in dGoalPos:
            return False
        lstGoalPosIndex = dGoalPos[pid]
        if not lstGoalPosIndex:
            return False
        return self.m_Index == lstGoalPosIndex[0]



class CCommonGoalPos(CBaseGoalPos):
    m_Type = GOALPOS_TYPE_COMMON
    
    def __init__(self, oGoalPosMgr, dParam):
        super(CCommonGoalPos, self).__init__(oGoalPosMgr, dParam)
        self.m_Event = 0

    
    def Release(self):
        oScene = self.m_GoalPosMgr.GetCurScene()
        if oScene:
            oScene.RemoveSceneEvent(self.m_Event)
        super(CCommonGoalPos, self).Release()

    
    def CreateDestroyRule(self, dParam):
        oLevelCtrl = self.m_GoalPosMgr.GetLevelCtrl()
        oScene = self.m_GoalPosMgr.GetCurScene()
        tPos = self.m_Pos
        tFace = self.m_Facing
        tSize = dParam['Size']
        tCenter = dParam['Center']
        fAngleY = cl_math.CalRotate2D(tFace)
        tOffset = cl_math.RotateAroundVector(tCenter, (0, 1, 0), fAngleY)
        tHalf = (tSize[0] / 2, tSize[1] / 2, tSize[2] / 2)
        tCenter = (tPos[0] + tOffset[0], tPos[1] + tOffset[1], tPos[2] + tOffset[2])
        self.m_Event = oScene.AddSceneEvent(oLevelCtrl, self.OnDestroy, None, SCENE_EVT_SHAPE_RECTANGLE, (tCenter, tHalf), {
            'Dir': tFace,
            'RoomPos': self.m_GoalPosMgr.m_RoomPos })

    
    def CreateHighLightRule(self, dParam):
        oLevelCtrl = self.m_GoalPosMgr.GetLevelCtrl()
        oLevelTrigger = oLevelCtrl.m_LevelTrigger
        oLevelNode = self.m_GoalPosMgr.GetCurLevel()
        iRoomPos = self.m_GoalPosMgr.m_RoomPos
        self.m_GoalPosMgr.m_RoomPos += 1
        dCondition = {
            'rule': TRIGGER_ROOMGOAL,
            'param': [
                oLevelNode.m_Level,
                iRoomPos] }
        oLevelTrigger.LevelAttention(self.OnHighLight, oLevelNode, dCondition)

    
    def OnDestroy(self, oListener, dMsgInfo):
        iHero = dMsgInfo['VID']
        if not self.m_GoalPosMgr:
            return None
        oHero = self.m_GoalPosMgr.m_Game.GetObject(iHero)
        if not oHero or not self.ValidTrigger(oHero.m_PlayerID):
            return None
        self.m_GoalPosMgr.SetGoalPosDestory(oHero.m_PlayerID, self.m_Index)

    
    def OnHighLight(self, oLevelCtrl):
        oWarMgr = self.m_GoalPosMgr.m_Game.m_WarMgr
        for pid in oWarMgr.GetRoomPlayer():
            if not self.ValidTrigger(pid):
                continue
            self.m_GoalPosMgr.SetGoalPosHighLight(pid, self.m_Index)
        



class CUnHighLightGoalPos(CCommonGoalPos):
    m_Type = GOALPOS_TYPE_UNHIGHLIGHT
    
    def CreateHighLightRule(self, dParam):
        pass

    
    def OnHighLight(self, oLevelCtrl):
        pass



class CHighLightGoalPos(CCommonGoalPos):
    m_InitShowMode = MINIMAPPT_SHOW_HIGHLIGHT
    m_Type = GOALPOS_HIGHLIGHT
    
    def CreateHighLightRule(self, dParam):
        pass

    
    def OnHighLight(self, oLevelCtrl):
        pass



class CPassBoxNpcGoalPos(CCommonGoalPos):
    m_Type = GOALPOS_TYPE_PASSBOXNPC
    
    def Release(self):
        oLevelCtrl = self.m_GoalPosMgr.GetLevelCtrl()
        self.m_GoalPosMgr.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, 'CPassBoxNpcGoalPos')
        super(CPassBoxNpcGoalPos, self).Release()

    
    def CreateDestroyRule(self, dParam):
        oLevelCtrl = self.m_GoalPosMgr.GetLevelCtrl()
        self.m_GoalPosMgr.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, 'CPassBoxNpcGoalPos')

    
    def OnNpcInteract(self, oLevelCtrl, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_PASSBOX:
            return None
        oScene = self.m_GoalPosMgr.GetCurScene()
        if not oScene or oScene.m_ID != oNpc.m_Scene:
            return None
        pid = dInfo['pid']
        iInteractStatus = oNpc.GetHeroInteractStatus(pid)
        if iInteractStatus != INTERACT_STATUS_DONE:
            return None
        oWarMgr = self.m_GoalPosMgr.m_Game.m_WarMgr
        lstHero = oWarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = self.m_GoalPosMgr.m_Game.GetObject(iHero)
            pid = oHero.m_PlayerID
            if pid not in self.m_GoalPosMgr.m_PlayerGoalPos:
                continue
            lstGoalPosIdx = self.m_GoalPosMgr.m_PlayerGoalPos[pid]
            if len(lstGoalPosIdx) != 2:
                idx = self.GetPassBoxIndex()
                if idx in lstGoalPosIdx:
                    lstGoalPosIdx.remove(idx)
                    continue
            dMsgInfo = {
                'VID': iHero }
            self.OnDestroy(oNpc, dMsgInfo)
        
        self.m_GoalPosMgr.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, 'CPassBoxNpcGoalPos')

    
    def GetPassBoxIndex(self):
        return len(self.m_GoalPosMgr.m_GoalPosInfo) - 1



class CPassTransferNpcGoalPos(CCommonGoalPos):
    m_Type = GOALPOS_TYPE_PASSTRANSFER
    
    def Release(self):
        oLevelCtrl = self.m_GoalPosMgr.GetLevelCtrl()
        self.m_GoalPosMgr.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, 'CPassTransferNpcGoalPos')
        super(CPassTransferNpcGoalPos, self).Release()

    
    def CreateHighLightRule(self, dParam):
        oLevelCtrl = self.m_GoalPosMgr.GetLevelCtrl()
        self.m_GoalPosMgr.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, 'CPassTransferNpcGoalPos')

    
    def OnNpcInteract(self, oLevelCtrl, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_PASSBOX:
            return None
        oScene = self.m_GoalPosMgr.GetCurScene()
        if not oScene or oScene.m_ID != oNpc.m_Scene:
            return None
        pid = dInfo['pid']
        iInteractStatus = oNpc.GetHeroInteractStatus(pid)
        if iInteractStatus != INTERACT_STATUS_DONE:
            return None
        self.OnHighLight(oLevelCtrl)
        self.m_GoalPosMgr.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnNpcInteract, 'CPassBoxNpcGoalPos')


g_GoalPosClass = {
    GOALPOS_TYPE_PASSTRANSFER: CPassTransferNpcGoalPos,
    GOALPOS_TYPE_PASSBOXNPC: CPassBoxNpcGoalPos,
    GOALPOS_TYPE_HIGHLIGHT: CHighLightGoalPos,
    GOALPOS_TYPE_UNHIGHLIGHT: CUnHighLightGoalPos,
    GOALPOS_TYPE_COMMON: CCommonGoalPos }

def CreateGoalPos(iType, oGoalPosMgr, dParam):
    if iType in g_GoalPosClass:
        cls = g_GoalPosClass[iType]
        return cls(oGoalPosMgr, dParam)

