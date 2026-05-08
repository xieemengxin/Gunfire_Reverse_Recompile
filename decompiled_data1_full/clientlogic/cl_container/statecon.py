# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/statecon.pyc
# RelativePath: clientlogic/cl_container/statecon.pyc
# Source Generated with Decompyle++
# File: statecon.pyc (Python 3.6)

from cl_commondefines import STATE_ABNORMAL_FIRE, BAG_TYPE_STATE, STATE_ADD_REFRESHORSYNC, STATE_ADD_LONGORSYNC, STATE_ADD_SAMESOURCE, STATE_ADD_REFRESH, STATE_ADD_HIGH, STATE_ADD_OVERTIME, STATE_TIME_LIMIT, STATE_ADD_LONG, STATE_ADD_REPLACE, STATE_TIME_FOREVER, WARRIOR_HERO, STATE_ADD_REFRESHORSYNC_SAMEITEM, ALL_STATE_ADD_SYNC, STATE_ADD_REPLACE_SAMEATTACK
from cl_only import GAME_FRAME, WeakProxy, SendAlert
import cl_container
import cl_msgcenter
import cl_duonet.dn_cl_state_net as statenet
import cl_perform
import cl_state
MAX_COUNT = 65535
STATE_REFRESH_FRAME_MAX = 20 * GAME_FRAME

def GS2CStateAdd(oWarrior, iIsPlayer, oState, dPlayer = None):
    if not dPlayer:
        if iIsPlayer:
            if oState.m_GameBroadcast:
                dPlayer = oWarrior.m_Game.GetRealPlayers()
            else:
                dPlayer = {
                    oWarrior.m_PlayerID: 1 }
        elif oState.m_OnlyLocalShow:
            oPlayer = oWarrior.m_Game.GetObject(oState.m_Attacker)
            if not oPlayer:
                return None
            dPlayer = {
                oPlayer.m_OwnerPlayerID: 1 }
        else:
            oScene = oWarrior.m_Game.m_SceneMgr.GetScene(oWarrior.m_Scene)
            dPlayer = dict(oScene.GetPlayers()) if oScene else { }
            if not dPlayer:
                return None
    (iWarrior, iStateID, iStateSID, iAttacker, iTime, iRemainTime, iCreateTime, iMaxCount, iCount) = oState.GetStateAddInfo()
    if iCount > MAX_COUNT:
        iCount = MAX_COUNT
        SendAlert('err', '%d 状态%s 的计数超过压包最大值,请配置最大计数' % (oWarrior.m_PlayerID, oState.m_Key))
    statenet.DN_GS2CStateAdd(iWarrior, iStateID, iStateSID, iAttacker, iTime, iRemainTime, iMaxCount, iCount, dPlayer)


def GS2CStateDel(oWarrior, iIsPlayer, oState):
    if iIsPlayer:
        if oState.m_GameBroadcast:
            dPlayer = oWarrior.m_Game.GetRealPlayers()
        else:
            dPlayer = {
                oWarrior.m_PlayerID: 1 }
    elif oState.m_OnlyLocalShow:
        oPlayer = oWarrior.m_Game.GetObject(oState.m_Attacker)
        if not oPlayer:
            return None
        dPlayer = {
            oPlayer.m_OwnerPlayerID: 1 }
    else:
        oScene = oWarrior.m_Game.m_SceneMgr.GetScene(oWarrior.m_Scene)
        dPlayer = dict(oScene.GetPlayers()) if oScene else { }
        if not dPlayer:
            return None
    statenet.DN_GS2CStateDel(oWarrior.m_ID, oState.m_ID, dPlayer)


