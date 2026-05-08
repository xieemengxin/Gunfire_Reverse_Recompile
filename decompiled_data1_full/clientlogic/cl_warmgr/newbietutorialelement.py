# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/newbietutorialelement.pyc
# RelativePath: clientlogic/cl_warmgr/newbietutorialelement.pyc
# Source Generated with Decompyle++
# File: newbietutorialelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_object.logging import NewbietutorialLog
from cl_only import Time2Frame
from cl_cscommondef import KILLHISTORY_COMPATIBY, DAM_TYPE_WEAKNESS, WARRIOR_MONSTER, DAM_MASK_ELEMENT, DAM_TYPE_THUNDER, DAM_TYPE_CORRISION, DAM_TYPE_FIRE
from cl_commondefines import STATE_ELE_MIX_VERTIGO, STATE_ELE_MIX_POISON, STATE_ELE_MIX_EXPLOSION, VIRTUAL_ITEM_TALENTWEIGHT, PROGRESSUNLOCK_WEAPON
import cl_msgcenter
import cl_notify
import cl_reward
HERO_SID = 205
BOSS_LUWU = 39011
CHECK_LUCKYEFF = 2
CHECK_MULTI_LUCKYEFF = 3
CRAZYDAM_TRIGGER = 'cd'
LUCKY_TRIGGER = 'lk'
MULTI_LUCKY_TRIGGER = 'mlk'
EXPLOSION_TRIGGER = 'exp'
VERTIGO_TRIGGER = 'vtg'
POISON_TRIGGER = 'poi'
THUNDER_DAM_TRIGGER = 'td'
FIRE_DAM_TRIGGER = 'fd'
CORROSION_DAM_TRIGGER = 'cod'
TRIGGERTYPE_TO_SAVE = {
    'CrazyDamTrigger': CRAZYDAM_TRIGGER,
    'LuckyHitTrigger': LUCKY_TRIGGER,
    'MultiLuckyHitTrigger': MULTI_LUCKY_TRIGGER,
    'ExplosionTrigger': EXPLOSION_TRIGGER,
    'VertigoTrigger': VERTIGO_TRIGGER,
    'PoisonTrigger': POISON_TRIGGER,
    'ThunderDamTrigger': THUNDER_DAM_TRIGGER,
    'FireDamTrigger': FIRE_DAM_TRIGGER,
    'CorrosionDamTrigger': CORROSION_DAM_TRIGGER }
TRIGGER_BY_ELETYPE = {
    DAM_TYPE_CORRISION: CORROSION_DAM_TRIGGER,
    DAM_TYPE_FIRE: FIRE_DAM_TRIGGER,
    DAM_TYPE_THUNDER: THUNDER_DAM_TRIGGER }

def CheckLuckyHitEff(oElement, dMsgInfo, iCurFrame, iEff):
    if iEff <= CHECK_LUCKYEFF:
        sTrigger = LUCKY_TRIGGER
    else:
        sTrigger = MULTI_LUCKY_TRIGGER
    if not oElement.GetTriggerEnable(sTrigger):
        return 0
    if not oElement.CheckOwnColdFrameByTrigger(sTrigger, iCurFrame) or not oElement.CheckDisplayTimes(sTrigger):
        return 0
    iLuckyHitEff = 0
    if 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iLuckyHitEff = oReason.Query('LuckyHitEff', 1)
    if iLuckyHitEff >= iEff:
        return 1
    return 0


def CheckHitWeakness(oElement, dMsgInfo, iCurFrame, iArg):
    sTrigger = CRAZYDAM_TRIGGER
    if not oElement.GetTriggerEnable(sTrigger):
        return 0
    if not oElement.CheckOwnColdFrameByTrigger(sTrigger, iCurFrame) or not oElement.CheckDisplayTimes(sTrigger):
        return 0
    iHitWeakness = 0
    if 'TrueChange' in dMsgInfo:
        lstDam = dMsgInfo['TrueChange']
        for _, oReason in lstDam:
            iDamType = oReason.Query('DamType')
            if iDamType & DAM_TYPE_WEAKNESS == DAM_TYPE_WEAKNESS:
                iHitWeakness = 1
        
    elif 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iDamType = oReason.Query('DamType')
        if iDamType & DAM_TYPE_WEAKNESS == DAM_TYPE_WEAKNESS:
            iHitWeakness = 1
    return iHitWeakness


