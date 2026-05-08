# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/linespawnaction.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/linespawnaction.pyc
# Source Generated with Decompyle++
# File: linespawnaction.pyc (Python 3.6)

from cl_only import ChooseKey, Functor, Time2Frame, ShufferList, PY_FLAG_DEAD, SendAlert, ChooseMulKeys
from cl_commondefines import SPAWN_ENTERROOM, SPAWN_DIFFERENTAREATRIGGERMONSTER, SPAMN_TRIGGERREMOVESTONEPILLAR, SPAWN_TRIGGERSTONEPILLAR, SPAMN_TRIGGERBUILDBEHAVIOR, SPAWN_TRIGGERSTOPDYINGSTATE, SPAWN_TRIGGERSTARTCHALLENGE, SPAWN_TRIGGERGAMEPAUSE, SPAWN_TRIGGERMONSTERCHOOSE, SPAWN_TRIGGERCOMNOTIFY, SPAWN_TRIGGERNPCPATH, SPAWN_CREATEAREAMONSTER, SPAWN_TRIGGERNPCBEHAVIOR, SPAWN_TRIGGERBUILD, SPAWN_REMOVEBUILD, SPAWN_ADDROOMCHALLENGE, SPAWN_TRIGGERLINEGOALPOS, SPAWN_TRIGGERSUPMONSTER, SPAWN_CRATEBUILD, SPAWN_MONSTERALLDIE, SPAWN_TIGGERBEHAVIOR, SPAWN_TRIGGERMONSTER, SPAWN_TIGGERREWARDNPC, SPAWN_TRIGGERGOALOK, SPAWN_TRIGGERGATE, CHASTATUS_WAIT, MODEL_TYPE_CAPSULE, NWARRIOR_NPC_CAR, DAM_USE_HP, DAM_TYPE_SCENE, CURVE_RING, CURVE_COMEANDGO
from cl_commondefines import CHECKTYPE_CLIENTBEHAVIOR, SPAWN_ONETIME_CLIENTBEHAVIOR, SPAWN_TRIGGERWINDCREATE, SPAWN_TRIGGERWINDDIE, SPAWN_NPCVISIBLE, PATHMODE_COLLISIONLESS, MODEL_TYPE_BOX
from cl_commondefines import SPAWN_BUILDPASSIVE, SPAWN_TIGGERCG, MINIMAPPT_SHOW_HIGHLIGHT, SPAWN_BLOCK_SCENEEVENT, SPAWN_TIGGERSURVIVORTRANSFER, SPAWN_TIGGERSURVIVORCREATEHINDER, SPAWN_TRIGGERCREATEMOVEBUILD
import cl_notify
import cl_msgcenter
import cl_snetwar
import cl_object
import cl_formula
import cl_reward
import cl_action
import cl_math
import cllib.lib_flag as lib_flag
import cl_bezier
import cl_modeldefine

def SpawnTriggerBehavior(oLineNode, tParam):
    if not oLineNode:
        return None
    if not oLineNode.m_Game:
        return None
    (iBehavior, iReSend) = tParam
    oGame = oLineNode.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        cl_snetwar.GS2CTriggerBehavior(oGame, iHero, iBehavior, [
            oHero.m_PlayerID])
    
    if not iReSend:
        return None
    oLevelCtrl = oLineNode.m_LevelNode.m_CtrlMgr
    if not oLevelCtrl:
        return None
    sKey = 'SpawnClientBehavior%s' % iBehavior
    oGame.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, sKey)
    iScene = oLineNode.m_LevelNode.m_Scene
    oGame.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, Functor(ReEnterClientBehavior, iScene, iBehavior), sKey)


def ReEnterClientBehavior(iScene, iBehavior, oWarMgr, oWarrior, dInfo):
    if iScene != dInfo['Scene']:
        return None
    iPlayer = oWarrior.m_PlayerID
    cl_snetwar.GS2CTriggerBehavior(oWarMgr.m_Game, oWarrior.m_ID, iBehavior, [
        iPlayer])


def SpawnTriggerGateCtrl(oLineNode, tParam, oTarget = None):
    oLevelNode = oLineNode.m_LevelNode
    (_, _, iDelay) = tParam
    iFrame = Time2Frame(iDelay)
    if iFrame:
        func = Functor(DelaySpawnTriggerGateCtrl, oLineNode, tParam, oTarget)
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'TriggerGateCtrl')
    else:
        DelaySpawnTriggerGateCtrl(oLineNode, tParam, oTarget)


def DelaySpawnTriggerGateCtrl(oLineNode, tParam, oTarget):
    oGame = oLineNode.m_Game
    if not oGame:
        return None
    oScene = oLineNode.GetCurScene()
    if not oScene:
        return None
    (_, iCurRoomIdx, iCurLineIdx) = oLineNode.GetLineIdx()
    oLevelCtrl = oLineNode.m_LevelNode.m_CtrlMgr
    if oLevelCtrl:
        dMsgInfo = {
            'VID': oTarget.m_ID if oTarget else 0 }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_TRIGGERGATECTRL, oLevelCtrl, dMsgInfo)
    (iPrefab, iAction, _) = tParam
    lstObstacle = oScene.GetObjectsByType('GateControl')
    for iObstacle in lstObstacle:
        oObstacle = oGame.GetObject(iObstacle)
        (_, iRoomIdx, iLineIdx) = oObstacle.m_LineIdx
        if iRoomIdx != iCurRoomIdx or iLineIdx != iCurLineIdx:
            continue
        if oObstacle.m_PendRemove:
            continue
        if oObstacle.m_Prefab == iPrefab:
            oObstacle.DoAction(iAction, { })
            break
    


