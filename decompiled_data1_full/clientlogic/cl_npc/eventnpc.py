# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/eventnpc.pyc
# RelativePath: clientlogic/cl_npc/eventnpc.pyc
# Source Generated with Decompyle++
# File: eventnpc.pyc (Python 3.6)

from cl_commondefines import NPC_OPTION_REWARD_COSTRELIC, NPC_CB_VALUE, NPC_OPTION_REWARD_RELIC, NPC_OPTION_COST_CURSERELIC, NPC_OPTION_COST_RELIC, NPC_OPTION_REWARD_WEAPONACTION, NPC_OPTION_REWARD_WEAPON, INTERACT_TYPE_FORBID, NPC_OPTION_REWARD_UPGRADERELIC
from cl_only import Functor
from cl_object.logging import WarnpcLog
from cl_notify import GetCommonNotifyMsg
import cl_netattr
import cl_perform
import cl_item
import cl_msgcenter
import cl_notify
import cl_formula
import cl_platformdata
from .mobject import SendNpcRefreshMsg, SendNpcChooseMsg
from . import magicbox
from . import net

class CEventNPC(magicbox.CBoxNPC):
    
    def __init__(self, *args):
        super(CEventNPC, self).__init__(*args)
        self.m_Stage = { }
        self.m_Event = { }
        self.m_Titles = { }
        self.m_EventDataSID = 0
        self.m_InteractChooseCnt = { }
        self.m_ExtraChoose = { }

    
    def Release(self):
        for dStage in self.m_Event.values():
            for oOption in dStage.values():
                oOption.Release()
            
        
        self.m_Event = { }
        super(CEventNPC, self).Release()

    
    def GetOption(self, tKey):
        if tKey[0] not in self.m_Event:
            return None
        if tKey[1] not in self.m_Event[tKey[0]]:
            return None
        return self.m_Event[tKey[0]][tKey[1]]

    
    def SetEvent(self, clsEventData):
        self.m_Event = { }
        self.m_Stage = { }
        lstHero = self.m_Game.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            self.m_InteractChooseCnt[iHero] = 0
        
        self.m_EventDataSID = clsEventData.m_SID
        for iStage, dStage in clsEventData.m_Event.items():
            self.m_Event[iStage] = { }
            for iOp, dOption in dStage.items():
                self.m_Event[iStage][iOp] = EventOption((iStage, iOp), dOption, self.m_FormulaLimit)
            
            self.m_Titles[iStage] = GetCommonNotifyMsg(clsEventData.m_Titles[iStage])
        

    
    def ValidInteract(self, oHero):
        if not self.m_Event:
            return False
        return super(CEventNPC, self).ValidInteract(oHero)

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        self.RefreshStage(oHero)
        self.SendInteractMsg(oHero)

    
    def HasNoLimitChoose(self, oHero, iStage):
        iHero = oHero.m_ID
        iExtra = oHero.Query('NpcInteractExtraChoose', 0)
        if iExtra and iHero not in self.m_ExtraChoose:
            return True
        for oOption in self.m_Event[iStage].values():
            if iHero not in oOption.m_ChooseHero:
                return True
        
        return False

    
    def RefreshStage(self, oHero):
        iHero = oHero.m_ID
        iNoLimit = oHero.Query('NpcInteractChooseNoLimit', 0)
        if iHero not in self.m_Stage:
            self.m_Stage[iHero] = 1
        iStage = self.m_Stage[iHero]
        if iNoLimit and iStage > 1:
            iPreStage = iStage - 1
            if self.HasNoLimitChoose(oHero, iPreStage):
                self.m_Stage[iHero] = iPreStage
                iStage = iPreStage
        if not iNoLimit and iStage in self.m_Event:
            for oOption in self.m_Event[iStage].values():
                if iHero in oOption.m_ChooseHero:
                    self.m_Stage[iHero] += 1
                    iStage = self.m_Stage[iHero]
                    break
            
        if iStage in self.m_Event:
            lstAllOption = []
            iExtra = oHero.Query('NpcInteractExtraChoose', 0)
            for iOp, oOption in self.m_Event[iStage].items():
                if not iHero not in oOption.m_ChooseHero:
                    if iExtra and iHero not in self.m_ExtraChoose:
                        oOption.TryInitOption(oHero)
                        lstOption = [
                            iOp,
                            oOption.ValidChoose(self, oHero)]
                        lstOption.extend(oOption.GetOptionData(oHero))
                        lstAllOption.append(lstOption)
                        continue
            
            sTitle = self.m_Titles[iStage]
            net.GS2CNpcEvent(oHero, self.m_ID, sTitle, lstAllOption)
            net.SetNpcUICallBackFunction(oHero, NPC_CB_VALUE, Functor(InteractChooseOption, self.m_ID), self)
            SendNpcRefreshMsg(oHero, self, iStage, lstAllOption)

    
    def ChooseOption(self, oHero, iOp):
        iStage = self.GetCurStage(oHero)
        dStage = self.m_Event.get(iStage, { })
        if not dStage:
            return 0
        oOption = dStage.get(iOp, None)
        if not oOption:
            return 0
        iExtra = oHero.Query('NpcInteractExtraChoose', 0)
        if (not iExtra or oHero.m_ID in self.m_ExtraChoose) and oHero.m_ID in oOption.m_ChooseHero:
            return 0
        if not oOption.ValidChoose(self, oHero):
            return 0
        if iExtra and oHero.m_ID in oOption.m_ChooseHero:
            bExtraChoose = True
        else:
            bExtraChoose = False
        oOption.TryChooseOption(self, oHero, Functor(self.ChooseOptionEnd, bExtraChoose))
        return 1

    
    def ChooseOptionEnd(self, bExtraChoose, oHero, tKey):
        iHero = oHero.m_ID
        if bExtraChoose:
            self.m_ExtraChoose[iHero] = 1
        iNoLimit = oHero.Query('NpcInteractChooseNoLimit', 0)
        iOldStage = self.m_Stage[iHero]
        if iNoLimit and self.m_Event[iOldStage]:
            self.RefreshStage(oHero)
            if not self.HasNoLimitChoose(oHero, iOldStage):
                self.m_Stage[iHero] += 1
            else:
                self.m_Stage[iHero] += 1
        None.BoxModelOpen(oHero.m_PlayerID)
        if self.m_Stage[iHero] not in self.m_Event:
            self.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
                oHero.m_PlayerID])
        SendNpcChooseMsg(oHero, self, tKey[1])

    
    def CostLog(self, oHero, sInfo):
        WarnpcLog.Info('%d %d %d evtopcost %s' % (self.m_Game.m_ID, oHero.m_PlayerID, self.m_SID, sInfo))

    
    def GetCurStage(self, oHero):
        return self.m_Stage.get(oHero.m_ID, 1)

    
    def ActionKey(self, tOp):
        sKey = 'NPC-%d-choose-event-%s' % (self.m_EventDataSID, tOp)
        return sKey



