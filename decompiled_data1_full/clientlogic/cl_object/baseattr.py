# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/baseattr.pyc
# RelativePath: clientlogic/cl_object/baseattr.pyc
# Source Generated with Decompyle++
# File: baseattr.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH, BASEATTR_CLIENT, WARRIOR_PET
from cl_only import CELL_REC, Time2Frame, SendAlert, TraceLog
import math
import cl_formula
import cl_object.reason
g_LimitInfo = {
    'AttSpeed': (20, 3000),
    'Toughness': (-90, 90),
    'Att': (100, 100000000),
    'HPMax': (100, 0x1387FFF8AD00),
    'ShieldMax': (0, 0x1387FFF8AD00),
    'ArmorMax': (0, 0x1387FFF8AD00),
    'CrazyEff': (10000, 9999999),
    'MoveSpeed': (0.2, 50),
    'ColdTime': (0, 9999999),
    'FillTime': (4, 9999999),
    'Radius': (0.8, 99),
    'TriggerTimes': (0, 100),
    'MinUseEnergy': (0, 9999999) }
cl_formula.g_LimitInfo = g_LimitInfo
MASK_REFRESH_NO = 0
MASK_REFRESH_REFRESH = 1
MASK_REFRESH_VALUE = 2
MASK_REFRESH_FORCEVALUE = 4