def SpawnSceneMonsterAllDie(oLineNode, tParam = None):
    lstFightType = tParam[0] if tParam else []
    oScene = oLineNode.GetCurScene()
    oGame = oLineNode.m_Game
    lstMonster = oScene.GetObjectsByType('Monster')
    if lstFightType:
        lstMonster = FilterExcludeMonster(oGame, lstMonster, lstFightType)
    oLineNode.m_MonsterCtrl.ClearPendSpawnMonster()
    if not lstMonster:
        return None
    iSize = 5
    for i in range(iSize, len(lstMonster)):
        iMonsterID = lstMonster[i]
        oMonster = oGame.GetObject(iMonsterID, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if oMonster.m_Agent:
            oMonster.m_Agent.PauseAgent('SplitMonsterDying')
        cl_action.HaltAllCasting(oMonster, 'SplitMonsterDying')
    
    SplitMonsterDying(oLineNode, lstMonster, iSize)


def IsExcludeFightType(iFightType, lstFightType):
    for iTarFightType in lstFightType:
        if iFightType & iTarFightType == iTarFightType:
            return True
    
    return False


def FilterExcludeMonster(oGame, lstMonster, lstFightType):
    lstNewMonste = []
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if IsExcludeFightType(oMonster.m_FightType, lstFightType):
            continue
        lstNewMonste.append(iMonster)
    
    return lstNewMonste


def SplitMonsterDying(oLineNode, lstMonster, iSize):
    lstCur = lstMonster[:iSize]
    lstRest = lstMonster[iSize:]
    oGame = oLineNode.m_Game
    if not oGame:
        return None
    oReason = cl_object.reason.CStrReason('LineSpawnAction', None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    for iMonsterID in lstCur:
        oMonster = oGame.GetObject(iMonsterID, PY_FLAG_DEAD)
        if not oMonster:
            continue
        oMonster.HPModifyDam(0, [
            [
                oMonster.HP(),
                oReason]])
        if oMonster.m_Part and not oMonster.IsDead():
            oMonster.HPModifyDam(0, [
                [
                    oMonster.HP(),
                    oReason]])
        if oMonster.m_Agent:
            oMonster.m_Agent.ResumeAgent('SplitMonsterDying')
    
    if lstRest:
        oLevelNode = oLineNode.m_LevelNode
        func = Functor(SplitMonsterDying, oLineNode, lstRest, iSize)
        oLevelNode.m_CtrlMgr.Call_Out(func, 1, 'SplitMonsterDying')


def SpawnCreateBuild(oLineNode, tParam):
    oLevelNode = oLineNode.m_LevelNode
    (_, iDelay) = tParam
    iFrame = Time2Frame(iDelay)
    if iFrame:
        func = Functor(DelaySpawnCreateBuild, oLineNode, tParam)
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'CreateBuild')
    else:
        DelaySpawnCreateBuild(oLineNode, tParam)


def DelaySpawnCreateBuild(oLineNode, tParam):
    (iPerfab, _) = tParam
    oLevelNode = oLineNode.m_LevelNode
    if not oLevelNode:
        return None
    oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
    oGame = oLevelNode.m_Game
    iScene = oLevelNode.m_Scene
    lstDynaBuild = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'dynabuild')
    lstInitBuild = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'initbuild')
    for dInfo in lstInitBuild:
        if dInfo['Prefab'] == iPerfab:
            iBuildSID = dInfo['SID']
            oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dInfo, oLineNode.GetLineIdx())
            return None
    
    for dInfo in lstDynaBuild:
        if dInfo['Prefab'] == iPerfab:
            iBuildSID = dInfo['SID']
            oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dInfo, oLineNode.GetLineIdx())
            return None
    
    dInitObstacle = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'lineob')
    dDynaObstacle = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'dynaob')
    dObstacle = { }
    dObstacle.update(dInitObstacle)
    dObstacle.update(dDynaObstacle)
    if iPerfab in dObstacle:
        dInfo = dObstacle[iPerfab]
        iBuildSID = dInfo['SID']
        oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dInfo, oLineNode.GetLineIdx())


def SpawnRemoveBuild(oLineNode, tParam):
    oLevelNode = oLineNode.m_LevelNode
    (_, iDelay) = tParam
    iFrame = Time2Frame(iDelay)
    if iFrame:
        func = Functor(DelaySpawnRemoveBuild, oLineNode, tParam)
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'RemoveBuild')
    else:
        DelaySpawnRemoveBuild(oLineNode, tParam)


def DelaySpawnRemoveBuild(oLineNode, tParam):
    (iPerfab, _) = tParam
    oGame = oLineNode.m_Game
    if not oGame:
        return None
    oScene = oLineNode.GetCurScene()
    lstBuild = oScene.GetObjectsByTypes([
        'Build',
        'Obstacle',
        'Trap',
        'GateControl'])
    tLineIdx = oLineNode.GetLineIdx()
    for bid in lstBuild:
        oBuild = oGame.GetObject(bid)
        if not oBuild:
            continue
        if not (oBuild.m_LineIdx) or oBuild.m_LineIdx != tLineIdx:
            continue
        if oBuild.m_PendRemove:
            continue
        if oBuild.m_Prefab == iPerfab:
            oBuild.DirectRemove('LineSpawnRemove')
    


def SpawnTriggerGoalOk(oLineNode, tParam):
    pass


