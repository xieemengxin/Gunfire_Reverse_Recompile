# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_framegame.pyc
# RelativePath: clientlogic/cl_framegame.pyc
# Source Generated with Decompyle++
# File: cl_framegame.pyc (Python 3.6)

from cl_only import InstantWarning, PRODUCT_MIN_NPC_ID, PythonError, PY_FLAG_DEAD, GAME_FRAME_SECOND
from cllib.lib_net import GetCPacketData, SetPacketDataForUnpack, UnpackInt
from cl_commondefines import MAX_STATE_TYPE
from cl_object.logging import ErrLog, OptimizationLog
import weakref
import C_frgame
import cl_warmgr
import cl_wardata
import cl_scene.mobject
import cl_scene.sceneevt
import cl_resmgr
import cl_world
import cl_msgcenter.mobject
import cl_perform.cartoon
import cl_perform.skill
import cl_betree.scenedata
import cl_minigame
import cl_link
import cl_betree.gamespace
import cl_duonet.dn_cl_framegame as framenet
import cl_gamestatus
import cl_gamekeep
import cl_aureole
import cl_random
import cl_framemovemgr
import cllib.lib_flag
import cl_netattr
import cl_container.statecon as statecon
if not cllib.lib_flag.g_IsLogicLayer:
    from pubtools.gctool import CNewGCTool
    import gc
    import sys
    import types
PYCB_SCENEEVENT = 1
PYCB_SCENELOAD = 8
PYCB_TIMERTIMEOUT = 9
if 'g_GameList' not in globals():
    g_GameList = { }

def CreateGame(iGame, iRandSeed):
    oGame = CLFrameGame(iGame, iRandSeed)
    g_GameList[iGame] = oGame
    return oGame.GetGameObj()


def ReleaseGame(iGame):
    if iGame not in g_GameList:
        return None
    g_GameList[iGame].Release()
    if not (cllib.lib_flag.g_IsLogicLayer) and cllib.lib_flag.g_IsInternalRun and sys.getrefcount(g_GameList[iGame]) > 2:
        ErrLog.Alert('Game%d释放时引用过多%d %s' % (iGame, sys.getrefcount(g_GameList[iGame]), gc.get_referrers(g_GameList[iGame])))
        for obj in gc.get_referrers(g_GameList[iGame]):
            if isinstance(obj, types.FrameType):
                ErrLog.Info('code %s' % obj.f_code.co_name)
                ErrLog.Info('locals %s' % obj.f_locals)
        
        oGCTool = CNewGCTool()
        oGCTool.AnalyseRef(g_GameList[iGame])
        C_frgame.PopCtrlGame(iGame)
    del g_GameList[iGame]


def RemoveGame(iGame, sReason):
    if iGame not in g_GameList:
        return None
    ErrLog.Alert('removegame%d %s' % (iGame, sReason))
    oGame = g_GameList[iGame]
    if oGame and oGame.m_Timer:
        oGame.m_Timer.Release()
    C_frgame.PopCtrlGame(iGame)
    del g_GameList[iGame]


def GetGame(iGame):
    if iGame not in g_GameList:
        return None
    return g_GameList[iGame].m_GameObj


def GetAllGame():
    dTemp = { }
    dTemp.update(g_GameList)
    return dTemp


def GetAllGameID():
    return list(g_GameList.keys())


