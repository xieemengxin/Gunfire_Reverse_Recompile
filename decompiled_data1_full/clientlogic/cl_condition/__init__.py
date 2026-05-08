# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_condition/__init__.pyc
# RelativePath: clientlogic/cl_condition/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_condition.con_state import *
from cl_condition.con_item import *
from cl_condition.con_passive import *
from cl_condition.con_aiperform import *
from cl_condition.con_task import *
from cl_condition.con_suit import *
from cl_condition.con_wand import *
from cl_commondefines import PF_TYPE_CAREERPF, DEFEND_TREND_SHIELD, WAND_COMP_TYPE_ACTION, WARRIOR_DEVICE, WARRIOR_HERO, DEVICE_UNIT_TYPE, ALL_TEMPREMOVERELIC_TYPE, WUKONG_HERO, GARDENER_HERO
from cl_cscommondef import EQUIP_MASK_WEAPON
from cl_only import SendAlert, ChooseKey, Time2Frame
from cl_cscommondef import VIRTUAL_ITEM_WANDCOMP, VIRTUAL_ITEM_WAND, WAND_COMP_TYPE_CONDITION, WAND_COMP_TYPE_ACTION
from cl_pxlayer import PXMASK_GROUNDBLK
import cl_formula
import cl_item.defines as itemdef

def CalFormula(oTarget, oLifeCycle, iVal):
    return cl_formula.GetResultByData(oTarget, iVal, {
        'LifeCycle': oLifeCycle })


def RandomTrigger(oTarget, oLifeCycle, iLimit, iRatio):
    dData = {
        'LifeCycle': oLifeCycle }
    iLimit = cl_formula.GetResultByData(oTarget, iLimit, dData)
    iRatio = cl_formula.GetResultByData(oTarget, iRatio, dData)
    if oTarget.m_Game.Random(iLimit) < iRatio:
        return 1
    return 0


def RandomChooseKey(oTarget, oLifeCycle, dChooseInfo):
    if dChooseInfo:
        return ChooseKey(oTarget.m_Game, dChooseInfo)
    return 0


def HasState(oTarget, oLifeCycle, iState):
    if oTarget.m_State.GetItemBySID(iState):
        return 1
    return 0


def CheckTargetFightType(oTarget, oLifeCycle, iFightType):
    if 255 & iFightType:
        if oTarget.m_FightType == iFightType:
            return 1
        return 0
    if oTarget.m_FightType & iFightType == iFightType:
        return 1
    return 0


def CheckTargetUnitFightType(oTarget, oLifeCycle, iUnit, iFightType):
    if iUnit == DEVICE_UNIT_TYPE:
        oUnit = oTarget.GetDevice()
    else:
        return 0
    if 255 & iFightType:
        if oUnit.m_FightType == iFightType:
            return 1
        return 0
    if oUnit.m_FightType & iFightType == iFightType:
        return 1
    return 0


def CheckDualWeaponType(oTarget, oLifeCycle):
    lstWeapon = oTarget.m_WieldCon.GetHoldWeapon()
    if len(lstWeapon) != 2:
        return 0
    (oMainWeapon, oDeputyWeapon) = lstWeapon
    if oMainWeapon[0].Type() == oDeputyWeapon[0].Type():
        return 1
    return 0


def CheckDualWeapon(oTarget, oLifeCycle):
    lstWeapon = oTarget.m_WieldCon.GetHoldWeapon()
    if len(lstWeapon) != 2:
        return 0
    (oMainWeapon, oDeputyWeapon) = lstWeapon
    if oMainWeapon[0].m_SID == oDeputyWeapon[0].m_SID:
        return 1
    return 0


def CheckTargetDefendTrend(oTarget, oLifeCycle, iDefTrend):
    if hasattr(oTarget, 'm_DefendTrend') and iDefTrend == DEFEND_TREND_SHIELD:
        return 1
    if oTarget.m_DefendTrend == iDefTrend:
        return 1
    return 0


def CheckOwnerDefendTrend(oTarget, oLifeCycle, iDefTrend):
    oOwner = oTarget.GetOwner()
    if not oOwner:
        return 0
    return CheckTargetDefendTrend(oOwner, oLifeCycle, iDefTrend)


def CheckHasRelic(oTarget, oLifeCycle, iRelic):
    if oTarget.m_RelicCon.IsEnabled(iRelic):
        return 1
    return 0


