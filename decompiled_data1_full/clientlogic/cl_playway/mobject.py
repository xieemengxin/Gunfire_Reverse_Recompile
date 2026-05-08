# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_playway/mobject.pyc
# RelativePath: clientlogic/cl_playway/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import Functor, ChooseKey, SendAlert, DeepCopy, Time2Frame
from cl_object.logging import LogicwarningLog, WarrelicLog
from cl_commondefines import MG_BULLET, MG_EQUIP, WARRIOR_MONSTER, MODEL_TYPE_SPHERE, SIDE_TYPE_HERO, OBSTACLE_SOURCE_LEVEL, MODEL_TYPE_BOX, NWARRIOR_DROP_TREASURE_DEAD, NWARRIOR_DROP_RELIC, DAM_TYPE_NORMAL, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, LEVEL_TYPE_HALL, VIRTUAL_ITEM_RELIC
from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON
from cl_pxlayer import PXLAYER_DEVENT
import cl_msgcenter
import cl_perform
import cl_formula
import cl_war
import cl_engphyobj
import cl_snetwar
import cl_reward

class CBasePlayWay(object):
    m_PlayWayName = ''
    
    def __init__(self, oDayTrial, oGame, iSourceItemSID):
        self.m_DayTrial = oDayTrial
        self.m_Game = oGame
        self.m_Key = '%s-%s' % (iSourceItemSID, self.__class__.__name__[1:])
        self.m_SourcItemSID = iSourceItemSID
        self.m_Data = { }

    
    def Init(self, tParam):
        pass

    
    def Release(self):
        self.m_DayTrial = None
        self.m_Game = None
        self.m_Data = { }

    
    def GetClientData(self, oHero):
        iHero = oHero.m_ID
        if iHero in self.m_Data:
            return self.m_Data[iHero]



class CPlayerAddSkill(CBasePlayWay):
    m_PlayWayName = '玩家附加技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnCreatePlayer, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnCreatePlayer(self, oListener, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['Hero']
        if oHero:
            oHero.AddPerform(self.m_PerformSID, 1)

    
    def Release(self):
        lstHero = self.m_Game.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                oHero.m_Perform.RemovePerform(oHero, self.m_PerformSID)
        
        super().Release()



class CMonsterAddSkill(CBasePlayWay):
    m_PlayWayName = '怪物附加技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        self.m_MonsterDict = tParam[1]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnCreateMonster(self, oListener, oWarMgr, dMsgInfo):
        iMonsterID = dMsgInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonsterID)
        if oMonster:
            if not self.m_MonsterDict:
                oMonster.AddPerform(self.m_PerformSID, 1)
            elif oMonster.m_SID in self.m_MonsterDict:
                oMonster.AddPerform(self.m_PerformSID, 1)



class CPlayerAddRelic(CBasePlayWay):
    m_PlayWayName = '获得指定秘卷'
    
    def Init(self, tParam):
        (self.m_Relic, self.m_ValidRemove) = tParam
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInit, f'''{self.m_Key}{self.m_Relic}''')

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['oCtrlHero']
        if oHero:
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_ADDRELIC, Functor(self.OnAddRelic, self.m_ValidRemove), 'DayTrialAddRelic')
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': self.m_Relic } }
            cl_reward.RewardItem(oHero.m_Game, oHero, [
                dReward], 'DayTrialAddRelic')

    
    def OnAddRelic(self, iValidRemove, oHero, dMsgInfo):
        dMsgInfo['ValidRemove'] = iValidRemove



