# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/passive.pyc
# RelativePath: clientlogic/cl_perform/passive.pyc
# Source Generated with Decompyle++
# File: passive.pyc (Python 3.6)

from cl_perform.mobject import CBasePerform as CCustomPerform
from cl_commondefines import PF_TYPE_PASSIVE, TYPE_PASSIVE_TIME_CD, TYPE_PASSIVE_TIME_CYCLE
from cl_only import Time2Frame, SendAlert, Frame2Time
import cl_formula
import cl_object.reason
import cl_object.lifecycle

class CPerform(CCustomPerform):
    m_Name = '被动技能'
    m_PFType = PF_TYPE_PASSIVE
    m_EnableActionInfo = { }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_BaseLevelArgData = { }
    m_LiteCD = 0
    m_OwnerTask = 0
    m_TempLevel = 0
    
    def __init__(self, oOwner, iLevel):
        super(CPerform, self).__init__(oOwner, iLevel)
        self.m_LifeCycle = None
        self.m_LifeCycleLevel = { }
        self.m_FactorInfo = { }
        self.m_DelCyclePassFlag = 0
        self.SetLevelArg()
        for idx in range(1, self.m_MaxLevel + 1):
            oLifeCycle = cl_object.lifecycle.CLifeCycle()
            enableFunc = self.m_EnableActionInfo[idx] if idx in self.m_EnableActionInfo else None
            disableFunc = self.m_DisableActionInfo[idx] if idx in self.m_DisableActionInfo else None
            oLifeCycle.Init(self, enableFunc, disableFunc)
            cdFunc = self.m_ColdDownCBActionInfo[idx] if idx in self.m_ColdDownCBActionInfo else None
            oLifeCycle.RegisterFunc('ColdDown', cdFunc)
            self.m_LifeCycleLevel[idx] = oLifeCycle
        

    
    def Release(self):
        if self.m_LifeCycle:
            self.m_LifeCycle.Release()
            self.m_LifeCycle = None
        for oLifeCycle in self.m_LifeCycleLevel.values():
            oLifeCycle.Release()
        
        self.m_LifeCycleLevel = { }
        super().Release()

    
    def Enable(self, oWarrior, iNotify = 0):
        if not oWarrior.m_OnGame:
            return None
        if self.m_Enable or self.m_Level not in self.m_LifeCycleLevel:
            return None
        oItem = self.GetMyItem()
        if oItem and not (oItem.m_LifeCycle.m_Enable):
            return None
        super(CPerform, self).Enable(oWarrior, iNotify)
        self.SetLifeCycle(oWarrior)
        self.m_LifeCycle.Enable(oWarrior)

    
    def SetLifeCycle(self, oWarrior):
        self.m_LifeCycle = self.GetLifeCycle()

    
    def Disable(self, oWarrior, iNotify = 1, iReleaseFlag = 0):
        if not (self.m_Enable) or self.m_Level not in self.m_LifeCycleLevel:
            return None
        if iReleaseFlag:
            self.m_LifeCycle.PFAndStateDisable(oWarrior)
        else:
            self.m_LifeCycle.Disable(oWarrior)
        self.m_LifeCycle = None
        self.DelPassTime(oWarrior, TYPE_PASSIVE_TIME_CD)
        self.DelPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE)
        super(CPerform, self).Disable(oWarrior, iNotify)

    
    def SetPassTime(self, oWarrior, iType, iFrame, dArgs = None):
        if not dArgs:
            dArgs = { }
        oItem = self.GetMyItem()
        iItemID = oItem.m_ID if oItem else 0
        dPassInfo = {
            'pfid': self.m_SID,
            'ItemID': iItemID,
            'Type': iType,
            'Args': dArgs }
        dPassInfo.update(dArgs)
        idx = self.m_ID * 10 + iType
        oWarrior.AddPFPassTime(idx, iFrame, dPassInfo)
        return idx

    
    def DelPassTime(self, oWarrior, iType):
        idx = self.m_ID * 10 + iType
        if not idx:
            return None
        oWarrior.DelPFPassTime(idx)

    
    def HasPassTime(self, oWarrior, iType):
        idx = self.m_ID * 10 + iType
        if not idx:
            return 0
        return oWarrior.HasPFPassTime(idx)

    
    def DoPassTimeCallBack(self, oWarrior, dPassInfo):
        iType = dPassInfo['Type']
        if iType == TYPE_PASSIVE_TIME_CYCLE:
            self.CycleTimeCallBack(oWarrior, dPassInfo)
        elif iType == TYPE_PASSIVE_TIME_CD:
            self.CDCallBack(oWarrior)

    
    def CDCallBack(self, oWarrior):
        oContainer = self.m_Container
        oContainer.DelColdTime(self.m_SID)
        if self.m_Level not in self.m_LifeCycleLevel:
            return None
        self.m_LifeCycleLevel[self.m_Level].CallFunc('ColdDown', oWarrior)

    
    def SetCDTime(self, oWarrior, iFrame):
        if iFrame <= 0:
            SendAlert('err', f'''game:{oWarrior.m_Game.m_ID} CDTime is negative {self.m_FactorInfo}, Perform:{self.m_SID}''')
            return None
        self.m_Container.RefreshColdTime(self.m_SID, iFrame)
        self.SetPassTime(oWarrior, TYPE_PASSIVE_TIME_CD, iFrame)

    
    def DelCDTime(self, oWarrior):
        self.m_Container.DelColdTime(self.m_SID)
        self.DelPassTime(oWarrior, TYPE_PASSIVE_TIME_CD)
        self.CDCallBack(oWarrior)

    
    def ModifyColdTime(self, oWarrior, iModifyTime):
        iColdTime = self.m_Container.GetColdTime(self.m_SID)
        iNowTime = iColdTime + iModifyTime
        if iNowTime > 0:
            self.SetCDTime(oWarrior, iNowTime)
        else:
            self.DelCDTime(oWarrior)

    
    def CycleTimeCallBack(self, oWarrior, dPassInfo):
        dArgs = dPassInfo['Args']
        dEvent = self.AttrCache()
        dEvent['LifeCycle'] = self.m_LifeCycle
        self.m_EventCB.CBFuncAction(oWarrior, dArgs['Group'], dEvent, { })
        iCycleTime = dArgs['CycleTime']
        if iCycleTime > 0 and not (self.m_DelCyclePassFlag):
            self.SetPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE, iCycleTime, dArgs)

    
    def SetCycleTime(self, oWarrior, iFirstTime, iCycleTime, iBaseCycleTime, iGroup):
        dArgs = {
            'CycleTime': iCycleTime,
            'Group': iGroup,
            'BaseCycleTime': iBaseCycleTime }
        self.m_DelCyclePassFlag = 0
        self.SetPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE, iFirstTime, dArgs)

    
    def DelCycleTime(self, oWarrior):
        self.m_DelCyclePassFlag = 1
        self.DelPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE)

    
    def HasCycleTime(self, oWarrior):
        return self.HasPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE)

    
    def AddCycleTimeChange(self, oWarrior, iMul, iAdd, sKey):
        bResult = True
        if sKey in self.m_FactorInfo:
            bResult = False
            (iOldMul, iOldAdd) = self.m_FactorInfo[sKey]
            if iOldMul == iMul and iOldAdd == iAdd:
                return bResult
        self.m_FactorInfo[sKey] = (iMul, iAdd)
        if not self.UpdateCycleTime(oWarrior):
            self.m_FactorInfo.pop(sKey)
        return bResult

    
    def UpdateCycleTime(self, oWarrior):
        idx = self.m_ID * 10 + TYPE_PASSIVE_TIME_CYCLE
        dPassInfo = oWarrior.GetPFPassTimeInfo(idx)
        if 'Args' not in dPassInfo:
            return False
        dArgs = dPassInfo['Args']
        iCycleTime = self.GetCycleTimeChange(dArgs['BaseCycleTime'])
        if iCycleTime <= 0:
            iBaseCycleTime = dArgs['BaseCycleTime']
            SendAlert('err', f'''game:{oWarrior.m_Game.m_ID} CycleTime is negative iBaseCycleTime: {iBaseCycleTime}, FactorInfo:{self.m_FactorInfo}, Perform:{self.m_SID}''')
            return False
        dArgs['CycleTime'] = iCycleTime
        self.SetPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE, iCycleTime, dArgs)
        return True

    
    def ClearCycleTimeChange(self, sKey, oWarrior):
        if sKey not in self.m_FactorInfo:
            return None
        self.m_FactorInfo.pop(sKey)
        self.UpdateCycleTime(oWarrior)

    
    def UpdateCurCycleTime(self, oWarrior, iChange):
        idx = self.m_ID * 10 + TYPE_PASSIVE_TIME_CYCLE
        iCBFrame = oWarrior.GetTimeUnitCBFrameByIdx(idx)
        dPassInfo = oWarrior.GetPFPassTimeInfo(idx)
        if not iCBFrame or not dPassInfo:
            return None
        self.DelPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE)
        iNewCBFrame = iCBFrame + iChange
        iCurFrame = self.m_Game.GetFrameNum()
        if iNewCBFrame > iCurFrame:
            self.SetPassTime(oWarrior, TYPE_PASSIVE_TIME_CYCLE, iNewCBFrame - iCurFrame, dPassInfo)
        else:
            self.CycleTimeCallBack(oWarrior, dPassInfo)

    
    def GetCycleTimeChange(self, iBaseCycleFrame):
        iToatlMul = 10000 + sum((iMul for iMul, _ in self.m_FactorInfo.values()))
        iTotalAdd = sum((iAdd for _, iAdd in self.m_FactorInfo.values()))
        iResultCycleTime = (iBaseCycleFrame + iTotalAdd) * iToatlMul // 10000
        return iResultCycleTime

    
    def SetLiteCD(self, iTime):
        iFrame = Time2Frame(iTime)
        iMarkFrame = self.m_Game.GetFrameNum()
        self.m_LiteCD = iFrame + iMarkFrame

    
    def LoadLiteCD(self, iOldCDFrame):
        if iOldCDFrame < self.m_Game.GetFrameNum():
            return None
        self.m_LiteCD = iOldCDFrame

    
    def CheckLiteCD(self):
        if not self.m_LiteCD:
            return 0
        if self.m_LiteCD <= self.m_Game.GetFrameNum():
            return 0
        return 1

    
    def ModifyLiteCD(self, iFrame):
        if not self.m_LiteCD:
            return None
        self.m_LiteCD += iFrame

    
    def GetRemainLiteCD(self):
        iCurFrame = self.m_Game.GetFrameNum()
        iRemainFrame = self.m_LiteCD - iCurFrame
        if iRemainFrame <= 0:
            return 0
        return Frame2Time(iRemainFrame)

    
    def GetOwnerTask(self):
        if not self.m_OwnerTask:
            return None
        return self.GetOwner().m_TaskCon.GetTaskByID(self.m_OwnerTask)

    
    def SubDesc(cls, oWarrior):
        return '\x00'

    SubDesc = classmethod(SubDesc)
    
    def PreChooseAction(cls, oWarrior):
        pass

    PreChooseAction = classmethod(PreChooseAction)
    
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

    
    def GetLifeCycleLevel(self):
        if self.m_TempLevel:
            return self.m_TempLevel
        return self.m_Level

    
    def SetTempLevelLifeCycle(self, oWarrior, iTempLevel):
        if iTempLevel not in self.m_LifeCycleLevel:
            return None
        self.m_TempLevel = iTempLevel
        self.Disable(oWarrior, iNotify = 0)
        self.Enable(oWarrior)

    
    def ClearTempLevelLifeCycle(self, oWarrior):
        self.m_TempLevel = 0
        self.Disable(oWarrior, iNotify = 0)
        self.Enable(oWarrior)

    
    def GetLifeCycle(self):
        if self.m_TempLevel:
            return self.m_LifeCycleLevel[self.m_TempLevel]
        return self.m_LifeCycleLevel[self.m_Level]

    
    def SetLevelArg(self):
        iLevel = self.GetLifeCycleLevel()
        self.m_LevelArgData = { }
        if iLevel not in self.m_BaseLevelArgData:
            return None
        for sAttr, val in self.m_BaseLevelArgData[iLevel].items():
            iValue = cl_formula.GetFormulaResultByLV(self, val, iLevel)
            self.m_LevelArgData[sAttr] = iValue
        

    
    def GetLevelArg(self, sAttr, iDefault = 0):
        if sAttr not in self.m_LevelArgData:
            return iDefault
        return self.m_LevelArgData[sAttr]

    
    def OnSetLevel(self):
        self.SetLevelArg()


