# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/survivorupgrademgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/survivorupgrademgr.pyc
# Source Generated with Decompyle++
# File: survivorupgrademgr.pyc (Python 3.6)

from cl_only import DeepCopy, ChooseKey, ShufferList
from cl_object.logging import SurvivorLog
from cl_commondefines import VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_TALENT, MG_RELIC, MG_EQUIP, MG_TALENT
from cl_cscommondef.cs_itemdef import ITEM_SOURCE_SURVIVOR, EQUIP_TYPE_MAINWEAPON
from cl_item.defines import EQUIP_TYPE_FUNDAMENTALWEAPON
from cl_minigame import MiniGameAttrInfo
import cl_msgcenter
import cl_snetwar
import cl_formula
import cl_reward
import cl_minigame
import cl_item
import cl_netattr
IDX_EXPERIENCE = 0
IDX_GRADE = 1
IDX_RATIO = 2
IDX_SKILLPOINT = 3
IDX_UPNEED = 4
IDX_EXTRAPOINT = 5
EXTRAOPTION_CHOOSEALL = 1
EXTRAOPTION_RADOMCHOOSE = 2
EXTRAOPTION_WEAPONUPGRADE = 3

class CSurvivorUpgradeMgr(object):
    m_CallFlag = 'SurvivorUpgradeMgr'
    
    def __init__(self, oSurvivorElement, oData):
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_GradeRewardData = oData.m_GradeRewardData
        self.m_SuperGradeRewardData = oData.m_SuperGradeRewardData
        self.m_SuperLevel = oData.m_Config.get('m_SuperLevel', 50)
        self.m_UpGradeInfo = oData.m_Config.get('m_UpGradeInfo', { })
        self.m_TeamExperienceInfo = oData.m_Config.get('m_TeamExperienceInfo', { })
        self.m_InitReward = oData.m_Config.get('m_InitReward', [])
        self.m_GetInitRewardHero = { }
        self.m_MaxGradeLevel = self.GetMaxGradeLevel()
        self.m_TeamExperienceRatio = 100
        self.m_HeroUpgradeInfo = { }
        self.m_Grade2Phase = { }
        self.m_CurRewardGrade = { }
        self.m_CurRewardInfo = { }
        self.m_ExtraRewardInfo = { }
        self.m_ExtraRewarMenuIdxInfo = { }
        self.m_ChooseAllCnt = { }

    
    def Init(self):
        iWarMgrID = self.m_Game.m_WarMgr.m_ID
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.InitUpGradeInfo, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.HeroUpGradeInfoRefresh, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.OnAddPlayer, self.m_CallFlag)

    
    def Release(self):
        oWarMgr = self.m_Game.m_WarMgr
        iWarMgrID = oWarMgr.m_ID
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(iWarMgrID, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.m_CallFlag)
        lstAllHero = oWarMgr.GetAllHero()
        for iHero in lstAllHero:
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.m_CallFlag)
        
        self.m_Survivor = None
        self.m_Game = None
        self.m_UpGradeInfo = { }
        self.m_CurRewardInfo = { }

    
    def Save(self, iHero):
        dData = { }
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return dData
        dData['HUP'] = self.m_HeroUpgradeInfo[iHero]
        dData['G2P'] = self.m_Grade2Phase[iHero]
        dData['CRG'] = self.m_CurRewardGrade[iHero]
        dData['INIT'] = self.m_GetInitRewardHero[iHero] if iHero in self.m_GetInitRewardHero else 0
        dData['EXTR'] = self.m_ExtraRewardInfo[iHero] if iHero in self.m_ExtraRewardInfo else []
        dData['CAC'] = self.m_ChooseAllCnt[iHero] if iHero in self.m_ChooseAllCnt else { }
        if iHero in self.m_CurRewardInfo and self.m_CurRewardInfo[iHero]:
            (_, iItemType, dReward, dExtraOption) = self.m_CurRewardInfo[iHero]
            dSaveReward = {
                'Type': iItemType,
                'Reward': dReward,
                'ExtraOption': dExtraOption }
            if iItemType == VIRTUAL_ITEM_EQUIP:
                dInfo = { }
                for iWeapon, dWeaponInfo in dReward.items():
                    oWeapon = dWeaponInfo['Item']
                    dInfo[iWeapon] = oWeapon.Save()
                
                dSaveReward['Reward'] = dInfo
            dData['RW'] = dSaveReward
        return DeepCopy(dData)

    
    def Load(self, iHero, dData):
        if not dData:
            return None
        self.m_HeroUpgradeInfo[iHero] = dData['HUP']
        self.m_Grade2Phase[iHero] = dData['G2P']
        self.m_CurRewardGrade[iHero] = dData['CRG']
        if dData['INIT']:
            self.m_GetInitRewardHero[iHero] = dData['INIT']
        if 'EXTR' in dData:
            self.m_ExtraRewardInfo[iHero] = dData['EXTR']
        if 'CAC' in dData:
            self.m_ChooseAllCnt[iHero] = dData['CAC']
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or 'RW' not in dData:
            return None
        dSaveReward = dData['RW']
        iItemType = dSaveReward['Type']
        if iItemType == VIRTUAL_ITEM_EQUIP:
            dReward = { }
            for iItem, dInfo in dSaveReward['Reward'].items():
                oWeapon = cl_item.CreateEquip(self.m_Game, dInfo['SID'], cl_item.GetBaseGrade(dInfo), dInfo['ID'])
                if not oWeapon:
                    continue
                oWeapon.Load(dInfo)
                lstAttr = cl_minigame.MiniGameAttrInfo(oWeapon, cl_netattr.PROP_DROPITEM_MAINWEAPON)
                dReward[iItem] = {
                    'Item': oWeapon,
                    'Attr': lstAttr }
            
        else:
            dReward = dSaveReward['Reward']
        dExtraInfo = {
            'ExtraOption': dSaveReward['ExtraOption'] }
        self.AddRewardInfo(oHero, iItemType, dReward, 'Load', dExtraInfo)

    
    def InitUpGradeInfo(self, oWarMgr, oTarget, dInfo):
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
        if self.m_HeroUpgradeInfo:
            return None
        self.RefreshTeamExperienceRatio()
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            oHero = self.m_Game.GetObject(iHero)
            if not oHero or iHero in self.m_CurRewardGrade:
                continue
            self.m_CurRewardGrade[iHero] = 1
            self.m_Grade2Phase[iHero] = {
                1: 0 }
            self.m_CurRewardInfo[iHero] = []
            self.m_HeroUpgradeInfo[iHero] = [
                0,
                1,
                100,
                1,
                100,
                0]
            self.m_HeroUpgradeInfo[iHero][IDX_UPNEED] = self.GetUpGradeNeed(oHero, 1)
            self.RefreshUpGradeClient(oHero.m_ID)
            self.InitRewardInfo(oHero)
        

    
    def InitRewardInfo(self, oHero):
        if oHero.m_ID in self.m_GetInitRewardHero:
            return None
        self.CreateReward(oHero, iIsInitReward = 1)

    
    def OnAddPlayer(self, oWarMgr, oTarget, dInfo):
        iHero = dInfo['Hero']
        cl_msgcenter.AddAttentionFunc(self.m_Game.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, self.OnChangeWeapon, self.m_CallFlag)

    
    def OnRemovePlayer(self, oWarMgr, oTarget, dInfo):
        self.RefreshTeamExperienceRatio()

    
    def OnChangeWeapon(self, oWarMgr, oTarget, dInfo):
        iHeroID = oTarget.m_ID
        if iHeroID not in self.m_CurRewardInfo or not self.m_CurRewardInfo[iHeroID]:
            return None
        (iMenuIdx, iItemType, dReplaceReward, dExtraOption) = self.m_CurRewardInfo[iHeroID]
        oItem = oTarget.m_WieldCon.GetCurWeapon()
        iChange = 0
        if (EXTRAOPTION_WEAPONUPGRADE in dExtraOption or oItem) and not oItem.CanUpgrade():
            dExtraOption.pop(EXTRAOPTION_WEAPONUPGRADE)
            iChange = 1
        elif oItem and oItem.CanUpgrade():
            iCurRewardGrade = self.m_CurRewardGrade[iHeroID]
            (_, _, lstExtraOption) = self.GetGradeRewardInfo(iCurRewardGrade)
            if iItemType == VIRTUAL_ITEM_EQUIP or EXTRAOPTION_WEAPONUPGRADE in lstExtraOption:
                dExtraOption[EXTRAOPTION_WEAPONUPGRADE] = 1
                iChange = 1
        if not iChange:
            return None
        self.m_CurRewardInfo[iHeroID] = (iMenuIdx, iItemType, dReplaceReward, dExtraOption)
        self.GS2CChooseItem(oTarget, 'ChangeWeapon')

    
    def RefreshTeamExperienceRatio(self):
        lstHero = self.m_Game.m_WarMgr.GetRoomHero()
        if not lstHero:
            return None
        iHeroCnt = len(lstHero)
        self.m_TeamExperienceRatio = self.m_TeamExperienceInfo[iHeroCnt]

    
    def HeroUpGradeInfoRefresh(self, oWarMgr, oTarget, dInfo):
        if not self.m_HeroUpgradeInfo:
            return None
        self.RefreshUpGradeClient(oTarget.m_ID)
        self.GS2CChooseItem(oTarget, 'Init')

    
    def GetUpGradeNeed(self, oHero, iGrade):
        for iRange, iValue in self.m_UpGradeInfo.items():
            if iGrade > iRange:
                continue
            return cl_formula.GetResultByData(oHero, iValue, { })
        
        return cl_formula.GetResultByData(oHero, self.m_UpGradeInfo[self.m_MaxGradeLevel], { })

    
    def GetMaxGradeLevel(self):
        iMax = 0
        for iRange in self.m_UpGradeInfo:
            iMax = iRange if iRange > iMax else iMax
        
        return iMax

    
    def AddExperience(self, iAddExperience):
        for iHero in self.m_Game.m_WarMgr.GetRoomHero():
            (iExperience, _, iRatio, _, iUpNeed, _) = self.m_HeroUpgradeInfo[iHero]
            iExperience += iAddExperience * self.m_TeamExperienceRatio * iRatio // 10000
            self.m_HeroUpgradeInfo[iHero][IDX_EXPERIENCE] = iExperience
            if iExperience >= iUpNeed:
                self.HeroUpGrade(iHero)
            self.RefreshUpGradeClient(iHero)
        

    
    def HeroUpGrade(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        (iExperience, iGrade, iRatio, iSkillPoint, iUpNeed, iExtraPoint) = self.m_HeroUpgradeInfo[oHero.m_ID]
        SurvivorLog.Debug('%d %d upgrade:%d %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iExperience, iUpNeed, iGrade))
        iExperience = iExperience - iUpNeed
        self.m_HeroUpgradeInfo[iHero][IDX_EXPERIENCE] = iExperience
        iGrade += 1
        self.m_Grade2Phase[iHero][iGrade] = self.m_Survivor.m_Phase
        self.m_HeroUpgradeInfo[oHero.m_ID][IDX_GRADE] = iGrade
        iSkillPoint += 1
        iUpNeed = self.GetUpGradeNeed(oHero, iGrade)
        self.m_HeroUpgradeInfo[iHero] = [
            iExperience,
            iGrade,
            iRatio,
            iSkillPoint,
            iUpNeed,
            iExtraPoint]
        dData = {
            'Grade': iGrade }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPGRADE, oHero, dData)
        self.m_Game.m_WarMgr.HandleUpGradeReport(oHero.m_PlayerID, iGrade, self.m_Survivor.m_Phase, self.m_Survivor.m_FightTimerMgr.GetPlayFrame())
        self.CreateReward(oHero)

    
    def RefreshUpGradeClient(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        (iExperience, iGrade, _, iSkillPoint, iUpNeed, iExtraPoint) = self.m_HeroUpgradeInfo[oHero.m_ID]
        cl_snetwar.GS2CHeroUpGradeInfoRefresh(oHero.m_PlayerID, iExperience, iGrade, iSkillPoint + iExtraPoint, iUpNeed)

    
    def GetHeroGrade(self, iHero):
        if iHero not in self.m_HeroUpgradeInfo:
            return 0
        return self.m_HeroUpgradeInfo[iHero][IDX_GRADE]

    
    def ValidReward(self, iHero, iIsInitReward = 0):
        if iHero not in self.m_HeroUpgradeInfo:
            return 0
        if iHero in self.m_CurRewardInfo and self.m_CurRewardInfo[iHero]:
            return 0
        if iHero not in self.m_CurRewardGrade:
            return 0
        iCurRewardGrade = self.m_CurRewardGrade[iHero] if iIsInitReward else self.m_CurRewardGrade[iHero] + 1
        tRewardInfo = self.GetGradeRewardInfo(iCurRewardGrade)
        if not tRewardInfo:
            return 0
        if iCurRewardGrade not in self.m_Grade2Phase[iHero]:
            return 0
        if not iIsInitReward and iHero not in self.m_GetInitRewardHero:
            return 0
        lstUpgradeInfo = self.m_HeroUpgradeInfo[iHero]
        iSkillPoint = lstUpgradeInfo[IDX_SKILLPOINT]
        if not iIsInitReward and iSkillPoint < 1:
            return 0
        return 1

    
    def ValidExtraReward(self, iHero):
        if iHero not in self.m_ExtraRewardInfo or not self.m_ExtraRewardInfo[iHero]:
            return 0
        (iRewardGrade, _, _) = self.m_ExtraRewardInfo[iHero][0]
        if iRewardGrade > self.m_CurRewardGrade[iHero]:
            return 0
        if iHero in self.m_CurRewardInfo and self.m_CurRewardInfo[iHero]:
            return 0
        return 1

    
    def ChangeSkillPoint(self, iHero, iChange, iExtra = 0):
        if not iExtra:
            iChangeIdx = IDX_SKILLPOINT
        else:
            iChangeIdx = IDX_EXTRAPOINT
        if iHero not in self.m_HeroUpgradeInfo:
            return None
        iSkillPoint = self.m_HeroUpgradeInfo[iHero][iChangeIdx]
        iSkillPoint += iChange
        if iSkillPoint < 0:
            iSkillPoint = 0
        iChange = iSkillPoint - self.m_HeroUpgradeInfo[iHero][iChangeIdx]
        if not iChange:
            return None
        self.m_HeroUpgradeInfo[iHero][iChangeIdx] = iSkillPoint
        self.RefreshUpGradeClient(iHero)

    
    def AddRewardInfo(self, oHero, iItemType, dReward, sReason, dExtInfo = None):
        oHero.IncMenuIdx()
        iMenuIdx = oHero.m_NpcUIMenuIdx
        dReplaceReward = self.ReplaceRewardInfo(oHero, iItemType, dReward, dExtInfo)
        if sReason == 'Load':
            dExtraOption = dExtInfo['ExtraOption']
        else:
            dExtraOption = self.GetExtraOptionInfo(oHero, iItemType, dExtInfo)
        self.m_CurRewardInfo[oHero.m_ID] = (iMenuIdx, iItemType, dReplaceReward, dExtraOption)
        self.GS2CChooseItem(oHero, sReason)

    
    def GetExtraOptionInfo(self, oHero, iItemType, dExtInfo):
        dOptionInfo = { }
        if not dExtInfo:
            return dOptionInfo
        lstOption = dExtInfo.get('ExtraOption', [])
        for iOption in lstOption:
            dOptionInfo[iOption] = 1
        
        iRemainCnt = self.GetChooseAllRemainCnt(oHero, iItemType)
        if iRemainCnt > 0:
            (iAllCnt, iRemainCnt) = self.m_ChooseAllCnt[oHero.m_ID][iItemType]
            dOptionInfo[EXTRAOPTION_CHOOSEALL] = iAllCnt * 1000 + iRemainCnt
        oItem = oHero.m_WieldCon.GetCurWeapon()
        if not oItem:
            return dOptionInfo
        if EXTRAOPTION_WEAPONUPGRADE in dOptionInfo and not oItem.CanUpgrade():
            dOptionInfo.pop(EXTRAOPTION_WEAPONUPGRADE)
        if iItemType == VIRTUAL_ITEM_EQUIP and oItem.CanUpgrade():
            dOptionInfo[EXTRAOPTION_WEAPONUPGRADE] = 1
        return dOptionInfo

    
    def ReplaceRewardInfo(self, oHero, iItemType, dReward, dExtInfo = None):
        if iItemType == VIRTUAL_ITEM_EQUIP:
            dReplaceType = oHero.Query('ForceReplaceEquip', { })
            if not dReplaceType:
                return dReward
            if not dExtInfo or 'MGSID' not in dExtInfo:
                return dReward
            oGame = self.m_Game
            iMiniGameSID = dExtInfo['MGSID']
            clsData = oGame.m_WarData.GetMiniGameData(iMiniGameSID)
            dWeight = clsData.GetChooseWeight(oHero)
            iAmount = len(dReward)
            lstReplaceType = list(dReplaceType)
            if len(lstReplaceType) > iAmount:
                lstReplaceType = ShufferList(oGame, lstReplaceType, iAmount)
            dReplaceReward = { }
            for dInfo in dReward.values():
                oEquip = dInfo['Item']
                iType = oEquip.m_Type
                if iType in lstReplaceType:
                    dReplaceReward[oEquip.m_SID] = dInfo
                    lstReplaceType.remove(iType)
            
            if lstReplaceType:
                dTypeWeight = { }
                dValid = oHero.Query('Illus')['Weapon']
                for iWeapon in dValid:
                    clsWeapon = cl_item.GetItemCls(iWeapon)
                    if clsWeapon.m_Type == EQUIP_TYPE_FUNDAMENTALWEAPON:
                        continue
                    if iWeapon not in dWeight:
                        continue
                    iWeaponType = clsWeapon.m_Type
                    if iWeaponType not in dTypeWeight:
                        dTypeWeight[iWeaponType] = { }
                    dTypeWeight[iWeaponType][iWeapon] = dWeight[iWeapon]
                
                iHero = oHero.m_ID
                iCurRewardGrade = self.m_CurRewardGrade[iHero]
                iPhase = self.m_Grade2Phase[iHero][iCurRewardGrade]
                iGrade = self.m_Survivor.GetWeaponGrade(dData = {
                    'Phase': iPhase })
                iInscriptionNum = self.m_Survivor.GetInscriptionNum(iPhase = iPhase)
                for iType in lstReplaceType:
                    if iType not in dTypeWeight or not dTypeWeight[iType]:
                        SurvivorLog.Alert('%d %d replace weapon weight err:%d %d %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iMiniGameSID, iType, dTypeWeight, dReplaceType[iType]))
                        return dReward
                    iEquip = ChooseKey(oGame, dTypeWeight[iType])
                    oEquip = cl_item.CreateEquip(oGame, iEquip, iGrade, oOwner = oHero, iSource = ITEM_SOURCE_SURVIVOR, dExtraAttr = {
                        'InscriptionNum': iInscriptionNum })
                    if iType & EQUIP_TYPE_MAINWEAPON:
                        oBulletcom = oEquip.GetComponent('Bullet')
                        if oBulletcom:
                            oBulletcom.BulletModify(oBulletcom.MaxBullet())
                    lstAttr = MiniGameAttrInfo(oEquip, cl_netattr.PROP_DROPITEM_MAINWEAPON)
                    dReplaceReward[oEquip.m_SID] = {
                        'Item': oEquip,
                        'Attr': lstAttr }
                
            iRemainingCount = iAmount - len(dReplaceReward)
            if iRemainingCount > 0:
                for iEquip, dInfo in dReward.items():
                    if iEquip not in dReplaceReward:
                        dReplaceReward[iEquip] = dInfo
                        iRemainingCount -= 1
                        if iRemainingCount <= 0:
                            break
                
            return dReplaceReward
        return dReward

    
    def GetGradeRewardInfo(self, iGrade):
        if iGrade <= self.m_SuperLevel:
            (iMaxLevel, lstReward) = self.m_GradeRewardData
        else:
            (iMaxLevel, lstReward) = self.m_SuperGradeRewardData
        if not lstReward:
            return None
        iRewardIdx = iGrade % iMaxLevel
        return lstReward[iRewardIdx]

    
    def CreateReward(self, oHero, iIsInitReward = 0):
        iHero = oHero.m_ID
        if not self.ValidReward(iHero, iIsInitReward):
            return None
        oGame = self.m_Game
        if not iIsInitReward:
            self.m_CurRewardGrade[iHero] += 1
            iCurRewardGrade = self.m_CurRewardGrade[iHero]
            (iMiniGame, iChooseCnt, lstExtraOption) = self.GetGradeRewardInfo(iCurRewardGrade)
        else:
            (iMiniGame, iChooseCnt) = self.m_InitReward
            lstExtraOption = []
            self.m_GetInitRewardHero[iHero] = 1
            iCurRewardGrade = self.m_CurRewardGrade[iHero]
        SurvivorLog.Debug('%d %d upgrade %d reward (%d, %d, %s) %d' % (oGame.m_ID, oHero.m_PlayerID, iCurRewardGrade, iMiniGame, iChooseCnt, lstExtraOption, iIsInitReward))
        dExtInfo = {
            'MGSID': iMiniGame,
            'ExtraOption': lstExtraOption }
        self.StartRewardMinigame(oHero, iMiniGame, iChooseCnt, dExtInfo)

    
    def CreateExtraReward(self, oHero):
        iHero = oHero.m_ID
        (_, iMiniGame, iChooseCnt) = self.m_ExtraRewardInfo[iHero].pop(0)
        SurvivorLog.Debug('%d %d upgrade extrareward (%d, %d)' % (self.m_Game.m_ID, oHero.m_PlayerID, iMiniGame, iChooseCnt))
        dExtInfo = {
            'MGSID': iMiniGame }
        self.StartRewardMinigame(oHero, iMiniGame, iChooseCnt, dExtInfo)
        if iHero in self.m_CurRewardInfo and self.m_CurRewardInfo[iHero]:
            self.m_ExtraRewarMenuIdxInfo[iHero] = self.m_CurRewardInfo[iHero][0]

    
    def StartRewardMinigame(self, oHero, iMiniGame, iChooseCnt, dExtInfo = None):
        iHero = oHero.m_ID
        oGame = self.m_Game
        clsMiniGame = oGame.m_WarData.GetMiniGameData(iMiniGame)
        if not clsMiniGame:
            SurvivorLog.Alert('%d %d nominigame%d' % (oGame.m_WarMgr.m_SID, oHero.m_PlayerID, iMiniGame))
            return None
        iMiniGameType = clsMiniGame.m_Type
        if iMiniGameType not in (MG_EQUIP, MG_TALENT, MG_RELIC):
            SurvivorLog.Alert('%d %d minigame %d type %d err' % (oGame.m_WarMgr.m_SID, oHero.m_PlayerID, iMiniGame, iMiniGameType))
            return None
        iCurRewardGrade = self.m_CurRewardGrade[iHero]
        iUpgradePhase = self.m_Grade2Phase[iHero][iCurRewardGrade]
        dData = {
            'MiniGameType': iMiniGameType,
            'ChooseCnt': iChooseCnt }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPGRADEREWARD_CREATE, oHero, dData)
        iChooseCnt = dData['ChooseCnt']
        dMGExtInfo = {
            'ChooseCnt': iChooseCnt,
            'Phase': iUpgradePhase,
            'ExtInfo': dExtInfo }
        oMiniGame = cl_minigame.NewMiniGame(oGame, iMiniGame, iHero, iHero, dMGExtInfo)
        if oMiniGame:
            oMiniGame.Start()
        else:
            SurvivorLog.Alert('%d %d create minigame %d err' % (oGame.m_WarMgr.m_SID, oHero.m_PlayerID, iMiniGame))

    
    def AddExtraReward(self, oHero, iMiniGame, iChooseCnt, sReason):
        iHeroID = oHero.m_ID
        if iHeroID not in self.m_ExtraRewardInfo:
            self.m_ExtraRewardInfo[iHeroID] = []
        iRewardGrade = self.GetHeroGrade(iHeroID)
        self.m_ExtraRewardInfo[iHeroID].append((iRewardGrade, iMiniGame, iChooseCnt))
        self.ChangeSkillPoint(iHeroID, 1, iExtra = 1)
        SurvivorLog.Info('%d %d add extrareward %d %d %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iMiniGame, iChooseCnt, sReason))
        if self.ValidExtraReward(iHeroID):
            self.CreateExtraReward(oHero)

    
    def GS2CChooseItem(self, oHero, sReason):
        iHero = oHero.m_ID
        if iHero not in self.m_CurRewardInfo or not self.m_CurRewardInfo[iHero]:
            return None
        (iMenuIdx, iItemType, dReward, dExtraOption) = self.m_CurRewardInfo[iHero]
        lstItem = []
        if EXTRAOPTION_RADOMCHOOSE not in dExtraOption:
            for dOption in dReward.values():
                lstAtt = dOption['Attr']
                lstItem.append({
                    'Attr': lstAtt })
            
        cl_snetwar.GS2CChooseRewardItem(oHero.m_PlayerID, iMenuIdx, iItemType, lstItem, dExtraOption)
        if sReason == 'UpGradeMiniGame':
            lstReward = list(dReward.keys())
            dData = {
                'lstReward': lstReward,
                'RewardType': iItemType }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPGRADEREWARD_CHOOSE, oHero, dData)

    
    def ValidChooseReward(self, oHero, iMenuIdx, iAnswer):
        iHeroID = oHero.m_ID
        (iCurMenuIdx, iItemType, dReward, dExtraOption) = self.m_CurRewardInfo[iHeroID]
        if (iMenuIdx != iCurMenuIdx or iAnswer != 0) and iAnswer not in dReward and iAnswer not in dExtraOption:
            SurvivorLog.Alert('%d %d %s noreward %d %d %d' % (self.m_Game.m_ID, oHero.m_PlayerID, list(dReward), iAnswer, iMenuIdx, iCurMenuIdx))
            return 0
        if iAnswer == 0 and iItemType != VIRTUAL_ITEM_RELIC:
            return 0
        if iAnswer == EXTRAOPTION_WEAPONUPGRADE:
            oItem = oHero.m_WieldCon.GetCurWeapon()
            if not oItem or not oItem.CanUpgrade():
                SurvivorLog.Alert('%d %d upgradeweapon %s %s err' % (self.m_Game.m_ID, oHero.m_PlayerID, list(dReward), list(dExtraOption)))
                return 0
        if iAnswer == EXTRAOPTION_CHOOSEALL:
            iChooseAllCnt = self.GetChooseAllRemainCnt(oHero, iItemType)
            if iChooseAllCnt < 1:
                return 0
        return 1

    
    def ChooseReward(self, oHero, iMenuIdx, iAnswer):
        iHero = oHero.m_ID
        if iHero not in self.m_CurRewardInfo or not self.m_CurRewardInfo[iHero]:
            return None
        if not self.ValidChooseReward(oHero, iMenuIdx, iAnswer):
            self.GS2CChooseItem(oHero, 'upgradechoose')
            return None
        (_, iItemType, dReward, dExtraOption) = self.m_CurRewardInfo[iHero]
        SurvivorLog.Info('%d %d choose upgradereward %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iAnswer))
        if iHero in self.m_ExtraRewarMenuIdxInfo and self.m_ExtraRewarMenuIdxInfo[iHero] == iMenuIdx:
            self.ChangeSkillPoint(iHero, -1, iExtra = 1)
        else:
            self.ChangeSkillPoint(iHero, -1)
        self.m_CurRewardInfo[iHero] = []
        lstReward = []
        sReason = ''
        iChooseAll = 0
        iChooseItem = iAnswer
        if iAnswer in dReward:
            sReason = 'upgradechoose%d' % iAnswer
            if iItemType == VIRTUAL_ITEM_EQUIP:
                dTrueReward = {
                    'item': iItemType,
                    'info': {
                        'sid': iAnswer,
                        'item': dReward[iAnswer]['Item'],
                        'data': { } } }
            elif iItemType == VIRTUAL_ITEM_RELIC:
                dTrueReward = {
                    'item': iItemType,
                    'info': {
                        'sid': iAnswer,
                        'amount': 1,
                        'level': dReward[iAnswer]['Level'] } }
            else:
                dTrueReward = {
                    'item': iItemType,
                    'info': {
                        'sid': iAnswer,
                        'amount': 1 } }
            lstReward = [
                dTrueReward]
        elif iAnswer in dExtraOption:
            if iAnswer == EXTRAOPTION_WEAPONUPGRADE:
                oItem = oHero.m_WieldCon.GetCurWeapon()
                oItem.Upgrade(iNotify = 0)
            elif iAnswer == EXTRAOPTION_RADOMCHOOSE and iItemType == VIRTUAL_ITEM_RELIC:
                lstRewardSID = list(dReward)
                iIndex = self.m_Game.Random(len(lstRewardSID))
                iChooseItem = lstRewardSID[iIndex]
                lstReward = [
                    {
                        'item': iItemType,
                        'info': {
                            'sid': iChooseItem,
                            'amount': 1,
                            'level': dReward[iChooseItem]['Level'] } }]
            elif iAnswer == EXTRAOPTION_CHOOSEALL:
                pass
            if iItemType == VIRTUAL_ITEM_TALENT:
                sReason = 'upgradechooseall'
                iChooseAll = 1
                self.CostChooseAllCnt(oHero, iItemType)
                for iTalent in dReward.keys():
                    lstReward.append({
                        'item': iItemType,
                        'info': {
                            'sid': iTalent,
                            'amount': 1 } })
                
        if lstReward:
            cl_reward.RewardItem(self.m_Game, oHero, lstReward, sReason, {
                'NoSendCreateRelicMsg': True })
        dData = {
            'RewardInfo': dReward,
            'RewardType': iItemType,
            'Choose': iChooseItem,
            'ChooseAll': iChooseAll }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPGRADEREWARD, oHero, dData)
        if self.ValidExtraReward(iHero):
            self.CreateExtraReward(oHero)
        else:
            self.CreateReward(oHero)

    
    def GetChooseAllRemainCnt(self, oHero, iItemType):
        iHero = oHero.m_ID
        if iHero not in self.m_ChooseAllCnt:
            return 0
        if iItemType not in self.m_ChooseAllCnt[iHero]:
            return 0
        return self.m_ChooseAllCnt[iHero][iItemType][1]

    
    def CostChooseAllCnt(self, oHero, iItemType):
        iHeroID = oHero.m_ID
        iHeroPlayerID = oHero.m_PlayerID
        (iTotalCnt, iRemainCnt) = self.m_ChooseAllCnt[iHeroID][iItemType]
        iRemainCnt -= 1
        SurvivorLog.Info('%d %d cost chooseallcnt %d %d %d' % (self.m_Game.m_ID, iHeroPlayerID, iItemType, iTotalCnt, iRemainCnt))
        self.m_ChooseAllCnt[iHeroID][iItemType] = (iTotalCnt, iRemainCnt)

    
    def SetChooseAllCnt(self, oHero, iItemType, iTotalCnt, sReason):
        iHeroID = oHero.m_ID
        iHeroPlayerID = oHero.m_PlayerID
        if iHeroID not in self.m_ChooseAllCnt:
            self.m_ChooseAllCnt[iHeroID] = { }
        SurvivorLog.Info('%d %d set chooseallcnt %d %d %s' % (self.m_Game.m_ID, iHeroPlayerID, iItemType, iTotalCnt, sReason))
        self.m_ChooseAllCnt[iHeroID][iItemType] = (iTotalCnt, iTotalCnt)

    
    def ClearChooseAllCnt(self, oHero, iItemType, sReason):
        iHeroID = oHero.m_ID
        self.SetChooseAllCnt(oHero, iItemType, 0, sReason)
        if iHeroID in self.m_CurRewardInfo and self.m_CurRewardInfo[iHeroID]:
            (iMenuIdx, iItemType, dReplaceReward, dExtraOption) = self.m_CurRewardInfo[iHeroID]
            if EXTRAOPTION_CHOOSEALL in dExtraOption:
                dExtraOption.pop(EXTRAOPTION_CHOOSEALL)
                self.m_CurRewardInfo[iHeroID] = (iMenuIdx, iItemType, dReplaceReward, dExtraOption)
                self.GS2CChooseItem(oHero, 'RefreshItem')

    
    def QueryPreviewUpgradeWeapon(self, oHero, iWeapon):
        iHero = oHero.m_ID
        if iHero not in self.m_CurRewardInfo or not self.m_CurRewardInfo[iHero]:
            SurvivorLog.Debug('%d %d noreward' % (self.m_Game.m_ID, oHero.m_PlayerID))
            return None
        (_, iItemType, _, _) = self.m_CurRewardInfo[iHero]
        if iItemType != VIRTUAL_ITEM_EQUIP:
            SurvivorLog.Debug('%d %d errtype %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iItemType))
            return None
        oWeapon = oHero.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            SurvivorLog.Debug('%d %d query noweapon %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iWeapon))
            return None
        lstAttr = []
        dPreview = oWeapon.PreviewWeaponUpgradeAttr()
        for sAttr, iValue in dPreview.items():
            (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME[sAttr]
            lstAttr.append((iIdx, iType, iLen, iValue))
        
        dAttr = {
            'Attr': lstAttr }
        cl_snetwar.GS2CPreviewUpgradeWeaponInfo(oHero.m_PlayerID, iWeapon, dAttr)



def NewSurvivorUpgradeMgr(oSurvivorElement, oData):
    return CSurvivorUpgradeMgr(oSurvivorElement, oData)