class CBaseAttr(object):
    m_Type = 'Base'
    m_JoinAttrCache = True
    
    def __init__(self, obj, sAttr, iVal, iFlag = BASEATTR_REFRESH):
        self.m_Attr = sAttr
        self.m_Refresh = 0
        self.m_Flag = iFlag
        if isinstance(iVal, (int, float)):
            self.m_BaseFormula = None
            self.m_BaseValue = iVal
        else:
            self.m_BaseFormula = iVal
            self.m_BaseValue = self.m_BaseFormula(obj)
        self.m_AttrLimit = None
        self.SetLimit()
        self.m_ForceCurValue = None
        self.m_CurValue = self.m_BaseValue
        if self.m_CurValue:
            self.CheckLimit()
        self.m_MulPositive = 0
        self.m_MulNegative = []
        self.m_AddPositive = 0
        self.m_AddNegative = 0
        self.m_FactorInfo = { }
        self.m_ForceSetInfo = { }
        self.m_SaveFactor = { }
        self.m_ExcludeFactor = { }
        self.m_IgnoreLinkInfo = { }
        self.m_FixedAddition = { }

    
    def Save(self):
        return self.m_SaveFactor

    
    def Load(self, obj, dData):
        self.m_SaveFactor = dData
        for sKey, (iMul, iAdd) in self.m_SaveFactor.items():
            self.AddValue(obj, iMul, iAdd, sKey)
        

    
    def ChangeBase(self, obj, iVal):
        if self.m_BaseFormula:
            self.m_BaseValue = self.m_BaseFormula(obj)
        elif self.m_BaseValue != iVal:
            self.m_BaseValue = iVal
        else:
            return None
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def AddValue(self, obj, iMul, iAdd, sKey, iSave = 0, iPreExclude = 0):
        if sKey in self.m_FactorInfo:
            (iOldMul, iOldAdd) = self.m_FactorInfo[sKey]
            if iOldMul == iMul and iOldAdd == iAdd:
                return None
            if iOldMul >= 0:
                self.m_MulPositive -= iOldMul
            else:
                self.m_MulNegative.remove(iOldMul)
            if iOldAdd >= 0:
                self.m_AddPositive -= iOldAdd
            else:
                self.m_AddNegative -= iOldAdd
        if iMul >= 0:
            self.m_MulPositive += iMul
        elif iMul < -10000:
            if self.m_Attr not in ('ColdTime',):
                from cl_warrior import CWarrior
                if not isinstance(obj, CWarrior):
                    oOwner = obj.GetOwner()
                    if oOwner:
                        lstPerform = oOwner.m_Perform.GetAllPerformSID()
                        lstState = oOwner.m_State.GetAllStateSID()
                    else:
                        lstPerform = []
                        lstState = []
                else:
                    lstPerform = obj.m_Perform.GetAllPerformSID()
                    lstState = obj.m_State.GetAllStateSID()
                sText = '%s att %s mul %s key %s pf %s st %s' % (obj.m_Game.m_ID, self.m_Attr, iMul, sKey, lstPerform, lstState)
                SendAlert('err', sText)
                TraceLog('err', sText)
            iMul = -10000
        self.m_MulNegative.append(iMul)
        self.m_FactorInfo[sKey] = (iMul, iAdd)
        if iAdd >= 0:
            self.m_AddPositive += iAdd
        else:
            self.m_AddNegative += iAdd
        if iSave:
            self.m_SaveFactor[sKey] = (iMul, iAdd)
        if iPreExclude:
            self.AddExcludeFactor(sKey)
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def ClearValue(self, obj, sKey):
        if sKey not in self.m_FactorInfo:
            return None
        (iMul, iAdd) = self.m_FactorInfo[sKey]
        if iMul >= 0:
            self.m_MulPositive -= iMul
        else:
            self.m_MulNegative.remove(iMul)
        if iAdd >= 0:
            self.m_AddPositive -= iAdd
        else:
            self.m_AddNegative -= iAdd
        del self.m_FactorInfo[sKey]
        if sKey in self.m_ExcludeFactor:
            self.m_ExcludeFactor.pop(sKey)
        if sKey in self.m_FixedAddition:
            self.m_FixedAddition.pop(sKey)
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def SetForceValue(self, obj, iValue, sKey, iPriority = 0):
        self.m_ForceSetInfo[sKey] = iValue
        self.UpdateRefresh(obj, MASK_REFRESH_FORCEVALUE)

    
    def ClearForceValue(self, obj, sKey):
        if sKey not in self.m_ForceSetInfo:
            return None
        self.m_ForceSetInfo.pop(sKey)
        self.UpdateRefresh(obj, MASK_REFRESH_FORCEVALUE)

    
    def AddExcludeFactor(self, sKey):
        self.m_ExcludeFactor[sKey] = 1

    
    def AddFixedAddition(self, obj, sKey, iValue):
        self.m_FixedAddition[sKey] = iValue
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def RemoveFixedAddition(self, obj, sKey):
        if sKey in self.m_FixedAddition:
            self.m_FixedAddition.pop(sKey)
            self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def ClearAll(self):
        self.m_Refresh = 0
        self.m_CurValue = 0
        self.m_BaseValue = 0
        self.m_MulPositive = 0
        self.m_MulNegative = []
        self.m_AddPositive = 0
        self.m_AddNegative = 0
        self.m_FactorInfo = { }
        self.m_ForceCurValue = None
        self.m_ForceSetInfo.clear()
        self.m_ExcludeFactor = { }

    
    def GetValue(self, obj):
        if self.m_Refresh:
            self.Refresh(obj)
        if self.m_ForceCurValue is not None:
            return self.m_ForceCurValue
        return self.m_CurValue

    
    def GetValueNotRefresh(self, obj = None):
        if self.m_ForceCurValue is not None:
            return self.m_ForceCurValue
        return self.m_CurValue

    
    def GetValueIgnForce(self, obj):
        if self.m_Refresh:
            self.Refresh(obj)
        return self.m_CurValue

    
    def UpdateRefresh(self, obj, iMask):
        self.m_Refresh |= iMask
        if self.m_Flag & BASEATTR_REFRESH:
            self.Refresh(obj)

    
    def Refresh(self, obj):
        iRefresh = self.m_Refresh
        self.m_Refresh = 0
        iOldValue = self.GetValueNotRefresh(obj)
        if obj and self.m_Attr in g_RefreshAttrBeforeFunc:
            g_RefreshAttrBeforeFunc[self.m_Attr](obj, iOldValue)
        if iRefresh & MASK_REFRESH_VALUE:
            self.m_CurValue = self.CalCurValue()
        if iRefresh & MASK_REFRESH_FORCEVALUE:
            self.m_ForceCurValue = self.CalForceCurValue()
        self.CheckLimit()
        if obj:
            self.RefreshClient(obj)
            if self.m_Attr in g_RefreshAttrAfterFunc:
                g_RefreshAttrAfterFunc[self.m_Attr](obj, iOldValue, self.GetValueNotRefresh(obj))
        return self

    
    def GetExcludeValue(self, lstExcludeFactors = None):
        iExcludeAdd = 0
        iMulPositive = 0
        lstMulNegative = []
        if lstExcludeFactors is None:
            lstExcludeFactors = self.m_ExcludeFactor
        for sKey in lstExcludeFactors:
            if sKey not in self.m_FactorInfo:
                continue
            (iMul, iAdd) = self.m_FactorInfo[sKey]
            iExcludeAdd += iAdd
            if iMul >= 0:
                iMulPositive += iMul
                continue
            lstMulNegative.append(iMul)
        
        iVal = self.m_BaseValue
        if self.m_AddPositive:
            iVal += self.m_AddPositive
        if self.m_AddNegative:
            iVal += self.m_AddNegative
        iVal -= iExcludeAdd
        iRealMulPositive = self.m_MulPositive - iMulPositive
        if iRealMulPositive:
            iVal = iVal * (10000 + iRealMulPositive) // 10000
        if self.m_MulNegative:
            for iRatio in self.m_MulNegative:
                if iRatio in lstMulNegative:
                    continue
                iVal = iVal * (10000 + iRatio) // 10000
            
        return int(iVal)

    
    def CalCurValue(self):
        iVal = self.m_BaseValue
        if self.m_AddPositive:
            iVal += self.m_AddPositive
        if self.m_AddNegative:
            iVal += self.m_AddNegative
        if self.m_MulPositive:
            iVal = iVal * (10000 + self.m_MulPositive) // 10000
        if self.m_MulNegative:
            for iRatio in self.m_MulNegative:
                iVal = iVal * (10000 + iRatio) // 10000
            
        if self.m_FixedAddition:
            iVal += sum(self.m_FixedAddition.values())
        return int(iVal)

    
    def CalForceCurValue(self):
        if self.m_ForceSetInfo:
            iFsVal = min(self.m_ForceSetInfo.values())
        else:
            iFsVal = None
        return iFsVal

    
    def RefreshClient(self, obj):
        if self.m_Flag & BASEATTR_CLIENT:
            obj.RefreshAttr(self.m_Attr, self.GetValueNotRefresh(obj))

    
    def AddIgnoreLink(self, obj, sKey):
        iRefresh = 0 if self.m_IgnoreLinkInfo else 1
        self.m_IgnoreLinkInfo[sKey] = 1
        if iRefresh:
            self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def RemoveIgnoreLink(self, obj, sKey):
        if sKey in self.m_IgnoreLinkInfo:
            self.m_IgnoreLinkInfo.pop(sKey)
        if not self.m_IgnoreLinkInfo:
            self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def SetLimit(self):
        if self.m_Attr in g_LimitInfo:
            self.m_AttrLimit = g_LimitInfo[self.m_Attr]

    
    def SetCustomLimit(self, obj, tLimit):
        self.m_AttrLimit = tLimit
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def RemoveCustomLimit(self, obj):
        self.m_AttrLimit = None
        self.SetLimit()
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def CheckLimit(self):
        if self.m_AttrLimit is not None:
            if self.m_CurValue < self.m_AttrLimit[0]:
                self.m_CurValue = self.m_AttrLimit[0]
            elif self.m_CurValue > self.m_AttrLimit[1]:
                self.m_CurValue = self.m_AttrLimit[1]
            if self.m_ForceCurValue is not None:
                if self.m_ForceCurValue < self.m_AttrLimit[0]:
                    self.m_ForceCurValue = self.m_AttrLimit[0]
                elif self.m_ForceCurValue > self.m_AttrLimit[1]:
                    self.m_ForceCurValue = self.m_AttrLimit[1]

    
    def IsMinValue(self, iCurValue):
        if self.m_AttrLimit is None:
            return 0
        if self.m_AttrLimit[0] == iCurValue:
            return 1
        return 0

    
    def SetBaseFormula(self, func):
        self.m_BaseFormula = func

    
    def GetChangeRatio(self, obj, iMaxRatio = 100):
        if self.m_BaseValue == 0:
            return 0
        iCurValue = self.GetValue(obj)
        if iCurValue < self.m_BaseValue:
            return self.m_BaseValue * iMaxRatio // iCurValue
        return iCurValue * iMaxRatio // self.m_BaseValue

    
    def CalMulChangeRatio(self):
        fVal = 1
        if self.m_MulPositive:
            fVal = fVal * (10000 + self.m_MulPositive) * 0.0001
        if self.m_MulNegative:
            for iRatio in self.m_MulNegative:
                fVal = fVal * (10000 + iRatio) * 0.0001
            
        return fVal

    
    def GetBaseAttr(self):
        return self.m_BaseValue

    
    def GetMulPositiveAttr(self):
        return self.m_MulPositive

    
    def GetKeyFactorInfo(self, sKey):
        if sKey not in self.m_FactorInfo:
            return (0, 0)
        return self.m_FactorInfo[sKey]

    
    def HasFactor(self, sKey):
        if sKey in self.m_FactorInfo:
            return 1
        return 0

    
    def HasForce(self, sKey = ''):
        if not sKey and self.m_ForceSetInfo:
            return True
        if sKey and sKey in self.m_ForceSetInfo:
            return True
        return False

    
    def PreviewChange(self, iMul, iAdd):
        if iMul > 0:
            self.m_MulPositive += iMul
        elif iMul < 0:
            self.m_MulNegative.append(iMul)
        if iAdd >= 0:
            self.m_AddPositive += iAdd
        else:
            self.m_AddNegative += iAdd
        iVal = self.CalCurValue()
        if iMul > 0:
            self.m_MulPositive -= iMul
        elif iMul < 0:
            self.m_MulNegative.remove(iMul)
        if iAdd >= 0:
            self.m_AddPositive -= iAdd
        else:
            self.m_AddNegative -= iAdd
        return int(iVal)

    
    def GetForecastValue(self, obj):
        iMulNegative = 10000
        if self.m_ForceCurValue is not None:
            return (self.m_ForceCurValue, 0, 0, iMulNegative)
        for iRatio in self.m_MulNegative:
            iMulNegative = iMulNegative * (10000 + iRatio) // 10000
        
        return (self.m_BaseValue, self.m_AddPositive + self.m_AddNegative, self.m_MulPositive, iMulNegative)

    
    def CalGradePreviewChangeValue(self, iMul, iAdd):
        iVal = self.m_BaseValue
        iCalMul = self.m_MulPositive + iMul
        iCalAdd = self.m_AddPositive + iAdd
        iVal += iCalAdd
        iVal += self.m_AddNegative
        if iCalMul:
            iVal = iVal * (10000 + iCalMul) // 10000
        for iRatio in self.m_MulNegative:
            iVal = iVal * (10000 + iRatio) // 10000
        
        return int(iVal)



