# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_relic.pyc
# RelativePath: clientlogic/cl_minigame/mg_relic.pyc
# Source Generated with Decompyle++
# File: mg_relic.pyc (Python 3.6)

from cl_only import ChooseKey, Functor, DeepCopy, ShufferList
from cl_commondefines import NWARRIOR_DROP_RELIC, VIRTUAL_ITEM_DROP, DEFAULT_DROP_RADIUS, RELIC_SUBMSG_GENERATE_CHOOSE, RELIC_SUBMSG_GENERATE_SURVIVOR, PLAYER_CHOOSEALL_RELIC, MG_RELIC, VIRTUAL_ITEM_RELIC, PLAYER_CHOOSE_ROLL, PLAYER_CHOOSE_GENERAL, PLAYER_CHOOSE_EXTEND, VIRTUAL_ITEM_MAGICPOWER, NWARRIOR_DROP_MAGIC_POWER, DROP_REASON_NPCREWARD
from cl_cscommondef import ALL_QUALITY_DESORDER
from cl_minigame import MiniGameRelicAttrInfo
from cl_reward import RewardItem
from cl_object.logging import WarrewardLog
from .mobject import CDropGame, CBaseGameData, CRewardChooseGame, CDropChoose
import cl_perform.load
import cl_math
import cl_npc.net as npcnet
import cl_msgcenter
import cl_drop

def ReSendRewardInfo(iMiniGame, oOwner, oTarget, dInfo):
    oMiniGame = oOwner.m_Game.m_MiniGameMgr.GetMiniGame(iMiniGame)
    if not oMiniGame:
        return None
    if not oOwner or oTarget.m_Scene != oOwner.m_Scene:
        return None
    if oTarget.m_ID == oMiniGame.m_Player:
        oMiniGame.SendChoose()


def PlayerChooseRelicEnd(iMiniGameID, oHero, iChooseAll):
    cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RELIC_CHOOSE_END, 'ClearChooseAll%d' % iMiniGameID)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RELIC_CHOOSE_END, oHero, dInfo = {
        'ChooseAll': iChooseAll })


def MiniGameEnd(oMiniGame):
    oMiniGame.m_Game.DoneGlobalAttention(oMiniGame.m_Owner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'PlayEnterScene%d' % oMiniGame.m_ID)
    oMiniGame.End()


def RewardRelic(who, iMiniGame, iRelic, dInfo, iChooseAll):
    dRelicReward = {
        'item': VIRTUAL_ITEM_RELIC,
        'info': {
            'sid': iRelic,
            'amount': 1,
            'level': dInfo['Level'] } }
    dExtInfo = {
        'NoSendCreateRelicMsg': True }
    if 'ExtendBag' in dInfo:
        dExtInfo['ExtendBag'] = 1
    RewardItem(who.m_Game, who, [
        dRelicReward], 'PlayerChoose%s' % iRelic, dExtInfo)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHOOSE_RELIC, who, dInfo = {
        'MGID': iMiniGame,
        'Relic': iRelic,
        'ChooseAll': iChooseAll })


def RewardMagicPowerDrop(who, oMiniGame, dRewardInfo, iCanChooseAll):
    oGame = who.m_Game
    oWarMgr = oGame.m_WarMgr
    oRelicTalentElement = oWarMgr.GetComponent('RelicTalentElement')
    if not oRelicTalentElement or not (oRelicTalentElement.m_Enable):
        return None
    iMagicPower = dRewardInfo['MagicPower']
    iOption = dRewardInfo['Option']
    if iCanChooseAll:
        vPos = (dRewardInfo['Pos'][0], oMiniGame.GetDropBasePos()[1], dRewardInfo['Pos'][2])
    else:
        vPos = oMiniGame.GetDropBasePos()
    oNpc = oGame.GetObject(oMiniGame.m_Owner)
    if not oNpc:
        return None
    oResMgr = oGame.m_ResMgr
    dDrop = {
        'Option': iOption,
        'MagicPower': iMagicPower,
        'Notify': oRelicTalentElement.m_MagicNotify }
    if iOption in oRelicTalentElement.m_MagicDrop:
        dDrop['SID'] = oRelicTalentElement.m_MagicDrop[iOption]
    dExtraInfo = {
        'DropReason': DROP_REASON_NPCREWARD }
    oDrop = oResMgr.CreateDrop(oNpc.m_Scene, NWARRIOR_DROP_MAGIC_POWER, vPos, [
        dDrop], dExtraInfo, { }, who.m_ID)
    oDrop.DelayPick(who)


