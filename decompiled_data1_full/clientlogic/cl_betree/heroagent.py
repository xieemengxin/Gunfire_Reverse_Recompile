# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/heroagent.pyc
# RelativePath: clientlogic/cl_betree/heroagent.pyc
# Source Generated with Decompyle++
# File: heroagent.pyc (Python 3.6)

from cl_only import PY_FLAG_SERVANTTARGET, Functor, Time2Frame, Second2Frame, GAME_FRAME, ChooseKey
from cl_behavior.defines import status, BT_RUNNING, BT_FAILURE, BT_SUCCESS, BT_INVALID
from cl_betree.mobject import CAgent as CBaseAgent
from cl_commondefines import MOVE_TYPE_NORMAL, FORBID_MOVE, MONSTER_PART_UNTAGGED, SKILLRET_SUCCESS, RESCUE_SUBMSG_END, WARRIOR_OBSTACLE, LEVEL_TYPE_BOSS, LEVEL_TYPE_HALL, STATA_QIANSUISHIELD, FIGHT_KEY_RERESCUEINTENSIFY, BIG_LION_STATE, STATE_TIME_FOREVER, STATE_TIME_LIMIT
from cl_item.defines import MAIN_HOLD
from cl_pxlayer import PXMASK_MOVEBLK, PXMASK_SIGHTBLK
from cl_perform.cartoon.defines import RayCastCartoon, ThrowByPowerCartoon
from cl_object.logging import TeammateaiLog
import enum
import cl_war
import cl_msgcenter
import cl_math
import cl_perform
import cl_facectrl
import cl_movectrl.crowdctrl
import cl_action
import cl_modeldefine
import cl_gamedebug as debug
import cl_state
import cl_object
import inspect
if 'g_PerformData' not in globals():
    g_PerformData = { }

def AnalysePerform(iPerform):
    mod = cl_perform.GetPerformMod(iPerform)
    if not mod:
        return None
    members = inspect.getmembers(mod)
    classes = [ member for member in members if inspect.isclass(member[1]) ]
    iRaySID = 0
    for clsname, cls in classes:
        if clsname != RayCastCartoon.__name__ and issubclass(cls, RayCastCartoon):
            iRaySID = cls.m_SID
            break
        if clsname != ThrowByPowerCartoon.__name__ and issubclass(cls, ThrowByPowerCartoon):
            iRaySID = cls.m_SID
            break
    else:
        return None
    g_PerformData[iPerform] = {
        'MainCrtID': iRaySID << 8 }


def GetPerformData(iPerform):
    if iPerform not in g_PerformData:
        AnalysePerform(iPerform)
    if iPerform in g_PerformData:
        return g_PerformData[iPerform]
    return { }

HALT_RESCUE_AGENT_FRAME = Second2Frame(3)
ATTACK_CDFRAME = Time2Frame(150)
ENDLESS_AIENHANCE_LAYER = 4
ENDLESS_AIENHANCE_LEVEL = 2

def MoveToPosEndCB(oOwner, _tPos, iFail):
    if not iFail and oOwner.m_Agent:
        oOwner.m_Agent.BTExec()


def MoveToPosEnd(oAgent, iStatus):
    oAgent.SetData('LastArrIdx', 0)
    if iStatus == BT_SUCCESS:
        oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)


def MoveToLockEnemyEnd(oAgent, iStatus):
    oAgent.Stop()
    oAgent.SetData('LastFollowTar', 0)


def StopMoveToLockEnemyCBFunc(oOwner, vTar, iFail):
    if not oOwner.m_Agent:
        return None
    if not iFail and not oOwner.IsDead():
        oAgent = oOwner.m_Agent
        oAgent.SetData('LastFollowTar', 0)
        oAgent.BTExec()


def SkillCastingEndFunc(oOwner, iPerform, oSkill):
    if not oOwner.m_Agent:
        return None
    iBackSwingFrame = oOwner.GetBackSwingRemainingFrame(iPerform)
    iDelayUpdateFrame = iBackSwingFrame + 1
    oAgent = oOwner.m_Agent
    oAgent.m_GameSpace.CallDelayUpdate(oAgent, iDelayUpdateFrame)


def ShiftEndFunc(oOwner, oSkill):
    if not oOwner.m_Agent:
        return None
    oAgent = oOwner.m_Agent
    oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)


def AlwayPass(*args):
    return 1


def AlwayReject(*args):
    return 0


def AoWuCheck(oAgent, _oPerform, _oTarget):
    oTeammateAIElement = oAgent.m_Game.m_WarMgr.GetComponent('TeammateAI')
    dValidWeapon = oTeammateAIElement.m_WeaponInfo
    oOwner = oAgent.m_OwnerObj
    oMainWeapon = oOwner.m_WieldCon.GetCurWeapon()
    if not oMainWeapon or oMainWeapon.m_SID not in dValidWeapon:
        return 0
    oDeputy = oOwner.m_WieldCon.GetDeputyPosWeapon()
    if not oDeputy or oDeputy.m_SID not in dValidWeapon:
        return 0
    return 1


def QingYanCheck(oAgent, _oPerform, oTarget):
    vOwner = oAgent.m_OwnerObj.GetPos()
    vTarget = oTarget.GetPos()
    if abs(vOwner[1] - vTarget[1]) > 2:
        return 0
    return 1


def QianSuiCheck(oAgent, oPerform, oTarget):
    if QianSuiUsingCheck(oAgent):
        return 0
    if oAgent.m_OwnerObj.CheckCastingAndBackSwingByPF(oPerform.m_SID):
        return 0
    return 1


def LynCheck(oAgent, oPerform, oTarget):
    iSpecialMHP = oTarget.m_SpecialMHP
    iSpecialMHPWeight = oTarget.QueryAttr('SpecialMHPWeight')
    iPFDam = oPerform.m_AIPerformDam
    iVictimTotalMax = oTarget.QueryAttr('HPMax') + oTarget.QueryAttr('ShieldMax') + oTarget.QueryAttr('ArmorMax')
    iAIlevelEnhance = oAgent.m_DamLevelEnhance
    iLine = (iPFDam / iSpecialMHP * iSpecialMHPWeight / 100) * iVictimTotalMax * iAIlevelEnhance / 100
    iCur = oTarget.HP() + oTarget.Shield() + oTarget.Armor()
    if iCur >= iLine:
        return 0
    iProb = oAgent.m_OwnerObj.Query('AIKillProb', 70)
    if iProb <= oAgent.m_Game.Random(100):
        return 0
    return 1


def QianSuiUsingCheck(oAgent):
    if oAgent.m_OwnerObj.CheckCastingAndBackSwingByPF(oAgent.m_CareerPF):
        return 1
    if oAgent.m_OwnerObj.m_State.GetItemBySID(STATA_QIANSUISHIELD):
        return 1
    return 0


def CangJueUsingCheck(oAgent):
    if oAgent.m_OwnerObj.m_State.GetItemBySID(BIG_LION_STATE):
        return 1
    return 0


def DefaultUsingCheck(oAgent):
    if not oAgent.m_OwnerObj.CheckCastingAndBackSwingByPF(oAgent.m_CareerPF):
        return 0
    return 1


