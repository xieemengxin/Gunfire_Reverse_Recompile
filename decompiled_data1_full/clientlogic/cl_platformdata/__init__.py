# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cllib.lib_only import RunMobileData
from cl_only import PythonError
import importlib
from . import pc
from . import mobile
from .pc import playway as pcplayway
from .pc import commonnotify as pcnotify
from .pc import playerInfo as pcplayInfo
from .pc import wand as pcwand
from .pc import wandcomp as pcwandcomp
from .pc import throw as pcthrow
from .pc import wandability as pcwandability
from .pc import commonative as pccommonative
from .pc import diceability as pcdiceability
from .pc import dicespecialitem as pcdicespecialitem
from .pc import s7module as pcs7module
from .pc import seasonpassive as pcseaonpassive
from .pc import s7crystal as pcs7crystal
from .pc import clientactive as pcclientactive
from .pc import s8gemitem as pcs8gemitem
from .pc import s8thirditem as pcs8thirditem
from .pc import s7specialpassive as pcs7specialpassive
from .mobile import playway as mobileplayway
from .mobile import commonnotify as mobilenotify
from .mobile import playerInfo as mobileplayInfo
from .mobile import wand as mobilewand
from .mobile import wandcomp as mobilewandcomp
from .mobile import commonative as mobilecommonative
from cl_sublimation import GetSublimationCls

def IsRunPCData():
    return not RunMobileData()


def ImportdMod(sPlatform, sPath, sMod):
    
    try:
        mod = importlib.import_module('cl_platformdata.%s.%s.%s' % (sPlatform, sPath, sMod))
    except:
        PythonError()
        return None

    return mod


def HasBulletType(iSID):
    if IsRunPCData():
        return pc.HasBulletType(iSID)
    return mobile.HasBulletType(iSID)


def GetAllWeaponBulletType():
    if IsRunPCData():
        return pc.GetAllWeaponBulletType()
    return mobile.GetAllWeaponBulletType()


def GetAllBulletType():
    if IsRunPCData():
        return pc.GetAllBulletType()
    return mobile.GetAllBulletType()


def GetBulletSubMsg():
    if IsRunPCData():
        return pc.GetBulletSubMsg()
    return mobile.GetBulletSubMsg()


def GetAllKeyType():
    if IsRunPCData():
        return pc.GetAllKeyType()
    return mobile.GetAllKeyType()


def GetLockWeapon():
    if IsRunPCData():
        return pc.GetLockWeapon()
    return mobile.GetLockWeapon()


def GetUnlockWeapon():
    if IsRunPCData():
        return pc.GetUnlockWeapon()
    return mobile.GetUnlockWeapon()


def GetWeaponPut():
    if IsRunPCData():
        return pc.GetWeaponPut()
    return mobile.GetWeaponPut()


def GetBenedictionPut():
    if IsRunPCData():
        return pc.GetBenedictionPut()
    return mobile.GetBenedictionPut()


def GetWeaponInternalPut():
    if IsRunPCData():
        return pc.GetWeaponInternalPut()
    return mobile.GetWeaponInternalPut()


def GetRelicInternalPut():
    if IsRunPCData():
        return pc.GetRelicInternalPut()
    return mobile.GetRelicInternalPut()


def GetRelicPut():
    if IsRunPCData():
        return pc.GetRelicPut()
    return mobile.GetRelicPut()


def GetRelicQuality():
    if IsRunPCData():
        return pc.GetRelicQuality()
    return mobile.GetRelicQuality()


def GetRelicQualityMap():
    if IsRunPCData():
        return pc.GetRelicQualityMap()
    return mobile.GetRelicQualityMap()


def GetRelicByType(iType):
    if IsRunPCData():
        dRelicType = pc.GetRelicType()
    else:
        dRelicType = mobile.GetRelicType()
    if iType in dRelicType:
        return list(dRelicType[iType])
    return []


def GetLockRelic():
    if IsRunPCData():
        return pc.GetLockRelic()
    return mobile.GetLockRelic()


def GetUnlockRelic():
    if IsRunPCData():
        return pc.GetUnlockRelic()
    return mobile.GetUnlockRelic()


def GetCurseRelic():
    if IsRunPCData():
        return pc.GetCurseRelic()
    return mobile.GetCurseRelic()


def GetBossRelic():
    if IsRunPCData():
        return pc.GetBossRelic()
    return mobile.GetBossRelic()


def GetGameExcludeRelic():
    if IsRunPCData():
        return pc.GetGameExcludeRelic()
    return mobile.GetGameExcludeRelic()


def GetNormalNoPutRelic():
    if IsRunPCData():
        return pc.GetNormalNoPutRelic()
    return mobile.GetNormalNoPutRelic()


def GetCanRepickupRelic():
    if IsRunPCData():
        return pc.GetCanRepickupRelic()
    return mobile.GetCanRepickupRelic()