def PlayerChooseGeneral(oMiniGame, oHero, idx, dExtInfo = None):
    lstReward = oMiniGame.Query('Reward', [])
    oGame = oHero.m_Game
    iMiniGame = oMiniGame.m_ID
    if oMiniGame.m_bOnlyChooseAll:
        WarrewardLog.Alert('%s %s %s only chooseall' % (oGame.m_ID, iMiniGame, oHero.m_PlayerID))
        return None
    iChooseAll = 0
    if idx >= len(lstReward):
        return None
    (iReward, dRewardInfo) = lstReward[idx]
    iType = dRewardInfo['Type']
    lstReward[idx][0] = 0
    if iReward == 0:
        WarrewardLog.Alert('%s %s %s %s reward is none' % (oGame.m_ID, iMiniGame, oHero.m_PlayerID, idx))
        return None
    if oHero.GetRelicChooseAllCnt() > 0:
        iCanChooseAll = 1
    else:
        iCanChooseAll = 0
    if iType == VIRTUAL_ITEM_RELIC:
        if dExtInfo and 'ExtendBag' in dExtInfo:
            dRewardInfo['ExtendBag'] = 1
        RewardRelic(oHero, iMiniGame, iReward, dRewardInfo, iChooseAll)
    elif iType == VIRTUAL_ITEM_MAGICPOWER:
        RewardMagicPowerDrop(oHero, oMiniGame, dRewardInfo, iCanChooseAll)
    if iCanChooseAll:
        oMiniGame.SetOnlyChooseAll()
        return None
    if iType == VIRTUAL_ITEM_RELIC:
        PlayerChooseRelicEnd(oMiniGame.m_ID, oHero, iChooseAll)
    MiniGameEnd(oMiniGame)


def PlayerChooseExtendRelic(oMiniGame, oHero, idx):
    oGame = oHero.m_Game
    oRelicCon = oHero.m_RelicCon
    iMiniGame = oMiniGame.m_ID
    if not oRelicCon.IsOpenExtendBag():
        WarrewardLog.Alert('%s %s %s choose extend not open' % (oGame.m_ID, iMiniGame, oHero.m_PlayerID))
        return None
    dExtInfo = {
        'ExtendBag': 1 }
    PlayerChooseGeneral(oMiniGame, oHero, idx, dExtInfo)


def ClearChooseAllMiniGame(iMiniGame, oHero, dMsgInfo):
    if not dMsgInfo['ChooseAll']:
        return None
    oGame = oHero.m_Game
    oMiniGame = oGame.m_MiniGameMgr.GetMiniGame(iMiniGame)
    if not oMiniGame:
        return None
    if oHero.GetRelicChooseAllCnt() <= 0:
        oMiniGame.Set('Reward', [])
        oNpc = oGame.GetObject(oMiniGame.m_Owner)
        if oNpc and oNpc.m_Scene == oHero.m_Scene:
            oMiniGame.SendChoose()
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RELIC_CHOOSE_END, 'ClearChooseAll%d' % iMiniGame)
        MiniGameEnd(oMiniGame)


def PlayerChooseAllRelic(oMiniGame, who, iAnswer):
    oGame = who.m_Game
    iMiniGame = oMiniGame.m_ID
    iCnt = who.GetRelicChooseAllCnt()
    if iCnt <= 0:
        WarrewardLog.Alert('%s %s %s no choose cnt' % (oGame.m_ID, iMiniGame, who.m_PlayerID))
        return None
    who.SetRelicChooseAllCnt(iCnt - 1)
    lstReward = oMiniGame.Query('Reward', [])
    oMiniGame.Set('Reward', [])
    iChooseAll = 1
    oRelicCon = who.m_RelicCon
    for iReward, dInfo in lstReward:
        if iReward == 0:
            continue
        iType = dInfo['Type']
        if iType == VIRTUAL_ITEM_RELIC:
            oRelic = oRelicCon.GetPerform(iReward)
            iLevel = dInfo['Level']
            if oRelic and iLevel <= oRelic.m_Level:
                dStaticInfo = {
                    'DropLevel': iLevel,
                    'DropSource': oRelicCon.m_PlayerID }
                cl_drop.DropPerform(who, iReward, dStaticInfo, bFly = True, iShare = 1)
                continue
            RewardRelic(who, iMiniGame, iReward, dInfo, iChooseAll)
            continue
        if iType == VIRTUAL_ITEM_MAGICPOWER:
            RewardMagicPowerDrop(who, oMiniGame, dInfo, 0)
    
    PlayerChooseRelicEnd(oMiniGame.m_ID, who, iChooseAll)
    MiniGameEnd(oMiniGame)


