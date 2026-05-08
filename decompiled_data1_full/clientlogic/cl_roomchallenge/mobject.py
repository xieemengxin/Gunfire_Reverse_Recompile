# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_roomchallenge/mobject.pyc
# RelativePath: clientlogic/cl_roomchallenge/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import WARRIOR_HERO, CHALLENGE_DEFEND, NWARRIOR_DROP_EQUIP, CHALLENGE_NOTIFY, MODEL_TYPE_SPHERE, CURWEAPON_SWITCH, CHALLENGE_SIGHT, CHALLENGE_DICESEASON_APPENDSKILL, CHALLENGE_COUNT_MUTANTMONSTER
from cl_commondefines import INTERACT_TYPE_FORBID, INTERACT_TYPE_ALLOW, OBSTACLE_SOURCE_LEVEL, MODEL_TYPE_BOX, CHALLENGE_LIMITLIVE, CHALLENGE_LIMITDEFEND, CHALLENGE_LIMITTIME
from cl_commondefines import CHALLENGE_TRAP, CHALLENGE_LIMITCONVOY, CHASTATUS_FAILED, CHALLENGE_NOTIFYLIMITTIME, CHASTATUS_FAILED, CHALLENGE_PLAYERPERFORM, CHALLENGE_ABERRANCE, CHALLENGE_APPENDSKILL
from cl_commondefines import CHALLENGE_ELITE, SIDE_TYPE_MONSTER, WARRIOR_ELITE, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_HATESEARCH, MONSTERAI_TYPE_DEFAULT, CHALLENGE_EXTRAMONSTER, SIDE_TYPE_MONSTER
from cl_commondefines import PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_HATESEARCH, MONSTERAI_TYPE_DEFAULT, PARAM_LEVEL_MEDIUM_HIGH, CHALLENGE_KILLSUMMON, CHALLENGE_BOXMONSTER, WARRIOR_MONSTER, WARRIOR_BUILD, WARRIOR_NORPART, WARRIOR_ELIPART
from cl_commondefines import STATE_TIME_LIMIT, MG_SOURCE_KILLMONSTER, CHASTATUS_OVER, CHASTATUS_WAIT, CHASTATUS_SUCCESS, CHASTATUS_CONTINUE, TRANSFER_DIRTO_MAIN, CHALLENGE_SUPERMONSTER, CHALLENGE_EXTRAELITE
from cl_commondefines import MG_EQUIP, STATE_DEFENDNPC, STATE_TIME_FOREVER, WARRIOR_BOSS, HIDELV_TYPE_ELITE, CHALLENGE_ELITEINTRUDE, CHALLENGE_MORALE_ELITEINTRUDE, CHALLENGE_BOXFLASH, WARRIOR_NORFLY
from cl_commondefines import MODE_RIDINGALONE, BENE_SOURCE_TEMP, STATUS_JUMP, DAM_TYPE_SCENE, DAM_USE_HP, CHALLENGE_KILLSUMMON_TRAP, CHALLENGE_OBSTACLEALIENATION, PARAM_LEVEL_CLOSE_HIGH, MONSTERAI_TYPE_AREAMOVE, HP_RADIO_SUB, CHALLENGE_SEASONELITEINTRUDE, DICE_SEASONCHALLENGE_UI
from cl_commondefines import MG_DICE, MAX_LAYER, BACKPACK_SEASONCHALLENGE_UI, MUTANT_ARG_CHANGE, MUTANT_NUM_CHANGE, WARRIOR_NORBADGER
from cl_only import SendAlert, Time2Frame, Frame2Time, Functor, PY_FLAG_DEAD, ChooseKey, ChooseRange, GetRandomCard, PY_FLAG_DIED
from cl_resmgr.aitempparam import GetAIConfParam
from cl_object.logging import LevelLog
from cl_resmgr import GetMonsterPower
from cl_pxlayer import PXMASK_BLOCK
from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON, ALL_BULLET
from cl_pxlayer import PXLAYER_DEVENT, PXMASK_GROUNDBLK
from cl_warmgr.levelline.linespawnaction import SpanwTriggerWindDie
from cl_cscommondef import DICE_QUALITY_LOW, DICE_QUALITY_RARE, DICE_QUALITY_TALE
import cl_msgcenter
import cl_notify
import cl_reward
import cl_item
import cl_snetwar
import cl_state
import cl_object
import cl_war
import cl_math
import cl_forbid
import cl_world
import cl_engphyobj
import cl_formula
import cl_newformula
ROOMCHALLENGE_UI_OPT_OVER = 0
ROOMCHALLENGE_UI_OPT_START = 1
ROOMCHALLENGE_UI_OPT_UPDATE = 2

class CBaseChallenge(object):
    m_SID = 0
    m_Type = 0
    m_ChallengeName = ''
    m_ChallengeNotify = ''
    m_SuccessNotify = ''
    m_FailedNotify = ''
    m_RewardNpc = 0
    m_EffectState = 0
    m_Reward = { }
    
    def __init__(self, oParent, oLevelNode, iRoomPos):
        self.m_Parent = oParent
        self.m_LevelNode = oLevelNode
        self.m_Game = oLevelNode.m_Game
        self.m_RoomPos = iRoomPos
        self.m_Status = CHASTATUS_WAIT
        self.m_bHaveEnterRoomEvent = False
        self.m_CollectData = { }

    
    def Init(self, clsData, dAddData):
        self.m_SID = clsData.m_SID
        oLevelNode = self.m_LevelNode
        self.m_Key = 'RCLG%s-%s-%s-%s-%s' % (self.m_SID, oLevelNode.m_LayerNum, oLevelNode.m_LevelNum, oLevelNode.m_Level, self.m_RoomPos)
        self.m_Status = CHASTATUS_CONTINUE
        self.m_Reward = clsData.m_Reward
        self.m_EffectState = clsData.m_EffectState
        self.m_ChallengeName = clsData.m_ChallengeName
        self.m_ChallengeNotify = clsData.m_ChallengeNotify
        self.m_SuccessNotify = clsData.m_SuccessNotify
        self.m_FailedNotify = clsData.m_FailedNotify
        lstPlayer = self.GetScenePlayers()
        sReason = dAddData['Reason'] if 'Reason' in dAddData else ''
        LevelLog.Info('%s players%s challenge:%s %s init levelid:%d roompos%d' % (self.m_Game.m_ID, lstPlayer, self.m_SID, sReason, self.m_LevelNode.m_Level, self.m_RoomPos))

    
    def Release(self):
        lstPlayer = self.GetScenePlayers()
        LevelLog.Info('%s players%s challenge:%s release rlt:%d levelid:%d roompos%d' % (self.m_Game.m_ID, lstPlayer, self.m_SID, self.m_Status, self.m_LevelNode.m_Level, self.m_RoomPos))
        self.m_Parent.ChallengeRelease(self.m_LevelNode.m_Level, self.m_RoomPos)
        self.m_Parent = None
        self.m_LevelNode = None
        self.m_Game = None

    
    def SetEnterRoomTiming(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        iRound = self.m_Game.m_WarMgr.m_Round
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        lstRoomList = self.m_LevelNode.m_RoomList
        oLineLst = lstRoomList[self.m_RoomPos]
        self.m_bHaveEnterRoomEvent = False
        for oLine in oLineLst:
            sLine = oLine.m_Name
            lstSpawnRule = oLevelConfData.GetLineSpawnRule(self.m_LevelNode.m_Level, sLine, iRound)
            for dSpawn in lstSpawnRule:
                tAction = dSpawn['Action']
                for dAction in tAction:
                    if dAction['type'] == 'EnterRoom':
                        self.m_bHaveEnterRoomEvent = True
                        break
                
            
        
        if self.m_bHaveEnterRoomEvent:
            cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_WAR_ENTERROOM, self.CheckEnterRoom, self.m_Key, -1, 0)
        else:
            self.CheckEnterRoom(oLevelCtrl, {
                'Level': self.m_LevelNode.m_Level })

    
    def ReleaseEnterRoomEvent(self):
        if self.m_bHaveEnterRoomEvent:
            oLevelCtrl = self.m_Parent.m_LevelCtrl
            cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_WAR_ENTERROOM, self.m_Key)

    
    def CheckEnterRoom(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iCurLevel = self.m_LevelNode.m_Level
        if iLevel != iCurLevel:
            return None
        self.OnEnterRoom(oLevelCtrl, dMsgInfo)

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        pass

    
    def GetScenePlayers(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        if not oScene:
            return []
        return oScene.GetPlayers()

    
    def GetSceneHero(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        if not oScene:
            return []
        return oScene.GetHeros()

    
    def ChallengeNotify(self, lstPlayer, iTime, sRplMsg, dReplace):
        cl_notify.SendCommonNotifyNoTransfer(self.m_Game, lstPlayer, iTime, sRplMsg, dReplace)

    
    def OnChallengeOverNotify(self, lstPlayer):
        if self.m_Status == CHASTATUS_SUCCESS:
            self.ChallengeNotify(lstPlayer, 500, self.m_SuccessNotify, { })
        else:
            self.ChallengeNotify(lstPlayer, 500, self.m_FailedNotify, { })

    
    def StartChallenge(self):
        pass

    
    def SendStartMsg(self):
        dData = {
            'LevelID': self.m_LevelNode.m_Level,
            'Room': self.m_RoomPos,
            'Type': self.m_Type }
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMCHALLENGESTART, oLevelCtrl, dData)

    
    def CheckChallengeStatus(self):
        return CHASTATUS_SUCCESS

    
    def CheckRoundReward(self, oGame, dReward):
        iRound = oGame.m_WarMgr.m_Round
        if iRound not in dReward:
            SendAlert('err', '未配置战场%d挑战%s周目%d掉落' % (oGame.m_WarMgr.m_SID, self.m_ChallengeName, iRound))
            iRound = sorted(dReward)[0]
        return dReward[iRound]

    
    def ChallengeOver(self, dParam):
        iStatus = self.CheckChallengeStatus()
        if iStatus in (CHASTATUS_WAIT, CHASTATUS_CONTINUE, CHASTATUS_OVER):
            return None
        self.m_Status = iStatus
        lstPlayer = self.GetScenePlayers()
        LevelLog.Info('%s players%s challenge:%s over rlt:%d levelid:%d roompos%d' % (self.m_Game.m_ID, lstPlayer, self.m_SID, self.m_Status, self.m_LevelNode.m_Level, self.m_RoomPos))
        if iStatus == CHASTATUS_SUCCESS:
            self.Reward(dParam)
        self.OnChallengeOverNotify(lstPlayer)
        dData = {
            'SID': self.m_SID,
            'Key': self.m_Key,
            'Rlt': self.m_Status == CHASTATUS_SUCCESS,
            'LevelID': self.m_LevelNode.m_Level,
            'Room': self.m_RoomPos,
            'Type': self.m_Type,
            'OtherInfo': dParam,
            'Scene': self.m_LevelNode.m_Scene,
            'Reward': self.m_Reward,
            'LevelType': self.m_LevelNode.m_LevelType,
            'Status': self.m_Status }
        oLevelCtrl = self.m_LevelNode.m_CtrlMgr
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, oLevelCtrl, dData)
        self.OnChallengeOver()
        self.m_Status = CHASTATUS_OVER
        self.Release()

    
    def OnChallengeOver(self):
        lstPlayer = self.GetScenePlayers()
        dReplace = self.GetReplaceInfo()
        cl_notify.ClearCommonNotifyNoTransfer(self.m_Game, lstPlayer, self.m_ChallengeNotify, dReplace)

    
    def Reward(self, dParam):
        if self.m_Status != CHASTATUS_SUCCESS:
            return None
        self.OnReward(dParam)

    
    def OnReward(self, dParam):
        if self.m_Reward:
            SendAlert('err', 'roomchallenge:%d 配了奖励，但无效果。请联系程序处理。' % self.m_SID)

    
    def HeroReEnterScene(self, lstPlayer):
        if self.m_Status not in (CHASTATUS_OVER, CHASTATUS_WAIT):
            self.RateNotify(lstPlayer)

    
    def RateNotify(self, lstPlayer):
        dReplace = self.GetReplaceInfo()
        self.ChallengeNotify(lstPlayer, 600000, self.m_ChallengeNotify, dReplace)
        cl_snetwar.GS2CStartChallenge(self.m_Game, self.m_Type, 0, self.m_ChallengeNotify, dReplace, lstPlayer)

    
    def GetReplaceInfo(self):
        return { }

    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        return True

    ValidCreate = classmethod(ValidCreate)


class CMonsterChallenge(CBaseChallenge):
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.OnPreRoomGoal, self.m_Key, -1, 0)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.OnCreateMonster, self.m_Key, -1, 0)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self.OnExecuteDieBefore, self.m_Key)
        self.m_LastMonsterInfo = { }
        self.m_GoalTrigger = False

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self.m_Key)
        super(CMonsterChallenge, self).Release()

    
    def OnPreRoomGoal(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoomPos = dMsgInfo['Room']
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
        self.m_GoalTrigger = True
        self.CustomRoomGoal()

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        pass

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        pass

    
    def OnExecuteDieBefore(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        if oVictim.m_MoveCtrl and oVictim.m_MoveCtrl.m_CurStatus == STATUS_JUMP:
            tPos = oVictim.m_MoveCtrl.m_JumpStart
        else:
            tPos = oVictim.GetPos()
        self.m_LastMonsterInfo = {
            'VID': oVictim.m_ID,
            'AID': dMsgInfo['AID'],
            'Pos': tPos,
            'Facing': oVictim.GetFacing() }

    
    def OnReward(self, dParam):
        if not dParam:
            return None
        iVictim = dParam['VID']
        oGame = self.m_Game
        oVictim = oGame.GetObject(iVictim)
        if oVictim:
            iAttack = dParam['AID']
            iRewarder = oVictim.Query('Rewarder', 0)
            if iRewarder:
                oRewarder = oGame.GetObject(iRewarder)
                if oRewarder and oRewarder.m_FightType & WARRIOR_HERO:
                    iAttack = iRewarder
            oAttack = oGame.GetObject(iAttack)
            if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
                dHero = self.GetSceneHero()
                if not dHero:
                    return None
                iAttack = ChooseKey(oGame, dHero)
            dReward = self.m_Reward
            self.m_Reward = { }
            if not dReward:
                return None
            iRound = oGame.m_WarMgr.m_Round
            if iRound not in dReward:
                SendAlert('err', '未配置战场%d挑战%s周目%d掉落' % (oGame.m_WarMgr.m_SID, self.m_ChallengeName, iRound))
                iRound = sorted(dReward)[0]
            dReward = dReward[iRound]
            iFlag = 0
            if oVictim.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
                iFlag = 1
            dExtInfo = {
                'CalOffset': 0,
                'CheckGoldenCup': 1,
                'CanReward': iFlag,
                'AutoReward': iFlag }
            dMGInfo = cl_reward.RewardItemByMiniGame(oVictim, iAttack, dReward, 'ChallengeReward%d' % iAttack, MG_SOURCE_KILLMONSTER, dExtInfo)
            oLevelCtrl = self.m_Parent.m_LevelCtrl
            dStaticInfo = { }
            dMsgInfo = {
                'MGInfo': dMGInfo,
                'Key': self.m_Key,
                'Scene': self.m_LevelNode.m_Scene,
                'ChallengeType': self.m_Type,
                'ChallengeSID': self.m_SID,
                'StaticInfo': dStaticInfo }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, oLevelCtrl, dMsgInfo)
            cl_reward.CreateDemon(oGame, iVictim, dMGInfo, dStaticInfo = dStaticInfo)

    
    def CustomRoomGoal(self):
        self.ChallengeOver(self.m_LastMonsterInfo)

    
    def AddEffectState(self, iMonster):
        oMonster = self.m_Game.GetObject(iMonster)
        if not oMonster or not (self.m_EffectState):
            return None
        dArgs = {
            'AID': oMonster.m_ID,
            'RS': cl_object.reason.CStrReason('RoomChallenge'),
            'arg': { } }
        return cl_state.AddState(oMonster, self.m_EffectState, STATE_TIME_FOREVER, 0, dArgs)

    
    def CheckMonsterDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if self.m_Status != CHASTATUS_CONTINUE:
            return False
        if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
            return False
        if oVictim.m_FightType == WARRIOR_NORPART or oVictim.m_FightType == WARRIOR_ELIPART:
            return False
        tLineIdx = oVictim.m_LineIdx
        if not tLineIdx or tLineIdx[0] != self.m_LevelNode.m_Level or tLineIdx[1] != self.m_RoomPos:
            return False
        return True

    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return False
        if iRoomPos >= len(oLevelNode.m_RoomList):
            return False
        for oLineNode in oLevelNode.m_RoomList[iRoomPos]:
            oMonsterCtrl = oLineNode.m_MonsterCtrl
            if not oMonsterCtrl.IsMonsterAllDie():
                return True
        
        return False

    ValidCreate = classmethod(ValidCreate)


class CBoxMonsterChallenge(CBaseChallenge):
    m_Type = CHALLENGE_BOXMONSTER
    m_ChallengeName = '宝箱怪挑战'
    m_Time = 0
    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        sid = clsData.m_Param[0]
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return False
        oScene = oGame.m_SceneMgr.GetScene(oLevelNode.m_Scene)
        lstObj = oScene.GetObjectsByType('Monster')
        for iTarget in lstObj:
            oTarget = oGame.GetObject(iTarget)
            if not oTarget or oTarget.m_SID != sid:
                continue
            dParam['BoxMonster'] = iTarget
            return True
        
        SendAlert('err', '场内不存在宝箱怪%d关卡%d房间挑战%d创建失败' % (sid, oLevelNode.m_Level, clsData.m_SID))
        return False

    ValidCreate = classmethod(ValidCreate)
    
    def Init(self, clsData, dAddData):
        super(CBoxMonsterChallenge, self).Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_DelayStartTime = clsData.m_Param[1]
        self.m_Time = clsData.m_Param[2]
        self.m_NotifyDie = cl_notify.GetCommonNotifyMsg(clsData.m_Param[3])
        self.m_HPRatio = clsData.m_Param[4]
        self.m_NotifyUp = cl_notify.GetCommonNotifyMsg(clsData.m_Param[5])
        self.m_NotifyDown = cl_notify.GetCommonNotifyMsg(clsData.m_Param[6])
        self.m_DieRemoveDelay = clsData.m_Param[7]
        self.m_EscapeRemoveDelay = clsData.m_Param[8]
        self.m_ChallengeFrame = Time2Frame(self.m_Time)
        self.m_BoxMonster = dAddData['BoxMonster']
        oTarget = self.m_Game.GetObject(self.m_BoxMonster)
        if oTarget:
            if self.m_EscapeRemoveDelay:
                oTarget.m_RemoveDelay = Time2Frame(self.m_EscapeRemoveDelay)
            oTarget.Set('ChallengeTime', self.m_Time)
        oLevelCtrl.Call_Out(self.OnStart, Time2Frame(self.m_DelayStartTime), self.m_Key + 'Start')
        self.m_StartFrame = 0

    
    def OnStart(self):
        self.m_StartFrame = self.m_Game.GetFrameNum()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIEDIST, self.OnEndAheadTime, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnEndAheadTime, self.m_Key)
        func = Functor(self.ChallengeOver, { })
        oLevelCtrl.Call_Out(func, self.m_ChallengeFrame, self.m_Key)
        self.RateNotify(self.GetScenePlayers())
        self.SendStartMsg()

    
    def ChallengeOver(self, dParam):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        dInfo = { }
        oTarget = self.m_Game.GetObject(self.m_BoxMonster)
        if oTarget:
            dInfo['targetHP'] = oTarget.m_HP
            dInfo['targetHPMax'] = oTarget.QueryAttr('HPMax')
            dInfo['Pos'] = oTarget.GetPos()
        if not dParam.get('EndAheadTime', 0):
            dInfo['passTime'] = Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame)
        dInfo.update(dParam)
        super(CBoxMonsterChallenge, self).ChallengeOver(dInfo)

    
    def OnEndAheadTime(self, oLevelCtrl, oTarget, dInfo):
        if self.CheckLastPlayerDead(oTarget.m_ID):
            self.ChallengeOver({
                'EndAheadTime': 1 })

    
    def CheckLastPlayerDead(self, iTarget):
        lstHero = self.m_Game.m_WarMgr.GetRoomHero()
        if iTarget not in lstHero:
            return False
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if oHero and not oHero.IsRealDied():
                return False
        
        return True

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if oVictim.m_ID != self.m_BoxMonster:
            return None
        oTarget = self.m_Game.GetObject(self.m_BoxMonster)
        if oTarget and self.m_DieRemoveDelay:
            oTarget.m_RemoveDelay = Time2Frame(self.m_DieRemoveDelay)
        self.ChallengeOver({ })

    
    def ClearAttention(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'Start')
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIEDIST, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Key)

    
    def OnChallengeOver(self):
        oBoxMonster = self.m_Game.GetObject(self.m_BoxMonster)
        if oBoxMonster:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, oBoxMonster, { })
        super().OnChallengeOver()
        oTarget = self.m_Game.GetObject(self.m_BoxMonster)
        if oTarget:
            oTarget.DieRemove()

    
    def Release(self):
        self.ClearAttention()
        super().Release()

    
    def CheckChallengeStatus(self):
        if self.m_Status == CHASTATUS_OVER:
            return self.m_Status
        return CHASTATUS_SUCCESS

    
    def OnChallengeOverNotify(self, lstPlayer):
        super().OnChallengeOverNotify(lstPlayer)
        if self.m_Status == CHASTATUS_SUCCESS:
            oTarget = self.m_Game.GetObject(self.m_BoxMonster)
            if not oTarget or oTarget.m_HP == 0:
                self.ChallengeNotify(lstPlayer, 500, self.m_NotifyDie, { })
            elif self.GetBoxMonsterHPRatio(oTarget) > self.m_HPRatio:
                self.ChallengeNotify(lstPlayer, 500, self.m_NotifyUp, { })
            else:
                self.ChallengeNotify(lstPlayer, 500, self.m_NotifyDown, { })

    
    def GetBoxMonsterHPRatio(self, oTarget):
        return oTarget.m_HP * 100 // oTarget.QueryAttr('HPMax')

    
    def RateNotify(self, lstPlayer):
        if not self.m_StartFrame:
            return None
        iRemainTime = Frame2Time(self.m_ChallengeFrame + self.m_StartFrame - self.m_Game.GetFrameNum())
        dReplace = self.GetReplaceInfo()
        self.ChallengeNotify(lstPlayer, iRemainTime, self.m_ChallengeNotify, dReplace)
        cl_snetwar.GS2CStartChallenge(self.m_Game, self.m_Type, iRemainTime, self.m_ChallengeNotify, dReplace, lstPlayer)

    
    def GetReplaceInfo(self):
        iRemainTime = Frame2Time(self.m_ChallengeFrame + self.m_StartFrame - self.m_Game.GetFrameNum())
        return {
            '$remain': str(iRemainTime),
            '$total': str(self.m_Time) }



class CKillSummonChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_KILLSUMMON
    m_ChallengeName = '杀戮召唤'
    
    def Init(self, clsData, dAddData):
        super(CKillSummonChallenge, self).Init(clsData, dAddData)
        self.m_ChooseData = clsData.m_Param[0]
        self.m_SpawnMonster = []
        self.m_KillMonster = []
        self.m_Status = CHASTATUS_WAIT
        self.SetEnterRoomTiming()
        self.m_LevelMonster = []
        self.m_IsHideLevelElite = 0
        iHideType = 0
        iHideLevel = dAddData['LevelID']
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl:
            iHideType = oLevelCtrl.m_HideLevelLib.get(iHideLevel, 0)
        if iHideType != HIDELV_TYPE_ELITE:
            self.m_LevelNode.LockRoom(self.m_RoomPos, 'KillSummonChallenge')
        else:
            self.m_IsHideLevelElite = 1

    
    def Release(self):
        self.m_SpawnMonster = []
        self.m_KillMonster = []
        self.m_LevelMonster = []
        self.ReleaseEnterRoomEvent()
        super(CKillSummonChallenge, self).Release()

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        if oVictim.m_ID in self.m_SpawnMonster or oVictim.m_ID not in self.m_KillMonster:
            self.m_KillMonster.append(oVictim.m_ID)
        elif oVictim.m_ID in self.m_LevelMonster:
            if self.m_IsHideLevelElite and self.m_GoalTrigger:
                return None
            tPos = self.m_LastMonsterInfo['Pos'] if 'Pos' in self.m_LastMonsterInfo else oVictim.GetPos()
            if cl_math.IsZero(tPos):
                tLastPos = self.m_LastMonsterInfo['Pos'] if 'Pos' in self.m_LastMonsterInfo else ()
                tInfo = (oVictim.m_InitScene, oVictim.m_Scene, oVictim.GetPos(), tLastPos)
                LevelLog.Alert('%s challenge:%s levelid:%d roompos%d zero pos %s' % (self.m_Game.m_ID, self.m_SID, self.m_LevelNode.m_Level, self.m_RoomPos, tInfo))
                return None
            tFace = oVictim.GetFacing()
            vFixDropPos = oVictim.Query('FixDropPos', None)
            iLineIdx = oVictim.m_LineIdx
            iMonsterSID = ChooseKey(oVictim.m_Game, self.m_ChooseData)
            oLevelCtrl = self.m_Parent.m_LevelCtrl
            oLevelCtrl.Call_Out(Functor(self.DelaySpawnMonster, iMonsterSID, tPos, tFace, iLineIdx, vFixDropPos), 1, self.m_Key + 'DelaySpawn')
        self.ChallengeOver(self.m_LastMonsterInfo)

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_Status = CHASTATUS_CONTINUE
        self.RateNotify(self.GetScenePlayers())

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        iMonsterID = dMsgInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonsterID)
        iExcludeMonster = 24011
        if oMonster:
            if oMonster.m_SID == iExcludeMonster or oMonster.m_FightType == WARRIOR_NORFLY:
                return None
        tLineIdx = dMsgInfo['LineIdx']
        if not tLineIdx:
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        self.m_LevelMonster.append(iMonsterID)
        self.AddEffectState(iMonsterID)

    
    def DelaySpawnMonster(self, iMonsterSID, tPos, tFace, iLineIdx, vFixDropPos):
        if (not (self.m_Game) or self.m_IsHideLevelElite) and self.m_GoalTrigger:
            return None
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        oMonster = self.m_Game.m_ResMgr.CreateMonster(self.m_LevelNode.m_Scene, iMonsterSID, tPos, tFace, SIDE_TYPE_MONSTER, 0, dAI, iLineIdx)
        if not oMonster:
            iWarNo = self.m_Game.m_WarMgr.m_SID
            SendAlert('err', '战场%d 地图%d 关卡%d 未配置怪物SID%d' % (iWarNo, self.m_LevelNode.m_Map, self.m_LevelNode.m_Level, iMonsterSID))
        elif not oMonster.IsDead():
            oMonster.Set('FixDropPos', vFixDropPos)
            self.m_SpawnMonster.append(oMonster.m_ID)

    
    def CheckChallengeStatus(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        if oLevelCtrl.Find_Call_Out(self.m_Key + 'DelaySpawn'):
            return CHASTATUS_CONTINUE
        if self.m_GoalTrigger and len(self.m_SpawnMonster) == len(self.m_KillMonster):
            return CHASTATUS_SUCCESS
        return CHASTATUS_CONTINUE

    
    def OnChallengeOver(self):
        super(CKillSummonChallenge, self).OnChallengeOver()
        if self.m_Status == CHASTATUS_SUCCESS:
            self.m_LevelNode.UnlockRoom(self.m_RoomPos, 'KillSummonChallenge')

    
    def CustomRoomGoal(self):
        if self.m_IsHideLevelElite:
            oLevelCtrl = self.m_Parent.m_LevelCtrl
            self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
            oReason = cl_object.reason.CStrReason('RoomGoalAction', None, {
                'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
            for iMonsterID in self.m_SpawnMonster:
                if iMonsterID not in self.m_KillMonster:
                    oMonster = self.m_Game.GetObject(iMonsterID, PY_FLAG_DEAD)
                    if oMonster:
                        oMonster.HPModifyDam(0, [
                            [
                                oMonster.HP(),
                                oReason]])
                    self.m_KillMonster.append(iMonsterID)
            
            self.m_Parent.m_LevelCtrl.Remove_Call_Out(self.m_Key + 'DelaySpawn')
        self.ChallengeOver(self.m_LastMonsterInfo)



class CExtraMonsterChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_EXTRAMONSTER
    m_ChallengeName = '额外怪物'
    m_MonsterSID = 0
    
    def Init(self, clsData, dAddData):
        super(CExtraMonsterChallenge, self).Init(clsData, dAddData)
        self.m_MonsterSID = clsData.m_Param[0]
        self.m_EliteID = 0
        self.m_ElitePos = None
        self.m_EliteDrop = None
        oLevelConfData = self.m_Parent.m_LevelCtrl.m_LevelConfData
        (self.m_ElitePos, self.m_EliteDrop) = self.m_LevelNode.GetEliteInfo(self.m_RoomPos, oLevelConfData)
        self.m_LevelNode.LockRoom(self.m_RoomPos, 'ExtraMonsterChallenge')

    
    def Release(self):
        self.m_Parent.m_LevelCtrl.Remove_Call_Out(self.m_Key)
        super(CExtraMonsterChallenge, self).Release()

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if not oVictim or oVictim.m_ID != self.m_EliteID:
            return None
        if oVictim.m_Reward:
            dReward = oVictim.m_Reward
            oVictim.m_Reward = { }
            self.m_Reward.update(dReward)
        self.ChallengeOver(self.m_LastMonsterInfo)

    
    def CreateMonsterInfo(self):
        if self.m_ElitePos:
            oLineNode = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
            tPos = self.m_ElitePos
            tFace = oLineNode.m_MonsterCtrl.GetMonsterFacing(tPos)
        else:
            tPos = self.m_LastMonsterInfo['Pos']
            tFace = self.m_LastMonsterInfo['Facing']
        tLineIdx = (self.m_LevelNode.m_Level, self.m_RoomPos, 0)
        (ret, tPos2) = self.m_Game.Scene_GetSpace(self.m_LevelNode.m_Scene, tPos)
        if ret:
            tPos = tPos2
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        iScene = self.m_LevelNode.m_Scene
        dInfo = {
            'Pos': tPos,
            'Face': tFace,
            'AI': dAI,
            'tLineIdx': tLineIdx,
            'Scene': iScene }
        return dInfo

    
    def CustomRoomGoal(self):
        if not (self.m_GoalTrigger) or not (self.m_LastMonsterInfo):
            return None
        dInfo = self.CreateMonsterInfo()
        iScene = self.m_LevelNode.m_Scene
        oGame = self.m_Game
        oWarData = oGame.m_WarData
        clsMonsterData = oWarData.GetMonsterData(self.m_MonsterSID)
        iDelayFrame = clsMonsterData.GetCreateDelayFrame()
        iEffectSID = clsMonsterData.m_CreateEffect
        if iEffectSID:
            iEffectID = oGame.NewNoSceneObjID()
            cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, dInfo['Pos'], self.GetScenePlayers())
        if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
        self.RateNotify(self.GetScenePlayers())
        if iDelayFrame:
            func = Functor(self.DelayCreateMonster, dInfo)
            self.m_Parent.m_LevelCtrl.Call_Out(func, iDelayFrame, self.m_Key)
        else:
            self.DelayCreateMonster(dInfo)

    
    def DelayCreateMonster(self, dInfo):
        oGame = self.m_Game
        iID = oGame.NewNPCID()
        dExtInfo = {
            'ID': iID }
        self.m_EliteID = iID
        if self.m_EliteDrop:
            dExtInfo['SetInfo'] = {
                'FixDropPos': self.m_EliteDrop['FixDropPos'],
                'CheckDropInfo': self.m_EliteDrop['CheckDropInfo'] }
        oMonster = oGame.m_ResMgr.CreateMonster(dInfo['Scene'], self.m_MonsterSID, dInfo['Pos'], dInfo['Face'], SIDE_TYPE_MONSTER, 0, dInfo['AI'], dInfo['tLineIdx'], dExtInfo)
        if not oMonster:
            iWarNo = oGame.m_WarMgr.m_SID
            SendAlert('err', '战场%d 地图%d 关卡%d 未配置怪物SID%d' % (iWarNo, self.m_LevelNode.m_Map, self.m_LevelNode.m_Level, self.m_MonsterSID))
        if oMonster.IsDead():
            return None
        self.AddEffectState(oMonster.m_ID)

    
    def RateNotify(self, lstPlayer):
        if not self.m_GoalTrigger:
            return None
        super(CExtraMonsterChallenge, self).RateNotify(lstPlayer)

    
    def OnChallengeOver(self):
        super(CExtraMonsterChallenge, self).OnChallengeOver()
        if self.m_Status == CHASTATUS_SUCCESS:
            self.m_LevelNode.UnlockRoom(self.m_RoomPos, 'ExtraMonsterChallenge')



class CEliteChallenge(CBaseChallenge):
    m_Type = CHALLENGE_ELITE
    m_ChallengeName = '精英怪物'
    m_MonsterSID = 0
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.OnPreRoomGoal, self.m_Key, -1, 0)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self.OnExecuteDieBefore, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        self.m_LevelNode.LockRoom(self.m_RoomPos, 'EliteChallenge')
        self.m_LastMonsterInfo = { }
        self.m_GoalTrigger = False
        self.m_MonsterSID = clsData.m_Param[0]
        self.m_EliteID = 0
        self.m_ElitePos = None
        self.m_EliteDrop = None
        iMin = clsData.m_Param[1]
        iMax = clsData.m_Param[2]
        dMonsterInfo = self.m_LevelNode.GetRoomMonsterInfo(self.m_RoomPos)
        iTotal = sum(dMonsterInfo.values())
        iMin = int(iTotal * iMin / 100)
        iMax = int(iTotal * iMax / 100)
        iTargetNum = self.m_Game.Random((iMax - iMin) + 1) + iMin
        self.m_TargetNum = min(iTotal, iTargetNum)
        self.m_TargetNum = max(1, self.m_TargetNum)
        oLevelConfData = oLevelCtrl.m_LevelConfData
        (self.m_ElitePos, self.m_EliteDrop) = self.m_LevelNode.GetEliteInfo(self.m_RoomPos, oLevelConfData)

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self.m_Key)
        super().Release()

    
    def OnPreRoomGoal(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoomPos = dMsgInfo['Room']
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
        self.m_GoalTrigger = True
        LevelLog.Debug('%s challenge:%s goaltrigger levelid:%d roompos%d' % (self.m_Game.m_ID, self.m_SID, self.m_LevelNode.m_Level, self.m_RoomPos))

    
    def OnExecuteDieBefore(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        self.m_LastMonsterInfo = {
            'VID': oVictim.m_ID,
            'AID': dMsgInfo['AID'],
            'Pos': oVictim.GetPos(),
            'Facing': oVictim.GetFacing() }

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        if oVictim.m_ID == self.m_EliteID:
            oVictim.SetDemonReward(1)
            self.ChallengeOver(self.m_LastMonsterInfo)
        else:
            self.m_TargetNum -= 1
            if self.m_TargetNum == 0:
                dInfo = self.CreateMonsterInfo()
                oGame = self.m_Game
                oWarData = oGame.m_WarData
                iScene = self.m_LevelNode.m_Scene
                clsMonsterData = oWarData.GetMonsterData(self.m_MonsterSID)
                iDelayFrame = clsMonsterData.GetCreateDelayFrame()
                iEffectSID = clsMonsterData.m_CreateEffect
                if iEffectSID:
                    iEffectID = oGame.NewNoSceneObjID()
                    cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, dInfo['Pos'], self.GetScenePlayers())
                if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                    cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
                self.RateNotify(self.GetScenePlayers())
                if iDelayFrame:
                    func = Functor(self.DelayCreateMonster, dInfo)
                    self.m_Parent.m_LevelCtrl.Call_Out(func, iDelayFrame, self.m_Key)
                else:
                    self.DelayCreateMonster(dInfo)

    
    def DelayCreateMonster(self, dInfo):
        oGame = self.m_Game
        iID = oGame.NewNPCID()
        dExtInfo = {
            'ID': iID }
        self.m_EliteID = iID
        if self.m_EliteDrop:
            dExtInfo['SetInfo'] = {
                'FixDropPos': self.m_EliteDrop['FixDropPos'],
                'CheckDropInfo': self.m_EliteDrop['CheckDropInfo'] }
        oMonster = self.m_Game.m_ResMgr.CreateMonster(dInfo['Scene'], self.m_MonsterSID, dInfo['Pos'], dInfo['Face'], SIDE_TYPE_MONSTER, 0, dInfo['AI'], dInfo['tLineIdx'], dExtInfo)
        if not oMonster:
            iWarNo = oGame.m_WarMgr.m_SID
            SendAlert('err', '战场%d 地图%d 关卡%d 未配置怪物SID%d' % (iWarNo, self.m_LevelNode.m_Map, self.m_LevelNode.m_Level, self.m_MonsterSID))
            return None
        if oMonster.IsDead():
            return None
        self.AddEffectState(oMonster.m_ID)

    
    def CreateMonsterInfo(self):
        if self.m_ElitePos:
            vPos = self.m_ElitePos
        else:
            vPos = self.m_LastMonsterInfo['Pos']
        oLineNode = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
        vFace = oLineNode.m_MonsterCtrl.GetMonsterFacing(vPos)
        tLineIdx = (self.m_LevelNode.m_Level, self.m_RoomPos, 0)
        (ret, vPos2) = self.m_Game.Scene_GetSpace(self.m_LevelNode.m_Scene, vPos)
        if ret:
            vPos = vPos2
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        iScene = self.m_LevelNode.m_Scene
        dInfo = {
            'Pos': vPos,
            'Face': vFace,
            'AI': dAI,
            'tLineIdx': tLineIdx,
            'Scene': iScene }
        return dInfo

    
    def OnChallengeOver(self):
        super().OnChallengeOver()
        if self.m_Status == CHASTATUS_SUCCESS:
            oLevelNode = self.m_LevelNode
            oLevelNode.UnlockRoom(self.m_RoomPos, 'EliteChallenge')
            bForceTrigger = False
            if not (self.m_GoalTrigger) and len(oLevelNode.m_RoomList) > self.m_RoomPos:
                lstLine = oLevelNode.m_RoomList[self.m_RoomPos]
                for oLine in lstLine:
                    if not oLine.IsGoal():
                        break
                else:
                    bForceTrigger = True
            if self.m_GoalTrigger or bForceTrigger:
                self.m_LevelNode.LineGoal(self.m_RoomPos)

    
    def CheckMonsterDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if self.m_Status != CHASTATUS_CONTINUE:
            return False
        if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
            return False
        tLineIdx = oVictim.m_LineIdx
        if not tLineIdx or tLineIdx[0] != self.m_LevelNode.m_Level or tLineIdx[1] != self.m_RoomPos:
            return False
        return True

    
    def AddEffectState(self, iMonster):
        oMonster = self.m_Game.GetObject(iMonster)
        if not oMonster or not (self.m_EffectState):
            return None
        dArgs = {
            'AID': oMonster.m_ID,
            'RS': cl_object.reason.CStrReason('RoomChallenge'),
            'arg': { } }
        cl_state.AddState(oMonster, self.m_EffectState, STATE_TIME_FOREVER, 0, dArgs)

    
    def RateNotify(self, lstPlayer):
        if self.m_TargetNum > 0:
            return None
        super().RateNotify(lstPlayer)

    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return False
        if iRoomPos >= len(oLevelNode.m_RoomList):
            return False
        for oLineNode in oLevelNode.m_RoomList[iRoomPos]:
            oMonsterCtrl = oLineNode.m_MonsterCtrl
            if not oMonsterCtrl.IsMonsterAllDie():
                return True
        
        return False

    ValidCreate = classmethod(ValidCreate)


class CExtraEliteChallenge(CExtraMonsterChallenge):
    m_Type = CHALLENGE_EXTRAELITE
    m_ChallengeName = '额外精英怪物'
    
    def Init(self, clsData, dAddData):
        super(CExtraEliteChallenge, self).Init(clsData, dAddData)
        self.m_EliteCnt = cl_formula.GetFormulaResult(self, clsData.m_Param[0])
        self.m_CreateInterval = cl_formula.GetFormulaResult(self, clsData.m_Param[1])
        self.m_ChooseData = self.GetChooseData(clsData.m_Param[2])
        self.m_LiveLimit = cl_formula.GetFormulaResult(self, clsData.m_Param[3])
        self.m_RoomGoalStart = clsData.m_Param[4] if len(clsData.m_Param) >= 5 else 0
        self.m_TargetNum = 0
        if not (self.m_RoomGoalStart) and len(clsData.m_Param) >= 7 and clsData.m_Param[5] and clsData.m_Param[6]:
            cl_msgcenter.DoneEvent(self.m_Parent.m_LevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
            iMin = clsData.m_Param[5]
            iMax = clsData.m_Param[6]
            dMonsterInfo = self.m_LevelNode.GetRoomMonsterInfo(self.m_RoomPos)
            iTotal = sum(dMonsterInfo.values())
            iMin = int(iTotal * iMin / 100)
            iMax = int(iTotal * iMax / 100)
            iTargetNum = self.m_Game.Random((iMax - iMin) + 1) + iMin
            self.m_TargetNum = min(iTotal, iTargetNum)
            self.m_TargetNum = max(1, self.m_TargetNum)
        self.m_EliteList = []
        self.m_CreateCnt = 0
        self.m_CreateInfo = None
        if not (self.m_RoomGoalStart) and not (self.m_TargetNum):
            cl_msgcenter.DoneEvent(self.m_Parent.m_LevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
            self.SetEnterRoomTiming()
            for oLineNode in self.m_LevelNode.m_RoomList[self.m_RoomPos]:
                oLineNode.m_MonsterCtrl.ClearPendSpawnMonster()
                oLineNode.LineTargetGoal(None)
            

    
    def Release(self):
        self.ReleaseEnterRoomEvent()
        super(CExtraEliteChallenge, self).Release()

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        if self.m_LevelNode.m_Level != dMsgInfo['Level']:
            return None
        self.m_Status = CHASTATUS_CONTINUE
        if not self.m_GoalTrigger:
            self.StartChallenge()

    
    def OnPreRoomGoal(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoomPos = dMsgInfo['Room']
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
        self.StartChallenge()

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if self.m_TargetNum:
            if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
                return None
            self.m_TargetNum -= 1
            if self.m_TargetNum <= 0:
                self.StartChallenge()
            return None
        if oVictim.m_FightType & WARRIOR_ELITE != WARRIOR_ELITE:
            return None
        if oVictim.m_ID not in self.m_EliteList:
            return None
        self.m_EliteList.remove(oVictim.m_ID)
        if self.m_LiveLimit and self.IsContinueCreate():
            self.DelayCreateMonster(self.m_CreateInfo)
        if len(self.m_EliteList) == 0 and self.m_CreateCnt == self.m_EliteCnt:
            self.ChallengeOver(self.m_LastMonsterInfo)

    
    def StartChallenge(self):
        self.m_GoalTrigger = True
        if not self.m_ElitePos:
            self.m_ElitePos = self.GetGuardElitePos()
            iWarNo = self.m_Game.m_WarMgr.m_SID
            SendAlert('err', '战场%d 关卡%d 未配置精英怪出生点' % (iWarNo, self.m_LevelNode.m_Level))
        self.RateNotify(self.GetScenePlayers())
        self.m_CreateInfo = self.CreateMonsterInfo()
        oGame = self.m_Game
        oWarData = oGame.m_WarData
        iScene = self.m_LevelNode.m_Scene
        iMonsterSID = self.GetMonsterSID()
        clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
        iDelayFrame = clsMonsterData.GetCreateDelayFrame()
        iEffectSID = clsMonsterData.m_CreateEffect
        if iEffectSID:
            iEffectID = oGame.NewNoSceneObjID()
            cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, self.m_CreateInfo['Pos'], self.GetScenePlayers())
        if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
        if iDelayFrame:
            func = Functor(self.DelayCreateMonster, self.m_CreateInfo)
            self.m_Parent.m_LevelCtrl.Call_Out(func, iDelayFrame, self.m_Key)
        else:
            self.DelayCreateMonster(self.m_CreateInfo)
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if MODE_RIDINGALONE in oGame.m_WarMgr.m_ModeType:
            lstBuild = oScene.GetObjectsByTypes([
                'Trap'])
            for iBuild in lstBuild:
                oBuild = self.m_Game.GetObject(iBuild)
                if not (oBuild.m_LineIdx) or oBuild.m_LineIdx[1] != self.m_RoomPos:
                    continue
                oBuild.StopPerform()
            
            iWindSID = 1060
            for oLineNode in self.m_LevelNode.m_RoomList[self.m_RoomPos]:
                SpanwTriggerWindDie(oLineNode, [
                    iWindSID])
            

    
    def DelayCreateMonster(self, dInfo):
        if not self.IsContinueCreate():
            return None
        iMonsterSID = self.GetMonsterSID()
        oGame = self.m_Game
        iID = oGame.NewNPCID()
        dExtInfo = {
            'ID': iID }
        self.m_CreateCnt += 1
        self.m_EliteList.append(iID)
        if self.m_EliteDrop:
            dExtInfo['SetInfo'] = {
                'FixDropPos': self.m_EliteDrop['FixDropPos'],
                'CheckDropInfo': self.m_EliteDrop['CheckDropInfo'] }
        oMonster = self.m_Game.m_ResMgr.CreateMonster(dInfo['Scene'], iMonsterSID, dInfo['Pos'], dInfo['Face'], SIDE_TYPE_MONSTER, 0, dInfo['AI'], dInfo['tLineIdx'], dExtInfo)
        if not oMonster:
            iWarNo = self.m_Game.m_WarMgr.m_SID
            SendAlert('err', '战场%d 地图%d 关卡%d 未配置怪物SID%d' % (iWarNo, self.m_LevelNode.m_Map, self.m_LevelNode.m_Level, self.m_MonsterSID))
            return None
        if not oMonster.IsDead():
            self.AddEffectState(oMonster.m_ID)
        if self.IsContinueCreate():
            func = Functor(self.DelayCreateMonster, dInfo)
            self.m_Parent.m_LevelCtrl.Call_Out(func, self.m_CreateInterval, self.m_Key)

    
    def IsContinueCreate(self):
        if self.m_CreateCnt < self.m_EliteCnt:
            if not (self.m_LiveLimit) or len(self.m_EliteList) < self.m_LiveLimit:
                return True
        return False

    
    def GetMonsterSID(self):
        iLen = len(self.m_ChooseData)
        iChoose = self.m_CreateCnt % iLen
        return self.m_ChooseData[iChoose]

    
    def GetChooseData(self, dChooseGroup):
        oWarMgr = self.m_Game.m_WarMgr
        iGroup = oWarMgr.Query('AssignGroup')
        tChoose = None
        if iGroup:
            if iGroup > len(dChooseGroup):
                iGroup = len(dChooseGroup)
            for idx, tGroup in enumerate(dChooseGroup):
                if idx + 1 == iGroup:
                    tChoose = tGroup
            
        else:
            tChoose = ChooseKey(self.m_Game, dChooseGroup)
        return tChoose

    
    def GetGuardElitePos(self):
        lstAllPos = []
        oLevelConfData = self.m_Parent.m_LevelCtrl.m_LevelConfData
        for oRoomLine in self.m_LevelNode.m_RoomList[self.m_RoomPos]:
            dPos = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, oRoomLine.m_Name, 'monsterspawn')
            lstAllPos.extend(dPos.values())
        
        vTargte = None
        for dPos in lstAllPos:
            if 'SpawnPos' not in dPos:
                continue
            for vPos in dPos['SpawnPos']:
                if not cl_math.IsZero(vPos):
                    vTargte = vPos
            
        
        return vTargte



class CEliteIntrudeChallenge(CEliteChallenge):
    m_Type = CHALLENGE_ELITEINTRUDE
    m_ChallengeName = '精英突入'
    
    def Init(self, clsData, dAddData):
        super(CEliteIntrudeChallenge, self).Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        iCurLayer = self.m_Game.m_WarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
        tLayerAndLevel = (iCurLayer, oLevelCtrl.m_LevelNum)
        self.m_MonsterSIDList = clsData.m_Param[0]
        self.m_WeaponInfo = self.GetWeaponInfo(tLayerAndLevel, clsData.m_Param[3])
        self.m_MonsterNum = self.GetChooseMonsterNum(tLayerAndLevel, clsData.m_Param[4])
        self.m_EliteDict = { }
        self.m_CreateCnt = 0

    
    def ChallengeStart(self):
        self.RateNotify(self.GetScenePlayers())

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        if oVictim.m_ID in self.m_EliteDict:
            self.m_EliteDict.pop(oVictim.m_ID)
        else:
            self.m_TargetNum -= 1
            if self.m_TargetNum == 0:
                dInfo = self.CreateMonsterInfo()
                oGame = self.m_Game
                oWarData = oGame.m_WarData
                iScene = self.m_LevelNode.m_Scene
                self.ChallengeStart()
                for _ in range(self.m_MonsterNum):
                    iMonsterSID = self.GetMonsterSID()
                    clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
                    iDelayFrame = clsMonsterData.GetCreateDelayFrame()
                    iEffectSID = clsMonsterData.m_CreateEffect
                    if iEffectSID:
                        iEffectID = oGame.NewNoSceneObjID()
                        cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, dInfo['Pos'], self.GetScenePlayers())
                    if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                        cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
                    if iDelayFrame:
                        func = Functor(self.DelayCreateMonster, dInfo, iMonsterSID)
                        self.m_Parent.m_LevelCtrl.Call_Out(func, iDelayFrame, self.m_Key)
                        continue
                    self.DelayCreateMonster(dInfo, iMonsterSID)
                
        if self.m_CreateCnt == self.m_MonsterNum and len(self.m_EliteDict) == 0:
            dWeaponInfo = { }
            if self.m_WeaponInfo['InscriptionExclusive'] > 0:
                dWeaponInfo['InscriptionExclusive'] = self.m_WeaponInfo['InscriptionExclusive']
            if self.m_WeaponInfo['SyncGrade'] > 0:
                dWeaponInfo['SyncGrade'] = 1
            self.m_LastMonsterInfo['WeaponInfo'] = dWeaponInfo
            self.ChallengeOver(self.m_LastMonsterInfo)

    
    def DelayCreateMonster(self, dInfo, iMonsterSID):
        oGame = self.m_Game
        iID = oGame.NewNPCID()
        dExtInfo = {
            'ID': iID }
        self.m_CreateCnt += 1
        self.m_EliteDict[iID] = 1
        if self.m_EliteDrop:
            dExtInfo['SetInfo'] = {
                'FixDropPos': self.m_EliteDrop['FixDropPos'],
                'CheckDropInfo': self.m_EliteDrop['CheckDropInfo'] }
        if 'DefaultSuper' in dInfo:
            dExtInfo['DefaultSuper'] = dInfo['DefaultSuper']
        oMonster = self.m_Game.m_ResMgr.CreateMonster(dInfo['Scene'], iMonsterSID, dInfo['Pos'], dInfo['Face'], SIDE_TYPE_MONSTER, 0, dInfo['AI'], dInfo['tLineIdx'], dExtInfo)
        if not oMonster:
            iWarNo = self.m_Game.m_WarMgr.m_SID
            SendAlert('err', '战场%d 地图%d 关卡%d 未配置怪物SID%d' % (iWarNo, self.m_LevelNode.m_Map, self.m_LevelNode.m_Level, self.m_MonsterSID))
            return None
        if oMonster.IsDead():
            return None
        self.AddEffectState(oMonster.m_ID)

    
    def OnReward(self, dParam):
        if not dParam:
            return None
        iVictim = dParam['VID']
        oGame = self.m_Game
        oVictim = oGame.GetObject(iVictim)
        if oVictim:
            iAttack = dParam['AID']
            iRewarder = oVictim.Query('Rewarder', 0)
            if iRewarder:
                oRewarder = oGame.GetObject(iRewarder)
                if oRewarder and oRewarder.m_FightType & WARRIOR_HERO:
                    iAttack = iRewarder
            oAttack = oGame.GetObject(iAttack)
            if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
                dHero = self.GetSceneHero()
                if not dHero:
                    return None
                iAttack = ChooseKey(oGame, dHero)
            dReward = self.m_Reward
            self.m_Reward = { }
            if not dReward:
                return None
            iRound = oGame.m_WarMgr.m_Round
            if iRound not in dReward:
                SendAlert('err', '未配置战场%d挑战%s周目%d掉落' % (oGame.m_WarMgr.m_SID, self.m_ChallengeName, iRound))
                iRound = sorted(dReward)[0]
            dReward = dReward[iRound]
            iFlag = 0
            if oVictim.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
                iFlag = 1
            dExtInfo = {
                'CalOffset': 0,
                'CheckGoldenCup': 1,
                'CanReward': iFlag,
                'AutoReward': iFlag,
                'WeaponInfo': dParam['WeaponInfo'] }
            dMGInfo = cl_reward.RewardItemByMiniGame(oVictim, iAttack, dReward, 'ChallengeReward%d' % iAttack, MG_SOURCE_KILLMONSTER, dExtInfo)
            oLevelCtrl = self.m_Parent.m_LevelCtrl
            dStaticInfo = { }
            dMsgInfo = {
                'MGInfo': dMGInfo,
                'Key': self.m_Key,
                'Scene': self.m_LevelNode.m_Scene,
                'ChallengeType': self.m_Type,
                'ChallengeSID': self.m_SID,
                'StaticInfo': dStaticInfo }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, oLevelCtrl, dMsgInfo)
            cl_reward.CreateDemon(oGame, iVictim, dMGInfo, dStaticInfo = dStaticInfo)

    
    def GetMonsterSID(self):
        iLen = len(self.m_MonsterSIDList)
        idx = self.m_Game.Random(iLen)
        return self.m_MonsterSIDList[idx]

    
    def GetWeaponInfo(self, tLayerAndLevel, dCustomInfo):
        dWeaponInfo = {
            'InscriptionExclusive': 0,
            'SyncGrade': 0 }
        if dCustomInfo and tLayerAndLevel in dCustomInfo:
            dWeaponInfo.update(dCustomInfo[tLayerAndLevel])
        return dWeaponInfo

    
    def GetChooseMonsterNum(self, tLayerAndLevel, dCustomInfo):
        if dCustomInfo and tLayerAndLevel in dCustomInfo:
            dMonsterNum = dCustomInfo[tLayerAndLevel]
            return ChooseKey(self.m_Game, dMonsterNum)
        return 0



class CAppendSkillChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_APPENDSKILL
    m_ChallengeName = '附加技能'
    m_PerformSID = 0
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_Status = CHASTATUS_WAIT
        self.SetEnterRoomTiming()
        self.m_PerformSID = clsData.m_Param[0]
        self.m_BanPlusPF = clsData.m_Param[1]
        self.m_BanAttrPlus = clsData.m_Param[2]
        if self.m_BanPlusPF or self.m_BanAttrPlus:
            self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEMONSTER, self.OnWarCreateMonster, self.m_Key)

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_Status = CHASTATUS_CONTINUE
        self.RateNotify(self.GetScenePlayers())

    
    def Release(self):
        self.ReleaseEnterRoomEvent()
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEMONSTER, self.m_Key)
        super(CAppendSkillChallenge, self).Release()

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        tLineIdx = dMsgInfo['LineIdx']
        if not tLineIdx:
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        self.AddMonsterPerform(dMsgInfo['Monster'])

    
    def AddMonsterPerform(self, iMonsterID):
        oMonster = self.m_Game.GetObject(iMonsterID)
        if not oMonster:
            return None
        oMonster.AddPerform(self.m_PerformSID, 1)
        self.AddEffectState(iMonsterID)

    
    def OnWarCreateMonster(self, oWarMgr, oMonster, dMsgInfo):
        if self.m_BanPlusPF:
            oMonster.m_BanPF = tuple(set(oMonster.m_BanPF + tuple(self.m_BanPlusPF)))
        if self.m_BanAttrPlus:
            lstPlus = []
            for iPlus in oMonster.m_AttrPlusPF:
                if iPlus in self.m_BanAttrPlus:
                    continue
                lstPlus.append(iPlus)
            
            oMonster.m_AttrPlusPF = tuple(lstPlus)



class CAberranceChallenge(CMonsterChallenge):
    m_ChallengeName = '怪物变异'
    m_Type = CHALLENGE_ABERRANCE
    m_MonsterSID = 0
    
    def Init(self, clsData, dAddData):
        super(CAberranceChallenge, self).Init(clsData, dAddData)
        self.m_MonsterSID = clsData.m_Param[0]
        self.m_Status = CHASTATUS_WAIT
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.SetEnterRoomTiming()
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER_PRE, self.OnCreateMonsterPre, self.m_Key, -1, 0)

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_Status = CHASTATUS_CONTINUE
        self.RateNotify(self.GetScenePlayers())

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.ReleaseEnterRoomEvent()
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER_PRE, self.m_Key)
        super(CAberranceChallenge, self).Release()

    
    def OnCreateMonsterPre(self, oLevelCtrl, dMsgInfo):
        tLineIdx = dMsgInfo['LineIdx']
        if not tLineIdx:
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        lstCreateInfo = dMsgInfo['CreateInfo']
        if not lstCreateInfo:
            return None
        oWarData = self.m_Game.m_WarData
        clsTarget = oWarData.GetMonsterData(self.m_MonsterSID)
        if not clsTarget:
            iWarNo = self.m_Game.m_WarMgr.m_SID
            SendAlert('err', '%d 战场%d 地图%d 关卡%d 未配置怪物SID%d' % (self.m_Game.m_ID, iWarNo, self.m_LevelNode.m_Map, self.m_LevelNode.m_Level, self.m_MonsterSID))
            return None
        iRound = self.m_Game.m_WarMgr.m_Round
        iLayer = self.m_Parent.m_LevelCtrl.m_LayerNum
        iBaseLayer = self.m_Game.m_WarMgr.GetBaseLayer(iLayer)
        iTargetBase = clsTarget.m_DataSID
        fTargetPower = GetMonsterPower(iRound, iBaseLayer, iTargetBase)
        if not fTargetPower:
            SendAlert('err', '%d 周目%d 幕数%d 基础幕数%d 怪物SID%d-基础配置%d 未配置战斗力系数' % (self.m_Game.m_ID, iRound, iLayer, iBaseLayer, self.m_MonsterSID, iTargetBase))
            return None
        fTotalPower = 0
        iExcludeMonster = 24011
        for dInfo in lstCreateInfo[:]:
            iSID = dInfo['MonsterSID']
            if iSID == iExcludeMonster:
                lstCreateInfo.remove(dInfo)
                continue
            clsMonsterData = oWarData.GetMonsterData(iSID)
            if clsMonsterData.m_FightType == WARRIOR_NORFLY:
                lstCreateInfo.remove(dInfo)
                continue
            fTotalPower += GetMonsterPower(iRound, iBaseLayer, clsMonsterData.m_DataSID, clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE)
        
        iOldAmount = len(lstCreateInfo)
        iNewAmount = max(1, round(fTotalPower / fTargetPower))
        iRemove = max(0, iOldAmount - iNewAmount)
        for _ in range(iRemove):
            lstCreateInfo.pop(self.m_Game.Random(len(lstCreateInfo)))
        
        for dInfo in lstCreateInfo:
            dInfo['MonsterSID'] = self.m_MonsterSID
        

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        tLineIdx = dMsgInfo['LineIdx']
        iMonsterID = dMsgInfo['Monster']
        if not tLineIdx:
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        self.AddEffectState(iMonsterID)



class CPlayerPerformChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_PLAYERPERFORM
    m_ChallengeName = '玩家附加技能'
    m_PerformSID = 0
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_Status = CHASTATUS_WAIT
        self.m_PerformSID = clsData.m_Param[0]
        self.m_DelayTime = clsData.m_Param[1]
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, self.m_Key, -1)
        self.SetEnterRoomTiming()

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_Key)
        lstHero = self.m_Game.m_WarMgr.GetAllHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                oHero.m_Perform.RemovePerform(oHero, self.m_PerformSID)
        
        self.ReleaseEnterRoomEvent()
        if self.m_DelayTime and self.m_DelayTime > 0:
            oLevelCtrl.Remove_Call_Out(self.m_Key + 'AddPerform')
        super().Release()

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_Status = CHASTATUS_CONTINUE
        self.RateNotify(self.GetScenePlayers())
        if self.m_DelayTime and self.m_DelayTime > 0:
            func = Functor(self.AddPerform)
            self.m_Parent.m_LevelCtrl.Call_Out(func, Time2Frame(self.m_DelayTime), self.m_Key + 'AddPerform')
        else:
            self.AddPerform()

    
    def AddPerform(self):
        for iHero in self.GetSceneHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                oHero.AddPerform(self.m_PerformSID, 1)
        

    
    def OnMapLoadOK(self, oLevelCtrl, oHero, dMsgInfo):
        iToLevel = dMsgInfo['LevelID']
        if iToLevel != self.m_LevelNode.m_Level:
            oHero.m_Perform.RemovePerform(oHero, self.m_PerformSID)
        else:
            oHero.AddPerform(self.m_PerformSID, 1)

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        tLineIdx = dMsgInfo['LineIdx']
        if not tLineIdx:
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        iMonsterID = dMsgInfo['Monster']
        self.AddEffectState(iMonsterID)



class CTimeChallenge(CBaseChallenge):
    m_ChallengeName = '限时通过'
    m_Type = CHALLENGE_LIMITTIME
    m_Time = 0
    
    def Init(self, clsData, dAddData):
        super(CTimeChallenge, self).Init(clsData, dAddData)
        self.m_Time = clsData.m_Param[0]
        self.m_PassRoom = False
        self.m_StartFrame = self.m_Game.GetFrameNum()
        self.m_ChallengeFrame = Time2Frame(self.m_Time)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        func = Functor(self.ChallengeOver, { })
        oLevelCtrl.Call_Out(func, self.m_ChallengeFrame, self.m_Key)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key, -1, 0)
        self.RateNotify(self.GetScenePlayers())

    
    def Release(self):
        self.m_Parent.m_LevelCtrl.Remove_Call_Out(self.m_Key)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        super(CTimeChallenge, self).Release()

    
    def OnRoomGoal(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoomPos = dMsgInfo['Room']
        if self.m_LevelNode.m_Level == iLevel and self.m_RoomPos == iRoomPos:
            self.m_PassRoom = True
            self.ChallengeOver({ })

    
    def CheckChallengeStatus(self):
        iNowFrame = self.m_Game.GetFrameNum()
        if iNowFrame <= self.m_StartFrame + self.m_ChallengeFrame and self.m_PassRoom:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def GetReplaceInfo(self):
        iRemainTime = Frame2Time(self.m_ChallengeFrame + self.m_StartFrame - self.m_Game.GetFrameNum())
        return {
            '$remain': str(iRemainTime),
            '$total': str(self.m_Time) }



class CNotifyLimitChallenge(CBaseChallenge):
    m_ChallengeName = '提示限时通过'
    m_Type = CHALLENGE_NOTIFYLIMITTIME
    m_Time = 0
    m_Behavior = 0
    
    def Init(self, clsData, dAddData):
        super(CNotifyLimitChallenge, self).Init(clsData, dAddData)
        self.m_Time = clsData.m_Param[0]
        self.m_StaBehavior = clsData.m_Param[1]
        self.m_StaInitStep = clsData.m_Param[2]
        self.m_StaDestStep = clsData.m_Param[3]
        self.m_EndBehavior = clsData.m_Param[4]
        self.m_EndInitStep = clsData.m_Param[5]
        self.m_EndDestStep = clsData.m_Param[6]
        self.m_PassRoom = False
        self.m_StartFrame = -1
        self.m_ChallengeFrame = Time2Frame(self.m_Time)
        self.m_Status = CHASTATUS_WAIT
        lstPlayer = self.GetScenePlayers()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key, -1, 0)
        cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_StaBehavior, self.m_StaInitStep, lstPlayer)

    
    def StartChallenge(self):
        self.m_Status = CHASTATUS_CONTINUE
        self.m_StartFrame = self.m_Game.GetFrameNum()
        self.RateNotify(self.GetScenePlayers())
        lstPlayer = self.GetScenePlayers()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        func = Functor(self.ChallengeOver, { })
        oLevelCtrl.Call_Out(func, self.m_ChallengeFrame, self.m_Key)
        cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_StaBehavior, self.m_StaDestStep, lstPlayer)
        cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_EndBehavior, self.m_EndInitStep, lstPlayer)

    
    def Release(self):
        self.m_Parent.m_LevelCtrl.Remove_Call_Out(self.m_Key)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        super(CNotifyLimitChallenge, self).Release()

    
    def OnRoomGoal(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoomPos = dMsgInfo['Room']
        if self.m_LevelNode.m_Level == iLevel and self.m_RoomPos == iRoomPos:
            self.m_PassRoom = True
            self.ChallengeOver({ })

    
    def CheckChallengeStatus(self):
        if self.m_StartFrame == -1:
            return CHASTATUS_CONTINUE
        iNowFrame = self.m_Game.GetFrameNum()
        if iNowFrame <= self.m_StartFrame + self.m_ChallengeFrame and self.m_PassRoom:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def OnChallengeOver(self):
        super(CNotifyLimitChallenge, self).OnChallengeOver()
        lstPlayer = self.GetScenePlayers()
        if self.m_Status in (CHASTATUS_SUCCESS, CHASTATUS_FAILED):
            cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_EndBehavior, self.m_EndDestStep, lstPlayer)

    
    def HeroReEnterScene(self, lstPlayer):
        super(CNotifyLimitChallenge, self).HeroReEnterScene(lstPlayer)
        if self.m_Status == CHASTATUS_WAIT:
            cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_StaBehavior, self.m_StaInitStep, lstPlayer)
        elif self.m_Status == CHASTATUS_CONTINUE:
            cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_EndBehavior, self.m_EndInitStep, lstPlayer)

    
    def GetReplaceInfo(self):
        iRemainTime = Frame2Time(self.m_ChallengeFrame + self.m_StartFrame - self.m_Game.GetFrameNum())
        return {
            '$remain': str(iRemainTime),
            '$total': str(self.m_Time) }



