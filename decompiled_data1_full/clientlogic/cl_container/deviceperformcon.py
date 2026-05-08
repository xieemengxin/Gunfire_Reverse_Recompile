# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/deviceperformcon.pyc
# RelativePath: clientlogic/cl_container/deviceperformcon.pyc
# Source Generated with Decompyle++
# File: deviceperformcon.pyc (Python 3.6)

from cl_object.logging import DeviceLog
from cl_commondefines import PF_TYPE_DEVICECOMP, PF_TYPE_DEVICEACTIVE, PERFORM_POS_MAIN, DEVICECOMP_TYPE_HERO, DEVICECOMP_TYPE_DEVICE, DEVICECOMP_TYPE_COMMON, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL
from cl_only import DeepCopy, ChooseKey
import cl_perform
import cl_snetwar as warnet
import cl_container.performcon
import cl_drop
import cl_platformdata
import cl_msgcenter
import cl_notify
import cl_formula

class CDevicePerformContainer(cl_container.performcon.CPerformContainer):
    
    def __init__(self, oWarrior):
        super().__init__(oWarrior)
        self.m_MaxPos = 0
        self.m_Component = { }
        self.m_EnableDeviceComp = { }
        self.m_Pos2DeviceComp = { }
        self.m_ExcludeComp = { }
        self.m_DeviceCompWeight = {
            DEVICECOMP_TYPE_COMMON: { },
            DEVICECOMP_TYPE_DEVICE: { },
            DEVICECOMP_TYPE_HERO: { } }
        self.m_AllDeviceComp = set()
        self.m_AcquiredComp = { }
        self.m_CurLevelChosenComp = { }
        self.m_ExcludeLevelChosenCompNum = 0

    
    def Release(self):
        oGame = self.m_Game
        oHero = oGame.GetObject(self.m_Owner)
        cl_msgcenter.DoneAttention(oHero, oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, 'ResetCompRecord')
        super().Release()

    
    def Save(self):
        dData = super().Save()
        dData['MP'] = self.m_MaxPos
        dData['EDC'] = dict(self.m_EnableDeviceComp)
        dData['CP'] = dict(self.m_Component)
        dData['AC'] = dict(self.m_AcquiredComp)
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.m_MaxPos = dData['MP']
        self.GS2CUpdateMaxPos()
        dPerformLevel = dData['PF']
        self.m_AcquiredComp = dData.get('AC', { })
        for iSID in dData['CP']:
            self.AddComponent(iSID, 'Load', dPerformLevel[iSID], iSync = 0)
        
        for iSID, iPos in dData['EDC'].items():
            self.EnableComponent(iSID, iPos, iSync = 0)
        
        self.RefreshDeviceCompInfo()

    
    def InitMaxPos(self, iMaxPos):
        if not self.m_MaxPos:
            self.m_MaxPos = iMaxPos

    
    def InitExcludeLevelChosenNum(self, iNum):
        self.m_ExcludeLevelChosenCompNum = iNum

    
    def OnAddDevice(self, sReason):
        self.InitDeviceCompWeight()
        self.GS2CUpdateMaxPos()
        if sReason in ('PlayerChoose', 'AutoChoose'):
            self.AddInitDeviceComp()
        oHero = self.m_Game.GetObject(self.m_Owner)
        cl_msgcenter.AddAttentionFunc(oHero, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelInit, 'ResetCompRecord')

    
    def AddInitDeviceComp(self):
        for iSID in self.m_DeviceCompWeight[DEVICECOMP_TYPE_COMMON]:
            self.AddComponent(iSID, 'InitComp', 1, iSync = 0)
        
        self.RefreshDeviceCompInfo()

    
    def AddAcquiredComp(self, iSID):
        self.m_AcquiredComp[iSID] = 1

    
    def ClearAll(self):
        for iSID in list(self.m_Component):
            self.RemoveComponent(iSID, 'ClearAll')
        
        oHero = self.m_Game.GetObject(self.m_Owner)
        for iSID in list(self.m_Perform):
            self.RemovePerform(oHero, iSID)
        

    
    def InitDeviceCompWeight(self):
        oHero = self.m_Game.GetObject(self.m_Owner)
        iDeviceSID = oHero.GetDeviceSID()
        dDeviceCompWeight = self.m_DeviceCompWeight
        dAllDeviceCompWeight = cl_platformdata.GetDeviceCompWeight()
        dDeviceCompWeight[DEVICECOMP_TYPE_HERO] = dict(dAllDeviceCompWeight[DEVICECOMP_TYPE_HERO].get(oHero.m_SID, { }).get(iDeviceSID, { }))
        dDeviceCompWeight[DEVICECOMP_TYPE_DEVICE] = dict(dAllDeviceCompWeight[DEVICECOMP_TYPE_DEVICE].get(iDeviceSID, { }))
        dDeviceCompWeight[DEVICECOMP_TYPE_COMMON] = dict(dAllDeviceCompWeight[DEVICECOMP_TYPE_COMMON])
        self.m_AllDeviceComp.update(dDeviceCompWeight[DEVICECOMP_TYPE_HERO].keys(), dDeviceCompWeight[DEVICECOMP_TYPE_DEVICE].keys(), dDeviceCompWeight[DEVICECOMP_TYPE_COMMON].keys())

    
    def OnLevelInit(self, oHero, oWarMgr, dMsgInfo):
        if 'LevelType' in dMsgInfo and dMsgInfo['LevelType'] in (LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, LEVEL_TYPE_HALL):
            self.m_CurLevelChosenComp = { }

    
    def CheckExcludeLevelChosen(self):
        iTotalLevel = 0
        for iSID in self.m_Component:
            oComp = self.m_Perform[iSID]
            iTotalLevel += oComp.m_Level
        
        if iTotalLevel > self.m_ExcludeLevelChosenCompNum:
            return 0
        return 1

    
    def AddLevelChosenInfo(self, lstChoose):
        for iSID in lstChoose:
            if iSID not in self.m_CurLevelChosenComp:
                self.m_CurLevelChosenComp[iSID] = 0
            self.m_CurLevelChosenComp[iSID] += 1
        

    
    def GetComponentChooseWeight(self, dChosen):
        dChooseWeight = { }
        for iType, dWeight in self.m_DeviceCompWeight.items():
            dTypeWeight = { }
            for iSID, iWeight in dWeight.items():
                iChosenCnt = dChosen[iSID] if iSID in dChosen else 0
                if iSID in self.m_Component:
                    oPerform = self.m_Perform[iSID]
                    iChosenCnt += oPerform.m_Level
                clsComponent = cl_perform.GetPerformModule(iSID)
                iExtWeight = 0 if iChosenCnt < clsComponent.m_MaxLevel or iSID in self.m_AcquiredComp else clsComponent.m_FirstChooseExtWeight
                dTypeWeight[iSID] = iWeight + iExtWeight
            
            if dTypeWeight:
                dChooseWeight[iType] = dTypeWeight
        
        return dChooseWeight

    
    def ChooseComponent(self, dRewardConfig, dChosen = None):
        lstResult = []
        iTotalNum = dRewardConfig.get('Num', 0)
        if iTotalNum <= 0:
            return lstResult
        dTypeWeight = dRewardConfig.get('Weight', { })
        dForceTypeNum = dRewardConfig.get('ForceNum', { })
        if self.CheckExcludeLevelChosen():
            dChosen = dict(self.m_CurLevelChosenComp)
        elif dChosen is None:
            dChosen = { }
        dChooseType = { }
        dChooseWeight = self.GetComponentChooseWeight(dChosen)
        oHero = self.m_Game.GetObject(self.m_Owner)
        for iType, iWeight in dTypeWeight.items():
            if iType not in dChooseWeight:
                continue
            iWeight = cl_formula.GetFormulaResult(oHero, iWeight)
            if iWeight > 0:
                dChooseType[iType] = iWeight
        
        for iType, iNum in dForceTypeNum.items():
            if iType not in dChooseType:
                continue
            if iTotalNum < iNum:
                iNum = iTotalNum
            lstComp = self.ChooseComponentExcludeMaxLevel(dChooseWeight, {
                iType: 1 }, iNum, dChosen)
            if iType not in dChooseWeight:
                dChooseType.pop(iType, 0)
            iTotalNum -= len(lstComp)
            lstResult.extend(lstComp)
            if iTotalNum <= 0:
                break
        
        if iTotalNum:
            lstComp = self.ChooseComponentExcludeMaxLevel(dChooseWeight, dChooseType, iTotalNum, dChosen)
            iTotalNum -= len(lstComp)
            lstResult.extend(lstComp)
            if iTotalNum and dChooseWeight:
                lstComp = self.ChooseComponentExcludeMaxLevel(dChooseWeight, dict.fromkeys(dChooseWeight, 1), iTotalNum, dChosen)
                iTotalNum -= len(lstComp)
                lstResult.extend(lstComp)
            if iTotalNum and self.m_Game.m_WarMgr.IsEndless():
                lstComp = self.ChooseComponentNoExclude(iTotalNum)
                lstResult.extend(lstComp)
        self.AddLevelChosenInfo(lstResult)
        return lstResult

    
    def ChooseComponentExcludeMaxLevel(self, dChooseWeight, dChooseType, iNum, dChosen):
        if not dChooseType or not dChooseWeight:
            return []
        lstResult = []
        oGame = self.m_Game
        for _ in range(iNum):
            iType = ChooseKey(oGame, dChooseType)
            if iType not in dChooseWeight:
                DeviceLog.Alert('%s %s type %s err %s %s' % (oGame.m_ID, self.m_PlayerID, iType, dChooseWeight, dChooseType))
                continue
            iSID = ChooseKey(oGame, dChooseWeight[iType])
            if not iSID:
                DeviceLog.Alert('%s %s type %s empty %s' % (oGame.m_ID, self.m_PlayerID, iType, dChooseWeight))
                continue
            self.AddAcquiredComp(iSID)
            lstResult.append(iSID)
            iChooseCnt = dChosen.setdefault(iSID, 0)
            dChosen[iSID] = iChooseCnt + 1
            clsComponent = cl_perform.GetPerformModule(iSID)
            iLeftCnt = clsComponent.m_MaxLevel - dChosen[iSID]
            if iSID in self.m_Component:
                iLeftCnt -= self.m_Perform[iSID].m_Level
            if iLeftCnt <= 0:
                dChooseWeight[iType].pop(iSID)
                if not dChooseWeight[iType]:
                    dChooseWeight.pop(iType)
                    dChooseType.pop(iType, 0)
                    if not not dChooseType:
                        if not dChooseWeight:
                            break
        
        return lstResult

    
    def ChooseComponentNoExclude(self, iNum):
        lstResult = []
        oGame = self.m_Game
        dChoose = dict.fromkeys(self.m_AllDeviceComp, 1)
        for _ in range(iNum):
            iSID = ChooseKey(oGame, dChoose)
            if not iSID:
                DeviceLog.Alert('%d %d choose empty %s' % (oGame.m_ID, self.m_PlayerID, dChoose))
                continue
            self.AddAcquiredComp(iSID)
            lstResult.append(iSID)
        
        return lstResult

    
    def GetDeviceCompWeight(self):
        return DeepCopy(self.m_DeviceCompWeight)

    
    def Refresh(self, dPlayer = None):
        if not self.m_MaxPos:
            return None
        super().Refresh(dPlayer)
        self.GS2CUpdateMaxPos()
        self.RefreshDeviceCompInfo()

    
    def SelfRefresh(self):
        self.Refresh()

    
    def RefreshDeviceCompInfo(self):
        dDeviceCompInfo = { }
        for iSID in self.m_Component:
            oPerform = self.m_Perform[iSID]
            if iSID not in self.m_EnableDeviceComp:
                iPos = 0
            else:
                iPos = self.m_EnableDeviceComp[iSID]
            dDeviceCompInfo[iSID] = [
                [
                    oPerform.m_Level,
                    iPos]]
        
        self.GS2CUpdateAllDeviceCompInfo(dDeviceCompInfo)

    
    def AddMaxPos(self, iAdd):
        DeviceLog.Debug('%d %d add maxpos cur:%d add:%d' % (self.m_Game.m_ID, self.m_PlayerID, self.m_MaxPos, iAdd))
        self.m_MaxPos += iAdd
        self.GS2CUpdateMaxPos()

    
    def GetComponent(self, iSID):
        if iSID not in self.m_Component:
            return None
        return self.m_Perform[iSID]

    
    def PickComponent(self, iSID, sReason):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if iSID in self.m_Component:
            if self.ValidRecycle(iSID):
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLE_DEVICECOMP, oOwner, {
                    'DeviceComponent': iSID })
                cl_notify.SendCommonNotify(self.m_Game, [
                    oOwner.m_PlayerID], 9480, { })
            else:
                self.UpgradeComponent(iSID, sReason)
        else:
            self.AddComponent(iSID, sReason)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ADD_DEVICE, oOwner, {
            'DeviceComponent': iSID })

    
    def ValidPickComponent(self, iSID, sReason):
        if iSID in self.m_Component:
            return self.ValidUpgradeComponent(iSID, sReason)
        return self.ValidAddComponent(iSID, sReason)

    
    def ValidComponentMaxLevel(self, iSID):
        if iSID not in self.m_Component:
            return False
        oPerform = self.m_Perform[iSID]
        return oPerform.m_Level == oPerform.m_MaxLevel

    
    def AddComponent(self, iSID, sReason, iLevel = 1, iSync = 1):
        if not self.ValidAddComponent(iSID, sReason):
            return 0
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        DeviceLog.Debug('%d %d add %d %s %s' % (oGame.m_ID, self.m_PlayerID, iSID, iLevel, sReason))
        oPerform = self.AddPerform(oOwner, iSID, iLevel, 0, 0)
        if not oPerform:
            DeviceLog.Alert('%d %d add %d err %s' % (oGame.m_ID, self.m_PlayerID, iSID, sReason))
            return 0
        self.m_Component[iSID] = 1
        self.AddAcquiredComp(iSID)
        if iSync:
            self.GS2CUpdateComponentLevel(iSID, oPerform.m_Level)
        return 1

    
    def ValidAddComponent(self, iSID, sReason):
        clsComponent = cl_perform.GetPerformModule(iSID)
        oGame = self.m_Game
        if not clsComponent:
            DeviceLog.Alert('%d %d %d invalid %s' % (oGame.m_ID, self.m_PlayerID, iSID, sReason))
            return False
        if clsComponent.m_PFType != PF_TYPE_DEVICECOMP:
            DeviceLog.Alert('%d %d add %d %s type %s err' % (oGame.m_ID, self.m_PlayerID, iSID, sReason, clsComponent.m_PFType))
            return False
        oOwner = oGame.GetObject(self.m_Owner)
        iDeviceSID = oOwner.GetDeviceSID()
        if not iDeviceSID:
            DeviceLog.Alert('%d %d add %d %s no device' % (oGame.m_ID, self.m_PlayerID, iSID, sReason))
            return False
        tExclusiveDevice = clsComponent.m_ExclusiveDevice
        if tExclusiveDevice and iDeviceSID not in tExclusiveDevice:
            DeviceLog.Alert('%d %d add %d %s device %s %s err' % (oGame.m_ID, self.m_PlayerID, iSID, sReason, iDeviceSID, tExclusiveDevice))
            return False
        tExclusiveHero = clsComponent.m_ExclusiveHero
        if tExclusiveHero and oOwner.m_SID not in tExclusiveHero:
            DeviceLog.Alert('%d %d add %d %s hero %s %s err' % (oGame.m_ID, self.m_PlayerID, iSID, sReason, oOwner.m_SID, tExclusiveHero))
            return False
        return True

    
    def UpgradeComponent(self, iSID, sReason):
        if not self.ValidUpgradeComponent(iSID, sReason):
            return False
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        oPerform = self.m_Perform[iSID]
        iCurLevel = oPerform.m_Level
        DeviceLog.Debug('%d %d upgrade %d curlevel:%d %s' % (oGame.m_ID, self.m_PlayerID, iSID, iCurLevel, sReason))
        oPerform.SetLevel(oOwner, iCurLevel + 1)
        self.GS2CUpdateComponentLevel(iSID, oPerform.m_Level)

    
    def ValidUpgradeComponent(self, iSID, sReason):
        if iSID not in self.m_Component:
            DeviceLog.Alert('%s %s upgrade %d %s err' % (self.m_Game.m_ID, self.m_PlayerID, iSID, sReason))
            return False
        oPerform = self.m_Perform[iSID]
        if oPerform.m_Level + 1 > oPerform.m_MaxLevel and not self.ValidRecycle(iSID):
            if not self.m_Game.m_WarMgr.IsEndless():
                DeviceLog.Debug('%s %s upgrade %d cur:%d max:%d %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, oPerform.m_Level, oPerform.m_MaxLevel, sReason))
            return False
        return True

    
    def ValidRecycle(self, iDeviceComp):
        if not self.m_Game.m_WarMgr.IsEndless():
            return False
        if iDeviceComp not in self.m_Perform:
            return False
        oPerform = self.m_Perform[iDeviceComp]
        if oPerform.m_Level < oPerform.m_MaxLevel:
            return False
        for iComp in self.m_AllDeviceComp:
            if iComp not in self.m_Perform:
                return False
            oPerform = self.m_Perform[iComp]
            if oPerform.m_Level < oPerform.m_MaxLevel:
                return False
        
        return True

    
    def DegradeComponent(self, iSID):
        if not self.ValidDegradeComponent(iSID):
            return None
        oGame = self.m_Game
        oHero = oGame.GetObject(self.m_Owner)
        if iSID in self.m_EnableDeviceComp:
            oDevice = oHero.GetDevice()
            oDevice.OnUpdateEnableDeviceComp()
        oPerform = self.m_Perform[iSID]
        iCurLevel = oPerform.m_Level
        DeviceLog.Debug('%d %d degrade %d cur:%d' % (oGame.m_ID, self.m_PlayerID, iSID, iCurLevel))
        iNewLevel = iCurLevel - 1
        if iNewLevel <= 0:
            self.RemoveComponent(iSID, 'Degrade')
        else:
            oPerform.SetLevel(oHero, iNewLevel)
            self.GS2CUpdateComponentLevel(iSID, oPerform.m_Level)
        dInfo = {
            'DropSource': oHero.m_PlayerID }
        cl_drop.DropPerform(oHero, iSID, dInfo, bFly = True, iShare = 1)

    
    def ValidDegradeComponent(self, iSID):
        if iSID not in self.m_Component:
            return False
        if iSID in self.m_DeviceCompWeight[DEVICECOMP_TYPE_COMMON]:
            oPerform = self.m_Perform[iSID]
            if oPerform.m_Level == 1:
                return False
        return True

    
    def RemoveComponent(self, iSID, sReason):
        if iSID not in self.m_Component:
            return None
        DeviceLog.Debug('%d %d remove %d %s' % (self.m_Game.m_ID, self.m_PlayerID, iSID, sReason))
        self.DisableComponent(iSID)
        oOwner = self.m_Game.GetObject(self.m_Owner)
        self.m_Component.pop(iSID, 0)
        self.RemovePerform(oOwner, iSID)
        self.GS2CUpdateComponentLevel(iSID, 0)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVE_DEVICECOMP, oOwner, {
            'DeviceComponent': iSID })

    
    def GetAllEnableComponentLevel(self):
        iLevel = 0
        for iSID in self.m_EnableDeviceComp:
            oPerform = self.m_Perform[iSID]
            iLevel += oPerform.m_Level
        
        return iLevel

    
    def GetAllDeviceComp(self):
        dDeviceComp = { }
        for oPerform in self.m_Perform.values():
            if not oPerform.m_PFType == PF_TYPE_DEVICECOMP:
                continue
            dDeviceComp[oPerform.m_SID] = oPerform.m_Level
        
        return dDeviceComp

    
    def GetDevicePerformByType(self, iType, iOnlyEnable):
        dTargetPerform = self.m_EnableDeviceComp if iOnlyEnable else self.m_Component
        dResult = { }
        for iPerformSID in dTargetPerform:
            oPerform = self.m_Perform[iPerformSID]
            if oPerform.m_Type == iType:
                dResult[iPerformSID] = oPerform.m_Level
        
        return dResult

    
    def GetAllEnableDeviceCompLevel(self):
        dEnableDeviceComp = { }
        for iPerform in self.m_EnableDeviceComp:
            if iPerform not in self.m_Perform:
                DeviceLog.Alert('deviceperformcon not %s %s %s' % (iPerform, list(self.m_Perform), self.m_EnableDeviceComp))
                continue
            oPerform = self.m_Perform[iPerform]
            dEnableDeviceComp[iPerform] = oPerform.m_Level
        
        return dEnableDeviceComp

    
    def GetAllEnableDeviceComp(self):
        return self.m_EnableDeviceComp

    
    def UpdateComponentPos(self, iSID, iPos):
        if iSID not in self.m_Component:
            return None
        oOwner = self.m_Game.GetObject(self.m_Owner)
        oDevice = oOwner.GetDevice()
        if not oDevice:
            return None
        oDevice.OnUpdateEnableDeviceComp()
        if iSID in self.m_EnableDeviceComp:
            if iPos == self.m_EnableDeviceComp[iSID]:
                return None
            self.DisableComponent(iSID)
        if not iPos:
            return None
        if iPos in self.m_Pos2DeviceComp:
            self.DisableComponent(self.m_Pos2DeviceComp[iPos])
        self.EnableComponent(iSID, iPos)

    
    def EnableComponent(self, iSID, iPos, iSync = 1):
        if not self.ValidEnableComponent(iSID, iPos):
            return None
        DeviceLog.Debug('%d %d enable %d %d' % (self.m_Game.m_ID, self.m_PlayerID, iSID, iPos))
        self.m_Pos2DeviceComp[iPos] = iSID
        self.m_EnableDeviceComp[iSID] = iPos
        oPerform = self.m_Perform[iSID]
        oOwner = self.m_Game.GetObject(self.m_Owner)
        self.UpdateExcludeComp(oPerform, iEnable = 1)
        oPerform.OnEnableComponent(oOwner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ENABLE_DEVICECOMP_CHANGE, oOwner, {
            'Enable': 1,
            'DeviceComponent': iSID,
            'DeviceCompType': oPerform.m_Type,
            'DeviceCom': iSID,
            'ExcludeComp': oPerform.m_ExcludeComp })
        if iSync:
            self.GS2CUpdateComponentPos(iSID, iPos)

    
    def ValidEnableComponent(self, iSID, iPos):
        if iPos <= 0 or iPos > self.m_MaxPos:
            return False
        if iSID not in self.m_Component:
            return False
        if iSID in self.m_ExcludeComp:
            return False
        if iSID in self.m_EnableDeviceComp:
            return False
        if iPos in self.m_Pos2DeviceComp:
            return False
        return True

    
    def DisableComponent(self, iSID):
        if iSID not in self.m_EnableDeviceComp:
            return None
        DeviceLog.Debug('%d %d disable %d %d' % (self.m_Game.m_ID, self.m_PlayerID, iSID, self.m_EnableDeviceComp[iSID]))
        oOwner = self.m_Game.GetObject(self.m_Owner)
        oPerform = self.m_Perform[iSID]
        oPerform.OnDisableComponent(oOwner)
        self.UpdateExcludeComp(oPerform, iEnable = 0)
        iPos = self.m_EnableDeviceComp.pop(iSID)
        self.m_Pos2DeviceComp.pop(iPos, 0)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_ENABLE_DEVICECOMP_CHANGE, oOwner, {
            'Enable': 0,
            'DeviceComponent': iSID })
        self.GS2CUpdateComponentPos(iSID, 0)

    
    def UpdateExcludeComp(self, oPerform, iEnable):
        tExcludeComp = oPerform.m_ExcludeComp
        dExcludeComp = self.m_ExcludeComp
        if iEnable:
            for iSID in tExcludeComp:
                if iSID not in dExcludeComp:
                    dExcludeComp[iSID] = 0
                dExcludeComp[iSID] += 1
            
        else:
            for iSID in tExcludeComp:
                if iSID not in dExcludeComp:
                    continue
                dExcludeComp[iSID] -= 1
                if dExcludeComp[iSID] <= 0:
                    dExcludeComp.pop(iSID)
            

    
    def GetComponentPos(self, iSID):
        if iSID not in self.m_EnableDeviceComp:
            return 0
        return self.m_EnableDeviceComp[iSID]

    
    def OnDeployDevice(self):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        for iSID in self.m_EnableDeviceComp:
            oPerform = self.m_Perform[iSID]
            oPerform.OnDeploy(oOwner)
        

    
    def OnRecycleDevice(self):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        for iSID in self.m_EnableDeviceComp:
            oPerform = self.m_Perform[iSID]
            oPerform.OnRecycle(oOwner)
        

    
    def GS2CUpdateComponentPos(self, iSID, iPos):
        warnet.GS2CUpdateDeviceCompPos(self.m_PlayerID, iSID, iPos)

    
    def GS2CUpdateComponentLevel(self, iSID, iLevel):
        warnet.GS2CUpdateDeviceCompLevel(self.m_PlayerID, iSID, iLevel)

    
    def GS2CUpdateMaxPos(self):
        warnet.GS2CDeviceCompMaxPos(self.m_PlayerID, self.m_MaxPos)

    
    def GS2CUpdateAllDeviceCompInfo(self, dDeviceCompInfo):
        warnet.GS2CUpdateAllDeviceCompInfo(self.m_PlayerID, dDeviceCompInfo)


