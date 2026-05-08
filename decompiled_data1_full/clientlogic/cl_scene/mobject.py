# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_scene/mobject.pyc
# RelativePath: clientlogic/cl_scene/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import SCENE_EVT_SHAPE_RECTANGLE, SCENE_EVT_SHAPE_SPHERE, PLAYMODE_ROGUELIKE
from cl_scene.scenepreload import CScenePreLoad
from cl_object.logging import SceneLog
from cl_commondefines import MODEL_TYPE_BOX, MODEL_TYPE_SPHERE
from cl_only import PY_FLAG_DEAD
import C_frscene
import cllib.lib_flag
import cllib.lib_load
import cl_msgcenter
import cl_betree
import cl_modeldefine
import cl_engphyobj

class CSceneEvtManage(object):
    
    def __init__(self, oGame, iScene):
        self.m_EventList = { }
        self.m_BindEvent = { }
        self.m_Scene = iScene
        self.m_Game = oGame

    
    def BindCBFunc(self, oOwner, iEvent, enterfunc, leavefunc, sKey):
        dEvent = self.m_BindEvent.setdefault(iEvent, { })
        dEvent[sKey] = {
            'owner': oOwner.m_ID,
            'func': (enterfunc, leavefunc) }

    
    def UnBindCBFunc(self, iEvent, sKey):
        if iEvent not in self.m_BindEvent:
            return None
        if sKey in self.m_BindEvent[iEvent]:
            self.m_BindEvent[iEvent].pop(sKey)
            if not self.m_BindEvent[iEvent]:
                self.m_BindEvent.pop(iEvent)

    
    def AddCBFunc(self, oOwner, enterfunc, leavefunc, iShape, lstArgs, dData, bExcludeDead):
        if iShape == SCENE_EVT_SHAPE_RECTANGLE:
            (vPos, vHalfExtent) = lstArgs
            dShapeInfo = {
                'Shape': MODEL_TYPE_BOX,
                'HalfExt': vHalfExtent }
        elif iShape == SCENE_EVT_SHAPE_SPHERE:
            (vPos, fRadius) = lstArgs
            dShapeInfo = {
                'Shape': MODEL_TYPE_SPHERE,
                'Radius': fRadius }
        else:
            return 0
        oEvent = cl_engphyobj.CreateDynamicEventObject(self.m_Game, dShapeInfo)
        if not oEvent:
            return 0
        iSceneEvent = oEvent.m_ID
        dInfo = { }
        dInfo['owner'] = oOwner.m_ID
        dInfo['func'] = (enterfunc, leavefunc)
        dInfo['data'] = dData
        dInfo['object'] = set()
        dInfo['exdead'] = bExcludeDead
        self.m_EventList[iSceneEvent] = dInfo
        oEvent.SetTriggerCallback(self.OnTrigger)
        oEvent.Goto(self.m_Scene, vPos, tFace = dData.get('Dir'))
        return iSceneEvent

    
    def RemoveCBFunc(self, iSceneEvent):
        if iSceneEvent not in self.m_EventList:
            return None
        dInfo = self.m_EventList.pop(iSceneEvent)
        lstTarget = list(dInfo['object'])
        for iTarget in lstTarget:
            oTarget = self.m_Game.GetObject(iTarget)
            if not oTarget:
                continue
            self.OnTrigger(iSceneEvent, oTarget, 1)
        
        oEvent = self.m_Game.GetObject(iSceneEvent)
        if oEvent:
            oEvent.Remove('RemoveCBFunc')

    
    def OnTrigger(self, iSceneEvent, oTarget, iLeave):
        if iSceneEvent not in self.m_EventList:
            return None
        dInfo = self.m_EventList[iSceneEvent]
        iTarget = oTarget.m_ID
        if dInfo['exdead'] and not self.m_Game.GetObject(iTarget, PY_FLAG_DEAD):
            return None
        dData = dInfo['data']
        if 'RoomPos' in dData:
            oLevelCtrl = self.m_Game.GetObject(dInfo['owner'])
            dMsgInfo = {
                'VID': oTarget.m_ID,
                'Event': iSceneEvent,
                'Scene': self.m_Scene,
                'RoomPos': dData['RoomPos'] }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_LEVELROOMDOORTRIGGER, oLevelCtrl, dMsgInfo)
        oListener = self.m_Game.GetObject(dInfo['owner'])
        (enterfunc, leavefunc) = dInfo['func']
        setObject = dInfo['object']
        if iLeave:
            func = leavefunc
            if iTarget in setObject:
                setObject.remove(iTarget)
            else:
                func = enterfunc
                setObject.add(iTarget)
        dData = {
            'VID': None.m_ID,
            'Event': iSceneEvent,
            'Scene': self.m_Scene }
        dData.update(dInfo['data'])
        if func:
            func(oListener, dData)

    
    def OnTriggerStatic(self, iSceneEvent, oTarget, iLeave):
        if iSceneEvent not in self.m_BindEvent:
            return None
        dEvent = self.m_BindEvent[iSceneEvent]
        for dInfo in list(dEvent.values()):
            oListener = self.m_Game.GetObject(dInfo['owner'])
            (enterfunc, leavefunc) = dInfo['func']
            if iLeave:
                func = leavefunc
            else:
                func = enterfunc
            dData = {
                'VID': oTarget.m_ID,
                'Event': iSceneEvent,
                'Scene': self.m_Scene }
            if func:
                func(oListener, dData)
        

    
    def Release(self):
        for iSceneEvent in list(self.m_EventList):
            self.RemoveCBFunc(iSceneEvent)
        
        self.m_EventList = { }
        self.m_BindEvent = { }
        self.m_Scene = 0
        self.m_Game = None



