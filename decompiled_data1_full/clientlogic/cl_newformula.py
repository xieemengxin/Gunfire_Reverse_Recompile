# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_newformula.pyc
# RelativePath: clientlogic/cl_newformula.pyc
# Source Generated with Decompyle++
# File: cl_newformula.pyc (Python 3.6)

from cl_commondefines import PF_TYPE_DEVICECOMP, PF_TYPE_BENEDICTION, RELIC_TYPE_CURSE, PF_TYPE_TALENT, WARRIOR_NORMAL, WARRIOR_ELITE, WARRIOR_BOSS, WARRIOR_MONSTER, WARRIOR_BARRIER, WARRIOR_HERO, ABNORMAL_DEFAULT, RIDING_ALONE, PLAYMODE_SURVIVOR, PF_TYPE_RELIC, NWARRIOR_NPC, PF_TYPE_CAREERPF, PF_TYPE_THROW, FLAW_KILLLINE, FLAW_UNBALANCE_EFFECTTIME, WARRIOR_PET_MINI, WARRIOR_PET_MINICLONE
from cl_commondefines import DAM_TYPE_FIRE, DAM_TYPE_CORRISION, DAM_TYPE_THUNDER, DAM_TYPE_ELEMENT, EXECUTOR_HERO, RELIC_TYPE_NORMAL, FLAW_UNBALANCE_IMMOBILIZETIME, WARRIOR_DEVICE, LEVEL_TYPE_FIGHT, INKMASTER_HERO, TOXIC_FOG, LEVEL_TYPE_BOSS, SUIT_ELEMENT, ALL_ELEMENT_RELIC, REASON_COSTBULLET_ATTACK, REASON_COSTBULLET_BULLETCHANGE, WAND_COMP_TYPE_ACTION, NO_THROW_PERFORM_CASE, WAND_COMP_TYPE_ACTION, GARDENER_HERO, MAX_LAYER
from cl_commondefines import WAND_COMP_TYPE_CONDITION, WUKONG_HERO, BOSS_DONOT_COUNT, NWARRIOR_DROP_BULLET
from cl_item.defines import QUALITY_TYPE_HIGH, QUALITY_TYPE_NORMAL, QUALITY_TYPE_LOW, QUALITY_TYPE_CURSE
from cl_only import Frame2Time, PY_FLAG_DEAD, SendAlert, ChooseKey, GAME_FRAME_TIME
from cl_object.logging import SkillLog, ErrLog
from cl_item.defines import MAIN_HOLD, DEPUTY_HOLD, EQUIP_TYPE_MAINWEAPON
from cl_abnormalconf import GetAbnormalEleTime, g_AllAbnormalStateSID
from cl_platformdata import GetSuitCoreRelicMap, GetSeasonSuitCls, GetSeasonSuitTag, GetLimitSeasonBened, GetDiceTagListInfo, GetModuleTag, GetS7ModuleByTag
from typing import TypeVar, get_type_hints
import math
import types
import itertools
import cl_math
import cl_perform
import cl_action
import cl_object.linkattr
import cl_item.defines as itemdef
import cl_formula
MAX_DAMAGE = 0x31FFFFED40
Attr = TypeVar('Attr', str, bytes)
FML_ARG_STDICT = 1
FML_ARG_SKILLOBJ = 2
FML_ARG_PASSIVE = 3
FML_ARG_VOBJ = 4
FML_ARG_VID = 5
FML_ARG_DAM = 6
FML_ARG_LV = 7
FML_ARG_SIDE = 8
FML_ARG_SEC = 9
FML_ARG_ITEM = 10
FML_ARG_AOBJ = 11
FML_ARG_AID = 12
FML_ARG_BASEDAM = 13
FML_ARG_ITEMINFO = 14
FML_ARG_OBJ = 15
FML_ARG_MSGINFO = 16

def AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo:
        return None
    if 'AID' in dMsgInfo:
        iAttack = dMsgInfo['AID']
    elif 'Skill' in dMsgInfo:
        iAttack = dMsgInfo['Skill'].m_Base['AID']
    else:
        iAttack = 0
    return obj.m_Game.GetObject(iAttack, PY_FLAG_DEAD)


def AnalyseVictim(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo:
        return 0
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    elif 'Skill' in dMsgInfo:
        iVictim = dMsgInfo['Skill'].m_Base['VID']
    else:
        iVictim = 0
    return iVictim


def AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs, iFiltDead = 1):
    if not dMsgInfo:
        return None
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    elif 'Skill' in dMsgInfo:
        iVictim = dMsgInfo['Skill'].m_Base['VID']
    else:
        iVictim = 0
    if iFiltDead:
        return obj.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    return obj.m_Game.GetObject(iVictim)


def AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs):
    if dOtherArgs and 'Weapon' in dOtherArgs:
        return dOtherArgs['Weapon']
    if dMsgInfo:
        oSkill = None
        iWeapon = 0
        iAttack = 0
        if 'Skill' in dMsgInfo:
            oSkill = dMsgInfo['Skill']
            iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
            iAttack = oSkill.m_Base['AID']
        elif 'ItemID' in dMsgInfo:
            iWeapon = dMsgInfo['ItemID']
        if iWeapon:
            if not iAttack and 'AID' in dMsgInfo:
                iAttack = dMsgInfo['AID']
            oAttack = obj.m_Game.GetObject(iAttack)
            if oAttack and oAttack.m_FightType & WARRIOR_HERO:
                oWeapon = oAttack.m_WieldCon.GetItemByID(iWeapon)
                if oWeapon:
                    return oWeapon


def GetStateAttack(obj, dData):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if not oState:
        return None
    return obj.m_Game.GetObject(oState.m_Attacker)


def Func10(obj, dData, dMsgInfo, dOtherArgs):
    return dData[FML_ARG_LV]


def Func11(obj, dData, dMsgInfo, dOtherArgs, iVal):
    if iVal < 0:
        iSign = -1
    elif iVal > 0:
        iSign = 1
    else:
        iSign = 0
    iTemp = abs(iVal)
    return obj.m_Game.Random(iTemp) * iSign


def Func13(obj, dData, dMsgInfo, dOtherArgs, *args):
    lstTmp = args[1:]
    dInfo = dict(enumerate(lstTmp))
    iPlayerCnt = obj.m_Game.m_WarMgr.GetAllPlayerCnt()
    if iPlayerCnt - 1 not in dInfo:
        return 0
    iFactor = dInfo[iPlayerCnt - 1]
    return iFactor


