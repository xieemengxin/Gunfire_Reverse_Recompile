# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/gamblercon.pyc
# RelativePath: clientlogic/cl_container/gamblercon.pyc
# Source Generated with Decompyle++
# File: gamblercon.pyc (Python 3.6)

from cl_object.logging import WarobjLog
from cl_only import WeakProxy, ChooseKey, ChooseKey
from cl_cscommondef import QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, QUALITY_TYPE_HIGH, QUALITY_TYPE_CURSE, PF_SUBMSG_THROW, ALL_QUALITY_DESORDER
from cl_commondefines import GAMBLER_CHOOSE_LAST, GAMBLER_CHOOSE_EQUITY, GAMBLER_REPLACE_DEFAULT, GAMBLER_REPLACE_LEAST, GAMBLER_REPLACE_LOWEST, SKILLCACHE_INT, UPGRADE_RELIC_TYPE_LOW, UPGRADE_RELIC_TYPE_NORMAL, UPGRADE_RELIC_TYPE_HIGH
import cl_snetwar
import cl_msgcenter
import cl_action
import math
g_Quality2Comb = {
    QUALITY_TYPE_HIGH: 4,
    QUALITY_TYPE_NORMAL: 3,
    QUALITY_TYPE_LOW: 2 }
g_Comb2Quality = {
    2: QUALITY_TYPE_LOW,
    3: QUALITY_TYPE_NORMAL,
    4: QUALITY_TYPE_HIGH }
GAMBLER_PRE_CAREER = 12007
GAMBLER_CAREER = 1317
GAMBLER_THROW = 1424
LOW_PROB_STATE = 32748
NORMAL_PROB_STATE = 32749
HIGH_PROB_STATE = 32750
g_ShowProbState = {
    QUALITY_TYPE_HIGH: HIGH_PROB_STATE,
    QUALITY_TYPE_NORMAL: NORMAL_PROB_STATE,
    QUALITY_TYPE_LOW: LOW_PROB_STATE }