class CVirtualScene(object):
    
    def __init__(self, oGame, iMap, iLevel, dParam):
        self.m_ID = -1
        self.m_SID = iMap
        self.m_Game = oGame
        self.m_Map = iMap
        self.m_Level = iLevel
        self.m_SceneEvtMgr = None
        self.m_Players = { }
        self.m_Heros = { }
        self.m_Objects = { }
        self.m_MonsterEnemy = []
        self.m_SceneData = None
        self.m_SceneParam = dParam
        self.m_BoundMax = (10000, 10000, 10000)
        self.m_BoundMin = (-10000, -10000, -10000)
        self.m_ScenePreLoad = CScenePreLoad(oGame)
        self.m_SceneLoad = False
        self.m_CustomData = { }
        self.m_ObstacleCount = 0
        self.m_MaxObstacleCount = 0

    
    def SID(self):
        return self.m_SID

    
    def Map(self):
        return self.m_Map

    
    def OnLoad(self):
        iAsyncload = cllib.lib_flag.g_OpenAsyncLoad
        if self.m_Game.m_WarMgr.m_PlayMode in (PLAYMODE_ROGUELIKE,):
            lstNavArea = list(self.m_SceneParam.get('Areas', []))
            if 99 in lstNavArea:
                lstNavArea.remove(99)
            lstNavArea.extend([ x + 1000 for x in lstNavArea ])
        else:
            lstNavArea = []
        self.m_SceneParam['NavAreas'] = lstNavArea
        self.m_ID = self.m_Game.Scene_Load(-1, self.m_Map, iAsyncload, cl_modeldefine.g_MaxNavMeshRadius, self.m_SceneParam)
        if self.m_ID == -1:
            SceneLog.Raise('Map%d Level%d CreateScene Fail' % (self.m_Map, self.m_Level))
        self.m_SceneEvtMgr = CSceneEvtManage(self.m_Game, self.m_ID)
        self.m_SceneData = cl_betree.NewAISceneData(self.m_Game, self.m_ID)
        if not iAsyncload:
            (self.m_BoundMax, self.m_BoundMin) = self.m_Game.Scene_GetSize(self.m_ID)
            self.m_SceneLoad = True
            if cllib.lib_flag.g_AutoDelMapRes:
                cllib.lib_load.ClearResourceTest()

    
    def UnLoad(self):
        if self.m_MaxObstacleCount > 127:
            if cllib.lib_flag.g_IsInternalRun:
                SceneLog.Alert('%d-%d obstacle count:%d' % (self.m_Map, self.m_Level, self.m_MaxObstacleCount))
            else:
                SceneLog.Info('%d-%d obstacle count:%d' % (self.m_Map, self.m_Level, self.m_MaxObstacleCount))
        self.HaltSkill()
        self.m_ScenePreLoad.Release()
        self.m_SceneEvtMgr.Release()
        self.ClearItem()
        self.m_SceneData.Release()
        self.m_Game.Scene_Delete(self.m_ID)
        if cllib.lib_flag.g_AutoDelMapRes:
            C_frscene.ClearSceneRes(self.m_Map)
        self.m_Game = None

    
    def Enter(self, obj):
        sType = obj.Type()
        if sType in self.m_Objects:
            self.m_Objects[sType][obj.m_ID] = 1
        else:
            self.m_Objects[sType] = {
                obj.m_ID: 1 }
        if obj.m_NavObstacle:
            self.m_ObstacleCount += 1
            if self.m_ObstacleCount > self.m_MaxObstacleCount:
                self.m_MaxObstacleCount = self.m_ObstacleCount

    
    def Leave(self, obj):
        sType = obj.Type()
        if sType in self.m_Objects and obj.m_ID in self.m_Objects[sType]:
            self.m_Objects[sType].pop(obj.m_ID)
        if obj.m_NavObstacle:
            self.m_ObstacleCount -= 1

    
    def GetObjectsByType(self, sType):
        if sType not in self.m_Objects:
            return []
        return list(self.m_Objects[sType])

    
    def GetObjectsByTypes(self, lstType):
        lstObject = []
        for sType in lstType:
            if sType not in self.m_Objects:
                continue
            lstObject.extend(list(self.m_Objects[sType]))
        
        return lstObject

    
    def ClearItem(self):
        for oItem in self.m_Game.Scene_GetObjects(self.m_ID):
            oItem.Remove('SC.ClearItem')
        

    
    def AddPlayer(self, pid, iHero):
        self.m_Players[pid] = 1
        self.m_Heros[iHero] = 1
        if iHero not in self.m_MonsterEnemy:
            self.m_MonsterEnemy.append(iHero)

    
    def DelPlayer(self, pid, iHero):
        if pid in self.m_Players:
            self.m_Players.pop(pid)
        if iHero in self.m_Heros:
            self.m_Heros.pop(iHero)
        if iHero in self.m_MonsterEnemy:
            self.m_MonsterEnemy.remove(iHero)

    
    def AddMonsterEnemy(self, iTarget):
        if iTarget not in self.m_MonsterEnemy:
            self.m_MonsterEnemy.append(iTarget)

    
    def DelMonsterEnemy(self, iTarget):
        if iTarget in self.m_MonsterEnemy:
            self.m_MonsterEnemy.remove(iTarget)

    
    def GetPlayers(self):
        return self.m_Players

    
    def GetHeros(self):
        return self.m_Heros

    
    def GetHerosExceptAI(self):
        dHeroExcAI = { }
        dSceneHero = self.m_Heros
        lstAIHero = self.m_Game.m_WarMgr.GetAllAIHero()
        for iHero in dSceneHero:
            if iHero not in lstAIHero:
                dHeroExcAI[iHero] = 1
        
        return dHeroExcAI

    
    def AddSceneEvent(self, oOwner, enterfunc, leavefunc, iShape, lstArgs, dData, bExcludeDead = True):
        return self.m_SceneEvtMgr.AddCBFunc(oOwner, enterfunc, leavefunc, iShape, lstArgs, dData, bExcludeDead)

    
    def RemoveSceneEvent(self, iSceneEvt):
        self.m_SceneEvtMgr.RemoveCBFunc(iSceneEvt)

    
    def BindSceneEvent(self, oOwner, iEvent, enterfunc, leavefunc, sKey = ''):
        self.m_SceneEvtMgr.BindCBFunc(oOwner, iEvent, enterfunc, leavefunc, sKey)

    
    def UnBindSceneEvent(self, iEvent, sKey = ''):
        self.m_SceneEvtMgr.UnBindCBFunc(iEvent, sKey)

    
    def ValidWarningPos(self, pos):
        tMin = self.m_BoundMin
        tMax = self.m_BoundMax
        if pos[0] < tMin[0] or pos[0] > tMax[0]:
            return False
        if pos[1] < tMin[1] - 30 or pos[1] > tMax[1]:
            return False
        if pos[2] < tMin[2] or pos[2] > tMax[2]:
            return False
        return True

    
    def IsInSceneBound(self, pos):
        tMin = self.m_BoundMin
        tMax = self.m_BoundMax
        if pos[0] < tMin[0] or pos[0] > tMax[0]:
            return False
        if pos[1] < tMin[1] or pos[1] > tMax[1]:
            return False
        if pos[2] < tMin[2] or pos[2] > tMax[2]:
            return False
        return True

    
    def GetBoundSize(self):
        return (self.m_BoundMax, self.m_BoundMin)

    
    def HaltSkill(self):
        self.m_Game.m_SkillMgr.LeaveScene(self.m_ID)

    
    def SceneGoto(self, obj, tPos):
        if not self.m_SceneLoad:
            SceneLog.Alert('Map%d Level%d obj(%d) %d enterscne unload ok' % (self.m_Map, self.m_Level, obj.m_SID, obj.m_ID))
            return None
        self.m_Game.Scene_Goto(obj.m_ID, self.m_ID, tPos)