def GS2CStateRefresh(oWarrior, iIsPlayer, oState):
    if iIsPlayer:
        if oState.m_GameBroadcast:
            dPlayer = oWarrior.m_Game.GetRealPlayers()
        else:
            dPlayer = {
                oWarrior.m_PlayerID: 1 }
    elif oState.m_OnlyLocalShow:
        oPlayer = oWarrior.m_Game.GetObject(oState.m_Attacker)
        if not oPlayer:
            return None
        dPlayer = {
            oPlayer.m_OwnerPlayerID: 1 }
    else:
        oScene = oWarrior.m_Game.m_SceneMgr.GetScene(oWarrior.m_Scene)
        dPlayer = dict(oScene.GetPlayers()) if oScene else { }
        if not dPlayer:
            return None
    (iWarrior, iStateID, iStateSID, iTime, iRemainTime, iMaxCount, iCount) = oState.GetStateRefreshInfo()
    if iCount > MAX_COUNT:
        iCount = MAX_COUNT
        SendAlert('err', '%d 状态%s 的计数超过压包最大值,请配置最大计数' % (oWarrior.m_PlayerID, oState.m_Key))
    statenet.DN_GS2CStateRefresh(iStateID, iTime, iRemainTime, iMaxCount, iCount, dPlayer)


def GS2CStateRefreshCnt(oWarrior, iIsPlayer, oState, iCnt):
    if iCnt > MAX_COUNT:
        iCnt = MAX_COUNT
        SendAlert('err', '%d 状态%s 的计数超过压包最大值,请配置最大计数' % (oWarrior.m_PlayerID, oState.m_Key))
    if iIsPlayer:
        if oState.m_GameBroadcast:
            dPlayer = oWarrior.m_Game.GetRealPlayers()
        else:
            dPlayer = {
                oWarrior.m_PlayerID: 1 }
    elif oState.m_OnlyLocalShow:
        oPlayer = oWarrior.m_Game.GetObject(oState.m_Attacker)
        if not oPlayer:
            return None
        dPlayer = {
            oPlayer.m_OwnerPlayerID: 1 }
    else:
        oScene = oWarrior.m_Game.m_SceneMgr.GetScene(oWarrior.m_Scene)
        dPlayer = dict(oScene.GetPlayers()) if oScene else { }
        if not dPlayer:
            return None
    iPerCountTime = oState.m_PerCountTime if oState.IsOpenCount() else 0
    statenet.DN_GS2CStateRefreshCnt(oState.m_ID, iCnt, iPerCountTime, dPlayer)


def GS2CStateRefreshExtraInfo(oWarrior, oState, dExtInfo, dPlayer):
    if 'arg' in oState.m_StateInfo and 'ForceSrcPF' in oState.m_StateInfo['arg']:
        iPerform = oState.m_StateInfo['arg']['ForceSrcPF']
    elif 'pfid' in oState.m_StateInfo:
        pass
    
    iPerform = 0
    iType = 0
    if iPerform:
        clsPerform = cl_perform.GetPerformModule(iPerform)
        if clsPerform:
            iType = clsPerform.m_PFType
    statenet.DN_GS2CStateRefreshExtraInfo(iType, oWarrior.m_ID, oState.m_ID, iPerform, dExtInfo, dPlayer)