def SpawnTriggerMonsterCreate(oLineNode, tParam):
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    oMonsterCtrl.StartSpawn(tParam)


def SpawnTriggerSuperMonsterCreate(oLineNode, tParam):
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    oMonsterCtrl.StartSpawn(tParam[:-2], super = {
        'affix': tParam[-2],
        'plusatt': tParam[-1] })


def SpawnTriggerMonsterChoose(oLineNode, tParam):
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    (iGroup, dArea, iChoose, dAmount, iDelay, iExt) = tParam
    oMonsterCtrl.StartSpawn((iGroup, dArea, dAmount, iDelay, iExt))


def SpawnTriggerGamePause(oLineNode, tParam):
    (iPauseTime, iDelayTime) = tParam
    oLineNode.m_Game.m_WarKeep.CallOutCommonGamePause(iPauseTime, iDelayTime)


def SpawnTriggerRewardNpc(oLineNode, tParam):
    (dNpcWeight, dAmount) = tParam
    oGame = oLineNode.m_Game
    iRound = oGame.m_WarMgr.m_Round
    iCycle = oGame.m_WarMgr.m_Cycle
    dNpcInfo = oGame.m_WarData.GetNpcChooseInfo()
    for iNpc in list(dNpcWeight):
        if not cl_reward.ValidExtraGoldenCup(oGame, {
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
    
    if not dNpcWeight:
        return None
    oLevelNode = oLineNode.m_LevelNode
    iScene = oLevelNode.m_Scene
    tAmount = ChooseKey(oGame, dAmount)
    iAmount = cl_formula.GetFormulaResult(oLevelNode, tAmount)
    lstNpcPos = oLevelNode.ChooseRewardNpcPos(oLineNode.GetLineIdx(), iAmount)
    lstNpcPos = ShufferList(oGame, lstNpcPos)
    for dPos in lstNpcPos:
        iNpc = ChooseKey(oGame, dNpcWeight)
        if not iNpc:
            continue
        dMsgInfo = {
            'NPC': iNpc,
            'LevelNode': oLevelNode,
            'NPCInfo': dPos,
            'Scene': iScene }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelNode.m_CtrlMgr, dMsgInfo)
        if not dMsgInfo['NPC']:
            continue
        oGame.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dPos, oLineNode.GetLineIdx())
    


def SpawnTriggerLineGoalPos(oLineNode, tParam):
    pass


def SpawnAddChallenge(oLineNode, tParam):
    (iChallengeSID, iSkipReward) = tParam
    oLevelNode = oLineNode.m_LevelNode
    oChallengeMgr = oLevelNode.m_CtrlMgr.m_RoomChallenge
    oChallengeMgr.AddChallenge(oLevelNode.m_Level, oLineNode.m_IndexInLevel, iChallengeSID, iSkipReward, sReason = 'LineSpawn')


def SpawnTriggerBuild(oLineNode, tParam):
    (dSIDWeight, dRoundCnt, iDelay) = tParam
    iRound = oLineNode.m_Game.m_WarMgr.m_Round
    if iRound not in dRoundCnt:
        return None
    oLevelNode = oLineNode.m_LevelNode
    iDelayFrame = Time2Frame(iDelay)
    if iDelayFrame:
        func = Functor(DelaySpawnTriggerBuild, oLineNode, (dSIDWeight, dRoundCnt[iRound]))
        oLevelNode.m_CtrlMgr.Call_Out(func, iDelayFrame, 'TriggerBuild')
    else:
        DelaySpawnTriggerBuild(oLineNode, (dSIDWeight, dRoundCnt[iRound]))


def DelaySpawnTriggerBuild(oLineNode, tParam):
    (dSIDWeight, dCountWeight) = tParam
    dSIDWeight = dict(dSIDWeight)
    oLevelNode = oLineNode.m_LevelNode
    if not oLevelNode:
        return None
    oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
    oGame = oLevelNode.m_Game
    iScene = oLevelNode.m_Scene
    lstDynaBuild = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'dynabuild')
    if not dCountWeight:
        for dInfo in lstDynaBuild:
            oGame.m_ResMgr.CreateBuild(iScene, dInfo['SID'], dInfo, oLineNode.GetLineIdx())
        
        return None
    dSID2DynaBuild = { }
    for dInfo in lstDynaBuild:
        iBuildSID = dInfo['SID']
        lstBuildInfo = dSID2DynaBuild.setdefault(iBuildSID, [])
        lstBuildInfo.append(dInfo)
    
    lstErrorSID = []
    for iBuildSID in list(dSIDWeight):
        if iBuildSID not in dSID2DynaBuild:
            lstErrorSID.append(iBuildSID)
            dSIDWeight.pop(iBuildSID)
    
    if lstErrorSID:
        SendAlert('err', '关卡%d 路线%s配置的建筑刷新%s未在场景建筑中' % (oLevelNode.m_Level, oLineNode.m_Name, lstErrorSID))
    for iRound, dCount in dCountWeight.items():
        if not dCount:
            SendAlert('err', '关卡%d 路线%s配置数据有误' % (oLevelNode.m_Level, oLineNode.m_Name))
            return None
    
    tAmount = ChooseKey(oGame, dCountWeight)
    iAmount = cl_formula.GetFormulaResult(oLevelNode, tAmount)
    for _ in range(iAmount):
        iBuildSID = ChooseKey(oGame, dSIDWeight)
        if not iBuildSID:
            return None
        iChooseIndex = oGame.Random(len(dSID2DynaBuild[iBuildSID]))
        dInfo = dSID2DynaBuild[iBuildSID].pop(iChooseIndex)
        oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dInfo, oLineNode.GetLineIdx())
        if not dSID2DynaBuild[iBuildSID]:
            dSIDWeight.pop(iBuildSID)
            if not dSIDWeight:
                break
    