def DefaultThrowPFUsingCheck(oAgent):
    if not oAgent.m_OwnerObj.CheckCastingAndBackSwingByPF(oAgent.m_ThrowPF):
        return 0
    return 1


class SpecialKey(enum.Enum):
    tType1 = ('救助强化', FIGHT_KEY_RERESCUEINTENSIFY)


class CAgent(CBaseAgent):
    m_EventKey = { }
    m_ConfigKey = {
        '重算间隔': 'IntervalTime' }
    m_Time2FrameConfig = { }
    m_DataKey = {
        '当前技能使用范围': 'CurPerformUseDis' }
    m_CacheKey = { }
    m_AgentEventKey = { }
    m_Enable = 0
    m_DamLevelEnhance = 100
    m_CareerPFCheckFunc = {
        201: AoWuCheck,
        206: QingYanCheck,
        213: QianSuiCheck,
        217: AlwayReject,
        218: LynCheck }
    m_UsingCareerPFCheckFunc = {
        213: QianSuiUsingCheck,
        220: CangJueUsingCheck }
    m_UsingThrowPFCheckFunc = { }
    
    def Config(self, oOwner, dConfig):
        super(CAgent, self).Config(oOwner, dConfig)
        self.m_CareerPF = 0
        self.m_ThrowPF = 0
        self.m_ShiftPF = 0
        oPerform = oOwner.GetCareerPerform()
        if oPerform:
            self.m_CareerPF = oPerform.m_SID
        oPerform = oOwner.GetThrowPerform()
        if oPerform:
            self.m_ThrowPF = oPerform.m_SID
        oPerform = oOwner.GetShiftPerform()
        if oPerform:
            self.m_ShiftPF = oPerform.m_SID
        self.Enable(oOwner)

    
    def SwitchPerform(self, sType, iPerform):
        if sType == 'Career':
            self.m_CareerPF = iPerform
        elif sType == 'Throw':
            self.m_ThrowPF = iPerform

    
    def Enable(self, oOwner):
        if self.m_Enable:
            return None
        self.m_Enable = 1
        if oOwner.m_MoveCtrl:
            oOwner.m_MoveCtrl.m_ComNav.E_Unstall()
            oOwner.m_MoveCtrl.Release(oOwner)
            oOwner.m_MoveCtrl = None
        oOwner.m_MoveCtrl = cl_movectrl.crowdctrl.CHeroCrowdCtrl(oOwner)
        oOwner.SetAttr('TurnSpeed', 10, iRefresh = 0)
        oOwner.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(oOwner)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_RESCUE, self.OnRescueEnd, 'HeroAgent', iSub = RESCUE_SUBMSG_END, iOnce = 0)
        self.ResumeAgent('Disable')
        oScene = self.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        if oScene:
            self.m_SceneData = oScene.m_SceneData
        self.InitHeroFunc()

    
    def Disable(self, oOwner, dMsgInfo):
        if not self.m_Enable:
            return None
        self.m_Enable = 0
        oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        self.StopMoving(self)
        oOwner.m_MoveCtrl.E_Unstall()
        oOwner.m_MoveCtrl.Release(oOwner)
        oOwner.m_MoveCtrl = None
        oOwner.m_MoveCtrl = cl_movectrl.clientctrl.CClientCtrlMgr(oOwner)
        oOwner.m_FaceCtrl.Release()
        oOwner.m_FaceCtrl = None
        oOwner.RemoveExtPacket('FaceTarget')
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_RESCUE, 'HeroAgent', iSub = RESCUE_SUBMSG_END)
        self.PauseAgent('Disable')
        self.ReleaseHeroFunc()

    
    def PauseAgent(self, sReason):
        TeammateaiLog.Debug('%s %s pauseagt %s' % (self.m_Game.m_ID, self.m_OwnerObj.m_PlayerID, sReason))
        super().PauseAgent(sReason)

    
    def ResumeAgent(self, sReason):
        TeammateaiLog.Debug('%s %s resumeagt %s' % (self.m_Game.m_ID, self.m_OwnerObj.m_PlayerID, sReason))
        super().ResumeAgent(sReason)

    
    def EnterScene(self, oScene):
        super().EnterScene(oScene)
        self.m_SceneData = oScene.m_SceneData
        self.RefreshDamLevelEnhance()
        self.Remove_Call_Out('EnterSceneResumeAI')
        self.Call_Out(Functor(self.ResumeAgent, 'LeaveScene'), GAME_FRAME, 'EnterSceneResumeAI')

    
    def LeaveScene(self):
        super(CAgent, self).LeaveScene()
        self.Remove_Call_Out('EnterSceneResumeAI')
        self.PauseAgent('LeaveScene')
        self.HaltPerform(self)
        self.SetData('LockTarget', 0)
        oOwner = self.m_OwnerObj
        if oOwner.m_MoveMode != MOVE_TYPE_NORMAL:
            oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        self.StopMoving(self)

    
    def InitHeroFunc(self):
        oOwner = self.m_OwnerObj
        self.CareerPFCheckFunc = self.m_CareerPFCheckFunc.get(oOwner.m_SID, AlwayPass)
        self.UsingCareerPFCheckFunc = self.m_UsingCareerPFCheckFunc.get(oOwner.m_SID, DefaultUsingCheck)
        self.UsingThrowPFCheckFunc = self.m_UsingThrowPFCheckFunc.get(oOwner.m_SID, DefaultThrowPFUsingCheck)

    
    def ReleaseHeroFunc(self):
        self.CareerPFCheckFunc = None
        self.UsingCareerPFCheckFunc = None
        self.UsingThrowPFCheckFunc = None

    
    def GetClassTypeName(oAgent):
        return 'CHeroAgent'

    GetClassTypeName = staticmethod(GetClassTypeName)
    
    def GetLeader(self, iCheckScene = 1):
        oTeammateAIElement = self.m_Game.m_WarMgr.GetComponent('TeammateAI')
        oTarget = oTeammateAIElement.GetFollowTarget(self.m_OwnerObj.m_ID) if oTeammateAIElement else None
        return oTarget

    
    def GetLockTarget(self):
        iTarget = self.GetData('LockTarget', 0)
        if iTarget:
            oTarget = self.m_Game.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
            if oTarget and oTarget.m_Scene == self.m_OwnerObj.m_Scene:
                return oTarget

    
    def CheckSpecialKey(iMark, oAgent):
        oOwner = oAgent.m_OwnerObj
        if oOwner.CheckSpecialKey(iMark):
            return True
        return False

    CheckSpecialKey = staticmethod(CheckSpecialKey)
    
    def CheckHasState(iState, oAgent):
        if oAgent.m_OwnerObj.m_State.GetItemBySID(iState):
            return True
        return False

    CheckHasState = staticmethod(CheckHasState)
    
    def RefreshDamLevelEnhance(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_OwnerObj.m_Scene)
        if not oScene:
            return None
        iAIlevelEnhance = 0
        oWarMgr = self.m_Game.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        if oLevelNode.m_LevelType != LEVEL_TYPE_HALL:
            dLayerData = oLevelCtrl.m_LevelCtrlConf[oLevelCtrl.m_LayerNum]
            if oWarMgr.IsEndless():
                iAIlevelEnhance = oLevelCtrl.m_LevelCtrlConf[ENDLESS_AIENHANCE_LAYER]['CtrlInfo'][ENDLESS_AIENHANCE_LEVEL]['AIlevelEnhance']
            elif oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
                dBossLevelInfo = dLayerData['BossInfo']['AIBosslevelEnhance']
                if dBossLevelInfo and oLevelNode.m_Level in dBossLevelInfo:
                    iAIlevelEnhance = dBossLevelInfo[oLevelNode.m_Level]
                elif oLevelCtrl.m_LevelNum in dLayerData['CtrlInfo']:
                    pass
                
            dLevelInfo = { }
            if dLevelInfo:
                iAIlevelEnhance = dLevelInfo['AIlevelEnhance']
        self.m_DamLevelEnhance = iAIlevelEnhance

    
    def ChooseNextGoalPos(oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        iLevel = oScene.m_Level if oScene else 0
        if not iLevel:
            return BT_FAILURE
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
        for iPlayer in oGame.m_WarMgr.GetRoomPlayer():
            if iPlayer == oOwner.m_PlayerID:
                continue
            if oMiniMap and iPlayer in oMiniMap.m_GoalPos:
                dGoalPos = oMiniMap.m_GoalPos[iPlayer]
                for oPos in dGoalPos.values():
                    fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, oPos.m_Pos, 3, PXMASK_MOVEBLK, oOwner.m_ID)
                    vPos = cl_math.Vec3Minus(oPos.m_Pos, (0, fGroundDis, 0))
                    oAgent.SetData('ArrivePos', vPos)
                    return BT_SUCCESS
                
        
        return BT_FAILURE

    ChooseNextGoalPos = staticmethod(ChooseNextGoalPos)
    
    def ChooseTargetAroundPos(self, oTarget):
        if not oTarget.m_Scene:
            return None
        oGame = self.m_Game
        vTarget = cl_math.Vec3Add(oTarget.GetPos(), (0, 0.5, 0))
        fGroundDis = oGame.Scene_GroundDistance(oTarget.m_Scene, vTarget, 5, PXMASK_MOVEBLK, oTarget.m_ID)
        vTarget = cl_math.Vec3Minus(vTarget, (0, fGroundDis, 0))
        vPos = oGame.Scene_RandomPointSectorInMesh(oTarget.m_Scene, vTarget, (1, 0, 0), 1, 5, 0, 180)
        if not vPos:
            for _ in range(5):
                vPos = oGame.Scene_RandomPointSectorInMesh(oTarget.m_Scene, vTarget, (1, 0, 0), 1, 5, 0, 180)
                if vPos:
                    break
            
        return vPos

    
    def ChooseLeaderPos(oAgent):
        oTarget = oAgent.GetLeader()
        if not oTarget or not (oTarget.m_Scene):
            return BT_FAILURE
        vPos = oAgent.ChooseTargetAroundPos(oTarget)
        if not vPos:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vPos)
        return BT_SUCCESS

    ChooseLeaderPos = staticmethod(ChooseLeaderPos)
    
    def ChooseEnemyAroundPos(fMinRadius, fMaxRadius, fLimitDis, oAgent):
        oTarget = oAgent.GetLockTarget()
        if not oTarget:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vEnemy = oTarget.GetPos()
        fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, (vEnemy[0], vEnemy[1] + 1.8, vEnemy[2]), 5, PXMASK_MOVEBLK, oOwner.m_ID)
        vEnemy = (vEnemy[0], vEnemy[1] + 1.8 - fGroundDis, vEnemy[2])
        if cl_math.CheckDistance(vEnemy, vOwner, fMaxRadius + fLimitDis):
            bCheckDis = True
            vDir = cl_math.Vec3Minus(vEnemy, vOwner)
            iMaxAngle = 120
        else:
            bCheckDis = False
            vDir = (1, 0, 0)
            iMaxAngle = 179
        for _ in range(5):
            vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vEnemy, vDir, fMinRadius, fMaxRadius, 1, iMaxAngle)
            if (vPos or bCheckDis) and cl_math.CheckDistance(vPos, vOwner, fLimitDis) and iMaxAngle > 30:
                iMaxAngle -= 30
                continue
        else:
            vPos = vEnemy
        oAgent.SetData('ArrivePos', vPos)
        oAgent.SetData('vEnd', vPos)
        if oGame.GetWarMgr().Query('DebugRay'):
            debug.ClearDebugLine(oAgent.m_Game, debug.LINE_TILE)
            (ox, oy, oz) = oOwner.GetPos()
            (tx, ty, tz) = vPos
            debug.DebugLine(oAgent.m_Game, ox, oy, oz, tx, ty, tz, 65535, debug.LINE_TILE)
        return BT_SUCCESS

    ChooseEnemyAroundPos = staticmethod(ChooseEnemyAroundPos)
    
    def MoveToPos(fStopDis, oAgent):
        oOwner = oAgent.m_OwnerObj
        vTarget = oAgent.GetData('ArrivePos')
        if not vTarget:
            return BT_FAILURE
        vOwner = oOwner.GetPos()
        oAgent.AddCurNodeEndFunc(MoveToPosEnd)
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        if iOldIdx and oOwner.m_MoveMode == MOVE_TYPE_NORMAL and cl_math.CheckDistance3D(vOwner, vTarget, fStopDis):
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oMoveCtrl = oOwner.m_MoveCtrl
        if iOldIdx:
            if not (oMoveCtrl.m_ArriveInfo) or iOldIdx != oMoveCtrl.m_ArriveInfo[0]:
                return BT_FAILURE
        if oAgent.SeekPath(oOwner, vTarget, func = MoveToPosEndCB):
            oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
            return BT_RUNNING
        return BT_FAILURE

    MoveToPos = staticmethod(MoveToPos)
    
    def ClearArrivePos(oAgent):
        oAgent.SetData('ArrivePos', None)
        return BT_SUCCESS

    ClearArrivePos = staticmethod(ClearArrivePos)
    
    def MoveToLockEnemy(fCatchDis, oAgent):
        oEnemy = oAgent.GetLockTarget()
        if not oEnemy:
            return BT_FAILURE
        if fCatchDis <= 0:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        iLastID = oAgent.GetData('LastFollowTar', 0)
        if iLastID == oEnemy.m_ID and iLastID != oOwner.m_MoveCtrl.m_FollowTarget:
            return BT_FAILURE
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        if oEnemy.m_MoveCtrl:
            fEnemyRadius = oEnemy.m_MoveCtrl.m_NavRadius
        else:
            (fEnemyRadius, _) = cl_modeldefine.GetModelDefine(oEnemy.m_Shape, 'NavMesh')
        fCatchDis += fEnemyRadius
        if cl_math.CheckDistance3D(vOwner, vEnemy, fCatchDis) and abs(vOwner[1] - vEnemy[1]) <= 2:
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oAgent.AddCurNodeEndFunc(MoveToLockEnemyEnd)
        if oAgent.FollowMove(oOwner, oEnemy.m_ID, fCatchDis, StopMoveToLockEnemyCBFunc):
            oAgent.SetData('LastFollowTar', oEnemy.m_ID)
            return BT_RUNNING
        return BT_FAILURE

    MoveToLockEnemy = staticmethod(MoveToLockEnemy)
    
    def FlashToPos(oAgent):
        vTarget = oAgent.GetData('ArrivePos')
        if not vTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oOwner.WalkTo(vTarget, 'heroagent')
        return BT_SUCCESS

    FlashToPos = staticmethod(FlashToPos)
    
    def StopMoving(oAgent):
        iRet = oAgent.Stop()
        if iRet:
            oAgent.SetData('ArrivePos', None)
            oAgent.SetData('LastArrIdx', 0)
            oAgent.SetData('LastFollowTar', 0)
            return BT_SUCCESS
        return BT_FAILURE

    StopMoving = staticmethod(StopMoving)
    
    def GetLeaderDis(oAgent):
        oTarget = oAgent.GetLeader()
        if oTarget and oTarget.m_Scene:
            return cl_math.CalDistance(oTarget.GetPos(), oAgent.m_OwnerObj.GetPos())
        return 999

    GetLeaderDis = staticmethod(GetLeaderDis)
    
    def GetLockEnemyDis(oAgent):
        oEnemy = oAgent.GetLockTarget()
        if not oEnemy:
            return 0
        return cl_math.CalDistance(oEnemy.GetPos(), oAgent.m_OwnerObj.GetPos()) - oEnemy.m_ModelRadius

    GetLockEnemyDis = staticmethod(GetLockEnemyDis)
    
    def SeekPath(self, oOwner, tPos, func = None):
        iForbidMove = oOwner.IsForbid(FORBID_MOVE)
        bNormal = oOwner.m_MoveMode == MOVE_TYPE_NORMAL
        if iForbidMove and bNormal:
            return False
        oMoveCtrl = oOwner.m_MoveCtrl
        if oMoveCtrl.HasSameArriveInfo(tPos):
            return True
        if oMoveCtrl.CheckResetArriveInfo():
            return False
        if iForbidMove or not bNormal:
            return False
        if oMoveCtrl.SeekPath(oOwner, tPos, func):
            return True
        return False

    
    def FollowMove(self, oOwner, iTarget, fStopDis, func, iAppointFrame = 0):
        iForbidMove = oOwner.IsForbid(FORBID_MOVE)
        bNormal = oOwner.m_MoveMode == MOVE_TYPE_NORMAL
        if iForbidMove and bNormal:
            return False
        oMoveCtrl = oOwner.m_MoveCtrl
        if oMoveCtrl.HasSameArriveTarget(iTarget):
            return True
        if iForbidMove or not bNormal:
            return False
        if oMoveCtrl.FollowMove(oOwner, iTarget, fStopDis, func, iAppointFrame = iAppointFrame):
            return True
        return False

    
    def Stop(self):
        oOwner = self.m_OwnerObj
        oMoveCtrl = oOwner.m_MoveCtrl
        if not oMoveCtrl:
            return 0
        if oOwner.m_MoveMode not in (MOVE_TYPE_NORMAL,):
            return 0
        oMoveCtrl.OverArrive(oOwner, 0, iCallBack = 0)
        return oMoveCtrl.Stop(oOwner)

    
    def ChooseTarget(oAgent):
        oGame = oAgent.m_Game
        iLastTarget = oAgent.GetData('LockTarget', 0)
        if iLastTarget and oGame.GetObject(iLastTarget, PY_FLAG_SERVANTTARGET):
            return BT_SUCCESS
        oLeader = oAgent.GetLeader()
        if not oLeader:
            return BT_FAILURE
        if not oLeader.m_Scene:
            return BT_FAILURE
        if not (oAgent.m_SceneData) or not (oAgent.m_SceneData.m_FightMonster):
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return BT_FAILURE
        if oLeader.m_Scene != oScene.m_ID:
            return BT_FAILURE
        dMonster = { }
        lstMonster = []
        for iMonster in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_SERVANTTARGET)
            if oMonster:
                lstMonster.append(iMonster)
                dMonster[iMonster] = oMonster
        
        if not dMonster:
            return BT_FAILURE
        iLeader = oLeader.m_ID
        iCurFrame = oGame.GetFrameNum()
        lstSortedDis = oAgent.m_SceneData.GetDisCache(iCurFrame, iLeader)
        if not lstSortedDis:
            dDis = oGame.Scene_GetTargetDisMap(iLeader, lstMonster)
            lstSortedDis = sorted(dDis.items(), key = (lambda x: x[1]))
            oAgent.m_SceneData.SetDisCache(iCurFrame, iLeader, lstSortedDis)
        iTarget = 0
        vOwner = oOwner.GetPos()
        for iMonster, _fDis in lstSortedDis:
            if iMonster not in dMonster:
                continue
            oTarget = dMonster[iMonster]
            vTarget = oTarget.GetPos()
            vOwner = (vOwner[0], vOwner[1] + oOwner.m_ModelHeight * 0.85, vOwner[2])
            vTarget = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * 0.93, vTarget[2])
            bAnyHit = oGame.Scene_RaycastAnyHit(oOwner.m_Scene, vOwner, vTarget, PXMASK_SIGHTBLK)
            if not bAnyHit:
                iTarget = iMonster
                break
        
        if iTarget:
            oAgent.SetData('LockTarget', iTarget)
            return BT_SUCCESS
        return BT_FAILURE

    ChooseTarget = staticmethod(ChooseTarget)
    
    def CancelLockTarget(oAgent):
        oAgent.SetData('LockTarget', 0)
        return BT_SUCCESS

    CancelLockTarget = staticmethod(CancelLockTarget)
    
    def IsEnemyInSight(self, oOwner, oTarget, iAngle):
        dInSight = self.GetCache('InSight', { })
        if oTarget.m_ID in dInSight:
            (iCacheAngle, bRes) = dInSight[oTarget.m_ID]
            if bRes and iAngle >= iCacheAngle:
                return bRes
            if not bRes and iAngle <= iCacheAngle:
                return bRes
        vOwner = oOwner.GetPos()
        vTarget = oTarget.GetPos()
        if cl_math.IsPlaneEqual(vOwner, vTarget):
            return True
        if iAngle < 180:
            vFace = oOwner.GetFacing()
            disp = cl_math.Vec3Minus(vTarget, vOwner)
            if cl_math.CheckVector2Angle(disp, vFace, iAngle):
                return False
        fOwnerCheckHeight = oOwner.m_ModelHeight * 0.85
        (x, z) = cl_math.Vec2DisplaceDir((vOwner[0], vOwner[2]), (vTarget[0] - vOwner[0], vTarget[2] - vOwner[2]), 0.5)
        vOwner = (x, vOwner[1] + fOwnerCheckHeight, z)
        vTarget = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * 0.85, vTarget[2])
        oGame = self.m_Game
        bSight = not oGame.Scene_RaycastAnyHit(oOwner.m_Scene, vOwner, vTarget, PXMASK_SIGHTBLK)
        dInSight[oTarget.m_ID] = (iAngle, bSight)
        self.SetCache('InSight', dInSight)
        return bSight

    
    def CheckCanSeeLock(oAgent):
        oGame = oAgent.m_Game
        oTarget = oGame.GetObject(oAgent.GetData('LockTarget', 0))
        if not oTarget:
            return False
        return oAgent.IsEnemyInSight(oAgent.m_OwnerObj, oTarget, iAngle = 180)

    CheckCanSeeLock = staticmethod(CheckCanSeeLock)
    
    def Attack(oAgent):
        oGame = oAgent.m_Game
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return BT_FAILURE
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            return BT_FAILURE
        iCurFrame = oGame.GetFrameNum()
        iCDFrame = oAgent.GetData('AttCD', 0)
        if iCurFrame < iCDFrame:
            return BT_RUNNING
        iStatus = oAgent.GetData('DelayAttack', BT_INVALID)
        if iStatus in (BT_SUCCESS, BT_FAILURE):
            oAgent.SetData('DelayAttack', BT_INVALID)
            return iStatus
        if iStatus != BT_RUNNING:
            oAgent.StartDelayAttack()
        return BT_RUNNING

    Attack = staticmethod(Attack)
    
    def StartDelayAttack(self, iHoldPos = MAIN_HOLD):
        oOwner = self.m_OwnerObj
        oWeapon = oOwner.m_WieldCon.GetCurWeapon(iHoldPos)
        if not oWeapon:
            return None
        sKey = 'DelayAttack' if iHoldPos == MAIN_HOLD else 'AICareerPF'
        iCDFrame = ATTACK_CDFRAME
        iAttSpeed = oWeapon.QueryAttr('AIAttSpeed')
        iWaitFrame = Time2Frame(10000 // iAttSpeed)
        iTotalCnt = iAttSpeed * iCDFrame // 2500
        iRet = self.AttackOnce(iHoldPos, self)
        if iRet != BT_SUCCESS:
            self.SetData(sKey, BT_FAILURE)
            return None
        if iTotalCnt > 1:
            if iWaitFrame < 1:
                oAttSpeedAttr = oWeapon.GetItemAttr('AttSpeed')
                dFactor = oAttSpeedAttr.m_FactorInfo
                TeammateaiLog.Debug('%s %s: waitframe:%d, weaponsid:%s, attspeed:%s %s' % (self.m_Game.m_ID, oOwner.m_PlayerID, iWaitFrame, oWeapon.m_SID, iAttSpeed, dFactor))
            self.SetData(sKey, BT_RUNNING)
            self.Remove_Call_Out(sKey)
            self.Call_Out(Functor(self.DelayAttack, iHoldPos, 1, iTotalCnt, iWaitFrame, iCDFrame), iWaitFrame, sKey)
        else:
            self.DelayAttackEnd(iHoldPos, iCDFrame)

    
    def DelayAttack(self, iHoldPos, iUsed, iTotalCnt, iWaitFrame, iCDFrame):
        sKey = 'DelayAttack' if iHoldPos == MAIN_HOLD else 'AICareerPF'
        if not self.IsActive():
            self.SetData(sKey, BT_FAILURE)
            return None
        iRet = self.AttackOnce(iHoldPos, self)
        if iRet != BT_SUCCESS:
            self.SetData(sKey, BT_FAILURE)
            return None
        iUsed += 1
        if iUsed >= iTotalCnt:
            self.DelayAttackEnd(iHoldPos, iCDFrame)
        else:
            self.Remove_Call_Out(sKey)
            self.Call_Out(Functor(self.DelayAttack, iHoldPos, iUsed, iTotalCnt, iWaitFrame, iCDFrame), iWaitFrame, sKey)

    
    def DelayAttackEnd(self, iHoldPos, iCDFrame):
        if iHoldPos == MAIN_HOLD:
            self.SetData('DelayAttack', BT_SUCCESS)
            iCurFrame = self.m_Game.GetFrameNum()
            self.SetData('AttCD', iCurFrame + iCDFrame)
            if iCDFrame < self.m_GameSpace.m_HeartBeatInterval:
                self.m_GameSpace.CallDelayUpdate(self, iCDFrame)
            else:
                self.Call_Out(Functor(self.StartDelayAttack, iHoldPos), iCDFrame, 'AICareerPF')

    
    def AttackOnce(iHoldPos, oAgent):
        oGame = oAgent.m_Game
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return BT_FAILURE
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oCurWeapon = oOwner.m_WieldCon.GetCurWeapon(iHoldPos)
        if not oCurWeapon:
            return BT_FAILURE
        oComPerform = oCurWeapon.GetComponent('Perform')
        iPerform = oComPerform.GetAttPerform()
        dPerformData = GetPerformData(iPerform)
        if not dPerformData:
            return BT_FAILURE
        iWeapon = oCurWeapon.m_ID
        iActNum = oOwner.GetActionNum()
        iCurFrame = oGame.GetFrameNum()
        vEnd = cl_math.Vec3Add(oTarget.GetPos(), (0, 0.9, 0))
        vStart = cl_math.Vec3Add(oOwner.GetPos(), (0, 1, 0))
        if iHoldPos == MAIN_HOLD:
            bHit = True if oGame.Random(100) < oCurWeapon.m_AIAccuracyRate else False
        else:
            bHit = False
        dNetCartoonData = { }
        oCacheData = cl_perform.skillcache.CSkillCacheData()
        dData = {
            'ActNum': iActNum,
            'Weapon': iWeapon,
            'AttrObj': iWeapon,
            'VID': iTarget,
            'Net': dNetCartoonData,
            'CtrlCache': oCacheData,
            'BulletChange': { },
            'CacheAttack': 1 }
        dMainCartoon = {
            'End': vEnd,
            'Start': vStart,
            'Frame': iCurFrame,
            'Over': 1 }
        iMainCrtID = dPerformData['MainCrtID']
        dNetCartoonData[iMainCrtID] = dMainCartoon
        if bHit:
            dMainCartoon['Ray'] = [
                (vEnd, (0, 0, 0), iTarget, MONSTER_PART_UNTAGGED)]
        pfobj = oOwner.GetPerform(iPerform, iWeapon)
        pfobj.DelCDTime(oOwner)
        iRlt = cl_war.UsePerform(oOwner, pfobj, dData)
        if iRlt != SKILLRET_SUCCESS:
            return BT_FAILURE
        oSkill = oGame.m_SkillMgr.GetSkill(oOwner.m_ID, iActNum)
        if oSkill:
            oSkill.Halt(sReason = None)
        return BT_SUCCESS

    AttackOnce = staticmethod(AttackOnce)
    
    def SetCurWeaponAccuracyRate(iAccuracyRate, iHoldPos, oAgent):
        oOwner = oAgent.m_OwnerObj
        oCurWeapon = oOwner.m_WieldCon.GetCurWeapon(iHoldPos)
        if not oCurWeapon:
            return BT_FAILURE
        oAgent.SetData('SaveAccuracyRate', oCurWeapon.m_AIAccuracyRate)
        oCurWeapon.m_AIAccuracyRate = iAccuracyRate
        return BT_SUCCESS

    SetCurWeaponAccuracyRate = staticmethod(SetCurWeaponAccuracyRate)
    
    def RestoreCurWeaponAccuracyRate(iHoldPos, oAgent):
        oOwner = oAgent.m_OwnerObj
        oCurWeapon = oOwner.m_WieldCon.GetCurWeapon(iHoldPos)
        if not oCurWeapon:
            return BT_FAILURE
        oCurWeapon.m_AIAccuracyRate = oAgent.GetData('SaveAccuracyRate', 0)
        return BT_SUCCESS

    RestoreCurWeaponAccuracyRate = staticmethod(RestoreCurWeaponAccuracyRate)
    
    def HaltPerform(oAgent):
        cl_action.HaltAllCasting(oAgent.m_OwnerObj, 'AI')
        oAgent.SetData('AttCD', 0)
        oAgent.SetData('DelayAttack', BT_INVALID)
        oAgent.Remove_Call_Out('DelayAttack')
        oAgent.HaltCareerPF(oAgent)
        oAgent.HaltThrowPF(oAgent)
        return BT_SUCCESS

    HaltPerform = staticmethod(HaltPerform)
    
    def CanUseCareerPF(oAgent):
        iStatus = oAgent.GetData('DelayAttack', BT_INVALID)
        if iStatus != BT_INVALID:
            return False
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return False
        oGame = oAgent.m_Game
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            return False
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(oAgent.m_CareerPF)
        if not oPerform:
            return False
        if not oPerform.CanUse(oOwner, { }):
            return False
        if not oAgent.CareerPFCheckFunc(oAgent, oPerform, oTarget):
            return False
        return True

    CanUseCareerPF = staticmethod(CanUseCareerPF)
    
    def UseCareerPF(oAgent):
        oGame = oAgent.m_Game
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return BT_FAILURE
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(oAgent.m_CareerPF)
        if not oPerform:
            return BT_FAILURE
        iPerform = oPerform.m_SID
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastPerform', 0) == iPerform:
            oAgent.SetData('LastPerform', 0)
            return BT_SUCCESS
        if not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        vEnd = oTarget.GetPos()
        vEnd = (vEnd[0], vEnd[1] + oTarget.m_ModelHeight * 0.85, vEnd[2])
        dData = {
            'pfid': iPerform,
            'VID': oTarget.m_ID,
            'vEnd': vEnd,
            'CastingEndFunc': Functor(SkillCastingEndFunc, oOwner, iPerform) }
        iRet = cl_war.UsePerform(oOwner, oPerform, dData)
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastPerform', iPerform)
                return BT_RUNNING
            return BT_SUCCESS
        return BT_FAILURE

    UseCareerPF = staticmethod(UseCareerPF)
    
    def IsUsingCareerPF(oAgent):
        return oAgent.UsingCareerPFCheckFunc(oAgent)

    IsUsingCareerPF = staticmethod(IsUsingCareerPF)
    
    def CancelShield(oAgent):
        if not QianSuiUsingCheck(oAgent):
            return BT_SUCCESS
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(oAgent.m_CareerPF)
        if not oPerform:
            return BT_SUCCESS
        dData = {
            'Custom': {
                'CancelShield': 1 } }
        iRet = cl_war.UsePerform(oOwner, oPerform, dData)
        if not iRet:
            return BT_FAILURE
        oAgent.SetData('LastPerform', 0)
        return BT_SUCCESS

    CancelShield = staticmethod(CancelShield)
    
    def HaltCareerPF(oAgent):
        oAgent.SetData('LastPerform', 0)
        oAgent.m_OwnerObj.HaltDualWieldState()
        oAgent.Remove_Call_Out('AICareerPF')
        return BT_SUCCESS

    HaltCareerPF = staticmethod(HaltCareerPF)
    
    def CanUseThrowPF(oAgent):
        iStatus = oAgent.GetData('DelayAttack', BT_INVALID)
        if iStatus != BT_INVALID:
            return False
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return False
        oGame = oAgent.m_Game
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            return False
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(oAgent.m_ThrowPF)
        if not oPerform:
            return False
        if not oPerform.CanUse(oOwner, { }):
            return False
        return True

    CanUseThrowPF = staticmethod(CanUseThrowPF)
    
    def UseThrowPF(oAgent):
        oGame = oAgent.m_Game
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return BT_FAILURE
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(oAgent.m_ThrowPF)
        if not oPerform:
            return BT_FAILURE
        iPerform = oPerform.m_SID
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastThrowPerform', 0) == iPerform:
            oAgent.SetData('LastThrowPerform', 0)
            return BT_SUCCESS
        if not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        vEnd = oTarget.GetCenter()
        dData = {
            'pfid': iPerform,
            'VID': oTarget.m_ID,
            'vEnd': vEnd,
            'CastingEndFunc': Functor(SkillCastingEndFunc, oOwner, iPerform) }
        iRet = cl_war.UsePerform(oOwner, oPerform, dData)
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastThrowPerform', iPerform)
                return BT_RUNNING
            return BT_SUCCESS
        return BT_FAILURE

    UseThrowPF = staticmethod(UseThrowPF)
    
    def IsUsingThrowPF(oAgent):
        return oAgent.UsingThrowPFCheckFunc(oAgent)

    IsUsingThrowPF = staticmethod(IsUsingThrowPF)
    
    def HaltThrowPF(oAgent):
        oAgent.SetData('LastThrowPerform', 0)
        oAgent.Remove_Call_Out('AIThrowPF')
        return BT_SUCCESS

    HaltThrowPF = staticmethod(HaltThrowPF)
    
    def CanUseShiftPF(oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(oAgent.m_ShiftPF)
        if not oPerform:
            return False
        if not oPerform.CanUse(oOwner, { }):
            return False
        return True

    CanUseShiftPF = staticmethod(CanUseShiftPF)
    
    def UseShiftPF(oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(oAgent.m_ShiftPF)
        if not oPerform:
            return BT_FAILURE
        iPerform = oPerform.m_SID
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastThrowPerform', 0) == iPerform:
            oAgent.SetData('LastThrowPerform', 0)
            return BT_SUCCESS
        if not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        dData = {
            'pfid': iPerform,
            'CastingEndFunc': Functor(ShiftEndFunc, oOwner) }
        iRet = cl_war.UsePerform(oOwner, oPerform, dData)
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastThrowPerform', iPerform)
                return BT_RUNNING
            return BT_SUCCESS
        return BT_FAILURE

    UseShiftPF = staticmethod(UseShiftPF)
    
    def FacePath(oAgent):
        oOwner = oAgent.m_OwnerObj
        oOwner.m_FaceCtrl.FacePath(oOwner, 'AI')
        return BT_SUCCESS

    FacePath = staticmethod(FacePath)
    
    def FaceTarget(iKeep, oAgent):
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        lstArgs = [
            iTarget,
            'AI',
            0,
            iKeep]
        oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)
        return BT_SUCCESS

    FaceTarget = staticmethod(FaceTarget)
    
    def ResumeFaceStatus(self):
        pass

    
    def NeedToRescue(oAgent):
        if oAgent.GetCache('RescueCache', 0):
            return BT_SUCCESS
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oScene = oGame.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return BT_FAILURE
        oRescueElement = oGame.m_WarMgr.GetComponent('RescueElement')
        if not oRescueElement:
            return BT_FAILURE
        iCurRescuingTarget = oAgent.GetData('RescueTarget', 0)
        if iCurRescuingTarget and oRescueElement.IsRescuing(oOwner, iCurRescuingTarget):
            oRescueTarget = oGame.GetObject(iCurRescuingTarget)
            if oRescueTarget and not (oRescueTarget.m_Agent):
                return BT_SUCCESS
        iCurRescuingTarget = 0
        dDying = { }
        dDyingAgent = { }
        dCanRescueAgent = { }
        dRescuingTarget = { }
        lstSceneHero = oScene.GetObjectsByType('Hero')
        for iHero in lstSceneHero:
            if iHero == oOwner.m_ID:
                continue
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.IsDying():
                if oHero.m_Agent:
                    dDyingAgent[iHero] = oHero
                else:
                    dDying[iHero] = oHero
            if oHero.m_Agent and not oHero.IsDead():
                iTarget = oRescueElement.GetRescuingTarget(oHero)
                if iTarget:
                    dRescuingTarget[iTarget] = 1
                    continue
                dCanRescueAgent[iHero] = oHero
        
        if not dDying and not dDyingAgent:
            return BT_FAILURE
        for iHero in dRescuingTarget:
            if iHero in dDying:
                dDying.pop(iHero)
                continue
            if iHero in dDyingAgent:
                dDyingAgent.pop(iHero)
        
        iTarget = 0
        if dDying:
            dDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, list(dDying), 1)
            lstSortedDis = sorted(dDis.items(), key = (lambda x: x[1]))
            lstCanRescueAgent = list(dCanRescueAgent)
            for iHero, fDis in lstSortedDis:
                oHero = dDying[iHero]
                iCanRescueFrame = oAgent.CalCanRescueFrame(oHero, fDis)
                if lstCanRescueAgent:
                    bNeedRescue = True
                    dAgentDis = oGame.Scene_GetTargetDisMap(iHero, lstCanRescueAgent)
                    for iAIHero, fAgentDis in dAgentDis.items():
                        oAIHero = dCanRescueAgent[iAIHero]
                        if oAIHero.m_Agent.CalCanRescueFrame(oHero, fAgentDis) > iCanRescueFrame:
                            bNeedRescue = False
                            break
                    
                    if not bNeedRescue:
                        continue
                    continue
                if iCurRescuingTarget or iCanRescueFrame < HALT_RESCUE_AGENT_FRAME:
                    iTarget = iHero
                    break
            
        if not iTarget:
            if iCurRescuingTarget:
                return BT_SUCCESS
            if not dDyingAgent:
                return BT_FAILURE
            fMinDis = 9999
            dDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, list(dDyingAgent))
            for iHero, fDis in dDis.items():
                if fDis < fMinDis:
                    fMinDis = fDis
                    iTarget = iHero
            
        oAgent.SetCache('RescueCache', iTarget)
        oAgent.SetData('RescueTarget', iTarget)
        return BT_SUCCESS

    NeedToRescue = staticmethod(NeedToRescue)
    
    def CalCanRescueFrame(self, oTarget, fDis):
        oOwner = self.m_OwnerObj
        oGame = self.m_Game
        oRescueElement = oGame.m_WarMgr.GetComponent('RescueElement')
        if not oRescueElement:
            return 0
        fSpeed = oOwner.MoveSpeed()
        iDyingSecond = oTarget.GetDyingSecond()
        fCanRescueSecond = iDyingSecond - fDis / (0.6 * fSpeed)
        iRemainRescueFrame = oRescueElement.GetRemainRescueFrame(oOwner)
        return Second2Frame(fCanRescueSecond) - iRemainRescueFrame

    
    def ChooseRescueNearbyPos(oAgent):
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        iLastTarget = oAgent.GetData('RescueTarget', 0)
        if not iLastTarget:
            return BT_FAILURE
        oLastTarget = oGame.GetObject(iLastTarget)
        if not oLastTarget or oLastTarget.m_Scene != oOwner.m_Scene or not oLastTarget.IsDying():
            oAgent.SetData('RescueTarget', 0)
            return BT_FAILURE
        vTarget = oLastTarget.GetPos()
        vPos = oAgent.GetData('ArrivePos')
        if vPos and cl_math.CheckDistance(vPos, vTarget, 5):
            return BT_SUCCESS
        vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vTarget, (1, 0, 0), 1, 5, 0, 180)
        if not vPos:
            for _ in range(5):
                vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vTarget, (1, 0, 0), 1, 5, 0, 180)
                if vPos:
                    break
            else:
                vPos = vTarget
        oAgent.SetData('ArrivePos', vPos)
        return BT_SUCCESS

    ChooseRescueNearbyPos = staticmethod(ChooseRescueNearbyPos)
    
    def ChooseRescueTargetPos(fDis, oAgent):
        iRescueTarget = oAgent.GetData('RescueTarget', 0)
        if not iRescueTarget:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oRescueTarget = oGame.GetObject(iRescueTarget)
        if not oRescueTarget or oRescueTarget.m_Scene != oOwner.m_Scene or not oRescueTarget.IsDying():
            oAgent.SetData('RescueTarget', 0)
            return BT_FAILURE
        vLastTarget = oAgent.GetData('ArrivePos')
        (tx, ty, tz) = oRescueTarget.GetPos()
        vTarget = (tx, ty - oRescueTarget.m_ModelRadius, tz)
        if vLastTarget and cl_math.CheckDistance3D(vLastTarget, vTarget, fDis):
            return BT_SUCCESS
        oAgent.SetData('ArrivePos', vTarget)
        return BT_SUCCESS

    ChooseRescueTargetPos = staticmethod(ChooseRescueTargetPos)
    
    def RescueTeammate(oAgent):
        if oAgent.GetData('RescueEnd', 0):
            oAgent.SetData('RescueEnd', 0)
            return BT_SUCCESS
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        iTarget = oAgent.GetData('RescueTarget', 0)
        oTarget = oGame.GetObject(iTarget)
        if not oTarget or oTarget.m_Scene != oOwner.m_Scene or not oTarget.IsDying():
            oAgent.SetData('RescueTarget', 0)
            return BT_FAILURE
        oRescueElement = oGame.m_WarMgr.GetComponent('RescueElement')
        if not oRescueElement:
            return BT_FAILURE
        iRescuingTarget = oRescueElement.GetRescuingTarget(oOwner)
        if iRescuingTarget:
            if iRescuingTarget != iTarget:
                oRescueElement.HaltRescue(oOwner, { })
                return BT_FAILURE
            return BT_RUNNING
        iRet = oRescueElement.StartRescue(oOwner, iTarget)
        if iRet:
            return BT_RUNNING
        return BT_FAILURE

    RescueTeammate = staticmethod(RescueTeammate)
    
    def OnRescueEnd(self, oListener, dMsgInfo):
        self.SetData('RescueTarget', 0)
        self.SetData('RescueEnd', 1)
        self.m_GameSpace.CallDelayUpdate(self, iFrame = 1)

    
    def CheckToRescueTargetDis(fDis, oAgent):
        oGame = oAgent.m_Game
        iRescueTarget = oAgent.GetData('RescueTarget', 0)
        oRescueTarget = oGame.GetObject(iRescueTarget)
        if not oRescueTarget:
            return False
        tRescueTargetDis = oAgent.GetCache('RescueTargetDisInfo', [])
        if tRescueTargetDis and iRescueTarget == tRescueTargetDis[0] and fDis == tRescueTargetDis[1]:
            return tRescueTargetDis[2]
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vTarget = oRescueTarget.GetPos()
        fNowDis = cl_math.CalDistance3D(vOwner, vTarget)
        bResult = False if fNowDis > fDis else True
        tRescueTargetDis = [
            iRescueTarget,
            fNowDis,
            bResult]
        oAgent.SetCache('RescueTargetDisInfo', tRescueTargetDis)
        return bResult

    CheckToRescueTargetDis = staticmethod(CheckToRescueTargetDis)
    
    def CheckRescueTargetCanSee(oAgent):
        oGame = oAgent.m_Game
        oTarget = oGame.GetObject(oAgent.GetData('RescueTarget', 0))
        if not oTarget:
            return False
        return oAgent.IsEnemyInSight(oAgent.m_OwnerObj, oTarget, iAngle = 180)

    CheckRescueTargetCanSee = staticmethod(CheckRescueTargetCanSee)
    
    def SearchNearShareItem(fDis, fLayerFactor, oAgent):
        oOwner = oAgent.m_OwnerObj
        oScene = oAgent.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return BT_FAILURE
        oWarMgr = oAgent.m_Game.m_WarMgr
        oTeammateAIElement = oWarMgr.GetComponent('TeammateAI')
        if not oTeammateAIElement:
            return BT_FAILURE
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return BT_FAILURE
        iLayer = oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)
        iShareItem = oTeammateAIElement.GetNearestShareItem(oOwner, fDis + iLayer * fLayerFactor)
        if not iShareItem:
            return BT_FAILURE
        oAgent.SetData('ShareItem', iShareItem)
        return BT_SUCCESS

    SearchNearShareItem = staticmethod(SearchNearShareItem)
    
    def GetHideDoorNpc(oAgent):
        oTeammateAIElement = oAgent.m_Game.m_WarMgr.GetComponent('TeammateAI')
        if not oTeammateAIElement:
            return BT_FAILURE
        iHideDoor = oTeammateAIElement.GetHideDoorNpc()
        if not iHideDoor:
            return BT_FAILURE
        oAgent.SetData('ShareItem', iHideDoor)
        return BT_SUCCESS

    GetHideDoorNpc = staticmethod(GetHideDoorNpc)
    
    def CheckHideDoorObstacle(oAgent):
        oShareItem = oAgent.m_Game.GetObject(oAgent.GetData('ShareItem', 0))
        if not oShareItem:
            return False
        if oShareItem.m_FightType & WARRIOR_OBSTACLE and oShareItem.Query('HideLevel'):
            return True
        return False

    CheckHideDoorObstacle = staticmethod(CheckHideDoorObstacle)
    
    def LockShareItem(oAgent):
        iItem = oAgent.GetData('ShareItem', 0)
        if not iItem:
            return BT_FAILURE
        oAgent.SetData('LockTarget', iItem)
        return BT_SUCCESS

    LockShareItem = staticmethod(LockShareItem)
    
    def AdddShareItemSignal(oAgent):
        iShareItem = oAgent.GetData('ShareItem', 0)
        if not iShareItem:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oShareItem = oGame.GetObject(iShareItem)
        if not oShareItem:
            return BT_FAILURE
        oTeammateAIElement = oGame.m_WarMgr.GetComponent('TeammateAI')
        if not oTeammateAIElement:
            return BT_FAILURE
        oSignalMgr = oGame.m_WarMgr.GetComponent('SignalElement')
        if not oSignalMgr:
            return BT_FAILURE
        oAgent.SetData('ShareItem', 0)
        oTeammateAIElement.RemoveShareItem(iShareItem)
        oSignalMgr.AddItemSignal(oAgent.m_OwnerObj, oShareItem)
        return BT_SUCCESS

    AdddShareItemSignal = staticmethod(AdddShareItemSignal)
    
    def ChooseCangJuePerformType(oAgent):
        dCanUsePerformType = oAgent.GetData('CanUsePerformType', { })
        dPerformTypeCD = oAgent.GetData('PerformTypeCD', { })
        dWeight = { }
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        for iPerformType in dCanUsePerformType:
            if not iPerformType not in dPerformTypeCD:
                if iCurFrame >= dPerformTypeCD[iPerformType]:
                    dWeight[iPerformType] = 1
                    continue
        
        if not dWeight:
            return BT_FAILURE
        iType = ChooseKey(oGame, dWeight)
        oAgent.SetData('CangJuePerformType', iType)
        return BT_SUCCESS

    ChooseCangJuePerformType = staticmethod(ChooseCangJuePerformType)
    
    def SetCangJuePerformTypeCD(iType, iCDFrame, oAgent):
        dPerformTypeCD = oAgent.SetDefaultData('PerformTypeCD', { })
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        dPerformTypeCD[iType] = iCurFrame + iCDFrame
        return BT_SUCCESS

    SetCangJuePerformTypeCD = staticmethod(SetCangJuePerformTypeCD)
    
    def CheckCangJuePerform(iType, oAgent):
        return oAgent.GetData('CangJuePerformType', 0) == iType

    CheckCangJuePerform = staticmethod(CheckCangJuePerform)
    
    def CanUseCangJueTurnPerform(oAgent):
        oGame = oAgent.m_Game
        if oAgent.m_OwnerObj.Query('BanTurn', 0):
            return False
        iCurFrame = oGame.GetFrameNum()
        return iCurFrame >= oAgent.GetData('TurnFrame', 0)

    CanUseCangJueTurnPerform = staticmethod(CanUseCangJueTurnPerform)
    
    def UseCertainPF(iPerform, oAgent):
        oGame = oAgent.m_Game
        iTarget = oAgent.GetData('LockTarget', 0)
        if not iTarget:
            return BT_FAILURE
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(iPerform)
        if not oPerform:
            return BT_FAILURE
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastCertainPerform', 0) == iPerform:
            oAgent.SetData('LastCertainPerform', 0)
            return BT_SUCCESS
        oPerform.DelCDTime(oOwner)
        if not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        vEnd = oTarget.GetCenter()
        dData = {
            'pfid': iPerform,
            'VID': oTarget.m_ID,
            'vEnd': vEnd,
            'CastingEndFunc': Functor(SkillCastingEndFunc, oOwner, iPerform) }
        iRet = cl_war.UsePerform(oOwner, oPerform, dData)
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastCertainPerform', iPerform)
                return BT_RUNNING
            return BT_SUCCESS
        return BT_FAILURE

    UseCertainPF = staticmethod(UseCertainPF)
    
    def SetCertainPFIndex(iPerform, iSkillCount, oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.GetPerform(iPerform)
        if not oPerform:
            return BT_FAILURE
        oPerform.SetArgValue('SkillCount', iSkillCount)
        return BT_SUCCESS

    SetCertainPFIndex = staticmethod(SetCertainPFIndex)
    
    def AddState(iState, iTime, oAgent):
        if iTime:
            iTimeType = STATE_TIME_LIMIT
        else:
            iTimeType = STATE_TIME_FOREVER
        oTarget = oAgent.m_OwnerObj
        oState = cl_state.AddState(oTarget, iState, iTimeType, Time2Frame(iTime), {
            'AID': oTarget.m_ID,
            'RS': cl_object.reason.CStrReason('BehaviorTree') })
        if not oState:
            return BT_FAILURE
        oState.Enable(oTarget)
        return BT_SUCCESS

    AddState = staticmethod(AddState)

