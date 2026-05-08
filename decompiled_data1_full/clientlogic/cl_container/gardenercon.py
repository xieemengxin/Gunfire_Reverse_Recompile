# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/gardenercon.pyc
# RelativePath: clientlogic/cl_container/gardenercon.pyc
# Source Generated with Decompyle++
# File: gardenercon.pyc (Python 3.6)

from cl_only import WeakProxy, Time2Frame, PY_FLAG_DEAD
from cl_commondefines import SETPHASE_PLANT, GARDENER_SEED, CREATE_SEED, REMOVE_SEED, CREATE_PLANT, REMOVE_PLANT, BEFORE_SEED_SHOOT, TRIGGER_SEED_SHOOT, SIDE_TYPE_HERO, STATE_TIME_FOREVER, ADD_PARASITIC
from cl_commondefines import GARDENER_THROW, GARDENER_THROW_TYPE_JAR, WARRIOR_PLANT, GARDENER_THROW_TYPE_NORMAL, GARDENER_CAREER, GARDENER_PARASITIC_STATE, GARDENER_PARASITIC, MODEL_TYPE_SPHERE
from cl_commondefines import PICK_SEED, FUNCMODE_TYPE_GARDENERPICKSEED, PATHMODE_STAYSTATUS, GARDENER_BARRIER_SUMMON, WARRIOR_MONSTER, HATCH_SEED, PLANT_SELECTCREATEPOS_POINTSECTOR, PLANT_SELECTCREATEPOS_POLYGON
from cl_commondefines import GARDENER_PLANT_SID, PLANT_PHASE_NORMAL, GARDENER_CANAIM_STATE, FUNCMODE_TYPE_AIMCORRISIONMONSTER, ABNORAML_CORRISION, OBJ_ENEMY, CHECKAIM_STATE_CANAIM, CHECKAIM_STATE_NOTCONFING
from cl_commondefines import CHECKAIM_STATE_NOTAIMOBJ, CHECKAIM_STATE_AIMMONSTERERR, CHECKAIM_STATE_AIMPLANTERR, CHECKAIM_STATE_AIMERRSIDE, PLANT_PHASE_ANGRY, PLANT_PHASE_TREE, GARDENER_AREA
from cl_commondefines import PAMOD_TYPE_DYNA, MODEL_TYPE_BOX
from cl_pxlayer import PXLAYER_BARRIER
from cl_platformdata import CheckValidGardenerAim, GetServantConfig
from cl_abnormalconf import GetAbnormalState
from cl_pxlayer import PXMASK_GROUNDBLK
from cl_object.logging import GardenerLog
import cl_modeldefine
import cl_msgcenter
import cl_snetwar
import cl_math
import cl_state
import cl_object
import cl_war
SEED_SHAPE = 1102