def SpawnTriggerNPCBehavior(oLineNode, tParam):
    (_, _, iDelay) = tParam
    oLevelNode = oLineNode.m_LevelNode
    iFrame = Time2Frame(iDelay)
    if iFrame:
        func = Functor(DelaySpawnTriggerNPCBehavior, oLineNode, tParam)
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'TriggerNPCBehavior')
    else:
        DelaySpawnTriggerNPCBehavior(oLineNode, tParam)


def DelaySpawnTriggerNPCBehavior(oLineNode, tParam):
    (iPrefab, iBehavior, _) = tParam
    oGame = oLineNode.m_Game
    if not oGame:
        return None
    oScene = oLineNode.GetCurScene()
    if not oScene:
        return None
    lstNPC = oScene.GetObjectsByType('NPC')
    lstPlayer = oScene.GetPlayers()
    for iNPC in lstNPC:
        oNpc = oGame.GetObject(iNPC)
        if not oNpc or oNpc.m_GlobalPrefab != iPrefab:
            continue
        cl_snetwar.GS2CTriggerBehavior(oGame, iNPC, iBehavior, lstPlayer)
    


def SpawnTriggerNPCPath(oLineNode, tParam):
    (_, _, iDelay) = tParam
    oLevelNode = oLineNode.m_LevelNode
    iFrame = Time2Frame(iDelay)
    if iFrame:
        func = Functor(DelaySpawnTriggerNPCPath, oLineNode, tParam)
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'TriggerNPCPath')
    else:
        DelaySpawnTriggerNPCPath(oLineNode, tParam)


def DelaySpawnTriggerNPCPath(oLineNode, tParam):
    (iPrefab, iPath, _) = tParam
    oGame = oLineNode.m_Game
    if not oGame:
        return None
    oScene = oLineNode.GetCurScene()
    if not oScene:
        return None
    lstNPC = oScene.GetObjectsByType('NPC')
    for iNPC in lstNPC:
        oNpc = oGame.GetObject(iNPC)
        if not oNpc or oNpc.m_GlobalPrefab != iPrefab or oNpc.m_FightType != NWARRIOR_NPC_CAR:
            continue
        oNpc.SetPath(iPath)
    


def SpawnTriggerCommonNotify(oLineNode, tParam):
    (iChat, iTime, iDelay) = tParam
    iFrame = Time2Frame(iDelay)
    if iFrame:
        oLevelNode = oLineNode.m_LevelNode
        func = Functor(SpawnTriggerCommonNotify, oLineNode, (iChat, iTime, 0))
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'TriggerNotify%d' % iChat)
    else:
        oGame = oLineNode.m_Game
        if not oGame:
            return None
        dExtInfo = { }
        if iTime:
            dExtInfo['iTime'] = iTime
        cl_notify.SendCommonNotify(oGame, oGame.GetRealPlayers(), iChat, {
            '$time': str(iTime) }, dExtInfo)


def SpawnStartChallenge(oLineNode, tParam):
    tLineIdx = oLineNode.GetLineIdx()
    oLevelNode = oLineNode.m_LevelNode
    oChallengeMgr = oLevelNode.m_CtrlMgr.m_RoomChallenge
    oChallenge = oChallengeMgr.GetChallenge(tLineIdx)
    if oChallenge and oChallenge.m_Status == CHASTATUS_WAIT:
        oChallenge.StartChallenge()


def SpawnStopDyingState(oLineNode, tParam):
    (iStopTime, iDelayTime) = tParam
    oWarMgr = oLineNode.m_Game.m_WarMgr
    oWarMgr.OnPlayingCG(iStopTime, iDelayTime)


def SpawnStonePillar(oLineNode, tParam):
    iDelay = tParam[10]
    iFrame = Time2Frame(iDelay)
    if iFrame:
        oLevelNode = oLineNode.m_LevelNode
        func = Functor(DelaySpawnStonePillar, oLineNode, tParam)
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'TriggerStonePillar')
    else:
        DelaySpawnStonePillar(oLineNode, tParam)