class CLimitConvoyChallenge(CBaseChallenge):
    m_ChallengeName = '限时护送'
    m_Type = CHALLENGE_LIMITCONVOY
    m_Time = 0
    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        iGlobalPrefab = clsData.m_Param[1]
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return False
        oScene = oGame.m_SceneMgr.GetScene(oLevelNode.m_Scene)
        lstNPC = oScene.GetObjectsByType('NPC')
        for iNPCID in lstNPC:
            oNPC = oGame.GetObject(iNPCID)
            if not oNPC or oNPC.m_GlobalPrefab != iGlobalPrefab:
                continue
            dParam['ChallengeNPC'] = iNPCID
            return True
        
        return False

    ValidCreate = classmethod(ValidCreate)
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_Time = clsData.m_Param[0]
        self.m_PassLevel = False
        self.m_StartFrame = 0
        self.m_ChallengeFrame = Time2Frame(self.m_Time)
        self.m_NPC = dAddData['ChallengeNPC']
        cl_msgcenter.AddAttentionFunc(self.m_Parent.m_LevelCtrl, self.m_NPC, cl_msgcenter.MSG_WAR_NPCSTOPINTERACT, self.OnStopInteract, self.m_Key, iSub = -1)

    
    def ClearAttention(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneAttention(oLevelCtrl, self.m_NPC, cl_msgcenter.MSG_WAR_NPCSTOPINTERACT, self.m_Key)
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        cl_msgcenter.DoneEvent(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_Key)

    
    def Release(self):
        self.ClearAttention()
        super().Release()

    
    def OnStopInteract(self, oLevelCtrl, oNPC, dInfo):
        self.m_StartFrame = self.m_Game.GetFrameNum()
        cl_msgcenter.DoneAttention(oLevelCtrl, oNPC.m_ID, cl_msgcenter.MSG_WAR_NPCSTOPINTERACT, self.m_Key)
        oNPC.StartConvoy()
        func = Functor(self.ChallengeOver, { })
        self.m_Parent.m_LevelCtrl.Call_Out(func, self.m_ChallengeFrame, self.m_Key)
        cl_msgcenter.AddFunction(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, self.m_Key, iSub = -1, iOnce = 1)
        self.RateNotify(self.GetScenePlayers())

    
    def ChallengeOver(self, dParam):
        self.ClearAttention()
        oNPC = self.m_Game.GetObject(self.m_NPC)
        oNPC.EndConvoy(self.CheckChallengeStatus() == CHASTATUS_SUCCESS)
        super().ChallengeOver(dParam)

    
    def OnLevelGoal(self, oWarMgr, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        if iLevel != self.m_LevelNode.m_Level:
            return None
        self.m_PassLevel = True
        self.ChallengeOver({ })

    
    def CheckChallengeStatus(self):
        if not self.m_StartFrame:
            return CHASTATUS_FAILED
        iNowFrame = self.m_Game.GetFrameNum()
        if iNowFrame <= self.m_StartFrame + self.m_ChallengeFrame and self.m_PassLevel:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def GetReplaceInfo(self):
        return { }

    
    def OnChallengeOver(self):
        lstPlayer = self.GetScenePlayers()
        cl_snetwar.GS2CClearChallengeUI(self.m_Game, self.m_Type, lstPlayer)

    
    def RateNotify(self, lstPlayer):
        if not self.m_StartFrame:
            return None
        iRemainTime = Frame2Time(self.m_ChallengeFrame + self.m_StartFrame - self.m_Game.GetFrameNum())
        oNPC = self.m_Game.GetObject(self.m_NPC)
        (iCurPathIndex, lstPathPos) = oNPC.GetPathInfo()
        lstPlayer = self.GetScenePlayers()
        cl_snetwar.GS2CLimitConvoy(self.m_Game, self.m_Type, self.m_ChallengeNotify, self.GetReplaceInfo(), iRemainTime, self.m_Time, self.m_NPC, iCurPathIndex, lstPathPos, lstPlayer)



class CBaseDefendChallenge(CBaseChallenge):
    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        iPrefab = clsData.m_Param[0]
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return False
        oScene = oGame.m_SceneMgr.GetScene(oLevelNode.m_Scene)
        lstObj = oScene.GetObjectsByType('Protege')
        for iTarget in lstObj:
            oTarget = oGame.GetObject(iTarget)
            if not oTarget or oTarget.m_Prefab != iPrefab:
                continue
            dParam['ProtegeTarget'] = iTarget
            return True
        
        SendAlert('err', '守卫预制体%d不存在 关卡%d房间挑战%d创建失败' % (iPrefab, oLevelNode.m_Level, clsData.m_SID))
        return False

    ValidCreate = classmethod(ValidCreate)
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_RemoveDelaySuc = 0
        self.m_RemoveDelayFail = 0
        self.m_DieClientBehavior = 0
        self.m_Protege = dAddData['ProtegeTarget']
        cl_msgcenter.AddAttentionFunc(self.m_Parent.m_LevelCtrl, self.m_Protege, cl_msgcenter.MSG_WAR_BUILD_STOP_INTERACT, self.OnStopInteract, self.m_Key, iSub = -1)
        self.m_ProtegeStart = False
        self.m_StartChallenger = 0

    
    def OnChallengeOver(self):
        super().OnChallengeOver()
        oGame = self.m_Game
        oTarget = oGame.GetObject(self.m_Protege)
        if oTarget:
            oTarget.DieRemove()

    
    def Release(self):
        self.ClearAttention()
        cl_snetwar.GS2CClearChallengeUI(self.m_Game, self.m_Type, self.GetScenePlayers())
        super().Release()

    
    def CheckChallengeStatus(self):
        oTarget = self.m_Game.GetObject(self.m_Protege, PY_FLAG_DEAD)
        if not oTarget:
            return CHASTATUS_FAILED
        return CHASTATUS_SUCCESS

    
    def OnProtegeDie(self, oLevelCtrl, oProtege, dInfo):
        self.m_LevelNode.LockRoom(self.m_RoomPos, 'BaseDefendChallenge')
        for tRoomList in self.m_LevelNode.m_RoomList:
            for oLineNode in tRoomList:
                oLineNode.m_MonsterCtrl.ClearPendSpawnMonster()
            
        
        if self.m_DieClientBehavior:
            lstPlayer = []
            for iHero in self.m_Game.m_WarMgr.GetLiveHero():
                oHero = self.m_Game.GetObject(iHero)
                if not oHero or oHero.IsDying():
                    continue
                lstPlayer.append(oHero.m_PlayerID)
            
            cl_snetwar.GS2CTriggerBehavior(self.m_Game, oProtege.m_ID, self.m_DieClientBehavior, lstPlayer)
        oProtege.m_RemoveDelay = Time2Frame(self.m_RemoveDelayFail)
        self.ChallengeOver({
            'Protege': self.m_Protege })

    
    def ClearAttention(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneAttention(oLevelCtrl, self.m_Protege, cl_msgcenter.MSG_WAR_BUILD_STOP_INTERACT, self.m_Key)
        cl_msgcenter.DoneAttention(oLevelCtrl, self.m_Protege, cl_msgcenter.MSG_WAR_DIE, self.m_Key, iSub = -1)

    
    def OnStopInteract(self, oLevelCtrl, oProtege, dInfo):
        self.m_ProtegeStart = True
        cl_msgcenter.AddAttentionFunc(oLevelCtrl, self.m_Protege, cl_msgcenter.MSG_WAR_DIE, self.OnProtegeDie, self.m_Key, iSub = -1)



class CDefendChallenge(CBaseDefendChallenge):
    m_ChallengeName = '守卫目标'
    m_Type = CHALLENGE_DEFEND
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_RemoveDelaySuc = clsData.m_Param[1]
        self.m_RemoveDelayFail = clsData.m_Param[2]
        self.m_DieClientBehavior = clsData.m_Param[3]
        oTarget = self.m_Game.GetObject(self.m_Protege)
        oTarget.m_RemoveDelay = Time2Frame(self.m_RemoveDelaySuc)
        self.m_Group = { }

    
    def OnStopInteract(self, oLevelCtrl, oProtege, dInfo):
        super().OnStopInteract(oLevelCtrl, oProtege, dInfo)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key, -1, 0)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_STARTSPAWN, self.OnStartSpawn, self.m_Key, iSub = -1, iOnce = 0)
        self.RateNotify(self.GetScenePlayers())
        self.m_StartChallenger = dInfo['Hero']
        self.StartChallenge()

    
    def OnStartSpawn(self, oLevelCtrl, dInfo):
        iGroupID = dInfo['GroupID']
        if iGroupID in self.m_Group:
            return None
        self.m_Group[iGroupID] = 1
        self.RateNotify(self.GetScenePlayers())

    
    def OnRoomGoal(self, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        iRoomPos = dInfo['Room']
        if self.m_LevelNode.m_Level == iLevel and self.m_RoomPos == iRoomPos:
            self.ChallengeOver({
                'Protege': self.m_Protege })

    
    def ClearAttention(self):
        super().ClearAttention()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_STARTSPAWN, self.m_Key)

    
    def RateNotify(self, lstPlayer):
        if not self.m_ProtegeStart:
            return None
        oLineNode = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
        iNow = oLineNode.m_MonsterCtrl.NowGroup()
        iTotal = oLineNode.m_MonsterCtrl.MaxGroup()
        lstPlayer = self.GetScenePlayers()
        cl_snetwar.GS2CTargetDefend(self.m_Game, self.m_Type, self.m_Protege, iNow, iTotal, self.m_ChallengeNotify, self.GetReplaceInfo(), lstPlayer)

    
    def StartChallenge(self):
        self.CustomStartNotify()

    
    def CustomStartNotify(self):
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oSignalMgr = oWarMgr.GetComponent('SignalElement')
        oStartHero = oGame.GetObject(self.m_StartChallenger)
        iAttach = 0
        lstPlayer = []
        for iHero in oWarMgr.GetLiveHero():
            if iHero == self.m_StartChallenger:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.m_Scene == self.m_LevelNode.m_Scene:
                continue
            lstPlayer.append(oHero.m_PlayerID)
            oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
            iLevel = oScene.m_Level
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
            dHideNpc = oMiniMap.m_HideTransfer.get(oHero.m_PlayerID, { })
            for iHideNpc in dHideNpc:
                oNpc = oGame.GetObject(iHideNpc)
                if not oNpc:
                    break
                if oNpc.Query('HideLevel') == self.m_LevelNode.m_Level:
                    iAttach = iHideNpc
                    break
            
        
        iAdder = oStartHero.m_PlayerID
        dParam = {
            'Adder': iAdder,
            'SID': 1216,
            'Attach': iAttach,
            'AdderName': oStartHero.Name(),
            'Players': lstPlayer }
        oSignalMgr.AddSignal(iAdder, dParam)

    
    def AddOverState(self):
        lstHero = self.m_Game.m_WarMgr.GetAllHero()
        iChallengeStatus = self.CheckChallengeStatus()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            dState = {
                'AID': self.m_StartChallenger,
                'RS': cl_object.reason.CStrReason('DefendChallenge'),
                'DefendNpc': {
                    'LevelNodeId': id(self.m_LevelNode) } }
            oState = cl_state.AddState(oHero, STATE_DEFENDNPC, STATE_TIME_FOREVER, 0, dState)
            if oState:
                oState.Enable(oHero)
        

    
    def OnChallengeOver(self):
        super().OnChallengeOver()
        if self.CheckChallengeStatus() == CHASTATUS_FAILED:
            self.AddOverState()



class CLimitDefendChallenge(CBaseDefendChallenge):
    m_ChallengeName = '限时守卫'
    m_Type = CHALLENGE_LIMITDEFEND
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_Time = clsData.m_Param[1]
        self.m_RemoveDelaySuc = clsData.m_Param[2]
        self.m_RemoveDelayFail = clsData.m_Param[3]
        self.m_DieClientBehavior = clsData.m_Param[4]
        self.m_StartFrame = 0
        self.m_ChallengeFrame = Time2Frame(self.m_Time)
        oTarget = self.m_Game.GetObject(self.m_Protege)
        oTarget.m_RemoveDelay = Time2Frame(self.m_RemoveDelaySuc)

    
    def OnStopInteract(self, oLevelCtrl, oProtege, dInfo):
        super().OnStopInteract(oLevelCtrl, oProtege, dInfo)
        self.m_StartFrame = self.m_Game.GetFrameNum()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        func = Functor(self.ChallengeOver, {
            'Protege': self.m_Protege })
        oLevelCtrl.Call_Out(func, self.m_ChallengeFrame, self.m_Key)
        self.RateNotify(self.GetScenePlayers())

    
    def ClearAttention(self):
        super().ClearAttention()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key)

    
    def RateNotify(self, lstPlayer):
        if not self.m_ProtegeStart:
            return None
        iRemainTime = Frame2Time(self.m_ChallengeFrame + self.m_StartFrame - self.m_Game.GetFrameNum())
        lstPlayer = self.GetScenePlayers()
        cl_snetwar.GS2CLimitDefend(self.m_Game, self.m_Type, self.m_Protege, iRemainTime, self.m_Time, self.m_ChallengeNotify, self.GetReplaceInfo(), lstPlayer)



class CLimitLiveChallenge(CBaseChallenge):
    m_ChallengeName = '限时存活'
    m_Type = CHALLENGE_LIMITLIVE
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_Delay = clsData.m_Param[0]
        self.m_Time = clsData.m_Param[1]
        self.m_StartFrame = 0
        self.m_StopFrame = 0
        self.m_DelayFrame = Time2Frame(self.m_Delay)
        self.m_ChallengeFrame = Time2Frame(self.m_Time)
        lstAllHero = self.m_Game.m_WarMgr.GetAllHero()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        for iHero in lstAllHero:
            cl_msgcenter.AddAttentionFunc(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, self.m_Key)
        
        lstHero = self.GetSceneHero()
        if not lstHero:
            return None
        self.AddSceneAttention(lstHero)
        self.TryStartChallenge()

    
    def OnChallengeOver(self):
        super().OnChallengeOver()
        self.ClearChallenge()

    
    def ClearChallenge(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        lstAllHero = self.m_Game.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            cl_msgcenter.DoneAttention(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.m_Key)
        
        self.DoneSceneAttention()
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'StartChallenge')
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'ChallengeOver')

    
    def AddSceneAttention(self, lstHero):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        for iHero in lstHero:
            cl_msgcenter.AddAttentionFunc(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OnLeaveScene, self.m_Key)
            cl_msgcenter.AddAttentionFunc(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, self.m_Key)
            cl_msgcenter.AddAttentionFunc(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnHeroRelife, self.m_Key)
        

    
    def DoneSceneAttention(self):
        lstHero = self.m_Game.m_WarMgr.GetAllHero()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_LEAVESCENE, self.m_Key)
            cl_msgcenter.DoneAttention(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
            cl_msgcenter.DoneAttention(oLevelCtrl, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.m_Key)
        

    
    def OnEnterScene(self, oLevelCtrl, oHero, dInfo):
        if oHero.m_Scene != self.m_LevelNode.m_Scene:
            return None
        self.AddSceneAttention([
            oHero.m_ID])
        self.TryStartChallenge()

    
    def TryStartChallenge(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        if self.m_DelayFrame:
            oLevelCtrl.Call_Out(self.StartChallenge, self.m_DelayFrame, self.m_Key + 'StartChallenge')
        else:
            self.StartChallenge()

    
    def StartChallenge(self):
        self.m_StartFrame = self.m_Game.GetFrameNum()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        func = Functor(self.ChallengeOver, { })
        oLevelCtrl.Call_Out(func, self.m_ChallengeFrame, self.m_Key + 'ChallengeOver')
        self.RateNotify(self.GetScenePlayers())

    
    def ChallengeOver(self, dParam):
        self.ClearChallenge()
        super().ChallengeOver(dParam)

    
    def OnLeaveScene(self, oLevelCtrl, oHero, dInfo):
        lstHero = self.GetSceneHero()
        if not lstHero:
            oLevelCtrl = self.m_Parent.m_LevelCtrl
            oLevelCtrl.Remove_Call_Out(self.m_Key + 'StartChallenge')
            oLevelCtrl.Remove_Call_Out(self.m_Key + 'ChallengeOver')

    
    def OnHeroDie(self, oLevelCtrl, oHero, dInfo):
        if not self.IsContinueTime():
            self.m_StopFrame = self.m_Game.GetFrameNum()
            oLevelCtrl.Remove_Call_Out(self.m_Key + 'ChallengeOver')
            cl_snetwar.GS2CUpdateChallenge(self.m_Game, self.GetScenePlayers(), 0)

    
    def OnHeroRelife(self, oLevelCtrl, oHero, dInfo):
        if self.IsContinueTime() and self.m_StopFrame != 0:
            self.m_ChallengeFrame += self.m_Game.GetFrameNum() - self.m_StopFrame
            oLevelCtrl.Call_Out(Functor(self.ChallengeOver, { }), self.GetRemainFrame(), self.m_Key + 'ChallengeOver')
            cl_snetwar.GS2CUpdateChallenge(self.m_Game, self.GetScenePlayers(), 1)
            self.m_StopFrame = 0

    
    def IsContinueTime(self):
        lstHero = self.GetSceneHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            if not oHero.IsDead():
                return True
        
        return False

    
    def GetRemainFrame(self):
        return max(self.m_StartFrame + self.m_ChallengeFrame - self.m_Game.GetFrameNum(), 0)

    
    def GetReplaceInfo(self):
        iRemainTime = Frame2Time(self.GetRemainFrame())
        return {
            '$remain': str(iRemainTime),
            '$total': str(self.m_Time) }

    
    def CheckChallengeStatus(self):
        lstHero = self.GetSceneHero()
        if not lstHero:
            return CHASTATUS_CONTINUE
        if self.m_StartFrame and self.m_StartFrame + self.m_ChallengeFrame <= self.m_Game.GetFrameNum():
            return CHASTATUS_SUCCESS
        return CHASTATUS_CONTINUE

    
    def Release(self):
        self.ClearChallenge()
        super(CLimitLiveChallenge, self).Release()



class CTrapChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_TRAP
    m_ChallengeName = '陷阱挑战'
    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        bFlag = CMonsterChallenge.ValidCreate(oGame, iLevel, iRoomPos, dParam, clsData)
        if not bFlag:
            return False
        iTrapSID = clsData.m_Param[0]
        if not oGame.m_WarData.GetBuildData(iTrapSID):
            return False
        return True

    ValidCreate = classmethod(ValidCreate)
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_TrapSID = clsData.m_Param[0]
        self.m_TrapPF = clsData.m_Param[1]
        self.m_Interval = clsData.m_Param[2]
        self.m_UsePFTimes = clsData.m_Param[3]
        self.m_DelayStart = clsData.m_Param[4]
        self.m_RunTimes = 0
        self.m_TrapID = 0
        self.m_Status = CHASTATUS_WAIT
        self.SetEnterRoomTiming()
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key, -1, 0)

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        self.m_TrapDict = { }
        self.ReleaseEnterRoomEvent()
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_Key)
        super().Release()

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_Status = CHASTATUS_CONTINUE
        for iHero in self.GetSceneHero():
            self.InitTrap(iHero)
        
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, self.m_Key, -1)
        self.RateNotify(self.GetScenePlayers())

    
    def OnPreRoomGoal(self, oLevelCtrl, dMsgInfo):
        pass

    
    def OnRoomGoal(self, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        iRoomPos = dInfo['Room']
        if self.m_LevelNode.m_Level == iLevel and self.m_RoomPos == iRoomPos:
            self.ChallengeOver(self.m_LastMonsterInfo)

    
    def OnMapLoadOK(self, oLevelCtrl, oHero, dMsgInfo):
        self.InitTrap(oHero.m_ID)

    
    def InitTrap(self, iHero):
        if self.m_TrapID:
            return None
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        oLevelNode = self.m_LevelNode
        tPos = oHero.GetPos()
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
            'SID': self.m_TrapSID,
            'Scale': [
                1,
                1,
                1],
            'Size': (1, 0, 0),
            'Origin': tPos,
            'Shape': MODEL_TYPE_BOX,
            'Source': OBSTACLE_SOURCE_LEVEL,
            'Live': 0,
            'Perform': [] }
        oTrap = self.m_Game.m_ResMgr.CreateBuild(oLevelNode.m_Scene, self.m_TrapSID, dInfo)
        self.m_TrapID = oTrap.m_ID
        if self.m_TrapPF:
            oPerform = oTrap.m_Perform.GetPerform(self.m_TrapPF)
            if not oPerform:
                oPerform = oTrap.AddPerform(self.m_TrapPF, 1)
            if not oPerform:
                self.m_TrapPF = None
            if self.m_DelayStart:
                self.m_Parent.m_LevelCtrl.Call_Out(self.UsePerform, Time2Frame(self.m_DelayStart), self.m_Key)
            else:
                self.UsePerform()

    
    def UsePerform(self):
        if not self.m_TrapPF:
            return None
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oTrap = self.m_Game.GetObject(self.m_TrapID)
        if not oTrap:
            return None
        lstHero = self.GetSceneHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or oHero.IsDead():
                continue
            tPos = oHero.GetPos()
            vRet = self.m_Game.Scene_RaycastSingle(self.m_LevelNode.m_Scene, tPos, cl_math.Vec3Add(tPos, (0, -5, 0)), PXMASK_BLOCK)
            if vRet[0] != -1:
                tPos = vRet[1]
            tPos = (tPos[0], tPos[1] + 1, tPos[2])
            oPerform = oTrap.m_Perform.GetPerform(self.m_TrapPF)
            dInfo = {
                'pfid': self.m_TrapPF,
                'VID': iHero,
                'vStart': tPos }
            cl_war.UsePerform(oTrap, oPerform, dInfo)
        
        self.m_RunTimes += 1
        if not self.m_UsePFTimes:
            oLevelCtrl.Call_Out(self.UsePerform, Time2Frame(self.m_Interval), self.m_Key)
        elif self.m_RunTimes < self.m_UsePFTimes:
            oLevelCtrl.Call_Out(self.UsePerform, Time2Frame(self.m_Interval), self.m_Key)



