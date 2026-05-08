# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_object/elementtype.pyc
# RelativePath: clientlogic/cl_object/elementtype.pyc
# Source Generated with Decompyle++
# File: elementtype.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_THUNDER, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_NORMAL, DAM_TYPE_TRUE
from cl_commondefines import BASEATTR_CLIENT, WEAPON_ELEMENTREFRESH_SET, WEAPON_ELEMENTREFRESH_REMOVE
from cl_only import WeakProxy
import cl_msgcenter
PrioriElementType = [
    DAM_TYPE_THUNDER,
    DAM_TYPE_FIRE,
    DAM_TYPE_CORRISION,
    DAM_TYPE_NORMAL,
    DAM_TYPE_TRUE]

class CElementType(object):
    
    def __init__(self, oAttrObj, iDamType, iFlag = BASEATTR_CLIENT):
        self.m_Flag = iFlag
        self.m_Value = iDamType
        self.m_AttrObj = WeakProxy(oAttrObj)
        self.m_ModifyDict = {
            'BaseType': iDamType }

    
    def RefreshValue(self):
        listValue = self.m_ModifyDict.values()
        for iElementType in PrioriElementType:
            if iElementType in listValue:
                self.m_Value = iElementType
                break
        else:
            self.m_Value = DAM_TYPE_NORMAL
        self.m_AttrObj.m_ElementType = self.m_Value
        if self.m_Flag & BASEATTR_CLIENT:
            self.m_AttrObj.RefreshAttr('ElementType', self.m_Value)

    
    def GetValue(self):
        return self.m_Value

    
    def SetModify(self, sKey, iDamType):
        self.m_ModifyDict[sKey] = iDamType
        self.RefreshValue()

    
    def RemoveSetModify(self, sKey):
        if sKey in self.m_ModifyDict:
            iElementType = self.m_ModifyDict.pop(sKey)
            self.RefreshValue()
            return iElementType

    
    def GetExcludeValue(self, sTargetKey):
        lstElementValue = [ iValue for sKey, iValue in self.m_ModifyDict.items() if sKey != sTargetKey ]
        for iElementType in PrioriElementType:
            if iElementType in lstElementValue:
                iReslutElementType = iElementType
                break
        else:
            iReslutElementType = DAM_TYPE_NORMAL
        return iReslutElementType



class CWeaponElementType(CElementType):
    
    def SetModify(self, sKey, iElementType):
        self.m_ModifyDict[sKey] = iElementType
        self.RefreshValue(sKey, WEAPON_ELEMENTREFRESH_SET, iElementType)

    
    def RemoveSetModify(self, sKey):
        if sKey in self.m_ModifyDict:
            iElementType = self.m_ModifyDict.pop(sKey)
            self.RefreshValue(sKey, WEAPON_ELEMENTREFRESH_REMOVE, iElementType)
            return iElementType

    
    def RefreshValue(self, sKey, iType, iElementType):
        super(CWeaponElementType, self).RefreshValue()
        if not self.m_AttrObj.m_Game:
            return None
        oTarget = self.m_AttrObj.m_Game.GetObject(self.m_AttrObj.m_Owner)
        if not oTarget:
            return None
        iHoldPos = self.m_AttrObj.GetComponent('Hold').HoldPos()
        dMsgInfo = {
            'ElementType': self.m_Value,
            'Weapon': self.m_AttrObj.m_ID,
            'HoldType': iHoldPos,
            'Reason': sKey,
            'RefreshElementType': iElementType }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_WEAPON_ELEMENTTYPE_REFRESH, oTarget, dMsgInfo, iSub = iType)



class CPerformElementType(CElementType):
    
    def RefreshValue(self):
        super(CPerformElementType, self).RefreshValue()
        oPerform = self.m_AttrObj
        oGame = oPerform.m_Game
        if not oGame:
            return None
        oTarget = oGame.GetObject(self.m_AttrObj.m_Owner)
        if not oTarget:
            return None
        dMsgInfo = {
            'Perform': oPerform.m_SID,
            'DamType': self.m_Value }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PERFORM_ELEMENTTYPE_REFRESH, oTarget, dMsgInfo, iSub = oPerform.m_SubMsg)