class CMoveSpeed(CBaseAttr):
    
    def __init__(self, obj, sAttr, iVal, iFlag = BASEATTR_REFRESH):
        super(CMoveSpeed, self).__init__(obj, sAttr, iVal, iFlag)
        self.ChangeBase(obj, iVal)

    
    def ChangeBase(self, obj, iVal):
        if self.m_BaseFormula:
            self.m_BaseValue = self.m_BaseFormula(obj) * CELL_REC
        elif self.m_BaseValue != iVal * CELL_REC:
            self.m_BaseValue = iVal * CELL_REC
        else:
            return None
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def CalCurValue(self):
        iVal = self.m_BaseValue
        if self.m_AddPositive:
            iVal += self.m_AddPositive * CELL_REC
        if self.m_AddNegative:
            iVal += self.m_AddNegative * CELL_REC
        if self.m_MulPositive:
            iVal = iVal * (10000 + self.m_MulPositive) * 0.0001
        if self.m_MulNegative:
            for iRatio in self.m_MulNegative:
                iVal = iVal * (10000 + iRatio) * 0.0001
            
        return iVal

    
    def CalForceCurValue(self):
        if self.m_ForceSetInfo:
            iFsVal = min(self.m_ForceSetInfo.values()) * CELL_REC
        else:
            iFsVal = None
        return iFsVal

    
    def RefreshClient(self, obj):
        if obj and self.m_Flag & BASEATTR_CLIENT and obj.m_InitScene:
            obj.SetSpeed(self.GetValueNotRefresh(obj))



