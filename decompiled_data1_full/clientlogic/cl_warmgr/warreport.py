# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/warreport.pyc
# RelativePath: clientlogic/cl_warmgr/warreport.pyc
# Source Generated with Decompyle++
# File: warreport.pyc (Python 3.6)

from cl_commondefines import WARRIOR_BUILD_TRAP, SETTLE_FINISHWAR, SETTLE_LOSEWAR, LEVEL_TYPE_FIGHT, LEVEL_TYPE_BOSS, LEVEL_TYPE_HIDE, LEVEL_TYPE_HALL, DAM_TYPE_WEAKNESS, RESCUE_SUBMSG_SUCCESS
from cl_commondefines import TYPE_RELIFE_PF, PF_TYPE_CONSHOOT, TYPE_RELIFE_RELIC, DAM_TYPE_NORMAL, KILL_INFO_DAM_EXPLOSION, SEASONDAM_SHOW_TYPE
from cl_commondefines import KILL_INFO_ROUND_KILL_MARK, KILL_INFO_DAM_NOT_EXPLOSION, KILL_INFO_DAM3_NOT_WEAKNESS, KILL_INFO_NOT_ABNORMAL, KILL_INFO_DAM3_WEAKNESS
from cl_commondefines import VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_TALENT, ATTACKERSUBMSG_NORMAL, WARRIOR_MONSTER, WARRIOR_ELITE, WARRIOR_BOSS, BOSS_DONOT_COUNT, WARRIOR_HERO, NWARRIOR_NPC_EVENT, NWARRIOR_NPC_REFRESH, BENE_SOURCE_LAYER
from cl_warmgr.mobject import CBaseElement
from cl_only import GAME_FRAME, DeepCopy
from cl_object.logging import LevelLog
from cl_abnormalconf import g_AllAbnormalStateSID, g_AllEleAbnormalState
from cl_evcon import CheckDamIsExplosion, CheckHitWeakness, GetEleDamType
import cl_item.defines as itemdef
import cl_snetwar
import cl_msgcenter
import cllib.lib_flag
import cl_formula

