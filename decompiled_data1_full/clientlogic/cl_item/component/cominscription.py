# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_item/component/cominscription.pyc
# RelativePath: clientlogic/cl_item/component/cominscription.pyc
# Source Generated with Decompyle++
# File: cominscription.pyc (Python 3.6)

from cl_only import ChooseKey, ShufferList, Functor, ChooseMulKeys, SendAlert
from cl_commondefines import BAG_TYPE_WIELD, INSCRIPTION_TYPE_NORMAL, INSCRIPTION_TYPE_RARE, INSCRIPTION_TYPE_GEMINI, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, ITEMPERFORM_ENABLE_UNHOLD, ITEMPERFORM_ENABLE_MAINHOLD, UPINS_TO_RARE, UPINS_TO_EXCLUSIVE, UPINS_TO_RARE_ALL, INSCRIPTION_STATE_SEALED, INSCRIPTION_STATE_DISBLE, PF_TYPE_INSCRIPTION, UPGRADE_INS_RS_COMMON, INSCRIPTION_STATE_SHARE
from cl_platformdata import GetInscriptionLib
from cl_object.logging import WarrewardLog
from cl_inscriptionpool import GetInscritionPool
from cl_item.defines import MAIN_HOLD
from .mobject import CItemComponent
import cl_item.defines as itemdef
import cl_perform
import cl_formula
import cl_msgcenter
MAX_INSCRIPTION_NUM = 6
BASE_GEMINI_NUM = 0
LEAST_GEMINI_NUM = 5
MAX_SEALEDINSCRIPTION_LV = 3
SEALEDINSCRIPTION_POOL = (1001, 1002, 1003)

def GetMaxInscriptionNum():
    return MAX_INSCRIPTION_NUM

g_InscriptionType2Lv = {
    INSCRIPTION_TYPE_EXCLUSIVE: 3,
    INSCRIPTION_TYPE_RARE: 2,
    INSCRIPTION_TYPE_NORMAL: 1 }
g_ActionType2UpType = {
    itemdef.WEAPON_ACTION_INSC_ONE_NORRARE2EXCLU: UPINS_TO_EXCLUSIVE,
    itemdef.WEAPON_ACTION_INSC_ALL_NOR2RARE: UPINS_TO_RARE_ALL,
    itemdef.WEAPON_ACTION_INSC_ONE_NOR2RARE: UPINS_TO_RARE }
g_GeminiInscriptionWeight = 625

