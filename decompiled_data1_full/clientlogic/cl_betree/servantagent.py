# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/servantagent.pyc
# RelativePath: clientlogic/cl_betree/servantagent.pyc
# Source Generated with Decompyle++
# File: servantagent.pyc (Python 3.6)

from cl_only import Functor, PY_FLAG_DEAD, GAME_FRAME, HALF_GAME_FRAME, PY_FLAG_SERVANTTARGET, ChooseKey, Time2Frame, PY_FLAG_SERVANTCHOOSETARGET
from cl_betree.mobject import CAgent as CBaseAgent
from cl_behavior.defines import status, BT_SUCCESS, BT_FAILURE, BT_RUNNING
from cl_commondefines import FORBID_MOVE, MOVE_TYPE_NORMAL, FACE_STATUS_PATH, FACE_STATUS_TARGET, MONSTER_PFAI_CATCH, HATEMETHOD_SHIELDPET, HATEMETHOD_LIONLOCKSTATE
from cl_commondefines import RESCUE_SUBMSG_SUCCESS, RESCUE_SUBMSG_END, WARRIOR_BOSS, MONSTER_TYPE_MASK, WARRIOR_MONSTER, HATEMETHOD_HERODIS, HATEMETHOD_IMMOBILIZE, HATEMETHOD_ACCESSIBLE
from cl_commondefines import SERVANT_FIGHTTYPE_HUMAN, SERVANT_FIGHTTYPE_TURRET, STATUS_DEFAULT, STATUS_PATROL, STATUS_RUN, STATUS_SPRINT, MONSTER_STATUS_DEFAULT, MONSTER_STATUS_ATTACK
from cl_commondefines import LION_MONSTER_LOCK_STATE, LION_MONSTER_ENHANCELOCK_STATE, WARRIOR_PET_HEROSIDE
from cl_pxlayer import PXMASK_MOVEBLK, PXMASK_SIGHTBLK, PXMASK_OBJECT, PXMASK_GROUNDBLK, PXMASK_MONSTER
from cl_object.logging import BehaviorLog
import enum
import cl_war
import cl_math
import cl_action
import cl_forbid
import cl_behavior
import cl_msgcenter
import cl_modeldefine
import cl_betree.pfai
import cl_betree.fuzzy
import cl_snetwar
import cl_gamedebug as debug

def MoveToPosEnd(oAgent, iStatus):
    oAgent.SetData('LastArrIdx', 0)
    if iStatus == BT_SUCCESS:
        oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)


def MoveToPosEndCB(oOwner, _tPos, iFail):
    if iFail:
        oOwner.m_Agent.SetData('LastArrIdx', 0)
    oOwner.m_Agent.BTExec()


def ClearTurnToLockEnemyEndFrame(oAgent, iStatus):
    oAgent.SetData('FaceEnemyEnd', 0)


def MoveToLockEnemyEnd(oAgent, iStatus):
    oAgent.SetData('LastFollowTar', 0)


def StopMoveToLockEnemyCBFunc(oOwner, vTar, iFail):
    if not iFail and not oOwner.IsDead():
        oAgent = oOwner.m_Agent
        oAgent.SetData('LastFollowTar', 0)
        oAgent.BTExec()


def SkillCastingEndFunc(oOwner, iPerform, oSkill):
    oAgent = oOwner.m_Agent
    if not oAgent:
        return None
    iBackSwingFrame = oOwner.GetBackSwingRemainingFrame(iPerform)
    iDelayUpdateFrame = iBackSwingFrame + 1
    oAgent.m_GameSpace.CallDelayUpdate(oAgent, iDelayUpdateFrame)


def UsePerformGroupEnd(oAgent, iStatus):
    oAgent.Remove_Call_Out('DelayUsePFGroup')
    oAgent.SetData('PFUsed', 0)
    oAgent.SetData('PFTotal', 0)
    oAgent.SetData('NextPFFrame', 0)
    oAgent.SetData('CurPFGroup', { })


def OnGetTargetInOwnerSight(iAngle, oOwner, oHero, dInfo):
    if not oOwner.m_Scene:
        cl_msgcenter.DoneAttention(oOwner, oHero.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, 'EnemyInHeroSight')
        return None
    oAgent = oOwner.m_Agent
    if not oAgent:
        return None
    iEnemy = oAgent.GetData('EnemyInHeroSight', 0)
    if iEnemy:
        return None
    if 'OriginalAID' in dInfo:
        return None
    iVictim = dInfo['CurVID']
    dOutSight = oAgent.GetCache('OutHeroSight', { })
    if iVictim in dOutSight:
        return None
    oGame = oAgent.m_Game
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
        return None
    fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, oVictim.GetPos(), 10, PXMASK_MOVEBLK, oOwner.m_ID)
    if fGroundDis < 5:
        vVictim = oVictim.GetPos()
        vHero = oHero.GetPos()
        vDir = cl_math.Vec3Minus(vVictim, vHero)
        vFace = oHero.GetFacing()
        if not cl_math.CheckVector2Angle(vDir, vFace, iAngle):
            oAgent.SetData('EnemyInHeroSight', iVictim)
            return None
    dOutSight[iVictim] = 1
    oAgent.SetCache('OutHeroSight', dOutSight)


class ActionSMArgType(enum.Enum):
    tType1 = ('Trigger', 1)
    tType2 = ('Bool', 2)
    tType3 = ('Float', 3)


class HateMethodType(enum.Enum):
    tType1 = ('玩家距离', HATEMETHOD_HERODIS)
    tType2 = ('优先被定身目标', HATEMETHOD_IMMOBILIZE)
    tType3 = ('优先仇恨可达目标', HATEMETHOD_ACCESSIBLE)
    tType4 = ('防御妖灵', HATEMETHOD_SHIELDPET)


class ServantFightType(enum.Enum):
    tType1 = ('人型战斗', SERVANT_FIGHTTYPE_HUMAN)
    tType2 = ('炮台型战斗', SERVANT_FIGHTTYPE_TURRET)


class MoveStatusType(enum.Enum):
    tType1 = ('DEFAULT', STATUS_DEFAULT)
    tType2 = ('PATROL', STATUS_PATROL)
    tType3 = ('RUN', STATUS_RUN)
    tType4 = ('SPRINT', STATUS_SPRINT)


class FightStatusType(enum.Enum):
    tType1 = ('DEFAULT', MONSTER_STATUS_DEFAULT)
    tType2 = ('ATTACK', MONSTER_STATUS_ATTACK)


