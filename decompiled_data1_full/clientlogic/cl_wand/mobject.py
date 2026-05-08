# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wand/mobject.pyc
# RelativePath: clientlogic/cl_wand/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import Time2Frame, ChooseKey, DeepCopy
from cl_item.baseitem import CBaseItem
from cl_object.logging import WandLog
from cl_cscommondef import WAND_MASK
from cl_commondefines import WAND_COMP_TYPE_CONDITION, WAND_COMP_TYPE_ACTION, BASEATTR_REFRESH, WAND_SUBMSG_FINISHCONDITION, WAND_SUBMSG_TRIGGERACTION, WAND_SUBMSG_WANDCDEND, WANDCOMP_SUBMSG_ADD, WANDCOMP_SUBMSG_REMOVE, WAND_SUBMSG_UPGRADE, WANDCOMP_TRIGGER_ACTION, WAND_ACTCOMP_CONTINUE, WAND_SUBMSG_EXTACTIONSLOT, WAND_QUALITY_TALE, PF_TYPE_WANDABILITY, ABILITY_QUALITY_NEGATIVE, ABILITY_QUALITY_FOUR, ABILITY_QUALITY_THREE, WAND_POSFUNC_INVALIDPROB, WAND_SUBMSG_ADDABILITY, WAND_SUBMSG_REMOVEABILITY, WAND_SUBTYPE_COPY, WAND_SUBTYPE_NORMAL, UNLOCK_WANDABILITY_SEASONTALENT, PAIR_WAND
from cl_propdata import INFO_PROP_NAME
from cl_netattr import GetPropValue
from cl_platformdata import GetWandAbilityByQuality, GetWandPointAbility, GetGWandPointAbility, GetPWandPointAbility, GetWandExcludeAbility, GetWandCompIcon
import cl_wand
import cl_formula
import cl_msgcenter
import cl_object.reason
import cl_object.baseattr
import cl_object.lifecycle
import cl_msgcenter.eventcbobj
import cl_wand.net as wandnet
import cl_perform
import math
WAND_COMP_POS_NONE = -1
WAND_EMPTY_COMP = (0, 0)
WANDCOMP_NOTRIGGER_NEXTPOS = (2121,)
MAX_WANDABILITY_NUM = 3
WANDCOMPINFO_INDEX = {
    WAND_COMP_TYPE_ACTION: 3,
    WAND_COMP_TYPE_CONDITION: 1 }
WANDABILITY_LOCKMAX = 2

class CWandData(object):
    m_SID = 0
    m_Name = ''
    m_Type = WAND_MASK
    m_Tag = ()
    m_ItemAttr = { }
    m_LevelInfo = { }
    m_SendWandCnt = False
    m_EvolutionTarget = 0
    
    def Create(cls, oGame, oWandCon, dWand, iGrade = 1, iPointID = 0, dTmp = None):
        oWand = CWand(oGame, 0, iPointID, dTmp)
        cls.InitItemData(oWand)
        if oWandCon:
            oWand.AddToContainer(oWandCon)
        if dWand:
            oWand.Load(dWand)
        oWand.Init(iGrade)
        return oWand

    Create = classmethod(Create)
    
    def InitItemData(cls, oWand):
        oWand.m_SID = cls.m_SID
        oWand.m_Name = cls.m_Name
        oWand.m_Type = cls.m_Type
        oWand.m_Tag = cls.m_Tag
        oWand.m_LevelInfo = dict(cls.m_LevelInfo)
        if cls.m_LevelInfo:
            oWand.m_MaxGrade = max(cls.m_LevelInfo)
        oWand.m_SendWandCnt = cls.m_SendWandCnt
        oWand.m_EvolutionTarget = cls.m_EvolutionTarget

    InitItemData = classmethod(InitItemData)