class CShieldRecoverTime(CBaseAttr):
    
    def RefreshClient(self, obj):
        pass



class CComMaxBullet(CBaseAttr):
    
    def SetForceValue(self, obj, iValue, sKey, iPriority = 0):
        self.m_ForceSetInfo[sKey] = (iValue, iPriority)
        self.UpdateRefresh(obj, MASK_REFRESH_FORCEVALUE)

    
    def CalForceCurValue(self):
        iFsVal = None
        if self.m_ForceSetInfo:
            iMaxPriority = -9999
            for iValue, iPriority in self.m_ForceSetInfo.values():
                if iPriority < iMaxPriority:
                    continue
                if iPriority > iMaxPriority:
                    iMaxPriority = iPriority
                    iFsVal = iValue
                    continue
                if iValue < iFsVal:
                    iFsVal = iValue
            
        return iFsVal

    
    def CalCurValue(self):
        iVal = self.m_BaseValue
        if self.m_AddPositive:
            iVal += self.m_AddPositive
        if self.m_AddNegative:
            iVal += self.m_AddNegative
        if self.m_MulPositive:
            iVal = iVal * (10000 + self.m_MulPositive) / 10000
        if self.m_MulNegative:
            for iRatio in self.m_MulNegative:
                iVal = iVal * (10000 + iRatio) / 10000
            
        iVal = max(iVal, 1)
        iVal = math.ceil(iVal)
        return iVal