def CheckHasExtendRelic(oTarget, oLifeCycle, iRelic):
    if oTarget.m_RelicCon.GetExtendRelic(iRelic):
        return 1
    return 0


def CheckHasTempRemoveRelic(oTarget, oLifeCycle, iRelic):
    for iType in ALL_TEMPREMOVERELIC_TYPE:
        if oTarget.m_RelicCon.GetTempRemoveRelic(iType, iRelic):
            return 1
    
    return 0


def CheckHasOrderRelicNum(oTarget, oLifeCycle, dRelic, iEnable):
    iNum = 0
    if iEnable:
        for iRelic in dRelic:
            if oTarget.m_RelicCon.IsEnabled(iRelic):
                iNum += 1
        
    else:
        for iRelic in dRelic:
            if oTarget.m_RelicCon.GetPerform(iRelic):
                iNum += 1
        
    return iNum


def CheckHasLockEnemy(oTarget, oLifeCycle):
    iLockEnemy = oTarget.Query('LockEnemy', 0)
    if iLockEnemy:
        return 1
    return 0


def CheckAddImmobilize(oTarget, oLifeCycle):
    return oTarget.IsImmobilize()


def GetWeaponBulletCnt(oTarget, oLifeCycle):
    oPerform = oLifeCycle.GetObject()
    if not oPerform:
        return 0
    oWeapon = oPerform.GetMyItem()
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return 0
    return oBulletCom.Bullet()


def CheckWarPlayMode(oTarget, oLifeCycle, iCheckMode):
    if oTarget.m_Game.m_WarMgr.m_PlayMode == iCheckMode:
        return 1
    return 0


def GetSceneData(oTarget, oLifeCycle, sAttr):
    if not oTarget.m_Scene:
        SendAlert('err', f'''{oLifeCycle.Key()}事件场景不存在''')
        return 0
    oGame = oTarget.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
    if not oScene:
        return 0
    if sAttr in oScene.m_CustomData:
        return oScene.m_CustomData[sAttr]
    return 0


def CheckWeaponTypeByHoldType(oTarget, oLifeCycle, iHoldType, iType):
    oItem = oTarget.m_WieldCon.GetCurWeapon(iHoldType)
    if not oItem:
        return 0
    if 15 & iType:
        if oItem.m_Type == iType:
            return 1
        return 0
    if oItem.m_Type & iType == iType:
        return 1
    return 0


def CheckTalentLevel(oTarget, oLifeCycle, iTalent):
    oTalent = oTarget.m_TalentCon.GetPerform(iTalent)
    if oTalent:
        return oTalent.m_Level
    return 0


def CheckWarPlayType(oTarget, oLifeCycle, iType):
    if oTarget.m_Game.m_WarMgr.GetPlayType() == iType:
        return 1
    return 0


def CheckHasSavedData(oTarget, oLifeCycle, sFlag):
    if oTarget.QuerySavedData('save.' + sFlag, None) is None:
        return 0
    return 1


def GetRelicGrade(oTarget, oLifeCycle, iRelic):
    oPerform = oTarget.m_RelicCon.GetPerform(iRelic)
    if not oPerform:
        return 0
    return oPerform.GetLifeCycleLevel()


def GetCustomData(oTarget, oLifeCycle, sKey):
    sCommonKey = oLifeCycle.m_Key
    sPreFix = sCommonKey.split('-', 1)[0]
    sFinalKey = '%s-%s' % (sPreFix, sKey)
    return oTarget.Query(sFinalKey)


def CheckPerformInCD(oTarget, oLifeCycle, iPerform):
    oPerformCon = oTarget.m_Perform
    if oPerformCon.GetTotalColdTime(iPerform) > 0:
        return 1
    return 0


def CheckHasPerform(oTarget, oLifeCycle, iPerform):
    if oTarget.m_Perform.GetPerform(iPerform) is None:
        return 0
    return 1


def CheckEnabledPerform(oTarget, oLifeCycle, iPerform):
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.m_Enable


def CheckHero(oTarget, oLifeCycle, iHero):
    if oTarget.m_SID == iHero:
        return 1
    return 0


def CheckOwnerHero(oTarget, oLifeCycle, iHero):
    iOwner = oTarget.m_Owner
    if not iOwner:
        return 0
    oOwner = oTarget.m_Game.GetObject(iOwner)
    if not oOwner:
        return 0
    if oOwner.m_SID == iHero:
        return 1
    return 0