class CLFrameGame(C_frgame.CFrameGame):
    
    def __init__(self, iGameID, iRandSeed):
        self.m_ID = iGameID
        C_frgame.CFrameGame.__init__(self, iGameID)
        self.InitGame(iRandSeed)
        self.m_InitRandSeed = iRandSeed
        self.m_NpcID = PRODUCT_MIN_NPC_ID
        self.m_CartoonID = 1
        self.m_StateID = 1
        self.m_NoSceneObjID = 1
        self.m_TraceNo = 1
        self.m_DropGroupID = 1
        self.m_SendAlertIdx = 1
        self.m_TestDelay = ()
        self.m_CtrlSimulateMap = { }
        self.m_CommandCacheList = []
        self.m_IsSingleGame = False
        self.m_PropChange = { }
        self.m_PropTeamChange = { }
        self.m_PropTeamInterval = 25
        self.m_StateChange = { }
        self.m_StateCntChange = { }
        self.m_StateTimeChange = { }
        self.m_StateLog = { }
        self.m_Timer = None
        self.m_WarData = None
        self.m_WarMgr = None
        self.m_SceneMgr = None
        self.m_ResMgr = None
        self.m_Betree = None
        self.m_LinkMgr = None
        self.m_SkillMgr = None
        self.m_Status = None
        self.m_WarKeep = None
        self.m_AureoleMgr = None
        self.m_RandomMgr = None
        self.m_FrameMoveMgr = None
        self.m_WarRelease = None
        self.m_WarPayMgr = None
        self.m_FrameMonitor = None
        self.m_ReleaseFlag = 0
        self.InitPyCallInfo(PYCB_SCENEEVENT, cl_scene.sceneevt.OnSceneEvt2)
        
        try:
            self.InitPyCallInfo(PYCB_TIMERTIMEOUT, OnTimerTimeOut)
        except:
            print('set calloutfunc failed')

        if cllib.lib_flag.g_OpenAsyncLoad:
            self.InitPyCallInfo(PYCB_SCENELOAD, cl_scene.mobject.OnSceneLoad)
        self.m_GameObj = weakref.proxy(self)
        self.m_MsgCenter = cl_msgcenter.mobject.CMsgCenter(self.m_GameObj)
        self.m_GlobalAttention = cl_msgcenter.mobject.CGameGlobalAttention(self.m_GameObj)
        self.m_MiniGameMgr = cl_minigame.CMiniGameMgr(self.m_GameObj)

    
    def Release(self):
        self.m_ReleaseFlag = 1
        self.m_GlobalAttention.Release()
        self.m_MiniGameMgr.Release()
        self.m_MsgCenter.Release()
        if self.m_SkillMgr:
            self.m_SkillMgr.Release()
        if self.m_WarMgr:
            self.m_WarMgr.Release()
        if self.m_SceneMgr:
            self.m_SceneMgr.Release()
        if self.m_ResMgr:
            self.m_ResMgr.Release()
        if self.m_Betree:
            self.m_Betree.Clear()
        if self.m_LinkMgr:
            self.m_LinkMgr.Release()
        if self.m_Status:
            self.m_Status.Release()
        if self.m_WarKeep:
            self.m_WarKeep.Release()
        if self.m_AureoleMgr:
            self.m_AureoleMgr.Release()
        if self.m_RandomMgr:
            self.m_RandomMgr.Release()
        if self.m_FrameMoveMgr:
            self.m_FrameMoveMgr.Release()
        if self.m_WarPayMgr:
            self.m_WarPayMgr.Release()
        if self.m_FrameMonitor:
            self.m_FrameMonitor.Release()
        if self.m_Timer:
            self.m_Timer.Release()
        if self.m_StateLog:
            OptimizationLog.Debug('%s state %s' % (self.m_ID, self.m_StateLog))

    
    def InitWarInfo(self, dWarInfo, dPlayerInfo):
        iWarNo = dWarInfo['WarNo']
        oGame = self.m_GameObj
        self.m_Timer = cl_world.CreateGlobalTimer(oGame)
        self.m_RandomMgr = cl_random.CRandomMgr()
        self.m_WarData = cl_wardata.LoadWarData(iWarNo)
        self.m_WarMgr = cl_warmgr.LoadWarMgr(oGame, iWarNo)
        self.m_SceneMgr = cl_scene.mobject.CSceneManager(oGame)
        self.m_ResMgr = cl_resmgr.CResManager(oGame)
        self.m_Betree = cl_betree.gamespace.NewGameSpace(oGame)
        self.m_LinkMgr = cl_link.CLinkManager(oGame)
        self.m_SkillMgr = cl_perform.skill.NewSkillManager(oGame)
        self.m_Status = cl_gamestatus.CGameStatus(oGame)
        self.m_WarKeep = cl_gamekeep.CGameWarKeep(oGame)
        self.m_AureoleMgr = cl_aureole.NewAureoleMgr(oGame)
        self.m_WarMgr.InitWarInfo(dWarInfo, dPlayerInfo)
        self.m_WarMgr.InitElement()
        self.m_WarMgr.InitPlayer(dPlayerInfo)
        self.m_WarMgr.InitWar()
        self.m_WarKeep.InitKeep()
        self.m_MiniGameMgr.InitAttention()
        self.m_FrameMoveMgr = cl_framemovemgr.CFrameMoveMgr()
        self.m_Betree.m_Open = 1
        self.m_IsSingleGame = self.m_WarMgr.IsSingleGame()
        if cllib.lib_flag.g_IsTradition:
            import cl_warpay
            self.m_WarPayMgr = cl_warpay.CWarPayManager(oGame)
        if cllib.lib_flag.g_OpenWarFrameCheck:
            import cl_framemonitor
            self.m_FrameMonitor = cl_framemonitor.CFrameMonitor(oGame)

    
    def GetWarData(self):
        return weakref.proxy(self.m_WarData)

    
    def GetSceneMgr(self):
        return weakref.proxy(self.m_SceneMgr)

    
    def GetResMgr(self):
        return weakref.proxy(self.m_ResMgr)

    
    def GetWarMgr(self):
        return weakref.proxy(self.m_WarMgr)

    
    def GetGameObj(self):
        return weakref.proxy(self)

    
    def CalRandSeed(self):
        iSeed = self.m_InitRandSeed * self.GetFrameNum() + 11259375
        return int(iSeed & 268435455)

    
    def NewNPCID(self):
        self.m_NpcID += 1
        if self.m_NpcID >= 2147483647:
            InstantWarning('NPCID overflow!')
        return self.m_NpcID

    
    def NewCartoonID(self):
        self.m_CartoonID += 1
        return self.m_CartoonID

    
    def NewStateID(self):
        self.m_StateID += 1
        if self.m_StateID > 268435455:
            self.m_StateID = 1
        return self.m_StateID * MAX_STATE_TYPE

    
    def NewNoSceneObjID(self):
        self.m_NoSceneObjID += 1
        if self.m_NoSceneObjID > 2147483647:
            self.m_NoSceneObjID = 1
        return self.m_NoSceneObjID

    
    def NewTraceNo(self):
        self.m_TraceNo += 1
        return self.m_TraceNo

    
    def NewSendAlertIdx(self):
        self.m_SendAlertIdx += 1
        return self.m_SendAlertIdx

    
    def Step(self):
        iFrame = self.GetFrameNum()
        self.S2CFrameStep(iFrame, self.GetRealPlayers())
        self.SimulateCtrlStep(iFrame)
        self.m_Betree.BetreeHeartBeat(iFrame)
        self.ProcessPropChange()
        if not (self.m_IsSingleGame) and iFrame % self.m_PropTeamInterval == 0:
            self.ProcessProTeamchange()
        self.ProcessState()
        self.m_ResMgr.ProcessDropCache()

    
    def S2CFrameStep(self, iFrame, dPlayers):
        framenet.DN_GS2CFightLoop(iFrame, dPlayers)

    
    def GetRealPlayers(self):
        return self.m_LinkMgr.GetLink()

    
    def CachePropChange(self, iObj, sAttr, iValue, iAttackPlayer):
        if iObj not in self.m_PropChange:
            self.m_PropChange[iObj] = {
                'Player': { },
                'Attr': { } }
        if iAttackPlayer:
            self.m_PropChange[iObj]['Player'][iAttackPlayer] = 1
        self.m_PropChange[iObj]['Attr'][sAttr] = iValue
        if self.m_IsSingleGame or not iAttackPlayer:
            return None
        if iObj not in self.m_PropTeamChange:
            self.m_PropTeamChange[iObj] = {
                'Player': { },
                'Attr': { } }
        if iAttackPlayer:
            self.m_PropTeamChange[iObj]['Player'][iAttackPlayer] = 1
        self.m_PropTeamChange[iObj]['Attr'][sAttr] = iValue

    
    def ProcessPropChange(self):
        dChange = self.m_PropChange
        self.m_PropChange = { }
        for iObj, dCache in dChange.items():
            obj = self.GetObject(iObj, PY_FLAG_DEAD)
            if not obj:
                continue
            for sAttr, iValue in dCache['Attr'].items():
                cl_netattr.GS2CPropChange(obj, sAttr, iValue, dCache['Player'])
            
        

    
    def ProcessProTeamchange(self):
        dChange = self.m_PropTeamChange
        self.m_PropTeamChange = { }
        dScenePlayer = { }
        for iObj, dCache in dChange.items():
            obj = self.GetObject(iObj, PY_FLAG_DEAD)
            if not obj:
                continue
            iScene = obj.m_Scene
            if iScene not in dScenePlayer:
                oScene = self.m_SceneMgr.GetScene(iScene)
                if not oScene:
                    continue
                dScenePlayer[iScene] = oScene.GetPlayers()
            dAttack = dCache['Player']
            lstPlayer = [ iPlayer for iPlayer in dScenePlayer[iScene] if iPlayer not in dAttack ]
            if not lstPlayer:
                continue
            for sAttr, iValue in dCache['Attr'].items():
                cl_netattr.GS2CPropChange(obj, sAttr, iValue, lstPlayer)
            
        

    
    def CacheStateAddDel(self, iObj, iStateSID, iStateID, iAdd):
        if iObj not in self.m_StateChange:
            self.m_StateChange[iObj] = { }
        if iAdd:
            self.m_StateChange[iObj][iStateID] = 1
        elif iStateID in self.m_StateChange[iObj]:
            self.m_StateChange[iObj][iStateID] = 0
            self.m_StateLog[iStateSID] = 1 if iStateSID not in self.m_StateLog else self.m_StateLog[iStateSID] + 1
        else:
            return 0
        return 1

    
    def CacheStateCnt(self, iObj, iStateSID, iState, iCnt):
        if iObj not in self.m_StateCntChange:
            self.m_StateCntChange[iObj] = { }
        if iState in self.m_StateCntChange[iObj]:
            self.m_StateLog[iStateSID] = 1 if iStateSID not in self.m_StateLog else self.m_StateLog[iStateSID] + 1
        self.m_StateCntChange[iObj][iState] = iCnt
        return 1

    
    def CacheStateTime(self, iObj, iState):
        if iObj not in self.m_StateTimeChange:
            self.m_StateTimeChange[iObj] = { }
        self.m_StateTimeChange[iObj][iState] = 1
        return 1

    
    def ProcessState(self):
        dChange = self.m_StateChange
        self.m_StateChange = { }
        for iObj, dState in dChange.items():
            obj = self.GetObject(iObj)
            if not obj:
                continue
            for iState, iAdd in dState.items():
                if not iAdd:
                    continue
                oState = obj.m_State.GetItem(iState)
                if not oState:
                    continue
                obj.m_State.GS2CItemAdd(oState, dPlayer = None, iRefresh = 1)
            
        
        dCntChange = self.m_StateCntChange
        self.m_StateCntChange = { }
        for iObj, dState in dCntChange.items():
            obj = self.GetObject(iObj)
            if not obj:
                continue
            iBoardCast = obj.m_State.m_GameBroadcast
            for iState, iCnt in dState.items():
                oState = obj.m_State.GetItem(iState)
                if not oState:
                    continue
                statecon.GS2CStateRefreshCnt(obj, iBoardCast, oState, iCnt)
            
        
        dTimeChange = self.m_StateTimeChange
        self.m_StateTimeChange = { }
        for iObj, dState in dTimeChange.items():
            obj = self.GetObject(iObj)
            if not obj:
                continue
            iBoardCast = obj.m_State.m_GameBroadcast
            for iState in dState:
                oState = obj.m_State.GetItem(iState)
                if not oState:
                    continue
                statecon.GS2CStateRefresh(obj, iBoardCast, oState)
            
        

    
    def SimulateCtrlStep(self, iFrame):
        for objID in self.m_WarMgr.GetLiveHero():
            obj = self.GetObject(objID)
            if obj and obj.m_MoveCtrl and obj.m_Scene:
                
                try:
                    obj.m_MoveCtrl.UpdateCtrlFrame(obj, iFrame)
                except:
                    PythonError()

        
        if self.m_FrameMoveMgr:
            self.m_FrameMoveMgr.Update(self, iFrame)

    
    def PushCommandCache(self, oHero):
        sData = GetCPacketData()
        self.m_CommandCacheList.append((oHero.m_PlayerID, sData))
        iLen = len(self.m_CommandCacheList)
        if iLen >= 64 and iLen % 32 == 0:
            dCmdCache = { }
            for tData in self.m_CommandCacheList:
                dUserCache = dCmdCache.setdefault(tData[0], { })
                iCmd = int(tData[1][0])
                if iCmd not in dUserCache:
                    dUserCache[iCmd] = 1
                    continue
                dUserCache[iCmd] += 1
            
            for pid, dUserCache in tuple(dCmdCache.items()):
                sUserCmd = '|'.join(map((lambda x: '0x%02x*%d' % x), dUserCache.items()))
                dCmdCache[pid] = sUserCmd
            
            sCmd = ','.join(map((lambda x: '%d-%s' % x), dCmdCache.items()))
            ErrLog.Alert('game %d cache cmd [%d] too more. [%s]' % (self.m_ID, len(self.m_CommandCacheList), sCmd))
            return False
        return True

    
    def ProcessCacheCommand(self):
        import cl_net
        cmdList = self.m_CommandCacheList
        self.m_CommandCacheList = []
        for iPlayer, sData in cmdList:
            obj = self.m_WarMgr.GetHeroByPlayer(iPlayer)
            if not obj:
                continue
            SetPacketDataForUnpack(sData)
            iCmd = UnpackInt(1)
            
            try:
                cl_net.OnProcessFightCommand(self, obj, iCmd)
            except:
                PythonError()

        

    
    def AddGlobalAttention(self, iListener, iMsg, cbfunc, sKey, iSub = -1):
        iMsg = cl_msgcenter.GetMsgKey(iMsg, iSub)
        self.m_GlobalAttention.AddAttention(iListener, iMsg, cbfunc, sKey)

    
    def DoneGlobalAttention(self, iListener, iMsg, sKey, iSub = -1):
        iMsg = cl_msgcenter.GetMsgKey(iMsg, iSub)
        self.m_GlobalAttention.DoneAttention(iListener, iMsg, sKey)

    
    def ReceiveMsg(self, iMsg, dMsgInfo):
        self.m_GlobalAttention.ReceiveMsg(self, iMsg, dMsgInfo)

    
    def __str__(self):
        return 'gameid:%s' % self.m_ID

    
    def __repr__(self):
        return 'gameid:%s' % self.m_ID



def OnTimerTimeOut(oObj, sFlag, fTime = 0):
    oLogFunc = ErrLog.Debug
    if sFlag == 'TU.State':
        oStateTimeUnit = oObj.m_StateTimeUnit
        if not oStateTimeUnit:
            return None
        oStateTimeUnit.OnTimeOut(oObj, fTime, oLogFunc)
    elif sFlag == 'TU.Passive':
        oPFPassTimeUnit = oObj.m_PFPassTimeUnit
        if not oPFPassTimeUnit:
            return None
        oPFPassTimeUnit.OnTimeOut(oObj, fTime, oLogFunc)
    elif oObj.IsSceneObj():
        oLogFunc('%s %s %s timeout %s time:%s' % (oObj.m_Game.m_ID, oObj.m_PlayerID, oObj.m_SID, sFlag, fTime))
    else:
        oLogFunc('%s timeout %s time:%s' % (oObj.m_Game.m_ID, sFlag, fTime))

