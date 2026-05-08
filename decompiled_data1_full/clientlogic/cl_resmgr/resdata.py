# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_resmgr/resdata.pyc
# RelativePath: clientlogic/cl_resmgr/resdata.pyc
# Source Generated with Decompyle++
# File: resdata.pyc (Python 3.6)

from cl_commondefines import BASEATTR_REFRESH, MODEL_TYPE_BOX, MODEL_TYPE_CAPSULE, PARAM_LEVEL_CUSTOM, MONSTERAI_TYPE_DEFAULT, DEFEND_TREND_NONE, WARRIOR_SERVANT, SIDE_TYPE_HERO, NWARRIOR_NPC_CAR, WARRIOR_MONSTER, WARRIOR_INCUBATOR, NWARRIOR_NPC, WARRIOR_BUILD, NWARRIOR_NPC_TRANSFER, NWARRIOR_NPC_SHOP, WARRIOR_DEVICE, WARRIOR_PET, PET_TYPE_WARRIOR, PET_QUALITY_NORMAL, WARRIOR_NORMAL, WARRIOR_ELITE, WARRIOR_NORFLY, ALLVERLAYER_VALID
from cl_commondefines import NWARRIOR_NPC_GOLDENCUP, WARRIOR_BOSS
from cl_cscommondef.cs_fight import SIDE_TYPE_OBSTACLE
from cl_modeldata import GetModel
from cl_only import SendAlert, Time2Frame
import cl_formula
import cl_monster
import cl_npc
import cl_betree
import cl_build
import cl_summon
import cl_roomchallenge
import cl_math
import cl_modeldefine
import cl_notify
import cl_platformdata
import cl_phasechallenge
import cl_servant
import cl_device
from . import aitempparam

class CBaseData(object):
    m_SID = 0
    
    def Create(self, oGame, dAddData):
        pass



