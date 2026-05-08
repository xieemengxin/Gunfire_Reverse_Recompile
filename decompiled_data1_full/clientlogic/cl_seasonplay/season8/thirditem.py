# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season8/thirditem.pyc
# RelativePath: clientlogic/cl_seasonplay/season8/thirditem.pyc
# Source Generated with Decompyle++
# File: thirditem.pyc (Python 3.6)

from cl_only import Time2Frame, SendAlert, Frame2Time, ChooseKey, DeepCopy
from cl_item.baseitem import CBaseItem
from cl_commondefines import THIRDITEM_MASK, SEASONPASSIVE_TAG_S8_THIRDCOMMON, SEASONPASSIVE_TAG_S8_COMMON, S8THIRDACTIVE_STATE_START, S8THIRDACTIVE_STATE_END, S8THIRDACTIVE_STATE_INITSTATE, S8THIRDACTIVE_STATE_ALLEND, S8THIRDACTIVE_ENERGY_CHANGE_ADD, S8THIRDACTIVE_ENERGY_CHANGE_SUB
from cl_commondefines import S8THIRDACTIVE_REFRESH_RECOVERVALUE, S8THIRDACTIVE_REFRESH_RECOVERINTERVAL, S8THIRDACTIVE_REFRESH_ENERGYCOST, S8THIRDACTIVE_REFRESH_MAXENERGY
from cl_platformdata import GetS8PassiveByTag, GetThirdItemSpecialAbility, GetThirdAbilityChooseRule, GetThirdAbilityNum
from cl_cscommondef import DEBUG_STATUS_NOPFCD
import cl_msgcenter

class CS8ThirdItemData(object):
    m_SID = 0
    m_Name = ''
    m_Type = THIRDITEM_MASK
    m_PassivePerform = 0
    m_ActivePerform = 0
    m_ItemAttr = { }
    
    def Create(cls, oGame, dItemData, iPointID = 0, dTmp = None):
        oItem = CS8ThirdItem(oGame, 0, iPointID, dTmp)
        cls.InitItemData(oItem)
        oItem.Init()
        if dItemData:
            oItem.Load(dItemData)
        oItem.OnCreate()
        return oItem

    Create = classmethod(Create)
    
    def Load(cls, oGame, dItemData, iPointID = 0, dTmp = None):
        oItem = CS8ThirdItem(oGame, 0, iPointID, dTmp)
        cls.InitItemData(oItem)
        oItem.Init()
        if dItemData:
            oItem.Load(dItemData)
        return oItem

    Load = classmethod(Load)
    
    def InitItemData(cls, oItem):
        oItem.m_SID = cls.m_SID
        oItem.m_Name = cls.m_Name
        oItem.m_Type = cls.m_Type
        oItem.m_PassivePerform = cls.m_PassivePerform
        oItem.m_ActivePerform = cls.m_ActivePerform
        oItem.m_ItemAttr = cls.m_ItemAttr

    InitItemData = classmethod(InitItemData)


