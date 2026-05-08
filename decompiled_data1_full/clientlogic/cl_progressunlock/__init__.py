# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_progressunlock/__init__.pyc
# RelativePath: clientlogic/cl_progressunlock/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import PROGRESSUNLOCK_RELIC, PROGRESSUNLOCK_WEAPON, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_RELIC, DROP_REASON_UNLOCK, LEVEL_TYPE_BOSS, ADJUSTWEAPON_UI, ITEM_SOURCE_GOOD
from cl_object.logging import WarunlockprogressLog
from cl_minigame.mg_equip import GetWeaponDropInfo
import cl_platformdata
import cl_reward
import cl_item
import cl_notify
import cl_msgcenter
import cl_putdata
import cl_snetwar
from . import trigger

class CProgressUnlock(object):
    
    def __init__(self, oGame, iOwner, iPlayer):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayer
        self.m_Trigger = { }
        self.m_Progress = { }
        self.m_DoneProgress = { }
        self.m_AdjustWeapon = []
        self.m_AlreadyShowUI = []
        self.AddAttention()

    
    def AddAttention(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            cl_msgcenter.AddAttentionFunc(oHero, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, InitPlayer, 'InitProgressUnlock')
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OnEnterScene, 'OnEnterScene', iOnce = 1)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_WIELDWEAPON, self.OnWieldAdjustWeapon, 'WieldAdjustWeapon', iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_BUYGOODS, self.OnBuyGood, 'BuyGood', iOnce = 0)
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_WEAPON_BEFORECREATE, self.OnCreateWeapon, 'CreateWeapon', iOnce = 0)

    
    def DoneAttention(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if oHero:
            cl_msgcenter.DoneAttention(oHero, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'InitProgressUnlock')
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_ENTERSCENE, 'OnEnterScene')
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_WIELDWEAPON, 'WieldAdjustWeapon')
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_BUYGOODS, 'BuyGood')
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_WEAPON_BEFORECREATE, 'CreateWeapon')

    
    def OnEnterScene(self, oOwner, dMsgInfo):
        self.SendAdjustWeapon()

    
    def OnWieldAdjustWeapon(self, oOwner, dInfo):
        if 'SID' not in dInfo:
            return None
        iWeaponSID = dInfo['SID']
        self.ChangeAdjustWeapon(iWeaponSID)

    
    def OnBuyGood(self, oOwner, dInfo):
        if 'SID' not in dInfo:
            return None
        iGoodSID = dInfo['SID']
        self.ChangeAdjustWeapon(iGoodSID)

    
    def OnCreateWeapon(self, oOwner, dInfo):
        if 'EquipSID' not in dInfo:
            return None
        if 'Source' in dInfo and dInfo['Source'] == ITEM_SOURCE_GOOD:
            return None
        iWeaponSID = dInfo['EquipSID']
        if iWeaponSID in self.m_AdjustWeapon and iWeaponSID not in self.m_AlreadyShowUI:
            self.m_AlreadyShowUI.append(iWeaponSID)
            cl_snetwar.GS2CUpdateUI(self.m_Game, ADJUSTWEAPON_UI, 0, '', { }, {
                'SID': iWeaponSID }, [
                self.m_PlayerID])

    
    def GetProgress(self):
        return self.m_Progress

    
    def GetAdjustWeaponData(self):
        dData = {
            'AdjustWeapon': list(self.m_AdjustWeapon),
            'AlreadyShowUI': list(self.m_AlreadyShowUI) }
        return dData

    
    def ChangeAdjustWeapon(self, iItemSID):
        if not iItemSID or iItemSID not in self.m_AdjustWeapon:
            return None
        self.m_AdjustWeapon.remove(iItemSID)
        if iItemSID in self.m_AlreadyShowUI:
            self.m_AlreadyShowUI.remove(iItemSID)
        self.SendAdjustWeapon()

    
    def SendAdjustWeapon(self):
        cl_notify.SendAdjustWeapon(self.m_Game, self.m_PlayerID, list(self.m_AdjustWeapon))

    
    def Save(self):
        if self.m_Game.m_WarMgr.CheckInitSingleGame():
            return { }
        dProgress = { }
        for iSID, iProgress in self.m_Progress.items():
            if iSID in self.m_DoneProgress:
                continue
            dProgress[iSID] = iProgress
        
        dData = {
            'PRO': dProgress,
            'AW': list(self.m_AdjustWeapon),
            'ASU': list(self.m_AlreadyShowUI) }
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_Progress = dData.get('PRO', { })
        self.m_AdjustWeapon = dData.get('AW', [])
        self.m_AlreadyShowUI = dData.get('ASU', [])

    
    def Register(self, dProgress):
        if not dProgress:
            return None
        self.m_Progress.update(dProgress)

    
    def InitAdjustWeaponData(self, dWeaponInfo):
        if not dWeaponInfo:
            return None
        if 'AdjustWeapon' in dWeaponInfo:
            self.m_AdjustWeapon = dWeaponInfo['AdjustWeapon']
        if 'AlreadyShowUI' in dWeaponInfo:
            self.m_AlreadyShowUI = dWeaponInfo['AlreadyShowUI']

    
    def InitProgress(self):
        dPutRelic = cl_platformdata.GetRelicPut()
        setWeapon = set(cl_putdata.GetAllPutWeapon())
        for iSID, iProgress in list(self.m_Progress.items()):
            clsData = cl_platformdata.GetUnlockProgressCls(iSID)
            if not clsData:
                WarunlockprogressLog.Info('%s err clsdata' % iSID)
                self.m_Progress.pop(iSID)
                continue
            iTriggerType = clsData.m_TriggerType
            if iTriggerType not in trigger.g_UnlockTrigger:
                WarunlockprogressLog.Info('%s err type %s' % (iSID, iTriggerType))
                self.m_Progress.pop(iSID)
                continue
            iType = clsData.m_Type
            iRewardSID = clsData.m_RewardSID
            if not iType == PROGRESSUNLOCK_RELIC or dPutRelic.get(iRewardSID, 0):
                WarunlockprogressLog.Alert(f'''relic{iRewardSID} no put but have unlock{iSID}''')
                self.m_Progress.pop(iSID)
                continue
            if iType == PROGRESSUNLOCK_WEAPON and iRewardSID not in setWeapon:
                WarunlockprogressLog.Info(f'''weapon{iRewardSID} no put but have unlock{iSID}''')
                self.m_Progress.pop(iSID)
                continue
            if iTriggerType not in self.m_Trigger:
                clsTrigger = trigger.g_UnlockTrigger[iTriggerType]
                self.m_Trigger[iTriggerType] = clsTrigger(self)
            oTrigger = self.m_Trigger[iTriggerType]
            oTrigger.Register(iSID, iProgress)
        

    
    def Release(self):
        self.DoneAttention()
        for oTrigger in self.m_Trigger.values():
            oTrigger.Release()
        
        self.m_Trigger = { }
        self.m_Owner = 0
        self.m_Game = None

    
    def GetTrigger(self, iTrigger):
        if iTrigger not in self.m_Trigger:
            return None
        return self.m_Trigger[iTrigger]

    
    def GetDoneProgress(self):
        lUnlock = []
        for iSID in self.m_DoneProgress:
            clsData = cl_platformdata.GetUnlockProgressCls(iSID)
            lUnlock.append([
                clsData.m_Type,
                clsData.m_RewardSID])
        
        return lUnlock

    
    def AddProgress(self, iSID, iAdd, dMsgInfo):
        if iSID not in self.m_Progress or iSID in self.m_DoneProgress:
            return None
        iPlayerID = self.m_PlayerID
        iOwner = self.m_Owner
        oGame = self.m_Game
        iCur = self.m_Progress[iSID]
        iNew = iCur + iAdd
        WarunlockprogressLog.Info('%d add %d %d %d' % (iPlayerID, iSID, iAdd, iNew))
        self.m_Progress[iSID] = iNew
        clsData = cl_platformdata.GetUnlockProgressCls(iSID)
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        dReward = { }
        if self.m_Progress[iSID] >= clsData.m_TargetValue:
            oHero = oGame.GetObject(iOwner)
            oTarget = oGame.GetObject(dMsgInfo['VID'])
            iType = clsData.m_Type
            iRewardSID = clsData.m_RewardSID
            sReason = 'unlockprogress'
            vDropPos = cl_reward.GetDropBasePos(oTarget) if oTarget else oHero.GetPos()
            dIllus = oHero.Query('Illus', { })
            if iType == PROGRESSUNLOCK_RELIC:
                lstForbid = oGame.m_WarMgr.GetForbidRelic()
                if iRewardSID in lstForbid:
                    WarunlockprogressLog.Debug('%d %d forbid relic %d' % (oGame.m_ID, iPlayerID, iRewardSID))
                else:
                    dReward = {
                        'item': VIRTUAL_ITEM_DROP,
                        'info': {
                            'DropType': NWARRIOR_DROP_RELIC,
                            'DropInfo': [
                                iRewardSID],
                            'DropPos': vDropPos } }
                    dIllus['Relic'].add(iRewardSID)
            elif iType == PROGRESSUNLOCK_WEAPON:
                (iGrade, iNewNum) = (0, 0)
                if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
                    (iGrade, iNewNum) = GetWeaponDropInfo(oLevelCtrl, oLevelNode.m_LevelType)
                    iGrade += 1
                    iNewNum += 1
                    iNewNum = min(oGame.m_WarData.GetMaxInscriptionNum(), iNewNum)
                if not iGrade:
                    iGrade = cl_reward.GetWeaponRewardGrade(oGame) + 1
                clsItem = cl_item.GetItemCls(iRewardSID)
                if not clsItem:
                    WarunlockprogressLog.Alert(f'''{iSID} reward cls{iRewardSID} not found''')
                    return None
                dExtraAttr = {
                    'PriorInscription': clsItem.m_UnlockInscription }
                oWeapon = cl_item.CreateEquip(oGame, iRewardSID, iGrade, oOwner = oHero, dExtraAttr = dExtraAttr)
                dInfo = { }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEDROPWEAPON, oHero, dInfo)
                if 'Enhance' in dInfo:
                    oWeapon.AddEnhance(dInfo['Enhance'], dInfo['Reason'])
                oInscriptionCom = oWeapon.GetComponent('Inscription')
                if oInscriptionCom:
                    if not iNewNum:
                        iNewNum = min(oGame.m_WarData.GetMaxInscriptionNum(), oInscriptionCom.m_InscriptionNum + 1)
                    oInscriptionCom.m_InscriptionNum = iNewNum
                    oInscriptionCom.AddInscription()
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_EQUIP,
                        'DropInfo': [
                            oWeapon],
                        'DropPos': vDropPos } }
                dIllus['Weapon'] = tuple(set(dIllus['Weapon']) | set([
                    iRewardSID]))
            else:
                WarunlockprogressLog.Alert(f'''未知解锁类型{iType} {iSID} {iRewardSID}''')
                return None
            self.m_DoneProgress[iSID] = 1
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UNLOCK, oHero, {
                'RewardSID': iRewardSID,
                'Type': iType })
            dExtInfo = {
                'Player': iOwner,
                'Abandoner': oTarget.m_ID,
                'DropReason': DROP_REASON_UNLOCK,
                'Scene': oTarget.m_Scene }
            if dReward:
                cl_reward.RewardItem(oGame, oHero, [
                    dReward], sReason, dExtInfo)
            oLevelNode.SetRandomChoose(iOwner)
            cl_notify.SendUnlockNotify(oGame, iPlayerID, iSID, iRewardSID, iType)



def InitPlayer(oListener, _oWarMgr, _dInfo):
    oListener.m_UnlockProgressCon.InitProgress()