class CMonsterData(CBaseData):
    m_DataSID = 0
    m_SID = 2000
    m_Name = '野怪'
    m_Shape = 0
    m_FightType = WARRIOR_MONSTER
    m_Side = 0
    m_AttPerform = 0
    m_PerformList = ()
    m_BaseAttrInfo = { }
    m_EndlessAttr = { }
    m_DemonAttr = { }
    m_TransElite = 0
    m_Betree = ''
    m_BetreeMap = { }
    m_Reward = { }
    m_AIConfig = { }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_NONE
    m_CombatForce = 0
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_BornActionInfo = { }
    m_CreateDelayFrame = 0
    m_CreateEffect = 0
    m_AccuracyFactor = 0
    m_MissingDisType = { }
    m_DodgeCDTime = { }
    m_BanPF = ()
    m_SurvivorAttrPlus = ()
    m_SurvivorBanPF = ()
    m_SurvivorGSCash = 0
    m_NormalMonster = 0
    m_ExtraAIArgs = { }
    m_ExtraPerform = { }
    m_SpecialMHP = 0
    m_DeviceEnergyPoint = { }
    
    def InitMonsterData(cls, oMonster, dAddData):
        iGrade = dAddData['Grade'] if 'Grade' in dAddData else 1
        iSide = dAddData['Side'] if 'Side' in dAddData else cls.m_Side
        tLineIdx = dAddData['Line'] if 'Line' in dAddData else None
        dAIConfig = dAddData['AI'] if 'AI' in dAddData else { }
        if 'Owner' in dAddData:
            oMonster.m_Owner = dAddData['Owner']
        if 'NoEnemyNotify' in dAddData:
            oMonster.m_NeedLockHeroEnemyNotify = dAddData['NoEnemyNotify']
        dAllAIConfig = { }
        oGame = oMonster.m_Game
        iTeam = 0 if oGame.m_WarMgr.IsSingleGame() else 1
        iRound = oGame.m_WarMgr.m_Round
        tKey = (iTeam, iRound)
        if iTeam and (1, 0) in cls.m_AIConfig:
            tKey = (1, 0)
        if not cls.m_AIConfig:
            dClsAIConfig = { }
        elif tKey not in cls.m_AIConfig:
            for iPlayer in oGame.GetRealPlayers():
                cl_notify.GS2CDebugMsg(oGame, iPlayer, '小怪%d不存在组队%d周目%dAI配置' % (cls.m_SID, tKey[0], tKey[1]))
            
            tKey = list(sorted(cls.m_AIConfig))[0]
        dClsAIConfig = cls.m_AIConfig[tKey]
        dAllAIConfig.update(dClsAIConfig)
        dAllAIConfig.update(dAIConfig)
        dAllAIConfig.update(cls.m_ExtraAIArgs)
        oMonster.m_SID = cls.m_SID
        oMonster.m_DataSID = cls.m_DataSID
        oMonster.m_FlawSID = cls.m_DataSID
        oMonster.m_Name = cls.m_Name
        oMonster.m_Shape = dAddData['Shape'] if 'Shape' in dAddData else cls.m_Shape
        oMonster.m_FightType = cls.m_FightType
        oMonster.m_LineIdx = tLineIdx
        oMonster.SetSide(iSide)
        oMonster.m_Grade = iGrade
        oMonster.m_AddGrade = dAddData['AddGrade']
        oMonster.m_AttPerform = cls.m_AttPerform
        oMonster.m_PerformList = cls.m_PerformList
        oMonster.m_CombatForce = cls.m_CombatForce
        oMonster.m_RunSpeedUpMul = cls.m_RunSpeedUpMul
        oMonster.m_SprintSpeedUpMul = cls.m_SprintSpeedUpMul
        oMonster.m_BornActionInfo = cls.m_BornActionInfo
        oMonster.m_AreaIndex = dAddData['AreaIndex'] if 'AreaIndex' in dAddData else 0
        iRefreshFlag = BASEATTR_REFRESH
        dBaseAttr = { }
        bEndless = oGame.m_WarMgr.IsEndless()
        if cls.m_EndlessAttr and bEndless:
            dBaseAttr = cls.m_EndlessAttr
        elif iRound in cls.m_BaseAttrInfo:
            dBaseAttr = cls.m_BaseAttrInfo[iRound]
        elif cls.m_BaseAttrInfo:
            iCurRound = max(cls.m_BaseAttrInfo)
            dBaseAttr = cls.m_BaseAttrInfo[iCurRound]
        if 'Demon' in dAddData:
            if cls.m_DemonAttr:
                if oGame.m_WarMgr.IsEndless() and 1 in cls.m_DemonAttr:
                    dDemonAttr = cls.m_DemonAttr[1]
                else:
                    dDemonAttr = cls.m_DemonAttr[0]
                dAttr = { }
                dAttr.update(dBaseAttr)
                dAttr.update(dDemonAttr)
                dBaseAttr = dAttr
            else:
                SendAlert('err', '战场%d未配置怪物%d妖化属性' % (oGame.m_WarMgr.m_SID, cls.m_SID))
            oMonster.m_FightType = cls.m_FightType & ~WARRIOR_NORMAL | WARRIOR_ELITE
            oMonster.Set('Demon', 1)
        cl_formula.ResetGradeFormulaAttr(oMonster, dBaseAttr, iGrade, iRefreshFlag)
        oMonster.SetCtrlModelData()
        oMonster.m_HP = oMonster.QueryAttr('HPMax')
        oMonster.m_Armor = oMonster.QueryAttr('ArmorMax')
        oMonster.m_Shield = oMonster.QueryAttr('ShieldMax')
        oMonster.m_Speed = oMonster.QueryAttr('MoveSpeed')
        oMonster.m_Energy = oMonster.QueryAttr('EnergyMax')
        if 'AIMethod' in dAIConfig:
            (iAIType, sBetree) = cls.GetMonsterBetree(dAIConfig['AIMethod'])
            cls.GetAITempParam(iAIType, dAllAIConfig)
            if not sBetree:
                SendAlert('err', '请检查导表SID%d怪物的行为树组合映射' % cls.m_SID)
            else:
                sBetree = cls.m_Betree
        oMonster.m_Agent = None.InitFsmAI(oMonster, 'cl_betree.monsteragent', sBetree, dAllAIConfig)
        oMonster.m_Reward = { }
        oMonster.m_Reward.update(cls.m_Reward)
        oMonster.m_PhasePF = { }
        oMonster.m_PhasePF.update(cls.m_PhasePF)
        oMonster.m_DefaultPhase = cls.m_DefaultPhase
        oMonster.m_PhaseHitPartToType = { }
        oMonster.m_PhaseHitPartToType.update(cls.m_PhaseHitPartToType)
        oMonster.m_AttrPlusPF = cls.m_AttrPlusPF
        oMonster.m_DefendTrend = cls.m_DefendTrend
        oMonster.m_AccuracyFactor = cls.m_AccuracyFactor
        oMonster.m_MissingDisType = cls.m_MissingDisType
        iDodgeCDTime = cls.m_DodgeCDTime.get(iRound, 0)
        oMonster.m_DodgeCDFrame = Time2Frame(iDodgeCDTime)
        oMonster.m_BanPF = cls.m_BanPF
        oMonster.m_SurvivorGSCash = cls.m_SurvivorGSCash
        oMonster.m_NormalMonster = cls.m_NormalMonster
        oMonster.m_ExtraPerform = cls.m_ExtraPerform
        oMonster.m_SpecialMHP = cls.m_SpecialMHP
        if 'DefaultSuper' in dAddData:
            (iSuperLevel, iPlus, iAf) = dAddData['DefaultSuper']
            oMonster.MonsterSuper(iSuperLevel, iPlus, iAf)
        if oMonster.m_FightType == WARRIOR_NORFLY:
            oMonster.m_GroundMaxDis = 25
        cls.InitComAtt(oMonster, bEndless)

    InitMonsterData = classmethod(InitMonsterData)
    
    def InitBaseData(cls):
        clsData = cl_platformdata.GetMonsterConfig(cls.m_DataSID)
        cls.m_Shape = clsData.m_Shape
        cls.m_FightType = clsData.m_FightType
        cls.m_AttPerform = clsData.m_AttPerform
        cls.m_PerformList = clsData.m_PerformList
        cls.m_Betree = clsData.m_Betree
        cls.m_BetreeMap = clsData.m_BetreeMap
        cls.m_DefaultPhase = clsData.m_DefaultPhase
        cls.m_PhasePF = clsData.m_PhasePF
        cls.m_PhaseHitPartToType = clsData.m_PhaseHitPartToType
        cls.m_AttrPlusPF = clsData.m_AttrPlusPF
        cls.m_DefendTrend = clsData.m_DefendTrend
        cls.m_AIConfig = clsData.m_AIConfig
        cls.m_CombatForce = clsData.m_CombatForce
        cls.m_BornActionInfo = clsData.m_BornActionInfo
        cls.m_AccuracyFactor = clsData.m_AccuracyFactor
        cls.m_MissingDisType = clsData.m_MissingDisType
        cls.m_CreateDelayFrame = clsData.m_CreateDelayFrame
        cls.m_CreateEffect = clsData.m_CreateEffect
        cls.m_DodgeCDTime = clsData.m_DodgeCDTime
        cls.m_BanPF = clsData.m_BanPF
        cls.m_SurvivorAttrPlus = clsData.m_SurvivorAttrPlus
        cls.m_SurvivorBanPF = clsData.m_SurvivorBanPF
        cls.m_ExtraAIArgs = clsData.m_ExtraAIArgs

    InitBaseData = classmethod(InitBaseData)
    
    def Create(cls, oGame, dAddData):
        return cl_monster.NewMonster(oGame, cls, dAddData)

    Create = classmethod(Create)
    
    def GetTransElite(cls):
        return cls.m_TransElite

    GetTransElite = classmethod(GetTransElite)
    
    def GetMonsterBetree(cls, iAIType):
        dCommon = cls.m_BetreeMap['Common']
        if iAIType in dCommon:
            return (iAIType, dCommon[iAIType])
        dDefault = cls.m_BetreeMap['Default']
        for iGroup, sBetree in dDefault.items():
            if iGroup & iAIType == iGroup:
                return (iGroup, sBetree)
        
        return (iAIType, '')

    GetMonsterBetree = classmethod(GetMonsterBetree)
    
    def GetAITempParam(cls, iAIType, dAIConfig):
        iAILevel = dAIConfig.get('AIParamLv', PARAM_LEVEL_CUSTOM)
        if iAIType != MONSTERAI_TYPE_DEFAULT and iAILevel == PARAM_LEVEL_CUSTOM:
            return None
        dTempParam = aitempparam.GetAIConfParam(iAIType, iAILevel)
        dAIConfig.update(dTempParam)

    GetAITempParam = classmethod(GetAITempParam)
    
    def GetCreateDelayFrame(cls):
        clsData = cl_platformdata.GetMonsterConfig(cls.m_DataSID)
        return clsData.m_CreateDelayFrame

    GetCreateDelayFrame = classmethod(GetCreateDelayFrame)
    
    def GetCreateEffect(cls):
        clsData = cl_platformdata.GetMonsterConfig(cls.m_DataSID)
        return clsData.m_CreateEffect

    GetCreateEffect = classmethod(GetCreateEffect)
    
    def InitComAtt(cls, oMonster, bEndless):
        dMonsterComAttInfo = cl_platformdata.GetMonsterComAttInfo()
        if bEndless:
            func = dMonsterComAttInfo['ComAttEndLess']
        else:
            func = dMonsterComAttInfo['ComAtt']
        iComAtt = cl_formula.GetFormulaResultByLV(oMonster, func, oMonster.m_Grade)
        for iFightType in (WARRIOR_ELITE, WARRIOR_BOSS):
            if oMonster.m_FightType & iFightType == iFightType:
                iComAtt = int(iComAtt * dMonsterComAttInfo['EliteMonsterCoefficient'])
                break
        else:
            iComAtt = int(iComAtt * dMonsterComAttInfo['MonsterCoefficient'])
        oMonster.SetAttr('ComAtt', iComAtt, 0)

    InitComAtt = classmethod(InitComAtt)