def CheckCurLevel(oTarget, oLifeCycle, iLevel):
    iScene = oTarget.m_Scene
    oScene = oTarget.m_Game.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return 0
    if oScene.m_Level == iLevel:
        return 1
    return 0


def CheckInPointLevel(oTarget, oLifeCycle, dLevel):
    iScene = oTarget.m_Scene
    oScene = oTarget.m_Game.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return 0
    iCurLevel = oScene.m_Level
    if iCurLevel not in dLevel:
        return 0
    return 1


def CheckInPointLayerNewLevel(oTarget, oLifeCycle, iLayer):
    iScene = oTarget.m_Scene
    oGame = oTarget.m_Game
    if not oGame:
        return 0
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    oWarMgr = oGame.m_WarMgr
    if not oWarMgr:
        return 0
    if oScene:
        iCurLevel = oScene.m_Level
        iCurBaseLayer = int(str(iCurLevel)[1])
    else:
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        if not oLevelCtrl:
            return 0
        iCurBaseLayer = oLevelCtrl.m_BaseLayerNum
        tLine = oTarget.m_LineIdx
        if not tLine:
            return 0
        iCurLevel = tLine[0]
    if iLayer and iCurBaseLayer != iLayer:
        return 0
    if iCurLevel not in oWarMgr.m_NewVerLayer:
        return 0
    return 1


def GetStateStatistics(oTarget, oLifeCycle, iStateSID, sAttr):
    oStateCon = oTarget.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return 0
    if sAttr in oState.m_Data:
        return oState.m_Data[sAttr]
    return 0


def GetStateCount(oTarget, oLifeCycle, iState):
    oState = oTarget.m_State.GetItemBySID(iState)
    if not oState:
        return 0
    return oState.GetCount()


def CheckGamblerAvailableQuailty(oTarget, oLifeCycle, iAssignQuality):
    iNum = oTarget.m_GamblerCon.GetAvailableQualityNum(iAssignQuality)
    if iNum > 0:
        return 1
    return 0


def GetGamblerQualityNum(oTarget, oLifeCycle, iAssignQuality):
    return oTarget.m_GamblerCon.HasQualityNum(iAssignQuality)


def CheckSingleRescue(oTarget, oLifeCycle):
    return oTarget.Query('SingleRescue')


def CheckPerformRecord(oTarget, oLifeCycle, iPerform):
    oAgent = oTarget.m_Agent
    if not oAgent:
        return 0
    dRecord = oAgent.GetData('PFRecord')
    if not dRecord:
        return 0
    iTimes = dRecord[iPerform] if iPerform in dRecord else 0
    return iTimes


def CheckOpenCycle(oTarget, oLifeCycle):
    return oTarget.m_Game.m_WarMgr.IsCycleWar()


def CheckWarCycle(oTarget, oLifeCycle):
    return oTarget.m_Game.m_WarMgr.GetWarCycle()


def CheckOpenElementMode(oTarget, oLifeCycle, dCheckElement):
    oGame = oTarget.m_Game
    oWarMgr = oGame.m_WarMgr
    for iType in dCheckElement:
        if iType not in oWarMgr.m_ModeType:
            return False
    
    return True


def GetInscriptioNumFromWeaponStoreNewWeapon(oTarget, oLifeCycle, iInscriptionType):
    oWarMgr = oTarget.m_Game.m_WarMgr
    oWeaponStoreCon = oTarget.m_WeaponStoreCon
    oWeaponStoreElement = oWarMgr.GetComponent('WeaponStoreElement')
    iResult = 0
    if not oWeaponStoreElement or not oWeaponStoreCon:
        return iResult
    lstNewWeapon = oWeaponStoreElement.GetNewWeaponFromWeaponStore(oTarget, True)
    for oWeapon in lstNewWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        iInscriptionNum = oInscriptionCom.GetInscriptionNumByType(iInscriptionType)
        iResult = max(iResult, iInscriptionNum)
    
    return iResult


def CheckOpenElementModeNumber(oTarget, oLifeCycle):
    oGame = oTarget.m_Game
    oWarMgr = oGame.m_WarMgr
    return len(oWarMgr.m_ModeType)


def GetFinalLayerInEndless(oTarget, oLifeCycle):
    oGame = oTarget.m_Game
    oWarMgr = oGame.m_WarMgr
    oEndlessElement = oWarMgr.GetEndlessElement()
    if not oEndlessElement or not (oEndlessElement.m_ChooseLayerMap):
        return 0
    return len(oEndlessElement.m_ChooseLayerMap) - 1


