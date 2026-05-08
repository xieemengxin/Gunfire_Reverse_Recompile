# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/survivorbornctrl.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/survivorbornctrl.pyc
# Source Generated with Decompyle++
# File: survivorbornctrl.pyc (Python 3.6)

from cl_commondefines import SCENE_EVT_SHAPE_SPHERE, WARRIOR_HERO, LEVEL_STATE_PREPARE, STATE_TIME_LIMIT, VIRTUAL_ITEM_GOLDENCUP, SURVIVOR_NPC_RARECUP, STATE_WUDI
from cl_only import Functor, Time2Frame, GAME_FRAME
from cl_pxlayer import PXMASK_STATIC, PXMASK_IMPENETRABLE
from cl_object.logging import SurvivorLog
import cl_msgcenter
import cl_world
import cl_snetwar
import cl_notify
import cl_gamedebug as debug
import cl_object.reason
import cl_state
import cl_reward
EFFECT_INIT = 1025
EFFECT_FIGHT = 1
EFFECT_PREREMOVE = 2

class CSurvivorBornMgr(cl_world.CObject):
    
    def __init__(self, oSurvivorElement, iID, oData):
        super(CSurvivorBornMgr, self).__init__(oSurvivorElement.m_Game, iID)
        self.m_CallFlag = 'SurvivorBorn'
        self.m_Survivor = oSurvivorElement
        self.m_Trigger = { }
        self.m_HeroBorn = []
        self.m_Event = None
        self.m_Scene = 0
        self.m_EffectID = 0
        self.m_EffectSID = 0
        self.m_CheckArea = ((0, 0, 0), 0)
        self.m_RemoveFrame = 0
        self.m_MaxWudiFrame = Time2Frame(oData.m_Config.get('MaxWudiTime', 12000))
        self.m_ResetWudiFrame = Time2Frame(oData.m_Config.get('WudiTime', 2000))
        self.m_WudiState = { }

    
    def Init(self):
        oGame = self.m_Game
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOk, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIEDIST, self.OnHeroDie, self.m_CallFlag)

    
    def Release(self):
        oGame = self.m_Game
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIEDIST, self.m_CallFlag)
        self.m_Trigger = { }
        self.m_HeroBorn = []
        self.m_Event = None
        self.m_Survivor = None
        self.RemoveFromList()

    
    def DestoryTriggerEvent(self):
        if self.m_Event and self.m_Scene:
            oGame = self.m_Game
            oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
            if not oScene:
                return None
            oScene.RemoveSceneEvent(self.m_Event)
            self.m_Event = None

    
    def OnPlayerMapLoadOk(self, oWarMgr, oTarget, dInfo):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_CurNode.m_Scene != self.m_Scene:
            return None
        if not self.m_EffectSID:
            return None
        oGame = self.m_Game
        vPos = self.m_CheckArea[0]
        fGroundDis = oGame.Scene_GroundDistance(self.m_Scene, vPos, 10, PXMASK_STATIC | PXMASK_IMPENETRABLE)
        vPos = (vPos[0], vPos[1] - fGroundDis, vPos[2])
        if not self.m_EffectID:
            self.m_EffectID = oGame.NewNoSceneObjID()
        cl_snetwar.GS2CAddEffect(oGame, self.m_Scene, self.m_EffectID, self.m_EffectSID, vPos, {
            oTarget.m_PlayerID: 1 })
        self.AddOrUpdateWudiState(oTarget.m_ID)

    
    def OnRemovePlayer(self, oWarMgr, oTarget, dInfo):
        if not self.m_Event:
            return None
        self.TryRemovePrepareArea()

    
    def OnHeroDie(self, oWarMgr, oTarget, dInfo):
        if not self.m_Event:
            return None
        if oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        self.m_Trigger[oTarget.m_ID] = 1
        self.TryRemovePrepareArea()

    
    def GetBornPos(self):
        return self.m_HeroBorn

    
    def InitHeroBorn(self):
        oGame = self.m_Game
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oBornLine = oLevelCtrl.m_CurNode.m_RoomList[0][0]
        lstBornData = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, oBornLine.m_Name, 'survivalData', 'BornData')
        iIndex = oGame.Random(len(lstBornData))
        dBornData = lstBornData[iIndex]
        self.m_HeroBorn = dBornData['bornpos']
        self.m_RemoveFrame = Time2Frame(dBornData['RemoveTime']) if 'RemoveTime' in dBornData else 5 * GAME_FRAME
        iScene = oLevelCtrl.m_CurNode.m_Scene
        self.m_Scene = iScene
        if oGame.m_WarMgr.IsTransferGame():
            oSurvivor = self.m_Survivor
            oSurvivor.m_FightTimerMgr.PauseCounting('TransferGame')
            CompensateRareCup(oSurvivor, dBornData['extrararecuppos'], iScene)
            TryAddPhase(oSurvivor)
            oSurvivor.m_NpcRefreshMgr.SpawnTransferNpc(dBornData['extranpc'])
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        enterfunc = OnHeroTriggerEnter
        leavefunc = OnHeroTriggerLeave
        self.m_CheckArea = (dBornData['center'], dBornData['radius'])
        self.m_Event = oScene.AddSceneEvent(self, enterfunc, leavefunc, SCENE_EVT_SHAPE_SPHERE, self.m_CheckArea, { }, False)
        self.m_EffectSID = EFFECT_INIT
        debug.DebugCircle(oGame, self.m_CheckArea[0], self.m_CheckArea[1], debug.LINE_TILE)

    
    def UpdateEffect(self, iEffectSID, iConfig):
        if self.m_EffectID:
            self.m_EffectSID = iEffectSID
            oGame = self.m_Game
            oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
            if not oScene:
                return None
            cl_snetwar.GS2CTriggerAnimator(oGame, oScene.GetPlayers(), self.m_EffectID, iConfig)

    
    def AddOrUpdateWudiState(self, iHero, iForce = 0):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        if iHero in self.m_WudiState:
            oState = oHero.m_State.GetItem(self.m_WudiState[iHero])
            if oState:
                SurvivorLog.Debug('game:%d : bornarearesetwudi %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_ResetWudiFrame))
                oState.SetTime(oHero, self.m_ResetWudiFrame, 0)
            elif iForce:
                dArgs = {
                    'AID': oHero.m_ID,
                    'RS': cl_object.reason.CStrReason('SurviorHeroEnter'),
                    'arg': { } }
                oState = cl_state.AddState(oHero, STATE_WUDI, STATE_TIME_LIMIT, self.m_ResetWudiFrame, dArgs)
                if oState:
                    oState.Enable(oHero)
                    SurvivorLog.Debug('game:%d : fightresetwudi %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_ResetWudiFrame))
                    self.m_WudiState[oHero.m_ID] = oState.m_ID
                else:
                    dArgs = {
                        'AID': oHero.m_ID,
                        'RS': cl_object.reason.CStrReason('SurviorHeroEnter'),
                        'arg': { } }
                    oState = cl_state.AddState(oHero, STATE_WUDI, STATE_TIME_LIMIT, self.m_MaxWudiFrame, dArgs)
                    if oState:
                        oState.Enable(oHero)
                        SurvivorLog.Debug('game:%d : bornareainitwudi %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_MaxWudiFrame))
                        self.m_WudiState[oHero.m_ID] = oState.m_ID

    
    def RemoveWudiState(self, iHero):
        if iHero not in self.m_WudiState:
            return None
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        oState = oHero.m_State.GetItem(self.m_WudiState[iHero])
        if oState:
            SurvivorLog.Debug('game:%d : bornarearemovewudi %d' % (self.m_Game.m_ID, oHero.m_PlayerID))
            oHero.m_State.RemoveItem(oState.m_ID)

    
    def TryRemovePrepareArea(self):
        lstLiveHero = self.m_Game.m_WarMgr.GetLiveHero()
        for iHero in lstLiveHero:
            if iHero in self.m_Trigger and self.m_Trigger[iHero]:
                continue
        else:
            self.DestoryTriggerEvent()
            func = Functor(RemovePrepareArea, self)
            self.Call_Out(func, self.m_RemoveFrame, 'RemovePrepareArea' + self.m_CallFlag)



def OnHeroTriggerEnter(oSurvivorBornMgr, dMsgInfo):
    iTriggerObj = dMsgInfo['VID']
    if iTriggerObj in oSurvivorBornMgr.m_Trigger:
        return None
    obj = oSurvivorBornMgr.m_Game.GetObject(iTriggerObj)
    if obj.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    oSurvivorBornMgr.m_Trigger[iTriggerObj] = 0
    if oSurvivorBornMgr.m_EffectSID == EFFECT_PREREMOVE:
        oSurvivorBornMgr.Remove_Call_Out('RemovePrepareArea' + oSurvivorBornMgr.m_CallFlag)
        oSurvivorBornMgr.UpdateEffect(EFFECT_FIGHT, 1005)


def OnHeroTriggerLeave(oSurvivorBornMgr, dMsgInfo):
    iTriggerObj = dMsgInfo['VID']
    oGame = oSurvivorBornMgr.m_Game
    obj = oGame.GetObject(iTriggerObj)
    if obj.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    oSurvivorBornMgr.m_Trigger[iTriggerObj] = 1
    oSurvivorBornMgr.TryRemovePrepareArea()
    if oSurvivorBornMgr.m_Survivor.m_LevelState == LEVEL_STATE_PREPARE:
        if oSurvivorBornMgr.m_Survivor.m_Phase <= oSurvivorBornMgr.m_Survivor.m_MaxPhase:
            cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), 9333, { })
        oSurvivorBornMgr.m_Survivor.Start(obj)
        if oSurvivorBornMgr.m_EffectSID == EFFECT_INIT:
            oSurvivorBornMgr.UpdateEffect(EFFECT_FIGHT, 1005)
        for iHero in oGame.m_WarMgr.GetRoomHero():
            if iHero == iTriggerObj:
                continue
            oSurvivorBornMgr.AddOrUpdateWudiState(iHero, iForce = 1)
        
    oSurvivorBornMgr.RemoveWudiState(iTriggerObj)


def RemovePrepareArea(oSurvivorBornMgr):
    oGame = oSurvivorBornMgr.m_Game
    if oSurvivorBornMgr.m_EffectID:
        oScene = oGame.m_SceneMgr.GetScene(oSurvivorBornMgr.m_Scene)
        if not oScene:
            return None
        cl_snetwar.GS2CDeleteEffect(oGame, oSurvivorBornMgr.m_Scene, oSurvivorBornMgr.m_EffectID, oScene.GetPlayers())
    oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIEDIST, oSurvivorBornMgr.m_CallFlag)
    oSurvivorBornMgr.m_EffectSID = 0
    oSurvivorBornMgr.m_EffectID = 0