def DelaySpawnStonePillar(oLineNode, tParam):
    oLevelNode = oLineNode.m_LevelNode
    if not oLevelNode:
        return None
    (vCenter, vSize, fRadius, fOffset, tArgs, iCnt, iBuildSID, iAction, iMaxPercent, iMaxRotate, _) = tParam
    fMaxX = vCenter[0] + vSize[0] * 0.5
    fMinX = vCenter[0] - vSize[0] * 0.5
    fMaxZ = vCenter[2] + vSize[2] * 0.5
    fMinZ = vCenter[2] - vSize[2] * 0.5
    fSize = fRadius * 2
    iGridXCnt = int((fMaxX - fMinX) // fSize)
    iGridZCnt = int((fMaxZ - fMinZ) // fSize)
    iGridCnt = iGridXCnt * iGridZCnt
    lstGrid = [ x for x in range(0, iGridCnt) ]
    lstGridFlag = [ [
1] * (iGridZCnt + 2) for _ in range(iGridXCnt + 2) ]
    iRemainGridCnt = iGridCnt
    lDirx = [
        1,
        1,
        -1,
        -1]
    lDirz = [
        1,
        -1,
        1,
        -1]
    oGame = oLevelNode.m_Game
    iScene = oLevelNode.m_Scene
    for _ in range(iGridCnt):
        if not iCnt:
            break
        iFail = 0
        if not iRemainGridCnt:
            break
        iRand = lstGrid[oGame.Random(iRemainGridCnt)]
        lstGrid.remove(iRand)
        iRemainGridCnt -= 1
        iX = iRand // iGridZCnt + 1
        iZ = iRand % iGridZCnt + 1
        for idir in range(0, 4):
            iJugX = iX + lDirx[idir]
            iJugZ = iZ + lDirz[idir]
            if not lstGridFlag[iJugX][iZ] or lstGridFlag[iX][iJugZ]:
                if not lstGridFlag[iJugX][iJugZ]:
                    iFail = 1
                    break
        
        if iFail:
            continue
        lstGridFlag[iX][iZ] = 0
        x = iX - 1
        z = iZ - 1
        vPos = (x * fSize + fMinX + fRadius, 0, z * fSize + fMinZ + fRadius)
        iMidOffset = fOffset * 0.5
        vOffet = (oGame.Random(fOffset * 100) * 0.01 - iMidOffset, vCenter[1], oGame.Random(fOffset * 100) * 0.01 - iMidOffset)
        vPos = cl_math.Vec3Add(vPos, vOffet)
        iCnt -= 1
        iAngleY = oGame.Random(iMaxRotate)
        (x, y, z) = vPos
        fHeight = tArgs[0]
        iPercent = oGame.Random(iMaxPercent % 100)
        fFall = fHeight * (100 + iPercent) / 100
        tOrigin = [
            x,
            y - fFall,
            z]
        vDest = [
            x,
            (y - fFall) + fHeight,
            z]
        dAddData = {
            'Angle': [
                0,
                iAngleY,
                0],
            'Center': [
                0,
                fHeight * 0.5,
                0],
            'GlobalArea': 0,
            'NextArea': 0,
            'Origin': tOrigin,
            'Perfab': 0,
            'SID': iBuildSID,
            'Scale': [
                1,
                1,
                1],
            'Source': 0,
            'Shape': MODEL_TYPE_CAPSULE,
            'Size': (10, 2, 0) }
        dAddData['Other'] = {
            'Action': {
                iAction: vDest } }
        oBuild = oGame.m_ResMgr.CreateBuild(iScene, iBuildSID, dAddData)
        if oBuild:
            oBuild.DoAction(iAction, { })
    


def SpawnRemoveStonePillar(oLineNode, tParam):
    (iBehavior, iDelay) = tParam
    oLevelNode = oLineNode.m_LevelNode
    oGame = oLineNode.m_Game
    oScene = oLineNode.GetCurScene()
    lstBuild = oScene.GetObjectsByType('StonePillar')
    lstPlayer = oGame.m_WarMgr.GetRoomPlayer()
    lstTriggerBuild = []
    for iBuild in lstBuild:
        oBuild = oGame.GetObject(iBuild)
        if not oBuild:
            continue
        lstTriggerBuild.append(iBuild)
        cl_snetwar.GS2CTriggerBehavior(oGame, iBuild, iBehavior, lstPlayer)
    
    iFrame = Time2Frame(iDelay)
    if iFrame:
        func = Functor(DelayRemoveStonePillar, oLineNode, lstTriggerBuild)
        oLevelNode.m_CtrlMgr.Call_Out(func, iFrame, 'TriggerRemoveStonePillar')
    else:
        DelayRemoveStonePillar(oLineNode, lstTriggerBuild)


def DelayRemoveStonePillar(oLineNode, lstBuild):
    oGame = oLineNode.m_Game
    if not oGame:
        return None
    for iBuild in lstBuild:
        oBuild = oGame.GetObject(iBuild)
        if not oBuild:
            continue
        oBuild.Remove('SpawnRemove')
    


def SpawnTriggerBuildBehavior(oLineNode, tParam):
    if not oLineNode:
        return None
    (dOther, iAction) = tParam
    dNewOther = { }
    for iWarNo, value in dOther.items():
        dNewOther[int(iWarNo)] = int(list(value.keys())[0])
    
    oGame = oLineNode.m_Game
    iWarNo = oGame.m_WarMgr.m_SID
    if iWarNo in dNewOther:
        iSID = dNewOther[iWarNo]
        oScene = oLineNode.GetCurScene()
        lstBuild = oScene.GetObjectsByTypes([
            'Build',
            'Obstacle',
            'Trap',
            'GateControl'])
        for bid in lstBuild:
            oBuild = oGame.GetObject(bid)
            if oBuild.m_SID == iSID:
                oBuild.DoAction(iAction, { })
        


def SpawnDifferentAreaTriggerMonster(oLineNode, tParam):
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    (iGroup, dArea, dAmount, iChoose, iDelay, iExt) = tParam
    oMonsterCtrl.StartSpawn((iGroup, dArea, dAmount, iDelay, iExt))


def SpawnEnterRoom(oLineNode, tParam):
    oLevelNode = oLineNode.m_LevelNode
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ENTERROOM, oLevelNode.m_CtrlMgr, {
        'Level': oLevelNode.m_Level })


def OneTimeClientBehavior(oLineNode, tParam):
    if len(tParam) != 2:
        return None
    oWarMgr = oLineNode.m_Game.m_WarMgr
    (iBehavior, iMonsterSID) = tParam
    oWarMgr.Set('OneTimeClientBehavior', {
        iMonsterSID: iBehavior })


def TriggerOneTimeClientBehavior(oGame, iBehavior):
    lstHero = oGame.m_WarMgr.GetRoomHero()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        dDoneType = oHero.SetDefault('CheckTips', { })
        if CHECKTYPE_CLIENTBEHAVIOR in dDoneType and iBehavior in dDoneType[CHECKTYPE_CLIENTBEHAVIOR]:
            continue
        lstDoneBehavior = dDoneType.setdefault(CHECKTYPE_CLIENTBEHAVIOR, [])
        lstDoneBehavior.append(iBehavior)
        cl_snetwar.GS2CTriggerBehavior(oGame, oHero.m_ID, iBehavior, [
            oHero.m_PlayerID])
    


def SpanwTriggerCreateWind(oLineNode, tParam):
    if lib_flag.g_IsMobileRun:
        return None
    (iWindID, lstArea, dRound) = tParam
    oLevelNode = oLineNode.m_LevelNode
    if not oLevelNode:
        return None
    iRound = oLineNode.m_Game.m_WarMgr.m_Round
    if iRound not in dRound:
        return None
    if not dRound[iRound]:
        return None
    oGame = oLevelNode.m_Game
    iAmount = ChooseKey(oGame, dRound[iRound])
    if not iAmount:
        return None
    lstArea = ShufferList(oGame, lstArea, iAmount)
    oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
    iScene = oLevelNode.m_Scene
    dSummonInfo = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'windsummonpos')
    dInitPos = { }
    dExtraPos = { }
    dBorn = { }
    dType = { }
    for iArea, dInitInfo in dSummonInfo.items():
        dBorn[iArea] = dInitInfo['LinePosInfo'][0]['Pos']
        dType[iArea] = dInitInfo['LineType']
        lstPos = []
        lstExtraPos = []
        for dPosInfo in dInitInfo['LinePosInfo']:
            lstPos.append(dPosInfo['Pos'])
            if dPosInfo['PosType'] == 1 and dPosInfo['ExtraPos']:
                lstExtraPos.append(dPosInfo['ExtraPos'])
        
        dInitPos[iArea] = lstPos
        dExtraPos[iArea] = lstExtraPos
    
    dInfo = { }
    for iArea in lstArea:
        dInfo['Origin'] = dBorn[iArea]
        lstTargetPos = []
        lstInitPos = dInitPos[iArea]
        lstExtraPos = dExtraPos[iArea]
        iTpye = dType[iArea]
        if iTpye == CURVE_COMEANDGO:
            if not lstExtraPos:
                lstTargetPos = cl_bezier.GetLinearBezierCurve(lstInitPos)
            else:
                lstTargetPos = cl_bezier.GetQuadraticPowerBezierCurve(lstInitPos, lstExtraPos, False)
        if iTpye == CURVE_RING:
            lstTargetPos = cl_bezier.GetQuadraticPowerBezierCurve(lstInitPos, lstExtraPos, True)
        oSummon = oGame.m_ResMgr.CreateSummon(iScene, iWindID, dInfo, oLineNode.GetLineIdx())
        oSummon.Set('MoveInfo', lstTargetPos)
        oSummon.Set('InitPos', lstInitPos)
        oSummon.StartMove(0, iTpye)
        oSummon.m_MoveCtrl.SetPathMode('WindTrapSummon', PATHMODE_COLLISIONLESS)
    