def GetConsumableRelic():
    if IsRunPCData():
        return pc.GetConsumableRelic()
    return mobile.GetConsumableRelic()


def GetBreedRelicGroup():
    if IsRunPCData():
        return pc.GetBreedRelicGroup()
    return mobile.GetBreedRelicGroup()


def GetRelic2Monster():
    if IsRunPCData():
        return pc.GetRelic2Monster()
    return mobile.GetRelic2Monster()


def GetMonsterExclude():
    if IsRunPCData():
        return pc.GetMonsterExclude()
    return mobile.GetMonsterExclude()


def GetMonsterRelicInternalPut():
    if IsRunPCData():
        return pc.GetMonsterRelicInternalPut()
    return mobile.GetMonsterRelicInternalPut()


def GetMonsterRelicPut():
    if IsRunPCData():
        return pc.GetMonsterRelicPut()
    return mobile.GetMonsterRelicPut()


def GetBossRelicPut():
    if IsRunPCData():
        return pc.GetBossRelicPut()
    return mobile.GetBossRelicPut()


def GetBossRelicMap():
    if IsRunPCData():
        return pc.GetBossRelicMap()
    return { }


def GetMapRelic():
    if IsRunPCData():
        return pc.GetMapRelic()
    return mobile.GetMapRelic()


def GetRoundForbidRelic(iRound):
    if IsRunPCData():
        dRelic = pc.GetRoundRelic()
    else:
        dRelic = mobile.GetRoundRelic()
    return dRelic.get(iRound, { })


def GetForbidRelic():
    if IsRunPCData():
        return pc.GetRoundRelic()
    return mobile.GetRoundRelic()


def GetOtherMonster():
    if IsRunPCData():
        return pc.GetOtherMonster()
    return mobile.GetOtherMonster()


def GetTalentLib():
    if IsRunPCData():
        return pc.GetTalentLib()
    return mobile.GetTalentLib()


def GeCommonTalentLib():
    if IsRunPCData():
        return pc.GetCommonTalentLib()
    return mobile.GetCommonTalentLib()


def GetMinorLib():
    if IsRunPCData():
        return pc.GetMinorLib()
    return mobile.GetMinorLib()


def GetBenedictionLib():
    if IsRunPCData():
        return pc.GetBenedictionLibrary()
    return mobile.GetBenedictionLibrary()


def GetBenedictionPrice():
    if IsRunPCData():
        return pc.GetBenedictionPrice()
    return mobile.GetBenedictionPrice()


def GetGameExcludeBened(iNumber):
    if IsRunPCData():
        return pc.GetGameExcludeBened(iNumber)
    return mobile.GetGameExcludeBened(iNumber)


def GetTeamOnlyBened():
    if IsRunPCData():
        return pc.GetTeamOnlyBened()
    return mobile.GetTeamOnlyBened()


def GetLimitModeBened(iModeType):
    if IsRunPCData():
        return pc.GetLimitModeBened(iModeType)
    return mobile.GetLimitModeBened(iModeType)


def GetLimitSeasonBened():
    if IsRunPCData():
        return pc.GetLimitSeasonBened()
    return mobile.GetLimitSeasonBened()


def GetLimitSeasonBenedLock():
    if IsRunPCData():
        return pc.GetLimitSeasonBenedLock()
    return mobile.GetLimitSeasonBenedLock()


def GetLimitSeasonTalentPut():
    if IsRunPCData():
        return pc.GetLimitSeasonTalentPut()
    return mobile.GetLimitSeasonTalentPut()

if 'g_MonsterConfigModule' not in globals():
    g_MonsterConfigModule = { }

def GetMonsterConfig(iDataSID):
    if iDataSID not in g_MonsterConfigModule:
        if IsRunPCData():
            if not pc.ValidMonsterConfig(iDataSID):
                return None
            sPlatform = 'pc'
        elif not mobile.ValidMonsterConfig(iDataSID):
            return None
        sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'monsterconfig', 'c%d' % iDataSID)
        if not mod:
            return None
        g_MonsterConfigModule[iDataSID] = mod
    return g_MonsterConfigModule[iDataSID].CMonsterData

if 'g_BuildConfigModule' not in globals():
    g_BuildConfigModule = { }

def GetBuildConfig(iDataSID):
    if iDataSID not in g_BuildConfigModule:
        if IsRunPCData():
            if not pc.ValidBuildConfig(iDataSID):
                return None
            sPlatform = 'pc'
        elif not mobile.ValidBuildConfig(iDataSID):
            return None
        sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'buildconfig', 'c%d' % iDataSID)
        if not mod:
            return None
        g_BuildConfigModule[iDataSID] = mod
    return g_BuildConfigModule[iDataSID].CBuildData

if 'g_SummonConfigModule' not in globals():
    g_SummonConfigModule = { }