class CRandomRelic(CBasePlayWay):
    m_PlayWayName = '获得随机秘卷'
    
    def Init(self, tParam):
        (self.m_RelicType, self.m_Quality, self.m_Num) = tParam
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInit, f'''{self.m_Key}{self.m_RelicType}''')

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        oHero = dMsgInfo['oCtrlHero']
        if not oHero:
            return None
        dValid = { }
        setAllUnlock = oHero.Query('Illus')['Relic']
        lstHas = oHero.m_RelicCon.GetAllPerformSID()
        for iRelic in setAllUnlock:
            if iRelic in lstHas:
                continue
            clsRelic = cl_perform.GetPerformModule(iRelic)
            if not clsRelic:
                continue
            if self.m_RelicType and clsRelic.m_RelicType != self.m_RelicType:
                continue
            if self.m_Quality and clsRelic.m_Quality != self.m_Quality:
                continue
            dValid[iRelic] = 1
        
        lstRelic = []
        for _ in range(self.m_Num):
            iRelic = ChooseKey(oGame, dValid)
            if not iRelic:
                tParam = (self.m_RelicType, self.m_Quality, self.m_Num)
                LogicwarningLog.Alert('daytrial %s no enough relic %s %s' % (oHero.m_ID, self.m_SourcItemSID, tParam))
                break
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iRelic } }
            cl_reward.RewardItem(oHero.m_Game, oHero, [
                dReward], 'DayTrialAddRandomRelic')
            dValid.pop(iRelic)
            lstRelic.append(iRelic)
        
        self.m_Data[oHero.m_ID] = lstRelic



class CSetMaxRelic(CBasePlayWay):
    m_PlayWayName = '设置秘卷上限'
    
    def Init(self, tParam):
        self.m_Num = tParam[0]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInit, f'''{self.m_Key}{self.m_Num}''')

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        oHero = dMsgInfo['oCtrlHero']
        if oHero:
            oHero = oGame.GetObject(oHero.m_ID)
            cbfunc = Functor(self.OnAddRelic)
            oHero.m_RelicCon.SetMaxRelicNum(self.m_Num, cbfunc)

    
    def OnAddRelic(self, oRelicCon, oNewRelic):
        oGame = self.m_Game
        iMax = oRelicCon.MaxRelicNum()
        lstAll = oRelicCon.GetAllPerformSID()
        if len(lstAll) > iMax:
            iNewRelic = oNewRelic.m_SID
            dValid = dict.fromkeys(lstAll, 1)
            dValid.pop(iNewRelic, 0)
            iRemoveRelic = ChooseKey(oGame, dValid)
            oRelicCon.RemoveRelic(iRemoveRelic, 'trialRelicTopLimit', 1)
            oRelicCon.GS2CReplaceRelic(iRemoveRelic, iNewRelic)



class CReplaceNpc(CBasePlayWay):
    m_PlayWayName = '替换Npc'
    
    def Init(self, tParam):
        self.m_ReplaceNpc = tParam[0]
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, self.OnCreateNpc, self.m_Key)

    
    def OnCreateNpc(self, oListener, oLevelCtrl, dMsgInfo):
        iNpc = dMsgInfo['NPC']
        if iNpc in self.m_ReplaceNpc:
            iNewNpc = ChooseKey(self.m_Game, self.m_ReplaceNpc[iNpc])
            dMsgInfo['NPC'] = iNewNpc



class CChangeLevelChooseCnt(CBasePlayWay):
    m_PlayWayName = '修改关卡抽取数量'
    
    def Init(self, tParam):
        (self.m_CntType, self.m_CntChange, self.m_LevelLimitChange) = tParam
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSECNT, self.OnChooseLevelCnt, self.m_Key + str(self.m_CntType))

    
    def OnChooseLevelCnt(self, oListener, oLevelCtrl, dMsgInfo):
        iType = dMsgInfo.get('Type', None)
        if iType == self.m_CntType:
            dMsgInfo['ChooseData']['Expect'] += self.m_CntChange
            dLimit = dMsgInfo['ChooseData']['Limit']
            for (iLayer, iLevel), iLimit in self.m_LevelLimitChange.items():
                if iLayer != oLevelCtrl.m_LayerNum:
                    continue
                dLimit[iLevel] = iLimit
            