class CNpcData(CBaseData):
    m_SID = 5000
    m_Name = '宝箱'
    m_Shape = 0
    m_ActionFunc = None
    m_FightType = NWARRIOR_NPC
    m_InteractDis = 5
    m_InitFunc = None
    m_Side = SIDE_TYPE_OBSTACLE
    m_Info = { }
    
    def InitNPCData(cls, oNpc, dAddData):
        tLineIdx = dAddData['Line'] if 'Line' in dAddData else None
        tFace = dAddData.get('Facing', (0, 0, 1))
        tScale = dAddData.get('Scale', (1, 1, 1))
        iGlobalPrefab = dAddData['GlobalPrefab'] if 'GlobalPrefab' in dAddData else 0
        oNpc.m_FightType = cls.m_FightType
        oNpc.m_SID = cls.m_SID
        oNpc.m_Name = cls.m_Name
        oNpc.m_Shape = cls.m_Shape
        oNpc.m_LineIdx = tLineIdx
        oNpc.m_GlobalPrefab = iGlobalPrefab
        oNpc.SetInteractDis(cls.m_InteractDis)
        oNpc.SetSide(cls.m_Side)
        dParam = CNpcData.GetNPCModeParam(cls.m_Shape, cls.m_FightType, tFace, tScale)
        CNpcData.SetData(oNpc, dAddData)
        oNpc.m_ModelData = GetModel(dParam)
        oNpc.m_VisiblePlayer = dAddData['VisiblePlayer'] if 'VisiblePlayer' in dAddData else { }
        oNpc.Set('Abandoner', dAddData['Abandoner'] if 'Abandoner' in dAddData else 0)
        func = cls.m_InitFunc
        if func:
            func(oNpc)
        dInfo = cls.m_Info
        if 'Action' in dInfo:
            oNpc.m_ActionFunc = dInfo['Action']
            oNpc.m_ActionType = dInfo['ActionType']

    InitNPCData = classmethod(InitNPCData)
    
    def Create(cls, oGame, dAddData):
        return cl_npc.NewNPC(oGame, cls, dAddData)

    Create = classmethod(Create)
    
    def GetNPCModeParam(iShape, iFightType, tFace, tScale):
        iAngleY = cl_math.CalAngle3D(tFace, (0, 0, 1))
        dParam = {
            'Shape': MODEL_TYPE_BOX,
            'Angle': (0, iAngleY, 0),
            'Scale': tScale }
        vBox = cl_modeldefine.GetModelDefine(iShape, 'Box')
        if vBox:
            dParam['Center'] = (0, vBox[1] / 2, 0)
            dParam['Size'] = vBox
        elif iFightType == NWARRIOR_NPC_TRANSFER:
            dParam['Center'] = (0, 1.75, 0)
            dParam['Size'] = (3.25, 3.5, 1.05)
        elif iFightType == NWARRIOR_NPC_SHOP:
            dParam['Center'] = (0, 0.7, 0)
            dParam['Size'] = (3.2, 1.4, 1.6)
        elif iFightType == NWARRIOR_NPC_CAR:
            dParam['Shape'] = MODEL_TYPE_CAPSULE
            dParam['Center'] = (0, 1, 0)
            dParam['Size'] = (2, 0.5, 0)
            dParam['LocalAngle'] = (0, 0, 90)
        else:
            dParam['Center'] = (0, 0.65, 0)
            dParam['Size'] = (2.15, 1.3, 1.55)
        return dParam

    GetNPCModeParam = staticmethod(GetNPCModeParam)
    
    def SetData(oNpc, dAddInfo):
        if oNpc.m_FightType == NWARRIOR_NPC_CAR and 'Paths' in dAddInfo:
            oNpc.Set('Paths', dAddInfo['Paths'])
        if 'GmClone' in dAddInfo:
            oNpc.Set('GmClone', dAddInfo['GmClone'])
        if oNpc.m_FightType == NWARRIOR_NPC_GOLDENCUP:
            if 'SelectedTalent' in dAddInfo:
                oNpc.Set('SelectedTalent', dAddInfo['SelectedTalent'])
            if 'Share' in dAddInfo and not dAddInfo['Share']:
                oNpc.m_Share = dAddInfo['Share']
            if 'SetInfo' in dAddInfo and dAddInfo['SetInfo']:
                for key, value in dAddInfo['SetInfo'].items():
                    oNpc.Set(key, value)
                

    SetData = staticmethod(SetData)


