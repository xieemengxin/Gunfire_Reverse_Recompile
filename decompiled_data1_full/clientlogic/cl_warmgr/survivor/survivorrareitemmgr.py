# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/survivorrareitemmgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/survivorrareitemmgr.pyc
# Source Generated with Decompyle++
# File: survivorrareitemmgr.pyc (Python 3.6)

from cl_object.logging import SurvivorLog
from cl_commondefines import WARRIOR_MONSTER, MG_SOURCE_KILLMONSTER, WARRIOR_HERO
import cl_msgcenter
import cl_formula
import cl_reward
import cl_platformdata

class CSurvivorRareItemMgr(object):
    
    def __init__(self, oSurvivorElement, oData):
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_CallFlag = 'SurvivorRareItemMgr'
        self.m_RareItemInfo = oData.m_RareItemConfig
        self.m_RareItemDropRecord = { }
        self.m_CurRareItemMinGameSID = 0
        self.m_DropInfo = { }
        self.m_ExcludeRareItem = { }
        self.m_CurRareItemConfig = { }

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_CallFlag, -1, 0)
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnDie, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROPRAREITEM, self.OnDrop, self.m_CallFlag)
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REWARDRAREITEM, self.OnReward, self.m_CallFlag)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DROPRAREITEM, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_REWARDRAREITEM, self.m_CallFlag)
        self.m_Survivor = None
        self.m_Game = None
        self.m_RareItemDropRecord = { }
        self.m_CurRareItemMinGameSID = 0
        self.m_DropInfo = { }
        self.m_ExcludeRareItem = { }
        self.m_CurRareItemConfig = { }

    
    def OnPhaseStart(self, oSurvivor, dMsgInfo):
        iPhase = dMsgInfo['Phase']
        self.SetCurRareIteMinGame(iPhase)

    
    def SetCurRareIteMinGame(self, iPhase):
        for iMiniGame, dInfo in self.m_RareItemInfo.items():
            if iMiniGame not in self.m_CurRareItemConfig:
                continue
            if iPhase not in dInfo['PhaseGroup']:
                continue
            if self.m_CurRareItemMinGameSID != iMiniGame:
                self.m_CurRareItemMinGameSID = iMiniGame
                self.m_DropInfo = { }
        else:
            self.m_CurRareItemMinGameSID = 0
            self.m_DropInfo = { }

    
    def OnDie(self, oWarMgr, oTarget, dInfo):
        oReason = dInfo['RS'] if 'RS' in dInfo else None
        if oReason and oReason.GetStrReason() == 'SurvivorGoalOK':
            return None
        if oTarget.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
            self.TryDropRareItem(oTarget, dInfo)

    
    def TryDropRareItem(self, oMonster, dInfo):
        if self.m_CurRareItemMinGameSID not in self.m_RareItemInfo:
            return None
        dRareItemInfo = self.m_RareItemInfo[self.m_CurRareItemMinGameSID]
        iExpectNum = cl_formula.GetFormulaResult(self, dRareItemInfo['ExpectNum'])
        if len(self.m_DropInfo) >= iExpectNum:
            return None
        iAttack = dInfo['AID']
        oAttack = self.m_Game.GetObject(iAttack)
        if not oAttack or oAttack.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        if iAttack in self.m_DropInfo:
            return None
        if oMonster.m_SID not in dRareItemInfo['TargetMonster']:
            return None
        if self.m_Game.Random(10000) < dRareItemInfo['DropRatio']:
            SurvivorLog.Debug('game:%d droprareitem:%d %d %d' % (self.m_Game.m_ID, self.m_Survivor.m_Phase, oMonster.m_SID, iAttack))
            self.m_DropInfo[iAttack] = 1
            dReward = {
                self.m_CurRareItemMinGameSID: (10000, 1) }
            dExtInfo = {
                'CalOffset': 0,
                'CheckGoldenCup': 1,
                'Abandoner': oMonster.m_ID,
                'CanReward': 1,
                'AutoReward': 1,
                'ExcludeRareItem': self.m_ExcludeRareItem }
            cl_reward.RewardItemByMiniGame(oMonster, iAttack, dReward, 'RareItemReward%d' % iAttack, MG_SOURCE_KILLMONSTER, dExtInfo)

    
    def OnDrop(self, oWarMgr, oTarget, dInfo):
        if 'lstRareItem' not in dInfo:
            return None
        for oRareItem in dInfo['lstRareItem']:
            if not oRareItem:
                continue
            self.RareItemRecord(oRareItem)
        

    
    def OnReward(self, oWarMgr, oTarget, dInfo):
        if 'Item' not in dInfo:
            return None
        oRareItem = dInfo['Item']
        if not oRareItem:
            return None
        self.RareItemRecord(oRareItem)

    
    def RareItemRecord(self, oRareItem):
        iRareItemSID = oRareItem.m_SID
        if iRareItemSID not in self.m_RareItemDropRecord:
            self.m_RareItemDropRecord[iRareItemSID] = 0
        self.m_RareItemDropRecord[iRareItemSID] += 1
        dRareItemLimit = cl_platformdata.GetRareItemLimit()
        iMaxCnt = cl_formula.GetFormulaResult(self, dRareItemLimit[iRareItemSID])
        if iMaxCnt and self.m_RareItemDropRecord[iRareItemSID] >= iMaxCnt:
            self.m_ExcludeRareItem[iRareItemSID] = 1



def NewSurvivorRareItemMgr(oSurvivorElement, oData):
    oMgr = CSurvivorRareItemMgr(oSurvivorElement, oData)
    oMgr.Init()
    return oMgr