class CIgnoreChallenge(CBasePlayWay):
    m_PlayWayName = '屏蔽房间挑战投放'
    
    def Init(self, tParam):
        sIgnore = tParam[0]
        lstIgnore = []
        for sKey in sIgnore.split('|'):
            if not sKey:
                continue
            iChallenge = int(sKey) % 10000
            lstIgnore.append(iChallenge)
        
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        oLevelCtrl.m_RoomChallenge.AddIgnoreChallenge(lstIgnore)



class CChangeLayerMonsterCnt(CBasePlayWay):
    m_PlayWayName = '修改指定幕的怪物数量'
    
    def Init(self, tParam):
        (self.m_Layer, self.m_AddCnt) = tParam
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERMONSTERCNT, self.OnChooseMonsterCnt, self.m_Key + str(self.m_Layer))

    
    def OnChooseMonsterCnt(self, oListener, oLevelCtrl, dMsgInfo):
        iExtAmount = dMsgInfo.get('ExtAmount', 0)
        iLayerNum = dMsgInfo.get('LayerNum', 0)
        if iLayerNum == self.m_Layer:
            iAddAmount = int(cl_formula.GetFormulaResult(self, self.m_AddCnt))
            dMsgInfo['ExtAmount'] = iExtAmount + iAddAmount



class CReplaceMonster(CBasePlayWay):
    
    def Init(self, tParam):
        self.m_ReplaceDict = tParam[0]
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CREATEMONSTER_PRE, self.OnCreateMonsterPre, self.m_Key)

    
    def OnCreateMonsterPre(self, oListener, oLevelCtrl, dMsgInfo):
        lstCreateInfo = dMsgInfo['CreateInfo']
        if not lstCreateInfo:
            return None
        oWarData = self.m_Game.m_WarData
        for dInfo in lstCreateInfo:
            iOldMonsterSID = dInfo['MonsterSID']
            if iOldMonsterSID not in self.m_ReplaceDict:
                continue
            iNewMonsterSID = self.m_ReplaceDict[iOldMonsterSID]
            clsNewMonsterData = oWarData.GetMonsterData(iNewMonsterSID)
            if not clsNewMonsterData:
                iWarNo = self.m_Game.GetWarMgr().m_SID
                SendAlert('err', '每日试炼战场%d 未配置怪物SID%d' % (iWarNo, iNewMonsterSID))
                continue
            dInfo['MonsterSID'] = iNewMonsterSID
        



class CSummonAddSkill(CBasePlayWay):
    m_PlayWayName = '召唤物附加技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WAR_CREATESUMMON, self.OnCreateSummon, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnCreateSummon(self, oListener, oTarget, dMsgInfo):
        iSummonID = dMsgInfo['Summon']
        oSummon = self.m_Game.GetObject(iSummonID)
        if oSummon:
            oSummon.AddPerform(self.m_PerformSID, 1)



class CChangeMonsteraf(CBasePlayWay):
    m_PlayWayName = '修改怪物词缀抽取'
    
    def Init(self, tParam):
        dMonsterAfLibrary = { }
        for iKey, iValue in tParam[0].items():
            dMonsterAfLibrary[iKey] = iValue
        
        self.m_Game.m_WarMgr.GetComponent('MonsterSuper').m_MonsterAfLib[2] = dMonsterAfLibrary



class CAddPerformOnRoomStart(CBasePlayWay):
    m_PlayWayName = '关卡房间目标开始时添加技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMSTART, self.OnRoomStart, self.m_Key)
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnRoomStart, self.m_Key)

    
    def OnRoomStart(self, oListener, oLevelCtrl, dMsgInfo):
        oScene = dMsgInfo['oScene']
        for iHero in oScene.GetHeros():
            oHero = self.m_Game.GetObject(iHero)
            oHero.AddPerform(self.m_PerformSID, 1)
        