def InteractChooseOption(iNpc, oHero, iOption):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    iResult = oNpc.ChooseOption(oHero, iOption)
    if not iResult:
        oNpc.RefreshStage(oHero)


class NPCEventData(object):
    m_SID = 0
    m_Titles = { }
    m_Event = { }


class EventOption(object):
    
    def __init__(self, tKey, dOption, dFormulaLimit):
        self.m_ID = tKey
        self.m_Title = GetCommonNotifyMsg(dOption['Title']) if dOption['Title'] else ''
        self.m_CostTips = GetCommonNotifyMsg(dOption['CostTips']) if dOption['CostTips'] else ''
        self.m_CostType = dOption['CostType']
        self.m_InitCostFunc = dOption['InitCostFunc']
        self.m_RewardTips = GetCommonNotifyMsg(dOption['RewardTips']) if dOption['RewardTips'] else ''
        self.m_RewardType = dOption['RewardType']
        self.m_InitRewardFunc = dOption['InitRewardFunc']
        self.m_GainRewardTips = dOption['GainRewardTips']
        self.m_RewardDelay = dOption['RewardDelay'] if 'RewardDelay' in dOption else 0
        self.m_LimitInfo = dFormulaLimit
        self.m_CostFunc = { }
        self.m_CostData = { }
        self.m_RewardFunc = { }
        self.m_RewardData = { }
        self.m_ExtraConditionFunc = { }
        self.m_ChooseFuncIdx = 0
        self.m_ChooseFunc = { }
        self.m_ChooseData = { }
        self.m_ChooseCallBack = { }
        self.m_CostRelic = { }
        self.m_ChooseHero = { }

    
    def Release(self):
        if self.m_RewardType == NPC_OPTION_REWARD_WEAPON:
            for dReward in self.m_RewardData.values():
                oWeapon = dReward['Item']
                if oWeapon and not oWeapon.GetOwner():
                    oWeapon.Release()
            
        self.m_CostFunc = { }
        self.m_CostData = { }
        self.m_RewardFunc = { }
        self.m_RewardData = { }
        self.m_ExtraConditionFunc = { }
        self.m_ChooseFunc = { }
        self.m_ChooseData = { }
        self.m_ChooseCallBack = { }

    
    def AddCostRelic(self, iHero, iRelic):
        self.m_CostRelic[iHero] = iRelic

    
    def AddChooseFunc(self, iHero, chooseFunc):
        self.m_ChooseFuncIdx += 1
        dChooseFunc = self.m_ChooseFunc.setdefault(iHero, { })
        dChooseFunc[self.m_ChooseFuncIdx] = chooseFunc
        return self.m_ChooseFuncIdx

    
    def AddChooseData(self, iHero, idx, dData):
        dChooseData = self.m_ChooseData.setdefault(iHero, { })
        dChooseData[idx] = dData

    
    def GetChooseData(self, iHero, idx):
        if iHero not in self.m_ChooseData:
            return { }
        if idx not in self.m_ChooseData[iHero]:
            return { }
        return self.m_ChooseData[iHero][idx]

    
    def TryInitOption(self, oHero):
        iHero = oHero.m_ID
        if self.m_CostType and iHero not in self.m_CostFunc and self.m_InitCostFunc:
            self.m_InitCostFunc(self, oHero)
        if self.m_RewardType and iHero not in self.m_RewardFunc and self.m_InitRewardFunc:
            self.m_InitRewardFunc(self, oHero)

    
    def GetOptionData(self, oHero):
        iHero = oHero.m_ID
        dCostData = self.m_CostData.get(iHero, { })
        iCostSID = dCostData.get('SID', 0)
        iCostAmount = dCostData.get('Amount', 0)
        dRewardData = self.m_RewardData.get(iHero, { })
        iRewardSID = dRewardData.get('SID', 0)
        dRewardAttr = self.GetRewardAttr(oHero)
        iRewardAmount = dRewardData.get('Amount', 0)
        dInfo = self.m_LimitInfo
        iRewardAmount = cl_formula.GetFormulaResult(oHero, iRewardAmount, dInfo)
        lstData = [
            self.m_Title,
            self.m_CostType,
            self.m_CostTips,
            iCostSID,
            iCostAmount,
            self.m_RewardType,
            self.m_RewardTips,
            iRewardSID,
            dRewardAttr,
            iRewardAmount]
        return lstData

    
    def GetRewardAttr(self, oHero):
        lstAttr = []
        iHero = oHero.m_ID
        dAttr = {
            'Attr': lstAttr }
        if iHero not in self.m_RewardData:
            return dAttr
        if self.m_RewardType == NPC_OPTION_REWARD_WEAPON:
            oWeapon = self.m_RewardData[iHero]['Item']
            if oWeapon:
                for sAttr in cl_netattr.INFO_OBJECT_INIT[cl_netattr.PROP_DROPITEM_MAINWEAPON]:
                    (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
                    iValue = cl_netattr.GetPropValue(oWeapon, sAttr, iMode)
                    if iValue is None:
                        continue
                    lstAttr.append((iIdx, iType, iLen, iValue))
                
        if self.m_RewardType == NPC_OPTION_REWARD_WEAPONACTION:
            iPos = self.m_RewardData[iHero]['Pos']
            (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME['Pos']
            lstAttr.append((iIdx, iType, iLen, iPos))
            oWeapon = oHero.m_WieldCon.GetItemByPos(iPos)
            if oWeapon:
                for sAttr in cl_netattr.INFO_OBJECT_INIT[cl_netattr.PROP_DROPITEM_MAINWEAPON]:
                    (iIdx, _, iType, iLen, iMode) = cl_netattr.INFO_PROP_NAME[sAttr]
                    iValue = cl_netattr.GetPropValue(oWeapon, sAttr, iMode)
                    if iValue is None:
                        continue
                    lstAttr.append((iIdx, iType, iLen, iValue))
                
        return dAttr

    
    def AddConditionFunc(self, iHero, conFunc):
        lstConFunc = self.m_ExtraConditionFunc.setdefault(iHero, [])
        lstConFunc.append(conFunc)

    
    def ValidChoose(self, oNpc, oHero):
        iHero = oHero.m_ID
        if self.m_CostType:
            if iHero not in self.m_CostFunc:
                return 0
            (validCostFunc, _) = self.m_CostFunc[iHero]
            if validCostFunc and not validCostFunc(oNpc, oHero):
                return 0
        if self.m_RewardType and iHero not in self.m_RewardFunc:
            return 0
        if iHero in self.m_ExtraConditionFunc:
            for conFunc in self.m_ExtraConditionFunc[iHero]:
                if not conFunc(oNpc, oHero):
                    return 0
            
        return 1

    
    def TryChooseOption(self, oNpc, oHero, cbFunc):
        iHero = oHero.m_ID
        self.m_ChooseCallBack[iHero] = cbFunc
        self.m_ChooseData.setdefault(iHero, { })
        self.ChooseOption(oNpc, oHero)

    
    def WaitChoose(self, oHero):
        iHero = oHero.m_ID
        if iHero not in self.m_ChooseFunc:
            return 0
        for idx in self.m_ChooseFunc[iHero]:
            if idx not in sorted(self.m_ChooseData[iHero]):
                return idx
        
        return 0

    
    def ChooseOption(self, oNpc, oHero):
        idx = self.WaitChoose(oHero)
        if idx:
            iHero = oHero.m_ID
            if iHero not in self.m_ChooseFunc:
                return None
            if idx not in self.m_ChooseFunc[iHero]:
                return None
            chooseFunc = self.m_ChooseFunc[iHero][idx]
            chooseFunc(oNpc, oHero)
        else:
            self.TrueChooseOption(oNpc, oHero)

    
    def TrueChooseOption(self, oNpc, oHero):
        if not self.ValidChoose(oNpc, oHero):
            return None
        iHero = oHero.m_ID
        if self.m_CostType:
            (_, costFunc) = self.m_CostFunc.pop(iHero)
            if not costFunc(oNpc, oHero):
                return None
        if self.m_RewardType:
            rewardFunc = self.m_RewardFunc.pop(iHero)
            rewardFunc(oNpc, oHero)
            if self.m_GainRewardTips:
                dReplaceInfo = { }
                sCost = self.GetCostStr(oHero)
                sReward = self.GetRewardStr(oHero)
                if sCost:
                    dReplaceInfo['$cost'] = sCost
                if sReward:
                    dReplaceInfo['$reward'] = sReward
                cl_notify.SendCommonNotify(oNpc.m_Game, [
                    oHero.m_PlayerID], self.m_GainRewardTips, dReplaceInfo)
        self.m_ChooseHero[iHero] = 1
        self.m_ExtraConditionFunc.pop(iHero, None)
        self.m_CostData.pop(iHero, None)
        dReward = self.m_RewardData.pop(iHero, { })
        iRelic = 0
        if self.m_RewardType == NPC_OPTION_REWARD_RELIC:
            iRelic = dReward['SID'] if 'SID' in dReward else 0
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EVENTNPC_AFTERREWARD, oHero, {
            'Relic': iRelic })
        cbFunc = self.m_ChooseCallBack.pop(iHero)
        cbFunc(oHero, self.m_ID)
        oNpc.m_InteractChooseCnt[oHero.m_ID] += 1

    
    def GetCostStr(self, oHero):
        sCost = ''
        iHero = oHero.m_ID
        if iHero in self.m_CostData:
            iCostSID = self.m_CostData[iHero].get('SID', 0)
            if iCostSID and self.m_CostType in (NPC_OPTION_COST_RELIC, NPC_OPTION_COST_CURSERELIC):
                sCost = cl_perform.GetPerformModule(iCostSID).m_Name
        if not sCost:
            tResult = cl_platformdata.GetCommonNotify(7267)
            if tResult is not None:
                (sCost, _) = tResult
        return sCost

    
    def GetRewardStr(self, oHero):
        sReward = ''
        iHero = oHero.m_ID
        if iHero in self.m_RewardData:
            lstRewardSID = self.m_RewardData[iHero].get('SID', [])
            if not lstRewardSID:
                return sReward
            if isinstance(lstRewardSID, int):
                lstRewardSID = [
                    lstRewardSID]
            lstReward = []
            for iRewardSID in lstRewardSID:
                if self.m_RewardType in (NPC_OPTION_REWARD_COSTRELIC, NPC_OPTION_REWARD_RELIC, NPC_OPTION_REWARD_UPGRADERELIC):
                    sReward = cl_perform.GetPerformModule(iRewardSID).m_Name
                elif self.m_RewardType == NPC_OPTION_REWARD_WEAPON:
                    sReward = cl_item.GetItemCls(iRewardSID).m_Name
                lstReward.append(sReward)
                if iRewardSID != lstRewardSID[-1]:
                    lstReward.append(' ')
            
            sReward = ''.join(lstReward)
        return sReward