class CExplodeRadius(CBaseAttr):
    
    def CalCurValue(self):
        fVal = self.m_BaseValue
        if self.m_AddPositive:
            fVal += self.m_AddPositive
        if self.m_AddNegative:
            fVal += self.m_AddNegative
        if self.m_MulPositive:
            fVal = fVal * (10000 + self.m_MulPositive) * 0.0001
        if self.m_MulNegative:
            for iRatio in self.m_MulNegative:
                fVal = fVal * (10000 + iRatio) * 0.0001
            
        return fVal



class CMaxForceSetAttr(CBaseAttr):
    
    def CalForceCurValue(self):
        if self.m_ForceSetInfo:
            iFsVal = max(self.m_ForceSetInfo.values())
        else:
            iFsVal = None
        return iFsVal



class CMulAttr(CBaseAttr):
    
    def __init__(self, obj, sAttr, iVal, iFlag = BASEATTR_REFRESH):
        super(CMulAttr, self).__init__(obj, sAttr, iVal, iFlag)
        self.m_MulFactor = []
        self.m_MulFactorInfo = { }
        self.m_ExcessVal = 0

    
    def CalCurValue(self):
        iVal = super().CalCurValue()
        if self.m_MulFactor:
            for iMul in self.m_MulFactor:
                iVal = iVal * (10000 + iMul) // 10000
            
        return iVal + self.m_ExcessVal

    
    def AddMulFactor(self, obj, iMul, sKey):
        if sKey in self.m_MulFactorInfo:
            iOldMul = self.m_MulFactorInfo[sKey]
            if iOldMul == iMul:
                return None
            self.m_MulFactor.remove(iOldMul)
        self.m_MulFactor.append(iMul)
        self.m_MulFactorInfo[sKey] = iMul
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def GetExcludeValue(self, lstExcludeFactor = None):
        iVal = super().GetExcludeValue(lstExcludeFactor)
        if lstExcludeFactor is None:
            lstMulFactor = self.m_MulFactor
        else:
            lstMulFactor = self.m_MulFactor[:]
            for sKey in lstExcludeFactor:
                if sKey in self.m_MulFactorInfo:
                    lstMulFactor.remove(self.m_MulFactorInfo[sKey])
            
        if lstMulFactor:
            for iMul in lstMulFactor:
                iVal = iVal * (10000 + iMul) // 10000
            
        return iVal

    
    def ClearValue(self, obj, sKey):
        super().ClearValue(obj, sKey)
        if sKey not in self.m_MulFactorInfo:
            return None
        iMul = self.m_MulFactorInfo[sKey]
        self.m_MulFactor.remove(iMul)
        self.m_MulFactorInfo.pop(sKey)
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)

    
    def ClearAll(self):
        super().ClearAll()
        self.m_MulFactor = []
        self.m_MulFactorInfo = { }
        self.m_ExcessVal = 0

    
    def CalMulChangeRatio(self):
        fVal = super().CalMulChangeRatio()
        if self.m_MulFactor:
            for iMul in self.m_MulFactor:
                fVal = fVal * (10000 + iMul) / 10000
            
        return fVal

    
    def SetExcessVal(self, obj, iVal):
        self.m_ExcessVal = iVal
        self.UpdateRefresh(obj, MASK_REFRESH_VALUE)