class CWand(CBaseItem):
    m_Tag = ()
    m_InitPerform = ()
    m_LevelInfo = { }
    m_EvolutionTarget = 0
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super().__init__(oGame, iTemp, iPointID, dTmp)
        self.m_Enable = 0
        self.m_ForbidCasting = 0
        self.m_SpellCDFlag = f'''wandspellcd-{self.m_ID}'''
        self.m_Comp = {
            WAND_COMP_TYPE_ACTION: { },
            WAND_COMP_TYPE_CONDITION: { } }
        self.m_CompTemp = {
            WAND_COMP_TYPE_ACTION: { },
            WAND_COMP_TYPE_CONDITION: { } }
        self.m_CompDismantleStatus = {
            WAND_COMP_TYPE_ACTION: { },
            WAND_COMP_TYPE_CONDITION: { } }
        self.m_ActionCompSealStatus = { }
        self.m_ExtActionComp = { }
        self.m_PosFunctionInfo = { }
        self.m_ExtActionCompNum = 0
        self.m_ExtraCallTimeProbInfo = { }
        self.m_ExtraCallTimeProb = 0
        self.m_CDDownFrame = 0
        self.m_CDSubFrame = 0
        self.m_GameID = oGame.m_ID
        self.m_WandCount = 0
        self.m_WandBaseCount = 0
        self.m_WandBaseCountInfo = { }
        self.m_WandMaxCount = 0
        self.m_SendWandCnt = False
        self.m_Quality = 0
        self.m_GrooveNum = (0, 0)
        if 'NoInitComp' in self.m_TmpData and self.m_TmpData['NoInitComp']:
            self.Set('InitComp', 0)
        if 'Reason' in self.m_TmpData and self.m_TmpData['Reason'] == 'initial':
            self.m_RedDot = False
        else:
            self.m_RedDot = True
        self.m_WandAbility = { }
        self.m_ExtConComp = { }
        self.m_ExtConCompNum = 0
        self.m_ExtConCompInfo = { }
        self.m_ExtActComp = { }
        self.m_ExtActCompNum = 0
        self.m_ExtActCompInfo = { }
        self.m_LockWandAbility = []
        self.m_CarryWandAbility = []
        self.m_MinTriggerAllCompInfo = { }
        self.m_MinTriggerAllCompNum = 0
        self.m_ExtActionCompCache = { }

    
    def __str__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-wand%s-%s-%s' % (self.m_GameID, iPlayerID, self.m_SID, self.m_Grade, self.m_ID)

    
    def __repr__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-wand%s-%s-%s' % (self.m_GameID, iPlayerID, self.m_SID, self.m_Grade, self.m_ID)

    
    def Release(self):
        for iType, dComp in self.m_CompTemp.items():
            for iPos in dComp:
                self.RemoveComp(iType, iPos, 'release', bSyncSameWand = False)
            
        
        super().Release()

    
    def Save(self):
        dData = super().Save()
        lstComp = []
        for iType, dComp in self.m_CompTemp.items():
            for iPos, (iCompSID, iLevel) in dComp.items():
                if not self.IsFromConEquip(iType, iPos):
                    continue
                lstComp.append((iType, iPos, iCompSID, iLevel))
            
        
        dData['SID'] = self.m_SID
        dData['Grade'] = self.m_Grade
        dData['CP'] = lstComp
        dData['RD'] = self.m_RedDot
        dData['WC'] = self.m_WandCount
        dData['WA'] = DeepCopy(self.m_WandAbility)
        dData['EC'] = self.GetExtConCompSaveInfo()
        dData['EA'] = self.GetExtActCompSaveInfo()
        dData['LWA'] = self.m_LockWandAbility
        dData['CWA'] = self.m_CarryWandAbility
        return dData

    
    def Load(self, dData):
        self.m_WandAbility = dData.get('WA', { })
        super().Load(dData)
        self.m_SID = dData['SID']
        self.m_Grade = dData['Grade']
        for iType, iPos, iCompSID, iLevel in dData['CP']:
            self.AddCustomComp(iType, iPos, iCompSID, iLevel, sReason = 'load')
        
        self.m_RedDot = dData['RD']
        self.m_WandCount = dData['WC']
        self.m_ExtConCompInfo = dData.get('EC', { })
        self.m_ExtActCompInfo = dData.get('EA', { })
        self.m_LockWandAbility = dData.get('LWA', [])
        self.m_CarryWandAbility = dData.get('CWA', [])

    
    def Enable(self):
        if self.m_Enable:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        self.m_Enable = 1
        for iPerform in self.m_InitPerform:
            oOwner.AddPerform(iPerform, self.m_Grade, iItem = self.m_ID, iEnable = 1)
        
        lstEvolutionPointAbility = GetWandPointAbility(self.m_EvolutionTarget)
        for iAbilityPerform, (iQuality, iFloatingRange) in self.m_WandAbility.items():
            oAbility = oOwner.AddPerform(iAbilityPerform, 1, iItem = self.m_ID, iEnable = 0)
            if oAbility:
                oAbility.SetQuality(iQuality, iFloatingRange)
                if iAbilityPerform not in lstEvolutionPointAbility:
                    oAbility.Enable(oOwner)
        
        for iType in (WAND_COMP_TYPE_ACTION, WAND_COMP_TYPE_CONDITION):
            dCurComp = self.m_Comp[iType]
            for iPos, oComp in list(dCurComp.items()):
                if iPos not in dCurComp or not dCurComp[iPos]:
                    continue
                oComp.Enable()
            
        

    
    def Disable(self):
        if not self.m_Enable:
            return None
        self.ClearSpellCD()
        oOwner = self.GetOwner()
        if oOwner and not (oOwner.m_ReleaseFlag):
            for iPerform in self.m_InitPerform:
                oOwner.RemovePerform(iPerform)
            
        for iAbilityPerform in self.m_WandAbility:
            oOwner.RemovePerform(iAbilityPerform)
        
        for iType in (WAND_COMP_TYPE_ACTION, WAND_COMP_TYPE_CONDITION):
            dCurComp = self.m_Comp[iType]
            for iPos, oComp in list(dCurComp.items()):
                if iPos not in dCurComp or not dCurComp[iPos]:
                    continue
                oComp.Disable()
            
        
        self.m_Enable = 0

    
    def AddToContainer(self, oContainer):
        if not self.m_ID:
            return None
        super().AddToContainer(oContainer)
        for dComp in self.m_Comp.values():
            for oComp in dComp.values():
                oComp.SetOwner(oContainer.m_Owner)
            
        

    
    def GetColdTime(self):
        iColdTime = self.QueryTmp('TrueColdTime', 0)
        if not iColdTime:
            return self.QueryAttr('ColdTime')
        return iColdTime

    
    def SetAttr(self, sAttr, iValue, iRefresh):
        if sAttr not in self.m_PrivateAttr:
            oAttr = cl_object.baseattr.NewAttr(self, sAttr, iValue, iRefresh)
            self.m_PrivateAttr[sAttr] = oAttr
        else:
            oAttr = self.m_PrivateAttr[sAttr]
            oAttr.ChangeBase(self, iValue)

    
    def GetAttr(self, sAttr):
        if sAttr in self.m_PrivateAttr:
            return self.m_PrivateAttr[sAttr]

    
    def SetGrade(self, iGrade):
        if iGrade not in self.m_LevelInfo:
            return None
        iEnable = self.m_Enable
        self.SetWandQuality(iGrade)
        if iEnable:
            self.Disable()
            super().SetGrade(iGrade)
            self.Enable()
        else:
            super().SetGrade(iGrade)

    
    def AttrChange(self, sAttr, iMul, iAdd, sKey, iRefresh = 1):
        super().AttrChange(sAttr, iMul, iAdd, sKey, iRefresh = iRefresh)
        self.GS2CWandPropChange(sAttr)
        oOwner = self.GetOwner()
        if oOwner and oOwner.m_WandCon.m_CurWand == self.m_ID:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND_ATTR_CHANGE, self.GetOwner(), {
                'Wand': self.m_ID,
                'Reason': sAttr }, oGame = self.m_Game)

    
    def AttrClear(self, sAttr, sKey, iRefresh = 1):
        super().AttrClear(sAttr, sKey, iRefresh = iRefresh)
        self.GS2CWandPropChange(sAttr)
        oOwner = self.GetOwner()
        if oOwner and oOwner.m_WandCon.m_CurWand == self.m_ID:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND_ATTR_CHANGE, self.GetOwner(), {
                'Wand': self.m_ID,
                'Reason': sAttr }, oGame = self.m_Game)

    
    def SetWandQuality(self, iQuality):
        self.m_Quality = iQuality

    
    def SetWandPosFunc(self, iPos, iFunc, sReason, iValue):
        dPosFunctionInfo = self.m_PosFunctionInfo
        if iPos not in dPosFunctionInfo:
            dPosFunctionInfo[iPos] = { }
        if iFunc not in dPosFunctionInfo[iPos]:
            dPosFunctionInfo[iPos][iFunc] = {
                sReason: iValue }
        else:
            dPosFunctionInfo[iPos][iFunc][sReason] = iValue
        WandLog.Debug('%s %s %s set posfun %s %s %s %s' % (self.m_Game.m_ID, self.GetPlayerID(), self.m_SID, iPos, iFunc, sReason, iValue))

    
    def ClearWandPosFunc(self, iPos, iFunc, sReason):
        dPosFunctionInfo = self.m_PosFunctionInfo
        if iPos not in dPosFunctionInfo:
            return None
        if iFunc not in dPosFunctionInfo[iPos] or sReason not in dPosFunctionInfo[iPos][iFunc]:
            return None
        dPosFunctionInfo[iPos][iFunc].pop(sReason)
        WandLog.Debug('%s %s %s clear posfun %s %s %s' % (self.m_Game.m_ID, self.GetPlayerID(), self.m_SID, iPos, iFunc, sReason))

    
    def CheckCompPosCanTrigger(self, iPos):
        dPosFunctionInfo = self.m_PosFunctionInfo
        if iPos not in dPosFunctionInfo:
            return 1
        if WAND_POSFUNC_INVALIDPROB not in dPosFunctionInfo[iPos]:
            return 1
        iProb = sum(dPosFunctionInfo[iPos][WAND_POSFUNC_INVALIDPROB].values())
        if not iProb:
            return 1
        if self.m_Game.Random(10000) > iProb:
            return 1
        return 0

    
    def GetWandQuality(self):
        return self.m_Quality

    
    def OnSetGrade(self):
        iInitComp = self.Query('InitComp', 1)
        self.Set('InitComp', 0)
        (iConditionCompNum, lstInitCondComp, iActionCompNum, lstInitActionComp, lstInitPerform, dAttr) = self.m_LevelInfo[self.m_Grade]
        iActionCompNum += self.m_ExtActionCompNum
        cl_formula.ResetNoSceneObjGradeFormulaAttr(self, dAttr, self.m_Grade, BASEATTR_REFRESH)
        self.m_InitPerform = lstInitPerform
        self.AddInitComp(WAND_COMP_TYPE_CONDITION, iConditionCompNum, lstInitCondComp, iInitComp)
        self.AddInitComp(WAND_COMP_TYPE_ACTION, iActionCompNum, lstInitActionComp, iInitComp)
        self.m_GrooveNum = (iConditionCompNum, iActionCompNum)
        self.RefreshMinTriggerAllCompNum()
        self.InitWandAbility(sReason = 'Init')

    
    def Upgrade(self):
        self.Set('InitComp', 1)
        self.SetBaseGrade(self.m_BaseGrade + 1, iSendMsg = 0)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCHANGE, self.GetOwner(), {
            'Wand': self.m_ID,
            'WandSID': self.m_SID,
            'Quality': self.GetWandQuality() }, oGame = self.m_Game, iSub = WAND_SUBMSG_UPGRADE)
        self.m_RedDot = True
        oOwner = self.GetOwner()
        if oOwner:
            oOwner.m_WandCon.SyncWandCompByPriority(self)

    
    def AddInitComp(self, iType, iCompNum, lstInitComp, iInitComp):
        dCompTemp = self.m_CompTemp[iType]
        dCompDismantleStatus = self.m_CompDismantleStatus[iType]
        for iIndex in range(iCompNum):
            if iIndex not in dCompTemp:
                dCompDismantleStatus[iIndex] = 1
                dCompTemp[iIndex] = WAND_EMPTY_COMP
        
        for iPos, (iCompSID, iLevel, iDismantleStatus) in enumerate(lstInitComp):
            if iDismantleStatus:
                if not iInitComp and self.ValidDismantlePos(iType, iPos):
                    continue
                dCompDismantleStatus[iPos] = iDismantleStatus
                if self.m_Container:
                    iLevel = self.m_Container.AddBagComp(iCompSID, iLevel, 1, 'wandinit')
                else:
                    dCompDismantleStatus[iPos] = iDismantleStatus
            None.AddComp(iType, iPos, iCompSID, iLevel, 'init', bSyncSameWand = False)
        

    
    def OnRemoveFromContainer(self):
        super().OnRemoveFromContainer()
        for iType, dCompStatus in self.m_CompDismantleStatus.items():
            for iPos, iStatus in dCompStatus.items():
                if iStatus:
                    self.RemoveComp(iType, iPos, 'remove', bSyncSameWand = False)
            
        
        self.m_LockWandAbility = []

    
    def GetWandShowInfo(self):
        (iConditionCompNum, iActionCompNum) = self.m_GrooveNum
        lstComInfo = self.GetCompInfo()
        lstWandAbility = self.GetWandAbilityInfo()
        return (self.m_Grade, self.GetColdTime(), iConditionCompNum, iActionCompNum, lstComInfo, lstWandAbility)

    
    def GetWandAbilityInfo(self):
        lstWandAbility = []
        for iAbility, (iQuality, iFloatingRange) in self.m_WandAbility.items():
            lstWandAbility.append([
                iAbility,
                iQuality,
                iFloatingRange])
        
        return lstWandAbility

    
    def GetWandLevelInfo(self):
        return self.m_LevelInfo

    
    def GetWandGroveNum(self):
        return self.m_GrooveNum

    
    def GetCompPos(self, iType, iSID, iLevel, iOnlyDismantle = 0):
        lstCompPos = []
        for iPos, (iCompSID, iCompLevel) in self.m_CompTemp[iType].items():
            if iOnlyDismantle and not self.ValidDismantlePos(iType, iPos):
                continue
            if iCompSID == iSID and iCompLevel == iLevel:
                lstCompPos.append(iPos)
        
        return lstCompPos

    
    def CheckRemoveComp(self, iType, iCompPos):
        dComp = self.m_Comp[iType]
        if iCompPos not in dComp:
            return 0
        oComp = dComp[iCompPos]
        if not oComp:
            return 0
        if oComp.m_SubType == WAND_SUBTYPE_COPY:
            return 0
        return 1

    
    def ValidDismantlePos(self, iType, iPos):
        if iType not in self.m_CompDismantleStatus or iPos not in self.m_CompDismantleStatus[iType]:
            return 0
        return self.m_CompDismantleStatus[iType][iPos]

    
    def ValidAddComp(self, iType, iPos, iCompSID, iCompLevel, iSubType = WAND_SUBTYPE_NORMAL):
        if iPos not in self.m_CompTemp[iType]:
            return 0
        if self.IsFromConEquip(iType, iPos):
            (iCurCompSID, iCurCompLevel) = self.m_CompTemp[iType][iPos]
            if iCurCompSID == iCompSID and iCurCompLevel == iCompLevel:
                return 0
            oOwner = self.GetOwner()
            if oOwner and self.GetEquipCompNum(iType, iCompSID, iCompLevel) >= oOwner.m_WandCon.GetBagCompNum(iCompSID, iCompLevel):
                return 0
        if iType == WAND_COMP_TYPE_CONDITION:
            for iTempPos, (iSID, _) in self.m_CompTemp[WAND_COMP_TYPE_CONDITION].items():
                if iSID != iCompSID:
                    continue
                if not self.ValidDismantlePos(iType, iTempPos):
                    return 0
            
        elif iType == WAND_COMP_TYPE_ACTION and iPos in self.m_ActionCompSealStatus and iPos != min(self.m_ActionCompSealStatus):
            return 0
        return 1

    
    def AddComp(self, iType, iPos, iCompSID, iCompLevel, sReason, bSyncSameWand = True, iSubType = WAND_SUBTYPE_NORMAL):
        if not self.ValidAddComp(iType, iPos, iCompSID, iCompLevel, iSubType):
            return 0
        oOwner = self.GetOwner()
        iPlayerID = oOwner.m_PlayerID if oOwner else 0
        oComp = cl_wand.CreateWandComp(oOwner, self.m_ID, iCompSID, iCompLevel, iPos, iSubType, sReason)
        if not oComp:
            WandLog.Alert('%s %s addcomp %s-%s invalid %s' % (self.m_Game.m_ID, iPlayerID, iCompSID, iCompLevel, sReason))
            return 0
        WandLog.Debug('%s %s addcomp %s %s-%s-%s-%s pos%s %s' % (self.m_Game.m_ID, iPlayerID, iType, self.m_SID, self.m_ID, iCompSID, iCompLevel, iPos, sReason))
        if iType == WAND_COMP_TYPE_CONDITION:
            for iTempPos, (iSID, _) in self.m_CompTemp[WAND_COMP_TYPE_CONDITION].items():
                if iSID != iCompSID:
                    continue
                self.RemoveCustomComp(iType, iTempPos)
            
        self.RemoveComp(iType, iPos, sReason + '-syncrmcomp', bSyncSameWand)
        self.m_CompTemp[iType][iPos] = (iCompSID, iCompLevel)
        if iPos in self.m_Comp[iType]:
            oOldComp = self.m_Comp[iType][iPos]
            WandLog.Alert('%s %s exist exception comp %s %s-%s-%s pos%s %s' % (self.m_Game.m_ID, iPlayerID, iType, self.m_SID, self.m_ID, oOldComp.m_SID, iPos, sReason))
            oOldComp.Disable()
            oOldComp.Release()
        self.m_Comp[iType][iPos] = oComp
        if bSyncSameWand:
            oOwner = self.GetOwner()
            if oOwner:
                lstWand = oOwner.m_WandCon.GetSameWand(self)
                for oWand in lstWand:
                    if oWand.m_ID == self.m_ID:
                        continue
                    oWand.AddComp(iType, iPos, iCompSID, iCompLevel, sReason + '-syncaddcomp', bSyncSameWand = False)
                    wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, [
                        oOwner.m_PlayerID], oWand)
                
        dSorted = { }
        for iCurPos in sorted(self.m_Comp[iType]):
            dSorted[iCurPos] = self.m_Comp[iType][iCurPos]
        
        self.m_Comp[iType] = dSorted
        if self.m_Enable:
            oComp.Enable()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, oOwner, {
                'CompPos': iPos,
                'Wand': self.m_ID,
                'WandSID': self.m_SID,
                'CompType': iType,
                'WandCompSID': iCompSID,
                'Quality': oComp.m_Level,
                'Reason': sReason }, iSub = WANDCOMP_SUBMSG_ADD)
        return oComp.m_ID

    
    def AddCustomComp(self, iType, iPos, iCompSID, iCompLevel, sReason = 'custom', bSyncSameWand = True):
        if not self.ValidDismantlePos(iType, iPos):
            return 0
        return self.AddComp(iType, iPos, iCompSID, iCompLevel, sReason, bSyncSameWand)

    
    def RemoveComp(self, iType, iPos, sReason, bSyncSameWand = True):
        oOldComp = self.m_Comp[iType].pop(iPos, None)
        if not oOldComp:
            return 0
        self.m_CompTemp[iType][iPos] = WAND_EMPTY_COMP
        iPlayerID = self.GetPlayerID()
        iWandCompSID = oOldComp.m_SID
        WandLog.Debug('%s %s rmcomp %s %s-%s-%s-%s pos%s %s' % (self.m_Game.m_ID, iPlayerID, iType, self.m_SID, self.m_ID, iWandCompSID, oOldComp.m_Level, iPos, sReason))
        oOldComp.Disable()
        oOldComp.Release()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCOMPCHANGE, self.GetOwner(), {
            'CompPos': iPos,
            'Wand': self.m_ID,
            'WandCompSID': iWandCompSID,
            'CompType': iType,
            'WandSID': self.m_SID,
            'Quality': oOldComp.m_Level,
            'Reason': sReason }, iSub = WANDCOMP_SUBMSG_REMOVE, oGame = self.m_Game)
        if bSyncSameWand:
            oOwner = self.GetOwner()
            if oOwner:
                lstWand = oOwner.m_WandCon.GetSameWand(self)
                for oWand in lstWand:
                    if oWand.m_ID == self.m_ID:
                        continue
                    oWand.RemoveComp(iType, iPos, sReason, bSyncSameWand = False)
                    wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, [
                        oOwner.m_PlayerID], oWand)
                
        return 1

    
    def RemoveCustomComp(self, iType, iPos):
        if not self.ValidDismantlePos(iType, iPos):
            iPlayerID = self.GetPlayerID()
            WandLog.Alert('%s %s rmcomp pos %s %s %s invalid' % (self.m_Game.m_ID, iPlayerID, self.m_SID, iType, iPos))
            return 0
        return self.RemoveComp(iType, iPos, 'custom')

    
    def RemoveAllCustomComp(self):
        for iType, dComp in self.m_Comp.items():
            for iPos in list(dComp):
                if not self.ValidDismantlePos(iType, iPos):
                    continue
                self.RemoveCustomComp(iType, iPos)
            
        

    
    def OnChangeCompNum(self, dChangeCompNum):
        dCurCompNum = { }
        sReason = 'ChangeCompNum'
        for iType, dCompTemp in self.m_CompTemp.items():
            for iPos, (iSID, iLevel) in dCompTemp.items():
                if not self.IsFromConEquip(iType, iPos):
                    continue
                if iSID not in dChangeCompNum:
                    continue
                tKey = (iSID, iLevel)
                if tKey not in dCurCompNum:
                    dCurCompNum[tKey] = 0
                dCurCompNum[tKey] += 1
                iNum = dChangeCompNum[iSID].get(iLevel, 0)
                if dCurCompNum[tKey] > iNum:
                    self.RemoveComp(iType, iPos, sReason)
            
        

    
    def GetCompInfo(self):
        lstComInfo = []
        for iType, dPosInfo in self.m_CompTemp.items():
            for iPos, (iCompSID, iLevel) in dPosInfo.items():
                if (iCompSID, iLevel) == WAND_EMPTY_COMP:
                    continue
                iDismantle = self.m_CompDismantleStatus[iType][iPos]
                oComp = self.m_Comp[iType][iPos]
                lstComInfo.append((iPos, iCompSID, iLevel, iDismantle, oComp.m_SubType, oComp.GetShowCallTimes()))
            
        
        return lstComInfo

    
    def GetEmptyPosByType(self, iType):
        for iPos, tComp in self.m_CompTemp[iType].items():
            if tComp == WAND_EMPTY_COMP:
                return iPos
        
        return WAND_COMP_POS_NONE

    
    def GetDismantleCompNum(self, iType, iComp, iLevel):
        iNum = 0
        tComp = (iComp, iLevel)
        for iPos, tEquipComp in self.m_CompTemp[iType].items():
            if not self.ValidDismantlePos(iType, iPos):
                continue
            if tComp == tEquipComp:
                iNum += 1
        
        return iNum

    
    def GetAllDismantleComp(self):
        dComp = {
            WAND_COMP_TYPE_ACTION: [],
            WAND_COMP_TYPE_CONDITION: [] }
        for iType, dPosInfo in self.m_CompTemp.items():
            lstComp = dComp[iType]
            for iPos, tComp in dPosInfo.items():
                if not self.IsFromConEquip(iType, iPos):
                    continue
                lstComp.append(tComp)
            
        
        return dComp

    
    def CheckEquipComp(self):
        for iType, dPosInfo in self.m_CompTemp.items():
            iIndex = WANDCOMPINFO_INDEX[iType]
            tInitComp = self.m_LevelInfo[self.m_Grade][iIndex]
            for iPos, tComp in dPosInfo.items():
                if tComp == WAND_EMPTY_COMP:
                    continue
                if iPos < len(tInitComp):
                    (iComp, iLevel, _) = tInitComp[iPos]
                    if tComp == (iComp, iLevel):
                        continue
                    continue
                return True
            
        
        return False

    
    def GetCompTemp(self):
        return self.m_CompTemp

    
    def OnFinishConditionComp(self, oFinishComp):
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND, oOwner, {
            'Wand': self.m_ID,
            'CompSID': oFinishComp.m_SID,
            'CompPos': oFinishComp.m_CurPos }, iSub = WAND_SUBMSG_FINISHCONDITION)
        self.TryTriggerAllActionComp()

    
    def TryTriggerAllActionComp(self):
        if self.m_ForbidCasting:
            return None
        if not self.WandCastingConditionsRefresh():
            return None
        self.TriggerAllActionComp()

    
    def WandCastingConditionsRefresh(self):
        if not self.m_Enable:
            return 0
        (iResult, lstConditionCompFinish) = self.GetCastingConditions()
        iPlayerID = self.GetPlayerID()
        wandnet.GS2CWandCastingConditions(self.m_Game, iPlayerID, self.m_ID, self.m_CDDownFrame, self.GetColdTime(), lstConditionCompFinish)
        return iResult

    
    def GetCastingConditions(self):
        lstConditionCompFinish = []
        dComp = self.m_Comp[WAND_COMP_TYPE_CONDITION]
        iCDResult = 0 if self.CheckSpellCD() else 1
        iFinishNum = 0
        for iPos, tComp in self.m_CompTemp[WAND_COMP_TYPE_CONDITION].items():
            if tComp != WAND_EMPTY_COMP:
                oComp = dComp[iPos]
                iFinish = oComp.CheckFinish()
                lstConditionCompFinish.append((iPos, iFinish))
                iFinishNum += iFinish
        
        iFinishResult = 0 if iFinishNum < self.m_MinTriggerAllCompNum else 1
        if iCDResult and iFinishResult:
            iResult = 1
        else:
            iResult = 0
        return (iResult, lstConditionCompFinish)

    
    def ResetConditionComp(self):
        for oComp in self.m_Comp[WAND_COMP_TYPE_CONDITION].values():
            oComp.ResetCondition()
        

    
    def GetConditionCompFinish(self):
        dComp = self.m_Comp[WAND_COMP_TYPE_CONDITION]
        for iPos, tComp in self.m_CompTemp[WAND_COMP_TYPE_CONDITION].items():
            if tComp == WAND_EMPTY_COMP:
                return 0
            oComp = dComp[iPos]
            if not oComp.CheckFinish():
                return 0
        
        return 1

    
    def AddExtraCallTimeProb(self, iProb, sReason):
        self.m_ExtraCallTimeProbInfo[sReason] = iProb
        self.m_ExtraCallTimeProb = sum(self.m_ExtraCallTimeProbInfo.values())

    
    def ClearExtraCallTimeProb(self, sReason):
        if sReason not in self.m_ExtraCallTimeProbInfo:
            return None
        self.m_ExtraCallTimeProbInfo.pop(sReason)
        self.m_ExtraCallTimeProb = sum(self.m_ExtraCallTimeProbInfo.values())

    
    def GetExtraWandCallTime(self):
        if self.m_ExtraCallTimeProb >= 0 and self.m_Game.Random(10000) <= self.m_ExtraCallTimeProb:
            return 1
        return 0

    
    def TriggerAllActionComp(self):
        self.EnterCD()
        for iPos, oComp in self.m_Comp[WAND_COMP_TYPE_ACTION].items():
            if not self.CheckCompPosCanTrigger(iPos):
                continue
            oComp.TriggerAction(self.GetExtraWandCallTime())
        
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND, oOwner, {
            'Wand': self.m_ID,
            'WandSID': self.m_SID,
            'WandTag': list(self.m_Tag) }, iSub = WAND_SUBMSG_TRIGGERACTION)

    
    def RandomTriggerActionComp(self, iNum = 1):
        if not self.m_Comp[WAND_COMP_TYPE_ACTION]:
            return None
        dActionComp = { 1: iPos for iPos in self.m_Comp[WAND_COMP_TYPE_ACTION] }
        for _ in range(iNum):
            iRandPos = ChooseKey(self.m_Game, dActionComp)
            if not self.CheckCompPosCanTrigger(iRandPos):
                continue
            oComp = self.m_Comp[WAND_COMP_TYPE_ACTION][iRandPos]
            oComp.TriggerAction(self.GetExtraWandCallTime())
        

    
    def TriggerPointPosActionComp(self, iPos):
        if not self.CheckCompPos(iPos):
            return None
        if not self.CheckCompPosCanTrigger(iPos):
            return None
        oComp = self.m_Comp[WAND_COMP_TYPE_ACTION][iPos]
        oComp.TriggerAction(self.GetExtraWandCallTime())

    
    def CheckCompPos(self, iPos):
        if iPos not in self.m_Comp[WAND_COMP_TYPE_ACTION]:
            return False
        return True

    
    def GetCompByPos(self, iType, iPos):
        if iPos not in self.m_Comp[iType]:
            return None
        return self.m_Comp[iType][iPos]

    
    def SetWandForbidCasting(self, bForbid):
        self.m_ForbidCasting = bForbid

    
    def EnterCD(self, iCDTime = 0):
        self.AddSpellCDFrame(iCDTime)
        self.ResetConditionComp()
        self.WandCastingConditionsRefresh()

    
    def AddSpellCDFrame(self, iCDTime = 0):
        if not self.m_Enable:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iColdTime = self.QueryAttr('ColdTime')
        iSpellCD = iCDTime if iCDTime else iColdTime
        if not iSpellCD:
            return None
        if iSpellCD != iColdTime:
            self.SetTmp('TrueColdTime', iCDTime)
        iSpellCDFrame = Time2Frame(iSpellCD)
        oOwner.Remove_Call_Out(self.m_SpellCDFlag)
        self.m_CDDownFrame = self.m_Game.GetFrameNum() + iSpellCDFrame
        oOwner.Call_Out(self.OnSpellColdDown, iSpellCDFrame, self.m_SpellCDFlag)

    
    def CheckSpellCD(self):
        if not self.m_Enable:
            return 0
        oOwner = self.GetOwner()
        if not oOwner:
            return 0
        return oOwner.Find_Call_Out(self.m_SpellCDFlag)

    
    def ClearSpellCD(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oOwner.Remove_Call_Out(self.m_SpellCDFlag)
        self.m_CDDownFrame = 0
        self.m_CDSubFrame = 0
        self.SetTmp('TrueColdTime', 0)

    
    def OnSpellColdDown(self):
        self.m_CDDownFrame = 0
        self.m_CDSubFrame = 0
        self.SetTmp('TrueColdTime', 0)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND, self.GetOwner(), { }, iSub = WAND_SUBMSG_WANDCDEND)
        self.TryTriggerAllActionComp()

    
    def SubSpellCD(self, iSubFrame, iMinLastFrame = 0):
        if not self.CheckSpellCD():
            return None
        iColdTimeFrame = Time2Frame(self.GetColdTime())
        if iColdTimeFrame - self.m_CDSubFrame <= iMinLastFrame:
            return None
        iSubFrame = min(iSubFrame, iColdTimeFrame - iMinLastFrame - self.m_CDSubFrame)
        iCurFrame = self.m_Game.GetFrameNum()
        iNewEndFrame = self.m_CDDownFrame - iSubFrame
        oOwner = self.GetOwner()
        oOwner.Remove_Call_Out(self.m_SpellCDFlag)
        iPlayerID = self.GetPlayerID()
        if iNewEndFrame <= iCurFrame:
            self.OnSpellColdDown()
            wandnet.GS2CWandCastingConditions(self.m_Game, iPlayerID, self.m_ID, iCurFrame, self.GetColdTime(), [])
            return None
        self.m_CDDownFrame = iNewEndFrame
        self.m_CDSubFrame += iSubFrame
        oOwner.Call_Out(self.OnSpellColdDown, iNewEndFrame - iCurFrame, self.m_SpellCDFlag)
        wandnet.GS2CWandCastingConditions(self.m_Game, iPlayerID, self.m_ID, self.m_CDDownFrame, self.GetColdTime(), [])

    
    def GetPlayerID(self):
        oOwner = self.GetOwner()
        if oOwner:
            return oOwner.m_PlayerID
        return 0

    
    def AddWandCount(self, iCount):
        if not self.m_Enable:
            return None
        self.m_WandCount += iCount
        self.FixWandCount()
        self.CacheWandCnt()

    
    def SetWandCount(self, iCount):
        if not self.m_Enable:
            return None
        self.m_WandCount = iCount
        self.FixWandCount()
        self.CacheWandCnt()

    
    def FixWandCount(self):
        if not self.m_WandMaxCount:
            return None
        self.m_WandCount = min(self.m_WandCount, self.m_WandMaxCount - self.m_WandBaseCount)

    
    def SetWandBaseCount(self, iCount, sKey, bClear):
        if not self.m_Enable:
            return None
        if bClear:
            if iCount not in self.m_WandBaseCountInfo:
                return None
            dKey = self.m_WandBaseCountInfo[iCount]
            if sKey not in dKey:
                return None
            dKey.pop(sKey)
            if not dKey:
                self.m_WandBaseCountInfo.pop(iCount)
            elif iCount not in self.m_WandBaseCountInfo:
                self.m_WandBaseCountInfo[iCount] = { }
        self.m_WandBaseCountInfo[iCount][sKey] = None
        if self.m_WandBaseCountInfo:
            self.m_WandBaseCount = max(self.m_WandBaseCountInfo)
        else:
            self.m_WandBaseCount = 0
        self.FixWandCount()
        self.GS2CWandCountInfo()

    
    def SetWandMaxCount(self, iCount):
        if not self.m_Enable:
            return None
        self.m_WandMaxCount = iCount
        self.FixWandCount()
        self.GS2CWandCountInfo()

    
    def GetWandCount(self):
        return self.m_WandCount + self.m_WandBaseCount

    
    def GetWandMaxCount(self):
        return self.m_WandMaxCount

    
    def GetWandCompByType(self, iType):
        if iType in self.m_Comp:
            return self.m_Comp[iType]
        return { }

    
    def CacheWandCnt(self):
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        if not oWandElement or not (oWandElement.m_Enable):
            return None
        oWandElement.CacheWandCnt(self.m_Owner, self.m_ID)

    
    def GS2CCountChange(self, bComp, bWandCnt, lstComp = None):
        if not self.m_Enable:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if bComp:
            self.GS2CWandConditionCompCountChange(lstComp)
        if self.m_SendWandCnt and bWandCnt:
            wandnet.GS2CWandCountChange(self.m_Game, oOwner.m_PlayerID, self.m_ID, self.GetWandCount())

    
    def SelfRefresh(self):
        if not self.m_Enable:
            return None
        self.WandCastingConditionsRefresh()
        self.GS2CWandConditionCompCountChange()
        if self.m_SendWandCnt:
            self.GS2CWandCountInfo()

    
    def GS2CWandCountInfo(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        wandnet.GS2CWandCountInfo(self.m_Game, oOwner.m_PlayerID, self.m_ID, self.GetWandCount(), self.GetWandMaxCount())

    
    def GS2CWandConditionCompCountChange(self, lstComp = None):
        for oComp in self.m_Comp[WAND_COMP_TYPE_CONDITION].values():
            if lstComp and oComp.m_ID not in lstComp:
                continue
            oComp.GS2CWandConditionCompCountChange()
        

    
    def SetRedDot(self, bState):
        self.m_RedDot = bState

    
    def GetRedDot(self):
        return self.m_RedDot

    
    def GS2CWandPropChange(self, sAttr):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        (iIdx, _, iType, iLen, iMode) = INFO_PROP_NAME[sAttr]
        iVal = GetPropValue(self, sAttr, iMode)
        if not iVal:
            return None
        lstPropInfo = []
        lstPropInfo.append((iIdx, iType, iLen, iVal))
        dPropInfo = {
            'Attr': lstPropInfo,
            'Player': [
                oOwner.m_PlayerID] }
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        wandnet.GS2CWandPropChange(self.m_Game, oOwner.m_PlayerID, self.m_ID, oOwner.m_Scene, dPropInfo, lstPlayer)

    
    def SetExtActionComp(self, sKey, iNum, iNotyfiy):
        iOldNum = 0
        if sKey in self.m_ExtActionComp:
            iOldNum = self.m_ExtActionComp[sKey]
        if iOldNum == iNum:
            return None
        self.m_ExtActionComp[sKey] = iNum
        self.m_ExtActionCompNum = (self.m_ExtActionCompNum - iOldNum) + iNum
        self.RefreshActionComp(sKey, iNotyfiy)
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND, oOwner, {
            'Wand': self.m_ID }, iSub = WAND_SUBMSG_EXTACTIONSLOT)

    
    def DelExtActionComp(self, sKey, iNotyfiy):
        if sKey not in self.m_ExtActionComp:
            return None
        iNum = self.m_ExtActionComp.pop(sKey)
        if not iNum:
            return None
        self.m_ExtActionCompNum -= iNum
        self.RefreshActionComp(sKey, iNotyfiy)
        oOwner = self.GetOwner()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND, oOwner, {
            'Wand': self.m_ID }, iSub = WAND_SUBMSG_EXTACTIONSLOT)

    
    def SetExtConComp(self, sKey, iNum, iNotyfiy):
        iOldNum = 0
        if sKey in self.m_ExtConComp:
            iOldNum = self.m_ExtConComp[sKey]
        if iOldNum == iNum:
            return None
        self.m_ExtConComp[sKey] = iNum
        self.m_ExtConCompNum = (self.m_ExtConCompNum - iOldNum) + iNum
        self.RefreshConComp(sKey, iNotyfiy)
        self.RefreshMinTriggerAllCompNum()

    
    def DelExtConComp(self, sKey, iNotyfiy):
        if sKey not in self.m_ExtConComp:
            return None
        iNum = self.m_ExtConComp.pop(sKey)
        if not iNum:
            return None
        self.m_ExtConCompNum -= iNum
        self.RefreshConComp(sKey, iNotyfiy)
        self.RefreshMinTriggerAllCompNum()

    
    def RefreshConComp(self, sReason, iNotyfiy):
        (iConCompNum, _, _, _, _, _) = self.m_LevelInfo[self.m_Grade]
        (iOldMaxConCompNum, iActionNum) = self.m_GrooveNum
        iNewMaxConCompNum = iConCompNum + self.m_ExtConCompNum
        dCompTemp = self.m_CompTemp[WAND_COMP_TYPE_CONDITION]
        dCompDismantleStatus = self.m_CompDismantleStatus[WAND_COMP_TYPE_CONDITION]
        if iOldMaxConCompNum < iNewMaxConCompNum:
            for iIndex in range(iOldMaxConCompNum, iNewMaxConCompNum):
                dCompTemp[iIndex] = WAND_EMPTY_COMP
                dCompDismantleStatus[iIndex] = 1
            
        else:
            for iIndex in range(iOldMaxConCompNum - 1, iNewMaxConCompNum - 1, -1):
                self.RemoveComp(WAND_COMP_TYPE_CONDITION, iIndex, 'refreshconcomp-%s' % sReason)
                dCompTemp.pop(iIndex)
                dCompDismantleStatus.pop(iIndex)
            
        self.m_GrooveNum = (iNewMaxConCompNum, iActionNum)
        if not iNotyfiy:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        wandnet.GS2CAddWand(self.m_Game, oOwner.m_ID, lstPlayer, self)
        self.SelfRefresh()

    
    def RefreshActionComp(self, sReason, iNotyfiy):
        (_, _, iActionCompNum, _, _, _) = self.m_LevelInfo[self.m_Grade]
        (iCondiCompNum, iOldMaxActionNum) = self.m_GrooveNum
        iNewMaxActionNum = iActionCompNum + self.m_ExtActionCompNum
        dCompTemp = self.m_CompTemp[WAND_COMP_TYPE_ACTION]
        dCompDismantleStatus = self.m_CompDismantleStatus[WAND_COMP_TYPE_ACTION]
        if iOldMaxActionNum < iNewMaxActionNum:
            for iIndex in range(iOldMaxActionNum, iNewMaxActionNum):
                dCompTemp[iIndex] = WAND_EMPTY_COMP
                dCompDismantleStatus[iIndex] = 1
            
        else:
            for iIndex in range(iOldMaxActionNum - 1, iNewMaxActionNum - 1, -1):
                self.RemoveComp(WAND_COMP_TYPE_ACTION, iIndex, 'refreshactioncomp-%s' % sReason)
                dCompTemp.pop(iIndex)
                dCompDismantleStatus.pop(iIndex)
            
        self.m_GrooveNum = (iCondiCompNum, iNewMaxActionNum)
        if not iNotyfiy:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        wandnet.GS2CAddWand(self.m_Game, oOwner.m_ID, lstPlayer, self)
        self.SelfRefresh()

    
    def GetExtConCompSaveInfo(self):
        (iConCompNum, _, _, _, _, _) = self.m_LevelInfo[self.m_Grade]
        iNewConCompNum = self.m_GrooveNum[0]
        if iConCompNum >= iNewConCompNum:
            return { }
        dConComp = { }
        for iPos, dComp in self.m_CompTemp[WAND_COMP_TYPE_CONDITION].items():
            if iPos >= iConCompNum and dComp and dComp != WAND_EMPTY_COMP:
                dConComp[iPos] = dComp
        
        return dConComp

    
    def RecoveryExtConCompSaveInfo(self):
        (iNewMaxConCompNum, _) = self.GetWandGroveNum()
        for iPos, (iCompSID, iCompLevel) in self.m_ExtConCompInfo.items():
            if iPos < iNewMaxConCompNum:
                self.AddComp(WAND_COMP_TYPE_CONDITION, iPos, iCompSID, iCompLevel, 'RecoveryExtConCompSaveInfo')
        
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        cl_wand.net.GS2CAddWand(self.m_Game, oOwner.m_ID, lstPlayer, self)
        self.SelfRefresh()

    
    def GetExtActCompSaveInfo(self):
        (_, _, iActCompNum, _, _, _) = self.m_LevelInfo[self.m_Grade]
        iNewActCompNum = self.m_GrooveNum[1]
        if iActCompNum >= iNewActCompNum:
            return { }
        dActComp = { }
        for iPos, dComp in self.m_CompTemp[WAND_COMP_TYPE_ACTION].items():
            if iPos >= iActCompNum and dComp and dComp != WAND_EMPTY_COMP:
                dActComp[iPos] = dComp
        
        return dActComp

    
    def RecoveryExtActCompSaveInfo(self, bSync = True):
        (_, iNewMaxActCompNum) = self.GetWandGroveNum()
        for iPos, (iCompSID, iCompLevel) in self.m_ExtActCompInfo.items():
            if iPos < iNewMaxActCompNum:
                self.AddComp(WAND_COMP_TYPE_ACTION, iPos, iCompSID, iCompLevel, 'RecoveryExtActCompSaveInfo', bSync)
        
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        lstPlayer = self.m_Game.m_WarMgr.GetRoomPlayer(iCalAI = 0)
        cl_wand.net.GS2CAddWand(self.m_Game, oOwner.m_ID, lstPlayer, self)
        self.SelfRefresh()

    
    def AutoUpdateComp(self, iType, iCompSID, iCompLevel):
        lstComp = list(self.m_CompTemp[iType].items())
        lstComp.reverse()
        bResult = False
        for iPos, (iSID, iLevel) in lstComp:
            if iCompSID == iSID and iCompLevel > iLevel:
                iRet = self.AddCustomComp(iType, iPos, iCompSID, iCompLevel, sReason = 'AutoUpdateComp')
                if not iRet:
                    continue
                bResult = True
                if iLevel == 1:
                    break
                iCompLevel = iLevel
        
        return bResult

    
    def HasWandAbility(self, iWandAbility):
        return iWandAbility in self.m_WandAbility

    
    def AddWandAbility(self, iWandAbility, iQuality = 0, iFloatingRange = 0, sReason = ''):
        if not self.ValidAddWandAbility(iWandAbility, iQuality):
            return 0
        oOwner = self.GetOwner()
        if not oOwner:
            return 0
        WandLog.Debug('%s %s %s addwandability %s %s %s %s %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, self.m_SID, self.m_ID, iWandAbility, iQuality, iFloatingRange, sReason))
        self.m_WandAbility[iWandAbility] = (iQuality, iFloatingRange)
        if self.m_Enable:
            oWandAbility = oOwner.AddPerform(iWandAbility, 1, iItem = self.m_ID, iEnable = 0)
            if oWandAbility:
                oWandAbility.SetQuality(iQuality, iFloatingRange)
                lstEvolutionPointAbility = GetWandPointAbility(self.m_EvolutionTarget)
                if iWandAbility not in lstEvolutionPointAbility:
                    oWandAbility.Enable(oOwner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND, self.GetOwner(), {
            'Wand': self.m_ID,
            'Ability': iWandAbility }, oGame = self.m_Game, iSub = WAND_SUBMSG_ADDABILITY)
        return 1

    
    def ValidAddWandAbility(self, iWandAbility, iQuality):
        oOwner = self.GetOwner()
        if not oOwner:
            return 0
        if self.m_Quality != WAND_QUALITY_TALE:
            WandLog.Debug('%s %s %s wandquality:%s not tale' % (self.m_Game.m_ID, oOwner.m_PlayerID, self.m_SID, self.m_Quality))
            return 0
        clsAbility = cl_perform.GetPerformModule(iWandAbility)
        if not clsAbility or clsAbility.m_PFType != PF_TYPE_WANDABILITY:
            WandLog.Debug('%s %s %s ability:%s type:%s not ability' % (self.m_Game.m_ID, oOwner.m_PlayerID, self.m_SID, iWandAbility, clsAbility.m_PFType))
            return 0
        if clsAbility.m_QualityValue and iQuality not in clsAbility.m_QualityValue:
            WandLog.Debug('%s %s %s ability:%s %s no quality:%s' % (self.m_Game.m_ID, oOwner.m_PlayerID, self.m_SID, iWandAbility, clsAbility.m_QualityValue, iQuality))
            return 0
        return 1

    
    def RemoveWandAbility(self, iWandAbility, sReason):
        oOwner = self.GetOwner()
        if not oOwner:
            return 0
        oGame = self.m_Game
        if iWandAbility not in self.m_WandAbility:
            WandLog.Alert('%s %s no wandability %s %s %s %s' % (oGame.m_ID, oOwner.m_PlayerID, self.m_SID, self.m_ID, iWandAbility, sReason))
            return 0
        WandLog.Debug('%s %s removewandability %s %s  %s %s' % (oGame.m_ID, oOwner.m_PlayerID, self.m_SID, self.m_ID, iWandAbility, sReason))
        self.m_WandAbility.pop(iWandAbility)
        if iWandAbility in self.m_LockWandAbility:
            self.m_LockWandAbility.remove(iWandAbility)
        if self.m_Enable:
            oOwner.RemovePerform(iWandAbility)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WAND, self.GetOwner(), {
            'Wand': self.m_ID,
            'Ability': iWandAbility }, oGame = self.m_Game, iSub = WAND_SUBMSG_REMOVEABILITY)
        return 1

    
    def InitWandAbility(self, sReason):
        oOwner = self.GetOwner()
        if not oOwner.HasSeasonTalent(UNLOCK_WANDABILITY_SEASONTALENT):
            return None
        if self.QueryTmp('BanInitAbility', 0):
            return None
        if self.m_WandAbility:
            return None
        if self.GetWandQuality() != WAND_QUALITY_TALE:
            return None
        if self.QueryTmp('Reason', 0) == 'gm_create_max_wand':
            return None
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        if not oWandElement or not (oWandElement.m_Enable):
            return None
        if self.UseCarryWandAbility(sReason):
            return None
        iNegativeRatio = oWandElement.GetNegativeRatio()
        dNotNegativeWeight = oWandElement.GetAbilityQualityWeight(iHasNegative = 0)
        dHasNegativeWeight = oWandElement.GetAbilityQualityWeight(iHasNegative = 1)
        lstAbility = self.ChooseWandAbility(iNegativeRatio, dHasNegativeWeight, dNotNegativeWeight, sReason = sReason)
        if not lstAbility:
            return None
        self.SetWandAbility(lstAbility, sReason)

    
    def UseCarryWandAbility(self, sReason):
        if not self.m_CarryWandAbility:
            return False
        self.SetWandAbility(self.m_CarryWandAbility, sReason, 1)
        return True

    
    def ChooseWandAbility(self, iNegativeRatio, dHasNegativeyWeight, dNotNegativeyWeight, dCertainlyQuality = None, sReason = '', iRetainLockWandAbility = 0, iPointAbilityWeight = 0, dLockAppointWeight = None):
        if self.GetWandQuality() != WAND_QUALITY_TALE:
            return { }
        oGame = self.m_Game
        oWandElement = oGame.m_WarMgr.GetWandElement()
        if not oWandElement or not (oWandElement.m_Enable):
            return { }
        iChooseNum = MAX_WANDABILITY_NUM
        lstAbility = []
        dExclude = { }
        iGWandPointAbility = GetGWandPointAbility(self.m_SID)
        iPWandPointAbility = GetPWandPointAbility(self.m_SID)
        bUsePointAbility = False
        dAbilityQualityWeight = { }
        if iRetainLockWandAbility and self.m_LockWandAbility:
            for iLockWandAbility in self.m_LockWandAbility:
                if iLockWandAbility not in self.m_WandAbility:
                    continue
                iChooseNum -= 1
                if dLockAppointWeight and not dAbilityQualityWeight:
                    dAbilityQualityWeight = dLockAppointWeight
                (iQuality, iFloatingRange) = self.m_WandAbility[iLockWandAbility]
                lstAbility.append([
                    iLockWandAbility,
                    iQuality,
                    iFloatingRange])
                if iLockWandAbility in (iGWandPointAbility, iPWandPointAbility):
                    bUsePointAbility = True
                    dExclude[iGWandPointAbility] = 1
                    dExclude[iPWandPointAbility] = 1
                    continue
                dExclude[iLockWandAbility] = 1
            
        lstChooseQuality = []
        if dCertainlyQuality and not dAbilityQualityWeight:
            for iCertainlyQuality, iNum in dCertainlyQuality.items():
                for _ in range(iNum):
                    if not iChooseNum:
                        break
                    iChooseNum -= 1
                    lstChooseQuality.append(iCertainlyQuality)
                
            
        if iChooseNum:
            if oGame.Random(100) < iNegativeRatio:
                iChooseNum -= 1
                lstChooseQuality.append(ABILITY_QUALITY_NEGATIVE)
                if not dAbilityQualityWeight:
                    dAbilityQualityWeight = dHasNegativeyWeight
                elif not dAbilityQualityWeight:
                    dAbilityQualityWeight = dNotNegativeyWeight
            if None:
                for _ in range(iChooseNum):
                    iQuality = ChooseKey(oGame, dAbilityQualityWeight)
                    lstChooseQuality.append(iQuality)
                
        lstWandExcludeAbility = GetWandExcludeAbility(self.m_SID)
        if lstWandExcludeAbility:
            dExclude.update(dict.fromkeys(lstWandExcludeAbility, 1))
        for iQuality in lstChooseQuality:
            iWandPointAbility = 0
            dAbilityQuality = dict(GetWandAbilityByQuality(iQuality))
            if not bUsePointAbility and iQuality == ABILITY_QUALITY_FOUR:
                iWandPointAbility = iGWandPointAbility
            elif not bUsePointAbility and iQuality == ABILITY_QUALITY_THREE:
                iWandPointAbility = iPWandPointAbility
            if iWandPointAbility:
                dAbilityQuality.update({
                    iWandPointAbility: 1 })
            setAbilityWeight = set(dAbilityQuality) - set(dExclude)
            dAbilityWeight = dict.fromkeys(setAbilityWeight, 1)
            if iWandPointAbility in dAbilityWeight and iPointAbilityWeight and oGame.Random(100) < iPointAbilityWeight:
                iAbility = iWandPointAbility
                bUsePointAbility = True
            else:
                iAbility = ChooseKey(oGame, dAbilityWeight)
                if iAbility == iWandPointAbility:
                    bUsePointAbility = True
            if not iAbility:
                WandLog.Debug('%s %s chooseability null %s %s %s %s' % (self.m_Game.m_ID, self.GetPlayerID(), self.m_SID, self.m_ID, iQuality, sReason))
                continue
            clsAbility = cl_perform.GetPerformModule(iAbility)
            if not clsAbility:
                WandLog.Debug('%s %s chooseability none %s %s %s %s' % (self.m_Game.m_ID, self.GetPlayerID(), self.m_SID, self.m_ID, iAbility, sReason))
                continue
            if clsAbility.CheckCanFloating():
                iFloatingRange = oWandElement.GetRandomAbilityFloatingRange(iQuality, clsAbility.GetFlotingType())
            else:
                iFloatingRange = 0
            lstAbility.append([
                iAbility,
                iQuality,
                iFloatingRange])
            dExclude[iAbility] = 1
        
        WandLog.Debug('%s %s chooseability %s %s %s %s' % (self.m_Game.m_ID, self.GetPlayerID(), self.m_SID, self.m_ID, lstAbility, sReason))
        return lstAbility

    
    def SetWandAbility(self, lstAbility, sReason, iIsUseCarryAbility = 0):
        oOwner = self.GetOwner()
        if not oOwner.HasSeasonTalent(UNLOCK_WANDABILITY_SEASONTALENT):
            return None
        self.Set('UseCarryWandAbility', iIsUseCarryAbility)
        WandLog.Debug('%s %s setwandability %s %s %s %s' % (self.m_Game.m_ID, self.GetPlayerID(), self.m_SID, self.m_ID, lstAbility, sReason))
        lstLockWandAbility = list(self.m_LockWandAbility)
        for iAbility in list(self.m_WandAbility):
            self.RemoveWandAbility(iAbility, sReason)
        
        for iAbility, iQuality, iFloatingRange in lstAbility:
            self.AddWandAbility(iAbility, iQuality, iFloatingRange, sReason)
        
        for iLockWandAbility in lstLockWandAbility:
            if iLockWandAbility not in self.m_WandAbility:
                continue
            self.LockWandAbility(iLockWandAbility, iLock = 1)
        

    
    def LockWandAbility(self, iAbility, iLock):
        if iAbility not in self.m_WandAbility:
            return None
        if iLock and len(self.m_LockWandAbility) >= WANDABILITY_LOCKMAX:
            return None
        WandLog.Debug('%s %s lockwandability %s %s %s %s %s' % (self.m_Game.m_ID, self.GetPlayerID(), self.m_SID, self.m_ID, iAbility, iLock, self.m_LockWandAbility))
        if iLock or iAbility not in self.m_LockWandAbility:
            self.m_LockWandAbility.append(iAbility)
        elif iAbility in self.m_LockWandAbility:
            self.m_LockWandAbility.remove(iAbility)

    
    def GetLockWandAbility(self):
        return self.m_LockWandAbility

    
    def SetCarryAbility(self, lstAbility):
        self.m_CarryWandAbility = lstAbility

    
    def SetMinTriggerAllCompNum(self, sKey, iNum):
        self.m_MinTriggerAllCompInfo[sKey] = iNum
        self.RefreshMinTriggerAllCompNum()

    
    def ClearMinTriggerAllCompNum(self, sKey):
        if sKey not in self.m_MinTriggerAllCompInfo:
            return None
        del self.m_MinTriggerAllCompInfo[sKey]
        self.RefreshMinTriggerAllCompNum()

    
    def RefreshMinTriggerAllCompNum(self):
        (iConditionCompNum, _) = self.m_GrooveNum
        self.m_MinTriggerAllCompNum = min(self.m_MinTriggerAllCompInfo.values()) if self.m_MinTriggerAllCompInfo else iConditionCompNum

    
    def GetCompIconNum(self, iType):
        dComp = self.m_CompTemp[iType]
        dIcon = { }
        for iCompSID, _ in dComp.values():
            iIconSID = GetWandCompIcon(iCompSID)
            if not iIconSID:
                continue
            dIcon[iIconSID] = 1
        
        return len(dIcon)

    
    def GetSubCompNum(self, iType, iSubType, sInitFlag = None):
        dComp = self.m_Comp[iType]
        iNum = 0
        for oComp in dComp.values():
            if oComp.m_SubType != iSubType:
                continue
            if sInitFlag and oComp.m_InitFlag != sInitFlag:
                continue
            iNum += 1
        
        return iNum

    
    def RemoveCompByInitFlag(self, iType, sInitFlag, bSyncSameWand):
        if iType not in self.m_Comp:
            return None
        sReason = 'RemoveCompByInitFlag-%s' % sInitFlag
        lstAllComp = list(self.m_Comp[iType])
        for iPos in lstAllComp:
            if iPos not in self.m_Comp[iType]:
                continue
            if self.m_Comp[iType][iPos].m_InitFlag != sInitFlag:
                continue
            self.RemoveComp(iType, iPos, sReason, bSyncSameWand)
        

    
    def GetEquipCompNum(self, iType, iComp, iLevel):
        iNum = 0
        tComp = (iComp, iLevel)
        for iPos, tEquipComp in self.m_CompTemp[iType].items():
            if self.IsFromConEquip(iType, iPos) and tComp == tEquipComp:
                iNum += 1
        
        return iNum

    
    def IsFromConEquip(self, iType, iPos):
        oComp = self.GetCompByPos(iType, iPos)
        if not oComp:
            return 0
        if oComp.m_SubType == WAND_SUBTYPE_COPY:
            return 0
        if not self.ValidDismantlePos(iType, iPos):
            return 0
        return 1

    
    def IsExtActCompPos(self, iPos):
        (_, _, iBaseActNum, _) = self.m_LevelInfo[self.m_Grade][:4]
        if iPos < iBaseActNum or iPos >= iBaseActNum + self.m_ExtActionCompNum:
            return False
        return True

    
    def UpdateExtActCompCache(self, iCompType, iPos, iCompSID, iLevel, iAdd):
        if self.m_SID != PAIR_WAND or iCompType != WAND_COMP_TYPE_ACTION or not self.IsExtActCompPos(iPos):
            return None
        if iAdd:
            self.m_ExtActionCompCache[iPos] = (iCompSID, iLevel)
        else:
            self.m_ExtActionCompCache.pop(iPos, None)

    
    def TryUseExtActCompCache(self):
        if self.m_SID != PAIR_WAND:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        oWanCon = oOwner.m_WandCon
        dActComp = self.m_Comp[WAND_COMP_TYPE_ACTION]
        for iPos, (iCompSID, iCompLevel) in self.m_ExtActionCompCache.items():
            if not self.IsExtActCompPos(iPos) or iPos in dActComp or not oWanCon.CheckBagComp(self, WAND_COMP_TYPE_ACTION, iCompSID, iCompLevel):
                continue
            self.AddComp(WAND_COMP_TYPE_ACTION, iPos, iCompSID, iCompLevel, 'useextactcompcache')
        
        wandnet.GS2CUpdateWandComp(self.m_Game, self.m_Owner, oWanCon.GetSendPlayer(self.m_ID), self)



