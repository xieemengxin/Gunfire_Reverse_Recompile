# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/hidelevelnode.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/hidelevelnode.pyc
# Source Generated with Decompyle++
# File: hidelevelnode.pyc (Python 3.6)

from cl_cscommondef.cs_fight import LEVEL_TYPE_HIDE, NWARRIOR_NPC_TRANSFER, GAMETYPE_NONE, GAMETYPE_DEFEND
from cl_cscommondef.cs_other import CBEHAVIOR_TRANSFER_REMOVE
from cl_math import RotateByEuler
from cl_only import SendAlert
from cl_object.logging import LevelLog
import cl_notify
import cl_msgcenter
import cl_snetwar
from . import baselevelnode

class CHideLevelNode(baselevelnode.CBaseLevelNode):
    m_LevelType = LEVEL_TYPE_HIDE
    m_GameType = GAMETYPE_NONE
    m_TargetName = ''
    m_AttentionName = 'HideLevelNode'
    
    def OnLevelInit(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        oScene.m_ScenePreLoad.InitPreLoadData({
            'NoWeapon': 1 })

    
    def InitFarTransferInfo(self, lstHero):
        if 'FarTransferInfo' in self.m_CustomData:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        if not oWarMgr or oWarMgr.IsSingleGame():
            return None
        dFarTransferInfo = { }
        for iPlayer in oWarMgr.GetRoomPlayer():
            dFarTransferInfo[iPlayer] = 1
        
        bFirst = True
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            dFarTransferInfo.pop(oHero.m_PlayerID, 0)
            if not bFirst:
                continue
            bFirst = False
            vPos = oHero.GetPos()
            tFace = oHero.GetFacing()
            tOppFace = RotateByEuler(tFace, (0, 180, 0))
            self.m_CustomData['CachePos'] = vPos
            self.m_CustomData['CacheFace'] = tOppFace
        
        LevelLog.Debug(f'''{self.m_Game.m_ID} {self.m_Level} initfartransferinfo {dFarTransferInfo}''')
        self.m_CustomData['FarTransferInfo'] = dFarTransferInfo
        for iPlayer, iLeftTimes in dFarTransferInfo.items():
            cl_snetwar.GS2CTransferHideLevelInfo(self.m_Game, iPlayer, self.m_Level, iLeftTimes)
        

    
    def AddTransferHero(self, oHero):
        dFarTransferHero = self.m_CustomData.setdefault('TransferHero', { })
        LevelLog.Info(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} {oHero.m_ID} addtransfer {dFarTransferHero}''')
        dFarTransferHero[oHero.m_ID] = 1

    
    def GetFarTransferInfo(self):
        if 'FarTransferInfo' in self.m_CustomData:
            return self.m_CustomData['FarTransferInfo']
        return { }

    
    def ValidTransfer(self, oHero):
        dFarTransferInfo = self.GetFarTransferInfo()
        if oHero.IsDead():
            return 0
        if oHero.m_PlayerID not in dFarTransferInfo:
            return 0
        if dFarTransferInfo[oHero.m_PlayerID] <= 0:
            return 0
        return 1

    
    def HeroEnterLevel(self, lstHero):
        dAssignBornPos = self.m_CtrlMgr.m_LevelAssignBornPos
        iMainLevel = self.m_CtrlMgr.m_CurNode.m_Level
        oWarMgr = self.m_Game.m_WarMgr
        dFarTransferInfo = self.GetFarTransferInfo()
        dFarTransferHero = self.m_CustomData['TransferHero'] if 'TransferHero' in self.m_CustomData else { }
        self.InitFarTransferInfo(lstHero)
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            if iHero in dFarTransferHero:
                dFarTransferHero.pop(iHero)
                vPos = self.m_CustomData['CachePos']
                tOppFace = self.m_CustomData['CacheFace']
            else:
                vPos = oHero.GetPos()
                tFace = oHero.GetFacing()
                tOppFace = RotateByEuler(tFace, (0, 180, 0))
            dFarTransferInfo.pop(oHero.m_PlayerID, 0)
            dLevelBornPos = dAssignBornPos.setdefault(iHero, { })
            data = dLevelBornPos.setdefault(iMainLevel, { })
            data['Pos'] = vPos
            data['Facing'] = tOppFace
            lstPlayer = oWarMgr.GetRoomPlayer()
            if oHero.m_PlayerID in lstPlayer:
                lstPlayer.remove(oHero.m_PlayerID)
            if lstPlayer:
                cl_notify.SendCommonNotify(self.m_Game, lstPlayer, 9303, {
                    '$$name': oHero.m_OwnerName })
        
        super(CHideLevelNode, self).HeroEnterLevel(lstHero)

    
    def GetAttentionKey(self):
        return '%s-%s' % (self.m_AttentionName, self.m_Scene)

    
    def OnPlayerMapLoadOK(self, oLevelCtrl, oHero, dInfo):
        super(CHideLevelNode, self).OnPlayerMapLoadOK(oLevelCtrl, oHero, dInfo)
        if dInfo['LevelID'] != oLevelCtrl.m_CurNode.m_Level:
            return None
        dFarTransferInfo = self.GetFarTransferInfo()
        if oHero.m_PlayerID in dFarTransferInfo:
            cl_snetwar.GS2CTransferHideLevelInfo(self.m_Game, oHero.m_PlayerID, self.m_Level, dFarTransferInfo[oHero.m_PlayerID])



class CChallengeHideLevelNode(CHideLevelNode):
    
    def OnLevelInit(self):
        super(CChallengeHideLevelNode, self).OnLevelInit()
        self.m_ValidEnterLevel = True
        cl_msgcenter.AddFunction(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnChallengeTrigger, 'ChallengeHideLevel', -1, 0)

    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, 'ChallengeHideLevel')

    
    def OnChallengeTrigger(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        iRlt = dMsgInfo['Rlt']
        if self.m_Level != iLevel:
            return None
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        lstPlayer = oScene.GetPlayers()
        cl_notify.SendCommonNotify(oGame, lstPlayer, 2119 if iRlt else 2120, { })
        self.m_ValidEnterLevel = iRlt
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, 'ChallengeHideLevel')
        if not iRlt:
            oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
            iScene = oLevelCtrl.m_CurNode.m_Scene
            oScene = oGame.m_SceneMgr.GetScene(iScene)
            for iNpc in oScene.GetObjectsByType('Transfer'):
                oNpc = oGame.GetObject(iNpc)
                if not oNpc:
                    continue
                if oNpc.m_FightType != NWARRIOR_NPC_TRANSFER:
                    continue
                if oNpc.Query('HideLevel', -1) != self.m_Level:
                    continue
                cl_snetwar.GS2CTriggerBehavior(oGame, iNpc, CBEHAVIOR_TRANSFER_REMOVE, lstPlayer)
                oNpc.Remove('ChallengeFail')
            

    
    def CheckHeroEnterLevel(self, lstHero):
        if not self.m_ValidEnterLevel:
            lstPlayer = []
            for iHero in lstHero:
                oHero = self.m_Game.GetObject(iHero)
                if not oHero:
                    continue
                lstPlayer.append(oHero.m_PlayerID)
            
            cl_notify.SendCommonNotify(self.m_Game, lstPlayer, 2121, { })
        return self.m_ValidEnterLevel



class CDefendLevelNode(CHideLevelNode):
    m_GameType = GAMETYPE_DEFEND
    m_TargetName = '守卫目标'
    m_AttentionName = 'DefendHideLevelNode'
    
    def OnLevelInit(self):
        super().OnLevelInit()
        cl_msgcenter.AddFunction(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnChallengeTrigger, self.GetAttentionKey(), -1, 0)

    
    def Release(self):
        self.m_CtrlMgr.Remove_Call_Out(self.GetAttentionKey())
        super().Release()

    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.GetAttentionKey())

    
    def OnChallengeTrigger(self, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        iRlt = dMsgInfo['Rlt']
        if self.m_Level != iLevel:
            return None
        if 'Protege' not in dMsgInfo['OtherInfo']:
            SendAlert('err', '守护关%s触发了非守护挑战%s' % (iLevel, dMsgInfo['Type']))
            return None
        iProtege = dMsgInfo['OtherInfo']['Protege']
        cl_msgcenter.DoneEvent(self.m_CtrlMgr, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.GetAttentionKey())
        if not iRlt:
            oProtege = self.m_Game.GetObject(iProtege)
            if not oProtege:
                self.OnChallengeFail()
                return None
            iRemoveDelay = oProtege.m_RemoveDelay
            if iRemoveDelay:
                self.m_CtrlMgr.Call_Out(self.OnChallengeFail, iRemoveDelay, self.GetAttentionKey())
            else:
                self.OnChallengeFail()

    
    def OnChallengeFail(self):
        if not self.m_CtrlMgr:
            return None
        self.m_PassLevel = False
        self.LevelGoal({
            'PassLevel': False })