def SpanwTriggerWindDie(oLineNode, tParam):
    if lib_flag.g_IsMobileRun:
        return None
    iWindID = tParam[0]
    oGame = oLineNode.m_Game
    if not oGame:
        return None
    oScene = oLineNode.GetCurScene()
    lstSummon = oScene.GetObjectsByType('Summon')
    tLineIdx = oLineNode.GetLineIdx()
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if not oSummon:
            continue
        if not (oSummon.m_LineIdx) or oSummon.m_LineIdx != tLineIdx:
            continue
        if oSummon.m_SID == iWindID:
            oReason = cl_object.reason.CStrReason('LineSpawnRemove', None, {
                'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
            oSummon.HPModifyDam(0, [
                [
                    oSummon.HP(),
                    oReason]])
    


def SpawnNpcVisible(oLineNode, tParam):
    iLimitEndless = tParam[1]
    oGame = oLineNode.m_Game
    if iLimitEndless and not oGame.m_WarMgr.GetEndlessElement():
        return None
    oScene = oLineNode.GetCurScene()
    if not oScene:
        return None
    iNpcSID = tParam[0]
    lstNpc = oScene.GetObjectsByTypes([
        'NPC',
        'Transfer'])
    lstPlayer = oScene.GetPlayers()
    oLevelCtrl = oLineNode.m_LevelNode.m_CtrlMgr
    if oLevelCtrl:
        oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(oScene.m_Level)
    else:
        oMiniMap = None
    for iNpc in lstNpc:
        oNpc = oGame.GetObject(iNpc)
        if not oNpc or oNpc.m_SID != iNpcSID:
            continue
        oNpc.ClearVisibleCondition()
        oNpc.NetAddTo(lstPlayer)
        if oMiniMap:
            dData = {
                'Pos': oNpc.GetPos(),
                'ShowMode': MINIMAPPT_SHOW_HIGHLIGHT }
            oMiniMap.AddTranferPos(oNpc.m_ID, dData)
    


def SpawnBuildPassive(oLineNode, tParam):
    if not oLineNode.m_Game:
        return None
    (iBuildSID, iPerform) = tParam
    oGame = oLineNode.m_Game
    oScene = oLineNode.GetCurScene()
    lstBuild = oScene.GetObjectsByTypes([
        'Build',
        'Obstacle',
        'Trap',
        'GateControl',
        'Protege'])
    for iBuild in lstBuild:
        oBuild = oGame.GetObject(iBuild, PY_FLAG_DEAD)
        if not oBuild or oBuild.m_SID != iBuildSID:
            continue
        oBuild.AddPerform(iPerform, iLevel = 1)
    


def SpawnTriggerCG(oLineNode, tParam):
    if not oLineNode:
        return None
    (iBehavior, iCanSkip) = tParam
    cl_action.CommonTriggerCG(oLineNode.m_Game, iBehavior, iCanSkip)


def SpawnLuoHouBlockSceneEvent(oLineNode, tParam):
    oScene = oLineNode.GetCurScene()
    if not oScene:
        return None
    (vCenterPos, fInnerRadius, fOuterRadius, iCount, iAngle) = tParam
    fMidRadius = (fInnerRadius + fOuterRadius) / 2
    lstRadius = (fInnerRadius, fMidRadius, fOuterRadius)
    lstPos = []
    (x, y, z) = vCenterPos
    vFace = None
    lstBlockData = []
    iOffsetAngle = int(360 / iCount)
    iCentreAngle = iAngle + iOffsetAngle // 2
    for _ in range(iCount):
        lstPos = []
        for idx, fDis in enumerate(lstRadius):
            x1 = x + fDis * cl_math.CosAngle(iAngle)
            z1 = z + fDis * cl_math.SinAngle(iAngle)
            vPos = (x1, y, z1)
            lstPos.append(vPos)
            if idx == 1:
                vFace = cl_math.RotateAroundVector(cl_math.Vec3Minus(vPos, vCenterPos), (0, 1, 0), 90)
        
        vCentrePos = (x + fMidRadius * cl_math.CosAngle(iCentreAngle), y, z + fMidRadius * cl_math.SinAngle(iCentreAngle))
        lstBlockData.append({
            'lstPos': lstPos,
            'Face': vFace,
            'CentrePos': vCentrePos })
        vFace = cl_math.RotateAroundVector(vFace, (0, -1, 0), iOffsetAngle)
        iAngle += iOffsetAngle
        iCentreAngle += iOffsetAngle
    
    oScene.m_CustomData['LuoHouBlockData'] = lstBlockData


def SpawnTriggerSurvivorTransfer(oLineNode, tParam):
    oLevelConfData = oLineNode.m_LevelNode.m_CtrlMgr.m_LevelConfData
    dTansferNpcInfo = oLevelConfData.GetLineConfig(oLineNode.m_LevelNode.m_Level, oLineNode.m_Name, 'transfernpc')
    if not dTansferNpcInfo:
        return None
    oSurvivorElement = oLineNode.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if not oSurvivorElement:
        return None
    iCount = tParam[0]
    dKeyInfo = dict.fromkeys(dTansferNpcInfo.keys(), 10)
    lstGroupKeys = ChooseMulKeys(oLineNode.m_Game, dKeyInfo, iCount)
    oTransferCtrl = oSurvivorElement.m_TransferCtrl
    oGame = oLineNode.m_LevelNode.m_Game
    iScene = oLineNode.m_LevelNode.m_Scene
    oTransferCtrl.Clear()
    for sGroup in lstGroupKeys:
        oTransferCtrl.SetGroupCDFrame(sGroup, 0)
        lstGroupNpcInfo = dTansferNpcInfo[sGroup]
        for dNpcInfo in lstGroupNpcInfo:
            iNpcSID = dNpcInfo['SID']
            dMsgInfo = {
                'NPC': iNpcSID,
                'LevelNode': oLineNode.m_LevelNode,
                'NPCInfo': dNpcInfo,
                'Scene': iScene }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLineNode.m_LevelNode.m_CtrlMgr, dMsgInfo)
            if not dMsgInfo['NPC']:
                continue
            dNpcInfo['Group'] = sGroup
            oNpc = oGame.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dNpcInfo, oLineNode.GetLineIdx())
            if not oNpc:
                continue
            oTransferCtrl.AddTransferNpc(sGroup, oNpc.m_ID)
        
    
    oTransferCtrl.RefreshTransferInfo()


