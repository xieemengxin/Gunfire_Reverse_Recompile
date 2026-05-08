# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season7/crystal.pyc
# RelativePath: clientlogic/cl_seasonplay/season7/crystal.pyc
# Source Generated with Decompyle++
# File: crystal.pyc (Python 3.6)

from cl_item.baseitem import CBaseItem
from cl_cscommondef import CRYSTAL_MASK
from cl_only import ShufferList, ChooseRange
from cl_object.logging import BackpackLog
from cl_commondefines import S7CRYSTAL_POINTADD
import cl_msgcenter
CALPOINT_CNTMAX = 4

class CCrystalData(object):
    m_SID = 0
    m_Name = ''
    m_Type = CRYSTAL_MASK
    m_CanRotate = False
    m_GridConfig = { }
    m_MaxPoint = 0
    m_CanChoosePoint = { }
    
    def Create(cls, oGame, oCrystalCon, dCrystal, iPointID = 0, dTmp = None):
        oCrystal = CCrystal(oGame, 0, iPointID, dTmp)
        cls.InitItemData(oCrystal)
        if oCrystalCon:
            oCrystal.AddToContainer(oCrystalCon)
        if dCrystal:
            oCrystal.Load(dCrystal)
        if not oCrystal.m_PointInfo:
            iChoosePoint = dCrystal['TP'] if 'TP' in dCrystal else 0
            dInitPointInfo = cls.CalInitPointInfo(oGame, iChoosePoint)
            oCrystal.Init(iTotalPoint = iChoosePoint, dInitPointInfo = dInitPointInfo)
        else:
            oCrystal.Init()
        return oCrystal

    Create = classmethod(Create)
    
    def InitItemData(cls, oCrystal):
        oCrystal.m_SID = cls.m_SID
        oCrystal.m_Name = cls.m_Name
        oCrystal.m_Type = cls.m_Type
        oCrystal.m_CanRotate = cls.m_CanRotate
        oCrystal.m_GridConfig = dict(cls.m_GridConfig)
        oCrystal.m_MaxPoint = cls.m_MaxPoint
        oCrystal.m_CanChoosePoint = cls.m_CanChoosePoint

    InitItemData = classmethod(InitItemData)
    
    def CalInitPointInfo(cls, oGame, iChoosePoint):
        if not iChoosePoint:
            return { }
        dResult = { }
        dGridConfig = cls.m_GridConfig
        lstKey = list(dGridConfig)
        iTotalPoint = iChoosePoint
        lstRandomPoint = ShufferList(oGame, lstKey)
        for tPos in lstRandomPoint:
            (iPointMin, _) = dGridConfig[tPos]
            iPoint = min(iPointMin, iTotalPoint)
            iTotalPoint -= iPoint
            dResult[tPos] = iPoint
        
        if not iTotalPoint:
            return dResult
        for tPos in lstRandomPoint:
            (_, iPointMax) = cls.m_GridConfig[tPos]
            iGapPoint = iPointMax - dResult[tPos]
            if not iGapPoint:
                continue
            iPoint = ChooseRange(oGame, 0, iGapPoint)
            iPoint = min(iPoint, iTotalPoint)
            iTotalPoint -= iPoint
            dResult[tPos] += iPoint
            if not iTotalPoint:
                return dResult
        
        for iCount in range(1, CALPOINT_CNTMAX):
            for tPos, (iPointMin, iPointMax) in cls.m_GridConfig.items():
                iGapPoint = iPointMax - dResult[tPos]
                if not iGapPoint:
                    continue
                if iCount + 1 == CALPOINT_CNTMAX:
                    iPoint = iGapPoint
                else:
                    iPoint = ChooseRange(oGame, 0, iPointMax)
                    iPoint = min(iPoint, iGapPoint)
                iPoint = min(iPoint, iTotalPoint)
                iTotalPoint -= iPoint
                dResult[tPos] += iPoint
                if not iTotalPoint:
                    return dResult
            
        
        return dResult

    CalInitPointInfo = classmethod(CalInitPointInfo)