class CChangeWeaponDamType(CBasePlayWay):
    m_PlayWayName = '非元素武器随机获得一种属性'
    
    def Init(self, tParam):
        self.m_Inscription = []
        for iInscription in tParam:
            self.m_Inscription.append(iInscription)
        
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WAR_GREATEWEAPON, self.OnCreateWeapon, self.m_Key)

    
    def OnCreateWeapon(self, oListener, oTarget, dMsgInfo):
        oWeapon = dMsgInfo['Weapon']
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        lstInscription = self.m_Inscription
        if not oInscriptionCom:
            return None
        if len(list(set(lstInscription) & set(oInscriptionCom.m_Inscription))) > 0:
            iNewNum = oInscriptionCom.m_InscriptionNum + 1
            oInscriptionCom.m_InscriptionNum = iNewNum
            oInscriptionCom.AddInscription()
            oInscriptionCom.m_Item.GS2CItemPropChange('Inscription', oInscriptionCom.GetAllInscription())
            return None
        if oWeapon.m_Type == EQUIP_TYPE_FUNDAMENTALWEAPON:
            return None
        if oWeapon.m_ElementType != DAM_TYPE_NORMAL:
            return None
        lstInscription = self.m_Inscription
        iInscription = lstInscription[self.m_Game.Random(len(lstInscription))]
        clsPerform = cl_perform.GetPerformModule(iInscription)
        if not clsPerform.CheckValidItem(oWeapon, oInscriptionCom.m_Inscription):
            return None
        oInscriptionCom.AppendInscription(iInscription)
        oInscriptionCom.m_InscriptionNum = oInscriptionCom.m_InscriptionNum + 1
        oInscriptionCom.m_Item.GS2CItemPropChange('Inscription', oInscriptionCom.GetAllInscription())



class CChangeWeaponDebuffProb(CBasePlayWay):
    m_PlayWayName = '修改所有武器元素异常概率'
    
    def Init(self, tParam):
        self.m_Mul = tParam[0]
        self.m_Add = tParam[1]
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WAR_GREATEWEAPON, self.OnCreateWeapon, self.m_Key)

    
    def OnCreateWeapon(self, oListener, oTarget, dMsgInfo):
        oWeapon = dMsgInfo['Weapon']
        oWeapon.AttrChange('DebuffProb', self.m_Mul, self.m_Add, self.m_Key, 0)



class CFilterAssignHideLevel(CBasePlayWay):
    m_PlayWayName = '屏蔽指定隐藏关'
    
    def Init(self, tParam):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        tFilterLevel = oLevelCtrl.m_FilterHideLevel
        oLevelCtrl.m_FilterHideLevel = tuple(set(tFilterLevel) | set(tParam[0]))



class CRandomRelicInList(CBasePlayWay):
    m_PlayWayName = '从指定遗物中随机获取一个'
    
    def Init(self, dParam):
        self.m_lstRelic = dParam[0]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInit, self.m_Key)

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        oGame = self.m_Game
        dChosen = { }
        oHero = dMsgInfo['oCtrlHero']
        if not oHero:
            return None
        dRelic = { }
        for iRelic, iGroup in self.m_lstRelic.items():
            if iGroup not in dRelic:
                dRelic[iGroup] = []
            dRelic[iGroup].append(iRelic)
        
        dChosen[oHero.m_ID] = []
        for lstRelic in dRelic.values():
            iRelic = lstRelic[oGame.Random(len(lstRelic))]
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iRelic } }
            cl_reward.RewardItem(oHero.m_Game, oHero, [
                dReward], 'DayTrialAddRandomRelic')
            dChosen[oHero.m_ID].append(iRelic)
        
        self.m_Data = dChosen



class CAddPerformOnLevelNodeGoalOK(CBasePlayWay):
    m_PlayWayName = '关卡目标达成添加技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelNodeGoalOK, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnLevelNodeGoalOK(self, oListener, oLevelCtrl, dMsgInfo):
        oGame = self.m_Game
        for iHero in oGame.m_WarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHero)
            if oHero:
                oHero.AddPerform(self.m_PerformSID, 1)
        



