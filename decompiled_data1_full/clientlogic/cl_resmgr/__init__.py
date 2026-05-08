# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_resmgr/__init__.pyc
# RelativePath: clientlogic/cl_resmgr/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import SendAlert
from cl_commondefines import NWARRIOR_DROP_EQUIP, MODE_WEAPONSTORE, NWARRIOR_DROP_CASH
from cl_object.logging import SceneLog
import cl_drop
import cl_math
import cl_perform
import cl_msgcenter
import cl_platformdata
from . import roundmonsterconfig

class CResManager(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_WarData = oGame.GetWarData()
        self.m_CurMainScene = 0
        self.m_CurFrameDropCnt = 0
        self.m_DropCache = []
        self.m_InitDropWindow = 6
        self.m_DropWindow = self.m_InitDropWindow
        self.m_MergeFrame = 0
        self.m_Merge = { }
        self.m_MergeStartCnt = 5
        self.m_MergeMaxCnt = 3

    
    def Release(self):
        self.m_Game = None
        self.m_WarData = None
        self.m_DropCache = []

    
    def CreateMainScene(self):
        oSceneMgr = self.m_Game.GetSceneMgr()
        iMainScene = self.m_WarData.GetMainScene()
        iMap = self.m_WarData.GetMapInfo(iMainScene)
        iLevel = 0
        iScene = oSceneMgr.CreateVirtualScene(iMap, iLevel)
        self.SetMainScene(iScene)

    
    def SetMainScene(self, iScene):
        self.m_CurMainScene = iScene

    
    def GetMainScene(self):
        return self.m_CurMainScene

    
    def CreateScene(self, iMap, iLevel, dParam = None):
        oSceneMgr = self.m_Game.GetSceneMgr()
        return oSceneMgr.CreateVirtualScene(iMap, iLevel, dParam)

    
    def ReleaseScene(self, iScene):
        oSceneMgr = self.m_Game.m_SceneMgr
        oSceneMgr.ReleaseScene(iScene)
        lstRemove = []
        for lstDrop in self.m_DropCache:
            if lstDrop[0] == iScene:
                lstRemove.append(lstDrop)
        
        for lstDrop in lstRemove:
            SceneLog.Debug('%s remove dropcache %s %s' % (self.m_Game.m_ID, iScene, lstDrop))
            self.m_DropCache.remove(lstDrop)
        

    
    def ProcessDropCache(self):
        self.m_CurFrameDropCnt = 0
        if not self.m_DropCache:
            return None
        lstDrop = self.m_DropCache[:self.m_DropWindow]
        self.m_DropCache = self.m_DropCache[self.m_DropWindow:]
        for tArgs in lstDrop:
            self.CreateDrop(*tArgs)
        
        if not self.m_DropCache:
            self.m_DropWindow = self.m_InitDropWindow
        else:
            iRestCnt = len(self.m_DropCache)
            if iRestCnt > self.m_DropWindow * 2:
                self.m_DropWindow += self.m_InitDropWindow

    
    def GetDropCache(self):
        return self.m_DropCache

    
    def TryMergeDrop(self, iScene, iType, tPos, lstDropData, dExtraInfo, dStaticInfo, iOwner):
        tKey = (iScene, iType, iOwner)
        if tKey not in self.m_Merge:
            return None
        dMerge = self.m_Merge[tKey]
        if len(dMerge) < self.m_MergeStartCnt:
            return None
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        if iCurFrame != self.m_MergeFrame:
            return None
        for iDrop, iMergeCnt in dMerge.items():
            if iMergeCnt >= self.m_MergeMaxCnt:
                continue
            oDrop = oGame.GetObject(iDrop)
            if oDrop and oDrop.CheckMerge(tPos, dExtraInfo, dStaticInfo):
                oMergeDrop = oDrop
                break
        else:
            return None
        iMergeDrop = oMergeDrop.m_ID
        dMerge[iMergeDrop] += 1
        if dMerge[iMergeDrop] >= self.m_MergeMaxCnt:
            dMerge.pop(iMergeDrop, 0)
        oMergeDrop.MergeDropData(lstDropData)
        return oMergeDrop

    
    def SaveMergeDrop(self, oDrop):
        if oDrop.m_FightType != NWARRIOR_DROP_CASH:
            return None
        iCurFrame = self.m_Game.GetFrameNum()
        if self.m_MergeFrame != iCurFrame:
            self.m_Merge = { }
        self.m_MergeFrame = iCurFrame
        tKey = (oDrop.m_Scene, oDrop.m_FightType, oDrop.m_Owner)
        dDrop = self.m_Merge.setdefault(tKey, { })
        dDrop[oDrop.m_ID] = 0

    
    def CreateDrop(self, iScene, iType, tPos, lstDropData, dExtraInfo, dStaticInfo = None, iOwner = 0, iSplit = 0):
        if dStaticInfo is None:
            dStaticInfo = { }
        oGame = self.m_Game
        if iSplit:
            if self.m_CurFrameDropCnt > self.m_InitDropWindow:
                self.m_DropCache.append((iScene, iType, tPos, lstDropData, dExtraInfo, dStaticInfo, iOwner))
                return None
            self.m_CurFrameDropCnt += 1
        tFixPos = (tPos[0], tPos[1] + 1, tPos[2])
        oDrop = self.TryMergeDrop(iScene, iType, tFixPos, lstDropData, dExtraInfo, dStaticInfo, iOwner)
        if oDrop:
            return oDrop
        iType = cl_drop.GetRealDropType(oGame, iType, lstDropData, dExtraInfo.get('ValidRemoveCurseRelic', 0), iOwner)
        oDrop = cl_drop.NewDrop(oGame, iType)
        if iType == NWARRIOR_DROP_EQUIP and MODE_WEAPONSTORE in self.m_Game.m_WarMgr.m_ModeType:
            oWeaponStoreElement = self.m_Game.m_WarMgr.GetComponent('WeaponStoreElement')
            if oWeaponStoreElement:
                oWeapon = lstDropData[0]
                oWeaponStoreElement.DealWeaponStoreInfo(oWeapon, iOwner, oDrop.m_ID)
                if oWeapon.Query('UnWarWeapon', 0):
                    dStaticInfo['DropSource'] = 0
        oDrop.SetOwner(iOwner)
        oDrop.SetDropData(lstDropData, dStaticInfo)
        if 'Abandoner' in dExtraInfo:
            oDrop.SetAbandoner(dExtraInfo['Abandoner'])
        if 'DropReason' in dExtraInfo:
            oDrop.Set('DropReason', dExtraInfo['DropReason'])
        elif 'DropReason' in dStaticInfo:
            oDrop.Set('DropReason', dStaticInfo['DropReason'])
        if iOwner:
            oDrop.SyncDropSource(iType, iOwner)
        oDrop.Goto(iScene, tFixPos)
        self.SaveMergeDrop(oDrop)
        return oDrop

    
    def CreateMonster(self, iScene, iMonsterSID, tPos, tFace, iSide = 0, iGrade = 0, dAI = None, tLineIdx = None, dExtInfo = None):
        if not dExtInfo:
            dExtInfo = { }
        oGame = self.m_Game
        dAddInfo = { }
        dData = {
            'MonsterSID': iMonsterSID,
            'LineIdx': tLineIdx,
            'Pos': tPos,
            'AddInfo': dAddInfo,
            'ExtInfo': dExtInfo }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.m_Game.m_WarMgr, dData)
        iMonsterSID = dData['MonsterSID']
        clsMonsterData = self.m_WarData.GetMonsterData(iMonsterSID)
        if not clsMonsterData:
            iLevel = tLineIdx[0] if tLineIdx else 0
            SendAlert('err', '战场%d未配置怪物 %d, 关卡%d' % (oGame.GetWarMgr().m_SID, iMonsterSID, iLevel))
            return None
        if iSide:
            dAddInfo['Side'] = iSide
        if dAI:
            dAddInfo['AI'] = dAI
        if tLineIdx:
            dAddInfo['Line'] = tLineIdx
        if 'ReplacePos' in dData:
            tPos = dData['ReplacePos']
        if 'ForceGrade' in dData:
            dAddInfo['AddGrade'] = 0
            iGrade = dData['ForceGrade']
        else:
            dAddInfo['AddGrade'] = iGrade
            iGrade += self.GetMonsterBaseGrade(iScene)
        if dExtInfo and 'ID' in dExtInfo:
            dAddInfo['ID'] = dExtInfo['ID']
        iGrade = max(1, iGrade)
        dAddInfo['Grade'] = iGrade
        if dExtInfo:
            dAddInfo.update(dExtInfo)
        oMonster = clsMonsterData.Create(oGame, dAddInfo)
        if 'Owner' in dAddInfo:
            oOwner = oGame.GetObject(dAddInfo['Owner'])
            if oOwner:
                vFixDropPos = oOwner.Query('FixDropPos')
                if vFixDropPos:
                    oMonster.Set('FixDropPos', vFixDropPos)
                    oMonster.Set('CheckDropInfo', oOwner.Query('CheckDropInfo'))
        oMonster.Goto(iScene, tPos, tFace)
        dMsgInfo = {
            'Monster': oMonster.m_ID,
            'LineIdx': tLineIdx }
        if dExtInfo:
            dMsgInfo.update(dExtInfo)
            if 'SetInfo' in dExtInfo:
                for key, value in dExtInfo['SetInfo'].items():
                    oMonster.Set(key, value)
                
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CREATEMONSTER, oMonster, dMsgInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_Game.m_WarMgr, dMsgInfo)
        if oMonster.IsDead():
            SceneLog.Alert(f'''{oGame.m_ID} create monster isdead {iMonsterSID} {oMonster.m_ID} {oMonster.m_FinalDam} {oMonster.m_DeadReason}''')
        return oMonster

    
    def CreateNpc(self, iScene, iNpcSID, dAddInfo, tLineIdx = None):
        oGame = self.m_Game
        clsNpcData = self.m_WarData.GetNpcData(iNpcSID)
        if not clsNpcData:
            iLevel = tLineIdx[0] if tLineIdx else 0
            SendAlert('err', '战场%d未配置NPC %d, 关卡%d' % (oGame.m_WarMgr.m_SID, iNpcSID, iLevel))
            return None
        if tLineIdx:
            dAddInfo['Line'] = tLineIdx
        SceneLog.Debug('%s createnpc %s %s %s %s' % (oGame.m_ID, iScene, iNpcSID, tLineIdx, dAddInfo))
        oNpc = clsNpcData.Create(oGame, dAddInfo)
        tPos = dAddInfo['Pos']
        tFace = dAddInfo['Facing'] if 'Facing' in dAddInfo else None
        tEuler = cl_math.Angle2Radians(dAddInfo['Angle']) if 'Angle' in dAddInfo else None
        oNpc.Goto(iScene, tPos, tFace, tEuler)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_NPCCREATEOVER, oNpc, {
            'NpcID': oNpc.m_ID })
        return oNpc

    
    def CreateSummon(self, iScene, iSummonSID, dAddInfo, tLineIdx = None, iGrade = 1):
        oGame = self.m_Game
        clsSummonData = self.m_WarData.GetSummonData(iSummonSID)
        if not clsSummonData:
            iLevel = tLineIdx[0] if tLineIdx else 0
            SendAlert('err', '战场%d未配置召唤物 %d, 关卡%d' % (oGame.GetWarMgr().m_SID, iSummonSID, iLevel))
            return None
        if tLineIdx:
            dAddInfo['Line'] = tLineIdx
        dAddInfo['Grade'] = iGrade
        dAddInfo['AddGrade'] = iGrade
        oSummon = clsSummonData.Create(oGame, dAddInfo)
        tPos = dAddInfo['Origin']
        tFace = dAddInfo.get('Facing', None)
        tEuler = cl_math.Angle2Radians(dAddInfo['Angle']) if 'Angle' in dAddInfo else None
        if 'Owner' in dAddInfo:
            oOwner = oGame.GetObject(dAddInfo['Owner'])
            if oOwner:
                vFixDropPos = oOwner.Query('FixDropPos')
                if vFixDropPos:
                    oSummon.Set('FixDropPos', vFixDropPos)
                    oSummon.Set('CheckDropInfo', oOwner.Query('CheckDropInfo'))
        oSummon.Goto(iScene, tPos, tFace, tEuler)
        return oSummon

    
    def CreateBuild(self, iScene, iBuildSID, dAddInfo, tLineIdx = None):
        oGame = self.m_Game
        clsBuildData = self.m_WarData.GetBuildData(iBuildSID)
        if not clsBuildData:
            iLevel = tLineIdx[0] if tLineIdx else 0
            iPrefab = dAddInfo['Prefab'] if 'Prefab' in dAddInfo else 0
            SendAlert('err', '战场%d未配置建筑 %d, 关卡%d预制体编号%d' % (oGame.GetWarMgr().m_SID, iBuildSID, iLevel, iPrefab))
            return None
        if tLineIdx:
            dAddInfo['Line'] = tLineIdx
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if oScene:
            dAddInfo['SceneMap'] = oScene.m_Map
        dAddInfo['GameID'] = oGame.m_ID
        dAddInfo['SceneID'] = iScene
        oBuild = clsBuildData.Create(oGame, dAddInfo)
        tPos = dAddInfo['Origin']
        tEuler = cl_math.Angle2Radians(dAddInfo['Angle']) if 'Angle' in dAddInfo else None
        oBuild.Goto(iScene, tPos, None, tEuler)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CREATEBUILD, self.m_Game.m_WarMgr, {
            'BuildID': oBuild.m_ID })
        return oBuild

    
    def CreateServant(self, iScene, iServantSID, dAddInfo):
        oGame = self.m_Game
        clsServantData = cl_platformdata.GetServantConfig(iServantSID)
        if not clsServantData:
            SendAlert('err', f'''未配置仆从{iServantSID}''')
            return None
        oServant = clsServantData.Create(oGame, dAddInfo)
        return oServant

    
    def CreateDevice(self, oHero, iDeviceSID, dAddInfo):
        clsDeviceData = cl_platformdata.GetDeviceClass(iDeviceSID)
        if not clsDeviceData:
            SendAlert('err', f'''装置{iDeviceSID}不存在''')
            return None
        oDevice = clsDeviceData.Create(self.m_Game, oHero, dAddInfo)
        return oDevice

    
    def CreateRoomChallenge(self, iLevel, iRoomPos, iChallengeSID, sReason = ''):
        oGame = self.m_Game
        clsChallengeData = self.m_WarData.GetChallengeData(iChallengeSID)
        if not clsChallengeData:
            SendAlert('err', '战场%d未配置房间挑战 %d' % (oGame.GetWarMgr().m_SID, iChallengeSID))
            return None
        dAddData = {
            'LevelID': iLevel,
            'RoomPos': iRoomPos,
            'Reason': sReason }
        oChallenge = clsChallengeData.Create(oGame, dAddData)
        return oChallenge

    
    def NewPerform(self, iPerform, oOwner, iLevel):
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if not clsPerform:
            return None
        return clsPerform(oOwner, iLevel)

    
    def GetMonsterBaseGrade(self, iScene):
        oSceneMgr = self.m_Game.m_SceneMgr
        oScene = oSceneMgr.GetScene(iScene)
        if not oScene:
            return 0
        iLevel = oScene.m_Level
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        return oLevelCtrl.GetMonsterBaseGrade(iLevel)