def CheckElementDamType(oElement, dMsgInfo, iCurFrame, iDamType):
    if iDamType not in TRIGGER_BY_ELETYPE:
        return 0
    sTrigger = TRIGGER_BY_ELETYPE[iDamType]
    if not oElement.GetTriggerEnable(sTrigger):
        return 0
    if not oElement.CheckOwnColdFrameByTrigger(sTrigger, iCurFrame) or not oElement.CheckDisplayTimes(sTrigger):
        return 0
    iElementType = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'ElementType' in oSkill.m_Cache:
            iElementType = oSkill.m_Cache['ElementType']
    if not iElementType and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iElementType = oReason.Query('DamType', 0) & DAM_MASK_ELEMENT
    if iDamType & iElementType:
        return 1
    if 'TrueChange' in dMsgInfo:
        lstTrueChange = dMsgInfo['TrueChange']
        for _, oReason in lstTrueChange:
            iElementType = oReason.Query('DamType', 0) & DAM_MASK_ELEMENT
            if iDamType & iElementType:
                return 1
        
    return 0

MIXDEBUFF_TRIGGER = {
    EXPLOSION_TRIGGER: STATE_ELE_MIX_EXPLOSION,
    POISON_TRIGGER: STATE_ELE_MIX_POISON,
    VERTIGO_TRIGGER: STATE_ELE_MIX_VERTIGO }
DAM_EVENT_TRIGGER = {
    THUNDER_DAM_TRIGGER: (CheckElementDamType, DAM_TYPE_THUNDER),
    FIRE_DAM_TRIGGER: (CheckElementDamType, DAM_TYPE_FIRE),
    CORROSION_DAM_TRIGGER: (CheckElementDamType, DAM_TYPE_CORRISION),
    CRAZYDAM_TRIGGER: (CheckHitWeakness, None),
    LUCKY_TRIGGER: (CheckLuckyHitEff, CHECK_LUCKYEFF),
    MULTI_LUCKY_TRIGGER: (CheckLuckyHitEff, CHECK_MULTI_LUCKYEFF) }