class CAddPerformOnChallengeOver(CBasePlayWay):
    m_PlayWayName = '挑战事件完成添加技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnChallengeOver, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnChallengeOver(self, oListener, oLevelCtrl, dMsgInfo):
        oGame = self.m_Game
        for iHero in oGame.m_WarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHero)
            if oHero:
                oHero.AddPerform(self.m_PerformSID, 1)
        



class CChangeMainLvItemChoose(CBasePlayWay):
    m_PlayWayName = '修改主线关卡道具抽取配置'
    
    def Init(self, tParam):
        self.m_ChooseItem = { }
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        dAllChooseItem = oLevelCtrl.m_ChooseItem
        dConfig = tParam[0]
        for iItem, _ in dConfig.items():
            if iItem not in dAllChooseItem:
                continue
            self.m_ChooseItem.update(DeepCopy(dAllChooseItem[iItem]))
        
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_CHOOSEITEM, self.OnChooseItem, self.m_Key)

    
    def OnChooseItem(self, oListener, oLevelCtrl, dMsgInfo):
        iLayerNum = dMsgInfo['iLayerNum']
        iLevelNum = dMsgInfo['iLevelNum']
        dChooseItem = dMsgInfo['ChooseData']
        tKey = (iLayerNum, iLevelNum)
        if tKey not in self.m_ChooseItem:
            return None
        for sKey in dChooseItem.keys():
            if sKey in self.m_ChooseItem[tKey]:
                dChooseItem[sKey] = self.m_ChooseItem[tKey][sKey]
        



class CAddRelicWhenPickRelic(CBasePlayWay):
    m_PlayWayName = '拾取秘卷时随机获得一个秘卷'
    
    def Init(self, tParam):
        self.m_PickQuality = tParam[0]
        self.m_MiniGame = tParam[1] % 10000
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInit, f'''{self.m_Key}{self.m_MiniGame}''')
        self.m_PickHis = { }

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['oCtrlHero']
        if oHero:
            self.m_PickHis[oHero.m_ID] = []
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_PICK, self.OnPick, f'''{self.m_Key}{self.m_MiniGame}''', -1, 0)

    
    def OnPick(self, oHero, dMsgInfo):
        if dMsgInfo['Type'] != NWARRIOR_DROP_RELIC:
            return None
        iItem = dMsgInfo['Item']
        if iItem in self.m_PickHis[oHero.m_ID]:
            return None
        clsItem = cl_perform.GetPerformModule(iItem)
        if clsItem.m_Quality != self.m_PickQuality:
            return None
        self.m_PickHis[oHero.m_ID].append(iItem)
        clsMiniGame = self.m_Game.m_WarData.GetMiniGameData(self.m_MiniGame)
        if not clsMiniGame:
            return None
        dWeight = { }
        setAllUnlock = oHero.Query('Illus')['Relic']
        lstHas = oHero.m_RelicCon.GetAllPerformSID()
        for iRelic, iWeight in clsMiniGame.m_ChooseWeight.items():
            if iRelic in lstHas:
                continue
            if iRelic not in setAllUnlock:
                continue
            if iItem == iRelic:
                continue
            dWeight[iRelic] = iWeight
        
        if not dWeight:
            WarrelicLog.Alert(f'''CAddRelicWhenPickRelic choose weight {dWeight}''')
            return None
        iChoose = ChooseKey(self.m_Game, dWeight)
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iChoose } }
        cl_reward.RewardItem(oHero.m_Game, oHero, [
            dReward], self.m_Key)
        oHero.m_RelicCon.GS2CAddExtraRelic(iChoose)



