# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/survivortrapmgr.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/survivortrapmgr.pyc
# Source Generated with Decompyle++
# File: survivortrapmgr.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_FIGHT
from cl_only import CopyDict, ChooseKey, SendAlert
import cl_msgcenter

class CSurvivorTrapMgr(object):
    
    def __init__(self, oSurvivorElement):
        self.m_Survivor = oSurvivorElement
        self.m_Game = oSurvivorElement.m_Game
        self.m_CallFlag = 'SurvivorTrapMgr'
        self.m_TrapGroup = { }
        self.m_TrapCongfig = { }
        self.m_CurTrapConfigSID = 0

    
    def Init(self):
        cl_msgcenter.AddFunction(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.OnPhaseStart, self.m_CallFlag, -1, 0)
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEBUILD, self.OnCreateBuild, self.m_CallFlag)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_Survivor, cl_msgcenter.MSG_WARMSG_PHASESTART, self.m_CallFlag)
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WAR_CREATEBUILD, self.m_CallFlag)

    
    def OnCreateBuild(self, oWarMgr, oTarget, dInfo):
        iBuildID = dInfo['BuildID']
        oBuild = self.m_Game.GetObject(iBuildID)
        if not oBuild or not (oBuild.m_LineIdx):
            return None
        (iLevel, _, _) = oBuild.m_LineIdx
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        if not oLevelNode.m_LevelType == LEVEL_TYPE_FIGHT:
            return None
        oLine = oLevelCtrl.GetLineNode(oBuild.m_LineIdx)
        oLevelConfData = oLevelNode.m_CtrlMgr.m_LevelConfData
        dTrapGroup = oLevelConfData.GetLineConfig(oLevelNode.m_Level, oLine.m_Name, 'trapGroup')
        if not dTrapGroup:
            return None
        for iGroup, lstPrefab in dTrapGroup.items():
            if oBuild.m_Prefab not in lstPrefab:
                continue
            if iGroup not in self.m_TrapGroup:
                self.m_TrapGroup[iGroup] = { }
            self.m_TrapGroup[iGroup][iBuildID] = 1
        

    
    def OnPhaseStart(self, oSurvivor, dMsgInfo):
        iPhase = dMsgInfo['Phase']
        if self.m_CurTrapConfigSID and iPhase not in self.m_TrapCongfig[self.m_CurTrapConfigSID]['OpenPhase']:
            self.StopAllTrap()
        for iSID, dInfo in self.m_TrapCongfig.items():
            if iPhase not in dInfo['OpenPhase']:
                continue
            if self.m_CurTrapConfigSID != iSID:
                self.m_CurTrapConfigSID = iSID
                self.OpenTrapGroup(iSID)
                break
        

    
    def OpenTrapGroup(self, iSID):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        iOpenNum = self.m_TrapCongfig[iSID]['OpenNum']
        dWeight = CopyDict(self.m_TrapCongfig[iSID]['weight'])
        for i in range(iOpenNum):
            if not dWeight:
                SendAlert('err', '关卡%s 陷阱配置%d陷阱组数量不足' % (oLevelNode.m_Level, iSID))
                break
            iTrapGroup = ChooseKey(self.m_Game, dWeight)
            dWeight.pop(iTrapGroup)
            if iTrapGroup not in self.m_TrapGroup:
                SendAlert('err', '关卡%s 陷阱配置%d陷阱组%d不存在' % (oLevelNode.m_Level, iSID, iTrapGroup))
                continue
            for iTrap in self.m_TrapGroup[iTrapGroup]:
                oTrap = self.m_Game.GetObject(iTrap)
                if oTrap:
                    oTrap.DonePerform()
            
        

    
    def StopAllTrap(self):
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iScene = oLevelCtrl.m_CurNode.m_Scene
        oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
        lstBuild = oScene.GetObjectsByTypes([
            'Trap'])
        for iBuild in lstBuild:
            oBuild = self.m_Game.GetObject(iBuild)
            oBuild.StopPerform()
        
        self.m_CurTrapConfigSID = 0



def NewSurvivorTrapMgr(oSurvivorElement):
    oMgr = CSurvivorTrapMgr(oSurvivorElement)
    oMgr.Init()
    return oMgr