def CheckIsEndless(oTarget, oLifeCycle):
    return oTarget.m_Game.m_WarMgr.IsEndless()


def CheckOpenElement(oTarget, oLifeCycle, dElement):
    oWarMgr = oTarget.m_Game.m_WarMgr
    for sElement in dElement:
        if oWarMgr.GetComponent(sElement):
            return 1
    
    return 0


def GetPassNumInEndless(oTarget, oLifeCycle):
    oGame = oTarget.m_Game
    oWarMgr = oGame.m_WarMgr
    oEndlessElement = oWarMgr.GetEndlessElement()
    if not oEndlessElement:
        return 0
    return oEndlessElement.GetPassLayerNum()


def CheckForceAttr(oTarget, oLifeCycle, sAttr, bCheckKey = False):
    sKey = oLifeCycle.Key()
    if bCheckKey:
        return oTarget.HasForceAtt(sAttr, sKey)
    return oTarget.HasForceAtt(sAttr)


def GetUsingSkillNumBySID(oTarget, oLifeCycle, iSkillSID, bCheckFromSelf):
    oSkillMgr = oTarget.m_Game.m_SkillMgr
    lstSkill = oSkillMgr.GetSkillBySID(iSkillSID)
    iTargetScene = oTarget.m_Scene
    iTargetID = oTarget.m_ID
    iResult = 0
    for oSkill in lstSkill:
        if oSkill.m_Base['Scene'] != iTargetScene:
            continue
        if bCheckFromSelf and oSkill.m_Base['AID'] != iTargetID:
            continue
        iResult += 1
    
    return iResult


def CheckMoveMode(oTarget, oLifeCycle, iMode):
    return oTarget.m_MoveMode == iMode


def GetDeviceEnergyRatio(oTarget, oLifeCycle):
    iMaxDeviceEnergy = oTarget.QueryAttr('MaxDeviceEnergy')
    if iMaxDeviceEnergy <= 0:
        SendAlert('err', f'''{oLifeCycle.Key()}装置能量上限异常''')
        return 0
    return int((oTarget.DeviceEnergy() / iMaxDeviceEnergy) * 100)


def CheckDeciveStatus(oTarget, oLifeCycle, iDeployed, iAcitve):
    oDeviceOwner = None
    if oTarget.m_FightType & WARRIOR_HERO:
        oDeviceOwner = oTarget
    elif oTarget.m_FightType & WARRIOR_DEVICE:
        oDeviceOwner = oTarget.GetOwner()
    if not oDeviceOwner:
        return False
    return oDeviceOwner.CheckDeciveStatus(iDeployed, iAcitve)


def CheckDualSate(oTarget, oLifeCycle):
    return oTarget.Query('DualState')


def GetWeaponSpecialAttr(oTarget, oLifeCycle, sKey):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    iValue = oWeapon.QueryAttrSpecial(sKey)
    if not iValue:
        return 0
    return iValue


def CommonGetWeaponPerformArgs(oTarget, oLifeCycle, iPerform, sArg):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return 0
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.GetArgValue(sArg)


def GetCareerPFBulletNum(oListener, oLifeCycle, iPerform):
    oPerform = oListener.GetPerform(iPerform)
    if oPerform and oPerform.m_PFType == PF_TYPE_CAREERPF:
        return oPerform.CurPFBullet()
    return 0


def GetWeaponPFBulletNum(oTarget, oLifeCycle, iPerform):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return 0
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.CurPFBullet()


def GetPerformAttrFromOwn(oListener, oLifeCycle, iPerform, sKey, iObjectType):
    oTarger = oListener.GetOwnObject(iObjectType)
    if not oTarger:
        return 0
    oPerform = oTarger.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sKey)


def GetWeaponInscriptionNumByTypeAndLevel(oListener, oLifeCycle, iInscriptionType, iSealedInscriptionLv):
    lstWeapon = oListener.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    if not lstWeapon:
        return 0
    iCount = 0
    for oWeapon in lstWeapon:
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if not oInscriptionCom:
            continue
        iCount += oInscriptionCom.GetInscriptionNumByType(iInscriptionType)
        if iSealedInscriptionLv:
            iCount += oInscriptionCom.GetSealedInscriptionNumByTypeAndLv(iInscriptionType, iSealedInscriptionLv)
    
    return iCount