class CBuildData(CBaseData):
    m_DataSID = 0
    m_SID = 1001
    m_Name = '普通建筑'
    m_Shape = 2001
    m_PerformList = ()
    m_BaseAttr = {
        'HPMax': 500 }
    m_LimitDam = 1
    m_Side = SIDE_TYPE_OBSTACLE
    m_FightType = WARRIOR_BUILD
    m_InitFunc = None
    m_SmashFunc = None
    m_InteractFunc = None
    m_SmashReserveGroup = { }
    
    def InitBuildData(cls, oBuild, dAddData):
        iGrade = dAddData['Grade'] if 'Grade' in dAddData else 1
        iSide = dAddData['Side'] if 'Side' in dAddData else cls.m_Side
        tLineIdx = dAddData['Line'] if 'Line' in dAddData else None
        iPrefab = dAddData['Prefab'] if 'Prefab' in dAddData else 0
        if 'Owner' in dAddData:
            oBuild.m_Owner = dAddData['Owner']
        oBuild.m_SID = cls.m_SID
        oBuild.m_Name = cls.m_Name
        oBuild.m_Shape = cls.m_Shape
        oBuild.m_LineIdx = tLineIdx
        oBuild.m_PerformList = cls.m_PerformList
        oBuild.m_FightType = cls.m_FightType
        oBuild.m_LimitDam = cls.m_LimitDam
        oBuild.m_ClassifyList = cls.m_ClassifyList
        oBuild.SetSide(iSide)
        oBuild.m_Grade = iGrade
        oBuild.m_Prefab = iPrefab
        oBuild.m_ModelData = GetModel(dAddData)
        oBuild.m_ClientGlobalArea = dAddData['GlobalArea'] if 'GlobalArea' in dAddData else 0
        iRefreshFlag = BASEATTR_REFRESH
        cl_formula.ResetGradeFormulaAttr(oBuild, cls.m_BaseAttr, iGrade, iRefreshFlag)
        oBuild.m_HP = oBuild.QueryAttr('HPMax')
        oBuild.m_SmashFunc = cls.m_SmashFunc
        oBuild.m_InteractFunc = cls.m_InteractFunc
        oBuild.m_SmashReserveGroup = cls.m_SmashReserveGroup
        func = cls.m_InitFunc
        if func:
            func(oBuild)

    InitBuildData = classmethod(InitBuildData)
    
    def InitBaseData(cls):
        clsData = cl_platformdata.GetBuildConfig(cls.m_DataSID)
        cls.m_FightType = clsData.m_FightType
        cls.m_Shape = clsData.m_Shape
        cls.m_PerformList = clsData.m_PerformList
        cls.m_LimitDam = clsData.m_LimitDam
        cls.m_BaseAttr = clsData.m_BaseAttr
        cls.m_InitFunc = clsData.m_InitFunc
        cls.m_ClassifyList = clsData.m_ClassifyList

    InitBaseData = classmethod(InitBaseData)
    
    def Create(cls, oGame, dAddData):
        return cl_build.NewBuild(oGame, cls, dAddData)

    Create = classmethod(Create)