class CNotifyChallenge(CBaseChallenge):
    m_Type = CHALLENGE_NOTIFY
    m_ChallengeName = '提示挑战'
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key, -1, 0)
        self.RateNotify(self.GetScenePlayers())

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        super().Release()

    
    def OnRoomGoal(self, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        iRoomPos = dInfo['Room']
        if self.m_LevelNode.m_Level == iLevel and self.m_RoomPos == iRoomPos:
            self.ChallengeOver({ })

    
    def RateNotify(self, lstPlayer):
        dReplace = self.GetReplaceInfo()
        self.ChallengeNotify(lstPlayer, 600000, self.m_ChallengeNotify, dReplace)
        cl_snetwar.GS2CStartChallenge(self.m_Game, self.m_Type, 0, self.m_ChallengeNotify, dReplace, lstPlayer)



class COldSightChallenge(CBaseChallenge):
    m_Type = CHALLENGE_SIGHT
    m_ChallengeName = '瞄准关挑战'
    
    def CheckChallengeStatus(self):
        if self.m_ChanllengeResult:
            return CHASTATUS_SUCCESS
        return CHASTATUS_FAILED

    
    def OnReward(self, dParam):
        oNpc = self.m_Game.GetObject(self.m_RewardNpc)
        if oNpc:
            oNpc.Set('Difficulty', self.m_CurPhase)
        cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_Launcher, self.m_SuccessBehavior, self.GetScenePlayers())

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'UsePF')
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'Group')
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'Option')
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'Option1')
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_CREATESUMMON, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_REMOVEOBJ, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_Key)
        for iHero in self.GetSceneHero():
            self.RestoreHero(iHero)
        
        super().Release()

    
    def GetReplaceInfo(self):
        iTotalCnt = self.m_CurConf['DieMissCnt'] if 'DieMissCnt' in self.m_CurConf else 0
        iMissCnt = self.m_CurConf['MissCnt'] if 'MissCnt' in self.m_CurConf else 0
        return {
            '$remain': str(iTotalCnt - iMissCnt),
            '$total': str(iTotalCnt) }

    
    def RateNotify(self, lstPlayer):
        if not self.m_TipStatus:
            return None
        super().RateNotify(lstPlayer)
        if self.m_TipStatus == 1:
            iRemainTime = self.m_CurConf['PhaseInterval'] - Time2Frame(self.m_Game.GetFrameNum() - self.m_StartFrame)
            if iRemainTime > 0:
                cl_snetwar.GS2CSightPhaseTime(self.m_Game, self.GetScenePlayers(), self.m_CurConf['CurPhase'], self.m_CurConf['Title'], self.m_CurConf['Option'], iRemainTime)

    
    def RestoreHero(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not oHero.Query('SightCurLevel'):
            return None
        oBulletCon = oHero.m_BulletCon
        if iHero in self.m_PickItem and self.m_PickItem[iHero]:
            self.m_PickBullet[iHero] = { }
            for iBulletSID, iAmount in oBulletCon.m_Bullet.items():
                self.m_PickBullet[iHero][iBulletSID] = iAmount
            
        oHero.Delete('SightCurLevel')
        oHero.UnForbid(cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        cl_snetwar.GS2CUnForbidRule(oHero, cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        oWeaponCon = oHero.m_WieldCon
        for iPos in list(oWeaponCon.m_Item.keys()):
            if oWeaponCon.GetPosType(iPos) == EQUIP_TYPE_FUNDAMENTALWEAPON:
                continue
            oWeapon = oWeaponCon.m_Item[iPos]
            oWeaponCon.RemoveItem(oWeapon, self.m_Key)
        
        for iPos, oWeapon in self.m_Weapon[iHero]:
            oWeaponCon.AddItem(oWeapon, iPos)
        
        oWeaponCon.SetCurWeapon(self.m_CurWeaponPos[iHero], CURWEAPON_SWITCH)
        oBulletCon.m_Bullet = { }
        for iSID, iAmount in self.m_Bullet[iHero].items():
            oBulletCon.SetBullet(iSID, iAmount)
        

    
    def InitHero(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or oHero.Query('SightCurLevel'):
            return None
        oHero.Set('SightCurLevel', (self.m_LevelNode.m_Level, self.m_RoomPos, 0))
        oHero.Forbid(cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        cl_snetwar.GS2CForbidRule(oHero, cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        self.m_Weapon[iHero] = []
        oWeaponCon = oHero.m_WieldCon
        self.m_CurWeaponPos[iHero] = oWeaponCon.GetCurWeaponPos()
        iFundamentalPos = 3
        for iPos in list(oWeaponCon.m_Item.keys()):
            if oWeaponCon.GetPosType(iPos) == EQUIP_TYPE_FUNDAMENTALWEAPON:
                iFundamentalPos = iPos
                continue
            oWeapon = oWeaponCon.m_Item[iPos]
            self.m_Weapon[iHero].append((iPos, oWeapon))
            oWeaponCon.RemoveItem(oWeapon, self.m_Key)
        
        self.m_Bullet[iHero] = { }
        oBulletCon = oHero.m_BulletCon
        for iBulletSID, iAmount in oBulletCon.m_Bullet.items():
            self.m_Bullet[iHero][iBulletSID] = iAmount
        
        oBulletCon = oHero.m_BulletCon
        oBulletCon.m_Bullet = { }
        if iHero in self.m_PickItem and self.m_PickItem[iHero]:
            oWeaponCon.AddItem(self.m_PickItem[iHero], 1)
            oWeaponCon.SetCurWeapon(1, CURWEAPON_SWITCH)
            for iSID, iAmount in self.m_PickBullet[iHero].items():
                oBulletCon.SetBullet(iSID, iAmount)
                oBulletCon.BulletModify(iSID, iAmount, self.m_Key, 0)
            
        else:
            oWeaponCon.SetCurWeapon(iFundamentalPos, CURWEAPON_SWITCH)
            for iSID in ALL_BULLET:
                oBulletCon.BulletModify(iSID, 10000, self.m_Key, 0)
            

    
    def AddSceneEvent(self):
        dShapeInfo = {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': 1 }
        self.m_EventSceneObj = cl_world.CSceneObject(self.m_Game, self.m_Game.NewNPCID())
        self.m_Trigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, self.m_EventSceneObj, PXLAYER_DEVENT, dShapeInfo, self.OnTrigger)
        self.m_Trigger.rigidbody.E_SetKinematic(1)
        self.m_EventSceneObj.Goto(self.m_LevelNode.m_Scene, self.m_ReadyPos)
        self.m_EffectID = self.m_Game.NewNoSceneObjID()
        cl_snetwar.GS2CAddEffect(self.m_Game, self.m_LevelNode.m_Scene, self.m_EffectID, 1019, self.m_ReadyPos, self.GetScenePlayers())

    
    def OnTrigger(self, oTarget, iLeave):
        if not iLeave:
            self.SceneEnterFunc()

    
    def SceneEnterFunc(self):
        self.StartChallenge()
        self.m_Trigger.Disable()
        self.m_EventSceneObj.Remove(self.m_Key)
        cl_snetwar.GS2CDeleteEffect(self.m_Game, self.m_LevelNode.m_Scene, self.m_EffectID, self.GetScenePlayers())

    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_ChanllengeResult = True
        self.m_TipStatus = 0
        self.m_StartFrame = 0
        self.m_OptionFunc = {
            1: self.SureFunc,
            2: self.CancelFunc }
        self.m_PickItem = { }
        self.m_PickBullet = { }
        self.m_CurWeaponPos = { }
        self.m_Weapon = { }
        self.m_Bullet = { }
        self.m_BelongHero = []
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_LauncherSID = clsData.m_Param[0]
        self.m_TargetSID = clsData.m_Param[1]
        self.m_PFSID = clsData.m_Param[2]
        self.m_HeroPFSID = clsData.m_Param[4]
        self.m_SuccessBehavior = clsData.m_Param[5]
        self.m_RewardNpc = 0
        iNpcSID = clsData.m_Param[6]
        if iNpcSID:
            oGame = self.m_Game
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            oScene = oGame.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
            lstObj = oScene.GetObjectsByType('NPC')
            for iTarget in lstObj:
                oTarget = oGame.GetObject(iTarget)
                if not oTarget or oTarget.m_SID != iNpcSID:
                    continue
                self.m_RewardNpc = iTarget
            
        dPhase = clsData.m_Param[3]
        self.m_PhaseConfig = { }
        for k, v in dPhase.items():
            self.m_PhaseConfig[k] = oLevelCtrl.m_Data.m_SightLevelConf[v]
        
        oLine = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
        oLevelConfData = oLevelCtrl.m_LevelConfData
        dAllPos = oLevelConfData.GetLineConfig(oLine.m_LevelNode.m_Level, oLine.m_Name, 'sightpos')
        self.m_StartPosDict = dAllPos['StartPos']
        self.m_ReadyPos = dAllPos['ReadyPos']
        self.m_CurPhase = 0
        self.m_CurGroup = 0
        self.m_GroupData = None
        self.m_CurConf = {
            'MaxPhase': len(self.m_PhaseConfig) }
        self.InitLauncher()
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PICK, self.OnPick, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnLoadMapOK, self.m_Key)
        for iHero in self.GetSceneHero():
            self.InitHero(iHero)
        

    
    def IsSameScene(self, oTarget):
        if oTarget.m_Scene != self.m_LevelNode.m_Scene:
            return False
        return True

    
    def OnPick(self, oLevelCtrl, oHero, dMsgInfo):
        if not self.IsSameScene(oHero):
            return None
        self.m_TipStatus = 3
        self.AddSceneEvent()
        if dMsgInfo['Type'] != NWARRIOR_DROP_EQUIP:
            return None
        self.m_PickItem[oHero.m_ID] = dMsgInfo['Item']
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PICK, self.m_Key)

    
    def OnLoadMapOK(self, oLevelCtrl, oHero, dMsgInfo):
        if oHero.m_Scene == self.m_LevelNode.m_Scene:
            self.InitHero(oHero.m_ID)

    
    def OnEnterScene(self, oLevelCtrl, oHero, dMsgInfo):
        if not oHero.m_FightType & WARRIOR_HERO:
            return None
        iOldScene = dMsgInfo['OldScene']
        if oHero.m_Scene == self.m_LevelNode.m_Scene or iOldScene != self.m_LevelNode.m_Scene:
            self.InitHero(oHero.m_ID)
        elif iOldScene == self.m_LevelNode.m_Scene:
            self.RestoreHero(oHero.m_ID)

    
    def StartChallenge(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_CREATESUMMON, self.OnCreateSummon, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_REMOVEOBJ, self.OnRemove, self.m_Key)
        self.NextGroup()

    
    def OnCreateSummon(self, oLevelCtrl, oTarget, dMsgInfo):
        if not self.IsSameScene(oTarget):
            return None
        iSummonID = dMsgInfo['Summon']
        oSummon = self.m_Game.GetObject(iSummonID)
        if oSummon:
            oTarget.AttrForceSet('HPMax', self.m_CurConf['TargetHP'], self.m_Key)

    
    def OnRemove(self, oLevelCtrl, oMonster, dInfo):
        if not self.IsSameScene(oMonster):
            return None
        if oMonster.m_SID != self.m_TargetSID:
            return None
        self.m_CurConf['RemoveCnt'] += 1
        if dInfo['Reason'] == 'CartoonOver':
            self.m_CurConf['MissCnt'] += 1
            self.RateNotify(self.GetScenePlayers())
            if self.m_CurConf['MissCnt'] >= self.m_CurConf['DieMissCnt']:
                self.m_ChanllengeResult = False
                self.m_CurPhase -= 1
                self.ChallengeOver({ })
                return None
        if self.m_CurConf['RemoveCnt'] >= self.m_CurConf['TotalLaunchCnt']:
            self.GS2CSightPhaseOption()
            return None

    
    def GS2CSightPhaseOption(self):
        if self.m_CurPhase >= self.m_CurConf['MaxPhase'] and self.m_CurGroup >= self.m_CurConf['MaxGroup']:
            self.ChallengeOver({ })
            return None
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Call_Out(self.GS2CSightPhaseOption1, Time2Frame(200), self.m_Key + 'Option1')

    
    def GS2CSightPhaseOption1(self):
        self.m_TipStatus = 1
        self.m_StartFrame = self.m_Game.GetFrameNum()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_snetwar.GS2CSightPhaseTime(self.m_Game, self.GetScenePlayers(), self.m_CurConf['CurPhase'], self.m_CurConf['Title'], self.m_CurConf['Option'], self.m_CurConf['PhaseInterval'])
        oLevelCtrl.Call_Out(self.CancelFunc, Time2Frame(self.m_CurConf['PhaseInterval']), self.m_Key + 'Option')

    
    def GS2CSightGroupTime(self):
        self.m_TipStatus = 2
        self.m_StartFrame = self.m_Game.GetFrameNum()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Call_Out(self.UsePerform, Time2Frame(self.m_CurConf['GroupInterval']), self.m_Key + 'Group')
        if self.m_CurGroup == 1:
            cl_notify.SendCommonNotify(self.m_Game, self.GetScenePlayers(), self.m_CurConf['PhaseTip'], { })

    
    def OnDie(self, oLevelCtrl, oMonster, dInfo):
        if not self.IsSameScene(oMonster):
            return None
        if oMonster.m_SID != self.m_TargetSID:
            return None

    
    def InitPhaseData(self):
        if self.m_CurPhase > self.m_CurConf['MaxPhase']:
            self.ChallengeOver({ })
            return None
        self.m_TipStatus = 4
        self.m_CurGroup = 1
        dOption = { }
        for k, v in self.m_PhaseConfig[self.m_CurPhase]['Option'].items():
            dOption[k] = cl_notify.GetCommonNotifyMsg(v)
        
        dInitData = {
            'CurPhase': self.m_CurPhase,
            'MaxGroup': len(self.m_PhaseConfig[self.m_CurPhase]['Group']),
            'CurGroup': self.m_CurGroup,
            'DieMissCnt': self.m_PhaseConfig[self.m_CurPhase]['FailCnt'],
            'MissCnt': 0,
            'RemoveCnt': 0,
            'Title': cl_notify.GetCommonNotifyMsg(self.m_PhaseConfig[self.m_CurPhase]['Title']),
            'PhaseTip': self.m_PhaseConfig[self.m_CurPhase]['PhaseTip'],
            'Option': dOption,
            'PhaseInterval': self.m_PhaseConfig[self.m_CurPhase]['PhaseInterval'] }
        iTotalLauchCnt = 0
        for dData in self.m_PhaseConfig[self.m_CurPhase]['Group']:
            iTotalLauchCnt += dData['PFCnt']
        
        dInitData['TotalLaunchCnt'] = iTotalLauchCnt
        self.m_CurConf.update(dInitData)
        self.InitGroupData()
        self.RateNotify(self.GetScenePlayers())

    
    def InitGroupData(self):
        if self.m_CurPhase > self.m_CurConf['MaxPhase'] or self.m_CurGroup > self.m_CurConf['MaxGroup']:
            self.ChallengeOver({ })
            return None
        self.m_GroupData = self.m_PhaseConfig[self.m_CurPhase]['Group'][self.m_CurGroup - 1]
        dInitData = {
            'MaxLaunchCnt': self.m_GroupData['PFCnt'],
            'LaunchCnt': 0,
            'LaunchInterval': self.m_GroupData['PFInterval'],
            'GroupInterval': self.m_GroupData['GroupInterval'],
            'TargetSpeed': self.m_GroupData['TargetSpeed'],
            'TargetScale': self.m_GroupData['TargetScale'],
            'TargetHP': self.m_GroupData['TargetHP'],
            'PosData': self.m_GroupData['PosData'],
            'StartPosData': list(self.m_GroupData['PosData'].keys()) }
        self.m_CurConf.update(dInitData)
        for iHero in self.GetSceneHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or not oHero.Query('SightCurLevel'):
                continue
            for iBulletSID in ALL_BULLET:
                oHero.m_BulletCon.BulletModify(iBulletSID, 10000, self.m_Key, 0)
            
        

    
    def NextGroup(self):
        self.m_CurGroup += 1
        if self.m_CurPhase == 0 or self.m_CurGroup > self.m_CurConf['MaxGroup']:
            self.m_CurPhase += 1
            if self.m_CurPhase > self.m_CurConf['MaxPhase']:
                self.ChallengeOver({ })
                return None
            self.InitPhaseData()
        else:
            self.InitGroupData()
        self.GS2CSightGroupTime()

    
    def UsePerform(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        if self.m_CurConf['LaunchCnt'] >= self.m_CurConf['MaxLaunchCnt']:
            if self.m_CurGroup < self.m_CurConf['MaxGroup']:
                self.NextGroup()
            return None
        oLauncher = self.m_Game.GetObject(self.m_Launcher)
        oPerform = oLauncher.m_Perform.GetPerform(self.m_PFSID)
        lstStart = self.m_CurConf['StartPosData']
        iStart = lstStart[self.m_Game.Random(len(lstStart))]
        vStart = self.m_StartPosDict[iStart]
        lstEnd = self.m_CurConf['PosData'][iStart]
        iEnd = lstEnd[self.m_Game.Random(len(lstEnd))]
        vEnd = self.m_StartPosDict[iEnd]
        dInfo = {
            'pfid': self.m_PFSID,
            'vStart': vStart,
            'vEnd': vEnd,
            'Custom': {
                'Scale': self.m_CurConf['TargetScale'],
                'Speed': self.m_CurConf['TargetSpeed'],
                'SummonSID': self.m_TargetSID,
                'Distance': int(cl_math.CalDistance(vStart, vEnd)) + 5 } }
        self.m_CurConf['LaunchCnt'] += 1
        cl_war.UsePerform(oLauncher, oPerform, dInfo)
        oLevelCtrl.Call_Out(self.UsePerform, Time2Frame(self.m_CurConf['LaunchInterval']), self.m_Key + 'UsePF')

    
    def InitLauncher(self):
        oLevelNode = self.m_LevelNode
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
            'SID': self.m_LauncherSID,
            'Scale': [
                1,
                1,
                1],
            'Size': (1, 0, 0),
            'Origin': self.m_ReadyPos,
            'Shape': MODEL_TYPE_BOX,
            'Source': OBSTACLE_SOURCE_LEVEL,
            'Live': 0,
            'Perform': [] }
        oLauncher = self.m_Game.m_ResMgr.CreateBuild(oLevelNode.m_Scene, self.m_LauncherSID, dInfo)
        self.m_Launcher = oLauncher.m_ID
        oLauncher.AddPerform(self.m_PFSID, 1)

    
    def SureFunc(self):
        if self.m_TipStatus != 1:
            return None
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'Option')
        self.NextGroup()

    
    def CancelFunc(self):
        if self.m_TipStatus != 1:
            return None
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'Option')
        self.ChallengeOver({ })



class CSightChallenge(CBaseChallenge):
    m_Type = CHALLENGE_SIGHT
    m_ChallengeName = '瞄准关挑战'
    
    def GetHitReplaceInfo(self):
        return {
            '$MaxHit': str(self.m_MaxHitCnt),
            '$Score': str(self.m_Score) }

    
    def GetReplaceInfo(self):
        iRemainTime = self.m_ChallengeTime - Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame)
        return {
            '$remain': str(iRemainTime),
            '$total': str(self.m_ChallengeTime) }

    
    def OnReward(self, dParam):
        for k, v in self.m_RewardConfig.items():
            if self.m_Score >= k and self.m_RewardLevel <= v:
                self.m_RewardLevel = v
        
        oNpc = self.m_Game.GetObject(self.m_RewardNpc)
        if oNpc:
            oNpc.Set('Difficulty', self.m_RewardLevel)
        cl_snetwar.GS2CTriggerBehavior(self.m_Game, self.m_Launcher, self.m_SuccessBehavior, self.GetScenePlayers())
        lstPlayer = self.GetScenePlayers()
        if self.m_RewardLevel in self.m_Notify:
            self.ChallengeNotify(lstPlayer, 500, cl_notify.GetCommonNotifyMsg(self.m_Notify[self.m_RewardLevel]), self.GetHitReplaceInfo())

    
    def OnChallengeOver(self):
        super().OnChallengeOver()
        lstPlayer = self.GetScenePlayers()
        cl_snetwar.GS2CClearChallengeUI(self.m_Game, self.m_Type, lstPlayer)

    
    def CheckChallengeStatus(self):
        return CHASTATUS_SUCCESS

    
    def RestoreHero(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not oHero.Query('SightCurLevel'):
            return None
        oBulletCon = oHero.m_BulletCon
        if iHero in self.m_PickItem and self.m_PickItem[iHero]:
            self.m_PickBullet[iHero] = { }
            for iBulletSID, iAmount in oBulletCon.m_Bullet.items():
                self.m_PickBullet[iHero][iBulletSID] = iAmount
            
        oHero.Delete('SightCurLevel')
        oHero.UnForbid(cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        cl_snetwar.GS2CUnForbidRule(oHero, cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        oWeaponCon = oHero.m_WieldCon
        for iPos in list(oWeaponCon.m_Item.keys()):
            if oWeaponCon.GetPosType(iPos) == EQUIP_TYPE_FUNDAMENTALWEAPON:
                continue
            oWeapon = oWeaponCon.m_Item[iPos]
            oWeaponCon.RemoveItem(oWeapon, self.m_Key)
        
        for iPos, oWeapon in self.m_Weapon[iHero]:
            oWeaponCon.AddItem(oWeapon, iPos)
        
        oWeaponCon.SetCurWeapon(self.m_CurWeaponPos[iHero], CURWEAPON_SWITCH)
        oBulletCon.m_Bullet = { }
        for iSID, iAmount in self.m_Bullet[iHero].items():
            oBulletCon.SetBullet(iSID, iAmount)
        
        oPerform = oHero.GetPerform(self.m_HeroPFSID)
        if oPerform:
            oPerform.Disable(oHero)
        for iPFSID in self.m_ForbidPerform:
            oPerform = oHero.GetPerform(iPFSID)
            if oPerform:
                oPerform.Enable(oHero)
        

    
    def InitHero(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        cl_snetwar.GS2CForbidRule(oHero, cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        if oHero.Query('SightCurLevel'):
            return None
        oHero.Set('SightCurLevel', (self.m_LevelNode.m_Level, self.m_RoomPos, 0))
        oHero.Forbid(cl_forbid.SIGHTFORBID_RULE, self.m_Key)
        self.m_Weapon[iHero] = []
        oWeaponCon = oHero.m_WieldCon
        self.m_CurWeaponPos[iHero] = oWeaponCon.GetCurWeaponPos()
        iFundamentalPos = 3
        for iPos in list(oWeaponCon.m_Item.keys()):
            if oWeaponCon.GetPosType(iPos) == EQUIP_TYPE_FUNDAMENTALWEAPON:
                iFundamentalPos = iPos
                continue
            oWeapon = oWeaponCon.m_Item[iPos]
            self.m_Weapon[iHero].append((iPos, oWeapon))
            oWeaponCon.RemoveItem(oWeapon, self.m_Key)
        
        self.m_Bullet[iHero] = { }
        oBulletCon = oHero.m_BulletCon
        for iBulletSID, iAmount in oBulletCon.m_Bullet.items():
            self.m_Bullet[iHero][iBulletSID] = iAmount
        
        oBulletCon = oHero.m_BulletCon
        oBulletCon.m_Bullet = { }
        if iHero in self.m_PickItem and self.m_PickItem[iHero]:
            oWeaponCon.AddItem(self.m_PickItem[iHero], 1)
            oWeaponCon.SetCurWeapon(1, CURWEAPON_SWITCH)
            for iSID, iAmount in self.m_PickBullet[iHero].items():
                oBulletCon.SetBullet(iSID, iAmount)
                oBulletCon.BulletModify(iSID, iAmount, self.m_Key, 0)
            
        else:
            oWeaponCon.SetCurWeapon(iFundamentalPos, CURWEAPON_SWITCH)
            for iSID in ALL_BULLET:
                oBulletCon.BulletModify(iSID, 10000, self.m_Key, 0)
            
        oPerform = oHero.GetPerform(self.m_HeroPFSID)
        if oPerform:
            oPerform.Enable(oHero)
        else:
            oHero.AddPerform(self.m_HeroPFSID, 1)
        for iPFSID in self.m_ForbidPerform:
            oPerform = oHero.GetPerform(iPFSID)
            if oPerform:
                oPerform.Disable(oHero)
        

    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_Status = CHASTATUS_WAIT
        self.m_PickItem = { }
        self.m_PickBullet = { }
        self.m_CurWeaponPos = { }
        self.m_Weapon = { }
        self.m_Bullet = { }
        self.m_BelongHero = []
        self.m_Score = 0
        self.m_RewardLevel = 1
        self.m_TargetSID = 0
        self.m_StartFrame = 0
        self.m_CurConfig = { }
        self.m_CurWeight = { }
        self.m_CurPFCnt = { }
        self.m_CurPeriodIdx = 0
        self.m_MaxHitCnt = 0
        self.m_HitCnt = 0
        self.m_Skill = { }
        self.m_InitFlag = False
        self.m_LauncherSID = clsData.m_Param[0]
        self.m_PFSID = clsData.m_Param[1]
        self.m_HeroPFSID = clsData.m_Param[2]
        self.m_SuccessBehavior = clsData.m_Param[3]
        self.InitRewardNpc(clsData.m_Param[4])
        self.m_ChallengeTime = clsData.m_Param[5]
        self.m_ScoreConfig = clsData.m_Param[6]
        self.m_RewardConfig = clsData.m_Param[7]
        self.m_PhaseConfig = clsData.m_Param[8]
        self.m_Period = sorted(self.m_PhaseConfig.keys())
        self.m_PeriodLen = len(self.m_Period)
        self.m_Notify = clsData.m_Param[9]
        self.m_DropInfo = clsData.m_Param[10]
        self.m_ForbidPerform = clsData.m_Param[11] if clsData.m_Param[11] else { }
        self.InitPosData()
        self.InitFlow(0)
        self.InitLauncher()
        for iHero in self.GetSceneHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                self.OnLoadMapOK(self.m_Parent.m_LevelCtrl, oHero, { })
        
        self.InitAttention()

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'UsePF')
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_CREATESUMMON, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PICK, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DP, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_ATTACK_END, self.m_Key)
        for iHero in self.GetSceneHero():
            self.RestoreHero(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                oHero.m_Perform.RemovePerform(oHero, self.m_HeroPFSID)
        
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        lstObj = oScene.GetObjectsByType('Summon')
        for iSummon in lstObj:
            oSummon = self.m_Game.GetObject(iSummon)
            if oSummon:
                oReason = cl_object.reason.CStrReason('SightChallenge')
                oSummon.HPDirectModify('HP', oSummon.m_ID, -oSummon.HP(), oReason)
        
        super().Release()

    
    def InitLauncher(self):
        oLevelNode = self.m_LevelNode
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
            'SID': self.m_LauncherSID,
            'Scale': [
                1,
                1,
                1],
            'Size': (1, 0, 0),
            'Origin': self.m_ReadyPos,
            'Shape': MODEL_TYPE_BOX,
            'Source': OBSTACLE_SOURCE_LEVEL,
            'Live': 0,
            'Perform': [] }
        oLauncher = self.m_Game.m_ResMgr.CreateBuild(oLevelNode.m_Scene, self.m_LauncherSID, dInfo)
        self.m_Launcher = oLauncher.m_ID
        oLauncher.AddPerform(self.m_PFSID, 1)

    
    def InitRewardNpc(self, iNpcSID):
        self.m_RewardNpc = 0
        if iNpcSID:
            oGame = self.m_Game
            oScene = oGame.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
            lstObj = oScene.GetObjectsByType('NPC')
            for iTarget in lstObj:
                oTarget = oGame.GetObject(iTarget)
                if not oTarget or oTarget.m_SID != iNpcSID:
                    continue
                self.m_RewardNpc = iTarget
            

    
    def InitPosData(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLine = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
        oLevelConfData = oLevelCtrl.m_LevelConfData
        dAllPos = oLevelConfData.GetLineConfig(oLine.m_LevelNode.m_Level, oLine.m_Name, 'sightpos')
        self.m_StartPosDict = dAllPos['StartPos']
        self.m_ReadyPos = dAllPos['ReadyPos']

    
    def InitFlow(self, iTime):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        if iTime not in self.m_PhaseConfig:
            return None
        self.m_CurPFCnt = { }
        self.m_CurWeight = { }
        dConfig = oLevelCtrl.m_Data.m_SightLevelConf[self.m_PhaseConfig[iTime]]
        self.m_CurConfig['PFInterval'] = dConfig['PFInterval']
        self.m_CurConfig['PFCnt'] = dConfig['PFCnt']
        self.m_PosData = dConfig['PosData']
        self.m_StartPosData = list(self.m_PosData.keys())
        self.m_CurConfig['Target'] = { }
        for SID, dData in dConfig['Target'].items():
            self.m_CurConfig['Target'][SID] = { }
            self.m_CurConfig['Target'][SID]['Speed'] = dData['Speed']
            self.m_CurConfig['Target'][SID]['Scale'] = dData['Scale']
            self.m_CurConfig['Target'][SID]['HP'] = dData['HP']
            self.m_CurConfig['Target'][SID]['Cnt'] = ChooseRange(self.m_Game, dData['Cnt'][0], dData['Cnt'][1])
            self.m_CurWeight[SID] = dData['Weight']
            self.m_CurPFCnt[SID] = 0
        

    
    def InitAttention(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PICK, self.OnPick, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnLoadMapOK, self.m_Key)

    
    def OnLoadMapOK(self, oLevelCtrl, oHero, dMsgInfo):
        if oHero.m_Scene == self.m_LevelNode.m_Scene:
            self.InitHero(oHero.m_ID)
            self.InitEquip(oHero)
            lstPlayer = [
                oHero.m_PlayerID]
            cl_snetwar.GS2CSightConfig(self.m_Game, lstPlayer, self.m_RewardConfig)
            if self.m_Status == CHASTATUS_SUCCESS:
                cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_SuccessBehavior, 0, lstPlayer)
            else:
                cl_snetwar.GS2CTriggerBehaviorStatus(self.m_Game, 0, self.m_SuccessBehavior, 1, lstPlayer)

    
    def InitEquip(self, oHero):
        if self.m_InitFlag is True:
            return None
        self.m_InitFlag = True
        oGame = self.m_Game
        clsData = oGame.m_WarData.GetMiniGameData(self.m_DropInfo)
        dWeight = clsData.GetChooseWeight(oHero) if clsData and clsData.m_Type == MG_EQUIP else { }
        iTrueWeapon = ChooseKey(oGame, dWeight)
        oWeapon = cl_item.CreateEquip(oGame, iTrueWeapon, 1)
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        oInscriptionCom.CleanInscription()
        oGame.GetResMgr().CreateDrop(self.m_LevelNode.m_Scene, NWARRIOR_DROP_EQUIP, self.m_ReadyPos, [
            oWeapon], { })
        self.AddSceneEvent()
        if self.m_Notify:
            self.ChallengeNotify(self.GetScenePlayers(), 500, cl_notify.GetCommonNotifyMsg(self.m_Notify[0]), { })

    
    def OnEnterScene(self, oLevelCtrl, oHero, dMsgInfo):
        if not oHero.m_FightType & WARRIOR_HERO:
            return None
        iOldScene = dMsgInfo['OldScene']
        if oHero.m_Scene == self.m_LevelNode.m_Scene or iOldScene != self.m_LevelNode.m_Scene:
            self.InitHero(oHero.m_ID)
        elif iOldScene == self.m_LevelNode.m_Scene:
            self.RestoreHero(oHero.m_ID)

    
    def IsSameScene(self, oTarget):
        if oTarget.m_Scene != self.m_LevelNode.m_Scene:
            return False
        return True

    
    def AddSceneEvent(self):
        self.m_EffectID = self.m_Game.NewNoSceneObjID()
        cl_snetwar.GS2CAddEffect(self.m_Game, self.m_LevelNode.m_Scene, self.m_EffectID, 1019, self.m_ReadyPos, self.GetScenePlayers())

    
    def OnPick(self, oLevelCtrl, oHero, dMsgInfo):
        if not self.IsSameScene(oHero):
            return None
        if dMsgInfo['Type'] != NWARRIOR_DROP_EQUIP:
            return None
        oWeapon = dMsgInfo['Item']
        oBulletCom = oWeapon.GetComponent('Bullet')
        if oBulletCom:
            oBulletCom.BulletModify(oBulletCom.MaxBullet())
        self.m_PickItem[oHero.m_ID] = oWeapon
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PICK, self.m_Key)
        self.StartChallenge()
        cl_snetwar.GS2CDeleteEffect(self.m_Game, self.m_LevelNode.m_Scene, self.m_EffectID, self.GetScenePlayers())

    
    def StartChallenge(self):
        self.m_Status = CHASTATUS_CONTINUE
        self.m_StartFrame = self.m_Game.GetFrameNum()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oFunc = Functor(self.ChallengeOver, { })
        oLevelCtrl.Call_Out(oFunc, Time2Frame(self.m_ChallengeTime), self.m_Key)
        self.RateNotify(self.GetScenePlayers())
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_CREATESUMMON, self.OnCreateSummon, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DP, self.OnDP, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, self.OnAttack, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_ATTACK_END, self.OnAttckEnd, self.m_Key)
        self.UsePerform()

    
    def OnCreateSummon(self, oLevelCtrl, oTarget, dMsgInfo):
        if not self.IsSameScene(oTarget):
            return None
        iSummonID = dMsgInfo['Summon']
        oSummon = self.m_Game.GetObject(iSummonID)
        if oSummon.m_SID not in self.m_CurConfig['Target']:
            return None
        if oSummon:
            oSummon.m_ValidShowTips = 0
            oTarget.AttrForceSet('HPMax', self.m_CurConfig['Target'][oSummon.m_SID]['HP'], self.m_Key)

    
    def OnDP(self, oLevelCtrl, oHero, dMsgInfo):
        if not self.IsSameScene(oHero):
            return None
        if oHero.m_ID not in self.m_Skill:
            self.m_Skill[oHero.m_ID] = []
        iActNum = dMsgInfo['Skill'].m_Base['ActNum']
        self.m_Skill[oHero.m_ID].append(iActNum)

    
    def OnAttack(self, oLevelCtrl, oWarrior, dMsgInfo):
        if not self.IsSameScene(oWarrior):
            return None
        iCurVID = dMsgInfo['CurVID']
        oVictim = self.m_Game.GetObject(iCurVID)
        if not oVictim or oVictim.m_SID not in self.m_ScoreConfig:
            return None
        if 'Skill' not in dMsgInfo:
            return None
        iActNum = dMsgInfo['Skill'].m_Base['ActNum']
        if oWarrior.m_ID in self.m_Skill:
            lstSkill = self.m_Skill[oWarrior.m_ID]
            if iActNum in lstSkill:
                lstSkill.remove(iActNum)
                self.m_HitCnt += 1
                if self.m_HitCnt > self.m_MaxHitCnt:
                    self.m_MaxHitCnt = self.m_HitCnt
        iScore = cl_formula.GetResultByData(oWarrior, self.m_ScoreConfig[oVictim.m_SID], {
            'SightHit': self.m_HitCnt })
        self.m_Score += iScore
        cl_snetwar.GS2CSightScore(self.m_Game, self.GetScenePlayers(), self.m_Score, iScore, self.m_HitCnt, iCurVID)

    
    def OnAttckEnd(self, oLevelCtrl, oHero, dMsgInfo):
        if not self.IsSameScene(oHero):
            return None
        iActNum = dMsgInfo['Skill'].m_Base['ActNum']
        lstSkill = self.m_Skill[oHero.m_ID]
        if iActNum in lstSkill:
            self.m_HitCnt = 0
        cl_snetwar.GS2CSightScore(self.m_Game, self.GetScenePlayers(), self.m_Score, 0, self.m_HitCnt, 0)

    
    def UsePerform(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        iCurTime = Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame)
        if self.m_PeriodLen > self.m_CurPeriodIdx + 1 and iCurTime > self.m_Period[self.m_CurPeriodIdx + 1]:
            self.m_CurPeriodIdx += 1
            self.InitFlow(self.m_Period[self.m_CurPeriodIdx])
        dWeight = { }
        for k, v in self.m_CurWeight.items():
            if self.m_CurPFCnt[k] < self.m_CurConfig['Target'][k]['Cnt']:
                dWeight[k] = v
        
        if not dWeight:
            dWeight = self.m_CurWeight
        self.m_TargetSID = ChooseKey(self.m_Game, dWeight)
        iCnt = self.m_Game.Random(self.m_CurConfig['PFCnt']) + 1
        self.m_CurPFCnt[self.m_TargetSID] += iCnt
        for i in range(iCnt):
            self.UsePerform1()
        
        oLevelCtrl.Call_Out(self.UsePerform, Time2Frame(self.m_CurConfig['PFInterval']), self.m_Key + 'UsePF')

    
    def UsePerform1(self):
        oLauncher = self.m_Game.GetObject(self.m_Launcher)
        oPerform = oLauncher.m_Perform.GetPerform(self.m_PFSID)
        lstStart = self.m_StartPosData
        iStart = lstStart[self.m_Game.Random(len(lstStart))]
        vStart = self.m_StartPosDict[str(iStart)]
        lstEnd = self.m_PosData[iStart]
        iEnd = lstEnd[self.m_Game.Random(len(lstEnd))]
        vEnd = self.m_StartPosDict[str(iEnd)]
        lstSpeed = self.m_CurConfig['Target'][self.m_TargetSID]['Speed']
        iSpeed = ChooseRange(self.m_Game, lstSpeed[0], lstSpeed[1])
        dInfo = {
            'pfid': self.m_PFSID,
            'vStart': vStart,
            'vEnd': vEnd,
            'Custom': {
                'Scale': self.m_CurConfig['Target'][self.m_TargetSID]['Scale'],
                'Speed': iSpeed,
                'SummonSID': self.m_TargetSID,
                'Distance': int(cl_math.CalDistance(vStart, vEnd)) } }
        cl_war.UsePerform(oLauncher, oPerform, dInfo)



class CSuperMonsterChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_SUPERMONSTER
    m_ChallengeName = '强化怪物'
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.OnCreateMonster, self.m_Key, -1, 0)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, self.m_Key, -1)
        self.m_BenedictionSID = clsData.m_Param[0]
        self.m_HeroBenediction = set()
        self.m_MonsterAf = 0
        self.m_AttrPlus = 0
        self.ChooseSuperMonster(clsData.m_Param[1], clsData.m_Param[2])
        for iHero in self.GetSceneHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                self.AddBenediction(oHero)
        
        oSuperCom = self.m_Game.m_WarMgr.GetComponent('MonsterSuper')
        oSuperCom.LockLevel(self.m_LevelNode.m_Level)
        self.SetEnterRoomTiming()

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.RateNotify(self.GetScenePlayers())

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_Key)
        lstHero = self.m_Game.m_WarMgr.GetAllHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                self.RemoveBenediction(oHero)
        
        oSuperCom = self.m_Game.m_WarMgr.GetComponent('MonsterSuper')
        oSuperCom.UnlockLevel(self.m_LevelNode.m_Level)
        self.ReleaseEnterRoomEvent()
        super(CSuperMonsterChallenge, self).Release()

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        tLineIdx = dMsgInfo['LineIdx']
        iMonsterID = dMsgInfo['Monster']
        if not tLineIdx:
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        oMonster = self.m_Game.GetObject(iMonsterID)
        if oMonster:
            lstAttrPlus = oMonster.m_AttrPlusPF
            if not lstAttrPlus:
                dPlayer = self.GetScenePlayers()
                LevelLog.Alert('game: %s monster: %s no attrplus challenge: %s player: %s round: %s-%s level: %s room: %s' % (self.m_Game.m_ID, oMonster.m_SID, self.m_SID, dPlayer, oLevelCtrl.m_BaseLayerNum, oLevelCtrl.m_LevelNum, self.m_LevelNode.m_Level, self.m_RoomPos))
                return None
            iPlusPF = self.m_AttrPlus
            if iPlusPF not in lstAttrPlus:
                iRand = self.m_Game.Random(len(lstAttrPlus))
                iPlusPF = lstAttrPlus[iRand]
            if not (self.m_MonsterAf) or not iPlusPF:
                SendAlert('err', '怪物%d强化有误，af:%s plus:%s' % (oMonster.m_SID, self.m_MonsterAf, iPlusPF))
                return None
            oMonster.MonsterSuper(oLevelCtrl.m_LayerNum, iPlusPF, self.m_MonsterAf)

    
    def OnMapLoadOK(self, oLevelCtrl, oHero, dMsgInfo):
        iToLevel = dMsgInfo['LevelID']
        if iToLevel != self.m_LevelNode.m_Level:
            self.RemoveBenediction(oHero)
        else:
            self.AddBenediction(oHero)

    
    def AddBenediction(self, oHero):
        if not oHero.m_BenedictionCon.HasBenediction(self.m_BenedictionSID):
            oHero.m_BenedictionCon.AddBenediction(self.m_BenedictionSID, 1, 'roomchallenge%d' % self.m_Type, iSource = BENE_SOURCE_TEMP)
            self.m_HeroBenediction.add(oHero.m_ID)

    
    def RemoveBenediction(self, oHero):
        if oHero.m_ID in self.m_HeroBenediction:
            oHero.m_BenedictionCon.RemoveBenediction(self.m_BenedictionSID)

    
    def ChooseSuperMonster(self, dMonsterAf, dAttrPlus):
        self.m_MonsterAf = ChooseKey(self.m_Game, dMonsterAf)
        self.m_AttrPlus = ChooseKey(self.m_Game, dAttrPlus)



class CKillSummonTrapChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_KILLSUMMON_TRAP
    m_ChallengeName = '杀戮召唤陷阱挑战'
    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        bFlag = CMonsterChallenge.ValidCreate(oGame, iLevel, iRoomPos, dParam, clsData)
        if not bFlag:
            return False
        iTrapSID = clsData.m_Param[0]
        if not oGame.m_WarData.GetBuildData(iTrapSID):
            SendAlert('err', '战场%d %s陷阱挑战未配置建筑%d' % (oGame.m_WarMgr.m_SID, clsData.m_SID, iTrapSID))
            return False
        return True

    ValidCreate = classmethod(ValidCreate)
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_TrapSID = clsData.m_Param[0]
        self.m_TrapPF = clsData.m_Param[1]
        self.m_SustainTime = clsData.m_Param[2]
        self.m_WarnTime = clsData.m_Param[3]
        self.m_TrapID = 0
        self.m_Status = CHASTATUS_WAIT
        self.SetEnterRoomTiming()
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key, -1, 0)

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        self.ReleaseEnterRoomEvent()
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        super().Release()

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_Status = CHASTATUS_CONTINUE
        self.InitTrap()
        self.RateNotify(self.GetScenePlayers())

    
    def OnPreRoomGoal(self, oLevelCtrl, dMsgInfo):
        pass

    
    def OnRoomGoal(self, oLevelCtrl, dInfo):
        iLevel = dInfo['Level']
        iRoomPos = dInfo['Room']
        if self.m_LevelNode.m_Level == iLevel and self.m_RoomPos == iRoomPos:
            self.ChallengeOver(self.m_LastMonsterInfo)

    
    def InitTrap(self):
        if self.m_TrapID:
            return None
        oLevelNode = self.m_LevelNode
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
            'SID': self.m_TrapSID,
            'Scale': [
                1,
                1,
                1],
            'Size': (1, 0, 0),
            'Origin': (0, 0, 0),
            'Shape': MODEL_TYPE_BOX,
            'Source': OBSTACLE_SOURCE_LEVEL,
            'Live': 0,
            'Perform': [] }
        oTrap = self.m_Game.m_ResMgr.CreateBuild(oLevelNode.m_Scene, self.m_TrapSID, dInfo)
        self.m_TrapID = oTrap.m_ID
        if self.m_TrapPF:
            oPerform = oTrap.m_Perform.GetPerform(self.m_TrapPF)
            if not oPerform:
                oPerform = oTrap.AddPerform(self.m_TrapPF, 1)
            if not oPerform:
                self.m_TrapPF = None

    
    def CheckSkillGroundPos(self, iScene, vPos, iGroundMaxDis):
        fGroundDis = self.m_Game.Scene_GroundDistance(iScene, (vPos[0], vPos[1] + 1.8, vPos[2]), iGroundMaxDis, PXMASK_GROUNDBLK)
        if fGroundDis < iGroundMaxDis:
            return (1, (vPos[0], (vPos[1] - fGroundDis) + 1.8, vPos[2]))
        return (0, vPos)

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        (iRet, vPos) = self.CheckSkillGroundPos(oVictim.m_Scene, oVictim.GetPos(), oVictim.m_GroundMaxDis)
        if not iRet:
            return None
        self.UsePerform(vPos)

    
    def UsePerform(self, tPos):
        if not self.m_TrapPF:
            return None
        oTrap = self.m_Game.GetObject(self.m_TrapID)
        if not oTrap:
            return None
        oPerform = oTrap.m_Perform.GetPerform(self.m_TrapPF)
        dInfo = {
            'pfid': self.m_TrapPF,
            'vStart': tPos,
            'Custom': {
                'SustainTime': self.m_SustainTime,
                'WarnTime': self.m_WarnTime } }
        cl_war.UsePerform(oTrap, oPerform, dInfo)



class CMoraleEliteIntrudeChallenge(CEliteIntrudeChallenge):
    m_Type = CHALLENGE_MORALE_ELITEINTRUDE
    m_ChallengeName = '士气精英突入'
    
    def Init(self, clsData, dAddData):
        super().Init(clsData, dAddData)
        self.m_Buff = clsData.m_Param[5]
        self.m_BuffMonster = clsData.m_Param[6]
        self.m_DeBuff = clsData.m_Param[7]
        self.m_DeBuffMonster = clsData.m_Param[8]
        self.m_MonsterBuff = { }

    
    def ChallengeStart(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        if oScene:
            lstMonster = oScene.GetObjectsByType('Monster')
            for iMonster in lstMonster:
                oMonster = self.m_Game.GetObject(iMonster)
                if not oMonster:
                    continue
                self.AddBuffState(oMonster)
            
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEMONSTER, self.OnCreateMonster, self.m_Key)
        super().ChallengeStart()

    
    def OnCreateMonster(self, oWarMgr, oMonster, dInfo):
        self.AddBuffState(oMonster)

    
    def AddBuffState(self, oMonster):
        if oMonster.m_SID in self.m_MonsterSIDList:
            return None
        if not oMonster.m_LineIdx:
            return None
        (iLevel, iRoomPos, _) = oMonster.m_LineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        iBuffState = 0
        if self.m_Buff:
            if not (self.m_BuffMonster) or oMonster.m_SID in self.m_BuffMonster:
                iBuffState = self.m_Buff
        if not iBuffState and self.m_DeBuff:
            if not (self.m_DeBuffMonster) or oMonster.m_SID in self.m_DeBuffMonster:
                iBuffState = self.m_DeBuff
        if not iBuffState:
            return None
        dArgs = {
            'AID': oMonster.m_ID,
            'RS': cl_object.reason.CStrReason('BuffEliteIntrudeChallenge'),
            'arg': { } }
        oState = cl_state.AddState(oMonster, iBuffState, STATE_TIME_FOREVER, 0, dArgs)
        if not oState:
            return None
        oState.Enable(oMonster)
        self.m_MonsterBuff[oMonster.m_ID] = oState.m_ID

    
    def RemoveBuffState(self):
        for iMonster, iBuffState in self.m_MonsterBuff.items():
            oMonster = self.m_Game.GetObject(iMonster)
            if not oMonster or not (oMonster.m_State):
                continue
            oMonster.m_State.RemoveItem(iBuffState)
        

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEMONSTER, self.m_Key)
        self.RemoveBuffState()
        super().Release()



