# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_season/mobject.pyc
# RelativePath: clientlogic/cl_season/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import SendAlert, WeakProxy, DeepCopy
from cl_object.lifecycle import CLifeCycle
from cl_object.logging import SeasonLog
from cl_commondefines import SEASONTASK_EXTINFO_TYPE_ELEABNORMAL, SEASONTASK_EXTINFO_TYPE_HERO, SEASONTASK_EXTINFO_TYPE_BENE, SEASONTASK_EXTINFO_TYPE_DEVICE, SEASONTASK_EXTINFO_TYPE_DEVICECOM, SEASONTASK_EXTINFO_TYPE_RELIC, SEASONTASK_EXTINFO_TYPE_WEAPONTYPE, SEASONSUBTASK_TYPE_ADD, SEASONSUBTASK_TYPE_MAX, SEASONTASK_EXTINFO_TYPE_WAND, SEASONTASK_EXTINFO_TYPE_SPECIALITEM, SEASONTASK_EXTINFO_TYPE_DICEPOINT, SEASONTASK_EXTINFO_TYPE_DICE, SEASONTASK_EXTINFO_TYPE_S7CRYSTAL, SEASONTASK_EXTINFO_TYPE_S7MODULE
import cl_msgcenter
import cl_msgcenter.eventcbobj
import cllib.lib_flag
import cl_snetwar as warnet
from . import NewSeasonTask, GetSeasonVersion, GetSeasonTaskCls, GetWarSeasonTask

