# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/survivormonsterctrl.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/survivormonsterctrl.pyc
# Source Generated with Decompyle++
# File: survivormonsterctrl.pyc (Python 3.6)

from cl_only import WeakProxy, ChooseKey, Time2Frame, ChooseRange, PY_FLAG_DEAD, ShufferList, SendAlert, ChooseMulKeys, Functor, GAME_FRAME_INF
from cl_commondefines import SIDE_TYPE_MONSTER, MONSTER_CLASSIFY_MASK, WARRIOR_ELITE, WARRIOR_MONSTER
from cl_object.logging import SurvivorLog
from cl_warmgr.levelline.linespawnaction import GetSpawnFunc
from math import ceil
import cl_math
import cl_formula
import cl_msgcenter
import functools
import cl_gamedebug as debug
import cl_snetwar
import cl_platformdata
from . import survivorspawnaction

class CSurvivorMonsterCtrl(object):
    
    def __init__(self, oLevelLine, oSurvivor):
        self.m_LevelLine = WeakProxy(oLevelLine)
        self.m_Survivor = WeakProxy(oSurvivor)
        self.m_Game = oLevelLine.m_Game
        self.m_Target = 0
        self.m_AdditionMonsterInfo = { }
        self.m_AdditionMonsterDebug = { }
        self.m_CurAdditionMonster = { }
        self.m_CallFlag = 'SurvivorMonsterCtrl'
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_CallFlag)
        self.m_GroupInfo = { }
        self.m_Monster = { }
        self.m_MonsterNo = { }
        self.m_PreSpawnAngle = 0
        self.m_PreSpawnDir = None

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_CallFlag)
        self.m_LevelLine = None
        self.m_Survivor = None
        self.m_Game = None
        self.m_GroupInfo = { }
        self.m_Monster = { }
        self.m_MonsterNo = { }

    
    def GetMonsterCategory(self):
        lstCategory = []
        oWarData = self.m_Game.m_WarData
        iLevel = self.m_LevelLine.m_LevelNode.m_Level
        if iLevel not in self.m_Survivor.m_LevelMap:
            return []
        iConfigSID = self.m_Survivor.m_LevelMap[iLevel]
        dPhaseConfig = self.m_Survivor.m_PhaseConfig[iConfigSID]
        for dPhaseInfo in dPhaseConfig.values():
            for iMonsterSID in dPhaseInfo['MonsterLimit']:
                clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
                if clsMonsterData.m_DataSID not in lstCategory:
                    lstCategory.append(clsMonsterData.m_DataSID)
            
        
        return lstCategory

    
    def GetRealMonsterCnt(self):
        return 0

    
    def IsMonsterAllDie(self):
        return True

    
    def StartSpawn(self, tSpawnInfo, **kwargs):
        pass

    
    def GetMonsterBelong(self, oMonster):
        return (0, 0)

    
    def GetAllMonsterBornPos(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        lstSpwanInfo = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, self.m_LevelLine.m_Name, 'survivalData', 'SpawnData')
        lstMonsterBronPos = []
        for dInfo in lstSpwanInfo:
            lstRangedAreaGroup = dInfo['RangedAreaGroup'] if 'RangedAreaGroup' in dInfo else []
            fHighLimit = dInfo['HighLimit'] if 'HighLimit' in dInfo else 0
            dCheckDropInfo = dInfo['CheckDropInfo'] if 'CheckDropInfo' in dInfo else { }
            vFixDropPos = dInfo['FixDropPos'] if 'FixDropPos' in dInfo else None
            iGroup = dInfo['Group'] if 'Group' in dInfo else 0
            lstMonsterBronPos.append((dInfo['SpawnPos'], dInfo['StartPos'], lstRangedAreaGroup, fHighLimit, (dCheckDropInfo, vFixDropPos), iGroup))
        
        return lstMonsterBronPos

    
    def InitAdditionMonsterInfo(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        lstSpwanInfo = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, self.m_LevelLine.m_Name, 'survivalData', 'SpareSpawnData')
        if not lstSpwanInfo:
            return None
        dMonsterInfo = { }
        for dInfo in lstSpwanInfo:
            iGroup = dInfo['Group']
            if 'EXMonsterSID' not in dInfo or not dInfo['EXMonsterSID']:
                SendAlert('err', '关卡%s 附属刷怪第%d组怪物SID漏配' % (self.m_LevelLine.m_LevelNode.m_Level, iGroup))
                continue
            iMonsterSID = dInfo['EXMonsterSID']
            iGrade = dInfo['EXGrade'] if 'EXGrade' in dInfo else 0
            lstRangedAreaGroup = dInfo['RangedAreaGroup'] if 'RangedAreaGroup' in dInfo else []
            dCheckDropInfo = dInfo['CheckDropInfo'] if 'CheckDropInfo' in dInfo else { }
            vFixDropPos = dInfo['FixDropPos'] if 'FixDropPos' in dInfo else None
            if iGroup not in dMonsterInfo:
                dMonsterInfo[iGroup] = []
            dMonsterInfo[iGroup].append((iMonsterSID, iGrade, dInfo['SpawnPos'], dInfo['StartPos'], lstRangedAreaGroup, (dCheckDropInfo, vFixDropPos)))
        
        self.m_AdditionMonsterInfo = dMonsterInfo

    
    def GetMeetDistancePos(self, oTarget, tRange):
        vTarget = oTarget.GetPos()
        self.m_Target = oTarget.m_ID
        lstPos = []
        lstHighLimitPos = []
        lstExtremePos = []
        lstExtremeHighLimitPos = []
        for tSpawnPos, tStartPos, lstRangedAreaGroup, fHighLimit, (dCheckDropInfo, vFixDropPos), iGroup in self.m_Survivor.m_MonsterBornPos:
            fDistance = cl_math.CalDistance(vTarget, tSpawnPos)
            tPosInfo = (tSpawnPos, tStartPos, lstRangedAreaGroup, (dCheckDropInfo, vFixDropPos), iGroup, fDistance)
            if fDistance >= tRange[0] and fDistance <= tRange[1]:
                if fHighLimit > 1e-06 and abs(vTarget[1] - tSpawnPos[1]) > fHighLimit:
                    lstHighLimitPos.append(tPosInfo)
                else:
                    lstPos.append(tPosInfo)
            if (fDistance > tRange[1] and fDistance <= tRange[2] or fHighLimit > 1e-06) and abs(vTarget[1] - tSpawnPos[1]) > fHighLimit:
                lstExtremeHighLimitPos.append(tPosInfo)
                continue
            lstExtremePos.append(tPosInfo)
        
        lstPos = ShufferList(self.m_Game, lstPos)
        lstExtremePos.sort(key = functools.cmp_to_key((lambda t1, t2: cl_math.CalDistance(vTarget, t1[0]) - cl_math.CalDistance(vTarget, t2[0]))))
        lstHighLimitPos.sort(key = functools.cmp_to_key((lambda t1, t2: cl_math.CalDistance(vTarget, t1[0]) - cl_math.CalDistance(vTarget, t2[0]))))
        lstExtremeHighLimitPos.sort(key = functools.cmp_to_key((lambda t1, t2: cl_math.CalDistance(vTarget, t1[0]) - cl_math.CalDistance(vTarget, t2[0]))))
        return (lstPos, lstExtremePos, lstHighLimitPos, lstExtremeHighLimitPos)

    
    def GetCalDistancePos(self, oTarget):
        vTarget = oTarget.GetPos()
        self.m_Target = oTarget.m_ID
        lstPos = []
        lstHighLimitPos = []
        for tSpawnPos, tStartPos, lstRangedAreaGroup, fHighLimit, (dCheckDropInfo, vFixDropPos), iGroup in self.m_Survivor.m_MonsterBornPos:
            fDistance = cl_math.CalDistance(vTarget, tSpawnPos)
            tPosInfo = (tSpawnPos, tStartPos, lstRangedAreaGroup, (dCheckDropInfo, vFixDropPos), iGroup, fDistance)
            if fHighLimit > 1e-06 and abs(vTarget[1] - tSpawnPos[1]) > fHighLimit:
                lstHighLimitPos.append(tPosInfo)
                continue
            lstPos.append(tPosInfo)
        
        lstPos = ShufferList(self.m_Game, lstPos)
        lstHighLimitPos = ShufferList(self.m_Game, lstHighLimitPos)
        return (lstPos, lstHighLimitPos)

    
    def CreateExpectedNumberMonsters(self):
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        iExpectedNumber = dPhaseInfo[self.m_Survivor.m_Phase]['ExpectedMonsterNumber']
        iGrade = dPhaseInfo[self.m_Survivor.m_Phase]['Grade']
        dMonsterWeight = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterWeight']
        dRes = self.GetNeedSpawnMonster({ }, self.m_Survivor.m_MonsterPower, dMonsterWeight, iExpectedNumber * 100)
        if not dRes:
            return None
        lstSpawnPos = self.GetMonsterSpawnPos(dRes)
        if not self.CheckSpawnPos(lstSpawnPos, dRes):
            return None
        self.CreateByMonsterArgs(dRes, self.m_Survivor.m_MonsterPower, iGrade, lstSpawnPos)

    
    def CheckMonsterPower(self, iTriggerNumber, dMonsterPower, dMonsterWeight):
        oGame = self.m_Game
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        lstMonster = oScene.GetObjectsByType('Monster')
        iCurPower = 0
        dCurMonster = { }
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster or oMonster.m_Owner:
                continue
            if oMonster.Query('AdditionMonster'):
                continue
            iPower = dMonsterPower[oMonster.m_SID] if oMonster.m_SID in dMonsterPower else 0
            iCurPower += iPower
            if oMonster.m_SID in dCurMonster:
                dCurMonster[oMonster.m_SID] += 1
                continue
            dCurMonster[oMonster.m_SID] = 1
        
        iTriggerPower = iTriggerNumber * 100
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        iExpectedPower = dPhaseInfo[self.m_Survivor.m_Phase]['ExpectedMonsterNumber'] * 100
        iEXtraPower = cl_formula.GetFormulaResult(self, dPhaseInfo[self.m_Survivor.m_Phase]['ExtraMonster']) * 100
        iExtraMonsterLimit = dPhaseInfo[self.m_Survivor.m_Phase]['ExtraMonsterLimit'] * 100
        iExpectedPower = min(iExpectedPower + iEXtraPower, iExpectedPower + iExtraMonsterLimit)
        iGrade = dPhaseInfo[self.m_Survivor.m_Phase]['Grade']
        if iTriggerPower > iCurPower:
            iNeedPower = iExpectedPower - iCurPower
            if iNeedPower < 0:
                SendAlert('err', '关卡%s 配置的触发数量与预期数量冲突,预期%d,当前:%d 阶段 %s' % (self.m_LevelLine.m_LevelNode.m_Level, iExpectedPower, iCurPower, self.m_Survivor.m_Phase))
                return None
            if iNeedPower == 0:
                return None
            dRes = self.GetNeedSpawnMonster(dCurMonster, dMonsterPower, dMonsterWeight, iNeedPower)
            if not dRes:
                SendAlert('err', '关卡%s 无怪可刷, 预期触发数量%d,当前:%d 阶段 %s' % (self.m_LevelLine.m_LevelNode.m_Level, iExpectedPower, iCurPower, self.m_Survivor.m_Phase))
                return None
            lstSpawnPos = self.GetMonsterSpawnPos(dRes)
            if not self.CheckSpawnPos(lstSpawnPos, dRes):
                return None
            self.CreateByMonsterArgs(dRes, dMonsterPower, iGrade, lstSpawnPos)

    
    def CreateByMonsterArgs(self, dRes, dMonsterPower, iGrade, lstSpawnPos):
        iIndex = 0
        iLen = len(lstSpawnPos)
        for iMonsterSID, iCount in dRes.items():
            if iMonsterSID in self.m_Survivor.m_SpareMonsterMgr.m_MeetMonster:
                iReplacePower = iCount * dMonsterPower[iMonsterSID]
                lstMonster = self.m_Survivor.m_SpareMonsterMgr.GetReplaceMonster(iMonsterSID, iReplacePower, dMonsterPower)
                for iMonster in lstMonster:
                    if iIndex >= iLen:
                        return None
                    self.CreateMonster(iMonster, iGrade, lstSpawnPos[iIndex], 'CustomAI')
                    iIndex += 1
                
            for _ in range(iCount):
                if iIndex >= iLen:
                    return None
                self.CreateMonster(iMonsterSID, iGrade, lstSpawnPos[iIndex], 'CustomAI')
                iIndex += 1
            
        

    
    def CreateMonster(self, iMonsterSID, iGrade, tSpawnInfo, sAI = 'CustomAI', dInfo = None):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        dCustomAI = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, self.m_LevelLine.m_Name, 'survivalData', sAI)
        dMonsterAIConfig = dCustomAI[1]
        oWarData = oGame.m_WarData
        clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
        if not clsMonsterData:
            SendAlert('err', '关卡%s 没有怪物%d' % (self.m_LevelLine.m_LevelNode.m_Level, iMonsterSID))
            return None
        if clsMonsterData.m_DataSID not in dMonsterAIConfig:
            SendAlert('err', '关卡%s 没有配置怪物%dAI' % (self.m_LevelLine.m_LevelNode.m_Level, clsMonsterData.m_DataSID))
            return None
        dAI = dMonsterAIConfig[clsMonsterData.m_DataSID]
        lstParamLv = dAI['AIParamLv']
        if isinstance(lstParamLv, list):
            lstParamLv = ShufferList(oGame, lstParamLv)
            dAI['AIParamLv'] = lstParamLv[0]
        (tPos, tShowPos, lstRangedAreaGroup, (dCheckDropInfo, vFixDropPos)) = (tSpawnInfo[0], tSpawnInfo[1], tSpawnInfo[2], tSpawnInfo[3])
        if not cl_math.IsZero(tShowPos) and clsMonsterData.m_FightType & WARRIOR_ELITE != WARRIOR_ELITE:
            dAI['ShowPos'] = tShowPos
        dAI['RangedAreaGroup'] = lstRangedAreaGroup
        tLineIdx = self.m_LevelLine.GetLineIdx()
        dExtInfo = {
            'survivormonster': 1 }
        if dInfo:
            dExtInfo.update(dInfo)
        oMonster = oGame.m_ResMgr.CreateMonster(self.m_LevelLine.m_LevelNode.m_Scene, iMonsterSID, tPos, None, SIDE_TYPE_MONSTER, iGrade, dAI, tLineIdx, dExtInfo)
        if vFixDropPos:
            oMonster.Set('FixDropPos', vFixDropPos)
        if dCheckDropInfo:
            oMonster.Set('CheckDropInfo', dCheckDropInfo)
        self.AfterCreateMonster(oMonster)
        return oMonster

    
    def AfterCreateMonster(self, oMonster):
        self.m_Survivor.m_SuperMonsterMgr.OnCreateMonster(oMonster)

    
    def GetNeedSpawnMonster(self, dCurMonster, dMonsterPower, dMonsterWeight, iNeedPower):
        dNeedMonsterRes = { }
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        dMonsterLimit = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterLimit']
        dMinMonster = { }
        dMaxMonster = { }
        dPriority = { }
        for iMonsterSID, (iMax, iMin) in dMonsterLimit.items():
            iMax = cl_formula.GetFormulaResult(self, iMax)
            iMin = cl_formula.GetFormulaResult(self, iMin)
            iMinNumber = ceil(iMin * 100 / dMonsterPower[iMonsterSID])
            iMaxNumber = ceil(iMax * 100 / dMonsterPower[iMonsterSID])
            if iMonsterSID not in dCurMonster:
                dMinMonster[iMonsterSID] = iMinNumber
                dPriority[iMonsterSID] = 1
                dMaxMonster[iMonsterSID] = iMaxNumber - iMinNumber
                continue
            iNumber = dCurMonster[iMonsterSID]
            if iNumber < iMinNumber:
                dMinMonster[iMonsterSID] = iMinNumber - iNumber
                dPriority[iMonsterSID] = (iMinNumber - iNumber) / iMinNumber
                continue
            if iNumber == iMinNumber:
                dMaxMonster[iMonsterSID] = iMaxNumber - iMinNumber
                continue
            if iNumber < iMaxNumber:
                dMaxMonster[iMonsterSID] = iMaxNumber - iNumber
                continue
            dMaxMonster[iMonsterSID] = 0
        
        lstPriority = sorted(dPriority)
        for iMonsterSID in lstPriority:
            iNum = dMinMonster[iMonsterSID]
            iPowerTotal = iNum * dMonsterPower[iMonsterSID]
            if iNeedPower >= iPowerTotal:
                iRange = iNum
            else:
                iRange = ceil(iNeedPower / dMonsterPower[iMonsterSID])
            iNeedPower -= iRange * dMonsterPower[iMonsterSID]
            dNeedMonsterRes[iMonsterSID] = iRange
            (iMax, iMin) = dMonsterLimit[iMonsterSID]
            iMax = cl_formula.GetFormulaResult(self, iMax)
            iMin = cl_formula.GetFormulaResult(self, iMin)
            iMinNumber = ceil(iMin * 100 / dMonsterPower[iMonsterSID])
            iMaxNumber = ceil(iMax * 100 / dMonsterPower[iMonsterSID])
            dMaxMonster[iMonsterSID] = iMaxNumber - iMinNumber
            if iNeedPower <= 0:
                return dNeedMonsterRes
        
        for _ in range(1000):
            iMonsterSID = ChooseKey(self.m_Game, dMonsterWeight)
            if dMaxMonster[iMonsterSID] <= 0:
                continue
            dMaxMonster[iMonsterSID] -= 1
            if iMonsterSID in dNeedMonsterRes:
                dNeedMonsterRes[iMonsterSID] += 1
            else:
                dNeedMonsterRes[iMonsterSID] = 1
            iNeedPower -= dMonsterPower[iMonsterSID]
            if iNeedPower <= 0:
                break
        
        return dNeedMonsterRes

    
    def GetMonsterSpawnPos(self, dRes):
        oTarget = self.m_Survivor.GetMaxDamageTarget()
        if not oTarget:
            oReport = self.m_Game.m_WarMgr.GetComponent('Warreport')
            lstDamage = oReport.GetTotalDamage()
            lstHero = self.m_Game.m_WarMgr.GetLiveHero()
            SurvivorLog.Alert('err', 'game:%d 没有刷怪玩家 %s %s' % (self.m_Game.m_ID, lstDamage, lstHero))
            return []
        if self.m_Survivor.m_SectorSpawn[self.m_Survivor.m_ConfigSID]:
            lstSectorPos = self.GetSectorMonsterSpawnPos(dRes, oTarget)
            if lstSectorPos:
                return lstSectorPos
        tSpawnPos = self.GetMeetDistancePos(oTarget, self.m_Survivor.m_MonsterRange)
        dRefreshGroupMap = self.m_Survivor.m_RefreshGroupMap[self.m_Survivor.m_ConfigSID]
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        dMonsterPriorSpawnRange = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterPriorSpawnRange']
        lstResPos = []
        for iMonsterSID, iCount in dRes.items():
            lstGroup = dRefreshGroupMap[iMonsterSID] if iMonsterSID in dRefreshGroupMap else []
            if iMonsterSID in dMonsterPriorSpawnRange:
                (iMinDis, iMaxDis, _) = dMonsterPriorSpawnRange[iMonsterSID]
            else:
                (iMinDis, iMaxDis) = (-1, -1)
            lstSparePos = []
            for lstTemp in tSpawnPos:
                for tPos in lstTemp:
                    if tPos in lstResPos:
                        continue
                    if not not lstGroup:
                        if tPos[4] in lstGroup:
                            fDis = tPos[5]
                            if iMinDis != -1 and iMaxDis != -1:
                                if fDis <= iMinDis or fDis >= iMaxDis:
                                    lstSparePos.append(tPos)
                                    continue
                                continue
                            iCount -= 1
                            lstResPos.append(tPos)
                            if not iCount:
                                break
                
                if not iCount:
                    break
            
            if iCount and lstSparePos:
                lstResPos.extend(lstSparePos[:iCount])
        
        if not lstResPos:
            return []
        iPosLen = len(lstResPos)
        iWaitNum = sum(dRes.values())
        if iPosLen < iWaitNum:
            vTarget = oTarget.GetPos()
            SendAlert('err', f'''关卡{self.m_LevelLine.m_LevelNode.m_Level} 刷怪点不够位置,待刷怪物数量{iWaitNum},位置数量{iPosLen}, 玩家位置{vTarget} 阶段{self.m_Survivor.m_Phase}''')
            for _ in range(iWaitNum - iPosLen):
                iIndex = self.m_Game.Random(len(lstResPos))
                lstResPos.append(lstResPos[iIndex])
            
        return lstResPos

    
    def GetSectorMonsterSpawnPos(self, dRes, oTarget):
        vTarget = oTarget.GetPos()
        tRange = self.m_Survivor.m_MonsterRange
        tSpawnPos = self.GetCalDistancePos(oTarget)
        dRefreshGroupMap = self.m_Survivor.m_RefreshGroupMap[self.m_Survivor.m_ConfigSID]
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        dMonsterPriorSpawnRange = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterPriorSpawnRange']
        (iMinDis, iMaxDis, _, iSpawnAngle) = tRange
        if not iSpawnAngle:
            iSpawnAngle = 90
        iShiftAngle = 30 if self.m_Game.Random(2) else -30
        iShiftCount = 360 // abs(iShiftAngle)
        iLimitDis = 1
        for i in range(iShiftCount * 2):
            lstResPos = []
            for iMonsterSID, iCount in dRes.items():
                lstGroup = dRefreshGroupMap[iMonsterSID] if iMonsterSID in dRefreshGroupMap else []
                if iMonsterSID in dMonsterPriorSpawnRange:
                    (iMinDis, iMaxDis, _) = dMonsterPriorSpawnRange[iMonsterSID]
                for lstTemp in tSpawnPos:
                    for tPos in lstTemp:
                        if tPos in lstResPos:
                            continue
                        if not not lstGroup:
                            if tPos[4] in lstGroup:
                                fDis = tPos[5]
                                if iLimitDis:
                                    if fDis <= iMinDis or fDis >= iMaxDis:
                                        continue
                                    continue
                                vSpawnPos = tPos[0]
                                disp = cl_math.Vec3Minus(vSpawnPos, vTarget)
                                if cl_math.CheckVector2Angle(disp, self.m_PreSpawnDir, int(iSpawnAngle / 2)):
                                    continue
                                iCount -= 1
                                lstResPos.append(tPos)
                                if not iCount:
                                    break
                    
                    if not iCount:
                        break
                
                if iCount:
                    break
            
            iPosLen = len(lstResPos)
            iWaitNum = sum(dRes.values())
            if iPosLen >= iWaitNum:
                break
            self.RefreshPreSpawnDir(iShiftAngle)
            if i == iShiftCount - 1:
                iLimitDis = 0
                self.RefreshPreSpawnDir()
        else:
            return []
        if self.m_Game.m_WarMgr.Query('DebugRay'):
            debug.ClearDebugLine(self.m_Game)
            debug.DebugSector(self.m_Game, vTarget, 70, self.m_PreSpawnDir, iSpawnAngle, debug.LINE_TILE)
        return lstResPos

    
    def CheckSpawnPos(self, lstSpawnPos, dRes):
        if not lstSpawnPos:
            oTarget = self.m_Game.GetObject(self.m_Target)
            if not oTarget:
                vTarget = []
            vTarget = oTarget.GetPos()
            SendAlert('err', f'''关卡{self.m_LevelLine.m_LevelNode.m_Level}所有规则下抽不到位置, 玩家位置{vTarget} 阶段{self.m_Survivor.m_Phase} {dRes}''')
            return False
        return True

    
    def GetExtraMonsterUpLimit(self, iMonster):
        dMonsterUpLimit = self.m_Survivor.m_SpareMonsterMgr.m_MonsterUpLimit
        iTotal = 0
        for iTempMonster in self.m_Survivor.m_SpareMonsterMgr.m_MeetMonster:
            dUpLimit = dMonsterUpLimit[iTempMonster]
            if iMonster in dUpLimit:
                iTotal += dUpLimit[iMonster]
        
        return iTotal

    
    def OnPhaseStart(self, oWarMgr, oTarget, dInfo):
        self.AdditionSpawn(dInfo['Phase'])

    
    def AdditionSpawn(self, iPhase):
        dPhaseInfo = self.m_Survivor.GetPhaseInfo()
        if iPhase not in dPhaseInfo:
            return None
        dAdditionSpawnInfo = dPhaseInfo[iPhase]['AdditionSpawnInfo']
        iTriggerAdditionSpawnNum = dAdditionSpawnInfo['TriggerAdditionSpawnNum']
        if not iTriggerAdditionSpawnNum:
            return None
        iGrade = dPhaseInfo[iPhase]['Grade']
        dSpawnInfo = dAdditionSpawnInfo['SpawnInfo']
        dSource = { }
        for iKey, dInfo in dSpawnInfo.items():
            dSource[iKey] = dInfo['TriggerWeight']
        
        lstChoose = ChooseMulKeys(self.m_Game, dSource, iTriggerAdditionSpawnNum)
        iPhaseTime = dPhaseInfo[iPhase]['PhaseTime'][0]
        iPhaseTime = cl_formula.GetFormulaResult(self, iPhaseTime)
        for iChoose in lstChoose:
            dSpawn = dSpawnInfo[iChoose]
            (iBegin, iEnd) = dSpawn['TriggerTime']
            iTime = 0
            if iBegin == 0 and iEnd == 0:
                iTime = self.m_Game.Random(iPhaseTime)
            else:
                iTime = ChooseRange(self.m_Game, iBegin, iEnd)
            iFrame = Time2Frame(iTime)
            dCreate = self.GetAdditionSpawnMonsterInfo(dSpawn['SpawnCnt'], dSpawn['Groups'], dSpawn['ChooseGroupNum'])
            self.DebugInfo(iPhase, iChoose, dCreate, iTime)
            sFlag = f'''{self.m_CallFlag}-{iPhase}-{iChoose}'''
            if iFrame > 0:
                cbFun = Functor(self.ExecuteAdditionSpawnMonster, dCreate, iGrade, sFlag)
                self.m_Survivor.Call_Out_Suspendable(cbFun, Time2Frame(iTime), sFlag)
                continue
            self.ExecuteAdditionSpawnMonster(dCreate, iGrade, sFlag)
        

    
    def GetAdditionSpawnMonsterInfo(self, iSpawnCnt, lstGroup, iChooseGroupNum):
        dSource = { }
        for iGroup in lstGroup:
            dSource[iGroup] = 1
        
        lstChoose = ChooseMulKeys(self.m_Game, dSource, iChooseGroupNum)
        iSpawnCnt = cl_formula.GetFormulaResult(self, iSpawnCnt)
        iVal = iSpawnCnt // len(lstChoose)
        dCreate = { }
        for iGroup in lstChoose:
            dCreate[iGroup] = iVal
        
        iRemain = iSpawnCnt % len(lstChoose)
        for iGroup, iVal in dCreate.items():
            if iRemain <= 0:
                break
            dCreate[iGroup] = iVal + 1
            iRemain -= 1
        
        return dCreate

    
    def ExecuteAdditionSpawnMonster(self, dCreate, iGrade, sFlag):
        if not self.ValidExecuteAdditionSpawn():
            return None
        iTotalMonster = 0
        for iGroup, iCount in dCreate.items():
            if iGroup not in self.m_AdditionMonsterInfo:
                oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
                SendAlert('err', f'''关卡{oLevelCtrl.m_CurNode.m_Level} 没有配置{iGroup}组幸存者附属刷怪''')
                continue
            lstSpwanInfo = self.m_AdditionMonsterInfo[iGroup]
            iLen = len(lstSpwanInfo)
            lstIndex = ShufferList(self.m_Game, list(range(iLen)))
            iIndex = 0
            for _ in range(iCount):
                tSpawnInfo = lstSpwanInfo[lstIndex[iIndex]]
                iMonsterSID = tSpawnInfo[0]
                iFinalGrade = iGrade + tSpawnInfo[1]
                oMonster = self.CreateMonster(iMonsterSID, iFinalGrade, (tSpawnInfo[2], tSpawnInfo[3], tSpawnInfo[4], tSpawnInfo[5], None), 'SpareCustomAI', {
                    'AdditionMonster': 1 })
                if oMonster:
                    oMonster.Set('AdditionMonster', 1)
                    cbfunc = Functor(self.OnAdditionMonsterDie, sFlag)
                    cl_msgcenter.AddAttentionFunc(self.m_Survivor, oMonster.m_ID, cl_msgcenter.MSG_WAR_DIE, cbfunc, self.m_CallFlag)
                    iTotalMonster += 1
                iIndex = (iIndex + 1) % iLen
            
        
        self.m_CurAdditionMonster = {
            sFlag: iTotalMonster }

    
    def ValidExecuteAdditionSpawn(self):
        if len(self.m_CurAdditionMonster) > 0:
            return False
        return True

    
    def OnAdditionMonsterDie(self, sFlag, oSurvivor, oMonster, dIfno):
        cl_msgcenter.DoneAttention(self.m_Survivor, oMonster.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        if sFlag not in self.m_CurAdditionMonster:
            return None
        iRemainCnt = self.m_CurAdditionMonster[sFlag] - 1
        if iRemainCnt <= 0:
            self.m_CurAdditionMonster.pop(sFlag)
        else:
            self.m_CurAdditionMonster[sFlag] = iRemainCnt

    
    def DebugInfo(self, iPhase, iChoose, dCreate, iTime):
        if iPhase not in self.m_AdditionMonsterDebug:
            self.m_AdditionMonsterDebug[iPhase] = { }
        self.m_AdditionMonsterDebug[iPhase][iChoose] = {
            'Create': dCreate,
            'TriggerTime': iTime }

    
    def RefreshPreSpawnDir(self, iShiftAngle = 0):
        sFlag = 'RefreshPreSpawnDir'
        self.m_Survivor.Remove_Call_Out_Suspendable(sFlag)
        if not iShiftAngle:
            iSpawnAngle = self.m_Survivor.m_MonsterRange[3]
            if not iSpawnAngle:
                iSpawnAngle = 180
            iShiftAngle = self.m_Game.Random(iSpawnAngle)
            if self.m_Game.Random(2):
                iShiftAngle = -iShiftAngle
        self.m_PreSpawnAngle = self.m_PreSpawnAngle + iShiftAngle
        self.m_PreSpawnDir = (cl_math.CosAngle(self.m_PreSpawnAngle), 0, cl_math.SinAngle(self.m_PreSpawnAngle))
        self.m_Survivor.Call_Out_Suspendable(self.RefreshPreSpawnDir, Time2Frame(3000), sFlag)

    
    def AddSpawnInfo(self, tSpawnInfo):
        pass

    
    def AddSpawnInfoByChooseArea(self, tSpawnInfo):
        pass

    
    def AddSpawnInfoByChooseAreaAndNumber(self, tSpawnInfo):
        pass



class CNewSurvivorMonsterCtrl(object):
    
    def __init__(self, oLevelLine, oSurvivor):
        self.m_LevelLine = WeakProxy(oLevelLine)
        self.m_Survivor = WeakProxy(oSurvivor)
        self.m_Game = oLevelLine.m_Game
        self.m_Target = 0
        self.m_CallFlag = 'NewSurvivorMonsterCtrl'
        self.m_GroupInfo = { }
        self.m_Monster = { }
        self.m_MonsterNo = { }
        self.m_SpecialMonster = { }
        self.m_SpecialPreNum = { }
        self.m_GroupPreNum = { }
        self.m_CallOutCnt = 0
        self.m_CallOutFlag = { }
        self.m_ExtAmount = 0
        self.m_MosnterCache = []
        self.m_MonsterLimitNum = 0

    
    def Release(self):
        self.m_LevelLine = None
        self.m_Survivor = None
        self.m_Game = None
        self.m_GroupInfo = { }
        self.m_Monster = { }
        self.m_MonsterNo = { }
        self.m_SpecialMonster = { }
        self.m_SpecialPreNum = { }
        self.m_CallOutFlag = { }
        self.m_MosnterCache = []

    
    def GetMonsterCategory(self):
        lstCategory = []
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelCtrl = oLevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        dMonsterSpawn = oLevelConfData.GetLineConfig(oLevelNode.m_Level, self.m_LevelLine.m_Name, 'monsterspawn')
        for dSpawn in dMonsterSpawn.values():
            if 'AssignSID' not in dSpawn:
                continue
            for lstDataSID in dSpawn['AssignSID'].values():
                for iDataSID in lstDataSID:
                    if iDataSID in lstCategory:
                        continue
                    lstCategory.append(iDataSID)
                
            
        
        return lstCategory

    
    def AddSpawnInfo(self, tSpawnInfo):
        (iGroupID, dSpawnArea, dAmount, _, tLimitExtAmount, _, iAreaChoose) = tSpawnInfo
        if not dAmount or not dSpawnArea:
            return None
        if iAreaChoose:
            lstArea = ChooseMulKeys(self.m_Game, dSpawnArea, iAreaChoose)
            dNewSpawnArea = { }
            for iArea in lstArea:
                dNewSpawnArea[iArea] = 100
            
        else:
            dNewSpawnArea = dSpawnArea
        oLevelNode = self.m_LevelLine.m_LevelNode
        oLevelCtrl = oLevelNode.m_CtrlMgr
        oLevelConfData = oLevelCtrl.m_LevelConfData
        lstSpawnArea = list(dNewSpawnArea.keys())
        dAreaMonsterSpawn = { }
        dMonsterSpawn = oLevelConfData.GetLineConfig(oLevelNode.m_Level, self.m_LevelLine.m_Name, 'monsterspawn')
        iLimitExtAmount = int(cl_formula.GetFormulaResult(self, tLimitExtAmount))
        for iArea in lstSpawnArea:
            if iArea in dMonsterSpawn:
                dAreaMonsterSpawn[iArea] = dMonsterSpawn[iArea]
        
        lstMonsterInfo = self.ChooseMonsterInfo(dAreaMonsterSpawn, dNewSpawnArea, dAmount, iLimitExtAmount)
        self.PreprocessCreateMonster(iGroupID, dAreaMonsterSpawn, lstMonsterInfo)

    
    def ChooseMonsterInfo(self, dAreaMonsterSpawn, dSpawnArea, dAmount, iLimitExtAmount):
        oGame = self.m_Game
        tAmount = ChooseKey(oGame, dAmount)
        if tAmount is None:
            SendAlert('err', '地图%d线路%s 怪物刷新数量配置有误（权重均为0），请检查' % (self.m_LevelLine.m_LevelNode.m_Map, self.m_LevelLine.m_Name))
            return []
        iAmount = cl_formula.GetFormulaResult(self, tAmount)
        oLevelNode = self.m_LevelLine.m_LevelNode
        if oGame.m_WarMgr.GetAllPlayerCnt() > 1 and iAmount != 0 and iLimitExtAmount > 0:
            iAmount += iLimitExtAmount
        lstSpawnArea = list(dSpawnArea.keys())
        dSpawnPos = {
            'Pos': { },
            'Weight': { } }
        dSpawnPos['Weight'].update(dSpawnArea)
        for iArea in lstSpawnArea:
            if iArea not in dAreaMonsterSpawn:
                SendAlert('err', '地图%d线路%s 不存在刷怪区域%d' % (oLevelNode.m_Map, self.m_LevelLine.m_Name, iArea))
                continue
            iLen = len(dAreaMonsterSpawn[iArea]['SpawnPos'])
            dSpawnPos['Pos'][iArea] = [ i for i in range(iLen) ]
        
        lstMonsterInfo = []
        oWarData = oGame.GetWarData()
        if iAmount > 0:
            for _ in range(iAmount):
                if not dSpawnPos['Weight']:
                    break
                iArea = ChooseKey(oGame, dSpawnPos['Weight'])
                if iArea not in dAreaMonsterSpawn:
                    continue
                dSpawnInfo = dAreaMonsterSpawn[iArea]
                iClassify = ChooseKey(oGame, dSpawnInfo['Weight'])
                dAssignSID = dSpawnInfo.get('AssignSID', { })
                lstBaseSID = []
                if iClassify in dAssignSID:
                    for iBaseSID in dAssignSID[iClassify]:
                        lstBaseSID.append(iBaseSID)
                    
                if not lstBaseSID:
                    SendAlert('err', '关卡%s 未能获取到怪物BaseSID %s' % (self.m_LevelLine.m_LevelNode.m_Level, self.m_Survivor.m_Phase))
                    continue
                lstBaseSID = ShufferList(oGame, lstBaseSID)
                iBaseSID = lstBaseSID[0]
                iMonsterSID = 0
                if iBaseSID in dSpawnInfo['CustomAI']:
                    dAIConf = dSpawnInfo['CustomAI'][iBaseSID]
                    iMonsterSID = dAIConf['MonsterSID'] if 'MonsterSID' in dAIConf else 0
                if not iMonsterSID:
                    lstMonsterSID = oWarData.GetBaseMonsterMap(iBaseSID)
                    if not lstMonsterSID:
                        SendAlert('err', '幸存者基础怪物配置%d未配置对应的战场怪物' % (iBaseSID,))
                        continue
                    iMonsterSID = lstMonsterSID[0]
                iCnt = 1
                lstPosIdx = ShufferList(self.m_Game, dSpawnPos['Pos'][iArea])
                for iPos in lstPosIdx[:iCnt]:
                    tPos = dSpawnInfo['SpawnPos'][iPos]
                    lstMonsterInfo.append((iArea, iClassify, iBaseSID, iMonsterSID, tPos))
                
                dSpawnPos['Pos'][iArea] = lstPosIdx[iCnt:]
                if not dSpawnPos['Pos'][iArea]:
                    dSpawnPos['Pos'].pop(iArea)
                    dSpawnPos['Weight'].pop(iArea)
            
        return lstMonsterInfo

    
    def PreprocessCreateMonster(self, iGroupID, dAreaMonsterSpawn, lstMonsterInfo):
        dGroup = self.m_GroupInfo.setdefault(iGroupID, {
            'Wait': { },
            'Live': [],
            'Die': [],
            'TotalWait': 0,
            'CurWait': 0 })
        lstWait = []
        dPatrolInfo = { }
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        iGrade = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterGrade']
        for idx, tMonsterInfo in enumerate(lstMonsterInfo):
            (iArea, iClassify, iBaseSID, iMonsterSID, tPos) = tMonsterInfo
            dSpawnInfo = dAreaMonsterSpawn[iArea]
            dAIConf = { }
            if iBaseSID in dSpawnInfo['CustomAI']:
                dAIConf = dSpawnInfo['CustomAI'][iBaseSID]
            else:
                dAIConf = dSpawnInfo['DefaultAI'][iClassify]
            lstPatrolPos = dAIConf.get('NewPatrolPos', [])
            dInfo = {
                'AIConfig': { } }
            dInfo['Grade'] = iGrade
            if 'IsFixedFace' in dSpawnInfo and dSpawnInfo['IsFixedFace']:
                dInfo['Angle'] = dSpawnInfo['Angle']
            if 'HatePrefab' in dSpawnInfo and dSpawnInfo['HatePrefab']:
                dInfo['HatePrefab'] = dSpawnInfo['HatePrefab']
                dInfo['HateValue'] = dSpawnInfo['HateValue']
                dInfo['HateType'] = dSpawnInfo['HateType']
            if 'FixDropPos' in dSpawnInfo and dSpawnInfo['FixDropPos']:
                dInfo['FixDropPos'] = dSpawnInfo['FixDropPos']
            if 'CheckDropInfo' in dSpawnInfo and dSpawnInfo['CheckDropInfo']:
                dInfo['CheckDropInfo'] = dSpawnInfo['CheckDropInfo']
            if 'Index' in dSpawnInfo:
                dInfo['AreaIndex'] = dSpawnInfo['Index']
            dInfo['BaseSID'] = iBaseSID
            dInfo['MonsterSID'] = iMonsterSID
            dInfo['Pos'] = tPos
            dInfo['AIConfig'].update(dAIConf)
            dInfo['AIConfig']['GroupID'] = iGroupID
            lstParamLv = dAIConf['AIParamLv']
            if isinstance(lstParamLv, list):
                lstParamLv = ShufferList(self.m_Game, lstParamLv)
                dInfo['AIConfig']['AIParamLv'] = lstParamLv[0]
            tPatrolKey = (iArea, iBaseSID)
            iPatrolIdx = dPatrolInfo.setdefault(tPatrolKey, 0)
            iPatrolCnt = len(lstPatrolPos)
            if iPatrolCnt:
                index = iPatrolIdx % iPatrolCnt
                dInfo['AIConfig']['PatrolPos'] = lstPatrolPos[index]
                dPatrolInfo[tPatrolKey] += 1
            lstWait.append(dInfo)
        
        idx = dGroup['TotalWait']
        dGroup['TotalWait'] += 1
        dGroup['Wait'][idx] = lstWait

    
    def AddSpawnInfoByChooseArea(self, tSpawnInfo):
        pass

    
    def AddSpawnInfoByChooseAreaAndNumber(self, tSpawnInfo):
        pass

    
    def AddHeroPosSpawnInfo(self, tSpawnInfo):
        (iGroup, _, dAmount, _, tLimitExtAmount, _, _, _, iIndex) = tSpawnInfo
        oGame = self.m_Game
        iAmount = ChooseKey(oGame, dAmount)
        iLimitExtAmount = int(cl_formula.GetFormulaResult(self, tLimitExtAmount))
        if oGame.m_WarMgr.GetAllPlayerCnt() > 1 and iAmount != 0 and iLimitExtAmount > 0:
            iAmount += iLimitExtAmount
        self.m_SpecialPreNum[iIndex] = iAmount
        if iGroup not in self.m_GroupPreNum:
            self.m_GroupPreNum[iGroup] = iAmount
        else:
            self.m_GroupPreNum[iGroup] += iAmount

    
    def GetRealMonsterCnt(self):
        iCnt = 0
        for dInfo in self.m_GroupInfo.values():
            for dMonsterInfo in dInfo['Wait'].values():
                iCnt += len(dMonsterInfo)
            
        
        return iCnt

    
    def ClearSpawnData(self):
        for sFlag in self.m_CallOutFlag:
            self.m_Survivor.Remove_Call_Out_Suspendable(sFlag)
        
        self.m_CallOutFlag = { }
        self.m_GroupInfo = { }
        self.m_Monster = { }
        self.m_MonsterNo = { }
        self.m_SpecialMonster = { }
        self.m_SpecialPreNum = { }
        self.m_GroupPreNum = { }
        self.m_MosnterCache = []
        self.m_MonsterLimitNum = 0
        self.m_Game.DoneGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_DIE, 'NewSurvivorMonsterLimit')

    
    def NewCallOutFlag(self):
        self.m_CallOutCnt += 1
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        sFlag = 'Spawn%s-%d-%d' % (self.m_LevelLine.m_Name, self.m_CallOutCnt, iScene)
        self.m_CallOutFlag[sFlag] = 1
        return sFlag

    
    def StartSpawn(self, tSpawnInfo, **kwargs):
        (iGroupID, _, _, iDelay, _, lstPerform, _) = tSpawnInfo
        if iGroupID not in self.m_GroupInfo:
            return None
        if not self.m_GroupInfo[iGroupID]['Wait']:
            return None
        iDelayFrame = Time2Frame(iDelay)
        if not iDelayFrame:
            self.CreateMonsters(iGroupID, lstPerform, **kwargs)
        else:
            sFlag = self.NewCallOutFlag()
            func = Functor(self.CreateMonsters, iGroupID, lstPerform, **kwargs)
            self.m_Survivor.Call_Out_Suspendable(func, iDelayFrame, sFlag)

    
    def CreateMonsters(self, iGroupID, lstPerform, **kwargs):
        oWarData = self.m_Game.m_WarData
        oLevelNode = self.m_LevelLine.m_LevelNode
        tLineIdx = self.m_LevelLine.GetLineIdx()
        dGroup = self.m_GroupInfo[iGroupID]
        iCurWait = dGroup['CurWait']
        if iCurWait not in dGroup['Wait']:
            return None
        lstWait = dGroup['Wait'][iCurWait]
        dGroup['CurWait'] += 1
        dDelay = { }
        for dInfo in lstWait:
            iMonsterSID = dInfo['MonsterSID']
            clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
            if not clsMonsterData:
                iWarNo = self.m_Game.GetWarMgr().m_SID
                sLineName = self.m_LevelLine.m_Name
                SendAlert('err', '战场%d地图%d线路%s 未配置怪物SID%d' % (iWarNo, oLevelNode.m_Map, sLineName, iMonsterSID))
                continue
            iDelayFrame = clsMonsterData.m_CreateDelayFrame
            lstSameDelayInfo = dDelay.setdefault(iDelayFrame, [])
            lstSameDelayInfo.append(dInfo)
        
        self.DelayCreateMonsters(iGroupID, tLineIdx, dDelay, iCurWait, lstPerform, **kwargs)
        if not lstWait:
            dGroup['Wait'].pop(iCurWait)
        self.TriggerGroupDie(iGroupID, 0, 0)

    
    def DelayCreateMonsters(self, iGroupID, tLineIdx, dDelay, iCurWait, lstPerform, **kwargs):
        oGame = self.m_Game
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        dPlayer = oGame.GetRealPlayers()
        oWarData = oGame.m_WarData
        for iDelayFrame, lstInfo in dDelay.items():
            for dInfo in lstInfo:
                clsMonsterData = oWarData.GetMonsterData(dInfo['MonsterSID'])
                iEffectSID = clsMonsterData.m_CreateEffect
                if iEffectSID:
                    iEffectID = oGame.NewNoSceneObjID()
                    cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, dInfo['Pos'], dPlayer)
                if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                    cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
            
            if iDelayFrame:
                sFlag = self.NewCallOutFlag()
                func = Functor(self.TrueCreateMonsters, iGroupID, tLineIdx, lstInfo, iCurWait, lstPerform, **kwargs)
                self.m_Survivor.Call_Out_Suspendable(func, iDelayFrame, sFlag)
                continue
            self.TrueCreateMonsters(iGroupID, tLineIdx, lstInfo, iCurWait, lstPerform, **kwargs)
        

    
    def TrueCreateMonsters(self, iGroupID, tLineIdx, lstInfo, iCurWait, lstPerform, **kwargs):
        oGame = self.m_Game
        oLevelNode = self.m_LevelLine.m_LevelNode
        iScene = oLevelNode.m_Scene
        iSide = SIDE_TYPE_MONSTER
        dGroup = self.m_GroupInfo[iGroupID]
        if iCurWait in dGroup['Wait']:
            dGroup['Wait'].pop(iCurWait)
        dHateTarget = { }
        for dInfo in lstInfo:
            iMonsterSID = dInfo['MonsterSID']
            tPos = dInfo['Pos']
            iGrade = dInfo['Grade']
            iBaseSID = dInfo['BaseSID']
            dAI = dInfo['AIConfig']
            if 'Angle' not in dInfo:
                tFace = self.GetMonsterFacing(tPos)
            else:
                iAngleY = int(dInfo['Angle'][1])
                tFace = cl_math.RotateByEuler((0, 0, 1), (0, iAngleY, 0))
            dExtInfo = {
                'SuperInfo': kwargs['super'] } if 'super' in kwargs else { }
            if 'AreaIndex' in dInfo:
                dExtInfo['AreaIndex'] = dInfo['AreaIndex']
            oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, tPos, tFace, iSide, iGrade, dAI, tLineIdx, dExtInfo)
            if lstPerform:
                for iPerform in lstPerform:
                    oMonster.AddPerform(iPerform, 1)
                
            if 'HatePrefab' in dInfo and dInfo['HatePrefab']:
                iPrefab = dInfo['HatePrefab']
                iHateTarget = 0
                if iPrefab in dHateTarget:
                    iHateTarget = dHateTarget[iPrefab]
                else:
                    oScene = self.m_Game.m_SceneMgr.GetScene(self.m_LevelLine.m_LevelNode.m_Scene)
                    if oScene:
                        for iTarget in oScene.GetObjectsByType(dInfo['HateType']):
                            oTarget = self.m_Game.GetObject(iTarget)
                            if not oTarget or oTarget.m_Prefab != iPrefab:
                                continue
                            iHateTarget = iTarget
                        
                    dHateTarget[iPrefab] = iHateTarget
                if iHateTarget and oMonster.m_Agent:
                    dHateData = {
                        iHateTarget: {
                            'Dam': { },
                            'Hate': [
                                dInfo['HateValue'],
                                GAME_FRAME_INF],
                            'Immutable': 1 } }
                    oMonster.m_Agent.SetData('HateData', dHateData)
            if 'FixDropPos' in dInfo and dInfo['FixDropPos']:
                oMonster.Set('FixDropPos', dInfo['FixDropPos'])
            if 'CheckDropInfo' in dInfo and dInfo['CheckDropInfo']:
                oMonster.Set('CheckDropInfo', dInfo['CheckDropInfo'])
            iID = oMonster.m_ID
            dGroup['Live'].append(iID)
            self.m_Monster[iID] = (iGroupID, iBaseSID, iMonsterSID)
        

    
    def GetMonsterFacing(self, vOriPos):
        oWarMgr = self.m_Game.m_WarMgr
        lstLive = oWarMgr.GetLiveHero()
        if lstLive:
            iCnt = 1 / len(lstLive)
            vDstPos = (0, 0, 0)
            for iHero in lstLive:
                oHero = self.m_Game.GetObject(iHero)
                tPos = oHero.GetPos()
                vDstPos = cl_math.Vec3Mad(vDstPos, tPos, iCnt)
            
            return cl_math.Vec3Minus(vDstPos, vOriPos)
        return (0, 0, 0)

    
    def GetMonsterBelong(self, oMonster):
        iSpawnGroup = oMonster.Query('SpawnGroup', 0)
        if iSpawnGroup:
            return (iSpawnGroup, oMonster.m_DataSID)
        if oMonster.m_ID in self.m_Monster:
            (iGroup, iBaseSID, _) = self.m_Monster[oMonster.m_ID]
            return (iGroup, iBaseSID)
        return (0, 0)

    
    def OnWarriorDie(self, dMsgInfo):
        iMonster = dMsgInfo['VID']
        iAttack = dMsgInfo['AID']
        if iMonster not in self.m_Monster:
            return None
        (iGroupID, _, _) = self.m_Monster[iMonster]
        dGroup = self.m_GroupInfo[iGroupID]
        if iMonster in dGroup['Live']:
            dGroup['Live'].remove(iMonster)
            dGroup['Die'].append(iMonster)
        oReason = dMsgInfo['RS'] if 'RS' in dMsgInfo else None
        if oReason and oReason.GetStrReason() == 'SurvivorGoalOK':
            return None
        self.TriggerGroupDie(iGroupID, iMonster, iAttack)

    
    def IsGroupAllDie(self, iGroup):
        if iGroup not in self.m_GroupInfo:
            return False
        dGroup = self.m_GroupInfo[iGroup]
        if dGroup['Wait'] or dGroup['Live']:
            return False
        return True

    
    def TriggerGroupDie(self, iGroup, iVictim, iAttack):
        tLineIdx = self.m_LevelLine.GetLineIdx()
        if self.IsGroupAllDie(iGroup):
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.m_Game.m_WarMgr, {
                'GroupID': iGroup,
                'LineIdx': tLineIdx,
                'VID': iVictim,
                'AID': iAttack })

    
    def SpawnMonster(self):
        oLevelCtrl = self.m_LevelLine.m_LevelNode.m_CtrlMgr
        dSpwanInfo = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, self.m_LevelLine.m_Name, 'SurvivorSpawn')
        if not dSpwanInfo:
            return None
        dPhaseCurInfo = dSpwanInfo[self.m_Survivor.m_Phase][self.m_Survivor.m_CurSpawn]
        oLevelTrigger = oLevelCtrl.m_LevelTrigger
        dLineGoalRule = dPhaseCurInfo['linegoal']
        if dLineGoalRule['Cond']:
            self.m_Survivor.m_PhaseReward = dLineGoalRule['Action']
            oLevelTrigger.LineAttention(self.m_Survivor.PhaseReward, self.m_LevelLine, dLineGoalRule['Cond'])
        lstSpawnRule = dPhaseCurInfo['SpawnRule']
        for dSpawn in lstSpawnRule:
            oCondition = dSpawn['Cond']
            tAction = dSpawn['Action']
            cbFunc = Functor(self.DownSpawn, tAction)
            oLevelTrigger.LineAttention(cbFunc, self.m_LevelLine, oCondition)
        

    
    def DownSpawn(self, tAction, oTarget = None):
        for dAction in tAction:
            func = dAction['func']
            if isinstance(func, int):
                iFunc = func
                func = survivorspawnaction.GetSpawnFunc(iFunc)
                if not func:
                    func = GetSpawnFunc(iFunc)
            if not func:
                continue
            param = dAction['param']
            func(self.m_LevelLine, param)
        

    
    def GetGroupRemainCount(self, iGroup):
        iRemain = 0
        if iGroup in self.m_GroupInfo:
            dInfo = self.m_GroupInfo[iGroup]
            iRemain += len(dInfo['Live'])
            for lstMonsterInfo in dInfo['Wait'].values():
                iRemain += len(lstMonsterInfo)
            
        return iRemain

    
    def GetSpecialPreNum(self):
        tLineIdx = self.m_LevelLine.GetLineIdx()
        dPreNum = { }
        dPreNum[tLineIdx] = sum(self.m_SpecialPreNum.values())
        return dPreNum

    
    def AddMonsterCache(self, tArgs):
        self.m_MosnterCache.append(tArgs)

    
    def SpawnHeroPosMonster(self, tParam, tForceParam = None):
        oHero = self.GetSpawnHero()
        if not oHero:
            return None
        oGame = self.m_Game
        vHero = oHero.GetPos()
        vFace = oHero.GetFacing()
        if tForceParam:
            (iGroupID, dDataSID, lstExtraPerform, iSpawnAngle, dSpawnDistance, iDelay, iAmount) = tForceParam
        else:
            (iGroupID, dDataSID, _, iDelay, _, lstExtraPerform, _, iSpawnAngle, iIndex) = tParam
            oLevelCtrl = self.m_LevelLine.m_LevelNode.m_CtrlMgr
            dSpawnInfo = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, self.m_LevelLine.m_Name, 'SurvivorSpawn')
            dPhaseCurInfo = dSpawnInfo[self.m_Survivor.m_Phase][self.m_Survivor.m_CurSpawn]
            dSpawnDistance = dPhaseCurInfo['SpawnDistance'] if dSpawnInfo else { }
            iAmount = self.m_SpecialPreNum[iIndex]
        dDataSIDSpawn = { }
        oWarData = oGame.GetWarData()
        iScene = self.m_LevelLine.m_LevelNode.m_Scene
        dPlayer = oGame.GetRealPlayers()
        for iCurIndex in range(iAmount):
            iSpecialMonsterNum = self.GetLiveSpecialMonsterNum()
            if self.m_MonsterLimitNum and iSpecialMonsterNum >= self.m_MonsterLimitNum:
                iRemainNum = iAmount - iCurIndex
                SurvivorLog.Debug(f'''{oGame.m_ID} addmonstercache {iGroupID} {iRemainNum} {iSpecialMonsterNum} {len(self.m_MosnterCache)}''')
                for _ in range(iRemainNum):
                    tArgs = (iGroupID, dDataSID, lstExtraPerform, iSpawnAngle, dSpawnDistance, 0, 1)
                    self.AddMonsterCache(tArgs)
                
                break
            iDataSID = ChooseKey(oGame, dDataSID)
            if iDataSID in dDataSIDSpawn:
                lstSpawnPos = dDataSIDSpawn[iDataSID]
            else:
                (lstResPos, lstIgnoreHeight, lstSemicircle, lstIgnoreAngle, lstIgnoreMax, lstAllPos) = self.GetSpawnPosInfo(iDataSID, dSpawnDistance, vHero, vFace, iSpawnAngle)
                for lstPos in (lstResPos, lstIgnoreHeight, lstSemicircle, lstIgnoreAngle, lstIgnoreMax, lstAllPos):
                    if not lstPos:
                        continue
                    dDataSIDSpawn[iDataSID] = lstPos
                
                lstSpawnPos = dDataSIDSpawn[iDataSID] if iDataSID in dDataSIDSpawn else []
            if not lstSpawnPos:
                if iDataSID in dSpawnDistance:
                    sInfo = '距离%s' % dSpawnDistance[iDataSID]
                else:
                    sInfo = '没有配置距离参数'
                SendAlert('err', '没有刷怪位置,关卡%s 基础怪物%s 玩家位置%s 面向%s 角度%s %s 阶段%s' % (self.m_LevelLine.m_LevelNode.m_Level, iDataSID, vHero, vFace, iSpawnAngle, sInfo, self.m_Survivor.m_Phase))
                continue
            idx = oGame.Random(len(lstSpawnPos))
            (tPos, dResSpawn) = lstSpawnPos[idx]
            clsData = cl_platformdata.GetMonsterConfig(iDataSID)
            iClassify = clsData.m_FightType & MONSTER_CLASSIFY_MASK
            if iClassify in dResSpawn['CustomAI']:
                dAIConf = dResSpawn['CustomAI'][iClassify]
                iMonsterSID = dAIConf['MonsterSID'] if 'MonsterSID' in dAIConf else 0
            elif iClassify not in dResSpawn['DefaultAI']:
                SendAlert('err', '关卡%s阶段%s位置点%s未配置种类%s的默认AI' % (self.m_LevelLine.m_LevelNode.m_Level, self.m_Survivor.m_Phase, tPos, iDataSID))
                continue
            dAIConf = dResSpawn['DefaultAI'][iClassify]
            iMonsterSID = 0
            lstParamLv = dAIConf['AIParamLv']
            if isinstance(lstParamLv, list):
                lstParamLv = ShufferList(oGame, lstParamLv)
                dAIConf['AIParamLv'] = lstParamLv[0]
            if not iMonsterSID:
                lstMonsterSID = oWarData.GetBaseMonsterMap(iDataSID)
                if not lstMonsterSID:
                    SendAlert('err', '玩家位置基础怪物配置%d未配置对应的战场怪物' % (iDataSID,))
                    continue
                iMonsterSID = lstMonsterSID[0]
            clsMonsterData = oWarData.GetMonsterData(iMonsterSID)
            iEffectSID = clsMonsterData.m_CreateEffect
            if iEffectSID:
                iEffectID = oGame.NewNoSceneObjID()
                cl_snetwar.GS2CAddEffect(oGame, iScene, iEffectID, iEffectSID, tPos, dPlayer)
            if clsMonsterData.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                cl_snetwar.GS2CEliteCreateTip(oGame, iScene)
            iDelayFrame = Time2Frame(iDelay)
            iMonsterID = oGame.NewNPCID()
            dSpecialMonster = self.m_SpecialMonster.setdefault(iGroupID, { })
            dSpecialMonster[iMonsterID] = 0
            if not iDelayFrame:
                self.TrueSpawnHeroPosMonster(iGroupID, iMonsterSID, tPos, dAIConf, lstExtraPerform, dResSpawn, iMonsterID)
                continue
            sFlag = self.NewCallOutFlag()
            func = Functor(self.TrueSpawnHeroPosMonster, iGroupID, iMonsterSID, tPos, dAIConf, lstExtraPerform, dResSpawn, iMonsterID)
            self.m_Survivor.Call_Out_Suspendable(func, iDelayFrame, sFlag)
        

    
    def TrueSpawnHeroPosMonster(self, iGroupID, iMonsterSID, tPos, dAIConf, lstExtraPerform, dResSpawn, iMonsterID):
        oGame = self.m_Game
        oLevelNode = self.m_LevelLine.m_LevelNode
        tLineIdx = self.m_LevelLine.GetLineIdx()
        iScene = oLevelNode.m_Scene
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        iGrade = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterGrade']
        dExtInfo = {
            'ID': iMonsterID }
        oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, tPos, None, SIDE_TYPE_MONSTER, iGrade, dAIConf, tLineIdx, dExtInfo)
        if lstExtraPerform:
            for iPerform in lstExtraPerform:
                oMonster.AddPerform(iPerform, 1)
            
        if 'FixDropPos' in dResSpawn and dResSpawn['FixDropPos']:
            oMonster.Set('FixDropPos', dResSpawn['FixDropPos'])
        if 'CheckDropInfo' in dResSpawn and dResSpawn['CheckDropInfo']:
            oMonster.Set('CheckDropInfo', dResSpawn['CheckDropInfo'])
        oMonster.Set('SpawnGroup', iGroupID)

    
    def GetSpawnHero(self):
        oGame = self.m_Game
        lstHero = oGame.m_WarMgr.GetRoomHero()
        if not lstHero:
            return None
        lstLive = []
        for iHero in lstHero:
            oTarget = oGame.GetObject(iHero, PY_FLAG_DEAD)
            if not oTarget:
                continue
            lstLive.append(iHero)
        
        iSpawnHero = 0
        if lstLive:
            iSpawnHero = ShufferList(oGame, lstLive)[0]
        else:
            iSpawnHero = ShufferList(oGame, lstHero)[0]
        oHero = oGame.GetObject(iSpawnHero)
        return oHero

    
    def CheckGroupAllDie(self, iMonsterID, iGroup):
        if iGroup not in self.m_SpecialMonster:
            return False
        if iMonsterID in self.m_SpecialMonster[iGroup]:
            self.m_SpecialMonster[iGroup][iMonsterID] = 1
        if len(self.m_SpecialMonster[iGroup]) > sum(self.m_SpecialMonster[iGroup].values()):
            return False
        return True

    
    def GetSpawnPosInfo(self, iDataSID, dSpawnDistance, vHero, vFace, iSpawnAngle):
        oLevelCtrl = self.m_LevelLine.m_LevelNode.m_CtrlMgr
        dMonsterSpawn = oLevelCtrl.m_LevelConfData.GetLineConfig(oLevelCtrl.m_CurNode.m_Level, self.m_LevelLine.m_Name, 'monsterspawn')
        (lstResPos, lstIgnoreHeight, lstSemicircle, lstIgnoreAngle, lstIgnoreMax, lstAllPos) = ([], [], [], [], [], [])
        for dSpawn in dMonsterSpawn.values():
            if 'AssignSID' not in dSpawn:
                continue
            for lstSpecies in dSpawn['AssignSID'].values():
                if iDataSID in lstSpecies:
                    break
            
            for vSpawnPos in dSpawn['SpawnPos']:
                tSpawnPos = (vSpawnPos, dSpawn)
                if not iDataSID in dSpawnDistance or lstResPos or lstIgnoreHeight or lstSemicircle or lstIgnoreAngle or lstIgnoreMax:
                    lstAllPos.append(tSpawnPos)
                (fMin, fMax, fMinHeight, fMaxHeight) = dSpawnDistance[iDataSID]
                fDistance = cl_math.CalDistance(vSpawnPos, vHero)
                if fDistance < fMin:
                    continue
                if not lstResPos or lstIgnoreHeight or lstSemicircle or lstIgnoreAngle:
                    lstIgnoreMax.append(tSpawnPos)
                if fDistance > fMax:
                    continue
                disp = cl_math.Vec3Minus(vSpawnPos, vHero)
                if iSpawnAngle and cl_math.CheckVector2Angle(disp, vFace, iSpawnAngle):
                    if not lstResPos or lstIgnoreHeight or lstSemicircle:
                        lstIgnoreAngle.append(tSpawnPos)
                    if not lstResPos:
                        pass
                    if not lstIgnoreHeight and iSpawnAngle < 90 and not cl_math.CheckVector2Angle(disp, vFace, 90):
                        lstSemicircle.append(tSpawnPos)
                        continue
                if not lstResPos:
                    fHeightdifference = vHero[1] - vSpawnPos[1]
                    if fHeightdifference < fMinHeight or fHeightdifference > fMaxHeight:
                        lstIgnoreHeight.append(tSpawnPos)
                        continue
                    continue
                lstResPos.append(tSpawnPos)
            
        
        return (lstResPos, lstIgnoreHeight, lstSemicircle, lstIgnoreAngle, lstIgnoreMax, lstAllPos)

    
    def GetAllRemainCount(self):
        iSpecical = sum(self.m_SpecialPreNum.values())
        for dMonster in self.m_SpecialMonster.values():
            for iDead in dMonster.values():
                if iDead:
                    iSpecical -= 1
            
        
        return iSpecical

    
    def GetSpecialGroupRemainCount(self, iGroup):
        if iGroup not in self.m_GroupPreNum:
            return 0
        if iGroup not in self.m_SpecialMonster:
            return 0
        iRemain = self.m_GroupPreNum[iGroup]
        for iDead in self.m_SpecialMonster[iGroup].values():
            if iDead:
                iRemain -= 1
        
        return iRemain

    
    def GetLiveSpecialMonsterNum(self):
        iNum = 0
        for dMonster in self.m_SpecialMonster.values():
            for iDead in dMonster.values():
                if not iDead:
                    iNum += 1
            
        
        return iNum

    
    def SetMonsterLimitNum(self, iNum):
        self.m_MonsterLimitNum = iNum

    
    def EnableMonsterLimit(self):
        oGame = self.m_Game
        oGame.AddGlobalAttention(self.m_Survivor.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnSpecialMonsterDie, 'NewSurvivorMonsterLimit')

    
    def OnSpecialMonsterDie(self, oSurvivor, oTarget, dInfo):
        if not oTarget.m_FightType & WARRIOR_MONSTER:
            return None
        iTarget = oTarget.m_ID
        for dMonster in self.m_SpecialMonster.values():
            if iTarget in dMonster:
                break
        else:
            return None
        if not self.m_MosnterCache:
            return None
        tForceParam = self.m_MosnterCache.pop(0)
        self.SpawnHeroPosMonster((), tForceParam)