def GetSummonConfig(iDataSID):
    if iDataSID not in g_SummonConfigModule:
        if IsRunPCData():
            if not pc.ValidSummonConfig(iDataSID):
                return None
            sPlatform = 'pc'
        elif not mobile.ValidSummonConfig(iDataSID):
            return None
        sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'summonconfig', 'c%d' % iDataSID)
        if not mod:
            return None
        g_SummonConfigModule[iDataSID] = mod
    return g_SummonConfigModule[iDataSID].CSummonData


def GetSummonClassify(iSummon):
    if IsRunPCData():
        return pc.GetSummonClassify(iSummon)
    return mobile.GetSummonClassify(iSummon)


def GetIgnoreBeTarget():
    if IsRunPCData():
        return pc.GetIgnoreBeTarget()
    return mobile.GetIgnoreBeTarget()

if 'g_ServantConfig' not in globals():
    g_ServantConfig = { }

def GetServantConfig(iSID):
    if iSID not in g_ServantConfig:
        if not pc.ValidServantConfigModule(iSID):
            return None
        mod = ImportdMod('pc', 'servant', 's%d' % iSID)
        if not mod:
            return None
        g_ServantConfig[iSID] = mod
    return g_ServantConfig[iSID].CServantData


def GetCommonNotify(iChat):
    if IsRunPCData():
        if iChat in pcnotify.g_CommonNotifyTable:
            return pcnotify.g_CommonNotifyTable[iChat]
        return None
    if iChat in mobilenotify.g_CommonNotifyTable:
        return mobilenotify.g_CommonNotifyTable[iChat]


def GetDayTrialItem(iItem):
    if IsRunPCData():
        if iItem in pcplayway.g_DayTrialItem:
            return pcplayway.g_DayTrialItem[iItem]
        return None
    if iItem in mobileplayway.g_DayTrialItem:
        return mobileplayway.g_DayTrialItem[iItem]


def GetDayTrialTheme(iThem):
    if IsRunPCData():
        if iThem in pcplayway.g_DayTrialTheme:
            return pcplayway.g_DayTrialTheme[iThem]
        return None
    if iThem in mobileplayway.g_DayTrialTheme:
        return mobileplayway.g_DayTrialTheme[iThem]

if 'g_ProgressUnlockCls' not in globals():
    g_ProgressModule = { }

def GetAllUnlockProgress():
    if IsRunPCData():
        return pc.GetAllUnlockProgress()
    return mobile.GetAllUnlockProgress()


def GetUnlockProgressCls(iSID):
    if iSID not in g_ProgressModule:
        if IsRunPCData():
            sPlatform = 'pc'
            if not pc.ValidUnlockProgress(iSID):
                return None
        sPlatform = 'mobile'
        if not mobile.ValidUnlockProgress(iSID):
            if not pc.ValidUnlockProgress(iSID):
                return None
            sPlatform = 'pc'
        mod = ImportdMod(sPlatform, 'progressunlock', 'u%d' % iSID)
        if not mod:
            return None
        g_ProgressModule[iSID] = mod
    return g_ProgressModule[iSID].CProgressUnlockData


def LoadAllUnlockProgress():
    lstUnlockProgress = GetAllUnlockProgress()
    for iSID in lstUnlockProgress:
        GetUnlockProgressCls(iSID)
    


def GetPlayerMaxGrade(oPlayer):
    if IsRunPCData():
        lstAllSublime = pc.GetAllSublime()
    else:
        lstAllSublime = mobile.GetAllSublime()
    iMaxGrade = 1
    dValidUserHero = { }
    for iSublime in lstAllSublime:
        clsSublimation = GetSublimationCls(iSublime)
        if not clsSublimation:
            continue
        iLimitHero = clsSublimation.m_LimitHero
        if iLimitHero:
            if iLimitHero not in dValidUserHero:
                dValidUserHero[iLimitHero] = oPlayer.m_HeroCon.ValidUseHero(iLimitHero, iLog = 0)
            if not dValidUserHero[iLimitHero]:
                continue
            continue
        iMaxGrade += clsSublimation.m_MaxLevel
    
    return iMaxGrade


def GetPlayerNextExp():
    if IsRunPCData():
        return pcplayInfo.g_PlayerNextExp
    return mobileplayInfo.g_PlayerNextExp


def GetInscriptionLib():
    if IsRunPCData():
        return pc.GetInscriptionLib()
    return mobile.GetInscriptionLib()


def ValidKnapsack(iSID):
    if IsRunPCData():
        return pc.ValidKnapsack(iSID)
    return mobile.ValidKnapsack(iSID)


def GetAllKnapsack():
    if IsRunPCData():
        return pc.GetAllKnapsack()
    return mobile.GetAllKnapsack()


def ValidAnimaModule(iSID):
    if IsRunPCData():
        return pc.ValidAnimaModule(iSID)
    return mobile.ValidAnimaModule(iSID)


