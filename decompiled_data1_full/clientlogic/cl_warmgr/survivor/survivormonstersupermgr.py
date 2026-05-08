# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/survivormonstersupermgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/survivormonstersupermgr.pyc
# Source Generated with Decompyle++
# File: survivormonstersupermgr.pyc (Python 3.6)

from cl_only import ChooseKey, SendAlert, WeakProxy
from cl_commondefines import WARRIOR_ELITE, WARRIOR_MONSTER, MG_SOURCE_KILLMONSTER, MG_CASH, MG_EXPERIENCE
import cl_only
import cl_perform
import cl_msgcenter
import cl_formula

class CSurvivorMonsterSuperMgr(object):
    
    def __init__(self, oSurvivorElement, oData):
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_PhaseConfig = oData.m_PhaseConfig
        self.m_SuperMonsterRewardMul = oData.m_Config.get('m_SuperMonsterRewardMul', 0)
        self.m_SuperInfo = { }
        self.m_SuperAfPF = { }
        self.m_SuperGroupInfo = { }
        self.m_MonsterAfLib = cl_only.DeepCopy(cl_perform.load.GetSurvivorMonsterAfLibrary())
        self.m_CallFlag = 'SurvivorSuperMonsterMgr'

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_CallFlag, -1, 0)
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_OWNERGETMINIGAMETIME, self.OnDorpReward, self.m_CallFlag)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_OWNERGETMINIGAMETIME, self.m_CallFlag)
        self.m_Survivor = None
        self.m_Game = None

    
    def OnPhaseStart(self, oSurvivor, dMsgInfo):
        self.m_SuperGroupInfo = { }
        iPhase = dMsgInfo['Phase']
        dPhaseInfo = self.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        if iPhase not in dPhaseInfo or not dPhaseInfo[iPhase]['MonsterSuper']:
            return None
        dSuperGroup = dPhaseInfo[iPhase]['MonsterSuper']
        for iGroup in dSuperGroup:
            self.m_SuperGroupInfo[iGroup] = 0
        
        for _, _, iSID in self.m_SuperInfo.values():
            self.RecordSuperGroup(iSID, 1)
        

    
    def GetSuperGroup(self, iSID):
        iPhase = self.m_Survivor.m_Phase
        dPhaseInfo = self.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        if iPhase not in dPhaseInfo or not dPhaseInfo[iPhase]['MonsterSuper']:
            return 0
        dSuperGroup = dPhaseInfo[iPhase]['MonsterSuper']
        for iGroup, dInfo in dSuperGroup.items():
            if iSID in dInfo['TargetMonster']:
                return iGroup
        
        return 0

    
    def RecordSuperGroup(self, iSID, iValue):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        iSuperGroup = self.GetSuperGroup(iSID)
        if not iSuperGroup:
            SendAlert('err', '关卡%s 阶段%d强化怪%d没有对应强化组' % (oLevelNode.m_Level, self.m_Survivor.m_Phase, iSID))
            return None
        self.m_SuperGroupInfo[iSuperGroup] += iValue

    
    def OnCreateMonster(self, oMonster):
        clsData = self.m_Game.m_WarData.GetMonsterData(oMonster.m_SID)
        if not clsData:
            return None
        oMonster.m_AttrPlusPF = clsData.m_SurvivorAttrPlus
        oMonster.m_BanPF = clsData.m_SurvivorBanPF
        self.TrySuperMonster(oMonster)

    
    def TrySuperMonster(self, oMonster):
        iGroup = self.GetSuperGroup(oMonster.m_SID)
        if not iGroup:
            return None
        if not self.ValidSuper(oMonster, iGroup):
            return None
        self.SuperMonster(oMonster, iGroup)

    
    def OnDie(self, oTarget):
        if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        if self.m_Survivor.m_Phase > self.m_Survivor.m_MaxPhase:
            return None
        if oTarget.m_ID in self.m_SuperInfo:
            (iPlusPF, iAfPF, iSID) = self.m_SuperInfo.pop(oTarget.m_ID)
            self.m_SuperAfPF[iAfPF] -= 1
            self.RecordSuperGroup(iSID, -1)

    
    def ValidSuper(self, oMonster, iGroup):
        if oMonster.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            return False
        dPhaseInfo = self.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        if self.m_Survivor.m_Phase not in dPhaseInfo:
            return False
        dGroupInfo = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterSuper'][iGroup]
        iSuperRatio = dGroupInfo['SuperRatio']
        if not iSuperRatio:
            return None
        (sMinSuperCnt, sMaxSuperCnt) = dGroupInfo['SuperLimit']
        iMinSuperCnt = cl_formula.GetFormulaResult(self, sMinSuperCnt)
        iMaxSuperCnt = cl_formula.GetFormulaResult(self, sMaxSuperCnt)
        iCurSuperCnt = self.m_SuperGroupInfo[iGroup]
        if iCurSuperCnt >= iMaxSuperCnt:
            return False
        if iCurSuperCnt < iMinSuperCnt:
            return True
        if self.m_Game.Random(100) < iSuperRatio:
            return True
        return False

    
    def SuperMonster(self, oMonster, iGroup):
        (iAfPF, iPlusPF) = self.RandomMonsterSuperInfo(oMonster)
        if not iAfPF or not iPlusPF:
            return None
        dPhaseInfo = self.m_PhaseConfig[self.m_Survivor.m_ConfigSID]
        dGroupInfo = dPhaseInfo[self.m_Survivor.m_Phase]['MonsterSuper'][iGroup]
        iSuperLevel = dGroupInfo['SuperGrade']
        oMonster.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)
        self.m_SuperInfo[oMonster.m_ID] = (iPlusPF, iAfPF, oMonster.m_SID)
        if iAfPF not in self.m_SuperAfPF:
            self.m_SuperAfPF[iAfPF] = 0
        self.m_SuperAfPF[iAfPF] += 1
        self.RecordSuperGroup(oMonster.m_SID, 1)

    
    def RandomMonsterSuperInfo(self, oMonster):
        iSuperAfPF = 0
        iSuperPlusPF = 0
        iPhase = self.m_Survivor.m_Phase
        dMonsterAfLib = self.m_MonsterAfLib.get(iPhase, { })
        dAfAll = { }
        for iAfPF, tValue in dMonsterAfLib.items():
            (iWeight, iMaxCnt) = tValue
            iAfCnt = self.m_SuperAfPF.get(iAfPF, 0)
            if iMaxCnt and iMaxCnt <= iAfCnt:
                continue
            dAfAll[iAfPF] = iWeight
        
        for iBanPF in oMonster.m_BanPF:
            dAfAll.pop(iBanPF, 0)
        
        iSuperAfPF = ChooseKey(self.m_Game, dAfAll)
        lstAttrPlus = oMonster.m_AttrPlusPF
        if lstAttrPlus:
            iRand = self.m_Game.Random(len(lstAttrPlus))
            iSuperPlusPF = lstAttrPlus[iRand]
        return (iSuperAfPF, iSuperPlusPF)

    
    def OnDorpReward(self, oWarMgr, oTarget, dInfo):
        iMiniGameType = dInfo['MiniGameType']
        iSource = dInfo['Source']
        if not iSource == MG_SOURCE_KILLMONSTER:
            return None
        if iMiniGameType not in (MG_CASH, MG_EXPERIENCE):
            return None
        if oTarget.m_ID not in self.m_SuperInfo:
            return None
        iOriTimes = dInfo['OriTimes']
        iOriTimes += iOriTimes * self.m_SuperMonsterRewardMul // 10000
        dInfo['OriTimes'] = iOriTimes