def GetMonsterSID(iRound, iLayer, iClassify, bElite = False):
    if iRound not in roundmonsterconfig.g_RoundMonsterConfig:
        return { }
    if iLayer not in roundmonsterconfig.g_RoundMonsterConfig[iRound]:
        return { }
    if iClassify not in roundmonsterconfig.g_RoundMonsterConfig[iRound][iLayer]:
        return { }
    if bElite:
        return roundmonsterconfig.g_RoundMonsterConfig[iRound][iLayer][iClassify]['Elite']
    return roundmonsterconfig.g_RoundMonsterConfig[iRound][iLayer][iClassify]['Normal']


def GetMonsterPower(iRound, iLayer, iBaseSID, bElite = False):
    if iRound not in roundmonsterconfig.g_RoundMonsterConfig:
        return 0
    if iLayer not in roundmonsterconfig.g_RoundMonsterConfig[iRound]:
        return 0
    dClassify = roundmonsterconfig.g_RoundMonsterConfig[iRound][iLayer]
    for _, dPower in dClassify.items():
        if bElite and iBaseSID in dPower['Elite']:
            return dPower['Elite'][iBaseSID]
        if not bElite and iBaseSID in dPower['Normal']:
            return dPower['Normal'][iBaseSID]
    
    return 0


def GetLayerMonsterBaseSID(iRound, iLayer):
    if iRound not in roundmonsterconfig.g_RoundMonsterConfig:
        return []
    if iLayer not in roundmonsterconfig.g_RoundMonsterConfig[iRound]:
        return []
    dLayer = roundmonsterconfig.g_RoundMonsterConfig[iRound][iLayer]
    lstMonster = []
    for dClassify in dLayer.values():
        lstElite = list(dClassify['Elite'].keys())
        lstNormal = list(dClassify['Normal'].keys())
        lstMonster.extend(lstElite)
        lstMonster.extend(lstNormal)
    
    return lstMonster