def GetAllAnimaModule():
    if IsRunPCData():
        return pc.GetAllAnimaModule()
    return mobile.GetAllAnimaModule()


def GetRareItemLimit():
    if IsRunPCData():
        return pc.GetRareItemLimit()
    return mobile.GetRareItemLimit()


def GetRareItmeLimitPlayType(iPlayType):
    if IsRunPCData():
        return pc.GetRareItmeLimitPlayType(iPlayType)
    return mobile.GetRareItmeLimitPlayType(iPlayType)

if 'g_Suitcls' not in globals():
    g_Suitcls = { }

def GetSuitCls(iSID):
    if iSID not in g_Suitcls:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'suit', 'suit%4d' % iSID)
        if not mod:
            return None
        g_Suitcls[iSID] = mod.CSuitData
    return g_Suitcls[iSID]


def GetAllSuit():
    if IsRunPCData():
        return pc.GetAllSuit()
    return mobile.GetAllSuit()


def GetGameExcludeSuit(iPlayType):
    if IsRunPCData():
        return pc.GetGameExcludeSuit(iPlayType)
    return mobile.GetGameExcludeSuit(iPlayType)


def GetLimitShow():
    if IsRunPCData():
        return pc.GetLimitShow()
    return mobile.GetLimitShow()


def GetSuitExclude(iSuit):
    if IsRunPCData():
        return pc.GetSuitExclude(iSuit)
    return mobile.GetSuitExclude(iSuit)

if 'g_TaskModule' not in globals():
    g_TaskModule = { }

def GetTaskClass(iTask):
    if iTask not in g_TaskModule:
        if IsRunPCData():
            if not pc.ValidTask(iTask):
                return None
            sPlatform = 'pc'
        elif not mobile.ValidTask(iTask):
            return None
        sPlatform = 'mobile'
        oTaskMod = ImportdMod(sPlatform, 'task', 'task%d' % iTask)
        if not oTaskMod:
            return None
        g_TaskModule[iTask] = oTaskMod
    return g_TaskModule[iTask].CTask


def GetMonsterFlawRange():
    if IsRunPCData():
        return pc.GetMonsterFlawRange()
    return mobile.GetMonsterFlawRange()


def GetMonsterFlaw():
    if IsRunPCData():
        return pc.GetMonsterFlaw()
    return mobile.GetMonsterFlaw()


def GetWeaknessFlawMonster():
    if IsRunPCData():
        return pc.GetWeaknessFlawMonster()
    return mobile.GetWeaknessFlawMonster()


def GetShareFlawCountMonster():
    if IsRunPCData():
        return pc.GetShareFlawCountMonster()
    return mobile.GetShareFlawCountMonster()


def GetImmuneExecuteMonster():
    if IsRunPCData():
        return pc.GetImmuneExecuteMonster()
    return mobile.GetImmuneExecuteMonster()


def GetReliceTalentWeight():
    if IsRunPCData():
        return pc.GetReliceTalentWeight()
    return mobile.GetReliceTalentWeight()


def GetDeviceCompWeight():
    return pc.GetDeviceCompWeight()


def GetAllDevice():
    return pc.GetAllDevice()

if 'g_DeviceModule' not in globals():
    g_DeviceModule = { }

def GetDeviceClass(iSID):
    if iSID not in g_DeviceModule:
        dAllDevice = GetAllDevice()
        if iSID not in dAllDevice:
            return None
        oDeviceMod = ImportdMod('pc', 'device', 'd%d' % iSID)
        if not oDeviceMod:
            return None
        g_DeviceModule[iSID] = oDeviceMod
    return g_DeviceModule[iSID].CDeviceData


def GetAllPet():
    return pc.GetAllPet()


def GetAllHeroSidePet():
    return pc.GetAllHeroSidePet()

if 'g_PetModule' not in globals():
    g_PetModule = { }

def GetPetClass(iSID):
    if iSID not in g_PetModule:
        dAllPet = dict(GetAllPet())
        dAllPet.update(GetAllHeroSidePet())
        if iSID not in dAllPet:
            return None
        oPetMod = ImportdMod('pc', 'pet', 'pet%d' % iSID)
        if not oPetMod:
            return None
        g_PetModule[iSID] = oPetMod
    return g_PetModule[iSID].CPetData


def GetDemonPlusWeight():
    if IsRunPCData():
        return pc.GetDemonPlusWeight()
    return mobile.GetDemonPlusWeight()


def GetPetAbilityPut():
    if IsRunPCData():
        return pc.GetPetAbilityPut()
    return mobile.GetPetAbilityPut()


def GetCommonSpell():
    if IsRunPCData():
        return pc.GetCommonSpell()
    return mobile.GetCommonSpell()


def GetPetPutWayReward():
    if IsRunPCData():
        return pc.GetPetPutWayReward()
    return mobile.GetPetPutWayReward()