class CWarReportElement(CBaseElement):
    m_CallFlag = 'WarMgr.WarreportElement'
    m_ExtDamType = {
        SEASONDAM_SHOW_TYPE: {
            4: 'SeasonSuitDamage',
            5: 'WandDamage',
            6: 'DiceDamage',
            7: 'BackpackDamage',
            8: 'S8Damage' } }
    m_DetailedSeasonDam = {
        4: 'SeasonSuitDamage',
        5: 'WandDamage',
        6: 'DiceDamage',
        7: 'BackpackDamage',
        8: 'S8Damage' }
    
    def __init__(self, oGame, nid, oData):
        super(CWarReportElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_WarReportData = CWarReportData(oGame, self)
        self.m_WarFrameSummary = None
        self.m_TotalDamage = { }
        self.m_SkillActNum = 0
        self.m_Cache = { }
        self.m_StatisticsSeasonDamage = {
            2: ('DeviceElement', self.OnSeasonDamage),
            3: ('ConquerElement', self.OnSeasonDamage),
            4: ('SeasonSuitElement', self.OnSeasonSuitDamage),
            5: ('WandElement', self.OnWandDamage),
            6: ('DiceElement', self.OnDiceDamage),
            7: ('BackpackElement', self.OnBackpackElement),
            8: ('S8Element', self.OnS8Element) }
        self.m_SeasonDamageFunc = None
        self.m_SeasonElement = None

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, 'ReportOnRemovePlayer', -1, 0, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeStart, 'ReportOnLevelInit', -1, 0, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, 'ReportOnLevelFinish', -1, 0, 1)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, 'ReportOnAddAllPlayer', -1, 0, 1)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, 'ReportOnLevelGoal', -1, 0, 1)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_KILL, self.OnKill, 'ReportKill', iSub = ATTACKERSUBMSG_NORMAL)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPONFIRE, self.OnWeaponFire, 'WeaponFire')
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_ASSISTKILL, self.OnAssistKill, 'ReportAssistKill', iSub = ATTACKERSUBMSG_NORMAL)
        self.m_Game.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_NPCCREATEOVER, self.OnCreateNpc, 'InteractNpc')

    
    def InitAfter(self):
        self.InitSeasonDamageFunc()

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, 'ReportOnRemovePlayer')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, 'ReportOnLevelInit')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'ReportOnLevelFinish')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'ReportOnAddAllPlayer')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'ReportOnLevelGoal')
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_KILL, 'ReportKill', iSub = ATTACKERSUBMSG_NORMAL)
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_WEAPONFIRE, 'WeaponFire')
        self.m_Game.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_ASSISTKILL, 'ReportAssistKill', iSub = ATTACKERSUBMSG_NORMAL)
        self.DoneAttention(self.m_WarMgr.GetRoomHero())
        self.m_WarReportData.Release()
        self.m_WarReportData = None
        if self.m_WarFrameSummary:
            self.m_WarFrameSummary.Release()
            self.m_WarFrameSummary = None
        self.m_WarMgr = None
        self.m_StatisticsSeasonDamage = { }
        self.m_SeasonDamageFunc = None
        self.m_SeasonElement = None
        super(CWarReportElement, self).Release()

    
    def AddAttention(self, lstHero):
        oWarMgr = self.m_WarMgr
        for iHero in lstHero:
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_AFTERADDCASH, self.OnAddCash, 'ReportAddCash')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDGSCASH, self.OnAddGSCash, 'ReportAddGSCash')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CONSUMEGSCASH, self.OnConsumeCash, 'ReportConsumeGSCash')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealDamage, 'ReportDealDamage', iSub = ATTACKERSUBMSG_NORMAL)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PFNODEKILL, self.OnPFNodeKill, 'ReportPFNodeKill')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELIC, self.OnRewardRelic, 'ReportReward')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDTALENT, self.OnRewardTalent, 'ReportReward')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_WIELDWEAPON, self.OnWieldWeapon, 'ReportWieldWeapon')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, self.OnDie, 'ReportDie')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, 'ReportRelife')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVERELIC, self.OnRemoveRelic, 'ReportRemoveRelic')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HP_CHANGE, self.OnHpModify, 'ReportHpChange')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RECEIVEDAMED, self.OnReceiveDam, 'ReportReceiveDam')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, self.OnAttack, 'ReportAttack')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnPerform, 'ReportPerform')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, 'ReportEnterScene')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OnLeaveScene, 'ReportLeaveScene')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, self.OnShieldRecover, 'ReportShieldRecover')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, self.OnTalentChoose, 'ReportTalentChoose')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TALENT_GEN_CHANGE, self.OnTalentGenChange, 'ReportTalentGenChange')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, self.OnDebuff, 'ReportDebuff')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RESCUE, self.OnSuccessSave, 'ReportSave', iSub = RESCUE_SUBMSG_SUCCESS)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_OPEN_BEFOR_BENED, self.OnBenedGen, 'ReportBenedGen')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDSUIT, self.OnAddSuit, 'ReportAddSuit')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CHOOSEBENED, self.OnChooseBened, 'ReportChooseBened')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADEREWARD_CHOOSE, self.OnChooseUpGradeReward, 'ReportChooseUpGradeReward')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADEREWARD, self.OnUpGradeReward, 'ReportUpGradeReward')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TALENT_GEN, self.OnRareTalentGen, 'ReportRareTalentGen')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRAREGOLDENCUP, self.OnAddRareGoldenCup, 'ReportAddRareGoldenCup')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_COMMONTALENT_GEN, self.OnCommonTalentGen, 'CommonTalentGen')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDBENED, self.OnAddBened, 'ReportAddBened')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TAKEOVERHERO, self.OnTakeOverHero, 'ReportTakeOverHero')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDOVERHERO, self.OnHandOverHero, 'ReportHandOverHero')
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CREATEGOLDENCUP, self.OnCreateGoldencup, 'ReportCreateGoldencup')
        

    
    def DoneAttention(self, lstHero):
        oWarMgr = self.m_WarMgr
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_AFTERADDCASH, 'ReportAddCash')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDGSCASH, 'ReportAddGSCash')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CONSUMEGSCASH, 'ReportConsumeGSCash')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, 'ReportDealDamage', iSub = ATTACKERSUBMSG_NORMAL)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PFNODEKILL, 'ReportPFNodeKill')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRELIC, 'ReportReward')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDTALENT, 'ReportReward')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_WIELDWEAPON, 'ReportWieldWeapon')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_DIE, 'ReportDie')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RELIFE, 'ReportRelife')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_REMOVERELIC, 'ReportRemoveRelic')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HP_CHANGE, 'ReportHpChange')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RECEIVEDAMED, 'ReportReceiveDam')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ATTACK, 'ReportAttack')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_PERFORM_START, 'ReportPerform')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, 'ReportEnterScene')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_LEAVESCENE, 'ReportLeaveScene')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_SHIELD_RECOVER, 'ReportShieldRecover')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TALENT_CHOOSE, 'ReportTalentChoose')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TALENT_GEN_CHANGE, 'ReportTalentGenChange')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, 'ReportDebuff')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RESCUE, 'ReportSave', iSub = RESCUE_SUBMSG_SUCCESS)
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_OPEN_BEFOR_BENED, 'ReportBenedGen')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDSUIT, 'ReportAddSuit')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADEREWARD_CHOOSE, 'ReportChooseUpGradeReward')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_UPGRADEREWARD, 'ReportUpGradeReward')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TALENT_GEN, 'ReportRareTalentGen')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDRAREGOLDENCUP, 'ReportAddRareGoldenCup')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_COMMONTALENT_GEN, 'CommonTalentGen')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_ADDBENED, 'ReportAddBened')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_TAKEOVERHERO, 'ReportTakeOverHero')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_HANDOVERHERO, 'ReportHandOverHero')
            cl_msgcenter.DoneAttention(oWarMgr, iHero, cl_msgcenter.MSG_WAR_CREATEGOLDENCUP, 'ReportCreateGoldencup')
        

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        if self.m_WarMgr.IsSingleGame():
            self.m_WarFrameSummary = CSingleFrameSummary(self.m_Game)
        else:
            self.m_WarFrameSummary = CTeamFrameSummary(self.m_Game)
        self.m_WarFrameSummary.m_TotalFrame = self.m_WarReportData.m_InitStartFrame
        lstHero = self.m_WarMgr.GetRoomHero()
        self.AddAttention(lstHero)
        if not self.m_TotalDamage:
            self.m_TotalDamage = dict.fromkeys(lstHero, 0)
        else:
            for iHero in lstHero:
                if iHero in self.m_TotalDamage:
                    continue
                LevelLog.Debug('%d totaldam err %d' % (self.m_Game.m_ID, iHero))
                self.m_TotalDamage[iHero] = 0
            
        for pid in self.m_WarMgr.GetAllPlayer():
            if pid not in self.m_Cache:
                self.m_Cache[pid] = { }
        

    
    def OnRemovePlayer(self, oWarMgr, dInfo):
        self.DoneAttention([
            dInfo['Hero']])

    
    def Save(self, iPlayer, dInfo = None):
        dData = self.m_WarReportData.SavePlayerWarData(iPlayer, dInfo)
        dTeamDam = { }
        oWarMgr = self.m_WarMgr
        lstPlayer = oWarMgr.GetAllPlayer()
        for pid in lstPlayer:
            oHero = oWarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            dTeamDam[pid] = self.m_TotalDamage[oHero.m_ID]
        
        dData['TeamDam'] = dTeamDam
        dData['Cache'] = self.m_Cache
        return DeepCopy(dData)

    
    def Load(self, iPlayer, dData):
        if 'WarData' in dData:
            return None
        oWarMgr = self.m_WarMgr
        dTeamDam = dData.get('TeamDam', { })
        for pid in dTeamDam:
            oHero = oWarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            self.m_TotalDamage[oHero.m_ID] = dTeamDam[pid]
        
        if 'Cache' in dData:
            self.m_Cache = dData['Cache']
        self.m_WarReportData.ReBuildPlayerWarData(iPlayer, dData)

    
    def OnLevelGoal(self, oWarMgr, dInfo):
        lstPlayer = self.m_WarMgr.GetRoomPlayer()
        iLevelID = dInfo['LevelID']
        iPassLevel = dInfo['PassLevel']
        iScene = dInfo['Scene']
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene or not oScene.GetObjectsByType('Hero'):
            return None
        if iPassLevel:
            self.m_WarReportData.SetLevelResult(iLevelID, lstPlayer, SETTLE_FINISHWAR)

    
    def OnLevelNodeStart(self, oWarMgr, dInfo):
        lstPlayer = self.m_WarMgr.GetAllPlayer()
        iLevelID = dInfo['LevelID']
        dInfo['LevelID'] = self.GetConfigLevel(iLevelID)
        self.m_WarReportData.StartLevelSummary(lstPlayer, dInfo)
        self.m_WarReportData.SetLevelResult(iLevelID, lstPlayer, SETTLE_LOSEWAR)

    
    def OnLevelNodeFinish(self, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        oReport = self.m_WarReportData.GetLayerLevelReport(iLevel)
        if oReport:
            lstPlayer = oReport.GetAllReportPlayer()
        else:
            lstPlayer = self.m_WarMgr.GetAllPlayer()
            LevelLog.Alert('%s no report %s %s' % (self.m_Game.m_ID, lstPlayer, dInfo))
        self.m_WarReportData.FinishLevelSummary(lstPlayer, dInfo)
        oWarFrameSummary = self.m_WarFrameSummary
        for pid in lstPlayer:
            iFrame = oWarFrameSummary.GetTrusteeshipFrame(pid)
            if iFrame > 0:
                self.m_WarReportData.SummaryWarInfo(pid, 'TrusteeshipFrame', iFrame)
        

    
    def GetCurHeroLevel(self, oHero):
        oScene = self.m_Game.m_SceneMgr.GetScene(oHero.m_Scene)
        if not oScene:
            return None
        iLevel = self.GetConfigLevel(oScene.m_Level)
        return iLevel

    
    def PausePlayFrameCounting(self):
        if self.m_WarFrameSummary:
            self.m_WarFrameSummary.PauseCounting()

    
    def ResumePlayFrameCounting(self):
        if self.m_WarFrameSummary:
            self.m_WarFrameSummary.ResumeCounting()

    
    def OnAddRareGoldenCup(self, oWarMgr, oHero, dInfo):
        iNpc = dInfo['NPC']
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryRareGoldenCup(iLevel, oHero.m_PlayerID, iNpc)

    
    def OnRareTalentGen(self, oWarMgr, oHero, dInfo):
        sReason = dInfo['Reason']
        iNpc = dInfo['NPC']
        dTalent = dInfo['Talent']
        iLevel = self.GetCurHeroLevel(oHero)
        if sReason == 'RewardChooseRareTalentGame':
            lstTalent = list(dTalent)
            self.m_WarReportData.SummaryRareTalentGen(iLevel, oHero.m_PlayerID, iNpc, lstTalent)

    
    def OnCommonTalentGen(self, oWarMgr, oHero, dInfo):
        lstTalent = dInfo['CommonTalentGen']
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'CommonTalentGen', lstTalent, bDeduplication = False)

    
    def OnChooseUpGradeReward(self, oWarMgr, oHero, dInfo):
        lstReward = dInfo['lstReward']
        iType = dInfo['RewardType']
        iLevel = self.GetCurHeroLevel(oHero)
        if iType == VIRTUAL_ITEM_RELIC:
            sAttr = 'UpGradeRelicGen'
        elif iType == VIRTUAL_ITEM_TALENT:
            sAttr = 'UpGradeTalentGen'
        else:
            return None
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, sAttr, lstReward, bDeduplication = False)

    
    def GetHeroUpGradeWeapon(self, oHero):
        oWeapon = oHero.m_WieldCon.GetCurWeapon()
        if not oWeapon:
            return None
        if oWeapon.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
            return None
        return oWeapon

    
    def OnUpGradeReward(self, oWarMgr, oHero, dInfo):
        dReward = dInfo['RewardInfo']
        lstReward = list(dReward)
        iType = dInfo['RewardType']
        iLevel = self.GetCurHeroLevel(oHero)
        lstData = []
        iChoose = dInfo['Choose']
        iChooseAll = dInfo['ChooseAll']
        if iType == VIRTUAL_ITEM_EQUIP:
            for iWeapon, dWeaponInfo in dReward.items():
                oWeapon = dWeaponInfo['Item']
                iGrade = oWeapon.m_BaseGrade
                tWeaponInfo = (iWeapon, iGrade, 0)
                lstData.append(tWeaponInfo)
            
            oUpGradeWeapon = self.GetHeroUpGradeWeapon(oHero)
            if oUpGradeWeapon:
                tWeaponInfo = (oUpGradeWeapon.m_SID, oUpGradeWeapon.m_BaseGrade, 1)
                lstData.append(tWeaponInfo)
            self.m_WarReportData.SummaryUpGradeWeaponGen(iLevel, oHero.m_PlayerID, lstData)
            if iChoose not in lstReward:
                oItem = oHero.m_WieldCon.GetCurWeapon()
                iUpGrade = 1
            else:
                oItem = dReward[iChoose]['Item']
                iUpGrade = 0
            tWeaponInfo = (oItem.m_SID, oItem.m_BaseGrade, iUpGrade)
            self.m_WarReportData.SummaryUpGradeWeapon(iLevel, oHero.m_PlayerID, tWeaponInfo)
            return None
        if iType == VIRTUAL_ITEM_RELIC:
            sAttr = 'UpGradeRelic'
        elif iType == VIRTUAL_ITEM_TALENT:
            sAttr = 'UpGradeTalent'
        if not iChooseAll:
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, sAttr, iChoose)
        else:
            for iReward in lstReward:
                self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, sAttr, iReward)
            

    
    def OnAddCash(self, oWarMgr, oHero, dInfo):
        iCash = dInfo['Cash']
        if iCash > 0:
            iLevel = self.GetCurHeroLevel(oHero)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Cash', iCash)

    
    def OnAddGSCash(self, oWarMgr, oHero, dInfo):
        iCash = dInfo['Cash']
        if iCash > 0:
            iLevel = self.GetCurHeroLevel(oHero)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'GSCash', iCash)

    
    def OnConsumeCash(self, oWarMgr, oHero, dInfo):
        iCash = dInfo['Cash']
        if iCash > 0:
            iLevel = self.GetCurHeroLevel(oHero)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'GSCash', -iCash)

    
    def OnDealDamage(self, oWarMgr, oHero, dInfo):
        if oHero.m_ID == dInfo['CurVID']:
            return None
        iTotalDam = cl_formula.CalDealTotalDam(dInfo)
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Damage', iTotalDam)
        self.m_TotalDamage[oHero.m_ID] += iTotalDam
        if self.m_SeasonDamageFunc:
            self.m_SeasonDamageFunc(oHero, self.m_SeasonElement, iTotalDam, dInfo)
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        if 'ItemID' not in oSkill.m_Cache:
            return None
        iItemID = oSkill.m_Cache['ItemID']
        iItemSID = oSkill.m_Cache['ItemSID']
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'WeaponDamage', iItemID, iTotalDam, iItemSID = iItemSID)
        if cllib.lib_flag.g_IsAuthorityRun:
            self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'WeaponDamage', iTotalDam)

    
    def InitSeasonDamageFunc(self):
        iSeasonNum = self.m_Game.m_WarMgr.m_SeasonNum
        if iSeasonNum not in self.m_StatisticsSeasonDamage:
            return None
        (sElementName, func) = self.m_StatisticsSeasonDamage[iSeasonNum]
        oSeasonElement = self.m_Game.m_WarMgr.GetComponent(sElementName)
        if not oSeasonElement or not oSeasonElement.CheckEnable():
            return None
        self.m_SeasonDamageFunc = func
        self.m_SeasonElement = oSeasonElement

    
    def OnSeasonDamage(self, oHero, _oSeasonElement, iTotalDam, dInfo):
        if 'OriginalAID' not in dInfo:
            return None
        if dInfo['OriginalAID'] == dInfo['CurVID']:
            return None
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'SeasonDamage', iTotalDam)

    
    def OnSeasonSuitDamage(self, oHero, oSeasonElement, iTotalDam, dInfo):
        if 'Skill' not in dInfo:
            return None
        iSuit = oSeasonElement.GetDamageSourceSuit(oHero.m_ID, dInfo['Skill'])
        if not iSuit:
            return None
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'SeasonDamage', iTotalDam)
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'SeasonSuitDamage', {
            iSuit: iTotalDam })

    
    def OnWandDamage(self, oHero, oSeasonElement, iTotalDam, dInfo):
        dDamageInfo = oSeasonElement.GetWandDamageInfo(iTotalDam, dInfo)
        if not dDamageInfo:
            return None
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'SeasonDamage', iTotalDam)
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'WandDamage', dDamageInfo)

    
    def OnDiceDamage(self, oHero, oSeasonElement, iTotalDam, dInfo):
        dDamageInfo = oSeasonElement.GetDiceDamageInfo(iTotalDam, dInfo)
        if not dDamageInfo:
            return None
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'SeasonDamage', iTotalDam)
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'DiceDamage', dDamageInfo)

    
    def OnBackpackElement(self, oHero, oSeasonElement, iTotalDam, dInfo):
        dDamageInfo = oSeasonElement.GetBackpackDamageInfo(iTotalDam, dInfo)
        if not dDamageInfo:
            return None
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'SeasonDamage', iTotalDam)
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'BackpackDamage', dDamageInfo)

    
    def OnS8Element(self, oHero, oSeasonElement, iTotalDam, dInfo):
        dDamageInfo = oSeasonElement.GetS8DamageInfo(iTotalDam, dInfo)
        if not dDamageInfo:
            return None
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'SeasonDamage', iTotalDam)
        self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'S8Damage', dDamageInfo)

    
    def OnPFNodeKill(self, oWarMgr, oHero, dInfo):
        oVictim = self.m_Game.GetObject(dInfo['VID'])
        if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
            return None
        iTotalDam = oVictim.HP() + oVictim.Shield() + oVictim.Armor()
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Damage', iTotalDam)
        self.m_TotalDamage[oHero.m_ID] += iTotalDam

    
    def OnKill(self, oWarMgr, oKiller, dInfo):
        if not oKiller:
            return None
        oGame = self.m_Game
        oTarget = oGame.GetObject(dInfo['VID'])
        if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
            return None
        lstHero = oGame.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            if oTarget.Query('Injured%d' % iHero):
                break
        else:
            return None
        iLevel = self.GetCurHeroLevel(oTarget)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oKiller.m_PlayerID, 'OwnKill', 1)
        lstHero = self.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Kill', 1)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'KillMonster', oTarget.m_DataSID, 1)
            if cllib.lib_flag.g_IsAuthorityRun:
                if oTarget.m_SuperLevel > 0:
                    tKillMonsterSIDAndSuper = (oTarget.m_SID, 1)
                else:
                    tKillMonsterSIDAndSuper = (oTarget.m_SID, 0)
                self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'KillMonsterSIDAndSuper', tKillMonsterSIDAndSuper, 1)
            if oTarget.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'KillElite', 1)
            if oTarget.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS and oTarget.m_FightType not in BOSS_DONOT_COUNT:
                self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'KillBoss', 1)
                self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'KillBossDetail', oTarget.m_SID, 1)
                dExtraInfo = self.m_WarMgr.m_ExtraInfo
                if dExtraInfo.get('NewVerLayer', 0) and not self.m_WarMgr.IsEndless():
                    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
                    self.m_WarReportData.SummaryWarInfo(oHero.m_PlayerID, 'PassNewVerLayer', [
                        oLevelCtrl.m_LayerNum])
        
        if oKiller.m_FightType == WARRIOR_HERO:
            self.RecordKillMonsterInfo(iLevel, oKiller, oTarget, dInfo)

    
    def OnAssistKill(self, oWarMgr, oAssist, dInfo):
        if not oAssist:
            return None
        oGame = self.m_Game
        oTarget = oGame.GetObject(dInfo['VID'])
        if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
            return None
        iLevel = self.GetCurHeroLevel(oTarget)
        if oTarget.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            self.m_WarReportData.SummaryLevelInfo(iLevel, oAssist.m_PlayerID, 'AssistKillElite', 1)
        if oTarget.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS and oTarget.m_FightType not in BOSS_DONOT_COUNT:
            self.m_WarReportData.SummaryLevelInfo(iLevel, oAssist.m_PlayerID, 'AssistKillBoss', 1)

    
    def RecordKillMonsterInfo(self, iLevel, oHero, oMonster, dMsgInfo):
        oReport = self.m_WarReportData.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        pid = oHero.m_PlayerID
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        if 'UnlockMonster' not in dPlayerData:
            return None
        dAllKillMonsterInfo = dPlayerData['UnlockMonster']
        dKillMonsterInfo = dAllKillMonsterInfo.setdefault(oMonster.m_DataSID, { })
        oGame = self.m_Game
        iRound = oGame.m_WarMgr.m_Round
        oEventCB = cl_msgcenter.eventcbobj.CEventCB(None, 'KillMonsterInfo')
        oEventCB.InitEventCBInfo({ }, dMsgInfo)
        dKillMonsterInfo2 = dKillMonsterInfo.setdefault(iRound, { })
        dKillMonsterInfo2.setdefault(KILL_INFO_ROUND_KILL_MARK, 0)
        dKillMonsterInfo2[KILL_INFO_ROUND_KILL_MARK] += 1
        lstState = oMonster.m_State.Values()
        iAbnormal = 0
        for oState in lstState:
            if oState.m_SID in g_AllAbnormalStateSID:
                iAbnormal |= g_AllEleAbnormalState[oState.m_SID]
        
        if iAbnormal == 0:
            iAbnormal = KILL_INFO_NOT_ABNORMAL
        dKillMonsterInfo2.setdefault(iAbnormal, 0)
        dKillMonsterInfo2[iAbnormal] += 1
        iDamType = KILL_INFO_DAM_NOT_EXPLOSION
        if CheckDamIsExplosion(oHero, oEventCB):
            iDamType = KILL_INFO_DAM_EXPLOSION
        dKillMonsterInfo2.setdefault(iDamType, 0)
        dKillMonsterInfo2[iDamType] += 1
        iDamType2 = GetEleDamType(oHero, oEventCB)
        iDamType2 = iDamType2 if iDamType2 != 0 else DAM_TYPE_NORMAL
        dKillMonsterInfo2.setdefault(iDamType2, 0)
        dKillMonsterInfo2[iDamType2] += 1
        iDamType3 = KILL_INFO_DAM3_NOT_WEAKNESS
        if CheckHitWeakness(oHero, oEventCB):
            iDamType3 = KILL_INFO_DAM3_WEAKNESS
        dKillMonsterInfo2.setdefault(iDamType3, 0)
        dKillMonsterInfo2[iDamType3] += 1

    
    def OnRewardRelic(self, oWarMgr, oHero, dInfo):
        iPerform = dInfo['iPerform']
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Relic', iPerform)
        if dInfo['Reason'] == 'upgradechoose':
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'UpGradeRelic', iPerform)

    
    def OnAddSuit(self, oWarMgr, oHero, dInfo):
        iSuit = dInfo['SuitID']
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'AddSuit', iSuit)

    
    def OnChooseBened(self, oWarMgr, oHero, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = oLevelCtrl.m_LayerNum if oLevelCtrl else 0
        if iLayer != 4:
            return None
        iBene = dInfo['Bene']
        if 'ReplaceInfo' in dInfo:
            (iReplace, iPos) = dInfo['ReplaceInfo']
            sInfo = '%s_%s_%s' % (iBene, iPos, iReplace)
        else:
            sInfo = '%s_null_null' % iBene
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'FourthBened', sInfo)

    
    def OnAddBened(self, oWarMgr, oHero, dInfo):
        iBenediction = dInfo['Bene']
        pid = oHero.m_PlayerID
        dGotBened = {
            iBenediction: 1 }
        self.m_WarReportData.SummaryWarInfo(pid, 'AllGotBened', dGotBened)

    
    def OnTakeOverHero(self, oWarMgr, oHero, dInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if oLevelCtrl.m_CurLType == LEVEL_TYPE_HALL:
            return None
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        pid = oHero.m_PlayerID
        self.m_WarFrameSummary.m_TakeOverStartFrame[pid] = iCurFrame

    
    def OnHandOverHero(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        iFrame = self.m_WarFrameSummary.GetTrusteeshipFrame(pid)
        if iFrame > 0:
            self.m_WarReportData.SummaryWarInfo(pid, 'TrusteeshipFrame', iFrame)

    
    def OnCreateGoldencup(self, oWarMgr, oHero, dInfo):
        pid = oHero.m_PlayerID
        self.m_WarReportData.SummaryWarInfo(pid, 'CreateGoldencupCount', 1)

    
    def OnRewardTalent(self, oWarMgr, oHero, dInfo):
        iTalent = dInfo['iPerform']
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SetPlayerWarInfo(oHero.m_PlayerID, 'LastTalent', iTalent)
        for _ in range(dInfo['CurLevel'], dInfo['Level']):
            self.m_WarReportData.SummaryTalent(iLevel, oHero.m_PlayerID, iTalent)
        

    
    def OnWieldWeapon(self, oWarMgr, oHero, dInfo):
        iType = dInfo['Type']
        iFirst = dInfo['FirstAdd']
        iLevel = self.GetCurHeroLevel(oHero)
        if iType & itemdef.EQUIP_TYPE_MAINWEAPON == itemdef.EQUIP_TYPE_MAINWEAPON and iFirst:
            iItemSID = dInfo['SID']
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Weapon', iItemSID, 1)

    
    def OnTalentChoose(self, oWarMgr, oHero, dInfo):
        sReason = dInfo['Reason']
        if sReason == 'RewardChooseRareTalentGame':
            iNpc = dInfo['NpcID']
            iTalent = dInfo['Choose']
            iLevel = self.GetCurHeroLevel(oHero)
            self.m_WarReportData.SummaryRareTalent(iLevel, oHero.m_PlayerID, iNpc, iTalent)

    
    def OnTalentGenChange(self, oWarMgr, oHero, dInfo):
        lstTalent = dInfo['Talents']
        if not lstTalent:
            return None
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'TalentGen', lstTalent, bDeduplication = False)

    
    def OnDebuff(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        if 'ItemID' not in oSkill.m_Cache:
            return None
        iItemID = oSkill.m_Cache['ItemID']
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'DebuffTimes', iItemID, 1)

    
    def OnSuccessSave(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'SavingTimes', 1)

    
    def OnEnterScene(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iPlayer = oHero.m_PlayerID
        oOldScene = self.m_Game.m_SceneMgr.GetScene(dInfo['OldScene'])
        if oOldScene:
            iOldLevel = self.GetConfigLevel(oOldScene.m_Level)
            self.m_WarReportData.SummaryLevelStayTime(iOldLevel, iPlayer, 0)
        self.m_WarReportData.SummaryLevelStayTime(iLevel, iPlayer, 1)
        if oLevelNode and oLevelNode.m_LevelType == LEVEL_TYPE_HIDE:
            self.m_WarReportData.SummaryLevelInfo(iLevel, iPlayer, 'EnterHide', iLevel)

    
    def OnDie(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Die', 1)
        oSurvivorElement = oWarMgr.GetSurvivorElement()
        if oSurvivorElement:
            iPhase = oWarMgr.GetBigDataPhase(oSurvivorElement)
            self.m_WarReportData.SummaryLevelPhaseDieInfo(iLevel, oHero.m_PlayerID, iPhase)

    
    def OnRelife(self, oWarMgr, oHero, dInfo):
        oReason = dInfo['RS']
        iAID = dInfo['AID']
        oSaver = self.m_Game.GetObject(iAID)
        if not oSaver:
            return None
        iType = oReason.Query('Type', 0)
        iLevel = self.GetCurHeroLevel(oHero)
        if iType in (TYPE_RELIFE_RELIC,):
            self.m_WarReportData.SummaryLevelInfo(iLevel, oSaver.m_PlayerID, 'RelicRelife', 1)
        if iType != TYPE_RELIFE_PF:
            return None
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryLevelInfo(iLevel, oSaver.m_PlayerID, 'Save', 1)

    
    def OnRemoveRelic(self, oWarMgr, oHero, dInfo):
        if not dInfo['Force']:
            iLevel = self.GetCurHeroLevel(oHero)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'RemoveRelic', dInfo['iPerform'], 1)

    
    def OnHpModify(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        if 'TotalCure' in dInfo:
            (iShield, iArmor, iHp) = dInfo['TotalCure']
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'ShieldUp', iShield)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'HpUp', iHp)
        if 'TotalDam' in dInfo:
            (iShield, iArmor, iHp) = dInfo['TotalDam']
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'ShieldDown', iShield)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'HpDown', iHp)
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'Injured', iHp + iShield)
            iAttack = dInfo['AID']
            oAttack = self.m_Game.GetObject(iAttack)
            if oAttack and oAttack.m_FightType & WARRIOR_BUILD_TRAP == WARRIOR_BUILD_TRAP:
                self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'InjuredByTrap', iHp + iArmor + iShield)

    
    def OnReceiveDam(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        iShield = oHero.Shield()
        self.m_WarReportData.SummaryFightTime(iLevel, oHero.m_PlayerID)
        self.m_WarReportData.SummaryShieldUp(iLevel, oHero.m_PlayerID, iShield)

    
    def OnWeaponFire(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iItemID = oSkill.m_Cache['ItemID']
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'FireTimes', iItemID, 1)

    
    def OnAttack(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryFightTime(iLevel, oHero.m_PlayerID)
        if 'Skill' not in dInfo:
            return None
        oSkill = dInfo['Skill']
        iSkillActNum = oSkill.m_Base['ActNum']
        pfType = oSkill.m_Base['PFType']
        if 'ItemID' not in oSkill.m_Cache:
            return None
        iItemID = oSkill.m_Cache['ItemID']
        oReason = dInfo['RS']
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'HitTimes', iItemID, 1)
        if self.m_SkillActNum != iSkillActNum or pfType == PF_TYPE_CONSHOOT:
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'CauseDamageTimes', iItemID, 1)
            self.m_SkillActNum = iSkillActNum
        if oReason.Query('DamType') & DAM_TYPE_WEAKNESS:
            self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'WeaknessTimes', iItemID, 1)

    
    def OnPerform(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        self.m_WarReportData.SummaryFightTime(iLevel, oHero.m_PlayerID)

    
    def OnLeaveScene(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        iShield = oHero.Shield()
        self.m_WarReportData.SummaryShieldUp(iLevel, oHero.m_PlayerID, iShield)

    
    def OnShieldRecover(self, oWarMgr, oHero, dInfo):
        iShield = oHero.Shield()
        self.m_WarReportData.StartShieldSummary(oHero.m_PlayerID, iShield)

    
    def OnReportFPS(self, oHero, iScene, iAve, iBelowLowRatio, iLowRatio, iMidRatio, iHighRatio, iAboveHighRatio, iGear, iMemoryUsage):
        oReportScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        if not oReportScene:
            return None
        iReportLevel = self.GetConfigLevel(oReportScene.m_Level)
        iLevel = self.GetCurHeroLevel(oHero)
        if iLevel != iReportLevel:
            LevelLog.Debug('%s fps report err %s %s' % (oHero.m_PlayerID, iReportLevel, iLevel))
        dFPS = {
            'ave_fps': iAve,
            'fps_rate_30': iBelowLowRatio,
            'fps_rate_40': iLowRatio,
            'fps_rate_50': iMidRatio,
            'fps_rate_60': iHighRatio,
            'above60fps_rate': iAboveHighRatio,
            'fps_gear': iGear }
        dSystemInfo = { }
        self.m_WarReportData.SummaryLevelInfo(iReportLevel, oHero.m_PlayerID, 'FPS', dFPS)
        self.m_WarReportData.SummaryLevelInfo(iReportLevel, oHero.m_PlayerID, 'SystemInfo', dSystemInfo)

    
    def OnBenedGen(self, oWarMgr, oHero, dInfo):
        iLevel = self.GetCurHeroLevel(oHero)
        lstBened = list(dInfo['BenedOp'])
        self.m_WarReportData.SummaryLevelInfo(iLevel, oHero.m_PlayerID, 'BenedGen', lstBened, bDeduplication = False)

    
    def GetTotalDamage(self):
        lstDamage = []
        for iHero, iDamage in self.m_TotalDamage.items():
            lstDamage.append((iHero, iDamage // 100))
        
        return lstDamage

    
    def GetTotalDamageByHeroID(self, iHeroID):
        if iHeroID not in self.m_TotalDamage:
            return 0
        return self.m_TotalDamage[iHeroID]

    
    def GetAllTotalDamage(self):
        lstDamage = []
        oWarMgr = self.m_WarMgr
        oWarMgrReportData = self.m_WarReportData
        iSeasonNowNum = self.m_Game.m_WarMgr.m_SeasonNum
        for iHero, iDamage in self.m_TotalDamage.items():
            pid = oWarMgr.GetPlayerIDByHeroID(iHero)
            iSeasonDamage = oWarMgrReportData.GetPlayerWarInfo(pid, 'SeasonDamage', default = 0)
            dExtDamInfo = { }
            for iType, dSeasonKeyInfo in self.m_ExtDamType.items():
                if iSeasonNowNum not in dSeasonKeyInfo:
                    continue
                dInfo = oWarMgrReportData.GetPlayerWarInfo(pid, dSeasonKeyInfo[iSeasonNowNum], default = { })
                if dInfo:
                    dSendInfo = { }
                    for iKey, iDam in dInfo.items():
                        dSendInfo[iKey] = iDam // 100
                    
                dExtDamInfo[iType] = dSendInfo
            
            lstDamage.append((iHero, iDamage // 100, iSeasonDamage // 100, dExtDamInfo))
        
        return lstDamage

    
    def GetConfigLevel(self, iLevel):
        oLevelCtrl = self.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return iLevel
        return oLevelCtrl.GetConfigLevel(iLevel)

    
    def OnCreateNpc(self, oWarMgr, oNpc, dMsgInfo):
        if oNpc.m_FightType != NWARRIOR_NPC_EVENT and oNpc.m_FightType != NWARRIOR_NPC_REFRESH:
            return None
        iLevel = self.GetCurHeroLevel(oNpc)
        oReport = self.m_WarReportData.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        lstPlayer = oWarMgr.GetRoomPlayer()
        for pid in lstPlayer:
            if pid not in oReport.m_PlayerData:
                continue
            dPlayerData = oReport.m_PlayerData[pid]
            if 'EventNpc' not in dPlayerData:
                continue
            dNpc = dPlayerData['EventNpc']
            dNpc[oNpc.m_ID] = {
                'NpcSID': oNpc.m_SID,
                'option_id': [],
                'choose_id': [] }
            cl_msgcenter.AddAttentionFunc(oWarMgr, oNpc.m_ID, cl_msgcenter.MSG_WAR_EVENTNPC_REFRESH, self.OnNpcRefresh, 'ReportNpcInteract')
            cl_msgcenter.AddAttentionFunc(oWarMgr, oNpc.m_ID, cl_msgcenter.MSG_WAR_EVENTNPC_CHOOSE, self.OnNpcChooseOption, 'ReportNpcChoose')
        

    
    def OnNpcRefresh(self, oWarMgr, oNpc, dMsgInfo):
        iLevel = self.GetCurHeroLevel(oNpc)
        oReport = self.m_WarReportData.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        pid = dMsgInfo['pid']
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        if 'EventNpc' not in dPlayerData:
            return None
        dNpc = dPlayerData['EventNpc']
        if oNpc.m_ID not in dNpc:
            return None
        dNpc[oNpc.m_ID]['option_id'] = []
        lstAllOption = dMsgInfo['AllOption']
        for lstData in lstAllOption:
            iOp = lstData[0]
            iValid = lstData[1]
            iOp = iOp if iValid or iOp == -1 else iOp + 1
            dNpc[oNpc.m_ID]['option_id'].append(iOp)
        

    
    def OnNpcChooseOption(self, oWarMgr, oNpc, dMsgInfo):
        iLevel = self.GetCurHeroLevel(oNpc)
        oReport = self.m_WarReportData.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        pid = dMsgInfo['pid']
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        if 'EventNpc' not in dPlayerData:
            return None
        dNpc = dPlayerData['EventNpc']
        if oNpc.m_ID not in dNpc:
            return None
        iOp = dMsgInfo['Option']
        iOp = iOp if iOp == -1 else iOp + 1
        dNpc[oNpc.m_ID]['choose_id'].append(iOp)



class CWarReportData(object):
    
    def __init__(self, oGame, oCtrl):
        self.m_Game = oGame
        self.m_ReportCtrl = oCtrl
        self.m_LevelReport = { }
        self.m_Index2Level = { }
        self.m_CurIndex = (1, 0)
        self.m_ShieldTmp = { }
        self.m_WarData = {
            'PlayerData': { } }
        self.m_InitStartFrame = 0

    
    def Release(self):
        for oReport in self.m_LevelReport.values():
            oReport.Release()
        
        self.m_LevelReport = { }
        self.m_Index2Level = { }

    
    def StartLevelSummary(self, lstPlayer, dInfo):
        iLevel = dInfo['LevelID']
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iCurMainLevel = oLevelCtrl.m_CurNode.m_Level if oLevelCtrl and oLevelCtrl.m_CurNode else 0
        if iLevel == iCurMainLevel:
            for oReprot in self.m_LevelReport.values():
                oReprot.Release()
            
            self.m_LevelReport = { }
            self.m_Index2Level = { }
        iLevelType = dInfo['LevelType']
        iLayerNum = dInfo['Layer']
        iLevelNum = dInfo['Level']
        tLevelIndex = (iLayerNum, iLevelNum)
        self.m_CurIndex = tLevelIndex
        tLayerLevelID = (iLayerNum, iLevel)
        if tLayerLevelID in self.m_LevelReport:
            return None
        oReport = CLevelReportData(self.m_Game, lstPlayer, iLevelType, iLevel, tLevelIndex)
        self.m_LevelReport[tLayerLevelID] = oReport
        lstLevel = self.m_Index2Level.setdefault(tLevelIndex, [])
        lstLevel.append(iLevel)

    
    def GetLayerLevelReport(self, iLevel):
        iLayerNum = self.m_CurIndex[0]
        tLayerLevelID = (iLayerNum, iLevel)
        if tLayerLevelID in self.m_LevelReport:
            return self.m_LevelReport[tLayerLevelID]

    
    def FinishLevelSummary(self, lstPlayer, dInfo):
        lstLevel = self.m_Index2Level.get(self.m_CurIndex, [])
        iPlayFrame = self.m_ReportCtrl.m_WarFrameSummary.GetCurLevelFrame()
        for iLevel in lstLevel:
            oReport = self.GetLayerLevelReport(iLevel)
            if not oReport:
                continue
            oReport.m_PlayFrame = iPlayFrame
            for pid in lstPlayer:
                self.SummaryLevelStayTime(iLevel, pid, 0)
                self.SummaryLevelSuit(iLevel, pid)
            
        
        for pid in lstPlayer:
            self.m_ReportCtrl.m_Cache[pid] = self.GetPlayerWarStatistics(pid)
        
        for iLevel in lstLevel:
            oReport = self.GetLayerLevelReport(iLevel)
            if oReport:
                oReport.m_Finish = 1
        

    
    def SummaryLevelInfo(self, iLevel, pid, sAttr, *tArgs, **kwargs):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        if sAttr not in dPlayerData:
            return None
        if isinstance(dPlayerData[sAttr], int):
            val = tArgs[0]
            dPlayerData[sAttr] += val
        elif isinstance(dPlayerData[sAttr], list):
            val = tArgs[0]
            if 'bDeduplication' in kwargs and not kwargs['bDeduplication']:
                dPlayerData[sAttr].append(val)
            elif val not in dPlayerData[sAttr]:
                dPlayerData[sAttr].append(val)
            elif isinstance(dPlayerData[sAttr], dict):
                if isinstance(tArgs[0], dict):
                    for key, val in tArgs[0].items():
                        dPlayerData[sAttr].setdefault(key, 0)
                        dPlayerData[sAttr][key] += val
                    
                else:
                    (key, val) = tArgs
                    dPlayerData[sAttr].setdefault(key, 0)
                    dPlayerData[sAttr][key] += val
        if None == 'Damage':
            dPlayerData['MaxDamage'] = max(dPlayerData['MaxDamage'], val)
        if sAttr == 'WeaponDamage':
            (_iItemId, iDam) = tArgs
            iItemSID = kwargs['iItemSID']
            if iDam > dPlayerData['MaxWeaponDamage']:
                dPlayerData['MaxWeaponDamage'] = iDam
                dPlayerData['MaxWeaponDamageSID'] = iItemSID
                self.SetPlayerWarInfo(pid, 'MaxWeaponDamage', iDam)

    
    def SummaryFightTime(self, iLevel, pid):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if oReport and pid in oReport.m_PlayerData:
            oReport.SummaryLevelFightTime(pid)

    
    def SummaryLevelStayTime(self, iLevel, pid, iEnter):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if oReport and pid in oReport.m_PlayerData:
            oReport.SummaryLevelStayTime(pid, iEnter)

    
    def SummaryLevelSuit(self, iLevel, pid):
        oSuitElement = self.m_Game.m_WarMgr.GetComponent('SuitElement')
        if not oSuitElement:
            return None
        iHero = self.m_Game.m_WarMgr.GetHeroIDByPlayerID(pid)
        lstSuit = oSuitElement.GetSuitByID(iHero)
        for iSuit in lstSuit:
            self.SummaryLevelInfo(iLevel, pid, 'AddSuit', iSuit)
        

    
    def StartShieldSummary(self, pid, iShiled):
        self.m_ShieldTmp[pid] = iShiled

    
    def SummaryShieldUp(self, iLevel, pid, iShield):
        if pid in self.m_ShieldTmp:
            iUp = iShield - self.m_ShieldTmp[pid]
            self.SummaryLevelInfo(iLevel, pid, 'ShieldUp', iUp)

    
    def SummaryTalent(self, iLevel, pid, iTalent):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        dPlayerData['Talent'].append(iTalent)

    
    def SummaryUpGradeWeaponGen(self, iLevel, pid, lstData):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        dPlayerData['UpGradeWeaponGen'].append(lstData)

    
    def SummaryUpGradeWeapon(self, iLevel, pid, tData):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        dPlayerData['UpGradeWeapon'].append(tData)

    
    def SummaryLevelPhaseDieInfo(self, iLevel, pid, iPhase):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        if iPhase not in dPlayerData['PhaseDeath']:
            dPlayerData['PhaseDeath'][iPhase] = 1
        else:
            dPlayerData['PhaseDeath'][iPhase] += 1

    
    def SummaryRareTalentGen(self, iLevel, pid, iNpc, lstTalent):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        dRareTalent = dPlayerData['RareTalentGen']
        dRareTalent[iNpc].extend(lstTalent)

    
    def SummaryRareGoldenCup(self, iLevel, pid, iNpc):
        if not iLevel:
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            iLevel = oLevelCtrl.m_CurNode.m_Level
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        dRareTalentGen = dPlayerData['RareTalentGen']
        dRareTalent = dPlayerData['RareTalent']
        dRareTalent[iNpc] = []
        dRareTalentGen[iNpc] = []

    
    def SummaryRareTalent(self, iLevel, pid, iNpc, iTalent):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        if pid not in oReport.m_PlayerData:
            return None
        dPlayerData = oReport.m_PlayerData[pid]
        dRareTalent = dPlayerData['RareTalent']
        dRareTalent[iNpc] = iTalent

    
    def SetLevelResult(self, iLevel, lstPlayer, iResult):
        oReport = self.GetLayerLevelReport(iLevel)
        if not oReport:
            return None
        for pid in lstPlayer:
            if pid not in oReport.m_PlayerData:
                continue
            dPlayerData = oReport.m_PlayerData[pid]
            dPlayerData['Result'] = iResult
        

    
    def ReBuildPlayerWarData(self, pid, dData):
        for key in dData:
            if key in ('Damage', 'New', 'TeamDam', 'Cache'):
                continue
            if key == 'WarSummaryData':
                self.m_WarData = dData['WarSummaryData']
                continue
            (_, iLevel) = key
            dLevelData = dData[key]
            tLevelIndex = dLevelData['LIndex']
            iLevelType = dLevelData['LType']
            iPlayFrame = 0
            if iLevelType in (LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT):
                if 'PlayFrame' in dLevelData:
                    iPlayFrame = dLevelData['PlayFrame']
                else:
                    iStartFrame = dLevelData['SFrame']
                    iEndFrame = dLevelData['EFrame']
                    iPauseFrame = dLevelData['PFrame']
                    iPlayFrame = iEndFrame - iStartFrame - iPauseFrame
            if key not in self.m_LevelReport:
                oReport = CLevelReportData(self.m_Game, [], iLevelType, iLevel, tLevelIndex)
                self.m_LevelReport[key] = oReport
                lstLevel = self.m_Index2Level.setdefault(tLevelIndex, [])
                lstLevel.append(iLevel)
                oReport.m_PlayFrame = iPlayFrame
            oReport = self.m_LevelReport[key]
            oReport.AddPlayer([
                pid])
            dPlayerData = oReport.m_PlayerData[pid]
            for sAttr, val in dLevelData.items():
                if sAttr not in dPlayerData:
                    continue
                dPlayerData[sAttr] = val
            
        
        if pid not in self.m_ReportCtrl.m_Cache:
            self.m_ReportCtrl.m_Cache[pid] = self.GetPlayerWarStatistics(pid)
        self.m_InitStartFrame = self.m_ReportCtrl.m_Cache[pid].get('PlayFrame', 0)
        for oReport in self.m_LevelReport.values():
            oReport.m_Finish = 1
        

    
    def SavePlayerWarData(self, pid, dInfo = None):
        dStatustics = {
            'Damage': 0,
            'WarSummaryData': self.m_WarData }
        bFilterUnFinish = True
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
        if (oSurvivorElement or dInfo) and 'BossLevelGoal' in dInfo:
            bFilterUnFinish = False
        for oReport in self.m_LevelReport.values():
            if not (oReport.m_Finish) and bFilterUnFinish:
                continue
            if pid not in oReport.m_PlayerData:
                continue
            dPlayerData = oReport.m_PlayerData[pid]
            dData = { }
            dData['LIndex'] = oReport.m_LevelIndex
            dData['LType'] = oReport.m_LevelType
            dData['PlayFrame'] = oReport.m_PlayFrame
            dData.update(dPlayerData)
            (iLayerNum, _) = oReport.m_LevelIndex
            dStatustics[(iLayerNum, oReport.m_Level)] = dData
            dStatustics['Damage'] += dData['Damage']
        
        return dStatustics

    
    def SetPlayerWarInfo(self, pid, sAttr, iValue):
        dAllPlayerWarData = self.m_WarData['PlayerData']
        if pid not in dAllPlayerWarData:
            dAllPlayerWarData[pid] = { }
        dAllPlayerWarData[pid][sAttr] = iValue

    
    def SummaryWarInfo(self, pid, sAttr, *tArgs, **kwargs):
        dAllPlayerWarData = self.m_WarData['PlayerData']
        if pid not in dAllPlayerWarData:
            dAllPlayerWarData[pid] = { }
        dPlayerData = dAllPlayerWarData[pid]
        if sAttr not in dPlayerData:
            dPlayerData[sAttr] = tArgs[0]
            return None
        if isinstance(tArgs[0], int):
            val = tArgs[0]
            dPlayerData[sAttr] += val
        elif isinstance(tArgs[0], list):
            val = tArgs[0]
            lstData = dPlayerData[sAttr]
            dPlayerData[sAttr] = list(set(lstData + val))
        elif isinstance(tArgs[0], dict):
            for key, val in tArgs[0].items():
                dPlayerData[sAttr].setdefault(key, 0)
                dPlayerData[sAttr][key] += val
            

    
    def GetPlayerWarInfo(self, pid, sAttr, default = 0):
        if pid not in self.m_WarData['PlayerData']:
            return default
        dPlayerInfo = self.m_WarData['PlayerData'][pid]
        if sAttr in dPlayerInfo:
            return dPlayerInfo[sAttr]
        return default

    
    def GetDetailedSeasonDamage(self, pid):
        iSeasonNum = self.m_Game.m_WarMgr.m_SeasonNum
        dDetailedSeasonDamage = self.m_ReportCtrl.m_DetailedSeasonDam
        if iSeasonNum not in dDetailedSeasonDamage:
            return { }
        sAttr = dDetailedSeasonDamage[iSeasonNum]
        return self.GetPlayerWarInfo(pid, sAttr, default = { })

    
    def GetPlayerWarStatistics(self, pid):
        oGame = self.m_Game
        oHero = oGame.m_WarMgr.GetHeroByPlayer(pid)
        dStatustics = self.m_ReportCtrl.m_Cache.get(pid, { })
        if dStatustics:
            dStatustics = DeepCopy(dStatustics)
        else:
            dStatustics = {
                'PlayFrame': 0,
                'FightLevel': 0,
                'BossLevel': 0,
                'LvSum': { },
                'HideLvSum': { },
                'Die': 0,
                'Injured': 0,
                'ShieldUp': 0,
                'ShieldDown': 0,
                'HpUp': 0,
                'HpDown': 0,
                'Damage': 0,
                'SurvivorGrade': 0,
                'OwnKill': 0,
                'Kill': 0,
                'KillElite': 0,
                'KillBoss': 0,
                'AssistKillElite': 0,
                'AssistKillBoss': 0,
                'EnterHide': [],
                'Talent': [],
                'TalentGen': [],
                'Relic': [],
                'Save': 0,
                'Cash': 0,
                'GSCash': 0,
                'FightFrame': 0,
                'MaxDamage': 0,
                'HideLevel': 0,
                'Weapon': { },
                'RemoveRelic': { },
                'KillMonster': { },
                'KillBossDetail': { },
                'SavingTimes': 0,
                'WeaponDamage': { },
                'HitTimes': { },
                'WeaknessTimes': { },
                'DebuffTimes': { },
                'FireTimes': { },
                'CauseDamageTimes': { },
                'MaxWeaponDamage': 0,
                'MaxWeaponDamageSID': 0,
                'Round': oGame.m_WarMgr.m_Round,
                'Cycle': oGame.m_WarMgr.m_Cycle,
                'Bened': [],
                'AllGotBened': { },
                'BenedGen': [],
                'RelicRelife': 0,
                'StayFrame': 0,
                'AddSuit': [],
                'FourthBened': [],
                'EnableSuit': [],
                'ModeType': oGame.m_WarMgr.m_ModeType,
                'RareTalent': [],
                'RareTalentGen': [],
                'UpGradeTalent': [],
                'UpGradeTalentGen': [],
                'UpGradeRelic': [],
                'UpGradeRelicGen': [],
                'UpGradeWeapon': [],
                'UpGradeWeaponGen': [],
                'PhaseDeath': { },
                'CommonTalentChosen': [],
                'CommonTalentGen': [],
                'TaskStatus': [],
                'SeasonNum': oGame.m_WarMgr.m_SeasonNum,
                'InjuredByTrap': 0,
                'SeasonDamage': 0,
                'PassNewVerLayer': [],
                'LvResult': { } }
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        dStatustics['LvCnt'] = oLevelCtrl.GetMaxLevel()
        dStatustics['CurLv'] = oLevelCtrl.m_CurNode.m_Level if oLevelCtrl.m_CurNode else 0
        dStatustics['Level'] = oLevelCtrl.m_LevelNum
        dStatustics['Layer'] = oLevelCtrl.m_LayerNum
        dStatustics['Goaled'] = oLevelCtrl.m_CurNode.HasGoaledCurNode() if oLevelCtrl.m_CurNode else 0
        dStatustics['Prog'] = oLevelCtrl.m_CurNode.GetCurNodeProgress() if oLevelCtrl.m_CurNode else 0
        dStatustics['FirstHall'] = oLevelCtrl.CheckFirstHall()
        dStatustics['EndlessCurLevelNum'] = oGame.m_WarMgr.GetEndlessCurLevelNum()
        dStatustics['EndlessMode'] = oGame.m_WarMgr.GetEndlessMode()
        dStatustics['AllGotBened'] = self.GetPlayerWarInfo(pid, 'AllGotBened', { })
        dStatustics['Bened'] = oHero.m_BenedictionCon.GetBenedictionSID(BENE_SOURCE_LAYER)
        dStatustics['CommonTalentChosen'] = list(oHero.m_TalentCon.GetAllCommonTalent())
        dStatustics['SeasonDamage'] = self.GetPlayerWarInfo(pid, 'SeasonDamage', 0)
        oSuitElement = oGame.m_WarMgr.GetComponent('SuitElement')
        if oSuitElement:
            dStatustics['EnableSuit'] = oSuitElement.GetEffectiveSuitInfo(oHero.m_ID)
        if oHero and oHero.m_SID == 207:
            dStatustics['Enhancement'] = oHero.QuerySavedData('RandomRewardFlag')
            dStatustics['EnhancementList'] = oHero.QuerySavedData('lstRewardpf', [])
        oSurvivorElement = oGame.m_WarMgr.GetComponent('SurvivorElement')
        oNewSurvivorElement = oGame.m_WarMgr.GetComponent('NewSurvivorElement')
        if oSurvivorElement:
            dStatustics['SurvivorGrade'] = oSurvivorElement.m_UpgradeMgr.GetHeroGrade(oHero.m_ID)
        if oSurvivorElement or oNewSurvivorElement:
            dStatustics['AnimaModule'] = oHero.Query('AnimaModule', [])
        oRidingAloneElement = oGame.m_WarMgr.GetComponent('RidingAloneElement')
        if oRidingAloneElement:
            lstBened = []
            if oRidingAloneElement.m_Bene:
                lstBened.append(oRidingAloneElement.m_Bene)
            dStatustics['EnableRidingAloneBened'] = lstBened
            if oRidingAloneElement.m_SpawnCnt:
                dStatustics['RidingAloneDifficulty'] = oRidingAloneElement.m_SpawnCnt
        oMonsterRelicElement = oGame.m_WarMgr.GetComponent('MonsterRelicElement')
        if oMonsterRelicElement and oMonsterRelicElement.m_SelectRelic:
            dStatustics['HeroSelectRelic'] = oMonsterRelicElement.m_SelectRelic
        dFPS = { }
        iFPSFrame = 0
        dSystemInfo = { }
        for oReport in self.m_LevelReport.values():
            if oReport.m_Finish:
                continue
            if pid not in oReport.m_PlayerData:
                continue
            iLevelType = oReport.m_LevelType
            (iLayerNum, iLevelNum) = oReport.m_LevelIndex
            iLevel = oReport.m_Level
            dPlayerData = oReport.m_PlayerData[pid]
            if 'LvResult' not in dStatustics:
                dStatustics['LvResult'] = { }
            dStatustics['LvResult'][(iLayerNum, iLevelNum)] = dPlayerData['Result']
            if iLevelType in (LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT):
                if iLevelType == LEVEL_TYPE_BOSS:
                    dStatustics['BossLevel'] += 1
                else:
                    dStatustics['FightLevel'] += 1
                iPlayFrame = oReport.m_PlayFrame
                if not (oReport.m_Finish) and self.m_ReportCtrl.m_WarFrameSummary:
                    iPlayFrame = self.m_ReportCtrl.m_WarFrameSummary.GetCurLevelFrame()
                dStatustics['PlayFrame'] += iPlayFrame
                dLayerSum = dStatustics['LvSum'].setdefault(iLayerNum, { })
                dLayerSum[iLevelNum] = (iLevelType, iLevel)
                dLevelFPS = dPlayerData.get('FPS', { })
                iFPSFrame = iFPSFrame + iPlayFrame if dLevelFPS else iFPSFrame
                for k, v in dLevelFPS.items():
                    dFPS.setdefault(k, 0)
                    v = v if k in ('ave_fps', 'fps_gear') else round(v / 10000, 3)
                    dFPS[k] += v * iPlayFrame
                    if k == 'fps_gear':
                        dFPS[k] = v
                
                dLevelSysInfo = dPlayerData.get('SystemInfo', { })
                for k, v in dLevelSysInfo.items():
                    if k not in dSystemInfo:
                        dSystemInfo[k] = [
                            v]
                    else:
                        dSystemInfo[k].append(v)
                
            elif iLevelType in (LEVEL_TYPE_HIDE,):
                dLayerSum = dStatustics['HideLvSum'].setdefault(iLayerNum, { })
                dLevelSum = dLayerSum.setdefault(iLevelNum, [])
                dLevelSum.append((iLevelType, iLevel))
            for sAttr, val in dPlayerData.items():
                if sAttr not in dStatustics:
                    continue
                if sAttr == 'MaxDamage':
                    dStatustics[sAttr] = max(dPlayerData[sAttr], dStatustics[sAttr])
                    continue
                if sAttr == 'MaxWeaponDamage' or sAttr == 'MaxWeaponDamageSID':
                    if dPlayerData['MaxWeaponDamage'] > dStatustics['MaxWeaponDamage']:
                        dStatustics['MaxWeaponDamage'] = dPlayerData['MaxWeaponDamage']
                        dStatustics['MaxWeaponDamageSID'] = dPlayerData['MaxWeaponDamageSID']
                        continue
                if sAttr in ('Talent', 'TalentGen'):
                    dStatustics[sAttr].extend(val)
                    continue
                if sAttr == 'RareTalentGen':
                    for v in val.values():
                        if not v:
                            dStatustics[sAttr].append(0)
                        else:
                            dStatustics[sAttr].append(v)
                    
                    continue
                if sAttr == 'RareTalent':
                    for v in val.values():
                        if not v:
                            dStatustics[sAttr].append(0)
                        else:
                            dStatustics[sAttr].append(v)
                    
                    continue
                if sAttr == 'StayFrame':
                    if iLevelType not in (LEVEL_TYPE_HALL,):
                        dStatustics[sAttr] += val
                        continue
                if isinstance(val, int):
                    dStatustics[sAttr] += val
                elif isinstance(val, list):
                    lstAttr = dStatustics[sAttr]
                    for v in val:
                        if v not in lstAttr:
                            lstAttr.append(v)
                    
                elif isinstance(val, dict):
                    dAttr = dStatustics[sAttr]
                    for k, v in val.items():
                        dAttr.setdefault(k, 0)
                        if sAttr == 'FPS' and isinstance(dAttr[k], str):
                            dAttr[k] = float(dAttr[k])
                        dAttr[k] += v
                    
            
        
        if iFPSFrame:
            dReportFPS = { }
            for k, v in dFPS.items():
                if k == 'fps_gear':
                    fFPS = v
                elif k == 'ave_fps':
                    fFPS = v // iFPSFrame
                else:
                    fFPS = round(v / iFPSFrame, 3)
                dReportFPS[k] = fFPS if k in ('ave_fps', 'fps_gear') else '%.3f' % fFPS
            
            dStatustics['FPS'] = dReportFPS
        else:
            dStatustics['FPS'] = { }
        if dSystemInfo:
            for k, v in dSystemInfo.items():
                dSystemInfo[k] = sum(dSystemInfo[k]) / len(dSystemInfo[k])
            
        dStatustics['SystemInfo'] = dSystemInfo
        oSurvivorElement = oGame.m_WarMgr.GetComponent('SurvivorElement')
        if oSurvivorElement:
            dStatustics['PlayFrame'] = oSurvivorElement.m_FightTimerMgr.GetPlayFrame()
        dStatustics['PassNewVerLayer'] = self.GetPlayerWarInfo(pid, 'PassNewVerLayer', default = [])
        if pid in self.m_WarData['PlayerData'] and 'TrusteeshipFrame' in self.m_WarData['PlayerData'][pid]:
            dStatustics['TrusteeshipFrame'] = self.m_WarData['PlayerData'][pid]['TrusteeshipFrame']
        return dStatustics

    
    def GetPlayerLevelStatustics(self, pid):
        dStatustics = { }
        lstLevel = self.m_Index2Level.get(self.m_CurIndex, [])
        for iLevel in lstLevel:
            oReport = self.GetLayerLevelReport(iLevel)
            if not oReport:
                continue
            if pid not in oReport.m_PlayerData:
                continue
            iPlayFrame = oReport.m_PlayFrame
            if not (oReport.m_Finish) and self.m_ReportCtrl.m_WarFrameSummary:
                iPlayFrame = self.m_ReportCtrl.m_WarFrameSummary.GetCurLevelFrame()
            dData = {
                'Finish': oReport.m_Finish,
                'LevelType': oReport.m_LevelType,
                'LevelID': oReport.m_Level,
                'PlayFrame': iPlayFrame }
            dData.update(oReport.m_PlayerData[pid])
            dStatustics[iLevel] = dData
            dReportFPS = { }
            dFPS = dData.setdefault('FPS', { })
            for k, v in dFPS.items():
                if k in ('ave_fps', 'fps_gear'):
                    dReportFPS[k] = v
                    continue
                fFPS = round(v / 10000, 3)
                dReportFPS[k] = '%.3f' % fFPS
            
            dData['FPS'] = dReportFPS
        
        return dStatustics

    
    def GetTeamMemberStatistics(self, lstTeamMember):
        dTeam = { }
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oSurvivorElement = oWarMgr.GetComponent('SurvivorElement')
        oNewSurvivorElement = oWarMgr.GetComponent('NewSurvivorElement')
        oAIElement = oWarMgr.GetComponent('TeammateAI')
        dReportCache = self.m_ReportCtrl.m_Cache
        for iNpcID in lstTeamMember:
            pid = oWarMgr.GetPlayerIDByHeroID(iNpcID)
            if not pid:
                continue
            oHero = oGame.GetObject(iNpcID)
            if not oHero:
                continue
            dData = {
                'Damage': 0,
                'MaxDamage': 0,
                'SurvivorGrade': 0,
                'OwnKill': 0,
                'SavingTimes': 0,
                'FireTimes': 0,
                'CauseDamageTimes': 0,
                'DebuffTimes': { },
                'WeaknessTimes': { },
                'HitTimes': { },
                'WeaponDamage': { },
                'AnimaModule': [],
                'KillElite': 0,
                'Die': 0,
                'RelicNum': 0,
                'Name': '',
                'pid': 0,
                'SID': 0,
                'DyingTimes': 0,
                'CommonTalentChosen': [],
                'TaskStatus': { },
                'RelicTalentBasePF': 0,
                'RelicTalent': { },
                'Device': 0,
                'SeasonDamage': 0,
                'DeviceComp': { },
                'PetSID': 0,
                'PetAttr': {
                    'Attr': [] },
                'PetOffset': { },
                'PetAbility': [],
                'PreAIDamage': -1,
                'AIDamage': -1,
                'IsAI': 0,
                'DetailedSeasonDam': { } }
            if pid in dReportCache:
                dCacheData = dReportCache[pid]
                if dCacheData:
                    self.SumupStatistics(dData, dCacheData)
            for oReport in self.m_LevelReport.values():
                if oReport.m_Finish:
                    continue
                if pid not in oReport.m_PlayerData:
                    continue
                dPlayerData = oReport.m_PlayerData[pid]
                self.SumupStatistics(dData, dPlayerData)
            
            if oSurvivorElement:
                dData['SurvivorGrade'] = oSurvivorElement.m_UpgradeMgr.GetHeroGrade(iNpcID)
            if oSurvivorElement or oNewSurvivorElement:
                dData['AnimaModule'] = oHero.Query('AnimaModule', [])
            dData['Damage'] = self.m_ReportCtrl.GetTotalDamageByHeroID(oHero.m_ID)
            dData['Name'] = oHero.m_OwnerName
            dData['pid'] = pid
            dData['SID'] = oHero.m_SID
            dData['DyingTimes'] = oHero.QuerySavedData('DyingTimes', 0)
            lstCommonTalent = []
            for iTalent in oHero.m_TalentCon.GetAllCommonTalent():
                oTalent = oHero.m_TalentCon.GetPerform(iTalent)
                lstCommonTalent.append((iTalent, oTalent.Level() if oTalent else 0))
            
            dData['CommonTalentChosen'] = lstCommonTalent
            dData['TaskStatus'] = oHero.m_TaskCon.GetAllTaskStatus()
            if oHero.m_RelicTalentCon:
                dData['RelicTalentBasePF'] = oHero.m_RelicTalentCon.m_Relic
                dData['RelicTalent'] = oHero.m_RelicTalentCon.GetTalentWarReportInfo()
            dData['SeasonDamage'] = self.GetPlayerWarInfo(pid, 'SeasonDamage', default = 0)
            if oHero.m_DeviceMgr:
                dData['Device'] = oHero.GetDeviceSID()
                dData['DeviceComp'] = oHero.m_DevicePerformCon.GetAllEnableDeviceCompLevel()
            if oHero.m_PetCon:
                dPetReportData = oHero.m_PetCon.GetReportData()
                dData.update(dPetReportData)
            if oAIElement:
                (dData['PreAIDamage'], dData['AIDamage']) = oAIElement.GetHeroDamage(pid)
                dData['IsAI'] = oAIElement.CheckIsAI(oHero.m_ID, oHero.Online())
            dData['DetailedSeasonDam'] = self.GetDetailedSeasonDamage(pid)
            dTeam[iNpcID] = dData
        
        return dTeam

    
    def SumupStatistics(self, dData, dPlayerData):
        dData['MaxDamage'] = max(dPlayerData['MaxDamage'], dData['MaxDamage'])
        dData['OwnKill'] += dPlayerData['OwnKill']
        dData['SavingTimes'] += dPlayerData['SavingTimes']
        dData['KillElite'] += dPlayerData['KillElite']
        dData['Die'] += dPlayerData['Die']
        dData['RelicNum'] += len(dPlayerData['Relic'])
        for iKey, iValue in dPlayerData['FireTimes'].items():
            dData['FireTimes'] += iValue
        
        for iKey, iValue in dPlayerData['CauseDamageTimes'].items():
            dData['CauseDamageTimes'] += iValue
        
        for iKey, iValue in dPlayerData['DebuffTimes'].items():
            dData['DebuffTimes'].setdefault(iKey, 0)
            dData['DebuffTimes'][iKey] += iValue
        
        for iKey, iValue in dPlayerData['WeaknessTimes'].items():
            dData['WeaknessTimes'].setdefault(iKey, 0)
            dData['WeaknessTimes'][iKey] += iValue
        
        for iKey, iValue in dPlayerData['HitTimes'].items():
            dData['HitTimes'].setdefault(iKey, 0)
            dData['HitTimes'][iKey] += iValue
        
        for iKey, iValue in dPlayerData['WeaponDamage'].items():
            dData['WeaponDamage'].setdefault(iKey, 0)
            dData['WeaponDamage'][iKey] += iValue
        

    
    def GetKillStatistics(self, pid):
        dKillMonster = { }
        for oReport in self.m_LevelReport.values():
            if pid not in oReport.m_PlayerData:
                continue
            dData = oReport.m_PlayerData[pid]
            for iMonster, iCnt in dData['KillMonsterSIDAndSuper'].items():
                iNow = dKillMonster[iMonster] if iMonster in dKillMonster else 0
                dKillMonster[iMonster] = iNow + iCnt
            
        
        return dKillMonster

    
    def GetPlayerWarStatisticsByAttr(self, pid, sAttr):
        dStatistics = {
            'AssistKillElite': 0,
            'AssistKillBoss': 0 }
        result = dStatistics[sAttr]
        dCache = self.m_ReportCtrl.m_Cache.get(pid, { })
        if sAttr in dCache:
            val = dCache[sAttr]
            if isinstance(val, int):
                result += val
        for oReport in self.m_LevelReport.values():
            if pid not in oReport.m_PlayerData:
                continue
            dPlayerData = oReport.m_PlayerData[pid]
            if sAttr not in dPlayerData:
                continue
            val = dPlayerData[sAttr]
            if isinstance(val, int):
                result += val
        
        return result



class CLevelReportData(object):
    
    def __init__(self, oGame, lstPlayer, iLevelType, iLevel, tLevelIndex):
        self.m_Game = oGame
        self.m_LevelType = iLevelType
        self.m_Level = iLevel
        self.m_LevelIndex = tLevelIndex
        self.m_Finish = 0
        self.m_PlayFrame = 0
        self.m_TmpFightFrame = { }
        self.m_TmpStayFrame = { }
        self.m_PlayerData = { }
        self.AddPlayer(lstPlayer)

    
    def AddPlayer(self, lstPlayer):
        for pid in lstPlayer:
            self.m_PlayerData[pid] = {
                'Die': 0,
                'Injured': 0,
                'ShieldUp': 0,
                'ShieldDown': 0,
                'HpUp': 0,
                'HpDown': 0,
                'Damage': 0,
                'SurvivorGrade': 0,
                'OwnKill': 0,
                'Kill': 0,
                'KillElite': 0,
                'KillBoss': 0,
                'AssistKillElite': 0,
                'AssistKillBoss': 0,
                'EnterHide': [],
                'Talent': [],
                'TalentGen': [],
                'Relic': [],
                'Save': 0,
                'Cash': 0,
                'GSCash': 0,
                'FightFrame': 0,
                'MaxDamage': 0,
                'HideLevel': 0,
                'Weapon': { },
                'RemoveRelic': { },
                'KillMonster': { },
                'KillBossDetail': { },
                'KillMonsterSIDAndSuper': { },
                'SavingTimes': 0,
                'WeaponDamage': { },
                'HitTimes': { },
                'WeaknessTimes': { },
                'DebuffTimes': { },
                'FireTimes': { },
                'CauseDamageTimes': { },
                'MaxWeaponDamage': 0,
                'MaxWeaponDamageSID': 0,
                'FPS': { },
                'SystemInfo': { },
                'BenedGen': [],
                'RelicRelife': 0,
                'UnlockMonster': { },
                'EventNpc': { },
                'StayFrame': 0,
                'Result': 0,
                'AddSuit': [],
                'FourthBened': [],
                'RareTalent': { },
                'RareTalentGen': { },
                'UpGradeTalent': [],
                'UpGradeTalentGen': [],
                'UpGradeRelic': [],
                'UpGradeRelicGen': [],
                'UpGradeWeapon': [],
                'UpGradeWeaponGen': [],
                'PhaseDeath': { },
                'CommonTalentGen': [],
                'InjuredByTrap': 0,
                'SeasonDamage': 0 }
        

    
    def Release(self):
        self.m_Game = None
        self.m_TmpFightFrame = { }
        self.m_PlayerData = { }

    
    def GetLevelType(self):
        return self.m_LevelType

    
    def GetAllReportPlayer(self):
        return list(self.m_PlayerData)

    
    def SummaryLevelFightTime(self, pid):
        iCurFrame = self.m_Game.GetFrameNum()
        iLimitFrame = GAME_FRAME * 5
        if pid not in self.m_TmpFightFrame:
            self.m_TmpFightFrame[pid] = (iCurFrame, False)
        (iStartFrame, bContinue) = self.m_TmpFightFrame[pid]
        if iStartFrame < iCurFrame - iLimitFrame:
            if bContinue:
                self.m_PlayerData[pid]['FightFrame'] += iCurFrame - iStartFrame
            self.m_TmpFightFrame[pid] = (iCurFrame, False)
        else:
            self.m_TmpFightFrame[pid] = (iStartFrame, True)

    
    def SummaryLevelStayTime(self, pid, iEnter):
        iCurFrame = self.m_Game.GetFrameNum()
        if pid not in self.m_TmpStayFrame:
            self.m_TmpStayFrame[pid] = (iCurFrame, False)
        (iStartFrame, bContinue) = self.m_TmpStayFrame[pid]
        if not iEnter:
            if bContinue and 'StayFrame' in self.m_PlayerData[pid]:
                self.m_PlayerData[pid]['StayFrame'] += iCurFrame - iStartFrame
            self.m_TmpStayFrame[pid] = (iCurFrame, False)
        else:
            self.m_TmpStayFrame[pid] = (iCurFrame, True)


FRAMESUM_STATUS_STOP = 0
FRAMESUM_STATUS_START = 1

class CBaseFrameSummary(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_Status = FRAMESUM_STATUS_START
        self.m_StartFrame = 0
        self.m_TotalFrame = 0
        self.m_PauseFrame = 0
        self.m_PauseStartFrame = -1
        self.m_TakeOverStartFrame = { }
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, self.OnRemovePlayer, 'FrameRemovePlayer', -1, 0, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelFinish, 'FrameLevelFinish', -1, 0, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoalOK, 'FrameLevelGoalOK', -1, 0, 0)
        lstHero = oWarMgr.GetRoomHero()
        self.AddPlayer(lstHero)

    
    def Release(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_REMOVEPLAYER, 'FrameRemovePlayer')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'FrameLevelFinish')
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'FrameLevelGoalOK')
        lstHero = oWarMgr.GetRoomHero()
        self.RemovePlayer(lstHero)
        self.m_Game = None

    
    def AddPlayer(self, lstHero):
        for iHero in lstHero:
            cl_msgcenter.AddAttentionFunc(self.m_Game.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnLoadMapOK, 'FrameLoadMapOK')
        

    
    def RemovePlayer(self, lstHero):
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(self.m_Game.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'FrameLoadMapOK')
        

    
    def StartSummary(self, iLevelType):
        if iLevelType == LEVEL_TYPE_HIDE:
            return None
        iFrame = self.GetCurLevelFrame()
        self.m_TotalFrame += iFrame
        self.m_StartFrame = self.m_Game.GetFrameNum()
        self.m_PauseFrame = 0
        self.m_PauseStartFrame = -1
        self.m_Status = FRAMESUM_STATUS_START
        if iLevelType == LEVEL_TYPE_HALL:
            self.PauseCounting(iNotify = 0)
        elif iLevelType in (LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT):
            self.ResumeCounting(iNotify = 0)
            self.ResetTakeOverStartFrame(self.m_StartFrame)
        self.NotifyPlayFrame()

    
    def GetCurLevelFrame(self):
        iCurFrame = self.m_Game.GetFrameNum()
        iFrame = iCurFrame - self.m_StartFrame
        iFrame -= self.m_PauseFrame
        if self.m_Status == FRAMESUM_STATUS_STOP and self.m_PauseStartFrame != -1:
            iFrame -= iCurFrame - self.m_PauseStartFrame
        return iFrame

    
    def ResetTakeOverStartFrame(self, iCurFrame):
        oGame = self.m_Game
        oWarmgr = oGame.m_WarMgr
        lstPlayer = oWarmgr.GetAllPlayer()
        for pid in lstPlayer:
            iHero = oWarmgr.GetHeroIDByPlayerID(pid)
            if not iHero:
                continue
            if oWarmgr.IsAIHero(iHero):
                self.m_TakeOverStartFrame[pid] = iCurFrame
        

    
    def GetTrusteeshipFrame(self, iPlayer):
        if iPlayer not in self.m_TakeOverStartFrame:
            return 0
        iCurFrame = self.m_Game.GetFrameNum()
        if self.m_Status == FRAMESUM_STATUS_STOP and self.m_PauseStartFrame != -1:
            iPauseFrame = iCurFrame - self.m_PauseStartFrame
        else:
            iPauseFrame = 0
        iFrame = iCurFrame - self.m_TakeOverStartFrame[iPlayer]
        self.m_TakeOverStartFrame.pop(iPlayer)
        iFrame -= self.m_PauseFrame + iPauseFrame
        return iFrame

    
    def GetPlayFrame(self):
        iFrame = self.GetCurLevelFrame()
        iFrame += self.m_TotalFrame
        return iFrame

    
    def PauseCounting(self, iNotify = 1):
        if self.m_Status == FRAMESUM_STATUS_STOP:
            return None
        self.m_Status = FRAMESUM_STATUS_STOP
        self.m_PauseStartFrame = self.m_Game.GetFrameNum()
        if iNotify:
            self.NotifyPlayFrame()

    
    def ResumeCounting(self, iNotify = 1):
        if self.m_Status == FRAMESUM_STATUS_START:
            return None
        self.m_Status = FRAMESUM_STATUS_START
        if self.m_PauseStartFrame != -1:
            self.m_PauseFrame += self.m_Game.GetFrameNum() - self.m_PauseStartFrame
            self.m_PauseStartFrame = -1
        if iNotify:
            self.NotifyPlayFrame()

    
    def NotifyPlayFrame(self, lstPlayer = None):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
        if oSurvivorElement:
            return None
        if lstPlayer is None:
            lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer()
        iFrame = self.GetPlayFrame()
        iGMShowTime = self.m_Game.m_WarMgr.Query('GMShowTime')
        if iGMShowTime:
            iFrame += GAME_FRAME * iGMShowTime
        for pid in lstPlayer:
            cl_snetwar.GS2CPlayTime(self.m_Game, pid, iFrame, self.m_Status)
        

    
    def OnRemovePlayer(self, oWarMgr, dInfo):
        self.RemovePlayer([
            dInfo['pid']])

    
    def OnLevelFinish(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_FIGHT:
            self.PauseCounting()

    
    def OnLevelGoalOK(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        if iLevelType == LEVEL_TYPE_BOSS:
            self.PauseCounting()

    
    def OnLoadMapOK(self, oWarMgr, oHero, dInfo):
        self.NotifyPlayFrame([
            oHero.m_PlayerID])



class CSingleFrameSummary(CBaseFrameSummary):
    
    def __init__(self, oGame):
        super(CSingleFrameSummary, self).__init__(oGame)
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, 'FrameLevelStart', -1, 0, 0)

    
    def OnLevelStart(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        self.StartSummary(iLevelType)

    
    def AddPlayer(self, lstHero):
        super(CSingleFrameSummary, self).AddPlayer(lstHero)
        for iHero in lstHero:
            cl_msgcenter.AddAttentionFunc(self.m_Game.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, 'FrameEnterScene')
        

    
    def RemovePlayer(self, lstHero):
        super(CSingleFrameSummary, self).RemovePlayer(lstHero)
        for iHero in lstHero:
            cl_msgcenter.DoneAttention(self.m_Game.m_WarMgr, iHero, cl_msgcenter.MSG_WAR_ENTERSCENE, 'FrameEnterScene')
        

    
    def OnEnterScene(self, oWarMgr, oHero, dInfo):
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if oLevelNode and oLevelNode.m_LevelType != LEVEL_TYPE_HALL:
            self.PauseCounting()

    
    def OnLoadMapOK(self, oWarMgr, oHero, dInfo):
        super(CSingleFrameSummary, self).OnLoadMapOK(oWarMgr, oHero, dInfo)
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if oLevelNode and oLevelNode.m_LevelType != LEVEL_TYPE_HALL:
            self.ResumeCounting()



class CTeamFrameSummary(CBaseFrameSummary):
    
    def __init__(self, oGame):
        super(CTeamFrameSummary, self).__init__(oGame)
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnLevelStart, 'FrameLevelInit', -1, 0, 0)

    
    def OnLevelStart(self, oWarMgr, dInfo):
        iLevelType = dInfo['LevelType']
        self.StartSummary(iLevelType)



def GetComponentClass(oMgrManager):
    return CWarReportElement

