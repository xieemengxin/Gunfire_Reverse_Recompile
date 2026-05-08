# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/thunderstormelement.pyc
# RelativePath: clientlogic/cl_warmgr/thunderstormelement.pyc
# Source Generated with Decompyle++
# File: thunderstormelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_cscommondef.cs_fight import LEVEL_TYPE_HIDE
from cl_only import DeepCopy, Time2Frame, Functor, Frame2Time, PY_FLAG_DEAD, SendAlert
from cl_commondefines import OBSTACLE_SOURCE_LEVEL, WARRIOR_HERO, MODEL_TYPE_BOX
import cl_msgcenter
import cl_war
import cl_snetwar as warnet
import cl_math
PREPAR_STAGE = 1
THUNDER_STAGE = 2
OVER_STAGE = 3
CHOOSE_RANDOM_TIMES = 10
CHOOSE_DIR_TIMES = 4

class CThunderstormElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CThunderstormElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_CallFlag = 'ThunderstormElement'
        self.m_StageTime = self.m_Data.m_Config.get('StageTime', { })
        self.m_Trap = self.m_Data.m_Config.get('Trap', (0, 0))
        self.m_ChooseSafeNum = self.m_Data.m_Config.get('SafeNum', (0, 0))
        self.m_RoomChoose = self.m_Data.m_Config.get('RoomChoose', 0)
        self.m_ThunderInfo = self.m_Data.m_Config.get('ThunderInfo', (100, 0, 1.5))
        self.m_ChooseThunderInfo = self.m_Data.m_Config.get('ChooseThunderInfo', { })
        self.m_StageInfo = { }
        self.m_LevleRoomSafePosInfo = { }
        self.m_CurSafeTrap = { }
        self.m_ShowHeroInfo = { }
        self.m_FristRoomFlag = 1

    
    def Init(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.OnRoomStart, 'RoomStart' + self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, 'RoomGoal' + self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LEVELROOMDOORTRIGGER, self.OnLevelRoomDoorTrigger, 'LevelRoomDoorTrigger' + self.m_CallFlag)
        cl_msgcenter.AddAttentionFunc(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, 'LevelFinish' + self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'PlayerMapLoadOK' + self.m_CallFlag)

    
    def Release(self):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMSTART, 'RoomStart' + self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, 'RoomGoal' + self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LEVELROOMDOORTRIGGER, 'LevelRoomDoorTrigger' + self.m_CallFlag)
        cl_msgcenter.DoneAttention(self, self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'LevelFinish' + self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'PlayerMapLoadOK' + self.m_CallFlag)
        super(CThunderstormElement, self).Release()
        self.m_WarMgr = None

    
    def OnPlayerMapLoadOK(self, oWarMgr, oHero, dMsgInfo):
        for tLevel, lstHero in self.m_ShowHeroInfo.items():
            (iLevel, _) = tLevel
            if oHero.m_ID in lstHero and iLevel == dMsgInfo['LevelID']:
                self.SendClientStageInfo(oHero, tLevel)
        

    
    def SendClientStageInfo(self, oHero, tLevel):
        iCurFrame = self.m_Game.GetFrameNum()
        (iStage, iTime, iStartFrame) = self.m_StageInfo[tLevel]
        iRemainTime = iTime - Frame2Time(iCurFrame - iStartFrame)
        lstCurSafeTrap = self.m_CurSafeTrap[tLevel]
        lstSafe = []
        for oTrap, SafeRadius, _ in lstCurSafeTrap:
            lstSafe.append([
                oTrap.GetPos(),
                SafeRadius])
        
        warnet.GS2CSendThunderStageInfo(self.m_Game, iStage, iTime, iRemainTime, lstSafe, {
            oHero.m_PlayerID: 1 })

    
    def OnLevelRoomDoorTrigger(self, oThunderstormElement, oLevelCtrl, dMsgInfo):
        oVictim = self.m_Game.GetObject(dMsgInfo['VID'])
        if not oVictim.m_FightType & WARRIOR_HERO:
            return None
        for tLevel in self.m_LevleRoomSafePosInfo:
            (iLevel, iRoom) = tLevel
            oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
            iScene = oLevelNode.m_Scene
            if iScene == dMsgInfo['Scene'] and iRoom == dMsgInfo['RoomPos']:
                lstShowHeroInfo = self.m_ShowHeroInfo.setdefault(tLevel, [])
                if dMsgInfo['VID'] not in lstShowHeroInfo:
                    lstShowHeroInfo.append(dMsgInfo['VID'])
                    oHero = self.m_Game.GetObject(dMsgInfo['VID'])
                    self.SendClientStageInfo(oHero, tLevel)
        

    
    def OnLevelFinish(self, oThunderstormElement, oLevelCtrl, dMsgInfo):
        lstAllLevelKey = list(self.m_LevleRoomSafePosInfo.keys())
        for tLevel in lstAllLevelKey:
            self.ClearAllLevelRoom(tLevel)
        
        self.m_FristRoomFlag = 1

    
    def OnRoomGoal(self, oThunderstormElement, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoom = dMsgInfo['Room']
        tLevel = (iLevel, iRoom)
        self.ClearAllLevelRoom(tLevel)

    
    def ClearAllLevelRoom(self, tLevel):
        if tLevel in self.m_LevleRoomSafePosInfo:
            self.m_LevleRoomSafePosInfo.pop(tLevel)
        lstHero = []
        if tLevel in self.m_ShowHeroInfo:
            lstHero = self.m_ShowHeroInfo.pop(tLevel)
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            warnet.GS2CSendThunderStageInfo(self.m_Game, OVER_STAGE, 0, 0, [], {
                oHero.m_PlayerID: 1 })
        
        (iLevel, iRoom) = tLevel
        sKey = 'ChangeStage_%s_%s' % (iLevel, iRoom) + self.m_CallFlag
        self.Remove_Call_Out(sKey)
        self.ClearLevelRoomStage(tLevel)

    
    def OnRoomStart(self, oThunderstormElement, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode.m_LevelType == LEVEL_TYPE_HIDE:
            return None
        iRoom = dMsgInfo['Room']
        tLevel = (iLevel, iRoom)
        iRandom = self.m_Game.Random(100)
        if iRandom >= self.m_RoomChoose:
            self.m_FristRoomFlag = 0
            return None
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        lstThunderstormSafeInfo = []
        for oLine in oLevelNode.m_RoomList[iRoom]:
            lstSafeInfo = oLevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'thunderstormsafepos')
            if not lstSafeInfo:
                continue
            lstThunderstormSafeInfo.extend(lstSafeInfo)
        
        if not lstThunderstormSafeInfo:
            return None
        self.m_LevleRoomSafePosInfo[tLevel] = lstThunderstormSafeInfo
        self.StartThunderstorm(tLevel)

    
    def StartThunderstorm(self, tLevel):
        self.ChangeStage(tLevel, PREPAR_STAGE, 1)

    
    def ChangeStage(self, tLevel, iStage, iStartStage):
        if iStage == PREPAR_STAGE:
            if not iStartStage:
                self.ClearLevelRoomStage(tLevel)
            self.InPreparStage(tLevel)
            iNextStage = THUNDER_STAGE
        elif iStage == THUNDER_STAGE:
            self.InThunderStage(tLevel)
            iNextStage = PREPAR_STAGE
        (iTime, iRandom) = self.m_StageTime[iStage - 1]
        iTime = (iTime + self.m_Game.Random(iRandom + 1)) * 100
        iStartFrame = self.m_Game.GetFrameNum()
        self.m_StageInfo[tLevel] = (iStage, iTime, iStartFrame)
        (iLevel, iRoom) = tLevel
        sKey = 'ChangeStage_%s_%s' % (iLevel, iRoom) + self.m_CallFlag
        func = Functor(self.ChangeStage, tLevel, iNextStage, 0)
        self.Call_Out(func, Time2Frame(iTime), sKey)
        if self.m_FristRoomFlag:
            lstHero = self.m_WarMgr.GetRoomHero()
            self.m_ShowHeroInfo[tLevel] = lstHero
            self.m_FristRoomFlag = 0
        if tLevel not in self.m_ShowHeroInfo:
            return None
        lstHero = self.m_ShowHeroInfo[tLevel]
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iScene = oLevelNode.m_Scene
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            if iScene == oHero.m_Scene:
                self.SendClientStageInfo(oHero, tLevel)
        

    
    def ClearLevelRoomStage(self, tLevel):
        if tLevel in self.m_CurSafeTrap:
            lstCurSafeTrap = self.m_CurSafeTrap.pop(tLevel)
            for oTrap, _, _ in lstCurSafeTrap:
                oTrap.Remove(self.m_CallFlag)
            
        (iLevel, iRoom) = tLevel
        sStartThunderKey = 'StartThunder_%s_%s' % (iLevel, iRoom) + self.m_CallFlag
        sChooseThunderKey = 'ChooseThunder_%s_%s' % (iLevel, iRoom) + self.m_CallFlag
        self.Remove_Call_Out(sStartThunderKey)
        self.Remove_Call_Out(sChooseThunderKey)

    
    def InPreparStage(self, tLevel):
        lstLevleRoomSafePos = self.m_LevleRoomSafePosInfo[tLevel]
        lstSafeInfo = self.ChooesSafeArea(DeepCopy(lstLevleRoomSafePos))
        (iTrap, iPerform) = self.m_Trap
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        (iLevel, _) = tLevel
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        lstCurSafeTrap = self.m_CurSafeTrap.setdefault(tLevel, [])
        for vPos, (SafeRadius, HitRadius) in lstSafeInfo:
            dInfo = {
                'Angle': [
                    0,
                    0,
                    0],
                'Center': [
                    0,
                    0,
                    0],
                'GlobalArea': 0,
                'NextArea': 0,
                'Perfab': 0,
                'SID': iTrap,
                'Scale': [
                    0,
                    0,
                    0],
                'Size': (0, 0, 0),
                'Origin': vPos,
                'Shape': MODEL_TYPE_BOX,
                'Source': OBSTACLE_SOURCE_LEVEL,
                'Live': 0,
                'Perform': [] }
            oTrap = self.m_Game.m_ResMgr.CreateBuild(oLevelNode.m_Scene, iTrap, dInfo)
            oTrap.AddPerform(iPerform, 1)
            lstCurSafeTrap.append((oTrap, SafeRadius, HitRadius))
        

    
    def InThunderStage(self, tLevel):
        self.SendInSafeHeroMsg(tLevel)
        self.StartThunder(tLevel)
        lstHero = self.m_WarMgr.GetRoomHero()
        iNum = len(lstHero)
        if iNum not in self.m_ChooseThunderInfo:
            SendAlert('err', '雷雨天气固定落雷点选择缺少对应玩家人数配置%d' % iNum)
            return None
        (iCnt, iRandom, iTime) = self.m_ChooseThunderInfo[iNum]
        if self.m_Game.Random(100) >= iRandom:
            return None
        if not iTime:
            (_, iStageTotalTime, _) = self.m_StageInfo[tLevel]
            iTime = self.m_Game.Random(iStageTotalTime)
        (iLevel, iRoom) = tLevel
        sKey = 'ChooseThunder_%s_%s' % (iLevel, iRoom) + self.m_CallFlag
        func = Functor(self.ChooseThunderStart, tLevel, iCnt)
        self.Call_Out(func, max(Time2Frame(iTime), 4), sKey)

    
    def ChooseThunderStart(self, tLevel, iCnt):
        if tLevel not in self.m_ShowHeroInfo:
            return None
        lstHero = self.m_ShowHeroInfo[tLevel]
        if not lstHero:
            return None
        lstCanChooseHero = []
        (iLevel, _) = tLevel
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iScene = oLevelNode.m_Scene
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            if iScene != oHero.m_Scene:
                continue
            if self.CheckHeroInSafeArea(oHero, tLevel):
                continue
            lstCanChooseHero.append(oHero)
        
        if not lstCanChooseHero:
            return None
        lstAllSafeTrapInfo = self.m_CurSafeTrap[tLevel]
        tSafeTrapInfo = lstAllSafeTrapInfo[0]
        (oTriggerTrap, _, _) = tSafeTrapInfo
        (_, iPerform) = self.m_Trap
        for _ in range(iCnt):
            oHero = lstCanChooseHero[self.m_Game.Random(len(lstCanChooseHero))]
            oPerform = oTriggerTrap.m_Perform.GetPerform(iPerform)
            dData = {
                'Custom': {
                    'vStart': oHero.GetPos() } }
            cl_war.UsePerform(oTriggerTrap, oPerform, dData)
        

    
    def SendInSafeHeroMsg(self, tLevel):
        if tLevel not in self.m_ShowHeroInfo:
            return None
        lstHero = self.m_ShowHeroInfo[tLevel]
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero, PY_FLAG_DEAD)
            if not oHero:
                continue
            if self.CheckHeroInSafeArea(oHero, tLevel):
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HEROINSAFE, oHero, { })
        

    
    def CheckHeroInSafeArea(self, oHero, tLevel):
        lstAllSafeTrapInfo = self.m_CurSafeTrap[tLevel]
        if not lstAllSafeTrapInfo:
            return False
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        (iLevel, _) = tLevel
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iScene = oLevelNode.m_Scene
        if iScene != oHero.m_Scene:
            return False
        vHeroPos = oHero.GetPos()
        for oTriggerTrap, fSafeRadius, _ in lstAllSafeTrapInfo:
            if cl_math.CheckDistance(oTriggerTrap.GetPos(), vHeroPos, fSafeRadius):
                return True
        
        return False

    
    def StartThunder(self, tLevel):
        (_, iPerform) = self.m_Trap
        (iTime, iCnt, ThunderRadius) = self.m_ThunderInfo
        iEachAngle = 360 // CHOOSE_DIR_TIMES
        lstAllSafeTrapInfo = self.m_CurSafeTrap[tLevel]
        vThunderPos = None
        for _ in range(CHOOSE_RANDOM_TIMES):
            tSafeTrapInfo = lstAllSafeTrapInfo[self.m_Game.Random(len(lstAllSafeTrapInfo))]
            (oTriggerTrap, SafeRadius, HitRadius) = tSafeTrapInfo
            vCenterPos = oTriggerTrap.GetPos()
            vFace = (1, 0, 0)
            iNum = self.m_Game.Random(CHOOSE_DIR_TIMES) + 1
            iMinAngle = (iNum - 1) * iEachAngle
            iMaxAngle = iNum * iEachAngle
            if iMinAngle >= 180:
                iMinAngle -= 180
                iMaxAngle -= 180
                vFace = (-1, 0, 0)
            vThunderPos = self.m_Game.Scene_RandomPointSectorInMesh(oTriggerTrap.m_Scene, vCenterPos, vFace, SafeRadius + ThunderRadius, HitRadius, iMinAngle, iMaxAngle)
            if vThunderPos:
                iCnt -= 1
                oPerform = oTriggerTrap.m_Perform.GetPerform(iPerform)
                dData = {
                    'Custom': {
                        'vStart': vThunderPos } }
                cl_war.UsePerform(oTriggerTrap, oPerform, dData)
            if not iCnt:
                break
        
        (iLevel, iRoom) = tLevel
        sKey = 'StartThunder_%s_%s' % (iLevel, iRoom) + self.m_CallFlag
        func = Functor(self.StartThunder, tLevel)
        self.Call_Out(func, Time2Frame(iTime), sKey)

    
    def ChooesSafeArea(self, lstLevleRoomSafePos):
        (iCnt, iRandom) = self.m_ChooseSafeNum
        iCnt = iCnt + self.m_Game.Random(iRandom + 1)
        lstCurSafeInfo = []
        if iCnt > len(lstLevleRoomSafePos):
            iCnt = len(lstLevleRoomSafePos)
        for _ in range(iCnt):
            lstInfo = lstLevleRoomSafePos[self.m_Game.Random(len(lstLevleRoomSafePos))]
            lstCurSafeInfo.append(lstInfo)
            lstLevleRoomSafePos.remove(lstInfo)
        
        return lstCurSafeInfo



def GetComponentClass(oMgrManager):
    return CThunderstormElement