def GetPetPutWayWeight():
    if IsRunPCData():
        return pc.GetPetPutWayWeight()
    return mobile.GetPetPutWayWeight()


def GetPetEggDrop():
    if IsRunPCData():
        return pc.GetPetEggDrop()
    return mobile.GetPetEggDrop()


def GetRareEggPut():
    if IsRunPCData():
        return pc.GetRareEggPut()
    return mobile.GetRareEggPut()


def GetNormalEggPut():
    if IsRunPCData():
        return pc.GetNormalEggPut()
    return mobile.GetNormalEggPut()


def GetFusePetConfig():
    if IsRunPCData():
        return pc.GetFusePetConfig()
    return mobile.GetFusePetConfig()


def GetPetTypeWeight():
    if IsRunPCData():
        return pc.GetPetTypeWeight()
    return mobile.GetPetTypeWeight()


def GetPetBuyPutWeight():
    if IsRunPCData():
        return pc.GetPetBuyPutWeight()
    return mobile.GetPetBuyPutWeight()


def GetPetOffsetLimit():
    if IsRunPCData():
        return pc.GetPetOffsetLimit()
    return mobile.GetPetOffsetLimit()


def GetPetAbilityByQuality(iQuality):
    if IsRunPCData():
        return pc.GetPetAbilityByQuality(iQuality)
    return mobile.GetPetAbilityByQuality(iQuality)


def GetPetAbilityGroup(iGroup):
    if IsRunPCData():
        return pc.GetPetAbilityGroup(iGroup)
    return mobile.GetPetAbilityGroup(iGroup)


def GetPetAbilityExclude(iAbility):
    if IsRunPCData():
        return pc.GetPetAbilityExclude(iAbility)
    return mobile.GetPetAbilityExclude(iAbility)


def GetAIMemberPetAbility():
    if IsRunPCData():
        return pc.GetAIMemberPetAbility()
    return mobile.GetAIMemberPetAbility()


def GetAITalentByHeroGrade(iHeroGrade):
    if IsRunPCData():
        return pc.GetAITalentByHeroGrade(iHeroGrade)
    return { }


def GetConquerPFWeight():
    if IsRunPCData():
        return pc.GetConquerPFWeight()
    return mobile.GetConquerPFWeight()


def GetWeaponTypeBySID(iWeapon):
    if IsRunPCData():
        return pc.GetWeaponTypeBySID(iWeapon)
    return mobile.GetWeaponTypeBySID(iWeapon)


def GetWeaponClassTag():
    if IsRunPCData():
        return pc.GetWeaponClassTag()
    return mobile.GetWeaponClassTag()


def GetHeroEmotion(iHeroSID, iGroup):
    if IsRunPCData():
        dHeroEmotion = pc.g_PCHeroToEm
    else:
        dHeroEmotion = mobile.g_HeroToEm
    tKey = (iHeroSID, iGroup)
    if tKey in dHeroEmotion:
        return dHeroEmotion[tKey]
    return 0


def GetWeaponSIDByType(iType):
    if IsRunPCData():
        return pc.GetWeaponSIDByType(iType)
    return mobile.GetWeaponSIDByType(iType)

if 'g_SeasonSuitcls' not in globals():
    g_SeasonSuitcls = { }

def GetSeasonSuitCls(iSID):
    if iSID not in g_SeasonSuitcls:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 'seasonsuit', 'seasonsuit%4d' % iSID)
        if not mod:
            return None
        g_SeasonSuitcls[iSID] = mod.CSuitData
    return g_SeasonSuitcls[iSID]


def GetSeasonSuit():
    if IsRunPCData():
        return pc.GetSeasonSuit()
    return { }


def GetSeasonSuitNotMain():
    if IsRunPCData():
        return pc.GetSeasonSuitNotMain()
    return { }


def GetSeasonSuitNotSub():
    if IsRunPCData():
        return pc.GetSeasonSuitNotSub()
    return { }


def GetCommonSeasonSuit():
    if IsRunPCData():
        return pc.GetCommonSeasonSuit()
    return mobile.GetCommonSeasonSuit()


def GetMinorSeasonSuit():
    if IsRunPCData():
        return pc.GetMinorSeasonSuit()
    return { }


def GetGameExcludeSeasonSuit(iPlayType):
    if IsRunPCData():
        return pc.GetGameExcludeSeasonSuit(iPlayType)
    return { }


def GetSeasonSuitExclude(iSuit):
    if IsRunPCData():
        return pc.GetSeasonSuitExclude(iSuit)
    return []


def GetSuitCoreRelicMap():
    if IsRunPCData():
        return pc.GetSuitCoreRelicMap()
    return mobile.GetSuitCoreRelicMap()


def GetSeasonSuitTag(iSuit):
    if IsRunPCData():
        return pc.GetSeasonSuitTag(iSuit)
    return mobile.GetSeasonSuitTag(iSuit)