def CompensateRareCup(oSurvivor, lstPos, iScene):
    dRecord = oSurvivor.m_RareCupInteractRecord['Record']
    oSurvivor.m_RareCupInteractRecord['Record'] = { }
    oGame = oSurvivor.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    iPosLen = len(lstPos)
    for idx, dPlayer in enumerate(dRecord.values()):
        if idx >= iPosLen:
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            SurvivorLog.Alert('%s level:%s 房主转移灵爵点位不足:%s/%s' % (oGame.m_ID, oLevelCtrl.m_CurNode.m_Level, iPosLen, len(dRecord)))
            break
        dVisiblePlayer = { }
        oTarget = None
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if oHero.m_PlayerID in dPlayer:
                continue
            dVisiblePlayer[oHero.m_PlayerID] = 1
            oTarget = oHero
        
        if dVisiblePlayer:
            SurvivorLog.Debug('game:%d compensaterarecup: %s %s %s %s' % (oGame.m_ID, dRecord, lstHero, lstPlayer, dVisiblePlayer))
            dReward = {
                'item': VIRTUAL_ITEM_GOLDENCUP,
                'info': {
                    'sid': SURVIVOR_NPC_RARECUP,
                    'DropPos': lstPos[idx],
                    'VisiblePlayer': dVisiblePlayer,
                    'Scene': iScene } }
            lstReward = [
                dReward]
            cl_reward.RewardItem(oGame, oTarget, lstReward, 'recordcompensate', {
                'Player': oTarget.m_ID })
    


def TryAddPhase(oSurvivor):
    if oSurvivor.m_RareCupInteractRecord['Finish']:
        if oSurvivor.m_Phase > oSurvivor.m_MaxPhase or not (oSurvivor.m_Phase):
            return None
        if oSurvivor.IsEliteChallengePhase():
            oSurvivor.m_Phase += 1


def NewSurvivorBornManager(oSurvivorElement, oData):
    oGame = oSurvivorElement.m_Game
    iID = oGame.NewNPCID()
    oSurvivorBornMgr = CSurvivorBornMgr(oSurvivorElement, iID, oData)
    oGame.CreateObject(iID, oSurvivorBornMgr)
    oSurvivorBornMgr.Init()
    return oSurvivorBornMgr