def PlayerRollRelic(oMiniGame, who, iAnswer):
    oGame = who.m_Game
    iMiniGame = oMiniGame.m_ID
    if oMiniGame.m_bOnlyChooseAll:
        WarrewardLog.Alert('%s %s %s only chooseall' % (oGame.m_ID, iMiniGame, who.m_PlayerID))
        return None
    if who.GetRollRelicCnt() <= 0:
        return None
    oRoll = oGame.m_WarMgr.GetComponent('RollRelicElement')
    if not oRoll:
        return None
    lstReward = oMiniGame.Query('Reward', [])
    oMiniGame.Set('Reward', [])
    for iRelic, dInfo in lstReward:
        if iAnswer == iRelic:
            iLevel = dInfo['Level']
            oRoll.RollMiniGameRelic(who, iLevel, oMiniGame.m_SID, iAnswer)
            break
    
    MiniGameEnd(oMiniGame)


class CRelicDropChoose(CDropChoose):
    
    def Filter(cls, oPlayer, dWeight, iCanRepeat = 0):
        return oPlayer.m_RelicCon.GetChooseRelicWeight(dWeight, iCanRepeat)

    Filter = classmethod(Filter)
    
    def Choose(cls, oPlayer, dWeight):
        oGame = oPlayer.m_Game
        dWeight = cls.Filter(oPlayer, dWeight)
        iRelic = oGame.m_RandomMgr.ChooseKey('relic%d' % oPlayer.m_ID, {
            'Select': dWeight })
        if not iRelic:
            return 0
        return iRelic

    Choose = classmethod(Choose)
    
    def FilterByQuality(cls, dWeight, iTargetQuality, dCheckQuality = { }):
        if iTargetQuality not in ALL_QUALITY_DESORDER:
            return { }
        setTargetQlt = cl_perform.load.GetRelicSetByQuality(iTargetQuality)
        dRet = { v: k for k, v in dWeight.items() if k in setTargetQlt }
        if not dRet and iTargetQuality > min(ALL_QUALITY_DESORDER):
            for iQuality in ALL_QUALITY_DESORDER:
                if iQuality not in dCheckQuality:
                    continue
                if iQuality >= iTargetQuality:
                    continue
                setQlt = cl_perform.load.GetRelicSetByQuality(iQuality)
                dRet = { v: k for k, v in dWeight.items() if k in setQlt }
                if dRet:
                    break
            
        return dRet

    FilterByQuality = classmethod(FilterByQuality)
    
    def ChooseExt(cls, oPlayer, dWeight, dExt):
        oGame = oPlayer.m_Game
        dQuality = dExt['Quality']
        if dQuality:
            iTargetQuality = ChooseKey(oGame, dQuality)
        else:
            iTargetQuality = 0
        dRepeatWeight = dWeight
        dOriWeight = cls.Filter(oPlayer, dWeight)
        iLimitQuality = dExt.get('LimitQuality', 0)
        dCheckQuality = dQuality if not iLimitQuality else { }
        if iTargetQuality:
            dWeight = cls.FilterByQuality(dOriWeight, iTargetQuality, dCheckQuality)
        else:
            dWeight = dOriWeight
        if not dWeight and iTargetQuality != 0:
            iFailedQuality = iTargetQuality
            for _ in range(len(dQuality)):
                iAdjustWeight = 0
                for iQuality in reversed(ALL_QUALITY_DESORDER):
                    if iQuality not in dQuality:
                        continue
                    if iFailedQuality >= iQuality:
                        iAdjustWeight += dQuality.pop(iQuality)
                        continue
                    dQuality[iQuality] += iAdjustWeight
                
                iNewTargetQuality = ChooseKey(oGame, dQuality)
                if iNewTargetQuality:
                    dWeight = cls.FilterByQuality(dOriWeight, iNewTargetQuality, dCheckQuality)
                if dWeight or not dQuality:
                    break
                iFailedQuality = iNewTargetQuality
            
        if not dWeight and iTargetQuality != 0 and iLimitQuality:
            dRepeatWeight = cls.Filter(oPlayer, dRepeatWeight, iCanRepeat = 1)
            dWeight = cls.FilterByQuality(dRepeatWeight, iTargetQuality, dQuality)
        if not dWeight:
            dWeight = cls.Filter(oPlayer, dExt['WeightStandby'])
        iRelic = oGame.m_RandomMgr.ChooseKey('relic%d' % oPlayer.m_ID, {
            'Select': dWeight })
        if not iRelic:
            return 0
        return iRelic

    ChooseExt = classmethod(ChooseExt)


class CDropRelicGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_RELIC
    m_ChooseWeight = { }
    m_FilterList = []
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropRelicGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CRelicDropChoose

    GetChooseClass = classmethod(GetChooseClass)


class CDropRelicGame(CDropGame):
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        lstReward = []
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return lstReward
        iTime = self.Query('Times', 1)
        lstWeightPop = self.Query('Exclude', [])
        for _ in range(iTime):
            iRelic = oChoosePool.QueryChoose(self.m_SID, {
                'lstWeightPop': lstWeightPop })
            if not iRelic:
                continue
            lstWeightPop.append(iRelic)
            lstDropInfo = [
                iRelic]
            vPos = self.m_Data['DropPos'] if 'DropPos' in self.m_Data else self.GetDropBasePos()
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RELIC,
                    'DropInfo': lstDropInfo,
                    'DropPos': vPos } }
            if 'DropLevel' in self.m_Data:
                clsPerform = cl_perform.GetPerformModule(iRelic)
                dReward['info']['DropLevel'] = self.m_Data['DropLevel'] if clsPerform.m_MaxLevel >= self.m_Data['DropLevel'] else 1
            lstReward.append(dReward)
        
        if len(lstReward) < iTime:
            LogEmpty(self)
        return lstReward



class CRewardChooseRelicGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_RELIC
    m_ChooseWeight = { }
    m_FilterList = []
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CRewardChooseRelicGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CRelicDropChoose

    GetChooseClass = classmethod(GetChooseClass)