def GetSeasonSuitByTag(iTag):
    if IsRunPCData():
        return pc.GetSeasonSuitByTag(iTag)
    return mobile.GetSeasonSuitByTag(iTag)


def GetSeasonSuitMain2Sub():
    if IsRunPCData():
        return pc.GetSeasonSuitMain2Sub()
    return { }


def GetSeasonSuitSub2Main():
    if IsRunPCData():
        return pc.GetSeasonSuitSub2Main()
    return { }


def GetCoreSeasonSuit():
    if IsRunPCData():
        return pc.GetCoreSeasonSuit()
    return { }


def GetLockSeasonSuitTemp():
    if IsRunPCData():
        return pc.GetLockSeasonSuitTemp()
    return mobile.GetLockSeasonSuitTemp()


def GetSeasonSuitTemplate():
    if IsRunPCData():
        return pc.GetSeasonSuitTemplate()
    return mobile.GetSeasonSuitTemplate()


def GetCardPackTemplate(iCardPack):
    if IsRunPCData():
        return pc.GetCardPackTemplate(iCardPack)
    return mobile.GetCardPackTemplate(iCardPack)


def GetTempCardPackPerform(iCardPack):
    if IsRunPCData():
        return pc.GetTempCardPackPerform(iCardPack)
    return mobile.GetTempCardPackPerform(iCardPack)


def GetCardPackMaxSuitNum(iCardPack):
    if IsRunPCData():
        return pc.GetCardPackMaxSuitNum(iCardPack)
    return mobile.GetCardPackMaxSuitNum(iCardPack)


def GetUnLockCardPackInfo():
    if IsRunPCData():
        return pc.GetUnLockCardPackInfo()
    return mobile.GetUnLockCardPackInfo()


def GetClassicCardPack():
    if IsRunPCData():
        return pc.GetClassicCardPack()
    return mobile.GetClassicCardPack()


def GetActiveSourceSuitMap():
    return pc.GetActiveSourceSuitMap()


def GetAllWandAbility():
    if IsRunPCData():
        return pcwandability.GetAllWandAbility()
    return { }


def GetWandAbilityByType(iType):
    if IsRunPCData():
        return pcwandability.GetWandAbilityByType(iType)
    return []


def GetWandAbilityByQuality(iQuality):
    if IsRunPCData():
        return pcwandability.GetWandAbilityByQuality(iQuality)
    return { }


def GetGWandPointAbility(iWandSID):
    if IsRunPCData():
        return pcwandability.GetGWandPointAbility(iWandSID)
    return 0


def GetPWandPointAbility(iWandSID):
    if IsRunPCData():
        return pcwandability.GetPWandPointAbility(iWandSID)
    return 0


def GetWandPointAbility(iWandSID):
    if IsRunPCData():
        return pcwandability.GetWandPointAbility(iWandSID)
    return []


def GetWandExcludeAbility(iAbilitySID):
    if IsRunPCData():
        return pcwandability.GetWandExcludeAbility(iAbilitySID)
    return []


def GetMonsterComAttInfo():
    return pc.GetMonsterComAttInfo()


def GetCommonActiveTag():
    if IsRunPCData():
        return pccommonative.GetCommonActiveTag()
    return mobilecommonative.GetCommonActiveTag()


def GetAllTask():
    if IsRunPCData():
        return pc.GetAllTask()
    return mobile.GetAllTask()


def GetTaskBeforeChooseCond():
    if IsRunPCData():
        return pc.GetTaskBeforeChooseCond()
    return mobile.GetTaskBeforeChooseCond()


def GetAllWand():
    if IsRunPCData():
        return pcwand.GetAllWand()
    return mobilewand.GetAllWand()


def GetAllPutWand():
    if IsRunPCData():
        return pcwand.GetAllPutWand()
    return mobilewand.GetAllPutWand()


def GetAllWandComp():
    if IsRunPCData():
        return pcwandcomp.GetAllWandComp()
    return mobilewandcomp.GetAllWandComp()


def GetWandPut(iPutSource):
    if IsRunPCData():
        return pcwand.GetWandPut(iPutSource)
    return mobilewand.GetWandPut(iPutSource)


def GetWandCompPut(iPutSource):
    if IsRunPCData():
        return pcwandcomp.GetWandCompPut(iPutSource)
    return mobilewandcomp.GetWandCompPut(iPutSource)


def GetWandCompType(iComp):
    if IsRunPCData():
        return pcwandcomp.GetWandCompType(iComp)
    return mobilewandcomp.GetWandCompType(iComp)


def GetWandCardPack():
    if IsRunPCData():
        return pcwand.GetWandCardPack()
    return { }


def GetWandByTag(iTag):
    if IsRunPCData():
        return pcwand.GetWandByTag(iTag)
    return []


def GetWandDropInfo(iWand):
    if IsRunPCData():
        return pcwand.GetWandDropInfo(iWand)
    return 0