def GetDevicePerformByType(oListener, oLifeCycle, dType, iOnlyEnable):
    oDevicePerformCon = oListener.m_DevicePerformCon
    iResult = 0
    for iType in dType:
        iResult += len(oDevicePerformCon.GetDevicePerformByType(iType, iOnlyEnable))
    
    return iResult


def CheckHasCurPet(oListener, oLifeCycle):
    if not oListener.m_FightType & WARRIOR_HERO:
        return 0
    if oListener.m_PetCon.m_CurPet:
        return 1
    return 0


def CheckCheckEggPriorType(oListener, oLifeCycle, iEggPriorType):
    if not oListener.m_FightType & WARRIOR_HERO:
        return 0
    oPetcon = oListener.m_PetCon
    if iEggPriorType == oPetcon.m_EggPriorType:
        return 1
    return 0


def CheckFarAwayPetAbility(oListener, oLifeCycle, iDis, iAbility):
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    vPos = oListener.GetPos()
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero)
        if not oHero:
            continue
        oPet = oHero.m_PetCon.GetCurPet()
        if not oPet:
            continue
        if not oPet.m_AbilityCon.HasAbility(iAbility):
            continue
        if not cl_math.CheckDistance(oPet.GetPos(), vPos, iDis):
            return 1
    
    return 0


def GetTargetStateInfo(oListener, oLifeCycle, iStateSID, sKey):
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return 0
    dStateInfo = oState.m_StateInfo
    dArg = dStateInfo['arg'] if 'arg' in dStateInfo else { }
    if sKey in dArg:
        return dArg[sKey]
    return 0


def CheckSourceWeaponInPointWeapons(oListener, oLifeCycle, dWeapon):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon or oWeapon.m_SID not in dWeapon:
        return 0
    return 1


def CheckSceneFightMonster(oListener, oLifeCycle):
    oScene = oListener.m_Game.m_SceneMgr.GetScene(oListener.m_Scene)
    if oScene and oScene.m_SceneData.GetFightMonster():
        return 1
    return 0


def CheckHasAIMember(oListener, oLifeCycle):
    return oListener.m_Game.m_WarMgr.CheckHasAIMember()


def GetSeasonSuitLevel(oListener, oLifeCycle, iSID):
    oSeasonSuit = oListener.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSeasonSuit:
        return 0
    if iSID in oSeasonSuit.m_Enable[oListener.m_ID]:
        return oSeasonSuit.m_Enable[oListener.m_ID][iSID]
    return 0


def CheckSeasonSuitElement(oListener, oLifeCycle, iElement):
    iNowElement = oListener.QuerySavedData('SeasonSuit_NowElement', 0)
    if iElement == iNowElement:
        return 1
    return 0


def CheckHasAllTalent(oListener, oLifeCycle):
    return oListener.m_TalentCon.CheckHasAllTalent()


def CheckTalenIsMaxlLevel(oListener, oLifeCycle, iTalent):
    iTalent = cl_formula.GetResultByData(oListener, iTalent, {
        'LifeCycle': oLifeCycle })
    oTalent = oListener.m_TalentCon.GetPerform(iTalent)
    if oTalent and oTalent.m_Level == oTalent.m_MaxLevel:
        return 1
    return 0


def CheckTalentCanUpgrade(oListener, oLifeCycle, iTalent):
    iTalent = cl_formula.GetResultByData(oListener, iTalent, {
        'LifeCycle': oLifeCycle })
    oTalentCon = oListener.m_TalentCon
    return oTalentCon.CheckTalentCanUpgrade(iTalent)


def CheckIsAIMember(oListener, oLifeCycle):
    oTeammateAIElement = oListener.m_Game.m_WarMgr.GetComponent('TeammateAI')
    if not oTeammateAIElement:
        return 0
    return oListener.m_PlayerID in oTeammateAIElement.m_AIMember


def CheckIsAIHero(oListener, oLifeCycle):
    return oListener.m_Game.m_WarMgr.IsAIHero(oListener.m_ID)


