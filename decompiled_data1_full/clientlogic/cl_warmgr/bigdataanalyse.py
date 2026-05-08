# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/bigdataanalyse.pyc
# RelativePath: clientlogic/cl_warmgr/bigdataanalyse.pyc
# Source Generated with Decompyle++
# File: bigdataanalyse.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import BAG_TYPE_EXWEAPON, BAG_TYPE_WEAPONSTORE, HIDELV_TYPE_CASH, MONSTER_CLASSIFY_BOXMONSTER, PF_TYPE_THROW, PF_TYPE_MONSTERACT, PF_TYPE_CAREERPF, WARRIOR_SUMMON, WARRIOR_MONSTER, WARRIOR_HERO, BOSS_DONOT_COUNT, WARRIOR_BOSS, LEVEL_TYPE_HALL, LEVEL_TYPE_BOSS, LEVEL_TYPE_HIDE, LEVEL_TYPE_FIGHT, WARRIOR_BOSSKING, STATE_DEMONKING_TIME, TREASURERELIC_GENERATELIST, TREASURERELIC_SELECTRELIC, SERVANT_FIGHTTYPE_HUMAN, SERVANT_FIGHTTYPE_TURRET, ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAKNESS, NWARRIOR_DROP_AXE
from cl_commondefines import NWARRIOR_NPC_WEAPONSTORE, MONSTER_SITUATION_DIE, MONSTER_SITUATION_ALIVE, STATE_ABNORMAL_FIRE, RELIC_RS_LOAD, TYPE_INIT, TYPE_TO_FUSE, TYPE_TO_LOTTERY, ACTIVATE_LEAST_TIME, WARRIOR_BOSSSTAT, BUILD_LUOHOU_CUT, MONSTER_LUOHOU_CREATECUT, NWARRIOR_DROP_RAREITEM, MONSTER_QIANLONG_LOCK, MONSTER_QIANLONG_SUMMON, MONSTER_QIANLONG_ESCAPE, PHASE_CHALLENGE_BOXMONSTER, PHASE_CHALLENGE_KILLBOXMONSTER, QIANLONG_TYPE_CASH, QIANLONG_TYPE_BOXMONSTER, QIANLONG_TYPE_KILLBOXMONSTER, PHASE_CHALLENGE_START, PHASE_CHALLENGE_OVER, PHASE_CHALLENGE_PLAYERLEAVE, PHASE_CHALLENGE_SEARCHTREASURE
from cl_commondefines import NWARRIOR_NPC_TASKNPC, TASK_CREATETASKLIST, TASK_CHOOSETASK, TASK_CHANGESTATUS, SETTLE_FINISHWAR, VIRTUAL_ITEM_GOLDENCUP, TYPE_CHOOSERELIC, TYPE_CHOOSETALENT, TYPE_CREATETALENT, DEVICECOMP_TYPE_COMMON, DEVICECOMP_TYPE_HERO, DEVICECOMP_TYPE_DEVICE, HIDELV_TYPE_SIGHT, HIDELV_TYPE_TRAP, HIDELV_TYPE_JUMP, PET_HANDLE_ONECLICKFUSE, PET_HANDLE_ACTIVEABILITY, PET_HANDLE_FROM_BAG, PET_HANDLE_FROM_NPC, NWARRIOR_NPC_WANDSHOP, WANDCOMP_SUBMSG_REMOVE, WAND_COMP_TYPE_CONDITION, WAND_COMP_TYPE_ACTION, MAF_TYPE_SEASONWAND, MAX_LAYER, WAND_SUBMSG_UPGRADE
from cl_commondefines import CONQUER_CHALLENGE_START, CONQUER_CHALLENGE_REWARD, CONQUER_MONSTER_WEAK_START, CONQUER_MONSTER_WEAK_END, PET_HANDLE_RAPIDSCREEN, PET_HANDLE_SETEGGTYPE, ADD_DICEENERGY, PET_HANDLE_USEACTIVE, PET_HANDLE_FUSE, PLAYMODE_ROGUELIKE, PET_HANDLE_BUY, ALL_PET_TYPE, TASK_CHOOSE_STATUS_CHOSEN, TASK_CHOOSE_STATUS_LOCK, TASK_CHOOSE_STATUS_UNRECEIVED, UPGRADE_INS_RS_TASK, WAND_SUBMSG_TRIGGERACTION, WAND_SUBMSG_ADD, WANDCOMP_SUBMSG_ADD, WAND_QUALITY_RARE, WAND_QUALITY_TALE, FUNDAMENTAL_WAND, SETTLE_LOSEWAR, SETTLE_DIRECTLEAVE, WANDSHOP_INITGOODS, WANDSHOP_REFRESHGOODS, VIRTUAL_ITEM_WANDCOMP
from cl_commondefines import WAND_QUALITY_NORMAL, WAND_QUALITY_RARE, WAND_QUALITY_TALE, TYPE_RELIFE_GSCASH, TYPE_RELIFE_BUY, TYPE_RELIFE_KILLBOSS, STATE_TIME_FOREVER, BIGDATA_REALDIE_STATE, PLAY_TYPE_MULTI, DICE_SUBMSG_ASSEMBLE, DICE_SUBMSG_DISASSEMBLE, DICE_SUBMSG_ADD, DICEABILITY_QUALITY_RED, DICESHOP_BUY_DICEPACKET, DICESHOP_BUY_POINTDICE, NWARRIOR_NPC_DICESHOP, NWARRIOR_DROP_DICE, GARDENER_HERO, PLAY_TYPE_SINGLE, NWARRIOR_NPC_S7SHOP
from cl_commondefines import WARRIOR_BUILD, S7CRYSTAL_ADD, S7MODULE_ENHANCE, S7MODULE_AUTOENHANCE, S7MODULE_DECREASE, CRTSTAL_RAWMATERIAL, S7_AUTO_EQUIP, S7_AUTO_UNEQUIP, SEASONSHOP_INITS7GOODS, SEASONSHOP_BUYS7CRYSTAL, SEASONSHOP_BUYS7PACKET, S7MODULE_ADD, S7CRYSTAL_REMOVE, S7MODULE_REMOVE, S7CRYSTAL_POINTADD
from cl_item.defines import RAREITEM_MASK
from cl_only import Frame2Time, SendAlert, PY_FLAG_DEAD, GAME_FRAME, DeepCopy, DEAD_FLAG_REAL
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
from cl_object.logging import ErrLog, TaskLog, DiceLog
from cl_evcon import CheckInPointPerformByMsgInfo
from cl_commondecorator import CheckFaultToleranceWithDefault, CheckFaultTolerance
from cl_platformdata import GetMonsterAfTag, GetS7CrystalType
import cl_msgcenter
import cl_perform
import cllib.lib_flag as lib_flag
import cli_player
import cl_platformdata
import cl_formula
import cl_object
import cl_state
import cllib.lib_server as lib_server

class CBigDataAnalyseMgr(CBaseElement):
    m_DoNotSendWhenWarEnd = [
        'Weapon',
        'RealDie',
        'CrystalComponent',
        'AutoAssembly',
        'SeasonNpc']
    
    def __init__(self, oGame, nid, oData):
        super(CBigDataAnalyseMgr, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_AnalyseCom = { }

    
    def Release(self):
        for oCom in self.m_AnalyseCom.values():
            oCom.Release()
        
        super(CBigDataAnalyseMgr, self).Release()

    
    def Init(self):
        self.InitCom()

    
    def InitCom(self):
        self.m_AnalyseCom['Weapon'] = CWeaponAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Monster'] = CMonsterAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Perform'] = CPerformAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Relic'] = CRelicAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Challenge'] = CChallengeAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Boss'] = CBossAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Hide'] = CHideLevelAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Gemini'] = CGeminiAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Servant'] = CServantAnalyseCom(self.m_Game)
        self.m_AnalyseCom['Starlight'] = CStarlightAnalyseCom(self.m_Game)
        self.m_AnalyseCom['StormChaser'] = CStormChaserAnalyseCom(self.m_Game)
        self.m_AnalyseCom['SeasonBenediction'] = CSeasonBenedictionAnalyseCom(self.m_Game)
        self.m_AnalyseCom['DyingAndRealDeath'] = CDyingTimeAndRealDeathAnalyseCom(self.m_Game)
        if self.m_WarMgr.m_PlayMode == PLAYMODE_ROGUELIKE:
            self.m_AnalyseCom['SpecialHeroSkill'] = CSpecialHeroSkillCom(self.m_Game)
            self.m_AnalyseCom['Inscription'] = CInscriptionAnalyseCom(self.m_Game)
            self.m_AnalyseCom['HeroSkill'] = CHeroSkillAnalyseCom(self.m_Game)
        if self.m_WarMgr.m_PlayType == PLAY_TYPE_MULTI:
            self.m_AnalyseCom['RealDie'] = CRealDieAnalyseCom(self.m_Game)

    
    def GetWarStatistics(self, pid):
        dInfo = { }
        for sKey, oCom in self.m_AnalyseCom.items():
            if sKey in self.m_DoNotSendWhenWarEnd:
                continue
            dInfo[sKey] = oCom.GetStatistics(pid)
        
        return dInfo

    
    def Save(self):
        dData = { }
        for sKey, oCom in self.m_AnalyseCom.items():
            dData[sKey] = oCom.Save()
        
        return dData

    
    def Load(self, dData):
        for sKey, oCom in self.m_AnalyseCom.items():
            if sKey in dData:
                oCom.Load(dData[sKey])
        

    
    def GetCom(self, sKey):
        if sKey not in self.m_AnalyseCom:
            return None
        return self.m_AnalyseCom[sKey]

    
    def SetCom(self, sKey, oCom):
        self.m_AnalyseCom[sKey] = oCom

    
    def InitWandSeasonAnalyseCom(self):
        self.m_AnalyseCom['TokenAttack'] = CTokenAttackAnalyseCom(self.m_Game)
        self.m_AnalyseCom['TokenFirstOpporuntity'] = CTokenFirstOpportunityAnalyseCom(self.m_Game)
        self.m_AnalyseCom['WeaponToken'] = CWeaponTokenAnalyseCom(self.m_Game)
        self.m_AnalyseCom['BuyAmplifier'] = CBuyAmplifierAnalyseCom(self.m_Game)
        self.m_AnalyseCom['TokenEquip'] = CTokenEquipAnalyseCom(self.m_Game)
        self.m_AnalyseCom['TokenStrengthenMonster'] = CTokenStrengthenMonsterAnalyseCom(self.m_Game)
        self.m_AnalyseCom['TokenNpcCost'] = CTokenNpcCostAnalyseCom(self.m_Game)
        self.m_AnalyseCom['LevelToken'] = CLevelTokenAnalyseCom(self.m_Game)
        self.m_AnalyseCom['TokenEntry'] = CTokenEntryAnalyseCom(self.m_Game)

    
    def GetWandSeasonLevelStatistics(self, pid, dBigDataReport = None):
        if dBigDataReport is None:
            return None
        oTokenAttackCom = self.GetCom('TokenAttack')
        if oTokenAttackCom:
            dBigDataReport['BigDataAna']['TokenAttack'] = oTokenAttackCom.GetLevelStatistics(pid)
        oTokenFirstOpporuntityCom = self.GetCom('TokenFirstOpporuntity')
        if oTokenFirstOpporuntityCom:
            dBigDataReport['BigDataAna']['TokenFirstOpporuntity'] = oTokenFirstOpporuntityCom.GetStatistics(pid)
        oWeaponTokenCom = self.GetCom('WeaponToken')
        if oWeaponTokenCom:
            dBigDataReport['BigDataAna']['WeaponToken'] = oWeaponTokenCom.GetStatistics(pid)
        oBuyAmplifierCom = self.GetCom('BuyAmplifier')
        if oBuyAmplifierCom:
            dBigDataReport['BigDataAna']['BuyAmplifier'] = oBuyAmplifierCom.GetStatistics(pid)
        oTokenEquipCom = self.GetCom('TokenEquip')
        if oTokenEquipCom:
            dBigDataReport['BigDataAna']['TokenEquip'] = oTokenEquipCom.GetStatistics(pid)
        oTokenStrengthenMonsterCom = self.GetCom('TokenStrengthenMonster')
        if oTokenStrengthenMonsterCom:
            dBigDataReport['BigDataAna']['TokenStrengthenMonster'] = oTokenStrengthenMonsterCom.GetLevelStatistics(pid)
        oTokenNpcCostCom = self.GetCom('TokenNpcCost')
        if oTokenNpcCostCom:
            dBigDataReport['BigDataAna']['TokenNpcCost'] = oTokenNpcCostCom.GetStatistics(pid)
        oLevelTokenCom = self.GetCom('LevelToken')
        if oLevelTokenCom:
            dBigDataReport['BigDataAna']['LevelToken'] = oLevelTokenCom.GetStatistics(pid)

    
    def InitDiceSeasonAnalyseCom(self):
        self.m_AnalyseCom['DiceEquip'] = CDiceEquipAnalyseCom(self.m_Game)
        self.m_AnalyseCom['FinalDiceEquip'] = CFinalDiceEquipAnalyseCom(self.m_Game)
        self.m_AnalyseCom['FirstRedEnerty'] = CFirstRedEnertyAnalyseCom(self.m_Game)
        self.m_AnalyseCom['RecycleDice'] = CRecycleDiceAnalyseCom(self.m_Game)
        self.m_AnalyseCom['DiceBuy'] = CDiceBuyAnalyseCom(self.m_Game)
        self.m_AnalyseCom['DiceSpecialItem'] = CDiceSpecialItemAnalyseCom(self.m_Game)

    
    def GetDiceSeasonLevelStatistics(self, pid, dBigDataReport = None):
        if dBigDataReport is None:
            return None
        oDiceEquipAnalyseCom = self.GetCom('DiceEquip')
        if oDiceEquipAnalyseCom:
            dBigDataReport['BigDataAna']['DiceEquip'] = oDiceEquipAnalyseCom.GetStatistics(pid)
        oFirstRedEnertyAnalyseCom = self.GetCom('FirstRedEnerty')
        if oFirstRedEnertyAnalyseCom:
            dBigDataReport['BigDataAna']['FirstRedEnerty'] = oFirstRedEnertyAnalyseCom.GetStatistics(pid)
        oRecycleDiceAnalyseCom = self.GetCom('RecycleDice')
        if oRecycleDiceAnalyseCom:
            dBigDataReport['BigDataAna']['RecycleDice'] = oRecycleDiceAnalyseCom.GetStatistics(pid)
        oDiceBuyAnalyseCom = self.GetCom('DiceBuy')
        if oDiceBuyAnalyseCom:
            dBigDataReport['BigDataAna']['DiceBuy'] = oDiceBuyAnalyseCom.GetStatistics(pid)
        oDiceSpecialItemAnalyseCom = self.GetCom('DiceSpecialItem')
        if oDiceSpecialItemAnalyseCom:
            dBigDataReport['BigDataAna']['DiceSpecialItem'] = oDiceSpecialItemAnalyseCom.GetLevelStatistics(pid)

    
    def InitSeason7AnalyseCom(self):
        self.m_AnalyseCom['CrystalComponent'] = CCrystalComponentAnalyseCom(self.m_Game)
        self.m_AnalyseCom['SeasonNpc'] = CSeasonNpcAnalyseCom(self.m_Game)
        self.m_AnalyseCom['AutoAssembly'] = CAutoAssemblyAnalyseCom(self.m_Game)
        self.m_AnalyseCom['StrengthenRollback'] = CStrengthenRollbackAnalyseCom(self.m_Game)

    
    def GetSeason7LevelStatistics(self, pid, dBigDataReport = None):
        if dBigDataReport is None:
            return None
        oCrystalComponentAnalyseCom = self.GetCom('CrystalComponent')
        if oCrystalComponentAnalyseCom:
            dBigDataReport['BigDataAna']['CrystalComponent'] = oCrystalComponentAnalyseCom.GetLevelStatistics(pid)
        oSeasonNpcAnalyseCom = self.GetCom('SeasonNpc')
        if oSeasonNpcAnalyseCom:
            dBigDataReport['BigDataAna']['SeasonNpc'] = oSeasonNpcAnalyseCom.GetLevelStatistics(pid)
        oAutoAssemblyAnalyseCom = self.GetCom('AutoAssembly')
        if oAutoAssemblyAnalyseCom:
            dBigDataReport['BigDataAna']['AutoAssembly'] = oAutoAssemblyAnalyseCom.GetLevelStatistics(pid)
        oStrengthenRollbackAnalyseCom = self.GetCom('StrengthenRollback')
        if oStrengthenRollbackAnalyseCom:
            dBigDataReport['BigDataAna']['StrengthenRollback'] = oStrengthenRollbackAnalyseCom.GetStatistics(pid)



class CBaseAnalyseCom(object):
    
    def __init__(self, oGame):
        self.m_Data = None
        self.m_Game = oGame

    
    def Save(self):
        raise NotImplementedError('subclasses must implement')

    
    def Load(self, dData):
        raise NotImplementedError('subclasses must implement')

    
    def CanLoad(self):
        if self.m_Data:
            return False
        return True



class CWeaponAnalyseCom(CBaseAnalyseCom):
    m_NeedLayerAttr = [
        'HoldTime']
    m_LayerAttr = [ 'Layer' + sAttr for sAttr in m_NeedLayerAttr ]
    m_UnAccumulation = [
        'WeaponSID',
        'OutLayer',
        'LstInscription']
    
    def __init__(self, oGame):
        super(CWeaponAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_LayerData = { }

    
    def Release(self):
        self.m_Game = None

    
    def GetLevelStatistics(self, pid):
        if pid not in self.m_Data:
            return { }
        dRet = self.CustomFilter(pid, self.m_Data[pid])
        self.m_Data[pid] = { }
        return dRet

    
    def GetLayerStatistics(self, pid):
        dLayer = self.m_LayerData.pop(pid, { })
        dLayer = self.CustomLayerFilter(pid, dLayer)
        return dLayer

    
    def AddLevelWeaponAna(self, pid, dWeaponAnaExport):
        dData = self.m_Data
        if pid not in dData:
            dData[pid] = { }
        dPlayerData = dData[pid]
        for iWeaponID, dWeaponExport in dWeaponAnaExport.items():
            if iWeaponID not in dPlayerData:
                dPlayerData[iWeaponID] = { }
            dWeaponData = dPlayerData[iWeaponID]
            for sKey, val in dWeaponExport.items():
                if sKey in self.m_LayerAttr:
                    continue
                if sKey in dWeaponData and sKey in self.m_UnAccumulation:
                    continue
                if isinstance(val, int):
                    dWeaponData.setdefault(sKey, 0)
                    dWeaponData[sKey] += val
                    continue
                if isinstance(val, list):
                    dWeaponData.setdefault(sKey, [])
                    dWeaponData[sKey].extend(val)
                    continue
                if isinstance(val, float):
                    dWeaponData.setdefault(sKey, 0)
                    dWeaponData[sKey] += val
            
        

    
    def AddLayerWeaponAna(self, pid, iLayer, dWeaponAnaExport, iLevelType):
        if iLevelType not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_HIDE, LEVEL_TYPE_BOSS):
            return None
        dPlayerData = self.m_LayerData.setdefault(pid, { })
        for sKey in self.m_NeedLayerAttr:
            sLayerKey = 'Layer' + sKey
            for iWeaponID, dWeaponExport in dWeaponAnaExport.items():
                dWeaponData = dPlayerData.setdefault(iWeaponID, { })
                dWeaponData['WeaponSID'] = dWeaponExport['WeaponSID']
                dWeaponData['HoldInscription'] = dWeaponExport['HoldInscription']
                dLayerData = dWeaponData.setdefault(sLayerKey, { })
                iCurValue = dLayerData.setdefault(iLayer, 0)
                iAddValue = dWeaponExport[sKey]
                dLayerData[iLayer] = iCurValue + iAddValue
            
        

    AddLayerWeaponAna = CheckFaultTolerance(AddLayerWeaponAna)
    
    def Save(self):
        dRet = {
            'Layer': DeepCopy(self.m_LayerData) }
        return dRet

    
    def Load(self, dData):
        if not self.CanLoad() or not dData:
            return None
        if 'Layer' in dData:
            self.m_LayerData = dData['Layer']
        else:
            self.m_Data = dData

    
    def CustomFilter(self, pid, dData):
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            lstRemove = []
            iMaxHoldTime = -1
            iUseWeapon = 0
            iInitWeaponSID = oHero.GetInitWeaponSID()
            for iWeaponID, dWeapon in dData.items():
                if dWeapon['WeaponSID'] == iInitWeaponSID:
                    iHoldTime = dWeapon['HoldTime']
                    if iHoldTime > iMaxHoldTime:
                        iMaxHoldTime = iHoldTime
                        iUseWeapon = iWeaponID
                    lstRemove.append(iWeaponID)
            
            if lstRemove:
                lstRemove.remove(iUseWeapon)
                for iWeapon in lstRemove:
                    dData.pop(iWeapon)
                
        return dData

    
    def CustomLayerFilter(self, pid, dData):
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            oWieldCon = oHero.m_WieldCon
            lstUseWeapon = oWieldCon.GetAllItemIDByType(EQUIP_TYPE_MAINWEAPON)
            for iWeaponID, dWeapon in dData.items():
                if iWeaponID in lstUseWeapon:
                    oWeapon = oWieldCon.GetItemByID(iWeaponID)
                    if oWeapon:
                        dWeapon['IfEquip'] = 1
            
        return dData

    CustomLayerFilter = CheckFaultToleranceWithDefault(Default = { })(CustomLayerFilter)


class CChallengeAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CChallengeAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = []
        self.InitEvent()

    
    def InitEvent(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_TRIGGER_CHALLENGE_EVENT, self.OnTriggerChallengeEvent, 'OnTriggerChallengeEvent')

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def ReleaseEvent(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_TRIGGER_CHALLENGE_EVENT, 'OnTriggerChallengeEvent')

    
    def OnTriggerChallengeEvent(self, oWarMgr, oOwner, dInfo):
        iChallengeId = dInfo['ChallengeId']
        iChallengeLevelId = dInfo['ChallengeLevel']
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iLayerNum = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
        if (iChallengeId, iChallengeLevelId, iLayerNum) in self.m_Data:
            return None
        self.m_Data.append((iChallengeId, iChallengeLevelId, iLayerNum))

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            return self.m_Data
        return []

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData



class CRelicAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CRelicAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = {
            'BoxAppRelic': { },
            'BoxChoRelic': { },
            'AppTimes': { },
            'AbandonRelic': [],
            'AbaTimes': { },
            'ExcTimes': { },
            'ChoTimes': { } }
        self.m_RelicAbandonInfo = { }
        self.InitEvent()

    
    def InitEvent(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDRELIC, self.OnRelicPickUp, 'OnRelicPickUp')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVERELIC, self.OnRelicAbandon, 'OnRelicAbandon')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GENERATE_RELIC, self.OnRelicGenerate, 'OnRelicGenerate')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHOOSE_RELIC, self.OnChooseRelic, 'OnChooseRelic')

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def ReleaseEvent(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADDRELIC, 'OnRelicPickUp')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REMOVERELIC, 'OnRelicAbandon')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_GENERATE_RELIC, 'OnRelicGenerate')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CHOOSE_RELIC, 'OnChooseRelic')

    
    def OnChooseRelic(self, oWarMgr, oOwner, dInfo):
        iRelic = dInfo['Relic'] if 'Relic' in dInfo else 0
        if not iRelic:
            return None
        if iRelic not in self.m_Data['BoxChoRelic']:
            self.m_Data['BoxChoRelic'][iRelic] = 1

    
    def OnRelicAbandon(self, oWarMgr, oOwner, dInfo):
        iRelic = dInfo['iPerform'] if 'iPerform' in dInfo else 0
        if not iRelic:
            return None
        if iRelic not in self.m_Data['AbandonRelic']:
            self.m_Data['AbandonRelic'].append(iRelic)
        if iRelic not in self.m_Data['AbaTimes']:
            self.m_Data['AbaTimes'][iRelic] = 0
        self.m_Data['AbaTimes'][iRelic] += 1
        if iRelic not in self.m_RelicAbandonInfo:
            self.m_RelicAbandonInfo[iRelic] = []
        pid = oOwner.m_PlayerID
        self.m_RelicAbandonInfo[iRelic].append(pid)

    
    def OnRelicPickUp(self, oWarMgr, oOwner, dInfo):
        iRelic = dInfo['iPerform'] if 'iPerform' in dInfo else 0
        if not iRelic:
            return None
        if dInfo['Reason'] == RELIC_RS_LOAD:
            return None
        if iRelic not in self.m_Data['ChoTimes']:
            self.m_Data['ChoTimes'][iRelic] = 0
        self.m_Data['ChoTimes'][iRelic] += 1
        iPickUpPlayer = oOwner.m_PlayerID
        if iRelic in self.m_RelicAbandonInfo and iPickUpPlayer not in self.m_RelicAbandonInfo[iRelic]:
            if iRelic not in self.m_Data['ExcTimes']:
                self.m_Data['ExcTimes'][iRelic] = 0
            self.m_Data['ExcTimes'][iRelic] += 1

    
    def OnRelicGenerate(self, oWarMgr, oOwner, dInfo):
        lstRelic = dInfo['Relic'] if 'Relic' in dInfo else []
        for iRelic in lstRelic:
            if iRelic not in self.m_Data['AppTimes']:
                self.m_Data['AppTimes'][iRelic] = 0
            self.m_Data['AppTimes'][iRelic] += 1
        
        sSource = dInfo['Source'] if 'Source' in dInfo else ''
        if sSource == 'MiniGame':
            for iRelic in lstRelic:
                if iRelic not in self.m_Data['BoxAppRelic']:
                    self.m_Data['BoxAppRelic'][iRelic] = 0
                self.m_Data['BoxAppRelic'][iRelic] += 1
            

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            return self.m_Data
        return { }

    
    def Save(self):
        dData = { }
        dData['Data'] = self.m_Data
        dData['RelicAbandonInfo'] = self.m_RelicAbandonInfo
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['Data']
            self.m_RelicAbandonInfo = dData['RelicAbandonInfo']

    
    def CanLoad(self):
        bCan = True
        for value in self.m_Data.values():
            if value:
                bCan = False
                break
        
        if self.m_RelicAbandonInfo:
            bCan = False
        return bCan



class CBossAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CBossAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Key = 'CBossAnalyseCom'
        self.m_Data = { }
        self.m_BossLineInfo = { }
        self.m_BossRelicData = { }
        self.InitEvent()
        self.m_CurBoss = None
        self.m_CurLayer = 0
        self.m_CurPhase = 0
        self.m_KingCom = None
        self.m_LuoHouCom = None

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None
        self.m_CurBoss = None
        self.m_CurPhase = 0
        if self.m_KingCom:
            self.m_KingCom.Release()
        self.m_KingCom = None
        if self.m_LuoHouCom:
            self.m_LuoHouCom.Release()
        self.m_LuoHouCom = None

    
    def SetCurBoss(self, oBoss, iPhase):
        self.m_CurBoss = oBoss
        self.m_CurPhase = iPhase

    
    def GetStatistics(self, pid):
        if not IsValidStats(self.m_WarMgr, pid):
            return { }
        if self.m_CurBoss:
            dData = self.GetPhaseData(self.m_CurBoss.m_SID, self.m_CurLayer, self.m_CurPhase)
            if dData:
                dData['fight_result'] = 1
        dResultData = { }
        for iMonster, dLayerData in self.m_Data.items():
            for iLayer, dPhaseData in dLayerData.items():
                for iPhase, dData in dPhaseData.items():
                    if dData['start_frame']:
                        dData['fight_frame'] += self.m_Game.GetFrameNum() - dData['start_frame']
                        dData['start_frame'] = 0
                    dData['fight_time'] = Frame2Time(dData['fight_frame'])
                    if self.m_KingCom and iMonster in self.m_KingCom.m_Data and iLayer in self.m_KingCom.m_Data[iMonster] and iPhase in self.m_KingCom.m_Data[iMonster][iLayer]:
                        dData.update(self.m_KingCom.m_Data[iMonster][iLayer][iPhase])
                    if self.m_LuoHouCom and iMonster == self.m_LuoHouCom.m_OwnerSID and iLayer in self.m_LuoHouCom.m_Data and iPhase in self.m_LuoHouCom.m_Data[iLayer]:
                        dData.update(self.m_LuoHouCom.m_Data[iLayer][iPhase])
                
            
            dResultData[iMonster] = {
                'LayerData': dLayerData,
                'BossLineInfo': self.m_BossLineInfo.get(iMonster, { }),
                'BossRelicData': self.m_BossRelicData.get(iMonster, { }) }
        
        return dResultData

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)
    
    def InitEvent(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_SWITCH_PHASE, self.OnSwitchPhase, self.m_Key)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Key)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealDam, self.m_Key)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnSkillStart, self.m_Key)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, self.m_Key, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDBOSSRELIC, self.OnAddBossRelic, self.m_Key, iSub = -1, iOnce = 0)

    
    def ReleaseEvent(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_SWITCH_PHASE, self.m_Key)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_Key)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_Key)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.m_Key)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_Key)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDBOSSRELIC, self.m_Key)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.m_Key)

    
    def OnStartFight(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType != LEVEL_TYPE_BOSS:
            return None
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.OnCreateMonsterBefore, self.m_Key, iSub = -1, iOnce = 0)

    OnStartFight = CheckFaultTolerance(OnStartFight)
    
    def OnCreateMonsterBefore(self, oWarMgr, dInfo):
        tLineIdx = dInfo['LineIdx']
        if not tLineIdx:
            return None
        oGame = self.m_Game
        iMonsterSID = dInfo['MonsterSID']
        clsMonsterData = oGame.m_WarData.GetMonsterData(iMonsterSID)
        if not clsMonsterData or clsMonsterData.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            return None
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER_BEFORE, self.m_Key)
        iCurLevel = tLineIdx[0]
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iCurLevel)
        iCurLayer = oLevelNode.m_LayerNum
        self.m_CurLayer = iCurLayer
        if iMonsterSID not in self.m_BossLineInfo:
            self.m_BossLineInfo[iMonsterSID] = {
                iCurLayer: iCurLevel }
        else:
            self.m_BossLineInfo[iMonsterSID][iCurLayer] = iCurLevel

    OnCreateMonsterBefore = CheckFaultTolerance(OnCreateMonsterBefore)
    
    def CreatePhaseData(self, iMonsterSID, iCurLayer, iPhase):
        if iMonsterSID not in self.m_Data:
            self.m_Data[iMonsterSID] = {
                iCurLayer: { } }
        elif iCurLayer not in self.m_Data[iMonsterSID]:
            self.m_Data[iMonsterSID][iCurLayer] = { }
        if iPhase not in self.m_Data[iMonsterSID][iCurLayer]:
            dData = {
                'final_result': 0,
                'fight_frame': 0,
                'start_frame': 0,
                'fight_result': 0,
                'death_result': [],
                'skill_times': { },
                'skill_damage': { },
                'skill_kill_times': { } }
            self.m_Data[iMonsterSID][iCurLayer][iPhase] = dData
        return self.m_Data[iMonsterSID][iCurLayer][iPhase]

    CreatePhaseData = CheckFaultToleranceWithDefault(Default = { })(CreatePhaseData)
    
    def GetPhaseData(self, iMonsterSID, iLayer, iPhase):
        if iMonsterSID not in self.m_Data or iLayer not in self.m_Data[iMonsterSID] or iPhase not in self.m_Data[iMonsterSID][iLayer]:
            return { }
        return self.m_Data[iMonsterSID][iLayer][iPhase]

    GetPhaseData = CheckFaultToleranceWithDefault(Default = { })(GetPhaseData)
    
    def OnSwitchPhase(self, oWarMgr, oOwner, dInfo):
        if oOwner.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS or oOwner.m_FightType in BOSS_DONOT_COUNT:
            return None
        iCurLayer = self.m_CurLayer
        self.ExtraInfo(oWarMgr, oOwner, dInfo)
        iOldPhase = dInfo['OldPhase']
        iNewPhase = dInfo['NewPhase']
        if iOldPhase != 0:
            dData = self.GetPhaseData(oOwner.m_SID, iCurLayer, iOldPhase)
            if not dData:
                return None
            if dData['start_frame']:
                dData['fight_frame'] += self.m_Game.GetFrameNum() - dData['start_frame']
                dData['start_frame'] = 0
        self.SetCurBoss(oOwner, iNewPhase)
        dData = self.CreatePhaseData(oOwner.m_SID, iCurLayer, iNewPhase)
        dData['start_frame'] = self.m_Game.GetFrameNum()
        if self.m_LuoHouCom:
            self.m_LuoHouCom.CreatePhaseData(oOwner.m_SID, iCurLayer, iNewPhase)

    OnSwitchPhase = CheckFaultTolerance(OnSwitchPhase)
    
    def ExtraInfo(self, oWarMgr, oOwner, dInfo):
        if oOwner.m_FightType & WARRIOR_BOSSKING == WARRIOR_BOSSKING and oOwner.m_SID not in self.m_Data:
            oDemonKing = CDemonKingInfo(self.m_Game, oOwner)
            self.m_KingCom = oDemonKing
        elif oOwner.m_FightType & WARRIOR_BOSSSTAT == WARRIOR_BOSSSTAT and oOwner.m_SID not in self.m_Data:
            oLuoHou = CLuoHouInfo(self.m_Game, oOwner)
            self.m_LuoHouCom = oLuoHou

    ExtraInfo = CheckFaultTolerance(ExtraInfo)
    
    def OnDie(self, oWarMgr, oOwner, dInfo):
        if oOwner.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            self.OnHeroDie(dInfo)
            return None
        if oOwner.m_FightType in BOSS_DONOT_COUNT:
            return None
        if oOwner.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            iPhase = oOwner.Phase()
            dData = self.GetPhaseData(oOwner.m_SID, self.m_CurLayer, iPhase)
            if not dData:
                return None
            self.SetCurBoss(None, 0)
            if dData['start_frame']:
                dData['fight_frame'] += self.m_Game.GetFrameNum() - dData['start_frame']
                dData['start_frame'] = 0
            for iPhase, dData in self.m_Data[oOwner.m_SID][self.m_CurLayer].items():
                dData['final_result'] = 1
            

    OnDie = CheckFaultTolerance(OnDie)
    
    def OnHeroDie(self, dInfo):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        oLevelNode = oLevelCtrl.m_CurNode
        if oLevelNode.m_LevelType != LEVEL_TYPE_BOSS:
            return None
        iAttacker = dInfo['AID']
        oAttacker = self.m_Game.GetObject(iAttacker)
        if not oAttacker:
            return None
        oBoss = self.m_CurBoss
        if not oBoss:
            return None
        iPhase = oBoss.Phase()
        dData = self.GetPhaseData(oBoss.m_SID, self.m_CurLayer, iPhase)
        if not dData:
            return None
        oPveDieElement = self.m_WarMgr.GetComponent('PVEDieElement')
        if oPveDieElement and oPveDieElement.CheckAllHeroDead():
            dData['fight_result'] = 1
        if oAttacker.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
            if oAttacker.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
                dData['death_result'].append(1)
                if 'Skill' in dInfo and 'pfid' in dInfo['Skill'].m_Base:
                    iPerform = dInfo['Skill'].m_Base['pfid']
                    if iPerform not in dData['skill_kill_times']:
                        dData['skill_kill_times'][iPerform] = 0
                    dData['skill_kill_times'][iPerform] += 1
                    if self.m_LuoHouCom:
                        self.m_LuoHouCom.OnKillHero(oAttacker, self.m_CurLayer, iPerform)
                    else:
                        dData['death_result'].append(2)
            elif oAttacker.m_FightType & WARRIOR_SUMMON == WARRIOR_SUMMON:
                iPerform = oAttacker.m_SrcPerform
                if iPerform not in dData['skill_kill_times']:
                    dData['skill_kill_times'][iPerform] = 0
                dData['skill_kill_times'][iPerform] += 1
                dData['death_result'].append(3)

    OnHeroDie = CheckFaultTolerance(OnHeroDie)
    
    def OnDealDam(self, oWarMgr, oTarget, dInfo):
        if not oTarget:
            return None
        oOwner = oTarget
        iPerform = 0
        if oTarget.m_FightType & WARRIOR_SUMMON == WARRIOR_SUMMON:
            if not (oTarget.m_Owner) or not (oTarget.m_SrcPerform):
                return None
            oOwner = self.m_Game.GetObject(oTarget.m_Owner)
            iPerform = oTarget.m_SrcPerform
        elif oOwner.m_FightType in BOSS_DONOT_COUNT:
            oOwner = self.m_CurBoss
        if not oOwner:
            return None
        if oOwner.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            return None
        if not iPerform and 'Skill' in dInfo and 'pfid' in dInfo['Skill'].m_Base:
            iPerform = dInfo['Skill'].m_Base['pfid']
        if not iPerform:
            return None
        iVictim = dInfo['CurVID']
        oVictim = self.m_Game.GetObject(iVictim)
        if oVictim.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        iPhase = oOwner.Phase()
        dData = self.GetPhaseData(oOwner.m_SID, self.m_CurLayer, iPhase)
        if not dData:
            return None
        iTotalDam = sum(dInfo['TotalDam'])
        if iPerform not in dData['skill_damage']:
            dData['skill_damage'][iPerform] = 0
        dData['skill_damage'][iPerform] += iTotalDam
        if self.m_LuoHouCom:
            self.m_LuoHouCom.OnDealDam(oTarget, iPerform, self.m_CurLayer, iTotalDam)

    OnDealDam = CheckFaultTolerance(OnDealDam)
    
    def OnSkillStart(self, oWarMgr, oTarget, dInfo):
        oOwner = oTarget
        iPerform = 0
        if oTarget.m_FightType & WARRIOR_SUMMON == WARRIOR_SUMMON:
            if not (oTarget.m_Owner) or not (oTarget.m_SrcPerform):
                return None
            oOwner = self.m_Game.GetObject(oTarget.m_Owner)
            iPerform = oTarget.m_SrcPerform
        elif oOwner.m_FightType in BOSS_DONOT_COUNT:
            oOwner = self.m_CurBoss
        if not oOwner:
            return None
        if oOwner.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            return None
        if not iPerform and 'Skill' in dInfo and 'pfid' in dInfo['Skill'].m_Base:
            iPerform = dInfo['Skill'].m_Base['pfid']
        if not iPerform:
            return None
        iPhase = oOwner.Phase()
        dData = self.GetPhaseData(oOwner.m_SID, self.m_CurLayer, iPhase)
        if not dData:
            return None
        iPerform = dInfo['Skill'].m_Base['pfid']
        if iPerform not in dData['skill_times']:
            dData['skill_times'][iPerform] = 0
        dData['skill_times'][iPerform] += 1
        if self.m_LuoHouCom:
            self.m_LuoHouCom.OnSkillStart(oOwner, self.m_CurLayer, iPerform)

    OnSkillStart = CheckFaultTolerance(OnSkillStart)
    
    def OnAddBossRelic(self, oWarMgr, dInfo):
        iCurLayer = dInfo['CurLayer']
        iBossSID = dInfo['BossSID']
        iBossRelic = dInfo['iPerform']
        if iBossSID not in self.m_BossRelicData:
            self.m_BossRelicData[iBossSID] = {
                iCurLayer: iBossRelic }
        else:
            self.m_BossRelicData[iBossSID][iCurLayer] = iBossRelic

    OnAddBossRelic = CheckFaultTolerance(OnAddBossRelic)
    
    def Save(self):
        dData = {
            'BA': self.m_Data,
            'BLI': self.m_BossLineInfo,
            'BRD': self.m_BossRelicData }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData.get('BA', { })
            self.m_BossLineInfo = dData.get('BLI', { })
            self.m_BossRelicData = dData.get('BRD', { })



class CMonsterAnalyseCom(CBaseAnalyseCom):
    m_SummaryList = [
        'LiveFrame',
        'KillFrame',
        'HitPlayerTimes',
        'FightTime',
        'MonsterKillHero',
        'MonsterDamage']
    
    def __init__(self, oGame):
        super(CMonsterAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_BigData = {
            MONSTER_SITUATION_ALIVE: { },
            MONSTER_SITUATION_DIE: { } }
        self.m_LevelBigData = { }
        self.m_PhaseBigData = {
            MONSTER_SITUATION_ALIVE: { },
            MONSTER_SITUATION_DIE: { } }
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            self.PreStatistics(pid)
            return self.m_BigData
        return { }

    
    def GetLevelStatistics(self, pid, iLevel):
        if IsValidStats(self.m_WarMgr, pid):
            self.PreStatistics(pid)
            return self.m_LevelBigData.get(iLevel, { })
        return { }

    
    def GetPhaseStatistics(self, pid, iPhase):
        if IsValidStats(self.m_WarMgr, pid):
            self.PrePhaseStatistics(pid, iPhase)
            return self.m_PhaseBigData
        return { }

    
    def PreStatistics(self, pid):
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            self.CalAllFightTime(oHero.m_Scene)
        self.ClassifyStatistics()

    
    def PrePhaseStatistics(self, pid, iPhase):
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            self.CalAllFightTime(oHero.m_Scene)
        self.ClassifyPhaseStatistics(iPhase)

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, 'BigDataAnalyse_LevelGoal', -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, 'BigDataAnalyse_LevelStart', -1, 0)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, 'BigDataAnalyse_Monster')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, self.OnReceiveDam, 'BigDataAnalyse_Monster')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAMED, self.OnReceiveDamed, 'BigDataAnalyse_Monster')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, 'BigDataAnalyse_Monster')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDamage, 'BigDataAnalyse_Monster')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, self.OnStartHate, 'BigDataAnalyse_Monster')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, self.OnEndHate, 'BigDataAnalyse_Monster')

    
    def ReleaseEvent(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'BigDataAnalyse_LevelGoal')
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, 'BigDataAnalyse_LevelStart')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, 'BigDataAnalyse_Monster')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, 'BigDataAnalyse_Monster')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAMED, 'BigDataAnalyse_Monster')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, 'BigDataAnalyse_Monster')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DEALTOTALDAM, 'BigDataAnalyse_Monster')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_START_HATE, 'BigDataAnalyse_Monster')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_MONSTER_END_HATE, 'BigDataAnalyse_Monster')

    
    def InitMonsterData(self, oMonster):
        dData = {
            'SID': oMonster.m_SID,
            'Level': self.GetMonsterLevel(oMonster),
            'Phase': self.GetMonsterPhase(),
            'IsDie': 0,
            'LiveFrame': 0,
            'KillFrame': 0,
            'HitPlayerTimes': 0,
            'FightTime': 0,
            'MonsterKillHero': 0,
            'MonsterDamage': 0 }
        self.m_Data[oMonster.m_ID] = dData

    
    def GetMonsterBigData(self):
        dData = {
            'TurnTimes': 0,
            'LiveFrame': 0,
            'KillFrame': 0,
            'HitPlayerTimes': 0,
            'FightTime': 0,
            'MonsterKillHero': 0,
            'MonsterDamage': 0 }
        return dData

    
    def GetMonsterLevel(self, oMonster):
        iLevel = 0
        if oMonster.m_LineIdx:
            iLevel = oMonster.m_LineIdx[0]
        if not iLevel:
            oScene = oMonster.m_Game.m_SceneMgr.GetScene(oMonster.m_Scene)
            if oScene:
                iLevel = oScene.m_Level
        if not iLevel:
            SendAlert('err', 'get monster level fail %d %d' % (oMonster.m_SID, iLevel))
        return iLevel

    
    def GetMonsterPhase(self):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
        if oSurvivorElement:
            return oSurvivorElement.m_Phase
        return 0

    
    def OnEnterScene(self, oWarMgr, oOwner, dInfo):
        if oOwner.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        iMonster = oOwner.m_ID
        dData = self.m_Data
        if iMonster not in dData:
            self.InitMonsterData(oOwner)
        iNowFrame = self.m_Game.GetFrameNum()
        oOwner.Set('BornFrame', iNowFrame)

    
    def OnReceiveDam(self, oWarMgr, oOwner, dInfo):
        if not oOwner or oOwner.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        if self.CheckIgnore(oOwner, dInfo):
            return None
        iVictim = dInfo['CurVID']
        oVictim = self.m_Game.GetObject(iVictim)
        if oVictim.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        iMonster = oOwner.m_ID
        dData = self.m_Data
        if iMonster not in dData:
            return None
        dData[iMonster]['HitPlayerTimes'] += 1

    
    def CheckIgnore(self, oOwner, dInfo):
        if 'RS' in dInfo and dInfo['RS'].Query('SourceState') == STATE_ABNORMAL_FIRE:
            return True
        return False

    
    def OnReceiveDamed(self, oWarMgr, oOwner, dInfo):
        if oOwner.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        if oOwner.Query('FirstAttackedFrame'):
            return None
        iNowFrame = self.m_Game.GetFrameNum()
        oOwner.Set('FirstAttackedFrame', iNowFrame)

    
    def OnDie(self, oWarMgr, oOwner, dInfo):
        if oOwner.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            self.OnHeroDie(dInfo)
            return None
        if oOwner.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        iMonster = oOwner.m_ID
        dData = self.m_Data
        if iMonster not in dData:
            return None
        self.CalFightTime(oOwner)
        iNowFrame = self.m_Game.GetFrameNum()
        iBornFrame = oOwner.Query('BornFrame')
        dData[iMonster]['IsDie'] = 1
        if iBornFrame:
            dData[iMonster]['LiveFrame'] += iNowFrame - iBornFrame
        iFirstAttackFrame = oOwner.Query('FirstAttackedFrame')
        if iFirstAttackFrame:
            dData[iMonster]['KillFrame'] += max(iNowFrame - iFirstAttackFrame, 1)

    
    def OnHeroDie(self, dInfo):
        iAttack = dInfo['AID']
        oAttack = self.m_Game.GetObject(iAttack)
        if not oAttack:
            return None
        if oAttack.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        iMonster = oAttack.m_ID
        dData = self.m_Data
        if iMonster not in dData:
            return None
        dData[iMonster]['MonsterKillHero'] += 1

    
    def OnDamage(self, oWarMgr, oOwner, dInfo):
        if not oOwner or oOwner.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        iMonster = oOwner.m_ID
        dData = self.m_Data
        if iMonster not in dData:
            return None
        iVictim = dInfo['CurVID']
        oVictim = self.m_Game.GetObject(iVictim)
        if oVictim.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        dData[iMonster]['MonsterDamage'] += sum(dInfo['TotalDam'])

    
    def OnStartHate(self, oWarMgr, oOwner, dInfo):
        if not oOwner or oOwner.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        oOwner.Set('StartFightFrame', self.m_Game.GetFrameNum())

    
    def OnEndHate(self, oWarMgr, oOwner, dInfo):
        if not oOwner or oOwner.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        iMonster = oOwner.m_ID
        if iMonster not in self.m_Data:
            return None
        self.CalFightTime(oOwner)

    
    def CalFightTime(self, oMonster):
        iStartFightFrame = oMonster.Query('StartFightFrame')
        if iStartFightFrame > 0:
            iNowFrame = self.m_Game.GetFrameNum()
            iMonster = oMonster.m_ID
            if iMonster not in self.m_Data:
                return None
            self.m_Data[iMonster]['FightTime'] += Frame2Time(iNowFrame - iStartFightFrame)
            oMonster.Set('StartFightFrame', iNowFrame)

    
    def CalAllFightTime(self, iScene):
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        for iMonsterId in oScene.GetObjectsByType('Monster'):
            oWarrior = self.m_Game.GetObject(iMonsterId)
            if not oWarrior:
                continue
            self.CalFightTime(oWarrior)
        

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        if dInfo['LevelType'] not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS):
            return None
        self.ClassifyStatistics()

    
    def OnLevelStart(self, oWarMgr, dInfo):
        if dInfo['LevelType'] not in (LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS):
            return None
        self.m_LevelBigData = { }

    
    def ClassifyStatistics(self):
        for dData in self.m_Data.values():
            if dData['IsDie']:
                iType = MONSTER_SITUATION_DIE
            else:
                iType = MONSTER_SITUATION_ALIVE
            iSID = dData['SID']
            if iSID not in self.m_BigData[iType]:
                self.m_BigData[iType][iSID] = self.GetMonsterBigData()
            dBigData = self.m_BigData[iType][iSID]
            dBigData['TurnTimes'] += 1
            for _, sKey in enumerate(self.m_SummaryList):
                dBigData[sKey] += dData[sKey]
            
            iLevel = dData['Level']
            if iLevel not in self.m_LevelBigData:
                self.m_LevelBigData[iLevel] = {
                    MONSTER_SITUATION_ALIVE: { },
                    MONSTER_SITUATION_DIE: { } }
            if iSID not in self.m_LevelBigData[iLevel][iType]:
                self.m_LevelBigData[iLevel][iType][iSID] = self.GetMonsterBigData()
            dLevelBigData = self.m_LevelBigData[iLevel][iType][iSID]
            dLevelBigData['TurnTimes'] += 1
            for _, sKey in enumerate(self.m_SummaryList):
                dLevelBigData[sKey] += dData[sKey]
            
        
        self.m_Data = { }

    
    def ClassifyPhaseStatistics(self, iPhase):
        self.m_PhaseBigData = {
            MONSTER_SITUATION_ALIVE: { },
            MONSTER_SITUATION_DIE: { } }
        for dData in self.m_Data.values():
            iMonsterPhase = dData['Phase']
            if iMonsterPhase > iPhase:
                continue
            if dData['IsDie']:
                iType = MONSTER_SITUATION_DIE
            else:
                iType = MONSTER_SITUATION_ALIVE
            iSID = dData['SID']
            if iSID not in self.m_PhaseBigData[iType]:
                self.m_PhaseBigData[iType][iSID] = self.GetMonsterBigData()
            dPhaseBigData = self.m_PhaseBigData[iType][iSID]
            dPhaseBigData['TurnTimes'] += 1
            for _, sKey in enumerate(self.m_SummaryList):
                dPhaseBigData[sKey] += dData[sKey]
            
        

    
    def Save(self):
        return self.m_BigData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_BigData = dData

    
    def CanLoad(self):
        for value in self.m_BigData.values():
            if value:
                return False
        
        return True



class CPerformAnalyseCom(CBaseAnalyseCom):
    m_SingleHitPerform = (1315,)
    
    def __init__(self, oGame):
        super(CPerformAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_SingleHit = { }
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            return self.m_Data
        return { }

    
    def InitEvent(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnPerformStart, 'BigDataAnalyse_Perform')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, self.OnPerformStart, 'BigDataAnalyse_Perform')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM, self.OnAttack, 'BigDataAnalyse_Perform')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, 'BigDataAnalyse_Perform')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_END, self.OnPerformEnd, 'BigDataAnalyse_Perform')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_HALT, self.OnPerformEnd, 'BigDataAnalyse_Perform')

    
    def ReleaseEvent(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, 'BigDataAnalyse_Perform')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, 'BigDataAnalyse_Perform')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM, 'BigDataAnalyse_Perform')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ATTACK, 'BigDataAnalyse_Perform')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_END, 'BigDataAnalyse_Perform')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_HALT, 'BigDataAnalyse_Perform')

    
    def GetInitData(self):
        dData = {
            'UseTimes': 0,
            'HitTimes': 0 }
        return dData

    
    def OnPerformStart(self, oWarMgr, oOwner, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if clsPerform.m_PFType not in (PF_TYPE_THROW, PF_TYPE_CAREERPF, PF_TYPE_MONSTERACT):
            return None
        dData = self.m_Data
        if iPerform not in dData:
            dData[iPerform] = self.GetInitData()
        dData[iPerform]['UseTimes'] += 1

    
    def OnAttack(self, oWarMgr, oOwner, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        dData = self.m_Data
        if iPerform not in dData:
            return None
        if iPerform in CPerformAnalyseCom.m_SingleHitPerform:
            if iPerform not in self.m_SingleHit:
                self.m_SingleHit[iPerform] = { }
            iActNum = oSkill.m_Base['ActNum']
            if iActNum not in self.m_SingleHit[iPerform]:
                dData[iPerform]['HitTimes'] += 1
                self.m_SingleHit[iPerform][iActNum] = 1
            else:
                dData[iPerform]['HitTimes'] += 1

    
    def OnPerformEnd(self, oWarMgr, oOwner, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid'] if 'pfid' in oSkill.m_Base else 0
        if iPerform not in self.m_SingleHit:
            return None
        iActNum = oSkill.m_Base['ActNum']
        self.m_SingleHit[iPerform].pop(iActNum, 0)

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData



class CHideLevelAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CHideLevelAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_CurLevel = 0
        self.m_CustomData = { }
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, 'BigDataAnalyse_HideLevelEnter')

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, 'BigDataAnalyse_HideLevelEnter')
        for oInfo in self.m_CustomData.values():
            if oInfo.m_Released:
                continue
            oInfo.Release()
        
        self.m_CustomData = { }
        self.m_Game = None
        self.m_WarMgr = None

    
    def GetStatistics(self, pid):
        if pid not in self.m_Data:
            return { }
        return self.m_Data[pid]

    
    def OnEnterScene(self, oWarMgr, oOwner, dInfo):
        if not oOwner or oOwner.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        iLevel = self.GetEnterHideLevel(oOwner.m_Scene)
        if not iLevel:
            return None
        self.m_CurLevel = iLevel
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        iHideType = oLevelCtrl.m_HideLevelLib[iLevel]
        self.EnterDetailLevel(iHideType, iLevel, oOwner.m_PlayerID)

    
    def EnterDetailLevel(self, iHideType, iLevel, pid):
        if iHideType == HIDELV_TYPE_CASH:
            oQianLongInfo = self.m_CustomData.get(HIDELV_TYPE_CASH, None)
            if not oQianLongInfo or oQianLongInfo.m_CurLevel != iLevel:
                self.m_CustomData[HIDELV_TYPE_CASH] = CHideQianLongInfo(self.m_Game, self, iLevel, iHideType, QIANLONG_TYPE_CASH)
                oQianLongInfo = self.m_CustomData[HIDELV_TYPE_CASH]
            if oQianLongInfo.m_LevelEnd:
                return None
            if not oQianLongInfo.QueryData(pid, 'participation'):
                oQianLongInfo.SetData(pid, 'participation', 1)

    
    def GetEnterHideLevel(self, iScene):
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return 0
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        iLevel = oLevelCtrl.GetConfigLevel(oScene.m_Level)
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode and oLevelNode.m_LevelType == LEVEL_TYPE_HIDE:
            return iLevel
        return 0

    
    def SetData(self, pid, iTpye, dInfo):
        if pid not in self.m_Data:
            self.m_Data[pid] = { }
        self.m_Data[pid][iTpye] = dInfo

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData



class CQianLongInfo(object):
    
    def __init__(self, oGame, oAnalyseCom, iLevel, iType, iQianlongType):
        self.m_Game = oGame
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_AnalyseCom = oAnalyseCom
        self.m_CustomData = { }
        self.m_Attention = []
        self.m_CurLevel = iLevel
        self.m_Type = iType
        self.m_QianLongType = iQianlongType
        self.m_StartFrame = 0
        self.m_LevelEnd = 0
        self.m_Flag = 'QianLongBigData'
        self.m_Released = 0
        self.InitData()
        self.InitEvent()

    
    def Release(self):
        self.m_Released = 1
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None
        self.m_AnalyseCom = None

    
    def InitData(self):
        self.m_StartFrame = self.m_Game.GetFrameNum()
        for pid in self.m_WarMgr.GetAllPlayer():
            if pid not in self.m_CustomData:
                self.m_CustomData[pid] = { }
            dHero = self.m_CustomData[pid]
            dHero['isKill'] = 0
            dHero['doDamage'] = []
            dHero['passTime'] = '0.00'
            dHero['blood'] = 0
            dHero['fullblood'] = 0
            dHero['participation'] = 0
            dHero['damage'] = 0
            dHero['qianLongType'] = self.m_QianLongType
            dHero['bombDamage'] = 0
            dHero['deathTimes'] = 0
            dHero['avatarTimes'] = 0
            dHero['killAmount'] = 0
            dHero['escapeAmount'] = 0
            dHero['stopTimes'] = 0
            dHero['isWin'] = 0
            dHero['isGet'] = 0
            dHero['durationFirst'] = 0
            dHero['durationSecond'] = 0
        

    
    def InitEvent(self):
        oWarMgr = self.m_WarMgr
        for iHero in oWarMgr.GetRoomHero():
            self.m_Attention.append((iHero, cl_msgcenter.MSG_WAR_DIE))
            self.m_Attention.append((iHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM))
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnHeroDamage, self.m_Flag)
        
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_Flag, iOnce = 0)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnSkillStart, self.m_Flag)

    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        for tAttention in self.m_Attention:
            (iTarget, iMsg) = tAttention
            cl_msgcenter.DoneAttention(oWarMgr, iTarget, iMsg, self.m_Flag)
        
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_Flag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PERFORM_START, self.m_Flag)

    
    def OnHeroDamage(self, oWarMgr, oOwner, dInfo):
        if not oOwner:
            return None
        iVictim = dInfo['CurVID']
        oVictim = self.m_Game.GetObject(iVictim)
        if not oVictim:
            return None
        if oVictim.m_FightType & MONSTER_CLASSIFY_BOXMONSTER == MONSTER_CLASSIFY_BOXMONSTER and oOwner.m_FightType & WARRIOR_HERO:
            pid = oOwner.m_PlayerID
            if pid not in self.m_CustomData:
                return None
            lstHero = self.m_CustomData[pid].get('doDamage', [])
            if pid not in lstHero:
                lstHero.append(pid)
                self.SetCommonData('doDamage', lstHero)
            iDamgae = self.QueryData(pid, 'damage')
            self.SetData(pid, 'damage', iDamgae + sum(dInfo['TotalDam']))
            if not self.QueryData(pid, 'durationFirst'):
                self.SetData(pid, 'durationFirst', self.m_Game.GetFrameNum() - self.m_StartFrame)

    
    def OnHeroDie(self, oWarMgr, oOwner, dInfo):
        if not oOwner:
            return None
        if oOwner.m_FightType & WARRIOR_HERO:
            pid = oOwner.m_PlayerID
            iDeadTimes = self.QueryData(pid, 'deathTimes')
            self.SetData(pid, 'deathTimes', iDeadTimes + 1)
        elif oOwner.m_FightType & MONSTER_CLASSIFY_BOXMONSTER == MONSTER_CLASSIFY_BOXMONSTER:
            oHero = self.m_Game.GetObject(dInfo['AID'])
            if not oHero:
                return None
            pid = oHero.m_PlayerID
            iKillAmount = self.QueryData(pid, 'killAmount')
            self.SetData(pid, 'killAmount', iKillAmount + 1)

    
    def OnCreateMonster(self, oWarMgr, dInfo):
        iMonster = dInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            return None
        if oMonster.m_FightType & MONSTER_CLASSIFY_BOXMONSTER == MONSTER_CLASSIFY_BOXMONSTER:
            self.m_Attention.append((iMonster, cl_msgcenter.MSG_WAR_DIE))
            cl_msgcenter.AddAttentionFunc(oWarMgr, iMonster, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, self.m_Flag)

    
    def OnMonsterDie(self, oWarMgr, oOwner, dInfo):
        if not oOwner:
            return None
        if oOwner.m_FightType & MONSTER_CLASSIFY_BOXMONSTER == MONSTER_CLASSIFY_BOXMONSTER:
            oHero = self.m_Game.GetObject(dInfo['AID'])
            if not oHero:
                return None
            pid = oHero.m_PlayerID
            iKillAmount = self.QueryData(pid, 'killAmount')
            self.SetData(pid, 'killAmount', iKillAmount + 1)

    
    def OnSkillStart(self, oWarMgr, oOwner, dInfo):
        if 'Skill' in dInfo and 'pfid' in dInfo['Skill'].m_Base:
            oSkill = dInfo['Skill']
            iPerform = oSkill.m_Base['pfid']
            if iPerform == MONSTER_QIANLONG_LOCK or 'TriggerPid' in oSkill.m_Custom:
                pid = oSkill.m_Custom['TriggerPid']
                iStopTimes = self.QueryData(pid, 'stopTimes')
                self.SetData(pid, 'stopTimes', iStopTimes + 1)
            elif iPerform == MONSTER_QIANLONG_SUMMON:
                self.AddCommonData('avatarTimes', 1)
            elif iPerform == MONSTER_QIANLONG_ESCAPE:
                self.AddCommonData('escapeAmount', 1)

    
    def SetData(self, pid, key, iValue):
        if pid not in self.m_CustomData:
            return None
        self.m_CustomData[pid][key] = iValue

    
    def SetCommonData(self, key, iValue):
        for dHero in self.m_CustomData.values():
            if key not in dHero:
                continue
            dHero[key] = iValue
        

    
    def AddCommonData(self, key, iValue):
        for dHero in self.m_CustomData.values():
            if key not in dHero:
                continue
            dHero[key] += iValue
        

    
    def QueryData(self, pid, key):
        if pid not in self.m_CustomData:
            return 0
        return self.m_CustomData[pid].get(key, 0)

    
    def GetStatistics(self, pid):
        if pid not in self.m_CustomData:
            return { }
        return self.m_CustomData[pid]



class CHideQianLongInfo(CQianLongInfo):
    
    def InitEvent(self):
        super().InitEvent()
        oWarMgr = self.m_WarMgr
        for iHero in oWarMgr.GetRoomHero():
            self.m_Attention.append((iHero, cl_msgcenter.MSG_WAR_REVTOTALDAM))
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_REVTOTALDAM, self.OnReceivedDamage, self.m_Flag)
        
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, self.m_Flag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGESTART, self.OnChallengeStart, self.m_Flag)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.OnChallengeEnd, self.m_Flag)

    
    def ReleaseEvent(self):
        super().ReleaseEvent()
        oWarMgr = self.m_WarMgr
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGESTART, self.m_Flag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.m_Flag)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_ENTERSCENE, self.m_Flag)

    
    def OnEnterScene(self, oWarMgr, oOwner, dInfo):
        if not oOwner or oOwner.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        iOldLevel = self.m_AnalyseCom.GetEnterHideLevel(dInfo['OldScene'])
        if iOldLevel == self.m_CurLevel:
            self.SetData(oOwner.m_PlayerID, 'participation', 2)

    
    def OnChallengeStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_StartFrame = self.m_Game.GetFrameNum()

    
    def OnChallengeEnd(self, oWarMgr, oLevelCtrl, dInfo):
        iBlood = 0
        iFullBlood = 0
        dOther = dInfo.get('OtherInfo', { })
        if 'targetHP' in dOther:
            iBlood = dOther['targetHP']
        if 'targetHPMax' in dOther:
            iFullBlood = dOther['targetHPMax']
        iResult = 1 if not iBlood else 0
        self.SetCommonData('isKill', iResult)
        self.SetCommonData('blood', iBlood)
        self.SetCommonData('fullblood', iFullBlood)
        self.SetCommonData('isWin', iResult)
        self.SetCommonData('isGet', iResult)
        for pid in self.m_WarMgr.GetAllPlayer():
            iFirstFrame = self.QueryData(pid, 'durationFirst')
            if iFirstFrame:
                sFirst = '%.1f' % iFirstFrame / GAME_FRAME
                sSeconde = '%.1f' % (self.m_Game.GetFrameNum() - self.m_StartFrame - iFirstFrame) / GAME_FRAME
                self.SetData(pid, 'durationFirst', sFirst)
                self.SetData(pid, 'durationSecond', sSeconde)
                continue
            sFirst = '%.1f' % (self.m_Game.GetFrameNum() - self.m_StartFrame) / GAME_FRAME
            self.SetData(pid, 'durationFirst', sFirst)
        
        self.End()

    
    def End(self):
        self.m_LevelEnd = 1
        for pid, dHero in self.m_CustomData.items():
            self.m_AnalyseCom.SetData(pid, self.m_Type, dHero)
        
        self.Release()

    
    def OnReceivedDamage(self, oWarMgr, oOwner, dInfo):
        if not oOwner:
            return None
        iAttacker = dInfo['AID']
        oAttacker = oOwner.m_Game.GetObject(iAttacker)
        if not oAttacker:
            return None
        if oAttacker.m_FightType & MONSTER_CLASSIFY_BOXMONSTER == MONSTER_CLASSIFY_BOXMONSTER and oOwner.m_FightType & WARRIOR_HERO:
            pid = oOwner.m_PlayerID
            iDamgae = self.QueryData(pid, 'bombDamage')
            self.SetData(pid, 'bombDamage', iDamgae + sum(dInfo['TotalDam']))