def GetWandRecycleInfo(iWand):
    if IsRunPCData():
        return pcwand.GetWandRecycleInfo(iWand)
    return 0


def GetAllWandPresetTemp():
    if IsRunPCData():
        return pcwand.GetAllWandPresetTemp()
    return mobilewand.GetAllWandPresetTemp()


def GetWandCompByTag(iTag):
    if IsRunPCData():
        return pcwandcomp.GetWandCompByTag(iTag)
    return []


def GetWandCompByRarity(iRarity):
    if IsRunPCData():
        return pcwandcomp.GetWandCompByRarity(iRarity)
    return []


def GetAllWandCompRarity():
    if IsRunPCData():
        return pcwandcomp.GetAllWandCompRarity()
    return []


def GetWandCompDropInfo(iComp):
    if IsRunPCData():
        return pcwandcomp.GetWandCompDropInfo(iComp)
    return 0


def GetWandCompRecycleInfo(iComp):
    if IsRunPCData():
        return pcwandcomp.GetWandCompRecycleInfo(iComp)
    return 0


def GetMonsterAttrClassify():
    if IsRunPCData():
        return pc.GetMonsterAttrClassify()
    return mobile.GetMonsterAttrClassify()


def GetMonsterAfTag():
    return pc.GetMonsterAfTag()


def GetAllDiceAbility():
    if IsRunPCData():
        return pcdiceability.GetAllDiceAbility()
    return { }


def GetExcludeDiceQuality(iQuality):
    if IsRunPCData():
        return pcdiceability.GetExcludeDiceQuality(iQuality)
    return { }


def GetDiceTagListInfo(iDice):
    if IsRunPCData():
        return pcdiceability.GetDiceTagListInfo(iDice)
    return []


def GetAllDiceSpecialItem():
    if IsRunPCData():
        return pcdicespecialitem.GetAllDiceSpecialItem()
    return { }


def GetDiceSpecialItemTriggerEnergy(iDiceSpecialItem):
    if IsRunPCData():
        return pcdicespecialitem.GetDiceSpecialItemTriggerEnergy(iDiceSpecialItem)
    return 0


def GetDiceSpecialTypeList(iType):
    if IsRunPCData():
        return pcdicespecialitem.GetDiceSpecialTypeList(iType)
    return []


def GetSpItemBanBenedicList():
    if IsRunPCData():
        return pcdicespecialitem.GetSpItemBanBenedicList()
    return []

if IsRunPCData():
    
    def GetWandCompIcon(iComp):
        return pcwandcomp.GetWandCompIcon(iComp)

    
    def GetDiceTagInfo():
        return pcdiceability.GetDiceTagInfo()

    
    def GetDiceSpecialItemCanBuy(iDiceSpecialItem):
        return pcdicespecialitem.GetDiceSpecialItemCanBuy(iDiceSpecialItem)

    
    def GetWandCompIconColor():
        return pcwandcomp.GetWandCompIconColor()

    
    def CheckValidGardenerAim(iModel):
        return pcthrow.CheckValidGardenerAim(iModel)

    
    def GetGardenerAimThrowType(iModel):
        return pcthrow.GetGardenerAimThrowType(iModel)

    
    def GetDiceSpecialItemByQuality(iQuality):
        return pcdicespecialitem.GetDiceSpecialItemByQuality(iQuality)

    
    def GetAIDice():
        return pcdiceability.GetAIDice()

    
    def GetDiceByPutOutPoolType(iPoolType):
        return pcdiceability.GetDiceByPutOutPoolType(iPoolType)

    
    def GetDicePointMaxSameAssemblyNum(iSID):
        return pcdiceability.GetDicePointMaxSameAssemblyNum(iSID)

    
    def GetDiceAIMapping():
        return pcdiceability.GetDiceAIMapping()

    
    def GetGardenerAimThrowRadius(iModel):
        return pcthrow.GetGardenerAimThrowRadius(iModel)

    
    def GetGardenerAimThrowElementType(iModel):
        return pcthrow.GetGardenerAimThrowElementType(iModel)

    
    def GetGardenerAimThrowCreateMonsterInfo(iModel, iWarNo):
        return pcthrow.GetGardenerAimThrowCreateMonsterInfo(iModel, iWarNo)

    
    def GetDicePresetTemplateInfo():
        return pc.GetDicePresetTemplateInfo()

    
    def GetS7Module():
        return pcs7module.GetS7Module()

    
    def GetS7Passive():
        return pcseaonpassive.GetS7Passive()

    
    def GetS7Crystal():
        return pcs7crystal.GetS7Crystal()

    
    def GetTotalPoint2Crystal():
        return pcs7crystal.GetTotalPoint2Crystal()

    
    def GetS7CrystalByType(iType):
        return pcs7crystal.GetS7CrystalByType(iType)

    
    def GetS7CrystalType(iCrystal):
        return pcs7crystal.GetS7CrystalType(iCrystal)

    
    def GetS7CostPoint(iPoint):
        return pcs7crystal.GetS7CostPoint(iPoint)

    
    def GetTargetPointCrystal(iPoint):
        return pcs7crystal.GetTargetPointCrystal(iPoint)

    
    def GetModuleByMaxPoint(iMaxPoint):
        return pcs7module.GetModuleByMaxPoint(iMaxPoint)

    
    def GetAllS7Module():
        return pcs7module.GetAllS7Module()

    
    def GetS7ModuleByTag(iTag):
        return pcs7module.GetS7ModuleByTag(iTag)

    
    def GetModuleTag(iModule):
        return pcs7module.GetModuleTag(iModule)

    
    def GetModuleEquipNumMax(iModule):
        return pcs7module.GetModuleEquipNumMax(iModule)

    
    def GetRelicByTag(iTag):
        return pc.GetRelicByTag(iTag)

    
    def GetExclusionCrystal(iCrystal):
        return pcs7crystal.GetExclusionCrystal(iCrystal)

    
    def GetCrystalTypePoint():
        return pcs7crystal.GetCrystalTypePoint()

    
    def GetClientActiveTag():
        return pcclientactive.GetClientActiveTag()

    
    def GetS8GemItem():
        return pcs8gemitem.GetS8GemItem()

    
    def GetS8ThirdItem():
        return pcs8thirditem.GetS8ThirdItem()

    
    def GetS8Passive():
        return pcseaonpassive.GetS8Passive()

    
    def GetS8Ability():
        return pcseaonpassive.GetS8Ability()

    
    def GetS8PassiveByTag(iTag):
        return pcseaonpassive.GetS8PassiveByTag(iTag)

    
    def GetThirdItemSpecialAbility(iItemSID):
        return pcseaonpassive.GetThirdItemSpecialAbility(iItemSID)

    
    def GetS7SpecialPassive():
        return pcs7specialpassive.GetS7SpecialPassive()

    
    def GetThirdAbilityChooseRule(iQuality):
        return pcs8thirditem.GetThirdAbilityChooseRule(iQuality)

    
    def GetThirdAbilityNum(iQuality):
        return pcs8thirditem.GetThirdAbilityNum(iQuality)