class CSeasonTask(object):
    m_SID = 0
    m_TargetValue = 0
    m_TaskValue = 0
    m_ShowTotalValue = 0
    m_ShowAccuracy = 1
    m_WarShowAccuracy = 1
    m_Reward = None
    m_Action = (None, None)
    m_CBFuncAction = { }
    m_WarExtInfoType = { }
    m_SubTaskInfo = { }
    m_Difficulty = 1
    
    def __init__(self, oTaskMgr, iCurValue):
        self.m_TaskMgr = WeakProxy(oTaskMgr)
        self.m_ArgData = { }
        self.m_Owner = self.m_TaskMgr.m_Owner
        self.m_Game = self.m_TaskMgr.m_Game
        self.m_Key = 'SeaonTask%d-%d-%d' % (self.m_TaskMgr.m_PlayerID, self.m_TaskMgr.m_Season, self.m_SID)
        self.m_CurValue = iCurValue
        self.m_Enable = 0
        self.m_EventCB = cl_msgcenter.eventcbobj.CEventCB(self.m_CBFuncAction, self.m_Key)
        self.m_LifeCycle = CLifeCycle()
        self.m_LifeCycle.Init(self, self.m_Action[0], self.m_Action[1])

    
    def Release(self):
        self.m_LifeCycle.Disable(self.GetOwner())
        self.m_LifeCycle.Release()
        self.m_TaskMgr = None
        self.m_ArgData = { }
        self.m_Game = None

    
    def Enable(self):
        if self.m_Enable:
            return None
        self.m_LifeCycle.Enable(self.GetOwner())
        self.m_Enable = 1

    
    def Disable(self):
        if not self.m_Enable:
            return None
        self.m_LifeCycle.Disable(self.GetOwner())
        self.m_Enable = 0

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def Key(self):
        return self.m_Key

    
    def AttrCache(self):
        dData = {
            'AID': self.m_Owner,
            'SeasonTaskSID': self.m_SID }
        return dData

    
    def GetShowInfo(self):
        iShowAccuracy = self.m_WarShowAccuracy
        if self.m_ShowTotalValue:
            oOwner = self.m_Game.GetObject(self.m_Owner)
            if not oOwner:
                return (0, self.m_ShowTotalValue // iShowAccuracy)
            iCur = oOwner.QuerySavedData(self.m_Key, 0)
            return (iCur // iShowAccuracy, self.m_ShowTotalValue // iShowAccuracy)
        return (self.m_CurValue // iShowAccuracy, self.m_TargetValue // iShowAccuracy)

    
    def GetArgValue(self, sArgs, iDefault = 0):
        if sArgs not in self.m_ArgData:
            return iDefault
        return self.m_ArgData[sArgs]

    
    def SetArgValue(self, sArgs, val):
        self.m_ArgData[sArgs] = val

    
    def SetArgValueDefault(self, sArgs, val):
        if sArgs not in self.m_ArgData:
            self.m_ArgData[sArgs] = val
            return val
        return self.m_ArgData[sArgs]



class CSeasonTaskMgr(object):
    m_ShowExtInfoType = {
        'Hero': SEASONTASK_EXTINFO_TYPE_HERO,
        'Bene': SEASONTASK_EXTINFO_TYPE_BENE,
        'Device': SEASONTASK_EXTINFO_TYPE_DEVICE,
        'DeviceCom': SEASONTASK_EXTINFO_TYPE_DEVICECOM,
        'NewRelic': SEASONTASK_EXTINFO_TYPE_RELIC,
        'WeaponType': SEASONTASK_EXTINFO_TYPE_WEAPONTYPE,
        'Eleabnormal': SEASONTASK_EXTINFO_TYPE_ELEABNORMAL,
        'WandSID': SEASONTASK_EXTINFO_TYPE_WAND,
        'SpecialItemSID': SEASONTASK_EXTINFO_TYPE_SPECIALITEM,
        'Point': SEASONTASK_EXTINFO_TYPE_DICEPOINT,
        'DiceSID': SEASONTASK_EXTINFO_TYPE_DICE,
        'CrystalSID': SEASONTASK_EXTINFO_TYPE_S7CRYSTAL,
        'ModuleSID': SEASONTASK_EXTINFO_TYPE_S7MODULE }
    m_ExtInfoTypeKeyList = {
        SEASONTASK_EXTINFO_TYPE_S7MODULE: [
            'ModuleSID'],
        SEASONTASK_EXTINFO_TYPE_S7CRYSTAL: [
            'CrystalSID'],
        SEASONTASK_EXTINFO_TYPE_DICE: [
            'DiceSID'],
        SEASONTASK_EXTINFO_TYPE_DICEPOINT: [
            'Point'],
        SEASONTASK_EXTINFO_TYPE_SPECIALITEM: [
            'SpecialItemSID'],
        SEASONTASK_EXTINFO_TYPE_WAND: [
            'WandSID'],
        SEASONTASK_EXTINFO_TYPE_ELEABNORMAL: [
            'Eleabnormal'],
        SEASONTASK_EXTINFO_TYPE_WEAPONTYPE: [
            'WeaponType'],
        SEASONTASK_EXTINFO_TYPE_RELIC: [
            'NewRelic'],
        SEASONTASK_EXTINFO_TYPE_DEVICECOM: [
            'DeviceCom'],
        SEASONTASK_EXTINFO_TYPE_DEVICE: [
            'Device'],
        SEASONTASK_EXTINFO_TYPE_BENE: [
            'Bene',
            'iPerform'],
        SEASONTASK_EXTINFO_TYPE_HERO: [
            'Hero'] }
    
    def __init__(self, oGame, iOwner, iPlayerID):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayerID
        self.m_SeasonTask = { }
        self.m_InitTaskValue = { }
        self.m_InitSubTaskValue = { }
        self.m_Season = oGame.m_WarMgr.m_SeasonNum
        self.m_CurDone = { }
        self.m_PreShow = { }
        self.m_DoneTask = { }
        self.m_ExtInfo = { }
        self.m_ShowExtInfo = { }
        self.m_RefreshShowExtInfo = { }
        cl_msgcenter.AddFunction(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, self.OnAddAllPlayer, 'InitSeasonTaskMgr' + str(self.m_PlayerID), -1, 0)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'InitSeasonTaskMgr' + str(self.m_PlayerID))
        for oSeasonTask in self.m_SeasonTask.values():
            oSeasonTask.Release()
        
        self.m_SeasonTask = { }
        self.m_DoneTask = { }
        self.m_Game = None

    
    def InitSeasonTask(self):
        if not cllib.lib_flag.g_OpenSeason:
            return None
        for oSeasonTask in list(self.m_SeasonTask.values()):
            oSeasonTask.Enable()
        
        warnet.GS2CSeasonTaskDone(self.m_DoneTask, self.m_PlayerID)

    
    def LoadSeasonTask(self, dSeasonTask):
        if not cllib.lib_flag.g_OpenSeason:
            return None
        if self.m_Season != GetSeasonVersion():
            if self.m_Season != 0 or not (cllib.lib_flag.g_IsAuthorityRun):
                SeasonLog.Debug('%d %d %d illegal season' % (self.m_Game.m_ID, self.m_PlayerID, self.m_Season))
            return None
        SeasonLog.Info('%d %d %d wartask %s' % (self.m_Game.m_ID, self.m_PlayerID, self.m_Season, dSeasonTask))
        iSeasonNum = self.m_Season
        dNewSeasonTask = GetWarSeasonTask(iSeasonNum)
        for iSID, iCurValue in dSeasonTask['War'].items():
            if iSID not in dNewSeasonTask:
                SeasonLog.Alert('%d %d %d illegal seasontask %d' % (self.m_Game.m_ID, self.m_PlayerID, iSeasonNum, iSID))
                continue
            if iSID not in self.m_SeasonTask:
                oSeasonTask = NewSeasonTask(iSeasonNum, iSID, self, iCurValue)
                if not oSeasonTask:
                    SendAlert('err', f'''赛季{iSeasonNum} 任务{iSID} 配置不存在''')
                    continue
                self.m_SeasonTask[iSID] = oSeasonTask
                if oSeasonTask.m_WarExtInfoType:
                    dExtInfo = dSeasonTask['ExtInfo'][iSID] if iSID in dSeasonTask['ExtInfo'] else { }
                    self.InitSeasonTaskExtInfo(oSeasonTask, dExtInfo)
            self.m_InitTaskValue[iSID] = iCurValue
        
        self.PretreatmentShowdata(dSeasonTask)

    
    def PretreatmentShowdata(self, dSeasonTask):
        dGSTask = dSeasonTask['GS']
        for iTask, (iValue, iTotalValue) in dGSTask.items():
            if iTask in dSeasonTask['ExtInfo']:
                self.InitGSTaskShowExtInfo(iTask, dSeasonTask['ExtInfo'][iTask])
            tExtInfo = self.GetShowExtInfo(iTask)
            self.m_PreShow[iTask] = [
                (iValue, iTotalValue, tExtInfo)]
        
        dWarTask = GetWarSeasonTask(self.m_Season)
        for iTask, iTargetValue in dSeasonTask['Done'].items():
            if iTask in dWarTask:
                clsTask = GetSeasonTaskCls(self.m_Season, iTask)
                iShowAccuracy = clsTask.m_WarShowAccuracy
                if clsTask.m_ShowTotalValue:
                    iShowValue = clsTask.m_ShowTotalValue // iShowAccuracy
                else:
                    iShowValue = iTargetValue // iShowAccuracy
                self.m_DoneTask[(iTask, iShowValue)] = 1
                continue
            self.m_DoneTask[(iTask, iTargetValue)] = 1
        

    
    def InitGSTaskShowExtInfo(self, iTask, dExtInfo):
        lstExtShowInfo = []
        for iType, lstSub in dExtInfo.items():
            lstExtSubShowInfo = []
            for iSub in lstSub:
                lstExtSubShowInfo.append((iSub, 0, 0))
            
            lstExtShowInfo.append((iType, lstExtSubShowInfo))
        
        self.m_ShowExtInfo[iTask] = lstExtShowInfo

    
    def AddTaskValue(self, iSID, iAdd):
        if iSID not in self.m_SeasonTask:
            return None
        oSeasonTask = self.m_SeasonTask[iSID]
        oSeasonTask.m_CurValue += iAdd
        if oSeasonTask.m_CurValue >= oSeasonTask.m_TargetValue:
            self.DoneSeasonTask(iSID)

    
    def AddTaskVauleBySubTask(self, oSeasonTask, iType, iSubTask, iAdd, iAddType):
        if not (oSeasonTask.m_SubTaskInfo) or iType not in oSeasonTask.m_SubTaskInfo or iSubTask not in oSeasonTask.m_SubTaskInfo[iType]:
            SendAlert('err', '%d任务配置了异常的子任务进度添加,对应策划请检查配置' % oSeasonTask.m_SID)
            return None
        iTaskSID = oSeasonTask.m_SID
        dExtInfo = self.m_ExtInfo[iTaskSID] if iTaskSID in self.m_ExtInfo else { }
        dExtSubInfo = dExtInfo[iType] if iType in dExtInfo else { }
        if iSubTask in dExtSubInfo:
            (iCurValue, iTotalValue) = dExtSubInfo[iSubTask]
        else:
            iCurValue = 0
            iTotalValue = oSeasonTask.m_SubTaskInfo[iType][iSubTask]
        if iCurValue >= iTotalValue:
            return None
        iCurValue += iAdd
        if iCurValue > iTotalValue:
            iAdd = iAdd - iCurValue - iTotalValue
            iCurValue = iTotalValue
        dExtSubInfo[iSubTask] = (iCurValue, iTotalValue)
        dExtInfo[iType] = dExtSubInfo
        self.m_ExtInfo[iTaskSID] = dExtInfo
        self.SetRefreshShowExtInfo(iTaskSID, iType, iSubTask)
        if iAddType == SEASONSUBTASK_TYPE_ADD:
            self.AddTaskValue(iTaskSID, iAdd)
        elif iAddType == SEASONSUBTASK_TYPE_MAX:
            iMaxSubValue = 0
            for _, (iCurValue, _) in dExtSubInfo.items():
                if iCurValue > iMaxSubValue:
                    iMaxSubValue = iCurValue
            
            oSeasonTask = self.m_SeasonTask[iTaskSID]
            if iMaxSubValue > oSeasonTask.m_CurValue:
                self.AddTaskValue(iTaskSID, iMaxSubValue - oSeasonTask.m_CurValue)

    
    def SetRefreshShowExtInfo(self, iTaskSID, iType, iSubTask):
        self.m_RefreshShowExtInfo[(iTaskSID, iType, iSubTask)] = 1

    
    def SetTaskValue(self, iSID, iNewValue):
        if iSID not in self.m_SeasonTask:
            return None
        oSeasonTask = self.m_SeasonTask[iSID]
        oSeasonTask.m_CurValue = iNewValue
        if oSeasonTask.m_CurValue >= oSeasonTask.m_TargetValue:
            self.DoneSeasonTask(iSID)

    
    def InitSeasonTaskExtInfo(self, oSeasonTask, dInitExtInfo):
        iSID = oSeasonTask.m_SID
        lstExtShowInfo = []
        for iType in oSeasonTask.m_WarExtInfoType:
            lstShowSub = []
            dInitInfo = self.m_InitSubTaskValue.setdefault(iSID, { })
            if oSeasonTask.m_SubTaskInfo and iType in oSeasonTask.m_SubTaskInfo:
                dInitSubTaskInfo = dInitInfo.setdefault(iType, { })
                for iSub in oSeasonTask.m_SubTaskInfo[iType]:
                    iCur = 0
                    iTotal = oSeasonTask.m_SubTaskInfo[iType][iSub]
                    if iType in dInitExtInfo and iSub in dInitExtInfo[iType]:
                        (iCur, iTotal) = dInitExtInfo[iType][iSub]
                    lstShowSub.append((iSub, iCur, iTotal))
                    dInitSubTaskInfo[iSub] = iCur
                
            elif iType not in dInitExtInfo:
                continue
            lstSub = dInitExtInfo[iType]
            for iSub in lstSub:
                lstShowSub.append((iSub, 0, 0))
            
            dInitInfo[iType] = DeepCopy(lstSub)
            lstExtShowInfo.append((iType, lstShowSub))
        
        self.m_ShowExtInfo[iSID] = lstExtShowInfo
        self.m_ExtInfo[iSID] = dInitExtInfo

    
    def UpdateExtShowInfo(self):
        if not self.m_RefreshShowExtInfo:
            return None
        for iTask, iUpdateType, iUpdateSubSID in self.m_RefreshShowExtInfo:
            iUpdateSubCurValue = 0
            iUpdateSubTotalValue = 0
            clsTask = GetSeasonTaskCls(self.m_Season, iTask)
            if clsTask.m_SubTaskInfo and iUpdateType in clsTask.m_SubTaskInfo:
                (iUpdateSubCurValue, iUpdateSubTotalValue) = self.m_ExtInfo[iTask][iUpdateType][iUpdateSubSID]
            lstShowExtInfo = self.m_ShowExtInfo[iTask] if iTask in self.m_ShowExtInfo else []
            if not lstShowExtInfo:
                lstSub = [
                    (iUpdateSubSID, iUpdateSubCurValue, iUpdateSubTotalValue)]
                lstShowExtInfo.append((iUpdateType, lstSub))
                self.m_ShowExtInfo[iTask] = lstShowExtInfo
                continue
            for iShowIndex, tShowExtInfo in enumerate(lstShowExtInfo):
                (iType, lstSub) = tShowExtInfo
                if not lstSub:
                    lstSub.append((iUpdateSubSID, iUpdateSubCurValue, iUpdateSubTotalValue))
                    continue
                for iSubIndex, (iSub, _, _) in enumerate(lstSub):
                    if iSub == iUpdateSubSID:
                        lstSub[iSubIndex] = (iSub, iUpdateSubCurValue, iUpdateSubTotalValue)
                        break
                
                if iType == iUpdateType:
                    lstShowExtInfo[iShowIndex] = (iType, lstSub)
                    break
            else:
                lstSub = [
                    (iUpdateSubSID, iUpdateSubCurValue, iUpdateSubTotalValue)]
                lstShowExtInfo.append((iUpdateType, lstSub))
            self.m_ShowExtInfo[iTask] = lstShowExtInfo
        
        self.m_RefreshShowExtInfo = { }

    
    def GetShowExtInfo(self, iSID):
        if iSID in self.m_ShowExtInfo:
            return self.m_ShowExtInfo[iSID]
        return []

    
    def GetKeyListByIntKey(self, iType):
        if iType in self.m_ExtInfoTypeKeyList:
            return self.m_ExtInfoTypeKeyList[iType]
        return []

    
    def GetSeasonTaskExtInfo(self, iSID):
        if iSID not in self.m_ExtInfo:
            return { }
        return self.m_ExtInfo[iSID]

    
    def RemoveSeasonTaskExtInfo(self, iSID):
        if iSID in self.m_ExtInfo:
            self.m_ExtInfo.pop(iSID)

    
    def SetSeasonTaskExtInfoByType(self, iSID, iType, lstValue):
        if iSID in self.m_ExtInfo and iType in self.m_ExtInfo[iSID]:
            self.m_ExtInfo[iSID][iType] = lstValue

    
    def SetSeasonTaskExtInfo(self, iSID, iType, Data):
        dExtInfo = self.m_ExtInfo.setdefault(iSID, { })
        if isinstance(Data, int):
            lstExtTypeInfo = dExtInfo.setdefault(iType, [])
            lstExtTypeInfo.append(Data)
            iSub = Data
        else:
            dExtTypeInfo = dExtInfo.setdefault(iType, { })
            (iSub, iCur, iTotal) = Data
            dExtTypeInfo[iSub] = (iCur, iTotal)
        self.SetRefreshShowExtInfo(iSID, iType, iSub)

    
    def DoneSeasonTask(self, iSID):
        SeasonLog.Info('%d %d %d donewartask %d' % (self.m_Game.m_ID, self.m_PlayerID, self.m_Season, iSID))
        oSeasonTask = self.m_SeasonTask.pop(iSID)
        self.m_CurDone[iSID] = oSeasonTask.m_CurValue
        oSeasonTask.Release()

    
    def SeasonTaskChangedReport(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl or oLevelCtrl.CheckFirstHall():
            return { }
        dTaskChanged = { }
        dExtInfoChanged = { }
        dChanged = { }
        for iSID, oSeasonTask in self.m_SeasonTask.items():
            if oSeasonTask.m_SubTaskExtProcess:
                continue
            iInitValue = self.m_InitTaskValue[iSID]
            iCurValue = oSeasonTask.m_CurValue
            if iCurValue > iInitValue:
                dTaskChanged[iSID] = iCurValue - iInitValue
                self.m_InitTaskValue[iSID] = iCurValue
            dTaskExtInfoChange = self.DealSubTaskValueChangeInfo(iSID)
            if dTaskExtInfoChange:
                dExtInfoChanged[iSID] = dTaskExtInfoChange
        
        for iSID, iCurValue in self.m_CurDone.items():
            iInitValue = self.m_InitTaskValue[iSID]
            dTaskChanged[iSID] = iCurValue - iInitValue
        
        self.m_CurDone = { }
        if dTaskChanged:
            dChanged['SeasonTask'] = dTaskChanged
        if dExtInfoChanged:
            dChanged['SeasonTaskExtInfo'] = dExtInfoChanged
        return dChanged

    
    def DealSubTaskValueChangeInfo(self, iSID):
        if iSID not in self.m_ExtInfo:
            return { }
        dExtInfoChange = { }
        clsTask = GetSeasonTaskCls(self.m_Season, iSID)
        for iType in clsTask.m_WarExtInfoType:
            if iType not in self.m_ExtInfo[iSID]:
                continue
            Data = self.m_ExtInfo[iSID][iType]
            if isinstance(Data, dict):
                ChangeData = { }
                for iSub, (iCur, iTotal) in Data.items():
                    if iSub not in self.m_InitSubTaskValue[iSID][iType]:
                        continue
                    iInit = self.m_InitSubTaskValue[iSID][iType][iSub]
                    if iCur > iInit:
                        iAdd = iCur - iInit
                        ChangeData[iSub] = (iAdd, iTotal)
                        self.m_InitSubTaskValue[iSID][iType][iSub] += iAdd
                
            else:
                ChangeData = []
                if iType not in self.m_InitSubTaskValue[iSID]:
                    self.m_InitSubTaskValue[iSID][iType] = []
                lstInitSub = self.m_InitSubTaskValue[iSID][iType]
                lstCurSub = self.m_ExtInfo[iSID][iType]
                ChangeData = list(set(lstCurSub) - set(lstInitSub))
                self.m_InitSubTaskValue[iSID][iType].extend(ChangeData)
            if not ChangeData:
                continue
            dExtInfoChange[iType] = ChangeData
        
        return dExtInfoChange

    
    def GetAllSeasonTaskData(self):
        dData = { }
        for iSID in self.m_InitTaskValue:
            tExtInfo = self.GetShowExtInfo(iSID)
            if iSID in self.m_SeasonTask:
                oSeasonTask = self.m_SeasonTask[iSID]
                (iCur, iTotal) = oSeasonTask.GetShowInfo()
                dData[iSID] = [
                    (iCur, iTotal, tExtInfo)]
                continue
            clsTask = GetSeasonTaskCls(self.m_Season, iSID)
            iShowAccuracy = clsTask.m_WarShowAccuracy
            if clsTask.m_ShowTotalValue:
                dData[iSID] = [
                    (clsTask.m_ShowTotalValue // iShowAccuracy, clsTask.m_ShowTotalValue // iShowAccuracy, tExtInfo)]
                continue
            dData[iSID] = [
                (clsTask.m_TargetValue // iShowAccuracy, clsTask.m_TargetValue // iShowAccuracy, tExtInfo)]
        
        dData.update(self.m_PreShow)
        return dData

    
    def GetSeasonInfo(self, iSeasonSID):
        dResult = { }
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if iSeasonSID not in self.m_SeasonTask:
            return dResult
        if not oOwner:
            return dResult
        oSeasonTask = self.m_SeasonTask[iSeasonSID]
        sKey = oSeasonTask.m_Key
        dResult['sKey'] = sKey
        iWarSeasonTaskValue = oOwner.QuerySavedData(sKey, 0)
        dResult['WarSeasonTaskValue'] = iWarSeasonTaskValue
        return dResult

    
    def Refresh(self):
        if not self.m_DoneTask:
            return None
        warnet.GS2CSeasonTaskDone(self.m_DoneTask, self.m_PlayerID)

    
    def OnAddAllPlayer(self, oWarMgr, dInfo):
        oHero = oWarMgr.m_Game.GetObject(self.m_Owner)
        if oHero:
            oHero.m_SeasonTaskMgr.InitSeasonTask()

    
    def Pause(self, sReason):
        SeasonLog.Debug('%d %d seasontask pause %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason))
        for oSeasonTask in list(self.m_SeasonTask.values()):
            oSeasonTask.Disable()
        

    
    def Resume(self, sReason):
        SeasonLog.Debug('%d %d seasontask resume %s' % (self.m_Game.m_ID, self.m_PlayerID, sReason))
        for oSeasonTask in list(self.m_SeasonTask.values()):
            oSeasonTask.Enable()
        