class CSummonData(CBaseData):
    m_SID = 1001
    m_Name = '召唤物'
    m_Shape = 2001
    m_FightType = NWARRIOR_NPC
    m_Action = None
    m_BaseAttr = { }
    m_Side = SIDE_TYPE_OBSTACLE
    m_BodyPart = ()
    m_DieAction = None
    m_PerformList = ()
    m_DataSID = 0
    
    def InitSummonData(cls, oSummon, dAddData):
        iGrade = dAddData['Grade'] if 'Grade' in dAddData else 1
        iSide = dAddData['Side'] if 'Side' in dAddData else cls.m_Side
        tLineIdx = dAddData['Line'] if 'Line' in dAddData else None
        iPrefab = dAddData['Prefab'] if 'Prefab' in dAddData else 0
        if 'Owner' in dAddData:
            oSummon.m_Owner = dAddData['Owner']
        oSummon.m_SID = cls.m_SID
        oSummon.m_Name = cls.m_Name
        oSummon.m_Shape = cls.m_Shape
        oSummon.m_LineIdx = tLineIdx
        oSummon.m_FightType = cls.m_FightType
        oSummon.m_Prefab = iPrefab
        oSummon.m_Grade = iGrade
        oSummon.m_AddGrade = dAddData['AddGrade'] if 'AddGrade' in dAddData else 0
        oSummon.m_BodyPart = cls.m_BodyPart
        oSummon.m_DieAction = cls.m_DieAction
        oSummon.m_DataSID = cls.m_DataSID
        oSummon.SetSide(iSide)
        if 'Shape' in dAddData:
            oSummon.m_ModelData = GetModel(dAddData)
        else:
            oSummon.m_ModelData = GetModel(cls.GetSummonModeParam(cls.m_Shape, cls.m_FightType))
        oSummon.m_PerformList = cls.m_PerformList
        iRefreshFlag = BASEATTR_REFRESH
        cl_formula.ResetGradeFormulaAttr(oSummon, cls.m_BaseAttr, iGrade, iRefreshFlag)
        oSummon.m_HP = oSummon.QueryAttr('HPMax')
        oSummon.m_Shield = oSummon.QueryAttr('ShieldMax')
        oSummon.m_Armor = oSummon.QueryAttr('ArmorMax')

    InitSummonData = classmethod(InitSummonData)
    
    def InitBaseData(cls):
        clsData = cl_platformdata.GetSummonConfig(cls.m_DataSID)
        cls.m_FightType = clsData.m_FightType
        cls.m_Shape = clsData.m_Shape
        cls.m_PerformList = clsData.m_PerformList
        cls.m_BodyPart = clsData.m_BodyPart
        cls.m_BaseAttr = clsData.m_BaseAttr
        cls.m_Action = clsData.m_Action

    InitBaseData = classmethod(InitBaseData)
    
    def Create(cls, oGame, dAddData):
        return cl_summon.NewSummon(oGame, cls, dAddData)

    Create = classmethod(Create)
    
    def GetSummonModeParam(iShape, iFightType):
        dParam = { }
        if iFightType == WARRIOR_INCUBATOR:
            tModelData = cl_modeldefine.GetModelDefine(iShape, 'NavMesh')
            if tModelData:
                dParam = {
                    'Shape': MODEL_TYPE_CAPSULE,
                    'Angle': (0, 0, 0),
                    'Scale': (1, 1, 1),
                    'Center': (0, 0, 0),
                    'Size': (tModelData[1], tModelData[0], 0) }
        if not dParam:
            dParam = {
                'Shape': MODEL_TYPE_CAPSULE,
                'Angle': (0, 0, 0),
                'Scale': (1, 1, 1),
                'Size': (1, 1, 0),
                'Center': (0, 0.65, 0) }
        return dParam

    GetSummonModeParam = staticmethod(GetSummonModeParam)


