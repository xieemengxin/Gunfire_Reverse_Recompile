# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/reliccon.pyc
# RelativePath: clientlogic/cl_container/reliccon.pyc
# Source Generated with Decompyle++
# File: reliccon.pyc (Python 3.6)

from cl_commondefines import BAY_TYPE_RELIC, PF_TYPE_RELIC, RELIC_TYPE_CURSE, RELIC_RS_LOAD, VIRTUAL_ITEM_RELIC, RELIC_TYPE_NORMAL, RECYCLE_RELIC, EXTENDRELIC_TO_TEMPRELIC, EXTENDBAG_TO_NORMAL, EXTENDBAG_TO_EXTEND
from cl_commondefines import NPC_CB_VALUELIST, RELICBAG_TYPE_EXTEND, MAX_EXTEND_RELIC_NUM, RECYCLE_EXTEND_RELIC, EXTENDBAG_TYPE_RELIC, BLANKRELIC, DROP_REASON_DISCARDRELIC, ALL_TEMPREMOVERELIC_TYPE
from cl_commondefines import NORMAL_REMOVE_RELIC, EXTEND_REMOVE_RELIC, RELIC_TO_NORMAL, TEMPREMOVE_REMOVE_RELIC, REMOVE_RELIC_TO_TEMPREMOVERELIC_TYPE, RELIC_TO_TEMPRELIC
from cl_commondefines import TEMPRELIC_CHECKSTATE_NOEXISTRELIC, TEMPRELIC_CHECKSTATE_NOALLOWREMOVE, TEMPRELIC_CHECKSTATE_UNOPENTYPE, TEMPRELIC_CHECKSTATE_HASRELIC, TEMPRELIC_CHECKSTATE_CANADD
from cl_cscommondef.cs_itemdef import QUALITY_TYPE_LOW
from cl_object.logging import WarrelicLog
from cl_only import ChooseKey, Functor, ShufferList
from cl_npc.eventnpcaction import EVENT_TYPE_DISABLE_CURSE_RELIC
from cl_only import SendAlert
from cl_platformdata import GetBreedRelicGroup
import cl_drop
import cl_container.performcon
import cl_perform.load
import cl_duonet.dn_cl_container_reliccon as relicnet
import cl_msgcenter
import cl_notify
import cl_object.reason
import cl_perform
import cl_platformdata
import cl_reward
import cl_npc.net as npcnet
import cl_snetwar

def GS2CAddRelic(oGame, iWarrior, iSID, iLevel, iPos, iValidRemove, dPlayer, iRollNum, iValidRecycle, iForceDisable, iNotifyType = 0, iSourceReason = 0):
    if not dPlayer:
        dPlayer = oGame.GetRealPlayers()
    netData = {
        'iWarrior': iWarrior,
        'iRelicSID': iSID,
        'iLevel': iLevel,
        'iPos': iPos,
        'iValidRemove': iValidRemove,
        'oGame': oGame,
        'dPlayer': dPlayer,
        'iRollNum': iRollNum,
        'iValidRecycle': iValidRecycle,
        'iForceDisable': iForceDisable,
        'iNotifyType': iNotifyType,
        'iPlaySource': iSourceReason }
    relicnet.DN_GS2CAddRelic(netData)


def GS2CRemoveRelic(oGame, iWarrior, iSID):
    netData = {
        'iWarrior': iWarrior,
        'iRelicSID': iSID,
        'oGame': oGame }
    relicnet.DN_GS2CRemoveRelic(netData)


def GS2CReplaceRelic(oGame, pid, iOldRelic, iNewRelic):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'iOldRelic': iOldRelic,
        'iNewRelic': iNewRelic }
    relicnet.DN_GS2CReplaceRelic(netData)


def GS2CAddExtraRelic(oGame, pid, iRelicSID):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'iRelicSID': iRelicSID }
    relicnet.DN_GS2CAddExtraRelic(netData)


def GS2CRandomRemoveRelic(oGame, pid, iRelicSID):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'iRelicSID': iRelicSID }
    relicnet.DN_GS2CRandomRemoveRelic(netData)


def GS2CRefreshRelicResult(oGame, pid, lstRelic):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'lstRelic': lstRelic }
    relicnet.DN_GS2CRefreshRelicResult(netData)


def GS2CRefreshRelic(oGame, pid, iNum):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'iNum': iNum }
    relicnet.DN_GS2CRefreshRelic(netData)


def GS2CUpdateShowQuality(oGame, pid, dUpdate, iUpgradeNum, iUpgradeType):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'dUpdate': dUpdate,
        'iUpgradeNum': iUpgradeNum,
        'iUpgradeType': iUpgradeType }
    relicnet.DN_GS2CUpdateShowQuality(netData)


def GS2CAddExtendRelic(oGame, pid, iSID, iLevel, iRollNum, iValidRecycle):
    netData = {
        'pid': pid,
        'iRelicSID': iSID,
        'iLevel': iLevel,
        'oGame': oGame,
        'iRollNum': iRollNum,
        'iValidRecycle': iValidRecycle }
    relicnet.DN_GS2CAddExtendRelic(netData)


def GS2CRemoveExtendRelic(oGame, pid, iSID):
    netData = {
        'pid': pid,
        'iRelicSID': iSID,
        'oGame': oGame }
    relicnet.DN_GS2CRemoveExtendRelic(netData)


def GS2CUpdateBlankRelicNum(oGame, pid, iRelicSID, iNum, iAddNum):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'iRelicSID': iRelicSID,
        'iNum': iNum,
        'iAddNum': iAddNum }
    relicnet.DN_GS2CUpdateBlankRelicNum(netData)


def GS2CSynTempRemoveRelic(oGame, pid, iGamePlayType, lstRelic):
    netData = {
        'pid': pid,
        'oGame': oGame,
        'iGamePlayType': iGamePlayType,
        'lstRelic': lstRelic }
    relicnet.DN_GS2CSynTempRemoveRelic(netData)


def C2GSRemoveRelic(who, iSID, iOperateType):
    oRelicCon = who.m_RelicCon
    oRelicCon.RemoveRelicByDrop(iSID, iOperateType, iAlert = 0)


def C2GSRefreshRelic(who, lstRelic):
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REFRESHRELIC, who, {
        'lstRelic': lstRelic })


def C2GSExchangeExtendRelic(who, iType, iRelicSID):
    oRelicCon = who.m_RelicCon
    oRelicCon.ExchangeExtendRelic(iType, iRelicSID)


def C2GSHandleTempRemoveRelic(who, iGamePlayType, lstRelic):
    oRelicCon = who.m_RelicCon
    oRelicCon.HandleTempRemoveRelic(iGamePlayType, lstRelic)

BLANKRELIC_MAX = 60000
BREED_RELIC_OBTAIN_MAX = 3