else:
    
    def GetWandCompIcon(iComp):
        return 0

    
    def GetDiceTagInfo():
        return { }

    
    def GetDiceSpecialItemCanBuy(iDiceSpecialItem):
        return 0

    
    def GetWandCompIconColor():
        return { }

    
    def CheckValidGardenerAim(iModel):
        return False

    
    def GetGardenerAimThrowType(iModel):
        return 0

    
    def GetDiceSpecialItemByQuality(iQuality):
        return { }

    
    def GetAIDice():
        return []

    
    def GetDiceByPutOutPoolType(iPoolType):
        return { }

    
    def GetDicePointMaxSameAssemblyNum(iSID):
        return 0

    
    def GetDiceAIMapping():
        return { }

    
    def GetGardenerAimThrowRadius(iModel):
        return 0

    
    def GetGardenerAimThrowElementType(iModel):
        return 0

    
    def GetGardenerAimThrowCreateMonsterInfo(iModel, iWarNo):
        return 0

    
    def GetDicePresetTemplateInfo():
        return { }

    
    def GetS7Module():
        return { }

    
    def GetS7Passive():
        return { }

    
    def GetS7Crystal():
        return { }

    
    def GetTotalPoint2Crystal():
        return { }

    
    def GetS7CrystalByType(iType):
        return { }

    
    def GetS7CrystalType(iType):
        return 0

    
    def GetS7CostPoint(iPoint):
        return { }

    
    def GetTargetPointCrystal(iPoint):
        return { }

    
    def GetModuleByMaxPoint(iMaxPoint):
        return { }

    
    def GetAllS7Module():
        return { }

    
    def GetS7ModuleByTag(iTag):
        return { }

    
    def GetModuleTag(iModule):
        return { }

    
    def GetModuleEquipNumMax(iModule):
        return { }

    
    def GetRelicByTag(iTag):
        return { }

    
    def GetExclusionCrystal(iCrystal):
        return { }

    
    def GetCrystalTypePoint():
        return { }

    
    def GetClientActiveTag():
        return { }

    
    def GetS8GemItem():
        return { }

    
    def GetS8ThirdItem():
        return { }

    
    def GetS8Passive():
        return { }

    
    def GetS8Ability():
        return pcseaonpassive.GetS8Ability()

    
    def GetS8PassiveByTag(iTag):
        return { }

    
    def GetThirdItemSpecialAbility(iItemSID):
        return { }

    
    def GetS7SpecialPassive():
        return { }

    
    def GetThirdAbilityChooseRule(iQuality):
        return { }

    
    def GetThirdAbilityNum(iQuality):
        return 0