def CheckHistoryKillBossLuWu(oElement, oHero, sTrigger):
    dMonster = oHero.Query('Monster', { })
    if 'KillBoss' in dMonster:
        iKill = dMonster['KillBoss'].get(BOSS_LUWU, 0) + dMonster['KillBoss'].get(KILLHISTORY_COMPATIBY, 0)
        NewbietutorialLog.Debug('%d %d kill %s %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, BOSS_LUWU, iKill))
        if iKill:
            return True
    oElement.m_CheckKillTrigger[sTrigger] = 1
    return False

EXTRARULE_FUNC = {
    1: CheckHistoryKillBossLuWu }

class CNewbieTutorialElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_CallFlag = 'NewbieTutorialElement'
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_NewbieOwner = 0
        self.m_TriggerInfo = { }
        for sConfig, sTrigger in TRIGGERTYPE_TO_SAVE.items():
            self.m_TriggerInfo[sTrigger] = self.m_Data.m_Config.get(sConfig, { })
        
        self.m_ShareColdFrame = Time2Frame(self.m_Data.m_Config.get('ShareColdTime', 0))
        self.m_LockModifyInfo = self.m_Data.m_Config.get('lockModify', { })
        self.m_UnlockModifyInfo = self.m_Data.m_Config.get('UnlockModify', { })
        self.m_MaxModifyTimes = self.m_Data.m_Config.get('MaxModifyTimes', 0)
        self.m_TriggerNotify = { }
        self.m_LastDisplayFrame = 0
        self.m_OwnColdFrameInfo = { }
        self.m_LastOwnDisplayFrame = { }
        self.m_FrameDisplayInfo = { }
        self.m_MaxDisplayTimesInfo = { }
        self.m_DisplayTimesInfo = { }
        self.m_LimitRangeInfo = { }
        self.m_TriggerEnable = { }
        self.m_CheckKillTrigger = { }
        self.m_UnLockWeapon = 0
        self.m_EnableModifyTimes = 0
        self.m_NeedAttention = 0
        self.m_Enable = 0

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, self.m_CallFlag, -1, 0)

    
    def Release(self):
        if self.m_Enable:
            self.m_Enable = 0
            oWarMgr = self.m_WarMgr
            cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_UNLOCK, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_TALENT_GEN, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_CallFlag)
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_ASSISTKILL, self.m_CallFlag)
        self.m_WarMgr = None
        super().Release()

    
    def Save(self):
        return {
            'TriggerEnable': self.m_TriggerEnable,
            'DisplayTimesInfo': self.m_DisplayTimesInfo,
            'CheckKillTrigger': self.m_CheckKillTrigger,
            'UnLockWeapon': self.m_UnLockWeapon }

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_TriggerEnable = dData.get('TriggerEnable', { })
        self.m_DisplayTimesInfo = dData.get('DisplayTimesInfo', { })
        self.m_CheckKillTrigger = dData.get('CheckKillTrigger', { })
        self.m_UnLockWeapon = dData.get('UnLockWeapon', 0)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        if oWarMgr.m_Round != 1 or not oWarMgr.IsSingleGame(bExcludeAIMember = True) or oWarMgr.IsTransferGame():
            return None
        self.m_Enable = 1
        cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_STARTFIGHT, self.OnStartFight, self.m_CallFlag)
        for sTrigger, dInfo in self.m_TriggerInfo.items():
            self.m_TriggerNotify[sTrigger] = dInfo['Notify']
            self.m_DisplayTimesInfo[sTrigger] = 0
            self.m_MaxDisplayTimesInfo[sTrigger] = dInfo['MaxDisplayTimes']
            self.m_LimitRangeInfo[sTrigger] = dInfo['LimitRange']
            self.m_OwnColdFrameInfo[sTrigger] = Time2Frame(dInfo['OwnColdTime'])
            self.m_LastOwnDisplayFrame[sTrigger] = 0
        
        lstHero = self.m_WarMgr.GetRoomHero(iCalAI = 0)
        if lstHero:
            iHero = lstHero[0]
            self.m_NewbieOwner = iHero
            self.CheckInitEvent(iHero)

    
    def CheckInitEvent(self, iHero):
        oGame = self.m_Game
        oHero = oGame.GetObject(iHero)
        if oHero.m_SID == HERO_SID and not (self.m_UnLockWeapon):
            self.InitModifyTalentWeight(oHero)
        for sTrigger, dInfo in self.m_TriggerInfo.items():
            if sTrigger not in self.m_TriggerEnable:
                self.SetTriggerEnable(sTrigger, self.CheckCondiction(oHero, sTrigger, dInfo))
        
        NewbietutorialLog.Debug('%d %d grade:%s playtimes:%s enable event: %s' % (oGame.m_ID, oHero.m_PlayerID, oHero.m_PlayerGrade, oHero.Query('AllSeasonRGPlayTimes', 0), self.m_TriggerEnable))
        if self.CheckHasChooseTriggerEnable(MIXDEBUFF_TRIGGER):
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, self.OnCauseMixDebuff, self.m_CallFlag)
        if self.CheckHasChooseTriggerEnable(DAM_EVENT_TRIGGER):
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, self.m_CallFlag)
        if self.m_CheckKillTrigger:
            cl_msgcenter.AddAttentionFunc(self, iHero, cl_msgcenter.MSG_WAR_ASSISTKILL, self.OnAssistKill, self.m_CallFlag)

    
    def InitModifyTalentWeight(self, oHero):
        iHasLock = 0
        lstAllWeapon = oHero.Query('Illus')['Weapon']
        for iLock in self.m_LockModifyInfo['lstLock']:
            if iLock not in lstAllWeapon:
                iHasLock = 1
                break
        
        if iHasLock:
            self.m_NeedAttention = 1
            for iTalent, iModify in self.m_LockModifyInfo['dModify'].items():
                if iModify:
                    self.ModifyTalentWeight(oHero, iTalent, iModify)
            
        for iUnlock in self.m_UnlockModifyInfo:
            if iUnlock not in lstAllWeapon:
                cl_msgcenter.AddAttentionFunc(self, oHero.m_ID, cl_msgcenter.MSG_WAR_UNLOCK, self.OnUnlock, self.m_CallFlag)
                break
        

    
    def OnStartFight(self, oElement, oWarMgr, dMsgInfo):
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return None
        for sTrigger in TRIGGERTYPE_TO_SAVE.values():
            tRange = self.m_LimitRangeInfo[sTrigger]
            if not tRange:
                continue
            iLimitLayer = tRange[0]
            iLimitLevel = tRange[1]
            if not iLimitLayer and not iLimitLevel:
                continue
            if not oLevelCtrl.m_LayerNum > iLimitLayer:
                if oLevelCtrl.m_LayerNum == iLimitLayer and iLimitLevel and oLevelCtrl.m_LevelNum > iLimitLevel:
                    self.SetTriggerEnable(sTrigger, False)
                    self.DisableEventByTrigger(sTrigger)
                    continue
        

    
    def OnUnlock(self, oElement, oHero, dMsgInfo):
        if 'Type' not in dMsgInfo or dMsgInfo['Type'] != PROGRESSUNLOCK_WEAPON or 'RewardSID' not in dMsgInfo:
            return None
        iWeapon = dMsgInfo['RewardSID']
        if self.m_NeedAttention and iWeapon in self.m_LockModifyInfo['lstLock']:
            self.m_NeedAttention = 0
            for iTalent in self.m_LockModifyInfo['dModify']:
                self.ModifyTalentWeight(oHero, iTalent, 0)
            
            if self.m_UnLockWeapon:
                cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_UNLOCK, self.m_CallFlag)
        if not (self.m_UnLockWeapon) and iWeapon in self.m_UnlockModifyInfo:
            self.m_UnLockWeapon = iWeapon
            if not self.m_NeedAttention:
                cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_UNLOCK, self.m_CallFlag)
            NewbietutorialLog.Debug('%d %d unlock %s' % (oHero.m_Game.m_ID, oHero.m_PlayerID, iWeapon))
            self.OnUnlockModify(oHero, iWeapon)

    
    def OnUnlockModify(self, oHero, iWeapon):
        cl_msgcenter.AddAttentionFunc(self, oHero.m_ID, cl_msgcenter.MSG_WAR_TALENT_GEN, self.OnTalentGen, self.m_CallFlag)
        for iTalent, iModify in self.m_UnlockModifyInfo[iWeapon].items():
            if iModify:
                self.ModifyTalentWeight(oHero, iTalent, iModify)
        

    
    def ModifyTalentWeight(self, oTarget, iTalent, iModify):
        NewbietutorialLog.Debug('%d %d modify talent %s %s' % (oTarget.m_Game.m_ID, oTarget.m_PlayerID, iTalent, iModify))
        lstReward = [
            {
                'item': VIRTUAL_ITEM_TALENTWEIGHT,
                'info': {
                    'talent': iTalent,
                    'modify': iModify } }]
        cl_reward.RewardItem(oTarget.m_Game, oTarget, lstReward, self.m_CallFlag, { })

    
    def OnTalentGen(self, oElement, oHero, dMsgInfo):
        self.m_EnableModifyTimes += 1
        if self.m_EnableModifyTimes >= self.m_MaxModifyTimes:
            NewbietutorialLog.Debug('%d %d modify %s end' % (oHero.m_Game.m_ID, oHero.m_PlayerID, self.m_UnLockWeapon))
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_TALENT_GEN, self.m_CallFlag)
            if self.m_UnLockWeapon in self.m_UnlockModifyInfo:
                for iTalent in self.m_UnlockModifyInfo[self.m_UnLockWeapon]:
                    self.ModifyTalentWeight(oHero, iTalent, 0)
                

    
    def OnCauseMixDebuff(self, oElement, oHero, dMsgInfo):
        if 'StateSID' not in dMsgInfo:
            return None
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        if not self.CheckShareColdFrame(iCurFrame):
            return None
        sTargetTrigger = ''
        for sTrigger, iStateSID in MIXDEBUFF_TRIGGER.items():
            if dMsgInfo['StateSID'] == iStateSID:
                sTargetTrigger = sTrigger
                break
        
        if not sTargetTrigger:
            return None
        iNotify = self.m_TriggerNotify[sTargetTrigger] if sTargetTrigger in self.m_TriggerNotify else 0
        if iNotify:
            self.CheckDisplay(iCurFrame, sTargetTrigger, iNotify)
            self.TryNotify(oHero, iCurFrame)

    
    def CheckDisplay(self, iCurFrame, sTrigger, iNotify):
        if not sTrigger or not iNotify or not self.GetTriggerEnable(sTrigger):
            return None
        if self.CheckOwnColdFrameByTrigger(sTrigger, iCurFrame) and self.CheckDisplayTimes(sTrigger):
            self.m_FrameDisplayInfo[iCurFrame] = iNotify

    
    def OnDealTotalDam(self, oElement, oHero, dMsgInfo):
        if 'CurVID' not in dMsgInfo:
            return None
        oGame = self.m_Game
        oVictim = oGame.GetObject(dMsgInfo['CurVID'])
        if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
            return None
        iCurFrame = oGame.GetFrameNum()
        if not self.CheckShareColdFrame(iCurFrame):
            return None
        if iCurFrame in self.m_FrameDisplayInfo:
            return None
        sTargetTrigger = ''
        for sTrigger, (cbFunc, iArg) in DAM_EVENT_TRIGGER.items():
            if cbFunc(self, dMsgInfo, iCurFrame, iArg):
                sTargetTrigger = sTrigger
                break
        
        if sTargetTrigger:
            self.m_FrameDisplayInfo[iCurFrame] = self.m_TriggerNotify[sTargetTrigger]
            self.TryNotify(oHero, iCurFrame)

    
    def OnAssistKill(self, oElement, oHero, dMsgInfo):
        if 'VID' not in dMsgInfo:
            return None
        oGame = self.m_Game
        oTarget = oGame.GetObject(dMsgInfo['VID'])
        if oTarget and oTarget.m_SID == BOSS_LUWU and oTarget.m_FightType & WARRIOR_MONSTER:
            NewbietutorialLog.Info('%d %d kill %s and unlock %s' % (oGame.m_ID, oHero.m_PlayerID, BOSS_LUWU, self.m_CheckKillTrigger))
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_ASSISTKILL, self.m_CallFlag)
            for sTrigger in self.m_CheckKillTrigger:
                self.SetTriggerEnable(sTrigger, True)
                if sTrigger in MIXDEBUFF_TRIGGER:
                    cl_msgcenter.AddAttentionFunc(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, self.OnCauseMixDebuff, self.m_CallFlag)
                if sTrigger in DAM_EVENT_TRIGGER:
                    cl_msgcenter.AddAttentionFunc(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, self.m_CallFlag)
            
            self.m_CheckKillTrigger = { }

    
    def DisableEventByTrigger(self, sTrigger):
        if sTrigger in MIXDEBUFF_TRIGGER and not self.CheckHasChooseTriggerEnable(MIXDEBUFF_TRIGGER):
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, self.m_CallFlag)
        if sTrigger in DAM_EVENT_TRIGGER and not self.CheckHasChooseTriggerEnable(DAM_EVENT_TRIGGER):
            cl_msgcenter.DoneAttention(self, self.m_NewbieOwner, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.m_CallFlag)

    
    def CheckBasicCondiction(self, oHero, dInfo):
        tGradeInfo = dInfo['PlayerGrade']
        tPlayTimes = dInfo['PlayTimes']
        iPlayerGrade = oHero.m_PlayerGrade
        iPlayTimes = oHero.Query('AllSeasonRGPlayTimes', 0)
        if iPlayerGrade < tGradeInfo[0] or iPlayerGrade >= tGradeInfo[1]:
            return False
        if iPlayTimes < tPlayTimes[0] or iPlayTimes >= tPlayTimes[1]:
            return False
        return True

    
    def CheckCondiction(self, oHero, sTrigger, dInfo):
        if not self.CheckBasicCondiction(oHero, dInfo):
            return False
        lstExtra = dInfo['ExtraRule']
        for iRule in lstExtra:
            if not EXTRARULE_FUNC[iRule](self, oHero, sTrigger):
                return False
        
        return True

    
    def CheckShareColdFrame(self, iCurFrame):
        if self.m_LastDisplayFrame and iCurFrame - self.m_LastDisplayFrame < self.m_ShareColdFrame:
            return False
        return True

    
    def CheckOwnColdFrameByTrigger(self, sTrigger, iCurFrame):
        iLastOwnDisplayFrame = self.m_LastOwnDisplayFrame[sTrigger]
        if iLastOwnDisplayFrame and iCurFrame - iLastOwnDisplayFrame < self.m_OwnColdFrameInfo[sTrigger]:
            return False
        return True

    
    def CheckDisplayTimes(self, sTrigger):
        iDisplayTimes = self.m_DisplayTimesInfo[sTrigger] if sTrigger in self.m_DisplayTimesInfo else 0
        iMaxDisplayTimes = self.m_MaxDisplayTimesInfo[sTrigger] if sTrigger in self.m_MaxDisplayTimesInfo else 0
        if iMaxDisplayTimes <= iDisplayTimes:
            return False
        return True

    
    def TryNotify(self, oHero, iCurFrame):
        if iCurFrame in self.m_FrameDisplayInfo:
            self.m_LastDisplayFrame = iCurFrame
            iNotify = self.m_FrameDisplayInfo[iCurFrame]
            sTrigger = self.GetNotifyTriggerType(iNotify)
            if self.AddDisplayTimes(sTrigger):
                self.m_LastOwnDisplayFrame[sTrigger] = iCurFrame
                NewbietutorialLog.Debug('%d %d frame:%s trigger: %s notify: %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iCurFrame, sTrigger, iNotify))
                cl_notify.SendCommonNotify(self.m_Game, {
                    oHero.m_PlayerID: 1 }, iNotify, { })

    
    def GetNotifyTriggerType(self, iNotify):
        for sTrigger, iCheckNotify in self.m_TriggerNotify.items():
            if iNotify == iCheckNotify:
                return sTrigger
        
        return ''

    
    def AddDisplayTimes(self, sTrigger):
        if sTrigger not in self.m_DisplayTimesInfo:
            return False
        self.m_DisplayTimesInfo[sTrigger] += 1
        if self.m_DisplayTimesInfo[sTrigger] >= self.m_MaxDisplayTimesInfo[sTrigger]:
            self.SetTriggerEnable(sTrigger, False)
            self.DisableEventByTrigger(sTrigger)
        return True

    
    def GetMaxDisplayTimes(self, sTrigger):
        if sTrigger not in self.m_MaxDisplayTimesInfo:
            return 0
        return self.m_MaxDisplayTimesInfo[sTrigger]

    
    def GetDisplayTimes(self, sTrigger):
        if sTrigger not in self.m_DisplayTimesInfo:
            return 0
        return self.m_DisplayTimesInfo[sTrigger]

    
    def GetRemainShareColdFrame(self):
        if self.m_LastDisplayFrame:
            iRemainFrame = self.m_ShareColdFrame - self.m_Game.GetFrameNum() - self.m_LastDisplayFrame
            if iRemainFrame > 0:
                return iRemainFrame
        return self.m_ShareColdFrame

    
    def GetRemainOwnColdFrame(self, sTrigger):
        if sTrigger not in self.m_OwnColdFrameInfo:
            return 0
        iLastOwnDisplayFrame = self.m_LastOwnDisplayFrame[sTrigger]
        if iLastOwnDisplayFrame:
            iRemainFrame = self.m_OwnColdFrameInfo[sTrigger] - self.m_Game.GetFrameNum() - iLastOwnDisplayFrame
            if iRemainFrame > 0:
                return iRemainFrame
        return self.m_OwnColdFrameInfo[sTrigger]

    
    def SetTriggerEnable(self, sTrigger, bEnable):
        self.m_TriggerEnable[sTrigger] = bEnable

    
    def GetTriggerEnable(self, sTrigger):
        if sTrigger not in self.m_TriggerEnable:
            return False
        return self.m_TriggerEnable[sTrigger]

    
    def CheckHasChooseTriggerEnable(self, dTrigger):
        for sTrigger in dTrigger:
            if sTrigger not in self.m_TriggerEnable:
                continue
            if self.m_TriggerEnable[sTrigger]:
                return True
        
        return False



def GetComponentClass(oMgrManager):
    return CNewbieTutorialElement