class CRelicContainer(cl_container.performcon.CPerformContainer):
    m_BagType = BAY_TYPE_RELIC
    
    def __init__(self, oWarrior):
        super(CRelicContainer, self).__init__(oWarrior)
        self.m_PosPerform = { }
        self.m_InitCarryNum = 1000
        self.m_MaxNum = 0
        self.m_LimitFunc = None
        self.m_LimitFuncBefore = None
        self.m_ShowQuality = { }
        self.m_RelicType2Relic = { }
        self.m_UnFilterHasNormalRatio = 0
        self.m_UnFilterHasCurseRatio = 0
        self.m_RepeatFunc = None
        self.m_FilterRelic = { }
        self.m_ExtendRelic = { }
        self.m_BlankRelic = 0
        self.m_BreedRelicCount = 0
        self.m_TempRemoveRelic = { }

    
    def Release(self):
        self.m_PosPerform = { }
        self.m_LimitFunc = None
        self.m_LimitFuncBefore = None
        self.m_RepeatFunc = None
        self.m_RelicType2Relic = { }
        super(CRelicContainer, self).Release()

    
    def Save(self):
        dData = super(CRelicContainer, self).Save()
        dValidRemove = { }
        dSource = { }
        dRollNum = { }
        dOwnerInfo = { }
        dForceDisable = { }
        for iSID, oPerform in self.m_Perform.items():
            dValidRemove[iSID] = oPerform.m_ValidRemove
            dSource[iSID] = oPerform.m_Source
            if oPerform.m_PFType == PF_TYPE_RELIC:
                dRollNum[iSID] = oPerform.m_RollNum
            dOwnerInfo[iSID] = oPerform.m_OwnerInfo
            dForceDisable[iSID] = oPerform.m_ForceDisable
        
        dData['VR'] = dValidRemove
        dData['S'] = dSource
        dData['RN'] = dRollNum
        dData['OI'] = dOwnerInfo
        dData['FD'] = dForceDisable
        dExtendRelic = { }
        for iSID, oPerform in self.m_ExtendRelic.items():
            dExtendRelic.setdefault(iSID, { })
            dExtendRelic[iSID]['RN'] = oPerform.m_RollNum
            dExtendRelic[iSID]['OI'] = oPerform.m_OwnerInfo
            dExtendRelic[iSID]['S'] = oPerform.m_Source
            dExtendRelic[iSID]['L'] = oPerform.m_Level
        
        dTempRemoveRelic = { }
        for iGamePlayType, dRelicInfo in self.m_TempRemoveRelic.items():
            dTempRemoveRelic.setdefault(iGamePlayType, { })
            for iSID, oPerform in dRelicInfo.items():
                dTempRemoveRelic[iGamePlayType][iSID] = { }
                dTempRemoveRelic[iGamePlayType][iSID]['RN'] = oPerform.m_RollNum
                dTempRemoveRelic[iGamePlayType][iSID]['OI'] = oPerform.m_OwnerInfo
                dTempRemoveRelic[iGamePlayType][iSID]['S'] = oPerform.m_Source
                dTempRemoveRelic[iGamePlayType][iSID]['L'] = oPerform.m_Level
            
        
        dData['ER'] = dExtendRelic
        dData['TRR'] = dTempRemoveRelic
        dData['BR'] = self.m_BlankRelic
        dData['BRC'] = self.m_BreedRelicCount
        return dData

    
    def Load(self, dData):
        super(CRelicContainer, self).Load(dData)
        dValidRemove = dData.get('VR', { })
        dSource = dData.get('S', { })
        dRollNum = dData.get('RN', { })
        dOwnerInfo = dData.get('OI', { })
        dForceDisable = dData.get('FD', { })
        for iSID, iLevel in dData['PF'].items():
            dExtInfo = { }
            if iSID in dValidRemove:
                dExtInfo['ValidRemove'] = dValidRemove[iSID]
            if iSID in dRollNum:
                dExtInfo['RollNum'] = dRollNum[iSID]
            if iSID in dOwnerInfo:
                dExtInfo['OwnerInfo'] = dOwnerInfo[iSID]
            if iSID in dForceDisable:
                dExtInfo['ForceDisable'] = dForceDisable[iSID]
            self.AddRelic(iSID, RELIC_RS_LOAD, iLevel, dExtInfo = dExtInfo, iSource = dSource.get(iSID, 0))
        
        dExtendRelic = dData.get('ER', { })
        for iSID, dExtInfo in dExtendRelic.items():
            iLevel = dExtInfo['L']
            iSource = dExtInfo['S']
            dExtInfo = {
                'RollNum': dExtInfo['RN'],
                'OwnerInfo': dExtInfo['OI'] }
            self.AddExtendRelic(iSID, RELIC_RS_LOAD, iLevel, dExtInfo = dExtInfo, iSource = iSource)
        
        dTempRemoveRelic = dData.get('TRR', { })
        for iGamePlayType, dRelicInfo in dTempRemoveRelic.items():
            self.m_TempRemoveRelic[iGamePlayType] = { }
            for iSID, dTempRemoveRelicInfo in dRelicInfo.items():
                iLevel = dTempRemoveRelicInfo['L']
                iSource = dTempRemoveRelicInfo['S']
                dExtInfo = {
                    'RollNum': dTempRemoveRelicInfo['RN'],
                    'OwnerInfo': dTempRemoveRelicInfo['OI'] }
                self.AddTempRemoveRelic(iGamePlayType, iSID, RELIC_RS_LOAD, iLevel, dExtInfo = dExtInfo, iSource = iSource)
            
        
        self.m_BlankRelic = dData.get('BR', 0)
        self.m_BreedRelicCount = dData.get('BRC', 0)

    
    def Refresh(self, dPlayer = None):
        if not dPlayer:
            dPlayer = { }
        for iPos, oPerform in self.m_PosPerform.items():
            self.GS2CAddRelic(oPerform, iPos, dPlayer)
        
        super(CRelicContainer, self).Refresh(dPlayer)

    
    def SelfRefresh(self):
        for oPerform in self.m_ExtendRelic.values():
            self.GS2CAddExtendRelic(oPerform)
        
        self.GS2CUpdateBlankRelicNum()
        for iGamePlayType in self.m_TempRemoveRelic:
            self.GS2CSynTempRemoveRelic(iGamePlayType)
        

    
    def CarryNum(self):
        return self.m_InitCarryNum

    
    def MaxRelicNum(self):
        return self.m_MaxNum

    
    def SetMaxRelicNum(self, iNum, cbfunc, iBefore = 0):
        self.m_MaxNum = iNum
        if iBefore:
            self.m_LimitFuncBefore = cbfunc
        else:
            self.m_LimitFunc = cbfunc
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner:
            oOwner.GS2CPropChange('MaxRelicNum', iNum)

    
    def SetRepeatFunc(self, oFunc):
        self.m_RepeatFunc = oFunc

    
    def GetAllPos(self):
        return list(range(1, self.CarryNum() + 1))

    
    def GetRelicPos(self, iPerform):
        if iPerform in self.m_Perform:
            return self.m_Perform[iPerform].m_Pos
        return 0

    
    def IsValidPos(self, iPos):
        if iPos < 1 or iPos > self.CarryNum():
            return False
        return True

    
    def GetEmptyPos(self):
        for iPos in self.GetAllPos():
            if iPos not in self.m_PosPerform:
                return iPos
        
        return 0

    
    def RemoveRelic(self, iSID, sReason, iForce = 0):
        oPerform = self.GetPerform(iSID)
        if not oPerform:
            return False
        if not iForce and not oPerform.ValidRemove():
            return False
        WarrelicLog.Info('%d %d removerelic %d %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, oPerform.m_Level, sReason))
        oOwner = self.m_Game.GetObject(self.m_Owner)
        iPos = oPerform.m_Pos
        iShowQuality = self.GetShowQuality(iSID)
        iRelicType = oPerform.m_RelicType
        self.RemovePerform(oOwner, iSID)
        if iRelicType in self.m_RelicType2Relic and iSID in self.m_RelicType2Relic[iRelicType]:
            self.m_RelicType2Relic[iRelicType].pop(iSID)
        self.m_PosPerform.pop(iPos)
        if iSID in self.m_ShowQuality:
            self.m_ShowQuality.pop(iSID)
        self.GS2CRemoveRelic(iSID)
        oReason = cl_object.reason.CStrReason(sReason)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVERELIC, oOwner, {
            'Force': iForce,
            'iPerform': iSID,
            'RS': oReason,
            'ShowQuality': iShowQuality })
        return True

    
    def AddRelic(self, iSID, sReason, iLevel = 1, dExtInfo = None, iSource = 0):
        if iSID == BLANKRELIC:
            self.ChangeBlankRelicNum(1, sReason)
            return None
        dInfo = {
            'iPerform': iSID,
            'Level': iLevel }
        if dExtInfo:
            dInfo.update(dExtInfo)
        oOwner = self.m_Game.GetObject(self.m_Owner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PREADDRELIC, oOwner, dInfo)
        iSID = dInfo['iPerform']
        pfobj = self.GetPerform(iSID)
        iOldValidRemove = pfobj.ValidRemove() if pfobj else -1
        iRollNum = dExtInfo['RollNum'] if dExtInfo and 'RollNum' in dExtInfo else 0
        iShare = dExtInfo['Share'] if dExtInfo and 'Share' in dExtInfo else 1
        iSourceReason = dExtInfo['SourceReason'] if dExtInfo and 'SourceReason' in dExtInfo else 0
        if pfobj:
            iRepeatDrop = dExtInfo['RepeatDrop'] if dExtInfo and 'RepeatDrop' in dExtInfo else 0
            oHero = self.m_Game.GetObject(self.m_Owner)
            if not iRepeatDrop:
                if pfobj.m_Level >= iLevel:
                    if self.m_RepeatFunc:
                        self.m_RepeatFunc(self.m_Game, self.m_Owner, iSID, iLevel, sReason)
                    elif sReason != 'gm':
                        WarrelicLog.TraceAlert('%d %d repeat relic %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, sReason))
                    return None
                WarrelicLog.Info('%d %d replace %s %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, pfobj.m_Level, iLevel, iOldValidRemove, sReason))
                cl_notify.SendCommonNotify(oHero.m_Game, [
                    oHero.m_PlayerID], 7242, { })
            dStaticInfo = {
                'ShareInfo': pfobj.GetShareInfo(),
                'DropLevel': pfobj.m_Level,
                'DropSource': pfobj.m_Source,
                'RollNum': iRollNum,
                'Share': iShare,
                'OwnerInfo': pfobj.m_OwnerInfo }
            cl_drop.DropPerform(oHero, iSID, dStaticInfo, True)
            self.RemoveRelic(iSID, 'replace', iForce = 1)
        iPFType = cl_perform.GetPerformClassAttr(iSID, 'm_PFType')
        if iPFType != PF_TYPE_RELIC:
            WarrelicLog.Alert('%d %d addrelic %s type %s err %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iPFType, sReason))
            return None
        if self.m_LimitFuncBefore and self.m_LimitFuncBefore(self, iSID, iLevel):
            return None
        WarrelicLog.Info('%d %d addrelic %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iLevel, sReason))
        dInfo = {
            'iPerform': iSID,
            'NewRelic': iSID,
            'Level': iLevel,
            'Reason': sReason,
            'MSG': cl_msgcenter.MSG_WAR_ADDRELIC }
        if dExtInfo:
            dInfo.update(dExtInfo)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDRELIC, oOwner, dInfo)
        iEnable = dInfo.get('Enable', 1)
        oPerform = self.AddPerform(oOwner, iSID, iLevel, 0, iItem = 0)
        if not oPerform:
            WarrelicLog.Alert('%d %d addrelic %s err %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, sReason))
            return None
        oPerform.InitSource(iSource, iSourceReason)
        dOwnerInfo = {
            self.m_PlayerID: 1 }
        if dExtInfo and 'OwnerInfo' in dExtInfo:
            dOwnerInfo.update(dInfo['OwnerInfo'])
        iForceDisable = dExtInfo['ForceDisable'] if dExtInfo and 'ForceDisable' in dExtInfo else 0
        oPerform.SetForceDisable(iForceDisable)
        oPerform.m_OwnerInfo = dOwnerInfo
        oPerform.SetRollNum(iRollNum)
        iValidRemove = -1
        if 'ValidRemove' in dInfo:
            iValidRemove = dInfo['ValidRemove']
        elif pfobj:
            iValidRemove = cl_perform.GetPerformClassAttr(iSID, 'm_ValidRemove')
        if iValidRemove != -1:
            self.RefreshRelicRemove(iSID, iValidRemove)
        iPos = self.GetEmptyPos()
        if not iPos:
            WarrelicLog.Alert('%d %d add relic err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iPos, sReason))
            return oPerform
        self.m_PosPerform[iPos] = oPerform
        oPerform.m_Pos = iPos
        dTypeRelics = self.m_RelicType2Relic.setdefault(oPerform.m_RelicType, { })
        dTypeRelics[iSID] = 1
        if not iForceDisable and iEnable:
            oPerform.Enable(oOwner)
        dMsgInfo = {
            'iPerform': iSID,
            'Reason': sReason,
            'SourceReason': iSourceReason,
            'Level': iLevel }
        if dExtInfo and 'MiniGameSource' in dExtInfo:
            dMsgInfo['MiniGameSource'] = dExtInfo['MiniGameSource']
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDRELICPERFORM, oOwner, dMsgInfo)
        if self.GetPerform(iSID):
            if dExtInfo and 'NotifyType' in dExtInfo:
                iNotifyType = dExtInfo['NotifyType']
            else:
                iNotifyType = 0
            self.GS2CAddRelic(oPerform, iPos, iNotifyType = iNotifyType)
        if self.m_LimitFunc:
            self.m_LimitFunc(self, oPerform)
        self.CheckBreedRelicGroup(oOwner, iSID)
        return oPerform

    
    def IsOpenExtendBag(self):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner and oOwner.IsOpenExtendBag(EXTENDBAG_TYPE_RELIC):
            return True
        return False

    
    def AddExtendRelic(self, iSID, sReason, iLevel = 1, dExtInfo = None, iSource = 0):
        if not self.IsOpenExtendBag():
            WarrelicLog.Alert('%d %d add extendrelic %s is not open' % (self.m_Game.m_ID, self.m_PlayerID, sReason))
            return None
        iPFType = cl_perform.GetPerformClassAttr(iSID, 'm_PFType')
        if iPFType != PF_TYPE_RELIC:
            WarrelicLog.Alert('%d %d add extendrelic %s type %s err %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iPFType, sReason))
            return None
        if self.IsExtendBagFull():
            WarrelicLog.Alert('%d %d add extendrelic %s is full %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, sReason))
            return None
        oGame = self.m_Game
        WarrelicLog.Info('%d %d add extendrelic %d %s %s' % (oGame.m_ID, self.m_PlayerID, iSID, iLevel, sReason))
        oOwner = oGame.GetObject(self.m_Owner)
        oPerform = oGame.m_ResMgr.NewPerform(iSID, oOwner, iLevel)
        oPerform.InitSource(iSource)
        dOwnerInfo = {
            self.m_PlayerID: 1 }
        if dExtInfo and 'OwnerInfo' in dExtInfo:
            dOwnerInfo.update(dExtInfo['OwnerInfo'])
        oPerform.m_OwnerInfo = dOwnerInfo
        iRollNum = dExtInfo['RollNum'] if dExtInfo and 'RollNum' in dExtInfo else 0
        oPerform.SetRollNum(iRollNum)
        self.m_ExtendRelic[iSID] = oPerform
        self.GS2CAddExtendRelic(oPerform)
        return oPerform

    
    def RemoveExtendRelic(self, iSID, sReason):
        if not self.IsOpenExtendBag():
            WarrelicLog.Alert('%d %d add extendrelic %s is not open' % (self.m_Game.m_ID, self.m_PlayerID, sReason))
            return None
        if iSID not in self.m_ExtendRelic:
            return False
        WarrelicLog.Info('%d %d remove extendrelic %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, sReason))
        oPerform = self.m_ExtendRelic.pop(iSID)
        oPerform.Release()
        self.GS2CRemoveExtendRelic(iSID)
        return True

    
    def IsExtendBagFull(self):
        if len(self.m_ExtendRelic) >= MAX_EXTEND_RELIC_NUM:
            return True
        return False

    
    def GetRelicByMixSID(self, iMixSID):
        if not iMixSID & RELICBAG_TYPE_EXTEND:
            return self.GetPerform(iMixSID)
        iSID = self.GetRelicSIDByMixSID(iMixSID)
        return self.GetExtendRelic(iSID)

    
    def GetRelicSIDByMixSID(self, iMixSID):
        return iMixSID & ~RELICBAG_TYPE_EXTEND

    
    def IsExistRelicByMixSID(self, iMixSID):
        if not iMixSID & RELICBAG_TYPE_EXTEND:
            return iMixSID in self.m_Perform
        iSID = self.GetRelicSIDByMixSID(iMixSID)
        return iSID in self.m_ExtendRelic

    
    def RemoveRelicByMixSID(self, iMixSID, sReason, iForce = 0):
        if iMixSID == BLANKRELIC:
            self.ChangeBlankRelicNum(-1, sReason)
            return True
        if not iMixSID & RELICBAG_TYPE_EXTEND:
            return self.RemoveRelic(iMixSID, sReason, iForce)
        iSID = self.GetRelicSIDByMixSID(iMixSID)
        return self.RemoveExtendRelic(iSID, sReason)

    
    def GetAllRelicByMixSID(self):
        dAllRelic = { }
        dAllRelic.update(self.m_Perform)
        for iSID, oPerform in self.m_ExtendRelic.items():
            iMixSID = oPerform.m_SID | RELICBAG_TYPE_EXTEND
            dAllRelic[iMixSID] = oPerform
        
        return dAllRelic

    
    def GetRelicLevelByMixSID(self, iMixSID):
        oPerform = self.GetRelicByMixSID(iMixSID)
        if oPerform:
            return oPerform.m_Level
        if iMixSID == BLANKRELIC and self.m_BlankRelic > 0:
            return 1
        return 0

    
    def IsSuperRelic(self, iMixSID):
        return self.GetRelicLevelByMixSID(iMixSID) > 1

    
    def GetExtendRelic(self, iSID):
        if iSID in self.m_ExtendRelic:
            return self.m_ExtendRelic[iSID]

    
    def GetAllExtendRelic(self):
        return self.m_ExtendRelic.values()

    
    def RefreshRelicRemove(self, iSID, iValidRemove):
        oPerform = self.GetPerform(iSID)
        if not oPerform:
            return None
        oPerform.m_ValidRemove = iValidRemove

    
    def GS2CPerformAdd(self, oPerform, dPlayer = None):
        pass

    
    def GS2CAddRelic(self, oPerform, iPos, dPlayer = None, iNotifyType = 0):
        iSID = oPerform.m_SID
        iLevel = oPerform.m_Level
        oHero = self.m_Game.GetObject(self.m_Owner)
        iRollNum = oPerform.m_RollNum if oPerform.m_Source == oHero.m_PlayerID else 99
        iValidRecycle = 0
        oRecycleDropElement = oHero.m_Game.m_WarMgr.GetComponent('RecycleDropElement')
        if oRecycleDropElement:
            iValidRecycle = oRecycleDropElement.ValidRecycleUnDrop(oHero, RECYCLE_RELIC, iSID)
        if oPerform.m_Source == oHero.m_PlayerID:
            iSourceReason = oPerform.m_SourceReason
        else:
            iSourceReason = 0
        GS2CAddRelic(self.m_Game, self.m_Owner, iSID, iLevel, iPos, oPerform.ValidRemove(), dPlayer, iRollNum, iValidRecycle, oPerform.m_ForceDisable, iNotifyType, iSourceReason)

    
    def GS2CRemoveRelic(self, iSID):
        GS2CRemoveRelic(self.m_Game, self.m_Owner, iSID)

    
    def GS2CAddExtendRelic(self, oPerform):
        iSID = oPerform.m_SID
        iLevel = oPerform.m_Level
        oHero = self.m_Game.GetObject(self.m_Owner)
        iRollNum = oPerform.m_RollNum if oPerform.m_Source == oHero.m_PlayerID else 99
        iValidRecycle = 0
        oRecycleDropElement = oHero.m_Game.m_WarMgr.GetComponent('RecycleDropElement')
        if oRecycleDropElement:
            iValidRecycle = oRecycleDropElement.ValidRecycleUnDrop(oHero, RECYCLE_EXTEND_RELIC, iSID)
        GS2CAddExtendRelic(self.m_Game, self.m_PlayerID, iSID, iLevel, iRollNum, iValidRecycle)

    
    def GS2CRemoveExtendRelic(self, iSID):
        GS2CRemoveExtendRelic(self.m_Game, self.m_PlayerID, iSID)

    
    def GS2CRefreshRelicResult(self, lstRelic):
        GS2CRefreshRelicResult(self.m_Game, self.m_PlayerID, lstRelic)

    
    def GS2CReplaceRelic(self, iOldRelic, iNewRelic):
        GS2CReplaceRelic(self.m_Game, self.m_PlayerID, iOldRelic, iNewRelic)

    
    def GS2CAddExtraRelic(self, iRelicSID):
        GS2CAddExtraRelic(self.m_Game, self.m_PlayerID, iRelicSID)

    
    def GS2CRandomRemoveRelic(self, iRelicSID):
        GS2CRandomRemoveRelic(self.m_Game, self.m_PlayerID, iRelicSID)

    
    def GS2CRefreshRelic(self, iNum):
        GS2CRefreshRelic(self.m_Game, self.m_PlayerID, iNum)

    
    def GS2CUpdateShowQuality(self, lstRelic, iUpgradeNum, iUpgradeType):
        dUpdate = { }
        for iRelic in lstRelic:
            dUpdate[iRelic] = self.m_ShowQuality[iRelic]
        
        GS2CUpdateShowQuality(self.m_Game, self.m_PlayerID, dUpdate, iUpgradeNum, iUpgradeType)

    
    def GS2CSynTempRemoveRelic(self, iGamePlayType):
        if iGamePlayType not in self.m_TempRemoveRelic:
            return None
        lstRelic = []
        dNowTempRelic = self.m_TempRemoveRelic[iGamePlayType]
        for iRelic, oPerform in dNowTempRelic.items():
            lstRelic.append((iRelic, oPerform.m_Level))
        
        GS2CSynTempRemoveRelic(self.m_Game, self.m_PlayerID, iGamePlayType, lstRelic)

    
    def GetAllRelicSID(self):
        dRelic = { }
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_RELIC:
                continue
            dRelic[oPerform.m_SID] = 1
        
        return dRelic

    
    def GetAllRelicSIDByType(self, iType):
        if iType in self.m_RelicType2Relic:
            return list(self.m_RelicType2Relic[iType])
        return []

    
    def GetAllRelicByType(self, iType):
        lstRelicSID = self.GetAllRelicSIDByType(iType)
        lstRelic = []
        for iRelic in lstRelicSID:
            oPerform = self.GetPerform(iRelic)
            if not oPerform:
                continue
            lstRelic.append(oPerform)
        
        return lstRelic

    
    def RemoveRelicByDrop(self, iSID, iOperateType, iAlert = 1, iShare = 1, iForce = 0):
        if iOperateType in NORMAL_REMOVE_RELIC:
            oRelic = self.GetPerform(iSID)
        elif iOperateType in EXTEND_REMOVE_RELIC:
            oRelic = self.GetExtendRelic(iSID)
        elif iOperateType in TEMPREMOVE_REMOVE_RELIC:
            oRelic = self.GetTempRemoveRelic(TEMPREMOVE_REMOVE_RELIC[iOperateType], iSID)
        else:
            oRelic = None
        if not oRelic:
            sLog = '%d %d remove not exist relic!!! %d %d ' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iOperateType)
            if iAlert:
                WarrelicLog.Alert(sLog)
            else:
                WarrelicLog.Debug(sLog)
            return None
        dShareInfo = oRelic.GetShareInfo()
        iSource = oRelic.m_Source
        dStaticInfo = {
            'ShareInfo': dShareInfo,
            'DropLevel': oRelic.m_Level,
            'DropSource': iSource,
            'RollNum': oRelic.m_RollNum,
            'Share': iShare,
            'OwnerInfo': oRelic.m_OwnerInfo,
            'DropReason': DROP_REASON_DISCARDRELIC,
            'SourceReason': oRelic.m_SourceReason }
        dMsgInfo = {
            'Relic': iSID,
            'Hero': self.m_Owner,
            'StaticInfo': dStaticInfo,
            'Operate': 'DropRelic' }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SURVIVOR_HANDLE_RELIC, self.m_Game.GetWarMgr(), dMsgInfo)
        oHero = self.m_Game.GetObject(self.m_Owner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORE_REMOVE_RELIC_DROP, oHero, dMsgInfo, iSub = iOperateType)
        iShare = dStaticInfo['Share']
        sReason = 'dropRelic'
        bRemove = False
        if iOperateType in NORMAL_REMOVE_RELIC:
            bRemove = self.RemoveRelic(iSID, sReason, iForce = iForce)
        elif iOperateType in EXTEND_REMOVE_RELIC:
            bRemove = self.RemoveExtendRelic(iSID, sReason)
        elif iOperateType in TEMPREMOVE_REMOVE_RELIC:
            bRemove = self.RemoveTempRemoveRelic(TEMPREMOVE_REMOVE_RELIC[iOperateType], iSID, sReason, iSendClient = 1)
        if bRemove:
            cl_drop.DropPerform(oHero, iSID, dStaticInfo, bFly = True, iShare = iShare)

    
    def ExchangeExtendRelic(self, iType, iRelicSID):
        if not self.IsOpenExtendBag():
            WarrelicLog.Alert('%d %d exchange extendrelic err' % (self.m_Game.m_ID, self.m_PlayerID))
            return None
        if iType not in (EXTENDBAG_TO_NORMAL, EXTENDBAG_TO_EXTEND):
            return None
        iPFType = cl_perform.GetPerformClassAttr(iRelicSID, 'm_PFType')
        if iPFType != PF_TYPE_RELIC:
            return None
        sReason = 'exchangerelic'
        oPerform = self.GetPerform(iRelicSID)
        oExtendPerform = self.GetExtendRelic(iRelicSID)
        if oPerform and oExtendPerform:
            if oPerform.m_Level >= oExtendPerform.m_Level:
                cl_notify.SendCommonNotify(self.m_Game, [
                    self.m_PlayerID], 2426, { })
                return None
            if self.RemoveRelic(iRelicSID, sReason, iForce = True) and self.RemoveExtendRelic(iRelicSID, sReason):
                self.ExchangeRelic(EXTENDBAG_TO_NORMAL, oExtendPerform, sReason)
                self.ExchangeRelic(EXTENDBAG_TO_EXTEND, oPerform, sReason)
            elif iType == EXTENDBAG_TO_NORMAL:
                if not oExtendPerform:
                    return None
                if self.RemoveExtendRelic(iRelicSID, sReason):
                    self.ExchangeRelic(EXTENDBAG_TO_NORMAL, oExtendPerform, sReason)
                elif not oPerform:
                    return None
        if not None.ValidRemove():
            return None
        if self.RemoveRelic(iRelicSID, sReason, iForce = True):
            self.ExchangeRelic(EXTENDBAG_TO_EXTEND, oPerform, sReason)

    
    def ExchangeRelic(self, iType, oPerform, sReason):
        iLevel = oPerform.m_Level
        iSource = oPerform.m_Source
        dExtInfo = {
            'RollNum': oPerform.m_RollNum,
            'OwnerInfo': oPerform.m_OwnerInfo }
        if iType == EXTENDBAG_TO_NORMAL:
            oRelic = self.AddRelic(oPerform.m_SID, sReason, iLevel, dExtInfo, iSource)
        else:
            oRelic = self.AddExtendRelic(oPerform.m_SID, sReason, iLevel, dExtInfo, iSource)
        if oRelic:
            dShareInfo = oPerform.GetShareInfo()
            oRelic.UploadPickInfo(dShareInfo)

    
    def GetChooseRelicWeight(self, dWeight, iCanRepeat = 0):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if not oHero:
            return { }
        dRelic = { }
        if not iCanRepeat:
            setRelic = oHero.Query('Illus')['Relic'] - set(self.GetFilterRelic())
        else:
            setRelic = oHero.Query('Illus')['Relic']
        for iRelic in setRelic:
            if iRelic in dWeight:
                dRelic[iRelic] = dWeight[iRelic]
        
        return dRelic

    
    def GetChooseRelicSet(self, setRelic, iLevel):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if not oHero:
            return []
        setAllRelic = oHero.Query('Illus')['Relic']
        lstFilterRelic = self.GetFilterRelic()
        for iSID, iCurLevel in self.GetAllPerformLevel().items():
            if iSID in lstFilterRelic and iLevel > iCurLevel:
                lstFilterRelic.remove(iSID)
        
        return setRelic & setAllRelic - set(lstFilterRelic)

    
    def GetAvailableRelic(self, iFilterRelic = 1):
        oHero = self.m_Game.GetObject(self.m_Owner)
        if not oHero:
            return []
        if iFilterRelic:
            return oHero.Query('Illus')['Relic'] - set(self.GetFilterRelic())
        return oHero.Query('Illus')['Relic']

    
    def RandomChooseRelic(self, iNum, iExcludeCurseRelic, iChooseQuality = 0, lstExcludeRelicLevel = None):
        if iNum <= 0:
            return []
        oHero = self.m_Game.GetObject(self.m_Owner)
        lstRelic = []
        lstCurseRelic = []
        lstExcludeHasRelic = []
        if iExcludeCurseRelic:
            lstCurseRelic = self.m_Game.m_WarData.GetAllCurseRelic()
        setAllUnlock = oHero.Query('Illus')['Relic'] - set(self.GetFilterRelic())
        for iRelic in setAllUnlock:
            if iRelic in lstCurseRelic:
                continue
            if iChooseQuality and iChooseQuality != self.GetShowQuality(iRelic):
                continue
            if lstExcludeRelicLevel is not None:
                oRelic = self.GetPerform(iRelic)
                if oRelic and oRelic.m_Level in lstExcludeRelicLevel:
                    lstExcludeHasRelic.append(iRelic)
                    continue
                continue
            lstRelic.append(iRelic)
        
        iChooseRelicNum = len(lstRelic)
        if iChooseRelicNum < iNum:
            iNum -= iChooseRelicNum
            lstExcludeHasRelic = ShufferList(self.m_Game, lstExcludeHasRelic, iNum)
            lstRelic.extend(lstExcludeHasRelic)
        else:
            lstRelic = ShufferList(self.m_Game, lstRelic, iNum)
        return lstRelic

    
    def GetRelicAfterFilter(self, dRelic):
        dResult = { }
        lstFilter = self.GetFilterRelic()
        lstWarPut = self.m_Game.m_WarMgr.GetWarPutRelic()
        for iRelic, iWeight in dRelic.items():
            if iRelic in lstFilter:
                continue
            if iRelic not in lstWarPut:
                continue
            dResult[iRelic] = iWeight
        
        return dResult

    
    def SetUnFilterHasRatio(self, iNormalRatio, iCurseRatio):
        if iNormalRatio < 0:
            iNormalRatio = 0
        elif iNormalRatio > 10000:
            iNormalRatio = 10000
        self.m_UnFilterHasNormalRatio = iNormalRatio
        if iCurseRatio < 0:
            iCurseRatio = 0
        elif iCurseRatio > 10000:
            iCurseRatio = 10000
        self.m_UnFilterHasCurseRatio = iCurseRatio

    
    def CheckFilterHasNormal(self):
        if self.m_UnFilterHasNormalRatio:
            oHero = self.m_Game.GetObject(self.m_Owner)
            setAllUnlock = oHero.Query('Illus')['Relic']
            lstCurseRelic = self.m_Game.m_WarData.GetAllCurseRelic()
            iAllNormalNum = len(setAllUnlock - set(lstCurseRelic))
            iNormalNum = self.GetNumByRelicType(RELIC_TYPE_NORMAL)
            if iNormalNum >= iAllNormalNum * self.m_UnFilterHasNormalRatio / 10000:
                return 0
        return 1

    
    def CheckFilterHasCurse(self):
        if self.m_UnFilterHasCurseRatio:
            oHero = self.m_Game.GetObject(self.m_Owner)
            lstCurseRelic = self.m_Game.m_WarData.GetAllCurseRelic()
            setAllUnlock = oHero.Query('Illus')['Relic']
            iAllCurseNum = len(setAllUnlock & set(lstCurseRelic))
            iCurseNum = self.GetNumByRelicType(RELIC_TYPE_CURSE)
            if iCurseNum >= iAllCurseNum * self.m_UnFilterHasCurseRatio / 10000:
                return 0
        return 1

    
    def StartRelicRefresh(self, iKey):
        oHero = self.m_Game.GetObject(self.m_Owner)
        iRefreshNum = oHero.Query(iKey, 0)
        if iRefreshNum:
            self.GS2CRefreshRelic(iRefreshNum)

    
    def RelicRefresh(self, iKey, iMiniGame, dData):
        oHero = self.m_Game.GetObject(self.m_Owner)
        iRefreshNum = oHero.Query(iKey, 0)
        oHero.Set(iKey, 0)
        if 'lstRelic' not in dData:
            WarrelicLog.Alert('%d %d refresh relic data error' % (self.m_Game.m_ID, self.m_PlayerID))
            return None
        if not dData['lstRelic']:
            return None
        if len(dData['lstRelic']) > iRefreshNum:
            WarrelicLog.Alert('%d %d refresh relic refreshnum error %d' % (self.m_Game.m_ID, self.m_PlayerID, len(dData['lstRelic'])))
            return None
        for iRelic in dData['lstRelic']:
            oPerform = self.GetPerform(iRelic)
            if not not oPerform:
                if oPerform.m_RelicType == RELIC_TYPE_CURSE:
                    WarrelicLog.Alert('%d %d refreshr relic error !!! %d ' % (self.m_Game.m_ID, self.m_PlayerID, iRelic))
                    return None
        
        clsMiniGame = self.m_Game.m_WarData.GetMiniGameData(iMiniGame)
        if not clsMiniGame:
            WarrelicLog.Alert('%d %d no minigame %s' % (self.m_Game.m_ID, self.m_PlayerID, iMiniGame))
            return None
        dWeight = { }
        lstOldRelic = dData['lstRelic']
        for iOldRelic in lstOldRelic:
            self.RemoveRelic(iOldRelic, iKey, 1)
        
        setAllUnlock = oHero.Query('Illus')['Relic']
        lstHas = self.GetAllPerformSID()
        for iRelic, iWeight in clsMiniGame.m_ChooseWeight.items():
            if iRelic in lstHas:
                continue
            if iRelic not in setAllUnlock:
                continue
            if iRelic in lstOldRelic:
                continue
            dWeight[iRelic] = iWeight
        
        lstRelic = []
        for _ in range(len(lstOldRelic)):
            iChoose = ChooseKey(self.m_Game, dWeight)
            if not iChoose:
                WarrelicLog.Alert('%d %d no enough relic to refresh' % (self.m_Game.m_ID, self.m_PlayerID))
                break
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iChoose } }
            cl_reward.RewardItem(oHero.m_Game, oHero, [
                dReward], iKey)
            lstRelic.append(iChoose)
            dWeight.pop(iChoose)
        
        self.GS2CRefreshRelicResult(lstRelic)

    
    def RefreshAllRelicItemInfo(self):
        for oPerform in self.m_PosPerform.values():
            self.GS2CAddRelic(oPerform, oPerform.m_Pos)
        

    
    def RefreshRelicItemInfo(self, lstRelic):
        for oPerform in lstRelic:
            self.GS2CAddRelic(oPerform, oPerform.m_Pos)
        

    
    def SetAllRelicTempUnRemove(self):
        dRelic = { }
        lstRefresh = []
        for oPerform in self.m_PosPerform.values():
            iValidRemove = oPerform.ValidRemove()
            dRelic[oPerform.m_SID] = iValidRemove
            oPerform.SetArgValue('TempValidRemove', 0)
            if iValidRemove:
                lstRefresh.append(oPerform)
        
        self.RefreshRelicItemInfo(lstRefresh)
        return dRelic

    
    def SetRelicTempRemoveType(self, dRelic):
        lstRefresh = []
        for iRelic, iRemove in dRelic.items():
            oPerform = self.GetPerform(iRelic)
            if not oPerform:
                continue
            oPerform.SetArgValue('TempValidRemove', iRemove)
            lstRefresh.append(oPerform)
        
        self.RefreshRelicItemInfo(lstRefresh)

    
    def DelRelicTempRemove(self, dRelic):
        lstRefresh = []
        for iRelic in dRelic:
            oPerform = self.GetPerform(iRelic)
            if not oPerform:
                continue
            oPerform.DelArgValue('TempValidRemove')
            lstRefresh.append(oPerform)
        
        self.RefreshRelicItemInfo(lstRefresh)

    
    def SetRelicForceDisable(self, lstRelic):
        oHero = self.m_Game.GetObject(self.m_Owner)
        lstRefresh = []
        for iRelic in lstRelic:
            oPerform = self.GetPerform(iRelic)
            if not oPerform:
                continue
            oPerform.SetForceDisable(1)
            oPerform.Disable(oHero)
            lstRefresh.append(oPerform)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_FORCEDISABLE_RELIC, oHero, {
                'iPerform': iRelic })
        
        self.RefreshRelicItemInfo(lstRefresh)

    
    def UnsetAllRelicForceDisable(self):
        lstRefresh = []
        for oPerform in self.m_PosPerform.values():
            if oPerform.m_ForceDisable:
                oPerform.SetForceDisable(0)
                lstRefresh.append(oPerform)
        
        self.RefreshRelicItemInfo(lstRefresh)

    
    def GetNumByRelicType(self, iType):
        if iType in self.m_RelicType2Relic:
            return len(self.m_RelicType2Relic[iType])
        return 0

    
    def GetRelicQuality(self, iMixSID):
        iSID = self.GetRelicSIDByMixSID(iMixSID)
        if iSID == BLANKRELIC:
            return QUALITY_TYPE_LOW
        return cl_perform.GetPerformClassAttr(iSID, 'm_Quality')

    
    def GetShowQuality(self, iSID):
        if iSID in self.m_ShowQuality:
            return self.m_ShowQuality[iSID]
        return cl_perform.GetPerformClassAttr(iSID, 'm_Quality')

    
    def SetShowQuality(self, iSID, iShowQuality):
        oHero = self.m_Game.GetObject(self.m_Owner)
        iOldQuality = self.GetShowQuality(iSID)
        self.m_ShowQuality[iSID] = iShowQuality
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_RELIC_SHOWQUALITY, oHero, {
            'OldQuality': iOldQuality,
            'iPerform': iSID })

    
    def GetChooseCurseRelic(self):
        lstCurseRelic = self.m_Game.m_WarData.GetAllCurseRelic()
        oHero = self.m_Game.GetObject(self.m_Owner)
        setFilter = set(self.GetAllRelicSIDByType(RELIC_TYPE_CURSE)) if self.CheckFilterHasCurse() else set()
        setRelic = oHero.Query('Illus')['Relic'] - setFilter
        dCurse = { }
        for iSID in lstCurseRelic:
            if iSID in setRelic:
                dCurse[iSID] = 1
        
        return dCurse

    
    def AddFilterRelic(self, iRelic, sKey):
        WarrelicLog.Debug('%s %s addfilter %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, sKey))
        if iRelic in cl_platformdata.GetConsumableRelic():
            return None
        if iRelic in self.m_FilterRelic:
            self.m_FilterRelic[iRelic][sKey] = 1
        else:
            self.m_FilterRelic[iRelic] = {
                sKey: 1 }

    
    def DelFilterRelic(self, iRelic, sKey):
        WarrelicLog.Debug('%s %s delfilter %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, sKey))
        if iRelic not in self.m_FilterRelic:
            return None
        self.m_FilterRelic[iRelic].pop(sKey, None)
        if not self.m_FilterRelic[iRelic]:
            self.m_FilterRelic.pop(iRelic, None)

    
    def GetFilterRelic(self):
        lstFilterRelic = list(self.m_FilterRelic)
        if self.CheckFilterHasNormal():
            lstFilterRelic.extend(self.GetAllRelicSIDByType(RELIC_TYPE_NORMAL))
        if self.CheckFilterHasCurse():
            lstFilterRelic.extend(self.GetAllRelicSIDByType(RELIC_TYPE_CURSE))
        return lstFilterRelic

    
    def GetAllRelicNum(self):
        return len(self.m_PosPerform)

    
    def CheckHasRelic(self, iRelic):
        if iRelic in self.m_Perform or iRelic in self.m_ExtendRelic:
            return True
        if iRelic == BLANKRELIC and self.m_BlankRelic > 0:
            return True
        return False

    
    def ChooseForceDisableCurseRelic(self, oOwner, iCnt, sKey):
        
        def CBChooseFunc(lstRelic, iCnt, sKey, oHero, lstAnswer):
            cl_msgcenter.DoneEvent(oHero.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, 'ForceDisableCurseRelic')
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'ForceDisableCurseRelic')
            sRecordKey = oHero.Query('ForceDisableCurseRelicKey', '')
            if sKey == sRecordKey:
                return None
            if not lstAnswer or len(lstAnswer) > iCnt:
                return None
            if not set(lstAnswer) <= set(lstRelic):
                return None
            npcnet.DelNpcUICallBackFunction(oHero, oHero.Query('DisableCurseUIIdx', 0), NPC_CB_VALUELIST)
            self.SetRelicForceDisable(lstAnswer)

        lstRelic = []
        for oRelic in self.GetAllPerform():
            if not oRelic.m_RelicType & RELIC_TYPE_CURSE:
                continue
            if oRelic.m_ForceDisable:
                continue
            lstRelic.append(oRelic.m_SID)
        
        if not lstRelic:
            return None
        func = Functor(self.RandomDisableCurseRelic, iCnt, lstRelic, sKey)
        cl_msgcenter.AddFunction(oOwner.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, func, 'ForceDisableCurseRelic', iSub = -1, iOnce = 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, func, 'ForceDisableCurseRelic', iOnce = 0)
        npcnet.GS2CNPCEventChoose(oOwner, VIRTUAL_ITEM_RELIC, iCnt, lstRelic, EVENT_TYPE_DISABLE_CURSE_RELIC)
        iMenuIdx = npcnet.SetNpcUICallBackFunction(oOwner, NPC_CB_VALUELIST, Functor(CBChooseFunc, lstRelic, iCnt, sKey))
        oOwner.Set('DisableCurseUIIdx', iMenuIdx)

    
    def RandomDisableCurseRelic(self, iCnt, lstRelic, sKey, oTarget, dMsgInfo):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        if not oOwner:
            return None
        sRecordKey = oOwner.Query('ForceDisableCurseRelicKey', '')
        if sKey == sRecordKey:
            return None
        oOwner.Set('ForceDisableCurseRelicKey', sKey)
        lstReward = ShufferList(self.m_Game, lstRelic, iCnt)
        WarrelicLog.Debug('%s %s random disable curserelic %s %s' % (self.m_Game.m_ID, self.m_PlayerID, lstReward, lstRelic))
        self.SetRelicForceDisable(lstReward)
        cl_msgcenter.DoneEvent(oOwner.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH_BEFORE, 'ForceDisableCurseRelic')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'ForceDisableCurseRelic')

    
    def ChangeBlankRelicNum(self, iNum, sReason):
        WarrelicLog.Info('%d %d changeblankrelic %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iNum, self.m_BlankRelic, sReason))
        self.m_BlankRelic += iNum
        if self.m_BlankRelic < 0 or self.m_BlankRelic > BLANKRELIC_MAX:
            SendAlert('err', '空白秘卷数量异常 %d %d' % (self.m_PlayerID, self.m_BlankRelic))
            self.m_BlankRelic = max(0, min(self.m_BlankRelic, BLANKRELIC_MAX))
        oHero = self.m_Game.GetObject(self.m_Owner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGEBLANKRELICNUM, oHero, {
            'ChangeNum': iNum,
            'Reason': sReason })
        iAddNum = iNum if iNum > 0 else 0
        self.GS2CUpdateBlankRelicNum(iAddNum)

    
    def GS2CUpdateBlankRelicNum(self, iAddNum = 0):
        GS2CUpdateBlankRelicNum(self.m_Game, self.m_PlayerID, BLANKRELIC, self.m_BlankRelic, iAddNum)

    
    def CheckBreedRelicGroup(self, oOwner, iSID):
        if oOwner.Query('Loading'):
            return None
        lstBreed = GetBreedRelicGroup()
        if iSID not in lstBreed:
            return None
        self.m_BreedRelicCount += 1
        if self.m_BreedRelicCount >= BREED_RELIC_OBTAIN_MAX:
            for iRelic in lstBreed:
                self.AddFilterRelic(iRelic, 'BreedGroup')
            

    
    def GetTempRemoveRelic(self, iGamePlayType, iSID):
        if iGamePlayType not in self.m_TempRemoveRelic:
            return None
        dRelic = self.m_TempRemoveRelic[iGamePlayType]
        if iSID not in dRelic:
            return None
        return dRelic[iSID]

    
    def IsOpenTempRelicPlayType(self, iGamePlayType):
        return iGamePlayType in self.m_TempRemoveRelic

    
    def CheckCanAddNormalRelic2TempRelic(self, iGamePlayType, iRelic):
        if not self.IsOpenTempRelicPlayType(iGamePlayType):
            return TEMPRELIC_CHECKSTATE_UNOPENTYPE
        oPerform = self.GetPerform(iRelic)
        if not oPerform:
            return TEMPRELIC_CHECKSTATE_NOEXISTRELIC
        if not oPerform.ValidRemove():
            return TEMPRELIC_CHECKSTATE_NOALLOWREMOVE
        if iRelic in self.m_TempRemoveRelic[iGamePlayType]:
            return TEMPRELIC_CHECKSTATE_HASRELIC
        return TEMPRELIC_CHECKSTATE_CANADD

    
    def CheckCanAddExtendRelic2TempRelic(self, iGamePlayType, iRelic):
        if not self.IsOpenTempRelicPlayType(iGamePlayType):
            return TEMPRELIC_CHECKSTATE_UNOPENTYPE
        oPerform = self.GetExtendRelic(iRelic)
        if not oPerform:
            return TEMPRELIC_CHECKSTATE_NOEXISTRELIC
        if iRelic in self.m_TempRemoveRelic[iGamePlayType]:
            return TEMPRELIC_CHECKSTATE_HASRELIC
        return TEMPRELIC_CHECKSTATE_CANADD

    
    def OpenTempRelicPlayType(self, iGamePlayType):
        if iGamePlayType not in ALL_TEMPREMOVERELIC_TYPE:
            return None
        if iGamePlayType not in self.m_TempRemoveRelic:
            WarrelicLog.Debug('%d %d open tempremoverelic %d' % (self.m_Game.m_ID, self.m_PlayerID, iGamePlayType))
            self.m_TempRemoveRelic[iGamePlayType] = { }

    
    def ClearTempRelicPlayType(self, iGamePlayType, iSendClient = 1):
        if not self.IsOpenTempRelicPlayType(iGamePlayType):
            return None
        WarrelicLog.Debug('%d %d clear tempremoverelic %d' % (self.m_Game.m_ID, self.m_PlayerID, iGamePlayType))
        for iRelic in list(self.m_TempRemoveRelic[iGamePlayType]):
            self.ReturnTempRemoveRelicToNormal(iRelic, 'ClearTempRelicPlayType', iGamePlayType, iSendClient)
        
        self.m_TempRemoveRelic.pop(iGamePlayType)

    
    def HandleTempRemoveRelic(self, iGamePlayType, lstRelic):
        WarrelicLog.Debug('%d %d HandleTempRemoveRelic %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iGamePlayType, lstRelic))
        sReason = 'SetTempRemoveRelic-%s' % iGamePlayType
        if iGamePlayType not in ALL_TEMPREMOVERELIC_TYPE:
            return None
        oHero = self.m_Game.GetObject(self.m_Owner)
        dMsgInfo = {
            'GamePlayType': iGamePlayType,
            'HandleRelic': lstRelic }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HANDLE_TEMPRELIC, oHero, dMsgInfo, iSub = iGamePlayType)
        if 'NoCanHandle' in dMsgInfo:
            return None
        iSendClient = 0
        for iRelic, iHandleType in lstRelic:
            if iHandleType == RELIC_TO_NORMAL:
                self.ReturnTempRemoveRelicToNormal(iRelic, sReason, iGamePlayType, iSendClient)
                continue
            if iHandleType == RELIC_TO_TEMPRELIC:
                self.AddNormalRelicToTempRemoveRelic(iRelic, sReason, iGamePlayType, iSendClient)
                continue
            if iHandleType == EXTENDRELIC_TO_TEMPRELIC:
                self.AddExtendRelicToTempRemoveRelic(iRelic, sReason, iGamePlayType, iSendClient)
        
        self.GS2CSynTempRemoveRelic(iGamePlayType)

    
    def AddTempRemoveRelic(self, iGamePlayType, iSID, sReason, iLevel = 1, dExtInfo = None, iSource = 0, iSendClient = 0):
        iPFType = cl_perform.GetPerformClassAttr(iSID, 'm_PFType')
        if iPFType != PF_TYPE_RELIC:
            WarrelicLog.Alert('%d %d add tempremoverelic err %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iPFType, iGamePlayType, sReason))
            return None
        if iGamePlayType not in self.m_TempRemoveRelic:
            return None
        WarrelicLog.Info('%d %d add tempremoverelic %d %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iGamePlayType, sReason, iSendClient))
        dRelic = self.m_TempRemoveRelic[iGamePlayType]
        oOwner = self.m_Game.GetObject(self.m_Owner)
        oPerform = oOwner.m_Game.m_ResMgr.NewPerform(iSID, oOwner, iLevel)
        oPerform.InitSource(iSource)
        dOwnerInfo = {
            self.m_PlayerID: 1 }
        if dExtInfo and 'OwnerInfo' in dExtInfo:
            dOwnerInfo.update(dExtInfo['OwnerInfo'])
        oPerform.m_OwnerInfo = dOwnerInfo
        iRollNum = dExtInfo['RollNum'] if dExtInfo and 'RollNum' in dExtInfo else 0
        oPerform.SetRollNum(iRollNum)
        dRelic[iSID] = oPerform
        if iSendClient:
            self.GS2CSynTempRemoveRelic(iGamePlayType)
        return oPerform

    
    def RemoveTempRemoveRelic(self, iGamePlayType, iSID, sReason, iSendClient = 0):
        if iGamePlayType not in self.m_TempRemoveRelic:
            return False
        dRelic = self.m_TempRemoveRelic[iGamePlayType]
        if iSID not in dRelic:
            return False
        WarrelicLog.Info('%d %d remove tempremoverelic %d %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iGamePlayType, sReason, iSendClient))
        oPerform = dRelic.pop(iSID)
        oPerform.Release()
        if iSendClient:
            self.GS2CSynTempRemoveRelic(iGamePlayType)
        return True

    
    def ReturnTempRemoveRelicToNormal(self, iRelic, sReason, iGamePlayType, iSendClient):
        oTempPerform = self.GetTempRemoveRelic(iGamePlayType, iRelic)
        if not oTempPerform:
            WarrelicLog.Alert('%d %d temprelic2normal %s no perform %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))
            return None
        iLevel = oTempPerform.m_Level
        iSource = oTempPerform.m_Source
        dExtInfo = {
            'RollNum': oTempPerform.m_RollNum,
            'OwnerInfo': oTempPerform.m_OwnerInfo }
        oNewPerform = self.GetPerform(iRelic)
        iOperateType = REMOVE_RELIC_TO_TEMPREMOVERELIC_TYPE[iGamePlayType]
        if oNewPerform and oNewPerform.m_Level >= iLevel:
            WarrelicLog.Debug('%d %d temprelic2normal drop %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))
            self.RemoveRelicByDrop(iRelic, iOperateType, iAlert = 1)
        elif self.RemoveTempRemoveRelic(iGamePlayType, iRelic, sReason, iSendClient):
            WarrelicLog.Debug('%d %d temprelic2normal add %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))
            self.AddRelic(iRelic, sReason, iLevel, dExtInfo, iSource)
        else:
            WarrelicLog.Alert('%d %d temprelic2normal err %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))

    
    def AddNormalRelicToTempRemoveRelic(self, iRelic, sReason, iGamePlayType, iSendClient):
        oPerform = self.GetPerform(iRelic)
        if not oPerform:
            WarrelicLog.Alert('%d %d normal2temprelic %s no perform %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))
            return None
        iLevel = oPerform.m_Level
        iSource = oPerform.m_Source
        dExtInfo = {
            'RollNum': oPerform.m_RollNum,
            'OwnerInfo': oPerform.m_OwnerInfo }
        iCheckState = self.CheckCanAddNormalRelic2TempRelic(iGamePlayType, iRelic)
        if iCheckState == TEMPRELIC_CHECKSTATE_CANADD and self.RemoveRelic(iRelic, sReason, iForce = 0) and self.AddTempRemoveRelic(iGamePlayType, iRelic, sReason, iLevel, dExtInfo, iSource, iSendClient):
            WarrelicLog.Debug('%d %d normal2temprelic add %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))
            return None
        WarrelicLog.Alert('%d %d normal2temprelic %s err %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason, self.m_TempRemoveRelic, iCheckState))

    
    def AddExtendRelicToTempRemoveRelic(self, iRelic, sReason, iGamePlayType, iSendClient):
        oPerform = self.GetExtendRelic(iRelic)
        if not oPerform:
            WarrelicLog.Alert('%d %d extend2temprelic %s no perform %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))
            return None
        iLevel = oPerform.m_Level
        iSource = oPerform.m_Source
        dExtInfo = {
            'RollNum': oPerform.m_RollNum,
            'OwnerInfo': oPerform.m_OwnerInfo }
        iCheckState = self.CheckCanAddExtendRelic2TempRelic(iGamePlayType, iRelic)
        if iCheckState == TEMPRELIC_CHECKSTATE_CANADD and self.RemoveExtendRelic(iRelic, sReason) and self.AddTempRemoveRelic(iGamePlayType, iRelic, sReason, iLevel, dExtInfo, iSource, iSendClient):
            WarrelicLog.Debug('%d %d extend2temprelic add %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason))
            return None
        WarrelicLog.Alert('%d %d extend2temprelic %s err %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iRelic, iGamePlayType, sReason, self.m_TempRemoveRelic, iCheckState))