class CSceneManager(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_VirtualSceneInfo = { }

    
    def Release(self):
        for oScene in self.m_VirtualSceneInfo.values():
            oScene.UnLoad()
        
        self.m_Game = None

    
    def CreateVirtualScene(self, iMap, iLevel, dParam):
        oScene = CVirtualScene(self.m_Game, iMap, iLevel, dParam)
        oScene.OnLoad()
        self.m_VirtualSceneInfo[oScene.m_ID] = oScene
        return oScene.m_ID

    
    def ReleaseScene(self, iScene):
        if iScene not in self.m_VirtualSceneInfo:
            return None
        oScene = self.m_VirtualSceneInfo[iScene]
        oScene.UnLoad()
        del self.m_VirtualSceneInfo[iScene]

    
    def GetScene(self, iScene):
        if iScene not in self.m_VirtualSceneInfo:
            return None
        oScene = self.m_VirtualSceneInfo[iScene]
        if not oScene.m_SceneLoad:
            return None
        return oScene

    
    def GetSceneIDByMap(self, iMap):
        for iScene, oScene in self.m_VirtualSceneInfo.items():
            if oScene.m_Map == iMap:
                return iScene
        
        return 0

    
    def GetAllSceneObjectsByType(self, sType):
        lstObj = []
        for oScene in self.m_VirtualSceneInfo.values():
            lstObj.extend(oScene.GetObjectsByType(sType))
        
        return lstObj



def OnSceneLoad(oGame, iScene):
    m_SceneMgr = oGame.m_SceneMgr
    if iScene not in m_SceneMgr.m_VirtualSceneInfo:
        return None
    oScene = m_SceneMgr.m_VirtualSceneInfo[iScene]
    (tBoundMax, tBoundMin) = oGame.Scene_GetSize(iScene)
    oScene.m_BoundMax = tBoundMax
    oScene.m_BoundMin = tBoundMin
    oScene.m_SceneLoad = True
    iLevel = oScene.m_Level
    oWarMgr = oGame.m_WarMgr
    SceneLog.Info('asyncload %s %s %s' % (oGame.m_ID, iScene, iLevel))
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_SCENELOAD, oWarMgr, {
        'iScene': iScene,
        'LevelID': iLevel })