def CommonGetTimeLimitInfo(oTarget, oLifeCycle, sArg, iTime):
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return 0
    dTimeLimitInfo = oLifeCycleOwner.GetArgValue(sArg, { })
    if not dTimeLimitInfo:
        return 0
    iLimitFrame = oTarget.m_Game.GetFrameNum() - Time2Frame(iTime)
    iAllRecordVal = 0
    for iRecordFrame, iRecordVal in dict(dTimeLimitInfo).items():
        if iRecordFrame >= iLimitFrame:
            iAllRecordVal += iRecordVal
            continue
        dTimeLimitInfo.pop(iRecordFrame)
    
    return iAllRecordVal


def CommonCheckRecycleReward(oListener, oLifeCycle, iType):
    return iType in oListener.Query('RecycleDropPrice', { })


def CommonCheckGameReleaseFlag(oListener, oLifeCycle):
    return oListener.m_Game.m_ReleaseFlag


def CheckWeaponClassifyTagByHoldType(oTarget, oLifeCycle, iHoldType, iClassifyTag):
    oWeapon = oTarget.m_WieldCon.GetCurWeapon(iHoldType)
    if not oWeapon:
        return 0
    if iClassifyTag in oWeapon.m_ClassifyTag:
        return 1
    return 0


def CheckWeaponInBag(oTarget, oLifeCycle, iWeaponSID):
    lstWeapon = oTarget.m_WieldCon.GetAllItemByMask(EQUIP_MASK_WEAPON)
    if not lstWeapon:
        return 0
    for oWeapon in lstWeapon:
        if oWeapon.m_SID == iWeaponSID:
            return 1
    
    return 0


def CheckIsReducingSpeed(oTarget, oLifeCycle):
    if oTarget.IsReducingSpeed():
        return 1
    return 0


def CheckIsReducingActionSpeed(oTarget, oLifeCycle):
    if oTarget.IsReducingActionSpeed():
        return 1
    return 0


def CheckSourceWeaponClassifyTag(oTarget, oLifeCycle, iClassifyTag):
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return 0
    if iClassifyTag in oWeapon.m_ClassifyTag:
        return 1
    return 0


def CommonGetSourceWandCount(oTarget, oLifeCycle):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oTarget.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
    if not oWand:
        return 0
    return oWand.GetWandCount()


def CommonCheckWandIsInCD(oTarget, oLifeCycle):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return 0
    return oWand.CheckSpellCD()


def CommonCheckCurWandIsInCD(oTarget, oLifeCycle):
    oWandCon = oTarget.m_WandCon
    if not oWandCon:
        return 0
    oWand = oWandCon.GetCurWand()
    if not oWand:
        return 0
    return oWand.CheckSpellCD()


def CommonCheckCurWandIsConditionFinish(oTarget, oLifeCycle):
    oWandCon = oTarget.m_WandCon
    if not oWandCon:
        return 0
    oWand = oWandCon.GetCurWand()
    if not oWand:
        return 0
    return oWand.GetConditionCompFinish()


def CommonCheckItemTmpData(oTarget, oLifeCycle, sKey):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oItem = oLifeCycleOwner.GetMyItem()
    if not oItem:
        return 0
    return oItem.QueryTmp(sKey, 0)


def CommonCheckCanTriggerNextPosComp(oTarget, oLifeCycle):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return False
    iCurPos = oLifeCycleOwner.GetCurPos()
    (_, iMaxComp) = oWand.GetWandGroveNum()
    if iCurPos >= iMaxComp - 1:
        return False
    dWandComp = oWand.GetWandCompByType(WAND_COMP_TYPE_ACTION)
    if not dWandComp:
        return False
    iNextPos = iCurPos + 1
    if iNextPos not in dWandComp:
        return False
    for iPos, oComp in dWandComp.items():
        if iPos > iCurPos and oComp.m_SID != oLifeCycleOwner.m_SID:
            return True
    
    return False


def CommonCheckHasQualityWandItem(oTarget, oLifeCycle, iQuality, iItemType):
    if iItemType == VIRTUAL_ITEM_WAND:
        dAllWand = oTarget.m_WandCon.GetAllWand()
        for oWand in dAllWand.values():
            if iQuality == oWand.GetWandQuality():
                return 1
        
    elif iItemType == VIRTUAL_ITEM_WANDCOMP:
        dAllBagComp = oTarget.m_WandCon.GetAllBagComp()
        for _, dCompInfo in dAllBagComp.items():
            if iQuality in dCompInfo:
                return 1
        
    return 0