class CNewSurvivorMonsterSuperMgr(CSurvivorMonsterSuperMgr):
    
    def __init__(self, oSurvivorElement, oData):
        self.m_Survivor = WeakProxy(oSurvivorElement)
        self.m_Game = self.m_Survivor.m_Game
        self.m_PhaseConfig = oData.m_PhaseConfig
        self.m_SuperInfo = { }
        self.m_SuperAfPF = { }
        self.m_SuperGroupInfo = { }
        self.m_MonsterAfLib = cl_only.DeepCopy(cl_perform.load.GetSurvivorMonsterAfLibrary(iNew = 1))
        self.m_CallFlag = 'NewSurvivorSuperMonsterMgr'

    
    def Init(self):
        oGame = self.m_Game
        cl_msgcenter.AddFunction(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(oGame.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_CallFlag, -1, 0)
        oGame.AddGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, self.m_CallFlag)

    
    def Release(self):
        oGame = self.m_Game
        cl_msgcenter.DoneEvent(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_CallFlag)
        cl_msgcenter.DoneEvent(oGame.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_CallFlag)
        oGame.DoneGlobalAttention(oGame.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_DIE, self.m_CallFlag)
        self.m_Survivor = None
        self.m_Game = None

    
    def OnCreateMonster(self, oWarMgr, dInfo):
        iMonsterID = dInfo['Monster']
        oGame = self.m_Game
        oMonster = oGame.GetObject(iMonsterID)
        clsData = oGame.m_WarData.GetMonsterData(oMonster.m_SID)
        if not clsData:
            return None
        oMonster.m_AttrPlusPF = clsData.m_SurvivorAttrPlus
        oMonster.m_BanPF = clsData.m_SurvivorBanPF
        self.TrySuperMonster(oMonster)

    
    def OnMonsterDie(self, oWarMgr, oTarget, dInfo):
        if not oTarget.m_FightType & WARRIOR_MONSTER:
            return None
        if self.m_Survivor.m_Phase > self.m_Survivor.m_MaxPhase:
            return None
        if oTarget.m_ID in self.m_SuperInfo:
            (_, iAfPF, iSID) = self.m_SuperInfo.pop(oTarget.m_ID)
            self.m_SuperAfPF[iAfPF] -= 1
            self.RecordSuperGroup(iSID, -1)



def NewSurvivorMonsterSuperMgr(oSurvivorElement, oData, iNew = 0):
    if iNew:
        oMgr = CNewSurvivorMonsterSuperMgr(oSurvivorElement, oData)
    else:
        oMgr = CSurvivorMonsterSuperMgr(oSurvivorElement, oData)
    oMgr.Init()
    return oMgr