class CRoomChallengeData(CBaseData):
    m_SID = 0
    m_Type = 0
    m_ChallengeName = ''
    m_ChallengeNotify = ''
    m_Reward = { }
    m_ExcludeLastRoom = 0
    m_ExcludeArea = []
    m_ValidVerLayer = ALLVERLAYER_VALID
    
    def Create(cls, oGame, dAddData):
        return cl_roomchallenge.NewChallenge(oGame, cls, dAddData)

    Create = classmethod(Create)
    
    def ExcludeLastRoom(cls):
        return cls.m_ExcludeLastRoom

    ExcludeLastRoom = classmethod(ExcludeLastRoom)
    
    def GetValidVerLayer(cls):
        return cls.m_ValidVerLayer

    GetValidVerLayer = classmethod(GetValidVerLayer)


class CPhaseChallengeData(CBaseData):
    m_SID = 0
    m_Type = 0
    m_ChallengeName = ''
    m_ChallengeNotify = ''
    m_SuccessNotify = ''
    m_FailedNotify = ''
    m_EffectState = 0
    m_ReadyTime = 0
    m_ChallengeTime = 0
    m_Reward = { }
    m_Param = tuple()
    m_IgnoreSingle = 0
    m_HpConfig = { }
    
    def Create(cls, oGame, dAddData):
        return cl_phasechallenge.NewPhaseChallenge(oGame, cls, dAddData)

    Create = classmethod(Create)


