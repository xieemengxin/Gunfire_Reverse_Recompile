# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/circlesummon.pyc
# RelativePath: clientlogic/cl_summon/circlesummon.pyc
# Source Generated with Decompyle++
# File: circlesummon.pyc (Python 3.6)

from cl_commondefines import FIGHT_KEY_WUDI
from cl_only import Time2Frame, ShufferList, Frame2Time, Functor
from cl_math import Rotate2DPointByPoint2, RotateByEuler
import cl_msgcenter
import cl_war
import cl_snetwar
from . import mobject

class CCirecleSummon(mobject.CBaseSummon):
    
    def __init__(self, oGame, iOwner):
        super(CCirecleSummon, self).__init__(oGame, iOwner)
        self.m_CumAngle = 0
        self.m_LinkObs = []
        self.m_RotateFrame = 0
        self.m_CreateCnt = 0
        self.m_Action = 0
        self.m_UpTime = 0
        self.m_Obstacle = []
        self.m_ChosenObstacle = []

    
    def OnInitAttr(self, clsData, dAddData):
        self.m_LinkObs = dAddData['LinkOb'] if 'LinkOb' in dAddData else []
        self.m_Pos = dAddData['Origin']
        self.AddBitAttr('SpecialKey', 'CircleSummon', FIGHT_KEY_WUDI)

    
    def TriggerSummon(self, dTrigger):
        if 'Angle' in dTrigger:
            iAngle = dTrigger['Angle'] + self.m_CumAngle
            self.m_CumAngle = iAngle % 360
        tFace = RotateByEuler((0, 0, 1), (0, int(self.m_CumAngle), 0))
        iRotateTime = Frame2Time(self.m_RotateFrame)
        self.SetFacing(tFace, iRotateTime)
        lstChoose = self.ChooseObstacle()
        if self.m_RotateFrame:
            oGame = self.m_Game
            iUpFrame = self.m_RotateFrame
            cl_snetwar.GS2CCircleSummonEffect(oGame, self.m_ID, lstChoose, 1, oGame.m_WarMgr.GetRoomPlayer())
            oGame.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, Functor(ResendEffect, lstChoose), 'CircleEffect')
            self.Call_Out(Functor(self.SpawnObstacle, lstChoose), iUpFrame, 'SpawnObstacle')
            self.Call_Out(Functor(self.ClearEffect, lstChoose), self.m_RotateFrame, 'ClearEffect')
        else:
            oGame = self.m_Game
            cl_snetwar.GS2CCircleSummonEffect(oGame, self.m_ID, lstChoose, 1, oGame.m_WarMgr.GetRoomPlayer())
            self.SpawnObstacle(lstChoose)

    
    def SetObstacle(self, lstChosen):
        self.m_ChosenObstacle = lstChosen

    
    def ChooseObstacle(self):
        if self.m_ChosenObstacle:
            lstChoose = self.m_ChosenObstacle
        else:
            lstChoose = ShufferList(self.m_Game, self.m_LinkObs, self.m_CreateCnt)
        return lstChoose

    
    def ClearEffect(self, lstChoose):
        oGame = self.m_Game
        cl_snetwar.GS2CCircleSummonEffect(oGame, self.m_ID, lstChoose, 0, oGame.m_WarMgr.GetRoomPlayer())
        oGame.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'CircleEffect')

    
    def SpawnObstacle(self, lstChoose):
        oGame = self.m_Game
        if (not (self.m_LinkObs) or not (self.m_CreateCnt)) and not (self.m_ChosenObstacle):
            return None
        tLineIdx = self.m_LineIdx
        if not tLineIdx:
            return None
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelConfData = oLevelCtrl.m_LevelConfData
        oLine = oLevelCtrl.GetLineNode(tLineIdx)
        if not oLine:
            return None
        iLevel = oLine.m_LevelNode.m_Level
        iScene = self.m_Scene
        dObstacle = oLevelConfData.GetLineConfig(iLevel, oLine.m_Name, 'dynaob')
        for iPrefab, dInfo in dObstacle.items():
            if iPrefab not in lstChoose:
                continue
            tOrigin = dInfo['Origin']
            tAngle = dInfo['Angle']
            iObstacle = dInfo['SID']
            dObFilter = { }
            dObFilter.update(dInfo)
            lstRat = [
                tOrigin[0],
                tOrigin[2]]
            lstOri = [
                self.m_Pos[0],
                self.m_Pos[2]]
            (ix, iz) = Rotate2DPointByPoint2(lstOri, lstRat, -(self.m_CumAngle))
            dObFilter['Origin'] = (ix, tOrigin[1], iz)
            dObFilter['Angle'] = (tAngle[0], tAngle[1] + self.m_CumAngle, tAngle[2])
            oObstacle = oGame.m_ResMgr.CreateBuild(iScene, iObstacle, dObFilter, tLineIdx)
            if not oObstacle:
                continue
            tTarPos = dInfo['Other']['Action'][str(self.m_Action)]
            tMoveDisp = (tTarPos[0] - tOrigin[0], tTarPos[1] - tOrigin[1], tTarPos[2] - tOrigin[2])
            oObstacle.DoAction(self.m_Action, {
                'Time': self.m_UpTime,
                'Disp': tMoveDisp })
            iObstacle = oObstacle.m_ID
            self.m_Obstacle.append(iObstacle)
            cl_msgcenter.AddAttentionFunc(self, iObstacle, cl_msgcenter.MSG_WAR_DIE, RemoveObstacle, 'SummonObstacle')
        

    
    def SetCircleParam(self, iTime, iCnt, iAction, iUpTime):
        self.m_RotateFrame = Time2Frame(iTime)
        self.m_CreateCnt = iCnt
        self.m_Action = iAction
        self.m_UpTime = iUpTime

    
    def RemoveObstacle(self, iObstacle):
        if iObstacle not in self.m_Obstacle:
            return None
        self.m_Obstacle.remove(iObstacle)
        cl_msgcenter.DoneAttention(self, iObstacle, cl_msgcenter.MSG_WAR_DIE, 'SummonObstacle')

    
    def ObstacleUsePerform(self, iPerform):
        self.Remove_Call_Out('SpawnObstacle')
        oGame = self.m_Game
        for iObstacle in list(self.m_Obstacle):
            oObstacle = oGame.GetObject(iObstacle)
            if not oObstacle:
                continue
            oPerform = oObstacle.GetPerformIfNoThenNew(iPerform)
            if not oPerform:
                continue
            cl_war.UsePerform(oObstacle, oPerform, { })
        



def RemoveObstacle(oListener, oOwner, dInfo):
    oListener.RemoveObstacle(dInfo['VID'])


def ResendEffect(lstChoose, oListener, oSender, dInfo):
    cl_snetwar.GS2CCircleSummonEffect(oListener.m_Game, oListener.m_ID, lstChoose, 1, [
        oSender.m_PlayerID])

