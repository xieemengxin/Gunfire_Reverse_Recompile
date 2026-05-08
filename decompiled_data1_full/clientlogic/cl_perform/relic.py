# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/relic.pyc
# RelativePath: clientlogic/cl_perform/relic.pyc
# Source Generated with Decompyle++
# File: relic.pyc (Python 3.6)

from cl_perform.passive import CPerform
from cl_commondefines import PF_TYPE_RELIC, RELIC_TYPE_NORMAL, RELIC_TYPE_CURSE, RELIC_LIFECYCLE_EFFECTIVE_SEQUENCE, RELIC_LIFECYCLE_FORCE, RELIC_LIFECYCLE_TEMPLEVEL, RELIC_LIFECYCLE_DEFAULT
from cl_only import DeepCopy
import cl_object.lifecycle
import cl_msgcenter.eventcbobj

class CRelic(CPerform):
    m_MaxUpgradeTimes = 0
    m_PFType = PF_TYPE_RELIC
    m_ValidRemove = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_Source = 0
    m_BasePrice = 0
    m_RollNum = 0
    m_ForceLifeCycle = None
    m_ForceDisable = 0
    m_LifeCycleType = RELIC_LIFECYCLE_DEFAULT
    
    def __init__(self, oOwner, iLevel):
        super(CRelic, self).__init__(oOwner, iLevel)
        self.m_ShareInfo = { }
        self.m_OwnerInfo = { }
        self.m_TempLevel = 0
        self.m_SourceReason = 0
        self.m_LifeCycleTypeInfo = DeepCopy(RELIC_LIFECYCLE_EFFECTIVE_SEQUENCE)
        self.m_DisableSource = { }

    
    def Release(self):
        if self.m_ForceLifeCycle:
            self.m_ForceLifeCycle.Release()
            self.m_ForceLifeCycle = None
        super().Release()

    
    def Enable(self, oWarrior, iNotify = 0):
        if (self.m_DisableSource or self.m_ForceDisable) and not (self.m_ForceLifeCycle):
            return None
        super().Enable(oWarrior, iNotify)

    
    def CDCallBack(self, oWarrior):
        oContainer = self.m_Container
        oContainer.DelColdTime(self.m_SID)
        self.m_LifeCycle.CallFunc('ColdDown', oWarrior)

    
    def ValidRemove(self):
        if self.m_RelicType == RELIC_TYPE_CURSE:
            oHero = self.GetOwner()
            if not oHero:
                return 0
            return oHero.GetRemoveCurseRelicValid()
        iTempValidRemove = self.GetArgValue('TempValidRemove', -1)
        if iTempValidRemove != -1:
            return iTempValidRemove
        return self.m_ValidRemove

    
    def InitSource(self, iSource, iSourceReason = 0):
        if self.m_Source:
            return None
        if not self.m_Game.m_WarMgr.Query('RecycleSelf', 1):
            iSource = 0
        self.m_Source = iSource
        self.m_SourceReason = iSourceReason

    
    def SetRollNum(self, iRollNum):
        self.m_RollNum = iRollNum

    
    def SetForceDisable(self, iDisable):
        self.m_ForceDisable = iDisable

    
    def SetDisableSource(self, sKey):
        self.m_DisableSource[sKey] = 1

    
    def ClearDisableSource(self, sKey):
        if sKey in self.m_DisableSource:
            self.m_DisableSource.pop(sKey)

    
    def GetShareInfo(self):
        return self.m_ShareInfo

    
    def UploadPickInfo(self, dShareInfo):
        self.m_ShareInfo = dShareInfo

    
    def SetLifeCycle(self, oWarrior):
        self.m_LifeCycle = self.GetLifeCycle()

    
    def SetOtherLifeCycle(self, oWarrior, iLifeCycleType, dInfo):
        if iLifeCycleType == RELIC_LIFECYCLE_FORCE:
            enableFunc = dInfo['enableFunc']
            disableFunc = dInfo['disableFunc']
            cdFunc = dInfo['cdFunc']
            cbFunc = dInfo['cbFunc']
            self.SetForceLifeCycle(enableFunc, disableFunc, cdFunc, cbFunc)
        elif iLifeCycleType == RELIC_LIFECYCLE_TEMPLEVEL:
            iTempLevel = dInfo['TempLevel']
            self.SetTempLevelLifeCycle(iTempLevel)
        bNeedReEnable = False
        iOldLifeCycleType = self.m_LifeCycleType
        for iType, iApply in self.m_LifeCycleTypeInfo.items():
            if iApply:
                self.m_LifeCycleType = iType
                if iType != iOldLifeCycleType:
                    bNeedReEnable = True
                break
        
        self.OnSetLevel()
        if bNeedReEnable and self.m_Enable:
            self.Disable(oWarrior, iNotify = 0)
            self.Enable(oWarrior)

    
    def RemoveOtherLifeCycle(self, oWarrior, iLifeCycleType):
        bNeedReEnable = True if self.m_Enable and iLifeCycleType == self.m_LifeCycleType else False
        if bNeedReEnable:
            self.Disable(oWarrior, iNotify = 0)
        if iLifeCycleType == RELIC_LIFECYCLE_FORCE:
            self.RemoveForceLifeCycle()
        elif iLifeCycleType == RELIC_LIFECYCLE_TEMPLEVEL:
            self.RemoveTempLevelLifeCycle()
        for iType, iApply in self.m_LifeCycleTypeInfo.items():
            if iApply:
                self.m_LifeCycleType = iType
                break
        
        self.OnSetLevel()
        if bNeedReEnable:
            self.Enable(oWarrior)

    
    def GetLifeCycle(self):
        if self.m_LifeCycleType == RELIC_LIFECYCLE_FORCE:
            return self.m_ForceLifeCycle
        if self.m_LifeCycleType == RELIC_LIFECYCLE_TEMPLEVEL:
            return self.m_LifeCycleLevel[self.m_TempLevel]
        return self.m_LifeCycleLevel[self.m_Level]

    
    def SetForceLifeCycle(self, enableFunc, disableFunc, cdFunc, cbFunc):
        if self.m_ForceLifeCycle:
            return None
        self.m_LifeCycleTypeInfo[RELIC_LIFECYCLE_FORCE] = 1
        oLifeCycle = cl_object.lifecycle.CLifeCycle()
        oLifeCycle.Init(self, enableFunc, disableFunc)
        oLifeCycle.RegisterFunc('ColdDown', cdFunc)
        self.m_ForceLifeCycle = oLifeCycle
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(cbFunc, self.m_Key)
        oOwner = self.GetOwner()
        dMsgInfo = {
            'RelicSID': self.m_SID,
            'IsSet': 1 }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SET_CORERELIC, oOwner, dMsgInfo)

    
    def RemoveForceLifeCycle(self):
        if not self.m_ForceLifeCycle:
            return None
        self.m_ForceLifeCycle.Release()
        self.m_ForceLifeCycle = None
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_LifeCycleTypeInfo[RELIC_LIFECYCLE_FORCE] = 0
        oOwner = self.GetOwner()
        dMsgInfo = {
            'RelicSID': self.m_SID,
            'IsRemove': 1 }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVE_CORERELIC, oOwner, dMsgInfo)

    
    def SetTempLevelLifeCycle(self, iTempLevel):
        if iTempLevel not in self.m_LifeCycleLevel:
            return None
        self.m_LifeCycleTypeInfo[RELIC_LIFECYCLE_TEMPLEVEL] = 1
        self.m_TempLevel = iTempLevel

    
    def RemoveTempLevelLifeCycle(self):
        self.m_LifeCycleTypeInfo[RELIC_LIFECYCLE_TEMPLEVEL] = 0
        self.m_TempLevel = self.m_Level

    
    def GetLifeCycleLevel(self):
        if self.m_LifeCycleType == RELIC_LIFECYCLE_TEMPLEVEL:
            return self.m_TempLevel
        return self.m_Level

    
    def AttrCache(self):
        oOwner = self.GetOwner()
        dData = { }
        dData['pfid'] = self.m_SID
        dData['PFLV'] = self.GetLifeCycleLevel()
        dData['PFKey'] = self.Key()
        dData['PFType'] = self.m_PFType
        dData['PFMainPerform'] = self.m_MainPerform
        dData['AID'] = self.m_Owner
        dData['ArgData'] = { }
        dData['ArgData'].update(self.m_ArgData)
        dData['RS'] = cl_object.reason.CPerformReason(self.m_SID, self.m_Owner, oOwner.m_SID, oOwner.m_FightType)
        oItem = self.GetMyItem()
        dData['ItemID'] = oItem.m_ID if oItem else 0
        return dData