class CRewardChooseRelicGame(CRewardChooseGame):
    m_SubOp = PLAYER_CHOOSE_GENERAL
    m_C2GSOPFunc = {
        PLAYER_CHOOSE_EXTEND: PlayerChooseExtendRelic,
        PLAYER_CHOOSEALL_RELIC: PlayerChooseAllRelic,
        PLAYER_CHOOSE_ROLL: PlayerRollRelic,
        PLAYER_CHOOSE_GENERAL: PlayerChooseGeneral }
    
    def __init__(self, oGame):
        super(CRewardChooseRelicGame, self).__init__(oGame)
        self.m_bOnlyChooseAll = False

    
    def OnInit(self):
        super(CRewardChooseRelicGame, self).OnInit()
        self.m_bOnlyChooseAll = False

    
    def SetOnlyChooseAll(self):
        self.m_bOnlyChooseAll = True
        oPlayer = self.m_Game.GetObject(self.m_Player)
        if oPlayer:
            iMiniGameID = self.m_ID
            cl_msgcenter.AddFunction(oPlayer, cl_msgcenter.MSG_WAR_RELIC_CHOOSE_END, Functor(ClearChooseAllMiniGame, iMiniGameID), 'ClearChooseAll%d' % iMiniGameID, -1, 0)
            npcnet.GS2CNpcChooseEnable(oPlayer.m_PlayerID, self.m_Owner, 0)

    
    def GetRewardInfo(self):
        lstReward = []
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return lstReward
        dChooseCnt = self.Query('ChooseCnt', { })
        dMsgInfo = { }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHOOSE_RELIC_START, oGame.GetObject(self.m_Player), dMsgInfo)
        iChooseCnt = ChooseKey(oGame, dChooseCnt)
        if 'ChooseCnt' in dMsgInfo:
            iChooseCnt = dMsgInfo['ChooseCnt']
        if not iChooseCnt:
            return lstReward
        iStartIdx = 0
        iTotalIdx = iChooseCnt
        vPos = self.GetDropBasePos()
        vFace = oOwner.GetFacing()
        vVertical = (-vFace[2], 0, vFace[0])
        fHeight = oOwner.m_ModelData.GetModelHeight()
        vPos = (vPos[0], vPos[1] + 1.5 * fHeight, vPos[2])
        fInterval = DEFAULT_DROP_RADIUS * 2
        lstRelicChoosed = []
        oNpc = self.m_Game.GetObject(self.m_Owner)
        dQuality = oNpc.GetArgValue('GMQuality')
        if dQuality:
            lstRelic = list(self.m_ChooseWeight)
            lstRelic = ShufferList(oGame, lstRelic)
            iQuality = None
            for iRelic in lstRelic:
                oPerform = cl_perform.GetPerformModule(iRelic)
                if iQuality and oPerform.m_Quality != iQuality:
                    continue
                if oPerform.m_Quality not in dQuality:
                    continue
                if dQuality[oPerform.m_Quality] <= 0:
                    del dQuality[iQuality]
                    if not dQuality:
                        break
                iLevel = dMsgInfo['RelicDropLevel'] if 'RelicDropLevel' in dMsgInfo else 1
                if 'ReplaceRelicInfo' in dMsgInfo:
                    iCanRepeat = dMsgInfo['RelicCanRepeat']
                    for iReplaceRelic, iReplaceLevel in dMsgInfo['ReplaceRelicInfo']:
                        if not iCanRepeat and iReplaceRelic in lstRelicChoosed:
                            continue
                        iRelic = iReplaceRelic
                        oPerform = cl_perform.GetPerformModule(iRelic)
                        iLevel = iReplaceLevel
                    
                lstRelicChoosed.append(iRelic)
                lstAttr = MiniGameRelicAttrInfo(oPerform, iLevel, oGame)
                lstReward.append([
                    iRelic,
                    {
                        'Pos': vDropPos,
                        'Attr': lstAttr,
                        'Level': iLevel,
                        'Type': VIRTUAL_ITEM_RELIC }])
                if len(lstReward) == iChooseCnt:
                    break
            
            if iQuality:
                dQuality[iQuality] -= 1
                if dQuality[iQuality] <= 0:
                    del dQuality[iQuality]
            if not dQuality:
                oNpc.DelArgValue('GMQuality')
            else:
                for idx in range(iChooseCnt):
                    iRelic = oChoosePool.QueryChoose(self.m_SID, {
                        'lstWeightPop': lstRelicChoosed })
                    if not iRelic:
                        continue
                    oPerform = cl_perform.GetPerformModule(iRelic)
                    if not oPerform:
                        WarrewardLog.Warn('%s no relic %s' % (self.m_SID, iRelic))
                        break
                    vDropPos = cl_math.Vec3DisplaceDir(vPos, vVertical, fInterval * (iStartIdx + idx - (iTotalIdx - 1) / 2))
                    dMsgInfo = {
                        'Relic': iRelic,
                        'Level': 1 }
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oGame.GetObject(self.m_Player), dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_CHOOSE)
                    iLevel = dMsgInfo['RelicDropLevel'] if 'RelicDropLevel' in dMsgInfo else 1
                    if 'ReplaceRelicInfo' in dMsgInfo:
                        iCanRepeat = dMsgInfo['RelicCanRepeat']
                        for iReplaceRelic, iReplaceLevel in dMsgInfo['ReplaceRelicInfo']:
                            if not iCanRepeat and iReplaceRelic in lstRelicChoosed:
                                continue
                            iRelic = iReplaceRelic
                            oPerform = cl_perform.GetPerformModule(iRelic)
                            if 'RelicUseOldLevel' in dMsgInfo and not dMsgInfo['RelicUseOldLevel']:
                                iLevel = iReplaceLevel
                        
                    lstRelicChoosed.append(iRelic)
                    lstAttr = MiniGameRelicAttrInfo(oPerform, iLevel, oGame)
                    lstReward.append([
                        iRelic,
                        {
                            'Pos': vDropPos,
                            'Attr': lstAttr,
                            'Level': iLevel,
                            'Type': VIRTUAL_ITEM_RELIC }])
                
        if len(lstReward) < iChooseCnt:
            LogEmpty(self)
        oGame.AddGlobalAttention(oOwner.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, Functor(ReSendRewardInfo, self.m_ID), 'PlayEnterScene%d' % self.m_ID)
        dMsgInfo = {
            'Relic': lstRelicChoosed,
            'Source': 'MiniGame',
            'MGOwner': self.m_Owner,
            'MGOwnerSID': oOwner.m_SID,
            'Reward': lstReward }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC, oGame.GetObject(self.m_Player), dMsgInfo)
        if 'SubOp' in dMsgInfo:
            self.m_SubOp = dMsgInfo['SubOp']
        return lstReward

    
    def SendChoose(self):
        lstReward = self.Query('Reward', [])
        oPlayer = self.m_Game.GetObject(self.m_Player)
        if oPlayer:
            npcnet.GS2CNpcChooseReward(oPlayer, self.m_Owner, lstReward, self.m_ID, self.m_SubOp)
            if self.m_bOnlyChooseAll:
                npcnet.GS2CNpcChooseEnable(oPlayer.m_PlayerID, self.m_Owner, 0)
        self.Leave()



class CRelicGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_RELIC
    m_ChooseWeight = { }
    m_FilterList = []
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CRelicGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CRelicDropChoose

    GetChooseClass = classmethod(GetChooseClass)


class CRelicGame(CDropGame):
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        lstReward = []
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return lstReward
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return lstReward
        iTimes = self.Query('Times', 1)
        clsData = oGame.m_WarData.GetMiniGameData(self.m_SID)
        bChangeRemove = True if clsData.m_ValidRemove != -1 else False
        lstRelicChoosed = self.Query('Exclude', [])
        iLimitQuality = self.Query('LimitQuality', 0)
        dExt = { }
        if bChangeRemove:
            dExt['remove'] = clsData.m_ValidRemove
        for _ in range(iTimes):
            iRelic = oChoosePool.QueryChoose(self.m_SID, {
                'lstWeightPop': lstRelicChoosed,
                'LimitQuality': iLimitQuality })
            if not iRelic:
                continue
            lstRelicChoosed.append(iRelic)
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iRelic,
                    'amount': 1 } }
            dReward['info'].update(dExt)
            if 'Level' in self.m_Data:
                clsPerform = cl_perform.GetPerformModule(iRelic)
                dReward['info']['level'] = self.m_Data['Level'] if clsPerform.m_MaxLevel >= self.m_Data['Level'] else 1
            lstReward.append(dReward)
        
        if len(lstReward) < iTimes:
            LogEmpty(self)
        return lstReward



class CUpgradeChooseRelicGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_RELIC
    m_ChooseWeight = { }
    m_FilterList = []
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CUpgradeChooseRelicGame

    GetGameClass = classmethod(GetGameClass)
    
    def GetChooseClass(cls):
        return CRelicDropChoose

    GetChooseClass = classmethod(GetChooseClass)


class CUpgradeChooseRelicGame(CRewardChooseGame):
    
    def GetRewardInfo(self):
        dReward = { }
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        iChooseCnt = self.Query('ChooseCnt', 0)
        if not iChooseCnt:
            return dReward
        oHero = oGame.GetObject(self.m_Player)
        if not oHero:
            return dReward
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(self.m_Player)
        if not oChoosePool:
            return dReward
        lstRelicChoosed = []
        for _ in range(iChooseCnt):
            iRelic = oChoosePool.QueryChoose(self.m_SID, {
                'lstWeightPop': lstRelicChoosed })
            if not iRelic:
                continue
            oPerform = cl_perform.GetPerformModule(iRelic)
            if not oPerform:
                WarrewardLog.Warn('%s no relic %s' % (self.m_SID, iRelic))
                break
            lstRelicChoosed.append(iRelic)
            dMsgInfo = {
                'Relic': iRelic }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oHero, dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_SURVIVOR)
            iLevel = dMsgInfo['RelicDropLevel'] if 'RelicDropLevel' in dMsgInfo else 1
            lstAttr = MiniGameRelicAttrInfo(oPerform, iLevel, oGame)
            dReward[iRelic] = {
                'Attr': lstAttr,
                'Level': iLevel }
        
        if len(dReward) < iChooseCnt:
            LogEmpty(self)
        dMsgInfo = {
            'Relic': list(dReward),
            'Source': 'MiniGame' }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC, oGame.GetObject(self.m_Player), dMsgInfo)
        return dReward

    
    def SendChoose(self):
        oHero = self.m_Game.GetObject(self.m_Player)
        if oHero:
            dReward = self.Query('Reward', { })
            oSurvivor = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
            if oSurvivor:
                dExtInfo = self.Query('ExtInfo', { })
                oSurvivor.m_UpgradeMgr.AddRewardInfo(oHero, VIRTUAL_ITEM_RELIC, dReward, 'UpGradeMiniGame', dExtInfo)
        self.End()



def LogEmpty(oRelicGame):
    oHero = oRelicGame.m_Game.GetObject(oRelicGame.m_Player)
    if oHero:
        iPlayer = oHero.m_PlayerID
        dRelicIllus = oHero.Query('Illus', { }).get('Relic', { })
        lstHas = oHero.m_RelicCon.GetAllPerformSID()
        WarrewardLog.Warn('%s empty %s illus %s has %s' % (iPlayer, oRelicGame.m_SID, dRelicIllus, lstHas))

