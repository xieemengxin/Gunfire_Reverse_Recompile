# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/talentcon.pyc
# RelativePath: clientlogic/cl_container/talentcon.pyc
# Source Generated with Decompyle++
# File: talentcon.pyc (Python 3.6)

from cl_commondefines import BAG_TYPE_TALENT, PF_TYPE_TALENT, TALENT_PRIORITY_NONE, TALENT_PRIORITY_MAX, TALENT_PRIORITY_MIN, NPC_CB_DICT, VIRTUAL_ITEM_TALENT
from cl_object.logging import WartalentLog
from cl_only import Functor, DeepCopy
import cl_container
import cl_container.performcon
import cl_msgcenter
import cl_reward
import cl_perform.load
import cl_npc.net
import cl_duonet.dn_cl_container_talentcon as talentnet

def GS2CAddTalent(oGame, iHero, iTalentSID, iBasicLevel, iMaxLevel, sSubDesc, dPlayer):
    if not dPlayer:
        dPlayer = oGame.GetRealPlayers()
    netData = {
        'iTalentSID': iTalentSID,
        'iBasicLevel': iBasicLevel,
        'iMaxLevel': iMaxLevel,
        'sSubDesc': sSubDesc,
        'iHero': iHero,
        'oGame': oGame,
        'dPlayer': dPlayer }
    talentnet.DN_GS2CAddTalent(netData)


def GS2CSendRewardSID(oGame, iHero, iRewardSID):
    dPlayer = oGame.GetRealPlayers()
    netData = {
        'iHero': iHero,
        'iRewardSID': iRewardSID,
        'oGame': oGame,
        'dPlayer': dPlayer }
    talentnet.DN_GS2CSendRewardSID(netData)


def GS2CRemoveTalent(oGame, iHero, iTalentSID):
    dPlayer = oGame.GetRealPlayers()
    netData = {
        'iTalentSID': iTalentSID,
        'iHero': iHero,
        'oGame': oGame,
        'dPlayer': dPlayer }
    talentnet.DN_GS2CRemoveTalent(netData)


def GS2CChooseChangeTalentLevel(oHero):
    oHero.IncMenuIdx()
    netData = {
        'iMenuIdx': oHero.m_NpcUIMenuIdx,
        'pid': oHero.m_PlayerID }
    talentnet.DN_GS2CChooseChangeTalentLevel(netData)


def GS2CBanTalentResult(pid, lstTalent):
    netData = {
        'lstTalent': lstTalent,
        'pid': pid }
    talentnet.DN_GS2CBanTalentResult(netData)


def GS2CDisableTalentResult(pid, lstTalent):
    netData = {
        'lstTalent': lstTalent,
        'pid': pid }
    talentnet.DN_GS2CDisableTalentResult(netData)


def C2GSDisableTalent(who, lstTalent):
    oTalentCon = who.m_TalentCon
    oTalentCon.DisableTalent('CommonDisable', lstTalent)