class CGamblerContainer(object):
    
    def __init__(self, oGame, oWarrior):
        self.m_Game = oGame
        self.m_WarriorObj = WeakProxy(oWarrior)
        self.m_QualityList = []
        self.m_GrooveNum = 3
        self.m_ReplceRule = GAMBLER_REPLACE_DEFAULT
        self.m_Prob = 0
        self.m_Mix2LowProb = 0
        self.m_QualityProb = { 0: iQuality for iQuality in ALL_QUALITY_DESORDER }
        self.InitEvent()
        self.m_QualityID = { 1: iID for iID in range(20) }
        self.m_UpgradeRelicType = UPGRADE_RELIC_TYPE_NORMAL
        self.m_SignReilc = []

    
    def InitEvent(self):
        cl_msgcenter.AddFunction(self.m_WarriorObj, cl_msgcenter.MSG_WAR_PERFORM_START, self.OnThrowPfStart, 'CGamblerContainer', PF_SUBMSG_THROW, iOnce = 0, iPriority = -1)
        cl_msgcenter.AddFunction(self.m_WarriorObj, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, self.OnAddRelicPerform, 'CGamblerContainer', iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarriorObj, cl_msgcenter.MSG_WAR_REMOVERELIC, self.OnRemoveRelic, 'CGamblerContainer', iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarriorObj, cl_msgcenter.MSG_WAR_CHANGE_RELIC_SHOWQUALITY, self.OnChangeRelicShowQuality, 'CGamblerContainer', iOnce = 0)
        cl_msgcenter.AddFunction(self.m_WarriorObj, cl_msgcenter.MSG_WAR_PLAYERLOGIN, self.OnPlayerLogin, 'CGamblerContainer', iOnce = 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarriorObj, cl_msgcenter.MSG_WAR_PERFORM_START, 'CGamblerContainer', PF_SUBMSG_THROW)
        cl_msgcenter.DoneEvent(self.m_WarriorObj, cl_msgcenter.MSG_WAR_ADDRELICPERFORM, 'CGamblerContainer')
        cl_msgcenter.DoneEvent(self.m_WarriorObj, cl_msgcenter.MSG_WAR_REMOVERELIC, 'CGamblerContainer')
        cl_msgcenter.DoneEvent(self.m_WarriorObj, cl_msgcenter.MSG_WAR_CHANGE_RELIC_SHOWQUALITY, 'CGamblerContainer')
        cl_msgcenter.DoneEvent(self.m_WarriorObj, cl_msgcenter.MSG_WAR_PLAYERLOGIN, 'CGamblerContainer')
        self.m_WarriorObj = None
        self.m_Game = None

    
    def Save(self):
        dData = {
            'UpgradeRelicType': self.m_UpgradeRelicType,
            'SignReilc': self.m_SignReilc }
        return dData

    
    def Load(self, dData):
        iUpgradeRelicType = dData.get('UpgradeRelicType', 0)
        if iUpgradeRelicType:
            self.m_UpgradeRelicType = iUpgradeRelicType
        self.m_SignReilc = dData.get('SignReilc', [])

    
    def OnPlayerLogin(self, oTarget, dInfo):
        self.RefreshUpgradeRelic()
        self.UpdateSignRelic()

    
    def StartCareerPF(self, oSkill):
        iEmptyGroove = self.m_GrooveNum - len(self.m_QualityList)
        dInfo = {
            'pfid': GAMBLER_CAREER,
            'Comb': 0,
            'OldQuality': list(self.m_QualityList) }
        if not self.IsFull():
            self.FullQuality()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CUSTOM_USEPERFORM_BEFORE, self.m_WarriorObj, dInfo)
        iComb = dInfo['Comb'] if dInfo['Comb'] else self.GetComb()
        iDamFactor = dInfo['DamFactor'] if 'DamFactor' in dInfo else 0
        self.UseCareerPF(oSkill, iComb, iEmptyGroove, iDamFactor)

    
    def OnThrowPfStart(self, oHero, dMsgInfo):
        oSkill = dMsgInfo['Skill']
        if not oSkill.m_Base['pfid'] == GAMBLER_THROW:
            return None
        if 'ForbidAppendQuality' in oSkill.m_Collect:
            oSkill.m_Collect['Quality'] = 0
            return None
        iNum = oSkill.m_Collect['QualityNum'] if 'QualityNum' in oSkill.m_Collect else 1
        iQuality = cl_action.GetSkillCacheData(oSkill, SKILLCACHE_INT)
        iQuality = self.TryAppendQuality(iQuality, GAMBLER_CHOOSE_LAST, True, iNum)
        oSkill.m_Collect['Quality'] = iQuality

    
    def OnPopQuality(self, iID):
        if iID in self.m_QualityID:
            self.m_QualityID[iID] = 1

    
    def TryAppendQuality(self, iAssignQuality, iChooseType, iFundamental, iNum = 1, iReplaceRule = 0):
        iQuality = self.TryAppendQualityNoRefresh(iAssignQuality, iChooseType, iFundamental, iNum, iReplaceRule)
        self.Refresh()
        self.UpdateShowProb()
        return iQuality

    
    def TryAppendQualityNoRefresh(self, iAssignQuality, iChooseType, iFundamental, iNum = 1, iReplaceRule = 0):
        iQuality = iAssignQuality if iAssignQuality else self.ChooseQuality(iChooseType, iFundamental)
        if not iQuality:
            return 0
        lstOldID = []
        for _ in range(iNum):
            iID = ChooseKey(self.m_Game, self.m_QualityID)
            self.m_QualityID[iID] = 0
            (bReplce, idx) = self.TryReplce(iReplaceRule)
            if not bReplce:
                self.m_QualityList.append((iID, iQuality))
            elif iReplaceRule:
                (iOldSID, _) = self.m_QualityList[idx]
                self.OnPopQuality(iOldSID)
                self.m_QualityList[idx] = (iID, iQuality)
            else:
                (iOldID, _) = self.m_QualityList.pop(idx)
                lstOldID.append(iOldID)
                self.m_QualityList.append((iID, iQuality))
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_GET_QUALITY, self.m_WarriorObj, {
                'Quality': iQuality })
            if not bReplce and len(self.m_QualityList) == self.m_GrooveNum:
                iComb = self.GetComb()
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_GET_COMB, self.m_WarriorObj, {
                    'Comb': iComb })
        
        for iOldID in lstOldID:
            self.OnPopQuality(iOldID)
        
        return iQuality

    
    def UpQuality(self, iQuality):
        if iQuality <= QUALITY_TYPE_NORMAL:
            iQuality *= 2
        return iQuality

    
    def GetMinQuality(self):
        if len(self.m_QualityList) <= 0:
            return QUALITY_TYPE_LOW
        iMinQuality = 0
        for _, iQuality in self.m_QualityList:
            if not not iMinQuality:
                if iQuality < iMinQuality:
                    iMinQuality = iQuality
                    continue
        
        return iMinQuality

    
    def GetMinNumQuality(self):
        if len(self.m_QualityList) <= 0:
            return QUALITY_TYPE_LOW
        dQuality = { }
        for _, iQuality in self.m_QualityList:
            dQuality[iQuality] = dQuality.get(iQuality, 0) + 1
        
        iMinNum = 0
        iMinQuality = 0
        for iQuality, iNum in dQuality.items():
            if not iMinQuality:
                iMinQuality = iQuality
                iMinNum = iNum
            if iNum < iMinNum:
                iMinQuality = iQuality
                iMinNum = iNum
                continue
            if iNum == iMinNum and iQuality < iMinQuality:
                iMinQuality = iQuality
                iMinNum = iNum
        
        return iMinQuality

    
    def TryReplce(self, iReplceRule):
        idx = 0
        if len(self.m_QualityList) >= self.m_GrooveNum:
            idx = self.GetReplaceIdx(iReplceRule)
            (_, iQuality) = self.m_QualityList[idx]
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_REPLACE_QUALITY, self.m_WarriorObj, {
                'Quality': iQuality })
            return (True, idx)
        return (False, idx)

    
    def GetReplaceIdx(self, iReplceRule):
        iResult = 0
        iExpectQuality = 0
        if iReplceRule == GAMBLER_REPLACE_LEAST:
            iExpectQuality = self.GetMinNumQuality()
        elif iReplceRule == GAMBLER_REPLACE_LOWEST:
            iExpectQuality = self.GetMinQuality()
        if iExpectQuality:
            for idx, (_, iQuality) in enumerate(self.m_QualityList):
                if iExpectQuality == iQuality:
                    iResult = idx
                    break
            
        return iResult

    
    def ChooseQuality(self, iChooseType, iFundamental):
        iTargetQuality = self.GetProbPlus(iChooseType)
        dQulityChoose = { iProb: iQuality for iQuality, iProb in self.m_QualityProb.items() if iQuality >= iTargetQuality }
        dFinalChoose = {
            QUALITY_TYPE_CURSE: self.m_QualityProb[QUALITY_TYPE_CURSE] }
        iQuality = ChooseKey(self.m_Game, dQulityChoose)
        if not iQuality:
            return 0
        dFinalChoose[iQuality] = self.m_QualityProb[iQuality]
        iQuality = ChooseKey(self.m_Game, dFinalChoose)
        if not iQuality and iFundamental:
            iQuality = QUALITY_TYPE_LOW
        return iQuality

    
    def UseCareerPF(self, oSkill, iComb, iEmptyGroove, iDamFactor):
        (x, y, z) = oSkill.m_Collect['End']
        iTargetID = oSkill.m_Collect['TargetID']
        dArgs = {
            'Comb': iComb,
            'x': int(x * 100),
            'y': int(y * 100),
            'z': int(z * 100),
            'EmptyGroove': iEmptyGroove,
            'TargetID': iTargetID,
            'DamFactor': iDamFactor }
        oPerform = self.m_WarriorObj.GetPerform(GAMBLER_CAREER, 0)
        cl_snetwar.GS2CNotifyStartSkill(self.m_Game, self.m_WarriorObj.m_PlayerID, GAMBLER_CAREER, oPerform.m_ID, 0, dArgs)

    
    def IsFull(self):
        return len(self.m_QualityList) >= self.m_GrooveNum

    
    def ClearAllQuality(self, iAssignComb = 0, iSkillClearFlag = 0, sReason = ''):
        iLen = len(self.m_QualityList)
        iComb = iAssignComb if iAssignComb else self.GetComb()
        dInfo = {
            'Comb': iComb }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_ALLGROOVE, self.m_WarriorObj, dInfo)
        sReason += 'ClearAll'
        for _ in range(iLen):
            self.ClearQuality(0, sReason)
        
        self.UpdateShowProb()
        if iLen > 0:
            self.Refresh(iSkillClearFlag)

    
    def ClearQuality(self, idx, sReason = ''):
        (iSID, iQuality) = self.m_QualityList.pop(idx)
        self.OnPopQuality(iSID)
        iEmpty = 1 if not self.m_QualityList else 0
        dInfo = {
            'Quality': iQuality,
            'Reason': sReason,
            'Empty': iEmpty }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_CLEAR_GROOVE, self.m_WarriorObj, dInfo)

    
    def ClearLastGroove(self):
        if not self.m_QualityList:
            return None
        self.ClearQuality(-1)
        self.Refresh()
        self.UpdateShowProb()

    
    def RandomClearGroove(self, iAssignQuality):
        lstIdx = []
        for idx, (_, iQuality) in enumerate(self.m_QualityList):
            if iAssignQuality and iAssignQuality != iQuality:
                continue
            lstIdx.append(idx)
        
        if lstIdx:
            iRandomIdx = lstIdx[self.m_Game.Random(len(lstIdx))]
            self.ClearQuality(iRandomIdx)
            self.Refresh()
            self.UpdateShowProb()

    
    def FullQuality(self):
        iLen = len(self.m_QualityList)
        if iLen >= self.m_GrooveNum:
            return None
        iAdd = self.m_GrooveNum - iLen
        for _ in range(iAdd):
            self.TryAppendQualityNoRefresh(0, GAMBLER_CHOOSE_EQUITY, True)
        
        self.Refresh()
        self.UpdateShowProb()

    
    def GetComb(self):
        iComb = 0
        lstQuality = []
        (iCurseBelong, _, _) = self.GetCurseBelong()
        for _, iQuality in self.m_QualityList:
            if iQuality == QUALITY_TYPE_CURSE:
                iQuality = iCurseBelong
            if iQuality in lstQuality:
                continue
            lstQuality.append(iQuality)
        
        if not lstQuality or len(lstQuality) > 1:
            iComb = 1
        else:
            iQuality = lstQuality[0]
            iComb = g_Quality2Comb[iQuality]
        return iComb

    
    def AddQualityProb(self, iQuality, iAddProb):
        if iQuality not in self.m_QualityProb:
            return None
        iProb = self.m_QualityProb[iQuality] + iAddProb
        self.m_QualityProb[iQuality] = max(iProb, 0)
        self.UpdateShowProb()

    
    def Refresh(self, iSkillClearFlag = 0):
        cl_snetwar.GS2CUpdateQuality(self.m_WarriorObj.m_PlayerID, self.m_GrooveNum, self.m_QualityList, iSkillClearFlag)

    
    def RefreshProb(self):
        lstQualityProb = []
        for iQuality, iProb in self.m_QualityProb.items():
            iProb = iProb // 10000
            lstQualityProb.append((iQuality, iProb))
        
        cl_snetwar.GS2CUpdateQualityProb(self.m_WarriorObj.m_PlayerID, lstQualityProb)

    
    def GetProbPlus(self, iChooseType):
        if not (self.m_QualityList) or iChooseType != GAMBLER_CHOOSE_LAST:
            return 0
        for _, iQuality in self.m_QualityList[::-1]:
            if iQuality != QUALITY_TYPE_CURSE:
                return iQuality
        
        return 0

    
    def GetCurseBelong(self):
        dRelicQualityCnt = {
            QUALITY_TYPE_HIGH: 0,
            QUALITY_TYPE_NORMAL: 0,
            QUALITY_TYPE_LOW: 0 }
        iCurseCnt = 0
        for _, iQuality in self.m_QualityList:
            if iQuality == QUALITY_TYPE_CURSE:
                iCurseCnt += 1
                continue
            dRelicQualityCnt[iQuality] = dRelicQualityCnt[iQuality] + 1
        
        iRelicQualityMaxCnt = -1
        iCurseBelong = -1
        for iQuality, iCnt in dRelicQualityCnt.items():
            if iCnt >= iRelicQualityMaxCnt and iQuality > iCurseBelong:
                iRelicQualityMaxCnt = iCnt
                iCurseBelong = iQuality
        
        return (iCurseBelong, iRelicQualityMaxCnt, iCurseCnt)

    
    def SetProb(self, iProb):
        self.m_Prob = iProb

    
    def ModifyGrooveNum(self, iModify):
        self.m_GrooveNum += iModify
        if self.m_GrooveNum < 1:
            self.m_GrooveNum = 1
        iExtraNum = len(self.m_QualityList) - self.m_GrooveNum
        if iExtraNum > 0:
            for _ in range(iExtraNum):
                self.ClearQuality(-1)
            
        self.Refresh()
        self.UpdateShowProb()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GAMBLER_MODIFY_GROOVENUM, self.m_WarriorObj, {
            'GrooveNum': self.m_GrooveNum })

    
    def SetReplaceRule(self, iRule):
        if self.m_ReplceRule != GAMBLER_REPLACE_DEFAULT:
            return None
        self.m_ReplceRule = iRule

    
    def ResetReplaceRule(self):
        self.m_ReplceRule = GAMBLER_REPLACE_DEFAULT

    
    def GetAvailableQualityNum(self, iAssignQuality):
        iNum = 0
        lstExisted = [ tInfo[0] for tInfo in self.m_QualityList ]
        oRelicCon = self.m_WarriorObj.m_RelicCon
        for oRelic in oRelicCon.m_Perform.values():
            if oRelic.m_SID in lstExisted:
                continue
            iShowQuality = oRelicCon.GetShowQuality(oRelic.m_SID)
            if iShowQuality == QUALITY_TYPE_CURSE:
                iNum += 1
                continue
            if iAssignQuality or iShowQuality == iAssignQuality:
                iNum += 1
                continue
            iNum += 1
        
        return iNum

    
    def HasQualityNum(self, iAssignQuality):
        iNum = 0
        for _, iQuality in self.m_QualityList:
            if iAssignQuality and iAssignQuality != iQuality:
                continue
            iNum += 1
        
        return iNum

    
    def OnChangeRelicShowQuality(self, oHero, dInfo):
        iSID = dInfo['iPerform']
        iOldQuality = dInfo['OldQuality']
        iShowQuality = oHero.m_RelicCon.GetShowQuality(iSID)
        self.m_QualityProb[iOldQuality] -= 10000
        self.m_QualityProb[iShowQuality] += 10000
        self.UpdateShowProb()

    
    def OnAddRelicPerform(self, oHero, dInfo):
        iSID = dInfo['iPerform']
        iShowQuality = oHero.m_RelicCon.GetShowQuality(iSID)
        self.m_QualityProb[iShowQuality] += 10000
        self.UpdateShowProb()
        self.RefreshUpgradeRelic()

    
    def OnRemoveRelic(self, oHero, dInfo):
        iShowQuality = dInfo['ShowQuality']
        self.m_QualityProb[iShowQuality] -= 10000
        self.UpdateShowProb()
        self.RefreshUpgradeRelic()

    
    def GetQualityTrueProb(self, iQuality):
        iQualityProb = self.m_QualityProb[iQuality]
        if not iQualityProb:
            return 0
        if iQuality == QUALITY_TYPE_CURSE:
            iLowProb = self.m_QualityProb[QUALITY_TYPE_LOW]
            iNorMalProb = self.m_QualityProb[QUALITY_TYPE_NORMAL]
            iHightProb = self.m_QualityProb[QUALITY_TYPE_HIGH]
            if iLowProb + iNorMalProb + iHightProb == 0:
                return 0
            iCurseProb = iQualityProb
            return (iCurseProb / (iLowProb + iNorMalProb + iHightProb)) * (iLowProb / (iLowProb + iCurseProb) + iNorMalProb / (iNorMalProb + iCurseProb) + iHightProb / (iHightProb + iCurseProb))
        iCurseProb = self.m_QualityProb[QUALITY_TYPE_CURSE]
        iFirstProb = iQualityProb / (self.m_QualityProb[QUALITY_TYPE_LOW] + self.m_QualityProb[QUALITY_TYPE_NORMAL] + self.m_QualityProb[QUALITY_TYPE_HIGH])
        iFinalProb = iQualityProb / (iQualityProb + iCurseProb)
        return iFirstProb * iFinalProb

    
    def UpdateShowProb(self):
        dCombProb = {
            QUALITY_TYPE_HIGH: 0,
            QUALITY_TYPE_NORMAL: 0,
            QUALITY_TYPE_LOW: 0 }
        lstQuality = []
        for _, iQuality in self.m_QualityList:
            if iQuality == QUALITY_TYPE_CURSE or iQuality in lstQuality:
                continue
            lstQuality.append(iQuality)
        
        if len(lstQuality) > 1:
            for iComb, iProb in dCombProb.items():
                self.SetShowProb(iComb, iProb)
            
            return None
        iEmptyGroove = self.m_GrooveNum - len(self.m_QualityList)
        iCurseProb = self.GetQualityTrueProb(QUALITY_TYPE_CURSE)
        if len(lstQuality) == 1:
            iQuality = lstQuality[0]
            iQualityProb = self.GetQualityTrueProb(iQuality)
            iCombProb = (iQualityProb + iCurseProb) ** iEmptyGroove
            dCombProb[iQuality] = iCombProb
        else:
            iLowProb = self.GetQualityTrueProb(QUALITY_TYPE_LOW)
            iNorMalProb = self.GetQualityTrueProb(QUALITY_TYPE_NORMAL)
            iHightProb = self.GetQualityTrueProb(QUALITY_TYPE_HIGH)
            dCombProb[QUALITY_TYPE_LOW] = (iLowProb + iCurseProb) ** iEmptyGroove - iCurseProb ** iEmptyGroove
            dCombProb[QUALITY_TYPE_NORMAL] = (iNorMalProb + iCurseProb) ** iEmptyGroove - iCurseProb ** iEmptyGroove
            dCombProb[QUALITY_TYPE_HIGH] = (iHightProb + iCurseProb) ** iEmptyGroove
        for iComb, iProb in dCombProb.items():
            self.SetShowProb(iComb, math.ceil(iProb * 100))
        

    
    def SetShowProb(self, iComb, iProb):
        iStateSID = g_ShowProbState[iComb]
        oState = self.m_WarriorObj.m_State.GetItemBySID(iStateSID)
        if oState:
            oState.SetCount(self.m_WarriorObj, iProb)

    
    def SetMix2LowProb(self, iProb):
        if iProb and self.m_Mix2LowProb:
            return None
        self.m_Mix2LowProb = iProb

    
    def SetUpgradeRelicType(self, iType):
        if iType == self.m_UpgradeRelicType:
            return None
        self.m_UpgradeRelicType = iType
        self.RefreshUpgradeRelic()

    
    def RefreshUpgradeRelic(self):
        iUpgradeCnt = self.m_WarriorObj.GetUpgradeRelicCnt()
        oRelicCon = self.m_WarriorObj.m_RelicCon
        dOldShowQuality = dict(oRelicCon.m_ShowQuality)
        oRelicCon.m_ShowQuality = { }
        for iRelicSID in dOldShowQuality:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGE_RELIC_SHOWQUALITY, self.m_WarriorObj, {
                'OldQuality': dOldShowQuality[iRelicSID],
                'iPerform': iRelicSID })
        
        if self.m_UpgradeRelicType == UPGRADE_RELIC_TYPE_LOW:
            iUpgradeCnt = self.UpGradeRelicToNext(QUALITY_TYPE_LOW, iUpgradeCnt)
        elif self.m_UpgradeRelicType == UPGRADE_RELIC_TYPE_NORMAL:
            iUpgradeCnt = self.UpGradeRelicToNext(QUALITY_TYPE_LOW, iUpgradeCnt)
            if iUpgradeCnt:
                iUpgradeCnt = self.UpGradeRelicToNext(QUALITY_TYPE_NORMAL, iUpgradeCnt)
            elif self.m_UpgradeRelicType == UPGRADE_RELIC_TYPE_HIGH:
                iUpgradeCnt = self.UpGradeRelicToNext(QUALITY_TYPE_NORMAL, iUpgradeCnt)
                if iUpgradeCnt:
                    iUpgradeCnt = self.UpGradeRelicToHight(iUpgradeCnt)
        None.m_WarriorObj.Set('RemainUpgradeCnt', iUpgradeCnt)
        oRelicCon.GS2CUpdateShowQuality(oRelicCon.m_ShowQuality, iUpgradeCnt, self.m_UpgradeRelicType)
        self.RefreshProb()

    
    def UpGradeRelicToNext(self, iQuality, iUpgradeCnt):
        oRelicCon = self.m_WarriorObj.m_RelicCon
        for iRelic in oRelicCon.GetAllRelicSID():
            if iUpgradeCnt <= 0:
                return 0
            if oRelicCon.GetShowQuality(iRelic) == iQuality:
                oRelicCon.SetShowQuality(iRelic, iQuality * 2)
                iUpgradeCnt -= 1
        
        return iUpgradeCnt

    
    def UpGradeRelicToHight(self, iUpgradeCnt):
        oRelicCon = self.m_WarriorObj.m_RelicCon
        for iRelic in oRelicCon.GetAllRelicSID():
            if iUpgradeCnt <= 0:
                return 0
            iShowQuality = oRelicCon.GetShowQuality(iRelic)
            for _ in range(iUpgradeCnt):
                if iShowQuality >= QUALITY_TYPE_HIGH:
                    break
                iShowQuality *= 2
                iUpgradeCnt -= 1
                oRelicCon.SetShowQuality(iRelic, iShowQuality)
            
        
        return iUpgradeCnt

    
    def GetCurCombQuality(self):
        if len(self.m_QualityList) < self.m_GrooveNum:
            return 0
        iComb = self.GetComb()
        if iComb in g_Comb2Quality:
            return g_Comb2Quality[iComb]
        return 0

    
    def GetQualityByMaxProb(self):
        iResultQuality = 0
        iMaxProb = 0
        for iQuality, iProb in self.m_QualityProb.items():
            if iMaxProb > iProb:
                continue
            iMaxProb = iProb
            iResultQuality = iQuality
        
        return iResultQuality

    
    def SignRelic(self, iRelic, iSign):
        if iSign or iRelic not in self.m_SignReilc:
            self.m_SignReilc.append(iRelic)
        elif iRelic in self.m_SignReilc:
            self.m_SignReilc.remove(iRelic)

    
    def UpdateSignRelic(self):
        cl_snetwar.GS2CUpdateSignRelic(self.m_WarriorObj.m_PlayerID, self.m_SignReilc)