class CFilterSublime(CBasePlayWay):
    m_PlayWayName = '屏蔽指定升华'
    
    def Init(self, tParam):
        self.m_SublimeSID = tParam[0]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYERINFO, self.OnInit, f'''{self.m_Key}{self.m_SublimeSID}''')

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        dInfo = dMsgInfo.get('Info', { })
        dSubliamation = dInfo.get('Sublimation', { })
        if self.m_SublimeSID in dSubliamation:
            dSubliamation.pop(self.m_SublimeSID)



class CFilterAssignMainLevel(CBasePlayWay):
    m_PlayWayName = '屏蔽指定主线关'
    
    def Init(self, tParam):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        tFilterLevel = oLevelCtrl.m_FilterMainLevel
        oLevelCtrl.m_FilterMainLevel = tuple(set(tFilterLevel) | set(tParam[0]))



class CUsePerformWhenDropDisppear(CBasePlayWay):
    m_PlayWayName = '在宝珠掉落物消失时释放技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        self.m_LauncherSID = tParam[1]
        self.m_RemoveTime = tParam[2]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROPDISAPPEAR, self.OnDisppear, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnDisppear(self, oListener, oWarMgr, dMsgInfo):
        if 'Type' not in dMsgInfo or dMsgInfo['Type'] != NWARRIOR_DROP_TREASURE_DEAD:
            return None
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
                0,
                0,
                0],
            'Size': (0, 0, 0),
            'Origin': dMsgInfo['DropPos'],
            'Shape': MODEL_TYPE_BOX,
            'Source': OBSTACLE_SOURCE_LEVEL,
            'Live': 0,
            'Perform': [] }
        oLauncher = self.m_Game.m_ResMgr.CreateBuild(dMsgInfo['Scene'], self.m_LauncherSID, dInfo)
        oPerform = oLauncher.GetPerformIfNoThenNew(self.m_PerformSID)
        oLauncher.SetSide(SIDE_TYPE_HERO)
        dData = {
            'vStart': dMsgInfo['DropPos'] }
        cl_war.UsePerform(oLauncher, oPerform, dData)
        oLauncher.Call_Out(Functor(oLauncher.Remove, 'RemoveTime'), Time2Frame(self.m_RemoveTime), 'RemoveTime')



class CBeadDropSceneEventDrop(CBasePlayWay):
    m_PlayWayName = '宝珠掉落物场景事件'
    
    def Init(self, tParam):
        self.m_Radius = tParam[0]
        self.m_PerformSID = tParam[1]
        self.m_DelayTime = tParam[2]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROP, self.OnDrop, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnDrop(self, oListener, oWarMgr, dMsgInfo):
        if 'Drop' not in dMsgInfo:
            return None
        oGame = self.m_Game
        oDrop = oGame.GetObject(dMsgInfo['Drop'])
        if not oDrop or oDrop.m_FightType != NWARRIOR_DROP_TREASURE_DEAD:
            return None
        dShapeInfo = {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': self.m_Radius }
        if 'Delaytime' in dMsgInfo and dMsgInfo['Delaytime']:
            oDrop.Call_Out(Functor(self.DelayAction, oDrop, dShapeInfo), Time2Frame(dMsgInfo['Delaytime']), 'DelayTimeAction')
        else:
            self.DelayAction(oDrop, dShapeInfo)

    
    def DelayAction(self, oDrop, dShapeInfo):
        if self.m_DelayTime:
            oDrop.Call_Out(Functor(self.DoAction, oDrop, dShapeInfo), Time2Frame(self.m_DelayTime), 'EventDelayAction')
        else:
            self.DoAction(oDrop, dShapeInfo)

    
    def DoAction(self, oDrop, dShapeInfo):
        oDrop.m_Trigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, oDrop, PXLAYER_DEVENT, dShapeInfo, self.OnTrigger)
        oDrop.m_Trigger.rigidbody.E_SetKinematic(1)

    
    def OnTrigger(self, oTarget, iLeave):
        if not oTarget.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
            return None
        if not iLeave:
            oTarget.AddPerform(self.m_PerformSID, 1)
        else:
            oTarget.m_Perform.RemovePerform(oTarget, self.m_PerformSID)



