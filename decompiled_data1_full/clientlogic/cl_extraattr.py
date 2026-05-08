# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_extraattr.pyc
# RelativePath: clientlogic/cl_extraattr.pyc
# Source Generated with Decompyle++
# File: cl_extraattr.pyc (Python 3.6)

import cl_msgcenter
from cl_commondefines import ALL_PERFORMCDRATE_TYPE, PERFORMCDRATE_TYPE_CAREER, PERFORMCDRATE_TYPE_PASSIVE, PERFORMCDRATE_TYPE_SHIFT

class CResistance(object):
    m_Limit = 9000
    
    def __init__(self, sAttr, iVal, iSync = 1):
        self.m_Attr = sAttr
        self.m_Refresh = 1
        self.m_ForceCurValue = None
        self.m_CurValue = iVal
        self.m_Resistance = { }
        self.m_Apply = { }
        self.m_RealValue = { }
        self.m_Sync = iSync

    
    def ModifyResistance(self, obj, iValue, iDamSrc, iElementType, iShow, sKey):
        tType = (iDamSrc, iElementType, iShow)
        if sKey in self.m_Apply:
            if tType in self.m_Apply[sKey]:
                iOldValue = self.m_Apply[sKey][tType]
                if iValue == iOldValue:
                    return None
                self.m_Resistance[tType] -= iOldValue
            self.m_Apply[sKey][tType] = iValue
        else:
            self.m_Apply[sKey] = {
                tType: iValue }
        if tType in self.m_Resistance:
            self.m_Resistance[tType] += iValue
        else:
            self.m_Resistance[tType] = iValue
        self.Refresh(obj)

    
    def ClearValue(self, obj, sKey):
        if sKey not in self.m_Apply:
            return None
        dApply = self.m_Apply.pop(sKey)
        for tType, iValue in dApply.items():
            if tType not in self.m_Resistance:
                continue
            self.m_Resistance[tType] -= iValue
        
        self.Refresh(obj)

    
    def Refresh(self, obj):
        (self.m_CurValue, self.m_RealValue) = self.CalResistanceValue()
        if self.m_Sync:
            obj.RefreshAttr(self.m_Attr, self.m_CurValue)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGERESISTANCE, obj, { })

    
    def CalResistanceValue(self):
        iCurValue = 0
        dRealValue = { }
        for (iDamSrc, iElementType, iShow), iValue in self.m_Resistance.items():
            tDamKey = (iDamSrc, iElementType)
            if iShow:
                iCurValue += iValue
            if tDamKey in dRealValue:
                dRealValue[tDamKey] += iValue
                continue
            dRealValue[tDamKey] = iValue
        
        if iCurValue > self.m_Limit:
            iCurValue = self.m_Limit
        return (iCurValue, dRealValue)

    
    def GetResistanceByType(self, iDamType):
        iTotal = 0
        for (iDamSrc, iElementType), iValue in self.m_RealValue.items():
            if iDamType & iDamSrc and iDamType & iElementType:
                iTotal += iValue
        
        if iTotal > self.m_Limit:
            iTotal = self.m_Limit
        return iTotal

    
    def ClearAll(self):
        self.m_Refresh = 0
        self.m_CurValue = 0
        self.m_BaseValue = 0
        self.m_Apply = { }
        self.m_ForceCurValue = None
        self.m_RealValue = { }

    
    def SetLimit(self, iLimit):
        self.m_Limit = iLimit



class CPerformCDRate(object):
    
    def __init__(self):
        self.m_PerformCDRate = dict.fromkeys(ALL_PERFORMCDRATE_TYPE, 0)
        self.m_Apply = { }

    
    def ModifyPerformCDRate(self, obj, iPerformType, iAdd, iMul, sKey):
        if iPerformType not in ALL_PERFORMCDRATE_TYPE:
            return None
        if sKey in self.m_Apply:
            if iPerformType in self.m_Apply[sKey] and (iAdd, iMul) == self.m_Apply[sKey][iPerformType]:
                return None
            self.m_Apply[sKey][iPerformType] = (iAdd, iMul)
        else:
            self.m_Apply[sKey] = {
                iPerformType: (iAdd, iMul) }
        self.Refresh(obj)

    
    def ClearValue(self, obj, sKey):
        if sKey not in self.m_Apply:
            return None
        self.m_Apply.pop(sKey)
        self.Refresh(obj)

    
    def Refresh(self, obj):
        self.CalPerformCDRate()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CHANGEPERFORMCDRATIO, obj, { })

    
    def CalPerformCDRate(self):
        dPositeive = {
            PERFORMCDRATE_TYPE_SHIFT: [
                10000,
                10000],
            PERFORMCDRATE_TYPE_PASSIVE: [
                10000,
                10000],
            PERFORMCDRATE_TYPE_CAREER: [
                10000,
                10000] }
        for dApply in self.m_Apply.values():
            for iType, (iAdd, iMul) in dApply.items():
                dPositeive[iType][0] += iAdd
                dPositeive[iType][1] *= (10000 + iMul) // 10000
            
        
        for iType, (iAdd, iMul) in dPositeive.items():
            self.m_PerformCDRate[iType] = iAdd * iMul // 10000 - 10000
        

    
    def GetPerformCDRateByType(self, iPerformType):
        return self.m_PerformCDRate[iPerformType]

    
    def GetAllPerformCDRate(self):
        return (self.m_PerformCDRate[PERFORMCDRATE_TYPE_CAREER], self.m_PerformCDRate[PERFORMCDRATE_TYPE_PASSIVE], self.m_PerformCDRate[PERFORMCDRATE_TYPE_SHIFT])