class CPhaseQianLongInfo(CQianLongInfo):
    
    def InitEvent(self):
        super().InitEvent()
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.OnChallengeOver, 'QianLong_ChallengeOver', iSub = PHASE_CHALLENGE_OVER)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.OnPlayerLeave, 'QianLong_PlayerLeave', iSub = PHASE_CHALLENGE_PLAYERLEAVE)

    
    def ReleaseEvent(self):
        super().ReleaseEvent()
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, 'QianLong_ChallengeOver', iSub = PHASE_CHALLENGE_OVER)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, 'QianLong_PlayerLeave', iSub = PHASE_CHALLENGE_PLAYERLEAVE)

    
    def OnChallengeOver(self, oWarMgr, oTarget, dInfo):
        iBlood = 0
        iFullBlood = 0
        dOther = dInfo.get('OtherInfo', { })
        if 'targetHP' in dOther:
            iBlood = dOther['targetHP']
        if 'targetHPMax' in dOther:
            iFullBlood = dOther['targetHPMax']
        self.SetCommonData('blood', iBlood)
        self.SetCommonData('fullblood', iFullBlood)
        self.SetCommonData('isWin', int(dInfo['Rlt']))
        self.SetCommonData('isGet', int(dInfo['Reward']))
        for pid in self.m_WarMgr.GetRoomPlayer():
            iFirstFrame = self.QueryData(pid, 'durationFirst')
            if iFirstFrame:
                sFirst = '%.1f' % iFirstFrame / GAME_FRAME
                sSeconde = '%.1f' % (self.m_Game.GetFrameNum() - self.m_StartFrame - iFirstFrame) / GAME_FRAME
                self.SetData(pid, 'durationFirst', sFirst)
                self.SetData(pid, 'durationSecond', sSeconde)
            else:
                sFirst = '%.1f' % (self.m_Game.GetFrameNum() - self.m_StartFrame) / GAME_FRAME
                self.SetData(pid, 'durationFirst', sFirst)
            self.m_AnalyseCom.SetData(pid, self.m_Type, self.m_CustomData[pid])
        
        self.Release()

    
    def OnPlayerLeave(self, oWarMgr, oTarget, dInfo):
        if 'pid' not in dInfo or not dInfo['pid']:
            return None
        pid = dInfo['pid']
        iBlood = 0
        iFullBlood = 0
        dOther = dInfo.get('OtherInfo', { })
        if 'targetHP' in dOther:
            iBlood = dOther['targetHP']
        if 'targetHPMax' in dOther:
            iFullBlood = dOther['targetHPMax']
        self.SetData(pid, 'blood', iBlood)
        self.SetData(pid, 'fullblood', iFullBlood)
        self.SetData(pid, 'isWin', int(dInfo['Rlt']))
        self.SetData(pid, 'isGet', int(dInfo['Reward']))
        iFirstFrame = self.QueryData(pid, 'durationFirst')
        if iFirstFrame:
            iFirst = round(iFirstFrame / GAME_FRAME, 1)
            iSeconde = round((self.m_Game.GetFrameNum() - self.m_StartFrame - iFirstFrame) / GAME_FRAME, 1)
            self.SetData(pid, 'durationFirst', iFirst)
            self.SetData(pid, 'durationSecond', iSeconde)
        else:
            iFirst = round((self.m_Game.GetFrameNum() - self.m_StartFrame) / GAME_FRAME, 1)
            self.SetData(pid, 'durationFirst', iFirst)
        self.m_AnalyseCom.SetData(pid, self.m_Type, self.m_CustomData[pid])
        if dInfo['Over']:
            self.Release()



class CSearchTreasureInfo(object):
    FAIL_TYPE_TIMEOUT = 1
    FAIL_TYPE_ALLDIE = 2
    FAIL_TYPE_ALLLEAVE = 3
    m_Type = PHASE_CHALLENGE_SEARCHTREASURE
    
    def __init__(self, oGame, oAnalyseCom, iPhase):
        self.m_Game = oGame
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_AnalyseCom = oAnalyseCom
        self.m_Phase = iPhase
        self.m_PhaseDeath = { }
        self.m_Data = { }
        self.m_StartFrame = self.m_Game.GetFrameNum()
        self.m_Released = 0
        self.InitEvent()

    
    def Release(self):
        self.m_Released = 1
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None
        self.m_AnalyseCom = None

    
    def InitEvent(self):
        oWarMgr = self.m_WarMgr
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.OnChallengeOver, 'SearchTreasure_Challenge', iSub = PHASE_CHALLENGE_OVER)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.OnPlayerLeave, 'SearchTreasure_Challenge', iSub = PHASE_CHALLENGE_PLAYERLEAVE)
        self.m_RoomHero = oWarMgr.GetRoomHero()
        for iHero in self.m_RoomHero:
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, 'SearchTreasure_Challenge')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIEDIST, self.OnHeroDieDist, 'SearchTreasure_Challenge')
        

    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, 'SearchTreasure_Challenge', iSub = PHASE_CHALLENGE_OVER)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, 'SearchTreasure_Challenge', iSub = PHASE_CHALLENGE_PLAYERLEAVE)
        for iHero in self.m_RoomHero:
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, 'SearchTreasure_Challenge')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIEDIST, 'SearchTreasure_Challenge')
        

    
    def GetCurPhase(self):
        oSurvivorElement = self.m_WarMgr.GetComponent('SurvivorElement')
        if oSurvivorElement:
            return oSurvivorElement.m_Phase
        return 0

    
    def GetAreaAmount(self):
        oSurvivorElement = self.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return 0
        oPhaseChallengeMgr = oSurvivorElement.m_PhaseChallengeMgr
        if not oPhaseChallengeMgr:
            return 0
        dChallenge = oPhaseChallengeMgr.m_Challenge
        if self.m_Phase in dChallenge:
            return dChallenge[self.m_Phase].m_SearchNum
        return 0

    
    def OnChallengeOver(self, oWarMgr, oTarget, dInfo):
        iType = dInfo['Type']
        if iType != self.m_Type:
            return None
        bRlt = dInfo['Rlt']
        if bRlt:
            self.RecordEnd(True)
        else:
            self.RecordEnd(False, self.FAIL_TYPE_TIMEOUT)

    
    def OnPlayerLeave(self, oWarMgr, oTarget, dInfo):
        iOver = dInfo['Over']
        if iOver:
            self.RecordEnd(False, self.FAIL_TYPE_ALLLEAVE)

    
    def OnHeroDie(self, oWarMgr, oHero, dInfo):
        iPhase = self.GetCurPhase()
        if iPhase in self.m_PhaseDeath:
            self.m_PhaseDeath[iPhase] += 1
        else:
            self.m_PhaseDeath[iPhase] = 1

    
    def OnHeroDieDist(self, oWarMgr, oHero, dInfo):
        oPveDieElement = self.m_WarMgr.GetComponent('PVEDieElement')
        if oPveDieElement and oPveDieElement.CheckAllHeroDead():
            self.RecordEnd(False, self.FAIL_TYPE_ALLDIE)

    
    def RecordEnd(self, bIsWin, iFailType = 0):
        dData = {
            'phase_death': self.m_PhaseDeath,
            'is_win': 1 if bIsWin else 0,
            'area_amount': self.GetAreaAmount(),
            'duration': Frame2Time(self.m_Game.GetFrameNum() - self.m_StartFrame) // 100,
            'fail_type': iFailType }
        self.m_AnalyseCom.SetMasterData(self.m_Type, dData)
        self.Release()



class CDemonKingInfo(object):
    
    def __init__(self, oGame, oOwner):
        self.m_Game = oGame
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_OwnerID = oOwner.m_ID
        self.m_Data = { }
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def InitEvent(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddAttentionFunc(oWarMgr, self.m_OwnerID, cl_msgcenter.MSG_WAR_DIE_BEFORE, self.OnDieBefore, 'DemonKing_DieBefore')

    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneAttention(oWarMgr, self.m_OwnerID, cl_msgcenter.MSG_WAR_DIE_BEFORE, 'DemonKing_DieBefore')

    
    def OnDieBefore(self, oListener, oTarget, dMsgInfo):
        oState = oTarget.m_State.GetItemBySID(STATE_DEMONKING_TIME)
        if not oState:
            return None
        iRemainFrame = oState.GetRemainTime()
        iFrame = oState.GetTime()
        iStateTime = Frame2Time(iFrame - iRemainFrame)
        dData = {
            'state_time': iStateTime }
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iCurLayer = oLevelCtrl.m_LayerNum
        iPhase = oTarget.m_Phase
        iMonster = oTarget.m_SID
        if iMonster not in self.m_Data:
            self.m_Data[iMonster] = {
                iCurLayer: {
                    iPhase: dData } }
        elif iCurLayer not in self.m_Data[iMonster]:
            self.m_Data[iMonster][iCurLayer] = {
                iPhase: dData }

    OnDieBefore = CheckFaultTolerance(OnDieBefore)


class CLuoHouInfo(object):
    
    def __init__(self, oGame, oOwner):
        self.m_Game = oGame
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_OwnerID = oOwner.m_ID
        self.m_OwnerSID = oOwner.m_SID
        self.m_Data = { }

    
    def Release(self):
        self.m_Game = None
        self.m_WarMgr = None

    
    def CreatePhaseData(self, iMonsterSID, iCurLayer, iPhase):
        if iMonsterSID != self.m_OwnerSID:
            return None
        if iCurLayer not in self.m_Data:
            self.m_Data[iCurLayer] = { }
        if iPhase not in self.m_Data[iCurLayer]:
            dData = {
                'cut_skill_times': { },
                'cut_skill_damage': { },
                'cut_skill_kill_times': { } }
            self.m_Data[iCurLayer][iPhase] = dData

    CreatePhaseData = CheckFaultTolerance(CreatePhaseData)
    
    def CheckCut(self, oOwner):
        iScene = oOwner.m_Scene
        oScene = oOwner.m_Game.m_SceneMgr.GetScene(iScene)
        lstObstacle = oScene.GetObjectsByType('Obstacle')
        for iObstacle in lstObstacle:
            oObstacle = oOwner.m_Game.GetObject(iObstacle, PY_FLAG_DEAD)
            if not oObstacle:
                continue
            if oObstacle.m_SID == BUILD_LUOHOU_CUT:
                return True
        
        return False

    
    def OnSkillStart(self, oTarget, iCurLayer, iPerform):
        if oTarget.m_ID != self.m_OwnerID:
            return None
        if not self.CheckCut(oTarget) and iPerform != MONSTER_LUOHOU_CREATECUT:
            return None
        iPhase = oTarget.m_Phase
        if iPerform not in self.m_Data[iCurLayer][iPhase]['cut_skill_times']:
            self.m_Data[iCurLayer][iPhase]['cut_skill_times'][iPerform] = 0
        self.m_Data[iCurLayer][iPhase]['cut_skill_times'][iPerform] += 1

    OnSkillStart = CheckFaultTolerance(OnSkillStart)
    
    def OnKillHero(self, oAttacker, iCurLayer, iPerform):
        if oAttacker.m_ID != self.m_OwnerID:
            return None
        if not self.CheckCut(oAttacker):
            return None
        iPhase = oAttacker.m_Phase
        if iPerform not in self.m_Data[iCurLayer][iPhase]['cut_skill_kill_times']:
            self.m_Data[iCurLayer][iPhase]['cut_skill_kill_times'][iPerform] = 0
        self.m_Data[iCurLayer][iPhase]['cut_skill_kill_times'][iPerform] += 1

    OnKillHero = CheckFaultTolerance(OnKillHero)
    
    def OnDealDam(self, oTarget, iPerform, iCurLayer, iTotalDam):
        if oTarget.m_ID != self.m_OwnerID:
            return None
        if not self.CheckCut(oTarget):
            return None
        iPhase = oTarget.m_Phase
        if iPerform not in self.m_Data[iCurLayer][iPhase]['cut_skill_damage']:
            self.m_Data[iCurLayer][iPhase]['cut_skill_damage'][iPerform] = 0
        self.m_Data[iCurLayer][iPhase]['cut_skill_damage'][iPerform] += iTotalDam

    OnDealDam = CheckFaultTolerance(OnDealDam)


class CGeminiAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_BigData = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, 'Gemini_OnAddAllPlayer', -1, 0)

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        self.InitEvent()

    
    def InitEvent(self):
        lstAllHero = self.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnDie, 'Gemini_OnDie')
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, 'Gemini_OnRelife')
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ENABLE_GEMINI, self.OnGeminiEnable, 'Gemini_OnGeminiEnable')
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_DISABLE_GEMINI, self.OnGeminiDisable, 'Gemini_OnGeminiDisable')
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WEAPONFIRE, self.OnWeaponFire, 'Gemini_OnWeaponFire')
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.OnChangeweapon, 'Gemini_OnChangeweapon')
        

    
    def ReleaseEvent(self):
        lstAllHero = self.m_WarMgr.GetAllHero()
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'Gemini_OnAddAllPlayer')
        for iHero in lstAllHero:
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, 'Gemini_OnDie')
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_RELIFE, 'Gemini_OnRelife')
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ENABLE_GEMINI, 'Gemini_OnGeminiEnable')
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_DISABLE_GEMINI, 'Gemini_OnGeminiDisable')
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WEAPONFIRE, 'Gemini_OnWeaponFire')
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, 'Gemini_OnChangeweapon')
        

    
    def GetStatistics(self, pid):
        self.PreStatistics(pid)
        if pid not in self.m_BigData:
            return { }
        return self.m_BigData[pid]

    
    def PreStatistics(self, pid):
        if pid not in self.m_Data:
            return None
        lstData = []
        iNowFrame = self.m_Game.GetFrameNum()
        iCount = 0
        for oInscriptionData in self.m_Data[pid]:
            if not oInscriptionData.m_Disable:
                oInscriptionData.CalActivateTime(iNowFrame, iNowFrame)
                oInscriptionData.PauseUseFrame(iNowFrame)
                iCount += 1
            if not oInscriptionData.m_Invalid:
                continue
            lstData.append(oInscriptionData.ExportToBigData())
        
        if iCount > 1:
            SendAlert('err', 'geminidata enable > 1')
        self.m_BigData[pid] = lstData

    
    def OnGeminiDisable(self, oWarMgr, oHero, dInfo):
        iInscriptionSID = dInfo['SID']
        oInscriptionData = self.GetCurData(oHero.m_PlayerID)
        if not oInscriptionData:
            return None
        if iInscriptionSID != oInscriptionData.m_InscriptionSID:
            SendAlert('err', f'''geminidata err {iInscriptionSID} {oInscriptionData.m_InscriptionSID}''')
            return None
        iNowFrame = self.m_Game.GetFrameNum()
        oInscriptionData.CalActivateTime(iNowFrame, iNowFrame)
        oInscriptionData.PauseUseFrame(iNowFrame)
        oInscriptionData.m_Disable = True

    
    def OnGeminiEnable(self, oWarMgr, oHero, dInfo):
        iInscriptionSID = dInfo['SID']
        pid = oHero.m_PlayerID
        lstPlayerData = self.m_Data.setdefault(pid, [])
        lstWeapon = oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
        if len(lstWeapon) < 2:
            SendAlert('err', 'weapon no enough')
            return None
        oInscriptionData = CInscriptionData(iInscriptionSID)
        oInscriptionData.SetWeapons(lstWeapon)
        oInscriptionData.Activate(self.m_Game.GetFrameNum())
        lstPlayerData.append(oInscriptionData)

    
    def OnDie(self, oWarMgr, oHero, dInfo):
        oInscriptionData = self.GetCurData(oHero.m_PlayerID)
        if not oInscriptionData:
            return None
        iNowFrame = self.m_Game.GetFrameNum()
        oInscriptionData.CalActivateTime(iNowFrame, -1)
        oInscriptionData.PauseUseFrame(iNowFrame)

    
    def OnRelife(self, oWarMgr, oHero, dInfo):
        oInscriptionData = self.GetCurData(oHero.m_PlayerID)
        if not oInscriptionData:
            return None
        oInscriptionData.Activate(self.m_Game.GetFrameNum())

    
    def OnWeaponFire(self, oWarMgr, oHero, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iWeapon = oSkill.m_Base['Weapon']
        if not iWeapon:
            return None
        oInscriptionData = self.GetCurData(oHero.m_PlayerID)
        if not oInscriptionData or oInscriptionData.m_Disable:
            return None
        iNowFrame = self.m_Game.GetFrameNum()
        oInscriptionData.OnWeaponFire(iWeapon, iNowFrame)

    
    def PlayerPauseUseFrame(self, pid):
        oInscriptionData = self.GetCurData(pid)
        if not oInscriptionData or oInscriptionData.m_Disable:
            return None
        iNowFrame = self.m_Game.GetFrameNum()
        oInscriptionData.PauseUseFrame(iNowFrame)

    
    def OnChangeweapon(self, oWarMgr, oHero, dInfo):
        oInscriptionData = self.GetCurData(oHero.m_PlayerID)
        if not oInscriptionData:
            return None
        iNowFrame = self.m_Game.GetFrameNum()
        oInscriptionData.PauseUseFrame(iNowFrame)

    
    def GetCurData(self, pid):
        if pid not in self.m_Data:
            return None
        lstPlayerData = self.m_Data[pid]
        if not lstPlayerData:
            return None
        return lstPlayerData[-1]

    
    def Save(self):
        dData = { }
        iNowFrame = self.m_Game.GetFrameNum()
        for pid, lstInscriptionData in self.m_Data.items():
            dData[pid] = []
            for oInscriptionData in lstInscriptionData:
                oInscriptionData.CalActivateTime(iNowFrame, iNowFrame)
                oInscriptionData.PauseUseFrame(iNowFrame)
                dData[pid].append(oInscriptionData.Save())
            
        
        return dData

    
    def Load(self, dData):
        iNowFrame = self.m_Game.GetFrameNum()
        for pid, lstInscriptionData in dData.items():
            self.m_Data[pid] = []
            for dInscriptionData in lstInscriptionData:
                oInscriptionData = CInscriptionData(dInscriptionData['InscriptionSID'])
                oInscriptionData.Load(dInscriptionData)
                if not oInscriptionData.m_Disable:
                    oInscriptionData.m_LastActivateFrame = iNowFrame
                self.m_Data[pid].append(oInscriptionData)
            
        



class CRareItemAnalyseCom(CBaseAnalyseCom):
    APPEAR_TYPE_DROP = 1
    APPEAR_TYPE_SHOP = 2
    
    def __init__(self, oGame):
        super(CRareItemAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_CurBoss = None
        self.m_Data = { }
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None
        self.m_CurBoss = None

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            return self.m_Data
        return { }

    
    def InitEvent(self):
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROPRAREITEM, self.OnDropRareItem, 'BigDataAnalyse_RareItem')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PICK, self.OnPick, 'BigDataAnalyse_RareItem')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_USERAREITEM, self.OnUseRareItem, 'BigDataAnalyse_RareItem')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RAREITEMGOODS, self.OnRareItemGoods, 'BigDataAnalyse_RareItem')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REWARDRAREITEM, self.OnRewardRareItem, 'BigDataAnalyse_RareItem')
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEMONSTER, self.OnCreateMonster, 'BigDataAnalyse_RareItem')

    
    def ReleaseEvent(self):
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROPRAREITEM, 'BigDataAnalyse_RareItem')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PICK, 'BigDataAnalyse_RareItem')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_USERAREITEM, 'BigDataAnalyse_RareItem')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_RAREITEMGOODS, 'BigDataAnalyse_RareItem')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REWARDRAREITEM, 'BigDataAnalyse_RareItem')
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEMONSTER, 'BigDataAnalyse_RareItem')

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def GetCurPhaseAndTime(self):
        oSurvivorElement = self.m_WarMgr.GetComponent('SurvivorElement')
        if oSurvivorElement.m_Phase > oSurvivorElement.m_MaxPhase:
            iPhase = 999
            iTime = self.m_CurBoss.m_Phase if self.m_CurBoss else 0
        else:
            iPhase = oSurvivorElement.m_Phase
            iFrame = self.m_Game.GetFrameNum() - oSurvivorElement.m_PhaseStartFrame
            iTime = Frame2Time(iFrame) // 100
        return (iPhase, iTime)

    
    def InitRareItemData(self, iSID, iApperType):
        (iPhase, iTime) = self.GetCurPhaseAndTime()
        return {
            'id': iSID,
            'appear_type': iApperType,
            'appear_phase': iPhase,
            'appear_time': iTime,
            'get_phase': 0,
            'get_time': 0,
            'get_times': 0,
            'use_phase': 0,
            'use_time': 0 }

    
    def OnDropRareItem(self, oWarMgr, oOwner, dInfo):
        lstRareItem = dInfo['lstRareItem']
        for oItem in lstRareItem:
            self.m_Data[oItem.m_ID] = self.InitRareItemData(oItem.m_SID, self.APPEAR_TYPE_DROP)
        

    
    def OnPick(self, oWarMgr, oOwner, dInfo):
        if dInfo['Type'] != NWARRIOR_DROP_RAREITEM:
            return None
        oItem = dInfo['Item']
        if oItem.m_Type != RAREITEM_MASK:
            return None
        self.RecordGetItem(oItem)

    
    def RecordGetItem(self, oItem):
        if oItem.m_ID not in self.m_Data:
            return None
        dItemData = self.m_Data[oItem.m_ID]
        if dItemData['get_times'] <= 0:
            (iPhase, iTime) = self.GetCurPhaseAndTime()
            dItemData['get_phase'] = iPhase
            dItemData['get_time'] = iTime
        dItemData['get_times'] += 1

    
    def OnUseRareItem(self, oWarMgr, oOwner, dInfo):
        oItem = dInfo['Item']
        if oItem.m_ID not in self.m_Data:
            return None
        dItemData = self.m_Data[oItem.m_ID]
        (iPhase, iTime) = self.GetCurPhaseAndTime()
        dItemData['use_phase'] = iPhase
        dItemData['use_time'] = iTime

    
    def OnRareItemGoods(self, oWarMgr, oOwner, dInfo):
        oItem = dInfo['Item']
        self.m_Data[oItem.m_ID] = self.InitRareItemData(oItem.m_SID, self.APPEAR_TYPE_SHOP)

    
    def OnRewardRareItem(self, oWarMgr, oOwner, dInfo):
        self.RecordGetItem(dInfo['Item'])

    
    def OnCreateMonster(self, oWarMgr, oOwner, dInfo):
        if oOwner.m_FightType & WARRIOR_BOSSSTAT == WARRIOR_BOSSSTAT:
            self.m_CurBoss = oOwner



class CInscriptionData(object):
    m_SingleUseMax = 4 * GAME_FRAME
    
    def __init__(self, iInscriptionSID):
        self.m_InscriptionSID = iInscriptionSID
        self.m_Weapons = []
        self.m_LastActivateFrame = -1
        self.m_ActivateTime = 0
        self.m_Disable = False
        self.m_Invalid = False

    
    def Activate(self, iNowFrame):
        self.m_LastActivateFrame = iNowFrame

    
    def SetWeapons(self, lstWeapon):
        lstWeaponData = []
        for oWeapon in lstWeapon:
            lstWeaponData.append({
                'SID': oWeapon.m_SID,
                'ID': oWeapon.m_ID,
                'UseFrame': 0,
                'LastUseFrame': 0 })
        
        self.m_Weapons = lstWeaponData

    
    def GetWeaponData(self, iWeaponID):
        for dWeapon in self.m_Weapons:
            if iWeaponID == dWeapon['ID']:
                return dWeapon
        

    
    def CalActivateTime(self, iNowFrame, iLastActivateFrame):
        if self.m_Disable:
            return None
        if self.m_LastActivateFrame >= 0:
            iFrame = iNowFrame - self.m_LastActivateFrame
            self.m_ActivateTime += Frame2Time(iFrame)
            self.m_LastActivateFrame = iLastActivateFrame
            if self.m_ActivateTime >= ACTIVATE_LEAST_TIME:
                self.m_Invalid = True

    
    def OnWeaponFire(self, iWeapon, iNowFrame):
        dWeaponData = self.GetWeaponData(iWeapon)
        if not dWeaponData:
            return None
        self.CalUseFrame(dWeaponData, iNowFrame)
        dWeaponData['LastUseFrame'] = iNowFrame

    
    def PauseUseFrame(self, iNowFrame):
        for dWeaponData in self.m_Weapons:
            self.CalUseFrame(dWeaponData, iNowFrame)
            dWeaponData['LastUseFrame'] = 0
        

    
    def CalUseFrame(self, dWeaponData, iNowFrame):
        iLastUseFrame = dWeaponData['LastUseFrame']
        if iLastUseFrame:
            dWeaponData['UseFrame'] += min(iNowFrame - iLastUseFrame, CInscriptionData.m_SingleUseMax)

    
    def ExportToBigData(self):
        lstWeapon = []
        for dWeapon in self.m_Weapons:
            lstWeapon.append({
                'SID': dWeapon['SID'],
                'UseTime': Frame2Time(dWeapon['UseFrame']) })
        
        dData = {
            'InscriptionSID': self.m_InscriptionSID,
            'Weapons': lstWeapon,
            'ActivateTime': self.m_ActivateTime }
        return dData

    
    def Save(self):
        dData = {
            'InscriptionSID': self.m_InscriptionSID,
            'Weapons': self.m_Weapons,
            'ActivateTime': self.m_ActivateTime,
            'Disable': self.m_Disable,
            'Invalid': self.m_Invalid }
        return dData

    
    def Load(self, dData):
        self.TempAdjust(dData)
        self.m_Weapons = dData['Weapons']
        self.m_ActivateTime = dData['ActivateTime']
        self.m_Disable = dData['Disable']
        self.m_Invalid = dData['Invalid']

    
    def TempAdjust(self, dData):
        lstWeapon = dData['Weapons']
        bAdjust = False
        for dWeapon in lstWeapon:
            if 'ID' not in dWeapon:
                ErrLog.Alert('gemini param err %s' % dWeapon)
                bAdjust = True
        
        if bAdjust:
            lstNewWeapon = []
            for dWeapon in lstWeapon:
                lstNewWeapon.append({
                    'SID': dWeapon['SID'],
                    'ID': 0,
                    'UseFrame': 0,
                    'LastUseFrame': 0 })
            
            dData['Weapons'] = lstNewWeapon



class CPhaseClgAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CPhaseClgAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_CustomData = { }
        self.m_MasterData = { }
        self.InitEvent()

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, self.OnTriggerChallengeEvent, 'PhaseClg_Start', iSub = PHASE_CHALLENGE_START, iOnce = 0)

    
    def Release(self):
        self.ReleaseEvent()
        for oInfo in self.m_CustomData.values():
            if oInfo.m_Released:
                continue
            oInfo.Release()
        
        self.m_CustomData = { }
        self.m_Game = None
        self.m_WarMgr = None

    
    def ReleaseEvent(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMSG_PHASECHALLENGE, 'PhaseClg_Start', iSub = PHASE_CHALLENGE_START)

    
    def OnTriggerChallengeEvent(self, oWarMgr, dInfo):
        iType = dInfo['Type']
        if iType in (PHASE_CHALLENGE_BOXMONSTER, PHASE_CHALLENGE_KILLBOXMONSTER):
            if iType not in self.m_CustomData:
                iLevel = dInfo['Level']
                iQianlongType = 0
                if iType == PHASE_CHALLENGE_BOXMONSTER:
                    iQianlongType = QIANLONG_TYPE_BOXMONSTER
                elif iType == PHASE_CHALLENGE_KILLBOXMONSTER:
                    iQianlongType = QIANLONG_TYPE_KILLBOXMONSTER
                if not iQianlongType:
                    return None
                self.m_CustomData[iType] = CPhaseQianLongInfo(self.m_Game, self, iLevel, iType, iQianlongType)
            oQianLongInfo = self.m_CustomData[iType]
            if oQianLongInfo.m_LevelEnd:
                return None
            oQianLongInfo.SetCommonData('participation', 1)
        elif iType == PHASE_CHALLENGE_SEARCHTREASURE and iType not in self.m_CustomData:
            iPhase = dInfo['Phase']
            self.m_CustomData[iType] = CSearchTreasureInfo(self.m_Game, self, iPhase)

    
    def GetStatistics(self, pid):
        dData = { }
        if IsValidStats(self.m_WarMgr, pid):
            dData.update(self.m_MasterData)
        if pid in self.m_Data:
            dData.update(self.m_Data[pid])
        return dData

    
    def SetData(self, pid, iTpye, dInfo):
        if pid not in self.m_Data:
            self.m_Data[pid] = { }
        self.m_Data[pid][iTpye] = dInfo

    
    def SetMasterData(self, iType, dInfo):
        self.m_MasterData[iType] = dInfo

    
    def CanLoad(self):
        if self.m_Data:
            return False
        if self.m_MasterData:
            return False
        return True

    
    def Save(self):
        return {
            'Data': self.m_Data,
            'MData': self.m_MasterData }

    
    def Load(self, dData):
        if self.CanLoad():
            if 'Data' in dData:
                self.m_Data = dData['Data']
            if 'MData' in dData:
                self.m_MasterData = dData['MData']



class CMonsterRelicAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CMonsterRelicAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_MonsterRelic'
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            return self.m_Data
        return { }

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMSG_TREASURERELIC, self.OnGenerateRelic, self.m_Flag, iSub = TREASURERELIC_GENERATELIST, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMSG_TREASURERELIC, self.OnSelectRelic, self.m_Flag, iSub = TREASURERELIC_SELECTRELIC, iOnce = 0)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADD_MONSTERRELIC, self.OnUseMonsterRelic, self.m_Flag)

    
    def ReleaseEvent(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMSG_TREASURERELIC, self.m_Flag, iSub = TREASURERELIC_GENERATELIST)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMSG_TREASURERELIC, self.m_Flag, iSub = TREASURERELIC_SELECTRELIC)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_ADD_MONSTERRELIC, self.m_Flag)

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def OnGenerateRelic(self, oWarMgr, dInfo):
        if 'Layer' not in dInfo or 'LayerRelic' not in dInfo:
            return None
        lstAppear = []
        for lstOption in dInfo['LayerRelic'].values():
            for dRelic in lstOption:
                lstAppear.extend(dRelic.keys())
            
        
        dRelicInfo = {
            'choose': [],
            'appear': lstAppear }
        iLayer = dInfo['Layer']
        self.m_Data[iLayer] = {
            'RelicInfo': dRelicInfo,
            'MonsterInfo': { } }

    
    def OnSelectRelic(self, oWarMgr, dInfo):
        if 'Relic' not in dInfo:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        if iLayer in self.m_Data and 'RelicInfo' in self.m_Data[iLayer] and 'choose' in self.m_Data[iLayer]['RelicInfo']:
            iRelic = dInfo['Relic']
            self.m_Data[iLayer]['RelicInfo']['choose'].append(iRelic)

    
    def OnUseMonsterRelic(self, oWarMgr, oOwner, dInfo):
        if 'Perform' not in dInfo or not dInfo['Perform']:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        if iLayer in self.m_Data and 'MonsterInfo' in self.m_Data[iLayer]:
            iPerform = dInfo['Perform']
            if iPerform not in self.m_Data[iLayer]['MonsterInfo']:
                self.m_Data[iLayer]['MonsterInfo'][iPerform] = 0
            self.m_Data[iLayer]['MonsterInfo'][iPerform] += 1



class CWeaponStoreAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CWeaponStoreAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_WeaponStore'
        self.InitEvent()
        self.InitData()

    
    def InitData(self):
        lstAllHero = self.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            self.m_Data[oHero.m_PlayerID] = self.GetInitData()
        

    
    def Refresh(self, pid):
        self.m_Data[pid] = self.GetInitData()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def InitEvent(self):
        lstAllHero = self.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPONCOM, self.OnAddWeapon, 'WeaponStore_OnAddWeapon')
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPONCOM, self.OnRemoveWeapon, 'WeaponStore_OnRemoveWeapon')
        
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.OnInteractNpc, 'WeaponStore_OnInteractNpc')

    
    def ReleaseEvent(self):
        lstAllHero = self.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPONCOM, 'WeaponStore_OnAddWeapon')
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPONCOM, 'WeaponStore_OnRemoveWeapon')
        
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, 'WeaponStore_OnInteractNpc')

    
    def OnInteractNpc(self, oWarMgr, oOwner, dInfo):
        iNpcType = dInfo['NpcType']
        if iNpcType != NWARRIOR_NPC_WEAPONSTORE:
            return None
        oHero = self.m_Game.GetObject(dInfo['Hero'])
        dPlayerData = self.m_Data[oHero.m_PlayerID]
        if not dPlayerData['IsInterAction']:
            dPlayerData['IsInterAction'] = 1

    
    def OnAddWeapon(self, oWarMgr, oOwner, dInfo):
        oWeapon = dInfo['Weapon']
        iBagType = dInfo['BagType']
        dPlayerData = self.m_Data[oOwner.m_PlayerID]
        iNum = 0
        if iBagType == BAG_TYPE_WEAPONSTORE:
            if oWeapon.m_ID in dPlayerData['AddWeaponStoreCom']:
                iNum = dPlayerData['AddWeaponStoreCom'][oWeapon.m_ID]['num']
            dWeapon = self.GetWeaponInfo(oWeapon, iNum + 1)
            dPlayerData['AddWeaponStoreCom'][oWeapon.m_ID] = dWeapon
        elif iBagType == BAG_TYPE_EXWEAPON:
            if oWeapon.m_ID in dPlayerData['AddWeaponCom']:
                iNum = dPlayerData['AddWeaponCom'][oWeapon.m_ID]['num']
            dWeapon = self.GetWeaponInfo(oWeapon, iNum + 1)
            dPlayerData['AddWeaponCom'][oWeapon.m_ID] = dWeapon

    
    def OnRemoveWeapon(self, oWarMgr, oOwner, dInfo):
        oWeapon = dInfo['Weapon']
        iBagType = dInfo['BagType']
        dPlayerData = self.m_Data[oOwner.m_PlayerID]
        iNum = 0
        if iBagType == BAG_TYPE_WEAPONSTORE:
            if oWeapon.m_ID in dPlayerData['RemoveWeaponStoreCom']:
                iNum = dPlayerData['RemoveWeaponStoreCom'][oWeapon.m_ID]['num']
            dWeapon = self.GetWeaponInfo(oWeapon, iNum + 1)
            dPlayerData['RemoveWeaponStoreCom'][oWeapon.m_ID] = dWeapon

    
    def GetInitData(self):
        dData = {
            'IsInterAction': 0,
            'AddWeaponCom': { },
            'AddWeaponStoreCom': { },
            'RemoveWeaponStoreCom': { } }
        return dData

    
    def GetWeaponInfo(self, oWeapon, iNum = 0):
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        dWeaponData = {
            'id': oWeapon.m_SID,
            'strengthen_lv': oWeapon.m_BaseGrade,
            'inscription': list(oInscriptionCom.m_Inscription) }
        if iNum:
            dWeaponData['num'] = iNum
        return dWeaponData

    
    def GetStatistics(self, pid):
        dSendData = { }
        dPlayerData = self.m_Data[pid]
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        lstWeaponStore = []
        for oWeapon in oHero.m_WeaponStoreCon.m_Item.values():
            dWeapon = self.GetWeaponInfo(oWeapon)
            lstWeaponStore.append(dWeapon)
        
        lstAddWeaponCom = []
        for dWeapon in dPlayerData['AddWeaponCom'].values():
            lstAddWeaponCom.append(dWeapon)
        
        lstAddWeaponStoreCom = []
        for dWeapon in dPlayerData['AddWeaponStoreCom'].values():
            lstAddWeaponStoreCom.append(dWeapon)
        
        lstRemoveWeaponStoreCom = []
        for dWeapon in dPlayerData['RemoveWeaponStoreCom'].values():
            lstRemoveWeaponStoreCom.append(dWeapon)
        
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        dSendData = {
            'WeaponStore': lstWeaponStore,
            'AddWeaponCom': lstAddWeaponCom,
            'AddWeaponStoreCom': lstAddWeaponStoreCom,
            'RemoveWeaponStoreCom': lstRemoveWeaponStoreCom,
            'Layer': oLevelCtrl.m_LayerNum,
            'IsInterAction': dPlayerData['IsInterAction'] }
        return dSendData

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData



class CServantAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CServantAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Servant = { }
        self.m_FightFrame = { }
        self.m_Level = { }
        self.m_Flag = 'BigDataAnalyse_Servant'
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        self.InitEvent()

    
    def InitEvent(self):
        lstAllHero = self.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or not (oHero.m_Servant):
                continue
            self.m_Servant[oHero.m_Servant] = oHero.m_PlayerID
            self.m_FightFrame[oHero.m_PlayerID] = {
                SERVANT_FIGHTTYPE_TURRET: -1,
                SERVANT_FIGHTTYPE_HUMAN: -1 }
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oHero.m_Servant, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, self.m_Flag, iSub = ATTACKERSUBMSG_NORMAL)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oHero.m_Servant, cl_msgcenter.MSG_WAR_DIE, self.OnDying, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oHero.m_Servant, cl_msgcenter.MSG_WAR_DIEDIST, self.OnDiedist, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oHero.m_Servant, cl_msgcenter.MSG_WAR_SERVANT_FIGHT_START, self.OnFightStart, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oHero.m_Servant, cl_msgcenter.MSG_WAR_SERVANT_FIGHT_END, self.OnFightEnd, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oHero.m_Servant, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, self.m_Flag)
        

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def ReleaseEvent(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iServant in self.m_Servant:
            cl_msgcenter.DoneAttention(self.m_WarMgr, iServant, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iServant, cl_msgcenter.MSG_WAR_DIE, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iServant, cl_msgcenter.MSG_WAR_DIEDIST, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iServant, cl_msgcenter.MSG_WAR_SERVANT_FIGHT_START, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iServant, cl_msgcenter.MSG_WAR_SERVANT_FIGHT_END, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iServant, cl_msgcenter.MSG_WAR_ENTERSCENE, self.m_Flag)
        

    
    def GetLevelStatistics(self, pid, iLevel):
        if iLevel not in self.m_Data:
            return { }
        if pid not in self.m_Data[iLevel]:
            return { }
        return self.m_Data[iLevel][pid]

    
    def OnEnterScene(self, oWarMgr, oOwner, dInfo):
        oScene = self.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        pid = oOwner.m_OwnerPlayerID
        iLevel = oScene.m_Level
        self.m_Level[pid] = iLevel
        if iLevel not in self.m_Data:
            self.m_Data[iLevel] = { }
        if pid not in self.m_Data[iLevel]:
            self.m_Data[iLevel][pid] = self.GetInitData()

    
    def OnFightStart(self, oWarMgr, oOwner, dInfo):
        iType = dInfo['Type']
        iFrame = dInfo['Frame']
        pid = oOwner.m_OwnerPlayerID
        self.m_FightFrame[pid][iType] = iFrame

    
    def OnFightEnd(self, oWarMgr, oOwner, dInfo):
        iType = dInfo['Type']
        iEndFrame = dInfo['Frame']
        self.CalFightFrame(oOwner, iType, iEndFrame)

    
    def CalFightFrame(self, oOwner, iType, iEndFrame):
        pid = oOwner.m_OwnerPlayerID
        iLevel = self.m_Level[pid]
        if not iType:
            iType = SERVANT_FIGHTTYPE_HUMAN if oOwner.m_Phase == 1 else SERVANT_FIGHTTYPE_TURRET
        if self.m_FightFrame[pid][iType] > 0:
            if not iEndFrame:
                iEndFrame = self.m_Game.GetFrameNum()
            iFightFrame = iEndFrame - self.m_FightFrame[pid][iType]
            if iType == SERVANT_FIGHTTYPE_HUMAN:
                self.m_Data[iLevel][pid]['servant_human_time'] += iFightFrame
            else:
                self.m_Data[iLevel][pid]['servant_turret_time'] += iFightFrame
            self.m_FightFrame[pid][iType] = 0

    
    def OnDealTotalDam(self, oWarMgr, oOwner, dInfo):
        iTotalDam = cl_formula.CalDealTotalDam(dInfo)
        pid = oOwner.m_OwnerPlayerID
        iLevel = self.m_Level[pid]
        if self.m_Data[iLevel][pid]['servant_max_damage'] < iTotalDam:
            self.m_Data[iLevel][pid]['servant_max_damage'] = iTotalDam
        self.m_Data[iLevel][pid]['servant_damage'] += iTotalDam

    
    def OnDying(self, oWarMgr, oOwner, dInfo):
        self.CalFightFrame(oOwner, 0, 0)
        if self.IsNotCalculate(oOwner):
            return None
        pid = oOwner.m_OwnerPlayerID
        iLevel = self.m_Level[pid]
        self.m_Data[iLevel][pid]['servant_fall_num'] += 1

    
    def OnDiedist(self, oWarMgr, oOwner, dInfo):
        pid = oOwner.m_OwnerPlayerID
        iLevel = self.m_Level[pid]
        if self.IsPassiveExplosin(oOwner, dInfo):
            self.m_Data[iLevel][pid]['servant_self_destruct'] += 1
            return None
        if self.IsNotCalculate(oOwner):
            return None
        self.m_Data[iLevel][pid]['servant_death_num'] += 1

    
    def IsPassiveExplosin(self, oOwner, dInfo):
        iCanExplosion = oOwner.Query('CanExplosion', 0)
        oReason = dInfo['RS']
        if iCanExplosion and oReason and oReason.GetStrReason() != 'AtiveExplosion':
            return 1
        return 0

    
    def IsNotCalculate(self, oServant):
        oOwner = oServant.GetOwner()
        if not oOwner or oOwner.IsDeadNoDying():
            return True
        if oServant.Query('CanExplosion', 0):
            return True
        return False

    
    def GetInitData(self):
        dData = {
            'servant_damage': 0,
            'servant_max_damage': 0,
            'servant_fall_num': 0,
            'servant_death_num': 0,
            'servant_self_destruct': 0,
            'servant_human_time': 0,
            'servant_turret_time': 0 }
        return dData

    
    def GetStatistics(self, pid):
        if pid not in self.m_Servant.values():
            return { }
        dData = self.GetInitData()
        for sKey in dData:
            for dPlayerData in self.m_Data.values():
                if pid not in dPlayerData:
                    continue
                dData[sKey] += dPlayerData[pid][sKey]
            
        
        return dData

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData



class CStarlightAnalyseCom(CBaseAnalyseCom):
    m_Weapon = (1215, 1218)
    m_AttackPf = (9215, 9218)
    m_Inscription = 4961
    
    def __init__(self, oGame):
        super(CStarlightAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_Starlight'
        self.m_CurLayer = 0
        self.m_Item = { }
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            return self.m_Data
        return { }

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelInit, self.m_Flag, iOnce = 0)

    
    def ReleaseEvent(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_Flag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PICK, self.m_Flag)
        lstAllHero = self.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, self.m_Flag, ATTACKERSUBMSG_NORMAL)
        

    
    def OnLevelInit(self, oWarMgr, dMsgInfo):
        iLayer = dMsgInfo['Layer']
        if self.m_CurLayer != iLayer:
            self.m_CurLayer = iLayer
            self.m_Data[iLayer] = { }

    
    def OnAddPlayer(self, oWarMgr, dMsgInfo):
        iHero = dMsgInfo['Hero']
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPON, self.OnAddWeapon, self.m_Flag)

    
    def OnAddWeapon(self, oWarMgr, oOwner, dMsgInfo):
        oWeapon = dMsgInfo['Weapon']
        if oWeapon.m_SID not in self.m_Weapon:
            return None
        if not self.m_Item:
            self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PICK, self.OnPick, self.m_Flag)
        iHero = oOwner.m_ID
        iItem = dMsgInfo['ItemID']
        if iHero in self.m_Item:
            lstItem = self.m_Item[iHero]
            if iItem not in lstItem:
                lstItem.append(iItem)
            else:
                self.m_Item[iHero] = [
                    iItem]
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.OnRemoveWeapon, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, self.m_Flag, ATTACKERSUBMSG_NORMAL)

    
    def OnRemoveWeapon(self, oWarMgr, oOwner, dMsgInfo):
        if dMsgInfo['SID'] not in self.m_Weapon:
            return None
        iHero = oOwner.m_ID
        iItem = dMsgInfo['ItemID']
        lstItem = self.m_Item[iHero]
        lstItem.remove(iItem)
        if not lstItem:
            self.m_Item.pop(iHero)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, self.m_Flag, ATTACKERSUBMSG_NORMAL)
            if not self.m_Item:
                self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_PICK, self.m_Flag)

    
    def OnAttack(self, oWarMgr, oOwner, dMsgInfo):
        if 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        if iPerform not in self.m_AttackPf:
            return None
        iHitWeakness = 0
        if 'MainDam' in dMsgInfo:
            lstDam = dMsgInfo['MainDam']
            for _, oReason in lstDam:
                iDamType = oReason.Query('DamType')
                if iDamType & DAM_TYPE_WEAKNESS == DAM_TYPE_WEAKNESS:
                    iHitWeakness = 1
                    break
            
        if not iHitWeakness:
            return None
        iWeapon = oSkill.m_Base['Weapon']
        iKey = iWeapon if self.m_Inscription in oSkill.m_Cache['Inscription'] else -iWeapon
        dData = self.m_Data[self.m_CurLayer]
        if iKey not in dData:
            dData[iKey] = {
                'FallTimes': 0,
                'GetTimes': 0 }
        dData[iKey]['FallTimes'] += 1

    
    def OnPick(self, oWarMgr, oOwner, dMsgInfo):
        if 'Type' not in dMsgInfo or dMsgInfo['Type'] != NWARRIOR_DROP_AXE:
            return None
        iWeapon = dMsgInfo['ItemID']
        oWeapon = oOwner.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oPerformCom = oWeapon.GetComponent('Perform')
        iKey = oWeapon.m_ID if oPerformCom.GetPerform(self.m_Inscription) else -(oWeapon.m_ID)
        if iKey not in self.m_Data[self.m_CurLayer]:
            iKey = -iKey
        self.m_Data[self.m_CurLayer][iKey]['GetTimes'] += 1


TASK_NOACTION = 0
TASK_GAMELOSE = 1
TASK_SUCCESS = 2
TASK_FAIL = 3

class CGreatTaskAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CGreatTaskAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_KeyNum = 0
        self.m_Npc2Key = { }
        self.m_Task2Key = { }
        self.m_Flag = 'BigDataAnalyse_GreatTask'
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        self.InitEvent()
        if not self.m_Data:
            for pid in oWarMgr.GetRoomPlayer():
                self.m_Data[pid] = { }
            

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iOnce = 0)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateNpc, self.m_Flag)
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_TASK, self.OnCreateTaskList, self.m_Flag, TASK_CREATETASKLIST)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_TASK, self.OnChooseTask, self.m_Flag, TASK_CHOOSETASK)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_TASK, self.OnChangeTaskStatus, self.m_Flag, TASK_CHANGESTATUS)
        

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_Flag)
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_TASK, self.m_Flag, TASK_CREATETASKLIST)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_TASK, self.m_Flag, TASK_CHOOSETASK)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_TASK, self.m_Flag, TASK_CHANGESTATUS)
        
        self.m_Game = None
        self.m_WarMgr = None

    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'KN': self.m_KeyNum,
            'TK': DeepCopy(self.m_Task2Key) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_KeyNum = dData['KN']
            self.m_Task2Key = dData['TK']

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            return self.m_Data[pid]
        return { }

    
    def OnCreateNpc(self, oWarMgr, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_TASKNPC:
            return None
        if not oNpc.m_LineIdx:
            oScene = self.m_Game.m_SceneMgr.GetScene(oNpc.m_Scene)
            iLevel = oScene.m_Level if oScene else 0
            TaskLog.Debug('%s tasknpc %s nolevel curlevel %s' % (self.m_Game.m_ID, oNpc.m_ID, iLevel))
            return None
        iKeyNum = self.NewKeyNum()
        self.m_Npc2Key[oNpc.m_ID] = { }
        for pid in self.m_WarMgr.GetRoomPlayer():
            if pid not in self.m_Data:
                continue
            self.m_Npc2Key[oNpc.m_ID][pid] = iKeyNum
            self.m_Data[pid][iKeyNum] = {
                'Level': oNpc.m_LineIdx[0],
                'Appear': [
                    0],
                'Choose': 0,
                'Result': TASK_NOACTION }
        

    
    def NewKeyNum(self):
        self.m_KeyNum += 1
        return self.m_KeyNum

    
    def GetCopyData(self, iNpc, pid, iKey):
        dData = DeepCopy(self.m_Data[pid][iKey])
        iKeyNum = self.NewKeyNum()
        self.m_Npc2Key[iNpc][pid] = iKeyNum
        self.m_Data[pid][iKeyNum] = dData
        return (iKey, dData)

    
    def OnCreateTaskList(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        if pid not in self.m_Data:
            return None
        iNpc = dInfo['NpcID']
        if iNpc not in self.m_Npc2Key:
            return None
        if pid not in self.m_Npc2Key[iNpc]:
            return None
        iKey = self.m_Npc2Key[iNpc][pid]
        if 'RefreshTask' in dInfo:
            (_, dData) = self.GetCopyData(iNpc, pid, iKey)
            dData['Choose'] = 0
        else:
            dData = self.m_Data[pid][iKey]
        dData['Appear'] = list(dInfo['TaskInfo'].values())

    
    def OnChooseTask(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        if pid not in self.m_Data:
            return None
        iNpc = dInfo['NpcID']
        if iNpc not in self.m_Npc2Key:
            return None
        if pid not in self.m_Npc2Key[iNpc]:
            return None
        iKey = self.m_Npc2Key[iNpc][pid]
        iChoose = self.m_Data[pid][iKey]['Choose']
        if iChoose:
            (iKey, dData) = self.GetCopyData(iNpc, pid, iKey)
        else:
            dData = self.m_Data[pid][iKey]
        iChooseTaskSID = dInfo['TaskSID']
        dData['Appear'] = self.GetNormalTask(oHero, iNpc, iChooseTaskSID, dData['Appear'])
        self.m_Task2Key[dInfo['TaskID']] = iKey
        dData['Choose'] = iChooseTaskSID
        dData['Result'] = TASK_GAMELOSE

    
    def GetNormalTask(self, oHero, iNpc, iChoose, lstTask):
        if not lstTask:
            return lstTask
        oNpc = oHero.m_Game.GetObject(iNpc)
        if not oNpc:
            return lstTask
        dTaskInfo = { }
        for iIndex, iTask in enumerate(lstTask):
            dTaskInfo[iIndex] = iTask
        
        dTaskChooseStatus = oNpc.GetTaskChooseStatus(oHero, dTaskInfo)
        lstNormalTask = []
        for iIndex, iTask in dTaskInfo.items():
            iChooseStatus = dTaskChooseStatus[iIndex]
            if iChooseStatus in (TASK_CHOOSE_STATUS_UNRECEIVED, TASK_CHOOSE_STATUS_LOCK):
                continue
            if iChooseStatus == TASK_CHOOSE_STATUS_CHOSEN and iTask != iChoose:
                continue
            lstNormalTask.append(iTask)
        
        return lstNormalTask

    
    def OnChangeTaskStatus(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        if pid not in self.m_Data:
            return None
        iTaskID = dInfo['TaskID']
        if iTaskID not in self.m_Task2Key:
            return None
        iKey = self.m_Task2Key.pop(iTaskID)
        self.m_Data[pid][iKey]['Result'] = dInfo['Status']

    
    def OnPlayerLevelGame(self, oWarMgr, dInfo):
        if not dInfo['AssignSettleType'] == SETTLE_FINISHWAR:
            return None
        oHero = self.m_Game.GetObject(dInfo['Hero'])
        if not oHero:
            return None
        pid = oHero.m_PlayerID
        if pid not in self.m_Data:
            return None
        dData = self.m_Data[pid]
        for oTask in oHero.m_TaskCon.m_Task.values():
            iKey = self.m_Task2Key.pop(oTask.m_ID, 0)
            if not iKey or iKey not in dData:
                continue
            dData[iKey]['Result'] = TASK_FAIL
        



class CNewSurvivorCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CNewSurvivorCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_NewSurvivor'
        oSurvivorElement = self.m_WarMgr.GetComponent('NewSurvivorElement')
        self.m_Survivor = oSurvivorElement
        self.m_PhaseLeftFightTimeInfo = { }
        self.m_WarInfo = { }
        self.InitEvent()
        self.InitData()
        self.m_PhaseTalentGenInfo = { }

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnDealPhaseInfo, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_Survivor, cl_msgcenter.MSG_WARMSG_RESTPHASE, self.OnRestPhase, self.m_Flag, iOnce = 0)
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_AFTERADDCASH, self.OnAddCash, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_KILL, self.OnKill, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_SHOPREFRESH, self.OnShopRefresh, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_BUYGOODS, self.OnBuyGoods, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADEWEAPON, self.OnWeaponUpGrade, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_RECASTWEAPON, self.OnWeaponRecast, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPON, self.OnAddWeapon, self.m_Flag)
        

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Data = { }
        self.m_Game = None
        self.m_WarMgr = None
        self.m_Survivor = None

    
    def ReleaseEvent(self):
        cl_msgcenter.DoneEvent(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_Survivor, cl_msgcenter.MSG_WARMSG_RESTPHASE, self.m_Flag)
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_AFTERADDCASH, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_KILL, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_SHOPREFRESH, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_BUYGOODS, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADEWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_RECASTWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPON, self.m_Flag)
        

    
    def InitData(self):
        for pid in self.m_WarMgr.GetRoomPlayer():
            self.m_Data[pid] = { }
            self.m_Data[pid]['PhaseInfo'] = { }
            self.m_Data[pid]['LeftFightTime'] = { }
            self.m_Data[pid]['WarInfo'] = {
                'TalentAppear': 0,
                'TalentBuy': 0,
                'WeaponUpdate': 0,
                'WeaponReforge': 0,
                'MaxWeaponLv': 0 }
        

    
    def GetInitData(self, oHero):
        dData = {
            'KillMonster': 0,
            'GetCoin': 0,
            'CostCoin': 0,
            'GoodsRefresh': 0,
            'LeftCoin': oHero.m_WarCash }
        return dData

    
    def OnAddWeapon(self, oWarMgr, oHero, dInfo):
        oWeapon = dInfo['Weapon']
        pid = oHero.m_PlayerID
        iMaxLv = self.m_Data[pid]['WarInfo']['MaxWeaponLv']
        if oWeapon.m_BaseGrade > iMaxLv:
            self.m_Data[pid]['WarInfo']['MaxWeaponLv'] = oWeapon.m_BaseGrade

    
    def OnWeaponUpGrade(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        self.m_Data[pid]['WarInfo']['WeaponUpdate'] += 1
        oWeapon = oHero.m_WieldCon.GetItemByID(dInfo['ItemID'])
        if not oWeapon:
            return None
        iMaxLv = self.m_Data[pid]['WarInfo']['MaxWeaponLv']
        if oWeapon.m_BaseGrade > iMaxLv:
            self.m_Data[pid]['WarInfo']['MaxWeaponLv'] = oWeapon.m_BaseGrade

    
    def OnWeaponRecast(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        self.m_Data[pid]['WarInfo']['WeaponReforge'] += 1

    
    def OnAddCash(self, oWarMgr, oHero, dInfo):
        iPhase = self.m_Survivor.m_Phase
        pid = oHero.m_PlayerID
        if iPhase not in self.m_Data[pid]['PhaseInfo']:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_BOSS:
            return None
        iCash = dInfo['Cash']
        if iCash > 0:
            self.m_Data[pid]['PhaseInfo'][iPhase]['GetCoin'] += iCash
        elif iCash < 0:
            self.m_Data[pid]['PhaseInfo'][iPhase]['CostCoin'] -= iCash
        self.m_Data[pid]['PhaseInfo'][iPhase]['LeftCoin'] = oHero.m_WarCash

    
    def OnKill(self, oWarMgr, oHero, dInfo):
        iPhase = self.m_Survivor.m_Phase
        pid = oHero.m_PlayerID
        if iPhase not in self.m_Data[pid]['PhaseInfo']:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_BOSS:
            return None
        oTarget = self.m_Game.GetObject(dInfo['VID'])
        if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
            return None
        self.m_Data[pid]['PhaseInfo'][iPhase]['KillMonster'] += 1

    
    def OnShopRefresh(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        iPhase = self.m_Survivor.m_Phase
        if iPhase not in self.m_Data[pid]['PhaseInfo']:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_CurNode.m_LevelType == LEVEL_TYPE_BOSS:
            return None
        self.m_Data[pid]['PhaseInfo'][iPhase]['GoodsRefresh'] += 1
        dGoodsMenu = dInfo['GoodsMenu']
        for oGoods in dGoodsMenu.values():
            if oGoods.m_GoodsType == VIRTUAL_ITEM_GOLDENCUP:
                self.m_Data[pid]['WarInfo']['TalentAppear'] += 1
        

    
    def OnBuyGoods(self, oWarMgr, oHero, dInfo):
        iType = dInfo['Type']
        if iType == VIRTUAL_ITEM_GOLDENCUP:
            pid = oHero.m_PlayerID
            self.m_Data[pid]['WarInfo']['TalentBuy'] += 1

    
    def OnRestPhase(self, oSurvivor, dInfo):
        iFightTime = oSurvivor.m_PhaseData[oSurvivor.m_Phase]['FightTime']
        iCurFrame = self.m_Game.GetFrameNum()
        iCostTime = Frame2Time(iCurFrame - self.m_Survivor.m_PhaseStartFrame - self.m_Survivor.m_PauseTotalFrame)
        if not iFightTime:
            iTime = iCostTime
        else:
            iTime = iFightTime - iCostTime
        for pid in self.m_WarMgr.GetRoomPlayer():
            self.m_Data[pid]['LeftFightTime'][oSurvivor.m_Phase] = iTime
        

    
    def OnDealPhaseInfo(self, oSurvivor, dInfo):
        for iHero in self.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                return None
            self.m_Data[oHero.m_PlayerID]['PhaseInfo'][self.m_Survivor.m_Phase] = self.GetInitData(oHero)
        

    
    def GetStatistics(self, pid):
        if pid not in self.m_Data:
            return { }
        dData = { }
        lstPhaseInfo = []
        for iPhase, dPhaseInfo in self.m_Data[pid]['PhaseInfo'].items():
            lstPhaseInfo.append({
                'phase': iPhase,
                'left_time': self.m_Data[pid]['LeftFightTime'][iPhase] if iPhase in self.m_Data[pid]['LeftFightTime'] else -1,
                'kill_monster': dPhaseInfo['KillMonster'],
                'get_coin': dPhaseInfo['GetCoin'],
                'cost_coin': dPhaseInfo['CostCoin'],
                'left_coin': dPhaseInfo['LeftCoin'],
                'goods_refresh': dPhaseInfo['GoodsRefresh'] })
        
        dData = {
            'PhaseInfo': lstPhaseInfo,
            'TalentAppear': self.m_Data[pid]['WarInfo']['TalentAppear'],
            'TalentBuy': self.m_Data[pid]['WarInfo']['TalentBuy'],
            'WeaponUpdate': self.m_Data[pid]['WarInfo']['WeaponUpdate'],
            'WeaponReforge': self.m_Data[pid]['WarInfo']['WeaponReforge'],
            'MaxWeaponLv': self.m_Data[pid]['WarInfo']['MaxWeaponLv'] }
        return dData

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData



class CStormChaserAnalyseCom(CBaseAnalyseCom):
    m_Weapon = 1606
    m_AttackPf = 9606
    m_CheckState = 1849
    
    def __init__(self, oGame):
        super(CStormChaserAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_StormChaser'
        self.m_Item = { }
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def GetStatistics(self, pid):
        if pid not in self.m_Data or not self.m_Data[pid]:
            return { }
        lstSendData = []
        for iLayer, dWeaponInfo in self.m_Data[pid].items():
            dLayerData = {
                'layer': iLayer,
                'map_id': dWeaponInfo['MapId'],
                'shoot_damage_times': dWeaponInfo['ShootDamageTimes'],
                'total_damage_times': dWeaponInfo['TotalDamgeTimes'] }
            lstSendData.append(dLayerData)
        
        return {
            self.m_Weapon: lstSendData }

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_Flag, iOnce = 0)

    
    def ReleaseEvent(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_Flag)
        lstAllHero = self.m_WarMgr.GetAllHero()
        for iHero in lstAllHero:
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, self.m_Flag, ATTACKERSUBMSG_NORMAL)
        

    
    def OnAddPlayer(self, oWarMgr, dMsgInfo):
        iHero = dMsgInfo['Hero']
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDWEAPON, self.OnAddWeapon, self.m_Flag)

    
    def OnAddWeapon(self, oWarMgr, oOwner, dMsgInfo):
        oWeapon = dMsgInfo['Weapon']
        if oWeapon.m_SID != self.m_Weapon:
            return None
        iHero = oOwner.m_ID
        iItem = dMsgInfo['ItemID']
        if iHero in self.m_Item:
            lstItem = self.m_Item[iHero]
            if iItem not in lstItem:
                lstItem.append(iItem)
            else:
                self.m_Item[iHero] = [
                    iItem]
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.OnRemoveWeapon, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, self.m_Flag, ATTACKERSUBMSG_NORMAL)

    
    def OnRemoveWeapon(self, oWarMgr, oOwner, dMsgInfo):
        if dMsgInfo['SID'] != self.m_Weapon:
            return None
        iHero = oOwner.m_ID
        iItem = dMsgInfo['ItemID']
        lstItem = self.m_Item[iHero]
        lstItem.remove(iItem)
        if not lstItem:
            self.m_Item.pop(iHero)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEWEAPON, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, self.m_Flag, ATTACKERSUBMSG_NORMAL)

    
    def OnAttack(self, oWarMgr, oOwner, dMsgInfo):
        if 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        if iPerform != self.m_AttackPf:
            return None
        dData = self.m_Data.setdefault(oOwner.m_PlayerID, { })
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_LayerNum not in dData:
            dData[oLevelCtrl.m_LayerNum] = {
                'ShootDamageTimes': 0,
                'TotalDamgeTimes': 0 }
        if oOwner.m_State.GetItemBySID(self.m_CheckState):
            dData[oLevelCtrl.m_LayerNum]['ShootDamageTimes'] += 1
        dData[oLevelCtrl.m_LayerNum]['TotalDamgeTimes'] += 1
        dData[oLevelCtrl.m_LayerNum]['MapId'] = oLevelCtrl.m_CurNode.m_Level



class CRelicTalentAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CRelicTalentAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_RelicTalent'
        self.m_ListenDrop = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def GetStatistics(self, pid):
        oGame = self.m_Game
        oWarMgr = self.m_WarMgr
        dRemoveDrop = { }
        for iDrop, iPlayer in self.m_ListenDrop.items():
            if iPlayer != pid:
                continue
            dRemoveDrop[iDrop] = 1
            cl_msgcenter.DoneAttention(oWarMgr, iDrop, cl_msgcenter.MSG_WAR_REMOVEOBJ, self.m_Flag)
            oDrop = oGame.GetObject(iDrop)
            if not iDrop:
                continue
            self.RecordGiveUpDrop(oDrop)
        
        for iDrop in dRemoveDrop:
            self.m_ListenDrop.pop(iDrop, 0)
        
        if pid in self.m_Data:
            return self.m_Data[pid]
        return { }

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        self.InitEvent()

    
    def InitEvent(self):
        oWarMgr = self.m_WarMgr
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            self.m_Data[iPlayer] = {
                'StartAppear': [],
                'StartChoose': 0,
                'IfAuto': 0,
                'WakeAppear': [],
                'WakeChoose': [],
                'Arcane': 0,
                'RelicDamage': 0,
                'Season': oWarMgr.m_SeasonNum }
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELICTALENT, self.OnChooseRelic, self.m_Flag, TYPE_CHOOSERELIC)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELICTALENT, self.OnChooseTalent, self.m_Flag, TYPE_CHOOSETALENT)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELICTALENT, self.OnCreateTalent, self.m_Flag, TYPE_CREATETALENT)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, self.OnChangeMagicPower, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealDamage, self.m_Flag, ATTACKERSUBMSG_NORMAL)
        

    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in oWarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELICTALENT, self.m_Flag, TYPE_CHOOSERELIC)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELICTALENT, self.m_Flag, TYPE_CHOOSETALENT)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELICTALENT, self.m_Flag, TYPE_CREATETALENT)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_Flag, ATTACKERSUBMSG_NORMAL)
        

    
    def OnChooseRelic(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        dData = self.m_Data[iPlayer]
        dData['StartAppear'] = dMsgInfo['Option']
        dData['StartChoose'] = dMsgInfo['Choose']
        dData['IfAuto'] = dMsgInfo['Auto']

    
    def OnChooseTalent(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        self.m_ListenDrop.pop(dMsgInfo['Drop'], 0)
        cl_msgcenter.DoneAttention(oWarMgr, dMsgInfo['Drop'], cl_msgcenter.MSG_WAR_REMOVEOBJ, self.m_Flag)
        self.m_Data[iPlayer]['WakeChoose'].append(dMsgInfo['Choose'])

    
    def OnCreateTalent(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        self.m_Data[iPlayer]['WakeAppear'].extend(dMsgInfo['Talent'])
        iDrop = dMsgInfo['Drop']
        if iDrop not in self.m_ListenDrop:
            self.m_ListenDrop[iDrop] = iPlayer
            cl_msgcenter.AddAttentionFunc(oWarMgr, iDrop, cl_msgcenter.MSG_WAR_REMOVEOBJ, self.OnDropRemove, self.m_Flag)

    
    def OnDropRemove(self, oWarMgr, oDrop, dMsgInfo):
        self.m_ListenDrop.pop(oDrop.m_ID, 0)
        self.RecordGiveUpDrop(oDrop)

    
    def RecordGiveUpDrop(self, oDrop):
        oHero = self.m_Game.GetObject(oDrop.m_Owner)
        if not oHero:
            return None
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        dReward = oHero.m_RelicTalentCon.m_DropReward
        if oDrop.m_ID not in dReward or not dReward[oDrop.m_ID]:
            return None
        self.m_Data[iPlayer]['WakeChoose'].append(0)

    
    def OnChangeMagicPower(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        dData = self.m_Data[iPlayer]
        dData['Arcane'] = dMsgInfo['MagicPower']

    
    def OnDealDamage(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        dPerform = oHero.m_RelicTalentCon.m_DamagePF
        if not dPerform or not CheckInPointPerformByMsgInfo(oHero, dPerform, dMsgInfo, 1, 1):
            return None
        if oHero.m_ID == dMsgInfo['CurVID']:
            return None
        iTotalDam = cl_formula.CalDealTotalDam(dMsgInfo)
        dData = self.m_Data[iPlayer]
        dData['RelicDamage'] += iTotalDam



class CDeviceAnalyseCom(CBaseAnalyseCom):
    m_ExcludeHideLevelType = (HIDELV_TYPE_SIGHT, HIDELV_TYPE_TRAP, HIDELV_TYPE_JUMP)
    
    def __init__(self, oGame):
        super(CDeviceAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_Device'
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoalOK, self.m_Flag, -1, 0)

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def GetStatistics(self, pid):
        if pid not in self.m_Data:
            return { }
        return self.m_Data[pid]

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_Flag)
        for iHero in oWarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DEVICE_INIT, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_GENERATE_DEVICECOMP, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADD_DEVICE, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'DeviceSID': 0,
                    'Auto': 0,
                    'CompNum': [
                        0,
                        0,
                        0],
                    'CompInfo': { } }
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DEVICE_INIT, self.OnChooseDevice, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_GENERATE_DEVICECOMP, self.OnGenerateDeviceComp, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADD_DEVICE, self.OnAddDeviceComp, self.m_Flag)
        

    
    def ValidLevel(self, dMsgInfo):
        iLevelType = dMsgInfo['LevelType']
        if iLevelType == LEVEL_TYPE_HALL:
            return False
        if iLevelType == LEVEL_TYPE_HIDE:
            iLevel = dMsgInfo['LevelID']
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            iHideType = oLevelCtrl.m_HideLevelLib.get(iLevel, 0)
            if iHideType in self.m_ExcludeHideLevelType:
                return False
        return True

    
    def OnLevelGoalOK(self, oWarMgr, dMsgInfo):
        if not self.ValidLevel(dMsgInfo):
            return None
        oGame = self.m_Game
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                continue
            oHero = oGame.GetObject(iHero)
            lstDeviceComp = oHero.m_DevicePerformCon.GetAllDeviceComp()
            dCompInfo = self.m_Data[iPlayer]['CompInfo']
            for iDeviceComponent in lstDeviceComp:
                if iDeviceComponent not in dCompInfo:
                    continue
                dCompInfo[iDeviceComponent]['get_pass'] += 1
            
            lstEnableDeviceComp = oHero.m_DevicePerformCon.GetAllEnableDeviceComp()
            for iDeviceComponent in lstEnableDeviceComp:
                if iDeviceComponent not in dCompInfo:
                    continue
                dCompInfo[iDeviceComponent]['install_pass'] += 1
            
        

    
    def OnChooseDevice(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        sReason = dMsgInfo['Reason']
        if sReason == 'AutoChoose':
            iAuto = 1
        elif sReason == 'PlayerChoose':
            iAuto = 0
        else:
            return None
        dData = self.m_Data[iPlayer]
        dData['Auto'] = iAuto
        dData['DeviceSID'] = dMsgInfo['DeviceSID']

    
    def OnGenerateDeviceComp(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        if 'DropInfo' not in dMsgInfo:
            return None
        lstDeviceComp = dMsgInfo['DropInfo']
        lstCompNum = self.m_Data[iPlayer]['CompNum']
        for iSID in lstDeviceComp:
            iType = cl_perform.GetPerformClassAttr(iSID, 'm_Type')
            if iType == DEVICECOMP_TYPE_COMMON:
                lstCompNum[0] += 1
                continue
            if iType == DEVICECOMP_TYPE_DEVICE:
                lstCompNum[1] += 1
                continue
            if iType == DEVICECOMP_TYPE_HERO:
                lstCompNum[2] += 1
        

    
    def OnAddDeviceComp(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        iDeviceComponent = dMsgInfo['DeviceComponent']
        oPerform = oHero.GetPerform(iDeviceComponent)
        if not oPerform:
            return None
        dCompInfo = self.m_Data[iPlayer]['CompInfo']
        dInfo = dCompInfo.setdefault(iDeviceComponent, { })
        iLevel = oPerform.m_Level
        if 'id' not in dInfo:
            dInfo['id'] = iDeviceComponent
            dInfo['lv'] = iLevel
            dInfo['install_pass'] = 0
            dInfo['get_pass'] = 0
        if iLevel > dInfo['lv']:
            dInfo['lv'] = iLevel



class CPetAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CPetAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_Pet'
        self.m_HasToHidHero = { }
        self.m_HasCompanionPet = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def GetStatistics(self, pid):
        if pid not in self.m_Data:
            return { }
        oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
        if oHero:
            oPetCon = oHero.m_PetCon
            oCurPet = oPetCon.GetCurPet()
            dInfo = self.m_Data[pid]
            if oCurPet:
                dInfo['PetType'] = oCurPet.m_PetType
                dInfo['CurPetAbility'] = oCurPet.Ability()
                dInfo['CurPetFuseNum'] = oCurPet.QuerySavedData('FuseNum', 0)
            else:
                dInfo['NoCurPet'] = 1
            oCompanionPet = oPetCon.GetCompanionPet()
            if oCompanionPet:
                dInfo['ActiveAbility'] = len(oCompanionPet.Ability())
            dInfo['PetAbilityMarkNum'] = len(oPetCon.m_AbilityMarkList)
            dInfo['PetAbilityTemplate'] = oPetCon.m_AbilityTemplate
        return self.m_Data[pid]

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in oWarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CHOOSEBENED, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADD_PETEGG, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HATCH_PET, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.m_Flag, PET_HANDLE_SETEGGTYPE)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.m_Flag, PET_HANDLE_ONECLICKFUSE)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.m_Flag, PET_HANDLE_FUSE)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.m_Flag, PET_HANDLE_RAPIDSCREEN)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.m_Flag, PET_HANDLE_BUY)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.m_Flag, PET_HANDLE_USEACTIVE)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.m_Flag, PET_HANDLE_ACTIVEABILITY)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.m_Flag)
        
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_Flag)
        self.m_Game = None
        self.m_WarMgr = None

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
        dHasCompanionPet = self.m_HasCompanionPet
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            oCompanionPet = oHero.m_PetCon.GetCompanionPet()
            if iPlayer not in self.m_Data:
                dPetHatchInfo = dict.fromkeys(ALL_PET_TYPE, 0)
                dInitData = {
                    'SeasonLevel': oHero.Query('SeasonLevel', 0),
                    'FirstChoice': 0,
                    'InitialBenediction': 0,
                    'PetAbilityMarkNum': 0,
                    'PetAbilityTemplate': 0,
                    'PetType': 0,
                    'PetNum': { },
                    'PetTotalNum': 0,
                    'PetHatchInfo': dPetHatchInfo,
                    'OneClickFuseNum': 0,
                    'FuseNumFromNPC': 0,
                    'FuseNumFromBag': 0,
                    'CurPetAbility': [],
                    'RapidScreen': 0,
                    'CurPetFuseNum': 0 }
                if oCompanionPet:
                    dInitData['CarryCompanionPet'] = 1
                    dInitData['UseActiveAbilityNum'] = 0
                    dInitData['CarryAbility'] = len(oCompanionPet.SealedAbility())
                    dInitData['CarryPetLevelNum'] = 0
                    dInitData['TotalLevelNum'] = 0
                    dInitData['ActiveInfo'] = {
                        'info': [] }
                    dInitData['ActiveAbility'] = 0
                else:
                    dInitData['CarryCompanionPet'] = 0
                iEggSum = sum(oHero.m_PetCon.m_PetEggCnt.values())
                dInitData['PetNum'][iLayer] = {
                    'layer': iLayer,
                    'get_num': iEggSum,
                    'total_num': iEggSum,
                    'fusion_num': 0 }
                dInitData['PetTotalNum'] = iEggSum
                self.m_Data[iPlayer] = dInitData
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CHOOSEBENED, self.OnChooseBened, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADD_PETEGG, self.OnAddPetEgg, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HATCH_PET, self.OnHatchEgg, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.OnSetEggType, self.m_Flag, PET_HANDLE_SETEGGTYPE)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.OnOneClickFuse, self.m_Flag, PET_HANDLE_ONECLICKFUSE)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.OnFuse, self.m_Flag, PET_HANDLE_FUSE)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.OnRapidScreen, self.m_Flag, PET_HANDLE_RAPIDSCREEN)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.OnBuyPet, self.m_Flag, PET_HANDLE_BUY)
            if oCompanionPet:
                dHasCompanionPet[iPlayer] = iHero
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.OnUseActiveAbility, self.m_Flag, PET_HANDLE_USEACTIVE)
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDLE_PET, self.OnActiveAbility, self.m_Flag, PET_HANDLE_ACTIVEABILITY)
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, self.m_Flag)
        
        if dHasCompanionPet:
            cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnChooseBened(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
        if iLayer != 1:
            return None
        iBene = dInfo['Bene']
        self.m_Data[iPlayer]['InitialBenediction'] = iBene

    
    def OnAddPetEgg(self, oWarMgr, oHero, dInfo):
        self.AddPetNum(oWarMgr, oHero)

    
    def OnBuyPet(self, oWarMgr, oHero, dInfo):
        self.AddPetNum(oWarMgr, oHero)

    
    def AddPetNum(self, oWarMgr, oHero):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
        dPetNum = self.m_Data[iPlayer]['PetNum']
        self.m_Data[iPlayer]['PetTotalNum'] += 1
        dPetNum.setdefault(iLayer, {
            'layer': iLayer,
            'get_num': 0,
            'total_num': 0,
            'fusion_num': 0 })
        dPetNum[iLayer]['get_num'] += 1
        dPetNum[iLayer]['total_num'] = self.m_Data[iPlayer]['PetTotalNum']

    
    def OnSetEggType(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        if self.m_Data[iPlayer]['FirstChoice'] == 0:
            oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
            iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
            self.m_Data[iPlayer]['FirstChoice'] = iLayer

    
    def OnHatchEgg(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        iEggPriorType = dInfo['EggPriorType']
        dPetHatchInfo = self.m_Data[iPlayer]['PetHatchInfo']
        if iEggPriorType not in dPetHatchInfo:
            dPetHatchInfo[iEggPriorType] = 1
        else:
            dPetHatchInfo[iEggPriorType] += 1

    
    def OnOneClickFuse(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        self.m_Data[iPlayer]['OneClickFuseNum'] += 1
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        dPetNum = self.m_Data[iPlayer]['PetNum']
        dPetNum.setdefault(iLayer, {
            'layer': iLayer,
            'get_num': 0,
            'total_num': 0,
            'fusion_num': 0 })
        iFuseTimes = dInfo['FuseTimes']
        dPetNum[iLayer]['fusion_num'] += iFuseTimes
        if dInfo['HandleFrom'] == PET_HANDLE_FROM_BAG:
            self.m_Data[iPlayer]['FuseNumFromBag'] += iFuseTimes
        elif dInfo['HandleFrom'] == PET_HANDLE_FROM_NPC:
            self.m_Data[iPlayer]['FuseNumFromNPC'] += iFuseTimes

    
    def OnFuse(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        dPetNum = self.m_Data[iPlayer]['PetNum']
        dPetNum.setdefault(iLayer, {
            'layer': iLayer,
            'get_num': 0,
            'total_num': 0,
            'fusion_num': 0 })
        dPetNum[iLayer]['fusion_num'] += 1
        if dInfo['HandleFrom'] == PET_HANDLE_FROM_BAG:
            self.m_Data[iPlayer]['FuseNumFromBag'] += 1
        elif dInfo['HandleFrom'] == PET_HANDLE_FROM_NPC:
            self.m_Data[iPlayer]['FuseNumFromNPC'] += 1

    
    def OnUseActiveAbility(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        self.m_Data[iPlayer]['UseActiveAbilityNum'] += 1

    
    def OnActiveAbility(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        setActiveAbility = dInfo['ActiveAbility']
        lstActiveInfo = self.m_Data[iPlayer]['ActiveInfo']['info']
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        iOrderID = len(lstActiveInfo) + 1
        oCompanionPet = oHero.m_PetCon.GetCompanionPet()
        for iAbility in setActiveAbility:
            oAbility = oCompanionPet.GetPerform(iAbility)
            dActiveInfo = {
                'order_id': iOrderID,
                'layer': iLayer,
                'type': oAbility.m_Quality }
            iOrderID += 1
            lstActiveInfo.append(dActiveInfo)
        

    
    def OnEnterScene(self, oWarMgr, oHero, dInfo):
        iHero = oHero.m_ID
        dHasToHidHero = self.m_HasToHidHero
        if iHero in dHasToHidHero:
            return None
        oScene = oHero.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
        if not oScene:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if not oLevelNode:
            return None
        if oLevelNode.m_LevelType != LEVEL_TYPE_HIDE:
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        if iPlayer not in self.m_Data:
            return None
        dHasToHidHero[iHero] = 1
        oPetCon = oHero.m_PetCon
        if oPetCon.m_CurPet == oPetCon.m_CompanionPet:
            self.m_Data[iPlayer]['CarryPetLevelNum'] += 1

    
    def OnLevelStart(self, oWarMgr, dMsgInfo):
        if dMsgInfo['LevelType'] == LEVEL_TYPE_HALL:
            return None
        bIsHide = dMsgInfo['LevelType'] == LEVEL_TYPE_HIDE
        if not bIsHide:
            self.m_HasToHidHero = { }
        oGame = oWarMgr.m_Game
        for iPlayer, iHero in self.m_HasCompanionPet.items():
            self.m_Data[iPlayer]['TotalLevelNum'] += 1
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            oPetCon = oHero.m_PetCon
            if oPetCon.m_CurPet == oPetCon.m_CompanionPet and not bIsHide:
                self.m_Data[iPlayer]['CarryPetLevelNum'] += 1
        

    
    def OnRapidScreen(self, oWarMgr, oHero, dInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        self.m_Data[iPlayer]['RapidScreen'] += 1



class CConquerAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super().__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Flag = 'BigDataAnalyse_Conquer'
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.OnChallengeStart, self.m_Flag, CONQUER_CHALLENGE_START, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.OnChallengeReward, self.m_Flag, CONQUER_CHALLENGE_REWARD, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.OnMonsterWeakStart, self.m_Flag, CONQUER_MONSTER_WEAK_START, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.OnMonsterWeakEnd, self.m_Flag, CONQUER_MONSTER_WEAK_END, 0)

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Flag, CONQUER_CHALLENGE_START)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Flag, CONQUER_CHALLENGE_REWARD)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Flag, CONQUER_MONSTER_WEAK_START)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CONQUERCHALLENGE, self.m_Flag, CONQUER_MONSTER_WEAK_END)
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def GetStatistics(self, pid):
        if IsValidStats(self.m_WarMgr, pid):
            return self.m_Data
        return { }

    
    def GetLevelStatistics(self, pid, iLevel):
        if IsValidStats(self.m_WarMgr, pid):
            dData = self.PreLevelStatistics(pid, iLevel)
            self.m_Data = { }
            return dData
        return { }

    
    def PreLevelStatistics(self, pid, iLevel):
        if 'level' not in self.m_Data or iLevel != self.m_Data['level']:
            return { }
        dData = { }
        lstTeammate = []
        iSubdueTimes = 0
        iDeath = 0
        for iPlayerID, dPlayerData in self.m_Data['player_data'].items():
            if iPlayerID == pid:
                iSubdueTimes = dPlayerData['subdue_times']
                iDeath = dPlayerData['death']
                continue
            lstTeammate.append(dPlayerData)
        
        dData['subdue_times'] = iSubdueTimes
        dData['death'] = iDeath
        dData['teammate'] = lstTeammate
        dData['monster_sid'] = self.m_Data['monster_sid']
        dData['if_special'] = self.m_Data['if_special']
        dData['weak_num'] = self.m_Data['weak_num']
        dData['first_weak_time'] = self.m_Data['first_weak_time']
        dData['avg_weak_time'] = self.m_Data['avg_weak_time']
        dData['challenge_result'] = self.m_Data['challenge_result']
        return dData

    
    def InitEvent(self):
        oWarMgr = self.m_WarMgr
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_START_CONQUER, self.OnStartConquer, self.m_Flag)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, self.m_Flag)
        

    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_START_CONQUER, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.m_Flag)
        

    
    def OnChallengeStart(self, oWarMgr, dInfo):
        self.InitEvent()
        self.m_CurLevel = dInfo['Level']
        dPlayerData = { }
        for iHero in self.m_WarMgr.GetAllHero():
            iPlayerID = self.m_WarMgr.GetPlayerIDByHeroID(iHero)
            dPlayerData[iPlayerID] = {
                'uid': self.m_WarMgr.GetPlayerAccount(iPlayerID),
                'subdue_times': 0,
                'death': 0 }
        
        self.m_Data = {
            'level': dInfo['Level'],
            'monster_sid': dInfo['MonsterSID'],
            'if_special': 1 if dInfo['PlusLevel'] else 0,
            'weak_num': 0,
            'first_weak_time': 0,
            'avg_weak_time': 0,
            'weak_timer': self.m_Game.GetFrameNum(),
            'challenge_result': 0,
            'player_data': dPlayerData }

    
    def OnChallengeReward(self, oWarMgr, dInfo):
        self.ReleaseEvent()
        self.m_Data['challenge_result'] = 1

    
    def OnMonsterWeakStart(self, oWarMgr, dInfo):
        if dInfo['IsContinue']:
            return None
        if 'weak_num' not in self.m_Data:
            return None
        iWeakNum = self.m_Data['weak_num']
        fTime = Frame2Time(self.m_Game.GetFrameNum() - self.m_Data['weak_timer']) / 100
        if iWeakNum <= 0:
            self.m_Data['first_weak_time'] = fTime
        else:
            fAvgWeakTime = self.m_Data['avg_weak_time']
            fTotalTime = fAvgWeakTime * (iWeakNum - 1) + fTime
            self.m_Data['avg_weak_time'] = fTotalTime / iWeakNum
        self.m_Data['weak_num'] = iWeakNum + 1

    
    def OnMonsterWeakEnd(self, oWarMgr, dInfo):
        if 'weak_timer' not in self.m_Data:
            return None
        self.m_Data['weak_timer'] = self.m_Game.GetFrameNum()

    
    def OnStartConquer(self, oWarMgr, oHero, dMsgInfo):
        if 'player_data' not in self.m_Data:
            return None
        dPlayerData = self.m_Data['player_data']
        iPlayerID = oHero.m_PlayerID
        if iPlayerID not in dPlayerData:
            return None
        dData = dPlayerData[iPlayerID]
        dData['subdue_times'] += 1

    
    def OnHeroDie(self, oWarMgr, oHero, dMsgInfo):
        if 'player_data' not in self.m_Data:
            return None
        dPlayerData = self.m_Data['player_data']
        iPlayerID = oHero.m_PlayerID
        if iPlayerID not in dPlayerData:
            return None
        dData = dPlayerData[iPlayerID]
        dData['death'] += 1



class CSpecialHeroSkillCom(CBaseAnalyseCom):
    m_Flag = 'BigDataAnalyse_SpecialHero'
    m_Hero = 218
    m_Skill = (1324, 1328)
    
    def __init__(self, oGame):
        super(CSpecialHeroSkillCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_CanSend = False
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def GetStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            self.m_Data[pid]['FirstHall'] = oLevelCtrl.CheckFirstHall()
            return self.m_Data[pid]
        return { }

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if oHero.m_SID != self.m_Hero:
                continue
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = self.GetInitData(iLayer = 0)
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PERFORM_END, self.OnUseSkill, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PERFORM_HALT, self.OnUseSkill, self.m_Flag)
        

    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        for iHero in oWarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PERFORM_END, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PERFORM_HALT, self.m_Flag)
        

    
    def GetInitData(self, iLayer):
        dInitData = {
            'Layer': iLayer,
            'FailNum': 0,
            'SuccessNum': 0,
            'IntensifyNum': 0 }
        return dInitData

    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        iLayer = dInfo['Layer']
        self.m_CanSend = False
        for iPlayer in self.m_Data:
            self.m_Data[iPlayer] = self.GetInitData(iLayer)
        

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    
    def OnUseSkill(self, oWarMgr, iHero, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        if iPerform not in self.m_Skill:
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero.m_ID)
        if iPlayer not in self.m_Data:
            return None
        iMode = oSkill.m_CacheData.GetPerformMode()
        if iMode == 0:
            self.m_Data[iPlayer]['FailNum'] += 1
        elif iMode == 1:
            self.m_Data[iPlayer]['IntensifyNum'] += 1
        elif iMode == 2:
            self.m_Data[iPlayer]['SuccessNum'] += 1

    
    def OnPlayerLevelGame(self, oWarMgr, dInfo):
        self.m_CanSend = True



class CSeasonSuitAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super().__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_LevelData = { }
        self.m_CustomSuitTempNum = { }
        self.m_Flag = 'BigDataAnalyse_SeasonSuit'
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, self.OnLevelNodeFinishBefore, self.m_Flag, iSub = -1, iOnce = 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, self.m_Flag)
        self.m_Game = None
        self.m_WarMgr = None

    
    def Save(self):
        dData = {
            'SC': self.m_Data,
            'SI': self.m_LevelData }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData.get('SC', { })
            self.m_LevelData = dData.get('SI', { })

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            return self.m_Data[pid]
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)
    
    def GetLevelStatistics(self, pid):
        if pid in self.m_Data:
            dData = self.m_Data[pid]
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            if oLevelCtrl.CheckFirstHall() and pid in self.m_LevelData:
                dFirstHall = {
                    'SeasonSuitTemp': self.m_LevelData[pid] }
                dFirstHall.update(dData)
                return dFirstHall
            return dData
        return { }

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = { })(GetLevelStatistics)
    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        dPlayerInfo = dInfo['CreateInfo']
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer in self.m_LevelData:
                continue
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                dSeasonSuit = dPlayerInfo.get(iPlayer, { }).get('SeasonSuit', { })
                if dSeasonSuit:
                    self.m_CustomSuitTempNum[iPlayer] = len(dSeasonSuit['CustomSuitTemp'])
                self.m_LevelData[iPlayer] = {
                    'season_lv': oHero.Query('SeasonLevel', 0) }
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def OnLevelNodeFinishBefore(self, oWarMgr, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        for iHero in oWarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'suit_info': {
                        'info': self.GetInitSuitInfo(oHero) } }
            else:
                self.m_Data[iPlayer]['suit_info']['info'] = self.GetInitSuitInfo(oHero)
            if oLevelCtrl.CheckFirstHall():
                self.GetSuitTempInfo(iPlayer)
        

    OnLevelNodeFinishBefore = CheckFaultTolerance(OnLevelNodeFinishBefore)
    
    def GetSuitTempInfo(self, iPlayer):
        oSeasonSuitElement = self.m_WarMgr.GetSeasonSuitElement()
        if not oSeasonSuitElement:
            return None
        dSeasonSuitTemplate = cl_platformdata.GetSeasonSuitTemplate()
        dSuitTempInfo = oSeasonSuitElement.GetSuitTemp(iPlayer)
        if not dSuitTempInfo:
            return None
        iTempID = list(dSuitTempInfo)[0]
        lstSuitTemp = dSuitTempInfo[iTempID]
        lstCurCardPackPerform = oSeasonSuitElement.GetCurCardPackPerform(iPlayer)
        iChooseTemp = 0
        if iTempID in dSeasonSuitTemplate:
            iChooseTemp = 1
        dSuitTempInfo = {
            'template_choice': iTempID if iChooseTemp else 0,
            'suit_choice': lstSuitTemp if not iChooseTemp else [
                0],
            'custom_suit': self.m_CustomSuitTempNum.get(iPlayer, 0),
            'suit_type': lstCurCardPackPerform[0] if lstCurCardPackPerform else 0 }
        self.m_LevelData[iPlayer].update(dSuitTempInfo)

    GetSuitTempInfo = CheckFaultTolerance(GetSuitTempInfo)
    
    def GetInitSuitInfo(self, oHero):
        oSeasonSuitElement = self.m_WarMgr.GetSeasonSuitElement()
        if not oSeasonSuitElement:
            return []
        dGrade = oSeasonSuitElement.GetAllSuitGradeInfo(oHero.m_ID)
        lstAllInfo = []
        for iSuit, iLv in dGrade.items():
            if iLv <= 0:
                continue
            iSuitOpenStatus = oSeasonSuitElement.GetSuitOpenStatus(oHero, iSuit)
            dSeasonSuitInfo = {
                'id': iSuit,
                'level': iLv,
                'status': iSuitOpenStatus }
            lstAllInfo.append(dSeasonSuitInfo)
        
        return lstAllInfo

    GetInitSuitInfo = CheckFaultToleranceWithDefault(Default = [])(GetInitSuitInfo)


class CRelicActivityAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super().__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_AddRelicInfo = { }
        self.m_LotteryInfo = { }
        self.m_FusionSuitInfo = { }
        self.m_Flag = 'BigDataAnalyse_RelicActivity'
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, iSub = -1, iOnce = 0)

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in oWarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELIC, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_FUSEDRELIC, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DONEREWARD_RELICLOTTERY, self.m_Flag)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_REDUCE_SUITCONDITION, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    
    def Save(self):
        dData = {
            'RLI': self.m_Data,
            'ARI': self.m_AddRelicInfo,
            'LI': self.m_LotteryInfo,
            'FSI': self.m_FusionSuitInfo }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData.get('RLI', { })
            self.m_AddRelicInfo = dData.get('ARI', { })
            self.m_LotteryInfo = dData.get('LI', { })
            self.m_FusionSuitInfo = dData.get('FSI', { })

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            if pid in self.m_AddRelicInfo:
                lstAddRelicInfo = list(self.m_AddRelicInfo[pid].values())
                self.m_Data[pid]['relic_info']['item'].extend(lstAddRelicInfo)
            if pid in self.m_LotteryInfo:
                lstLotteryInfo = list(self.m_LotteryInfo[pid].values())
                self.m_Data[pid]['draw_info']['item'] = lstLotteryInfo
            if pid in self.m_FusionSuitInfo:
                lstFusionSuitInfo = list(self.m_FusionSuitInfo[pid])
                self.m_Data[pid]['fusion_suit'] = lstFusionSuitInfo
            return self.m_Data[pid]
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)
    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELIC, self.OnAddRelic, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_FUSEDRELIC, self.OnFuseRelic, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DONEREWARD_RELICLOTTERY, self.OnDoneReward, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_REDUCE_SUITCONDITION, self.OnReduceSuitCondition, self.m_Flag)
                self.m_AddRelicInfo[iPlayer] = { }
                self.m_LotteryInfo[iPlayer] = { }
                self.m_FusionSuitInfo[iPlayer] = { }
                self.m_Data[iPlayer] = {
                    'relic_info': {
                        'item': [] },
                    'draw_info': {
                        'item': [] } }
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def OnAddRelic(self, oWarMgr, oHero, dInfo):
        iRelic = dInfo['iPerform'] if 'iPerform' in dInfo else 0
        if not iRelic:
            return None
        if dInfo['Reason'] == RELIC_RS_LOAD:
            return None
        clsRelic = cl_perform.GetPerformModule(iRelic)
        if not clsRelic:
            return None
        dRelicInfo = {
            'id': iRelic,
            'type': TYPE_INIT,
            'lv': dInfo['Level'],
            'quality': clsRelic.m_Quality }
        self.m_AddRelicInfo[oHero.m_PlayerID][iRelic] = dRelicInfo

    OnAddRelic = CheckFaultTolerance(OnAddRelic)
    
    def OnFuseRelic(self, oWarMgr, oHero, dInfo):
        lstCostRelic = dInfo['CostRelic']
        self.AddRelicRecord(oWarMgr, oHero, lstCostRelic, TYPE_TO_FUSE)

    OnFuseRelic = CheckFaultTolerance(OnFuseRelic)
    
    def OnDoneReward(self, oWarMgr, oHero, dInfo):
        lstCostRelic = [
            dInfo['CostRelic']]
        self.AddRelicRecord(oWarMgr, oHero, lstCostRelic, TYPE_TO_LOTTERY)
        lstReward = []
        dRewardRecord = dInfo['HeroRecord']
        for iReward, _, _ in dRewardRecord:
            lstReward.append(iReward)
        
        dDrawInfo = {
            'num': len(lstReward),
            'if_shut': dInfo['IsClose'],
            'reward': lstReward }
        self.m_LotteryInfo[oHero.m_PlayerID][dInfo['Npc']] = dDrawInfo

    OnDoneReward = CheckFaultTolerance(OnDoneReward)
    
    def AddRelicRecord(self, oWarMgr, oHero, lstCostRelic, iType):
        if not lstCostRelic:
            return None
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_AddRelicInfo:
            return None
        dAddRelicInfo = self.m_AddRelicInfo[iPlayer]
        for iCostRelic in lstCostRelic:
            if iCostRelic not in dAddRelicInfo:
                continue
            dRelicInfo = dAddRelicInfo.pop(iCostRelic)
            dRelicInfo['type'] = iType
            self.m_Data[iPlayer]['relic_info']['item'].append(dRelicInfo)
        

    AddRelicRecord = CheckFaultTolerance(AddRelicRecord)
    
    def OnReduceSuitCondition(self, oWarMgr, oHero, dInfo):
        if dInfo['Reason'] == 'InitChosen':
            return None
        iPlayer = oHero.m_PlayerID
        iFuseSuit = dInfo['Suit']
        self.m_FusionSuitInfo[iPlayer][iFuseSuit] = 1

    OnReduceSuitCondition = CheckFaultTolerance(OnReduceSuitCondition)


