# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/performcon.pyc
# RelativePath: clientlogic/cl_container/performcon.pyc
# Source Generated with Decompyle++
# File: performcon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_COLDTIME
from cl_only import GAME_FRAME_TIME, WeakProxy, Functor
from cl_commondefines import PERFORM_POS_EXT, PERFORM_POS_MAIN, PERFORM_POS_MINOR, ITEMPERFORM_ENABLE_HOLD, ITEMPERFORM_ENABLE_UNHOLD, ITEMPERFORM_ENABLE_MAINHOLD, PF_TYPE_SUBCLASSIFY, PF_TYPE_SUITACTIVE
from cl_item.defines import MAIN_HOLD
from cl_object.logging import SkillLog, OtherLog
import weakref
import cl_netattr
import cl_msgcenter
import cl_duonet.dn_cl_perform_net

def GS2CPerformColdTimeAdd(oGame, pid, iWarrior, iPerform, iRemainTime, iCacheRemainTime, iCacheSumTime, iActNum):
    netData = {
        'iWarrior': iWarrior,
        'iPerform': iPerform,
        'iRemainTime': iRemainTime,
        'iCacheRemainTime': iCacheRemainTime,
        'iCacheSumTime': iCacheSumTime,
        'ActNum': iActNum,
        'pid': pid,
        'oGame': oGame }
    cl_duonet.dn_cl_perform_net.DN_GS2CPerformColdTimeAdd(netData)


def GS2CPerformColdTimeDel(oGame, pid, iWarrior, iPerform):
    netData = {
        'iWarrior': iWarrior,
        'iPerform': iPerform,
        'pid': pid,
        'oGame': oGame }
    cl_duonet.dn_cl_perform_net.DN_GS2CPerformColdTimeDel(netData)


def GS2CPerformColdTimeNoAdd(oGame, pid, iWarrior, iPerform, iActNum):
    netData = {
        'iWarrior': iWarrior,
        'iPerform': iPerform,
        'pid': pid,
        'ActNum': iActNum,
        'oGame': oGame }
    cl_duonet.dn_cl_perform_net.DN_GS2CPerformColdTimeNoAdd(netData)


def GS2CWeaponPerformColdTimeAdd(oGame, pid, iWeapon, iPerform, iRemainTime, iSumTime):
    pass


def GS2CWeaponPerformColdTimeDel(oGame, pid, iWeapon, iPerform):
    pass