class CCrystal(CBaseItem):
    m_CanRotate = False
    m_GridConfig = { }
    m_RotateLimit = 4
    m_CanChoosePoint = { }
    
    def __init__(self, oGame, iTemp = 0, iPointID = 0, dTmp = None):
        super().__init__(oGame, iTemp, iPointID, dTmp)
        self.m_GameID = oGame.m_ID
        self.m_TotalPoint = 0
        self.m_PointInfo = { }
        self.m_ExtPointInfo = { }
        self.m_Rotate = 0
        self.m_MaxPoint = 0

    
    def __str__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-s7crystal%s-%s-%s-%s-%s' % (self.m_GameID, iPlayerID, self.m_SID, self.m_Grade, self.m_ID, self.m_TotalPoint, self.GetNowTotalPoint())

    
    def __repr__(self):
        iPlayerID = 0
        if self.m_Game and self.m_Owner:
            oOwner = self.GetOwner()
            if oOwner:
                iPlayerID = oOwner.m_PlayerID
        return '%s-%s-s7crystal%s-%s-%s-%s-%s' % (self.m_GameID, iPlayerID, self.m_SID, self.m_Grade, self.m_ID, self.m_TotalPoint, self.GetNowTotalPoint())

    
    def Load(self, dData):
        super().Load(dData)
        self.m_SID = dData.get('SID', 0)
        self.m_TotalPoint = dData.get('TP', 0)
        self.m_PointInfo = dData.get('PI', { })
        self.m_ExtPointInfo = dData.get('EP', { })
        self.m_Rotate = dData.get('R', 0)

    
    def Save(self):
        dData = super().Save()
        dData['SID'] = self.m_SID
        dData['TP'] = self.m_TotalPoint
        dData['PI'] = dict(self.m_PointInfo)
        dData['EP'] = dict(self.m_ExtPointInfo)
        dData['R'] = self.m_Rotate
        return dData

    
    def Init(self, iGrade = 1, iTotalPoint = 0, dInitPointInfo = None):
        super().Init(iGrade)
        if iTotalPoint:
            self.m_TotalPoint = iTotalPoint
        self.SetPointInfo(dInitPointInfo)

    
    def SetPointInfo(self, dInitPointInfo):
        if not dInitPointInfo or self.m_PointInfo:
            return None
        self.m_PointInfo = dInitPointInfo

    
    def IsFull(self):
        if sum(self.m_PointInfo.values()) < self.m_MaxPoint:
            return 0
        return 1

    
    def GetCanAddPointGrid(self, iMaxPoint = 0):
        lstGrid = []
        iRotate = self.m_Rotate
        for tPos, iPoint in self.m_PointInfo.items():
            tInitPos = self.RotatePos(tPos, -iRotate)
            if tInitPos not in self.m_GridConfig:
                BackpackLog.Alert('%s pointinfo err %s %s' % (self, self.m_PointInfo, self.m_GridConfig))
                continue
            (_, iPointMax) = self.m_GridConfig[tInitPos]
            if iPointMax:
                iPointMax = max(iMaxPoint, iPointMax)
            if iPoint < iPointMax:
                lstGrid.append(tPos)
        
        return lstGrid

    
    def GetNowTotalPoint(self):
        return sum(self.m_PointInfo.values())

    
    def AddPoint(self, iTotalPoint, lstGrid):
        if not iTotalPoint:
            return None
        oGame = self.m_Game
        lstGrid = ShufferList(oGame, lstGrid)
        iRotate = self.m_Rotate
        for iCount in range(1, CALPOINT_CNTMAX):
            for tPos in lstGrid:
                tInitPos = self.RotatePos(tPos, -iRotate)
                if tInitPos not in self.m_GridConfig:
                    BackpackLog.Alert('%s pointinfo err %s %s' % (self, self.m_PointInfo, self.m_GridConfig))
                    continue
                (iPointMin, iPointMax) = self.m_GridConfig[tInitPos]
                iGapPoint = iPointMax - self.m_PointInfo[tPos]
                if not iGapPoint:
                    continue
                if iCount + 1 == CALPOINT_CNTMAX:
                    iPoint = iGapPoint
                else:
                    iPoint = ChooseRange(oGame, iPointMin, iGapPoint)
                iPoint = min(iPoint, iTotalPoint)
                iTotalPoint -= iPoint
                self.m_PointInfo[tPos] += iPoint
                if not iTotalPoint:
                    return None
            
        

    
    def IsExtPointEffect(self):
        return self.m_TotalPoint < sum(self.m_PointInfo.values())

    
    def AddExtPoint(self, sKey, iTotalPoint, lstGrid, iMaxPoint = 0):
        if not iTotalPoint:
            return None
        if self.ReEnableExtPointEffect(sKey):
            return None
        oGame = self.m_Game
        lstGrid = ShufferList(oGame, lstGrid)
        lstGrid2 = lstGrid[:]
        iRotate = self.m_Rotate
        dPlayer = self.m_ExtPointInfo.setdefault(self.GetOwner().m_PlayerID, { })
        dExtPoint = dPlayer.setdefault(sKey, { })
        dTempPoint = { }
        for _ in range(iTotalPoint):
            if not lstGrid2 or not iTotalPoint:
                return None
            tRandomPos = lstGrid2[oGame.Random(len(lstGrid2))]
            tInitPos = self.RotatePos(tRandomPos, -iRotate)
            if tInitPos not in self.m_GridConfig:
                BackpackLog.Alert('%s pointinfo err %s %s' % (self, self.m_PointInfo, self.m_GridConfig))
                lstGrid2.remove(tRandomPos)
                continue
            (_, iPointMax) = self.m_GridConfig[tInitPos]
            if iPointMax:
                iPointMax = max(iPointMax, iMaxPoint)
            iTotalPoint -= 1
            if tRandomPos in dTempPoint:
                dTempPoint[tRandomPos] += 1
            else:
                dTempPoint[tRandomPos] = 1
            if tInitPos in dExtPoint:
                dExtPoint[tInitPos] += 1
            else:
                dExtPoint[tInitPos] = 1
            if self.m_PointInfo[tRandomPos] + dTempPoint[tRandomPos] >= iPointMax:
                lstGrid2.remove(tRandomPos)
        
        self.TrueAddExtPoint(list(dTempPoint.items()))

    
    def ClearExtPoint(self, sKey, iRemove = 1):
        iPlayerID = self.GetOwner().m_PlayerID
        if iPlayerID not in self.m_ExtPointInfo:
            return None
        if not self.IsExtPointEffect():
            return None
        if iRemove:
            dExtPoint = self.m_ExtPointInfo[iPlayerID].pop(sKey, { })
        else:
            dExtPoint = self.m_ExtPointInfo[iPlayerID][sKey]
        for tPos, iPoint in dExtPoint.items():
            tNewPos = self.RotatePos(tPos, self.m_Rotate)
            if tNewPos not in self.m_PointInfo:
                BackpackLog.Alert('%s clear extpoint err %s %s %s' % (self, dExtPoint, self.m_PointInfo, self.m_Rotate))
                continue
            self.m_PointInfo[tNewPos] -= iPoint
        

    
    def ReEnableExtPointEffect(self, sKey, oWarrior = None):
        if oWarrior:
            iPlayerID = oWarrior.m_PlayerID
        else:
            iPlayerID = self.GetOwner().m_PlayerID
        if iPlayerID not in self.m_ExtPointInfo:
            return 0
        if sKey not in self.m_ExtPointInfo[iPlayerID]:
            return 0
        if self.IsExtPointEffect():
            return -1
        dExtPoint = self.m_ExtPointInfo[iPlayerID][sKey]
        lstPoint = []
        for tPos, iPoint in dExtPoint.items():
            tNewPos = self.RotatePos(tPos, self.m_Rotate)
            if tNewPos not in self.m_PointInfo:
                BackpackLog.Alert('%s extpoint effect err %s %s %s' % (self, dExtPoint, self.m_PointInfo, self.m_Rotate))
                continue
            lstPoint.append((tNewPos, iPoint))
        
        self.TrueAddExtPoint(lstPoint)
        return 1

    
    def TrueAddExtPoint(self, lstPointInfo):
        iAddPoint = 0
        for tPos, iPoint in lstPointInfo:
            self.m_PointInfo[tPos] += iPoint
            iAddPoint += iPoint
        
        if self.m_Owner:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONITEMCHANGE, self.GetOwner(), {
                'S7Item': self.m_ID,
                'CrystalSID': self.m_SID,
                'AddPoint': iAddPoint }, iSub = S7CRYSTAL_POINTADD)

    
    def GetPointInfo(self):
        return self.m_PointInfo

    
    def Rotate(self, iRotate = 1):
        if iRotate <= 0:
            return None
        self.m_PointInfo = self.GetEffPointByRotate(iRotate)
        self.m_Rotate = (self.m_Rotate + iRotate) % self.m_RotateLimit
        return self.m_PointInfo

    
    def GetEffPointByRotate(self, iRotate):
        dPointInfo = { }
        for tOldPos, iPoint in self.m_PointInfo.items():
            tNewPos = self.RotatePos(tOldPos, iRotate)
            dPointInfo[tNewPos] = iPoint
        
        return dPointInfo

    
    def RotatePos(self, tPos, iRotate):
        iRotate = iRotate % self.m_RotateLimit
        for _ in range(iRotate):
            (x, y) = tPos
            tPos = (-y, x)
        
        return tPos

    
    def GetEffGrid(self):
        lstEffPoint = []
        for (iEffX, iEffY), iPoint in self.GetPointInfo().items():
            lstEffPoint.append((iEffX, iEffY, iPoint))
        
        return lstEffPoint

    
    def GetRotate(self):
        return self.m_Rotate

    
    def GetLock(self):
        return self.Query('Lock')

    
    def OnRemoveFromContainer(self):
        oOwner = self.GetOwner()
        if oOwner and self.IsExtPointEffect():
            iPlayerID = oOwner.m_PlayerID
            lstAllKey = [ sKey for sKey in self.m_ExtPointInfo.get(iPlayerID, { }).keys() ]
            for sKey2 in lstAllKey:
                self.ClearExtPoint(sKey2, iRemove = 0)
            