class CS8ThirdItem(CBaseItem):
    m_CallOutFlag = 'S8ThirdItem'
    m_ItemAttrToSubMsg = {
        'MaxEnergy': S8THIRDACTIVE_REFRESH_MAXENERGY,
        'EnergyCost': S8THIRDACTIVE_REFRESH_ENERGYCOST,
        'RecoverInterval': S8THIRDACTIVE_REFRESH_RECOVERINTERVAL,
        'RecoverValue': S8THIRDACTIVE_REFRESH_RECOVERVALUE }
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super().__init__(oGame, iTemp, iPointID, dTmp)
        self.m_GameID = oGame.m_ID
        self.m_Quality = 0
        self.m_PassivePerform = 0
        self.m_ActivePerform = 0
        self.m_Ability = { }
        self.m_Energy = 0
        self.m_KeepState = { }
        self.m_StartTime = 0
        self.m_EndTime = 0

    
    def __str__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-%s-%s-%s-%s-%s-%s-%s-%s' % (self.m_GameID, iPlayerID, self.__class__.__name__, self.m_SID, self.m_ID, self.m_Quality, self.m_PassivePerform, self.m_ActivePerform, self.m_Ability, self.m_Energy)

    
    def __repr__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-%s-%s-%s-%s-%s-%s-%s-%s' % (self.m_GameID, iPlayerID, self.__class__.__name__, self.m_SID, self.m_ID, self.m_Quality, self.m_PassivePerform, self.m_ActivePerform, self.m_Ability, self.m_Energy)

    
    def Load(self, dData):
        super().Load(dData)
        self.m_SID = dData.get('SID', 0)
        self.m_Quality = dData.get('QL', 0)
        self.m_Ability = dData.get('AB', { })
        self.m_Energy = dData.get('E', 0)

    
    def Save(self):
        dData = super().Save()
        dData['SID'] = self.m_SID
        dData['QL'] = self.m_Quality
        dData['AB'] = self.m_Ability
        dData['E'] = self.m_Energy
        return dData

    
    def OnCreate(self):
        lstAbility = self.ChooseAbility()
        self.m_Ability = { }
        for iAbility, iQuality in lstAbility:
            self.m_Ability[iAbility] = iQuality
        

    
    def Release(self):
        self.Disable()
        self.m_Ability = { }
        self.m_KeepState = { }
        super().Release()

    
    def Enable(self):
        if self.m_Enable:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        self.m_Enable = 1
        iRecoverInterval = self.QueryAttr('RecoverInterval')
        if iRecoverInterval:
            oOwner.Call_Out(self.AutoRecoverEnergy, Time2Frame(iRecoverInterval), self.m_CallOutFlag)

    
    def Disable(self):
        if not self.m_Enable:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        self.m_Enable = 0
        oOwner.Remove_Call_Out(self.m_CallOutFlag)
        self.ClearKeepState()

    
    def ChooseAbility(self):
        iQuality = self.m_Quality
        iAbilityNum = GetThirdAbilityNum(iQuality)
        lstChooseQuality = self.ChooseAbilityQuality(iAbilityNum)
        dCanChooseAbility = DeepCopy(self.GetCanChooseAbility())
        lstAbility = []
        for iQuality in lstChooseQuality:
            if not dCanChooseAbility:
                break
            iAbility = ChooseKey(self.m_Game, dCanChooseAbility)
            dCanChooseAbility.pop(iAbility)
            lstAbility.append((iAbility, iQuality))
        
        if len(lstAbility) != iAbilityNum:
            SendAlert('err', '%d %d chooseabilityquality err %s %s %s %s %s' % (self.m_Game.m_ID, self.m_Owner, self, iAbilityNum, lstAbility, lstChooseQuality, dCanChooseAbility))
        return lstAbility

    
    def GetCanChooseAbility(self):
        dCanChooseAbility = { }
        dCanChooseAbility.update(GetS8PassiveByTag(SEASONPASSIVE_TAG_S8_COMMON))
        dCanChooseAbility.update(GetS8PassiveByTag(SEASONPASSIVE_TAG_S8_THIRDCOMMON))
        dSpecialAbility = GetThirdItemSpecialAbility(self.m_SID)
        dCanChooseAbility.update(dSpecialAbility)
        return dCanChooseAbility

    
    def ChooseAbilityQuality(self, iChooseNum):
        oGame = self.m_Game
        iQuality = self.m_Quality
        dQualityChoose = DeepCopy(GetThirdAbilityChooseRule(iQuality))
        dQuality2Num = { }
        lstChooseQuality = []
        for _ in range(0, iChooseNum):
            if not dQualityChoose:
                break
            (iAbilityQuality, iMaxNum) = ChooseKey(oGame, dQualityChoose)
            iQualityNum = dQuality2Num[iAbilityQuality] + 1 if iAbilityQuality in dQuality2Num else 1
            dQuality2Num[iAbilityQuality] = iQualityNum
            lstChooseQuality.append(iAbilityQuality)
            if iQualityNum >= iMaxNum:
                dQualityChoose.pop((iAbilityQuality, iMaxNum))
        
        return lstChooseQuality

    
    def GetAllAttr(self):
        dAttr = { }
        for sAttr in self.m_PrivateAttr:
            dAttr[sAttr] = self.QueryAttr(sAttr)
        
        dAttr['Energy'] = self.m_Energy
        dAttr['AllTime'] = self.GetAllTime()
        dAttr['RemainTime'] = self.GetRemainTime()
        return dAttr

    
    def KeepStateStart(self, oState):
        if not oState or oState.m_Item != self.m_ID:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, oOwner, { }, iSub = S8THIRDACTIVE_STATE_START)
        if not self.m_KeepState:
            self.m_StartTime = self.m_Game.GetFrameNum()
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, oOwner, { }, iSub = S8THIRDACTIVE_STATE_INITSTATE)
        self.m_KeepState[oState.m_ID] = 1
        self.KeepStateUpdate()

    
    def KeepStateEnd(self, oState):
        if not oState or oState.m_Item != self.m_ID:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, oOwner, { }, iSub = S8THIRDACTIVE_STATE_END)
        self.m_KeepState.pop(oState.m_ID, None)
        if not self.m_KeepState:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8THIRDACTIVE_STATE, oOwner, {
                'KeepTime': self.GetKeepTime() }, iSub = S8THIRDACTIVE_STATE_ALLEND)
            self.m_StartTime = 0
        self.KeepStateUpdate()

    
    def KeepStateUpdate(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oStateCon = oOwner.m_State
        if not oStateCon:
            return None
        iEndTime = 0
        for iState in self.m_KeepState:
            oState = oStateCon.GetItem(iState)
            if not oState:
                continue
            iEndTime = max(iEndTime, oState.m_StartTime + oState.GetTime())
        
        self.m_EndTime = iEndTime
        oS8Con = self.GetItemContainer()
        if oS8Con:
            oS8Con.GS2CRefreshItemAttr(self.m_ID, [
                'AllTime',
                'RemainTime'])

    
    def ClearKeepState(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oStateCon = oOwner.m_State
        if not oStateCon:
            return None
        for iState in list(self.m_KeepState):
            oStateCon.RemoveItem(iState)
        

    
    def GetKeepTime(self):
        iStartFrame = self.m_StartTime
        if not iStartFrame:
            return 0
        iCurFrame = self.m_Game.GetFrameNum()
        return Frame2Time(iCurFrame - iStartFrame)

    
    def GetAllTime(self):
        iAllTime = self.m_EndTime - self.m_StartTime
        if iAllTime < 0:
            return 0
        return Frame2Time(iAllTime)

    
    def GetRemainTime(self):
        iRemainTime = self.m_EndTime - self.m_Game.GetFrameNum()
        if iRemainTime < 0:
            return 0
        return Frame2Time(iRemainTime)

    
    def RefreshAttr(self, sAttr, iValue):
        if sAttr == 'MaxEnergy' and self.m_Energy > iValue:
            self.m_Energy = iValue
        oS8Con = self.GetItemContainer()
        if oS8Con:
            oS8Con.GS2CRefreshItemAttr(self.m_ID, [
                sAttr])
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, oOwner, { }, iSub = self.m_ItemAttrToSubMsg[sAttr])

    
    def Energy(self):
        return self.m_Energy

    
    def CheckCanUseActive(self):
        iEnergyCost = self.QueryAttr('EnergyCost')
        return self.m_Energy >= iEnergyCost

    
    def UseActiveCost(self):
        oOwner = self.GetOwner()
        if oOwner and oOwner.Query('DebugStatus', 0) & DEBUG_STATUS_NOPFCD == DEBUG_STATUS_NOPFCD:
            return 0
        iEnergyCost = self.QueryAttr('EnergyCost')
        return self.ChangeEnergy(-iEnergyCost)

    
    def ChangeEnergy(self, iChange):
        iOldEnergy = self.m_Energy
        iNewEnergy = iOldEnergy + iChange
        iMaxEnergy = self.QueryAttr('MaxEnergy')
        if iNewEnergy < 0:
            iNewEnergy = 0
            iTrueChange = -iOldEnergy
        elif iNewEnergy > iMaxEnergy:
            iNewEnergy = iMaxEnergy
            iTrueChange = iMaxEnergy - iOldEnergy
        else:
            iTrueChange = iChange
        oOwner = self.GetOwner()
        if oOwner:
            if iTrueChange > 0:
                dMsgInfo = {
                    'AddEnergy': iTrueChange }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, oOwner, dMsgInfo, iSub = S8THIRDACTIVE_ENERGY_CHANGE_ADD)
            elif iTrueChange < 0:
                dMsgInfo = {
                    'EnergyCost': iTrueChange }
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_STHIRDACTIVE_ENERGY_CHANGE, oOwner, dMsgInfo, iSub = S8THIRDACTIVE_ENERGY_CHANGE_SUB)
            else:
                return 0
        self.m_Energy = iNewEnergy
        oS8Con = self.GetItemContainer()
        if oS8Con:
            oS8Con.GS2CRefreshItemAttr(self.m_ID, [
                'Energy'])
        return iNewEnergy - iOldEnergy

    
    def AutoRecoverEnergy(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oOwner.Remove_Call_Out(self.m_CallOutFlag)
        iRecoverInterval = self.QueryAttr('RecoverInterval')
        if iRecoverInterval:
            oOwner.Call_Out(self.AutoRecoverEnergy, Time2Frame(iRecoverInterval), self.m_CallOutFlag)
        iRecoverValue = self.QueryAttr('RecoverValue')
        self.ChangeEnergy(iRecoverValue)