class CChangeMiniGameInfo(CBasePlayWay):
    m_PlayWayName = '修改奖励权重比例'
    
    def Init(self, tParam):
        self.m_Param = tParam
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_MINIGAMEINIT, self.OnInitMiniGmae, self.m_Key)

    
    def OnInitMiniGmae(self, oListener, oWarMgr, dMsgInfo):
        iType = dMsgInfo['MiniGameType'] if 'MiniGameType' in dMsgInfo else 0
        dChooseWeight = dMsgInfo['ChooseWeight'] if 'ChooseWeight' in dMsgInfo else { }
        if iType == MG_EQUIP:
            if self.m_Param[0] not in dChooseWeight:
                return None
            iRatio = dChooseWeight[self.m_Param[0]]
            iRatio += iRatio * self.m_Param[1] // 10000 + self.m_Param[2]
            dChooseWeight[self.m_Param[0]] = iRatio
        elif iType == MG_BULLET:
            dBulletBag = dMsgInfo['ExtInfo']
            for idx, dInfo in dBulletBag.items():
                if self.m_Param[0] not in dInfo:
                    continue
                iRatio = dChooseWeight[idx]
                iRatio += iRatio * self.m_Param[1] // 10000 + self.m_Param[2]
                dChooseWeight[idx] = iRatio
            



class CAddRelicWhenRelife(CBasePlayWay):
    m_PlayWayName = '复活时随机获取秘卷'
    
    def Init(self, tParam):
        self.m_MiniGame = tParam[0] % 10000
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInit, f'''{self.m_Key}{self.m_MiniGame}''')

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['oCtrlHero']
        if oHero:
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, f'''{self.m_Key}{self.m_MiniGame}''', -1, 0)

    
    def OnRelife(self, oHero, dMsgInfo):
        clsMiniGame = self.m_Game.m_WarData.GetMiniGameData(self.m_MiniGame)
        if not clsMiniGame:
            return None
        dWeight = { }
        setAllUnlock = oHero.Query('Illus')['Relic']
        lstHas = oHero.m_RelicCon.GetAllPerformSID()
        for iRelic, iWeight in clsMiniGame.m_ChooseWeight.items():
            if iRelic in lstHas:
                continue
            if iRelic not in setAllUnlock:
                continue
            dWeight[iRelic] = iWeight
        
        iChoose = ChooseKey(self.m_Game, dWeight)
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iChoose } }
        cl_reward.RewardItem(oHero.m_Game, oHero, [
            dReward], self.m_Key)
        oHero.m_RelicCon.GS2CAddExtraRelic(iChoose)



class CSetGoldencupRefresh(CBasePlayWay):
    m_PlayWayName = '设置金爵刷新信息'
    
    def Init(self, tParam):
        self.m_MaxRefreshTime = tParam[0]
        self.m_RefreshCost = tParam[1]
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteract, self.m_Key)

    
    def OnInteract(self, oListener, oTarget, dMsgInfo):
        iNpc = dMsgInfo['NPC']
        oGame = self.m_Game
        oNpc = oGame.GetObject(iNpc)
        oHero = oGame.GetObject(dMsgInfo['Hero'])
        if self.ValidSetInfo(oNpc, oHero):
            oNpc.SetRefreshCost(self.m_RefreshCost, dMsgInfo['Hero'])
            oNpc.SetMaxRefreshTimes(self.m_MaxRefreshTime, dMsgInfo['Hero'])

    
    def ValidSetInfo(self, oNpc, oHero):
        if not oNpc:
            return False
        if oNpc.m_FightType not in [
            NWARRIOR_NPC_GOLDENCUP,
            NWARRIOR_NPC_LIMITGOLDENCUP,
            NWARRIOR_NPC_EXCHANGEGOLDENCUP]:
            return False
        if oNpc.m_IsExtraInteractRule:
            return False
        if oNpc.GetMaxRefreshTimes(oHero):
            return False
        return True