class CGardenerContainer(object):
    m_MaxGroundDis = 10
    m_CollisionFactor = 1
    m_ClearPlantPriority = {
        PLANT_PHASE_TREE: 1,
        PLANT_PHASE_ANGRY: 2,
        PLANT_PHASE_NORMAL: 3 }
    m_BossLevelPos = {
        1101009: {
            'RangeType': PLANT_SELECTCREATEPOS_POLYGON,
            'ListPos': [
                (10.8, 0, 18.4),
                (10.8, 0, 3.2),
                (-24.7, 0, 2.6),
                (-25.1, 0, 17.8)] },
        1301002: {
            'RangeType': PLANT_SELECTCREATEPOS_POLYGON,
            'ListPos': [
                (56.6, 3.4, 29.8),
                (55.1, 3.4, 19.2),
                (10.2, 3.4, 20.5),
                (12.2, 3.4, 36.1)] },
        1301003: {
            'RangeType': PLANT_SELECTCREATEPOS_POLYGON,
            'ListPos': [
                (51.5, 3.4, 18.8),
                (52.7, 3.4, 8.3),
                (14.9, 3.4, 10.8),
                (16.4, 3.4, 21.5)] },
        1403003: {
            'RangeType': PLANT_SELECTCREATEPOS_POINTSECTOR,
            'BossPos': (0, 0.2, 0),
            'GroundHeight': 0.2,
            'InnerRadius': 0,
            'OuterRadius': 10,
            'StartAngle': 1,
            'EndAngle': 90 },
        1403004: {
            'RangeType': PLANT_SELECTCREATEPOS_POINTSECTOR,
            'BossPos': (0, 0.2, 0),
            'GroundHeight': 0.2,
            'InnerRadius': 0,
            'OuterRadius': 10,
            'StartAngle': 1,
            'EndAngle': 90 } }
    m_CallFlag = 'CGardenerContainer'
    m_PickMistake = 1
    
    def __init__(self, oGame, oWarrior, dCustomConArgs):
        self.m_Game = oGame
        self.m_WarriorObj = WeakProxy(oWarrior)
        self.m_PlantDict = { }
        self.m_PlantMax = 8
        self.m_SeedDict = { }
        self.m_SeedMax = dCustomConArgs['SeedMax'] if 'SeedMax' in dCustomConArgs else 0
        self.m_SeedLifeFrame = Time2Frame(dCustomConArgs['SeedTime']) if 'SeedTime' in dCustomConArgs else 0
        self.m_AreaEffectInfo = {
            'AreaEffectID': 0,
            'AreaEffectShape': 0,
            'EffectStart': (0, 0, 0),
            'EffectScale': (0, 0, 0) }
        self.m_ThrowInfo = { }
        self.m_DomainBarrier = 0
        self.m_FieldSeedInfo = { }
        self.m_AimJar = { }
        self.InitPlantModelInfo()
        self.InitEvent()

    
    def InitPlantModelInfo(self):
        self.m_PlantModelRadius = 0
        oGame = self.m_Game
        clsPlantData = GetServantConfig(GARDENER_PLANT_SID)
        if not clsPlantData:
            GardenerLog.Alert('%s %s not exit cls plant' % (oGame.m_ID, self.m_WarriorObj.m_PlayerID))
            return None
        tModel = cl_modeldefine.GetModelDefine(clsPlantData.m_Shape, 'Physx')
        if not tModel:
            GardenerLog.Alert('%s %s not exit model: %s plant' % (oGame.m_ID, self.m_WarriorObj.m_PlayerID, clsPlantData.m_Shape))
            return None
        self.m_PlantModelRadius = tModel[0]

    
    def InitEvent(self):
        oHero = self.m_WarriorObj
        sCallFlag = self.m_CallFlag
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_USE_THROWPF, self.OnUseThrowPf, sCallFlag, iOnce = 0, iPriority = -1)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OnLeaveScene, sCallFlag, iOnce = 0, iPriority = -1)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_DIE, self.OnHeroDie, sCallFlag, iOnce = 0, iPriority = -1)
        cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_PLAYERONREADY, self.OnPlayerReady, sCallFlag, iOnce = 0, iPriority = -1)

    
    def ReleaseEvent(self):
        oHero = self.m_WarriorObj
        sCallFlag = self.m_CallFlag
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_USE_THROWPF, sCallFlag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_LEAVESCENE, sCallFlag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_DIE, sCallFlag)
        cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_PLAYERONREADY, sCallFlag)

    
    def Release(self):
        self.ReleaseEvent()
        for oPlant in list(self.m_PlantDict.values()):
            oPlant.Remove('GardenerRelease')
        
        self.m_PlantDict = { }
        for iSeed in list(self.m_SeedDict):
            self.RemoveSeed(iSeed, 'Release')
        
        self.ClearDomainBarrierSummon(iDelayRemove = 0)
        self.RemoveAimJar()
        self.m_SeedDict = { }
        self.m_FieldSeedInfo = { }
        self.m_WarriorObj = None
        self.m_Game = None

    
    def CreatePlant(self, vPos, iPhase, iCheckPos, sReason, fDetectArea = 0, fCollisionFactor = m_CollisionFactor, iGrade = 1, iInitHPRatio = 0):
        oGame = self.m_Game
        if not len(self.m_PlantDict) >= self.m_PlantMax and self.ClearOnePlant('plantmax'):
            lstPlantInfo = []
            for oPlant in self.m_PlantDict.values():
                if not oPlant:
                    continue
                lstPlantInfo.append((oPlant.IsDead(), oPlant.HP(), oPlant.Phase()))
            
            GardenerLog.Alert('%s %s plantmax err %s %s %s' % (oGame.m_ID, self.m_WarriorObj.m_PlayerID, sReason, len(self.m_PlantDict), lstPlantInfo))
            return None
        (bRet, vPos) = self.GetPlantCreatePos(vPos, iCheckPos, fDetectArea, fCollisionFactor, sReason)
        if not bRet:
            return None
        oOwner = self.m_WarriorObj
        dAddData = {
            'Owner': oOwner.m_ID,
            'Phase': iPhase,
            'Grade': iGrade,
            'Reason': sReason }
        if iInitHPRatio:
            dAddData['InitHPRatio'] = iInitHPRatio
        iScene = oOwner.m_Scene
        oPlant = oGame.m_ResMgr.CreateServant(iScene, GARDENER_PLANT_SID, dAddData)
        if not oPlant:
            GardenerLog.Alert('%d %d createplanterr %s %s' % (oGame.m_ID, self.m_WarriorObj.m_PlayerID, GARDENER_PLANT_SID, sReason))
            return None
        self.m_PlantDict[oPlant.m_ID] = oPlant
        oPlant.Goto(iScene, vPos)
        oPlant.m_MoveCtrl.SetPathMode('PlantStayStatus', PATHMODE_STAYSTATUS)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, oOwner, {
            'VID': oPlant.m_ID,
            'Reason': sReason,
            'PlanPhase': oPlant.Phase() }, iSub = CREATE_PLANT)
        return oPlant

    
    def SetPlantPhase(self, iPlant, iPhase):
        if iPlant not in self.m_PlantDict:
            return None
        oPlant = self.m_PlantDict[iPlant]
        if iPhase == oPlant.Phase():
            return None
        oPlant.SetPhase(iPhase)
        oPlant.OnSetPlantPhase()
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, self.m_WarriorObj, {
            'VID': oPlant.m_ID,
            'PlanPhase': oPlant.Phase() }, iSub = SETPHASE_PLANT)

    
    def GetPlantCreatePos(self, vCreatePos, iCheckPos, fDetectArea, fCollisionFactor, sReason):
        oGame = self.m_Game
        if iCheckPos:
            vCreatePos = self.GetPosInGround(vCreatePos)
            if not vCreatePos:
                return (False, (0, 0, 0))
        iScene = self.m_WarriorObj.m_Scene
        (iGetSpaceRet, vCreatePos) = oGame.Scene_GetSpace(iScene, vCreatePos)
        if iGetSpaceRet:
            if fDetectArea <= 0:
                fDetectArea = self.m_PlantModelRadius
            if fCollisionFactor <= 0:
                fCollisionFactor = self.m_CollisionFactor
            (iRet, vAroundPos) = oGame.Scene_GetAroundUnoccupiedPos(iScene, vCreatePos, fDetectArea, fCollisionFactor)
            if iRet:
                vCreatePos = vAroundPos
        return (True, vCreatePos)

    
    def RemovePlant(self, iPlant, sReason):
        if iPlant not in self.m_PlantDict:
            return None
        self.m_PlantDict.pop(iPlant)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_PLANT, self.m_WarriorObj, {
            'VID': iPlant,
            'Reason': sReason }, iSub = REMOVE_PLANT)

    
    def GetPosInGround(self, vPos):
        oGame = self.m_Game
        iScene = self.m_WarriorObj.m_Scene
        vPos = (vPos[0], vPos[1] + 0.1, vPos[2])
        fGroundDis = oGame.Scene_GroundDistance(iScene, vPos, self.m_MaxGroundDis, PXMASK_GROUNDBLK)
        if fGroundDis >= self.m_MaxGroundDis:
            return None
        return (vPos[0], vPos[1] - fGroundDis, vPos[2])

    
    def CreateSeed(self, vPos, sReason, iCheckPos, iNum):
        oOwner = self.m_WarriorObj
        oGame = self.m_Game
        if iNum <= 0:
            GardenerLog.Alert('%d %d createseed fail not num %s %s %s' % (oGame.m_ID, oOwner.m_PlayerID, vPos, iNum, sReason))
            return False
        vTargetPos = self.GetPosInGround(vPos) if iCheckPos else vPos
        if not vTargetPos:
            return False
        iNeedRemove = len(self.m_SeedDict) + iNum - self.m_SeedMax
        if iNeedRemove > 0:
            for _ in range(iNeedRemove):
                for iSeed in self.m_SeedDict:
                    self.RemoveSeed(iSeed, 'NumLimit')
                
            
        (iRadius, _) = cl_modeldefine.GetModelDefine(SEED_SHAPE, 'Physx')
        dAddInfo = {
            'Owner': oOwner.m_ID,
            'Origin': vTargetPos,
            'Side': SIDE_TYPE_HERO,
            'Shape': MODEL_TYPE_SPHERE,
            'Angle': (0, 0, 0),
            'Center': (0, 0, 0),
            'Scale': (1, 1, 1),
            'Size': (iRadius, 0, 0) }
        for _ in range(iNum):
            oSeed = oGame.m_ResMgr.CreateSummon(oOwner.m_Scene, GARDENER_SEED, dAddInfo)
            if not oSeed:
                GardenerLog.Alert('%d %d createseed fail not seed %s %s %s' % (oGame.m_ID, oOwner.m_PlayerID, vPos, vTargetPos, sReason))
                return False
            self.m_SeedDict[oSeed.m_ID] = oSeed
            oSeed.m_RemoveAction = self.OnRemoveSeed
            oSeed.SetLifeFrame(self.m_SeedLifeFrame)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, oOwner, {
                'SeedID': oSeed.m_ID }, iSub = CREATE_SEED)
        
        return True

    
    def CheckUseBossLevelCreatePos(self, iLevel):
        if iLevel in self.m_BossLevelPos:
            return 1
        return 0

    
    def GetBossLevelAutoCreatePos(self, iLevel):
        if iLevel not in self.m_BossLevelPos:
            return (False, (0, 0, 0))
        oGame = self.m_Game
        oHero = self.m_WarriorObj
        iScene = oHero.m_Scene
        dBossPosInfo = self.m_BossLevelPos[iLevel]
        iRangeType = dBossPosInfo['RangeType']
        if iRangeType == PLANT_SELECTCREATEPOS_POLYGON:
            vRandomPos = oGame.Scene_RandomPointPolyInMesh(iScene, dBossPosInfo['ListPos'])
            if not vRandomPos:
                return (False, (0, 0, 0))
            return (True, vRandomPos)
        if iRangeType == PLANT_SELECTCREATEPOS_POINTSECTOR:
            (fHeroX, _, fHeroZ) = oHero.GetPos()
            vPos = (fHeroX, dBossPosInfo['GroundHeight'], fHeroZ)
            (ret, vPos) = oGame.Scene_GetSpace(iScene, vPos)
            if not ret:
                return (False, (0, 0, 0))
            vFace = cl_math.Vec3Minus(dBossPosInfo['BossPos'], vPos)
            vRandomPos = oGame.Scene_RandomPointSectorInMesh(iScene, vPos, vFace, dBossPosInfo['InnerRadius'], dBossPosInfo['OuterRadius'], dBossPosInfo['StartAngle'], dBossPosInfo['EndAngle'])
            if not vRandomPos:
                return (True, vPos)
            return (True, vRandomPos)

    
    def PickSeed(self, iSeed):
        oHero = self.m_WarriorObj
        if not oHero.GetFuncModeTimes(FUNCMODE_TYPE_GARDENERPICKSEED):
            GardenerLog.Debug('%s %s getfuncmode err: %s' % (self.m_Game.m_ID, oHero.m_PlayerID, FUNCMODE_TYPE_GARDENERPICKSEED))
            return None
        if iSeed not in self.m_SeedDict:
            GardenerLog.Debug('%s %s no seed: %s %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iSeed, self.m_SeedDict))
            return None
        vPos = self.m_SeedDict[iSeed].GetPos()
        vHeroPos = oHero.GetPos()
        iPickRange = oHero.GetFunModeInfo(FUNCMODE_TYPE_GARDENERPICKSEED, 'PickRange')
        if cl_math.CalDistance3D(vPos, vHeroPos) > iPickRange + self.m_PickMistake:
            GardenerLog.Debug('%s %s over range: %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iPickRange))
            return None
        oHero.CostFuncModeTimes(FUNCMODE_TYPE_GARDENERPICKSEED, 1)
        self.RemoveSeed(iSeed, 'PickSeed', iDelayFrame = 25)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, self.m_WarriorObj, {
            'PickSeedNum': 1 }, iSub = PICK_SEED)

    
    def RemoveSeed(self, iSeed, sReason, iDelayFrame = 0):
        if iSeed not in self.m_SeedDict:
            return None
        if iSeed in self.m_FieldSeedInfo:
            self.m_FieldSeedInfo.pop(iSeed)
        if not iDelayFrame:
            self.m_SeedDict[iSeed].Remove(sReason)
        else:
            self.m_SeedDict[iSeed].RemoveOnlyServer(sReason, iDelayFrame)

    
    def UpdateFieldSeedInfo(self, iSeed):
        self.m_FieldSeedInfo[iSeed] = 1

    
    def ClearFieldSeedInfo(self):
        self.m_FieldSeedInfo = { }

    
    def GetFieldSeedInfo(self):
        return self.m_FieldSeedInfo

    
    def OnRemoveSeed(self, oSeed):
        self.m_SeedDict.pop(oSeed.m_ID)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, self.m_WarriorObj, { }, iSub = REMOVE_SEED)

    
    def HatchSeed(self, iSeed, sReason, iPlantPhase = PLANT_PHASE_NORMAL):
        if iSeed not in self.m_SeedDict:
            return None
        oSeed = self.m_SeedDict[iSeed]
        vSeedPos = oSeed.GetPos()
        sReason = 'HatchSeed-%s' % sReason
        self.RemoveSeed(iSeed, sReason)
        oPlant = self.CreatePlant(vSeedPos, iPlantPhase, iCheckPos = 0, sReason = sReason)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, self.m_WarriorObj, { }, iSub = HATCH_SEED)
        return oPlant

    
    def GetRandomSeedID(self):
        if not self.m_SeedDict:
            return 0
        lstSeed = list(self.m_SeedDict)
        iRandom = self.m_Game.Random(len(lstSeed))
        return lstSeed[iRandom]

    
    def ClearAllPlant(self, sReason):
        for oPlant in list(self.m_PlantDict.values()):
            oPlant.ExecuteSelf(sReason)
        

    
    def ClearOnePlant(self, sReason):
        iMinHp = 999999
        iMinPriority = 0
        iClearPlant = 0
        for iPlant, oPlant in self.m_PlantDict.items():
            iPhase = oPlant.Phase()
            iHP = oPlant.HP()
            iPriority = self.m_ClearPlantPriority[iPhase]
            if not iPriority > iMinPriority:
                if iPriority == iMinPriority and iHP < iMinHp:
                    iMinPriority = iPriority
                    iMinHp = iHP
                    iClearPlant = iPlant
                    continue
        
        if not iClearPlant:
            return 0
        oClearPlant = self.m_PlantDict[iClearPlant]
        oClearPlant.ExecuteSelf(sReason)
        if oClearPlant.IsDead():
            return 1
        return 0

    
    def ClearTargetPlant(self, iPlant, sReason):
        if iPlant not in self.m_PlantDict:
            return None
        oClearPlant = self.m_PlantDict[iPlant]
        oClearPlant.ExecuteSelf(sReason)

    
    def ClearAllSeed(self, sReason):
        for iSeed in list(self.m_SeedDict):
            self.RemoveSeed(iSeed, sReason)
        

    
    def TriggerSeedShoot(self, vPos, iCheckPos, sReason):
        oOwner = self.m_WarriorObj
        dInfo = { }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, oOwner, dInfo, iSub = BEFORE_SEED_SHOOT)
        iSeedNum = 1
        if 'DoubleSeed' in dInfo:
            iSeedNum *= 2
        self.CreateSeed(vPos, sReason, iCheckPos, iSeedNum)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GARDENER_OPERATION_SEED, oOwner, dInfo, iSub = TRIGGER_SEED_SHOOT)

    
    def GetPlant(self, iPlant, iPlantPhase = 0):
        if iPlant not in self.m_PlantDict:
            return None
        oPlant = self.m_PlantDict[iPlant]
        if not iPlantPhase:
            return oPlant
        if oPlant.Phase() == iPlantPhase:
            return oPlant

    
    def GetNearestSeed(self, vPos):
        if not self.m_SeedDict:
            return None
        fMinDis = 999
        oNearestSeed = None
        for oSeed in self.m_SeedDict.values():
            fDis = cl_math.CalDistance3D(vPos, oSeed.GetPos())
            if fDis < fMinDis:
                fMinDis = fDis
                oNearestSeed = oSeed
        
        return oNearestSeed

    
    def CheckValidGardenerAim(self, iTarget):
        oGame = self.m_Game
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            return CHECKAIM_STATE_NOTAIMOBJ
        if not (oTarget.m_Scene) and not oTarget.Query('Aiming'):
            return CHECKAIM_STATE_NOTAIMOBJ
        iShape = oTarget.m_Shape
        oHero = self.m_WarriorObj
        iHero = oHero.m_ID
        if not CheckValidGardenerAim(iShape):
            return CHECKAIM_STATE_NOTCONFING
        iFightType = oTarget.m_FightType
        if iFightType & WARRIOR_PLANT != WARRIOR_PLANT:
            if not cl_math.CheckTargetType(self.m_Game, oTarget, iHero, SIDE_TYPE_HERO, OBJ_ENEMY):
                return CHECKAIM_STATE_AIMERRSIDE
            if iFightType & WARRIOR_MONSTER and not self.CheckAimMonster(oTarget):
                return CHECKAIM_STATE_AIMMONSTERERR
        if not self.CheckAimPlant(oTarget):
            return CHECKAIM_STATE_AIMPLANTERR
        return CHECKAIM_STATE_CANAIM

    
    def CheckAimMonster(self, oMonster):
        oStateCon = oMonster.m_State
        oHero = self.m_WarriorObj
        iHeroID = oHero.m_ID
        if oStateCon.GetItemBySource(GARDENER_CANAIM_STATE, iHeroID) or oMonster.Query('CommonMonsterFly'):
            return 1
        if oHero.GetFuncModeTimes(FUNCMODE_TYPE_AIMCORRISIONMONSTER) and oStateCon.GetItemBySID(GetAbnormalState(ABNORAML_CORRISION)):
            return 1
        return 0

    
    def CheckAimPlant(self, oPlant):
        if not self.GetPlant(oPlant.m_ID):
            return 0
        return 1

    
    def SetThrowInfo(self, iAimTarget, iThrowType, dInfo):
        if not iAimTarget:
            return None
        self.m_ThrowInfo[iAimTarget] = {
            'ThrowType': iThrowType,
            'CustomData': dInfo }

    
    def GetThrowType(self, iAimTarget):
        if iAimTarget not in self.m_ThrowInfo:
            return GARDENER_THROW_TYPE_NORMAL
        if 'ThrowType' not in self.m_ThrowInfo[iAimTarget]:
            return GARDENER_THROW_TYPE_NORMAL
        return self.m_ThrowInfo[iAimTarget]['ThrowType']

    
    def GetThrowInfo(self, iAimTarget):
        if iAimTarget not in self.m_ThrowInfo:
            return { }
        if 'CustomData' not in self.m_ThrowInfo[iAimTarget]:
            return { }
        return self.m_ThrowInfo[iAimTarget]['CustomData']

    
    def ClearThrowInfo(self, iAimTarget):
        if iAimTarget not in self.m_ThrowInfo:
            return None
        self.m_ThrowInfo.pop(iAimTarget)

    
    def StartThrowPF(self, iAimTarget, iThrowType, dInfo):
        self.SetThrowInfo(iAimTarget, iThrowType, dInfo)
        oPerform = self.m_WarriorObj.GetPerform(GARDENER_THROW)
        dStartSkillInfo = {
            'ThrowType': iThrowType,
            'Shape': dInfo['Shape'] if 'Shape' in dInfo else 0,
            'ExtraMonsterBoom': oPerform.GetArgValue('ExtraMonsterBoom'),
            'AimTarget': iAimTarget }
        cl_snetwar.GS2CNotifyStartSkill(self.m_Game, self.m_WarriorObj.m_PlayerID, GARDENER_THROW, oPerform.m_ID, 0, dStartSkillInfo)

    
    def OnUseThrowPf(self, oHero, dMsgInfo):
        if oHero.m_Agent:
            return None
        oSkill = dMsgInfo['Skill']
        if not oSkill.m_Base['pfid'] == GARDENER_THROW:
            return None
        dSkillCustom = oSkill.m_Custom
        iAimTarget = dSkillCustom['AimTarget'] if 'AimTarget' in dSkillCustom else 0
        iThrowType = dSkillCustom['ThrowType'] if 'ThrowType' in dSkillCustom else GARDENER_THROW_TYPE_NORMAL
        if iThrowType != self.GetThrowType(iAimTarget):
            GardenerLog.Alert('%d %d use err throwtype %s %s' % (self.m_Game.m_ID, self.m_WarriorObj.m_PlayerID, iThrowType, self.GetThrowType(iAimTarget)))
            self.ClearThrowInfo(iAimTarget)
            return None
        dSkillCustom.update(self.GetThrowInfo(iAimTarget))
        if iThrowType == GARDENER_THROW_TYPE_JAR:
            dSkillCustom['CanReward'] = 1
        self.ClearThrowInfo(iAimTarget)

    
    def StartCareerPF(self, vPos):
        (x, y, z) = vPos
        dInfo = {
            'x': int(x * 100),
            'y': int(y * 100),
            'z': int(z * 100) }
        oPerform = self.m_WarriorObj.GetPerform(GARDENER_CAREER)
        cl_snetwar.GS2CNotifyStartSkill(self.m_Game, self.m_WarriorObj.m_PlayerID, GARDENER_CAREER, oPerform.m_ID, 0, dInfo)

    
    def AddParasiticState(self, iTarget, sReason, iCount = 0):
        oTarget = self.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if (not oTarget or oTarget.Query('Petrified', 0) or not (oTarget.m_FightType & WARRIOR_MONSTER)) and not oTarget.Query('SpecialParasiticTarget', 0):
            return None
        oHero = self.m_WarriorObj
        if not iCount:
            oPerform = oHero.GetPerform(GARDENER_THROW)
            if not oPerform:
                return None
            iCount = oPerform.CalAttr('DamInterval')
        oEntityParasiticState = None
        oEntity = None
        iEntityCount = 0
        oParasiticState = self.TryAddTargetParasiticState(oTarget, sReason)
        if not oParasiticState:
            return None
        if oTarget.m_FightType & WARRIOR_MONSTER and oTarget.m_DataSID in frozenset({3921, 3906}):
            oEntity = oTarget.GetOwner()
            if not oEntity:
                return None
            oEntityParasiticState = self.TryAddTargetParasiticState(oEntity, sReason)
            if not oEntityParasiticState:
                return None
            if 'EntityAdd' not in sReason and not oEntityParasiticState.GetCount():
                iEntityCount = oEntityParasiticState.GetCount()
        dInfo = {
            'VID': iTarget,
            'AddCount': iCount,
            'Reason': sReason }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PARASITIC, oHero, dInfo, iSub = ADD_PARASITIC)
        if oParasiticState.m_LifeCycle:
            oParasiticState.AddCount(oTarget, dInfo['AddCount'] + iEntityCount)
        if oEntity and oEntityParasiticState and not oEntity.IsDead() and 'EntityAdd' not in sReason:
            oEntityParasiticState.AddCount(oEntity, dInfo['AddCount'])

    
    def TryAddTargetParasiticState(self, oTarget, sReason):
        oHero = self.m_WarriorObj
        iHeroID = oHero.m_ID
        oParasiticState = oTarget.m_State.GetItemBySource(GARDENER_PARASITIC_STATE, iHeroID)
        if oParasiticState:
            return oParasiticState
        oPerform = oHero.GetPerform(GARDENER_THROW)
        if not oPerform:
            return None
        dData = {
            'AID': iHeroID,
            'RS': cl_object.reason.CStrReason(sReason),
            'arg': {
                'MaxStateCount': oPerform.CalAttr('CommonMaxCount'),
                'StateTriggerInterval': oPerform.GetArgValue('StateTriggerInterval'),
                'NotReduceRatio': oPerform.GetArgValue('NotReduceRatio'),
                'Spread': oPerform.GetArgValue('Spread'),
                'AddCanAimMonsterState': oPerform.GetArgValue('AddCanAimMonsterState') } }
        oParasiticState = cl_state.AddState(oTarget, GARDENER_PARASITIC_STATE, STATE_TIME_FOREVER, iTime = 0, dState = dData)
        if not oParasiticState:
            return None
        oParasiticState.Enable(oTarget)
        return oParasiticState

    
    def CauseParasiticDam(self, iTarget, iMul, iParasiticCount, dTransDamFactor):
        oTarget = self.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            return None
        oHero = self.m_WarriorObj
        oPerform = oHero.GetPerform(GARDENER_PARASITIC)
        if not oPerform:
            return None
        if not iParasiticCount:
            oParasiticState = oTarget.m_State.GetItemBySource(GARDENER_PARASITIC_STATE, oHero.m_ID)
            if not oParasiticState:
                return None
            iParasiticCount = oParasiticState.GetCount()
        if iMul:
            dTransDamFactor['ParasiticDamMul'] = (0, iMul, 0)
        dCustom = {
            'Mul': iParasiticCount,
            'TransDamFactor': dTransDamFactor }
        dPerform = {
            'Custom': dCustom,
            'VID': iTarget }
        cl_war.UseOnlyServerPerform(oHero, oPerform, dPerform)

    
    def ClearOtherInfo(self):
        self.ClearDomainBarrierSummon(iDelayRemove = 0)
        self.m_WarriorObj.Delete('FieldCenterPos')
        self.RemoveAimJar()
        self.m_ThrowInfo = { }
        self.ClearArea()

    
    def OnLeaveScene(self, oTarget, dInfo):
        self.ClearOtherInfo()

    
    def OnHeroDie(self, oTarget, dInfo):
        self.ClearArea()

    
    def OnPlayerReady(self, oTarget, dInfo):
        if not self.m_AreaEffectInfo['AreaEffectID'] or 'reenter' not in dInfo or not dInfo['reenter']:
            return None
        self.SendArea(oTarget)

    
    def CreateSummonBarrier(self, vCenter, vScale, iHPMax):
        self.ClearDomainBarrierSummon(iDelayRemove = 0)
        oHero = self.m_WarriorObj
        oGame = self.m_Game
        clsSummonData = oGame.m_WarData.GetSummonData(GARDENER_BARRIER_SUMMON)
        if not clsSummonData:
            return None
        fBaseBarrierRadius = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'Physx')[0]
        iHero = oHero.m_ID
        dAddInfo = {
            'Owner': iHero,
            'ObjShape': clsSummonData.m_Shape,
            'Angle': (0, 0, 0),
            'Scale': vScale,
            'CanAddBuff': 0,
            'SendMsgTarget': iHero,
            'Shape': MODEL_TYPE_SPHERE,
            'Center': (0, 0, 0),
            'Size': (fBaseBarrierRadius, 0, 0),
            'Side': SIDE_TYPE_HERO,
            'HPMax': iHPMax }
        oSummon = clsSummonData.Create(oGame, dAddInfo)
        if not oSummon:
            return None
        oSummon.m_RemoveAction = self.ResetDomainBarrierInfo
        self.m_DomainBarrier = oSummon.m_ID
        oSummon.Goto(oHero.m_Scene, vCenter)
        self.AddBarrierExtraPhyModel(oSummon, fBaseBarrierRadius * vScale[0])

    
    def AddBarrierExtraPhyModel(self, oSummon, fSize):
        lstResult = self.GetBarrierBoxInfo(fSize, fWidth = 2, fHight = 2)
        for tHalfExt, vCenter in lstResult:
            dParam = {
                'Shape': MODEL_TYPE_BOX,
                'HalfExt': tHalfExt,
                'Center': vCenter }
            oSummon.AddExtraPhyModel(PAMOD_TYPE_DYNA, PXLAYER_BARRIER, dParam)
        

    
    def GetBarrierBoxInfo(self, fBarrierRadius, fWidth, fHight):
        fLength = cl_math.CalDistance((0, 0, 0), (fBarrierRadius, 0, fBarrierRadius))
        fHalfExtZ = fHight / 2
        fHalfExtX = fLength / 2
        fHalfExtY = fWidth / 2
        fDis = fHalfExtX - fHalfExtZ
        lstResult = [
            ((fHalfExtY, fHalfExtZ, fHalfExtX), (fDis, fHalfExtZ, 0)),
            ((fHalfExtY, fHalfExtZ, fHalfExtX), (-fDis, fHalfExtZ, 0)),
            ((fHalfExtX, fHalfExtZ, fHalfExtY), (0, fHalfExtZ, fDis)),
            ((fHalfExtX, fHalfExtZ, fHalfExtY), (0, fHalfExtZ, -fDis))]
        return lstResult

    
    def ResetBarrierExtraPhyModel(self, fScale):
        oBarrierSummon = self.m_Game.GetObject(self.m_DomainBarrier)
        if not oBarrierSummon:
            return None
        oBarrierSummon.ClearAllExtraPhyModel()
        clsSummonData = self.m_Game.m_WarData.GetSummonData(GARDENER_BARRIER_SUMMON)
        if not clsSummonData:
            return None
        fBaseBarrierRadius = cl_modeldefine.GetModelDefine(clsSummonData.m_Shape, 'Physx')[0]
        self.AddBarrierExtraPhyModel(oBarrierSummon, fBaseBarrierRadius * fScale)

    
    def ResetDomainBarrierInfo(self, oBarrierSummon):
        self.m_DomainBarrier = 0

    
    def ClearDomainBarrierSummon(self, iDelayRemove):
        sReason = 'ClearDomainBarrierSummon'
        oSummon = self.m_Game.GetObject(self.m_DomainBarrier)
        if not oSummon:
            return None
        if iDelayRemove:
            oSummon.ScenesRemoveDelay(sReason)
        else:
            oSummon.Remove(sReason)
        self.m_DomainBarrier = 0

    
    def CheckIsDomainBarrierSummon(self, iSummon):
        if iSummon == self.m_DomainBarrier:
            return 1
        return 0

    
    def SetAimJar(self, iJar):
        self.m_AimJar[iJar] = 1

    
    def ClearAimJar(self, iJar):
        if iJar in self.m_AimJar:
            self.m_AimJar.pop(iJar)

    
    def CheckAimJar(self, iJar):
        return iJar in self.m_AimJar

    
    def RemoveAimJar(self):
        oGame = self.m_Game
        for iJar in self.m_AimJar:
            oJar = oGame.GetObject(iJar)
            if not oJar:
                continue
            oJar.Remove('RemoveAimJar')
        
        self.m_AimJar = { }

    
    def GetDomainBarrierID(self):
        return self.m_DomainBarrier

    
    def CreateArea(self, iShape, vStart, vScale):
        self.ClearArea()
        oHero = self.m_WarriorObj
        oPerform = oHero.GetPerform(GARDENER_AREA)
        if not oPerform:
            return None
        dData = {
            'Custom': {
                'vStart': vStart,
                'vScale': vScale } }
        cl_war.UsePerform(oHero, oPerform, dData)
        oGame = self.m_Game
        iEffectID = oGame.NewNoSceneObjID()
        self.m_AreaEffectInfo = {
            'AreaEffectID': iEffectID,
            'AreaEffectShape': iShape,
            'EffectStart': vStart,
            'EffectScale': vScale }
        self.SendArea(oHero)

    
    def SendArea(self, oHero):
        iEffectID = self.m_AreaEffectInfo['AreaEffectID']
        iShape = self.m_AreaEffectInfo['AreaEffectShape']
        vStart = self.m_AreaEffectInfo['EffectStart']
        vScale = self.m_AreaEffectInfo['EffectScale']
        cl_snetwar.GS2CAddEffect(self.m_Game, oHero.m_Scene, iEffectID, iShape, vStart, {
            oHero.m_PlayerID: 1 }, vScale = vScale)

    
    def ClearArea(self):
        iEffectID = self.m_AreaEffectInfo['AreaEffectID']
        if not iEffectID:
            return None
        self.m_AreaEffectInfo = {
            'AreaEffectID': 0,
            'AreaEffectShape': 0,
            'EffectStart': (0, 0, 0),
            'EffectScale': (0, 0, 0) }
        oHero = self.m_WarriorObj
        oGame = self.m_Game
        cl_snetwar.GS2CDeleteEffect(oGame, oHero.m_Scene, iEffectID, {
            oHero.m_PlayerID: 1 })