class CInscriptionComponent(CItemComponent):
    
    def __init__(self, oItem, dParser):
        super(CInscriptionComponent, self).__init__(oItem, dParser)
        self.m_Inscription = []
        self.m_SealedInscription = []
        self.m_ShareInscription = []
        self.m_Type2Num = { }
        self.m_Item.AddAttention(itemdef.MSG_ITEM_ADD, self.OnItemAddToContainer, 'InscriptionCom')
        self.m_Item.AddAttention(itemdef.MSG_ITEM_REMOVE, self.OnItemRemoveFromContainer, 'InscriptionCom')
        self.m_InscriptionNum = 0
        self.m_DisableInscription = { }
        self.m_TempDisableInscription = { }
        self.InitInscriptionNum()
        self.ResetInscription()
        self.m_ResetTimes = 0
        self.m_ExtraInscriptionTimes = 0
        self.m_NowSealedInscriptionLv = 0
        self.m_RecastWeight = { }

    
    def Save(self):
        dData = { }
        dData['Inscription'] = list(self.m_Inscription)
        dData['ResetTimes'] = self.m_ResetTimes
        dData['ExtraTimes'] = self.m_ExtraInscriptionTimes
        dData['SealedIns'] = self.m_SealedInscription
        dData['DisableIns'] = self.m_DisableInscription
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_ResetTimes = dData.get('ResetTimes', 0)
        self.m_ExtraInscriptionTimes = dData.get('ExtraTimes', 0)
        lstInscription = dData.get('Inscription', [])
        self.m_InscriptionNum = len(lstInscription)
        self.CleanInscription()
        for iSID in lstInscription:
            self.AppendInscription(iSID)
        
        lstSealedInscription = dData.get('SealedIns', [])
        if lstSealedInscription:
            self.m_SealedInscription = lstSealedInscription
        elif lstInscription and self.m_Item.m_Game.m_WarMgr.IsUseSealedInscription():
            self.m_SealedInscription = []
            self.InitSealedInscription()
        self.m_DisableInscription = dict.fromkeys(dData.get('DisableIns', { }), 1)
        for iInscription in self.m_DisableInscription:
            self.DisableInscription(iInscription)
        
        self.RefreshDisbleInscription()

    
    def Release(self):
        oItem = self.m_Item
        if oItem:
            oItem.DoneAttention(itemdef.MSG_ITEM_ADD, 'InscriptionCom')
            oItem.DoneAttention(itemdef.MSG_ITEM_REMOVE, 'InscriptionCom')
            oItem.DoneAttention(itemdef.MSG_ITEM_REMOVE, 'SealedInscription')
            for sKey in self.m_TempDisableInscription:
                oItem.DoneAttention(itemdef.MSG_ITEM_UNHOLD, sKey)
            
        self.m_TempDisableInscription = { }
        super().Release()

    
    def InitInscriptionNum(self):
        dTmpData = self.m_Item.m_TmpData
        if 'NotInitInscription' in dTmpData:
            return None
        iNum = dTmpData.get('InscriptionNum', 0)
        iTempInsNumUpperLimit = dTmpData.get('TempInsNumUpperLimit', MAX_INSCRIPTION_NUM)
        if not iNum:
            oGame = self.m_Item.m_Game
            oWarMgr = oGame.m_WarMgr
            oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
            if not oLevelCtrl:
                return None
            iLayer = oLevelCtrl.m_LayerNum
            iLevel = oLevelCtrl.m_LevelNum
            iNum = oGame.m_WarData.GetInscriptionNum(iLayer, iLevel, oLevelCtrl)
        if iNum > iTempInsNumUpperLimit:
            iNum = iTempInsNumUpperLimit
        self.m_InscriptionNum = iNum

    
    def GetAllInscription(self, iFill = 1, lstDisable = None, iIgnoreDisable = 1):
        lstPerform = self.m_Inscription[:]
        if iIgnoreDisable:
            if not lstDisable:
                lstDisable = self.GetDisableInscription()
            for iPerform in lstDisable:
                if iPerform in lstPerform:
                    lstPerform.remove(iPerform)
            
        if iFill and len(lstPerform) < MAX_INSCRIPTION_NUM:
            lstPerform.extend([
                0] * (MAX_INSCRIPTION_NUM - len(lstPerform)))
        return lstPerform

    
    def GetInscriptionByType(self, iType):
        lstCur = []
        for iPerform in self.m_Inscription:
            clsPerform = cl_perform.GetPerformModule(iPerform)
            if clsPerform.m_InscriptionType != iType:
                continue
            lstCur.append(iPerform)
        
        return lstCur

    
    def GetInscriptionNum(self):
        return self.m_InscriptionNum

    
    def GetExtraInscriptionTimes(self):
        return self.m_ExtraInscriptionTimes

    
    def GetRecastTimes(self):
        return self.m_ResetTimes

    
    def GetInscriptionLib(self):
        oItem = self.m_Item
        if not oItem.m_ExtInscriptionWeight:
            return GetInscriptionLib()
        return oItem.m_ExtInscriptionWeight

    
    def RecastGemini(self):
        self.m_ResetTimes += 1
        lstCur = []
        lstInscription = list(self.m_Inscription)
        for iPerform in lstInscription:
            clsPerform = cl_perform.GetPerformModule(iPerform)
            if clsPerform.m_InscriptionType != INSCRIPTION_TYPE_GEMINI:
                continue
            self.RemoveInscription(iPerform)
            lstCur.append(iPerform)
        
        if not self.m_RecastWeight:
            dAll = GetInscriptionLib()
            if INSCRIPTION_TYPE_GEMINI not in dAll:
                return None
            for iSID, iWeight in dAll[INSCRIPTION_TYPE_GEMINI].items():
                if iWeight <= 0:
                    continue
                if self.ValidAddInscription(iSID) or iSID in lstCur:
                    self.m_RecastWeight[iSID] = g_GeminiInscriptionWeight // 5
                    continue
                self.m_RecastWeight[iSID] = g_GeminiInscriptionWeight
            
            if not self.m_RecastWeight:
                return None
        iNum = self.GetInscriptionNum()
        iCur = len(self.m_Inscription)
        if iNum > iCur:
            iChooseNum = iNum - iCur
            if iChooseNum > 1:
                iChooseNum = 1
                oItem = self.m_Item
                oGame = oItem.m_Game
                if oItem and oGame:
                    oOwner = oItem.GetOwner()
                    if oGame and oOwner:
                        WarrewardLog.TraceAlert('%d %s recastgemini err %s %s %s %s %s %s' % (oGame.m_ID, oOwner.m_PlayerID, oItem.m_SID, oItem.m_Grade, lstInscription, self.m_Inscription, iNum, iCur))
            self.ChooseGeminiInscription(iChooseNum, lstCur)
        self.m_Item.GS2CItemPropChange('Inscription', self.GetAllInscription())

    
    def Recast(self):
        self.m_ResetTimes += 1
        self.ResetInscription()
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECAST_INSCRIPTION, oOwner, {
                'ItemID': self.m_Item.m_ID })

    
    def ResetInscriptionNum(self, iNum):
        if iNum > MAX_INSCRIPTION_NUM:
            iNum = MAX_INSCRIPTION_NUM
        if self.m_InscriptionNum == iNum:
            return None
        self.m_InscriptionNum = iNum
        self.ResetInscription()

    
    def GetInscriptionNumByType(self, iInscriptionType):
        return self.m_Type2Num.get(iInscriptionType, 0)

    
    def GetEnableInscriptionNumByType(self, iInscriptionType):
        iNum = self.m_Type2Num.get(iInscriptionType, 0)
        if self.m_NowSealedInscriptionLv:
            if self.m_NowSealedInscriptionLv == 1 and iInscriptionType == INSCRIPTION_TYPE_NORMAL:
                iNum += 1
            elif self.m_NowSealedInscriptionLv == 2 and iInscriptionType == INSCRIPTION_TYPE_RARE:
                iNum += 1
            elif self.m_NowSealedInscriptionLv == 3 and iInscriptionType == INSCRIPTION_TYPE_EXCLUSIVE:
                iNum += 1
        iSubNum = 0
        lstPerfromSID = self.GetDisableInscription()
        for iPerformSID in lstPerfromSID:
            clsPerform = cl_perform.GetPerformModule(iPerformSID)
            if clsPerform.m_InscriptionType == iInscriptionType:
                iSubNum += 1
        
        iNum -= iSubNum
        return iNum

    
    def ValidUpgradeActionType(self, iActionType):
        if iActionType not in g_ActionType2UpType:
            return 0
        return self.ValidUpgradeByUptype(g_ActionType2UpType[iActionType])

    
    def ValidUpgradeByUptype(self, sUpType):
        iTargetType = 0
        lstOptionType = []
        iOpenTempExclusive = 0
        if sUpType in [
            UPINS_TO_RARE,
            UPINS_TO_RARE_ALL]:
            iTargetType = INSCRIPTION_TYPE_RARE
            lstOptionType = [
                INSCRIPTION_TYPE_NORMAL]
        elif sUpType == UPINS_TO_EXCLUSIVE:
            iTargetType = INSCRIPTION_TYPE_EXCLUSIVE
            lstOptionType = [
                INSCRIPTION_TYPE_NORMAL,
                INSCRIPTION_TYPE_RARE]
            iTempExclusiveInscription = self.m_Item.m_TmpData.get('TempExclusiveInscription', 0)
            if not iTempExclusiveInscription:
                iOpenTempExclusive = 1
                self.m_Item.m_TmpData['TempExclusiveInscription'] = 3
        (iAdd, _) = self.ChooseInscriptionByType(iTargetType, 1, iAppend = 0)
        if not iAdd:
            if iOpenTempExclusive:
                self.m_Item.m_TmpData.pop('TempExclusiveInscription', 0)
            return 0
        iValid = 0
        for iType in lstOptionType:
            if iType in self.m_Type2Num and self.m_Type2Num[iType]:
                iValid = 1
                break
        
        if iOpenTempExclusive:
            self.m_Item.m_TmpData.pop('TempExclusiveInscription', 0)
        return iValid

    
    def UpgradeByActionType(self, iActionType, dInfo):
        if iActionType not in g_ActionType2UpType:
            return []
        sUpType = g_ActionType2UpType[iActionType]
        if sUpType == UPINS_TO_EXCLUSIVE:
            iTempExclusiveInscription = self.m_Item.m_TmpData.get('TempExclusiveInscription', 0)
            if not iTempExclusiveInscription:
                self.m_Item.m_TmpData['TempExclusiveInscription'] = 3
        dInfo[sUpType] = 1
        return self.UpgradeInscription(dInfo)

    
    def UpgradeInscription(self, dArgs = None):
        if not isinstance(dArgs, dict):
            dArgs = { }
        iCnt = dArgs['InscriptionCnt'] if 'InscriptionCnt' in dArgs else 1
        tUpType = self.GetInscriptionUpgradeType(dArgs)
        sUpType = tUpType[0] if tUpType else UPINS_TO_RARE
        iTargetType = INSCRIPTION_TYPE_RARE
        if 'Appoint' in dArgs:
            lstCur = dArgs['Appoint']
        else:
            lstCur = self.GetInscriptionByType(INSCRIPTION_TYPE_NORMAL)
        if sUpType == UPINS_TO_RARE or not iCnt or sUpType == UPINS_TO_RARE_ALL:
            iCnt = len(lstCur)
        elif sUpType == UPINS_TO_EXCLUSIVE:
            if 'Appoint' not in dArgs:
                lstCur.extend(self.GetInscriptionByType(INSCRIPTION_TYPE_RARE))
            iTargetType = INSCRIPTION_TYPE_EXCLUSIVE
        lstCur = ShufferList(self.m_Item.m_Game, lstCur)
        lstCur = lstCur[:iCnt]
        lstUpgrade = self.ReplaceInscription(lstCur, iTargetType)
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            iReason = dArgs['Reason'] if 'Reason' in dArgs else UPGRADE_INS_RS_COMMON
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_UPGRADE_INSCRIPTION, oOwner, {
                'ItemID': self.m_Item.m_ID,
                'OldInscription': lstCur,
                'Reason': iReason })
        return lstUpgrade

    
    def ReplaceInscription(self, lstCur, iTargetType):
        oPerformCom = self.m_Item.GetComponent('Perform')
        if not oPerformCom:
            return []
        lstAllUpgrade = []
        for iSID in lstCur:
            if iSID not in self.m_Inscription:
                continue
            oPerform = oPerformCom.GetPerform(iSID)
            if oPerform:
                if oPerform.m_InscriptionType in (INSCRIPTION_TYPE_GEMINI,):
                    continue
                oOwner = self.m_Item.GetOwner()
                oPerform.Disable(oOwner)
            else:
                self.DisableAttr(iSID)
            (iRet, lstUpgrade) = self.ChooseInscriptionByType(iTargetType, 1)
            if not iRet:
                self.RemoveSealedInscription(iTargetType)
                (iRet, lstUpgrade) = self.ChooseInscriptionByType(iTargetType, 1)
            if iRet:
                lstAllUpgrade.extend(lstUpgrade)
                self.RemoveInscription(iSID)
                continue
            if oPerform:
                oPerform.Enable(oOwner)
                continue
            self.EnableAttr(iSID)
        
        self.FullSealedInscription()
        self.m_Item.GS2CItemPropChange('Inscription', self.GetAllInscription())
        return lstAllUpgrade

    
    def ValidChooseInscription(self, iType):
        dAll = GetInscriptionLib()
        if iType not in dAll:
            return 0
        if self.GetRestTypeNum(iType) < 1:
            return 0
        lstHas = self.m_Inscription
        for iSID, iWeight in dAll[iType].items():
            if not iWeight or iSID in lstHas:
                continue
            clsPerform = cl_perform.GetPerformModule(iSID)
            if clsPerform.CheckValidItem(self.m_Item, lstHas):
                return 1
        
        return 0

    
    def ExtraInscription(self):
        self.m_ExtraInscriptionTimes += 1
        self.m_Item.GS2CItemPropChange('AddInscriptionTimes')
        self.m_InscriptionNum += 1
        self.AddInscription()

    
    def GetInscriptionUpgradeType(self, dArgs):
        return tuple(set(dArgs) & set((UPINS_TO_RARE, UPINS_TO_EXCLUSIVE, UPINS_TO_RARE_ALL)))

    
    def AttrCache(self):
        lstInscription = self.GetAllInscription(iFill = 0)
        if self.m_NowSealedInscriptionLv:
            iInscription = self.m_SealedInscription[self.m_NowSealedInscriptionLv - 1]
            lstInscription.append(iInscription)
        dCache = {
            'Inscription': lstInscription }
        return dCache

    
    def CleanInscription(self):
        for iSID in self.m_Inscription[:]:
            self.RemoveInscription(iSID)
        

    
    def ResetInscription(self):
        lstExclude = []
        lstGemini = []
        if self.m_Inscription:
            lstGemini = self.GetInscriptionByType(INSCRIPTION_TYPE_GEMINI)
            lstExclude = self.m_Inscription[:]
            self.CleanInscription()
        iNum = self.m_InscriptionNum
        dTmpData = self.m_Item.m_TmpData
        lstPriorChoose = dTmpData.get('PriorInscription', [])
        if lstPriorChoose:
            self.m_Item.RemoveTmp('PriorInscription')
            for iPerform in lstPriorChoose:
                iNum -= 1
                self.AppendInscription(iPerform)
                if iNum <= 0:
                    return None
            
        if lstGemini:
            (iAdd, _) = self.ChooseInscriptionByType(INSCRIPTION_TYPE_GEMINI, 1, lstGemini)
            if not iAdd:
                self.AppendInscription(lstGemini[0])
            iNum -= 1
        iExclusiveIncription = dTmpData.get('InscriptionExclusive', 0)
        if iExclusiveIncription:
            iExclusiveIncription = min(iNum, iExclusiveIncription)
            (iAdd, _) = self.ChooseInscriptionByType(INSCRIPTION_TYPE_EXCLUSIVE, iExclusiveIncription)
            iNum -= iAdd
        iChange = self.ChooseInscription(iNum, lstExclude, iAlert = 0)
        if iChange < iNum and lstExclude:
            iLeft = iNum - iChange
            lstChoose = []
            for iPerform in lstExclude:
                if not self.ValidAddInscription(iPerform):
                    continue
                lstChoose.append(iPerform)
            
            iChooseLen = len(lstChoose)
            if iChooseLen > iLeft:
                ShufferList(self.m_Item.m_Game, lstChoose)
                lstChoose = lstChoose[:iLeft]
            elif iChooseLen < iLeft:
                oItem = self.m_Item
                WarrewardLog.Alert('%d %s reset noenough inscription %s %s' % (oItem.m_Game.m_ID, oItem.m_SID, self.m_Inscription, lstExclude))
            for iPerform in lstChoose:
                self.AppendInscription(iPerform)
            
        oGame = self.m_Item.m_Game
        if oGame.m_WarMgr.IsUseSealedInscription():
            self.InitSealedInscription()
        self.m_Item.GS2CItemPropChange('Inscription', self.GetAllInscription())

    
    def GetRestTypeNum(self, iType):
        iRest = MAX_INSCRIPTION_NUM
        if iType == INSCRIPTION_TYPE_GEMINI:
            iMax = BASE_GEMINI_NUM + self.m_Item.m_Game.m_WarMgr.Query('AdditionalGemini', 0)
            iTempGeminiInscription = self.m_Item.m_TmpData.get('TempGeminiInscription', 0)
            if iTempGeminiInscription:
                iMax = iTempGeminiInscription
            iRest = iMax - self.m_Type2Num.get(INSCRIPTION_TYPE_GEMINI, 0)
        elif iType == INSCRIPTION_TYPE_EXCLUSIVE:
            iMax = self.m_Item.m_Game.m_WarMgr.Query('ExclusiveInscription', 0)
            iTempExclusiveInscription = self.m_Item.m_TmpData.get('TempExclusiveInscription', 0)
            if iTempExclusiveInscription:
                iMax = iTempExclusiveInscription
            iRest = iMax - self.m_Type2Num.get(INSCRIPTION_TYPE_EXCLUSIVE, 0)
        return iRest

    
    def GetProp(self, iType, iGrade):
        if iType == INSCRIPTION_TYPE_GEMINI and self.m_InscriptionNum >= LEAST_GEMINI_NUM and self.m_Item.m_Game.m_WarMgr.Query('AdditionalGemini', 0):
            return 10000
        oGame = self.m_Item.m_Game
        dAllProb = oGame.m_WarData.GetInscriptionProb()
        dBaseProb = dAllProb.get(iType, { })
        if dBaseProb:
            iGrade = oGame.m_WarData.GetWeaponNewGrade(dBaseProb, iGrade)
        iBase = dBaseProb[iGrade] if iGrade in dBaseProb else 0
        dAddition = oGame.m_WarMgr.Query('AdditionalInscriptionProp', { })
        iAddition = dAddition[iType] if iType in dAddition else 0
        iPropAdd = 0
        dTmpData = self.m_Item.m_TmpData
        dPropAddByType = dTmpData.get('PropAddByType', { })
        if iType in dPropAddByType:
            for _, iAdd in dPropAddByType[iType].items():
                iPropAdd += iAdd
            
        if not iAddition:
            if iPropAdd:
                return iBase * (1 + iPropAdd / 100)
            return iBase
        if iPropAdd:
            return iBase * (1 + iAddition / 100) * (1 + iPropAdd / 100)
        return iBase * (1 + iAddition / 100)

    
    def AddInscription(self):
        iNum = self.GetInscriptionNum()
        if iNum > MAX_INSCRIPTION_NUM:
            iNum = MAX_INSCRIPTION_NUM
        iCur = len(self.m_Inscription)
        iAdd = iNum - iCur
        if not iAdd:
            return None
        self.ChooseInscription(iAdd, [], iAlert = 0)
        self.m_Item.GS2CItemPropChange('Inscription', self.GetAllInscription())

    
    def ResetInscriptionByType(self, iType, iCnt, iKeepType = None):
        if iType not in GetInscriptionLib():
            return None
        lstInscription = []
        for iPerform in self.m_Inscription:
            clsPerform = cl_perform.GetPerformModule(iPerform)
            if clsPerform.m_InscriptionType == INSCRIPTION_TYPE_GEMINI:
                continue
            if iKeepType and clsPerform.m_InscriptionType == iKeepType:
                continue
            lstInscription.append(iPerform)
        
        for iPerform in ShufferList(self.m_Item.m_Game, lstInscription)[:iCnt]:
            if self.GetRestTypeNum(iType) < 1:
                break
            self.RemoveInscription(iPerform)
            (iRet, _) = self.ChooseInscriptionByType(iType, 1)
            if not iRet:
                self.AppendInscription(iPerform)
        
        self.m_Item.GS2CItemPropChange('Inscription', self.GetAllInscription())

    
    def ResetInscriptionByID(self, iSID, iCnt, iKeepType = None):
        if not cl_perform.GetPerformModule(iSID):
            return None
        lstInscription = []
        for iPerform in self.m_Inscription:
            clsPerform = cl_perform.GetPerformModule(iPerform)
            if clsPerform.m_InscriptionType == INSCRIPTION_TYPE_GEMINI:
                continue
            if iKeepType and clsPerform.m_InscriptionType == iKeepType:
                continue
            lstInscription.append(iPerform)
        
        for iPerform in ShufferList(self.m_Item.m_Game, lstInscription)[:iCnt]:
            self.RemoveInscription(iPerform)
        
        self.AppendInscription(iSID)
        self.m_Item.GS2CItemPropChange('Inscription', self.GetAllInscription())

    
    def ChooseInscription(self, iNum, lstExclude, iAlert = 1):
        iChange = 0
        if iNum < 1:
            return iChange
        oGame = self.m_Item.m_Game
        iGrade = self.m_Item.m_Grade
        for iType in (INSCRIPTION_TYPE_GEMINI, INSCRIPTION_TYPE_EXCLUSIVE, INSCRIPTION_TYPE_RARE):
            iProb = self.GetProp(iType, iGrade)
            iTypeRest = self.GetRestTypeNum(iType)
            for _ in range(iNum):
                if iTypeRest < 1:
                    break
                if oGame.Random(10000) >= iProb:
                    continue
                (iAdd, _) = self.ChooseInscriptionByType(iType, 1, lstExclude, iAlert)
                if iAdd:
                    iChange += iAdd
                    iNum -= iAdd
                    iTypeRest -= iAdd
                    if iNum < 1:
                        return iChange
                    continue
            
        
        for iType in (INSCRIPTION_TYPE_NORMAL, INSCRIPTION_TYPE_RARE):
            if iNum < 1:
                return iChange
            (iAdd, lstAddPerform) = self.ChooseInscriptionByType(iType, iNum, lstExclude, iAlert)
            WarrewardLog.Debug('%d guaranteed choose insc %s %s %s %s %s' % (oGame.m_ID, self.m_Item.m_SID, iGrade, iAdd, lstAddPerform, self.m_Inscription))
            iChange += iAdd
            iNum -= iAdd
        
        return iChange

    
    def ValidAddInscription(self, iSID):
        if iSID in self.m_Inscription or iSID in self.m_SealedInscription:
            return 0
        clsPerform = cl_perform.GetPerformModule(iSID)
        if not clsPerform:
            SendAlert('err', '检验不存在铭刻:%s' % iSID)
            return 0
        iType = clsPerform.m_InscriptionType
        if self.GetRestTypeNum(iType) < 1:
            return 0
        if not clsPerform.CheckValidItem(self.m_Item, self.m_Inscription):
            return 0
        return 1

    
    def ChooseInscriptionByType(self, iType, iNum, lstExclude = None, iAlert = 1, iAppend = 1):
        dAll = self.GetInscriptionLib()
        if iType not in dAll:
            return (0, [])
        iAdd = 0
        oItem = self.m_Item
        dWeight = { }
        for iSID, iWeight in dAll[iType].items():
            if iWeight <= 0:
                continue
            if lstExclude and iSID in lstExclude:
                continue
            if self.ValidAddInscription(iSID):
                dWeight[iSID] = iWeight
        
        if not dWeight:
            return (iAdd, [])
        lstPerform = []
        for _ in range(iNum):
            iPerform = ChooseKey(self.m_Item.m_Game, dWeight)
            if not iPerform:
                if iAlert and iType == INSCRIPTION_TYPE_NORMAL:
                    WarrewardLog.Alert('%d %s no enough inscription %s %s' % (oItem.m_Game.m_ID, oItem.m_SID, self.m_Inscription, lstExclude))
                break
            lstPerform.append(iPerform)
            dWeight.pop(iPerform, 0)
            clsPerform = cl_perform.GetPerformModule(iPerform)
            (_, lstInscription, _) = clsPerform.m_ExcludeList
            for iSID in lstInscription:
                dWeight.pop(iSID, 0)
            
            if iAppend:
                self.AppendInscription(iPerform)
            iAdd += 1
        
        return (iAdd, lstPerform)

    
    def ChooseGeminiInscription(self, iNum, lstExclude = None):
        oItem = self.m_Item
        iAdd = 0
        dWeight = { }
        for iExclude in lstExclude:
            if iExclude in self.m_RecastWeight:
                dWeight[iExclude] = self.m_RecastWeight.pop(iExclude, 0)
        
        for _ in range(iNum):
            iPerform = ChooseKey(self.m_Item.m_Game, self.m_RecastWeight)
            if not iPerform:
                WarrewardLog.Alert('%d %s no enough gemini inscription %s %s' % (oItem.m_Game.m_ID, oItem.m_SID, self.m_Inscription, lstExclude))
                break
            iWeight = self.m_RecastWeight.pop(iPerform, 0)
            dWeight[iPerform] = int(iWeight / 5) if iWeight > 5 else 1
            clsPerform = cl_perform.GetPerformModule(iPerform)
            (_, lstInscription, _) = clsPerform.m_ExcludeList
            for iSID in lstInscription:
                if iSID in self.m_RecastWeight:
                    dWeight[iSID] = self.m_RecastWeight.pop(iSID, 0)
            
            self.AppendInscription(iPerform)
            iAdd += 1
        
        self.m_RecastWeight.update(dWeight)
        return iAdd

    
    def OnItemAddToContainer(self, oItem, oOwner):
        oCon = oItem.GetItemContainer()
        if oCon.m_BagType != BAG_TYPE_WIELD:
            return None
        for iSID in self.m_Inscription:
            clsPerform = cl_perform.GetPerformModule(iSID)
            iInscriptionType = clsPerform.m_InscriptionType
            if iInscriptionType == INSCRIPTION_TYPE_GEMINI:
                self.TryEnableGemini(iSID)
                continue
            self.EnablePerform(iSID)
        

    
    def OnItemRemoveFromContainer(self, oItem, oOwner):
        oTarget = self.m_Item
        oPerformCom = oTarget.GetComponent('Perform')
        for iSID in self.m_Inscription:
            oPerformCom.m_Perform.RemovePerform(oOwner, iSID)
            clsPerform = cl_perform.GetPerformModule(iSID)
            iInscriptionType = clsPerform.m_InscriptionType
            if iInscriptionType == INSCRIPTION_TYPE_GEMINI:
                self.DisableGemini(iSID)
        

    
    def AppendInscription(self, iSID):
        iTempInsNumUpperLimit = self.m_Item.QueryTmp('TempInsNumUpperLimit')
        if iTempInsNumUpperLimit and len(self.m_Inscription) >= iTempInsNumUpperLimit:
            self.m_InscriptionNum = iTempInsNumUpperLimit
            return None
        clsPerform = cl_perform.GetPerformModule(iSID)
        if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
            oItem = self.m_Item
            oGame = oItem.m_Game
            if oItem and oGame:
                oOwner = oItem.GetOwner()
                if oOwner:
                    WarrewardLog.TraceAlert('%d %s appendinsc err %s %s %s' % (oGame.m_ID, oOwner.m_PlayerID, oItem.m_SID, oItem.m_Grade, iSID))
            return None
        self.m_Inscription.append(iSID)
        iInscriptionType = clsPerform.m_InscriptionType
        self.m_Type2Num[iInscriptionType] = self.m_Type2Num.setdefault(iInscriptionType, 0) + 1
        if iInscriptionType == INSCRIPTION_TYPE_GEMINI:
            self.TryEnableGemini(iSID)
        else:
            self.m_RecastWeight = { }
            self.EnableAttr(iSID)
            self.EnablePerform(iSID)
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_APPEND_INSCRIPTION, oOwner, {
                'SID': iSID,
                'ItemID': self.m_Item.m_ID })

    
    def RemoveInscription(self, iSID):
        self.DisableInscription(iSID)
        self.m_Inscription.remove(iSID)
        self.OnRemoveDisableInscription(iSID)
        clsPerform = cl_perform.GetPerformModule(iSID)
        iInscriptionType = clsPerform.m_InscriptionType
        self.m_Type2Num[iInscriptionType] -= 1
        if iInscriptionType == INSCRIPTION_TYPE_GEMINI:
            self.DisableGemini(iSID)
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVE_INSCRIPTION, oOwner, {
                'SID': iSID,
                'ItemID': self.m_Item.m_ID })

    
    def GetFormulaAttr(self, iSID):
        oTarget = self.m_Item
        oOwner = oTarget.GetOwner()
        clsPerform = cl_perform.GetPerformModule(iSID)
        if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
            return { }
        dEventData = oTarget.AttrCache()
        dAttr = { }
        for sAttr, (iAdd, iMul, iForce) in clsPerform.m_ItemAttr.items():
            iAdd = cl_formula.GetResultByData(oOwner, iAdd, dEventData)
            iMul = cl_formula.GetResultByData(oOwner, iMul, dEventData)
            iForce = cl_formula.GetResultByData(oOwner, iForce, dEventData)
            dAttr[sAttr] = (iAdd, iMul, iForce)
        
        return dAttr

    
    def EnableAttr(self, iSID, dFormulaAttr = None):
        oTarget = self.m_Item
        clsPerform = cl_perform.GetPerformModule(iSID)
        if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
            return None
        if not dFormulaAttr:
            dFormulaAttr = self.GetFormulaAttr(iSID)
        sKey = 'InscriptCom%d' % iSID
        for sAttr, (iAdd, iMul, iForce) in dFormulaAttr.items():
            if iForce:
                oTarget.ItemAttrForceSet(sAttr, iForce, sKey)
                continue
            oTarget.AttrChange(sAttr, iMul, iAdd, sKey)
        
        if clsPerform.m_ElementType:
            oTarget.m_ElementTypeObj.SetModify(sKey, clsPerform.m_ElementType)
            oOwner = oTarget.GetOwner()
            if oOwner:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INSCRIPTION_ENABLE_ELEMENTTYPE, oOwner, {
                    'ItemID': oTarget.m_ID })

    
    def EnablePerform(self, iSID):
        oItem = self.m_Item
        if not oItem.GetItemContainer():
            return None
        oPerformCom = oItem.GetComponent('Perform')
        if oPerformCom:
            pfobj = oPerformCom.GetPerform(iSID)
            if not pfobj:
                iEnable = self.IsEnable(iSID)
                oPerformCom.AddPerform(iSID, 1, iEnable)

    
    def DisableInscription(self, iSID):
        oTarget = self.m_Item
        oOwner = oTarget.GetOwner()
        oPerformCom = oTarget.GetComponent('Perform')
        oPerformCom.m_Perform.RemovePerform(oOwner, iSID)
        self.DisableAttr(iSID)

    
    def DisableAttr(self, iSID):
        oTarget = self.m_Item
        clsPerform = cl_perform.GetPerformModule(iSID)
        if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
            return None
        dAttr = clsPerform.m_ItemAttr
        sKey = 'InscriptCom%d' % iSID
        for sAttr, (_, _, iForce) in dAttr.items():
            if iForce:
                oTarget.ItemAttrForceClear(sAttr, sKey)
                continue
            oTarget.AttrClear(sAttr, sKey)
        
        self.RemoveSetModifyByInscription(sKey)

    
    def RemoveSetModifyByInscription(self, sKey):
        oItem = self.m_Item
        iElement = oItem.m_ElementTypeObj.RemoveSetModify(sKey)
        if not iElement:
            return None
        oOwner = oItem.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INSCRIPTION_DISABLE_ELEMENTTYPE, oOwner, {
                'ItemID': oItem.m_ID })

    
    def GetAnotherWeaponInscriptionCom(self):
        oItem = self.m_Item
        oCon = oItem.GetItemContainer()
        if not oCon or oCon.m_BagType != BAG_TYPE_WIELD:
            return None
        lstPos = oCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
        for iPos in lstPos:
            if oItem.m_Pos != iPos:
                oOtherItem = oCon.GetItem(iPos)
                if oOtherItem:
                    return oOtherItem.GetComponent('Inscription')
        

    
    def CheckCanEnableGemini(self, oOtherInscriptionCom, iSID):
        oPerformCom = self.m_Item.GetComponent('Perform')
        if not oPerformCom:
            return 0
        oPerform = oPerformCom.GetPerform(iSID)
        if oPerform:
            if oPerform.m_Enable:
                return 0
            oOtherPerformCom = oOtherInscriptionCom.m_Item.GetComponent('Perform')
            if not oOtherPerformCom:
                return 0
            oOtherPerform = oOtherPerformCom.GetPerform(iSID)
            if oOtherPerform:
                if oOtherPerform.m_Enable:
                    return 0
                oOwner = self.m_Item.GetOwner()
                if not oOwner:
                    return 0
                oWeapon = oOwner.m_WieldCon.GetCurWeapon(MAIN_HOLD)
                if oWeapon and oWeapon.IsInitWeapon():
                    return 0
        return 1

    
    def TryEnableGemini(self, iSID):
        oOtherInscriptionCom = self.GetAnotherWeaponInscriptionCom()
        if oOtherInscriptionCom:
            if not self.CheckCanEnableGemini(oOtherInscriptionCom, iSID):
                return None
            if iSID in oOtherInscriptionCom.m_Inscription:
                oOwner = self.m_Item.GetOwner()
                if oOwner:
                    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ENABLE_GEMINI, oOwner, {
                        'SID': iSID })
                self.EnablePerform(iSID)
                oOtherInscriptionCom.EnablePerform(iSID)
                dAttr = self.GetFormulaAttr(iSID)
                dOtherAttr = oOtherInscriptionCom.GetFormulaAttr(iSID)
                self.EnableAttr(iSID, dAttr)
                oOtherInscriptionCom.EnableAttr(iSID, dOtherAttr)

    
    def DisableGemini(self, iSID):
        oOtherInscriptionCom = self.GetAnotherWeaponInscriptionCom()
        if oOtherInscriptionCom and iSID in oOtherInscriptionCom.m_Inscription:
            oOwner = self.m_Item.GetOwner()
            if oOwner:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DISABLE_GEMINI, oOwner, {
                    'SID': iSID })
            oOtherInscriptionCom.DisableInscription(iSID)

    
    def GetSealedInscription(self):
        if not self.m_SealedInscription:
            return [
                0,
                0,
                0]
        return self.m_SealedInscription

    
    def InitSealedInscription(self):
        self.m_SealedInscription = []
        for iInscriptionPool in SEALEDINSCRIPTION_POOL:
            iInscription = self.ChooseSealedInscription(iInscriptionPool)
            self.m_SealedInscription.append(iInscription)
        
        if not all(self.m_SealedInscription):
            oWarMgr = self.m_Item.m_Game.m_WarMgr
            WarrewardLog.Alert(f'''{self.m_Item.m_SID} not enough inscription pool {self.m_SealedInscription} {self.m_Inscription} {oWarMgr.m_SID}''')
        self.m_Item.GS2CItemPropChange('SealedInscription', self.GetSealedInscription())

    
    def ChooseSealedInscription(self, iPool):
        oGame = self.m_Item.m_Game
        dInscription = GetInscritionPool(iPool)
        dValidInscription = { }
        lstHas = self.m_Inscription
        for iInscription, iWeight in dInscription.items():
            clsPerform = cl_perform.GetPerformModule(iInscription)
            if iInscription in lstHas or not clsPerform.CheckValidItem(self.m_Item, lstHas):
                continue
            dValidInscription[iInscription] = iWeight
        
        iInscription = ChooseKey(oGame, dValidInscription)
        if not iInscription:
            iInscription = 0
        return iInscription

    
    def OnItemRemoveDisableSealedInscription(self, oItem, oOwner):
        iNowSealedInscriptionLv = self.m_NowSealedInscriptionLv
        if not iNowSealedInscriptionLv:
            return None
        self.DisableSealedInscription(iNowSealedInscriptionLv)

    
    def EnableSealedInscription(self, iLv):
        if not self.m_SealedInscription:
            return None
        if self.m_NowSealedInscriptionLv:
            return None
        if iLv <= 0 or iLv > MAX_SEALEDINSCRIPTION_LV:
            return None
        iInscription = self.m_SealedInscription[iLv - 1]
        if not iInscription:
            return None
        oPerformCom = self.m_Item.GetComponent('Perform')
        if not oPerformCom:
            return None
        oItem = self.m_Item
        if not oItem.GetItemContainer():
            return None
        self.m_NowSealedInscriptionLv = iLv
        iEnable = self.IsEnable(iInscription)
        oPerformCom.AddPerform(iInscription, 1, iEnable, iNotify = 1)
        self.EnableAttr(iInscription)
        oItem.AddAttention(itemdef.MSG_ITEM_REMOVE, self.OnItemRemoveDisableSealedInscription, 'SealedInscription')
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INSCRIPTION_STATE_REFRESH, oOwner, {
                'ItemID': self.m_Item.m_ID,
                'Enable': 1 }, iSub = INSCRIPTION_STATE_SEALED)

    
    def DisableSealedInscription(self, iLv):
        if not self.m_SealedInscription:
            return None
        if not self.m_NowSealedInscriptionLv:
            return None
        if iLv <= 0 or iLv > MAX_SEALEDINSCRIPTION_LV:
            return None
        iInscription = self.m_SealedInscription[iLv - 1]
        if not iInscription:
            return None
        oItem = self.m_Item
        oPerformCom = oItem.GetComponent('Perform')
        if not oPerformCom:
            return None
        oPerform = oPerformCom.GetPerform(iInscription)
        if not oPerform:
            return None
        self.m_NowSealedInscriptionLv = 0
        oPerformCom.m_Perform.RemovePerform(self.m_Item.GetOwner(), iInscription, iNotify = 1)
        clsPerform = cl_perform.GetPerformModule(iInscription)
        if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
            return None
        dAttr = clsPerform.m_ItemAttr
        sKey = 'InscriptCom%d' % iInscription
        for sAttr, (_, _, iForce) in dAttr.items():
            if iForce:
                oItem.ItemAttrForceClear(sAttr, sKey)
                continue
            oItem.AttrClear(sAttr, sKey)
        
        self.RemoveSetModifyByInscription(sKey)
        oItem.DoneAttention(itemdef.MSG_ITEM_REMOVE, 'SealedInscription')
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INSCRIPTION_STATE_REFRESH, oOwner, {
                'ItemID': self.m_Item.m_ID,
                'Enable': 0 }, iSub = INSCRIPTION_STATE_SEALED)

    
    def RemoveSealedInscription(self, iType):
        if iType not in g_InscriptionType2Lv:
            return None
        iLv = g_InscriptionType2Lv[iType]
        if len(self.m_SealedInscription) < iLv:
            return None
        self.DisableSealedInscription(iLv)
        self.m_SealedInscription[iLv - 1] = 0

    
    def GetSealedInscriptionNumByTypeAndLv(self, iType, iLevel):
        if iType not in g_InscriptionType2Lv:
            return 0
        if iLevel == g_InscriptionType2Lv[iType]:
            return 1
        return 0

    
    def FullSealedInscription(self):
        bReChoose = False
        for iDx, iInscription in enumerate(self.m_SealedInscription):
            if not iInscription:
                iPool = SEALEDINSCRIPTION_POOL[iDx]
                iInscription = self.ChooseSealedInscription(iPool)
                bReChoose = True
                self.m_SealedInscription[iDx] = iInscription
        
        if bReChoose:
            self.m_Item.GS2CItemPropChange('SealedInscription', self.GetSealedInscription())

    
    def AddShareInscription(self, iSID):
        if iSID in self.m_ShareInscription:
            return None
        self.m_ShareInscription.append(iSID)
        oItem = self.m_Item
        oPerformCom = oItem.GetComponent('Perform')
        iEnable = self.IsEnable(iSID)
        oPerformCom.AddPerform(iSID, 1, iEnable)
        self.EnableAttr(iSID)
        self.RefreshShareInscription()

    
    def RemoveShareInscription(self, lstInscription = None):
        if not lstInscription:
            lstInscription = self.m_ShareInscription[:]
        oItem = self.m_Item
        oPerformCom = oItem.GetComponent('Perform')
        for iSID in lstInscription:
            if iSID in self.m_ShareInscription:
                self.m_ShareInscription.remove(iSID)
            if iSID in self.m_Inscription:
                continue
            oPerformCom.m_Perform.RemovePerform(oItem.GetOwner(), iSID)
            clsPerform = cl_perform.GetPerformModule(iSID)
            if not clsPerform or clsPerform.m_PFType != PF_TYPE_INSCRIPTION:
                continue
            dAttr = clsPerform.m_ItemAttr
            sKey = 'InscriptCom%d' % iSID
            for sAttr, (_, _, iForce) in dAttr.items():
                if iForce:
                    oItem.ItemAttrForceClear(sAttr, sKey)
                    continue
                oItem.AttrClear(sAttr, sKey)
            
            self.RemoveSetModifyByInscription(sKey)
        
        self.RefreshShareInscription()

    
    def UpdateShareInscriptionEffect(self):
        for iInscription in self.m_ShareInscription:
            for iSID in self.m_Inscription:
                clsPerform = cl_perform.GetPerformModule(iSID)
                (_, lstInscription, _) = clsPerform.m_ExcludeList
                if iInscription in lstInscription:
                    self.DisableInscription(iInscription)
                    break
            else:
                self.EnablePerform(iInscription)
        

    
    def GetShareInscription(self):
        return self.m_ShareInscription

    
    def RefreshShareInscription(self):
        oItem = self.m_Item
        lstShare = self.GetShareInscription()
        oItem.GS2CItemPropChange('ShareInscription', lstShare)
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INSCRIPTION_STATE_REFRESH, oOwner, {
                'ItemID': self.m_Item.m_ID }, iSub = INSCRIPTION_STATE_SHARE)

    
    def IsEnable(self, iInscription):
        oItem = self.m_Item
        oHoldComp = oItem.GetComponent('Hold')
        iHoldPos = oHoldComp.HoldPos()
        iItemEnableType = cl_perform.GetPerformModule(iInscription).m_ItemEnableType
        iEnable = 0
        if not iItemEnableType & ITEMPERFORM_ENABLE_HOLD or iHoldPos:
            if (iItemEnableType & ITEMPERFORM_ENABLE_UNHOLD or not iHoldPos or iItemEnableType & ITEMPERFORM_ENABLE_MAINHOLD) and iHoldPos == MAIN_HOLD:
                iEnable = 1

    
    def RandomTempDisableInscription(self, sKey, iNum, lstSecond = None):
        if self.m_Inscription and sKey not in self.m_TempDisableInscription:
            lstDisable = self.GetDisableInscription()
            dInscription = { }
            for iSID in self.m_Inscription:
                clsPerform = cl_perform.GetPerformModule(iSID)
                iInscriptionType = clsPerform.m_InscriptionType
                if iInscriptionType != INSCRIPTION_TYPE_GEMINI and iSID not in lstDisable:
                    dInscription[iSID] = 1
            
            if lstSecond:
                lstSecond = ShufferList(self.m_Item.m_Game, lstSecond)
                for iInscription in lstSecond:
                    if len(dInscription) > iNum and iInscription in dInscription:
                        dInscription.pop(iInscription)
                
            if len(dInscription) > iNum:
                lstInscription = ChooseMulKeys(self.m_Item.m_Game, dInscription, iNum)
                dInscription = { }
                for iSID in lstInscription:
                    dInscription[iSID] = 1
                
            self.TempDisableInscription(sKey, dInscription)
            return dInscription
        return { }

    
    def TempDisableInscription(self, sKey, dDisable, iCover = 1):
        if not dDisable:
            return None
        if iCover:
            self.m_TempDisableInscription[sKey] = dDisable
        else:
            dInscription = self.m_TempDisableInscription.setdefault(sKey, { })
            dInscription.update(dDisable)
        for iInscription in dDisable:
            if iInscription not in self.m_Inscription:
                continue
            self.DisableInscription(iInscription)
        
        oItem = self.m_Item
        WarrewardLog.Debug('%s tempdisins %s %s %s %s' % (oItem.m_Game.m_ID, oItem.m_ID, sKey, dDisable, iCover))
        oItem.AddAttention(itemdef.MSG_ITEM_UNHOLD, Functor(self.OnUnholdTempDisableInscription, sKey), sKey)
        self.RefreshDisbleInscription()

    
    def OnUnholdTempDisableInscription(self, sKey, oItem, oOwner):
        oItem.DoneAttention(itemdef.MSG_ITEM_UNHOLD, sKey)
        self.RemoveTempDisbleInscription(sKey, iRefresh = 1)

    
    def GetDisableInscription(self):
        dInscription = { }
        oItem = self.m_Item
        iHold = oItem.GetComponent('Hold').IsHold()
        if iHold:
            for dTemp in self.m_TempDisableInscription.values():
                dInscription.update(dTemp)
            
        dInscription.update(self.m_DisableInscription)
        return list(dInscription)

    
    def RefreshDisbleInscription(self):
        oItem = self.m_Item
        lstDisable = self.GetDisableInscription()
        oItem.GS2CItemPropChange('DisableInscription', lstDisable)
        oItem.GS2CItemPropChange('Inscription', self.GetAllInscription(lstDisable = lstDisable))
        oOwner = self.m_Item.GetOwner()
        if oOwner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_INSCRIPTION_STATE_REFRESH, oOwner, {
                'ItemID': self.m_Item.m_ID }, iSub = INSCRIPTION_STATE_DISBLE)

    
    def TransDisableInscirption(self, sKey, dInscription = None):
        oItem = self.m_Item
        oItem.DoneAttention(itemdef.MSG_ITEM_REMOVE, sKey)
        self.m_TempDisableInscription.pop(sKey, { })
        if not dInscription:
            return None
        WarrewardLog.Debug('%s transtempdisins %s %s %s' % (oItem.m_Game.m_ID, oItem.m_ID, sKey, dInscription))
        for iPerform in dInscription:
            self.m_DisableInscription[iPerform] = 1
        
        self.RefreshDisbleInscription()

    
    def OnRemoveDisableInscription(self, iSID):
        if iSID in self.m_DisableInscription:
            self.m_DisableInscription.pop(iSID)
        self.RefreshDisbleInscription()

    
    def ReplaceTempDisableInscription(self, sKey, lstReplace, iNum = 0):
        if sKey not in self.m_TempDisableInscription:
            return { }
        dInscription = self.m_TempDisableInscription[sKey]
        oItem = self.m_Item
        oGame = oItem.m_Game
        for iInscription in lstReplace:
            if iInscription not in dInscription:
                WarrewardLog.Alert('%d %s repdisins %s %s %s' % (oGame.m_ID, oItem.m_ID, iInscription, dInscription, self.m_Inscription))
                continue
            iNum += 1
            dInscription.pop(iInscription)
        
        lstDisable = self.GetDisableInscription()
        dInscription = { }
        for iSID in self.m_Inscription:
            clsPerform = cl_perform.GetPerformModule(iSID)
            iInscriptionType = clsPerform.m_InscriptionType
            if iInscriptionType != INSCRIPTION_TYPE_GEMINI and iSID not in lstDisable:
                dInscription[iSID] = 1
        
        if not dInscription:
            WarrewardLog.Debug('%d %s repdisinsnonew %s %s %s' % (oGame.m_ID, oItem.m_ID, iInscription, dInscription, self.m_Inscription))
            return dInscription
        lstDisable = ChooseMulKeys(self.m_Item.m_Game, dInscription, iNum)
        dInscription = { }
        for iSID in lstDisable:
            dInscription[iSID] = 1
        
        self.TempDisableInscription(sKey, dInscription, iCover = 0)
        return self.m_TempDisableInscription[sKey]

    
    def RemoveTempDisbleInscription(self, sKey, iRefresh = 1):
        dInscription = self.m_TempDisableInscription.pop(sKey, { })
        if not dInscription:
            return None
        for iInscription in dInscription:
            if iInscription not in self.m_Inscription:
                continue
            self.EnableAttr(iInscription)
            self.EnablePerform(iInscription)
        
        if iRefresh:
            self.RefreshDisbleInscription()

    
    def GetTempDisbleInscription(self, sKey):
        if sKey not in self.m_TempDisableInscription:
            return { }
        return self.m_TempDisableInscription[sKey]