def Func14(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_Game.GetFrameNum()


def Func16(obj, dData, dMsgInfo, dOtherArgs, a, b):
    iRandMin = int(a * 100)
    iRandMax = int(b * 100)
    return (iRandMin + obj.m_Game.Random(max(0, iRandMax - iRandMin))) / 100


def Func17(obj, dData, dMsgInfo, dOtherArgs, a, b):
    if 'RandCache' in dData:
        return dData['RandCache']
    iRandMin = int(a * 100)
    iRandMax = int(b * 100)
    iRet = (iRandMin + obj.m_Game.Random(max(0, iRandMax - iRandMin))) / 100
    dData['RandCache'] = iRet
    return iRet


def Func105(obj, dData, dMsgInfo, dOtherArgs):
    iShieldMax = obj.ShieldMax()
    iShield = obj.Shield()
    fRatio = iShield / iShieldMax if iShieldMax > 0 else 0
    return fRatio


def Func201(obj, dData, dMsgInfo, dOtherArgs):
    if dData and 'Layer' in dData:
        return dData['Layer']
    oLevelCtrl = obj.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    iLayer = 0
    if oLevelCtrl:
        (iLayer, _) = oLevelCtrl.GetLayerAndLevelMap(oLevelCtrl.m_LayerNum, oLevelCtrl.m_LevelNum)
    if dData and 'MaxLayer' in dData and iLayer > dData['MaxLayer']:
        return dData['MaxLayer']
    return iLayer


def Func202(obj, dData, dMsgInfo, dOtherArgs):
    oLevelCtrl = obj.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    iLevel = 0
    iLayer = 1
    if oLevelCtrl:
        (iLayer, iLevel) = oLevelCtrl.GetLayerAndLevelMap(oLevelCtrl.m_LayerNum, oLevelCtrl.m_LevelNum)
    if dData and 'MaxLayer' in dData:
        if (iLayer > dData['MaxLayer'] or dData['MaxLayer'] == iLayer) and iLevel > dData['MaxLevel']:
            return dData['MaxLevel']
    return iLevel


def Func203(obj, dData, dMsgInfo, dOtherArgs):
    if 'QualityCoff' not in dData:
        return 0
    return dData['QualityCoff'] / 100


def Func204(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_Game.m_WarMgr.GetAllPlayerCnt()


def Func205(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_Game.m_WarMgr.m_Round


def Func206(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_WarGSCash


def Func207(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_WarCash


def Func208(obj, dData, dMsgInfo, dOtherArgs):
    return dMsgInfo['Cost']


def Func209(obj, dData, dMsgInfo, dOtherArgs):
    oWarMgr = obj.m_Game.m_WarMgr
    oElement = oWarMgr.GetComponent('TeammateAI')
    if oElement and oElement.m_InitPlayerNum:
        return oElement.m_InitPlayerNum
    return oWarMgr.GetAllPlayerCnt()


def Func210(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_RELIC:
            continue
        if oPerform.m_RelicType == RELIC_TYPE_CURSE:
            iCount += 1
    
    iAddingRelic = dMsgInfo['NewRelic'] if dMsgInfo and 'NewRelic' in dMsgInfo else 0
    if iAddingRelic:
        iAddingRelicType = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_RelicType')
        if iAddingRelicType == RELIC_TYPE_CURSE:
            iCount += 1
    return iCount


def Func211(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_FightType & NWARRIOR_NPC and FML_ARG_VID in dData:
        oNpc = obj
        iVictim = dData[FML_ARG_VID]
    elif obj.m_FightType & WARRIOR_HERO and 'Npc' in dData:
        oNpc = obj.m_Game.GetObject(dData['Npc'])
        iVictim = obj.m_ID
    else:
        return 0
    if not oNpc:
        return 0
    dTimes = oNpc.Query('HeroRefreshTimes', { })
    if iVictim in dTimes:
        return dTimes[iVictim]
    return 0


def Func212(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    return obj.GetArgValue(sAttr)


def Func213(obj, dData, dMsgInfo, dOtherArgs):
    if 'Debuff' not in dMsgInfo:
        return 0
    dDebuffInfo = dMsgInfo['Debuff']
    iDebuffTime = dDebuffInfo['DebuffTime']
    return iDebuffTime


def Func214(obj, dData, dMsgInfo, dOtherArgs):
    if dMsgInfo['Reason'] not in (REASON_COSTBULLET_ATTACK, REASON_COSTBULLET_BULLETCHANGE):
        return 0
    iChange = dMsgInfo['Amount']
    iCost = -iChange if iChange < 0 else 0
    return iCost


def Func215(obj, dData, dMsgInfo, dOtherArgs):
    if dMsgInfo['Reason'] == 'fillbullet':
        return 0
    iChange = dMsgInfo['Amount']
    iCost = -iChange if iChange < 0 else 0
    return iCost


def Func216(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_RELIC:
            continue
        if oPerform.m_Quality == QUALITY_TYPE_HIGH and oPerform.m_RelicType != RELIC_TYPE_CURSE:
            iCount += 1
    
    iAddingRelic = dMsgInfo['NewRelic'] if dMsgInfo and 'NewRelic' in dMsgInfo else 0
    if iAddingRelic:
        iAddingRelicQuality = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_Quality')
        iAddingRelicType = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_RelicType')
        if iAddingRelicQuality == QUALITY_TYPE_HIGH and iAddingRelicType != RELIC_TYPE_CURSE:
            iCount += 1
    return iCount


def Func217(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not sAttr:
        return 0
    if not obj.m_Scene:
        return 0
    oGame = obj.m_Game
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    if sAttr in oScene.m_CustomData:
        return oScene.m_CustomData[sAttr]
    return 0


def Func218(obj, dData, dMsgInfo, dOtherArgs):
    oGame = obj.m_Game
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    iCnt = 0
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero)
        if not oHero or oHero.IsDead():
            continue
        iCnt += 1
    
    return iCnt


def Func219(obj, dData, dMsgInfo, dOtherArgs):
    if 'RelicSID' not in dData:
        return 0
    iCost = cl_perform.GetPerformClassAttr(dData['RelicSID'], 'm_BasePrice')
    if iCost:
        return iCost
    return 0


def Func220(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_PlayerGrade


def Func221(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_Game.m_WarMgr.m_Cycle


def Func222(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_RELIC:
            continue
        iCount += 1
    
    if dMsgInfo and 'NewRelic' in dMsgInfo and dMsgInfo['NewRelic']:
        iCount += 1
    return iCount


def Func223(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_TalentCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_TALENT:
            continue
        iCount += oPerform.m_Level
    
    return iCount


def Func224(obj, dData, dMsgInfo, dOtherArgs):
    oGame = obj.m_Game
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    iCnt = 0
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero)
        if oHero.IsDeadNoDying():
            continue
        iCnt += 1
    
    return iCnt


def Func225(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWarMgr = obj.m_Game.m_WarMgr
    oRoundElement = oWarMgr.GetComponent('RoundElement')
    if sAttr in oRoundElement.m_MonsterAdjust:
        return oRoundElement.m_MonsterAdjust[sAttr] / 10000
    return 0


def Func226(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_RELIC:
            continue
        if oPerform.m_Quality == QUALITY_TYPE_NORMAL and oPerform.m_RelicType != RELIC_TYPE_CURSE:
            iCount += 1
    
    iAddingRelic = dMsgInfo['NewRelic'] if dMsgInfo and 'NewRelic' in dMsgInfo else 0
    if iAddingRelic:
        iAddingRelicQuality = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_Quality')
        iAddingRelicType = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_RelicType')
        if iAddingRelicQuality == QUALITY_TYPE_NORMAL and iAddingRelicType != RELIC_TYPE_CURSE:
            iCount += 1
    return iCount


def Func227(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_RELIC:
            continue
        if oPerform.m_Quality == QUALITY_TYPE_LOW and oPerform.m_RelicType != RELIC_TYPE_CURSE:
            iCount += 1
    
    iAddingRelic = dMsgInfo['NewRelic'] if dMsgInfo and 'NewRelic' in dMsgInfo else 0
    if iAddingRelic:
        iAddingRelicQuality = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_Quality')
        iAddingRelicType = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_RelicType')
        if iAddingRelicQuality == QUALITY_TYPE_LOW and iAddingRelicType != RELIC_TYPE_CURSE:
            iCount += 1
    return iCount


def Func228(obj, dData, dMsgInfo, dOtherArgs):
    oSurvivorElement = obj.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if oSurvivorElement:
        dPhaseInfo = oSurvivorElement.m_PhaseConfig[oSurvivorElement.m_ConfigSID]
        iExpectedNumber = dPhaseInfo[oSurvivorElement.m_Phase]['ExpectedMonsterNumber']
        return iExpectedNumber
    return 0


def Func229(obj, dData, dMsgInfo, dOtherArgs):
    oSurvivorElement = obj.m_Game.m_WarMgr.GetComponent('SurvivorElement')
    if not oSurvivorElement:
        return 0
    return oSurvivorElement.m_UpgradeMgr.GetHeroGrade(obj.m_ID)


def Func230(obj, dData, dMsgInfo, dOtherArgs):
    if 'TalentType' not in dMsgInfo:
        return 0
    iTalentType = dMsgInfo['TalentType']
    oTalentCon = obj.m_TalentCon
    if iTalentType in oTalentCon.m_TalentTypeInfo:
        return oTalentCon.m_TalentTypeInfo[iTalentType]
    return 0


def Func231(obj, dData, dMsgInfo, dOtherArgs):
    oGame = obj.m_Game
    lstHero = oGame.m_WarMgr.GetRoomHero()
    if not lstHero:
        return 0
    iCnt = 0
    iTotalGrade = 0
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        iCnt += 1
        iTotalGrade += oHero.m_PlayerGrade
    
    if not iCnt:
        return 0
    return iTotalGrade // iCnt


def Func232(obj, dData, dMsgInfo, dOtherArgs):
    if 'Cost' in dMsgInfo:
        return dMsgInfo['Cost']
    return 0


def Func234(obj, dData, dMsgInfo, dOtherArgs):
    return obj.Query('UnlockBlocPoskNum') - obj.Query('UsedBlocPoskNum')


def Func235(obj, dData, dMsgInfo, dOtherArgs, sType):
    oWarMgr = obj.m_Game.m_WarMgr
    if sType == RIDING_ALONE:
        iPlayerCnt = oWarMgr.Query('GMSpawnCnt')
        if iPlayerCnt:
            return iPlayerCnt
        oRidingAloneElement = oWarMgr.GetComponent('RidingAloneElement')
        if oRidingAloneElement:
            return oRidingAloneElement.m_SpawnCnt
    return oWarMgr.GetAllPlayerCnt()


def Func236(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    oScene = obj.m_Game.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return iCount
    iCount = oScene.m_SceneData.m_MonsterNum[obj.m_ID] if obj.m_ID in oScene.m_SceneData.m_MonsterNum else 0
    return iCount


def Func237(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_Game.m_WarMgr.m_PlayMode != PLAYMODE_SURVIVOR:
        return 0
    oLevelCtrl = obj.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    if oLevelCtrl and oLevelCtrl.m_CurNode:
        iLevel = oLevelCtrl.m_CurNode.m_Level
        if iLevel:
            return oLevelCtrl.GetLevelLayer(iLevel)
        return 0
    return 0


def Func238(obj, dData, dMsgInfo, dOtherArgs):
    oSurvivor = obj.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
    if oSurvivor:
        iSecond = Frame2Time(obj.m_Game.GetFrameNum() - oSurvivor.m_PhaseStartFrame - oSurvivor.m_PauseTotalFrame) / 100
        iFightSecond = oSurvivor.m_PhaseData[oSurvivor.m_Phase]['FightTime'] / 100
        if iFightSecond > iSecond:
            return math.ceil(iFightSecond - iSecond)
    return 0


def Func239(obj, dData, dMsgInfo, dOtherArgs, iType):
    pfobj = dData['LifeCycle'].GetObject()
    if not pfobj:
        return 0
    if iType > 2:
        return 0
    dSampleWeaponInfo = pfobj.GetArgValue('SampleWeaponInfo')
    if not dSampleWeaponInfo:
        return 0
    return sum((x[iType] for x in dSampleWeaponInfo.values()))


def Func240(obj, dData, dMsgInfo, dOtherArgs):
    iNpcID = 0
    if 'NpcID' in dMsgInfo:
        iNpcID = dMsgInfo['NpcID']
    elif 'ShopNpc' in dMsgInfo:
        iNpcID = dMsgInfo['ShopNpc']
    return iNpcID


def Func241(obj, dData, dMsgInfo, dOtherArgs):
    oSurvivor = obj.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
    iFightTime = 0
    if oSurvivor:
        iFightTime = oSurvivor.m_PhaseData[oSurvivor.m_Phase]['FightTime']
    return iFightTime


def Func242(obj, dData, dMsgInfo, dOtherArgs):
    return len(obj.m_OccuptPlayer)


def Func243(obj, dData, dMsgInfo, dOtherArgs):
    iMGID = 0
    if 'MGID' in dMsgInfo:
        iMGID = dMsgInfo['MGID']
    return iMGID


def Func244(obj, dData, dMsgInfo, dOtherArgs):
    oWarMgr = obj.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    return oLevelCtrl.GetLevelCount(LEVEL_TYPE_FIGHT)


def Func245(obj, dData, dMsgInfo, dOtherArgs):
    oWarMgr = obj.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    return oLevelCtrl.GetLevelCount(LEVEL_TYPE_BOSS)


def Func246(obj, dData, dMsgInfo, dOtherArgs):
    oGame = obj.m_Game
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    return oScene.m_Level


def Func247(obj, dData, dMsgInfo, dOtherArgs):
    oLevelCtrl = obj.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    if oLevelCtrl and oLevelCtrl.m_CurNode:
        return oLevelCtrl.m_CurNode.m_Level
    return 0


def Func248(obj, dData, dMsgInfo, dOtherArgs):
    oWarMgr = obj.m_Game.m_WarMgr
    oReport = oWarMgr.GetComponent('Warreport')
    if not oReport:
        return 0
    return oReport.m_WarReportData.GetPlayerWarInfo(obj.m_PlayerID, 'LastTalent')


def Func301(obj, dData, dMsgInfo, dOtherArgs):
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    if oAttack:
        return oAttack.HP() + oAttack.Shield()
    return 0


def Func302(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim:
        iTrueVictim = oVictim.Query('TentacleOwner', 0)
        oVictim = obj.m_Game.GetObject(iTrueVictim) if iTrueVictim else oVictim
    if oVictim:
        return GetWarriorAttr(sAttr, oVictim)
    return 0


def Func303(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if sAttr not in oSkill.m_Cache:
        return 0
    return oSkill.m_Cache[sAttr]


def Func304(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    return GetWarriorAttr(sAttr, obj)


def Func305(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    if oAttack:
        return GetWarriorAttr(sAttr, oAttack)
    return 0


def Func306(obj, dData, dMsgInfo, dOtherArgs):
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oAttack:
        return 0
    iHP = oAttack.HP()
    iHPMax = oAttack.QueryAttr('HPMax')
    fRatio = iHP / iHPMax if iHPMax > 0 else 0
    return fRatio


def Func307(obj, dData, dMsgInfo, dOtherArgs):
    iHP = obj.HP()
    iHPMax = obj.QueryAttr('HPMax')
    fRatio = iHP / iHPMax if iHPMax > 0 else 0
    return fRatio


def Func308(obj, dData, dMsgInfo, dOtherArgs):
    if 'PFLV' in dData:
        return dData['PFLV']
    oPerform = dData['LifeCycle'].GetObject()
    return oPerform.GetLifeCycleLevel()


def Func309(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'BaseBullet' in oSkill.m_Collect:
        iBase = oSkill.m_Collect['BaseBullet']
    else:
        iBase = 0
        SkillLog.Error('Func309获取基础子弹消耗失败 战场ID%s 技能SID%d' % (oSkill.m_Game.m_ID, oSkill.m_Base['pfid']))
    iExt = oSkill.m_Collect['ExtBulletUse'] if 'ExtBulletUse' in oSkill.m_Collect else 0
    iRet = iBase + iExt
    if 'SpecialBullet' in oSkill.m_Collect:
        iRet += oSkill.m_Collect['SpecialBullet']
    return iRet


def Func310(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    clsPerform = cl_perform.GetPerformModule(iPerform)
    if not clsPerform:
        return 0
    return clsPerform.m_BulletUse


def Func311(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim:
        return oVictim.HP()
    return 0


def Func312(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim:
        return oVictim.Shield()
    return 0


def Func313(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim:
        return oVictim.Armor()
    return 0


def Func314(obj, dData, dMsgInfo, dOtherArgs):
    iArmorMax = obj.QueryAttr('ArmorMax')
    iArmor = obj.Armor()
    fRatio = iArmor / iArmorMax if iArmorMax > 0 else 0
    return fRatio


def Func315(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iRet = oSkill.m_Collect['RealBullet'] if 'RealBullet' in oSkill.m_Collect else 0
    if 'SpecialBullet' in oSkill.m_Collect:
        iRet += oSkill.m_Collect['SpecialBullet']
    return iRet


def Func321(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iItem = oSkill.m_Base['Weapon']
    oWeapon = obj.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return 0
    iMax = oWeapon.m_ExtItemAttr['MaxBeacon'] if 'MaxBeacon' in oWeapon.m_ExtItemAttr else 0
    return min(iMax, oSkill.m_CacheData.m_BeaconCount)


def Func322(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim or not oAttack:
        return 0
    return cl_math.CalDistance3D(oVictim.GetPos(), oAttack.GetPos())


def Func323(obj, dData, dMsgInfo, dOtherArgs):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iLost = dMsgInfo['TotalDam'][0]
    iShieldMax = oVictim.ShieldMax()
    return iLost * 100 // iShieldMax


def Func324(obj, dData, dMsgInfo, dOtherArgs):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iLost = dMsgInfo['TotalDam'][2]
    iHPMax = oVictim.QueryAttr('HPMax')
    return iLost * 100 // iHPMax


def Func325(obj, dData, dMsgInfo, dOtherArgs):
    iHPMax = obj.QueryAttr('HPMax')
    iHp = obj.HP()
    iShieldMax = obj.ShieldMax()
    iShield = obj.Shield()
    return (iHPMax + iShieldMax - iHp - iShield) * 100 // (iHPMax + iShieldMax)


def Func326(obj, dData, dMsgInfo, dOtherArgs):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    return sum(dMsgInfo['TotalDam'])


def Func327(obj, dData, dMsgInfo, dOtherArgs):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iHPMax = obj.QueryAttr('HPMax')
    iShieldMax = obj.ShieldMax()
    iArmorMax = obj.QueryAttr('ArmorMax')
    return sum(dMsgInfo['TotalDam']) * 100 // (iHPMax + iShieldMax + iArmorMax)


def Func330(obj, dData, dMsgInfo, dOtherArgs, sid):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    fRatio = cl_action.CalCrtFlyDis(oSkill, sid) / cl_action.CalCrtFlyMaxDis(oSkill, sid)
    return fRatio


def Func331(obj, dData, dMsgInfo, dOtherArgs, sid):
    oTalent = obj.m_TalentCon.GetPerform(sid)
    if oTalent:
        return oTalent.m_Level
    return 0


def Func332(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_TalentCon.GetAllTalentLevelSum()


def Func333(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iHPNow = oVictim.HP()
    iHPMax = oVictim.QueryAttr('HPMax')
    return (iHPMax - iHPNow) / iHPMax


def Func334(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iHPNow = oVictim.HP()
    iHPMax = oVictim.QueryAttr('HPMax')
    return iHPMax - iHPNow


def Func335(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if not oSkill.m_Base['Weapon']:
        return 0
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
        return 0
    oWeapon = oAttack.m_WieldCon.GetItemByID(oSkill.m_Base['Weapon'])
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.Bullet()


def Func336(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if sKey in oSkill.m_Collect:
        return oSkill.m_Collect[sKey]
    return 0


def Func337(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dTriggerCartoon = oSkill.m_Collect['TriggerCartoon'] if 'TriggerCartoon' in oSkill.m_Collect else { }
    if not dTriggerCartoon:
        return 0
    dCurCartoon = oSkill.GetCurCartoon()
    if not dCurCartoon:
        return 0
    iCurCartoon = dCurCartoon['ID']
    if iCurCartoon in dTriggerCartoon:
        iValue = dTriggerCartoon[iCurCartoon]
    elif 'Parent' in dCurCartoon:
        iValue = dTriggerCartoon[dCurCartoon['Parent']] if dCurCartoon['Parent'] in dTriggerCartoon else 0
    else:
        iValue = 0
    return iValue


def Func338(obj, dData, dMsgInfo, dOtherArgs):
    if 'TriggerNum' in dMsgInfo:
        return dMsgInfo['TriggerNum']
    return 0


def Func339(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'LastVLST' not in oSkill.m_Update:
        return 0
    return len(oSkill.m_Update['LastVLST'])


def Func340(obj, dData, dMsgInfo, dOtherArgs, sKey, iAddExtInfo = 0):
    sKey = 'MoveDis%s' % sKey
    if iAddExtInfo:
        oLifeCycle = dData['LifeCycle']
        sKey = '%s-%s' % (oLifeCycle.Key(), sKey)
    (_, fDis) = obj.Query(sKey, (0, 0))
    return int(fDis)


def Func341(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_Phase


def Func343(obj, dData, dMsgInfo, dOtherArgs, sid):
    oBulletContainer = obj.m_BulletCon
    return oBulletContainer.Bullet(sid)


def Func344(obj, dData, dMsgInfo, dOtherArgs):
    if 'TotalCure' not in dMsgInfo:
        return 0
    return sum(dMsgInfo['TotalCure'])


def Func345(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iUse = oSkill.m_Collect['BulletUse'] if 'BulletUse' in oSkill.m_Collect else 0
    if iUse == 0:
        return iUse
    if 'BulletCountSigln' not in oSkill.m_Update:
        oSkill.m_Update['BulletCountSigln'] = 0
    oSkill.m_Update['BulletCountSigln'] += iUse
    if oSkill.m_Update['BulletCountSigln'] <= oSkill.m_Collect['BulletUse']:
        return iUse
    return 0


def Func346(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if not oSkill.m_Base['Weapon']:
        return 0
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
        return 0
    oWeapon = oAttack.m_WieldCon.GetItemByID(oSkill.m_Base['Weapon'])
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    iBulletSID = oBulletCom.m_BulletType
    return obj.m_BulletCon.GetMaxBullet(iBulletSID)


def Func347(obj, dData, dMsgInfo, dOtherArgs, sid):
    oBulletContainer = obj.m_BulletCon
    return oBulletContainer.GetMaxBullet(sid)


def Func349(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_Owner:
        SendAlert('err', '召唤物%d没有拥有者' % obj.m_SID)
        return 0
    oOwner = obj.m_Game.GetObject(obj.m_Owner)
    if not oOwner.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
        return 0
    return oOwner.m_Phase


def Func350(obj, dData, dMsgInfo, dOtherArgs):
    return obj.QueryAttr('ModelRadius')


def Func351(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if not oSkill.m_Base['Weapon']:
        return 0
    oAttack = oSkill.GetAttack()
    if not oAttack or not (oAttack.m_FightType & WARRIOR_HERO):
        return 0
    oWeapon = oAttack.m_WieldCon.GetItemByID(oSkill.m_Base['Weapon'])
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    iBulletSID = oBulletCom.m_BulletType
    return obj.m_BulletCon.Bullet(iBulletSID)


def Func352(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo or 'CurHitPos' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    oCurHitPos = dMsgInfo['CurHitPos']
    dCurCartoon = oSkill.GetCurCartoon()
    if 'End' not in dCurCartoon:
        return 0
    return cl_math.CalDistance(oCurHitPos, dCurCartoon['End'])


def Func353(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo:
        return 0
    if 'Radius' in dMsgInfo:
        return dMsgInfo['Radius']
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'Radius' not in oSkill.m_Cache:
        return 0
    return oSkill.m_Cache['Radius']


def Func354(obj, dData, dMsgInfo, dOtherArgs):
    if 'ExcessChange' not in dMsgInfo:
        return 0
    if isinstance(dMsgInfo['ExcessChange'], int):
        return dMsgInfo['ExcessChange']
    if not dMsgInfo['ExcessChange']:
        return 0
    iValue = 0
    for lstDam in dMsgInfo['ExcessChange']:
        iValue += lstDam[0]
    
    return iValue


def Func355(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'FillTime' not in oSkill.m_Cache:
        return 0
    return oSkill.m_Cache['FillTime']


def Func356(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oAttack:
        return 0
    dCurCartoon = oSkill.GetCurCartoon()
    if 'End' not in dCurCartoon:
        return 0
    return cl_math.CalDistance(oAttack.GetPos(), dCurCartoon['End'])


def Func357(obj, dData, dMsgInfo, dOtherArgs):
    if 'MainCure' not in dMsgInfo:
        return 0
    lstChange = dMsgInfo['MainCure']
    if 'FlowCure' in dMsgInfo and dMsgInfo['FlowCure']:
        lstChange += dMsgInfo['FlowCure']
    iTotalChange = 0
    for iChange, oReason in lstChange:
        iTotalChange += iChange
    
    return iTotalChange


def Func358(obj, dData, dMsgInfo, dOtherArgs, sid, sKey):
    oPerform = obj.m_Perform.GetPerform(sid)
    if not oPerform:
        return 0
    if sKey in oPerform.m_BaseAttrData:
        return oPerform.m_BaseAttrData[sKey]
    return 0


def Func359(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'lstVLST' not in oSkill.m_Collect:
        return 0
    return len(oSkill.m_Collect['lstVLST'])


def Func360(obj, dData, dMsgInfo, dOtherArgs, sid, sAttr):
    oPerform = obj.GetPerform(sid)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def Func361(obj, dData, dMsgInfo, dOtherArgs, sid, sArgs):
    oPerform = obj.GetPerform(sid)
    if not oPerform:
        return 0
    return oPerform.GetArgValue(sArgs)


def Func362(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    iValue = GetWarriorAttr(sAttr, obj)
    oAttr = obj.GetAttr(sAttr)
    iBaseValue = oAttr.GetBaseAttr()
    if iValue > iBaseValue:
        return int(100 * (iValue - iBaseValue) / iBaseValue)
    return 0


def Func363(obj, dData, dMsgInfo, dOtherArgs):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    if 'TotalDam' not in dMsgInfo:
        return 0
    return dMsgInfo['TotalDam'][0]


def Func364(obj, dData, dMsgInfo, dOtherArgs):
    if 'Cash' in dMsgInfo:
        return dMsgInfo['Cash']
    return 0


def Func365(obj, dData, dMsgInfo, dOtherArgs):
    iFrame = obj.GetShieldRecoverFullFrame()
    return Frame2Time(iFrame)


def Func366(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not obj.m_Part:
        return 0
    oPart = obj.m_Game.GetObject(obj.m_Part)
    if not oPart:
        return 0
    return GetWarriorAttr(sAttr, oPart)


def Func367(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oGame = obj.m_Game
    iRound = oGame.m_WarMgr.m_Round
    clsMonsterData = oGame.m_WarData.GetMonsterData(obj.m_SID)
    if iRound in clsMonsterData.m_BaseAttrInfo:
        dBaseAttr = clsMonsterData.m_BaseAttrInfo[iRound]
    elif clsMonsterData.m_BaseAttrInfo:
        iCurRound = max(clsMonsterData.m_BaseAttrInfo)
        dBaseAttr = clsMonsterData.m_BaseAttrInfo[iCurRound]
    else:
        return 0
    if sAttr in dBaseAttr:
        return dBaseAttr[sAttr]
    return 0


def Func368(obj, dData, dMsgInfo, dOtherArgs):
    if 'RemainTime' in dMsgInfo:
        return dMsgInfo['RemainTime']
    return 0


def Func369(obj, dData, dMsgInfo, dOtherArgs):
    iDam = 0
    lstTrueChange = dMsgInfo['TrueChange']
    lstExcessChange = dMsgInfo['ExcessChange']
    for iChange, _ in lstTrueChange:
        iDam += iChange
    
    for iChange, _ in lstExcessChange:
        iDam += iChange
    
    return iDam


def Func370(obj, dData, dMsgInfo, dOtherArgs, dMonsterMapping):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iVicFightType = oVictim.m_FightType
    if iVicFightType in BOSS_DONOT_COUNT and WARRIOR_NORMAL in dMonsterMapping:
        return dMonsterMapping[WARRIOR_NORMAL]
    for iFightType in dMonsterMapping:
        if iVicFightType & iFightType == iFightType:
            return dMonsterMapping[iFightType]
    
    return 0


def Func372(obj, dData, dMsgInfo, dOtherArgs):
    if 'LuckyHitEff' in dMsgInfo:
        return dMsgInfo['LuckyHitEff']
    return 1


def Func373(obj, dData, dMsgInfo, dOtherArgs, sid):
    oPerform = obj.GetPerform(sid)
    if not oPerform:
        return 0
    return oPerform.GetLifeCycleLevel()


def Func374(obj, dData, dMsgInfo, dOtherArgs):
    iHp = obj.HP()
    iShield = obj.Shield()
    iArmor = obj.Armor()
    iResult = iHp + iShield + iArmor
    return iResult


def Func375(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim or oVictim.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return 0
    iCount = oVictim.m_RelicCon.GetNumByRelicType(RELIC_TYPE_CURSE)
    iAddingRelic = dMsgInfo['NewRelic'] if dMsgInfo and 'NewRelic' in dMsgInfo else 0
    if iAddingRelic:
        iAddingRelicType = cl_perform.GetPerformClassAttr(iAddingRelic, 'm_RelicType')
        if iAddingRelicType == RELIC_TYPE_CURSE:
            iCount += 1
    return iCount


def Func376(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    iItem = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    oPerform = obj.GetPerform(iPerform, iItem)
    if not oPerform:
        return 0
    return oPerform.CalAttr('PFBulletUse')


def Func377(obj, dData, dMsgInfo, dOtherArgs):
    iTotalHp = obj.HP() + obj.Shield() + obj.Armor()
    iTotalHpMax = obj.QueryAttr('HPMax') + obj.QueryAttr('ShieldMax') + obj.QueryAttr('ArmorMax')
    return iTotalHpMax - iTotalHp


def Func378(obj, dData, dMsgInfo, dOtherArgs):
    iTimes = 0
    dRelifeInfo = obj.Query('RelifeInfo', { })
    if dRelifeInfo:
        for iType, dType in dRelifeInfo.items():
            for _, (_, iRemainTimes, _, _) in dType.items():
                iTimes += iRemainTimes
            
        
    return iTimes


def Func379(obj, dData, dMsgInfo, dOtherArgs):
    iHPNow = obj.HP()
    iHPMax = obj.QueryAttr('HPMax')
    return (iHPMax - iHPNow) * 100 // iHPMax


def Func380(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_DevicePerformCon.GetAllEnableComponentLevel()


def Func381(obj, dData, dMsgInfo, dOtherArgs, sid, sAttr):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    oServant = obj.m_Game.GetObject(obj.m_Servant)
    if not oServant:
        return 0
    oPerform = oServant.GetPerform(sid)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def Func382(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_Owner:
        return 0
    oOwner = obj.m_Game.GetObject(obj.m_Owner)
    if not oOwner:
        return 0
    return cl_math.CalDistance3D(obj.GetPos(), oOwner.GetPos())


def Func383(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_Owner:
        return 0
    oOwner = obj.m_Game.GetObject(obj.m_Owner)
    if not oOwner:
        return 0
    iTotalHP = oOwner.HP() + oOwner.Shield() + oOwner.Armor()
    return iTotalHP


def Func384(obj, dData, dMsgInfo, dOtherArgs):
    clsPerform = cl_perform.GetPerformModule(obj.m_AttPerform)
    if not clsPerform:
        return None
    return clsPerform.m_ElementType


def Func385(obj, dData, dMsgInfo, dOtherArgs):
    if 'RealCost' not in dMsgInfo:
        return 0
    return dMsgInfo['RealCost']


def Func386(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'Skill' in dMsgInfo and dMsgInfo['Skill']:
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
        iItem = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'pfid' in dMsgInfo and 'ItemID' in dMsgInfo:
        iPerform = dMsgInfo['pfid']
        iItem = dMsgInfo['ItemID']
    elif 'LifeCycle' in dData:
        sKey = dData['LifeCycle'].m_Key
    else:
        sKey = ''
    SendAlert('err', '%s无法获取【事件武器技能属性】，请检查消息监听' % sKey)
    return 0


def Func387(obj, dData, dMsgInfo, dOtherArgs):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iHPMax = oVictim.QueryAttr('HPMax')
    iShieldMax = oVictim.ShieldMax()
    iArmorMax = oVictim.QueryAttr('ArmorMax')
    return sum(dMsgInfo['TotalDam']) * 100 // (iHPMax + iShieldMax + iArmorMax)


def Func388(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not obj.m_Owner:
        return 0
    oOwner = obj.m_Game.GetObject(obj.m_Owner)
    if not oOwner:
        return 0
    iValue = GetWarriorAttr(sAttr, oOwner)
    oAttr = oOwner.GetAttr(sAttr)
    iBaseValue = oAttr.GetBaseAttr()
    if iValue > iBaseValue:
        return int(100 * (iValue - iBaseValue) / iBaseValue)
    return 0


def Func389(obj, dData, dMsgInfo, dOtherArgs):
    return obj.ExcessHP()


def Func390(obj, dData, dMsgInfo, dOtherArgs):
    return obj.ExcessArmor()


def Func391(obj, dData, dMsgInfo, dOtherArgs):
    return obj.ExcessShield()


def Func401(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    if 'arg' not in dStateInfo:
        return 0
    dArgData = dStateInfo['arg']
    if 'Cache' not in dArgData:
        return 0
    dCache = dArgData['Cache']
    if dCache and 'Att' in dCache:
        return dCache['Att']
    return 0


def Func402(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    if 'PFLV' in dStateInfo:
        return dStateInfo['PFLV']
    return 0


def Func403(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    return GetWarriorAttr(sAttr, obj)


def Func404(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if oState:
        return oState.GetCount()
    return 0


def Func405(obj, dData, dMsgInfo, dOtherArgs):
    iShieldMax = obj.ShieldMax()
    iShield = obj.Shield()
    if iShield > iShieldMax:
        iShield = iShieldMax
    fRatio = iShield / iShieldMax if iShieldMax > 0 else 0
    return fRatio


def Func406(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if oState:
        return oState.m_CreateFrame
    return 0


def Func407(obj, dData, dMsgInfo, dOtherArgs, sid):
    oState = obj.m_State.GetItemBySID(sid)
    if oState:
        return Frame2Time(oState.GetTime())
    return 0


def Func408(obj, dData, dMsgInfo, dOtherArgs):
    dStateInfo = { }
    if 'State' in dMsgInfo:
        dStateInfo = dMsgInfo['State'].m_StateInfo
    elif 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    elif 'StateInfo' in dMsgInfo:
        dStateInfo = dMsgInfo['StateInfo']
    elif 'LifeCycle' in dData:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    if 'arg' not in dStateInfo:
        return 0
    dArgData = dStateInfo['arg']
    if 'AbnormalSourceDam' in dArgData:
        iDam = dArgData['AbnormalSourceDam']
    elif 'Cache' in dArgData:
        dCache = dArgData['Cache']
        iDam = dCache['Att'] if dCache and 'Att' in dCache else 0
    else:
        iDam = 0
    return iDam


def Func409(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if not oState:
        return 0
    oReason = oState.Reason()
    iWeapon = oReason.Query('Item', 0)
    oWeapon = obj.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.MaxBullet()


def Func410(obj, dData, dMsgInfo, dOtherArgs, sid):
    oState = obj.m_State.GetItemBySID(sid)
    if oState:
        return oState.GetCount()
    return 0


def Func411(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oAttacker = GetStateAttack(obj, dData)
    if not oAttacker:
        return 0
    return GetWarriorAttr(sAttr, oAttacker)


def Func412(obj, dData, dMsgInfo, dOtherArgs, iState):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    oState = oVictim.m_State.GetItemBySID(iState)
    if oState:
        return oState.GetCount()
    return 0


def Func413(obj, dData, dMsgInfo, dOtherArgs, iState):
    iVictim = AnalyseVictim(obj, dData, dMsgInfo, dOtherArgs)
    if not iVictim:
        return 0
    oVictim = obj.m_Game.GetObject(iVictim)
    if not oVictim:
        return 0
    lstState = oVictim.m_State.GetItems(iState)
    iResult = 0
    iTargetID = obj.m_ID
    for oState in lstState:
        iAttacker = oState.m_Attacker
        if iAttacker != iTargetID:
            continue
        iResult = oState.GetCount()
    
    return iResult


def Func414(obj, dData, dMsgInfo, dOtherArgs, iState):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    lstState = oVictim.m_State.GetItems(iState)
    lstResult = []
    iTargetID = obj.m_ID
    for oState in lstState:
        iAttacker = oState.m_Attacker
        if iAttacker != iTargetID:
            continue
        lstResult.append(oState)
    
    return len(lstResult)


def Func415(obj, dData, dMsgInfo, dOtherArgs, iState):
    if 'AID' in dData:
        iAttacker = dData['AID']
    else:
        oState = dData['LifeCycle'].GetObject()
        iAttacker = oState.m_Attacker
    lstState = obj.m_State.GetItems(iState)
    lstResult = []
    for oState in lstState:
        if oState.m_Attacker != iAttacker:
            continue
        lstResult.append(oState)
    
    return len(lstResult)


def Func417(obj, dData, dMsgInfo, dOtherArgs, iType):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    elif 'StateInfo' in dMsgInfo:
        dStateInfo = dMsgInfo['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    if 'arg' not in dStateInfo:
        return ABNORMAL_DEFAULT
    dArgData = dStateInfo['arg']
    if 'Cache' not in dArgData:
        return ABNORMAL_DEFAULT
    dCache = dArgData['Cache']
    iFactor = dCache[iType] if iType in dCache else ABNORMAL_DEFAULT
    return iFactor


def Func418(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    if 'IsDam' not in dMsgInfo:
        return 0
    if not dMsgInfo['IsDam']:
        return 0
    return sum(dMsgInfo['TotalDam'])


def Func419(obj, dData, dMsgInfo, dOtherArgs, sBaseKey):
    sKey = f'''RecentDis{sBaseKey}'''
    return obj.Query(sKey, 99999)


def Func420(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    oPerform = obj.m_Perform.GetPerform(iPerform)
    iBulletSID = oPerform.CalAttr('BulletSID')
    if not iBulletSID:
        return 0
    return obj.m_BulletCon.m_Bullet[iBulletSID]


def Func421(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    oPerform = obj.m_Perform.GetPerform(iPerform)
    iBulletSID = oPerform.CalAttr('BulletSID')
    if not iBulletSID:
        return 0
    return oPerform.CalBulletUse(oSkill)


def Func422(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    if 'Att' in dStateInfo:
        return dStateInfo['Att']
    return 0


def Func423(obj, dData, dMsgInfo, dOtherArgs):
    if 'PredictChange' not in dMsgInfo:
        return 0
    return sum(dMsgInfo['PredictChange'])


def Func424(obj, dData, dMsgInfo, dOtherArgs):
    if 'AID' not in dData:
        return 0
    if 'StateSID' not in dData:
        return 0
    oOwner = obj.m_Game.GetObject(dData['AID'])
    if not oOwner:
        return 0
    oState = oOwner.m_State.GetItemBySID(dData['StateSID'])
    if oState:
        return oState.GetCount()
    return 0


def Func425(obj, dData, dMsgInfo, dOtherArgs):
    if 'PredictChange' not in dMsgInfo:
        return 0
    return sum(dMsgInfo['PredictChange']) + dMsgInfo['ExcessChange']


def Func426(obj, dData, dMsgInfo, dOtherArgs):
    iTimes = 0
    dRelifeInfo = obj.Query('RelifeInfo', { })
    if dRelifeInfo:
        for iType, dType in dRelifeInfo.items():
            for _, (_, _, iMaxTimes, _) in dType.items():
                iTimes += iMaxTimes
            
        
    return iTimes


def Func427(obj, dData, dMsgInfo, dOtherArgs, sKey):
    sKey = 'TargetList%d' % sKey
    if not obj.m_Scene:
        return 0
    oGame = obj.m_Game
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    if sKey not in oScene.m_CustomData:
        return 0
    lstTarget = []
    for iTarget in oScene.m_CustomData[sKey]:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if iTarget != obj.m_ID:
            lstTarget.append(iTarget)
    
    return len(lstTarget)


def Func428(obj, dData, dMsgInfo, dOtherArgs, sid):
    oState = obj.m_State.GetItemBySID(sid)
    if oState:
        return oState.m_MaxCount
    return 0


def Func429(obj, dData, dMsgInfo, dOtherArgs, sArg):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if oState:
        return oState.GetArgValue(sArg)
    return 0


def Func430(obj, dData, dMsgInfo, dOtherArgs, sid):
    oState = obj.m_State.GetItemBySID(sid)
    if oState:
        return Frame2Time(oState.GetRemainTime())
    return 0


def Func431(obj, dData, dMsgInfo, dOtherArgs, sid):
    if 'AID' in dData:
        iAttack = dData['AID']
    else:
        oState = dData['LifeCycle'].GetObject()
        iAttack = oState.m_Attacker
    lstState = obj.m_State.GetItems(sid)
    for oState in lstState:
        if oState.m_Attacker != iAttack:
            continue
        return oState.GetCount()
    
    return 0


def Func432(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if oState:
        return Frame2Time(oState.GetAllTime())
    return 0


def Func433(obj, dData, dMsgInfo, dOtherArgs, sid):
    oState = obj.m_State.GetItemBySID(sid)
    if oState:
        return oState.GetRemainTime() / oState.GetTime()
    return 0


def Func434(obj, dData, dMsgInfo, dOtherArgs, sid):
    if 'AID' in dData:
        oAttacker = obj.m_Game.GetObject(dData['AID'])
    else:
        oState = dData['LifeCycle'].GetObject()
        oAttacker = obj.m_Game.GetObject(oState.m_Attacker)
    lstState = oAttacker.m_State.GetItems(sid)
    for oState in lstState:
        return oState.GetCount()
    
    return 0


def Func435(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if not oState:
        return 0
    dInfo = oState.m_Data.setdefault('EffectiveTimeInfo', { })
    oGame = obj.m_Game
    iCurFrame = oGame.GetFrameNum()
    iEffectiveTime = 0
    iStateCnt = oState.GetCount()
    iTotal = sum(dInfo.values())
    if iTotal > iStateCnt:
        dTemp = { }
        iCnt = 0
        iInvalidNumber = iTotal - iStateCnt
        for iFrame, iCount in dInfo.items():
            if iCnt < iInvalidNumber:
                if iCnt + iCount <= iInvalidNumber:
                    iCnt += iCount
                    continue
                dTemp[iFrame] = iCnt + iCount - iInvalidNumber
                iCnt = iInvalidNumber
                continue
            dTemp[iFrame] = iCount
        
        dInfo = dTemp
    for iFrame, iCount in dInfo.items():
        if iFrame - iCurFrame > 0:
            iEffectiveTime += (iFrame - iCurFrame) * iCount
    
    return Frame2Time(iEffectiveTime)


def Func436(obj, dData, dMsgInfo, dOtherArgs):
    iTotalDam = 0
    for iDam, _ in itertools.chain(dMsgInfo['MainDam'], dMsgInfo['FlowDam']):
        iTotalDam += iDam
    
    return iTotalDam


def Func437(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if not oState:
        return 0
    if sKey in oState.m_Data:
        return oState.m_Data[sKey]
    return 0


def Func438(obj, dData, dMsgInfo, dOtherArgs):
    iDam = 0
    if 'StateInfo' in dMsgInfo and 'arg' in dMsgInfo['StateInfo']:
        dArgData = dMsgInfo['StateInfo']['arg']
        if 'AbnormalSourceDam' in dArgData:
            iDam = dArgData['AbnormalSourceDam']
    return iDam


def Func439(obj, dData, dMsgInfo, dOtherArgs):
    oAttacker = GetStateAttack(obj, dData)
    if not oAttacker:
        return 0
    if obj.m_ID == oAttacker.m_ID:
        return 0
    return cl_math.CalDistance3D(oAttacker.GetPos(), obj.GetPos())


def Func440(obj, dData, dMsgInfo, dOtherArgs):
    return obj.QuerySavedData('GSCashRelifeTimes', 0)


def Func441(obj, dData, dMsgInfo, dOtherArgs):
    if dData and 'Phase' in dData:
        return dData['Phase']
    oSurvivorElement = obj.m_Game.m_WarMgr.GetSurvivorElement()
    if oSurvivorElement:
        return oSurvivorElement.m_Phase
    return 0


def Func442(obj, dData, dMsgInfo, dOtherArgs):
    return obj.QuerySavedData('BuyRelifeItemTimes', 0)


def Func443(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    return oSkill.m_Base['ActNum']


def Func444(obj, dData, dMsgInfo, dOtherArgs):
    iEffectDam = sum(dMsgInfo['TotalDam'])
    iExcessDam = 0
    for iDam, _ in dMsgInfo['ExcessChange']:
        iExcessDam += iDam
    
    iTotalDam = iEffectDam + iExcessDam
    if iTotalDam % 100:
        iTotalDam = (iTotalDam - iTotalDam % 100) + 100
    return iTotalDam


def Func445(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    if not dStateInfo:
        return 0
    iWeapon = dStateInfo['RS'].Query('Item', 0)
    oWeapon = obj.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    return oWeapon.m_SID


def Func446(obj, dData, dMsgInfo, dOtherArgs, sid):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    lstState = oVictim.m_State.GetItems(sid)
    iAllRemain = 0
    iTargetID = obj.m_ID
    for oState in lstState:
        iAttacker = oState.m_Attacker
        if iAttacker != iTargetID:
            continue
        iAllRemain += oState.GetRemainTime()
    
    return Frame2Time(iAllRemain)


def Func447(obj, dData, dMsgInfo, dOtherArgs, sid):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    oState = oVictim.m_State.GetItemBySID(sid)
    if not oState:
        return 0
    return oState.m_MaxCount


def Func448(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    oPerform = obj.m_Perform.GetPerform(iPerform)
    iBulletSID = oPerform.CalAttr('BulletSID')
    if not iBulletSID:
        return 0
    iRealBullet = oSkill.m_Collect['RealBullet'] if 'RealBullet' in oSkill.m_Collect else 0
    if not iRealBullet:
        return 0
    return iRealBullet - oSkill.m_Collect['BaseBullet']


def Func449(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_TalentCon.GetAllDisableTalentLevelSum()


def Func450(obj, dData, dMsgInfo, dOtherArgs, sid, sAttr):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    oState = oVictim.m_State.GetItemBySID(sid)
    if not oState:
        return 0
    return oState.GetArgValue(sAttr)


def Func451(obj, dData, dMsgInfo, dOtherArgs, sid, sAttr):
    oState = obj.m_State.GetItemBySID(sid)
    if not oState:
        return 0
    return oState.GetArgValue(sAttr)


def Func452(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    if not dStateInfo:
        return 0
    iItem = dStateInfo['RS'].Query('Item', 0)
    return iItem


def Func453(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'LastVLST' not in oSkill.m_Update:
        return 0
    iNum = 0
    for iTarget in oSkill.m_Update['LastVLST']:
        oTarget = oSkill.m_Game.GetObject(iTarget)
        if oTarget and oTarget.m_FightType & WARRIOR_MONSTER:
            iNum += 1
    
    return iNum


def Func454(obj, dData, dMsgInfo, dOtherArgs, iTotalTime):
    oState = dData['LifeCycle'].GetObject()
    iTime = Frame2Time(obj.m_Game.GetFrameNum() - oState.m_CreateFrame)
    iRemainTime = iTotalTime - iTime
    if iRemainTime:
        return iRemainTime
    return 0


def Func505(obj, dData, dMsgInfo, dOtherArgs):
    if dMsgInfo and 'Skill' in dMsgInfo:
        dCache = dMsgInfo['Skill'].m_Cache
        if 'MaxBullet' not in dCache:
            return 0
        return dCache['MaxBullet']
    if 'ItemKey' in dData:
        return dData['MaxBullet']
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        return oWeapon.QueryAttr('MaxBullet')
    return 0


def Func506(obj, dData, dMsgInfo, dOtherArgs):
    if dMsgInfo and 'Skill' in dMsgInfo:
        dCache = dMsgInfo['Skill'].m_Cache
        if 'MaxBullet' not in dCache:
            return 0
        return dCache['MaxBullet']
    if 'ItemKey' in dData:
        return dData['MaxBullet']
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        oAttr = oWeapon.GetItemAttr('MaxBullet')
        if isinstance(oAttr, cl_object.linkattr.CLinkAttr):
            oAttr = oAttr.GetLink(oWeapon.m_ID)
        if not oAttr:
            return 0
        if not oAttr.m_Refresh:
            oAttr.Refresh(oWeapon)
        return oAttr.m_CurValue
    return 0


def Func507(obj, dData, dMsgInfo, dOtherArgs):
    if 'ItemKey' in dData:
        return dData['MaxBullet']
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        return oWeapon.QueryAttr('MaxBullet')
    return 0


def Func509(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if dMsgInfo and 'Skill' in dMsgInfo:
        dCache = dMsgInfo['Skill'].m_Cache
        if sAttr not in dCache:
            return 0
        return dCache[sAttr]
    if 'ItemKey' in dData:
        return dData[sAttr]
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        return GetItemAttr(sAttr, oWeapon)
    return 0


def Func510(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    iItem = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iItem = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    if not iItem and 'ItemID' in dData:
        iItem = dData['ItemID']
    oCon = obj.m_WieldCon
    lstPos = oCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
    for iPos in lstPos:
        oOtherItem = oCon.GetItem(iPos)
        if oOtherItem and oOtherItem.m_ID != iItem:
            return GetItemAttr(sAttr, oOtherItem)
    
    return 0


def Func511(obj, dData, dMsgInfo, dOtherArgs):
    if dMsgInfo and 'Skill' in dMsgInfo:
        dCache = dMsgInfo['Skill'].m_Cache
        if 'CurBullet' not in dCache:
            return 0
        return dCache['CurBullet']
    if 'ItemKey' in dData:
        return dData['CurBullet']
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        return oBulletCom.Bullet()
    return 0


def Func512(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    return dMsgInfo[sAttr]


def Func513(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    dSummon = obj.m_SummonDict
    if not dSummon:
        return 0
    iCount = 0
    iResult = 0
    for iSummon in dSummon:
        oSummon = obj.m_Game.GetObject(iSummon, PY_FLAG_DEAD)
        if not oSummon:
            continue
        if oSummon.m_FightType & WARRIOR_BARRIER == WARRIOR_BARRIER:
            iCount += 1
            iResult = GetWarriorAttr(sAttr, oSummon)
    
    if iCount > 1:
        ErrLog.Alert('%s 玩家拥有多个屏障召唤物 %s' % (obj.m_PlayerID, dSummon))
    return iResult


def Func514(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    dArg = dStateInfo['arg'] if 'arg' in dStateInfo else { }
    if sAttr in dArg:
        return dArg[sAttr]
    return 0


def Func515(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    iTarget = obj.m_Owner
    oTarget = obj.m_Game.GetObject(iTarget)
    if not oTarget:
        ErrLog.Alert('召唤物%s 归属者不存在, 属性公式', obj.m_SID)
        return None
    return GetWarriorAttr(sAttr, oTarget)


def Func516(obj, dData, dMsgInfo, dOtherArgs, sid):
    iTarget = obj.m_Owner
    oTarget = obj.m_Game.GetObject(iTarget)
    if not oTarget:
        ErrLog.Alert('召唤物%s 归属者不存在, 天赋等级公式', obj.m_SID)
        return None
    oTalent = oTarget.m_TalentCon.GetPerform(sid)
    if oTalent:
        return oTalent.m_Level
    return 0


def Func517(obj, dData, dMsgInfo, dOtherArgs):
    lstAdd = obj.m_WieldCon.GetWeapons(MAIN_HOLD)
    for oWeapon in lstAdd:
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        return oBulletCom.MaxBullet()
    
    return 0


def Func518(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    return obj.Query(sAttr)


def Func519(obj, dData, dMsgInfo, dOtherArgs, sid):
    iTarget = obj.m_Owner
    oTarget = obj.m_Game.GetObject(iTarget)
    if not oTarget:
        ErrLog.Alert('召唤物%s 归属者不存在, 召唤物归属者指定状态计数公式', obj.m_SID)
        return None
    oState = oTarget.m_State.GetItemBySID(sid)
    if oState:
        return oState.GetCount()
    return 0


def Func520(obj, dData, dMsgInfo, dOtherArgs, sid):
    if 'AID' in dData:
        oAttacker = obj.m_Game.GetObject(dData['AID'])
    else:
        oState = dData['LifeCycle'].GetObject()
        oAttacker = obj.m_Game.GetObject(oState.m_Attacker)
    if not oAttacker:
        return 0
    oTalent = oAttacker.m_TalentCon.GetPerform(sid)
    if oTalent:
        return oTalent.m_Level
    return 0


def Func521(obj, dData, dMsgInfo, dOtherArgs, sid):
    oTarget = obj.GetOwner()
    if not oTarget:
        ErrLog.Alert('召唤物%s 归属者不存在, 召唤物归属者指定技能等级', obj.m_SID)
        return None
    oPerform = oTarget.GetPerform(sid)
    if oPerform:
        return oPerform.Level()
    return 0


def Func522(obj, dData, dMsgInfo, dOtherArgs):
    iSecond = obj.GetRestDyingSecond() if hasattr(obj, 'GetRestDyingSecond') else 0
    return iSecond


def Func523(obj, dData, dMsgInfo, dOtherArgs, sAbnormalType):
    return GetAbnormalEleTime(sAbnormalType)


def Func524(obj, dData, dMsgInfo, dOtherArgs):
    lstAdd = obj.m_WieldCon.GetWeapons(MAIN_HOLD)
    for oWeapon in lstAdd:
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        oBulletContainer = obj.m_BulletCon
        iBulletSID = oBulletCom.m_BulletType
        return oBulletContainer.GetMaxBullet(iBulletSID)
    
    return 0


def Func525(obj, dData, dMsgInfo, dOtherArgs):
    lstAdd = obj.m_WieldCon.GetWeapons(MAIN_HOLD)
    for oWeapon in lstAdd:
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        return oBulletCom.Bullet()
    
    return 0


def Func526(obj, dData, dMsgInfo, dOtherArgs):
    oWeapon = obj.m_WieldCon.GetCurWeapon(MAIN_HOLD)
    if oWeapon:
        return oWeapon.m_Grade
    return 0


def Func527(obj, dData, dMsgInfo, dOtherArgs):
    if 'SightHit' in dData:
        return dData['SightHit']
    return 0


def Func528(obj, dData, dMsgInfo, dOtherArgs):
    oWarMgr = obj.m_Game.GetWarMgr()
    oReport = oWarMgr.GetComponent('Warreport')
    if not oReport:
        return 0
    return oReport.m_WarReportData.GetPlayerWarInfo(obj.m_PlayerID, 'MaxWeaponDamage')


def Func529(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = obj.GetThrowPerform()
    if not oPerform:
        return 0
    if 'SID' not in dMsgInfo:
        return 0
    if not dMsgInfo['SID'] == oPerform.CalAttr('BulletSID'):
        return 0
    iChange = dMsgInfo['Amount']
    iCost = -iChange if iChange < 0 else 0
    return iCost


def Func530(obj, dData, dMsgInfo, dOtherArgs):
    oPerformcon = obj.m_Perform
    oPerform = obj.GetCareerPerform()
    if not oPerform:
        return 0
    iColdTimeFrame = oPerformcon.GetTotalColdTime(oPerform.m_SID)
    iTime = Frame2Time(iColdTimeFrame)
    return iTime


def Func531(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iHp = oVictim.HP()
    iShield = oVictim.Shield()
    iArmor = oVictim.Armor()
    iHPMax = oVictim.QueryAttr('HPMax')
    iShieldMax = oVictim.ShieldMax()
    iArmorMax = oVictim.QueryAttr('ArmorMax')
    return (iHp + iShield + iArmor) * 100 // (iHPMax + iShieldMax + iArmorMax)


def Func532(obj, dData, dMsgInfo, dOtherArgs):
    lstAdd = obj.m_WieldCon.GetWeapons(DEPUTY_HOLD)
    for oWeapon in lstAdd:
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        return oBulletCom.Bullet()
    
    return 0


def Func533(obj, dData, dMsgInfo, dOtherArgs):
    lstAdd = obj.m_WieldCon.GetWeapons(DEPUTY_HOLD)
    for oWeapon in lstAdd:
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        return oBulletCom.MaxBullet()
    
    return 0


def Func534(obj, dData, dMsgInfo, dOtherArgs, iSummonID):
    dSummon = obj.m_SummonDict
    if not dSummon:
        return 0
    if not dMsgInfo:
        return 0
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    oGame = obj.m_Game
    iCurScene = oSkill.m_Base['Scene']
    iCurWeapon = oSkill.m_Base['Weapon']
    oSummon = None
    for iCurSummon in dSummon:
        oCurSummon = oGame.GetObject(iCurSummon)
        if not oCurSummon:
            continue
        if oCurSummon.m_Scene != iCurScene:
            continue
        if oCurSummon.m_SrcWeapon != iCurWeapon:
            continue
        if oCurSummon.m_SID == iSummonID:
            oSummon = oCurSummon
            break
    
    if not oSummon:
        return 0
    return int(cl_math.CalDistance3D(oSummon.GetPos(), obj.GetPos()))


def Func535(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = obj.GetThrowPerform()
    if not oPerform:
        return 0
    if not dMsgInfo['SID'] == oPerform.CalAttr('BulletSID'):
        return 0
    iChange = dMsgInfo['Amount']
    iAdd = iChange if iChange > 0 else 0
    return iAdd


def Func536(obj, dData, dMsgInfo, dOtherArgs):
    iResult = 0
    for iState in g_AllAbnormalStateSID:
        if not obj.m_State.GetItemBySID(iState):
            continue
        iResult += 1
    
    return iResult


def Func537(obj, dData, dMsgInfo, dOtherArgs):
    if 'AddEnergy' in dMsgInfo:
        return dMsgInfo['AddEnergy']
    return 0


def Func538(obj, dData, dMsgInfo, dOtherArgs):
    if 'EnergyCost' in dMsgInfo:
        return dMsgInfo['EnergyCost']
    return 0


def Func540(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'EnergyCost' in oSkill.m_Collect:
        return oSkill.m_Collect['EnergyCost']
    return 0


def Func541(obj, dData, dMsgInfo, dOtherArgs):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    if 'TotalDam' not in dMsgInfo:
        return 0
    return dMsgInfo['TotalDam'][2]


def Func542(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'Distance' not in oSkill.m_Cache:
        return 0
    return oSkill.m_Cache['Distance']


def Func543(obj, dData, dMsgInfo, dOtherArgs, dWeight):
    return ChooseKey(obj.m_Game, dWeight)


def Func544(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oRoundElement = obj.m_Game.m_WarMgr.GetComponent('RoundElement')
    if sAttr in oRoundElement.m_ModeMonsterAttrAdjust:
        return oRoundElement.m_ModeMonsterAttrAdjust[sAttr]
    return 0


def Func545(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_TotalGainWarCash


def Func546(obj, dData, dMsgInfo, dOtherArgs, sid):
    oSkillMgr = obj.m_Game.m_SkillMgr
    lstSkill = oSkillMgr.GetSkillBySID(sid)
    if 'CurVID' not in dMsgInfo:
        return 0
    if 'ItemID' not in dData:
        return 0
    for oCurSkill in lstSkill:
        if oCurSkill.m_Base['AID'] != obj.m_ID:
            continue
        if oCurSkill.m_Base['Weapon'] != dData['ItemID']:
            continue
        dDamTimes = oCurSkill.m_Collect['DamTimes'] if 'DamTimes' in oCurSkill.m_Collect else { }
        if not dDamTimes:
            return 0
        iCurVID = dMsgInfo['CurVID']
        if iCurVID in dDamTimes:
            return dDamTimes[iCurVID]
        return 0
    
    return 0


def Func547(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if dOtherArgs and 'Perform' in dOtherArgs:
        oPerform = dOtherArgs['Perform']
    else:
        oPerform = dData['LifeCycle'].GetObject()
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def Func548(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    return cl_action.GetTrajectory(oSkill)


def Func549(obj, dData, dMsgInfo, dOtherArgs):
    if 'EnergyChange' in dMsgInfo:
        return abs(dMsgInfo['EnergyChange'])
    return 0


def Func550(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    return oSkill.m_CacheData.m_SignSpeed


def Func551(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo:
        return None
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return None
    return dMsgInfo['TotalDam'][1]


def Func552(obj, dData, dMsgInfo, dOtherArgs):
    oWeapon = obj.m_WieldCon.GetCurWeapon(DEPUTY_HOLD)
    if oWeapon:
        return oWeapon.m_Grade
    return 0


def Func553(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not dMsgInfo or 'TotalCure' not in dMsgInfo:
        return 0
    if sAttr not in cl_formula.g_HpTypeIndex:
        return 0
    iIndex = cl_formula.g_HpTypeIndex[sAttr]
    return dMsgInfo['TotalCure'][iIndex]


def Func554(obj, dData, dMsgInfo, dOtherArgs):
    if not dData or 'Drop' not in dData:
        return 0
    iDrop = dData['Drop']
    oDrop = obj.m_Game.GetObject(iDrop)
    if not oDrop:
        return 0
    return oDrop.Query('SurvivorPhase', 0)


def Func555(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = obj.m_WieldCon.GetCurWeapon(MAIN_HOLD)
    if oWeapon:
        return GetItemAttr(sAttr, oWeapon)
    return 0


def Func556(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim and oVictim.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
        return oVictim.m_WarCash
    return 0


def Func557(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim:
        return oVictim.QueryAttr('HPMax') + oVictim.QueryAttr('ShieldMax') + oVictim.QueryAttr('ArmorMax')
    return 0


def Func558(obj, dData, dMsgInfo, dOtherArgs):
    iHp = obj.HP()
    iShield = obj.Shield()
    iArmor = obj.Armor()
    iHPMax = obj.QueryAttr('HPMax')
    iShieldMax = obj.ShieldMax()
    iArmorMax = obj.QueryAttr('ArmorMax')
    return (iHp + iShield + iArmor) * 100 // (iHPMax + iShieldMax + iArmorMax)


def Func559(obj, dData, dMsgInfo, dOtherArgs, idx):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    return dMsgInfo['Skill'].m_CacheData.m_IntParaList[idx]


def Func560(obj, dData, dMsgInfo, dOtherArgs):
    oGamblerCom = obj.m_GamblerCon
    if oGamblerCom:
        return oGamblerCom.m_Prob
    return 0


def Func561(obj, dData, dMsgInfo, dOtherArgs):
    oGamblerCom = obj.m_GamblerCon
    if oGamblerCom:
        return len(oGamblerCom.m_QualityList)
    return 0


def Func562(obj, dData, dMsgInfo, dOtherArgs):
    return dMsgInfo['Comb']


def Func563(obj, dData, dMsgInfo, dOtherArgs):
    oGamblerCom = obj.m_GamblerCon
    if oGamblerCom:
        return oGamblerCom.m_GrooveNum
    return 0


def Func564(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    return oSkill.m_CacheData.m_PerformMode


def Func565(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oTarget = obj.GetOwner()
    if not oTarget:
        return 0
    lstWeapon = oTarget.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        if not oWeapon or oWeapon.GetComponent('Hold').HoldPos() == MAIN_HOLD:
            continue
        return GetItemAttr(sAttr, oWeapon)
    
    return 0


def Func566(obj, dData, dMsgInfo, dOtherArgs):
    if 'SurvivalFrame' in dMsgInfo:
        return dMsgInfo['SurvivalFrame']
    return 0


def Func567(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    iServant = obj.m_Servant
    oServant = obj.m_Game.GetObject(iServant)
    if not oServant:
        return 0
    return oServant.m_Phase


def Func568(obj, dData, dMsgInfo, dOtherArgs, sQuality):
    iQuality = GetQualityNumber(sQuality)
    oGamblerCom = obj.m_GamblerCon
    if oGamblerCom:
        return oGamblerCom.HasQualityNum(iQuality)
    return 0


def Func569(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    oGame = obj.m_Game
    oHero = oGame.GetObject(obj.m_Owner)
    if oHero and oHero.m_TalentCon:
        for oPerform in oHero.m_TalentCon.GetAllPerform():
            if oPerform.m_PFType != PF_TYPE_TALENT:
                continue
            iCount += oPerform.m_Level
        
    return iCount


def Func570(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        return oWeapon.QueryItemBaseAttr(sAttr)
    return 0


def Func571(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    iItem = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iItem = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    if not iItem and 'ItemID' in dData:
        iItem = dData['ItemID']
    oCon = obj.m_WieldCon
    lstPos = oCon.m_Type2Pos[itemdef.EQUIP_TYPE_MAINWEAPON]
    for iPos in lstPos:
        oOtherItem = oCon.GetItem(iPos)
        if oOtherItem and oOtherItem.m_ID != iItem:
            return oOtherItem.QueryItemBaseAttr(sAttr)
    
    return 0


def Func572(obj, dData, dMsgInfo, dOtherArgs):
    return len(obj.m_Game.m_WarMgr.GetRoomHero())


def Func573(obj, dData, dMsgInfo, dOtherArgs):
    return cl_perform.GetPerformClassAttr(dMsgInfo['iPerform'], 'm_Quality')


def Func574(obj, dData, dMsgInfo, dOtherArgs, sid):
    if not obj.m_Scene:
        return 0
    oGame = obj.m_Game
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    lstHero = oScene.GetHeros()
    iCnt = 0
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        if oHero.IsDead():
            continue
        if oHero.m_RelicCon.IsEnabled(sid):
            iCnt += 1
    
    return iCnt


def Func575(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_RELIC:
            continue
        if oPerform.m_Level == 2:
            iCount += 1
    
    if not dMsgInfo:
        return iCount
    if 'NewRelic' in dMsgInfo and 'Level' in dMsgInfo:
        iNewRelic = dMsgInfo['NewRelic']
        iLevel = dMsgInfo['Level']
        if iNewRelic and iLevel == 2:
            iCount += 1
    return iCount


def Func576(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    lstItem = obj.m_WieldCon.GetWeapons(iFlag = -1)
    if not lstItem:
        return 0
    oTarWeapon = None
    for oWeapon in lstItem:
        if oWeapon.IsInitWeapon():
            continue
        oTarWeapon = oWeapon
    
    if not oTarWeapon:
        return 0
    return GetItemAttr(sAttr, oTarWeapon)


def Func577(obj, dData, dMsgInfo, dOtherArgs, iRandMin, iRandMax):
    return iRandMin + obj.m_Game.Random(max(0, iRandMax - iRandMin))


def Func578(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        return oWeapon.GetSpecialAttr(sAttr)
    return 0


def Func579(obj, dData, dMsgInfo, dOtherArgs, iStart, iGap, iNum):
    dChooseInfo = { }
    for _ in range(iNum):
        dChooseInfo[iStart] = 1
        iStart += iGap
    
    return ChooseKey(obj.m_Game, dChooseInfo)


def Func580(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = dData['LifeCycle'].GetObject()
    return oPerform.m_Stack


def Func581(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    if 'TaskID' not in dData:
        return 0
    oSkill = dMsgInfo['Skill']
    sKey = 'Task%d-%d%s' % (dData['TaskSID'], dData['TaskID'], sKey)
    if sKey in oSkill.m_Collect:
        return oSkill.m_Collect[sKey]
    return 0


def Func582(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'OldVal' not in dMsgInfo:
        return -1
    return dMsgInfo['OldVal']


def Func583(obj, dData, dMsgInfo, dOtherArgs, iNumber, dScope, iDefault):
    for iKey in dScope:
        if iNumber < iKey:
            return dScope[iKey]
    
    return iDefault


def Func584(obj, dData, dMsgInfo, dOtherArgs, iStatIdx):
    if 'LifeCycle' not in dData:
        return 0
    oTask = dData['LifeCycle'].GetObject()
    return oTask.GetRecordStat(iStatIdx)


def Func585(obj, dData, dMsgInfo, dOtherArgs):
    if 'FlawCon' not in dData:
        return 0
    oFlawCon = dData['FlawCon']
    return oFlawCon.GetFlawAttr(obj, FLAW_KILLLINE, iCalAddition = 1)


def Func586(obj, dData, dMsgInfo, dOtherArgs):
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oAttack or not oVictim or not (oAttack.m_FightType & WARRIOR_HERO) or not (oVictim.m_FightType & WARRIOR_MONSTER):
        return 0
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if not oWeapon:
        return 0
    iAIWeaponDam = oWeapon.m_AIWeaponDam
    if not iAIWeaponDam:
        return 0
    return CalAIDamage(oAttack, oVictim, iAIWeaponDam)


def Func587(obj, dData, dMsgInfo, dOtherArgs):
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oAttack or not oVictim or not (oAttack.m_FightType & WARRIOR_HERO) or not (oVictim.m_FightType & WARRIOR_MONSTER):
        return 0
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    oPerform = oAttack.GetPerform(oSkill.m_Base['pfid'])
    if not oPerform:
        return 0
    if oPerform.m_PFType in (PF_TYPE_CAREERPF, PF_TYPE_THROW):
        iAIPerformDam = oPerform.m_AIPerformDam
    else:
        iAIPerformDam = oPerform.GetArgValue('AIPerformDam', 0)
    if not iAIPerformDam:
        return 0
    iAIDamFactor = oSkill.m_Custom['AIDamFactor'] if 'AIDamFactor' in oSkill.m_Custom else 0
    oReason = dMsgInfo['RS']
    dOtherInfo = oReason.Query('OtherInfo', { })
    if 'AIDamFactor' in dOtherInfo:
        iAIDamFactor += dOtherInfo['AIDamFactor']
    return CalAIDamage(oAttack, oVictim, iAIPerformDam, iAIDamFactor)


def Func588(obj, dData, dMsgInfo, dOtherArgs, iTime):
    oGame = obj.m_Game
    oElement = oGame.m_WarMgr.GetComponent('TeammateAI')
    if not oElement or not (oElement.m_HeroDieInfo):
        return 0
    iCnt = 0
    iTargetFrame = iTime // GAME_FRAME_TIME
    iCurFrame = oGame.GetFrameNum()
    lstHero = oGame.m_WarMgr.GetAllHeroExceptAI()
    for iHero in lstHero:
        for iFrame in oElement.m_HeroDieInfo[iHero]:
            if iCurFrame - iFrame <= iTargetFrame:
                iCnt += 1
                continue
        
    
    return iCnt


def Func589(obj, dData, dMsgInfo, dOtherArgs):
    return obj.QueryAttr('HPMax') + obj.QueryAttr('ShieldMax') + obj.QueryAttr('ArmorMax')


def Func590(obj, dData, dMsgInfo, dOtherArgs):
    if not (obj.m_FightType & WARRIOR_HERO) or obj.m_SID != EXECUTOR_HERO:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    return obj.m_FlawCon.GetFlawAttr(oVictim, FLAW_UNBALANCE_EFFECTTIME)


def Func591(obj, dData, dMsgInfo, dOtherArgs, iTargetValues):
    iResult = 0
    for iLevel in obj.m_TalentCon.GetAllTalentLevel().values():
        if iLevel == iTargetValues:
            iResult += 1
    
    return iResult


def Func592(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_LineIdx:
        return 0
    oEndlessElement = obj.m_Game.m_WarMgr.GetEndlessElement()
    if oEndlessElement:
        (iLevel, iRoomPos, _) = obj.m_LineIdx
        return oEndlessElement.GetMonsterExtraGrade(iLevel, iRoomPos)
    return 0


def Func593(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'FlawHitTimes' not in dMsgInfo:
        return 0
    return dMsgInfo['FlawHitTimes']


def Func594(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    return obj.Resistance()


def Func595(obj, dData, dMsgInfo, dOtherArgs):
    oWarMgr = obj.m_Game.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    return oWarMgr.GetBaseLayer(oLevelCtrl.m_LayerNum)


def Func596(obj, dData, dMsgInfo, dOtherArgs, iSessionSID):
    oSeasonTaskMgr = obj.m_SeasonTaskMgr
    dSeasonInfo = oSeasonTaskMgr.GetSeasonInfo(iSessionSID)
    if 'WarSeasonTaskValue' not in dSeasonInfo:
        return 0
    return dSeasonInfo['WarSeasonTaskValue']


def Func597(obj, dData, dMsgInfo, dOtherArgs):
    oMove = obj.GetAttr('MoveSpeed')
    if not oMove:
        return 0
    iChangeRatio = oMove.GetChangeRatio(obj)
    if iChangeRatio < 100:
        return 0
    return iChangeRatio - 100


def Func598(obj, dData, dMsgInfo, dOtherArgs, sKey):
    sKey = 'save.' + sKey
    return obj.QuerySavedData(sKey, 0)


def Func599(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iResult = 0
    for iState in g_AllAbnormalStateSID:
        if not oVictim.m_State.GetItemBySID(iState):
            continue
        iResult += 1
    
    return iResult


def Func600(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    return obj.MagicPower()


def Func601(obj, dData, dMsgInfo, dOtherArgs):
    if 'UseCountAdd' in dMsgInfo:
        return dMsgInfo['UseCountAdd']
    return 0


def Func602(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = obj.GetThrowPerform()
    if not oPerform:
        return 0
    iBullet = oPerform.CalAttr('BulletSID')
    iBagBulletMax = obj.m_BulletCon.GetMaxBullet(iBullet)
    return iBagBulletMax


def Func603(obj, dData, dMsgInfo, dOtherArgs):
    if 'ChangeMagicPowerValue' not in dMsgInfo:
        return 0
    return dMsgInfo['ChangeMagicPowerValue']


def Func604(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if sKey not in oSkill.m_Custom:
        return 0
    return oSkill.m_Custom[sKey]


def Func605(obj, dData, dMsgInfo, dOtherArgs):
    oEndlessElement = obj.m_Game.m_WarMgr.GetEndlessElement()
    if not oEndlessElement:
        return 1
    return oEndlessElement.GetMonsterTeamFactor(obj)


def Func606(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = obj.m_WieldCon.GetCurWeapon(MAIN_HOLD)
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return 0
    oAttr = oWeapon.GetItemAttr(sAttr)
    if not oAttr or oAttr.m_Type != 'Link':
        return 0
    return oAttr.GetOverFlowValue(oWeapon)


def Func607(obj, dData, dMsgInfo, dOtherArgs):
    if 'SID' in dMsgInfo:
        return dMsgInfo['SID']
    return 0


def Func608(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = obj.m_WieldCon.GetDeputyPosWeapon()
    if oWeapon:
        return GetItemAttr(sAttr, oWeapon)
    return 0


def Func609(obj, dData, dMsgInfo, dOtherArgs):
    lstWeapon = obj.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    dReturn = {
        DAM_TYPE_THUNDER: 1,
        DAM_TYPE_CORRISION: 1,
        DAM_TYPE_FIRE: 1 }
    dChoose = { }
    for oWeapon in lstWeapon:
        iElement = oWeapon.m_ElementType & DAM_TYPE_ELEMENT
        if iElement not in dReturn:
            continue
        dChoose[iElement] = 1
    
    if dChoose:
        return ChooseKey(obj.m_Game, dChoose)
    return ChooseKey(obj.m_Game, dReturn)


def Func610(obj, dData, dMsgInfo, dOtherArgs, iStateSID, sKey):
    oStateCon = obj.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return 0
    if sKey not in oState.m_Data:
        return 0
    return oState.m_Data[sKey]


def Func611(obj, dData, dMsgInfo, dOtherArgs):
    if not (obj.m_FightType & WARRIOR_HERO) or obj.m_SID != EXECUTOR_HERO:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    return obj.m_FlawCon.GetKillLine(oVictim)


def Func612(obj, dData, dMsgInfo, dOtherArgs):
    if not (obj.m_FightType & WARRIOR_HERO) or obj.m_SID != EXECUTOR_HERO:
        return 0
    iVictim = AnalyseVictim(obj, dData, dMsgInfo, dOtherArgs)
    dFlaw = obj.m_FlawCon.GetFlaw(iVictim)
    if not dFlaw:
        return 0
    return len(dFlaw)


def Func613(obj, dData, dMsgInfo, dOtherArgs, iInscriptionType):
    iCount = 0
    lstWeapon = obj.m_WieldCon.GetWeapons()
    if not lstWeapon:
        return iCount
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        iCount += oInscriptionCom.GetEnableInscriptionNumByType(iInscriptionType)
    
    return iCount


def Func614(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = dData['LifeCycle'].GetObject()
    iExcludeRelic = 0
    if oPerform.m_PFType == PF_TYPE_RELIC:
        iExcludeRelic = oPerform.m_SID
    iCount = 0
    lstRelic = obj.m_RelicCon.GetAllRelicByType(RELIC_TYPE_NORMAL)
    for oRelic in lstRelic:
        if oRelic.m_Level < oRelic.m_MaxLevel and oRelic.m_SID != iExcludeRelic:
            iCount += 1
    
    return iCount


def Func615(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oAttacker = GetStateAttack(obj, dData)
    if not oAttacker:
        return 0
    return oAttacker.Query(sAttr)


def Func616(obj, dData, dMsgInfo, dOtherArgs):
    oAttacker = GetStateAttack(obj, dData)
    if not oAttacker:
        return 0
    if not (oAttacker.m_FightType & WARRIOR_HERO) or oAttacker.m_SID != EXECUTOR_HERO:
        return 0
    return oAttacker.m_FlawCon.GetFlawAttr(obj, FLAW_UNBALANCE_IMMOBILIZETIME, iCalAddition = 1)


def Func617(obj, dData, dMsgInfo, dOtherArgs, iSID):
    iCount = 0
    oGame = obj.m_Game
    for iHero in oGame.m_WarMgr.GetRoomHero(iCalAI = 0):
        oHero = oGame.GetObject(iHero)
        if not oHero or oHero.m_SID != iSID:
            continue
        iCount += 1
    
    return iCount


def Func618(obj, dData, dMsgInfo, dOtherArgs, iInscriptionType):
    iCount = 0
    lstWeapon = obj.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    if not lstWeapon:
        return iCount
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        iCount += oInscriptionCom.GetEnableInscriptionNumByType(iInscriptionType)
    
    return iCount


def Func619(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'StateInfo' in dData:
        dStateInfo = dData['StateInfo']
    else:
        oState = dData['LifeCycle'].GetObject()
        dStateInfo = oState.m_StateInfo
    dArg = dStateInfo['arg'] if 'arg' in dStateInfo else { }
    if sAttr in dArg:
        return dArg[sAttr]
    return 0


def Func620(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim:
        return oVictim.m_ID
    return 0


def Func621(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'ArgData' not in oSkill.m_Cache or sAttr not in oSkill.m_Cache['ArgData']:
        return 0
    return oSkill.m_Cache['ArgData'][sAttr]


def Func622(obj, dData, dMsgInfo, dOtherArgs):
    if 'TrueAlter' in dMsgInfo:
        return abs(dMsgInfo['TrueAlter'])
    return 0


def Func623(obj, dData, dMsgInfo, dOtherArgs):
    iAlterDeviceEnergy = dMsgInfo['Alter'] if 'Alter' in dMsgInfo else 0
    iTrueAlterDeviceEnergy = dMsgInfo['TrueAlter'] if 'TrueAlter' in dMsgInfo else 0
    if iAlterDeviceEnergy > 0 and iAlterDeviceEnergy > iTrueAlterDeviceEnergy:
        return iAlterDeviceEnergy - iTrueAlterDeviceEnergy
    return 0


def Func624(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    return obj.GetDeviceID()


def Func625(obj, dData, dMsgInfo, dOtherArgs):
    if 'AddCount' not in dMsgInfo:
        return 0
    return dMsgInfo['AddCount']


def Func626(obj, dData, dMsgInfo, dOtherArgs, iStateSID):
    if 'StateSID' not in dMsgInfo:
        return 0
    if iStateSID != dMsgInfo['StateSID']:
        return 0
    if 'Count' in dMsgInfo:
        return dMsgInfo['Count']
    return 0


def Func627(obj, dData, dMsgInfo, dOtherArgs, iState):
    iDevice = obj.GetDeviceID()
    if not iDevice:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    lstState = oVictim.m_State.GetItems(iState)
    iResult = 0
    for oState in lstState:
        iAttacker = oState.m_Attacker
        if iAttacker != iDevice:
            continue
        iResult = oState.GetCount()
    
    return iResult


def Func628(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'LastVLST' not in oSkill.m_Update:
        return 0
    if obj.m_FightType & WARRIOR_HERO:
        oOwner = obj
    elif obj.m_FightType & WARRIOR_DEVICE:
        oOwner = obj.GetOwner()
    else:
        SendAlert('err', '全部命中者与所属英雄基础移速差总和百分比 未获取到所属英雄%s' % obj.m_SID)
        return 0
    iAllDifference = 0
    oGame = obj.m_Game
    iBaseMoveSpeed = GetWarriorAttr('BMoveSpeed', oOwner)
    for iVictimID in oSkill.m_Update['LastVLST']:
        oVictim = oGame.GetObject(iVictimID)
        if not oVictim:
            continue
        iVictimBaseMoveSpeed = GetWarriorAttr('BMoveSpeed', oVictim)
        iDifference = abs(iBaseMoveSpeed - iVictimBaseMoveSpeed)
        iAllDifference += iDifference
    
    iResult = iAllDifference / iBaseMoveSpeed
    return iResult


def Func629(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_RelicCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_RELIC:
            continue
        if oPerform.ValidRemove():
            continue
        iCount += 1
    
    return iCount


def Func630(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    oBenediction = obj.m_BenedictionCon
    for oPerform in oBenediction.m_Perform.values():
        if oPerform.m_PFType != PF_TYPE_BENEDICTION:
            continue
        if not oPerform.m_Career:
            continue
        iCount += 1
    
    return iCount


def Func632(obj, dData, dMsgInfo, dOtherArgs, iPointLevel):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    oDevicePerformCon = obj.m_DevicePerformCon
    iCount = 0
    for oPerorm in oDevicePerformCon.GetAllPerform():
        if oPerorm.m_PFType != PF_TYPE_DEVICECOMP:
            continue
        if oPerorm.m_Level != iPointLevel:
            continue
        iCount += 1
    
    return iCount


def Func633(obj, dData, dMsgInfo, dOtherArgs):
    if 'TriggerFrame' in dMsgInfo:
        return Frame2Time(dMsgInfo['TriggerFrame'])
    return 0


def Func634(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    oServant = obj.m_Game.GetObject(obj.m_Servant)
    if not oServant:
        return 0
    return GetWarriorAttr(sAttr, oServant)


def Func635(obj, dData, dMsgInfo, dOtherArgs, sid, sArgs):
    if obj.m_FightType & WARRIOR_HERO:
        oDevice = obj.GetDevice()
    elif obj.m_FightType & WARRIOR_DEVICE:
        oDevice = obj
    else:
        return 0
    oPerform = oDevice.GetPerform(sid)
    if not oPerform:
        return 0
    return oPerform.GetArgValue(sArgs)


def Func636(obj, dData, dMsgInfo, dOtherArgs):
    oGame = obj.m_Game
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    if obj.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = obj.m_InkCon
    return oInkCon.GetNumInInkAreaByType(WARRIOR_MONSTER)


def Func637(obj, dData, dMsgInfo, dOtherArgs, sid, sAttr):
    if obj.m_FightType & WARRIOR_HERO:
        oDevice = obj.GetDevice()
    elif obj.m_FightType & WARRIOR_DEVICE:
        oDevice = obj
    else:
        return 0
    oPerform = oDevice.GetPerform(sid)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def Func638(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = obj.m_InkCon
    return oInkCon.GetCurInkValue()


def Func639(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    oDevice = obj.GetDevice()
    if not oDevice:
        return 0
    return GetWarriorAttr(sAttr, oDevice)


def Func640(obj, dData, dMsgInfo, dOtherArgs, sKey):
    oDevice = obj.GetDevice()
    if not oDevice:
        return 0
    sKey = 'MoveDis%s' % sKey
    (_, fDis) = oDevice.Query(sKey, (0, 0))
    return int(fDis)


def Func641(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_FightType & WARRIOR_DEVICE:
        oDevice = obj
    elif obj.m_FightType & WARRIOR_HERO:
        oDevice = obj.GetDevice()
    else:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    oToxicPerform = oDevice.GetPerform(TOXIC_FOG)
    if not oToxicPerform:
        return 0
    iToxicState = oToxicPerform.GetArgValue('ToxicStateSID')
    oState = oVictim.m_State.GetItemBySource(iToxicState, oDevice.m_ID)
    if not oState:
        return 0
    return oState.GetCount()


def Func642(obj, dData, dMsgInfo, dOtherArgs):
    if 'Distance' in dMsgInfo:
        return dMsgInfo['Distance']
    return 0


def Func643(obj, dData, dMsgInfo, dOtherArgs, sKey):
    return obj.QuerySavedData(sKey, 0)


def Func644(obj, dData, dMsgInfo, dOtherArgs):
    lstWeapon = obj.m_WieldCon.GetAllItem()
    iMaxGrade = 0
    for oWeapon in lstWeapon:
        if oWeapon.m_Type == itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON:
            continue
        iRealGrade = oWeapon.m_Grade - oWeapon.GetExtGrade()
        if iRealGrade <= iMaxGrade:
            continue
        iMaxGrade = iRealGrade
    
    return iMaxGrade


def Func645(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_FightType & WARRIOR_DEVICE:
        oDevice = obj
    elif obj.m_FightType & WARRIOR_HERO:
        oDevice = obj.GetDevice()
    else:
        return 0
    return len(oDevice.m_SummonDict)


def Func646(obj, dData, dMsgInfo, dOtherArgs):
    if 'CureInfo' in dMsgInfo:
        iTotalChange = 0
        for iChange, oReason in dMsgInfo['CureInfo']:
            iTotalChange += iChange
        
        return iTotalChange
    if 'TotalDam' in dMsgInfo:
        return -dMsgInfo['TotalDam'][2]
    if 'TotalCure' in dMsgInfo:
        return dMsgInfo['TotalCure'][2]
    return 0


def Func647(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dCache = oSkill.m_Cache
    if 'MaxBullet' not in dCache:
        return 0
    if 'SkillFillBullet' not in oSkill.m_Collect:
        return 0
    return oSkill.m_Collect['SkillFillBullet'] * 100 // dCache['MaxBullet']


def Func648(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'BaseBullet' not in oSkill.m_Collect:
        return 0
    iBaseBullet = oSkill.m_Collect['BaseBullet']
    iBulletUse = oSkill.m_Collect['BulletUse'] if 'BulletUse' in oSkill.m_Collect else 0
    if 'ExtShootBulletUse' in oSkill.m_Collect:
        iBulletUse += oSkill.m_Collect['ExtShootBulletUse']
    if 'OtherBulletUse' in oSkill.m_Collect:
        for iBullte in oSkill.m_Collect['OtherBulletUse'].values():
            iBulletUse += iBullte
        
    if iBulletUse > iBaseBullet:
        return iBulletUse - iBaseBullet
    return 0


def Func649(obj, dData, dMsgInfo, dOtherArgs, iStateSID):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'PFAddState' not in oSkill.m_Update:
        return 0
    if iStateSID not in oSkill.m_Update['PFAddState']:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iVictim = oVictim.m_ID
    if iVictim not in oSkill.m_Update['PFAddState'][iStateSID]:
        return 0
    iState = oSkill.m_Update['PFAddState'][iStateSID][iVictim]
    oState = oVictim.m_State.GetItem(iState)
    if oState:
        return Frame2Time(oState.GetRemainTime())
    return 0


def Func650(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    return obj.QueryMaxAttr(sAttr)


def Func651(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if not dMsgInfo:
        return 0
    if sKey in dMsgInfo:
        return dMsgInfo[sKey]
    return 0


def Func652(obj, dData, dMsgInfo, dOtherArgs, sKey):
    return obj.m_OffsetRange[sKey] * obj.m_AttrOffset[sKey] / 10


def Func653(obj, dData, dMsgInfo, dOtherArgs, iPerform):
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if not oWeapon:
        return 0
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return 0
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.CurPFBullet()


def Func654(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_Game.m_WarMgr.m_Cycle > 0:
        return 1
    return 0


def Func655(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_MonsterLastWeakCount


def Func656(obj, dData, dMsgInfo, dOtherArgs):
    return len(obj.m_ConquerCacheDict)


def Func657(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    return obj.GetCareerPerformID()


def Func658(obj, dData, dMsgInfo, dOtherArgs, sid):
    oPerform = obj.m_Perform.GetPerform(sid)
    if oPerform and oPerform.m_PFType == PF_TYPE_CAREERPF:
        return oPerform.CurPFBullet()
    return 0


def Func659(obj, dData, dMsgInfo, dOtherArgs):
    iVictim = AnalyseVictim(obj, dData, dMsgInfo, dOtherArgs)
    if not iVictim:
        return 0
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    lstHitFlaw = obj.m_FlawCon.GetSkillHitFlaw(oSkill, iVictim)
    if lstHitFlaw:
        return lstHitFlaw[0]
    return 0


def Func660(obj, dData, dMsgInfo, dOtherArgs):
    if 'AllPet' not in dData:
        return 0
    lstPet = dData['AllPet']
    sAttr = dData['Attr']
    iRes = 0
    for oPet in lstPet:
        iRes += oPet.m_AttrOffset[sAttr]
    
    return iRes


def Func661(obj, dData, dMsgInfo, dOtherArgs, iAbility, sKey):
    if obj.m_FightType & WARRIOR_HERO:
        obj = obj.m_PetCon.GetCurPet()
        if not obj:
            return 0
    return obj.m_AbilityCon.QueryInheritableInfo(iAbility, sKey)


def Func662(obj, dData, dMsgInfo, dOtherArgs):
    if 'StateID' in dData:
        oState = obj.m_State.GetItem(dData['StateID'])
    else:
        oState = dData['LifeCycle'].GetObject()
    if 'DelayCnt' in oState.m_DelayInfo:
        return oState.m_DelayInfo['DelayCnt']
    return 0


def Func663(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    return iPerform


def Func664(obj, dData, dMsgInfo, dOtherArgs):
    iCurLevel = dMsgInfo['CurLevel'] if 'CurLevel' in dMsgInfo else 0
    iLevel = dMsgInfo['Level'] if 'Level' in dMsgInfo else 0
    return iLevel - iCurLevel


def Func665(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_FightType & WARRIOR_HERO:
        obj = obj.m_PetCon.GetCurPet()
        if not obj:
            return 0
    return len(obj.Ability())


def Func666(obj, dData, dMsgInfo, dOtherArgs, iPerform, sKey):
    oPerform = dData['LifeCycle'].GetObject()
    oWeapon = oPerform.GetMyItem()
    if not oWeapon:
        return 0
    oGame = obj.m_Game
    oSkill = oGame.m_SkillMgr.GetSkillBySource(iPerform, obj.m_ID, oWeapon.m_ID)
    if not oSkill:
        return 0
    if sKey in oSkill.m_Collect:
        return oSkill.m_Collect[sKey]
    return 0


def Func667(obj, dData, dMsgInfo, dOtherArgs):
    return dMsgInfo['RemainResetTime']


def Func668(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if oWeapon:
        return oWeapon.GetSpecialAttrMax(sAttr)
    return 0


def Func669(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    return oOwner.QueryAttr('HPMax') + oOwner.QueryAttr('ShieldMax') + oOwner.QueryAttr('ArmorMax')


def Func670(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    oWeapon = oOwner.m_WieldCon.GetCurWeapon(MAIN_HOLD)
    if oWeapon:
        return GetItemAttr(sAttr, oWeapon)
    return 0


def Func671(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = obj.m_InkCon
    return oInkCon.GetMaxInkValue()


def Func672(obj, dData, dMsgInfo, dOtherArgs, iIsReal):
    if iIsReal or 'RealChange' in dMsgInfo:
        return dMsgInfo['RealChange']
    if 'NeedChange' in dMsgInfo:
        return dMsgInfo['NeedChange']
    return 0


def Func673(obj, dData, dMsgInfo, dOtherArgs):
    return len(obj.Ability())


def Func674(obj, dData, dMsgInfo, dOtherArgs):
    return len(obj.GetEnableSpell())


def Func675(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return 0
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'ScanInfo' not in oSkill.m_Collect:
        return 0
    dScanInfo = oSkill.m_Collect['ScanInfo']
    if iVictim not in dScanInfo:
        return 0
    return dScanInfo[iVictim]


def Func676(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if 'ScanNum' not in oSkill.m_Collect:
        return 0
    return oSkill.m_Collect['ScanNum']


def Func677(obj, dData, dMsgInfo, dOtherArgs):
    if not (obj.m_FightType & WARRIOR_HERO) or obj.m_SID != EXECUTOR_HERO:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    iKillLine = obj.m_FlawCon.GetKillLine(oVictim)
    iHpRatio = (oVictim.HP() + oVictim.Shield() + oVictim.Armor()) * 10000 // (oVictim.QueryAttr('HPMax') + oVictim.QueryAttr('ShieldMax') + oVictim.QueryAttr('ArmorMax'))
    if iKillLine <= iHpRatio:
        return 0
    return iKillLine - iHpRatio


def Func678(obj, dData, dMsgInfo, dOtherArgs):
    oGame = obj.m_Game
    if not obj.m_FightType & WARRIOR_HERO:
        iVictim = dData[FML_ARG_VID]
        oHero = oGame.GetObject(iVictim)
    else:
        oHero = obj
    if not oHero:
        return 100
    return oHero.QuerySavedData('CycleGSCashRelief', 100)


def Func679(obj, dData, dMsgInfo, dOtherArgs, iPerform):
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if not oWeapon:
        return 0
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return 0
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.MaxPFBullet()


def Func680(obj, dData, dMsgInfo, dOtherArgs, sKey):
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if not oWeapon:
        return 0
    if sKey not in oWeapon.m_ExtItemAttr:
        return 0
    return oWeapon.m_ExtItemAttr[sKey]


def Func681(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    oPerform = oOwner.GetThrowPerform()
    if not oPerform:
        return 0
    iBullet = oPerform.CalAttr('BulletSID')
    return oOwner.m_BulletCon.GetMaxBullet(iBullet)


def Func682(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    oPerform = oOwner.GetThrowPerform()
    if not oPerform:
        return 0
    iBullet = oPerform.CalAttr('BulletSID')
    return oOwner.m_BulletCon.Bullet(iBullet)


def Func683(obj, dData, dMsgInfo, dOtherArgs):
    return dMsgInfo['Cost'] * 100 // dMsgInfo['MaxBullet']


def Func684(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs, iFiltDead = 0)
    if not oVictim:
        return 0
    dInfo = oVictim.Query(sAttr, { })
    if obj.m_ID in dInfo:
        return dInfo[obj.m_ID]
    return 0


def Func685(obj, dData, dMsgInfo, dOtherArgs):
    oLifeCycleOwner = dData['LifeCycle'].GetObject()
    dPFRecoverWeaponPFBullet = oLifeCycleOwner.GetArgValue('PFRecoverWeaponPFBullet', { })
    if 'Skill' in dMsgInfo:
        iEventPerform = dMsgInfo['Skill'].m_Base['pfid']
    elif 'pfid' in dMsgInfo:
        iEventPerform = dMsgInfo['pfid']
    else:
        iEventPerform = 0
    if iEventPerform in dPFRecoverWeaponPFBullet:
        return dPFRecoverWeaponPFBullet[iEventPerform]
    if 'Default' in dPFRecoverWeaponPFBullet:
        return dPFRecoverWeaponPFBullet['Default']
    return 0


def Func686(obj, dData, dMsgInfo, dOtherArgs, iPerform, sAttr):
    oWeapon = dData['LifeCycle'].GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return 0
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return 0
    if sAttr not in oPerform.m_Attr:
        return 0
    return oPerform.CalAttr(sAttr)


def Func687(obj, dData, dMsgInfo, dOtherArgs):
    oWeapon = dData['LifeCycle'].GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform:
        return 0
    oLinkAttr = oPerform.GetAttr('MaxPFBullet')
    if not oLinkAttr.m_Type == 'Link':
        return 0
    return oLinkAttr.GetChangeValue(oPerform)


def Func688(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim and oVictim.m_Resistance:
        return oVictim.m_Resistance.m_CurValue
    return 0


def Func689(obj, dData, dMsgInfo, dOtherArgs):
    if 'ActiveAbility' in dMsgInfo:
        return len(dMsgInfo['ActiveAbility'])
    return 0


def Func690(obj, dData, dMsgInfo, dOtherArgs):
    return len(obj.m_Game.m_WarMgr.GetAllAIHero())


def Func691(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs, iFiltDead = 0)
    if not oVictim:
        return 0
    dInfo = obj.Query(sAttr, { })
    if oVictim.m_ID in dInfo:
        return dInfo[oVictim.m_ID]
    return 0


def Func692(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if not 'VID' or 'StateID' not in dMsgInfo:
        return 0
    oStateOwner = obj.m_Game.GetObject(dMsgInfo['VID'])
    if not oStateOwner:
        return 0
    oStateCon = oStateOwner.m_State
    oState = oStateCon.GetItem(dMsgInfo['StateID'])
    if not oState:
        return 0
    dStateInfo = oState.m_StateInfo
    dArg = dStateInfo['arg'] if 'arg' in dStateInfo else { }
    if sKey in dArg:
        return dArg[sKey]
    return 0


def Func693(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'IsDam' not in dMsgInfo or not dMsgInfo['IsDam']:
        return 0
    if 'TotalDam' not in dMsgInfo:
        return 0
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs, iFiltDead = 0)
    if not oVictim:
        return 0
    sAttr = 'HP' if oVictim.Query('Defend2HP', 0) else sAttr
    if sAttr not in cl_formula.g_HpTypeIndex:
        return 0
    iIndex = cl_formula.g_HpTypeIndex[sAttr]
    return dMsgInfo['TotalDam'][iIndex]


def Func694(obj, dData, dMsgInfo, dOtherArgs):
    oAttack = AnalyseAttackObj(obj, dData, dMsgInfo, dOtherArgs)
    if oAttack:
        return oAttack.HP() + oAttack.Shield() + oAttack.Armor()
    return 0


def Func695(obj, dData, dMsgInfo, dOtherArgs):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if oVictim:
        return oVictim.HP() + oVictim.Shield() + oVictim.Armor()
    return 0


def Func696(obj, dData, dMsgInfo, dOtherArgs):
    iVictim = AnalyseVictim(obj, dData, dMsgInfo, dOtherArgs)
    return iVictim in obj.m_Game.m_WarMgr.GetAllHeroExceptAI()


def Func697(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = obj.m_InkCon
    return oInkCon.CheckTargetInInkAreaNum(obj.m_ID)


def Func698(obj, dData, dMsgInfo, dOtherArgs):
    iOwner = dMsgInfo['Owner'] if 'Owner' in dMsgInfo else 0
    if iOwner == obj.m_PlayerID:
        iAdder = dMsgInfo['Adder'] if 'Adder' in dMsgInfo else 0
        if iAdder != iOwner:
            return 1
        return 0
    return 0


def Func699(obj, dData, dMsgInfo, dOtherArgs):
    iAdder = dMsgInfo['Adder'] if 'Adder' in dMsgInfo else 0
    iOwner = dMsgInfo['Owner'] if 'Owner' in dMsgInfo else 0
    if iAdder and iAdder == iOwner:
        return 1
    return 0


def Func700(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_FightType & WARRIOR_MONSTER:
        SendAlert('err', '公式【存活怪物召唤物数量】拥有者不是怪物 %s' % obj)
        return 0
    oGame = obj.m_Game
    iNowCnt = 0
    for iSummonID in obj.m_MonsterSummon:
        oSummon = oGame.GetObject(iSummonID, PY_FLAG_DEAD)
        if oSummon:
            iNowCnt += 1
    
    return iNowCnt


def Func701(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_FightType & WARRIOR_HERO:
        obj = obj.m_PetCon.GetCurPet()
        if not obj:
            return 0
    if obj.m_FightType not in (WARRIOR_PET_MINI, WARRIOR_PET_MINICLONE):
        return 0
    if obj.m_FightType == WARRIOR_PET_MINI:
        return len(obj.m_Clone)
    oOwnerPet = obj.m_Game.GetObject(obj.m_OwnerPet)
    if oOwnerPet:
        return len(oOwnerPet.m_Clone)
    return 0


def Func702(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_FightType != WARRIOR_PET_MINI:
        return 0
    return obj.m_MaxCloneNum


def Func703(obj, dData, dMsgInfo, dOtherArgs):
    oRelicCon = obj.m_RelicCon
    for iRelic, iElement in ALL_ELEMENT_RELIC.items():
        if oRelicCon.GetPerform(iRelic):
            return iElement
    
    return 0


def Func704(obj, dData, dMsgInfo, dOtherArgs, iSID):
    oSeasonSuitElement = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuitElement:
        return 0
    return oSeasonSuitElement.GetSuitElement(obj, iSID)


def Func705(obj, dData, dMsgInfo, dOtherArgs):
    iNowElement = obj.QuerySavedData('SeasonSuit_NowElement', 0)
    if iNowElement not in SUIT_ELEMENT:
        return 0
    lstCanChoose = [ iElement for iElement in SUIT_ELEMENT if iElement != iNowElement ]
    return lstCanChoose[obj.m_Game.Random(2)]


def Func706(obj, dData, dMsgInfo, dOtherArgs):
    if 'Option' in dMsgInfo:
        return dMsgInfo['Option']
    return -1


def Func707(obj, dData, dMsgInfo, dOtherArgs):
    return obj.Query('StateCountEff', 100) / 100


def RelicQualityCount(lstRelic, iQuality):
    iCount = 0
    for iRelic in lstRelic:
        oRelic = cl_perform.GetPerformModule(iRelic)
        if not oRelic or not iQuality:
            if iQuality and oRelic.m_Quality == iQuality:
                iCount += 1
                continue
    
    return iCount


def Func708(obj, dData, dMsgInfo, dOtherArgs, iQuality):
    if 'RelicOutput' not in dMsgInfo:
        return 0
    return RelicQualityCount(dMsgInfo['RelicOutput'], GetQualityNumber(iQuality))


def Func709(obj, dData, dMsgInfo, dOtherArgs, iQuality):
    if 'RelicInput' not in dMsgInfo:
        return 0
    return RelicQualityCount(dMsgInfo['RelicInput'], GetQualityNumber(iQuality))


def Func710(obj, dData, dMsgInfo, dOtherArgs):
    oGame = obj.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return 0
    oScene = oGame.m_SceneMgr.GetScene(obj.m_Scene)
    if not oScene:
        return 0
    iLevel = oScene.m_Level
    oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
    if not oLevelNode:
        return 0
    dMonsterSum = oLevelNode.GetRoomMonsterInfo(oLevelNode.m_CurRoomPos)
    iAll = dMonsterSum['Wait'] + dMonsterSum['Die'] + dMonsterSum['Live']
    if not iAll:
        return 0
    return (dMonsterSum['Wait'] + dMonsterSum['Live']) * 100 // iAll


def Func711(obj, dData, dMsgInfo, dOtherArgs, iQuality):
    iAssignQuality = GetQualityNumber(iQuality)
    if not iAssignQuality:
        return 0
    if 'OldQuality' not in dMsgInfo:
        return 0
    lstOldQuality = dMsgInfo['OldQuality']
    iNum = 0
    for _, iQuality in lstOldQuality:
        if iAssignQuality != iQuality:
            continue
        iNum += 1
    
    return iNum


def Func712(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    return obj.GetExcessRatioByType(sAttr)


def Func713(obj, dData, dMsgInfo, dOtherArgs):
    iResult = 0
    oRelicCon = obj.m_RelicCon
    for iRelic in ALL_ELEMENT_RELIC:
        if oRelicCon.GetPerform(iRelic):
            iResult += 1
    
    return iResult


def Func714(obj, dData, dMsgInfo, dOtherArgs):
    return dMsgInfo['OldBullet']


def Func715(obj, dData, dMsgInfo, dOtherArgs, iTargetLv):
    oSeasonSuit = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return 0
    iCount = 0
    dSuitEnable = oSeasonSuit.GetAllSuitGradeInfo(obj.m_ID)
    for iLv in dSuitEnable.values():
        if iTargetLv == iLv:
            iCount += 1
    
    return iCount


def Func716(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'LifeCycle' not in dData:
        return 0
    oTask = dData['LifeCycle'].GetObject()
    return oTask.GetSaveData(sAttr)


def Func717(obj, dData, dMsgInfo, dOtherArgs, sArg):
    if 'LifeCycle' not in dData:
        return 0
    pfobj = dData['LifeCycle'].GetObject()
    if not pfobj:
        return 0
    return pfobj.GetArgValue(sArg)


def Func718(obj, dData, dMsgInfo, dOtherArgs):
    if 'ChangeNum' in dMsgInfo:
        return abs(dMsgInfo['ChangeNum'])
    return 0


def Func719(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_RelicCon.m_BlankRelic


def Func720(obj, dData, dMsgInfo, dOtherArgs):
    if 'RelicOutput' not in dMsgInfo:
        return 0
    iNum = 0
    lstSuitCoreRelic = GetSuitCoreRelicMap().values()
    for iRelic, iIsPick in dMsgInfo['RelicOutput'].items():
        if iRelic in lstSuitCoreRelic and not iIsPick:
            iNum += 1
    
    return iNum


def Func721(obj, dData, dMsgInfo, dOtherArgs, iThreshold):
    oSuitElement = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return 0
    iNum = 0
    dCurSituate = oSuitElement.GetCurSituate(obj)
    for iSuit, dCondictionInfo in dCurSituate.items():
        clsSuit = GetSeasonSuitCls(iSuit)
        if not clsSuit:
            continue
        iCoreRelic = clsSuit.m_CoreRelic
        if not iCoreRelic:
            continue
        if sum(dCondictionInfo.values()) + oSuitElement.GetConditionReduceNum(obj.m_ID, iSuit) >= len(dCondictionInfo) - iThreshold:
            iNum += 1
    
    return iNum


def Func722(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = obj.GetThrowPerform()
    if not oPerform:
        return 0
    return oPerform.m_SID


def Func723(obj, dData, dMsgInfo, dOtherArgs, iTag):
    oSeasonSuit = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return 0
    iCount = 0
    dSuitEnable = oSeasonSuit.GetAllSuitGradeInfo(obj.m_ID)
    for iSuit, iLv in dSuitEnable.items():
        if iTag in GetSeasonSuitTag(iSuit) and iLv >= oSeasonSuit.GetSuitMaxGrade(iSuit):
            iCount += 1
    
    return iCount


def Func724(obj, dData, dMsgInfo, dOtherArgs):
    if 'Bene' not in dMsgInfo:
        return 0
    iBenediction = dMsgInfo['Bene']
    clsBenediction = cl_perform.GetPerformModule(iBenediction)
    if not clsBenediction or clsBenediction.m_PFType != PF_TYPE_BENEDICTION:
        return 0
    return iBenediction


def Func725(obj, dData, dMsgInfo, dOtherArgs):
    if 'ChangeNum' in dMsgInfo:
        return dMsgInfo['ChangeNum']
    return 0


def Func726(obj, dData, dMsgInfo, dOtherArgs):
    lstResult = dMsgInfo['Result']
    if not lstResult:
        return 0
    return lstResult[0]


def Func727(obj, dData, dMsgInfo, dOtherArgs, iSuit, sKey):
    oSeasonSuit = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return 0
    return oSeasonSuit.GetSavedSuitArg(obj, iSuit, sKey)


def Func728(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oAttr = obj.GetAttr(sAttr)
    iMulPositive = oAttr.GetMulPositiveAttr()
    return iMulPositive / 100


def Func729(obj, dData, dMsgInfo, dOtherArgs):
    oWarMgr = obj.m_Game.GetWarMgr()
    oReport = oWarMgr.GetComponent('Warreport')
    if not oReport:
        return 0
    return oReport.m_WarReportData.GetPlayerWarInfo(obj.m_PlayerID, 'CreateGoldencupCount')


def Func730(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = obj.GetCareerPerform()
    if not oPerform:
        return 0
    return obj.m_Perform.GetCover(oPerform.m_SID)


def Func731(obj, dData, dMsgInfo, dOtherArgs, iSuit):
    oSeasonSuit = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return 0
    iHero = obj.m_ID
    if iSuit in oSeasonSuit.m_Enable[iHero]:
        return oSeasonSuit.m_Enable[iHero][iSuit]
    return 0


def Func732(obj, dData, dMsgInfo, dOtherArgs):
    if 'iTime' in dMsgInfo:
        return dMsgInfo['iTime']
    return 0


def Func734(obj, dData, dMsgInfo, dOtherArgs):
    return dData['LotteryCnt']


def Func735(obj, dData, dMsgInfo, dOtherArgs):
    oSeasonSuitElement = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuitElement:
        return 0
    return oSeasonSuitElement.GetEnableSuitNum(obj.m_ID)


def Func736(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if not dMsgInfo or 'Custom' not in dMsgInfo:
        return 0
    if sKey in dMsgInfo['Custom']:
        return dMsgInfo['Custom'][sKey]
    return 0


def Func737(obj, dData, dMsgInfo, dOtherArgs):
    oSeasonSuitElement = obj.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuitElement:
        return 0
    return oSeasonSuitElement.GetAllSuitGrade(obj.m_ID)


def Func738(obj, dData, dMsgInfo, dOtherArgs, sKey):
    oGame = obj.m_Game
    tLineIdx = obj.m_LineIdx
    if not tLineIdx:
        return 0
    oCtrlMgr = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oChallenge = oCtrlMgr.m_RoomChallenge.GetChallenge(tLineIdx)
    if not oChallenge:
        return 0
    if sKey not in oChallenge.m_CollectData:
        return 0
    return oChallenge.m_CollectData[sKey]


def Func739(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return 0
    oTask = dData['LifeCycle'].GetObject()
    return oTask.m_ID


def Func740(obj, dData, dMsgInfo, dOtherArgs):
    return dData['ExtraLotteryCnt']


def Func742(obj, dData, dMsgInfo, dOtherArgs, sArg):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWandComp = oLifeCycle.GetObject()
    return oWandComp.GetArgValue(sArg)


def Func744(obj, dData, dMsgInfo, dOtherArgs, iType):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    return obj.m_PerformCDRate.GetPerformCDRateByType(iType)


def Func745(obj, dData, dMsgInfo, dOtherArgs, iType):
    oAttacker = GetStateAttack(obj, dData)
    if not oAttacker:
        return 0
    if not oAttacker.m_FightType & WARRIOR_HERO:
        return 0
    return oAttacker.m_PerformCDRate.GetPerformCDRateByType(iType)


def Func746(obj, dData, dMsgInfo, dOtherArgs, iStateSID):
    oLifeCycle = dData['LifeCycle']
    dEvent = oLifeCycle.AttrCache()
    if 'ItemID' in dEvent:
        iItem = dEvent['ItemID']
    elif 'RS' in dEvent:
        iItem = dEvent['RS'].Query('Item')
    else:
        return 0
    oState = obj.m_State.GetStateBySource(iStateSID, obj.m_ID, iItem)
    if not oState:
        return 0
    return oState.GetCount()


def Func747(obj, dData, dMsgInfo, dOtherArgs, iWandSID, sKey):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWand = oLifeCycle.GetObject().GetMyItem()
    if not oWand:
        return 0
    dComp = oWand.m_Comp
    if WAND_COMP_TYPE_ACTION not in dComp:
        return 0
    iResult = 0
    dActionWandComp = dComp[WAND_COMP_TYPE_ACTION]
    for oWandComp in dActionWandComp.values():
        if oWandComp.m_SID == iWandSID:
            iResult += oWandComp.GetArgValue(sKey)
    
    return iResult


def Func748(obj, dData, dMsgInfo, dOtherArgs):
    oState = dData['LifeCycle'].GetObject()
    if oState:
        return Frame2Time(oState.GetRemainTime())
    return 0


def Func749(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oItem = oLifeCycle.GetObject().GetMyItem()
    if not oItem:
        return 0
    return oItem.m_BaseGrade


def Func750(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_WandCon:
        return 0
    pfobj = dData['LifeCycle'].GetObject()
    if not pfobj:
        return 0
    oWand = obj.m_WandCon.GetWandByID(pfobj.m_Item)
    if not oWand:
        return 0
    return pfobj.m_Item


def Func751(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = dData['LifeCycle'].GetObject()
    if not oOwner:
        return 0
    oItem = oOwner.GetMyItem()
    if not oItem:
        return 0
    return oItem.m_ID


def Func752(obj, dData, dMsgInfo, dOtherArgs, iWandSID, iDefault):
    oWand = GetSourceWand(obj, dData)
    if not oWand or oWand.m_SID != iWandSID:
        return iDefault
    return oWand.GetWandCount()


def Func753(obj, dData, dMsgInfo, dOtherArgs):
    oWand = obj.m_WandCon.GetCurWand()
    if not oWand:
        return 0
    return oWand.m_Grade


def Func754(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWand = oLifeCycle.GetObject().GetMyItem()
    if not oWand:
        return 0
    dComp = oWand.m_Comp
    if WAND_COMP_TYPE_ACTION not in dComp:
        return 0
    dActionWandComp = dComp[WAND_COMP_TYPE_ACTION]
    return len(dActionWandComp)


def Func755(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = dData['LifeCycle'].GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform:
        return 0
    if sAttr not in oPerform.m_Attr:
        return 0
    return oPerform.CalAttr(sAttr)


def Func756(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oItem = oLifeCycle.GetObject().GetMyItem()
    if not oItem:
        return 0
    return GetItemAttr(sAttr, oItem)


def Func758(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWandComp = oLifeCycle.GetObject()
    if not oWandComp:
        return 0
    return oWandComp.GetKeepValue(sAttr, 0)


def Func759(obj, dData, dMsgInfo, dOtherArgs):
    if 'Weapon' not in dOtherArgs:
        return 0
    oWeapon = dOtherArgs['Weapon']
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    oBulletContainer = obj.m_BulletCon
    iBulletSID = oBulletCom.m_BulletType
    return oBulletContainer.GetMaxBullet(iBulletSID)


def Func760(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    return oOwner.Query(sAttr, 0)


def Func761(obj, dData, dMsgInfo, dOtherArgs, iPos):
    if iPos > 2:
        return 0
    if 'Cartoon' not in dMsgInfo:
        return 0
    dCartoon = dMsgInfo['Cartoon']
    if 'Final' in dCartoon:
        return dCartoon['Final'][iPos]
    if 'CurPos' in dCartoon:
        return dCartoon['CurPos'][iPos]
    return 0


def Func762(obj, dData, dMsgInfo, dOtherArgs, iPFSID, sKey, iSuperNum):
    oPerform = obj.GetPerform(iPFSID)
    if not oPerform:
        return 0
    iSuperNum += 1
    sArgs = f'''{sKey}{iSuperNum}'''
    return oPerform.GetArgValue(sArgs)


def Func763(obj, dData, dMsgInfo, dOtherArgs):
    oPerform = obj.GetThrowPerform()
    if not oPerform:
        return NO_THROW_PERFORM_CASE
    return oPerform.BulletUse()


def Func764(obj, dData, dMsgInfo, dOtherArgs):
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'ItemID' in oSkill.m_Cache:
            return oSkill.m_Cache['ItemID']
        return 0
    if 'ItemID' in dMsgInfo:
        return dMsgInfo['ItemID']
    return 0


def Func765(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWand = oLifeCycle.GetObject().GetMyItem()
    if not oWand:
        return 0
    tGrooveNum = oWand.GetWandGroveNum()
    return tGrooveNum[WAND_COMP_TYPE_ACTION]


def Func766(obj, dData, dMsgInfo, dOtherArgs):
    if 'RealDiedCnt' in dData:
        return dData['RealDiedCnt']
    oWatch = obj.m_Game.m_WarMgr.GetComponent('WatchElement')
    if not oWatch:
        return 0
    return oWatch.GetRelifeInfo(obj.m_PlayerID, 'RealDiedCnt')


def Func767(obj, dData, dMsgInfo, dOtherArgs):
    return obj.m_Scene


def Func768(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    return oOwner.Query('PlantAttMul')


def Func769(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_SID != GARDENER_HERO:
        return 0
    oGardencon = obj.m_GardenerCon
    return len(oGardencon.m_SeedDict)


def Func770(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_SID != GARDENER_HERO:
        return 0
    oGardencon = obj.m_GardenerCon
    return len(oGardencon.m_PlantDict)


def Func771(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    return oOwner.Query('PlantAttSpeedMul')


def Func772(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oComp = oLifeCycle.GetObject()
    if not oComp:
        return 0
    oWand = oComp.GetMyItem()
    if not oWand:
        return 0
    return len(oWand.m_ActionCompSealStatus)


def Func773(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    dLimitBened = GetLimitSeasonBened()
    oBenediction = obj.m_BenedictionCon
    for oPerform in oBenediction.m_Perform.values():
        if oPerform.m_PFType != PF_TYPE_BENEDICTION:
            continue
        if oPerform.m_SID not in dLimitBened:
            continue
        iCount += 1
    
    return iCount


def Func774(obj, dData, dMsgInfo, dOtherArgs, iCompSID):
    oWand = obj.m_WandCon.GetCurWand()
    if not oWand:
        return 0
    for oComp in oWand.m_Comp[WAND_COMP_TYPE_CONDITION].values():
        if oComp.m_SID == iCompSID:
            return 1
    
    return 0


def Func775(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWand = oLifeCycle.GetObject().GetMyItem()
    if not oWand:
        return 0
    iResult = 0
    dActionWandComp = oWand.GetWandCompByType(WAND_COMP_TYPE_ACTION)
    for oWandComp in dActionWandComp.values():
        if oWandComp.m_CopyWandTimes:
            iResult += oWandComp.GetArgValue(sKey)
    
    return iResult


def Func776(obj, dData, dMsgInfo, dOtherArgs):
    oWand = obj.m_WandCon.GetCurWand()
    if not oWand:
        return 0
    return oWand.m_ID


def Func777(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWandComp = oLifeCycle.GetObject()
    if not oWandComp:
        return 0
    return oWandComp.GetConditionCount()


def Func778(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return -1
    oLifeCycle = dData['LifeCycle']
    oWand = oLifeCycle.GetObject().GetMyItem()
    if not oWand:
        return -1
    (_, iActionCompNum) = oWand.GetWandGroveNum()
    return iActionCompNum - 1


def Func779(obj, dData, dMsgInfo, dOtherArgs):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oWandAbility = oLifeCycle.GetObject()
    if not oWandAbility:
        return 0
    return oWandAbility.GetFinalValue()


def Func780(obj, dData, dMsgInfo, dOtherArgs, sKey):
    if 'LifeCycle' not in dData:
        return 0
    oLifeCycle = dData['LifeCycle']
    oItem = oLifeCycle.GetObject().GetMyItem()
    if not oItem:
        return 0
    return oItem.QueryTmp(sKey)


def Func781(obj, dData, dMsgInfo, dOtherArgs, iItem, sKey):
    oItem = obj.m_WieldCon.GetItemByID(iItem)
    if not oItem and obj.m_WandCon:
        oItem = obj.m_WandCon.GetWandByID(iItem)
    if not oItem:
        return 0
    return oItem.QueryTmp(sKey)


def Func782(obj, dData, dMsgInfo, dOtherArgs, sid, sArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    oPerform = oOwner.GetPerform(sid)
    if not oPerform:
        return 0
    return oPerform.GetArgValue(sArgs)


def Func784(obj, dData, dMsgInfo, dOtherArgs, iCalOverflow = 0):
    if obj.m_SID != WUKONG_HERO:
        return 0
    iStrength = obj.Query('StrengthLayer')
    if iCalOverflow:
        iStrength += obj.Query('OverFlowStrengthLayer')
    return iStrength


def Func785(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = obj.m_WieldCon.GetCurWeapon(DEPUTY_HOLD)
    if oWeapon:
        return GetItemAttr(sAttr, oWeapon)
    return 0


def Func786(obj, dData, dMsgInfo, dOtherArgs):
    if 'PreCash' in dMsgInfo:
        return dMsgInfo['PreCash']
    return 0


def Func788(obj, dData, dMsgInfo, dOtherArgs, iPos):
    oWand = GetSourceWand(obj, dData)
    if not oWand:
        return 0
    oComp = oWand.GetCompByPos(WAND_COMP_TYPE_ACTION, iPos)
    if not oComp:
        return 0
    return oComp.m_SID


def Func789(obj, dData, dMsgInfo, dOtherArgs, iPos):
    oWand = GetSourceWand(obj, dData)
    if not oWand:
        return 0
    oComp = oWand.GetCompByPos(WAND_COMP_TYPE_ACTION, iPos)
    if not oComp:
        return 0
    return oComp.m_Level


def Func790(obj, dData, dMsgInfo, dOtherArgs):
    if 'BuyNum' in dMsgInfo:
        return dMsgInfo['BuyNum']
    return 0


def Func791(obj, dData, dMsgInfo, dOtherArgs, iEndlessResult):
    (iLayer, _) = GetLayerAndLevel(obj)
    if iLayer > MAX_LAYER:
        return iEndlessResult
    return iLayer


def Func792(obj, dData, dMsgInfo, dOtherArgs, iEndlessResult):
    (iLayer, iLevel) = GetLayerAndLevel(obj)
    if iLayer > MAX_LAYER:
        return iEndlessResult
    return iLevel


def Func793(obj, dData, dMsgInfo, dOtherArgs):
    if 'Wand' not in dMsgInfo:
        return None
    iWand = dMsgInfo['Wand']
    oWand = obj.m_WandCon.GetWandByID(iWand)
    if not oWand:
        return 0
    return oWand.GetCompIconNum(WAND_COMP_TYPE_CONDITION)


def Func794(obj, dData, dMsgInfo, dOtherArgs):
    oWand = GetSourceWand(obj, dData)
    if not oWand:
        return 0
    dComp = oWand.m_Comp
    if WAND_COMP_TYPE_CONDITION not in dComp:
        return 0
    dActionWandComp = dComp[WAND_COMP_TYPE_CONDITION]
    return len(dActionWandComp)


def Func795(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = AnalyseWeapon(obj, dData, dMsgInfo, dOtherArgs)
    if not oWeapon:
        return 0
    return GetItemAttr(sAttr, oWeapon)


def Func796(obj, dData, dMsgInfo, dOtherArgs):
    if 'Wand' not in dMsgInfo:
        return -1
    oWand = obj.m_WandCon.GetWandByID(dMsgInfo['Wand'])
    if not oWand:
        return -1
    dComp = oWand.m_Comp[WAND_COMP_TYPE_CONDITION]
    if not dComp:
        return -1
    iPos = min(dComp)
    return iPos


def Func797(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_SID != GARDENER_HERO:
        return 0
    return obj.m_GardenerCon.GetRandomSeedID()


def Func798(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs, iFiltDead = 0)
    if not oVictim:
        return 0
    return oVictim.Query(sAttr)


def Func799(obj, dData, dMsgInfo, dOtherArgs, sKey, iFrame):
    oLifeCycleOwner = dData['LifeCycle'].GetObject()
    if not oLifeCycleOwner:
        return 0
    dTimeLimitInfo = oLifeCycleOwner.GetArgValue(sKey, { })
    if iFrame not in dTimeLimitInfo:
        return 0
    return dTimeLimitInfo[iFrame]


def Func800(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    return oOwner.Query('PlantHpAdd')


def Func801(obj, dData, dMsgInfo, dOtherArgs):
    oOwner = obj.GetOwner()
    if not oOwner:
        return 0
    return oOwner.Query('PlantAttDisAdd')


def Func802(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_DiceCon:
        return 0
    return obj.m_DiceCon.GetAccumulatedRollPoint()


def Func803(obj, dData, dMsgInfo, dOtherArgs):
    if not obj or 'Reward' not in dMsgInfo:
        return 0
    return dMsgInfo['Reward']


def Func804(obj, dData, dMsgInfo, dOtherArgs):
    oLifeCycleOwner = dData['LifeCycle'].GetObject()
    if not oLifeCycleOwner:
        return 0
    return oLifeCycleOwner.m_Item


def Func805(obj, dData, dMsgInfo, dOtherArgs):
    oLifeCycleOwner = dData['LifeCycle'].GetObject()
    if not oLifeCycleOwner:
        return 0
    oDice = oLifeCycleOwner.GetMyItem()
    if not oDice:
        return 0
    return oDice.m_ID


def Func806(obj, dData, dMsgInfo, dOtherArgs):
    iCount = 0
    for oPerform in obj.m_TalentCon.GetAllPerform():
        if oPerform.m_PFType != PF_TYPE_TALENT:
            continue
        if oPerform.m_Level != oPerform.m_MaxLevel:
            continue
        iCount += 1
    
    return iCount


def Func807(obj, dData, dMsgInfo, dOtherArgs):
    oDiceElement = obj.m_Game.m_WarMgr.GetDiceElement()
    if not oDiceElement:
        return 0
    return oDiceElement.GetAccumulatedChallengePoint()


def Func808(obj, dData, dMsgInfo, dOtherArgs):
    iOverflowBullet = dMsgInfo['NewBullet'] - dMsgInfo['MaxBullet']
    if iOverflowBullet > 0:
        return iOverflowBullet
    return 0


def Func809(obj, dData, dMsgInfo, dOtherArgs):
    if 'Point' in dMsgInfo:
        return dMsgInfo['Point']
    oLifeCycleOwner = dData['LifeCycle'].GetObject()
    if not oLifeCycleOwner:
        return 0
    oDice = oLifeCycleOwner.GetMyItem()
    if not oDice:
        return 0
    return oDice.m_RollPoint


def Func810(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if 'LifeCycle' not in dData or not dData['LifeCycle']:
        return 0
    sKey = dData['LifeCycle'].m_Key
    if not obj.HasAttr(sAttr):
        return 0
    oAttr = obj.GetAttr(sAttr)
    return oAttr.GetExcludeValue([
        sKey])


def Func811(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = dData['LifeCycle'].GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform:
        return 0
    oAttr = oPerform.GetAttr(sAttr)
    if not oAttr:
        return 0
    if oAttr.m_Type == 'Link':
        if oPerform.m_ID not in oAttr.m_BaseAttrDict:
            return 0
        return oAttr.m_BaseAttrDict[oPerform.m_ID].m_BaseValue
    return oAttr.m_BaseValue


def Func812(obj, dData, dMsgInfo, dOtherArgs, iState):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    oState = oVictim.m_State.GetItemBySource(iState, obj.m_ID)
    if not oState:
        return 0
    return Frame2Time(obj.m_Game.GetFrameNum() - oState.m_CreateFrame)


def Func813(obj, dData, dMsgInfo, dOtherArgs, sid, sAttr):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs)
    if not oVictim:
        return 0
    oState = oVictim.m_State.GetItemBySource(sid, obj.m_ID)
    if not oState:
        return 0
    return oState.GetArgValue(sAttr)


def Func814(obj, dData, dMsgInfo, dOtherArgs):
    if 'PredictChange' not in dMsgInfo:
        return 0
    return dMsgInfo['PredictChange'][2]


def Func815(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not obj.HasAttr(sAttr):
        return 0
    iValue = GetWarriorAttr(sAttr, obj)
    oAttr = obj.GetAttr(sAttr)
    iBaseValue = oAttr.GetBaseAttr()
    if not iBaseValue:
        return 0
    return 100 * (iValue - iBaseValue) // iBaseValue


def Func816(obj, dData, dMsgInfo, dOtherArgs):
    if obj.m_SID != GARDENER_HERO:
        return 0
    oGardencon = obj.m_GardenerCon
    return oGardencon.GetDomainBarrierID()


def Func817(obj, dData, dMsgInfo, dOtherArgs):
    iDice = 0
    if 'Dice' in dMsgInfo:
        iDice = dMsgInfo['Dice']
    elif 'Item' in dMsgInfo:
        iDice = dMsgInfo['Item']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iDice = oSkill.m_Custom['DiceID'] if 'DiceID' in oSkill.m_Custom else 0
    oDice = obj.m_DiceCon.GetDiceByID(iDice)
    if not oDice:
        return 0
    return oDice.m_RollPoint


def Func818(obj, dData, dMsgInfo, dOtherArgs):
    if 'TrueChange' not in dMsgInfo:
        return 0
    iAllChange = 0
    for iChange, _ in dMsgInfo['TrueChange']:
        iAllChange += iChange
    
    return iAllChange


def Func819(obj, dData, dMsgInfo, dOtherArgs, sid, sAttr):
    if obj.m_FightType & WARRIOR_HERO:
        oDevice = obj.GetDevice()
    elif obj.m_FightType & WARRIOR_DEVICE:
        oDevice = obj
    else:
        return 0
    oPerform = oDevice.GetPerform(sid)
    if not oPerform:
        return 0
    oAttr = oPerform.GetAttr(sAttr)
    if not oAttr:
        return 0
    return oAttr.GetBaseAttr()


def Func820(obj, dData, dMsgInfo, dOtherArgs):
    if not obj.m_FightType & WARRIOR_HERO:
        return 0
    if not obj.m_DiceCon:
        return 0
    return obj.m_DiceCon.GetDiceEnergy()


def Func821(obj, dData, dMsgInfo, dOtherArgs):
    oDiceCon = obj.m_DiceCon
    if not oDiceCon:
        return 0
    dAssembledDice = oDiceCon.GetAssembleDice()
    if not dAssembledDice:
        return 0
    iSumPoint = 0
    for iDice in dAssembledDice.values():
        oDice = oDiceCon.GetDiceByID(iDice)
        if not oDice:
            continue
        iSumPoint += oDice.m_RollPoint
    
    return iSumPoint


def Func822(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not obj.HasAttr(sAttr):
        return 0
    oAttr = obj.GetAttr(sAttr)
    return sum(oAttr.m_FixedAddition.values())


def Func823(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if not oSkill or sAttr not in oSkill.m_VarCache:
        return 0
    return oSkill.m_VarCache[sAttr]


def Func824(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    oPerform = obj.GetPerform(oSkill.m_Base['pfid'])
    if not oPerform or sAttr not in oPerform.m_Attr:
        return 0
    oAttr = oPerform.m_Attr[sAttr]
    return oAttr.GetValueIgnForce(obj)


def Func825(obj, dData, dMsgInfo, dOtherArgs):
    if 'ItemID' not in dMsgInfo:
        return 0
    iWeapon = dMsgInfo['ItemID']
    oWeapon = obj.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return 0
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform:
        return 0
    iMaxPFBullet = oPerform.MaxPFBullet()
    if not iMaxPFBullet:
        return 0
    return (oPerform.CurPFBullet() / iMaxPFBullet) * 100


def Func826(obj, dData, dMsgInfo, dOtherArgs):
    oAttacker = GetStateAttack(obj, dData)
    if not oAttacker:
        return 0
    return oAttacker.m_ID


def Func827(obj, dData, dMsgInfo, dOtherArgs):
    oDiceCon = obj.m_DiceCon
    if not oDiceCon:
        return 0
    dAssembledDice = oDiceCon.GetAssembleDice()
    if not dAssembledDice:
        return 0
    dResult = { }
    for iDice in dAssembledDice.values():
        oDice = oDiceCon.GetDiceByID(iDice)
        if not oDice:
            continue
        lstTag = GetDiceTagListInfo(oDice.m_SID)
        for iTag in lstTag:
            if iTag not in dResult:
                dResult[iTag] = 1
                continue
            dResult[iTag] += 1
        
    
    if not dResult:
        return 0
    return max(dResult.values())


def Func828(obj, dData, dMsgInfo, dOtherArgs, iState):
    oVictim = AnalyseVictimObj(obj, dData, dMsgInfo, dOtherArgs, iFiltDead = 0)
    if not oVictim:
        ErrLog.TraceAlert(f'''受击者来源自身的最大状态计数异常 iState = {iState}, oGameID = {obj.m_GameID}''')
        return 9999
    oState = oVictim.m_State.GetItemBySource(iState, obj.m_ID)
    if not oState:
        return 9999
    return oState.m_MaxCount


def Func829(obj, dData, dMsgInfo, dOtherArgs):
    oState = dData['LifeCycle'].GetObject()
    return oState.GetCount() >= oState.m_MaxCount


def Func830(obj, dData, dMsgInfo, dOtherArgs):
    oScene = obj.m_Game.m_SceneMgr.GetScene(obj.m_Scene)
    iCnt = oScene.m_SceneData.Query('PF-1986Cnt', 0)
    return iCnt


def Func831(obj, dData, dMsgInfo, dOtherArgs, iPerform, sAttr):
    oWeapon = dData['LifeCycle'].GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return 0
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.GetArgValue(sAttr)


def Func832(obj, dData, dMsgInfo, dOtherArgs, iState, iFromMsgAID = 0, iFromSameItem = 0):
    lstState = obj.m_State.GetItems(iState)
    if not lstState:
        return 0
    iAttack = 0
    if iFromMsgAID:
        if 'AID' in dMsgInfo:
            iAttack = dMsgInfo['AID']
        elif 'Skill' in dMsgInfo:
            iAttack = dMsgInfo['Skill'].m_Base['AID']
    iItemID = dData['ItemID'] if 'ItemID' in dData else 0
    for oState in lstState:
        if iFromMsgAID and oState.m_Attacker != iAttack:
            continue
        if iFromSameItem and oState.m_Item != iItemID:
            continue
        return 1
    
    return 0


def Func833(obj, dData, dMsgInfo, dOtherArgs):
    dSubCDPerform = obj.SetDefault('SubCDPerform', { })
    return len(dSubCDPerform)


def Func834(obj, dData, dMsgInfo, dOtherArgs):
    iGrade = 0
    lstWeapon = obj.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    for oWeapon in lstWeapon:
        iGrade += oWeapon.m_BaseGrade
    
    return iGrade


def Func835(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oWeapon = obj.m_WieldCon.GetItemByType(itemdef.EQUIP_TYPE_FUNDAMENTALWEAPON)
    if not oWeapon:
        return 0
    return GetItemAttr(sAttr, oWeapon)


def Func836(obj, dData, dMsgInfo, dOtherArgs):
    if 'Module' not in dData:
        return 0
    return len(obj.m_BackpackCon.GetSameTagModule(dData['Module']))


def Func837(obj, dData, dMsgInfo, dOtherArgs):
    oContainer = obj.m_WieldCon
    lstWeapon = oContainer.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    lstGrade = []
    for oWeapon in lstWeapon:
        lstGrade.append(oWeapon.m_BaseGrade)
    
    if lstGrade:
        return min(lstGrade)
    return 0


def Func839(obj, dData, dMsgInfo, dOtherArgs):
    oBackPackCon = obj.m_BackpackCon
    if not oBackPackCon:
        return 0
    return oBackPackCon.GetAllEquipModulePoint()


def Func840(obj, dData, dMsgInfo, dOtherArgs):
    oBackPackCon = obj.m_BackpackCon
    if not oBackPackCon:
        return 0
    return oBackPackCon.GetEquipModuleInfo(iCheckSID = 0, iCheckTag = 0, iCheckFullPoint = 1, iGetNum = 1)


def Func841(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oAttr = obj.GetAttr(sAttr)
    if not oAttr:
        return 0
    fVal = oAttr.CalMulChangeRatio()
    if not fVal:
        return 0
    return int(fVal * 10000)


def Func842(obj, dData, dMsgInfo, dOtherArgs):
    if 'Cash' in dMsgInfo:
        return dMsgInfo['Cash']
    return 0


def Func843(obj, dData, dMsgInfo, dOtherArgs):
    oCurWeapon = obj.m_WieldCon.GetCurWeapon()
    if not oCurWeapon:
        return 0
    if oCurWeapon.IsInitWeapon():
        return 0
    oBulletCom = oCurWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.BulletType()


def Func844(obj, dData, dMsgInfo, dOtherArgs):
    oResistance = obj.m_Resistance
    iPositiveAdd = 0
    if not oResistance:
        return iPositiveAdd
    for dApplyInfo in oResistance.m_Apply.values():
        for iApply in dApplyInfo.values():
            if iApply > 0:
                iPositiveAdd += iApply
        
    
    return iPositiveAdd


def Func845(obj, dData, dMsgInfo, dOtherArgs):
    return obj.Query('LockEnemy', 0)


def Func846(obj, dData, dMsgInfo, dOtherArgs, iTarget):
    oBackpackCon = obj.m_BackpackCon
    if not oBackpackCon:
        return 0
    return oBackpackCon.GetReachedPointsNum(iTarget)


def Func847(obj, dData, dMsgInfo, dOtherArgs):
    oBackPackCon = obj.m_BackpackCon
    if not oBackPackCon:
        return 0
    return oBackPackCon.GetOverflowPoint()


def Func848(obj, dData, dMsgInfo, dOtherArgs):
    if not dMsgInfo or 'Skill' not in dMsgInfo:
        return 0
    return dMsgInfo['Skill'].m_CacheData.m_ExtraTrajectory


def Func849(obj, dData, dMsgInfo, dOtherArgs):
    oBackPackCon = obj.m_BackpackCon
    if not oBackPackCon:
        return 0
    return oBackPackCon.GetDiffMaxPointModuleNum()


def Func850(obj, dData, dMsgInfo, dOtherArgs):
    oBackPackCon = obj.m_BackpackCon
    if not oBackPackCon:
        return 0
    return oBackPackCon.GetEffectMaxPointModuleNum()


def Func851(obj, dData, dMsgInfo, dOtherArgs, dCheckModuleTag = None, iExcludeOverflow = 1):
    oBackPackCon = obj.m_BackpackCon
    if not oBackPackCon:
        return 0
    return oBackPackCon.GetAllEquipModulePoint(dCheckModuleTag, iExcludeOverflow)


def Func852(obj, dData, dMsgInfo, dOtherArgs, sKey):
    return obj.GetCustomValue(sKey)


def Func853(obj, dData, dMsgInfo, dOtherArgs, iState):
    lstState = obj.m_State.GetItems(iState)
    if not lstState:
        return 0
    iResult = 0
    for oState in lstState:
        iResult += oState.GetCount()
    
    return iResult


def Func854(obj, dData, dMsgInfo, dOtherArgs, iTarget):
    oBackpackCon = obj.m_BackpackCon
    if not oBackpackCon:
        return 0
    return oBackpackCon.GetFullyActModuleCnt(iTarget)


def Func855(obj, dData, dMsgInfo, dOtherArgs, iDefault):
    if 'ModuleInfo' not in dData or 'Module' not in dData:
        return iDefault
    iModuleSID = dData['Module']
    dTag = GetModuleTag(iModuleSID)
    if not dTag:
        return iDefault
    iCount = 0
    dSameTagModule = { }
    for iTag in dTag:
        dModule = GetS7ModuleByTag(iTag)
        dSameTagModule.update(dModule)
    
    for iModuleSID, _ in dData['ModuleInfo']:
        if iModuleSID in dSameTagModule:
            iCount += 1
    
    if iCount:
        return iCount
    return iDefault


def Func857(obj, dData, dMsgInfo, dOtherArgs):
    lstWeapon = obj.m_WieldCon.GetWeapons(MAIN_HOLD)
    if not lstWeapon:
        return 0
    for oWeapon in lstWeapon:
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        oBulletContainer = obj.m_BulletCon
        iBulletSID = oBulletCom.m_BulletType
        return oBulletContainer.Bullet(iBulletSID)
    


def Func858(obj, dData, dMsgInfo, dOtherArgs):
    oS8Con = obj.m_S8Con
    if not oS8Con:
        return 0
    oEquipThirdItem = oS8Con.GetEquipThirdItem()
    if not oEquipThirdItem:
        return 0
    return oEquipThirdItem.GetKeepTime()


def Func859(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    pfobj = dData['LifeCycle'].GetObject()
    if not pfobj:
        return 0
    return pfobj.GetLevelArg(sAttr)


def Func860(obj, dData, dMsgInfo, dOtherArgs, sKey, iSuffix):
    if iSuffix:
        sKey = sKey + '-%s' % dData['LifeCycle'].m_Key
    oGame = obj.m_Game
    iCurFrame = oGame.GetFrameNum()
    iResult = 0
    dCustomData = obj.Query(sKey, { })
    dCustom = { }
    for iVal, iLastFrame in dCustomData.items():
        if iLastFrame < iCurFrame:
            continue
        iResult += iVal
        dCustom[iVal] = iLastFrame
    
    obj.Set(sKey, dCustom)
    return iResult


def Func861(obj, dData, dMsgInfo, dOtherArgs, iBulletSID):
    if 'Type' not in dMsgInfo or dMsgInfo['Type'] != NWARRIOR_DROP_BULLET:
        return 0
    if 'Item' not in dMsgInfo:
        return 0
    dItem = dMsgInfo['Item']
    iNum = 0
    for iSID, iCnt in dItem.items():
        if iSID != iBulletSID:
            continue
        iNum += iCnt
    
    return iNum


def Func862(obj, dData, dMsgInfo, dOtherArgs, sAttr):
    oS8Con = obj.m_S8Con
    if not oS8Con:
        return 0
    oEquipThirdItem = oS8Con.GetEquipThirdItem()
    if not oEquipThirdItem:
        return 0
    return oEquipThirdItem.QueryAttr(sAttr)


def Func863(obj, dData, dMsgInfo, dOtherArgs):
    oS8Con = obj.m_S8Con
    if not oS8Con:
        return 0
    oEquipThirdItem = oS8Con.GetEquipThirdItem()
    if not oEquipThirdItem:
        return 0
    return oEquipThirdItem.Energy()


def Func1(obj, dData, dMsgInfo, dOtherArgs, l, r):
    if l > r:
        return l
    return r


def Func2(obj, dData, dMsgInfo, dOtherArgs, l, r):
    if l < r:
        return l
    return r


def Func3(obj, dData, dMsgInfo, dOtherArgs, a, b):
    return a % b


def Func4(obj, dData, dMsgInfo, dOtherArgs, a, x):
    return a ** x


def Func5(obj, dData, dMsgInfo, dOtherArgs, iRet):
    return math.ceil(iRet)

g_NewFormulaDict = { }
setParams = {
    'obj',
    'dData',
    'dMsgInfo',
    'dOtherArgs'}
lstAttrs = list(globals())
for sAttr in lstAttrs:
    if sAttr[:2] == '__':
        continue
    func = globals()[sAttr]
    if not isinstance(func, types.FunctionType):
        continue
    if not func.__doc__:
        continue
    code = func.__code__
    if not setParams.issubset(code.co_varnames):
        continue
    lstArgs = []
    dTypeHints = get_type_hints(func)
    for sArg in code.co_varnames[4:code.co_argcount]:
        if sArg in dTypeHints and dTypeHints[sArg] == Attr:
            lstArgs.append((sArg, 'Attr'))
        else:
            lstArgs.append((sArg, 'Any'))
    
    for sName in func.__doc__.split('|'):
        iDefaultNum = len(func.__defaults__) if func.__defaults__ else 0
        g_NewFormulaDict[sName] = (func.__name__, lstArgs, iDefaultNum)
    


def GetNewFormulaDict():
    return g_NewFormulaDict


def CalAIDamage(oAttack, oVictim, iBaseDam, iAIDamFactor = 0):
    iSpecialMHP = oVictim.m_SpecialMHP
    iSpecialMHPWeight = oVictim.QueryAttr('SpecialMHPWeight')
    if not iSpecialMHP or not iSpecialMHPWeight:
        return 0
    iVictimTotalMax = oVictim.QueryAttr('HPMax') + oVictim.QueryAttr('ShieldMax') + oVictim.QueryAttr('ArmorMax')
    iFinalDam = (iBaseDam / iSpecialMHP * iSpecialMHPWeight / 100) * iVictimTotalMax
    if not iFinalDam:
        return 0
    dAIBaseDamageFactor = oAttack.Query('AIBaseDamageFactor', { })
    iAIlevelEnhance = oAttack.m_Agent.m_DamLevelEnhance if oAttack.m_Agent else 0
    if iAIlevelEnhance:
        iFinalDam = iFinalDam * iAIlevelEnhance / 100
    if iAIDamFactor:
        iFinalDam = iFinalDam * iAIDamFactor / 10000
    for iMul in dAIBaseDamageFactor.values():
        iFinalDam = iFinalDam * (10000 + iMul) / 10000
    
    if iFinalDam > MAX_DAMAGE:
        iFinalDam = MAX_DAMAGE
    return iFinalDam


def GetSourceWand(obj, dData):
    if not obj.m_WandCon:
        return None
    pfobj = dData['LifeCycle'].GetObject()
    if not pfobj:
        return None
    return obj.m_WandCon.GetWandByID(pfobj.m_Item)


def GetLayerAndLevel(obj):
    oLevelCtrl = obj.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    iLayer = 1
    iLevel = 0
    if oLevelCtrl:
        (iLayer, iLevel) = oLevelCtrl.GetLayerAndLevelMap(oLevelCtrl.m_LayerNum, oLevelCtrl.m_LevelNum)
    return (iLayer, iLevel)

QUERY_GET = 1
QUERYEXT_GET = 2
QUERYBASE_GET = 3
ATTR_GET = 4
FUNC_GET = 5
EXTSET_GET = 6
ITEMBASE_GET = 7
g_AttrGetFunc = {
    'Grade': ATTR_GET,
    'Speed': FUNC_GET,
    'AttSpeed': QUERY_GET,
    'MoveSpeed': QUERY_GET,
    'HP': FUNC_GET,
    'HPMax': QUERY_GET,
    'Armor': FUNC_GET,
    'ArmorMax': QUERY_GET,
    'Shield': FUNC_GET,
    'ShieldMax': QUERY_GET,
    'Energy': FUNC_GET,
    'EnergyMax': QUERY_GET,
    'Att': QUERY_GET,
    'Toughness': QUERY_GET,
    'RHP': QUERY_GET,
    'RShield': QUERY_GET,
    'REnergy': QUERY_GET,
    'DefKnockBack': QUERY_GET,
    'DebuffFactor': QUERY_GET,
    'BAtt': QUERYBASE_GET,
    'BMoveSpeed': QUERYBASE_GET,
    'BAttSpeed': QUERYBASE_GET,
    'BHPMax': QUERYBASE_GET,
    'EAtt': QUERYEXT_GET,
    'EMoveSpeed': QUERYEXT_GET,
    'EAttSpeed': QUERYEXT_GET,
    'EHPMax': QUERYEXT_GET,
    'FillTime': QUERY_GET,
    'PreDodgeTime': ATTR_GET,
    'DodgeTime': ATTR_GET,
    'PostDodgeTime': ATTR_GET,
    'Width': QUERY_GET,
    'EnergyCost': EXTSET_GET,
    'SkillFortuneFactor': QUERY_GET,
    'LuckFortuneFactor': QUERY_GET,
    'FortuneRadio': QUERY_GET,
    'DeviceEnergy': FUNC_GET,
    'RDeviceEnergy': QUERY_GET,
    'MaxDeviceEnergy': QUERY_GET,
    'HitRange': QUERY_GET,
    'RelifeTime': QUERY_GET,
    'PerformCDRate': QUERY_GET,
    'DebuffFactor': QUERY_GET,
    'Phase': ATTR_GET }

def GetWarriorAttr(sAttr, oWarrior):
    if sAttr not in g_AttrGetFunc:
        return 0
    iType = g_AttrGetFunc[sAttr]
    if iType == QUERY_GET:
        return oWarrior.QueryAttr(sAttr)
    if iType == QUERYEXT_GET:
        return oWarrior.QueryAttrExt(sAttr)
    if iType == QUERYBASE_GET:
        return oWarrior.QueryAttrBase(sAttr)
    if iType == ATTR_GET:
        return getattr(oWarrior, 'm_%s' % sAttr)
    if iType == EXTSET_GET:
        return oWarrior.Query(sAttr)
    return getattr(oWarrior, sAttr)()

g_ItemAttrGetFunc = {
    'ID': ATTR_GET,
    'Grade': ATTR_GET,
    'MaxBullet': QUERY_GET,
    'EffectDis': QUERY_GET,
    'AttDis': QUERY_GET,
    'Att': QUERY_GET,
    'FillTime': QUERY_GET,
    'AttSpeed': QUERY_GET,
    'CrazyEff': QUERY_GET,
    'Accuracy': QUERY_GET,
    'ElementType': ATTR_GET,
    'BallisticType': ATTR_GET,
    'ItemSID': ITEMBASE_GET,
    'ItemType': ITEMBASE_GET,
    'ItemGrade': ITEMBASE_GET,
    'ItemKey': ITEMBASE_GET,
    'ItemAmount': ITEMBASE_GET,
    'ItemBaseGrade': ITEMBASE_GET,
    'ColdTime': QUERY_GET }

def GetItemAttr(sAttr, oItem):
    iType = QUERY_GET
    if sAttr in g_ItemAttrGetFunc:
        iType = g_ItemAttrGetFunc[sAttr]
    if iType == QUERY_GET:
        return oItem.QueryAttr(sAttr)
    if iType == ATTR_GET:
        return getattr(oItem, 'm_%s' % sAttr)
    if iType == ITEMBASE_GET:
        return getattr(oItem, 'm_%s' % sAttr[4:])
    return getattr(oItem, sAttr)()

g_QualityString2Number = {
    'QUALITY_TYPE_LOW': QUALITY_TYPE_LOW,
    'QUALITY_TYPE_NORMAL': QUALITY_TYPE_NORMAL,
    'QUALITY_TYPE_HIGH': QUALITY_TYPE_HIGH,
    'QUALITY_TYPE_CURSE': QUALITY_TYPE_CURSE }

def GetQualityNumber(sQuality):
    if sQuality in g_QualityString2Number:
        return g_QualityString2Number[sQuality]
    return 0


def GetObjLevelNode(obj):
    if not obj or not (obj.m_LineIdx):
        return None
    iLevel = obj.m_LineIdx[0]
    oGame = obj.m_Game
    if not oGame:
        return None
    oWarMgr = oGame.m_WarMgr
    oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
    if not oLevelCtrl:
        return None
    return oLevelCtrl.GetLevelNode(iLevel)


def GetObjLayerAndLevel(obj, iGetBaseLayer = 0):
    oLevelNode = GetObjLevelNode(obj)
    if not oLevelNode:
        return (0, 0)
    iLayerNum = oLevelNode.m_LayerNum
    iLevelNum = oLevelNode.m_LevelNum
    if iGetBaseLayer:
        oLevelCtrl = oLevelNode.m_CtrlMgr
        if oLevelCtrl:
            iLayerNum = oLevelCtrl.m_BaseLayerNum
    return (iLayerNum, iLevelNum)