def CommonGetCompNumByType(oTarget, oLifeCycle, iCompType):
    if iCompType not in (WAND_COMP_TYPE_CONDITION, WAND_COMP_TYPE_ACTION):
        return 0
    oWandCon = oTarget.m_WandCon
    if not oWandCon:
        return 0
    oWand = oWandCon.GetCurWand()
    if not oWand:
        return 0
    return len(oWand.m_Comp[iCompType])


def CommonCheckCurWandAllPointCompPointQuality(oTarget, oLifeCycle, iQuality, iCompType):
    oWand = oTarget.m_WandCon.GetCurWand()
    if not oWand:
        return 0
    (iMaxConditionNum, iMaxActionNum) = oWand.GetWandGroveNum()
    if iCompType == WAND_COMP_TYPE_ACTION:
        iMaxNum = iMaxActionNum
    elif iCompType == WAND_COMP_TYPE_CONDITION:
        iMaxNum = iMaxConditionNum
    else:
        SendAlert('err', f'''法杖模块类型配置有误：{iCompType}''')
        return 0
    dComp = oWand.GetWandCompByType(iCompType)
    if len(dComp) < iMaxNum:
        return 0
    for oComp in dComp.values():
        if oComp.GetLifeCycleLevel() != iQuality:
            return 0
    
    return 1


def CommonCheckPerformInGroupOfPF(oTarget, oLifeCycle, iPerfrom):
    if not oTarget.m_Agent:
        return 0
    oPFAI = oTarget.m_Agent.m_PFAI
    if not oPFAI:
        return 0
    if iPerfrom not in oPFAI.m_GroupOfPF:
        return 0
    return 1


def CommonGetGroundDistance(oTarget, oLifeCycle):
    vPos = oTarget.GetPos()
    return oTarget.m_Game.Scene_GroundDistance(oTarget.m_Scene, (vPos[0], vPos[1] + 1.8, vPos[2]), oTarget.m_GroundMaxDis, PXMASK_GROUNDBLK, oTarget.m_ID) - 1.8


def CommonGetCompNumFromSrcWand(oTarget, oLifeCycle, dCompInfo):
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oTarget.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
    if not oWand:
        return 0
    iNum = 0
    for dComp in oWand.m_CompTemp.values():
        for iCompSID, _ in dComp.values():
            if iCompSID in dCompInfo:
                iNum += 1
        
    
    return iNum


def CommonCheckInPointWand(oTarget, oLifeCycle, dPointWand):
    oWandCon = oTarget.m_WandCon
    if not oWandCon:
        return 0
    oWand = oWandCon.GetCurWand()
    if not oWand:
        return 0
    if oWand.m_SID in dPointWand:
        return 1
    return 0


def CommonCheckStateArgsDict(oTarget, oLifeCycle, iStateSID, sArgs, iFromSelf, iFromSameItem):
    iAttack = oTarget.m_ID if iFromSelf else 0
    if iFromSameItem:
        dEventInfo = oLifeCycle.AttrCache()
        iItem = dEventInfo['ItemID']
    else:
        iItem = 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
    if not oState:
        return None
    if oState.GetArgValue(sArgs, { }):
        return 1
    return 0


def CommonGetWUKONGStrengthLayer(oTarget, oLifeCycle, iCalOverflow):
    if oTarget.m_SID != WUKONG_HERO:
        return 0
    iStrength = oTarget.Query('StrengthLayer')
    if iCalOverflow:
        iStrength += oTarget.Query('OverFlowStrengthLayer')
    return iStrength


def CommonCheckGardenerFieldSeedInfo(oTarget, oLifeCycle):
    if oTarget.m_SID != GARDENER_HERO:
        return 0
    if oTarget.m_GardenerCon.GetFieldSeedInfo():
        return 1
    return 0


def CommonGetDiceEnergy(oTarget, oLifeCycle):
    if not oTarget.m_FightType & WARRIOR_HERO:
        return 0
    if not oTarget.m_DiceCon:
        return 0
    return oTarget.m_DiceCon.GetDiceEnergy()


def CommonCheckInPointWandByHoldType(oTarget, oLifeCycle, iHoldType, iWeaponSID):
    oWeapon = oTarget.m_WieldCon.GetCurWeapon(iHoldType)
    if not oWeapon:
        return 0
    if oWeapon.m_SID == iWeaponSID:
        return 1
    return 0


def CommonCheckTargetDeadReason(oTarget, oLifeCycle, sKey):
    if not oTarget.m_DeadReason:
        return 0
    return sKey in oTarget.m_DeadReason.GetStrReason()