class CStateContainer(cl_container.CListContainer):
    m_BagType = BAG_TYPE_STATE
    m_CheckItemUpdate = False
    m_GameBroadcast = 0
    m_SyncIntervalFrame = 5
    
    def __init__(self, oWarrior):
        super(CStateContainer, self).__init__(oWarrior.m_Owner)
        self.m_Game = oWarrior.m_Game
        self.m_WarriorObj = WeakProxy(oWarrior)
        self.m_StateBySid = { }
        self.m_ReleaseFlag = 0
        self.m_LastSyncFrame = { }
        if oWarrior.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            self.m_GameBroadcast = 1
        iDebugFrame = self.m_Game.m_WarMgr.Query('DebugStateSync')
        if iDebugFrame:
            self.m_SyncIntervalFrame = iDebugFrame

    
    def Release(self):
        self.m_ReleaseFlag = 1
        if not self.m_WarriorObj:
            return None
        if self.m_WarriorObj.m_Delete:
            iRefresh = 0
        else:
            iRefresh = 1
        for oState in list(self.m_Item.values()):
            oState.Disable(self.m_WarriorObj, iRefresh, self.m_ReleaseFlag)
            oState.Release()
        
        self.m_WarriorObj = None
        self.m_Game = None
        self.m_Item = None
        self.m_StateBySid = { }
        self.m_LastSyncFrame = None

    
    def DisableAllState(self, iRefresh):
        dResult = { }
        oOwner = self.m_WarriorObj
        self.m_ReleaseFlag = 1
        for oState in list(self.m_Item.values()):
            if not oState.m_Enable:
                continue
            dResult[oState.m_SID] = 1
            oState.Disable(oOwner, iRefresh)
        
        self.m_ReleaseFlag = 0
        return dResult

    
    def EnableStates(self, dState):
        oOwner = self.m_WarriorObj
        for iStateSID in dState:
            lstState = self.GetItems(iStateSID)
            for oState in lstState:
                if oState.m_Enable:
                    continue
                oState.Enable(oOwner)
            
        

    
    def GetOwner(self):
        return self.m_WarriorObj

    
    def Save(self):
        dData = { }
        for oState in self.m_Item.values():
            if oState.m_SaveToRecord and oState.m_TimeType == STATE_TIME_FOREVER:
                dData[oState.m_SID] = {
                    'Cnt': oState.GetCount(),
                    'Stat': oState.GetStateStatistics() }
        
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        oOwner = self.GetOwner()
        for iSID, dState in dData.items():
            oState = self.GetItemBySID(iSID)
            if not oState:
                oState = cl_state.NewState(iSID, self.m_Game)
                if not oState:
                    continue
                oState.m_Owner = oOwner.m_ID
                oState.m_TimeType = STATE_TIME_FOREVER
                oState.m_Time = 0
                oState.m_AllTime = 0
                self.AddItem(oState)
                oState.Enable(oOwner)
            oState.m_CurCount = 0
            oState.AddCount(oOwner, dState['Cnt'])
            if 'Stat' in dState:
                oState.SetStateStatistics(dState['Stat'])
        

    
    def GetItemBySID(self, iSid):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return None
        return self.m_StateBySid[iSid][0]

    
    def GetEnableItemBySID(self, iSid):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return None
        for oState in self.m_StateBySid[iSid]:
            if oState.m_Enable:
                return oState
        

    
    def GetItemBySIDWithIndex(self, iSid, iIndex):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return None
        if iIndex >= len(self.m_StateBySid[iSid]):
            return None
        return self.m_StateBySid[iSid][iIndex]

    
    def GetItems(self, iSid):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return []
        return self.m_StateBySid[iSid]

    
    def GetItemBySource(self, iSid, iFromTarget):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return None
        for oState in self.m_StateBySid[iSid]:
            if oState.m_Attacker == iFromTarget:
                return oState
        

    
    def GetStateBySource(self, iSid, iAttack, iItem):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return None
        lstState = self.GetItems(iSid)
        for oState in lstState:
            if iAttack and oState.m_Attacker != iAttack:
                continue
            if iItem and oState.m_Item != iItem:
                continue
            return oState
        

    
    def GetStateLayer(self, iSid):
        if iSid not in self.m_StateBySid:
            return 0
        return len(self.m_StateBySid[iSid])

    
    def HasState(self, iSid):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return False
        for oState in self.m_StateBySid[iSid]:
            if oState.m_ID in self.m_Item:
                return True
        
        return False

    
    def HasStateInList(self, lstState):
        for iSID in lstState:
            if self.HasState(iSID):
                return True
        
        return False

    
    def CheckHasStateFrom(self, iSid, iAttack, iItem):
        lstState = self.GetItems(iSid)
        for oState in lstState:
            if iAttack and oState.m_Attacker != iAttack:
                continue
            if iItem and oState.m_Item != iItem:
                continue
            return True
        
        return False

    
    def GetStateNum(self, iSid):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return 0
        iNum = 0
        for oState in self.m_StateBySid[iSid]:
            if oState.m_ID in self.m_Item:
                iNum += 1
        
        return iNum

    
    def GetGetStateNumInList(self, lstState):
        iNum = 0
        for iSID in lstState:
            iNum += self.GetStateNum(iSID)
        
        return iNum

    
    def GetStateCountByAttacker(self, iStateSID, iAttacker):
        if iStateSID not in self.m_StateBySid or not self.m_StateBySid[iStateSID]:
            return 0
        for oState in self.m_StateBySid[iStateSID]:
            if oState.m_ID not in self.m_Item:
                continue
            if oState.m_Attacker == iAttacker:
                return oState.GetCount()
        
        return 0

    
    def GetAllStateSID(self):
        return list(self.m_StateBySid)

    
    def OnAddItem(self, oState):
        oState.m_StartTime = self.m_Game.GetFrameNum()
        iStateSID = oState.m_SID
        if iStateSID not in self.m_StateBySid:
            self.m_StateBySid[iStateSID] = []
        lstState = self.m_StateBySid[iStateSID]
        iAddType = oState.m_AddType
        if iAddType == STATE_ADD_REPLACE:
            for oOwnState in lstState:
                self.RemoveItem(oOwnState.m_ID)
            
            lstState.append(oState)
        elif iAddType == STATE_ADD_LONG:
            if lstState:
                oOldState = lstState[0]
                if oOldState.m_TimeType == STATE_TIME_LIMIT:
                    if oState.m_TimeType == STATE_TIME_FOREVER or oOldState.GetRemainTime() < oState.GetRemainTime():
                        self.RemoveItem(oOldState.m_ID)
                    else:
                        self.DelItem(oState.m_ID)
                        return None
            lstState.append(oState)
        elif iAddType == STATE_ADD_HIGH:
            if lstState:
                for oOldState in lstState:
                    if oOldState and oOldState.m_Enable or oState.CheckHighAttr(self.m_WarriorObj, oOldState):
                        oOldState.Disable(self.m_WarriorObj, 0)
                        self.GS2CItemDel(oOldState)
                    else:
                        oState.m_WaitEnable = 1
                
            lstState.append(oState)
        elif iAddType in (STATE_ADD_OVERTIME, STATE_ADD_REFRESH):
            lstState.append(oState)
        elif iAddType == STATE_ADD_SAMESOURCE:
            if lstState:
                for oOldState in lstState:
                    iOldItem = oOldState.m_Item
                    iNewItem = oState.m_Item
                    if iOldItem and iOldItem == iNewItem:
                        self.RemoveItem(oOldState.m_ID)
                        break
                
            lstState.append(oState)
        elif iAddType == STATE_ADD_LONGORSYNC:
            if lstState:
                for oOldState in lstState:
                    if oOldState and oState.m_Attacker == oOldState.m_Attacker:
                        iOldItem = oOldState.m_Item
                        iNewItem = oState.m_Item
                        if iOldItem and iOldItem == iNewItem or oOldState.m_TimeType == STATE_TIME_LIMIT:
                            if oState.m_TimeType == STATE_TIME_FOREVER or oOldState.GetRemainTime() < oState.GetRemainTime():
                                iAddFrame = oState.GetTime() - oOldState.GetRemainTime()
                                oOldState.m_StateInfo.update(oState.m_StateInfo)
                                oOldState.AddTime(self.m_WarriorObj, iAddFrame, STATE_REFRESH_FRAME_MAX)
                        self.DelItem(oState.m_ID)
                        return None
                
            lstState.append(oState)
        elif iAddType == STATE_ADD_REFRESHORSYNC:
            if lstState:
                for oOldState in lstState:
                    if oOldState and oState.m_Attacker == oOldState.m_Attacker or oOldState.m_TimeType != STATE_TIME_FOREVER:
                        iAddFrame = oState.GetTime() - oOldState.GetRemainTime()
                        oOldState.AddTime(self.m_WarriorObj, iAddFrame, STATE_REFRESH_FRAME_MAX)
                    if oOldState.m_LifeCycle:
                        oOldState.m_StateInfo.update(oState.m_StateInfo)
                        oOldState.m_LifeCycle.CallFunc('Refresh', self.m_WarriorObj)
                    self.DelItem(oState.m_ID)
                    return None
                
            lstState.append(oState)
        elif iAddType == STATE_ADD_REFRESHORSYNC_SAMEITEM:
            if lstState:
                iNewItem = oState.m_Item
                for oOldState in lstState:
                    if oOldState and oOldState.m_Item == iNewItem or oOldState.m_TimeType != STATE_TIME_FOREVER:
                        iAddFrame = oState.GetTime() - oOldState.GetRemainTime()
                        oOldState.AddTime(self.m_WarriorObj, iAddFrame, STATE_REFRESH_FRAME_MAX)
                    if oOldState.m_LifeCycle:
                        oOldState.m_StateInfo.update(oState.m_StateInfo)
                        oOldState.m_LifeCycle.CallFunc('Refresh', self.m_WarriorObj)
                    self.DelItem(oState.m_ID)
                    return None
                
            lstState.append(oState)
        elif iAddType == STATE_ADD_REPLACE_SAMEATTACK:
            if lstState:
                iNewAttacker = oState.m_Attacker
                for oOldState in lstState:
                    iAttacker = oOldState.m_Attacker
                    if iAttacker and iAttacker == iNewAttacker:
                        self.RemoveItem(oOldState.m_ID)
                        break
                
            lstState.append(oState)
        else:
            lstState.append(oState)
        if not (oState.m_IsFollowState) and self.m_WarriorObj:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDSTATE, self.m_WarriorObj, {
                'VID': self.m_WarriorObj.m_ID,
                'StateID': oState.m_ID,
                'StateSID': oState.m_SID })
        return oState

    
    def OnRemoveItem(self, oState):
        iStateSID = oState.m_SID
        if iStateSID in self.m_StateBySid and oState in self.m_StateBySid[iStateSID]:
            self.m_StateBySid[iStateSID].remove(oState)
        if not oState.m_Enable:
            oState.Release()
            return None
        oState.Disable(self.m_WarriorObj, 1)
        oNewState = self.GetItemBySID(iStateSID)
        if oNewState and oNewState.m_AddType == STATE_ADD_HIGH:
            oNewState = None
            lstState = self.m_StateBySid[iStateSID][:]
            for oTmpState in lstState:
                if not oTmpState:
                    continue
                if oTmpState.m_TimeType == STATE_TIME_LIMIT and oTmpState.GetRemainTime() <= 0:
                    oTmpState.Disable(self.m_WarriorObj, 0)
                    self.RemoveItem(oTmpState.m_ID)
                    continue
                if not oNewState:
                    oNewState = oTmpState
                    continue
                if oTmpState.CheckHighAttr(self.m_WarriorObj, oNewState):
                    oNewState = oTmpState
            
            if oNewState:
                oNewState.m_WaitEnable = 0
                if oNewState.m_TimeType == STATE_TIME_LIMIT:
                    oNewState.m_Time = oNewState.GetRemainTime()
                oNewState.m_StartTime = self.m_Game.GetFrameNum()
                oNewState.SetDelayFirstFrame(oState.CalNextDelay())
                oNewState.Enable(self.m_WarriorObj)
                self.GS2CItemAdd(oNewState)
        oState.Release()

    
    def RemoveAllItemBySID(self, iSid):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return None
        lstState = self.m_StateBySid[iSid][:]
        for oState in lstState:
            self.RemoveItem(oState.m_ID)
        
        self.m_StateBySid[iSid] = []

    
    def RemoveItemBySource(self, iSid, iFromTarget):
        if iSid not in self.m_StateBySid or not self.m_StateBySid[iSid]:
            return None
        lstState = self.m_StateBySid[iSid][:]
        for oState in lstState:
            if oState.m_Attacker == iFromTarget:
                self.RemoveItem(oState.m_ID)
        

    
    def Refresh(self, dPlayer = None):
        for oState in self.m_Item.values():
            self.GS2CItemAdd(oState, dPlayer, iRefresh = 1)
            if oState.IsOpenCount():
                self.GS2CRefreshCnt(oState)
        

    
    def Replace(self, oTarget, oOldState, oNewState, bRemove = True):
        if bRemove:
            self.RemoveItem(oOldState.m_ID)
        else:
            oOldState.Disable(self.m_WarriorObj, 0)
            self.GS2CItemDel(oOldState)
        oNewState.Enable(oTarget)
        self.GS2CItemAdd(oNewState)

    
    def RefreshAllShowTime(self):
        for oState in self.m_Item.values():
            if oState.m_IsShow:
                GS2CStateRefresh(self.m_WarriorObj, self.m_GameBroadcast, oState)
        

    
    def IsFinalState(self, oState):
        if not oState:
            return True
        bFinal = True
        if oState.m_AddType == STATE_ADD_HIGH:
            iSID = oState.m_SID
            lstState = self.GetItems(iSID)
            iCurFrame = self.m_Game.GetFrameNum()
            iNowStateEndTime = iCurFrame + oState.GetRemainTime()
            for oItem in lstState:
                if not oItem or oItem.m_ID == oState.m_ID:
                    continue
                iItemEndTime = iCurFrame + oItem.GetRemainTime()
                if iItemEndTime < iNowStateEndTime:
                    continue
                bFinal = False
            
        return bFinal

    
    def GS2CItemAdd(self, oState, dPlayer = None, iRefresh = 0):
        oWarriorObj = self.m_WarriorObj
        if not oWarriorObj or not (oWarriorObj.m_Scene):
            return None
        if not oState.m_Game:
            return None
        if not oState.m_IsShow:
            return None
        if oState.m_WaitEnable:
            return None
        if not iRefresh:
            iState = oState.m_ID
            if self.m_Game.CacheStateAddDel(oWarriorObj.m_ID, oState.m_SID, iState, iAdd = 1):
                return None
            if oState.m_AddType in ALL_STATE_ADD_SYNC:
                iLastFrame = self.m_LastSyncFrame[iState] if iState in self.m_LastSyncFrame else 0
                iCurFrame = self.m_Game.GetFrameNum()
                if iLastFrame and iLastFrame + self.m_SyncIntervalFrame >= iCurFrame:
                    return None
                self.m_LastSyncFrame[iState] = iCurFrame
        GS2CStateAdd(oWarriorObj, self.m_GameBroadcast, oState, dPlayer)
        if oState.m_SendExtraInfo:
            dExtraInfo = oState.GetArgValue('StateExtraInfo', { })
            if not oWarriorObj.m_PlayerID:
                oScene = oState.m_Game.m_SceneMgr.GetScene(oWarriorObj.m_Scene)
                if not oScene:
                    return None
                dPlayer = oScene.GetPlayers()
            else:
                dPlayer = {
                    oWarriorObj.m_PlayerID: 1 }
            GS2CStateRefreshExtraInfo(oWarriorObj, oState, dExtraInfo, dPlayer)

    
    def GS2CItemDel(self, oState, iRefresh = 0):
        if not oState.m_IsShow:
            return None
        if oState.m_TimeType == STATE_TIME_LIMIT and not oState.GetRemainTime():
            if iRefresh:
                GS2CStateDel(self.m_WarriorObj, self.m_GameBroadcast, oState)
            return None
        if not (self.m_WarriorObj.m_OwnerPlayerID) and self.m_WarriorObj.IsDead():
            return None
        if self.m_Game.CacheStateAddDel(self.m_WarriorObj.m_ID, oState.m_SID, oState.m_ID, iAdd = 0):
            return None
        GS2CStateDel(self.m_WarriorObj, self.m_GameBroadcast, oState)

    
    def GS2CRefreshCnt(self, oState):
        if not (oState.m_IsShow) or not (oState.m_ShowStateCnt):
            return None
        iCnt = oState.GetCount()
        if self.m_Game.CacheStateCnt(self.m_WarriorObj.m_ID, oState.m_SID, oState.m_ID, iCnt):
            return None
        GS2CStateRefreshCnt(self.m_WarriorObj, self.m_GameBroadcast, oState, iCnt)

    
    def GS2CRefreshState(self, oWarrior, oState, iRefresh = 0):
        if not oState.m_IsShow:
            return None
        if iRefresh:
            self.m_Game.CacheStateTime(oWarrior.m_ID, oState.m_ID)
            return None
        iState = oState.m_ID
        iLastFrame = self.m_LastSyncFrame[iState] if iState in self.m_LastSyncFrame else 0
        iCurFrame = self.m_Game.GetFrameNum()
        if iLastFrame and iLastFrame + self.m_SyncIntervalFrame >= iCurFrame:
            return None
        self.m_LastSyncFrame[iState] = iCurFrame
        GS2CStateRefresh(self.m_WarriorObj, self.m_GameBroadcast, oState)


