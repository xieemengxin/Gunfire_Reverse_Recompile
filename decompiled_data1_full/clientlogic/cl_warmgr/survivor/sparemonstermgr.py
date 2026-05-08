# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/sparemonstermgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/sparemonstermgr.pyc
# Source Generated with Decompyle++
# File: sparemonstermgr.pyc (Python 3.6)

from cl_only import Time2Frame, Functor, ChooseKey
from math import ceil
import cl_msgcenter
import cl_formula

class CSpareMonsterMgr(object):
    
    def __init__(self, oSurvivorElement):
        self.m_CallFlag = 'SurvivorSpareMonster'
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_CallOutFlag = { }
        self.m_MonsterWeight = { }
        self.m_MonsterUpLimit = { }
        self.m_MeetMonster = { }
        self.m_SpawnMonster = { }
        self.m_TriggerNumber = { }

    
    def Init(self):
        oGame = self.m_Game
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_CallFlag)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_CallFlag)

    
    def Release(self):
        oGame = self.m_Game
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_CallFlag)
        self.m_Survivor = None
        self.m_CallOutFlag = { }
        self.m_MonsterWeight = { }
        self.m_MonsterUpLimit = { }
        self.m_MeetMonster = { }
        self.m_SpawnMonster = { }
        self.m_TriggerNumber = { }
        self.m_Game = None

    
    def OnCreateMonster(self, oWarMgr, oTarget, dInfo):
        if 'survivormonster' not in dInfo or 'AdditionMonster' in dInfo:
            return None
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        dCycleNumber = dPhaseInfo[self.m_Survivor.m_Phase]['CycleNumber']
        if not dCycleNumber:
            return None
        oMonster = self.m_Game.GetObject(dInfo['Monster'])
        iMonsterSID = oMonster.m_SID
        if iMonsterSID not in self.m_TriggerNumber:
            return None
        if iMonsterSID in self.m_SpawnMonster:
            self.m_SpawnMonster[iMonsterSID] += 1
        else:
            self.m_SpawnMonster[iMonsterSID] = 1
        if iMonsterSID not in self.m_MeetMonster and self.m_SpawnMonster[iMonsterSID] >= self.m_TriggerNumber[iMonsterSID]:
            self.m_MeetMonster[iMonsterSID] = 1

    
    def OnPhaseStart(self, oWarMgr, oTarget, dInfo):
        for sCallFlag in self.m_CallOutFlag:
            self.m_Survivor.Remove_Call_Out_Suspendable(sCallFlag)
        
        self.m_CallOutFlag = { }
        self.m_MonsterWeight = { }
        self.m_MonsterUpLimit = { }
        self.m_MeetMonster = { }
        self.m_TriggerNumber = { }
        iPhase = dInfo['Phase']
        dPhaseInfo = self.m_Survivor.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        if iPhase not in dPhaseInfo:
            return None
        dCycleNumber = dPhaseInfo[iPhase]['CycleNumber']
        if not dCycleNumber:
            return None
        dSpareMonster = dPhaseInfo[iPhase]['SpareMonster']
        dMonsterWeight = { }
        dMonsterUpLimit = { }
        for iMonster, dSpare in dSpareMonster.items():
            dWeight = { }
            dUpLimit = { }
            for iSpareSID, (iWeight, iUpLimit) in dSpare.items():
                dWeight[iSpareSID] = iWeight
                dUpLimit[iSpareSID] = iUpLimit
            
            dMonsterWeight[iMonster] = dWeight
            dMonsterUpLimit[iMonster] = dUpLimit
        
        self.m_MonsterWeight = dMonsterWeight
        self.m_MonsterUpLimit = dMonsterUpLimit
        dTriggerNumber = { }
        for iMonsterSID, (iCycle, sNumber) in dCycleNumber.items():
            iNumber = cl_formula.GetFormulaResult(self, sNumber)
            dTriggerNumber[iMonsterSID] = iNumber
            iCycleFrame = Time2Frame(iCycle)
            cFun = Functor(self.ResetMonsterCycle, iMonsterSID, iCycleFrame, iNumber)
            sFlag = self.m_CallFlag + str(iMonsterSID)
            self.m_Survivor.Call_Out_Suspendable(cFun, iCycleFrame, sFlag)
            self.m_CallOutFlag[sFlag] = 1
        
        self.m_TriggerNumber = dTriggerNumber

    
    def ResetMonsterCycle(self, iMonsterSID, iCycleFrame, iNumber):
        sCallFlag = self.m_CallFlag + str(iMonsterSID)
        self.m_Survivor.Remove_Call_Out_Suspendable(sCallFlag)
        self.m_SpawnMonster[iMonsterSID] = 0
        if iMonsterSID in self.m_MeetMonster:
            self.m_MeetMonster.pop(iMonsterSID)
        cFun = Functor(self.ResetMonsterCycle, iMonsterSID, iCycleFrame, iNumber)
        self.m_Survivor.Call_Out_Suspendable(cFun, iCycleFrame, sCallFlag)

    
    def GetReplaceMonster(self, iMonsterSID, iReplacePower, dMonsterPower):
        dMonsterWeight = self.m_MonsterWeight[iMonsterSID]
        dMonsterLimit = self.m_MonsterUpLimit[iMonsterSID]
        dRealLimit = { }
        for iTempMonster, iTempNumber in dMonsterLimit.items():
            iTempNumber = ceil(iTempNumber * 100 / dMonsterPower[iTempMonster])
            dRealLimit[iTempMonster] = iTempNumber
        
        lstReplaceMonster = []
        for _ in range(1000):
            if not dRealLimit:
                break
            iMonster = ChooseKey(self.m_Game, dMonsterWeight)
            if iMonster not in dRealLimit:
                continue
            if dRealLimit[iMonster] <= 0:
                dRealLimit.pop(iMonster)
                continue
            dRealLimit[iMonster] -= 1
            iReplacePower -= dMonsterPower[iMonster]
            if iReplacePower >= 0:
                lstReplaceMonster.append(iMonster)
                continue
        
        return lstReplaceMonster



def NewSpareMonsterMgr(oSurvivorElement):
    oSpareMonsterMgr = CSpareMonsterMgr(oSurvivorElement)
    oSpareMonsterMgr.Init()
    return oSpareMonsterMgr