class CAgent(CBaseAgent):
    m_HateRatio = 1.1
    m_ConfigKey = {
        '攻击范围': 'HitRange' }
    m_DataKey = {
        '当前技能使用范围': 'CurPerformUseDis',
        '跟随状态': 'FollowMoveStatus',
        '仇恨计算方式': 'HateMethod',
        '瞬移坐标': 'TransferPos',
        '技能使用范围最小值': 'MinPerformUseDis',
        '可移动释放技能': 'MoveUsePerform',
        '是否仇恨召唤物': 'HateSummon',
        '是否仇恨守护目标': 'HataProtege' }
    m_ConfigAttr = {
        'HitRange'}
    
    def __init__(self):
        super(CAgent, self).__init__()
        self.m_PFAI = None
        self.m_CurPerformUseHeight = 0

    
    def Config(self, oOwner, dConfig):
        super(CAgent, self).Config(oOwner, dConfig)
        if 'PFAI' in dConfig:
            self.m_PFAI = cl_betree.pfai.NewPFAI(dConfig['PFAI'], oOwner)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_RESCUE, self.OnRescueEnd, 'ServantAgentEnd', iSub = RESCUE_SUBMSG_END, iOnce = 0)
        cl_msgcenter.AddFunction(oOwner, cl_msgcenter.MSG_WAR_RESCUE, self.OnRescueSuccess, 'ServantAgentSuccess', iSub = RESCUE_SUBMSG_SUCCESS, iOnce = 0)

    
    def GetConfig(self, sKey, default = None):
        if sKey in self.m_ConfigAttr:
            return self.m_OwnerObj.QueryAttr(sKey)
        return super(CAgent, self).GetConfig(sKey, default)

    
    def OnRescueEnd(self, oTarget, dMsgInfo):
        self.SetData('RescueTarget', 0)
        self.SetData('RescueEnd', 1)
        self.m_GameSpace.CallDelayUpdate(self, iFrame = 1)

    
    def OnRescueSuccess(self, oTarget, dMsgInfo):
        iCurFrame = self.m_Game.GetFrameNum()
        self.SetData('LastRescueFrame', iCurFrame)

    
    def Release(self):
        oOwner = self.m_OwnerObj
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_RESCUE, 'ServantAgentEnd', iSub = RESCUE_SUBMSG_END)
        cl_msgcenter.DoneEvent(oOwner, cl_msgcenter.MSG_WAR_RESCUE, 'ServantAgentSuccess', iSub = RESCUE_SUBMSG_SUCCESS)
        if self.m_PFAI:
            self.m_PFAI.Release()
        super(CAgent, self).Release()

    
    def EnterScene(self, oScene):
        super().EnterScene(oScene)
        self.ResumeAgent('LeaveScene')

    
    def LeaveScene(self):
        super(CAgent, self).LeaveScene()
        self.PauseAgent('LeaveScene')
        self.SetLockEnemy(0)
        self.HaltPerform(self)
        oOwner = self.m_OwnerObj
        if oOwner.m_MoveMode != MOVE_TYPE_NORMAL:
            oOwner.m_MoveMode = MOVE_TYPE_NORMAL
        self.Stop()
        self.SetData('HateData', { })
        self.SetData('ArrivePos', None)
        self.SetCache('HeroSceneDis', { })

    
    def AddForceHateTarget(self, iTarget):
        dForceHateTarget = self.GetData('ForceHateTarget', { })
        if iTarget not in dForceHateTarget:
            if not dForceHateTarget:
                self.SetLockEnemy(iTarget)
            dForceHateTarget[iTarget] = 1
        self.SetData('ForceHateTarget', dForceHateTarget)

    
    def RemoveForceHateTarget(self, iTarget):
        dForceHateTarget = self.GetData('ForceHateTarget', { })
        dForceHateTarget.pop(iTarget, 0)

    
    def ClearForceHateTarget(self):
        self.SetData('ForceHateTarget', { })

    
    def UpdateInAdvance(iFrame, oAgent):
        oAgent.m_GameSpace.CallDelayUpdate(oAgent, iFrame)
        return BT_SUCCESS

    UpdateInAdvance = staticmethod(UpdateInAdvance)
    
    def GetPhase(oAgent):
        return oAgent.m_OwnerObj.Phase()

    GetPhase = staticmethod(GetPhase)
    
    def SetLockEnemy(self, iTarget):
        self.m_OwnerObj.SetLockEnemy(iTarget)

    
    def GetLockEnemy(self):
        iLockEnemy = self.m_OwnerObj.Query('LockEnemy', 0)
        if iLockEnemy:
            oEnemy = self.m_Game.GetObject(iLockEnemy, PY_FLAG_DEAD)
            if oEnemy and oEnemy.m_Scene == self.m_OwnerObj.m_Scene:
                return oEnemy
            self.SetLockEnemy(0)

    
    def GetHateTarget(self):
        dForceHateTarget = self.GetData('ForceHateTarget', { })
        for iTarget in dForceHateTarget:
            oTarget = self.m_Game.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
            if oTarget:
                return dForceHateTarget
        
        dTarget = self.GetCache('HateTarget', { })
        if not dTarget:
            dTarget = self.m_SceneData.m_FightMonster
        return dTarget

    
    def GetHeroEnemyDis(self):
        dDis = self.GetCache('HeroSceneDis', { })
        if dDis:
            return dDis
        if not self.m_SceneData:
            return { }
        oServant = self.m_OwnerObj
        oHero = oServant.GetOwner()
        if not oHero:
            return { }
        dTarget = self.GetHateTarget()
        if not dTarget:
            return { }
        dDis = self.m_Game.Scene_GetTargetDisMap(oHero.m_ID, list(dTarget), 1)
        self.SetCache('HeroSceneDis', dDis)
        return dDis

    
    def SeekPath(self, oOwner, tPos, func = None):
        iForbidMove = oOwner.IsForbid(FORBID_MOVE)
        bNormal = oOwner.m_MoveMode == MOVE_TYPE_NORMAL
        if iForbidMove and oOwner.HasRule(cl_forbid.NAVSEEK_RULE) and not oOwner.Query('SeekAlert'):
            oCurrent = oOwner.m_Agent.m_CurrentBT
            sName = oCurrent.GetName() if oCurrent else ''
            oOwner.Set('SeekAlert', 1)
            BehaviorLog.Error(f'''{self.m_Game.m_ID} {oOwner.m_SID} {sName} forbid seepath''')
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

    
    def UpdateAIRuningState(iState, oAgent):
        oOwner = oAgent.m_OwnerObj
        oScene = oAgent.m_Game.m_SceneMgr.GetScene(oOwner.m_Scene)
        if not oScene:
            return BT_FAILURE
        iOldState = oAgent.GetData('AIState', 0)
        if iState == iOldState:
            return BT_SUCCESS
        if iState == 1:
            oScene.DelMonsterEnemy(oOwner.m_ID)
        else:
            oScene.AddMonsterEnemy(oOwner.m_ID)
        oAgent.SetData('AIState', iState)
        return BT_SUCCESS

    UpdateAIRuningState = staticmethod(UpdateAIRuningState)
    
    def SetForceMoveSpeed(iSpeed, oAgent):
        if iSpeed < 0:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        if iSpeed:
            oOwner.AttrForceSet('MoveSpeed', iSpeed, 'ServantAgent')
        else:
            oOwner.AttrForceClear('MoveSpeed', 'ServantAgent')
        return BT_SUCCESS

    SetForceMoveSpeed = staticmethod(SetForceMoveSpeed)
    
    def CheckSceneHasFightMonster(fLimitHeroDis, oAgent):
        if oAgent.GetCache('NoHate', 0):
            return False
        if not oAgent.m_SceneData:
            return False
        if not fLimitHeroDis:
            if oAgent.m_SceneData.m_FightMonster:
                return True
            return False
        dDis = oAgent.m_Game.Scene_GetTargetDisMap(oAgent.m_OwnerObj.m_ID, list(oAgent.m_SceneData.m_FightMonster), 1)
        for _, fDis in dDis.items():
            if fDis <= fLimitHeroDis:
                return True
        
        return False

    CheckSceneHasFightMonster = staticmethod(CheckSceneHasFightMonster)
    
    def IsEnterFight(oAgent):
        if not oAgent.m_SceneData:
            return False
        if 'EnterFight' in oAgent.m_SceneData.m_Data:
            return True
        oGame = oAgent.m_Game
        for iTarget in oAgent.GetHateTarget():
            oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
            if oTarget:
                return True
        
        return False

    IsEnterFight = staticmethod(IsEnterFight)
    
    def ChooseOwnerAroundPos(fMinRadius, fMaxRadius, iAngle1, iAngle2, oAgent):
        oServant = oAgent.m_OwnerObj
        iScene = oServant.m_Scene
        if not iScene:
            return BT_FAILURE
        oHero = oServant.GetOwner()
        if not oHero:
            return BT_FAILURE
        oGame = oAgent.m_Game
        vTarget = oHero.GetPos()
        vPos = oGame.Scene_RandomPointSectorInMesh(iScene, vTarget, oHero.GetFacing(), fMinRadius, fMaxRadius, iAngle1, iAngle2)
        if not vPos:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vPos)
        if oGame.GetWarMgr().Query('DebugRay'):
            debug.ClearDebugLine(oAgent.m_Game, debug.LINE_TILE)
            (ox, oy, oz) = oServant.GetPos()
            (tx, ty, tz) = vPos
            debug.DebugLine(oAgent.m_Game, ox, oy, oz, tx, ty, tz, 65535, debug.LINE_TILE)
        return BT_SUCCESS

    ChooseOwnerAroundPos = staticmethod(ChooseOwnerAroundPos)
    
    def ChooseEnemyAroundPos(fMinRadius, fMaxRadius, fLimitDis, oAgent):
        oTarget = oAgent.GetLockEnemy()
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
    
    def ChooseRangedPos(fRadius, fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oAgent.Remove_Call_Out('CleanMoveDir')
        oOwner = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        tMoveDir = oAgent.GetData('MoveDir', None)
        vEnd = None
        if tMoveDir and tMoveDir[0] and cl_math.CheckDistance(vOwner, vEnemy, 2 * fRadius):
            (vLastDir, fFirstDis) = tMoveDir
            iAngle = oGame.Random(46)
            iAngle = -iAngle if oGame.Random(2) else iAngle
            fDis = oGame.Random(int(100 * (fMaxDis - fMinDis))) / 100 + fMinDis
            vDir = cl_math.RotateAroundVector(vLastDir, (0, 1, 0), iAngle)
            vEnd = cl_math.Vec3DisplaceDir(vOwner, vDir, fDis)
            fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, vEnd, 2, PXMASK_MOVEBLK | PXMASK_OBJECT, oOwner.m_ID)
            vEnd = oAgent.m_Game.Scene_NavMeshRayCast(oOwner.m_Scene, vOwner, (vEnd[0], vEnd[1] - fGroundDis, vEnd[2]))
            if cl_math.CheckDistance(vEnd, vEnemy, 5):
                vEnd = None
            else:
                oAgent.SetData('MoveDir', (vDir, fFirstDis))
        if not vEnd or cl_math.CheckDistance(vEnd, vOwner, 0.01):
            vDir = cl_math.Vec3Minus(vEnemy, vOwner)
            if vEnemy == vOwner:
                vCenter = vEnemy
            else:
                vCenter = cl_math.Vec3DisplacePos(vEnemy, vOwner, fRadius)
            vEnd = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vCenter, vDir, fMinDis, fMaxDis, iMinAngle, iMaxAngle)
            if not vEnd:
                (fMinDis, fMaxDis, iMinAngle, iMaxAngle) = (3, fMaxDis + 2, 60, 120)
                for _ in range(3):
                    vEnd = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vOwner, vDir, fMinDis, fMaxDis, iMinAngle, iMaxAngle)
                    if vEnd:
                        break
                
                if not vEnd:
                    oAgent.SetData('MoveDir', None)
                    return BT_FAILURE
            vMoveDir = cl_math.Vec3Minus(vEnd, vOwner)
            oAgent.SetData('MoveDir', (vMoveDir, cl_math.CalDistance(vOwner, vEnd)))
        oAgent.SetData('ArrivePos', vEnd)
        if oGame.GetWarMgr().Query('DebugRay'):
            debug.ClearDebugLine(oAgent.m_Game, debug.LINE_TILE)
            (ox, oy, oz) = oOwner.GetPos()
            (tx, ty, tz) = vEnd
            debug.DebugLine(oAgent.m_Game, ox, oy, oz, tx, ty, tz, 65535, debug.LINE_TILE)
        return BT_SUCCESS

    ChooseRangedPos = staticmethod(ChooseRangedPos)
    
    def ChooseTargetAwayPos(fRange, fAngle, iRayNum, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vTarget = oTarget.GetPos()
        vEnd = oOwner.m_MoveCtrl.E_KeepAwayRayCastPos(vTarget, fRange, -fAngle, fAngle, iRayNum)
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    ChooseTargetAwayPos = staticmethod(ChooseTargetAwayPos)
    
    def ChooseHateFlankPos(fMinDis, fMaxDis, iMinAngle, iMaxAngle, oAgent):
        dHate = oAgent.GetData('HateData', { })
        oOwner = oAgent.m_OwnerObj
        oGame = oAgent.m_Game
        vMonster = [
            0,
            0,
            0]
        iCnt = 0
        for iMonster in dHate:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if oMonster:
                vMonster = cl_math.Vec3Add(vMonster, oMonster.GetPos())
                iCnt += 1
        
        if iCnt:
            vTarget = cl_math.Vec3MulF(vMonster, 1 / iCnt)
        else:
            oEnemy = oAgent.GetLockEnemy()
            if not oEnemy:
                return BT_FAILURE
            vTarget = oEnemy.GetPos()
        vStart = oOwner.GetPos()
        vDir = cl_math.Vec3Minus(vTarget, vStart)
        vEnd = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vStart, vDir, fMinDis, fMaxDis, iMinAngle, iMaxAngle)
        if not vEnd:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vEnd)
        return BT_SUCCESS

    ChooseHateFlankPos = staticmethod(ChooseHateFlankPos)
    
    def GetOwnerToLockEnemyDis(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return 0
        oOwner = oAgent.m_OwnerObj
        oHero = oOwner.GetOwner()
        if not oHero:
            return 0
        return cl_math.CalDistance(oEnemy.GetPos(), oHero.GetPos())

    GetOwnerToLockEnemyDis = staticmethod(GetOwnerToLockEnemyDis)
    
    def CheckHasUsedSkill(oAgent):
        dPerform = oAgent.GetData('CurChosenPF', { })
        if dPerform:
            return True
        return False

    CheckHasUsedSkill = staticmethod(CheckHasUsedSkill)
    
    def ModifySkillEndPosByTarget(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        vPos = oEnemy.Query('PerformAttackedPos')
        if vPos:
            oAgent.SetData('vEnd', vPos)
        return BT_SUCCESS

    ModifySkillEndPosByTarget = staticmethod(ModifySkillEndPosByTarget)
    
    def LockEnemyIsBoss(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        return oTarget.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS

    LockEnemyIsBoss = staticmethod(LockEnemyIsBoss)
    
    def CheckLockTargetSID(iSID, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        return oTarget.m_DataSID == iSID

    CheckLockTargetSID = staticmethod(CheckLockTargetSID)
    
    def FaceSkillEndPos(iTurnSpeed, oAgent):
        vEnd = oAgent.GetData('vEnd', ())
        if not vEnd:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oOwner.m_FaceCtrl.FacePos(oOwner, vEnd, 'FaceSkillEndPos', iTurnSpeed / GAME_FRAME)
        return BT_SUCCESS

    FaceSkillEndPos = staticmethod(FaceSkillEndPos)
    
    def FacePath(oAgent):
        oOwner = oAgent.m_OwnerObj
        if not oOwner.m_FaceCtrl:
            return BT_FAILURE
        oOwner.m_FaceCtrl.FacePath(oOwner, 'AI')
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_PATH, ('AI',)))
        return BT_SUCCESS

    FacePath = staticmethod(FacePath)
    
    def FaceLockEnemy(iKeep, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        lstArgs = [
            oEnemy.m_ID,
            'AI',
            0,
            iKeep]
        oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_TARGET, lstArgs))
        return BT_SUCCESS

    FaceLockEnemy = staticmethod(FaceLockEnemy)
    
    def TurnToLockEnemy(iTurnTime, iKeep, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        iCurFrame = oAgent.m_Game.GetFrameNum()
        iEndFrame = oAgent.GetData('FaceEnemyEnd', 0)
        if iEndFrame:
            if iEndFrame <= iCurFrame:
                return BT_SUCCESS
            return BT_RUNNING
        oOwner = oAgent.m_OwnerObj
        lstArgs = [
            oEnemy.m_ID,
            'AI',
            iTurnTime,
            iKeep]
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_TARGET, lstArgs))
        oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)
        if iTurnTime:
            iTurnFrame = Time2Frame(iTurnTime)
            oAgent.SetData('FaceEnemyEnd', iCurFrame + iTurnFrame)
            oAgent.AddCurNodeEndFunc(ClearTurnToLockEnemyEndFrame)
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, iTurnFrame)
            return BT_RUNNING
        return BT_SUCCESS

    TurnToLockEnemy = staticmethod(TurnToLockEnemy)
    
    def FaceRescueTarget(iKeep, oAgent):
        iTarget = oAgent.GetData('RescueTarget', 0)
        if not iTarget:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        lstArgs = [
            iTarget,
            'AI',
            0,
            iKeep]
        oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)
        oAgent.SetData('LastFaceStatus', (FACE_STATUS_TARGET, lstArgs))
        return BT_SUCCESS

    FaceRescueTarget = staticmethod(FaceRescueTarget)
    
    def CheckLockAlive(oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return False
        if oTarget.IsDead():
            return False
        return True

    CheckLockAlive = staticmethod(CheckLockAlive)
    
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
    
    def ResumeFaceStatus(self):
        if not self.m_bActive:
            return None
        tPreFaceStatus = self.GetData('LastFaceStatus', ())
        if tPreFaceStatus:
            oOwner = self.m_OwnerObj
            (iStatus, lstArgs) = tPreFaceStatus
            oOwner.m_FaceCtrl.m_FaceVictim = 0
            if iStatus == FACE_STATUS_PATH:
                oOwner.m_FaceCtrl.FacePath(oOwner, *lstArgs)
            elif iStatus == FACE_STATUS_TARGET:
                oOwner.m_FaceCtrl.FaceTarget(oOwner, *lstArgs)

    
    def FlashToPos(oAgent):
        vTarget = oAgent.GetData('ArrivePos')
        if not vTarget:
            vTarget = oAgent.GetData('TransferPos')
            if not vTarget:
                return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oOwner.WalkTo(vTarget, 'servantagent')
        oAgent.SetData('ArrivePos', None)
        oAgent.SetData('TransferPos', None)
        return BT_SUCCESS

    FlashToPos = staticmethod(FlashToPos)
    
    def MoveToLockEnemy(fCatchDis, oAgent):
        oEnemy = oAgent.GetLockEnemy()
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
    
    def MoveToHeroPos(fCatchDis, oAgent):
        oOwner = oAgent.m_OwnerObj
        oHero = oOwner.GetOwner()
        if not oHero:
            return BT_FAILURE
        if fCatchDis <= 0:
            return BT_FAILURE
        vOwner = oOwner.GetPos()
        vHero = oHero.GetGroundPos()
        if cl_math.CheckDistance3D(vOwner, vHero, fCatchDis) and abs(vOwner[1] - vHero[1]) <= 1.5:
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        if oAgent.FollowMove(oOwner, oHero.m_ID, fCatchDis, None):
            return BT_RUNNING
        return BT_FAILURE

    MoveToHeroPos = staticmethod(MoveToHeroPos)
    
    def ChooseLockTargetNearestSpace(bCalEnemyRadius, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vEnemy = oEnemy.GetPos()
        vOwner = oOwner.GetPos()
        if bCalEnemyRadius:
            (fEnemyRadius, _) = cl_modeldefine.GetModelDefine(oEnemy.m_Shape, 'NavMesh')
            vEnemy = cl_math.Vec3DisplacePos(vEnemy, vOwner, fEnemyRadius)
        (iRet, vPos) = oAgent.m_Game.Scene_GetAccessibleDestPos(oOwner.m_Scene, vOwner, vEnemy)
        if not iRet:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vPos)
        oAgent.SetData('vEnd', vPos)
        return BT_SUCCESS

    ChooseLockTargetNearestSpace = staticmethod(ChooseLockTargetNearestSpace)
    
    def FollowMove(self, oOwner, iTarget, fStopDis, func, iAppointFrame = 0):
        iForbidMove = oOwner.IsForbid(FORBID_MOVE)
        bNormal = oOwner.m_MoveMode == MOVE_TYPE_NORMAL
        if iForbidMove and oOwner.HasRule(cl_forbid.NAVSEEK_RULE) and not oOwner.Query('SeekAlert'):
            oCurrent = oOwner.m_Agent.m_CurrentBT
            sName = oCurrent.GetName() if oCurrent else ''
            oOwner.Set('SeekAlert', 1)
            BehaviorLog.Error(f'''{self.m_Game.m_ID} {oOwner.m_SID} {sName} forbid followmove''')
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

    
    def UseLockEnemyPos(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oAgent.SetData('ArrivePos', oEnemy.GetPos())

    UseLockEnemyPos = staticmethod(UseLockEnemyPos)
    
    def GetCurMap(oAgent):
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oAgent.m_OwnerObj.m_Scene)
        if not oScene:
            return ''
        return str(oScene.Map())

    GetCurMap = staticmethod(GetCurMap)
    
    def CatchLockEnemy(fCatchDis, fHeight, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        if fCatchDis <= 0:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        if vEnemy[1] - vOwner[1] > fHeight:
            oAgent.Stop()
            return BT_FAILURE
        iOldIdx = oAgent.GetData('LastArrIdx', 0)
        oAgent.AddCurNodeEndFunc(MoveToPosEnd)
        if oEnemy.m_MoveCtrl:
            fEnemyRadius = oEnemy.m_MoveCtrl.m_NavRadius
        else:
            (fEnemyRadius, _) = cl_modeldefine.GetModelDefine(oEnemy.m_Shape, 'NavMesh')
        fCatchDis += fEnemyRadius
        if iOldIdx and oOwner.m_MoveMode == MOVE_TYPE_NORMAL and cl_math.CheckDistance3D(vOwner, vEnemy, fCatchDis):
            if oAgent.Stop():
                return BT_SUCCESS
            if not oOwner.IsStop():
                return BT_RUNNING
            return BT_FAILURE
        oMoveCtrl = oOwner.m_MoveCtrl
        if iOldIdx:
            if not (oMoveCtrl.m_ArriveInfo) or iOldIdx != oMoveCtrl.m_ArriveInfo[0]:
                return BT_FAILURE
        vTarget = cl_math.Vec3DisplaceDir(vEnemy, cl_math.Vec3Minus(vOwner, vEnemy), oMoveCtrl.m_NavRadius + fEnemyRadius)
        if oAgent.SeekPath(oOwner, vTarget, func = MoveToPosEndCB):
            oAgent.SetData('LastArrIdx', oMoveCtrl.m_ArriveInfo[0])
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, 5)
            return BT_RUNNING
        return BT_FAILURE

    CatchLockEnemy = staticmethod(CatchLockEnemy)
    
    def SpecifyEndPosOffset(x, y, z, bArrive, bSkillEnd, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        vPos = (x, y, z)
        vEnemy = oEnemy.GetPos()
        oGame = oAgent.m_Game
        iShiftAngle = 90 if oGame.Random(2) else -90
        fDis = oGame.Random(40) / 10
        vDir = cl_math.Vec3Minus(vEnemy, vPos)
        vArrivePos = cl_math.Vec3DestPosDirPlane(vPos, vDir, fDis, iShiftAngle)
        if bArrive:
            oAgent.SetData('ArrivePos', vArrivePos)
        if bSkillEnd:
            oAgent.SetData('vEnd', vArrivePos)
        return BT_SUCCESS

    SpecifyEndPosOffset = staticmethod(SpecifyEndPosOffset)
    
    def TargetAwayPos(fRange, bArrive, bSkillEnd, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        vEnemy = oEnemy.GetPos()
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        (x, z) = cl_math.Vec2DisplaceDir((vEnemy[0], vEnemy[2]), (vOwner[0] - vEnemy[0], vOwner[2] - vEnemy[2]), fRange)
        vRetPos = (x, vEnemy[1], z)
        if bArrive:
            oAgent.SetData('ArrivePos', vRetPos)
        if bSkillEnd:
            oAgent.SetData('vEnd', vRetPos)
        return BT_SUCCESS

    TargetAwayPos = staticmethod(TargetAwayPos)
    
    def GetDistanceFormSpecifyPos(x, y, z, oAgent):
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        return cl_math.CalDistance(vOwner, (x, y, z))

    GetDistanceFormSpecifyPos = staticmethod(GetDistanceFormSpecifyPos)
    
    def GetTargetOffsetPos(x, y, z, bArrive, bSkillEnd, oAgent):
        oTarget = oAgent.GetLockEnemy()
        if not oTarget:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        vTarget = oTarget.GetPos()
        vPos = cl_math.Vec3Add(vTarget, (x, y, z))
        fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, (vPos[0], vPos[1] + 2, vPos[2]), 10, PXMASK_GROUNDBLK, oOwner.m_ID)
        vPos = (vPos[0], vPos[1] + 2 - fGroundDis, vPos[2])
        if bArrive:
            oAgent.SetData('ArrivePos', vPos)
        if bSkillEnd:
            oAgent.SetData('vEnd', vPos)
        return BT_SUCCESS

    GetTargetOffsetPos = staticmethod(GetTargetOffsetPos)
    
    def IsLockEnemyPosAccessible(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        if oEnemy.Query('ForceNoDest'):
            return False
        vEnemy = oEnemy.GetPos()
        oGame = oAgent.m_Game
        fModelRadius = oEnemy.m_ModelRadius
        lstVictim = oGame.Scene_SweepMultiple(oEnemy.m_Scene, vEnemy, fModelRadius, (0, -1, 0), 0.1, PXMASK_MOVEBLK, {
            'BlockMask': PXMASK_MOVEBLK })
        if not lstVictim:
            return True
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        return oGame.Scene_IsDestPosAccessible(oOwner.m_Scene, vOwner, vEnemy)

    IsLockEnemyPosAccessible = staticmethod(IsLockEnemyPosAccessible)
    
    def IsEnemyInSight(self, oOwner, oTarget, iAngle, iUsePerform = 0):
        dInSight = self.GetCache('InSight', { })
        if oTarget.m_ID in dInSight:
            (iCacheAngle, bRes, iCacheUse) = dInSight[oTarget.m_ID]
            if iUsePerform == iCacheUse:
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
        if iUsePerform:
            fOwnerCheckHeight = self.m_CurPerformUseHeight if self.m_CurPerformUseHeight else oOwner.m_ModelHeight * 0.55
        else:
            fOwnerCheckHeight = oOwner.m_ModelHeight * 0.85
        (x, z) = cl_math.Vec2DisplaceDir((vOwner[0], vOwner[2]), (vTarget[0] - vOwner[0], vTarget[2] - vOwner[2]), 0.5)
        vOwner = (x, vOwner[1] + fOwnerCheckHeight, z)
        vTarget = (vTarget[0], vTarget[1] + oTarget.m_ModelHeight * 0.85, vTarget[2])
        oGame = self.m_Game
        bSight = not oGame.Scene_RaycastAnyHit(oOwner.m_Scene, vOwner, vTarget, PXMASK_SIGHTBLK)
        dInSight[oTarget.m_ID] = (iAngle, bSight, iUsePerform)
        self.SetCache('InSight', dInSight)
        return bSight

    
    def CheckCanSeeLock(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        return oAgent.IsEnemyInSight(oAgent.m_OwnerObj, oEnemy, 180, iUsePerform = 1)

    CheckCanSeeLock = staticmethod(CheckCanSeeLock)
    
    def CheckInHeroSight(iAngle, oAgent):
        oOwner = oAgent.m_OwnerObj
        oHero = oOwner.GetOwner()
        if not oHero:
            return False
        vOwner = oOwner.GetPos()
        vHero = oHero.GetPos()
        vDir = cl_math.Vec3Minus(vOwner, vHero)
        vFace = oHero.GetFacing()
        if cl_math.CheckVector2Angle(vDir, vFace, iAngle):
            return False
        return True

    CheckInHeroSight = staticmethod(CheckInHeroSight)
    
    def CheckHasState(iState, oAgent):
        if oAgent.m_OwnerObj.m_State.GetItemBySID(iState):
            return True
        return False

    CheckHasState = staticmethod(CheckHasState)
    
    def StopMoving(oAgent):
        iRet = oAgent.Stop()
        if iRet:
            oAgent.SetData('ArrivePos', None)
            oAgent.SetData('LastFollowTar', 0)
            oAgent.SetData('LastArrIdx', 0)
            oOwner = oAgent.m_OwnerObj
            oOwner.AttrForceClear('MoveSpeed', 'ServantAgent')
            return BT_SUCCESS
        return BT_FAILURE

    StopMoving = staticmethod(StopMoving)
    
    def Stop(self):
        oOwner = self.m_OwnerObj
        oMoveCtrl = oOwner.m_MoveCtrl
        if not oMoveCtrl:
            return 0
        if oOwner.m_MoveMode not in (MOVE_TYPE_NORMAL,):
            return 0
        oMoveCtrl.OverArrive(oOwner, 0, iCallBack = 0)
        if self.GetData('MoveDir', None):
            self.Call_Out(self.CleanMoveDir, HALF_GAME_FRAME, 'CleanMoveDir')
        return oMoveCtrl.Stop(oOwner)

    
    def CleanMoveDir(self):
        self.SetData('MoveDir', None)

    
    def ChooseHateTarget(iHateMethod, fLimitHeroDis, oAgent):
        oAgent.UpdateHate(iHateMethod, fLimitHeroDis)
        dHateData = oAgent.GetData('HateData', { })
        iMaxVal = -1
        iMaxTarget = 0
        lstMaxTarget = []
        for iTarget, dData in dHateData.items():
            if iMaxVal < dData['Hate'][0]:
                iMaxVal = dData['Hate'][0]
                iMaxTarget = iTarget
                lstMaxTarget = [
                    iMaxTarget]
                continue
            if iMaxVal == dData['Hate'][0]:
                lstMaxTarget.append(iTarget)
        
        if iMaxTarget:
            oNowTarget = oAgent.GetLockEnemy()
            iNowTarget = oNowTarget.m_ID if oNowTarget else 0
            if iMaxTarget != iNowTarget:
                iNowVal = dHateData[iNowTarget]['Hate'][0] if iNowTarget in dHateData else -1
                if iMaxVal > iNowVal * oAgent.m_HateRatio:
                    if len(lstMaxTarget) > 1:
                        dDis = oAgent.m_Game.Scene_GetTargetDisMap(oAgent.m_OwnerObj.m_ID, lstMaxTarget, 1)
                        lstSortDis = sorted(dDis.items(), key = (lambda item: item[1]))
                        iMaxTarget = lstSortDis[0][0]
                    oAgent.SetLockEnemy(iMaxTarget)
            return BT_SUCCESS
        oAgent.SetLockEnemy(0)
        return BT_FAILURE

    ChooseHateTarget = staticmethod(ChooseHateTarget)
    
    def ChooseAttackTarget(fLimitHeroDis, bInSight, oAgent):
        oAgent.UpdateHate(HATEMETHOD_HERODIS)
        dHateData = oAgent.GetData('HateData', { })
        oGame = oAgent.m_Game
        oOwner = oAgent.m_OwnerObj
        oHero = oOwner.GetOwner()
        if not oHero:
            return BT_FAILURE
        dDis = oGame.Scene_GetTargetDisMap(oHero.m_ID, list(dHateData), 1)
        fMinDis = 999
        iNearest = 0
        for iTarget, fDis in dDis.items():
            if fLimitHeroDis and fDis > fLimitHeroDis:
                continue
            if bInSight:
                oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
                if not oTarget:
                    continue
                if not oAgent.IsEnemyInSight(oOwner, oTarget, iAngle = 180, iUsePerform = 1):
                    continue
                continue
            if fDis < fMinDis:
                fMinDis = fDis
                iNearest = iTarget
        
        if iNearest:
            oAgent.SetLockEnemy(iNearest)
            return BT_SUCCESS
        oAgent.SetLockEnemy(0)
        return BT_FAILURE

    ChooseAttackTarget = staticmethod(ChooseAttackTarget)
    
    def ChooseSeeEnemy(iHateMethod, fArea, oAgent):
        oAgent.UpdateHate(iHateMethod)
        oNowTarget = oAgent.GetLockEnemy()
        oOwner = oAgent.m_OwnerObj
        oAgent.m_CurPerformUseHeight = 1.05
        if oNowTarget and not oAgent.IsEnemyInSight(oOwner, oNowTarget, iAngle = 180, iUsePerform = 1):
            oNowTarget = None
        dHateData = oAgent.GetData('HateData', { })
        oGame = oAgent.m_Game
        dDis = oGame.Scene_GetTargetDisMap(oAgent.m_OwnerObj.m_ID, list(dHateData), 1)
        iMaxVal = -1
        iMaxTarget = 0
        fMinDis = 9999
        (iNearestTarget, fNearestDis) = (0, 9999)
        for iTarget, fDis in dDis.items():
            if fDis > fArea:
                continue
            oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
            if not oTarget:
                continue
            if fDis < fNearestDis:
                iNearestTarget = iTarget
                fNearestDis = fDis
            if not oAgent.IsEnemyInSight(oOwner, oTarget, iAngle = 180, iUsePerform = 1):
                continue
            iTargetHate = dHateData[iTarget]['Hate'][0]
            if not iMaxVal < iTargetHate:
                if iMaxVal == iTargetHate and fDis < fMinDis:
                    fMinDis = fDis
                    iMaxVal = iTargetHate
                    iMaxTarget = iTarget
                    continue
        
        if iMaxTarget:
            iNowTarget = oNowTarget.m_ID if oNowTarget else 0
            if iMaxTarget != iNowTarget:
                iNowVal = dHateData[iNowTarget]['Hate'][0] if iNowTarget in dHateData else -1
                if iMaxVal > iNowVal * oAgent.m_HateRatio:
                    oAgent.SetLockEnemy(iMaxTarget)
                elif iNearestTarget:
                    oAgent.SetLockEnemy(iNearestTarget)
                else:
                    oAgent.SetLockEnemy(0)
        if None.m_OwnerObj.Query('LockEnemy', 0):
            return BT_SUCCESS
        return BT_FAILURE

    ChooseSeeEnemy = staticmethod(ChooseSeeEnemy)
    
    def GetDisEff(self, fDis, tDisEff):
        fDisEff = 1
        fLastLimitDis = 0
        for fLimitDis, fLimitEff in tDisEff:
            if fLimitDis == fLastLimitDis:
                BehaviorLog.Error('%d %d dis %s err %s' % (self.m_OwnerObj.m_Game.m_ID, self.m_OwnerObj.m_SID, fLimitDis, tDisEff))
                continue
            if fDis <= fLimitDis:
                fDisEff += (fLimitEff - fDisEff) * (fDis - fLastLimitDis) / (fLimitDis - fLastLimitDis)
                break
            fLastLimitDis = fLimitDis
            fDisEff = fLimitEff
        
        return fDisEff

    
    def UpdateHate(self, iHateMethod, fLimitHeroDis = 0):
        dHateData = { }
        if iHateMethod in (HATEMETHOD_HERODIS, HATEMETHOD_IMMOBILIZE, HATEMETHOD_ACCESSIBLE, HATEMETHOD_SHIELDPET, HATEMETHOD_LIONLOCKSTATE):
            oGame = self.m_Game
            oOwner = self.m_OwnerObj
            dHeroDis = self.GetHeroEnemyDis()
            dServantDis = oGame.Scene_GetTargetDisMap(oOwner.m_ID, list(dHeroDis), 1)
            iNowTarget = self.m_OwnerObj.Query('LockEnemy', 0)
            tHeroDisEff = oOwner.m_HateDisEff['HeroDisEff'] if 'HeroDisEff' in oOwner.m_HateDisEff else ()
            tServantDisEff = oOwner.m_HateDisEff['ServantDisEff'] if 'ServantDisEff' in oOwner.m_HateDisEff else ()
            fMaxHate = 0
            for iTarget, fHeroDis in dHeroDis.items():
                if fLimitHeroDis and fHeroDis > fLimitHeroDis:
                    if iTarget == iNowTarget:
                        self.SetLockEnemy(0)
                        continue
                oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTCHOOSETARGET)
                if not oTarget:
                    if iTarget == iNowTarget:
                        self.SetLockEnemy(0)
                        continue
                iFightType = oTarget.m_FightType
                dBaseHateConfig = oOwner.m_BaseHate
                if iFightType & WARRIOR_MONSTER:
                    if oTarget.m_DataSID in dBaseHateConfig:
                        iBaseHate = dBaseHateConfig[oTarget.m_DataSID]
                    elif iFightType in dBaseHateConfig['FightType']:
                        iBaseHate = dBaseHateConfig['FightType'][iFightType]
                    elif iFightType & MONSTER_TYPE_MASK in dBaseHateConfig['FightType']:
                        iBaseHate = dBaseHateConfig['FightType'][iFightType & MONSTER_TYPE_MASK]
                    else:
                        iBaseHate = dBaseHateConfig['Default']
                if iFightType in dBaseHateConfig['FightType']:
                    iBaseHate = dBaseHateConfig['FightType'][iFightType]
                else:
                    iBaseHate = dBaseHateConfig['Default']
                fHeroDisEff = self.GetDisEff(fHeroDis, tHeroDisEff)
                fServantDisEff = self.GetDisEff(dServantDis[iTarget], tServantDisEff)
                fHate = iBaseHate * fHeroDisEff * fServantDisEff
                dHateData[iTarget] = {
                    'Hate': [
                        fHate] }
                if fHate > fMaxHate:
                    fMaxHate = fHate
            
            if iHateMethod == HATEMETHOD_IMMOBILIZE:
                for iTarget, dHate in dHateData.items():
                    oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
                    if oTarget and oTarget.IsImmobilize():
                        dHate['Hate'][0] += fMaxHate
                
            elif iHateMethod == HATEMETHOD_ACCESSIBLE:
                vOwner = oOwner.GetPos()
                for iTarget, dHate in dHateData.items():
                    oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
                    if oTarget and oGame.Scene_IsDestPosAccessible(oOwner.m_Scene, vOwner, oTarget.GetPos()):
                        dHate['Hate'][0] += fMaxHate
                
            elif iHateMethod == HATEMETHOD_SHIELDPET:
                oHero = oOwner.GetOwner()
                if oHero:
                    vHero = oHero.GetPos()
                    vDir = oHero.GetFacing()
                    (iAngle, fRange, fHalfHeight, fHateFactor) = oOwner.Query('AddHateArgs', (0, 0, 0, 1))
                    dQArgs = {
                        'Mask': PXMASK_MONSTER,
                        'BlockMask': 0 }
                    lstTarget = oGame.Scene_GetSectorObjects(oOwner.m_Scene, vHero, vDir, fRange, fHalfHeight, iAngle, PXMASK_MONSTER, dQArgs)
                    for iTarget in lstTarget:
                        if iTarget not in dHateData:
                            continue
                        dHate = dHateData[iTarget]
                        dHate['Hate'][0] *= fHateFactor
                    
                elif iHateMethod == HATEMETHOD_LIONLOCKSTATE:
                    for iTarget, dHate in dHateData.items():
                        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
                        if not oTarget.m_State.GetItemBySID(LION_MONSTER_LOCK_STATE):
                            if oTarget.m_State.GetItemBySID(LION_MONSTER_ENHANCELOCK_STATE):
                                dHate['Hate'][0] += fMaxHate
                                continue
                    
            if not dHateData:
                self.SetCache('NoHate', 1)
                for iTarget in dHeroDis:
                    oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
                    if not oTarget:
                        continue
                    dHateData[iTarget] = {
                        'Hate': [
                            0] }
                
        self.SetData('HateData', dHateData)

    
    def HateAllMonster(oAgent):
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oAgent.m_OwnerObj.m_Scene)
        if not oScene:
            return BT_FAILURE
        lstTarget = oScene.GetObjectsByType('Monster')
        oAgent.SetCache('HateTarget', lstTarget)
        return BT_SUCCESS

    HateAllMonster = staticmethod(HateAllMonster)
    
    def HateRangeMonster(fLimitDis, oAgent):
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oAgent.m_OwnerObj.m_Scene)
        if not oScene:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        lstMonster = oScene.GetObjectsByType('Monster')
        dDis = oAgent.m_Game.Scene_GetTargetDisMap(oOwner.m_ID, lstMonster, 1)
        dTarget = { }
        for iMonster, fDis in dDis.items():
            if fDis <= fLimitDis:
                dTarget[iMonster] = 1
        
        oAgent.SetCache('HateTarget', dTarget)
        return BT_SUCCESS

    HateRangeMonster = staticmethod(HateRangeMonster)
    
    def HateAllTargetByType(bSummon, bProtege, oAgent):
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oAgent.m_OwnerObj.m_Scene)
        if not oScene:
            return BT_FAILURE
        dTarget = { }
        lstType = [
            'Monster',
            'Summon'] if bSummon else [
            'Monster']
        iSide = oAgent.m_OwnerObj.m_Side
        for iTarget in oScene.GetObjectsByTypes(lstType):
            oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
            if oTarget and oTarget.m_Side != iSide:
                dTarget[iTarget] = 1
        
        if bProtege:
            for iProtege in oScene.GetObjectsByType('Protege'):
                oProtege = oGame.GetObject(iProtege, PY_FLAG_SERVANTTARGET)
                if oProtege and oProtege.m_SID == 1169:
                    dTarget[iProtege] = 1
            
        oAgent.SetCache('HateTarget', dTarget)
        return BT_SUCCESS

    HateAllTargetByType = staticmethod(HateAllTargetByType)
    
    def ChooseEnemyBySceneObj(bSummon, bProtege, bCasting, oAgent):
        oGame = oAgent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oAgent.m_OwnerObj.m_Scene)
        dWeight = { }
        for iMonster in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_SERVANTTARGET)
            if not oMonster:
                continue
            if bCasting and not oMonster.GetAllCasting():
                continue
            dWeight[oMonster.m_ID] = 1
        
        if dWeight:
            iMonster = ChooseKey(oGame, dWeight)
            oAgent.SetLockEnemy(iMonster)
            return BT_SUCCESS
        if bSummon:
            iSide = oAgent.m_OwnerObj.m_Side
            for iSummon in oScene.GetObjectsByType('Summon'):
                oSummon = oGame.GetObject(iSummon, PY_FLAG_SERVANTTARGET)
                if not oSummon or oSummon.m_Side == iSide:
                    continue
                dWeight[oSummon.m_ID] = 1
            
            if dWeight:
                iSummon = ChooseKey(oGame, dWeight)
                oAgent.SetLockEnemy(iSummon)
                return BT_SUCCESS
        if bProtege:
            for iProtege in oScene.GetObjectsByType('Protege'):
                oProtege = oGame.GetObject(iProtege, PY_FLAG_SERVANTTARGET)
                if oProtege and oProtege.m_SID == 1169:
                    dWeight[oProtege.m_ID] = 1
            
            if dWeight:
                iProtege = ChooseKey(oGame, dWeight)
                oAgent.SetLockEnemy(iProtege)
                return BT_SUCCESS
        return BT_FAILURE

    ChooseEnemyBySceneObj = staticmethod(ChooseEnemyBySceneObj)
    
    def GetHateListCnt(oAgent):
        dHate = oAgent.GetData('HateData', { })
        oGame = oAgent.m_Game
        lstRemove = []
        for iTarget in dHate:
            if not oGame.GetObject(iTarget, PY_FLAG_DEAD):
                lstRemove.append(iTarget)
        
        if lstRemove:
            for iTarget in lstRemove:
                dHate.pop(iTarget)
            
        return len(dHate)

    GetHateListCnt = staticmethod(GetHateListCnt)
    
    def GetLockEnemyDis(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return 0
        return cl_math.CalDistance(oEnemy.GetPos(), oAgent.m_OwnerObj.GetPos())

    GetLockEnemyDis = staticmethod(GetLockEnemyDis)
    
    def GetLockEnemyHeightDis(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return 0
        vEnemy = oEnemy.GetPos()
        vPos = oAgent.m_OwnerObj.GetPos()
        return abs(vEnemy[1] + oEnemy.m_HeightOffset - vPos[1])

    GetLockEnemyHeightDis = staticmethod(GetLockEnemyHeightDis)
    
    def GetHeroDis(oAgent):
        oServant = oAgent.m_OwnerObj
        oHero = oServant.GetOwner()
        if not oHero:
            return 0
        return cl_math.CalDistance(oHero.GetPos(), oAgent.m_OwnerObj.GetPos())

    GetHeroDis = staticmethod(GetHeroDis)
    
    def NeedToRescue(oAgent):
        oOwner = oAgent.m_OwnerObj
        dRescueConfig = oOwner.Query('RescueConfig', { })
        if not dRescueConfig:
            return BT_FAILURE
        iPerform = oAgent.GetCurPerformSID()
        if iPerform and oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_FAILURE
        iLastRescueFrame = oAgent.GetData('LastRescueFrame', 0)
        iRescueCDFrame = dRescueConfig['RescueCDFrame']
        if iLastRescueFrame and iRescueCDFrame:
            iCurFrame = oAgent.m_Game.GetFrameNum()
            if iCurFrame < iLastRescueFrame + iRescueCDFrame:
                return BT_FAILURE
        oHero = oOwner.GetOwner()
        if not oHero or not oHero.IsDying():
            return BT_FAILURE
        oAgent.SetData('RescueTarget', oHero.m_ID)
        return BT_SUCCESS

    NeedToRescue = staticmethod(NeedToRescue)
    
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
        fGroundDis = oGame.Scene_GroundDistance(oOwner.m_Scene, (vTarget[0], vTarget[1] + 1.8, vTarget[2]), 5, PXMASK_MOVEBLK, oOwner.m_ID)
        vTarget = (vTarget[0], vTarget[1] + 1.8 - fGroundDis, vTarget[2])
        vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vTarget, (1, 0, 0), 1, 5, 0, 180)
        if not vPos:
            for _ in range(5):
                vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vTarget, (1, 0, 0), 1, 5, 0, 180)
                if vPos:
                    break
            else:
                return BT_FAILURE
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
    
    def RescueTarget(oAgent):
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
        if oRescueElement.IsRescuing(oOwner, iTarget):
            if not oRescueElement.CheckRescueDis(oOwner):
                return BT_FAILURE
            return BT_RUNNING
        iRet = oRescueElement.StartRescue(oOwner, iTarget)
        if iRet:
            return BT_RUNNING
        return BT_FAILURE

    RescueTarget = staticmethod(RescueTarget)
    
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
    
    def ChooseAttack(oAgent):
        oOwner = oAgent.m_OwnerObj
        iPerform = oOwner.m_AttPerform
        oPerform = oOwner.m_Perform.GetPerform(iPerform)
        if not oPerform or not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1) }
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChooseAttack = staticmethod(ChooseAttack)
    
    def ChooseCertainPF(iPerform, oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oOwner.m_Perform.GetPerform(iPerform)
        if not oPerform:
            return BT_FAILURE
        oPerform.DelCDTime(oOwner)
        if not oPerform.CanUse(oOwner, { }):
            return BT_FAILURE
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1) }
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChooseCertainPF = staticmethod(ChooseCertainPF)
    
    def ChoosePFByMonsterSkill(fHeightOffset, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        dCasting = { }
        for iActNum, dCast in oEnemy.GetAllCasting():
            dCasting[dCast['pfid']] = iActNum
        
        if not dCasting:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vEnemyPos = oEnemy.GetPos()
        vClone = None
        vFar = (vEnemyPos[0], vEnemyPos[1] + fHeightOffset, vEnemyPos[2])
        oGame = oAgent.m_Game
        iStatus = 0
        dPerform = { }
        if oOwner.m_Phase == 1 or 39211 in dCasting:
            oSkill = oGame.m_SkillMgr.GetSkill(oEnemy.m_ID, dCasting[39211])
            if oSkill:
                iStatus = oSkill.m_VarCache['status'] if 'status' in oSkill.m_VarCache else 0
                vDir = oSkill.m_Custom['vDir']
                vEnd = cl_math.Vec3DestPosDirPlane(vEnemyPos, vDir, 50, 0)
                vClone = (vEnd[0], vEnd[1] + fHeightOffset, vEnd[2])
            else:
                dPerform = {
                    7151: 1000,
                    7144: 1 }
                oAgent.SetData('vEnd', vFar)
        if not dPerform:
            if iStatus == 1:
                dPerform = {
                    7141: 1,
                    7142: 1000,
                    7148: 500 }
                if not vClone:
                    return BT_FAILURE
                oAgent.SetData('vEnd', vClone)
            else:
                dPerform = {
                    7150: 1000,
                    7143: 1 }
                oAgent.SetData('vEnd', vFar)
        iPerform = 0
        dWeight = { }
        for iPerform, iWeight in dPerform.items():
            oPerform = oOwner.m_Perform.GetPerform(iPerform)
            if not oPerform:
                continue
            if not oPerform.CanUse(oOwner, { }):
                continue
            dWeight[iPerform] = iWeight
        
        if not dWeight:
            return BT_FAILURE
        iPerform = ChooseKey(oGame, dWeight)
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1) }
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChoosePFByMonsterSkill = staticmethod(ChoosePFByMonsterSkill)
    
    def ChooseFarPFByServantPhase(oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        if oOwner.m_Phase == 1:
            dPerform = {
                7150: 1000,
                7143: 1 }
        else:
            dPerform = {
                7151: 1000,
                7144: 1 }
        dWeight = { }
        for iPerform, iWeight in dPerform.items():
            oPerform = oOwner.m_Perform.GetPerform(iPerform)
            if not oPerform:
                continue
            if not oPerform.CanUse(oOwner, { }):
                continue
            dWeight[iPerform] = iWeight
        
        if not dWeight:
            return BT_FAILURE
        iPerform = ChooseKey(oAgent.m_Game, dWeight)
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1) }
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChooseFarPFByServantPhase = staticmethod(ChooseFarPFByServantPhase)
    
    def ChoosePF(oAgent):
        if oAgent.m_PFAI:
            iType = MONSTER_PFAI_CATCH
            oEnemy = oAgent.GetLockEnemy()
            dExtra = { }
            if not oEnemy:
                oAgent.ChooseHateTarget(0, 0, oAgent)
                oEnemy = oAgent.GetLockEnemy()
                if not oEnemy:
                    return BT_FAILURE
            dExtra['Enemy'] = oEnemy
            oOwner = oAgent.m_OwnerObj
            dChosen = oAgent.m_PFAI.ChoosePFGroup(oOwner, iType, dExtra)
            if dChosen:
                oAgent.SetData('CurPFGroup', dChosen)
                for iPerform, iCntLower, iCntUpper, _ in dChosen.values():
                    dPerform = {
                        'pfid': iPerform,
                        'Multi': (iCntLower, iCntUpper) }
                    oAgent.SetData('CurChosenPF', dPerform)
                    oAgent.SetCurPerformDis()
                    return BT_SUCCESS
                
        return BT_FAILURE

    ChoosePF = staticmethod(ChoosePF)
    
    def ChoosePFByArgs(fReduceDis, oAgent):
        dChoosePF = oAgent.GetData('ChoosePF', { })
        if not dChoosePF:
            return BT_FAILURE
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        fDis = cl_math.CalDistance(oEnemy.GetPos(), oOwner.GetPos()) - fReduceDis
        if fDis < 0:
            fDis = 0
        dWeight = { }
        for (fMin, fMax), dTempPerform in dChoosePF.items():
            if fMin <= fDis and fDis <= fMax:
                for iPerform, iWeight in dTempPerform.items():
                    oPerform = oOwner.m_Perform.GetPerform(iPerform)
                    if not oPerform:
                        continue
                    if not oPerform.CanUse(oOwner, { }):
                        continue
                    dWeight[iPerform] = iWeight
                
        
        if not dWeight:
            return BT_FAILURE
        iPerform = ChooseKey(oAgent.m_Game, dWeight)
        dPerform = {
            'pfid': iPerform,
            'Multi': (1, 1) }
        oAgent.SetData('CurChosenPF', dPerform)
        oAgent.SetCurPerformDis()
        return BT_SUCCESS

    ChoosePFByArgs = staticmethod(ChoosePFByArgs)
    
    def Attack(iUseTarget, oAgent):
        oOwner = oAgent.m_OwnerObj
        oPerform = oAgent.GetCurPerform()
        if not oPerform:
            return BT_FAILURE
        iPerform = oPerform.m_SID
        if oOwner.CheckCastingAndBackSwingByPF(iPerform):
            return BT_RUNNING
        if oAgent.GetData('LastPerform', 0) == iPerform:
            oAgent.SetData('LastPerform', 0)
            oAgent.SetData('CurChosenPF', { })
            return BT_SUCCESS
        oTarget = None
        if iUseTarget:
            oTarget = oAgent.GetLockEnemy()
            if not oTarget:
                return BT_FAILURE
        vEnd = oAgent.GetData('vEnd', ())
        if not vEnd:
            vEnd = oTarget.GetPos() if oTarget else oOwner.GetPos()
        else:
            oAgent.SetData('vEnd', ())
        dData = {
            'VID': oTarget.m_ID if oTarget else 0,
            'vEnd': vEnd,
            'CastingEndFunc': Functor(SkillCastingEndFunc, oOwner, iPerform) }
        dPerform = oAgent.GetData('CurChosenPF', { })
        (iCntLower, iCntUpper) = dPerform['Multi']
        if iCntUpper > 1:
            iUseTimes = oAgent.m_Game.Random((iCntUpper - iCntLower) + 1) + iCntLower
        else:
            iUseTimes = 1
        dData['Custom'] = {
            'BallisticType': iUseTimes,
            'FromAI': True }
        if oOwner.m_FightType & WARRIOR_PET_HEROSIDE == WARRIOR_PET_HEROSIDE and oOwner.m_PetSkillInfo:
            dData['Custom'].update(oOwner.m_PetSkillInfo)
        if 'Custom' in dPerform:
            dData['Custom'].update(dPerform['Custom'])
        iRet = cl_war.UsePerform(oOwner, oPerform, dData)
        dPFRecord = oAgent.GetData('PFRecord', { })
        iOldTimes = dPFRecord[iPerform] if iPerform in dPFRecord else 0
        dPFRecord[iPerform] = iOldTimes + 1
        oAgent.SetData('PFRecord', dPFRecord)
        if iRet:
            if oOwner.CheckCastingAndBackSwingByPF(iPerform):
                oAgent.SetData('LastPerform', iPerform)
                return BT_RUNNING
            oAgent.SetData('CurChosenPF', { })
            return BT_SUCCESS
        return BT_FAILURE

    Attack = staticmethod(Attack)
    
    def UsePerformGroup(iUseTarget, oAgent):
        dChosen = oAgent.GetData('CurPFGroup')
        if not dChosen:
            return oAgent.Attack(iUseTarget, oAgent)
        oAgent.AddCurNodeEndFunc(UsePerformGroupEnd)
        iTotalCnt = oAgent.GetData('PFTotal', 0)
        if iTotalCnt == -1:
            return BT_SUCCESS
        if not iTotalCnt:
            iTotalCnt = len(dChosen)
            oAgent.SetData('PFTotal', iTotalCnt)
        DelayUsePFGroup(oAgent, iUseTarget, iTotalCnt)
        iUsedCnt = oAgent.GetData('PFUsed', 0)
        if iUsedCnt == -1:
            return BT_FAILURE
        if iUsedCnt >= iTotalCnt and not oAgent.m_OwnerObj.CheckCastingAndBackSwingByPF(oAgent.GetCurPerformSID()):
            return BT_SUCCESS
        return BT_RUNNING

    UsePerformGroup = staticmethod(UsePerformGroup)
    
    def SetCurPerformDis(self):
        oPerform = self.GetCurPerform()
        if not oPerform:
            self.SetData('CurPerformUseDis', 0)
            self.m_CurPerformUseHeight = 0
        else:
            self.SetData('CurPerformUseDis', oPerform.GetAttDistance())
            self.m_CurPerformUseHeight = oPerform.m_UseHeight

    
    def HaltPerform(oAgent):
        oOwner = oAgent.m_OwnerObj
        cl_action.HaltAllCasting(oOwner, 'BehaviorTree')
        oAgent.Remove_Call_Out('DelayUsePFGroup')
        oAgent.SetData('PFTotal', -1)
        oAgent.SetData('PFUsed', 0)
        oAgent.SetData('NextPFFrame', 0)
        return BT_SUCCESS

    HaltPerform = staticmethod(HaltPerform)
    
    def GetCurPerform(self):
        dPerform = self.GetData('CurChosenPF', { })
        if not dPerform:
            return None
        iPerform = dPerform['pfid']
        oPerform = self.m_OwnerObj.GetPerform(iPerform)
        return oPerform

    
    def GetCurPerformSID(self):
        dPerform = self.GetData('CurChosenPF', { })
        if not dPerform:
            return 0
        return dPerform['pfid']

    
    def GetChoosePF(oAgent):
        return oAgent.GetCurPerformSID()

    GetChoosePF = staticmethod(GetChoosePF)
    
    def IsPerformUseArea(bCalEnemyModel, oAgent):
        oEnemy = oAgent.GetLockEnemy()
        if not oEnemy:
            return False
        oOwner = oAgent.m_OwnerObj
        oPerform = oAgent.GetCurPerform()
        if not oPerform:
            return False
        vOwner = oOwner.GetPos()
        vTarget = oEnemy.GetPos()
        fPerformDis = oPerform.GetAttDistance()
        if bCalEnemyModel:
            fPerformDis += oEnemy.m_ModelRadius + oEnemy.m_ExtraModelDistance
        if cl_math.CheckDistance3D(vOwner, vTarget, fPerformDis):
            return True
        return False

    IsPerformUseArea = staticmethod(IsPerformUseArea)
    
    def ClearHateTarget(oAgent):
        oAgent.SetLockEnemy(0)
        return BT_SUCCESS

    ClearHateTarget = staticmethod(ClearHateTarget)
    
    def IsHeroCtrlUsePF(oAgent):
        dPerform = oAgent.GetData('HeroCtrlPF', { })
        if dPerform:
            oAgent.SetData('HeroCtrlPF', { })
            oOwner = oAgent.m_OwnerObj
            iPerform = dPerform['pfid']
            oPerform = oOwner.m_Perform.GetPerform(iPerform)
            if not oPerform:
                return BT_FAILURE
            oPerform.DelCDTime(oOwner)
            dPerform['Multi'] = (1, 1)
            oAgent.SetData('CurChosenPF', dPerform)
            oAgent.SetCurPerformDis()
            return BT_SUCCESS
        return BT_FAILURE

    IsHeroCtrlUsePF = staticmethod(IsHeroCtrlUsePF)
    
    def SendFightStatusMessage(iType, bStart, oAgent):
        dMsgInfo = {
            'Type': iType,
            'Frame': oAgent.m_Game.GetFrameNum() }
        if bStart:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SERVANT_FIGHT_START, oAgent.m_OwnerObj, dMsgInfo)
        else:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SERVANT_FIGHT_END, oAgent.m_OwnerObj, dMsgInfo)

    SendFightStatusMessage = staticmethod(SendFightStatusMessage)
    
    def CalFrameOwnerOutSight(iAngle, oAgent):
        oGame = oAgent.m_Game
        iCurFrame = oGame.GetFrameNum()
        iStartFrame = oAgent.GetData('StartOutSight', 0)
        oAgent.SetData('StartOutSight', iCurFrame)
        if not iStartFrame:
            return 0
        iOutSightFrame = oAgent.GetData('OutSightFrame', 0)
        oOwner = oAgent.m_OwnerObj
        oHero = oOwner.GetOwner()
        if not oHero:
            return iOutSightFrame
        vOwner = oOwner.GetPos()
        vHero = oHero.GetPos()
        vDir = cl_math.Vec3Minus(vOwner, vHero)
        vFace = oHero.GetFacing()
        if not cl_math.CheckVector2Angle(vDir, vFace, iAngle):
            return iOutSightFrame
        iTotalFrame = (iCurFrame - iStartFrame) + iOutSightFrame
        oAgent.SetData('OutSightFrame', iTotalFrame)
        return iTotalFrame

    CalFrameOwnerOutSight = staticmethod(CalFrameOwnerOutSight)
    
    def ClearTimeAtOwnerOutSight(oAgent):
        oAgent.SetData('StartOutSight', 0)
        oAgent.SetData('OutSightFrame', 0)
        return BT_SUCCESS

    ClearTimeAtOwnerOutSight = staticmethod(ClearTimeAtOwnerOutSight)
    
    def GetTargetInOwnerSightByDamage(iAngle, oAgent):
        if oAgent.GetData('StartAttentionFlag', 0):
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        oHero = oOwner.GetOwner()
        if not oHero:
            return BT_FAILURE
        cl_msgcenter.AddAttentionFunc(oOwner, oHero.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, Functor(OnGetTargetInOwnerSight, iAngle), 'EnemyInHeroSight')
        oAgent.SetData('StartAttentionFlag', 1)
        return BT_SUCCESS

    GetTargetInOwnerSightByDamage = staticmethod(GetTargetInOwnerSightByDamage)
    
    def RemoveOwnerSightDamageAttention(oAgent):
        oOwner = oAgent.m_OwnerObj
        oHero = oOwner.GetOwner()
        oAgent.SetData('StartAttentionFlag', 0)
        if not oHero:
            return BT_FAILURE
        cl_msgcenter.DoneAttention(oOwner, oHero.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, 'EnemyInHeroSight')
        return BT_SUCCESS

    RemoveOwnerSightDamageAttention = staticmethod(RemoveOwnerSightDamageAttention)
    
    def ChoosePosByOwnerSightTarget(fDis, iMinAngle, iMaxAngle, oAgent):
        iEnemy = oAgent.GetData('EnemyInHeroSight', 0)
        if not iEnemy:
            return BT_FAILURE
        oGame = oAgent.m_Game
        oEnemy = oGame.GetObject(iEnemy, PY_FLAG_DEAD)
        if not oEnemy:
            oAgent.SetData('EnemyInHeroSight', 0)
            return BT_FAILURE
        oOwner = oAgent.m_OwnerObj
        vOwner = oOwner.GetPos()
        vEnemy = oEnemy.GetPos()
        iRet = oGame.Scene_IsDestPosAccessible(oOwner.m_Scene, vOwner, vEnemy)
        if iRet:
            iNavRadius = oEnemy.m_MoveCtrl.m_NavRadius if oEnemy.m_MoveCtrl else 3
            (iSpaceRet, vPos) = oGame.Scene_GetSpace(oOwner.m_Scene, vEnemy)
            vPos = oGame.Scene_RandomPointSectorInMesh(oOwner.m_Scene, vEnemy, oOwner.GetFacing(), iNavRadius, iNavRadius + fDis, iMinAngle, iMaxAngle)
            if not iSpaceRet:
                oAgent.SetData('EnemyInHeroSight', 0)
                return BT_FAILURE
        (iDestRet, vPos) = oAgent.m_Game.Scene_GetAccessibleDestPos(oOwner.m_Scene, vOwner, vEnemy)
        if not iDestRet or abs(vPos[1] - vEnemy[1]) > 3:
            oAgent.SetData('EnemyInHeroSight', 0)
            return BT_FAILURE
        oAgent.SetData('ArrivePos', vPos)
        oAgent.SetData('EnemyInHeroSight', 0)
        return BT_SUCCESS

    ChoosePosByOwnerSightTarget = staticmethod(ChoosePosByOwnerSightTarget)
    
    def SetActionSM(iStatus, oAgent):
        oOwner = oAgent.m_OwnerObj
        oOwner.Set('CacheMoveStatus', iStatus)
        if oOwner.Query('ForceMoveStatus'):
            return BT_SUCCESS
        oOwner.m_MoveStatusMgr.ChangeStatus(oOwner, iStatus)
        return BT_SUCCESS

    SetActionSM = staticmethod(SetActionSM)
    
    def SetFightStatus(iStatus, oAgent):
        oOwner = oAgent.m_OwnerObj
        if oOwner.Query('FightStatusFlag'):
            oOwner.m_FightStatusMgr.ChangeStatus(oOwner, iStatus)
        return BT_SUCCESS

    SetFightStatus = staticmethod(SetFightStatus)
    
    def SetActionSMArgs(iType, sArgsName, sArgsValue, oAgent):
        if iType == 1:
            fArgsValue = 0
        elif iType == 2:
            if not sArgsValue:
                return BT_FAILURE
            if sArgsValue.lower() in ('true', '1'):
                fArgsValue = 1
            else:
                fArgsValue = 0
        elif iType == 3:
            if not sArgsValue:
                return BT_FAILURE
            fArgsValue = round(float(sArgsValue), 2)
        else:
            return BT_FAILURE
        cl_snetwar.GS2CMonsterActionSM(oAgent.m_OwnerObj, iType, sArgsName, fArgsValue)
        return BT_SUCCESS

    SetActionSMArgs = staticmethod(SetActionSMArgs)