def GS2CPerformAdd(oGame, iWarrior, oPerform, iType, iPos, dPlayer = None):
    if dPlayer is None:
        dPlayer = oGame.GetRealPlayers()
        if not dPlayer:
            return None
    dInfo = cl_netattr.MakePerformAddPacket(oPerform)
    netData = {
        'iPerformID': oPerform.m_ID,
        'iOwnerID': iWarrior,
        'iItemID': oPerform.m_Item,
        'iPerformType': iType,
        'iPos': iPos,
        'iAttIdx': oPerform.m_AttPerformIdx,
        'dInfo': dInfo,
        'oGame': oGame,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_perform_net.DN_GS2CPerformAdd(netData)


def GS2CPerformAddUseInterval(oGame, pid, iWarrior, iPerform, iRemainTime):
    netData = {
        'iWarrior': iWarrior,
        'iPerform': iPerform,
        'iRemainTime': iRemainTime,
        'pid': pid,
        'oGame': oGame }
    cl_duonet.dn_cl_perform_net.DN_GS2CPerformAddUseInterval(netData)


def GS2CPerformRemove(oGame, iWarrior, oPerform, dPlayer):
    netData = {
        'iOwnerID': iWarrior,
        'iPerformID': oPerform.m_ID,
        'iPerformType': oPerform.m_PFType,
        'oGame': oGame,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_perform_net.DN_GS2CPerformRemove(netData)


class CPerformContainer(object):
    m_BagType = BAG_TYPE_COLDTIME
    
    def __init__(self, oWarrior):
        self.m_Owner = oWarrior.m_ID
        self.m_PlayerID = oWarrior.m_PlayerID
        self.m_Game = oWarrior.m_Game
        self.m_Perform = { }
        self.InitColdTimeData()

    
    def InitColdTimeData(self):
        self.m_ColdTime = { }
        self.m_SumColdTime = { }
        self.m_CacheColdTime = { }
        self.m_CacheSumColdTime = { }
        self.m_LastAttrValue = { }
        self.m_UseIntervalTime = { }
        self.m_PauseColdTime = { }
        self.m_ReachMaxCoverFunc = { }

    
    def SetOwner(self, oOwner):
        if oOwner:
            self.m_Owner = oOwner.m_ID
            self.m_PlayerID = oOwner.m_PlayerID
        else:
            self.m_Owner = 0
            self.m_PlayerID = 0

    
    def GetOwnerID(self):
        return self.m_Owner

    
    def GS2CPerformAdd(self, oPerform, dPlayer = None):
        if not (self.m_PlayerID) and not (oPerform.m_ClientNeed):
            return None
        GS2CPerformAdd(self.m_Game, self.m_Owner, oPerform, oPerform.m_PFType, oPerform.GetPerformPos(), dPlayer)

    
    def GS2CPerformRemove(self, oPerform, dPlayer = None):
        if oPerform.m_PFType != PF_TYPE_SUITACTIVE or not (self.m_PlayerID):
            return None
        if not dPlayer:
            dPlayer = {
                self.m_PlayerID: 1 }
        GS2CPerformRemove(self.m_Game, self.m_Owner, oPerform, dPlayer)

    
    def AddPerform(self, oOwner, iPerform, iLevel, iEnable, iItem, iAttPerformIdx = 255, iNotify = 0):
        if iPerform in self.m_Perform:
            oPerform = self.m_Perform[iPerform]
            if oPerform.m_Owner == oOwner.m_ID:
                oPerform.SetLevel(oOwner, iLevel)
                self.GS2CPerformAdd(oPerform)
                return oPerform
        oPerform = oOwner.m_Game.m_ResMgr.NewPerform(iPerform, oOwner, iLevel)
        if not oPerform:
            return None
        self.m_Perform[iPerform] = oPerform
        oPerform.m_Container = weakref.proxy(self)
        oPerform.m_Item = iItem
        oPerform.m_AttPerformIdx = iAttPerformIdx
        for iExtPerform in oPerform.m_ExtPerform:
            if iExtPerform in self.m_Perform:
                oExtPerform = self.m_Perform[iExtPerform]
                OtherLog.Debug('%d extperform err %d %d %d' % (self.m_Game.m_ID, iExtPerform, oPerform.m_SID, oExtPerform.m_MainPerform))
            oExtPF = oOwner.m_Game.m_ResMgr.NewPerform(iExtPerform, oOwner, iLevel)
            self.m_Perform[iExtPerform] = oExtPF
            oExtPF.m_MainPerform = oPerform.m_SID
            oExtPF.m_Item = oPerform.m_Item
            oExtPF.m_AttPerformIdx = iAttPerformIdx
            oExtPF.m_Container = weakref.proxy(self)
            self.GS2CPerformAdd(oExtPF)
        
        self.GS2CPerformAdd(oPerform)
        if iEnable:
            oPerform.Enable(oOwner, iNotify)
        return oPerform

    
    def RemovePerform(self, oOwner, iPerform, iNotify = 0):
        if iPerform not in self.m_Perform:
            return None
        oPerform = self.m_Perform[iPerform]
        oPerform.Disable(oOwner, iNotify)
        oPerform.m_Container = None
        self.GS2CPerformRemove(oPerform)
        oPerform.Release()
        return self.m_Perform.pop(iPerform)

    
    def EnablePerform(self, oOwner, iPerform, iNotify):
        if iPerform not in self.m_Perform:
            return None
        oPerform = self.m_Perform[iPerform]
        oPerform.Enable(oOwner, iNotify)

    
    def DisablePerform(self, oOwner, iPerform, iNotify):
        if iPerform not in self.m_Perform:
            return None
        oPerform = self.m_Perform[iPerform]
        oPerform.Disable(oOwner, iNotify)

    
    def GetPerform(self, iPerform):
        if iPerform not in self.m_Perform:
            return None
        return self.m_Perform[iPerform]

    
    def AllPerformEnable(self, iNotify = 1):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        for oPerform in list(self.m_Perform.values()):
            if oPerform.m_Enable:
                continue
            oPerform.Enable(oOwner, iNotify)
        

    
    def AllPerformDisable(self, iNotify = 0):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        for oPerform in list(self.m_Perform.values()):
            oPerform.Disable(oOwner, iNotify)
        

    
    def GetAllPerformSID(self):
        return list(self.m_Perform)

    
    def GetAllPerform(self):
        return self.m_Perform.values()

    
    def GetAllPerformLevel(self):
        dLevel = { }
        for oPerform in self.m_Perform.values():
            dLevel[oPerform.m_SID] = oPerform.Level()
        
        return dLevel

    
    def GetAllPerformStack(self):
        dStack = { }
        for oPerform in self.m_Perform.values():
            dStack[oPerform.m_SID] = oPerform.m_Stack
        

    
    def GetPerformSIDByType(self, iType):
        lstRet = []
        if iType & PF_TYPE_SUBCLASSIFY:
            lstRet = [ sid for sid, obj in self.m_Perform.items() if obj.m_PFType == iType ]
        else:
            lstRet = [ sid for sid, obj in self.m_Perform.items() if obj.m_PFType & iType == iType ]
        return lstRet

    
    def Release(self):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        if oOwner and oOwner.m_ReleaseFlag:
            oOwner = None
        self.m_ColdTime = { }
        for oPerform in self.m_Perform.values():
            if oOwner:
                oPerform.Disable(oOwner, iReleaseFlag = 1)
            oPerform.m_Container = None
            oPerform.Release()
        
        self.m_Perform = { }
        self.m_Game = None

    
    def Save(self):
        dData = { }
        dData['PF'] = self.GetAllPerformLevel()
        return dData

    
    def Load(self, dData):
        pass

    
    def GetCDPerform(self, iPerform):
        if iPerform not in self.m_Perform:
            return 0
        oPerform = self.m_Perform[iPerform]
        iCDPerform = oPerform.m_CDPerform
        if iCDPerform and iCDPerform in self.m_Perform:
            return iCDPerform
        return iPerform

    
    def ModifyColdTime(self, idx, iTime):
        idx = self.GetCDPerform(idx)
        if idx not in self.m_ColdTime:
            return None
        iCacheRemainTime = self.GetCacheColdTime(idx)
        if iCacheRemainTime > 0:
            iNowRemainTime = iCacheRemainTime
            iRealTime = max(-iNowRemainTime, iTime)
            self.m_CacheColdTime[idx] += iRealTime
        else:
            iNowRemainTime = self.GetNowCoverRemainTime(idx)
            iRealTime = max(-iNowRemainTime, iTime)
        if iTime > 0:
            iMaxColdTimeFrame = self.GetMaxColdTime(idx)
            if iMaxColdTimeFrame < iNowRemainTime + iTime:
                iRealTime = iMaxColdTimeFrame - iNowRemainTime
        self.SetTotalColdTime(idx, self.m_ColdTime[idx] + iRealTime)
        self.GS2CColdTimeAdd(idx)

    
    def GetPerformCDAndMaxCover(self, idx):
        iOwner = self.GetOwnerID()
        oOwner = self.m_Game.GetObject(iOwner)
        oPerform = self.GetPerform(idx)
        if not oPerform:
            SkillLog.Debug('%s %s pfcd rerr %s' % (self.m_Game.m_ID, self.m_PlayerID, idx))
            return (999, 1)
        iPerformCD = oPerform.GetCDTime(oOwner)
        iPerformMaxCover = oPerform.GetMaxCover(oOwner)
        return (iPerformCD, iPerformMaxCover)

    
    def InitPerformColdTimeData(self, idx, iRemainTime):
        (iPerformCD, iPerformMaxCover) = self.GetPerformCDAndMaxCover(idx)
        self.m_CacheColdTime[idx] = self.m_Game.GetFrameNum()
        self.m_CacheSumColdTime[idx] = 0
        self.m_LastAttrValue[idx] = { }
        self.m_LastAttrValue[idx]['ColdTime'] = iPerformCD
        self.m_LastAttrValue[idx]['MaxCover'] = iPerformMaxCover
        self.SetTotalColdTime(idx, self.m_Game.GetFrameNum() + iRemainTime)

    
    def AddColdTimeNoSend(self, idx, iRemainTime):
        if iRemainTime <= 0:
            return None
        idx = self.GetCDPerform(idx)
        if self.InColdTime(idx):
            self.SetTotalColdTime(idx, self.m_ColdTime[idx] + iRemainTime)
        else:
            self.InitPerformColdTimeData(idx, iRemainTime)

    
    def AddColdTime(self, idx, iRemainTime, iSend = 1, iActNum = 0):
        dInfo = {
            'pfid': idx,
            'iTime': iRemainTime }
        if iSend:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDPERFORMCD, self.m_Game.GetObject(self.m_Owner), dInfo, oGame = self.m_Game)
        iNewRemainFrame = dInfo['iTime']
        if iNewRemainFrame <= 0:
            if iRemainTime > 0:
                GS2CPerformColdTimeNoAdd(self.m_Game, self.m_PlayerID, self.GetOwnerID(), idx, iActNum)
            return None
        idx = self.GetCDPerform(idx)
        if self.InColdTime(idx):
            self.SetTotalColdTime(idx, self.m_ColdTime[idx] + iNewRemainFrame)
        else:
            self.InitPerformColdTimeData(idx, iNewRemainFrame)
        self.GS2CColdTimeAdd(idx, iActNum)

    
    def PauseColdDown(self, idx, iForce = 1):
        (iPerformCD, _) = self.GetPerformCDAndMaxCover(idx)
        if self.InColdTime(idx) and iPerformCD:
            self.m_PauseColdTime[idx] = 100 * (self.m_ColdTime[idx] - self.m_Game.GetFrameNum()) // iPerformCD
            self.DelColdTime(idx, 0)

    
    def ReStartColdDown(self, idx, iSend = 1):
        if idx in self.m_PauseColdTime and self.m_PauseColdTime[idx]:
            (iPerformCD, _) = self.GetPerformCDAndMaxCover(idx)
            iRemainTime = self.m_PauseColdTime[idx] * iPerformCD // 100
            self.m_PauseColdTime.pop(idx)
            self.AddColdTime(idx, iRemainTime, iSend)

    
    def SetColdTime(self, idx, iRemainTime, iSumTime):
        if iRemainTime <= 0 or iRemainTime > iSumTime:
            return None
        idx = self.GetCDPerform(idx)
        (iPerformCD, iPerformMaxCover) = self.GetPerformCDAndMaxCover(idx)
        iCover = self.GetCover(idx)
        iWaitCover = iPerformMaxCover - iCover - 1
        self.m_CacheColdTime[idx] = self.m_Game.GetFrameNum() + iRemainTime
        self.m_CacheSumColdTime[idx] = iSumTime
        self.SetTotalColdTime(idx, self.m_CacheColdTime[idx] + iWaitCover * iPerformCD)
        self.GS2CColdTimeAdd(idx)

    
    def RefreshColdTime(self, idx, iRemainTime):
        idx = self.GetCDPerform(idx)
        if not self.InColdTime(idx):
            self.AddColdTimeNoSend(idx, iRemainTime)
            self.SetColdTime(idx, iRemainTime, iRemainTime)
            return None
        iNowTime = self.GetColdTime(idx)
        if iNowTime < iRemainTime:
            self.SetColdTime(idx, iRemainTime, iRemainTime)
        elif iNowTime > iRemainTime:
            iMaxColdTime = self.GetMaxColdTime(idx)
            self.SetColdTime(idx, iRemainTime, iMaxColdTime)

    
    def DelColdTime(self, idx, iForce = 1):
        idx = self.GetCDPerform(idx)
        if idx not in self.m_ColdTime:
            return None
        self.m_ColdTime.pop(idx)
        self.m_CacheColdTime.pop(idx)
        self.m_CacheSumColdTime.pop(idx)
        self.m_LastAttrValue.pop(idx)
        if iForce == 1:
            self.GS2CColdTimeDel(idx)

    
    def DelNowCoverColdTime(self, idx):
        idx = self.GetCDPerform(idx)
        if idx not in self.m_ColdTime:
            return None
        self.SetTotalColdTime(idx, self.m_ColdTime[idx] - self.GetColdTime(idx))

    
    def InColdTime(self, idx):
        idx = self.GetCDPerform(idx)
        if idx in self.m_ColdTime:
            if self.m_ColdTime[idx] > self.m_Game.GetFrameNum():
                return 1
            self.DelColdTime(idx, 0)
        return 0

    
    def GetNowCoverRemainTime(self, idx):
        idx = self.GetCDPerform(idx)
        (iPerformCD, iPerformMaxCover) = self.GetPerformCDAndMaxCover(idx)
        iColdTime = 0
        if idx in self.m_ColdTime:
            iRemainTime = self.GetTotalColdTime(idx)
            if iRemainTime > 0:
                iCacheRemainTime = self.GetCacheColdTime(idx)
                iCover = self.GetCover(idx)
                if iCacheRemainTime > 0:
                    iColdTime = iCacheRemainTime
                else:
                    iFirstRemainTime = iRemainTime - iPerformCD * (iPerformMaxCover - 1 - iCover)
                    if iFirstRemainTime > 0:
                        iColdTime = iFirstRemainTime
                    else:
                        self.DelColdTime(idx, 0)

    
    def GetCurCoverRemainTime(self, idx):
        idx = self.GetCDPerform(idx)
        (iPerformCD, iPerformMaxCover) = self.GetPerformCDAndMaxCover(idx)
        iColdTime = 0
        if idx in self.m_ColdTime:
            iRemainTime = self.GetTotalColdTime(idx)
            if iRemainTime > 0:
                iCacheRemainTime = self.GetCacheColdTime(idx)
                if iCacheRemainTime > 0:
                    iColdTime = iCacheRemainTime
                elif iRemainTime > iPerformCD:
                    iCover = iRemainTime // iPerformCD
                    iFirstRemainTime = iRemainTime - iPerformCD * iCover
                    if iFirstRemainTime > 0:
                        iColdTime = iFirstRemainTime
                    
                iColdTime = iRemainTime
            else:
                self.DelColdTime(idx, 0)
        return iColdTime

    
    def GetColdTime(self, idx):
        idx = self.GetCDPerform(idx)
        if idx in self.m_PauseColdTime:
            return self.m_PauseColdTime[idx]
        (iPerformCD, iPerformMaxCover) = self.GetPerformCDAndMaxCover(idx)
        iColdTime = 0
        if idx in self.m_ColdTime:
            iRemainTime = self.GetTotalColdTime(idx)
            if iRemainTime > 0:
                iCacheRemainTime = self.GetCacheColdTime(idx)
                iCover = self.GetCover(idx)
                if iCacheRemainTime > 0 or iCover == 0:
                    iColdTime = iCacheRemainTime
                else:
                    iFirstRemainTime = iRemainTime - iPerformCD * (iPerformMaxCover - 1)
                    if iFirstRemainTime > 0:
                        iColdTime = iFirstRemainTime
                    else:
                        self.DelColdTime(idx, 0)

    
    def GetTotalColdTime(self, idx):
        idx = self.GetCDPerform(idx)
        iColdTime = 0
        if idx in self.m_ColdTime:
            iRemainTime = self.m_ColdTime[idx] - self.m_Game.GetFrameNum()
            if iRemainTime > 0:
                iColdTime = iRemainTime
            else:
                self.DelColdTime(idx, 0)
        return iColdTime

    
    def GetCacheColdTime(self, idx):
        idx = self.GetCDPerform(idx)
        iColdTime = 0
        if idx in self.m_CacheColdTime:
            iCacheRemainTime = self.m_CacheColdTime[idx] - self.m_Game.GetFrameNum()
            if iCacheRemainTime > 0:
                iColdTime = iCacheRemainTime
        return iColdTime

    
    def GetMaxColdTime(self, idx):
        idx = self.GetCDPerform(idx)
        if not self.InColdTime(idx):
            return 0
        iOwner = self.GetOwnerID()
        oOwner = self.m_Game.GetObject(iOwner)
        oPerform = self.GetPerform(idx)
        iPerformCD = oPerform.GetCDTime(oOwner)
        if self.GetCacheColdTime(idx) > 0:
            iMaxColdTime = self.m_CacheSumColdTime[idx]
        else:
            iMaxColdTime = iPerformCD
        return iMaxColdTime

    
    def HasCover(self, idx):
        iCover = self.GetCover(idx)
        return iCover > 0

    
    def GetCover(self, idx):
        idx = self.GetCDPerform(idx)
        if idx in self.m_PauseColdTime:
            return 0
        (_, iPerformMaxCover) = self.GetPerformCDAndMaxCover(idx)
        if not self.InColdTime(idx):
            return iPerformMaxCover
        iPerformCD = self.m_LastAttrValue[idx]['ColdTime']
        if iPerformCD == 0:
            return iPerformMaxCover - 1
        iPerformMaxCover = self.m_LastAttrValue[idx]['MaxCover']
        iRemainTime = self.GetTotalColdTime(idx)
        iCacheRemainTime = self.GetCacheColdTime(idx)
        if iCacheRemainTime > 0:
            iWaitRemainTime = iRemainTime - iCacheRemainTime
            iCover = iPerformMaxCover - iWaitRemainTime // iPerformCD - 1
        else:
            iCover = iPerformMaxCover - (iRemainTime + iPerformCD - 1) // iPerformCD
        if iCover < 0:
            SkillLog.Debug('%s %s %s covererr %s %s %s %s' % (self.m_Game.m_ID, self.m_PlayerID, idx, iPerformMaxCover, iRemainTime, iCacheRemainTime, iPerformCD))
            iCover = 0
        return iCover

    
    def RefreshColdTimeAttr(self, idx, sAttr):
        if idx != self.GetCDPerform(idx):
            return None
        if sAttr == 'ColdTime':
            self.PerformColdTimeChange(idx, sAttr)
        elif sAttr == 'MaxCover':
            self.PerformMaxCoverChange(idx, sAttr)

    
    def PerformColdTimeChange(self, idx, sAttr):
        (iPerformCD, iPerformMaxCover) = self.GetPerformCDAndMaxCover(idx)
        if not self.InColdTime(idx):
            return None
        iLastPerformCD = self.m_LastAttrValue[idx][sAttr]
        iCover = self.GetCover(idx)
        iCacheRemainTime = self.GetCacheColdTime(idx)
        iWaitCover = iPerformMaxCover - iCover - 1
        if iCacheRemainTime <= 0:
            self.m_CacheColdTime[idx] = self.m_ColdTime[idx] - iWaitCover * iLastPerformCD
            self.m_CacheSumColdTime[idx] = iLastPerformCD
        self.SetTotalColdTime(idx, self.m_CacheColdTime[idx] + iWaitCover * iPerformCD)
        if idx in self.m_LastAttrValue:
            self.m_LastAttrValue[idx][sAttr] = iPerformCD
        self.GS2CColdTimeAdd(idx)

    
    def PerformMaxCoverChange(self, idx, sAttr):
        iOwner = self.GetOwnerID()
        oOwner = self.m_Game.GetObject(iOwner)
        idx = self.GetCDPerform(idx)
        oPerform = self.GetPerform(idx)
        iPerformMaxCover = oPerform.GetMaxCover(oOwner)
        if not self.InColdTime(idx):
            self.GS2CColdTimeAdd(idx)
            return None
        iCover = self.GetCover(idx)
        iLastPerformMaxCover = self.m_LastAttrValue[idx][sAttr]
        self.m_LastAttrValue[idx][sAttr] = iPerformMaxCover
        if iLastPerformMaxCover > iPerformMaxCover and iCover >= iPerformMaxCover:
            self.DelColdTime(idx)
        elif iLastPerformMaxCover > iPerformMaxCover and iCover < iPerformMaxCover:
            iTotalColdTime = self.m_ColdTime[idx] - self.m_LastAttrValue[idx]['ColdTime'] * (iLastPerformMaxCover - iPerformMaxCover)
            self.SetTotalColdTime(idx, iTotalColdTime)
            self.GS2CColdTimeAdd(idx)
        else:
            self.GS2CColdTimeAdd(idx)

    
    def DelCoverColdTime(self, iPerform):
        iColdTime = self.GetMaxColdTime(iPerform)
        if not iColdTime:
            return None
        if iPerform not in self.m_ColdTime:
            return None
        iAllColdTime = self.m_ColdTime[iPerform]
        iTotalColdTime = iAllColdTime - iColdTime if iAllColdTime > iColdTime else 0
        self.SetTotalColdTime(iPerform, iTotalColdTime, iIsDel = 1)
        self.GS2CColdTimeAdd(iPerform)

    
    def SetTotalColdTime(self, idx, iFrame, iIsDel = 0):
        self.m_ColdTime[idx] = iFrame
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, self.m_Game.GetObject(self.m_Owner), {
            'pfid': idx,
            'IsDel': iIsDel }, oGame = self.m_Game)

    
    def ReachMaxCoverFunc(self, oOwner, idx):
        if idx in self.m_PauseColdTime or idx not in self.m_ReachMaxCoverFunc:
            return None
        oOwner.Remove_Call_Out('ReachMaxCoverFunc-%s' % idx)
        for func in self.m_ReachMaxCoverFunc[idx].values():
            func(oOwner, {
                'pfid': idx })
        

    
    def OnModifyPerformCD(self, oTarget, dInfo):
        iPerform = dInfo['pfid']
        if iPerform in self.m_ReachMaxCoverFunc and iPerform in self.m_ColdTime:
            iDelayFrame = self.m_ColdTime[iPerform] - self.m_Game.GetFrameNum()
            if iDelayFrame > 0:
                oTarget.Remove_Call_Out('ReachMaxCoverFunc-%s' % iPerform)
                oTarget.Call_Out(Functor(self.ReachMaxCoverFunc, oTarget, iPerform), iDelayFrame, 'ReachMaxCoverFunc-%s' % iPerform)
            elif iDelayFrame < 0:
                self.ReachMaxCoverFunc(oTarget, iPerform)

    
    def AddReachMaxCoverFunc(self, iPerform, sKey, func):
        if iPerform not in self.m_Perform:
            return None
        dMaxCoverFunc = self.m_ReachMaxCoverFunc
        if not dMaxCoverFunc:
            cl_msgcenter.AddFunction(self.m_Game.GetObject(self.m_Owner), cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, self.OnModifyPerformCD, 'ReachMaxCoverFunc', iOnce = 0)
        if iPerform not in dMaxCoverFunc:
            dMaxCoverFunc[iPerform] = {
                sKey: func }
        else:
            dMaxCoverFunc[iPerform][sKey] = func

    
    def ClearReachMaxCoverFunc(self, iPerform, sClearKey):
        dMaxCoverFunc = self.m_ReachMaxCoverFunc
        if iPerform not in dMaxCoverFunc:
            return None
        dMaxCoverFunc[iPerform].pop(sClearKey, None)
        if not dMaxCoverFunc[iPerform]:
            dMaxCoverFunc.pop(iPerform)
            oOwner = self.m_Game.GetObject(self.m_Owner)
            oOwner.Remove_Call_Out('ReachMaxCoverFunc-%s' % iPerform)
            if not dMaxCoverFunc:
                cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_MODIFYPERFORMCD, 'ReachMaxCoverFunc')

    
    def AddUseInterval(self, idx, iRemainTime):
        idx = self.GetCDPerform(idx)
        if iRemainTime <= 0:
            return None
        self.m_UseIntervalTime[idx] = self.m_Game.GetFrameNum() + iRemainTime
        self.GS2CAddUseInterval(idx, iRemainTime)

    
    def InUseInterval(self, idx):
        idx = self.GetCDPerform(idx)
        if idx in self.m_UseIntervalTime:
            if self.m_UseIntervalTime[idx] > self.m_Game.GetFrameNum():
                return 1
            self.m_UseIntervalTime.pop(idx)
        return 0

    
    def Refresh(self, dPlayer = None):
        for oPerform in self.m_Perform.values():
            oPerform.Refresh()
            self.GS2CPerformAdd(oPerform, dPlayer)
        
        for idx, iTime in self.m_ColdTime.items():
            iTime = iTime - self.m_Game.GetFrameNum()
            if iTime <= 0:
                continue
            self.GS2CColdTimeAdd(idx)
        

    
    def SelfRefresh(self):
        pass

    
    def IsEnabled(self, iPerform):
        if iPerform in self.m_Perform:
            pfobj = self.m_Perform[iPerform]
            return pfobj.m_Enable
        return False

    
    def RefreshItem(self, idx):
        idx = self.GetCDPerform(idx)
        if idx in self.m_ColdTime:
            iTime = self.m_ColdTime[idx] - self.m_Game.GetFrameNum()
            if iTime > 0:
                self.GS2CColdTimeAdd(idx)

    
    def GS2CAddUseInterval(self, idx, iRemainTime):
        if not self.m_PlayerID:
            return None
        GS2CPerformAddUseInterval(self.m_Game, self.m_PlayerID, self.GetOwnerID(), idx, iRemainTime * GAME_FRAME_TIME)

    
    def GS2CColdTimeAdd(self, idx, iActNum = 0):
        if not self.m_PlayerID:
            return None
        if idx not in self.m_ColdTime:
            iCacheSumTime = 0
        else:
            iCacheSumTime = self.m_CacheSumColdTime[idx]
        iRemainTime = self.GetTotalColdTime(idx)
        iCacheRemainTime = self.GetCacheColdTime(idx)
        GS2CPerformColdTimeAdd(self.m_Game, self.m_PlayerID, self.GetOwnerID(), idx, iRemainTime * GAME_FRAME_TIME, iCacheRemainTime * GAME_FRAME_TIME, iCacheSumTime * GAME_FRAME_TIME, iActNum)

    
    def GS2CColdTimeDel(self, idx):
        if not self.m_PlayerID:
            return None
        GS2CPerformColdTimeDel(self.m_Game, self.m_PlayerID, self.GetOwnerID(), idx)