class CSetRelicRefresh(CBasePlayWay):
    m_PlayWayName = '过关后刷新秘卷'
    
    def Init(self, tParam):
        self.m_RefreshNum = tParam[0]
        self.m_MiniGame = tParam[1]
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnStartRelicRefresh, self.m_Key)
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WAR_REFRESHRELIC, self.OnRelicRefresh, self.m_Key)
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, self.m_Key)

    
    def OnLevelFinish(self, oListener, oWarMgr, dMsgInfo):
        iKey = 'RefreshRelic' + self.m_Key
        if dMsgInfo['LevelType'] != LEVEL_TYPE_HALL:
            for iHero in oWarMgr.GetLiveHero():
                oHero = self.m_Game.GetObject(iHero)
                oHero.Set(iKey, self.m_RefreshNum)
            

    
    def OnStartRelicRefresh(self, oListener, oTarget, dMsgInfo):
        iKey = 'RefreshRelic' + self.m_Key
        oTarget.m_RelicCon.StartRelicRefresh(iKey)

    
    def OnRelicRefresh(self, oListener, oTarget, dMsgInfo):
        iKey = 'RefreshRelic' + self.m_Key
        oTarget.m_RelicCon.RelicRefresh(iKey, self.m_MiniGame, dMsgInfo)



class CBuildAddSkill(CBasePlayWay):
    m_PlayWayName = '建筑附加技能'
    
    def Init(self, tParam):
        self.m_PerformSID = tParam[0]
        self.m_BuildDict = tParam[1]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEBUILD, self.OnCreateBuild, f'''{self.m_Key}{self.m_PerformSID}''')

    
    def OnCreateBuild(self, oListener, oWarMgr, dMsgInfo):
        iBuildID = dMsgInfo['BuildID']
        oBuild = self.m_Game.GetObject(iBuildID)
        if oBuild:
            if not self.m_BuildDict:
                oBuild.AddPerform(self.m_PerformSID, 1)
            elif oBuild.m_SID in self.m_BuildDict:
                oBuild.AddPerform(self.m_PerformSID, 1)



class CExtraInfo(CBasePlayWay):
    m_PlayWayName = '额外信息显示'
    
    def Init(self, tParam):
        self.m_Ratio = tParam[0]
        cl_msgcenter.AddAttentionFunc(self.m_DayTrial, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnInit, self.m_Key + 'ExtraInfo')
        self.m_Game.AddGlobalAttention(self.m_DayTrial.m_ID, cl_msgcenter.MSG_WAR_ATTACK_END, self.OnAttackEnd, self.m_Key + 'ExtraInfo')

    
    def OnInit(self, oListener, oWarMgr, dMsgInfo):
        oHero = dMsgInfo['oCtrlHero']
        if oHero:
            self.m_Data[oHero.m_ID] = [
                0]

    
    def OnAttackEnd(self, oListener, oTarget, dMsgInfo):
        oWarMgr = self.m_Game.GetWarMgr()
        oReport = oWarMgr.GetComponent('Warreport')
        if not oReport:
            return None
        iMaxWeaponDamage = oReport.m_WarReportData.GetPlayerWarInfo(oTarget.m_PlayerID, 'MaxWeaponDamage')
        iMaxShow = (iMaxWeaponDamage // 100) * self.m_Ratio // 10000
        if self.m_Data[oTarget.m_ID][0] < iMaxShow:
            self.m_Data[oTarget.m_ID] = [
                iMaxShow]
            lstInfo = [
                (self.m_SourcItemSID, [
                    iMaxShow])]
            cl_snetwar.GS2CDayTrialItemInfo(oTarget, lstInfo)