def SpawnSurvivorCreateHinder(oLineNode, tParam):
    iArea = oLineNode.m_Area
    iRatio = tParam[0]
    dExcludeInfo = tParam[1]
    dExcludeHinderGroup = { }
    oLevelNode = oLineNode.m_LevelNode
    oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
    dObstacle = oLevelConfData.GetMapConfig(oLevelNode.m_Level, 'hinderob')
    if not dObstacle or iArea not in dObstacle:
        SendAlert('err', '关卡%d 路线%s未配置阻碍' % (oLevelNode.m_Level, oLineNode.m_Name))
        return None
    dHinderGroupInfo = dObstacle[iArea]
    tLineIdx = oLineNode.GetLineIdx()
    oWarMgr = oLineNode.m_Game.m_WarMgr
    lstSurvivorHinder = oWarMgr.Query('SurvivorHinder', [])
    if not lstSurvivorHinder:
        for dHinderGroup in dHinderGroupInfo.values():
            if oLineNode.m_Game.Random(100) >= iRatio:
                continue
            lstChoose = []
            for iHinderGroup in dHinderGroup:
                if iHinderGroup in dExcludeHinderGroup:
                    continue
                lstChoose.append(iHinderGroup)
            
            if not lstChoose:
                continue
            idx = oLineNode.m_Game.Random(len(lstChoose))
            iHinderGroup = lstChoose[idx]
            iExcludeHinderGroup = dExcludeInfo[iHinderGroup] if iHinderGroup in dExcludeInfo else 0
            if iExcludeHinderGroup:
                dExcludeHinderGroup[iExcludeHinderGroup] = 1
            lstCreate = dHinderGroup[iHinderGroup]
            lstSurvivorHinder.extend(lstCreate)
        
        oWarMgr.Set('SurvivorHinder', lstSurvivorHinder)
    for dHinderInfo in lstSurvivorHinder:
        iHinderSID = dHinderInfo['SID']
        oLineNode.m_Game.m_ResMgr.CreateBuild(oLevelNode.m_Scene, iHinderSID, dHinderInfo, tLineIdx)
    