class CTalentContainer(cl_container.performcon.CPerformContainer):
    m_BagType = BAG_TYPE_TALENT
    m_DisableKey = 'DisableTalent'
    
    def __init__(self, oWarrior):
        super(CTalentContainer, self).__init__(oWarrior)
        self.m_TalentTypeInfo = { }
        self.m_BanTalentInfo = { }
        self.m_CommonTalentInfo = { }
        self.m_DisableTalentInfo = { }

    
    def Load(self, dData):
        super(CTalentContainer, self).Load(dData)
        if 'DIS' in dData:
            self.m_DisableTalentInfo = dData['DIS']
        for iSID, iLevel in dData['PF'].items():
            self.AddTalent(iSID, iLevel, 'load')
        
        if 'BAN' in dData:
            self.m_BanTalentInfo = dData['BAN']
        if 'COM' in dData:
            self.m_CommonTalentInfo = dData['COM']

    
    def Save(self):
        dData = super(CTalentContainer, self).Save()
        dData['BAN'] = DeepCopy(self.m_BanTalentInfo)
        dData['COM'] = DeepCopy(self.m_CommonTalentInfo)
        dData['DIS'] = DeepCopy(self.m_DisableTalentInfo)
        return dData

    
    def Refresh(self, dPlayer = None):
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            self.GS2CAddTalent(oPerform, dPlayer)
        
        oHero = self.m_Game.GetObject(self.m_Owner)
        iRewardSID = oHero.QuerySavedData('RandomRewardFlag', 0)
        if iRewardSID:
            self.SendRewardSID(iRewardSID)
        self.SendCommonTalent()
        self.SendBanTalent()
        self.SendDisableTalent()
        super(CTalentContainer, self).Refresh(dPlayer)

    
    def RemoveTalent(self, iTalent, sReason = None):
        oTalent = self.GetPerform(iTalent)
        if not oTalent:
            WartalentLog.Alert('%d %d remove talent error id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, sReason))
            return False
        WartalentLog.Info('%d %d removetalent %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, sReason))
        self.UpdateTalentType(oTalent.m_TalentType, -(oTalent.m_Level))
        oOwner = self.m_Game.GetObject(self.m_Owner)
        iCurLevel = oTalent.m_Level
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVETALENT, oOwner, {
            'iPerform': iTalent,
            'Level': 0,
            'CurLevel': iCurLevel,
            'Reason': sReason })
        self.RemoveDisableTalent(iTalent, sReason)
        self.RemovePerform(oOwner, iTalent)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, oOwner, {
            'iPerform': iTalent,
            'CurLevel': iCurLevel })
        self.GS2CRemoveTalent(iTalent)
        return True

    
    def RemoveAllTalent(self, sReason = None):
        lstRemoveTalent = []
        for iPerformSID, oPerform in self.m_Perform.items():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            lstRemoveTalent.append(iPerformSID)
        
        for iTalent in lstRemoveTalent:
            self.RemoveTalent(iTalent, sReason)
        

    
    def AddTalent(self, iTalent, iLevel, sReason, dExtInfo = None):
        iPFType = cl_perform.GetPerformClassAttr(iTalent, 'm_PFType')
        if iPFType != PF_TYPE_TALENT:
            return None
        oCurTalent = self.GetPerform(iTalent)
        iCurLevel = oCurTalent.m_Level if oCurTalent else 0
        if iLevel >= iCurLevel and self.CheckTalentIsBan(iTalent):
            WartalentLog.Alert('%d %d addtalent error %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, iLevel, sReason))
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        WartalentLog.Info('%d %d addtalent %d %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, iLevel, sReason))
        dDisableTalent = self.GetAllDisableTalent()
        iEnable = 1 if iTalent not in dDisableTalent else 0
        oTalent = self.AddPerform(oOwner, iTalent, iLevel, iEnable, 0)
        if not oTalent:
            return None
        dInfo = {
            'iPerform': iTalent,
            'Level': oTalent.m_Level,
            'CurLevel': iCurLevel,
            'Reason': sReason }
        if dExtInfo and 'NpcID' in dExtInfo:
            dInfo['NpcID'] = dExtInfo['NpcID']
            oNpc = self.m_Game.GetObject(dInfo['NpcID'])
            if oNpc:
                dInfo['DropReason'] = oNpc.GetCreateSource()
        self.UpdateTalentType(oTalent.m_TalentType, iLevel - iCurLevel)
        if iTalent in dDisableTalent:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DISABLETALENT_CHANGED, oOwner, { })
        self.GS2CAddTalent(oTalent)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADDTALENT, oOwner, dInfo)
        return oTalent

    
    def DeGradeTalent(self, iTalent, iDeGrade, sReason):
        if iDeGrade <= 0:
            WartalentLog.Alert('%d %d degrade: %d <= 0 id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iDeGrade, iTalent, sReason))
            return False
        oTalent = self.GetPerform(iTalent)
        if not oTalent or oTalent.m_PFType != PF_TYPE_TALENT:
            WartalentLog.Alert('%d %d degrade talent error id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, sReason))
            return False
        iLevel = oTalent.m_Level
        if iLevel < iDeGrade:
            WartalentLog.Alert('%d %d degrade: %d > curlevel:%d id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iDeGrade, iLevel, iTalent, sReason))
            iDeGrade = iLevel
        if iLevel == iDeGrade:
            return self.RemoveTalent(iTalent, sReason)
        oTalent = self.AddTalent(iTalent, iLevel - iDeGrade, sReason)
        if not oTalent:
            return False
        return True

    
    def UpgradeTalent(self, iTalent, iUpgrade, sReason):
        if iUpgrade <= 0:
            WartalentLog.Alert('%d %d upgrade: %d <= 0 id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iUpgrade, iTalent, sReason))
            return None
        if not self.CheckTalentCanUpgrade(iTalent, sReason = sReason, iLog = 1):
            return None
        oTalent = self.GetPerform(iTalent)
        iLevel = oTalent.m_Level
        iMaxLevel = oTalent.m_MaxLevel
        iTargetLevel = iLevel + iUpgrade
        if iTargetLevel > iMaxLevel:
            iTargetLevel = iMaxLevel
        self.AddTalent(iTalent, iTargetLevel, sReason)

    
    def UpdateTalentType(self, iTalentType, iNum):
        if iTalentType not in self.m_TalentTypeInfo:
            self.m_TalentTypeInfo[iTalentType] = iNum
        else:
            self.m_TalentTypeInfo[iTalentType] += iNum

    
    def GS2CAddTalent(self, oTalent, dPlayer = None):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        iTalentSID = oTalent.m_SID
        iLevel = oTalent.Level()
        iMaxLevel = oTalent.m_MaxLevel
        sSubDesc = oTalent.SubDesc(oOwner)
        GS2CAddTalent(self.m_Game, self.m_Owner, iTalentSID, iLevel, iMaxLevel, sSubDesc, dPlayer)

    
    def GS2CRemoveTalent(self, iTalentSID):
        GS2CRemoveTalent(self.m_Game, self.m_Owner, iTalentSID)

    
    def AllPerformEnable(self):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        iOpenDisableTalent = self.CheckOpenDisableTalent()
        dDisableTalent = self.GetAllDisableTalent()
        for oTalent in list(self.m_Perform.values()):
            if iOpenDisableTalent and oTalent.m_SID in dDisableTalent:
                continue
            if oTalent.m_Enable:
                continue
            oTalent.Enable(oOwner)
        

    
    def GetAllTalentLevel(self):
        dLevel = { }
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            dLevel[oPerform.m_SID] = oPerform.Level()
        
        return dLevel

    
    def GetAllTalentLevelSum(self):
        iSum = 0
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            iSum += oPerform.Level()
        
        return iSum

    
    def GetAllTalentSubDesc(self):
        dRet = { }
        oOwner = self.m_Game.GetObject(self.m_Owner)
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            sSubDesc = oPerform.SubDesc(oOwner)
            if sSubDesc != '\x00':
                dRet[oPerform.m_SID] = sSubDesc
        
        return dRet

    
    def GetAllTalentSID(self, iExcludeRareTalent = 0):
        lstTalent = []
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            if iExcludeRareTalent and oPerform.m_IsRareTalent:
                continue
            lstTalent.append(oPerform.m_SID)
        
        return lstTalent

    
    def GetAllTalentList(self):
        lstTalent = []
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            iSID = oPerform.m_SID
            for _ in range(oPerform.Level()):
                lstTalent.append(iSID)
            
        
        return lstTalent

    
    def GetTalentListByPriority(self, iPriorityType, iExcludeMaxLevel = 0, iExcludeOneLevel = 0, iExcludeBan = 0):
        lstTalent = []
        iMaxLevel = 1
        iMinLevel = 999
        dLevel = { }
        dBanTalent = self.GetAllBanTalent()
        for oPerform in self.m_Perform.values():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            iSID = oPerform.m_SID
            iLevel = oPerform.m_Level
            if iExcludeMaxLevel and iLevel == oPerform.m_MaxLevel:
                continue
            if iExcludeOneLevel and oPerform.m_MaxLevel == 1:
                continue
            if iExcludeBan and iSID in dBanTalent:
                continue
            if iPriorityType != TALENT_PRIORITY_NONE:
                dLevel.setdefault(iLevel, [])
                dLevel[iLevel].append(iSID)
                if iLevel > iMaxLevel:
                    iMaxLevel = iLevel
                if iLevel < iMinLevel:
                    iMinLevel = iLevel
                    continue
            lstTalent.append(iSID)
        
        if iPriorityType == TALENT_PRIORITY_MAX:
            lstTalent = dLevel.get(iMaxLevel, [])
        elif iPriorityType == TALENT_PRIORITY_MIN:
            lstTalent = dLevel.get(iMinLevel, [])
        return lstTalent

    
    def SendRewardSID(self, iRewardSID):
        GS2CSendRewardSID(self.m_Game, self.m_Owner, iRewardSID)

    
    def CheckHasAllTalent(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        dTalentLib = cl_perform.load.GetTalentLib().get(oHero.m_Career, { })
        dBanTalentInfo = self.GetAllBanTalent()
        for iTalent in dTalentLib:
            if iTalent in dBanTalentInfo:
                continue
            oTalent = self.GetPerform(iTalent)
            if not not oTalent:
                if oTalent.m_Level < oTalent.GetMaxUpgradeLevel():
                    return False
        
        dCommonTalent = self.GetAllCommonTalent()
        for iTalent in dCommonTalent:
            oTalent = self.GetPerform(iTalent)
            if not not oTalent:
                if oTalent.m_Level < oTalent.GetMaxUpgradeLevel():
                    return False
        
        return True

    
    def GetAllValidTalent(self, iUseLib, iExcludeCurTalent):
        dAll = { }
        oHero = self.m_Game.GetObject(self.m_Owner)
        dTalentLib = cl_perform.load.GetTalentLib().get(oHero.m_Career, { })
        if iUseLib:
            dAll.update(dTalentLib)
            dAll.update(self.GetAllCommonTalent())
        else:
            dAll = { 1: iTalnet for iTalnet in dTalentLib.keys() | self.GetAllCommonTalent().keys() }
        for iTalent in self.GetAllBanTalent():
            dAll.pop(iTalent)
        
        for oTalent in self.m_Perform.values():
            if oTalent.m_PFType != PF_TYPE_TALENT:
                continue
            if not iExcludeCurTalent:
                if oTalent.m_Level >= oTalent.m_MaxLevel:
                    dAll.pop(oTalent.m_SID, None)
                    continue
        
        return dAll

    
    def ChooseChangeTalentLevel(self, sReason):
        if not self.GetAllTalentSID() or self.CheckHasAllTalent():
            return None
        oHero = self.m_Game.GetObject(self.m_Owner)
        GS2CChooseChangeTalentLevel(oHero)
        cl_npc.net.SetNpcUICallBackFunction(oHero, NPC_CB_DICT, Functor(self.PlayerChooseChangeTalentLevel, sReason))

    
    def PlayerChooseChangeTalentLevel(self, sReason, oHero, dAnswer):
        oGame = self.m_Game
        iPlayerID = self.m_PlayerID
        WartalentLog.Info('%d %d  choose change level %s %s' % (oGame.m_ID, iPlayerID, sReason, dAnswer))
        if len(dAnswer) != 1:
            WartalentLog.Alert('%d %d choose change answer err' % (oGame.m_ID, iPlayerID))
            return None
        for iTalent in dAnswer:
            bRet = self.DeGradeTalent(iTalent, 1, sReason)
            if not bRet:
                return None
        
        dBanTalent = self.GetAllBanTalent()
        for iTalent in dAnswer.values():
            oTalent = self.GetPerform(iTalent)
            if oTalent:
                self.UpgradeTalent(iTalent, 1, sReason)
                continue
            iPFType = cl_perform.GetPerformClassAttr(iTalent, 'm_PFType')
            if iPFType != PF_TYPE_TALENT:
                WartalentLog.Alert('%d %d choose change talent err %d' % (oGame.m_ID, iPlayerID, iTalent))
                continue
            if iTalent in dBanTalent:
                WartalentLog.Alert('%d %d choose ban talent err %d' % (oGame.m_ID, iPlayerID, iTalent))
                continue
            dRealReward = {
                'item': VIRTUAL_ITEM_TALENT,
                'info': {
                    'sid': iTalent,
                    'amount': 1 } }
            cl_reward.RewardItem(oGame, oHero, [
                dRealReward], sReason, None)
        

    
    def GetCommonTalentWeight(self):
        dChooseWeight = { }
        dAllCommonTalent = self.GetAllCommonTalent()
        for iTalent, iWeight in dAllCommonTalent.items():
            oTalent = self.GetPerform(iTalent)
            if not not oTalent:
                if oTalent.m_Level < oTalent.m_MaxLevel:
                    dChooseWeight[iTalent] = iWeight
                    continue
        
        return dChooseWeight

    
    def GetAllCommonTalent(self):
        dInfo = { }
        for dTalent in self.m_CommonTalentInfo.values():
            dInfo.update(dTalent)
        
        return dInfo

    
    def GetCommonTalent(self, sReason):
        if sReason in self.m_CommonTalentInfo:
            return self.m_CommonTalentInfo[sReason]
        return { }

    
    def AddCommonTalent(self, sReason, dTalent):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        dCommonTalentLib = cl_perform.load.GetCommonTalentLib()
        iOwnerCareer = oOwner.m_Career
        dAllCommonTalent = { }
        for iCareer, dCommonTalent in dCommonTalentLib.items():
            if iCareer == iOwnerCareer:
                continue
            dAllCommonTalent.update(dCommonTalent)
        
        for iTalent in dTalent:
            if iTalent not in dAllCommonTalent:
                WartalentLog.Alert('%d %d addcommontalent err %d' % (self.m_Game.m_ID, self.m_PlayerID, iTalent))
                return False
        
        self.m_CommonTalentInfo[sReason] = dTalent
        self.SendCommonTalent()
        return True

    
    def SendCommonTalent(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        cl_npc.net.GS2CCommonTalentChosen(oHero, self.GetAllCommonTalent())

    
    def GetAllBanTalent(self):
        dInfo = { }
        for dTalent in self.m_BanTalentInfo.values():
            dInfo.update(dTalent)
        
        return dInfo

    
    def AddBanTalent(self, sReason, dTalent):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        dTalentLib = cl_perform.load.GetTalentLib().get(oOwner.m_Career, { })
        for iTalent in dTalent:
            if iTalent not in dTalentLib:
                WartalentLog.Alert('%d %d addbantalent err %d' % (self.m_Game.m_ID, self.m_PlayerID, iTalent))
                return False
        
        self.m_BanTalentInfo[sReason] = dTalent
        self.SendBanTalent()
        return True

    
    def GetBanTalent(self, sReason):
        if sReason in self.m_BanTalentInfo:
            return self.m_BanTalentInfo[sReason]
        return { }

    
    def ClearBanTalent(self, sReason):
        if sReason in self.m_BanTalentInfo:
            self.m_BanTalentInfo.pop(sReason)
            self.SendBanTalent()

    
    def SendBanTalent(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        GS2CBanTalentResult(oHero.m_PlayerID, self.GetAllBanTalent())

    
    def CheckOpenDisableTalent(self):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        return oOwner.Query(self.m_DisableKey, 0)

    
    def SwitchDisableTalent(self, iOpen, sReason):
        WartalentLog.Info('%d %d switch disable %s %s' % (self.m_Game.m_ID, self.m_PlayerID, iOpen, sReason))
        oOwner = self.m_Game.GetObject(self.m_Owner)
        sKey = self.m_DisableKey
        if iOpen:
            self.OpenTalentDisable()
        else:
            oOwner.Delete(sKey)
            self.ClearDisableTalent('CommonDisable')
        oOwner.GS2CPropChange(sKey)

    
    def GetAllDisableTalentLevelSum(self):
        iSum = 0
        dDisableTalent = self.GetAllDisableTalent()
        for iPerform in dDisableTalent:
            oPerform = self.GetPerform(iPerform)
            if not oPerform:
                continue
            iSum += oPerform.Level()
        
        return iSum

    
    def GetAllDisableTalent(self):
        if not self.CheckOpenDisableTalent():
            return { }
        dInfo = { }
        for dTalent in self.m_DisableTalentInfo.values():
            dInfo.update(dTalent)
        
        return dInfo

    
    def DisableTalent(self, sReason, lstTalent):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if not self.CheckOpenDisableTalent():
            WartalentLog.Alert('%d %d disable err %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason))
            return None
        OldDisableTalentSet = set(self.GetAllDisableTalent())
        dTalent = { }
        for iTalent in lstTalent:
            oPerform = self.GetPerform(iTalent)
            if not oPerform or oPerform.m_PFType != PF_TYPE_TALENT:
                WartalentLog.Alert('%d %d disable perform err %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent))
                return None
            dTalent[iTalent] = 1
        
        WartalentLog.Info('%d %d disable perform %s %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason, lstTalent))
        self.m_DisableTalentInfo[sReason] = dTalent
        DisableTalentSet = set(self.GetAllDisableTalent())
        EnableTalentSet = OldDisableTalentSet - DisableTalentSet
        for iTalent in EnableTalentSet:
            oPerform = self.GetPerform(iTalent)
            if oPerform.m_Enable:
                continue
            oPerform.Enable(oOwner)
        
        for iTalent in DisableTalentSet:
            oPerform = self.GetPerform(iTalent)
            if not oPerform.m_Enable:
                continue
            oPerform.Disable(oOwner)
        
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DISABLETALENT_CHANGED, oOwner, { })
        self.SendDisableTalent()

    
    def OpenTalentDisable(self):
        if self.CheckOpenDisableTalent():
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        oOwner.Set(self.m_DisableKey, 1)
        for iTalent in self.GetAllDisableTalent():
            oPerform = self.GetPerform(iTalent)
            if not oPerform.m_Enable:
                continue
            oPerform.Disable(oOwner)
        
        self.SendDisableTalent()

    
    def RemoveDisableTalent(self, iTalent, sReason):
        oPerform = self.GetPerform(iTalent)
        if not oPerform or oPerform.m_PFType != PF_TYPE_TALENT:
            WartalentLog.Alert('%d %d removedisable perform err %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent))
            return None
        WartalentLog.Info('%d %d removedisable %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, sReason))
        for dDisableTalent in self.m_DisableTalentInfo.values():
            dDisableTalent.pop(iTalent, None)
        
        oOwner = self.m_Game.GetObject(self.m_Owner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DISABLETALENT_CHANGED, oOwner, { })
        self.SendDisableTalent()

    
    def ClearDisableTalent(self, sReason):
        if sReason in self.m_DisableTalentInfo:
            WartalentLog.Info('%d %d cleardisable %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason))
            oOwner = self.m_Game.GetObject(self.m_Owner)
            for iTalent in self.m_DisableTalentInfo[sReason]:
                oPerform = self.GetPerform(iTalent)
                if oPerform.m_Enable:
                    continue
                oPerform.Enable(oOwner)
            
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DISABLETALENT_CHANGED, oOwner, { })
            self.SendDisableTalent()

    
    def SendDisableTalent(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        GS2CDisableTalentResult(oHero.m_PlayerID, self.GetAllDisableTalent())

    
    def CheckTalentCanUpgrade(self, iTalent, sReason = None, iLog = 0):
        if self.CheckTalentIsBan(iTalent):
            if iLog:
                WartalentLog.Alert('%d %d upgrade talent error talent is banned id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, sReason))
            return 0
        oTalent = self.GetPerform(iTalent)
        if not oTalent or oTalent.m_PFType != PF_TYPE_TALENT:
            if iLog:
                WartalentLog.Alert('%d %d upgrade talent error id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, sReason))
            return 0
        iLevel = oTalent.m_Level
        iMaxLevel = oTalent.m_MaxLevel
        if iLevel >= iMaxLevel:
            if iLog:
                WartalentLog.Alert('%d %d upgrade talent is maxlevel id: %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iTalent, sReason))
            return 0
        return 1

    
    def CheckTalentIsBan(self, iTalent):
        dBanTalent = self.GetAllBanTalent()
        if iTalent not in dBanTalent:
            return 0
        return 1