class CServantData(CBaseData):
    m_SID = 2000
    m_Name = '仆从'
    m_Shape = 0
    m_FightType = WARRIOR_SERVANT
    m_Side = SIDE_TYPE_HERO
    m_AttPerform = 0
    m_PerformList = ()
    m_BaseAttrInfo = { }
    m_Betree = ''
    m_AIConfig = { }
    m_DefendTrend = DEFEND_TREND_NONE
    m_BaseHate = { }
    m_DefaultPhase = 1
    m_PhasePF = { }
    m_HateDisEff = { }
    
    def InitServantData(cls, oServant, dAddData):
        iGrade = dAddData['Grade'] if 'Grade' in dAddData else 1
        iSide = dAddData['Side'] if 'Side' in dAddData else cls.m_Side
        if 'Owner' in dAddData:
            oServant.m_Owner = dAddData['Owner']
        oGame = oServant.m_Game
        iRound = oGame.m_WarMgr.m_Round
        oServant.m_SID = cls.m_SID
        oServant.m_Name = cls.m_Name
        oServant.m_Shape = cls.m_Shape
        oServant.m_FightType = cls.m_FightType
        oServant.SetSide(iSide)
        oServant.m_Grade = iGrade
        oServant.m_AttPerform = cls.m_AttPerform
        oServant.m_PerformList = cls.m_PerformList
        oServant.m_BaseHate = cls.m_BaseHate
        oServant.m_PhasePF = { }
        oServant.m_PhasePF.update(cls.m_PhasePF)
        oServant.m_DefaultPhase = cls.m_DefaultPhase
        oServant.m_HateDisEff = { }
        oServant.m_HateDisEff.update(cls.m_HateDisEff)
        iRefreshFlag = BASEATTR_REFRESH
        dAllAIConfig = { }
        dAllAIConfig.update(cls.m_AIConfig)
        dBaseAttr = { }
        dBaseAttrInfo = { }
        iPhase = dAddData['Phase'] if 'Phase' in dAddData else oServant.m_DefaultPhase
        if iRound in cls.m_BaseAttrInfo:
            dBaseAttrInfo = cls.m_BaseAttrInfo[iRound]
        elif cls.m_BaseAttrInfo:
            iCurRound = max(cls.m_BaseAttrInfo)
            dBaseAttrInfo = cls.m_BaseAttrInfo[iCurRound]
        if dBaseAttrInfo:
            if iPhase not in dBaseAttrInfo:
                iPhase = oServant.m_DefaultPhase
            dBaseAttr.update(dBaseAttrInfo[iPhase])
        cl_formula.ResetGradeFormulaAttr(oServant, dBaseAttr, iGrade, iRefreshFlag)
        oServant.SetCtrlModelData()
        oServant.m_HP = oServant.QueryAttr('HPMax')
        oServant.m_Armor = oServant.QueryAttr('ArmorMax')
        oServant.m_Shield = oServant.QueryAttr('ShieldMax')
        oServant.m_Speed = oServant.QueryAttr('MoveSpeed')
        oServant.m_Energy = oServant.QueryAttr('EnergyMax')
        oServant.m_Agent = cl_betree.InitFsmAI(oServant, 'cl_betree.servantagent', cls.m_Betree, dAllAIConfig)
        oServant.m_DefendTrend = cls.m_DefendTrend
        oServant.m_AttrInfo = dBaseAttr

    InitServantData = classmethod(InitServantData)
    
    def Create(cls, oGame, dAddData):
        return cl_servant.CreateServant(oGame, cls, dAddData)

    Create = classmethod(Create)