class CObstacleAlienationChallenge(CMonsterChallenge):
    m_Type = CHALLENGE_OBSTACLEALIENATION
    m_ChallengeName = '障碍异化挑战'
    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        bFlag = CMonsterChallenge.ValidCreate(oGame, iLevel, iRoomPos, dParam, clsData)
        if not bFlag:
            return False
        iObstacleSID = clsData.m_Param[2]
        if not oGame.m_WarData.GetBuildData(iObstacleSID):
            SendAlert('err', '战场%d %s %d 未配置建筑%d' % (oGame.m_WarMgr.m_SID, cls.m_ChallengeName, clsData.m_SID, iObstacleSID))
            return False
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        oLine = oLevelNode.m_RoomList[iRoomPos][-1]
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        dObstacle = oLevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'lineob')
        for dInfo in dObstacle.values():
            iObstacle = dInfo['SID']
            if iObstacle == iObstacleSID:
                return True
        
        SendAlert('err', '战场%d %s %d %d %d 未配置障碍%d' % (oGame.m_WarMgr.m_SID, cls.m_ChallengeName, clsData.m_SID, iLevel, iRoomPos, iObstacleSID))
        return False

    ValidCreate = classmethod(ValidCreate)
    
    def Init(self, clsData, dAddData):
        super(CObstacleAlienationChallenge, self).Init(clsData, dAddData)
        self.m_RoundMax = clsData.m_Param[0]
        self.m_RoundTime = clsData.m_Param[1]
        self.m_RoundDelayFrame = Time2Frame(self.m_RoundTime)
        self.m_ObstacleSID = clsData.m_Param[2]
        self.m_SpawnDelayFrame = Time2Frame(clsData.m_Param[3])
        self.m_SpawnMonsterInfo = clsData.m_Param[4]
        self.m_AlienationRatio = clsData.m_Param[5]
        self.m_CurrentRound = 1
        self.m_AlienationNum = 0
        self.m_SpawnMonster = []
        self.m_KillMonster = []
        self.m_LineObstacleInfo = { }
        self.m_LineObstacle = { }
        self.m_Status = CHASTATUS_WAIT
        self.SetEnterRoomTiming()
        self.m_LevelNode.LockRoom(self.m_RoomPos, 'ObstacleAlienationChallenge')

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'SpawnStart')
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'SpawnMonster')
        oLevelCtrl.Remove_Call_Out(self.m_Key + 'SpawnObstacle')
        self.m_SpawnMonster = []
        self.m_KillMonster = []
        self.m_LineObstacleInfo = { }
        self.m_LineObstacle = { }
        self.ReleaseEnterRoomEvent()
        super(CObstacleAlienationChallenge, self).Release()

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_Status = CHASTATUS_CONTINUE
        self.InitObstacle()
        self.RateNotify(self.GetScenePlayers())

    
    def InitObstacle(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
        if not oScene:
            return None
        oLine = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
        oLevelConfData = self.m_LevelNode.m_CtrlMgr.m_LevelConfData
        dObstacle = oLevelConfData.GetLineConfig(self.m_LevelNode.m_Level, oLine.m_Name, 'lineob')
        for iPrefab, dInfo in dObstacle.items():
            iObstacleSID = dInfo['SID']
            if iObstacleSID != self.m_ObstacleSID:
                continue
            self.m_LineObstacleInfo[iPrefab] = dInfo
        
        self.m_AlienationNum = len(self.m_LineObstacleInfo) * self.m_AlienationRatio // 100
        lstIndex = GetRandomCard(self.m_Game, self.m_AlienationNum, len(self.m_LineObstacleInfo))
        iIndex = 0
        for iObstacle in oScene.GetObjectsByType('Obstacle'):
            oObstacle = self.m_Game.GetObject(iObstacle, PY_FLAG_DEAD)
            if not oObstacle or oObstacle.m_SID != self.m_ObstacleSID:
                continue
            tLineIdx = oObstacle.m_LineIdx
            if not tLineIdx or tLineIdx[0] != self.m_LevelNode.m_Level or tLineIdx[1] != self.m_RoomPos:
                continue
            if iIndex in lstIndex:
                oObstacle.m_SmashFunc = None
                self.m_LineObstacle[oObstacle.m_ID] = 1
            else:
                self.m_LineObstacle[oObstacle.m_ID] = 0
            iIndex += 1
        
        self.DelaySpawn()

    
    def DelaySpawn(self):
        cl_snetwar.GS2CObstacleAlienationRoundInfo(self.m_Game, self.m_RoundMax, self.m_CurrentRound, self.m_RoundTime, self.m_LineObstacle, self.GetScenePlayers())
        self.m_Parent.m_LevelCtrl.Call_Out(self.SpawnStart, self.m_RoundDelayFrame, self.m_Key + 'SpawnStart')

    
    def SpawnStart(self):
        self.SpawnMonster()

    
    def SpawnMonster(self):
        if self.CheckAlienationObstacle():
            self.ChallengeOver(self.m_LastMonsterInfo)
            return None
        oReason = cl_object.reason.CStrReason(self.m_Key, None, {
            'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
        lstAllMonsterInfo = []
        for iObstacle, iAlienation in dict(self.m_LineObstacle).items():
            if not iAlienation:
                continue
            oObstacle = self.m_Game.GetObject(iObstacle, PY_FLAG_DEAD)
            if not oObstacle:
                continue
            dMonsterInfo = self.GetMonsterInfo(oObstacle)
            lstAllMonsterInfo.extend(dMonsterInfo)
            oObstacle.HPModifyDam(0, [
                [
                    oObstacle.HP(),
                    oReason]])
        
        if not lstAllMonsterInfo:
            return None
        if self.m_SpawnDelayFrame > 0:
            oFunc = Functor(self.CreateMonster, lstAllMonsterInfo)
            self.m_Parent.m_LevelCtrl.Call_Out(oFunc, self.m_SpawnDelayFrame, self.m_Key + 'SpawnMonster')
        else:
            self.CreateMonster(lstAllMonsterInfo)

    
    def GetMonsterInfo(self, oObstacle):
        iScene = self.m_LevelNode.m_Scene
        tFace = oObstacle.GetFacing()
        tLine = oObstacle.m_LineIdx
        fModelRadius = oObstacle.m_ModelRadius
        vCenterPos = oObstacle.GetPos()
        lstMonsterInfo = []
        for iMonster, iNum in self.m_SpawnMonsterInfo.items():
            for _ in range(iNum):
                for _ in range(10):
                    tPos = self.m_Game.Scene_RandomPointSectorInMesh(iScene, vCenterPos, (1, 0, 0), fModelRadius, 2, 1, 180)
                    if tPos:
                        vCenterPos = tPos
                        lstMonsterInfo.append((iMonster, tPos, tFace, tLine))
                        break
                
            
        
        return lstMonsterInfo

    
    def CreateMonster(self, lstAllMonsterInfo):
        dAI = {
            'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
            'AIMethod': MONSTERAI_TYPE_DEFAULT }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
        dAI.update(dHateSearchAI)
        iScene = self.m_LevelNode.m_Scene
        for iMonster, tPos, tFace, tLine in lstAllMonsterInfo:
            oMonster = self.m_Game.m_ResMgr.CreateMonster(iScene, iMonster, tPos, tFace, SIDE_TYPE_MONSTER, 0, dAI, tLine)
            if not oMonster or oMonster.IsDead():
                continue
            self.AddEffectState(oMonster.m_ID)
            self.m_SpawnMonster.append(oMonster.m_ID)
        

    
    def DelaySpawnObstacle(self):
        if self.m_CurrentRound >= self.m_RoundMax:
            return None
        self.m_Parent.m_LevelCtrl.Call_Out(self.SpawnObstacle, 10, self.m_Key + 'SpawnObstacle')

    
    def SpawnObstacle(self):
        self.m_CurrentRound += 1
        lstIndex = GetRandomCard(self.m_Game, self.m_AlienationNum, len(self.m_LineObstacleInfo))
        oLine = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
        dLiveObstacle = { }
        for iObstacle in self.m_LineObstacle:
            oObstacle = self.m_Game.GetObject(iObstacle, PY_FLAG_DEAD)
            if not oObstacle:
                continue
            dLiveObstacle[oObstacle.m_Prefab] = oObstacle
        
        for iIndex, iPrefab in enumerate(self.m_LineObstacleInfo):
            if iPrefab not in dLiveObstacle:
                dInfo = self.m_LineObstacleInfo[iPrefab]
                oObstacle = self.m_Game.m_ResMgr.CreateBuild(self.m_LevelNode.m_Scene, self.m_ObstacleSID, dInfo, oLine.GetLineIdx())
                if not oObstacle:
                    continue
            oObstacle = dLiveObstacle[iPrefab]
            if iIndex in lstIndex:
                oObstacle.m_SmashFunc = None
                self.m_LineObstacle[oObstacle.m_ID] = 1
                continue
            self.m_LineObstacle[oObstacle.m_ID] = 0
        
        self.DelaySpawn()

    
    def CheckMonsterDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if self.m_Status != CHASTATUS_CONTINUE:
            return False
        if not oVictim:
            return False
        if not (oVictim.m_FightType & WARRIOR_MONSTER) and not (oVictim.m_FightType & WARRIOR_BUILD):
            return False
        tLineIdx = oVictim.m_LineIdx
        if not tLineIdx or tLineIdx[0] != self.m_LevelNode.m_Level or tLineIdx[1] != self.m_RoomPos:
            return False
        return True

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        if oVictim.m_ID in self.m_SpawnMonster and oVictim.m_ID not in self.m_KillMonster:
            self.m_KillMonster.append(oVictim.m_ID)
        if oVictim.m_FightType & WARRIOR_MONSTER or len(self.m_SpawnMonster) == len(self.m_KillMonster):
            self.ChallengeOver(self.m_LastMonsterInfo)
        elif oVictim.m_FightType & WARRIOR_BUILD and oVictim.m_ID in self.m_LineObstacle:
            self.m_LineObstacle.pop(oVictim.m_ID)
            oReason = dMsgInfo['RS']
            sReason = oReason.GetStrReason()
            if self.CheckAlienationObstacle():
                if sReason != self.m_Key:
                    oLevelCtrl.Remove_Call_Out(self.m_Key + 'SpawnStart')
                    if self.m_GoalTrigger or self.m_CurrentRound >= self.m_RoundMax:
                        self.ChallengeOver(self.m_LastMonsterInfo)
                        return None
                self.DelaySpawnObstacle()

    
    def CheckAlienationObstacle(self):
        for iAlienation in self.m_LineObstacle.values():
            if iAlienation:
                return False
        
        return True

    
    def CheckChallengeStatus(self):
        if not (self.m_GoalTrigger) and self.m_CurrentRound < self.m_RoundMax:
            return CHASTATUS_CONTINUE
        if not self.CheckAlienationObstacle():
            return CHASTATUS_CONTINUE
        if len(self.m_SpawnMonster) != len(self.m_KillMonster):
            return CHASTATUS_CONTINUE
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        if oLevelCtrl.Find_Call_Out(self.m_Key + 'SpawnStart'):
            return CHASTATUS_CONTINUE
        if oLevelCtrl.Find_Call_Out(self.m_Key + 'SpawnMonster'):
            return CHASTATUS_CONTINUE
        if oLevelCtrl.Find_Call_Out(self.m_Key + 'SpawnObstacle'):
            return CHASTATUS_CONTINUE
        return CHASTATUS_SUCCESS

    
    def OnChallengeOver(self):
        super(CObstacleAlienationChallenge, self).OnChallengeOver()
        if self.m_Status == CHASTATUS_SUCCESS:
            self.m_LevelNode.UnlockRoom(self.m_RoomPos, 'ObstacleAlienationChallenge')
            if self.m_GoalTrigger:
                self.m_LevelNode.LineGoal(self.m_RoomPos)



class CBoxFlashChallenge(CBaseChallenge):
    m_Type = CHALLENGE_BOXFLASH
    m_ChallengeName = '宝箱怪快闪'
    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode:
            return False
        if iRoomPos >= len(oLevelNode.m_RoomList):
            return False
        for oLineNode in oLevelNode.m_RoomList[iRoomPos]:
            oMonsterCtrl = oLineNode.m_MonsterCtrl
            if not oMonsterCtrl.IsMonsterAllDie():
                return True
        
        return False

    ValidCreate = classmethod(ValidCreate)
    
    def Init(self, clsData, dAddData):
        super(CBoxFlashChallenge, self).Init(clsData, dAddData)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.OnPreRoomGoal, self.m_Key, -1, 0)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self.OnExecuteDieBefore, self.m_Key)
        self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        self.m_LevelNode.LockRoom(self.m_RoomPos, 'BoxFlashChallenge')
        self.m_LastMonsterInfo = { }
        self.m_GoalTrigger = False
        self.m_BoxMonster = 0
        self.m_MonsterSID = clsData.m_Param[0]
        dMonsterInfo = self.m_LevelNode.GetRoomMonsterInfo(self.m_RoomPos)
        self.m_Total = sum(dMonsterInfo.values())
        iIntrudeMin = clsData.m_Param[1]
        iIntrudeMax = clsData.m_Param[2]
        self.m_IntrudeNum = self.CalTargetNum(iIntrudeMin, iIntrudeMax)
        iFleeMin = clsData.m_Param[3]
        iFleeMax = clsData.m_Param[4]
        self.m_FleeNum = self.CalTargetNum(iFleeMin, iFleeMax)
        self.m_KillNum = 0
        self.m_AppendStateHPRatio = clsData.m_Param[5]
        self.m_AppendState = clsData.m_Param[6]
        self.m_AppendStateFrame = Time2Frame(clsData.m_Param[7])

    
    def CalTargetNum(self, iMin, iMax):
        iMin = int(self.m_Total * iMin / 100)
        iMax = int(self.m_Total * iMax / 100)
        iTargetNum = self.m_Game.Random((iMax - iMin) + 1) + iMin
        return max(1, min(self.m_Total, iTargetNum))

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_Key)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, self.m_Key)
        super(CBoxFlashChallenge, self).Release()

    
    def OnPreRoomGoal(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        iRoomPos = dMsgInfo['Room']
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)
        self.m_GoalTrigger = True
        LevelLog.Debug('%s challenge:%s goaltrigger levelid:%d roompos%d' % (self.m_Game.m_ID, self.m_SID, self.m_LevelNode.m_Level, self.m_RoomPos))

    
    def OnExecuteDieBefore(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        self.m_LastMonsterInfo = {
            'VID': oVictim.m_ID,
            'AID': dMsgInfo['AID'],
            'Pos': oVictim.GetGroundPos(),
            'Facing': oVictim.GetFacing() }

    
    def CheckMonsterDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if self.m_Status != CHASTATUS_CONTINUE:
            return False
        if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
            return False
        tLineIdx = oVictim.m_LineIdx
        if not tLineIdx or tLineIdx[0] != self.m_LevelNode.m_Level or tLineIdx[1] != self.m_RoomPos:
            return False
        return True

    
    def ChallengeStart(self):
        self.CreateMonster()
        self.RateNotify(self.GetScenePlayers())

    
    def OnDie(self, oLevelCtrl, oVictim, dMsgInfo):
        if not self.CheckMonsterDie(oLevelCtrl, oVictim, dMsgInfo):
            return None
        if oVictim.m_ID == self.m_BoxMonster:
            self.m_Status = CHASTATUS_SUCCESS
            self.ChallengeOver(self.m_LastMonsterInfo)
            return None
        self.m_KillNum += 1
        if self.m_KillNum == self.m_FleeNum:
            self.m_Status = CHASTATUS_FAILED
            self.ChallengeOver(self.m_LastMonsterInfo)
            return None
        if self.m_KillNum == self.m_IntrudeNum:
            self.ChallengeStart()

    
    def CreateMonster(self):
        vPos = self.m_LastMonsterInfo['Pos']
        oLineNode = self.m_LevelNode.m_RoomList[self.m_RoomPos][-1]
        vFace = oLineNode.m_MonsterCtrl.GetMonsterFacing(vPos)
        tLineIdx = (self.m_LevelNode.m_Level, self.m_RoomPos, 0)
        (ret, vPos2) = self.m_Game.Scene_GetSpace(self.m_LevelNode.m_Scene, vPos)
        if ret:
            vPos = vPos2
        dAI = {
            'AIParamLv': PARAM_LEVEL_CLOSE_HIGH,
            'AIMethod': MONSTERAI_TYPE_AREAMOVE }
        dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_CLOSE_HIGH)
        dAI.update(dHateSearchAI)
        iScene = self.m_LevelNode.m_Scene
        dInfo = {
            'Pos': vPos,
            'Face': vFace,
            'AI': dAI,
            'tLineIdx': tLineIdx,
            'Scene': iScene }
        oMonster = self.m_Game.m_ResMgr.CreateMonster(dInfo['Scene'], self.m_MonsterSID, dInfo['Pos'], dInfo['Face'], SIDE_TYPE_MONSTER, 0, dInfo['AI'], dInfo['tLineIdx'])
        if not oMonster:
            iWarNo = self.m_Game.GetWarMgr().m_SID
            SendAlert('err', '战场%d 地图%d 关卡%d 未配置怪物SID%d' % (iWarNo, self.m_LevelNode.m_Map, self.m_LevelNode.m_Level, self.m_MonsterSID))
            return None
        if oMonster.IsDead():
            return None
        oMonster.AddHPThreshold(self.m_AppendStateHPRatio, HP_RADIO_SUB, 'BoxFlashChallenge', self.AppendState)
        self.m_BoxMonster = oMonster.m_ID

    
    def AppendState(self, oMonster, dMsgInfo):
        oMonster.ClearHPThresholdByKey(HP_RADIO_SUB, 'BoxFlashChallenge')
        if self.IsChallengeOver():
            return None
        lstHero = self.m_Game.m_WarMgr.GetRoomHero(iCalAI = 0)
        for iPlayer in lstHero:
            oPlayer = self.m_Game.GetObject(iPlayer, PY_FLAG_DIED)
            if not oPlayer:
                continue
            dState = {
                'AID': iPlayer,
                'RS': cl_object.reason.CStrReason('BoxFlashChallenge') }
            oState = cl_state.AddState(oPlayer, self.m_AppendState, STATE_TIME_LIMIT, self.m_AppendStateFrame, dState)
            if not oState:
                continue
            oState.Enable(oPlayer)
        

    
    def CheckChallengeStatus(self):
        return self.m_Status

    
    def IsChallengeOver(self):
        if self.m_Status in (CHASTATUS_FAILED, CHASTATUS_SUCCESS, CHASTATUS_OVER):
            return True
        return False

    
    def OnChallengeOver(self):
        if not self.IsChallengeOver():
            return None
        oBoxMonster = self.m_Game.GetObject(self.m_BoxMonster, PY_FLAG_DEAD)
        if oBoxMonster:
            if oBoxMonster.m_Agent:
                oBoxMonster.m_Agent.HaltPerform(oBoxMonster.m_Agent)
                oBoxMonster.m_Agent.PauseAgent('ChallengeOver')
            oBoxMonster.Stop()
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ROOM_CHALLENGE, oBoxMonster, { })
            oBoxMonster.DieRemove()
        self.m_LevelNode.UnlockRoom(self.m_RoomPos, 'BoxFlashChallenge')
        if self.m_GoalTrigger:
            self.m_LevelNode.LineGoal(self.m_RoomPos)
        super(CBoxFlashChallenge, self).OnChallengeOver()

    
    def OnReward(self, dParam):
        if not dParam:
            return None
        iVictim = dParam['VID']
        oGame = self.m_Game
        oVictim = oGame.GetObject(iVictim)
        if not oVictim:
            return None
        iAttack = dParam['AID']
        iRewarder = oVictim.Query('Rewarder', 0)
        if iRewarder:
            oRewarder = oGame.GetObject(iRewarder)
            if oRewarder and oRewarder.m_FightType & WARRIOR_HERO:
                iAttack = iRewarder
        oAttack = oGame.GetObject(iAttack)
        if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
            dHero = self.GetSceneHero()
            if not dHero:
                return None
            iAttack = ChooseKey(oGame, dHero)
        dReward = self.m_Reward
        self.m_Reward = { }
        if not dReward:
            return None
        iRound = oGame.m_WarMgr.m_Round
        if iRound not in dReward:
            SendAlert('err', '未配置战场%d挑战%s周目%d掉落' % (oGame.m_WarMgr.m_SID, self.m_ChallengeName, iRound))
            iRound = sorted(dReward)[0]
        dReward = dReward[iRound]
        dExtInfo = {
            'CalOffset': 0,
            'CheckGoldenCup': 1,
            'CanReward': 1,
            'AutoReward': 1 }
        dMGInfo = cl_reward.RewardItemByMiniGame(oVictim, iAttack, dReward, 'ChallengeReward%d' % iAttack, MG_SOURCE_KILLMONSTER, dExtInfo)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        dStaticInfo = { }
        dMsgInfo = {
            'MGInfo': dMGInfo,
            'Key': self.m_Key,
            'Scene': self.m_LevelNode.m_Scene,
            'ChallengeType': self.m_Type,
            'ChallengeSID': self.m_SID,
            'StaticInfo': dStaticInfo }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE_CREATEDEMON, oLevelCtrl, dMsgInfo)
        cl_reward.CreateDemon(oGame, iVictim, dMGInfo, dStaticInfo = dStaticInfo)



class CSeasonEliteIntrudeChallenge(CEliteIntrudeChallenge):
    m_Type = CHALLENGE_SEASONELITEINTRUDE
    m_ChallengeName = '赛季精英突入'
    
    def Init(self, clsData, dAddData):
        super(CSeasonEliteIntrudeChallenge, self).Init(clsData, dAddData)
        self.m_MonsterAf = clsData.m_Param[5]
        self.m_AttrPlus = clsData.m_Param[6]

    
    def CreateMonsterInfo(self):
        dInfo = super(CSeasonEliteIntrudeChallenge, self).CreateMonsterInfo()
        iAf = ChooseKey(self.m_Game, self.m_MonsterAf)
        iPlus = ChooseKey(self.m_Game, self.m_AttrPlus)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        dInfo['DefaultSuper'] = (oLevelCtrl.m_LayerNum, iPlus, iAf)
        return dInfo