def SpanwTriggerCreateMoveBuild(oLineNode, tParam):
    oLevelNode = oLineNode.m_LevelNode
    oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
    iScene = oLevelNode.m_Scene
    dMoveBuild = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLineNode.m_Name, 'movebuildpos')
    oGame = oLineNode.m_Game
    iPointBuildSID = tParam[0]
    tLineIdx = oLineNode.GetLineIdx()
    for dBuild in dMoveBuild.values():
        iBuildSID = dBuild['BuildSID']
        if iPointBuildSID != iBuildSID:
            continue
        clsBuildData = oGame.m_WarData.GetBuildData(iBuildSID)
        tModelData = cl_modeldefine.GetModelDefine(clsBuildData.m_Shape, 'Box')
        dAddData = {
            'Angle': dBuild['Angle'],
            'Center': [
                0,
                tModelData[1] * 0.5,
                0],
            'Origin': dBuild['Origin'],
            'GlobalArea': 0,
            'SID': iBuildSID,
            'Scale': [
                1,
                1,
                1],
            'Shape': MODEL_TYPE_BOX,
            'Size': tModelData,
            'EndPos': dBuild['EndPos'],
            'MoveType': dBuild['MoveType'],
            'MoveTime': dBuild['MoveTime'] }
        oGame.m_ResMgr.CreateBuild(iScene, iPointBuildSID, dAddData, tLineIdx)
    

g_SpawnFunc = {
    SPAWN_TRIGGERCREATEMOVEBUILD: SpanwTriggerCreateMoveBuild,
    SPAWN_TIGGERSURVIVORCREATEHINDER: SpawnSurvivorCreateHinder,
    SPAWN_TIGGERSURVIVORTRANSFER: SpawnTriggerSurvivorTransfer,
    SPAWN_BLOCK_SCENEEVENT: SpawnLuoHouBlockSceneEvent,
    SPAWN_TIGGERCG: SpawnTriggerCG,
    SPAWN_BUILDPASSIVE: SpawnBuildPassive,
    SPAWN_NPCVISIBLE: SpawnNpcVisible,
    SPAWN_TRIGGERWINDDIE: SpanwTriggerWindDie,
    SPAWN_TRIGGERWINDCREATE: SpanwTriggerCreateWind,
    SPAWN_ONETIME_CLIENTBEHAVIOR: OneTimeClientBehavior,
    SPAWN_ENTERROOM: SpawnEnterRoom,
    SPAWN_DIFFERENTAREATRIGGERMONSTER: SpawnDifferentAreaTriggerMonster,
    SPAMN_TRIGGERREMOVESTONEPILLAR: SpawnRemoveStonePillar,
    SPAMN_TRIGGERBUILDBEHAVIOR: SpawnTriggerBuildBehavior,
    SPAWN_TRIGGERSTONEPILLAR: SpawnStonePillar,
    SPAWN_TRIGGERSTOPDYINGSTATE: SpawnStopDyingState,
    SPAWN_TRIGGERSTARTCHALLENGE: SpawnStartChallenge,
    SPAWN_TRIGGERGAMEPAUSE: SpawnTriggerGamePause,
    SPAWN_TRIGGERMONSTERCHOOSE: SpawnTriggerMonsterChoose,
    SPAWN_TRIGGERCOMNOTIFY: SpawnTriggerCommonNotify,
    SPAWN_TRIGGERNPCPATH: SpawnTriggerNPCPath,
    SPAWN_TRIGGERNPCBEHAVIOR: SpawnTriggerNPCBehavior,
    SPAWN_TRIGGERBUILD: SpawnTriggerBuild,
    SPAWN_CREATEAREAMONSTER: SpawnTriggerMonsterCreate,
    SPAWN_ADDROOMCHALLENGE: SpawnAddChallenge,
    SPAWN_REMOVEBUILD: SpawnRemoveBuild,
    SPAWN_TRIGGERLINEGOALPOS: SpawnTriggerLineGoalPos,
    SPAWN_TRIGGERSUPMONSTER: SpawnTriggerSuperMonsterCreate,
    SPAWN_CRATEBUILD: SpawnCreateBuild,
    SPAWN_MONSTERALLDIE: SpawnSceneMonsterAllDie,
    SPAWN_TIGGERBEHAVIOR: SpawnTriggerBehavior,
    SPAWN_TIGGERREWARDNPC: SpawnTriggerRewardNpc,
    SPAWN_TRIGGERGOALOK: SpawnTriggerGoalOk,
    SPAWN_TRIGGERMONSTER: SpawnTriggerMonsterCreate,
    SPAWN_TRIGGERGATE: SpawnTriggerGateCtrl }

def GetSpawnFunc(idx):
    if idx in g_SpawnFunc:
        return g_SpawnFunc[idx]