class CDeviceData(CBaseData):
    m_SID = 1000
    m_Name = '装置'
    m_Shape = 0
    m_HeroExtAttr = { }
    m_HeroExtPassive = ()
    m_HeroPerformInfo = { }
    m_ActiveDisablePerform = ()
    m_FightType = WARRIOR_DEVICE
    m_Side = SIDE_TYPE_HERO
    m_AttPerform = 0
    m_PerformList = ()
    m_BaseAttrInfo = { }
    m_Betree = ''
    m_AIConfig = { }
    m_BaseHate = { }
    m_HateDisEff = { }
    m_ActiveStopEnergyRecover = 0
    
    def InitDeviceData(cls, oHero, oDevice, dAddData):
        iGrade = dAddData['Grade'] if 'Grade' in dAddData else 1
        iSide = dAddData['Side'] if 'Side' in dAddData else cls.m_Side
        oDevice.SetOwner(oHero)
        oDevice.m_SID = cls.m_SID
        oDevice.m_Name = cls.m_Name
        oDevice.m_Shape = cls.m_Shape
        oDevice.m_FightType = cls.m_FightType
        oDevice.SetSide(iSide)
        oDevice.m_AttPerform = cls.m_AttPerform
        oDevice.m_PerformList = cls.m_PerformList
        oDevice.m_ActiveDisablePerform = cls.m_ActiveDisablePerform
        iRefreshFlag = BASEATTR_REFRESH
        dAllAIConfig = { }
        dAllAIConfig.update(cls.m_AIConfig)
        dBaseAttr = dict(cls.m_BaseAttrInfo)
        cl_formula.ResetGradeFormulaAttr(oDevice, dBaseAttr, iGrade, iRefreshFlag)
        oDevice.SetCtrlModelData()
        oDevice.m_HP = oDevice.QueryAttr('HPMax')
        oDevice.m_Speed = oDevice.QueryAttr('MoveSpeed')
        oDevice.m_Agent = cl_betree.InitFsmAI(oDevice, 'cl_betree.servantagent', cls.m_Betree, dAllAIConfig)
        oDevice.m_AttrInfo = dBaseAttr
        if cls.m_BaseHate:
            oDevice.m_BaseHate = cls.m_BaseHate
        if cls.m_HateDisEff:
            oDevice.m_HateDisEff = cls.m_HateDisEff
        oDevice.m_ActiveStopEnergyRecover = cls.m_ActiveStopEnergyRecover

    InitDeviceData = classmethod(InitDeviceData)
    
    def Create(cls, oGame, oHero, dAddData):
        return cl_device.CreateDevice(oGame, oHero, cls, dAddData)

    Create = classmethod(Create)


class CPetData(CBaseData):
    m_SID = 1000
    m_MonsterDataSID = 0
    m_Name = '妖灵'
    m_PetType = PET_TYPE_WARRIOR
    m_Quality = PET_QUALITY_NORMAL
    m_BaseAttrInfo = { }
    m_OffsetRange = { }
    m_FightType = WARRIOR_PET
    m_Side = SIDE_TYPE_HERO
    m_AttPerform = 0
    m_PerformList = ()
    m_AbilityGroup = ()
    m_Betree = ''
    m_AIConfig = { }
    m_BaseHate = { }
    m_HateDisEff = { }
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_HateFactor = 1
    m_Shape = 0
    
    def InitPetData(cls, oPet):
        oPet.m_SID = cls.m_SID
        oPet.m_MonsterDataSID = cls.m_MonsterDataSID
        oPet.m_Name = cls.m_Name
        oPet.m_Shape = cls.m_Shape
        oPet.m_FightType = cls.m_FightType
        oPet.m_PetType = cls.m_PetType
        oPet.m_Quality = cls.m_Quality
        oPet.SetSide(cls.m_Side)
        oPet.m_AttPerform = cls.m_AttPerform
        oPet.m_PerformList = cls.m_PerformList
        oPet.m_AbilityGroup = cls.m_AbilityGroup
        oPet.m_AttrInfo = dict(cls.m_BaseAttrInfo)
        oPet.m_OffsetRange = dict(cls.m_OffsetRange)
        oPet.m_RunSpeedUpMul = cls.m_RunSpeedUpMul
        oPet.m_SprintSpeedUpMul = cls.m_SprintSpeedUpMul
        oPet.m_HateFactor = cls.m_HateFactor
        oPet.m_BaseHate = cls.m_BaseHate
        oPet.m_HateDisEff = { }
        oPet.m_HateDisEff.update(cls.m_HateDisEff)
        dAllAIConfig = { }
        dAllAIConfig.update(cls.m_AIConfig)
        oPet.m_Agent = cl_betree.InitFsmAI(oPet, 'cl_betree.servantagent', cls.m_Betree, dAllAIConfig)
        oConquerElement = oPet.m_Game.m_WarMgr.GetComponent('ConquerElement')
        oPet.m_AttrGrowth = oConquerElement.m_PetGrowth if oConquerElement else {
            'HPMax': 10,
            'Att': 32 }

    InitPetData = classmethod(InitPetData)

