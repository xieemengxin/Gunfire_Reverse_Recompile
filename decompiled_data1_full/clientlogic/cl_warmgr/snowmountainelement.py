# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/snowmountainelement.pyc
# RelativePath: clientlogic/cl_warmgr/snowmountainelement.pyc
# Source Generated with Decompyle++
# File: snowmountainelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_resmgr.aitempparam import GetAIConfParam
from cl_commondefines import PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, MONSTERAI_TYPE_HATESEARCH, WARRIOR_ELITE, SIDE_TYPE_MONSTER, LEVEL_TYPE_FIGHT, BUYRULE_CASHREFRESHFREE, BUYRULE_REFRESHFREE
from cl_only import Functor, SendAlert
import cl_msgcenter
import cl_snetwar

class CSnowMountainElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CSnowMountainElement, self).__init__(oGame, nid, oData)
        self.m_CallFlag = 'SnowMountainElement'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_EliteMonster = self.m_Data.m_Config.get('ELITE', [])
        self.m_ReplaceNpc = self.m_Data.m_Config.get('REPLACENPC', { })
        self.m_ExtraChallenge = self.m_Data.m_Config.get('EXTRACHALLENGE', { })
        self.InitElement()

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.OnKillMonSterGroup, 'KillMonSterGroup' + self.m_CallFlag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, 'AddPlayer' + self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, 'CreateMonster' + self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr.GetComponent('LevelCtrl'), cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.OnCreateNpc, 'ReplaceNpc' + self.m_CallFlag, -1, 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, 'KillMonSterGroup' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'AddPlayer' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, 'CreateMonster' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(self.m_WarMgr.GetComponent('LevelCtrl'), cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, 'ReplaceNpc' + self.m_CallFlag)
        super(CSnowMountainElement, self).Release()
        self.m_WarMgr = None

    
    def InitElement(self):
        self.m_WarMgr.Set('SnowMountainChallenge', self.m_ExtraChallenge)

    
    def OnHalfOpen(self):
        for iHero in self.m_WarMgr.GetAllHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            self.OnAddPlayer(self.m_WarMgr, {
                'oCtrlHero': oHero })
        

    
    def OnCreateMonster(self, oWarMgr, dInfo):
        if 'SnowMountainMonster' in dInfo:
            return None
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        iMonsterID = dInfo['Monster']
        oMonster = oGame.GetObject(iMonsterID)
        if oMonster.m_FightType & WARRIOR_ELITE != WARRIOR_ELITE or oMonster.Query('Demon'):
            return None
        iLevel = dInfo['LineIdx'][0] if dInfo['LineIdx'] else oLevelCtrl.m_CurNode.m_Level
        self.SuperMonster(oMonster, oLevelCtrl, iLevel)

    
    def OnAddPlayer(self, oWarMgr, dInfo):
        oHero = dInfo['oCtrlHero']
        oHero.m_BuyMgr.AddRule(BUYRULE_CASHREFRESHFREE, self.m_CallFlag, 1)
        oHero.m_BuyMgr.AddRule(BUYRULE_REFRESHFREE, self.m_CallFlag, 1)

    
    def OnCreateNpc(self, oLevelCtrl, dInfo):
        iNpc = dInfo['NPC']
        if iNpc in self.m_ReplaceNpc:
            iNewNpc = self.m_ReplaceNpc[iNpc]
            dInfo['NPC'] = iNewNpc

    
    def OnKillMonSterGroup(self, oWarMgr, dInfo):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        iLayerNum = oGame.m_WarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
        if iLayerNum != 4:
            return None
        iMaxLevel = oLevelCtrl.m_LevelCtrlConf[iLayerNum]['CtrlSize']
        iLevelNum = oLevelCtrl.m_LevelNum
        if iLevelNum == iMaxLevel:
            return None
        iGroupID = dInfo['GroupID']
        tLineIdx = dInfo['LineIdx']
        oLevelNode = oLevelCtrl.GetLevelNode(tLineIdx[0])
        if oLevelNode != oLevelCtrl.m_CurNode:
            return None
        iRoomPos = tLineIdx[1]
        oLineNode = oLevelNode.m_RoomList[iRoomPos][-1]
        iMaxGroup = oLineNode.m_MonsterCtrl.MaxGroup()
        if iMaxGroup != 1 and iGroupID != iMaxGroup - 1:
            return None
        iLevelType = oLevelNode.m_LevelType
        lstRoom = oLevelNode.m_RoomList
        if iLevelType == LEVEL_TYPE_FIGHT and iRoomPos == len(lstRoom) - 1:
            (vElitePos, dEliteDrop) = oLevelNode.GetEliteInfo(iRoomPos, oLevelCtrl.m_LevelConfData)
            if not vElitePos:
                SendAlert('err', '关卡%s 雪山模式未配置强化怪刷新点' % tLineIdx[0])
                return None
            vFace = oLineNode.m_MonsterCtrl.GetMonsterFacing(vElitePos)
            tLineIdx = (oLevelNode.m_Level, iRoomPos, 0)
            (ret, vPos2) = self.m_Game.Scene_GetSpace(oLevelNode.m_Scene, vElitePos)
            if ret:
                vElitePos = vPos2
            dAI = {
                'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
                'AIMethod': MONSTERAI_TYPE_DEFAULT }
            dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
            dAI.update(dHateSearchAI)
            iScene = oLevelNode.m_Scene
            dInfo = {
                'Pos': vElitePos,
                'Face': vFace,
                'AI': dAI,
                'tLineIdx': tLineIdx,
                'Scene': iScene }
            oWarData = oGame.m_WarData
            iNum = len(self.m_EliteMonster)
            iMonsterSID = self.m_EliteMonster[oGame.Random(iNum)]
            clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
            iDelayFrame = clsMonsterData.GetCreateDelayFrame()
            iEffectSID = clsMonsterData.m_CreateEffect
            if iEffectSID:
                iEffectID = oGame.NewNoSceneObjID()
                cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, vElitePos, oGame.GetRealPlayers())
            if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
            oLevelNode.LockRoom(iRoomPos, 'SnowMountain')
            if iDelayFrame:
                func = Functor(self.DelayCreateMonster, dInfo, oLevelCtrl, iMonsterSID, dEliteDrop)
                self.Call_Out(func, iDelayFrame, 'DelayCreateMonster' + self.m_CallFlag + str(oLevelNode.m_Level))
            else:
                self.DelayCreateMonster(dInfo, oLevelCtrl, iMonsterSID, dEliteDrop)

    
    def DelayCreateMonster(self, dInfo, oLevelCtrl, iMonsterSID, dEliteDrop):
        (iLevel, iRoomPos, _) = dInfo['tLineIdx']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode != oLevelCtrl.m_CurNode:
            return None
        self.Remove_Call_Out('DelayCreateMonster' + self.m_CallFlag + str(iLevel))
        oMonster = self.m_Game.m_ResMgr.CreateMonster(dInfo['Scene'], iMonsterSID, dInfo['Pos'], dInfo['Face'], SIDE_TYPE_MONSTER, 0, dInfo['AI'], dInfo['tLineIdx'], {
            'SnowMountainMonster': 1 })
        if oMonster:
            if dEliteDrop:
                oMonster.Set('FixDropPos', dEliteDrop['FixDropPos'])
                oMonster.Set('CheckDropInfo', dEliteDrop['CheckDropInfo'])
            self.SuperMonster(oMonster, oLevelCtrl, iLevel)
            oMonster.Set('SnowSuperMonster', 1)
            func = Functor(self.OnDie, oMonster.m_ID, iLevel, iRoomPos)
            self.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, func, 'OnDie' + self.m_CallFlag)
        else:
            SendAlert('err', '关卡%s 雪山模式配置强化怪SID:%s不存在' % (iLevel, iMonsterSID))
            self.UnlockRoom(oLevelCtrl, iLevel, iRoomPos)

    
    def OnDie(self, iMonsterID, iLevel, iRoomPos, oLevelCtrl, oVictim, dInfo):
        if oVictim.m_ID != iMonsterID:
            return None
        self.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, 'OnDie' + self.m_CallFlag)
        self.UnlockRoom(oLevelCtrl, iLevel, iRoomPos)

    
    def UnlockRoom(self, oLevelCtrl, iLevel, iRoomPos):
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        oLevelNode.UnlockRoom(iRoomPos, 'SnowMountain')

    
    def SuperMonster(self, oMonster, oLevelCtrl, iLevel):
        oSuperCom = self.m_Game.m_WarMgr.GetComponent('MonsterSuper')
        if oSuperCom:
            oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
            (iAfPF, iPlusPF) = oSuperCom.RandomMonsterSuperInfo(oMonster, [], oLevelNode.m_LevelType)
            iSuperLevel = oSuperCom.GetMonsterSuperLevel(oLevelNode.m_LevelType)
            oMonster.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)



def GetComponentClass(oMgrManager):
    return CSnowMountainElement