class CWandComp(object):
    m_SID = 0
    m_Type = 0
    m_Level = 1
    m_Tag = ()
    m_ActionInfo = { }
    m_TriggerActionInfo = { }
    m_CBFuncAction = { }
    m_TriggerType = 0
    m_PresetAction = None
    m_CopyWandTimes = 0
    m_SubType = WAND_SUBTYPE_NORMAL
    
    def __init__(self, oOwner, iItem, iCurLevel, iPos, iSubType, sInitFlag):
        self.m_Owner = oOwner.m_ID
        self.m_Game = oOwner.m_Game
        self.m_ID = oOwner.m_Game.NewNoSceneObjID()
        self.m_Key = 'WC%d-%d' % (self.m_SID, self.m_ID)
        self.m_Item = iItem
        self.m_Enable = 0
        self.m_Level = iCurLevel
        self.m_CurPos = iPos
        self.m_FinishCondition = 0
        self.m_ArgData = { }
        self.m_KeepData = { }
        self.m_LifeCycle = None
        self.m_ConditionCount = 0
        self.m_FinishConditionCount = 0
        self.m_ChangeFinishConditionCountFactor = 0
        self.m_CallTimes = 0
        self.m_CallTimesInfo = { }
        self.m_MaxLevel = max(self.m_ActionInfo)
        self.m_EventCB = cl_msgcenter.eventcbobj.CCycleEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_LifeCycleLevel = { }
        self.m_SubType = iSubType
        self.m_InitFlag = sInitFlag
        for iLevel, (oEnableFunc, oDisableFunc) in self.m_ActionInfo.items():
            oLifeCycle = cl_object.lifecycle.CLifeCycle()
            oLifeCycle.Init(self, oEnableFunc, oDisableFunc)
            if iLevel in self.m_TriggerActionInfo:
                oLifeCycle.RegisterFunc('TriggerAction', self.m_TriggerActionInfo[iLevel])
            self.m_LifeCycleLevel[iLevel] = oLifeCycle
        
        self.InitCallTimes()
        self.m_ShowCallTimes = 0

    
    def Release(self):
        if self.m_LifeCycle:
            self.m_LifeCycle.Release()
            self.m_LifeCycle = None
        for oLifeCycle in self.m_LifeCycleLevel.values():
            oLifeCycle.Release()
        
        self.m_LifeCycleLevel = { }
        self.m_Game = None

    
    def CheckCanCopy(self):
        if not (self.m_Enable) or not (self.m_CopyWandTimes):
            return False
        return True

    
    def SetShowCallTimes(self, iValue):
        self.m_ShowCallTimes = iValue

    
    def GetShowCallTimes(self):
        return self.m_ShowCallTimes

    
    def CheckNextCopyActionComp(self):
        if not self.CheckCanCopy():
            return (0, 0)
        oWand = self.GetMyItem()
        if not oWand:
            return (0, 0)
        iCurPos = self.GetCurPos()
        (_, iMaxComp) = oWand.GetWandGroveNum()
        if iCurPos >= iMaxComp - 1:
            return (0, 0)
        dWandComp = oWand.GetWandCompByType(WAND_COMP_TYPE_ACTION)
        iNextPos = iCurPos + 1
        if iNextPos not in dWandComp:
            return (0, 0)
        for iPos, oComp in dWandComp.items():
            if iPos > iCurPos and not (oComp.m_CopyWandTimes) and oComp.CanTriggerByNextPos():
                return (iPos, oComp.m_Level)
        
        return (0, 0)

    
    def InitCallTimes(self):
        if self.m_CopyWandTimes:
            self.SetCallTimesInfo('CopyCompInit', self.m_CopyWandTimes)
        else:
            self.SetCallTimesInfo('CompInit', 1)

    
    def SetCallTimesInfo(self, sKey, iCallTimes):
        self.m_CallTimesInfo[sKey] = iCallTimes
        self.m_CallTimes = sum(self.m_CallTimesInfo.values())

    
    def RemoveCallTimesInfo(self, sKey):
        if sKey in self.m_CallTimesInfo:
            self.m_CallTimesInfo.pop(sKey)
            self.m_CallTimes = sum(self.m_CallTimesInfo.values())

    
    def GetPreviousCopyComp(self):
        oWand = self.GetMyItem()
        if not oWand:
            return []
        iCurPos = self.GetCurPos()
        if iCurPos <= 0:
            return []
        lstCopyCompPos = []
        dWandComp = oWand.GetWandCompByType(WAND_COMP_TYPE_ACTION)
        for iPreviousPos in range(iCurPos - 1, -1, -1):
            if iPreviousPos not in dWandComp:
                return lstCopyCompPos
            if not dWandComp[iPreviousPos].m_CopyWandTimes:
                return lstCopyCompPos
            lstCopyCompPos.append(iPreviousPos)
        
        return lstCopyCompPos

    
    def CopyActionCompEffect(self, iPos, iLevel):
        if not self.CheckCanCopy():
            return None
        oWand = self.GetMyItem()
        if not oWand:
            return None
        oTargetComp = oWand.GetCompByPos(WAND_COMP_TYPE_ACTION, iPos)
        if not oTargetComp:
            self.SetKeepValue('CopyTargetSID', 0)
            return None
        if iLevel in oTargetComp.m_ActionInfo:
            (oEnableFunc, oDisableFunc) = oTargetComp.m_ActionInfo[iLevel]
            if oEnableFunc:
                self.m_LifeCycle.RegisterFunc('Enable', oEnableFunc)
            if oDisableFunc:
                self.m_LifeCycle.RegisterFunc('Disable', oDisableFunc)
            self.SetKeepValue('CopyTargetSID', oTargetComp.m_SID)
        if iLevel in oTargetComp.m_TriggerActionInfo:
            self.m_LifeCycle.RegisterFunc('TriggerAction', oTargetComp.m_TriggerActionInfo[iLevel])
        if oTargetComp.m_CBFuncAction:
            self.m_EventCB = cl_msgcenter.eventcbobj.CCycleEventCB(oTargetComp.m_CBFuncAction, self.m_Key)

    
    def ClearCopyEffect(self):
        if not self.CheckCanCopy():
            return None
        self.SetKeepValue('CopyTargetSID', 0)
        for sKey in ('Enable', 'Disable', 'TriggerAction'):
            self.m_LifeCycle.DumpFunc(sKey)
        
        self.m_EventCB = cl_msgcenter.eventcbobj.CCycleEventCB(self.m_CBFuncAction, self.m_Key)

    
    def SetOwner(self, iOwner):
        self.m_Owner = iOwner

    
    def GetOwner(self):
        if not self.m_Game:
            return None
        return self.m_Game.GetObject(self.m_Owner)

    
    def GetMyItem(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if self.m_Item:
            return oOwner.m_WandCon.GetWandByID(self.m_Item)

    
    def Key(self):
        return self.m_Key

    
    def Enable(self):
        oOwner = self.GetOwner()
        if not oOwner or not (oOwner.m_OnGame):
            return None
        if self.m_Enable or self.m_Level not in self.m_LifeCycleLevel:
            return None
        oWand = self.GetMyItem()
        if not oWand or not (oWand.m_LifeCycle.m_Enable):
            return None
        self.m_Enable = 1
        self.m_LifeCycle = self.m_LifeCycleLevel[self.m_Level]
        if self.m_Type == WAND_COMP_TYPE_ACTION:
            if self.CheckCanCopy():
                (iTargetPos, iTargetLevel) = self.CheckNextCopyActionComp()
                if iTargetPos and iTargetLevel:
                    self.CopyActionCompEffect(iTargetPos, iTargetLevel)
                    self.EnableCopyChain(oOwner, oWand, iTargetPos, iTargetLevel)
                elif self.CanTriggerByNextPos():
                    self.EnableCopyChain(oOwner, oWand, self.m_CurPos, self.m_Level)
        None.m_LifeCycle.Enable(oOwner)

    
    def Disable(self, iReleaseFlag = 0):
        if not (self.m_Enable) or self.m_Level not in self.m_LifeCycleLevel:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if iReleaseFlag:
            self.m_LifeCycle.PFAndStateDisable(oOwner)
        else:
            self.m_LifeCycle.Disable(oOwner)
        oWand = self.GetMyItem()
        if not oWand:
            return None
        if self.m_Type == WAND_COMP_TYPE_ACTION:
            self.DisableCopyChain(oOwner, oWand)
        self.m_LifeCycle = None
        self.m_Enable = 0
        self.ClearComp()

    
    def EnableCopyChain(self, oOwner, oWand, iTargetPos, iTargetLevel):
        for iPos in self.GetPreviousCopyComp():
            oCopyComp = oWand.GetCompByPos(WAND_COMP_TYPE_ACTION, iPos)
            oCopyComp.CopyActionCompEffect(iTargetPos, iTargetLevel)
            oCopyLifeCycle = oCopyComp.m_LifeCycle
            if oCopyLifeCycle and oCopyLifeCycle.m_Enable:
                oCopyLifeCycle.CallFunc('Enable', oOwner)
        

    
    def DisableCopyChain(self, oOwner, oWand):
        for iPos in self.GetPreviousCopyComp():
            oCopyComp = oWand.GetCompByPos(WAND_COMP_TYPE_ACTION, iPos)
            oCopyLifeCycle = oCopyComp.m_LifeCycle
            if oCopyLifeCycle:
                oCopyLifeCycle.CallFunc('Disable', oOwner)
            oCopyComp.ClearCopyEffect()
        

    
    def ClearComp(self):
        self.m_ArgData = { }
        self.m_FinishCondition = 0

    
    def SetLevel(self, iLevel):
        if iLevel not in self.m_LifeCycleLevel:
            return None
        if self.m_Enable:
            self.Disable()
            self.m_Level = iLevel
            self.Enable()
        else:
            self.m_Level = iLevel

    
    def GetCompMaxLevel(self):
        return self.m_MaxLevel

    
    def CheckFinish(self):
        return self.m_FinishCondition

    
    def SetFinishConditionCount(self, iCount):
        if not self.VaildConditionCount():
            return None
        if self.m_ChangeFinishConditionCountFactor:
            self.SetKeepValue('BaseFinshCount', iCount)
            iCount = iCount * (100 + self.m_ChangeFinishConditionCountFactor) // 100
        self.m_FinishConditionCount = iCount if iCount >= 1 else 1
        self.TriggerWandComp()

    
    def SetConditionCount(self, iCount):
        self.AddConditionCount(iCount - self.m_ConditionCount)

    
    def AddConditionCount(self, iCount):
        if not self.VaildConditionCount():
            return None
        if not self.m_FinishConditionCount:
            return None
        self.m_ConditionCount += iCount
        self.TriggerWandComp()

    
    def VaildConditionCount(self):
        if not (self.m_Enable) or not (self.m_Type == WAND_COMP_TYPE_CONDITION):
            return False
        oWand = self.GetMyItem()
        if not oWand or oWand.QueryTmp('ForbidCompCount', 0):
            return False
        return True

    
    def TriggerWandComp(self):
        iFinishCount = self.m_ConditionCount // self.m_FinishConditionCount
        for _ in range(iFinishCount):
            if self.m_ConditionCount < self.m_FinishConditionCount:
                break
            self.m_ConditionCount -= self.m_FinishConditionCount
            self.FinishCondition()
        
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        if not oWandElement or not (oWandElement.m_Enable):
            return None
        oWandElement.CacheCompCnt(self.m_Owner, self.m_Item, self.m_ID)

    
    def GS2CWandConditionCompCountChange(self):
        if not self.m_FinishConditionCount:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iCount = self.m_FinishConditionCount - self.m_ConditionCount
        if iCount < 0:
            WandLog.TraceAlert('%d %d compcounterr %d %d %d' % (self.m_Game.m_ID, oOwner.m_PlayerID, self.m_SID, self.m_FinishConditionCount, self.m_ConditionCount))
            iCount = 0
        wandnet.GS2CWandConditionCompCountChange(self.m_Game, oOwner.m_PlayerID, self.m_Item, self.m_SID, iCount)

    
    def GetConditionCount(self):
        return self.m_ConditionCount

    
    def FinishCondition(self):
        if not (self.m_Enable) or not (self.m_Type == WAND_COMP_TYPE_CONDITION):
            return None
        self.m_ArgData = { }
        self.m_FinishCondition = 1
        oWand = self.GetMyItem()
        if oWand:
            oWand.OnFinishConditionComp(self)

    
    def ResetCondition(self, iOnlyResetArg = 0):
        if not self.m_Type == WAND_COMP_TYPE_CONDITION:
            return None
        self.m_ArgData = { }
        self.m_ConditionCount = 0
        oWandElement = self.m_Game.m_WarMgr.GetWandElement()
        oWandElement.CacheCompCnt(self.m_Owner, self.m_Item, self.m_ID)
        if iOnlyResetArg:
            return None
        self.m_FinishCondition = 0

    
    def WandActCompTriggerInfo(self, iNeedCount, iCount, iTime):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iEndFrame = self.m_Game.GetFrameNum() + Time2Frame(iTime)
        wandnet.GS2CWandActCompTrigger(self.m_Game, oOwner.m_PlayerID, self.m_Item, self.m_CurPos, iNeedCount, iCount, iEndFrame, iTime)

    
    def TriggerAction(self, iWandCallTimes):
        if not self.m_Enable:
            return None
        if not self.m_LifeCycle:
            return None
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if self.m_TriggerType != WAND_ACTCOMP_CONTINUE:
            wandnet.GS2CWandActCompInstantTrigger(self.m_Game, oOwner.m_PlayerID, self.m_Item, self.m_CurPos)
        iCurLevel = self.m_Level
        for _ in range(self.m_CallTimes + iWandCallTimes):
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WANDCOMP, self.GetOwner(), {
                'Quality': iCurLevel,
                'CurPos': self.m_CurPos }, oGame = self.m_Game, iSub = WANDCOMP_TRIGGER_ACTION)
            self.m_LifeCycle.CallFunc('TriggerAction', oOwner)
        

    
    def AttrCache(self):
        dData = {
            'SID': self.m_SID,
            'PFLV': self.m_Level,
            'Key': self.m_Key,
            'Type': self.m_Type,
            'Owner': self.m_Owner,
            'ArgData': dict(self.m_ArgData),
            'ItemID': self.m_ID,
            'RS': cl_object.reason.CStrReason(self.m_Key, dData = {
                'Item': self.m_ID }) }
        return dData

    
    def GetLifeCycleLevel(self):
        return self.m_Level

    
    def GetCurPos(self):
        return self.m_CurPos

    
    def GetArgValue(self, key, default = 0):
        if key not in self.m_ArgData:
            return default
        return self.m_ArgData[key]

    
    def SetArgValue(self, key, val):
        self.m_ArgData[key] = val

    
    def SetArgValueDefault(self, key, val):
        if key not in self.m_ArgData:
            self.m_ArgData[key] = val
            return val
        return self.m_ArgData[key]

    
    def AddArgValue(self, key, value):
        if key in self.m_ArgData:
            self.m_ArgData[key] += value
        else:
            self.m_ArgData[key] = value

    
    def DelArgValue(self, key):
        if key in self.m_ArgData:
            self.m_ArgData.pop(key)

    
    def GetKeepValue(self, key, default = 0):
        if key not in self.m_KeepData:
            return default
        return self.m_KeepData[key]

    
    def SetKeepValue(self, key, val):
        self.m_KeepData[key] = val

    
    def AddKeepValue(self, key, value):
        if key in self.m_KeepData:
            self.m_KeepData[key] += value
        else:
            self.m_KeepData[key] = value

    
    def DelKeepValue(self, key):
        if key in self.m_KeepData:
            self.m_KeepData.pop(key)

    
    def CanTriggerByNextPos(self):
        if self.m_SID in WANDCOMP_NOTRIGGER_NEXTPOS:
            return False
        return True