def DelayUsePFGroup(oAgent, iUseTarget, iTotalCnt):
    if not oAgent.IsActive():
        oAgent.SetData('PFUsed', -1)
        return None
    iUsedCnt = oAgent.GetData('PFUsed', 0)
    if iUsedCnt >= iTotalCnt:
        return None
    iCurFrame = oAgent.m_Game.GetFrameNum()
    if iUsedCnt >= 1:
        iNextPFFrame = oAgent.GetData('NextPFFrame', 0)
        if iNextPFFrame:
            if iNextPFFrame <= iCurFrame:
                oAgent.SetData('NextPFFrame', 0)
                dPFGroup = oAgent.GetData('CurPFGroup')
                (iPerform, iCntLower, iCntUpper, _) = dPFGroup[iUsedCnt]
                dPerform = {
                    'pfid': iPerform,
                    'Multi': (iCntLower, iCntUpper),
                    'Type': oAgent.GetData('CurPFGroupType') }
                oAgent.SetData('CurChosenPF', dPerform)
                pfobj = oAgent.GetCurPerform()
                if not pfobj:
                    oAgent.SetData('PFUsed', -1)
                    return None
                pfobj.DelCDTime(oAgent.m_OwnerObj)
            else:
                return None
    iRet = CAgent.Attack(iUseTarget, oAgent)
    if iRet == BT_FAILURE:
        oAgent.SetData('PFUsed', -1)
        return None
    if iRet == BT_SUCCESS:
        iUsedCnt += 1
        oAgent.SetData('PFUsed', iUsedCnt)
        if iUsedCnt >= iTotalCnt:
            return None
        dPFGroup = oAgent.GetData('CurPFGroup')
        if iUsedCnt not in dPFGroup:
            oCurrentBT = oAgent.PYGetCurrentBT()
            if oCurrentBT:
                sInfo = oCurrentBT.GetPathName()
                BehaviorLog.Alert('%s err used cnt %s %s %s' % (sInfo, iUsedCnt, iTotalCnt, dPFGroup))
        (_, _, _, iDelayFrame) = dPFGroup[iUsedCnt]
        oAgent.Remove_Call_Out('DelayUsePFGroup')
        if iDelayFrame:
            oAgent.SetData('NextPFFrame', iCurFrame + iDelayFrame)
            oAgent.Call_Out(Functor(DelayUsePFGroup, oAgent, iUseTarget, iTotalCnt), iDelayFrame, 'DelayUsePFGroup')
        else:
            oAgent.SetData('NextPFFrame', 1)
            DelayUsePFGroup(oAgent, iUseTarget, iTotalCnt)