class CInscriptionAnalyseCom(CBaseAnalyseCom):
    m_Flag = 'BigDataAnalyse_Inscription'
    
    def __init__(self, oGame):
        super().__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_Upgrade = { }
        self.m_Weapon = { }
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def Save(self):
        return { }

    
    def Load(self, dData):
        pass

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            return self.m_Data[pid]
        return { }

    
    def InitEvent(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iSub = -1, iOnce = 0)

    InitEvent = CheckFaultTolerance(InitEvent)
    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        for iHero in oWarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADE_INSCRIPTION, self.m_Flag)
        

    ReleaseEvent = CheckFaultTolerance(ReleaseEvent)
    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero:
                continue
            pid = oHero.m_PlayerID
            if pid in self.m_Data:
                continue
            self.m_Data[pid] = []
            self.RefreshWeapon(oHero)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADE_INSCRIPTION, self.OnUpgradeInscription, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def AddReplaceWeaponRecord(self, pid, iOldWeaponSID, iNewWeaponSID):
        if pid not in self.m_Data:
            return None
        self.m_Data[pid].append({
            'replace_weapon': iOldWeaponSID,
            'weapon_id': iNewWeaponSID,
            'replace_inscription': 0,
            'replace_type': 0 })

    AddReplaceWeaponRecord = CheckFaultTolerance(AddReplaceWeaponRecord)
    
    def AddReplaceInscriptionRecord(self, pid, iWeaponSID, iInsSID, iType):
        if pid not in self.m_Data:
            return None
        self.m_Data[pid].append({
            'replace_weapon': 0,
            'weapon_id': iWeaponSID,
            'replace_inscription': iInsSID,
            'replace_type': iType })

    AddReplaceInscriptionRecord = CheckFaultTolerance(AddReplaceInscriptionRecord)
    
    def OnUpgradeInscription(self, _oWarmgr, oHero, dMsgInfo):
        iItem = dMsgInfo['ItemID']
        oWeapon = oHero.m_WieldCon.GetItemByID(iItem)
        if not oWeapon:
            return None
        dUpgrade = self.m_Upgrade.setdefault(oHero.m_PlayerID, { })
        dWeaponUpgrade = dUpgrade.setdefault(iItem, { })
        for iInscription in dMsgInfo['OldInscription']:
            iType = 0
            if dMsgInfo['Reason'] == UPGRADE_INS_RS_TASK:
                iType = 1
                self.AddReplaceInscriptionRecord(oHero.m_PlayerID, oWeapon.m_SID, iInscription, iType)
            if iInscription not in dWeaponUpgrade:
                dWeaponUpgrade[iInscription] = iType
        

    OnUpgradeInscription = CheckFaultTolerance(OnUpgradeInscription)
    
    def UpdateWeaponInscription(self, pid, iWeapon, iWeaponSID, setInscription):
        dUpgrade = self.m_Upgrade[pid] if pid in self.m_Upgrade else { }
        dWeaponUpgrade = dUpgrade[iWeapon] if iWeapon in dUpgrade else { }
        for iInscription in setInscription:
            if iInscription in dWeaponUpgrade and dWeaponUpgrade[iInscription]:
                continue
            self.AddReplaceInscriptionRecord(pid, iWeaponSID, iInscription, 0)
        

    UpdateWeaponInscription = CheckFaultTolerance(UpdateWeaponInscription)
    
    def OnLevelNodeInit(self, _oWarMgr, dMsgInfo):
        if dMsgInfo['LevelType'] == LEVEL_TYPE_HIDE:
            return None
        for lstData in self.m_Data.values():
            lstData.clear()
        

    OnLevelNodeInit = CheckFaultTolerance(OnLevelNodeInit)
    
    def OnLevelNodeFinish(self, _oWarMgr, _dMsgInfo):
        for pid in self.m_Data:
            self.RefreshInfo(pid)
        

    OnLevelNodeFinish = CheckFaultTolerance(OnLevelNodeFinish)
    
    def OnPlayerLevelGame(self, _oWarMgr, dMsgInfo):
        self.RefreshInfo(dMsgInfo['pid'])

    OnPlayerLevelGame = CheckFaultTolerance(OnPlayerLevelGame)
    
    def RefreshInfo(self, pid):
        oHero = self.m_WarMgr.GetHeroByPlayer(pid)
        if not oHero:
            return None
        dOldWeapon = dict(self.m_Weapon[pid])
        dNewWeapon = dict(self.RefreshWeapon(oHero))
        lstWeapon = list(dOldWeapon)
        for iWeapon in lstWeapon:
            if iWeapon in dNewWeapon:
                dOld = dOldWeapon.pop(iWeapon)
                dNew = dNewWeapon.pop(iWeapon)
                setChange = dOld['Inscription'] - dNew['Inscription']
                self.UpdateWeaponInscription(pid, iWeapon, dNew['SID'], setChange)
        
        if dOldWeapon:
            lstOldWeapon = list(dOldWeapon)
            lstNewWeapon = list(dNewWeapon)
            for iOldWeapon in lstOldWeapon:
                dOld = dOldWeapon[iOldWeapon]
                for iNewWeapon in lstNewWeapon:
                    dNew = dNewWeapon[iNewWeapon]
                    if dOld['SID'] == dNew['SID']:
                        dOldWeapon.pop(iOldWeapon)
                        dNewWeapon.pop(iNewWeapon)
                        setChange = dOld['Inscription'] - dNew['Inscription']
                        self.UpdateWeaponInscription(pid, iOldWeapon, dOld['SID'], setChange)
                        lstNewWeapon = list(dNewWeapon)
                        break
                
            
        if dOldWeapon:
            lstOldWeapon = list(dOldWeapon)
            lstNewWeapon = list(dNewWeapon)
            lstOldWeapon.sort(key = (lambda x: dOldWeapon[x]['Pos']))
            lstNewWeapon.sort(key = (lambda x: dNewWeapon[x]['Pos']))
            for idx, iOldWeapon in enumerate(lstOldWeapon):
                if idx < len(lstNewWeapon):
                    iNewWeapon = lstNewWeapon[idx]
                    iNewWeaponSID = dNewWeapon[iNewWeapon]['SID']
                else:
                    iNewWeaponSID = 0
                self.AddReplaceWeaponRecord(pid, dOldWeapon[iOldWeapon]['SID'], iNewWeaponSID)
            
        self.m_Upgrade[pid] = { }

    RefreshInfo = CheckFaultTolerance(RefreshInfo)
    
    def RefreshWeapon(self, oHero):
        dWeapon = { }
        for oWeapon in oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON):
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            dWeapon[oWeapon.m_ID] = {
                'SID': oWeapon.m_SID,
                'Inscription': set(oInscriptionCom.GetAllInscription(iFill = 0, iIgnoreDisable = 0) if oInscriptionCom else []),
                'Pos': oWeapon.m_Pos }
        
        self.m_Weapon[oHero.m_PlayerID] = dWeapon
        return dWeapon

    RefreshWeapon = CheckFaultTolerance(RefreshWeapon)


class CTokenAttackAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CTokenAttackAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_TokenAttack'
        self.m_BeneInfo = { }
        self.m_CurLayer = 0
        self.m_SeasonLv = { }
        self.m_CanSend = False
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                oHero = self.m_Game.GetObject(iHero)
                self.m_SeasonLv[iPlayer] = oHero.Query('SeasonLevel', 0)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEBENED, self.OnRemoveBene, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDBENED, self.OnAddBene, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WAND, self.OnWandTrigger, self.m_Flag, WAND_SUBMSG_TRIGGERACTION)
                self.m_Data[iPlayer] = { }
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVEBENED, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ADDBENED, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WAND, self.m_Flag, WAND_SUBMSG_TRIGGERACTION)
        
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.m_Flag)
        self.m_Game = None
        self.m_WarMgr = None

    
    def OnRemoveBene(self, oWarMgr, oHero, dMsgInfo):
        iBene = dMsgInfo['Bene']
        iHero = oHero.m_ID
        iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
        lstBene = self.m_BeneInfo.setdefault(iPlayer, [])
        if iBene not in lstBene:
            return None
        lstBene.remove(iBene)

    OnRemoveBene = CheckFaultTolerance(OnRemoveBene)
    
    def OnAddBene(self, oWarMgr, oHero, dMsgInfo):
        iBene = dMsgInfo['Bene']
        iHero = oHero.m_ID
        iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
        lstBene = self.m_BeneInfo.setdefault(iPlayer, [])
        if iBene in lstBene:
            return None
        lstBene.append(iBene)

    OnAddBene = CheckFaultTolerance(OnAddBene)
    
    def OnWandTrigger(self, oWarMgr, oHero, dMsgInfo):
        iWandSID = dMsgInfo['WandSID']
        lstTag = dMsgInfo['WandTag']
        iHero = oHero.m_ID
        iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
        dWandTriggerInfo = self.m_Data.setdefault(iPlayer, { })
        if iWandSID not in dWandTriggerInfo:
            dWandTriggerInfo[iWandSID] = {
                'token_id': iWandSID,
                'token_type': lstTag,
                'attack_num': 1 }
        else:
            dWandTriggerInfo[iWandSID]['attack_num'] += 1

    OnWandTrigger = CheckFaultTolerance(OnWandTrigger)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dMsgInfo):
        self.m_CurLayer = dMsgInfo['Layer']
        self.m_CanSend = False
        for iPlayer in self.m_Data:
            self.m_Data[iPlayer] = { }
        

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'CL': self.m_CurLayer,
            'BI': DeepCopy(self.m_BeneInfo),
            'SL': DeepCopy(self.m_SeasonLv) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_BeneInfo = dData['BI']
            self.m_CurLayer = dData['CL']
            self.m_SeasonLv = dData['SL']

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            dData = self.m_Data[pid]
            lstData = []
            for dCustomData in dData.values():
                dOtherData = {
                    'season_lv': self.m_SeasonLv[pid],
                    'seanson_lingyou': self.m_BeneInfo[pid] if pid in self.m_BeneInfo else [],
                    'layer': self.m_CurLayer }
                dOtherData.update(dCustomData)
                lstData.append(dOtherData)
            
            return lstData
        return []

    GetStatistics = CheckFaultToleranceWithDefault(Default = [])(GetStatistics)
    
    def GetLevelStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = self.m_Data[pid]
            lstData = []
            for dCustomData in dData.values():
                dOtherData = {
                    'season_lv': self.m_SeasonLv[pid],
                    'seanson_lingyou': self.m_BeneInfo[pid] if pid in self.m_BeneInfo else [],
                    'layer': self.m_CurLayer }
                dOtherData.update(dCustomData)
                lstData.append(dOtherData)
            
            return lstData
        return []

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = [])(GetLevelStatistics)


class CTokenFirstOpportunityAnalyseCom(CBaseAnalyseCom):
    FIRST_GET_RAREWAND = 1
    FIRST_GET_TALEWAND = 2
    FIRST_EQUIP_WANDCOMP = 3
    FIRST_SWITCH_OTHER_WAND = 4
    
    def __init__(self, oGame):
        super(CTokenFirstOpportunityAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_TokenFirstOpporuntity'
        self.m_FirstRecord = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCHANGE, self.OnWandChange, self.m_Flag, WAND_SUBMSG_ADD)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCHANGE, self.OnWandChange, self.m_Flag, WAND_SUBMSG_UPGRADE)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.OnWandEnable, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.OnAddWandComp, self.m_Flag, WANDCOMP_SUBMSG_ADD)
                self.m_Data[iPlayer] = { }
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCHANGE, self.m_Flag, WAND_SUBMSG_ADD)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCHANGE, self.m_Flag, WAND_SUBMSG_UPGRADE)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.m_Flag, WANDCOMP_SUBMSG_ADD)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def OnWandChange(self, oWarMgr, oHero, dMsgInfo):
        iQuality = dMsgInfo['Quality']
        if iQuality == WAND_QUALITY_RARE:
            iTokenType = self.FIRST_GET_RAREWAND
        elif iQuality == WAND_QUALITY_TALE:
            iTokenType = self.FIRST_GET_TALEWAND
        else:
            return None
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelNum = oLevelCtrl.m_LevelNum
        iLayer = oLevelCtrl.m_LayerNum
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        lstFirstRecord = self.m_FirstRecord.setdefault(iPlayer, [])
        if iTokenType not in lstFirstRecord:
            lstFirstRecord.append(iTokenType)
            dData = self.m_Data.setdefault(iPlayer, { })
            dData[iTokenType] = {
                'info_type': iTokenType,
                'layer': iLayer,
                'stage_num': iLevelNum }
        if self.FIRST_GET_RAREWAND in lstFirstRecord and self.FIRST_GET_TALEWAND in lstFirstRecord:
            cl_msgcenter.DoneAttention(self.m_WarMgr, oHero.m_ID, cl_msgcenter.MSG_WAR_WANDCHANGE, self.m_Flag, WAND_SUBMSG_ADD)
            cl_msgcenter.DoneAttention(self.m_WarMgr, oHero.m_ID, cl_msgcenter.MSG_WAR_WANDCHANGE, self.m_Flag, WAND_SUBMSG_UPGRADE)

    OnWandChange = CheckFaultTolerance(OnWandChange)
    
    def OnWandEnable(self, oWarMgr, oHero, dMsgInfo):
        if 'LastWand' not in dMsgInfo or dMsgInfo['LastWand'] != FUNDAMENTAL_WAND:
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLevelNum = oLevelCtrl.m_LevelNum
        iLayer = oLevelCtrl.m_LayerNum
        lstFirstRecord = self.m_FirstRecord.setdefault(iPlayer, [])
        if self.FIRST_SWITCH_OTHER_WAND in lstFirstRecord:
            cl_msgcenter.DoneAttention(self.m_WarMgr, oHero.m_ID, cl_msgcenter.MSG_WAR_WANDENABLE, self.m_Flag)
            return None
        lstFirstRecord.append(self.FIRST_SWITCH_OTHER_WAND)
        dData = self.m_Data.setdefault(iPlayer, { })
        dData[self.FIRST_SWITCH_OTHER_WAND] = {
            'info_type': self.FIRST_SWITCH_OTHER_WAND,
            'layer': iLayer,
            'stage_num': iLevelNum }
        cl_msgcenter.DoneAttention(self.m_WarMgr, oHero.m_ID, cl_msgcenter.MSG_WAR_WANDENABLE, self.m_Flag)

    OnWandEnable = CheckFaultTolerance(OnWandEnable)
    
    def OnAddWandComp(self, oWarMgr, oHero, dMsgInfo):
        sReason = dMsgInfo['Reason']
        if sReason == 'init':
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum
        iLevelNum = oLevelCtrl.m_LevelNum
        lstFirstRecord = self.m_FirstRecord.setdefault(iPlayer, [])
        if self.FIRST_EQUIP_WANDCOMP in lstFirstRecord:
            cl_msgcenter.DoneAttention(self.m_WarMgr, oHero.m_ID, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.m_Flag, WANDCOMP_SUBMSG_ADD)
            return None
        lstFirstRecord.append(self.FIRST_EQUIP_WANDCOMP)
        dData = self.m_Data.setdefault(iPlayer, { })
        dData[self.FIRST_EQUIP_WANDCOMP] = {
            'info_type': self.FIRST_EQUIP_WANDCOMP,
            'layer': iLayer,
            'stage_num': iLevelNum }
        cl_msgcenter.DoneAttention(self.m_WarMgr, oHero.m_ID, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.m_Flag, WANDCOMP_SUBMSG_ADD)

    OnAddWandComp = CheckFaultTolerance(OnAddWandComp)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'FR': DeepCopy(self.m_FirstRecord) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_FirstRecord = dData['FR']

    
    def GetStatistics(self, pid):
        if pid in self.m_Data and self.m_Data[pid]:
            dData = self.m_Data[pid]
            lstData = []
            for dCustomData in dData.values():
                lstData.append(dCustomData)
            
            self.m_Data[pid] = { }
            return lstData
        return []

    GetStatistics = CheckFaultToleranceWithDefault(Default = [])(GetStatistics)


class CWeaponTokenAnalyseCom(CBaseAnalyseCom):
    SPECIAL_TOKEN = (1013, 1018, 1019)
    
    def __init__(self, oGame):
        super(CWeaponTokenAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_WeaponTokenAnalyse'
        self.m_Token = { }
        self.m_KillBossFlag = False
        self.m_RecordState = True
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.OnLevelGoal, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                oHero = self.m_Game.GetObject(iHero)
                self.m_Data[iPlayer] = {
                    'weapon_id': 1202,
                    'season_lv': oHero.Query('SeasonLevel', 0) }
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.OnWandEnable, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDDISABLE, self.OnWandDisable, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.OnHoldWeapon, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDDISABLE, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def OnWandEnable(self, oWarMgr, oHero, dMsgInfo):
        iWandSID = dMsgInfo['WandSID']
        if iWandSID not in self.SPECIAL_TOKEN:
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        self.m_Token[iPlayer] = iWandSID

    OnWandEnable = CheckFaultTolerance(OnWandEnable)
    
    def OnWandDisable(self, oWarMgr, oHero, dMsgInfo):
        iWandSID = dMsgInfo['WandSID']
        if iWandSID not in self.SPECIAL_TOKEN:
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        if iPlayer not in self.m_Token:
            return None
        self.m_Token.pop(iPlayer)

    OnWandDisable = CheckFaultTolerance(OnWandDisable)
    
    def OnHoldWeapon(self, oWarMgr, oHero, dMsgInfo):
        iItemSID = dMsgInfo['ItemSID']
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        dData = self.m_Data.setdefault(iPlayer, { })
        dData['weapon_id'] = iItemSID

    OnHoldWeapon = CheckFaultTolerance(OnHoldWeapon)
    
    def OnLevelGoal(self, oWarMgr, oLevelCtrl, dMsgInfo):
        iLevel = dMsgInfo['Level']
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS and oLevelCtrl.m_LayerNum == MAX_LAYER:
            self.m_KillBossFlag = True
            cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.m_Flag)

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'TK': DeepCopy(self.m_Token),
            'KBF': self.m_KillBossFlag,
            'RS': self.m_RecordState }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_Token = dData['TK']
            self.m_KillBossFlag = dData['KBF']
            self.m_RecordState = dData['RS']

    
    def GetStatistics(self, pid):
        if self.m_RecordState and pid in self.m_Token:
            dData = {
                'token_id': self.m_Token[pid] }
            if self.m_KillBossFlag:
                dData['KillBossFlag'] = 1
                self.m_RecordState = False
            dData.update(self.m_Data[pid])
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CBuyAmplifierAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CBuyAmplifierAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_BuyAmplifier'
        self.m_CurWandShopGoods = { }
        self.m_CanSend = False
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateNpc, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                oHero = self.m_Game.GetObject(iHero)
                self.m_CurWandShopGoods[iPlayer] = { }
                self.m_Data[iPlayer] = {
                    'season_lv': oHero.Query('SeasonLevel', 0),
                    'amplifier': {
                        'item': [] } }
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP, self.OnInitGoods, self.m_Flag, WANDSHOP_INITGOODS)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP, self.OnRefreshGoods, self.m_Flag, WANDSHOP_REFRESHGOODS)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP_BUY, self.OnBuyGoods, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP, self.m_Flag, WANDSHOP_INITGOODS)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP, self.m_Flag, WANDSHOP_REFRESHGOODS)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP_BUY, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def UpdateCurShopGoods(self, iPlayer, dWandCompGoods = None):
        dGoodsInfo = { }
        if dWandCompGoods is None:
            return dGoodsInfo
        for iRarity, dCompData in dWandCompGoods.items():
            for iCompSID in dCompData:
                dGoodsInfo[(iCompSID, iRarity)] = 0
            
        
        self.m_CurWandShopGoods[iPlayer] = dGoodsInfo

    UpdateCurShopGoods = CheckFaultTolerance(UpdateCurShopGoods)
    
    def CollectShopGoodsData(self, iPlayer):
        for tGoodsInfo, iBuyState in self.m_CurWandShopGoods[iPlayer].items():
            lstItems = self.m_Data[iPlayer]['amplifier']['item']
            (iCompSID, iRarity) = tGoodsInfo
            dItemInfo = {
                'id': iCompSID,
                'type': iRarity,
                'if_buy': iBuyState }
            lstItems.append(dItemInfo)
        

    CollectShopGoodsData = CheckFaultTolerance(CollectShopGoodsData)
    
    def OnInitGoods(self, oWarMgr, oHero, dMsgInfo):
        dWandCompGoods = dMsgInfo['WandComp']
        if not dWandCompGoods:
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        self.UpdateCurShopGoods(iPlayer, dWandCompGoods)

    OnInitGoods = CheckFaultTolerance(OnInitGoods)
    
    def OnRefreshGoods(self, oWarMgr, oHero, dMsgInfo):
        dWandCompGoods = dMsgInfo['WandComp']
        if not dWandCompGoods:
            return None
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        self.CollectShopGoodsData(iPlayer)
        self.UpdateCurShopGoods(iPlayer, dWandCompGoods)

    OnRefreshGoods = CheckFaultTolerance(OnRefreshGoods)
    
    def OnBuyGoods(self, oWarMgr, oHero, dMsgInfo):
        iItemType = dMsgInfo['ItemType']
        if iItemType != VIRTUAL_ITEM_WANDCOMP:
            return None
        iRarity = dMsgInfo['Rarity']
        iCompSID = dMsgInfo['ItemSID']
        tGoodsKey = (iCompSID, iRarity)
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        if tGoodsKey not in self.m_CurWandShopGoods[iPlayer]:
            return None
        self.m_CurWandShopGoods[iPlayer][tGoodsKey] = 1

    OnBuyGoods = CheckFaultTolerance(OnBuyGoods)
    
    def OnCreateNpc(self, oWarMgr, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_WANDSHOP:
            return None
        self.m_CanSend = True

    OnCreateNpc = CheckFaultTolerance(OnCreateNpc)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'NBSG': DeepCopy(self.m_CurWandShopGoods) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_CurWandShopGoods = dData['NBSG']

    
    def GetStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            self.CollectShopGoodsData(pid)
            dSendData = DeepCopy(self.m_Data[pid])
            self.m_Data[pid]['amplifier'] = {
                'item': [] }
            self.m_CurWandShopGoods[pid] = { }
            self.m_CanSend = False
            return dSendData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CTokenEquipAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CTokenEquipAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_TokenEquip'
        self.m_WandData = { }
        self.m_CurWand = { }
        self.m_CanSend = False
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                oHero = self.m_Game.GetObject(iHero)
                self.m_Data[iPlayer] = {
                    'season_lv': oHero.Query('SeasonLevel', 0),
                    'token_type': 0,
                    'layer': 0,
                    'equip_amplifier': [],
                    'equip_condition': [] }
                self.m_WandData[iPlayer] = { }
                self.m_CurWand[iPlayer] = 0
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.OnAddComp, self.m_Flag, WANDCOMP_SUBMSG_ADD)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.OnRemoveComp, self.m_Flag, WANDCOMP_SUBMSG_REMOVE)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.OnWandEnable, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDDISABLE, self.OnWandDisable, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.m_Flag, WANDCOMP_SUBMSG_ADD)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.m_Flag, WANDCOMP_SUBMSG_REMOVE)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDDISABLE, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dMsgInfo):
        iLayer = dMsgInfo['Layer']
        self.m_CanSend = False
        for iPlayer in self.m_Data:
            self.m_Data[iPlayer]['layer'] = iLayer
        

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnAddComp(self, oWarMgr, oHero, dMsgInfo):
        iWandCompSID = dMsgInfo['WandCompSID']
        iWandID = dMsgInfo['Wand']
        iWandCompType = dMsgInfo['CompType']
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        dWandInfo = self.m_WandData[iPlayer]
        dCompData = dWandInfo.setdefault(iWandID, { })
        if iWandCompType == WAND_COMP_TYPE_CONDITION:
            lstComp = dCompData.setdefault('equip_condition', [])
        elif iWandCompType == WAND_COMP_TYPE_ACTION:
            lstComp = dCompData.setdefault('equip_amplifier', [])
        else:
            return None
        lstComp.append(iWandCompSID)

    OnAddComp = CheckFaultTolerance(OnAddComp)
    
    def OnRemoveComp(self, oWarMgr, oHero, dMsgInfo):
        iWandCompSID = dMsgInfo['WandCompSID']
        iWandID = dMsgInfo['Wand']
        iWandCompType = dMsgInfo['CompType']
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        dWandInfo = self.m_WandData[iPlayer]
        dCompData = dWandInfo.setdefault(iWandID, { })
        if iWandCompType == WAND_COMP_TYPE_CONDITION:
            lstComp = dCompData.setdefault('equip_condition', [])
        elif iWandCompType == WAND_COMP_TYPE_ACTION:
            lstComp = dCompData.setdefault('equip_amplifier', [])
        else:
            return None
        if iWandCompSID not in lstComp:
            return None
        lstComp.remove(iWandCompSID)

    OnRemoveComp = CheckFaultTolerance(OnRemoveComp)
    
    def OnWandEnable(self, oWarMgr, oHero, dMsgInfo):
        iWandID = dMsgInfo['Wand']
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        self.m_CurWand[iPlayer] = iWandID
        dWandData = self.m_WandData[iPlayer]
        if iWandID not in dWandData:
            dWandData[iWandID] = {
                'token_type': dMsgInfo['WandTag'] }
        else:
            dWandData[iWandID]['token_type'] = dMsgInfo['WandTag']

    OnWandEnable = CheckFaultTolerance(OnWandEnable)
    
    def OnWandDisable(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        self.m_CurWand[iPlayer] = 0

    OnWandDisable = CheckFaultTolerance(OnWandDisable)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'CW': DeepCopy(self.m_CurWand),
            'WD': DeepCopy(self.m_WandData) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_WandData = dData['WD']
            self.m_CurWand = dData['CW']

    
    def GetStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = { }
            dData.update(self.m_Data[pid])
            dWandData = self.m_WandData[pid]
            iCurWand = self.m_CurWand[pid]
            if iCurWand in dWandData:
                dData.update(dWandData[iCurWand])
                return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CTokenStrengthenMonsterAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CTokenStrengthenMonsterAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_TokenStrengthenMonster'
        self.m_SeasonLv = { }
        self.m_CurLayer = 0
        self.m_CanSend = False
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                oHero = self.m_Game.GetObject(iHero)
                self.m_SeasonLv[iPlayer] = oHero.Query('SeasonLevel', 0)
                self.m_Data[iPlayer] = { }
            cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dMsgInfo):
        self.m_CurLayer = dMsgInfo['Layer']
        self.m_CanSend = False
        for iPlayer in self.m_Data:
            self.m_Data[iPlayer] = { }
        

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnDie(self, oWarMgr, oHero, dMsgInfo):
        iAttack = dMsgInfo['AID']
        oAttack = self.m_Game.GetObject(iAttack)
        if not oAttack:
            return None
        if not oAttack.m_FightType & WARRIOR_MONSTER:
            return None
        tMonsterSuperInfo = oAttack.Query('MonsterSuper')
        if not tMonsterSuperInfo:
            return None
        (_, iAfPF) = tMonsterSuperInfo
        if not iAfPF:
            return None
        dTag = GetMonsterAfTag()
        if MAF_TYPE_SEASONWAND not in dTag or iAfPF not in dTag[MAF_TYPE_SEASONWAND]:
            return None
        tKey = (oAttack.m_SID, iAfPF)
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        dDieRecord = self.m_Data.setdefault(iPlayer, { })
        if tKey not in dDieRecord:
            dDieRecord[tKey] = {
                'monster_id': oAttack.m_SID,
                'season_lv': self.m_SeasonLv[iPlayer] if iPlayer in self.m_SeasonLv else 0,
                'layer': self.m_CurLayer,
                'strengthen_id': iAfPF,
                'defeat_num': 1 }
        else:
            dDieRecord[tKey]['defeat_num'] += 1

    OnDie = CheckFaultTolerance(OnDie)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'SL': DeepCopy(self.m_SeasonLv) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_SeasonLv = dData['SL']

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            dData = self.m_Data[pid]
            lstData = []
            for dCustomData in dData.values():
                lstData.append(dCustomData)
            
            return lstData
        return []

    GetStatistics = CheckFaultToleranceWithDefault(Default = [])(GetStatistics)
    
    def GetLevelStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = self.m_Data[pid]
            lstData = []
            for dCustomData in dData.values():
                lstData.append(dCustomData)
            
            return lstData
        return []

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = [])(GetLevelStatistics)


class CTokenNpcCostAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CTokenNpcCostAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_TokenNpcCost'
        self.m_CanSend = False
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                oHero = self.m_Game.GetObject(iHero)
                self.m_Data[iPlayer] = {
                    'season_lv': oHero.Query('SeasonLevel', 0),
                    'layer': 0,
                    'coin_cost': 0 }
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP_BUY, self.OnBuyWandShopGoods, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        for iHero in self.m_WarMgr.GetAllHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP_BUY, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dMsgInfo):
        self.m_CanSend = False
        for iPlayer in self.m_Data:
            self.m_Data[iPlayer]['layer'] = dMsgInfo['Layer']
            self.m_Data[iPlayer]['coin_cost'] = 0
        

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnBuyWandShopGoods(self, oWarMgr, oHero, dMsgInfo):
        iCost = dMsgInfo['Cost']
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        dRecord = self.m_Data[iPlayer]
        dRecord['coin_cost'] += iCost

    OnBuyWandShopGoods = CheckFaultTolerance(OnBuyWandShopGoods)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']

    
    def GetStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            return self.m_Data[pid]
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CLevelTokenAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CLevelTokenAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_LevelToken'
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = 0
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.OnWandEnable, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDDISABLE, self.OnWandDisable, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDENABLE, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDDISABLE, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def OnWandEnable(self, oWarMgr, oHero, dMsgInfo):
        iWandSID = dMsgInfo['WandSID']
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        self.m_Data[iPlayer] = iWandSID

    OnWandEnable = CheckFaultTolerance(OnWandEnable)
    
    def OnWandDisable(self, oWarMgr, oHero, dMsgInfo):
        iPlayer = oWarMgr.GetPlayerIDByHeroID(oHero.m_ID)
        self.m_Data[iPlayer] = 0

    OnWandDisable = CheckFaultTolerance(OnWandDisable)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            return self.m_Data[pid]
        return 0

    GetStatistics = CheckFaultToleranceWithDefault(Default = 0)(GetStatistics)


class CTokenEntryAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CTokenEntryAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_TokenEntry'
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = { }
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_PLAYERLEVELREPORT_BEFORE, self.OnPlayerSettle, self.m_Flag)
                cl_msgcenter.AddAttentionFunc(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP_BEFORE_ROLL, self.OnShopNpcRollWand, self.m_Flag)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_PLAYERLEVELREPORT_BEFORE, self.m_Flag)
            cl_msgcenter.DoneAttention(self.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_WANDSHOP_BEFORE_ROLL, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def OnPlayerSettle(self, oWarMgr, oHero, dMsgInfo):
        oWandCon = oHero.m_WandCon
        if not oWandCon:
            return None
        dPlayerData = self.m_Data[oHero.m_PlayerID]
        oCurWand = oWandCon.GetCurWand()
        if not oCurWand:
            return None
        dPlayerData['token_id'] = oCurWand.m_SID
        dPlayerData['entry_list'] = list(oCurWand.m_WandAbility)

    OnPlayerSettle = CheckFaultTolerance(OnPlayerSettle)
    
    def OnShopNpcRollWand(self, oWarMgr, oHero, dMsgInfo):
        dPlayerData = self.m_Data[oHero.m_PlayerID]
        if 'RollWand' not in dMsgInfo:
            return None
        if 'recast_nums' not in dPlayerData:
            dPlayerData['recast_nums'] = 0
        if 'lock_nums' not in dPlayerData:
            dPlayerData['lock_nums'] = 0
        oRollWand = dMsgInfo['RollWand']
        dPlayerData['recast_nums'] += 1
        dPlayerData['lock_nums'] += (1 if oRollWand.m_LockWandAbility else 0)
        dRecastMaterial = dPlayerData.setdefault('recast_material', {
            WAND_QUALITY_TALE: 0,
            WAND_QUALITY_RARE: 0,
            WAND_QUALITY_NORMAL: 0 })
        iConsumeWandQuality = dMsgInfo.get('ConsumeWandQuality', 0)
        if iConsumeWandQuality in dRecastMaterial:
            dRecastMaterial[iConsumeWandQuality] += 1

    OnShopNpcRollWand = CheckFaultTolerance(OnShopNpcRollWand)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']

    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            return self.m_Data[pid]
        return 0

    GetStatistics = CheckFaultToleranceWithDefault(Default = 0)(GetStatistics)


class CRealDieAnalyseCom(CBaseAnalyseCom):
    m_RelifeTypeDict = {
        TYPE_RELIFE_KILLBOSS: 3,
        TYPE_RELIFE_BUY: 2,
        TYPE_RELIFE_GSCASH: 1 }
    
    def __init__(self, oGame):
        super(CRealDieAnalyseCom, self).__init__(oGame)
        oWarMgr = oGame.GetWarMgr()
        self.m_WarMgr = oWarMgr
        self.m_Flag = 'BigDataAnalyse_RealDie'
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        self.m_BaseInfo = { }

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        oGame = self.m_Game
        self.SetBaseInfo()
        for iHero in oWarMgr.GetBigDataHero():
            oHero = oGame.GetObject(iHero)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DIEDIST, self.OnRealDie, self.m_Flag, -1, 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def SetBaseInfo(self):
        oWarMgr = self.m_WarMgr
        self.m_BaseInfo = {
            'WarNo': oWarMgr.m_SID,
            'Round': oWarMgr.m_Round,
            'Cycle': oWarMgr.m_Cycle,
            'TeamNumber': len(oWarMgr.GetAllHero()) }

    SetBaseInfo = CheckFaultTolerance(SetBaseInfo)
    
    def StartListen(self, oHero):
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, self.m_Flag, -1, 0)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.OnSettleWar, self.m_Flag, -1, 0)

    StartListen = CheckFaultTolerance(StartListen)
    
    def DoneListen(self, oHero):
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.m_Flag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_PLAYERSETTLE, self.m_Flag)

    DoneListen = CheckFaultTolerance(DoneListen)
    
    def OnRelife(self, oHero, dMsgInfo):
        iRelifeType = 0
        if 'RS' in dMsgInfo:
            oReason = dMsgInfo['RS']
            iType = oReason.Query('Type', 0)
            iRelifeType = self.m_RelifeTypeDict.get(iType, 0)
        self.SettleTrueDie(oHero, iRelifeType)
        self.DoneListen(oHero)

    OnRelife = CheckFaultTolerance(OnRelife)
    
    def OnRealDie(self, oHero, dMsgInfo):
        lstLive = self.m_WarMgr.GetLivePlayer(iCalAI = 0)
        if len(lstLive) <= 1:
            return None
        self.StartListen(oHero)
        self.AddTrueDieState(oHero)

    OnRealDie = CheckFaultTolerance(OnRealDie)
    
    def OnSettleWar(self, oHero, dMsgInfo):
        if oHero.m_Dead != DEAD_FLAG_REAL:
            return None
        self.SettleTrueDie(oHero)
        self.DoneListen(oHero)

    OnSettleWar = CheckFaultTolerance(OnSettleWar)
    
    def AddTrueDieState(self, oHero):
        dArgs = {
            'AID': oHero.m_ID,
            'RS': cl_object.reason.CStrReason(self.m_Flag),
            'arg': { } }
        oState = cl_state.AddState(oHero, BIGDATA_REALDIE_STATE, STATE_TIME_FOREVER, 0, dArgs)
        if not oState:
            return None
        oState.Enable(oHero)

    AddTrueDieState = CheckFaultTolerance(AddTrueDieState)
    
    def SettleTrueDie(self, oHero, iRelifeType = 0):
        oState = oHero.m_State.GetItemBySID(BIGDATA_REALDIE_STATE)
        if not oState:
            return None
        iPlayer = oHero.m_PlayerID
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        dTrueDieInfo = {
            'WarMask': self.m_WarMgr.m_WarMask,
            'Layer': oLevelCtrl.m_LayerNum,
            'Hero': oHero.m_SID,
            'team_fight_time': oState.GetCount(),
            'attack_times': oState.m_Data['WatchPfUse'] if 'WatchPfUse' in oState.m_Data else 0,
            'hit_times': oState.m_Data['WatchPfHit'] if 'WatchPfHit' in oState.m_Data else 0,
            'revive_way': iRelifeType }
        dTrueDieInfo.update(self.m_BaseInfo)
        self.SendBigData(iPlayer, dTrueDieInfo)
        cl_state.RemoveState(oHero, BIGDATA_REALDIE_STATE)

    SettleTrueDie = CheckFaultTolerance(SettleTrueDie)
    
    def SendBigData(self, iPlayer, dTrueDieInfo):
        iLGS = self.m_WarMgr.m_PlayerMask['All'][iPlayer]['LGS']
        iGameID = self.m_Game.m_ID
        lib_server.L2SRealDieBigData(iLGS, iGameID, iPlayer, dTrueDieInfo)

    SendBigData = CheckFaultTolerance(SendBigData)
    
    def GetStatistics(self, pid):
        return { }

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DIEDIST, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)


class CDiceEquipAnalyseCom(CBaseAnalyseCom):
    m_BossResultDefeat = 0
    m_BossResultSuccess = 1
    m_BossResultHalfExit = 2
    
    def __init__(self, oGame):
        super(CDiceEquipAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_DiceEquip'
        self.m_CurLayer = 0
        self.m_CanSend = False
        self.m_AliveState = { }
        self.m_PassBossLevel = False
        self.m_DiceInfo = { }
        self.m_AlreadySend = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            self.m_AliveState[iPlayer] = 1
            self.m_DiceInfo[iPlayer] = { }
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'special_item': self.InitSpecialItemData(oHero),
                    'season_lv': oHero.Query('SeasonLevel', 0) }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Flag, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, self.m_Flag, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.OnAssembleDice, self.m_Flag, iSub = DICE_SUBMSG_ASSEMBLE, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.OnDisAssembleDice, self.m_Flag, iSub = DICE_SUBMSG_DISASSEMBLE, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DIE, self.m_Flag)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.m_Flag)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.m_Flag, iSub = DICE_SUBMSG_ASSEMBLE)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.m_Flag, iSub = DICE_SUBMSG_DISASSEMBLE)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'AS': DeepCopy(self.m_AliveState),
            'DF': DeepCopy(self.m_DiceInfo),
            'ALS': DeepCopy(self.m_AlreadySend),
            'CL': self.m_CurLayer,
            'PL': self.m_PassBossLevel,
            'CS': self.m_CanSend }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_AliveState = dData['AS']
            self.m_DiceInfo = dData['DF']
            self.m_CurLayer = dData['CL']
            self.m_PassBossLevel = dData['PL']
            self.m_CanSend = dData['CS']
            self.m_AlreadySend = dData['ALS']

    
    def OnRelife(self, oHero, dInfo):
        self.m_AliveState[oHero.m_PlayerID] = 1

    OnRelife = CheckFaultTolerance(OnRelife)
    
    def OnDie(self, oHero, dInfo):
        self.m_AliveState[oHero.m_PlayerID] = 0

    OnDie = CheckFaultTolerance(OnDie)
    
    def InitSpecialItemData(self, oHero):
        if not oHero or not (oHero.m_DiceCon):
            return []
        dSpecialItemInfo = oHero.m_DiceCon.m_SpecialItemInfo
        if not dSpecialItemInfo:
            return []
        lstSpecItem = list(dSpecialItemInfo.values())
        return lstSpecItem

    InitSpecialItemData = CheckFaultToleranceWithDefault(Default = [])(InitSpecialItemData)
    
    def OnAssembleDice(self, oHero, dMsgInfo):
        if 'Dice' not in dMsgInfo:
            return None
        iDice = dMsgInfo['Dice']
        oDice = oHero.m_DiceCon.GetDiceByID(iDice)
        dDiceInfo = {
            'dice_id': oDice.m_SID,
            'dice_lv': oDice.m_Quality,
            'entry_lv': dMsgInfo['AbilityQuality'] if 'AbilityQuality' in dMsgInfo else oDice.GetDiceAbilityQuality() }
        dPlayerDiceInfo = self.m_DiceInfo[oHero.m_PlayerID]
        dPlayerDiceInfo[iDice] = dDiceInfo

    
    def OnDisAssembleDice(self, oHero, dMsgInfo):
        if 'Dice' not in dMsgInfo:
            return None
        iDice = dMsgInfo['Dice']
        dPlayerDiceInfo = self.m_DiceInfo[oHero.m_PlayerID]
        dPlayerDiceInfo.pop(iDice, None)

    
    def OnStartFight(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType != LEVEL_TYPE_BOSS:
            return None
        self.m_CanSend = True
        self.m_AlreadySend = { }

    OnStartFight = CheckFaultTolerance(OnStartFight)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CanSend = False
        self.m_CurLayer = dInfo['Layer']
        self.m_PassBossLevel = False

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_PassBossLevel = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnPlayerLevelGame(self, oWarMgr, dInfo):
        if 'AssignSettleType' not in dInfo or dInfo['AssignSettleType'] != SETTLE_FINISHWAR:
            return None
        self.m_PassBossLevel = True

    OnPlayerLevelGame = CheckFaultTolerance(OnPlayerLevelGame)
    
    def GetStatistics(self, pid):
        if self.m_CanSend and pid not in self.m_AlreadySend and pid in self.m_Data:
            dData = {
                'dice_info': {
                    'item': list(self.m_DiceInfo[pid].values()) },
                'layer': self.m_CurLayer }
            dData.update(self.m_Data[pid])
            dData['boss_result'] = self.CheckBossResult(pid)
            self.m_AlreadySend[pid] = 1
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)
    
    def CheckBossResult(self, iPlayer):
        if self.m_PassBossLevel:
            return self.m_BossResultSuccess
        if self.m_AliveState[iPlayer]:
            return self.m_BossResultHalfExit
        return self.m_BossResultDefeat

    CheckBossResult = CheckFaultTolerance(CheckBossResult)


class CFinalDiceEquipAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CFinalDiceEquipAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_FinalDiceEquip'
        self.m_CurLayer = 0
        self.m_CanSend = { }
        self.m_RecordMaxLayer = { }
        self.m_DiceInfo = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            dCreateInfo = dInfo.get('CreateInfo', { })
            dPlayerInfo = dCreateInfo[iPlayer] if iPlayer in dCreateInfo else { }
            self.m_RecordMaxLayer[iPlayer] = self.GetRecordMaxLayer(dPlayerInfo)
            self.m_CanSend[iPlayer] = False
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'special_item': self.InitSpecialItemData(oHero),
                    'season_lv': oHero.Query('SeasonLevel', 0) }
                self.m_DiceInfo[iPlayer] = { }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.OnAssembleDice, self.m_Flag, iSub = DICE_SUBMSG_ASSEMBLE, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.OnDisAssembleDice, self.m_Flag, iSub = DICE_SUBMSG_DISASSEMBLE, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.m_Flag, iSub = DICE_SUBMSG_ASSEMBLE)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.m_Flag, iSub = DICE_SUBMSG_DISASSEMBLE)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'DF': DeepCopy(self.m_DiceInfo),
            'RML': DeepCopy(self.m_RecordMaxLayer),
            'CS': DeepCopy(self.m_CanSend),
            'CL': self.m_CurLayer }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_RecordMaxLayer = dData['RML']
            self.m_DiceInfo = dData['DF']
            self.m_CanSend = dData['CS']
            self.m_CurLayer = dData['CL']

    
    def GetRecordMaxLayer(self, dPlayerInfo):
        if 'MaxRoundInfo' not in dPlayerInfo:
            return 0
        (_, _, iRecordLayer) = dPlayerInfo['MaxRoundInfo']
        return iRecordLayer

    GetRecordMaxLayer = CheckFaultToleranceWithDefault(Default = 0)(GetRecordMaxLayer)
    
    def InitSpecialItemData(self, oHero):
        if not oHero or not (oHero.m_DiceCon):
            return []
        dSpecialItemInfo = oHero.m_DiceCon.m_SpecialItemInfo
        if not dSpecialItemInfo:
            return []
        lstSpecItem = list(dSpecialItemInfo.values())
        return lstSpecItem

    InitSpecialItemData = CheckFaultToleranceWithDefault(Default = [])(InitSpecialItemData)
    
    def OnAssembleDice(self, oHero, dMsgInfo):
        if 'Dice' not in dMsgInfo:
            return None
        iDice = dMsgInfo['Dice']
        oDice = oHero.m_DiceCon.GetDiceByID(iDice)
        dDiceInfo = {
            'dice_id': oDice.m_SID,
            'dice_lv': oDice.m_Quality,
            'entry_lv': dMsgInfo['AbilityQuality'] if 'AbilityQuality' in dMsgInfo else oDice.GetDiceAbilityQuality() }
        dPlayerDiceInfo = self.m_DiceInfo[oHero.m_PlayerID]
        dPlayerDiceInfo[iDice] = dDiceInfo

    OnAssembleDice = CheckFaultTolerance(OnAssembleDice)
    
    def OnDisAssembleDice(self, oHero, dMsgInfo):
        if 'Dice' not in dMsgInfo:
            return None
        iDice = dMsgInfo['Dice']
        dPlayerDiceInfo = self.m_DiceInfo[oHero.m_PlayerID]
        dPlayerDiceInfo.pop(iDice, None)

    OnDisAssembleDice = CheckFaultTolerance(OnDisAssembleDice)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType != LEVEL_TYPE_BOSS:
            return None
        iCurLayer = dInfo['Layer']
        for iPlayer in self.m_CanSend.keys():
            if not iCurLayer >= MAX_LAYER:
                if iCurLayer >= self.m_RecordMaxLayer[iPlayer]:
                    self.m_CanSend[iPlayer] = True
                    continue
        

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def GetStatistics(self, pid):
        if pid in self.m_CanSend and self.m_CanSend[pid] and pid in self.m_Data:
            dData = {
                'dice_info': {
                    'item': list(self.m_DiceInfo[pid].values()) },
                'layer': self.m_CurLayer }
            dData.update(self.m_Data[pid])
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CFirstRedEnertyAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CFirstRedEnertyAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_FirstRedEnerty'
        self.m_CurLayer = 0
        self.m_RecordAbility = []
        self.m_SendData = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'special_item': self.InitSpecialItemData(oHero),
                    'season_lv': oHero.Query('SeasonLevel', 0) }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.OnAddDice, self.m_Flag, iSub = DICE_SUBMSG_ADD, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, self.OnChangeDicePoint, self.m_Flag, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.m_Flag, iSub = DICE_SUBMSG_ADD)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'RA': DeepCopy(self.m_RecordAbility),
            'SD': DeepCopy(self.m_SendData),
            'CL': self.m_CurLayer }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_RecordAbility = dData['RA']
            self.m_SendData = dData['SD']
            self.m_CurLayer = dData['CL']

    
    def InitSpecialItemData(self, oHero):
        if not oHero or not (oHero.m_DiceCon):
            return []
        dSpecialItemInfo = oHero.m_DiceCon.m_SpecialItemInfo
        if not dSpecialItemInfo:
            return []
        lstSpecItem = list(dSpecialItemInfo.values())
        return lstSpecItem

    InitSpecialItemData = CheckFaultToleranceWithDefault(Default = [])(InitSpecialItemData)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnAddDice(self, oHero, dMsgInfo):
        if 'Dice' not in dMsgInfo:
            return None
        iDice = dMsgInfo['Dice']
        oDice = oHero.m_DiceCon.GetDiceByID(iDice)
        iAbilityQuality = oDice.GetDiceAbilityQuality()
        iSID = oDice.m_SID
        if iAbilityQuality == DICEABILITY_QUALITY_RED and iSID not in self.m_RecordAbility:
            self.m_RecordAbility.append(iSID)
            iLevelID = 0
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            if oLevelCtrl:
                oLevelNode = oLevelCtrl.m_CurNode
                iLevelID = oLevelNode.m_Level if oLevelNode else 0
            self.m_SendData[oHero.m_PlayerID] = {
                'stage_id': iLevelID }
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.m_Flag, iSub = DICE_SUBMSG_ADD)
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, self.m_Flag)
            DiceLog.Debug('%s %s adddice record first red entry %s %s ' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iSID, iLevelID))

    OnAddDice = CheckFaultTolerance(OnAddDice)
    
    def OnChangeDicePoint(self, oHero, dMsgInfo):
        if 'Dice' not in dMsgInfo:
            return None
        iDice = dMsgInfo['Dice']
        oDice = oHero.m_DiceCon.GetDiceByID(iDice)
        iAbilityQuality = oDice.GetDiceAbilityQuality()
        iSID = oDice.m_SID
        if iAbilityQuality == DICEABILITY_QUALITY_RED and iSID not in self.m_RecordAbility:
            self.m_RecordAbility.append(iSID)
            iLevelID = 0
            oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
            if oLevelCtrl:
                oLevelNode = oLevelCtrl.m_CurNode
                iLevelID = oLevelNode.m_Level if oLevelNode else 0
            self.m_SendData[oHero.m_PlayerID] = {
                'stage_id': iLevelID }
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICECHANGE, self.m_Flag, iSub = DICE_SUBMSG_ADD)
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_AFTER_CONSETDICEPOINT, self.m_Flag)
            DiceLog.Debug('%s %s changepoint record first red entry %s %s ' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iSID, iLevelID))

    OnChangeDicePoint = CheckFaultTolerance(OnChangeDicePoint)
    
    def GetStatistics(self, pid):
        if pid in self.m_SendData and pid in self.m_Data:
            dData = {
                'layer': self.m_CurLayer }
            dData.update(self.m_Data[pid])
            dData.update(self.m_SendData[pid])
            self.m_SendData.pop(pid)
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CRecycleDiceAnalyseCom(CBaseAnalyseCom):
    ADDENERGY_REASON_THROW = 'SetDicePoint'
    
    def __init__(self, oGame):
        super(CRecycleDiceAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_RecycleDice'
        self.m_CurLayer = 0
        self.m_CanSend = False
        self.m_RecordInfo = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'special_item': self.InitSpecialItemData(oHero),
                    'season_lv': oHero.Query('SeasonLevel', 0) }
                self.m_RecordInfo[iPlayer] = {
                    'recycle_num': 0,
                    'throw_energy': 0,
                    'total_energy': 0 }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_CHANGE_DICEENERGY, self.OnAddSpecialEnergy, self.m_Flag, iSub = ADD_DICEENERGY, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_RECYCLEDROP, self.OnRecycleDice, self.m_Flag, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_CHANGE_DICEENERGY, self.m_Flag, iSub = ADD_DICEENERGY)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RECYCLEDROP, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'RI': DeepCopy(self.m_RecordInfo),
            'CL': self.m_CurLayer,
            'CS': self.m_CanSend }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_RecordInfo = dData['RI']
            self.m_CurLayer = dData['CL']
            self.m_CanSend = dData['CS']

    
    def InitSpecialItemData(self, oHero):
        if not oHero or not (oHero.m_DiceCon):
            return []
        dSpecialItemInfo = oHero.m_DiceCon.m_SpecialItemInfo
        if not dSpecialItemInfo:
            return []
        lstSpecItem = list(dSpecialItemInfo.values())
        return lstSpecItem

    InitSpecialItemData = CheckFaultToleranceWithDefault(Default = [])(InitSpecialItemData)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']
        self.m_CanSend = False

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnAddSpecialEnergy(self, oHero, dMsgInfo):
        if 'AddEnergy' not in dMsgInfo or 'Reason' not in dMsgInfo:
            return None
        iAddEnergy = dMsgInfo['AddEnergy']
        sReason = dMsgInfo['Reason']
        dRecordInfo = self.m_RecordInfo[oHero.m_PlayerID]
        if sReason == self.ADDENERGY_REASON_THROW:
            iThrowEnergy = dRecordInfo.get('throw_energy', 0)
            dRecordInfo['throw_energy'] = iThrowEnergy + iAddEnergy
        dRecordInfo['total_energy'] += iAddEnergy

    OnAddSpecialEnergy = CheckFaultTolerance(OnAddSpecialEnergy)
    
    def OnRecycleDice(self, oHero, dMsgInfo):
        if 'RecycleDropType' not in dMsgInfo or dMsgInfo['RecycleDropType'] != NWARRIOR_DROP_DICE:
            return None
        dRecordInfo = self.m_RecordInfo.setdefault(oHero.m_PlayerID, { })
        dRecordInfo['recycle_num'] += 1

    OnRecycleDice = CheckFaultTolerance(OnRecycleDice)
    
    def OnPlayerLevelGame(self, oWarMgr, dInfo):
        if 'AssignSettleType' not in dInfo or dInfo['AssignSettleType'] != SETTLE_FINISHWAR:
            return None
        self.m_CanSend = True

    OnPlayerLevelGame = CheckFaultTolerance(OnPlayerLevelGame)
    
    def GetAndInitRecordInfo(self, pid):
        dData = { }
        dRecordInfo = self.m_RecordInfo.setdefault(pid, { })
        dData['recycle_num'] = dRecordInfo.get('recycle_num', 0)
        dData['throw_energy'] = dRecordInfo.get('throw_energy', 0)
        dData['total_energy'] = dRecordInfo.get('total_energy', 0)
        self.m_RecordInfo[pid] = {
            'recycle_num': 0,
            'throw_energy': 0,
            'total_energy': 0 }
        return dData

    GetAndInitRecordInfo = CheckFaultToleranceWithDefault(Default = { })(GetAndInitRecordInfo)
    
    def GetStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = {
                'layer': self.m_CurLayer }
            dData.update(self.m_Data[pid])
            dData.update(self.GetAndInitRecordInfo(pid))
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CDiceBuyAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CDiceBuyAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_DiceBuy'
        self.m_CurLayer = 0
        self.m_CurNpcLevel = 0
        self.m_BuyDicePacketInfo = { }
        self.m_BuyPointDice = { }
        self.m_Cost = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateNpc, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'special_item': self.InitSpecialItemData(oHero),
                    'season_lv': oHero.Query('SeasonLevel', 0) }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DICESHOP_BUY, self.OnBuyDicePacket, self.m_Flag, iSub = DICESHOP_BUY_DICEPACKET, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DICESHOP_BUY, self.OnBuyPointDice, self.m_Flag, iSub = DICESHOP_BUY_POINTDICE, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICESHOP_BUY, self.m_Flag, iSub = DICESHOP_BUY_DICEPACKET)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DICESHOP_BUY, self.m_Flag, iSub = DICESHOP_BUY_POINTDICE)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'BDPI': DeepCopy(self.m_BuyDicePacketInfo),
            'CT': DeepCopy(self.m_Cost),
            'BPD': self.m_BuyPointDice,
            'CL': self.m_CurLayer,
            'CNL': self.m_CurNpcLevel }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_BuyDicePacketInfo = dData['BDPI']
            self.m_BuyPointDice = dData['BPD']
            self.m_CurLayer = dData['CL']
            self.m_CurNpcLevel = dData['CNL']
            self.m_Cost = dData.get('CT', { })

    
    def InitSpecialItemData(self, oHero):
        if not oHero or not (oHero.m_DiceCon):
            return []
        dSpecialItemInfo = oHero.m_DiceCon.m_SpecialItemInfo
        if not dSpecialItemInfo:
            return []
        lstSpecItem = list(dSpecialItemInfo.values())
        return lstSpecItem

    InitSpecialItemData = CheckFaultToleranceWithDefault(Default = [])(InitSpecialItemData)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnCreateNpc(self, oWarMgr, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_DICESHOP:
            return None
        if not oNpc.m_LineIdx:
            oScene = self.m_Game.m_SceneMgr.GetScene(oNpc.m_Scene)
            self.m_CurNpcLevel = oScene.m_Level if oScene else 0
        else:
            self.m_CurNpcLevel = oNpc.m_LineIdx[0]
        for pid in self.m_WarMgr.GetRoomPlayer():
            self.InitStatisticData(pid)
        

    OnCreateNpc = CheckFaultTolerance(OnCreateNpc)
    
    def InitStatisticData(self, iPlayer):
        self.m_BuyPointDice[iPlayer] = (0, 0)
        self.m_BuyDicePacketInfo[iPlayer] = {
            'optional_info': [] }
        self.m_Cost[iPlayer] = 0

    InitStatisticData = CheckFaultTolerance(InitStatisticData)
    
    def OnBuyDicePacket(self, oHero, dMsgInfo):
        if 'Quality' not in dMsgInfo or 'ChooseDice' not in dMsgInfo or 'Cost' not in dMsgInfo:
            return None
        iQuality = dMsgInfo['Quality']
        iChooseDice = dMsgInfo['ChooseDice']
        iPlayer = oHero.m_PlayerID
        dDicePacketInfo = self.m_BuyDicePacketInfo.setdefault(iPlayer, { })
        lstPacketQuality = dDicePacketInfo.setdefault('optional_info', [])
        lstPacketQuality.append('%d_%d' % (iQuality, iChooseDice))
        iCost = self.m_Cost.get(iPlayer, 0)
        self.m_Cost[iPlayer] = iCost + dMsgInfo['Cost']

    OnBuyDicePacket = CheckFaultTolerance(OnBuyDicePacket)
    
    def OnBuyPointDice(self, oHero, dMsgInfo):
        if 'ChoosePoint' not in dMsgInfo:
            return None
        iChosePoint = dMsgInfo['ChoosePoint']
        iPlayer = oHero.m_PlayerID
        (iSumPoint, iBuyDiceNum) = self.m_BuyPointDice[iPlayer] if oHero.m_PlayerID in self.m_BuyPointDice else (0, 0)
        iSumPoint += iChosePoint
        iBuyDiceNum += 1
        self.m_BuyPointDice[oHero.m_PlayerID] = (iSumPoint, iBuyDiceNum)
        iCost = self.m_Cost.get(iPlayer, 0)
        self.m_Cost[iPlayer] = iCost + dMsgInfo['Cost']

    OnBuyPointDice = CheckFaultTolerance(OnBuyPointDice)
    
    def GetAndClearBuyInfo(self, pid):
        dData = { }
        dDicePacketInfo = self.m_BuyDicePacketInfo.setdefault(pid, { })
        lstOptionInfo = dDicePacketInfo.setdefault('optional_info', [])
        if lstOptionInfo:
            dData.update(dDicePacketInfo)
        else:
            dData['optional_info'] = [
                '0_0']
        (iSumPoint, iBuyDiceNum) = self.m_BuyPointDice.setdefault(pid, (0, 0))
        dData['dice_points'] = [
            iSumPoint,
            iBuyDiceNum]
        dData['cost_energy'] = self.m_Cost.get(pid, 0)
        self.m_BuyPointDice.pop(pid)
        self.m_BuyDicePacketInfo.pop(pid)
        self.m_Cost.pop(pid, 0)
        return dData

    GetAndClearBuyInfo = CheckFaultToleranceWithDefault(Default = {
        'optional_info': [
            '0_0'],
        'dice_points': [
            0,
            0],
        'cost_energy': 0 })(GetAndClearBuyInfo)
    
    def GetStatistics(self, pid):
        if pid in self.m_BuyDicePacketInfo:
            dData = self.GetAndClearBuyInfo(pid)
            dData.update(self.m_Data[pid])
            dData['layer'] = self.m_CurLayer
            dData['stage_id'] = self.m_CurNpcLevel
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CSeasonBenedictionAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CSeasonBenedictionAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_SeasonBenediction'
        self.m_CanSend = False
        self.m_BenedictionInfo = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'season': oWarMgr.m_SeasonNum,
                    'season_lv': oHero.Query('SeasonLevel', 0) }
            self.m_BenedictionInfo[iPlayer] = {
                'lingyou_list': [],
                'lingyou_tab': 0,
                'lingyou_replace': 0 }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_OPEN_BEFOR_BENED, self.OnGenBeforeBene, self.m_Flag, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_CHOOSEBENED, self.OnChooseBene, self.m_Flag, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_OPEN_BEFOR_BENED, self.m_Flag)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_CHOOSEBENED, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'BI': DeepCopy(self.m_BenedictionInfo),
            'CS': self.m_CanSend }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_BenedictionInfo = dData['BI']
            self.m_CanSend = dData['CS']

    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CanSend = False

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnGenBeforeBene(self, oHero, dMsgInfo):
        if 'BenedOp' not in dMsgInfo or not dMsgInfo['BenedOp']:
            return None
        dCreateBeneInfo = dMsgInfo['BenedOp']
        dBeneInfo = self.m_BenedictionInfo.setdefault(oHero.m_PlayerID, { })
        lstCanChooseBene = list(dCreateBeneInfo.keys())
        lstRecordBene = dBeneInfo.setdefault('lingyou_list', [])
        lstRecordBene.extend(lstCanChooseBene)

    OnGenBeforeBene = CheckFaultTolerance(OnGenBeforeBene)
    
    def OnChooseBene(self, oHero, dMsgInfo):
        if 'Bene' not in dMsgInfo:
            return None
        iBenediction = dMsgInfo['Bene']
        dBeneInfo = self.m_BenedictionInfo.setdefault(oHero.m_PlayerID, { })
        dBeneInfo['lingyou_tab'] = iBenediction
        if 'ReplaceInfo' in dMsgInfo:
            (iReplaceBene, _) = dMsgInfo['ReplaceInfo']
            dBeneInfo['lingyou_replace'] = iReplaceBene
        else:
            dBeneInfo['lingyou_replace'] = 0

    OnChooseBene = CheckFaultTolerance(OnChooseBene)
    
    def GetBeneRecordInfo(self, pid):
        dData = { }
        dBeneInfo = self.m_BenedictionInfo.setdefault(pid, { })
        lstBene = dBeneInfo.setdefault('lingyou_list', [])
        if lstBene:
            dData['lingyou_list'] = lstBene
        else:
            dData['lingyou_list'] = [
                0]
        iBene = dBeneInfo.setdefault('lingyou_tab', 0)
        dData['lingyou_tab'] = iBene
        iReplace = dBeneInfo.setdefault('lingyou_replace', 0)
        dData['lingyou_replace'] = iReplace
        self.m_BenedictionInfo[pid] = { }
        return dData

    GetBeneRecordInfo = CheckFaultToleranceWithDefault(Default = { })(GetBeneRecordInfo)
    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            dData = { }
            dData.update(self.m_Data[pid])
            dData.update(self.GetBeneRecordInfo(pid))
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)
    
    def GetLevelStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = { }
            dData.update(self.m_Data[pid])
            dData.update(self.GetBeneRecordInfo(pid))
            return dData
        return { }

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = { })(GetLevelStatistics)


class CDiceSpecialItemAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CDiceSpecialItemAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_DiceSpecialItem'
        self.m_CanSend = False
        self.m_CurLayer = 0
        self.m_SpecialItemUseInfo = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            dCreateInfo = dInfo.get('CreateInfo', { })
            dPlayerInfo = dCreateInfo[iPlayer] if iPlayer in dCreateInfo else { }
            self.m_SpecialItemUseInfo[iPlayer] = { }
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'season_lv': oHero.Query('SeasonLevel', 0) }
                dSpecialItemData = self.GetSpecialItemData(oHero, dPlayerInfo)
                self.m_Data[iPlayer].update(dSpecialItemData)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_USEDICESPECIALITEM, self.OnUseSpecialItem, self.m_Flag, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_USEDICESPECIALITEM, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'SIUI': DeepCopy(self.m_SpecialItemUseInfo),
            'CL': self.m_CurLayer,
            'CS': self.m_CanSend }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_SpecialItemUseInfo = dData['SIUI']
            self.m_CurLayer = dData['CL']
            self.m_CanSend = dData['CS']

    
    def GetSpecialItemData(self, oHero, dPlayerInfo):
        dData = {
            'unlock_special_item': [
                0],
            'auto_item': [
                0],
            'special_item': [
                0] }
        if dPlayerInfo:
            if 'SpecialItemInfo' in dPlayerInfo:
                lstSpecItem = list(oHero.m_DiceCon.m_SpecialItemInfo.values()) if oHero.m_DiceCon.m_SpecialItemInfo else [
                    0]
                lstChooseSpecItem = dPlayerInfo['SpecialItemInfo']
                dData['special_item'] = lstSpecItem
                setAutoItem = set(lstSpecItem) - set(lstChooseSpecItem)
                if setAutoItem:
                    dData['auto_item'] = list(setAutoItem)
            if 'UnLockSpecailItem' in dPlayerInfo and dPlayerInfo['UnLockSpecailItem']:
                dData['unlock_special_item'] = dPlayerInfo['UnLockSpecailItem']
        return dData

    GetSpecialItemData = CheckFaultToleranceWithDefault(Default = [])(GetSpecialItemData)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']
        self.m_CanSend = False

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnUseSpecialItem(self, oHero, dMsgInfo):
        if 'SpecialItemSID' not in dMsgInfo:
            return None
        iSpecialItemSID = dMsgInfo['SpecialItemSID']
        dUseInfo = self.m_SpecialItemUseInfo.setdefault(oHero.m_PlayerID, { })
        if iSpecialItemSID in dUseInfo:
            dUseInfo[iSpecialItemSID] += 1
        else:
            dUseInfo[iSpecialItemSID] = 1

    OnUseSpecialItem = CheckFaultTolerance(OnUseSpecialItem)
    
    def GetSpecialItemUseInfo(self, pid):
        lstUseNum = []
        dData = {
            'use_nums': lstUseNum }
        lstSpecialItem = self.m_Data[pid]['special_item']
        dSpecialItemUseInfo = self.m_SpecialItemUseInfo.setdefault(pid, { })
        for iSpecialItem in lstSpecialItem:
            iUseNum = dSpecialItemUseInfo[iSpecialItem] if iSpecialItem in dSpecialItemUseInfo else 0
            lstUseNum.append(iUseNum)
        
        self.m_SpecialItemUseInfo[pid] = { }
        return dData

    GetSpecialItemUseInfo = CheckFaultToleranceWithDefault(Default = { })(GetSpecialItemUseInfo)
    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            dData = {
                'layer': self.m_CurLayer }
            dData.update(self.m_Data[pid])
            dData.update(self.GetSpecialItemUseInfo(pid))
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)
    
    def GetLevelStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = {
                'layer': self.m_CurLayer }
            dData.update(self.m_Data[pid])
            dData.update(self.GetSpecialItemUseInfo(pid))
            return dData
        return { }

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = { })(GetLevelStatistics)


class CCrystalComponentAnalyseCom(CBaseAnalyseCom):
    m_EnterBossLevel = 0
    m_LeaveBossLevel = 1
    
    def __init__(self, oGame):
        super(CCrystalComponentAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_CrystalComponent'
        self.m_CurLayer = 0
        self.m_CurBossLevel = 0
        self.m_StageResult = -1
        self.m_CanSend = False
        self.m_RecordInfo = { }
        self.m_DropCrystalInfo = { }
        self.m_DropModuleInfo = { }
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, self.m_Flag, iSub = -1, iOnce = 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'season_lv': oHero.Query('SeasonLevel', 0) }
                self.m_RecordInfo[iPlayer] = {
                    'crystal_num': 0,
                    'crystal_point': 0,
                    'component_num': 0 }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnAddCrystal, self.m_Flag, iSub = S7CRYSTAL_ADD, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnAddCrystalPoint, self.m_Flag, iSub = S7CRYSTAL_POINTADD, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnAddModule, self.m_Flag, iSub = S7MODULE_ADD, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnRemoveCrystal, self.m_Flag, iSub = S7CRYSTAL_REMOVE, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnRemoveModule, self.m_Flag, iSub = S7MODULE_REMOVE, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7CRYSTAL_ADD)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7CRYSTAL_POINTADD)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7MODULE_ADD)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7CRYSTAL_REMOVE)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7MODULE_REMOVE)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'RI': DeepCopy(self.m_RecordInfo) }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_RecordInfo = dData['RI']

    
    def OnAddCrystal(self, oHero, dMsgInfo):
        if 'S7Item' not in dMsgInfo or 'CrystalSID' not in dMsgInfo:
            return None
        iCrystalType = GetS7CrystalType(dMsgInfo['CrystalSID'])
        if iCrystalType == CRTSTAL_RAWMATERIAL:
            return None
        iCrystal = dMsgInfo['S7Item']
        iPlayer = oHero.m_PlayerID
        dDropCrystalInfo = self.m_DropCrystalInfo.setdefault(iPlayer, { })
        if iCrystal not in dDropCrystalInfo:
            dRecordInfo = self.m_RecordInfo[iPlayer]
            dRecordInfo['crystal_num'] += 1
            iPoint = dMsgInfo['TotalPoint'] if 'TotalPoint' in dMsgInfo else 0
            dRecordInfo['crystal_point'] += iPoint
        else:
            dDropCrystalInfo.pop(iCrystal)

    
    def OnAddCrystalPoint(self, oHero, dMsgInfo):
        if 'CrystalSID' not in dMsgInfo or 'AddPoint' not in dMsgInfo:
            return None
        iCrystalType = GetS7CrystalType(dMsgInfo['CrystalSID'])
        if iCrystalType == CRTSTAL_RAWMATERIAL:
            return None
        dRecordInfo = self.m_RecordInfo[oHero.m_PlayerID]
        iAddPoint = dMsgInfo['AddPoint']
        dRecordInfo['crystal_point'] += iAddPoint

    
    def OnAddModule(self, oHero, dMsgInfo):
        if 'S7Item' not in dMsgInfo:
            return None
        iModule = dMsgInfo['S7Item']
        iPlayer = oHero.m_PlayerID
        dDropModuleInfo = self.m_DropModuleInfo.setdefault(iPlayer, { })
        if iModule not in dDropModuleInfo:
            dRecordInfo = self.m_RecordInfo[iPlayer]
            dRecordInfo['component_num'] += 1
        else:
            dDropModuleInfo.pop(iModule)

    
    def OnRemoveCrystal(self, oHero, dMsgInfo):
        if 'S7Item' not in dMsgInfo or 'Drop' not in dMsgInfo or not dMsgInfo['Drop']:
            return None
        iCrystal = dMsgInfo['S7Item']
        dDropCrystalInfo = self.m_DropCrystalInfo.setdefault(oHero.m_PlayerID, { })
        dDropCrystalInfo[iCrystal] = 1

    
    def OnRemoveModule(self, oHero, dMsgInfo):
        if 'S7Item' not in dMsgInfo or 'Drop' not in dMsgInfo or not dMsgInfo['Drop']:
            return None
        iModule = dMsgInfo['S7Item']
        dDropModuleInfo = self.m_DropModuleInfo.setdefault(oHero.m_PlayerID, { })
        dDropModuleInfo[iModule] = 1

    
    def OnStartFight(self, oWarMgr, dInfo):
        self.m_DropCrystalInfo = { }
        self.m_DropModuleInfo = { }
        iLevelType = dInfo['LevelType']
        if iLevelType != LEVEL_TYPE_BOSS:
            return None
        self.m_CanSend = False

    OnStartFight = CheckFaultTolerance(OnStartFight)
    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CanSend = False
        self.m_CurBossLevel = 0
        self.m_StageResult = -1
        self.m_CurLayer = dInfo['Layer']

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CurBossLevel = dInfo['LevelID']
            self.m_StageResult = self.m_LeaveBossLevel
            self.m_CanSend = True
            return None
        if 'Transfer' not in dInfo:
            return None
        dTransfer = dInfo['Transfer']
        if not dTransfer:
            return None
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        iTranLevelID = dTransfer['LevelID']
        iTranLayer = dTransfer['LayerNum']
        iTranLevel = dTransfer['LevelNum']
        (iTranLevelType, _) = oLevelCtrl.GetLevelInfo(iTranLayer, iTranLevel, iTranLevelID)
        if iTranLevelType == LEVEL_TYPE_BOSS:
            self.m_CurBossLevel = iTranLevelID
            self.m_StageResult = self.m_EnterBossLevel
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnPlayerLevelGame(self, oWarMgr, dInfo):
        if 'AssignSettleType' not in dInfo or dInfo['AssignSettleType'] != SETTLE_FINISHWAR:
            return None
        self.m_StageResult = self.m_LeaveBossLevel
        self.m_CanSend = True

    OnPlayerLevelGame = CheckFaultTolerance(OnPlayerLevelGame)
    
    def GetCrystalInfo(self, lstCrystalInfo):
        dData = { }
        dData['item'] = [ {
'id': iModule,
'point': iPoint } for iModule, iPoint in lstCrystalInfo ]
        return dData

    GetCrystalInfo = CheckFaultToleranceWithDefault(Default = { })(GetCrystalInfo)
    
    def GetModuleInfo(self, lstModuleInfo):
        dData = { }
        dData['item'] = [ {
'id': iModule,
'point': iPoint } for iModule, iPoint in lstModuleInfo ]
        return dData

    GetModuleInfo = CheckFaultToleranceWithDefault(Default = { })(GetModuleInfo)
    
    def GetRecordInfo(self, iPlayer):
        if iPlayer not in self.m_RecordInfo:
            return { }
        return self.m_RecordInfo[iPlayer]

    GetRecordInfo = CheckFaultToleranceWithDefault(Default = { })(GetRecordInfo)
    
    def GetLevelStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = {
                'layer': self.m_CurLayer,
                'stage_id': self.m_CurBossLevel,
                'stage_result': self.m_StageResult }
            oHero = self.m_WarMgr.GetHeroByPlayer(pid)
            oBackPackCon = oHero.m_BackpackCon
            (iEffPoint, iUnEffPoint) = oBackPackCon.GetEffPointAndUnEffPoint()
            dData['effective_point'] = iEffPoint
            dData['invalid_point'] = iUnEffPoint
            dData['crystal_info'] = self.GetCrystalInfo(oBackPackCon.GetAllEquipCrystalSIDAndPoint())
            dData['component_info'] = self.GetModuleInfo(oBackPackCon.GetAllEquipModuleSIDAndPoint())
            dData.update(self.GetRecordInfo(pid))
            dData.update(self.m_Data[pid])
            return dData
        return { }

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = { })(GetLevelStatistics)


class CSeasonNpcAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CSeasonNpcAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_SeasonNpc'
        self.m_CurLayer = 0
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        self.m_Game.AddGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateNpc, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONSHOP, self.OnInitS7Goods, self.m_Flag, iSub = SEASONSHOP_INITS7GOODS, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONSHOP, self.OnBuyS7CrystalGood, self.m_Flag, iSub = SEASONSHOP_BUYS7CRYSTAL, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONSHOP, self.OnBuyS7CrystalGood, self.m_Flag, iSub = SEASONSHOP_BUYS7PACKET, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        self.m_Game.DoneGlobalAttention(self.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONSHOP, self.m_Flag, iSub = SEASONSHOP_INITS7GOODS)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONSHOP, self.m_Flag, iSub = SEASONSHOP_BUYS7CRYSTAL)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONSHOP, self.m_Flag, iSub = SEASONSHOP_BUYS7PACKET)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'CL': self.m_CurLayer }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_CurLayer = dData['CL']

    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnCreateNpc(self, oWarMgr, oNpc, dInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_S7SHOP:
            return None
        oScene = self.m_Game.m_SceneMgr.GetScene(oNpc.m_Scene)
        iCurNpcLevel = oScene.m_Level
        for pid in self.m_WarMgr.GetRoomPlayer():
            self.InitStatisticData(pid, iCurNpcLevel)
        

    OnCreateNpc = CheckFaultTolerance(OnCreateNpc)
    
    def InitStatisticData(self, iPlayer, iCurNpcLevel):
        self.m_Data[iPlayer] = {
            'stage_id': iCurNpcLevel,
            'if_interaction': 0,
            'if_coin_enough': 0,
            'if_buy': 0 }

    InitStatisticData = CheckFaultTolerance(InitStatisticData)
    
    def OnInitS7Goods(self, oHero, dMsgInfo):
        if 'MinCash' not in dMsgInfo or 'TotalCash' not in dMsgInfo:
            return None
        iMinCash = dMsgInfo['MinCash']
        iTotalCash = dMsgInfo['TotalCash']
        if iMinCash < 0 or iTotalCash < 0:
            return None
        iPlayer = oHero.m_PlayerID
        dRecordInfo = self.m_Data.setdefault(iPlayer, { })
        dRecordInfo['if_interaction'] = 1
        iHasCash = oHero.Cash()
        if iHasCash >= iTotalCash:
            dRecordInfo['if_coin_enough'] = 2
        elif iHasCash >= iMinCash:
            dRecordInfo['if_coin_enough'] = 1

    OnInitS7Goods = CheckFaultTolerance(OnInitS7Goods)
    
    def OnBuyS7CrystalGood(self, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        if iPlayer not in self.m_Data:
            return None
        if 'SellOutAll' not in dMsgInfo:
            return None
        iSellOutAll = dMsgInfo['SellOutAll']
        dRecordInfo = self.m_Data[iPlayer]
        if iSellOutAll:
            dRecordInfo['if_buy'] = 2
        else:
            dRecordInfo['if_buy'] = 1

    OnBuyS7CrystalGood = CheckFaultTolerance(OnBuyS7CrystalGood)
    
    def GetAndClearRecordInfo(self, pid):
        return self.m_Data.pop(pid, { })

    GetAndClearRecordInfo = CheckFaultToleranceWithDefault(Default = { })(GetAndClearRecordInfo)
    
    def GetLevelStatistics(self, pid):
        if pid in self.m_Data:
            dData = self.GetAndClearRecordInfo(pid)
            dData['layer'] = self.m_CurLayer
            return dData
        return { }

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = { })(GetLevelStatistics)


class CAutoAssemblyAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CAutoAssemblyAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_AutoAssembly'
        self.m_CanSend = False
        self.m_CurLayer = 0
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iOnce = 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'assembly_num': 0,
                    'clear_num': 0 }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.OnS7AutoEquip, self.m_Flag, iSub = S7_AUTO_EQUIP, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.OnS7AutoUnEquip, self.m_Flag, iSub = S7_AUTO_UNEQUIP, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.m_Flag, iSub = S7_AUTO_EQUIP)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_S7_CONTAINER_OPERATION, self.m_Flag, iSub = S7_AUTO_UNEQUIP)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'CL': self.m_CurLayer,
            'CS': self.m_CanSend }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_CurLayer = dData['CL']
            self.m_CanSend = dData['CS']

    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']
        self.m_CanSend = False

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnLevelGoal(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    OnLevelGoal = CheckFaultTolerance(OnLevelGoal)
    
    def OnS7AutoEquip(self, oHero, dMsgInfo):
        dRecordInfo = self.m_Data[oHero.m_PlayerID]
        dRecordInfo['assembly_num'] += 1

    OnS7AutoEquip = CheckFaultTolerance(OnS7AutoEquip)
    
    def OnS7AutoUnEquip(self, oHero, dMsgInfo):
        dRecordInfo = self.m_Data[oHero.m_PlayerID]
        dRecordInfo['clear_num'] += 1

    OnS7AutoUnEquip = CheckFaultTolerance(OnS7AutoUnEquip)
    
    def OnPlayerLevelGame(self, oWarMgr, dInfo):
        if 'AssignSettleType' not in dInfo or dInfo['AssignSettleType'] != SETTLE_FINISHWAR:
            return None
        self.m_CanSend = True

    OnPlayerLevelGame = CheckFaultTolerance(OnPlayerLevelGame)
    
    def GetAndInitRecordInfo(self, pid):
        dData = { }
        dRecordInfo = self.m_Data.setdefault(pid, { })
        dData['assembly_num'] = dRecordInfo.get('assembly_num', 0)
        dData['clear_num'] = dRecordInfo.get('clear_num', 0)
        self.m_Data[pid] = {
            'assembly_num': 0,
            'clear_num': 0 }
        return dData

    GetAndInitRecordInfo = CheckFaultToleranceWithDefault(Default = { })(GetAndInitRecordInfo)
    
    def GetLevelStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            dData = {
                'layer': self.m_CurLayer }
            dData.update(self.GetAndInitRecordInfo(pid))
            return dData
        return { }

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = { })(GetLevelStatistics)


class CStrengthenRollbackAnalyseCom(CBaseAnalyseCom):
    
    def __init__(self, oGame):
        super(CStrengthenRollbackAnalyseCom, self).__init__(oGame)
        self.m_Data = { }
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_StrengthenRollback'
        self.m_CurLayer = 0
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'material_num': 0,
                    'strengthen_num': 0,
                    'auto_strengthen_num': 0,
                    'rollback_num': 0 }
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnAddCrystal, self.m_Flag, iSub = S7CRYSTAL_ADD, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnEnhanceModule, self.m_Flag, iSub = S7MODULE_ENHANCE, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnAutoEnhanceModule, self.m_Flag, iSub = S7MODULE_AUTOENHANCE, iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.OnDecreaseModule, self.m_Flag, iSub = S7MODULE_DECREASE, iOnce = 0)
        

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7CRYSTAL_ADD)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7MODULE_ENHANCE)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7MODULE_AUTOENHANCE)
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.m_Flag, iSub = S7MODULE_DECREASE)
        
        self.m_Game = None
        self.m_WarMgr = None

    Release = CheckFaultTolerance(Release)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'CL': self.m_CurLayer }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_CurLayer = dData['CL']

    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        self.m_CurLayer = dInfo['Layer']

    OnLayerStart = CheckFaultTolerance(OnLayerStart)
    
    def OnAddCrystal(self, oHero, dMsgInfo):
        if 'CrystalSID' not in dMsgInfo:
            return None
        iCrystalSID = dMsgInfo['CrystalSID']
        iCrystalType = GetS7CrystalType(iCrystalSID)
        if iCrystalType != CRTSTAL_RAWMATERIAL:
            return None
        dRecordInfo = self.m_Data[oHero.m_PlayerID]
        dRecordInfo['material_num'] += 1

    OnAddCrystal = CheckFaultTolerance(OnAddCrystal)
    
    def OnEnhanceModule(self, oHero, dMsgInfo):
        if 'AddPoint' not in dMsgInfo:
            return None
        iAddPoint = dMsgInfo['AddPoint']
        if not iAddPoint:
            return None
        dRecordInfo = self.m_Data[oHero.m_PlayerID]
        dRecordInfo['strengthen_num'] += iAddPoint

    OnEnhanceModule = CheckFaultTolerance(OnEnhanceModule)
    
    def OnAutoEnhanceModule(self, oHero, dMsgInfo):
        if 'AddPoint' not in dMsgInfo:
            return None
        iAddPoint = dMsgInfo['AddPoint']
        if not iAddPoint:
            return None
        dRecordInfo = self.m_Data[oHero.m_PlayerID]
        dRecordInfo['auto_strengthen_num'] += iAddPoint

    OnAutoEnhanceModule = CheckFaultTolerance(OnAutoEnhanceModule)
    
    def OnDecreaseModule(self, oHero, dMsgInfo):
        if 'SubPoint' not in dMsgInfo:
            return None
        iSubPoint = dMsgInfo['SubPoint']
        if not iSubPoint:
            return None
        dRecordInfo = self.m_Data[oHero.m_PlayerID]
        dRecordInfo['rollback_num'] += iSubPoint

    OnDecreaseModule = CheckFaultTolerance(OnDecreaseModule)
    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            dData = {
                'layer': self.m_CurLayer }
            dRecordInfo = dict(self.m_Data[pid])
            dData.update(dRecordInfo)
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)


class CDyingTimeAndRealDeathAnalyseCom(CBaseAnalyseCom):
    LIVE_STATUS_LIFE = 0
    LIVE_STATUS_FALL = 1
    LIVE_STATUS_DEAD = 2
    m_CanSendDataPhase = (13, 26)
    
    def __init__(self, oGame):
        super(CDyingTimeAndRealDeathAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Flag = 'BigDataAnalyse_DyingAndRealDeath'
        self.m_CanSend = True
        self.m_Data = { }
        self.m_PhaseData = { }
        self.m_FallInfo = { }
        self.m_Status = { }
        self.m_SurvivorElement = None
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, -1, 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            if iPlayer not in self.m_Data:
                self.m_Data[iPlayer] = {
                    'fall_time': 0,
                    'real_death': 0 }
            self.InitPhaseData(iPlayer)
            oHero = self.m_Game.GetObject(iHero)
            if oWarMgr.m_PlayType == PLAY_TYPE_SINGLE:
                cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DIEDIST, self.OnRealDieBySingle, self.m_Flag, -1, 0)
                continue
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DIEDIST, self.OnRealDie, self.m_Flag, -1, 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_Flag, -1, 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, self.m_Flag, -1, 0)
        
        self.m_SurvivorElement = self.m_WarMgr.GetComponent('SurvivorElement')
        if self.m_SurvivorElement:
            self.m_CanSend = False
            cl_msgcenter.AddFunction(self.m_SurvivorElement, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_Flag, -1, 0)

    OnAddAllPlayer = CheckFaultTolerance(OnAddAllPlayer)
    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        if self.m_SurvivorElement:
            cl_msgcenter.DoneEvent(self.m_SurvivorElement, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_Flag)
        for iHero in self.m_WarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if oHero or self.m_WarMgr.m_PlayType == PLAY_TYPE_SINGLE:
                cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DIEDIST, self.m_Flag)
                continue
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DIEDIST, self.m_Flag)
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DIE, self.m_Flag)
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_RELIFE, self.m_Flag)
        
        self.m_Game = None
        self.m_WarMgr = None
        self.m_SurvivorElement = None

    Release = CheckFaultTolerance(Release)
    
    def InitPhaseData(self, pid):
        self.m_PhaseData[pid] = {
            'fall_time': 0,
            'real_death': 0 }

    InitPhaseData = CheckFaultTolerance(InitPhaseData)
    
    def Save(self):
        dData = {
            'DT': DeepCopy(self.m_Data),
            'PD': DeepCopy(self.m_PhaseData),
            'ST': DeepCopy(self.m_Status),
            'FI': DeepCopy(self.m_FallInfo),
            'CS': self.m_CanSend }
        return dData

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData['DT']
            self.m_PhaseData = dData['PD']
            self.m_Status = dData['ST']
            self.m_FallInfo = dData['FI']
            self.m_CanSend = dData['CS']

    
    def OnRealDieBySingle(self, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        self.SetRecordByKey(iPlayer, 'real_death', 1)

    OnRealDieBySingle = CheckFaultTolerance(OnRealDieBySingle)
    
    def OnRealDie(self, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        self.SetStatus(iPlayer, self.LIVE_STATUS_DEAD)
        self.SetRecordByKey(iPlayer, 'real_death', 1)

    OnRealDie = CheckFaultTolerance(OnRealDie)
    
    def OnDie(self, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        self.SetStatus(iPlayer, self.LIVE_STATUS_FALL)
        iNowFrame = self.m_Game.GetFrameNum()
        self.m_FallInfo[iPlayer] = iNowFrame

    OnDie = CheckFaultTolerance(OnDie)
    
    def OnRelife(self, oHero, dMsgInfo):
        iPlayer = oHero.m_PlayerID
        self.SetStatus(iPlayer, self.LIVE_STATUS_LIFE)

    OnRelife = CheckFaultTolerance(OnRelife)
    
    def SetStatus(self, iPlayer, iStatus):
        iCurStatus = self.m_Status.get(iPlayer, self.LIVE_STATUS_LIFE)
        if iStatus == iCurStatus:
            return None
        self.CalAndRecordFallTime(iPlayer, iCurStatus)
        self.m_Status[iPlayer] = iStatus

    SetStatus = CheckFaultTolerance(SetStatus)
    
    def CalAndRecordFallTime(self, iPlayer, iStatus = 0):
        if not iStatus:
            iStatus = self.m_Status.get(iPlayer, self.LIVE_STATUS_LIFE)
        if iStatus == self.LIVE_STATUS_FALL:
            iNowFrame = self.m_Game.GetFrameNum()
            iFallFrame = self.m_FallInfo.get(iPlayer, 0)
            if iFallFrame > 0 and iFallFrame < iNowFrame:
                iFallTime = Frame2Time(iNowFrame - iFallFrame)
                self.SetRecordByKey(iPlayer, 'fall_time', iFallTime)

    CalAndRecordFallTime = CheckFaultTolerance(CalAndRecordFallTime)
    
    def SetRecordByKey(self, iPlayer, sKey, iAdd):
        dPhaseData = self.m_PhaseData.setdefault(iPlayer, { })
        dPhaseData.setdefault(sKey, 0)
        dPhaseData[sKey] += iAdd
        dData = self.m_Data.setdefault(iPlayer, { })
        dData.setdefault(sKey, 0)
        dData[sKey] += iAdd

    SetRecordByKey = CheckFaultTolerance(SetRecordByKey)
    
    def OnPhaseStart(self, oSurvivor, dMsgInfo):
        if 'Phase' not in dMsgInfo:
            return None
        iPhase = dMsgInfo['Phase']
        if iPhase in self.m_CanSendDataPhase:
            self.m_CanSend = True
        else:
            self.m_CanSend = False

    OnPhaseStart = CheckFaultTolerance(OnPhaseStart)
    
    def GetStatistics(self, pid):
        if pid in self.m_Data:
            dData = { }
            if self.m_WarMgr and self.m_WarMgr.m_PlayType == PLAY_TYPE_MULTI:
                self.CalAndRecordFallTime(pid)
            dData.update(self.m_Data[pid])
            return dData
        return { }

    GetStatistics = CheckFaultToleranceWithDefault(Default = { })(GetStatistics)
    
    def GetLevelStatistics(self, pid):
        if self.m_CanSend and pid in self.m_PhaseData:
            dData = { }
            dData.update(self.m_PhaseData[pid])
            self.InitPhaseData(pid)
            return dData
        return { }

    GetLevelStatistics = CheckFaultToleranceWithDefault(Default = { })(GetLevelStatistics)


class CHeroSkillAnalyseCom(CBaseAnalyseCom):
    m_Flag = 'BigDataAnalyse_HeroSkill'
    m_HeroAttention = {
        GARDENER_HERO: {
            (cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1): (lambda oAnalyseCom: oAnalyseCom.Gardener_ThrowSkillHit),
            (cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL): (lambda oAnalyseCom: oAnalyseCom.Gardener_CareerSkillHit),
            (cl_msgcenter.MSG_WAR_USE_THROWPF, -1): (lambda oAnalyseCom: oAnalyseCom.Gardener_UseThrowSkill),
            (cl_msgcenter.MSG_WAR_USE_CAREERPF, -1): (lambda oAnalyseCom: oAnalyseCom.Gardener_UseCareerSkill) } }
    
    def __init__(self, oGame):
        super(CHeroSkillAnalyseCom, self).__init__(oGame)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_Data = { }
        self.m_CanSend = False
        self.InitEvent()

    
    def Release(self):
        self.ReleaseEvent()
        self.m_Game = None
        self.m_WarMgr = None

    
    def Save(self):
        return self.m_Data

    
    def Load(self, dData):
        if self.CanLoad():
            self.m_Data = dData

    
    def GetStatistics(self, pid):
        if self.m_CanSend and pid in self.m_Data:
            return self.m_Data[pid]
        return { }

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.OnPlayerLevelGame, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_Flag, iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelGoal, self.m_Flag, iSub = -1, iOnce = 0)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.AddAttentionFunc(self.m_WarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.OnLayerStart, self.m_Flag)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        for iHero in oWarMgr.GetBigDataHero():
            iPlayer = oWarMgr.GetPlayerIDByHeroID(iHero)
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or oHero.m_SID not in self.m_HeroAttention:
                continue
            if iPlayer in self.m_Data:
                continue
            self.m_Data[iPlayer] = self.GetInitData(iLayer = 0)
            dAttention = self.m_HeroAttention[oHero.m_SID]
            for (iMsg, iSub), cFunc in dAttention.items():
                cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, iMsg, cFunc(self), self.m_Flag, iSub = iSub)
            
        

    
    def ReleaseEvent(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WAR_PLAYERCHOOSELEAVEGAME, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.m_Flag)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        cl_msgcenter.DoneAttention(oWarMgr, oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_LAYERSTART, self.m_Flag)
        for iHero in oWarMgr.GetBigDataHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or oHero.m_SID not in self.m_HeroAttention:
                continue
            dAttention = self.m_HeroAttention[oHero.m_SID]
            for iMsg, iSub in dAttention:
                cl_msgcenter.DoneAttention(oWarMgr, iHero, iMsg, self.m_Flag, iSub = iSub)
            
        

    
    def GetInitData(self, iLayer):
        dInitData = {
            'Layer': iLayer,
            'SkillInfo': { } }
        return dInitData

    
    def OnLayerStart(self, oWarMgr, oLevelCtrl, dInfo):
        iLayer = dInfo['Layer']
        self.m_CanSend = False
        for iPlayer in self.m_Data:
            self.m_Data[iPlayer] = self.GetInitData(iLayer)
        

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        if dInfo['LevelType'] == LEVEL_TYPE_BOSS:
            self.m_CanSend = True

    
    def OnPlayerLevelGame(self, oWarMgr, dInfo):
        self.m_CanSend = True

    
    def GetSkillInfo(self, iPerform, iPlayerID, bSpecialSkill = False):
        dSkillInfo = self.m_Data[iPlayerID]['SkillInfo']
        if iPerform in dSkillInfo and bSpecialSkill in dSkillInfo[iPerform]:
            return dSkillInfo[iPerform][bSpecialSkill]
        dInfo = dSkillInfo.setdefault(iPerform, { })
        dCollectInfo = dInfo.setdefault(bSpecialSkill, {
            'skill_use': 0,
            'skill_hit': 0,
            'if_special_skill': 0 })
        if bSpecialSkill:
            dCollectInfo['if_special_skill'] = 1
        return dCollectInfo

    
    def Gardener_UseThrowSkill(self, _oWarMgr, oHero, dInfo):
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        if iPerform != oHero.GetThrowPerformID():
            return None
        bSpecialSkill = 1 if oSkill.m_Custom['ThrowType'] else 0
        dSkillInfo = self.GetSkillInfo(iPerform, oHero.m_PlayerID, bSpecialSkill)
        dSkillInfo['skill_use'] += 1

    
    def Gardener_ThrowSkillHit(self, _oWarMgr, oHero, dInfo):
        if 'Skill' not in dInfo or 'GardenThrowHit' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        if iPerform != oHero.GetThrowPerformID():
            return None
        dCustom = oSkill.m_Custom
        if dCustom['ThrowType']:
            return None
        dHitEnemy = dCustom.setdefault('HitEnemy', { })
        iVictim = dInfo['VID']
        if iVictim in dHitEnemy:
            return None
        oVictim = oSkill.m_Game.GetObject(iVictim)
        if not oVictim:
            return None
        if oVictim.m_FightType & WARRIOR_BUILD:
            return None
        dHitEnemy[iVictim] = 1
        dSkillInfo = self.GetSkillInfo(iPerform, oHero.m_PlayerID)
        dSkillInfo['skill_hit'] += 1

    
    def CheckGardenerCareerSkill(self, oHero):
        if oHero.GetPerform(13562):
            return False
        return True

    
    def Gardener_UseCareerSkill(self, _oWarMgr, oHero, dInfo):
        if not self.CheckGardenerCareerSkill(oHero):
            return None
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        oHero.m_Perform.GetPerform(iPerform)
        dSkillInfo = self.GetSkillInfo(iPerform, oHero.m_PlayerID)
        dSkillInfo['skill_use'] += 1

    
    def Gardener_CareerSkillHit(self, _oWarMgr, oHero, dInfo):
        if not self.CheckGardenerCareerSkill(oHero):
            return None
        if 'OriginalAID' not in dInfo:
            return None
        iAID = dInfo['OriginalAID']
        oPlant = oHero.m_GardenerCon.GetPlant(iAID)
        if not oPlant:
            return None
        if 'PF1333' not in oPlant.Reason():
            return None
        iPerform = oHero.GetCareerPerformID()
        dSkillInfo = self.GetSkillInfo(iPerform, oHero.m_PlayerID)
        dSkillInfo['skill_hit'] += 1



def IsValidStats(oWarMgr, pid):
    if lib_flag.g_IsStandaloneClient:
        who = cli_player.GetPlayer(pid)
        if who and who.m_WarMaster:
            return True
    if lib_flag.g_IsMobileRun or lib_flag.g_IsPCRunFight:
        iRoomPlayerCnt = len(oWarMgr.GetRoomPlayer())
        if iRoomPlayerCnt <= 1:
            return True
    return False


def GetComponentClass(oWarManager):
    return CBigDataAnalyseMgr