class CDiceSeasonAppendSkillChallenge(CAppendSkillChallenge):
    m_Type = CHALLENGE_DICESEASON_APPENDSKILL
    m_ChallengeName = '骰子赛季附加技能'
    m_DiceQualityToDialogueSID = {
        DICE_QUALITY_TALE: '2457',
        DICE_QUALITY_RARE: '2456',
        DICE_QUALITY_LOW: '2455' }
    m_GuaranteedPoint = 1
    
    def Init(self, clsData, dAddData):
        oWarMgr = self.m_Game.m_WarMgr
        self.m_LvToEffectVal = clsData.m_Param[3]
        self.m_DiceEnergy = { }
        self.m_DiceQualityDialogue = ''
        self.m_RecordReward = { }
        if not self.m_LvToEffectVal:
            SendAlert('err', '未配置战场%d挑战%s周目%d品质主要参数' % (oWarMgr.m_SID, self.m_ChallengeName, oWarMgr.m_Round))
        self.m_LvToMinorVal = clsData.m_Param[4]
        oWarMgr = self.m_Game.m_WarMgr
        (self.m_Point, iLv) = DiceChallengeChoosePointAndLv(oWarMgr)
        self.m_ChallengeLv = iLv
        if not iLv or iLv not in self.m_LvToEffectVal:
            if self.m_LvToEffectVal:
                self.m_EffectVal = self.m_LvToEffectVal[max(self.m_LvToEffectVal)]
            else:
                self.m_EffectVal = 0
            self.m_Point = self.m_GuaranteedPoint
        else:
            self.m_EffectVal = self.m_LvToEffectVal[iLv]
        if self.m_LvToMinorVal:
            if iLv in self.m_LvToMinorVal:
                self.m_MinorVal = self.m_LvToMinorVal[iLv]
            else:
                self.m_MinorVal = self.m_LvToMinorVal[max(self.m_LvToMinorVal)]
        else:
            self.m_MinorVal = 0
        super(CDiceSeasonAppendSkillChallenge, self).Init(clsData, dAddData)

    
    def ValidCreate(cls, oGame, iLevel, iRoomPos, dParam, clsData):
        oDiceElement = oGame.m_WarMgr.GetDiceElement()
        if not oDiceElement:
            return False
        return CAppendSkillChallenge.ValidCreate(oGame, iLevel, iRoomPos, dParam, clsData)

    ValidCreate = classmethod(ValidCreate)
    
    def AddMonsterPerform(self, iMonsterID):
        oMonster = self.m_Game.GetObject(iMonsterID)
        if not oMonster:
            return None
        oPerform = oMonster.AddPerform(self.m_PerformSID, 1, iEnable = 0)
        if not oPerform:
            return None
        oPerform.SetArgValue('ChallengeLv', self.m_ChallengeLv)
        oPerform.SetArgValue('EffectVal', self.m_EffectVal)
        oPerform.SetArgValue('MinorVal', self.m_MinorVal)
        oPerform.Enable(oMonster)
        self.AddEffectState(iMonsterID)

    
    def RateNotify(self, lstPlayer):
        self.GS2CUpdateUI(1, self.m_ChallengeNotify, lstPlayer)

    
    def GS2CUpdateUI(self, iOperate, iNotify, lstPlayer):
        for iPlayer in lstPlayer:
            dReplace = self.GetReplaceInfo(iPlayer)
            dExtInfo = { }
            cl_snetwar.GS2CUpdateUI(self.m_Game, DICE_SEASONCHALLENGE_UI, iOperate, iNotify, dReplace, dExtInfo, [
                iPlayer])
        

    
    def GetReplaceInfo(self, iPlayer):
        dInfo = {
            '$Effect': str(self.m_EffectVal),
            '$DicePoint': str(self.m_Point),
            '$Num': str(self.m_DiceEnergy[iPlayer]) if iPlayer in self.m_DiceEnergy else '0',
            '$Quality': str(self.m_DiceQualityDialogue),
            '$Minor': str(self.m_MinorVal) }
        return dInfo

    
    def OnChallengeOver(self):
        lstPlayer = self.GetScenePlayers()
        self.GS2CUpdateUI(0, self.m_ChallengeNotify, lstPlayer)

    
    def OnChallengeOverNotify(self, lstPlayer):
        if self.m_Status == CHASTATUS_SUCCESS:
            iNotify = self.m_SuccessNotify
        else:
            iNotify = self.m_FailedNotify
        self.GS2CUpdateUI(1, iNotify, lstPlayer)

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        self.m_DiceEnergy = self.DiceChallengeRewardEnergy()
        self.m_DiceQualityDialogue = self.DiceChallengeRewardDiceQualityDialogue()
        self.m_RecordReward = self.m_Reward
        super().OnEnterRoom(oLevelCtrl, dMsgInfo)

    
    def DiceChallengeRewardEnergy(self):
        oWarMgr = self.m_Game.m_WarMgr
        oDiceElement = oWarMgr.GetDiceElement()
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        dDiceEnergy = { }
        if self.m_SID not in oDiceElement.m_ChallengePutInfo:
            return dDiceEnergy
        iLayer = oDiceElement.GetSceneLayer(oLevelCtrl, self.m_LevelNode.m_Scene)
        iEnergy = oDiceElement.m_DiceEnergyInfo['SeasonChallenge'].get(iLayer, 0)
        if not iEnergy:
            return dDiceEnergy
        lstHero = oWarMgr.GetAllHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            oDiceCon = oHero.m_DiceCon
            if not oDiceCon:
                continue
            iTrueEnergy = oDiceElement.GetIncreaseEnergy(oHero, iEnergy)
            dDiceEnergy[oHero.m_PlayerID] = iTrueEnergy
        
        return dDiceEnergy

    
    def DiceChallengeRewardDiceQualityDialogue(self):
        dDiceQualityInfo = { }
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        dReward = self.m_Reward
        if not dReward:
            return ''
        dReward = self.CheckRoundReward(oGame, dReward)
        for iRewardSID in dReward:
            clsData = oGame.m_WarData.GetMiniGameData(iRewardSID)
            if clsData.m_Type != MG_DICE:
                continue
            iMaxLayer = max(clsData.m_ChooseQualityWeight)
            iLayer = min(iMaxLayer, oLevelCtrl.m_LayerNum)
            dDiceQualityInfo.update(clsData.m_ChooseQualityWeight[iLayer])
        
        sDiceQualityDialogue = '|'.join((self.m_DiceQualityToDialogueSID[iDiceQuality] for iDiceQuality in dDiceQualityInfo))
        return sDiceQualityDialogue



class CCountMutantMonster(CAppendSkillChallenge):
    m_Type = CHALLENGE_COUNT_MUTANTMONSTER
    m_ChallengeName = '统计异化怪'
    m_MustMutantNum = 3
    
    def Init(self, clsData, dAddData):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        iLayer = min(MAX_LAYER, oLevelCtrl.m_LayerNum)
        self.m_ChallengeRoomHero = []
        self.m_MutantRatio = clsData.m_Param[3]
        self.m_MutantMonster = { }
        dLayer2MutantLimit = cl_formula.CalArgsFormula(self, clsData.m_Param[4], { })
        dLayer2MutantMaxNum = cl_formula.CalArgsFormula(self, clsData.m_Param[5], { })
        self.m_CollectData['MutantLimit'] = dLayer2MutantLimit[iLayer] if iLayer in dLayer2MutantLimit else 0
        self.m_CollectData['MutantMaxNum'] = dLayer2MutantMaxNum[iLayer] if iLayer in dLayer2MutantMaxNum else 0
        self.m_ExtraPerform = clsData.m_Param[6]
        self.m_MutantTransferPerform = clsData.m_Param[7]
        dArg2MutantNum = cl_formula.CalArgsFormula(self, clsData.m_Param[8], { })
        self.m_MutantArg = sorted(dArg2MutantNum.items(), key = (lambda x: x[1]), reverse = True)
        self.m_CycleTriggerInfo = clsData.m_Param[9]
        self.m_CollectData['BaseLayerArg'] = self.GetBaseAndNewLayerArg(clsData.m_Param[10])
        self.m_UIExtInfo = {
            'num': list(dArg2MutantNum.values()),
            'time': list(dArg2MutantNum),
            'max': self.m_CollectData['MutantMaxNum'],
            'baselayerarg': self.m_CollectData['BaseLayerArg'] }
        self.m_TriggerPerform = self.m_CycleTriggerInfo.get('Perform', 0)
        self.m_LayerRadius = self.m_CycleTriggerInfo.get('LayerRadius', { })
        self.m_InitChooseNum = self.m_CycleTriggerInfo.get('InitChooseNum', 0)
        self.m_ChooseNum = self.m_InitChooseNum
        self.m_MaxChooseNum = self.m_CycleTriggerInfo.get('MaxChooseNum', 0)
        self.m_CycleTriggerTime = self.m_CycleTriggerInfo.get('CycleTriggerTime', 0)
        super().Init(clsData, dAddData)
        self.m_CallOutKey = self.m_Key + 'CycleTrigger'
        if self.m_CycleTriggerTime > 0:
            oLevelCtrl.Call_Out(self.OnCycleTrigger, Time2Frame(self.m_CycleTriggerTime), self.m_CallOutKey)
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, self.m_Key)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_LEVELROOMDOORTRIGGER, self.OnLevelRoomDoorTrigger, self.m_Key, -1, 0)
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomGoal, self.m_Key, -1, 0)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_PREROOMGOAL, self.m_Key)

    
    def Release(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_CallOutKey)
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_LEVELROOMDOORTRIGGER, self.m_Key)
        cl_msgcenter.DoneEvent(oLevelCtrl, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Key)
        super().Release()

    
    def GetBaseAndNewLayerArg(self, dConfig):
        if not dConfig:
            return 0
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        iBaseLayer = oLevelCtrl.m_BaseLayerNum
        iLevel = self.m_LevelNode.m_Level
        if iLevel in self.m_Game.m_WarMgr.m_NewVerLayer and (iBaseLayer, 1) in dConfig:
            return dConfig[(iBaseLayer, 1)]
        if iBaseLayer in dConfig:
            return dConfig[iBaseLayer]
        return 0

    
    def GetMutantArgVal(self, iMutantNum):
        for iArgVal, iMutantNumLimit in self.m_MutantArg:
            if iMutantNum >= iMutantNumLimit:
                return iArgVal
        
        return 0

    
    def CheckMustMutant(self, oMonster):
        iCurMustMutantNum = self.m_CollectData['CurMustMutantNum'] if 'CurMustMutantNum' in self.m_CollectData else 0
        if iCurMustMutantNum >= self.m_MustMutantNum:
            return 0
        if oMonster.m_FightType == WARRIOR_NORBADGER:
            return 0
        self.m_CollectData['CurMustMutantNum'] = iCurMustMutantNum + 1
        return 1

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        tLineIdx = dMsgInfo['LineIdx']
        if not tLineIdx:
            return None
        (iLevel, iRoomPos, _) = tLineIdx
        if iLevel != self.m_LevelNode.m_Level or iRoomPos != self.m_RoomPos:
            return None
        iMonsterID = dMsgInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonsterID)
        if not oMonster:
            return None
        (iLayerNum, _) = cl_newformula.GetObjLayerAndLevel(oMonster)
        iLayerNum = min(iLayerNum, MAX_LAYER)
        oWarMgr = self.m_Game.m_WarMgr
        if iLayerNum not in self.m_MutantRatio:
            SendAlert('err', '未配置战场%d挑战%s幕数%d对应异化概率' % (oWarMgr.m_SID, self.m_ChallengeName, iLayerNum))
            return None
        if not self.CheckMustMutant(oMonster):
            iMutantRatio = self.m_MutantRatio.get(iLayerNum, 0)
            if self.m_Game.Random(100) >= iMutantRatio:
                return None
        self.MonsterMutant(oMonster)

    
    def MonsterMutant(self, oMonster):
        if self.m_Status == CHASTATUS_OVER:
            return None
        if not oMonster or oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            return None
        iMonsterID = oMonster.m_ID
        if iMonsterID in self.m_MutantMonster:
            return None
        iMutantMaxNum = self.m_CollectData['MutantMaxNum']
        iMutantLimit = self.m_CollectData['MutantLimit']
        iCurMutantNum = self.m_CollectData['MutantNum'] if 'MutantNum' in self.m_CollectData else 0
        if iCurMutantNum >= iMutantMaxNum:
            return None
        self.AddMutantMonster(iMonsterID)
        if self.m_PerformSID:
            CustomAddPerform(oMonster, self.m_PerformSID, 1, {
                'MutantLimit': iMutantLimit,
                'MutantMaxNum': iMutantMaxNum })
        iTransPf = self.m_MutantTransferPerform
        if iTransPf:
            CustomAddPerform(oMonster, iTransPf, 1, {
                'MutantLimit': iMutantLimit,
                'MutantMaxNum': iMutantMaxNum })
        if self.m_TriggerPerform:
            CustomAddPerform(oMonster, self.m_TriggerPerform, 1, { })
        oState = self.AddEffectState(iMonsterID)
        if oState:
            oState.Enable(oMonster)

    
    def ClearMonsterMutant(self):
        iTransPf = self.m_MutantTransferPerform
        if not iTransPf:
            return None
        for iMonster in self.m_MutantMonster:
            oMonster = self.m_Game.GetObject(iMonster)
            if not oMonster:
                continue
            oMonster.RemovePerform(iTransPf)
        

    
    def OnMonsterDie(self, oWarMgr, oMonster, dMsgInfo):
        iMonsterID = oMonster.m_ID
        self.RemoveMutantMonster(iMonsterID)

    
    def AddMutantMonster(self, iMonsterID):
        self.m_MutantMonster[iMonsterID] = 1
        self.OnMutantNumChange()
        self.AddExtPerform(iMonsterID)

    
    def RemoveMutantMonster(self, iMonsterID):
        if iMonsterID not in self.m_MutantMonster:
            return None
        self.m_MutantMonster.pop(iMonsterID, 0)
        self.OnMutantNumChange()

    
    def AddExtPerform(self, iMonsterID):
        iExtPerform = self.m_ExtraPerform
        if not iExtPerform:
            return None
        iMutantNum = self.m_CollectData['MutantNum'] if 'MutantNum' in self.m_CollectData else 0
        if iMutantNum > self.m_CollectData['MutantLimit']:
            oMonster = self.m_Game.GetObject(iMonsterID)
            if not oMonster:
                return None
            oMonster.AddPerform(self.m_ExtraPerform, 1)

    
    def OnMutantNumChange(self):
        iOldMutantNum = self.m_CollectData['MutantNum'] if 'MutantNum' in self.m_CollectData else 0
        iOldMutantArgVal = self.m_CollectData['CurMutantArgVal'] if 'CurMutantArgVal' in self.m_CollectData else 0
        iNewMutantNum = len(self.m_MutantMonster)
        iNewMutantArgVal = self.GetMutantArgVal(iNewMutantNum)
        self.m_CollectData['MutantNum'] = iNewMutantNum
        self.m_CollectData['CurMutantArgVal'] = iNewMutantArgVal
        self.GS2CUpdateUI(ROOMCHALLENGE_UI_OPT_UPDATE, self.m_ChallengeNotify, self.GetScenePlayers())
        (iNeedAddPerform, iNeedRemovePerform) = self.CheckNeedOperation(iOldMutantNum, iNewMutantNum)
        self.DoExtraOperation(iNeedAddPerform, iNeedRemovePerform)
        dInfo = {
            'CurMutantArgVal': iNewMutantArgVal,
            'MutantNum': iNewMutantNum }
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        if iOldMutantArgVal != iNewMutantArgVal:
            if self.m_CycleTriggerTime > 0:
                if iNewMutantArgVal <= 0:
                    oLevelCtrl.Remove_Call_Out(self.m_CallOutKey)
                else:
                    self.m_CycleTriggerTime = iNewMutantArgVal
                    if not oLevelCtrl.Find_Call_Out(self.m_CallOutKey):
                        oLevelCtrl.Call_Out(self.OnCycleTrigger, Time2Frame(self.m_CycleTriggerTime), self.m_CallOutKey)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_COMMON_ROOMCHALLENGE, oLevelCtrl, dInfo, iSub = MUTANT_ARG_CHANGE)
        if iOldMutantNum != iNewMutantNum:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_COMMON_ROOMCHALLENGE, oLevelCtrl, dInfo, iSub = MUTANT_NUM_CHANGE)

    
    def CheckNeedOperation(self, iOldMutantNum, iNewMutantNum):
        iMutantLimit = self.m_CollectData['MutantLimit']
        (iNeedAddPerform, iNeedRemovePerform) = (0, 0)
        if iOldMutantNum < iMutantLimit and iNewMutantNum >= iMutantLimit:
            iNeedAddPerform = 1
        elif iOldMutantNum >= iMutantLimit and iNewMutantNum < iMutantLimit:
            iNeedRemovePerform = 1
        return (iNeedAddPerform, iNeedRemovePerform)

    
    def DoExtraOperation(self, iNeedAddPerform, iNeedRemovePerform):
        if not iNeedAddPerform and not iNeedRemovePerform:
            return None
        if self.m_CycleTriggerTime > 0:
            if iNeedAddPerform:
                self.m_ChooseNum = self.m_MaxChooseNum
            elif iNeedRemovePerform:
                self.m_ChooseNum = self.m_InitChooseNum
        iExtraPerform = self.m_ExtraPerform
        if not iExtraPerform:
            return None
        for iMonsterID in self.m_MutantMonster:
            oMonster = self.m_Game.GetObject(iMonsterID)
            if not oMonster:
                continue
            if iNeedAddPerform:
                oMonster.AddPerform(iExtraPerform, 1)
                continue
            if iNeedRemovePerform:
                oMonster.RemovePerform(iExtraPerform)
        

    
    def OnRoomGoal(self, oLevelCtrl, dMsgInfo):
        self.OnPreRoomGoal(oLevelCtrl, dMsgInfo)

    
    def OnCycleTrigger(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.Remove_Call_Out(self.m_CallOutKey)
        if self.m_CycleTriggerTime > 0:
            oLevelCtrl.Call_Out(self.OnCycleTrigger, Time2Frame(self.m_CycleTriggerTime), self.m_CallOutKey)
        if self.m_MutantMonster:
            oGame = self.m_Game
            oScene = oGame.m_SceneMgr.GetScene(self.m_LevelNode.m_Scene)
            if not oScene:
                return None
            dChooseWeight = { }
            dFightMonster = oScene.m_SceneData.GetFightMonster()
            for iMutantMonster in self.m_MutantMonster:
                if iMutantMonster in dFightMonster:
                    dChooseWeight[iMutantMonster] = 1
            
            if not dChooseWeight:
                return None
            iChooseMonster = ChooseKey(oGame, dChooseWeight)
            oChooseMonster = oGame.GetObject(iChooseMonster, PY_FLAG_DIED)
            if not oChooseMonster:
                return None
            oPerform = oChooseMonster.GetPerform(self.m_TriggerPerform)
            if oPerform:
                lstLockTarget = []
                dSceneHeros = oScene.GetHeros()
                for iHero in self.m_ChallengeRoomHero:
                    if iHero in dSceneHeros:
                        lstLockTarget.append(iHero)
                
                if lstLockTarget:
                    dCustom = {
                        'ChooseNum': self.m_ChooseNum,
                        'LockTarget': lstLockTarget }
                    iCurBaseLayer = oGame.m_WarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
                    if iCurBaseLayer in self.m_LayerRadius:
                        dCustom['TriggerRadius'] = self.m_LayerRadius[iCurBaseLayer]
                    cl_war.UsePerform(oChooseMonster, oPerform, {
                        'Custom': dCustom })

    
    def OnEnterRoom(self, oLevelCtrl, dMsgInfo):
        super().OnEnterRoom(oLevelCtrl, dMsgInfo)
        if self.m_RoomPos == 0:
            self.m_ChallengeRoomHero = self.m_Game.m_WarMgr.GetRoomHero()

    
    def OnLevelRoomDoorTrigger(self, oLevelCtrl, dMsgInfo):
        iHero = dMsgInfo['VID']
        oTarget = self.m_Game.GetObject(iHero)
        if not oTarget.m_FightType & WARRIOR_HERO:
            return None
        if iHero in self.m_ChallengeRoomHero:
            return None
        self.m_ChallengeRoomHero.append(iHero)
        oTeammateAIElement = self.m_Game.m_WarMgr.GetComponent('TeammateAI')
        if oTeammateAIElement:
            for iAIHero, iTarget in oTeammateAIElement.GetAllFollowTargetInfo().items():
                if iAIHero in self.m_ChallengeRoomHero or iTarget != iHero:
                    continue
                self.m_ChallengeRoomHero.append(iAIHero)
            

    
    def RateNotify(self, lstPlayer):
        self.GS2CUpdateUI(ROOMCHALLENGE_UI_OPT_START, self.m_ChallengeNotify, lstPlayer)

    
    def OnChallengeOver(self):
        self.ClearMonsterMutant()
        lstPlayer = self.GetScenePlayers()
        self.GS2CUpdateUI(ROOMCHALLENGE_UI_OPT_OVER, self.m_ChallengeNotify, lstPlayer)

    
    def GS2CUpdateUI(self, iOperate, iNotify, lstPlayer):
        for iPlayer in lstPlayer:
            dReplace = self.GetReplaceInfo(iPlayer)
            cl_snetwar.GS2CUpdateUI(self.m_Game, BACKPACK_SEASONCHALLENGE_UI, iOperate, iNotify, dReplace, self.m_UIExtInfo, [
                iPlayer])
        

    
    def GetReplaceInfo(self, iPlayer):
        dInfo = {
            '$count': str(self.m_CollectData.get('MutantNum', 0)),
            '$limit': str(self.m_CollectData.get('MutantLimit', 0)) }
        return dInfo



def DiceChallengeChoosePointAndLv(oWarMgr):
    oDiceElement = oWarMgr.GetDiceElement()
    if not oDiceElement:
        return (0, 0)
    return oDiceElement.ChooseChallengePointAndLv()


def CustomAddPerform(oWarrior, iPerformSID, iLevel, dArgs):
    if not oWarrior:
        return None
    oPerform = oWarrior.AddPerform(iPerformSID, iLevel, iEnable = 0)
    if not oPerform:
        return None
    for sKey, iValue in dArgs.items():
        oPerform.SetArgValue(sKey, iValue)
    
    oPerform.Enable(oWarrior)