class CEquipPerformContainer(CPerformContainer):
    m_BagType = BAG_TYPE_COLDTIME
    
    def __init__(self, oItem):
        self.m_Equip = WeakProxy(oItem)
        self.m_Game = oItem.m_Game
        self.m_Perform = { }
        self.InitColdTimeData()

    
    def Release(self):
        super(CEquipPerformContainer, self).Release()
        self.m_Equip = None

    
    def GetOwnerID(self):
        return self.m_Equip.m_Owner

    
    def GS2CPerformAdd(self, oPerform, dPlayer = None):
        oOwner = self.m_Equip.GetOwner()
        if oOwner:
            GS2CPerformAdd(self.m_Game, oOwner.m_ID, oPerform, oPerform.m_PFType, oPerform.GetPerformPos())

    
    def GS2CColdTimeAdd(self, idx):
        pass

    
    def GS2CColdTimeDel(self, iPerform):
        pass

    
    def AllPerformChangeEnableByHold(self, iHoldPos):
        oOwner = self.m_Game.GetObject(self.GetOwnerID())
        for oPerform in list(self.m_Perform.values()):
            iItemEnableType = oPerform.m_ItemEnableType
            iEnable = 0
            if not iItemEnableType & ITEMPERFORM_ENABLE_HOLD or iHoldPos:
                if (iItemEnableType & ITEMPERFORM_ENABLE_UNHOLD or not iHoldPos or iItemEnableType & ITEMPERFORM_ENABLE_MAINHOLD) and iHoldPos == MAIN_HOLD:
                    iEnable = 1
            if None:
                oPerform.Enable(oOwner)
                continue
            oPerform.Disable(oOwner)
        