g_AttrCls = {
    'MoveSpeed': CMoveSpeed,
    'ShieldRecoverTime': CShieldRecoverTime,
    'MaxBullet': CComMaxBullet,
    'Radius': CExplodeRadius,
    'ShieldMax': CMulAttr,
    'ArmorMax': CMulAttr,
    'HPMax': CMulAttr,
    'ColdTime': CMaxForceSetAttr }

def NewAttr(obj, sAttr, iValue, iRefresh):
    if sAttr not in g_AttrCls:
        return CBaseAttr(obj, sAttr, iValue, iRefresh)
    clsAttr = g_AttrCls[sAttr]
    return clsAttr(obj, sAttr, iValue, iRefresh)


def AfterRefreshHPMax(oWarrior, iOldValue, iCurValue):
    if not iOldValue:
        return None
    if oWarrior.IsDead():
        return None
    if iCurValue > oWarrior.m_HP:
        iOldHP = oWarrior.HP()
    else:
        iOldHP = iOldValue
    iNewHP = max(iOldHP * iCurValue // iOldValue, 100)
    iChange = iNewHP - oWarrior.m_HP
    oReason = cl_object.reason.CStrReason('属性上限刷新')
    oWarrior.HPDirectModify('HP', oWarrior.m_ID, iChange, oReason, iOldValue, iCalExcess = 0)
    oWarrior.UpdateExcessAttr('HP')


def AfterRefreshMaxBullet(oItem, iOldValue, iCurValue):
    oBulletCom = oItem.GetComponent('Bullet')
    oBulletCom.MaxBulletChange()


def AfterRefreshShieldMax(oWarrior, iOldValue, iCurValue):
    if oWarrior.IsDead():
        return None
    iOldShield = oWarrior.m_Shield
    if not iOldValue:
        iNewShield = iCurValue
    else:
        iNewShield = iOldShield * iCurValue // iOldValue
    iChange = iNewShield - oWarrior.m_Shield
    oReason = cl_object.reason.CStrReason('属性上限刷新')
    oWarrior.HPDirectModify('Shield', oWarrior.m_ID, iChange, oReason, iOldValue, iCalExcess = 0)
    oWarrior.UpdateShieldRecoverStatus()
    oWarrior.UpdateExcessAttr('Shield')


def AfterRefreshEnergyMax(oWarrior, iOldValue, iCurValue):
    if oWarrior.IsDead():
        return None
    iOldEnergy = oWarrior.m_Energy
    if not iOldValue:
        iNewEnergy = iCurValue
    else:
        iNewEnergy = iOldEnergy * iCurValue // iOldValue
    oWarrior.m_Energy = iNewEnergy
    oWarrior.GS2CPropChange('Energy')
    oWarrior.UpdateEnergyRecoverStatus()


def AfterRefreshRShield(oWarrior, iOldValue, iCurValue):
    oWarrior.UpdateShieldRecoverStatus()


def AfterRefreshREnergy(oWarrior, iOldValue, iCurValue):
    oWarrior.UpdateEnergyRecoverStatus()


def AfterRefreshTurnSpeed(oWarrior, iOldValue, iCurValue):
    if iOldValue == iCurValue:
        return None
    if oWarrior.m_FaceCtrl:
        oWarrior.m_FaceCtrl.RefreshTurnSpeed(iCurValue)


def AfterRefreshShieldRecoverTime(oWarrior, iOldValue, iCurValue):
    iHaltStartFrame = oWarrior.GetShieldRecoverHaltFrame()
    if iHaltStartFrame:
        iPassFrame = oWarrior.m_Game.GetFrameNum() - iHaltStartFrame
        iOldFrame = Time2Frame(iOldValue)
        iCurFrame = Time2Frame(iCurValue)
        iNewFrame = (iOldFrame - iPassFrame) * iCurFrame // iOldFrame
        oWarrior.UpdateHaltShieldRecover(iNewFrame)


def AfterRefreshArmorMax(oWarrior, iOldValue, iCurValue):
    if oWarrior.IsDead():
        return None
    iOldArmor = oWarrior.Armor()
    if not iOldValue:
        iNewArmor = iCurValue
    else:
        iNewArmor = iOldArmor * iCurValue // iOldValue
    iChange = iNewArmor - iOldArmor
    oReason = cl_object.reason.CStrReason('属性上限刷新')
    oWarrior.HPDirectModify('Armor', oWarrior.m_ID, iChange, oReason, iOldValue, iCalExcess = 0)
    oWarrior.UpdateExcessAttr('Armor')


def AfterDeviceEnergyMax(oWarrior, iOldValue, iCurValue):
    iOldDeviceEnergy = oWarrior.DeviceEnergy(iOldValue)
    if not iOldValue:
        iNewDeviceEnergy = iCurValue
    else:
        iNewDeviceEnergy = iOldDeviceEnergy * iCurValue // iOldValue
    iChange = iNewDeviceEnergy - iOldDeviceEnergy
    if iChange:
        oWarrior.TrueDeviceEnergyModify(iOldDeviceEnergy, iChange, True)


def AfterRefreshRDeviceEnergy(oWarrior, iOldValue, iCurValue):
    oWarrior.UpdateDeviceEnergyRecoverStatus()


def AfterRefreshMaxPFBullet(oPerform, iOldValue, iCurValue):
    if oPerform.m_Item:
        oWeapon = oPerform.GetMyItem()
        if oWeapon:
            oWeapon.OnMaxPFBulletChange(oPerform)
    iCurPFBullet = oPerform.CurPFBullet()
    if iCurPFBullet <= iCurValue:
        return None
    oPerform.m_CurPFBullet = iCurValue
    oPerform.RefreshCurPFBullet()


def AfterRefreshScale(oWarrior, iOldValue, iCurValue):
    if iOldValue == iCurValue:
        return None
    if oWarrior.m_FightType & WARRIOR_PET:
        oWarrior.SetModelScale(iCurValue)

g_RefreshAttrAfterFunc = {
    'HPMax': AfterRefreshHPMax,
    'MaxBullet': AfterRefreshMaxBullet,
    'ShieldMax': AfterRefreshShieldMax,
    'RShield': AfterRefreshRShield,
    'ShieldRecoverTime': AfterRefreshShieldRecoverTime,
    'ArmorMax': AfterRefreshArmorMax,
    'EnergyMax': AfterRefreshEnergyMax,
    'REnergy': AfterRefreshREnergy,
    'TurnSpeed': AfterRefreshTurnSpeed,
    'MaxDeviceEnergy': AfterDeviceEnergyMax,
    'MaxPFBullet': AfterRefreshMaxPFBullet,
    'RDeviceEnergy': AfterRefreshRDeviceEnergy,
    'Scale': AfterRefreshScale }

def BeforeRefreshRHP(oTarget, iCurValue):
    if not iCurValue:
        iNowFrame = oTarget.m_Game.GetFrameNum()
        oTarget.Set('CalHPFrame', iNowFrame)
    else:
        oTarget.HP()


def BeforeRefreshShieldMax(oTarget, iCurValue):
    oTarget.Shield()


def BeforeRefreshRShield(oTarget, iCurValue):
    oTarget.Shield()


def BeforeRefreshEnergyMax(oTarget, iCurValue):
    oTarget.Energy()

g_RefreshAttrBeforeFunc = {
    'RHP': BeforeRefreshRHP,
    'ShieldMax': BeforeRefreshShieldMax,
    'RShield': BeforeRefreshRShield,
    'EnergyMax': BeforeRefreshEnergyMax }
