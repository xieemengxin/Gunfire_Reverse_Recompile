# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evact/__init__.pyc
# RelativePath: clientlogic/cl_evact/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import DeepCopy, ChooseMulKeys, PY_FLAG_DIED, PY_FLAG_DEAD, ShufferList
from cl_evact.ev_item import *
from cl_evact.ev_state import *
from cl_evact.ev_passive import *
from cl_evact.ev_scene import *
from cl_evact.ev_achieve import *
from cl_evact.ev_unlock import *
from cl_evact.ev_task import *
from cl_evact.ev_season import *
from cl_evact.ev_wand import *
from cl_commondefines import TYPE_RELIFE_PASSIVE, RELIC_TYPE_CURSE, JUMPFIGURE_RELIC, JUMPFIGURE_KILLMONSTER, JUMPFIGURE_UPGRADEWEAPON, JUMPFIGURE_BUYGOODS, SKILLCACHE_PARENTACTNUM, GARDENER_HERO, PF_TYPE_CAREERPF
from cl_commondefines import WARRIOR_NORPART, WARRIOR_ELIPART, DAM_TYPE_WEAPON, DAM_TYPE_SHIELD, DAM_MASK_SRC, WARRIOR_SUMMON, WARRIOR_BEACON, DAM_TYPE_TRUE, OBJ_SELF, MG_EQUIP, STATE_ADD_SYNC, MG_SOURCE_KILLMONSTER, WARRIOR_BOSS, PF_TYPE_CHARGE, WARRIOR_MOVEEFFECT, WARRIOR_NORMAL, WARRIOR_ELITE, WARRIOR_PET_MINI, WARRIOR_PET_MINICLONE
from cl_commondefines import PF_TYPE_CONSHOOT, PF_TYPE_TRIGGERCLIENT, PF_TYPE_SHOOT, NWARRIOR_DROP_CASH, NWARRIOR_DROP_GSCASH, NWARRIOR_DROP_TREASURE_DEAD, VIRTUAL_ITEM_DROP, MG_BULLET, VIRTUAL_ITEM_RELIC, MG_RELIC, RELIC_SUBMSG_GENERATE_GOOD
from cl_commondefines import NWARRIOR_DROP_RELIFE, DISABLE_TYPE_SCENEEVENT, DISABLE_TYPE_KEY, DISABLE_TYPE_CALL, FIGHT3_KEY_IGNELBEEXECUTED, DEFEND_TREND_SHIELD, DEFEND_TREND_ARMOR, INSCRIPTION_TYPE_GEMINI, PLANT_PHASE_NORMAL, PF_TYPE_ATTACK
from cl_commondefines import BASEATTR_CLIENT, NWARRIOR_DROP_EQUIP, LEVEL_TYPE_BOSS, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, SIDE_TYPE_MONSTER, MONSTERAI_TYPE_HATESEARCH, IMMUNITY_SHOWCAST, MODEL_TYPE_SPHERE, MODEL_TYPE_BOX, PF_TYPE_RELIC, MODEL_TYPE_CAPSULE, MODEL_TYPE_SCALECTRLAGENT
from cl_commondefines import DAM_TYPE_SCENE, GAMBLER_HERO, WARRIOR_SERVANT, SCENEOBJ_TYPE, SKILLCACHE_LSTINT, SKILLCACHE_LSTPOS, SKILLCACHE_LSTINTSPECIAL, DAM_MASK_ELEMENT, TYPE_RELIFE_ALL, DISABLE_TYPE_TARGETSET, EXECUTOR_HERO, DEVICE_UNIT_TYPE, DEVICE_USEPERFORM_POSTYPE_OWNER, DEVICE_USEPERFORM_POSTYPE_SERVANT, DEVICE_USEPERFORM_POSTYPE_ENDPOS, NWARRIOR_NPC_S7SHOP
from cl_commondefines import OBJECT_CURPET, OBJECT_SERVANT, SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY, INKMASTER_HERO, GAMBLER_CHOOSE_EQUITY, DIE_PRIORITY_KILL, PF_TYPE_PETABILITY, PF_TYPE_PETACTIVE, RELIC_LIFECYCLE_TEMPLEVEL, DAM_TYPE_NORMAL, SIDE_TYPE_HERO, NWARRIOR_NPC_GSCASHSHOP, NWARRIOR_NPC_SHOP, ATT_SHAPE_SECTOR, LION_HERO, LION_MONSTER_LOCK_STATE, LION_MONSTER_ENHANCELOCK_STATE, NWARRIOR_NPC_DICESHOP, NONA_HERO
from cl_commondefines import TYPE_THROWRATIONNUMCHANG_DEFAULT, TYPE_THROWRATIONNUMCHANG_ADD, TYPE_THROWRATIONNUMCHANG_SUB, BLANKRELIC, NWARRIOR_NPC_RELICLOTTERY, NWARRIOR_DROP_NODISTANCEBULLET, VIRTUAL_ITEM_RANDOM, VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_AUTOPERFORM, VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIC, DICE_QUALITY_ALL, LION_SMALL_NOR_THROW, LION_BIG_THROW, BIG_LION_STATE
from cl_commondefines import LION_MONSTER_FLY_STATE, LION_MONSTER_FALL_STATE, WARRIOR_PLANT, LION_SMALL_ENHANCE_THROW, WARRIOR_MECH, NWARRIOR_DROP_SUMMONSOUL
from cl_cscommondef import ITEM_SOURCE_DROP, SUIT_HANDLE_INTENSIFY, SUIT_HANDLE_BANRELIC, VIRTUAL_ITEM_EQUIP, ITEM_SOURCE_GOOD, QUALITY_FACTOR, VIRTUAL_ITEM_WAND, VIRTUAL_ITEM_WANDCOMP, DROP_REASON_NORMAL, NWARRIOR_DROP_RELIC
from cl_pxlayer import PXMASK_PLAYER, PXMASK_MONSTER, PXMASK_LIVEOBJ, PXMASK_BLOCK, PXMASK_RBULLET, PXLAYER_EBULLET, PXMASK_SERVANT
from cl_resmgr.aitempparam import GetAIConfParam
from cl_platformdata import GetInscriptionLib, GetMonsterConfig, GetCommonSpell, GetAllWand, GetAllWandComp, GetExcludeDiceQuality
from cl_object.reason import REASON_TYPE_PERFORM
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
from cl_object.logging import LevelLog, WarnpcLog, DiceLog, ErrLog
from cl_platformdata.custom.commonative.customaction import CommonAddToxicCount
from cl_abnormalconf import g_AllAbnormalStateSID
import cl_snetwar
import cl_formula
import cl_math
import cl_reward
import cl_msgcenter
import cl_behavior
import cl_war
import cl_perform
import cl_perform.mobject
import cl_item.defines as itemdef
import cl_item
import cl_abnormalconf
import cl_engphyobj
import cl_action
import cl_minigame
import cl_shop
import cl_platformdata
import cl_notify
import cl_newformula
import cl_shop.goodsdata
import cl_modeldefine
import cl_modeldata
import cl_seasonplay.season7 as clseason7

def EventGetTargetByType(oListener, oEventCB, iTargetType):
    iTarget = 0
    if iTargetType == OBJ_ATTACK:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        if 'AID' in dMsgInfo:
            iTarget = dMsgInfo['AID']
        elif 'Skill' in dMsgInfo:
            iTarget = dMsgInfo['Skill'].m_Base['AID']
        elif iTargetType == OBJ_VICTIM:
            dMsgInfo = oEventCB.GetCBMsgInfo()
            if 'CurVID' in dMsgInfo:
                iTarget = dMsgInfo['CurVID']
            elif 'VID' in dMsgInfo:
                iTarget = dMsgInfo['VID']
            elif 'Skill' in dMsgInfo:
                oSkill = dMsgInfo['Skill']
                iTarget = oSkill.m_Base['VID']
                if not iTarget and 'CurVID' in oSkill.m_Update:
                    iTarget = oSkill.m_Update['CurVID']
                elif iTargetType == OBJ_SELF:
                    iTarget = oListener.m_ID
    dTransInfo = None.GetCBTransInfo()
    dTransInfo['TargetList'] = [
        iTarget] if iTarget else []


def EventGetHeroTarget(oListener, oEventCB, iAlive, iSameScene, iIsExcSelf = 0, iIsExcAI = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    oGame = oListener.m_Game
    if iSameScene:
        lstHero = []
        oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
        if oScene:
            lstHero = oScene.GetHeros() if not iIsExcAI else oScene.GetHerosExceptAI()
        elif iIsExcAI:
            lstHero = oGame.m_WarMgr.GetAllHeroExceptAI()
        else:
            lstHero = oGame.m_WarMgr.GetAllHero()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if iAlive and oHero.IsDead():
                continue
            if iIsExcSelf and oHero.m_ID == oListener.m_ID:
                continue
            lstTar.append(iHero)
        
    dTransInfo['TargetList'] = lstTar


def EventGetRangeTargetByTargetType(oListener, oEventCB, iRange, iTargetType, iIsBlkStatic = 1):
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    if not oListener.m_Scene:
        return None
    dMask = {
        'Mask': PXMASK_LIVEOBJ }
    if not iIsBlkStatic:
        dMask['BlockMask'] = 0
    oGame = oListener.m_Game
    iRange = cl_formula.GetResultByData(oListener, iRange, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    lstArgs = [
        oListener.GetPos(),
        iRange]
    lstVLST = cl_math.GetAttackTargetList(oGame, oListener.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    for iTarget in lstVLST:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not cl_math.CheckTargetType(oGame, oTarget, oListener.m_ID, oListener.m_Side, iTargetType):
            continue
        dTransInfo['TargetList'].append(oTarget.m_ID)
    


def EventGetRangeTargetByFightType(oListener, oEventCB, iRange, iFightType, iIsExcSelf, iIsBlkStatic, iRandomCount = 0, iUsePos = 0, iPetrochemical = 1, dCloseGround = None, iExcSuperMonster = 0, iExculueKey = 0, iNotRandom = 0, iSort = 0, iExculueTarget = 0):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    if not oListener.m_Scene:
        return None
    iRange = cl_formula.GetResultByData(oListener, iRange, dEventInfo, dMsgInfo)
    bCheckTargetFight = iFightType & SCENEOBJ_TYPE != iFightType
    if iFightType & WARRIOR_HERO and iFightType & WARRIOR_SERVANT:
        iPxMask = PXMASK_PLAYER | PXMASK_SERVANT
    elif iFightType & WARRIOR_HERO:
        iPxMask = PXMASK_PLAYER
    elif iFightType & WARRIOR_MONSTER:
        iPxMask = PXMASK_MONSTER
    elif iFightType & WARRIOR_MOVEEFFECT == WARRIOR_MOVEEFFECT:
        iPxMask = PXMASK_RBULLET
    else:
        bCheckTargetFight = True
        iPxMask = PXMASK_LIVEOBJ
    dMask = {
        'Mask': iPxMask }
    if not iIsBlkStatic:
        dMask['BlockMask'] = 0
    oGame = oListener.m_Game
    vPos = oListener.GetPos()
    if dCloseGround and oListener.m_SID in dCloseGround:
        iMax = dCloseGround[oListener.m_SID]
        fGroundDis = oGame.Scene_GroundDistance(oListener.m_Scene, vPos, iMax, PXMASK_BLOCK, oListener.m_ID)
        vPos = (vPos[0], vPos[1] - fGroundDis, vPos[2])
    vPos = (vPos[0], vPos[1] + oListener.m_ModelHeight / 2, vPos[2])
    if iUsePos and 'EPFPos' in dTransInfo:
        vPos = dTransInfo['EPFPos']
    lstArgs = [
        vPos,
        iRange]
    lstVLST = cl_math.GetAttackTargetList(oGame, oListener.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    lstTarget = []
    for iTarget in lstVLST:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not not oTarget:
            if (bCheckTargetFight or iFightType & oTarget.m_FightType != iFightType or iIsExcSelf) and iTarget == oListener.m_ID:
                continue
        if iPetrochemical and oTarget.m_FightType & WARRIOR_MONSTER and oTarget.IsPetrochemical():
            continue
        if iExcSuperMonster and oTarget.Query('MonsterSuper'):
            continue
        if iExculueKey and oTarget.QueryBitAttr('SpecialKey') & iExculueKey:
            continue
        if iExculueTarget:
            iExculueTarget = cl_formula.GetResultByData(oListener, iExculueTarget, dEventInfo, dMsgInfo)
            if iTarget == iExculueTarget:
                continue
            continue
        lstTarget.append(oTarget.m_ID)
    
    if iSort:
        dDis = oGame.Scene_GetTargetDisMap(oListener.m_ID, list(lstTarget))
        lstSort = sorted(dDis.items(), key = (lambda item: item[1]))
        lstTarget = [ x[0] for x in lstSort ]
    if iRandomCount:
        if iNotRandom:
            dTransInfo['TargetList'] = lstTarget[:iRandomCount]
        else:
            dTransInfo['TargetList'] = ShufferList(oGame, lstTarget, iRandomCount)
    else:
        dTransInfo['TargetList'] = lstTarget


def EventGetRangeTargetByWeight(oListener, oEventCB, iRange, iFightType, iCount, iMaxHeight, dMonsterWeight, dLifeWeight, dStateWeight):
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    vPos = oListener.GetPos()
    iRange = cl_formula.GetResultByData(oListener, iRange, dEventInfo, dMsgInfo)
    iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    fGroundDis = oGame.Scene_GroundDistance(oListener.m_Scene, vPos, iMaxHeight, PXMASK_BLOCK, oListener.m_ID)
    vPos = (vPos[0], vPos[1] - fGroundDis, vPos[2])
    vPos = (vPos[0], vPos[1] + oListener.m_ModelHeight / 2, vPos[2])
    dMask = {
        'Mask': PXMASK_MONSTER,
        'BlockMask': 0 }
    lstArgs = [
        vPos,
        iRange]
    lstVLST = cl_math.GetAttackTargetList(oGame, oListener.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    lstLifeWeight = sorted(dLifeWeight.items(), key = (lambda item: item[0]), reverse = True)
    iState = 0
    iStateWeight = 0
    iWithoutStateWeight = 0
    for iConfState, dInfo in dStateWeight.items():
        iState = iConfState
        iStateWeight = dInfo['hava']
        iWithoutStateWeight = dInfo['without']
    
    lstTarget = []
    for iTarget in lstVLST:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iFightType & oTarget.m_FightType != iFightType or oTarget is oListener:
            continue
        iLifeRatio = int(((oTarget.HP() + oTarget.Armor() + oTarget.Shield()) / (oTarget.QueryAttr('HPMax') + oTarget.QueryAttr('ArmorMax') + oTarget.QueryAttr('ShieldMax'))) * 100)
        fLifeWeight = 0
        for iLife, fWeightConfig in lstLifeWeight:
            if iLifeRatio >= iLife:
                fLifeWeight = fWeightConfig
                break
        
        iTypeWeight = dMonsterWeight.get(oTarget.m_SID, 0)
        if oTarget.m_State.GetItemBySID(iState):
            fWeight = fLifeWeight * iTypeWeight * iStateWeight
        else:
            fWeight = fLifeWeight * iTypeWeight * iWithoutStateWeight
        if fWeight > 0:
            lstTarget.append((oTarget.m_ID, fWeight))
    
    iCnt = min(iCount, len(lstTarget))
    lstTarget = sorted(lstTarget, key = (lambda item: item[1]), reverse = True)
    lstTargetId = []
    for i in range(iCnt):
        lstTargetId.append(lstTarget[i][0])
    
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTargetId


def EventTargetGetRangeTargetByFightType(oListener, oEventCB, iRange, iFightType, iIsExcSelf, iIsBlkStatic, iRandomCount = 0, iPetrochemical = 1, iSort = 0, iRepeatChoose = 0, cExtCheckFunc = None, iSortReverse = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    if iFightType & WARRIOR_HERO:
        iPxMask = PXMASK_PLAYER
    elif iFightType & WARRIOR_MONSTER:
        iPxMask = PXMASK_MONSTER
    else:
        iPxMask = PXMASK_LIVEOBJ
    dMask = {
        'Mask': iPxMask }
    if not iIsBlkStatic:
        dMask['BlockMask'] = 0
    lstNewTarget = []
    iRange = cl_formula.GetResultByData(oListener, iRange, dEventInfo, dMsgInfo)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget or not (oTarget.m_Scene):
            continue
        vPos = oTarget.GetPos()
        vPos = (vPos[0], vPos[1] + oTarget.m_ModelHeight / 2, vPos[2])
        lstArgs = [
            vPos,
            iRange]
        lstVLST = cl_math.GetAttackTargetList(oGame, oListener.m_Scene, ATT_SHAPE_SPHERE, lstArgs, dMask)
        if not lstVLST:
            continue
        if iSort:
            dVLST = oGame.Scene_GetTargetDisMap(iTarget, list(lstVLST))
            lstSort = sorted(dVLST.items(), key = (lambda x: x[1]), reverse = True if iSortReverse else False)
            lstVLST = [ x[0] for x in lstSort ]
        for iNewTarget in lstVLST:
            if iNewTarget in lstNewTarget:
                continue
            oNewTarget = oGame.GetObject(iNewTarget, PY_FLAG_DEAD)
            if (not oNewTarget or iFightType & oNewTarget.m_FightType != iFightType or iIsExcSelf) and oNewTarget is oTarget:
                continue
            if iPetrochemical and oNewTarget.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER and oNewTarget.IsPetrochemical():
                continue
            if not cExtCheckFunc and cl_formula.GetResultByData(oNewTarget, cExtCheckFunc, dEventInfo, dMsgInfo):
                continue
            lstNewTarget.append(iNewTarget)
        
    
    if not lstNewTarget:
        dTransInfo['TargetList'] = []
        return None
    iRandomCount = cl_formula.GetResultByData(oListener, iRandomCount, dEventInfo, dMsgInfo)
    if iRandomCount:
        if iSort:
            dTransInfo['TargetList'] = lstNewTarget[:iRandomCount]
        elif iRepeatChoose:
            iNewTarLen = len(lstNewTarget)
            lstChoose = []
            for _ in range(iRandomCount):
                idx = oGame.Random(iNewTarLen)
                lstChoose.append(lstNewTarget[idx])
            
            dTransInfo['TargetList'] = lstChoose
        else:
            dTransInfo['TargetList'] = ShufferList(oGame, lstNewTarget, iRandomCount)
    else:
        dTransInfo['TargetList'] = lstNewTarget


def EventTargetGetSectorTargetByFightType(oListener, oEventCB, iFightType, iRadius, fHeight, iAngle, iIsBlkStatic, iCount, iExculueKey, iRandom, iPetrochemical = 0, iSort = 0, iExculueTarget = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    if not oListener.m_Scene:
        return None
    if iFightType & WARRIOR_HERO:
        iPxMask = PXMASK_PLAYER
    elif iFightType & WARRIOR_MONSTER:
        iPxMask = PXMASK_MONSTER
    else:
        iPxMask = PXMASK_LIVEOBJ
    dMask = {
        'Mask': iPxMask }
    if not iIsBlkStatic:
        dMask['BlockMask'] = 0
    oGame = oListener.m_Game
    vPos = oListener.GetCenter()
    vPos = (vPos[0], vPos[1] - fHeight / 2, vPos[2])
    vFacing = oListener.GetFacing()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iRadius = cl_formula.GetResultByData(oListener, iRadius, dEventInfo, dMsgInfo)
    lstArgs = [
        vPos,
        vFacing,
        iRadius,
        fHeight,
        iAngle]
    if cl_math.IsZero(vFacing):
        lstVLST = set()
    else:
        lstVLST = cl_math.GetAttackTargetList(oGame, oListener.m_Scene, ATT_SHAPE_SECTOR, lstArgs, dMask)
    lstTarget = []
    for iTarget in lstVLST:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or oTarget.m_FightType & iFightType != iFightType:
            continue
        if oTarget.QueryBitAttr('SpecialKey') & iExculueKey:
            continue
        if iPetrochemical and oTarget.m_FightType & WARRIOR_MONSTER and oTarget.IsPetrochemical():
            continue
        if iExculueTarget:
            iExculueTarget = cl_formula.GetResultByData(oListener, iExculueTarget, dEventInfo, dMsgInfo)
            if iTarget == iExculueTarget:
                continue
            continue
        lstTarget.append(iTarget)
    
    if iSort:
        dDis = oGame.Scene_GetTargetDisMap(oListener.m_ID, list(lstTarget))
        lstSort = sorted(dDis.items(), key = (lambda item: item[1]))
        lstTarget = [ x[0] for x in lstSort ]
    if iCount:
        iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
        if iRandom:
            lstTarget = ShufferList(oGame, lstTarget, iCount)
        else:
            lstTarget = lstTarget[:iCount]
    dTransInfo['TargetList'] = lstTarget


def EventExcludeTargetByFightType(oListener, oEventCB, iFightType):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = []
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if 255 & iFightType or oTarget.m_FightType == iFightType:
            continue
        if oTarget.m_FightType & iFightType == iFightType:
            continue
        lstTarget.append(iTarget)
    
    dTransInfo['TargetList'] = lstTarget


def EventExcludeTargetByState(oListener, oEventCB, iState):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = []
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or oTarget.m_State.GetItemBySID(iState):
            continue
        lstTarget.append(iTarget)
    
    dTransInfo['TargetList'] = lstTarget


def EventGetTargetByDistanceAndState(oListener, oEventCB, iState):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = []
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_State.GetItemBySID(iState):
            continue
        lstTarget.append(iTarget)
    
    oGame = oListener.m_Game
    dDis = oGame.Scene_GetTargetDisMap(oListener.m_ID, lstTarget, 1)
    lstNewTarget = []
    if dDis:
        iNearTarget = min(dDis, key = (lambda iTar: dDis[iTar]))
        lstNewTarget.append(iNearTarget)
    dTransInfo['TargetList'] = lstNewTarget


def EventGetTargetByState(oListener, oEventCB, iState, iCount):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = []
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        if not oTarget.m_State.GetItemBySID(iState):
            continue
        lstTarget.append(iTarget)
    
    if iCount:
        dTransInfo['TargetList'] = lstTarget[:iCount] if iCount <= len(lstTarget) else lstTarget
    else:
        dTransInfo['TargetList'] = lstTarget


def EventPriorGetTargetByState(oListener, oEventCB, iState, iCount):
    if iCount <= 0:
        SendAlert('err', '%s事件 优先获取目标队列中拥有指定状态的目标 数量有误' % oEventCB.m_Key)
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if len(dTransInfo['TargetList']) <= iCount:
        return None
    lstPrior = []
    lstSecond = []
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_State.GetItemBySID(iState):
            iCount -= 1
            lstPrior.append(iTarget)
            if iCount <= 0:
                break
            continue
    
    if iCount:
        lstPrior.extend(lstSecond[:iCount])
    dTransInfo['TargetList'] = lstPrior


def EventGetTargetBySummonOwner(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    if oListener.m_FightType & WARRIOR_SUMMON == WARRIOR_SUMMON:
        dTransInfo['TargetList'] = [
            oListener.m_Owner]
    else:
        dTransInfo['TargetList'] = []


def EventGetStateInfoTarget(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    if 'StateInfo' in dEventInfo:
        lstTar.append(dEventInfo['StateInfo']['AID'])


def EventGetAllMonsterByTargetScene(oListener, oEventCB, iFilterDie, iFilterSelf = 0, iFilterAdd = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTransTarget = []
    dTransInfo['TargetList'] = lstTransTarget
    if not oListener.m_Scene:
        SendAlert('err', f'''{oEventCB.m_Key}事件场景不存在:{oListener.m_Scene}''')
        return None
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    lstTarget = oScene.GetObjectsByType('Monster')
    if not iFilterDie and not iFilterSelf and not iFilterAdd:
        dTransInfo['TargetList'] = lstTarget
    else:
        dEventInfo = oEventCB.GetCBEventInfo()
        iAttacker = 0
        if 'AID' in dEventInfo:
            iAttacker = dEventInfo['AID']
        iSelfID = oListener.m_ID
        for iTarget in lstTarget:
            if iFilterSelf and iSelfID == iTarget:
                continue
            if iFilterAdd and iAttacker == iTarget:
                continue
            if iFilterDie:
                oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
                if not oTarget:
                    continue
                continue
            lstTransTarget.append(iTarget)
        


def EventGetAllMonsterWithStateByTargetScene(oListener, oEventCB, dTargetState, iFilterDie, iFilterSelf, iFilterAdd, iFromSelf = 0):
    if not dTargetState:
        return None
    EventGetAllMonsterByTargetScene(oListener, oEventCB, iFilterDie, iFilterSelf, iFilterAdd)
    oGame = oListener.m_Game
    dTransTarget = { }
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo or not dTransInfo['TargetList']:
        return None
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        for iState in dTargetState:
            if iFromSelf:
                lstState = oTarget.m_State.GetItems(iState)
                for oState in lstState:
                    if oState.m_Attacker == oListener.m_ID:
                        dTransTarget[iTarget] = 1
                        break
                
                if iTarget in dTransTarget:
                    break
        
    
    dTransInfo['TargetList'] = list(dTransTarget)


def EventGetAllMonsterByStateMark(oListener, oEventCB, iState, sMark):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iTarget = dTransInfo['TargetList'][0]
    newlstTarget = []
    oTarget = oListener.m_Game.GetObject(iTarget)
    if sMark == 'dMonster' and oTarget and oTarget.m_State.GetItemBySID(iState):
        dMonster = oListener.Query('dMonster', { })
        for lstMonster in dMonster.values():
            newlstTarget = newlstTarget + lstMonster
        
        newlstTarget = list(set(newlstTarget))
        if iTarget in newlstTarget:
            newlstTarget.remove(iTarget)
        oListener.Set('dMonster', { })
    if sMark == 'lstMonsterCleanBySkill':
        newlstTarget = oListener.Query('lstMonsterCleanBySkill', [])
        oListener.Set('lstMonsterCleanBySkill', [])
    lstTarget = []
    for iTarget in newlstTarget:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if oTarget and oTarget.m_State.GetItemBySID(iState):
            lstTarget.append(iTarget)
    
    dTransInfo['TargetList'] = list(set(lstTarget))


def EventGetTargetByLevelBoss(oListener, oEventCB):
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    for mid in oScene.GetObjectsByType('Monster'):
        oMonster = oGame.GetObject(mid)
        if not oMonster:
            continue
        if oMonster.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            continue
        lstTar.append(mid)
    


def EventGetTargetByNearestHero(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    oGame = oListener.m_Game
    lstHero = oGame.GetWarMgr().GetLiveHero()
    iTarget = 0
    fMinDistance = 0
    vSelfPos = oListener.GetPos()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero)
        if not oHero or oHero.m_ID == oListener.m_ID:
            continue
        if oHero.m_Scene != oListener.m_Scene:
            continue
        fDistance = cl_math.CalDistance3D(vSelfPos, oHero.GetPos())
        if not not iTarget:
            if fDistance < fMinDistance:
                iTarget = iHero
                fMinDistance = fDistance
                continue
    
    if iTarget:
        lstTar.append(iTarget)


def EventGetTargetByHighHp(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if 'LastVLST' not in oSkill.m_Update:
        return None
    lstVLST = oSkill.m_Update['LastVLST']
    oGame = oListener.m_Game
    lstVictim = []
    for iVictim in lstVLST:
        oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
        if not oVictim:
            continue
        lstVictim.append((oVictim.HP(), oVictim.m_ID))
    
    if lstVictim:
        lstVictim.sort(reverse = True)
        lstTar.append(lstVictim[0][1])


def EventGetTargetByServant(oListener, oEventCB):
    EventGetTargetByOwnObj(oListener, oEventCB, OBJECT_SERVANT)


def EventGetTargetByOwnObj(oListener, oEventCB, iObjectType):
    dTransInfo = oEventCB.GetCBTransInfo()
    iTarget = oListener.GetOwnObjectID(iObjectType)
    dTransInfo['TargetList'] = [
        iTarget] if iTarget else []


def EventTargetGetTargetByOwnObj(oListener, oEventCB, iObjectType):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = dTransInfo['TargetList']
    if not lstTarget:
        return None
    oTarget = oListener.m_Game.GetObject(lstTarget[0])
    if not oTarget:
        return None
    EventGetTargetByOwnObj(oTarget, oEventCB, iObjectType)


def EventGetTargetByRelic(oListener, oEventCB, iRelic, iIncludeSelf = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    if not oListener.m_Scene:
        SendAlert('err', f'''{oEventCB.m_Key}事件场景不存在:{oListener.m_Scene}''')
        return None
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    lstHero = oScene.GetHeros()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
        if not oHero:
            continue
        if not iIncludeSelf and iHero == oListener.m_ID:
            continue
        if oHero.m_RelicCon.IsEnabled(iRelic):
            lstTar.append(iHero)
    


def EventGetTargetByMonsterRelic(oListener, oEventCB, iMonsterRelic, iIncludeSelf = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    if not oListener.m_Scene:
        SendAlert('err', f'''{oEventCB.m_Key}事件场景不存在:{oListener.m_Scene}''')
        return None
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    lstMonster = oScene.GetObjectsByType('Monster')
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if not iIncludeSelf and iMonster == oListener.m_ID:
            continue
        if oMonster.m_Perform.GetPerform(iMonsterRelic):
            lstTar.append(iMonster)
    


def EventGetTargetByAttackHero(oLitener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    if 'AID' in dMsgInfo:
        lstTar.append(dMsgInfo['AID'])
    elif 'Skill' in dMsgInfo:
        lstTar.append(dMsgInfo['Skill'].m_Base['AID'])
    if not lstTar:
        return None
    oTarget = oLitener.m_Game.GetObject(lstTar[0])
    if oTarget and oTarget.m_FightType & WARRIOR_SERVANT:
        lstTar[0] = oTarget.GetOwner().m_ID


def CBTriggerGroup(oListener, oEventCB, dWeight, bDirectly = False):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'PFType' in dEventInfo and dEventInfo['PFType'] == PF_TYPE_BULLETCHANGE:
        iRand = oListener.m_LineRandom.Random(10000)
    else:
        iRand = oListener.m_Game.Random(10000)
    iCmpValue = 0
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for iGroup, iChance in dWeight.items():
        iChance = cl_formula.GetResultByData(oListener, iChance, dEventInfo, dMsgInfo)
        iCmpValue += iChance
        if iRand < iCmpValue or bDirectly:
            if iGroup not in oEventCB.m_CBFuncAction:
                return None
            func = oEventCB.m_CBFuncAction[iGroup]
            func(oEventCB, oListener)
        else:
            oEventCB.CBFuncAction(oListener, iGroup, dEventInfo, dMsgInfo)
        return None
    


def RepeatTriggerGroup(oListener, oEventCB, iGroup, iRepeat, iDirectTrigger = 0):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iRepeat = cl_formula.GetResultByData(oListener, iRepeat, dEventInfo, dMsgInfo)
    iMaxRepeat = 5
    if iRepeat > iMaxRepeat:
        SendAlert('err', '%s重复执行回调行为组%d次,超出%d次上限' % (oEventCB.m_Key, iRepeat, iMaxRepeat))
        iRepeat = iMaxRepeat
    if iDirectTrigger:
        func = Functor(oEventCB.m_CBFuncAction[iGroup], oEventCB, oListener)
    else:
        func = Functor(oEventCB.CBFuncAction, oListener, iGroup, dEventInfo, dMsgInfo)
    for _ in range(iRepeat):
        func()
    


def TrueTriggerGroup(iListener, sKey, oLifeCycle, iGroup, iDelayFrame, dMsgInfo):
    if not oLifeCycle.m_Owner:
        return None
    oBuff = oLifeCycle.GetObject()
    oListener = oBuff.m_Game.GetObject(iListener)
    if not oListener:
        return None
    if isinstance(oBuff, cl_perform.mobject.CBasePerform) and not (oBuff.m_Enable):
        oListener.Delete(sKey)
        return None
    if not oBuff.m_EventCB:
        return None
    dEventInfo = oLifeCycle.AttrCache()
    dEventInfo['LifeCycle'] = oLifeCycle
    oBuff.m_EventCB.CBFuncAction(oListener, iGroup, dEventInfo, dMsgInfo)
    iCount = oListener.Query(sKey, 0)
    if iCount > 1:
        oListener.Add(sKey, -1)
        oListener.Call_Out(Functor(TrueTriggerGroup, iListener, sKey, oLifeCycle, iGroup, iDelayFrame, dMsgInfo), iDelayFrame, sKey)
    else:
        oListener.Delete(sKey)


def DelayTriggerGroup(oListener, oEventCB, iGroup, iRepeat, iDelayTime, iUseMsgInfo, iUnique = 0, dExtraMsgInfo = None):
    
    def ClearFunc(oWarrior, oLifeCycle):
        oWarrior.Delete(sKey)
        oWarrior.Remove_Call_Out(sKey)

    if iRepeat < 1:
        return None
    if iUnique:
        sKey = 'DelayTrigger-%s-%s' % (oEventCB.m_Key, oListener.m_Game.GetFrameNum())
    else:
        sKey = 'DelayTrigger-' + oEventCB.m_Key
    if not oListener.Query(sKey, 0):
        dEventInfo = oEventCB.GetCBEventInfo()
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iDelayTime = cl_formula.GetResultByData(oListener, iDelayTime, dEventInfo, dMsgInfo)
        iDelayFrame = Time2Frame(iDelayTime)
        oListener.Set(sKey, iRepeat)
        dDelayMsgInfo = dExtraMsgInfo if dExtraMsgInfo else { }
        if iUseMsgInfo:
            if 'CurVID' in dMsgInfo:
                dDelayMsgInfo['CurVID'] = dMsgInfo['CurVID']
            elif 'VID' in dMsgInfo:
                dDelayMsgInfo['CurVID'] = dMsgInfo['VID']
            if 'Skill' in dMsgInfo:
                oSkill = dMsgInfo['Skill']
                if 'CurVID' not in dDelayMsgInfo:
                    dDelayMsgInfo['CurVID'] = oSkill.m_Base['VID']
                dDelayMsgInfo['ActNum'] = oSkill.m_Base['ActNum']
                if 'Cartoon' in dMsgInfo:
                    dDelayMsgInfo['Cartoon'] = dMsgInfo['Cartoon']
        oLifeCycle = dEventInfo['LifeCycle']
        oListener.Call_Out(Functor(TrueTriggerGroup, oListener.m_ID, sKey, oLifeCycle, iGroup, iDelayFrame, dDelayMsgInfo), iDelayFrame, sKey)
        oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, 0)


def RemoveDelayTriggerGroup(oListener, oEventCB):
    sKey = 'DelayTrigger-' + oEventCB.m_Key
    oListener.Delete(sKey)
    oListener.Remove_Call_Out(sKey)


def NextFrameTriggerGroup(oListener, oEventCB, iGroup, iUseMsgInfo = 0):
    
    def TrueTriggerGroup(oLifeCycle, iGroup, dMsgInfo):
        if not oLifeCycle.m_Owner:
            return None
        pfobj = oLifeCycle.GetObject()
        if not pfobj.m_Enable:
            return None
        dEventInfo = oLifeCycle.AttrCache()
        dEventInfo['LifeCycle'] = oLifeCycle
        oEventCB.CBFuncAction(oListener, iGroup, dEventInfo, dMsgInfo)

    sKey = 'NextFrameTrigger-' + oEventCB.m_Key
    if not oListener.Find_Call_Out(sKey):
        dEventInfo = oEventCB.GetCBEventInfo()
        dNextFrameMsgInfo = { }
        if iUseMsgInfo:
            dMsgInfo = oEventCB.GetCBMsgInfo()
            if 'CurVID' in dMsgInfo:
                dNextFrameMsgInfo['CurVID'] = dMsgInfo['CurVID']
            elif 'VID' in dMsgInfo:
                dNextFrameMsgInfo['CurVID'] = dMsgInfo['VID']
            elif 'Skill' in dMsgInfo:
                dNextFrameMsgInfo['CurVID'] = dMsgInfo['Skill'].m_Base['VID']
        oLifeCycle = dEventInfo['LifeCycle']
        oListener.Call_Out(Functor(TrueTriggerGroup, oLifeCycle, iGroup, dNextFrameMsgInfo), 1, sKey)


def EventClientBehavior(oListener, oEventCB, iBehavior, iStop = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstPlayer = oListener.m_Game.m_WarMgr.GetRoomPlayer()
    for iVictim in dTransInfo['TargetList']:
        cl_snetwar.GS2CTriggerBehavior(oListener.m_Game, iVictim, iBehavior, lstPlayer, iStop)
    


def EventChangeHP(oListener, oEventCB, iValue):
    EventChangeDefValue(oListener, oEventCB, iValue, DAM_USE_HP)


def EventChangeShield(oListener, oEventCB, iValue):
    EventChangeDefValue(oListener, oEventCB, iValue, DAM_USE_SHIELD)


def EventChangeArmor(oListener, oEventCB, iValue):
    EventChangeDefValue(oListener, oEventCB, iValue, DAM_USE_ARMOR)


def EventChangeDefValue(oListener, oEventCB, iValue, iDamUseType, iShowTips = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oReason = dEventInfo['RS'].ExtInfo({
        'ShowTips': iShowTips,
        'DamType': DAM_TYPE_TRUE | iDamUseType })
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        iFormulaValue = cl_formula.GetResultByData(oTarget, iValue, dEventInfo, dMsgInfo)
        if iFormulaValue < 0:
            lstChange = [
                (-iFormulaValue, oReason)]
            if 'CurVID' in dMsgInfo and dMsgInfo['CurVID'] == iTarget and 'FlowDam' in dMsgInfo:
                dMsgInfo['FlowDam'].extend(lstChange)
            else:
                oTarget.HPModifyDam(oListener.m_ID, lstChange)
        if iFormulaValue > 0:
            lstChange = [
                (iFormulaValue, oReason)]
            if 'CurVID' in dMsgInfo and dMsgInfo['CurVID'] == iTarget and 'FlowCure' in dMsgInfo:
                dMsgInfo['FlowCure'].extend(lstChange)
                continue
            oTarget.HPModifyCure(oListener.m_ID, lstChange)
    


def EventChangeEnergy(oListener, oEventCB, iValue):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        iFormulaValue = cl_formula.GetResultByData(oTarget, iValue, dEventInfo, dMsgInfo)
        oTarget.EnergyModify(iFormulaValue)
    


def EventTargetDamage(oListener, oEventCB, iValue, iDamType, iShowTips, iCalByListener = 0, iSendMsg = 0, iPlaySound = 1, iCalLuckyHit = 0, iUseByAttacker = 0, iCalWeakness = 0, iCalSkillFactor = 0, iExShowTipsType = 0, iTimes = 0, iCopyTimes = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dReason = {
        'ShowTips': iShowTips,
        'DamType': iDamType,
        'ExInfo': iPlaySound,
        'CalLuckyHit': iCalLuckyHit }
    if iExShowTipsType:
        dReason['ExInfo'] = iPlaySound | iExShowTipsType if iPlaySound else iExShowTipsType
        if iTimes:
            iTimes = cl_formula.GetResultByData(oListener, iTimes, dEventInfo, dMsgInfo)
            iTimes = 7 if iTimes > 7 else iTimes
            dReason['ExInfo'] = dReason['ExInfo'] | iTimes << 1
    if iCopyTimes:
        if iTimes:
            SendAlert('err', '%s回调目标伤害的跳字段数和复制伤害次数不能同时使用' % oEventCB.m_Key)
            return None
        iCopyTimes = cl_formula.GetResultByData(oListener, iCopyTimes, dEventInfo, dMsgInfo)
        if iCopyTimes > 6:
            iCopyTimes = 6
        dReason['CopyTimes'] = iCopyTimes
        dReason['ExInfo'] = dReason['ExInfo'] | iCopyTimes + 1 << 1
    if 'StateSID' in dEventInfo:
        dReason['SourceState'] = dEventInfo['StateSID']
    if 'Skill' in dMsgInfo:
        dReason['FromActNum'] = dMsgInfo['Skill'].m_Base['ActNum']
    if 'RS' in dMsgInfo:
        dReason['FromDamType'] = dMsgInfo['RS'].Query('DamType', 0)
    oReason = dEventInfo['RS'].ExtInfo(dReason)
    if iCalByListener:
        iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    if iUseByAttacker and 'AID' in dMsgInfo:
        iAttack = dMsgInfo['AID']
    else:
        iAttack = dEventInfo['AID']
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        iDamage = cl_formula.GetResultByData(oTarget, iValue, dEventInfo, dMsgInfo)
        lstDam = [
            (iDamage, oReason)]
        if 'CurVID' in dMsgInfo and dMsgInfo['CurVID'] == iTarget and 'FlowDam' in dMsgInfo and not iUseByAttacker:
            dMsgInfo['FlowDam'].extend(lstDam)
            continue
        dDamFactor = dMsgInfo['CBDamFactor'] if 'CBDamFactor' in dMsgInfo else {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } }
        dDamage = {
            'AID': iAttack,
            'CurVID': iTarget,
            'MainDam': lstDam,
            'FlowDam': [],
            'RS': oReason,
            'DamFactor': dDamFactor }
        if 'CrazyEff' in dEventInfo:
            dDamage['CrazyEff'] = dEventInfo['CrazyEff']
        if iCalWeakness and 'CrazyEff' in dMsgInfo:
            dDamage['CrazyEff'] = dMsgInfo['CrazyEff']
        if iCalLuckyHit and 'LuckyHitEff' in dMsgInfo:
            dDamage['LuckyHitEff'] = dMsgInfo['LuckyHitEff']
        if iCalSkillFactor and 'Skill' in dMsgInfo:
            dDamage['Skill'] = dMsgInfo['Skill']
        oTarget.ReceiveDamage(iAttack, dDamage, iSendMsg)
    


def EventAddMarkShieldDam(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'RS' not in dEventInfo:
        return None
    oReason = dEventInfo['RS'].ExtInfo({
        'ThunderStrike': 1 })
    dEventInfo['RS'] = oReason


def EventAddMarkInReason(oListener, oEventCB, iPeriod):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oSkill.m_Cache['DebuffPeriod'] = iPeriod


def EventTargetSputterRealDamage(oListener, oEventCB, iRate, iShowTips):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'FinalDam' in dMsgInfo:
        iDam = dMsgInfo['FinalDam']
        iDam = iDam * iRate // 100
        iDamType = DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL
        EventTargetDamage(oListener, oEventCB, iDam, iDamType, iShowTips)
    else:
        SendAlert('err', '%s需要监听击杀消息' % oEventCB.m_Key)


def EventTargetSputterDamage(oListener, oEventCB, iRate, iShowTips, iPlaySound = 1, iSendMsg = 0, iCalLuckyHit = 0, iUseByAttacker = 0, iCalWeakness = 0, iTimes = 1, iCalSkillFactor = 0, iExShowTipsType = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DamFactor' in dMsgInfo:
        dMsgInfo['CBDamFactor'] = DeepCopy(dMsgInfo['DamFactor'])
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'CurVID' not in oSkill.m_Update:
            return None
        iVictim = oSkill.m_Update['CurVID']
        dVictim = oSkill.m_Update[iVictim]
        dMsgInfo['CBDamFactor'] = DeepCopy(dVictim['DamFactor'])
    dEventInfo = oEventCB.GetCBEventInfo()
    iRate = cl_formula.GetResultByData(oListener, iRate, dEventInfo, dMsgInfo)
    if not iTimes:
        iTimes = 1
    if 'MainDam' in dMsgInfo:
        for lstDam in dMsgInfo['MainDam']:
            (iDam, oReason) = lstDam
            iDam = iDam * iRate // 100
            iDamType = oReason.Query('DamType', 0)
            for _ in range(iTimes):
                EventTargetDamage(oListener, oEventCB, iDam, iDamType, iShowTips, 0, iSendMsg, iPlaySound, iCalLuckyHit, iUseByAttacker, iCalWeakness, iCalSkillFactor, iExShowTipsType)
            
        
    elif 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iDam = oReason.Query('InitDam')
        if iDam:
            iDam = iDam * iRate // 100
            iDamType = oReason.Query('DamType', 0)
            for _ in range(iTimes):
                EventTargetDamage(oListener, oEventCB, iDam, iDamType, iShowTips, 0, iSendMsg, iPlaySound, iCalLuckyHit, iUseByAttacker, iCalWeakness, iCalSkillFactor, iExShowTipsType)
            
    if 'CBDamFactor' in dMsgInfo:
        dMsgInfo.pop('CBDamFactor')


def EventCBCopyMainDamage(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo or 'FlowDam' not in dMsgInfo:
        return None
    lstFlowDam = dMsgInfo['FlowDam']
    for lstDam in dMsgInfo['MainDam']:
        (iDam, oReason) = lstDam
        oCopyReason = oReason.ExtInfo({ })
        lstFlowDam.append((iDam, oCopyReason))
    


def EventCBSkillCopyWeaponTrajectoryDamage(oListener, oEventCB, iCalProbability, iMulDamage, iAddDamage):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iCalProbability = cl_formula.GetResultByData(oListener, iCalProbability, dEventInfo, dMsgInfo)
    if iCalProbability < 0:
        return None
    iAddDamage = cl_formula.GetResultByData(oListener, iAddDamage, dEventInfo, dMsgInfo)
    iMulDamage = cl_formula.GetResultByData(oListener, iMulDamage, dEventInfo, dMsgInfo)
    dCopyArgs = {
        oEventCB.m_Key: (iAddDamage, iMulDamage) }
    if 'CopyWeapon' not in oSkill.m_Collect:
        oSkill.m_Collect['CopyWeapon'] = {
            'CalProbability': iCalProbability,
            'CopyArgs': dCopyArgs,
            'CopyCartoon': { } }
    else:
        dOldCopyWeapon = oSkill.m_Collect['CopyWeapon']
        if dOldCopyWeapon['CalProbability'] < iCalProbability:
            dOldCopyWeapon['CalProbability'] = iCalProbability
            dOldCopyWeapon['CopyArgs'] = dCopyArgs


def EventCBCopyPerformDamage(oListener, oEventCB, iTimes):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iTimes = cl_formula.GetResultByData(oListener, iTimes, dEventInfo, dMsgInfo)
    oSkill = dMsgInfo['Skill']
    oSkill.m_Collect['CopyTimes'] = iTimes


def EventCBCopyCurPerformDamage(oListener, oEventCB, iTimes):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iTimes = cl_formula.GetResultByData(oListener, iTimes, dEventInfo, dMsgInfo)
    oReason = dMsgInfo['RS']
    iTimes += oReason.Query('CopyTimes', 0)
    oReason.SetInfo('CopyTimes', iTimes)
    iExInfo = oReason.Query('ExInfo', 1) | iTimes + 1 << 1
    oReason.SetInfo('ExInfo', iExInfo)


def EventCBReduceExcessDamage(oListener, oEventCB, iThresHold):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo or 'ExcessChange' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iTempCnt = cl_formula.GetResultByData(oListener, iThresHold, dEventInfo, dMsgInfo)
    iThresHold = iTempCnt
    lstPredictChange = dMsgInfo['PredictChange']
    iOldPredictChange = sum(lstPredictChange)
    if iOldPredictChange:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        oReason = dMsgInfo['RS'] if 'RS' in dMsgInfo else None
        iDamType = oReason.Query('DamType', 0) if oReason else 0
        for idx, _, iUseType in cl_formula.g_DamTypeSequence:
            if not lstPredictChange[idx] and iDamType & iUseType or iTempCnt:
                lstPredictChange[idx] = 0
                continue
            if lstPredictChange[idx] >= iTempCnt:
                lstPredictChange[idx] = iTempCnt
                iTempCnt = 0
                continue
            iTempCnt -= lstPredictChange[idx]
        
        iExcessChange = dMsgInfo['ExcessChange']
        iNewPredictChange = sum(lstPredictChange)
        if iNewPredictChange + iExcessChange > iThresHold:
            iExcessChange = iThresHold - iNewPredictChange
        if dMsgInfo['ExcessChange'] > 0:
            dMsgInfo['ExcessChange'] = iExcessChange


def EventTargetCure(oListener, oEventCB, iValue, iCurType, iShowTips, iCalByListener = 0, iTime = 0):
    
    def DelayEventTargetCure(oTarget, dCure):
        oTarget.ReceiveCure(oListener.m_ID, dCure)

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    dData = {
        'ShowTips': iShowTips,
        'DamType': iCurType }
    if 'ItemID' in dEventInfo:
        dData['Item'] = dEventInfo['ItemID']
    oReason = dEventInfo['RS'].ExtInfo(dData)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iCalByListener:
            iCure = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
        else:
            iCure = cl_formula.GetResultByData(oTarget, iValue, dEventInfo, dMsgInfo)
        if not iCure:
            continue
        lstCure = [
            [
                iCure,
                oReason]]
        if 'CurVID' in dMsgInfo and dMsgInfo['CurVID'] == iTarget and 'FlowCure' in dMsgInfo:
            dMsgInfo['FlowCure'].extent(lstCure)
            continue
        dCure = {
            'MainCure': lstCure,
            'FlowCure': [],
            'RS': oReason }
        if not iTime:
            oTarget.ReceiveCure(oListener.m_ID, dCure)
            continue
        oTarget.Call_Out(Functor(DelayEventTargetCure, oTarget, dCure), Time2Frame(iTime), oEventCB.m_Key)
    


def EventChangeCureType(oListener, oEventCB, iOldType, iNewtype, iAdaptive):
    
    def ChangeCureType(dMsgInfo, sFlag, iOldType, iNewtype):
        iType = CURE_TYPE_PERFORM | iNewtype
        for idx, lstCure in enumerate(dMsgInfo[sFlag]):
            (_, oReason) = lstCure
            iCureType = oReason.Query('DamType', 0)
            if iCureType & iOldType:
                oReason = oReason.ExtInfo({
                    'DamType': iType })
                dMsgInfo[sFlag][idx][1] = oReason
        

    if iAdaptive:
        if iNewtype & DAM_USE_ARMOR or iNewtype & DAM_USE_SHIELD:
            if not oListener.QueryAttr('ShieldMax') and oListener.QueryAttr('ArmorMax'):
                iNewtype = DAM_USE_ARMOR
            if not oListener.QueryAttr('ArmorMax') and oListener.QueryAttr('ShieldMax'):
                iNewtype = DAM_USE_SHIELD
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainCure' not in dMsgInfo:
        return None
    ChangeCureType(dMsgInfo, 'MainCure', iOldType, iNewtype)
    if 'FlowCure' in dMsgInfo and dMsgInfo['FlowCure']:
        ChangeCureType(dMsgInfo, 'FlowCure', iOldType, iNewtype)


def EventReduceBulletUse(oListener, oEventCB, iClientBehavior):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oSkill.m_Collect['NoBulletUse'] = 1
    if iClientBehavior:
        cl_snetwar.GS2CTriggerBehavior(oListener.m_Game, oListener.m_ID, iClientBehavior, [
            oListener.m_PlayerID], 0)


def EventSplitTargetExecCBFuncAction(oListener, oEventCB, iGroup):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList'][:]
    for iTarget in lstTar:
        dTransInfo['TargetList'] = [
            iTarget]
        func = oEventCB.m_CBFuncAction[iGroup]
        func(oEventCB, oListener)
    


def EventSetLimitDamage(oListener, oEventCB, iLimitDam):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iLimitDam = cl_formula.GetResultByData(oListener, iLimitDam, dEventInfo, dMsgInfo)
    iTotalChange = 0
    for idx, iChange in enumerate(dMsgInfo['PredictChange']):
        if iTotalChange + iChange >= iLimitDam:
            dMsgInfo['PredictChange'][idx] = iLimitDam - iTotalChange
            iTotalChange = iLimitDam
            continue
        iTotalChange += iChange
    
    oVictim = oListener.m_Game.GetObject(dMsgInfo['VID'])
    if oVictim and oVictim.m_Side == SIDE_TYPE_HERO:
        dMsgInfo['ExcessChange'] = 0


def EventSetPreCureHp(oListener, oEventCB, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PreCureHp' in dMsgInfo:
        (_iHp, sKey) = dMsgInfo['PreCureHp']
        SendAlert('err', '回调设置预回复血量只支持单来源 已有%s，新增%s' % (sKey, oEventCB.m_Key))
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    dMsgInfo['PreCureHp'] = (iValue, oEventCB.m_Key)


def EventChangeDamFactor(oListener, oEventCB, iType, iAdd, iMul, iMask, sSuffix = ''):
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = GetCommonEventKey(dEventInfo)
    if sSuffix:
        sKey += sSuffix
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    dMsgInfo['DamFactor'][iType][sKey] = (iAdd, iMul, iMask)


def EventRecordDamFactorIndex(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DamFactor' not in dMsgInfo:
        return None
    if 'DamFactorIndex' not in dMsgInfo:
        dMsgInfo['DamFactorIndex'] = { }
    if iType not in dMsgInfo['DamFactorIndex']:
        dMsgInfo['DamFactorIndex'][iType] = len(dMsgInfo['DamFactor'][iType])


def EventAddRecordDamFactor(oListener, oEventCB, iType, iEffect):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DamFactorIndex' not in dMsgInfo or iType not in dMsgInfo['DamFactorIndex']:
        return None
    iDamFactorIndex = dMsgInfo['DamFactorIndex'][iType]
    iNowDamFactorIndex = len(dMsgInfo['DamFactor'][iType])
    if iNowDamFactorIndex <= iDamFactorIndex:
        return None
    dDamFactor = dMsgInfo['DamFactor'][iType]
    lstChangeFactor = list(dDamFactor.items())[-(iNowDamFactorIndex - iDamFactorIndex):]
    for sKey, (iAdd, iMul, iMask) in lstChangeFactor:
        if iAdd > 0:
            iAdd += iAdd * iEffect // 10000
        if iMul > 0:
            iMul += iMul * iEffect // 10000
        dDamFactor[sKey] = (iAdd, iMul, iMask)
    


def EventSetDamCrazyEff(oListener, oEvnetCB, iValue):
    dMsgInfo = oEvnetCB.GetCBMsgInfo()
    if 'CrazyEff' in dMsgInfo:
        dMsgInfo['CrazyEff'] = iValue


def EventChangeDamCrazyEff(oListener, oEvnetCB, iAdd, iMul):
    dMsgInfo = oEvnetCB.GetCBMsgInfo()
    if 'CrazyEff' in dMsgInfo:
        dEventInfo = oEvnetCB.GetCBEventInfo()
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
        iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
        dMsgInfo['CrazyEff'] = dMsgInfo['CrazyEff'] * (10000 + iMul) // 10000 + iAdd


def EventChangeEleStateCache(oListener, oEventCB, sAttr, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'StateInfo' not in dMsgInfo:
        return None
    dState = dMsgInfo['StateInfo']
    dStateCache = dState['arg']['Cache']
    if sAttr not in dStateCache:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    dStateCache[sAttr] = dStateCache[sAttr] * (10000 + iMul) // 10000 + iAdd


def EventChangeSkillCache(oListener, oEventCB, sAttr, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if sAttr not in oSkill.m_Cache:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    oSkill.m_Cache[sAttr] = oSkill.m_Cache[sAttr] * (10000 + iMul) // 10000 + iAdd


def EventChangeCauseEleStateDamFactor(oListener, oEventCB, iType, iAdd, iMul, iMask):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'StateInfo' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = GetCommonEventKey(dEventInfo)
    dState = dMsgInfo['StateInfo']
    dStateDamFactor = dState['arg']['DamFactor']
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    dStateDamFactor[iType][sKey] = (iAdd, iMul, iMask)


def EventSetSkillCache(oListener, oEventCB, sAttr, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    oSkill.m_Cache[sAttr] = iValue


def EventSetSkillCacheData(oListener, oEventCB, iChooseIndex, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    if iChooseIndex in [
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTPOS,
        SKILLCACHE_LSTINTSPECIAL]:
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, iChooseIndex, [
            iValue])
    else:
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, iChooseIndex, iValue)


def EventAddSkillCacheData(oListener, oEventCB, iChooseIndex, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    if iChooseIndex not in [
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTPOS,
        SKILLCACHE_LSTINTSPECIAL]:
        SendAlert('err', '%s错误的缓存key %s' % (oEventCB.m_Key, iChooseIndex))
        return None
    oSkill = dMsgInfo['Skill']
    lstValue = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, iChooseIndex)
    if not lstValue:
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, iChooseIndex, [
            iValue])
    else:
        lstValue.append(iValue)
        cl_perform.skillcache.SetSkillCacheByIndex(oSkill, iChooseIndex, lstValue)


def EventAddBagBullet(oListener, oEventCB, iBullet, iAmount):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = GetCommonEventKey(dEventInfo)
    iAmount = cl_formula.GetResultByData(oListener, iAmount, dEventInfo, dMsgInfo)
    oBulletCon = oListener.m_BulletCon
    if iAmount < 0:
        iHasBullet = oBulletCon.Bullet(iBullet)
        if iHasBullet + iAmount < 0:
            iAmount = 0 - iHasBullet
    oBulletCon.BulletModify(iBullet, int(iAmount), sKey)


def EventCBModifyTargetBagBulletByRatio(oListener, oEventCB, dBullet, iRatio):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    sKey = oEventCB.m_Key
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget or not (oTarget.m_FightType & WARRIOR_HERO):
            continue
        dWeight = { }
        oBulletCon = oTarget.m_BulletCon
        for iBullet, iWeight in dBullet.items():
            if oBulletCon.Bullet(iBullet):
                dWeight[iBullet] = iWeight
        
        if not dWeight:
            continue
        iChangeBullet = ChooseKey(oGame, dWeight)
        iAmount = oBulletCon.Bullet(iChangeBullet) * iRatio
        oBulletCon.BulletModify(iChangeBullet, iAmount, sKey)
    


def EventCBSetPhase(oListener, oEventCB, iPhase):
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iPhase = cl_formula.GetResultByData(oListener, iPhase, dEventInfo, dMsgInfo)
    oListener.SetPhase(iPhase)


def EventCBKillSummon(oListener, oEventCB, iPrefab):
    oGame = oListener.m_Game
    iScene = oListener.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstSummon = oScene.GetObjectsByType('Summon')
    for iSummon in lstSummon:
        oSummon = oGame.GetObject(iSummon)
        if oSummon and oSummon.m_Prefab == iPrefab:
            oSummon.Remove('EventTrigger')
            break
    


def EventCBSetDamageType(oListener, oEventCB, iNewDamType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    lstOnlyType = [
        DAM_MASK_ELEMENT,
        DAM_MASK_PART,
        DAM_MASK_SRC]
    dEventInfo = oEventCB.GetCBEventInfo()
    iNewDamType = cl_formula.GetResultByData(oListener, iNewDamType, dEventInfo, dMsgInfo)
    for idx, (iDam, oReason) in enumerate(dMsgInfo['MainDam']):
        iDamType = oReason.Query('DamType', 0)
        if iDamType & DAM_TYPE_SHIELD and iNewDamType & DAM_MASK_PART:
            continue
        iForbidModifyType = oReason.Query('ForbidModifyType', 0)
        if iForbidModifyType & iNewDamType:
            continue
        iChange = 0
        for iChangeType in lstOnlyType:
            if iNewDamType & iChangeType:
                iDamType = iDamType & ~iChangeType | iNewDamType
                iChange = 1
                break
        
        if not iChange:
            iDamType |= iNewDamType
        oReason = oReason.ExtInfo({
            'DamType': iDamType })
        dMsgInfo['MainDam'][idx] = [
            iDam,
            oReason]
    


def EventCBForbidCrazy(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['ForbidCrazy'] = 1


def EventCBSetCurPerformCD(oListener, oEventCB, iTime):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iTime' not in dMsgInfo:
        return None
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    dMsgInfo['iTime'] = iTime


def EventCBSubCareerPerformColdTime(oListener, oEventCB, iAdd, iMul):
    pfobj = oListener.GetCareerPerform()
    if not pfobj:
        return None
    iPerform = pfobj.m_SID
    iColdTimeFrame = oListener.m_Perform.GetTotalColdTime(iPerform)
    if not iColdTimeFrame:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iFrame = Time2Frame(iAdd)
    if iMul:
        iMaxColdTimeFrame = oListener.m_Perform.GetMaxColdTime(iPerform)
        iFrame += iMaxColdTimeFrame * iMul // 100
    oListener.m_Perform.ModifyColdTime(iPerform, -iFrame)


def EventCBRefreshPerformColdTime(oListener, oEventCB, iPerform):
    oPerformCon = oListener.m_Perform
    pfobj = oPerformCon.GetPerform(iPerform)
    if not pfobj:
        return None
    oPerformCon.DelCoverColdTime(iPerform)


def EventCBSubPerformColdTimeByCover(oListener, oEventCB, iCover):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'pfid' not in dMsgInfo or 'iTime' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iCover = cl_formula.GetResultByData(oListener, iCover, dEventInfo, dMsgInfo)
    if iCover <= 0:
        return None
    oPerformCon = oListener.m_Perform
    pfobj = oPerformCon.GetPerform(dMsgInfo['pfid'])
    if not pfobj:
        return None
    iSubCD = pfobj.GetCDTime(oListener) * iCover // 100
    iCurTotalCD = dMsgInfo['iTime']
    if iCurTotalCD > iSubCD:
        dMsgInfo['iTime'] -= iSubCD
    else:
        dMsgInfo['iTime'] = 0


def EventCBSetCollectInfo(oListener, oEventCB, sAttr, iAdd, iAddExtInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
    elif 'ActNum' in dMsgInfo:
        oSkill = oListener.m_Game.m_SkillMgr.GetSkill(oListener.m_ID, dMsgInfo['ActNum'])
    else:
        oSkill = None
    if not oSkill:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if iAddExtInfo:
        sAttr = '%s%s' % (oEventCB.m_Key, sAttr)
    iValue = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oSkill.m_Collect[sAttr] = iValue


def EventCBAddCollectInfo(oListener, oEventCB, sAttr, iAdd, iAddExtInfo = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
    elif 'ActNum' in dMsgInfo:
        oSkill = oListener.m_Game.m_SkillMgr.GetSkill(oListener.m_ID, dMsgInfo['ActNum'])
    else:
        return None
    if not oSkill:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if iAddExtInfo:
        sAttr = '%s%s' % (oEventCB.m_Key, sAttr)
    iOldValue = oSkill.m_Collect[sAttr] if sAttr in oSkill.m_Collect else 0
    iValue = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oSkill.m_Collect[sAttr] = iOldValue + iValue


def EventCBClearCollectInfo(oListener, oEventCB, sAttr, iAddExtInfo = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    if iAddExtInfo:
        sAttr = '%s%s' % (oEventCB.m_Key, sAttr)
    oSkill = dMsgInfo['Skill']
    oSkill.m_Collect.pop(sAttr, 0)


def EventCBUpdateCustomPosInfo(oListener, oEventCB, dData):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oSkill.m_Custom.update(dData)


def EventCBAddCash(oListener, oEventCB, iAdd, iJumpFigure, iSource, iCnt = 0, iIsBlockMsg = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = GetCommonEventKey(dEventInfo)
    idx = sKey.find('-')
    if idx != -1:
        sKey = sKey[:idx]
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iSendMsg = 0 if iIsBlockMsg else 1
    if iAdd == 0:
        return None
    if iAdd < 0 and oListener.m_WarCash == 0:
        return None
    if iAdd < 0 and oListener.m_WarCash < -iAdd:
        iAdd = -(oListener.m_WarCash)
    oListener.AddCash(iAdd, sKey, iSendMsg, iLog = 0)
    if iJumpFigure:
        iCnt = cl_formula.GetResultByData(oListener, iCnt, dEventInfo, dMsgInfo)
        iTarget = 0
        if iSource == JUMPFIGURE_KILLMONSTER:
            iTarget = dMsgInfo['VID'] if 'VID' in dMsgInfo else 0
        elif iSource in (JUMPFIGURE_BUYGOODS, JUMPFIGURE_UPGRADEWEAPON):
            iCnt = -dMsgInfo['Cost'] if 'Cost' in dMsgInfo else 0
        cl_snetwar.GS2CJumpFigure(oListener, iSource, iTarget, iCnt)


def EventCBAddTargetCash(oListener, oEventCB, iAdd, iJumpFigure, iSource, iCnt, iIsBlockMsg):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            EventCBAddCash(oTarget, oEventCB, iAdd, iJumpFigure, iSource, iCnt, iIsBlockMsg)
    


def CommonAddWarCashByReason(oTarget, oEventCB, iCash, sReason, sExcReason, iJumpFigure):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = GetCommonEventKey(dEventInfo)
    if sReason:
        for strReason in sReason.split(';'):
            if strReason not in dMsgInfo['Reason']:
                return None
        
    if sExcReason:
        for strReason in sExcReason.split(';'):
            if strReason in dMsgInfo['Reason']:
                return None
        
    if 'NewRelic' in dMsgInfo:
        iSID = dMsgInfo['NewRelic']
        clsRelic = cl_perform.GetPerformModule(iSID)
        if clsRelic and clsRelic.m_RelicType == RELIC_TYPE_CURSE:
            return None
    iCash = cl_formula.GetResultByData(oTarget, iCash, dEventInfo, dMsgInfo)
    oTarget.AddCash(iCash, sKey, iSendMsg = 1, iLog = 0)
    if iJumpFigure and dMsgInfo.get('MSG', 0) == cl_msgcenter.MSG_WAR_ADDRELIC:
        cl_snetwar.GS2CJumpFigure(oTarget, JUMPFIGURE_RELIC, 0, iCash)


def EventCBChangeGetCash(oListener, oEventCB, iMul, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Cash' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iCash = dMsgInfo['Cash']
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iCash += iCash * iMul // 10000 + iAdd
    dMsgInfo['Cash'] = iCash


def EventCBSetMonsterStatePolicy(oListener, oEventCB, sName, dState):
    if oListener.m_Agent:
        oListener.m_Agent.SetData('StatePolicy%s' % sName, dState)


def EventCBPushHeroTarget(oListener, oEventCB, fSpeed, fMaxDis, fDownSpeed = 0, fGravaty = 9.8, iForceAngle = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    vStart = oListener.GetPos()
    if iForceAngle and oListener.m_MoveCtrl and oListener.m_MoveCtrl.m_ArriveInfo:
        vPathEnd = oListener.m_MoveCtrl.m_ArriveInfo[1]
        vMoveDir = cl_math.Vec3Minus(vPathEnd, vStart)
    else:
        vMoveDir = None
    fSecondOut = fMaxDis / fSpeed
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not (oTarget.m_MoveCtrl):
            continue
        if oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            continue
        vTar = oTarget.GetPos()
        vDir = cl_math.Vec3Minus(vTar, vStart)
        if vMoveDir and not cl_math.CheckVector2Angle(vMoveDir, vDir, iForceAngle):
            iAngle = iForceAngle if cl_math.VectorCross2D(vDir, vMoveDir) < 0 else -iForceAngle
            vNerTar = cl_math.Vec3DestPosDirPlane(vStart, vMoveDir, 1, iAngle)
            vDir = cl_math.Vec3Minus(vNerTar, vStart)
        oTarget.m_MoveCtrl.PushMove(oTarget, vDir, fSpeed, fSecondOut, fDownSpeed, fGravaty)
    


def EventCBPushMonsterTarget(oListener, oEventCB, fSpeed, fMaxDis, sStartTarget):
    if not oListener.m_Game:
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    if sStartTarget == 'StateAttacker':
        dEventInfo = oEventCB.GetCBEventInfo()
        iStateID = dEventInfo['StateID']
        oState = oListener.m_State.GetItem(iStateID)
        if not oState:
            return None
        oAttacker = oGame.GetObject(oState.m_Attacker)
        if not oAttacker:
            return None
        vStart = oAttacker.GetPos()
    else:
        vStart = oListener.GetPos()
    fSecondOut = fMaxDis / fSpeed
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not (oTarget.m_MoveCtrl):
            continue
        if oTarget.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            continue
        iPush = oTarget.GetKnockedBack({ }, 10000)
        if iPush:
            vTar = oTarget.GetPos()
            vDir = cl_math.Vec3Minus(vTar, vStart)
            oTarget.m_MoveCtrl.PushMove(oTarget, vDir, fSpeed, fSecondOut)
    


def EventCBAddEleAbnormalTrigger(oListener, oEventCB, iDamType, iProb, iReplace = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iDamType = cl_formula.GetResultByData(oListener, iDamType, dEventInfo, dMsgInfo)
    iProb = cl_formula.GetResultByData(oListener, iProb, dEventInfo, dMsgInfo)
    lstMainDam = dMsgInfo['MainDam']
    for idx, (iDam, oReason) in enumerate(lstMainDam):
        lstExt = oReason.Query('ExtEleAbnormal', [])
        lstExt.append({
            'DamType': iDamType,
            'Prob': iProb,
            'Replace': iReplace })
        oNewReason = oReason.ExtInfo({
            'ExtEleAbnormal': lstExt })
        iDam = lstMainDam[idx][0]
        lstMainDam[idx] = [
            iDam,
            oNewReason]
    


def EventCBChangeMiniGameTimesCal(oWarrior, oEventCB, iRatioMul, iRatioAdd, iTimesMul, iTimesAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Ratio' not in dMsgInfo or 'OriTimes' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iRatioMul = cl_formula.GetResultByData(oWarrior, iRatioMul, dEventInfo, dMsgInfo)
    iRatioAdd = cl_formula.GetResultByData(oWarrior, iRatioAdd, dEventInfo, dMsgInfo)
    iTimesMul = cl_formula.GetResultByData(oWarrior, iTimesMul, dEventInfo, dMsgInfo)
    iTimesAdd = cl_formula.GetResultByData(oWarrior, iTimesAdd, dEventInfo, dMsgInfo)
    iRatio = dMsgInfo['Ratio']
    iOriTimes = dMsgInfo['OriTimes']
    iRatio += iRatio * iRatioMul // 10000 + iRatioAdd
    iOriTimes += iOriTimes * iTimesMul // 10000 + iTimesAdd
    dMsgInfo['Ratio'] = iRatio
    dMsgInfo['OriTimes'] = iOriTimes


def EventCBChangeMiniGameInfo(oListener, oEventCB, iRewardSID, iRatioMul, iRatioAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iType = dMsgInfo['MiniGame']
    if iType == MG_EQUIP:
        OnChangeEquipMiniGameRatio(dMsgInfo, iRewardSID, iRatioMul, iRatioAdd)
    elif iType == MG_BULLET:
        OnChangeBulletMiniGameRatio(dMsgInfo, iRewardSID, iRatioMul, iRatioAdd)


def OnChangeEquipMiniGameRatio(dMsgInfo, iRewardSID, iRatioMul, iRatioAdd):
    dChooseWeight = dMsgInfo['ChooseWeight']
    if iRewardSID not in dChooseWeight:
        return None
    iRatio = dChooseWeight[iRewardSID]
    iRatio += iRatio * iRatioMul // 10000 + iRatioAdd
    dChooseWeight[iRewardSID] = iRatio


def OnChangeBulletMiniGameRatio(dMsgInfo, iRewardSID, iRatioMul, iRatioAdd):
    dChooseWeight = dMsgInfo['ChooseWeight']
    dBulletBag = dMsgInfo['ExtInfo']
    for idx, dInfo in dBulletBag:
        if iRewardSID not in dInfo:
            continue
        iRatio = dChooseWeight[idx]
        iRatio += iRatio * iRatioMul // 10000 + iRatioAdd
        dChooseWeight[idx] = iRatio
    


def EventCBChangeRelicDropProb(oListener, oEventCB, iDropID, iRatioMul, iRatioAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iDropID not in dMsgInfo:
        return None
    iRatio = dMsgInfo[iDropID]
    iRatio = iRatio * iRatioMul + iRatioAdd
    dMsgInfo[iDropID] = iRatio


def EventCBAddMainWeaponFactorElement(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iItemID = dEventInfo['ItemID']
    if not iItemID and 'Skill' in dMsgInfo:
        iItemID = dMsgInfo['Skill'].m_Base['Weapon']
    if not iItemID:
        return None
    lstWeapon = oListener.m_WieldCon.GetAllItemByType(itemdef.EQUIP_TYPE_MAINWEAPON)
    lstElement = []
    for oWeapon in lstWeapon:
        if iItemID == oWeapon.m_ID:
            continue
        lstElement.append(oWeapon.m_ElementType)
    
    oSkill = dMsgInfo['Skill']
    oSkill.m_Custom['ExtraFactorElement'] = lstElement


def EventCBChangeLuckyHit(oListener, oEventCB, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LuckyHit' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dMsgInfo['LuckyHit'] += iAdd


def EventCBDropWeaponBullet(oListener, oEventCB, iAmount, iUseNoDistanceBullet = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    else:
        iWeapon = 0
    if 'VID' not in dMsgInfo and 'CurVID' not in dMsgInfo:
        return None
    if not iWeapon:
        return None
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = GetCommonEventKey(dEventInfo)
    iAmount = cl_formula.GetResultByData(oListener, iAmount, dEventInfo, dMsgInfo)
    lstDropInfo = [
        {
            oWeapon.GetBulletType(): iAmount }]
    iVictim = dMsgInfo['VID'] if 'VID' in dMsgInfo else dMsgInfo['CurVID']
    oVictim = oListener.m_Game.GetObject(iVictim)
    if not oVictim:
        return None
    vPos = cl_reward.GetDropBasePos(oVictim)
    if iUseNoDistanceBullet:
        iDropType = NWARRIOR_DROP_NODISTANCEBULLET
    else:
        iDropType = NWARRIOR_DROP_BULLET
    dReward = {
        'item': VIRTUAL_ITEM_DROP,
        'info': {
            'DropType': iDropType,
            'DropInfo': lstDropInfo,
            'DropPos': vPos } }
    cl_reward.RewardItem(oListener.m_Game, oListener, [
        dReward], sKey, {
        'Player': oListener.m_ID })


def EventCBDropTreasureDeadDrop(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo:
        return None
    oVictim = oListener.m_Game.GetObject(dMsgInfo['VID'])
    if not oVictim:
        return None
    vPos = cl_reward.GetDropBasePos(oVictim)
    lstDropInfo = [
        {
            'Hero': oListener,
            'DropPos': vPos,
            'Delaytime': 0 }]
    oVictim.m_Game.GetResMgr().CreateDrop(oVictim.m_Scene, NWARRIOR_DROP_TREASURE_DEAD, vPos, lstDropInfo, { })


def EventCBTargetPosCreateDrop(oListener, oEventCB, iDropType, iCnt, iDropNum = 1, iOnlyRewardSelf = 0, iSplitCnt = 0, iDisplace = 0):
    dTrans = oEventCB.GetCBTransInfo()
    sKey = oEventCB.m_Key
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    if iDropType not in [
        NWARRIOR_DROP_CASH,
        NWARRIOR_DROP_GSCASH]:
        SendAlert('err', '%s回调在目标位置掉落只支持铜币或者精魄掉落' % sKey)
        return None
    oGame = oListener.m_Game
    if not iOnlyRewardSelf:
        lstHero = oGame.m_WarMgr.GetLiveHero()
    elif oListener.m_FightType & WARRIOR_HERO:
        lstHero = [
            oListener.m_ID]
    else:
        SendAlert('err', '%s回调在目标位置掉落给予非英雄单位奖励' % sKey)
        return None
    iMaxCnt = 20
    if iDropNum > iMaxCnt:
        SendAlert('err', '%s回调在目标位置掉落 掉落数量配置 %d 超出保底上限 %d，有需求请联系程序' % (sKey, iDropNum, iMaxCnt))
        iDropNum = iMaxCnt
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        iTrueCnt = cl_formula.GetResultByData(oTarget, iCnt, dEventInfo, dMsgInfo)
        if iDisplace:
            vDir = oTarget.GetFacing()
            vDir = [
                vDir[0],
                0,
                vDir[2]]
            vPos = cl_math.Vec3DisplaceDir(oTarget.GetPos(), vDir, iDisplace)
        else:
            vPos = cl_reward.GetDropBasePos(oTarget)
        if iSplitCnt:
            lstReward = []
            iLoopCnt = (iTrueCnt + iSplitCnt - 1) // iSplitCnt
            if iLoopCnt > iMaxCnt:
                SendAlert('err', '%s回调在目标位置掉落 %d 拆分掉落物后数量 %d 超出保底上限 %d，有需求请联系程序' % (sKey, iTrueCnt, iLoopCnt, iMaxCnt))
                iLoopCnt = iMaxCnt
                iSplitCnt = (iTrueCnt + iLoopCnt - 1) // iLoopCnt
            for _ in range(iLoopCnt):
                iCash = iSplitCnt if iTrueCnt > iSplitCnt else iTrueCnt
                iTrueCnt -= iSplitCnt
                dCash = {
                    'Cash': iCash } if iDropType == NWARRIOR_DROP_CASH else {
                    'GSCash': iCash }
                lstDropInfo = [
                    dCash]
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': iDropType,
                        'DropInfo': lstDropInfo,
                        'DropPos': vPos } }
                lstReward.append(dReward)
            
        elif iDropType == NWARRIOR_DROP_CASH:
            pass
        
        dCash = {
            'GSCash': iTrueCnt }
        lstDropInfo = [
            dCash]
        dReward = {
            'item': VIRTUAL_ITEM_DROP,
            'info': {
                'DropType': iDropType,
                'DropInfo': lstDropInfo,
                'DropPos': vPos } }
        lstReward = [ dReward for _ in range(iDropNum) ]
        for iHero in lstHero:
            cl_reward.RewardItem(oGame, oTarget, lstReward, sKey, {
                'Player': iHero })
        
    


def EventCBRecordSkillCollectTarget(oListener, oEventCB, sKey, iCurCartoon = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s回调记录技能统计事件目标 事件未获取目标' % oEventCB.m_Key)
        return None
    oSkill = dMsgInfo['Skill']
    oGame = oListener.m_Game
    if iCurCartoon:
        dTarget = oSkill.m_Update.setdefault(sKey, { })
    else:
        dTarget = oSkill.m_Collect.setdefault(sKey, { })
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        dTarget[iTarget] = 1
    


def EventCBGetSkillCollectTargetNum(oListener, oEventCB, sKey, iCurCartoon):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if iCurCartoon:
        dTarget = oSkill.m_Update.get(sKey, { })
    else:
        dTarget = oSkill.m_Collect.get(sKey, { })
    return len(dTarget)


def EventCBGetThrowChangeNumTypeByRatio(oListener, oEventCB, iCheckRatio):
    oPerform = oListener.GetThrowPerform()
    if not oPerform:
        return TYPE_THROWRATIONNUMCHANG_DEFAULT
    iBulletSID = oPerform.CalAttr('BulletSID')
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SID' not in dMsgInfo or 'Amount' not in dMsgInfo:
        return TYPE_THROWRATIONNUMCHANG_DEFAULT
    if iBulletSID != dMsgInfo['SID']:
        return TYPE_THROWRATIONNUMCHANG_DEFAULT
    oBulletCon = oListener.m_BulletCon
    iMaxBullet = oBulletCon.GetMaxBullet(iBulletSID)
    iCurBullet = oBulletCon.Bullet(iBulletSID)
    iCheckNum = iMaxBullet * iCheckRatio
    iAmount = dMsgInfo['Amount']
    iPreCostNum = iCurBullet - iAmount
    if iPreCostNum <= iCheckNum:
        if iCurBullet > iCheckNum:
            return TYPE_THROWRATIONNUMCHANG_ADD
        return TYPE_THROWRATIONNUMCHANG_DEFAULT
    if iCurBullet <= iCheckNum:
        return TYPE_THROWRATIONNUMCHANG_SUB
    return TYPE_THROWRATIONNUMCHANG_DEFAULT


def EventCBGetTotalHPChangeByCureRatio(oListener, oEventCB, iExtraCureRatio):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iResultChange = 0
    if 'CureInfo' in dMsgInfo and 'TotalCure' in dMsgInfo:
        iTotalChange = 0
        for iChange, _ in dMsgInfo['CureInfo']:
            iTotalChange += iChange
        
        iRealCure = sum(dMsgInfo['TotalCure'])
        if iRealCure < iTotalChange:
            iResultChange += (iTotalChange - iRealCure) * iExtraCureRatio
        iResultChange += iRealCure
    elif 'TrueChange' in dMsgInfo:
        for iChange, _ in dMsgInfo['TrueChange']:
            iResultChange += iChange
        
    return iResultChange


def EventCBRemoveSelfFromTarget(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstNewTar = []
    for iTarget in dTrans['TargetList']:
        if iTarget != oListener.m_ID:
            lstNewTar.append(iTarget)
    
    dTrans['TargetList'] = lstNewTar


def EventCBGetSkillCacheAttr(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    if sKey not in oSkill.m_Collect:
        return 0
    return oSkill.m_Collect[sKey]


def EventCBRecordTriggerCartoon(oListener, oEventCB, iMax):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dCartoon = oSkill.GetCurCartoon()
        if not dCartoon:
            return None
        iCartoon = dCartoon['ID'] if 'ID' in dCartoon else 0
        dTriggerCartoon = oSkill.m_Collect.setdefault('TriggerCartoon', { })
        iOld = dTriggerCartoon[iCartoon] if iCartoon in dTriggerCartoon else 0
        dTriggerCartoon[iCartoon] = min(iMax, iOld + 1)


def EventCBRecordHitCartoon(oListener, oEventCB, iAddExtInfo = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dCartoon = oSkill.GetCurCartoon()
        if not dCartoon:
            return None
        sAttr = 'HitCartoon'
        if iAddExtInfo:
            sAttr = '%s%s' % (oEventCB.m_Key, sAttr)
        dEventHit = oSkill.m_Collect.setdefault(sAttr, { })
        dHitCartoon = dEventHit.setdefault(oEventCB.Key(), { })
        iCartoon = dCartoon['ID'] if 'ID' in dCartoon else 0
        dHitCartoon[iCartoon] = 1


def _EventCBRecoverBullet(oListener, oEventCB, iReconverNum, iClientBehavior):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iSend = 1
    if 'PFType' in dEventInfo and dEventInfo['PFType'] == PF_TYPE_BULLETCHANGE:
        iSend = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
        oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return None
        iAdd = oBulletCom.BulletModify(iReconverNum, iSend)
        iRest = iReconverNum - iAdd
        if iRest:
            sKey = GetCommonEventKey(oEventCB.GetCBEventInfo())
            oListener.m_BulletCon.BulletModify(oBulletCom.BulletType(), iRest, sKey)
    if iClientBehavior:
        cl_snetwar.GS2CTriggerBehavior(oListener.m_Game, oListener.m_ID, iClientBehavior, [
            oListener.m_PlayerID], 0)


def EventCBRecoverBulletByMishitCartoon(oListener, oEventCB, iPerNum, iClientBehavior):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dHitCollect = oSkill.m_Collect['HitCartoon'] if 'HitCartoon' in oSkill.m_Collect else { }
        sKey = oEventCB.Key()
        dHitCartoon = dHitCollect[sKey] if sKey in dHitCollect else { }
        iHitCartoon = len(dHitCartoon)
        iTotal = cl_action.GetTrajectory(oSkill)
        iMishit = iTotal - iHitCartoon
        if iMishit <= 0 or iPerNum < 1:
            return None
        _EventCBRecoverBullet(oListener, oEventCB, iPerNum * iMishit, iClientBehavior)


def EventCBRecoverBulletByMishitBullet(oListener, oEventCB, iBulletNum, iClientBehavior):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dHitCollect = oSkill.m_Collect['HitCartoon'] if 'HitCartoon' in oSkill.m_Collect else { }
        sKey = oEventCB.Key()
        dHitCartoon = dHitCollect[sKey] if sKey in dHitCollect else { }
        iHitCartoon = len(dHitCartoon)
        if iHitCartoon == 0:
            iBulletNum = cl_formula.GetResultByData(oListener, iBulletNum, dEventInfo, dMsgInfo)
            _EventCBRecoverBullet(oListener, oEventCB, iBulletNum, iClientBehavior)


def EventCBUpdateSpreadAbnormalDam(oListener, oEventCB, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'StateInfo' in dMsgInfo:
        dState = dMsgInfo['StateInfo']
    elif 'StateID' not in dMsgInfo:
        return None
    iVictim = dMsgInfo['VID']
    iState = dMsgInfo['StateID']
    if iVictim == oListener.m_ID:
        oTarget = oListener
    else:
        oTarget = oListener.m_Game.GetObject(iVictim)
    oState = oTarget.m_State.GetItem(iState)
    if not oState:
        return None
    dState = oState.m_StateInfo
    if 'arg' not in dState or 'AbnormalSourceDam' not in dState['arg']:
        return None
    iDam = dState['arg']['AbnormalSourceDam']
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    dState['arg']['AbnormalSourceDam'] = iDam * (10000 + iMul) // 10000 + iAdd


def EventCBSetTargetStateCount(oListener, oEventCB, iStateSID, iCount, iFromSelf = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iFormulaCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if not iFromSelf:
            oState = oTarget.m_State.GetItemBySID(iStateSID)
            if oState:
                iNowCount = oState.GetCount()
                iAddCount = iFormulaCount - iNowCount
                oState.AddCount(oTarget, iAddCount)
                continue
        lstState = oTarget.m_State.GetItems(iStateSID)
        for oState in lstState:
            if oState.m_Attacker != oListener.m_ID:
                continue
            iNowCount = oState.GetCount()
            iAddCount = iFormulaCount - iNowCount
            oState.AddCount(oTarget, iAddCount)
        
    


def EventCBGetTargetStateCount(oListener, oEventCB, iState, iFromSelf = 0, iFromSameItem = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if iFromSelf or iFromSameItem:
        iStateOwner = oListener.m_ID if iFromSelf else 0
        dEventInfo = oEventCB.GetCBEventInfo()
        iItem = dEventInfo['ItemID'] if iFromSameItem else 0
        oState = oTarget.m_State.GetStateBySource(iState, iStateOwner, iItem)
        if not oState:
            return 0
        return oState.GetCount()
    oState = oTarget.m_State.GetItemBySID(iState)
    if not oState:
        return 0
    return oState.GetCount()


def EventCBSetTargetStateMaxCount(oListener, oEventCB, iStateSID, iCount, iCalByListener = 0, iFromSameItem = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    if iCalByListener:
        iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iFromSameItem:
            iItem = dEventInfo['ItemID'] if 'ItemID' in dEventInfo else 0
            oState = oTarget.m_State.GetStateBySource(iStateSID, 0, iItem)
        else:
            oState = oTarget.m_State.GetItemBySID(iStateSID)
        if oState:
            iFormulaCount = cl_formula.GetResultByData(oTarget, iCount, dEventInfo, dMsgInfo)
            oState.SetMaxCount(oTarget, iFormulaCount)
    


def EventCBSetTargetStateMinCount(oListener, oEventCB, iStateSID, iCount):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if oState:
            iFormulaCount = cl_formula.GetResultByData(oTarget, iCount, dEventInfo, dMsgInfo)
            oState.SetMinCount(oTarget, iFormulaCount)
    


def EventCBAddTargetStateMaxCount(oListener, oEventCB, iStateSID, iCount):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iFormulaCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if oState:
            oState.SetMaxCount(oTarget, iFormulaCount + oState.m_MaxCount)
    


def EventCBAddTargetStateCount(oListener, oEventCB, iStateSID, iAdd, iFromSelf = 0, iFromSameItem = 0, iTime = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iAddCount = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iTime:
        iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
        iFrame = Time2Frame(iTime)
    else:
        iFrame = 0
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iFromSelf or iFromSameItem:
            lstState = oTarget.m_State.GetItems(iStateSID)
            for oState in lstState:
                if iFromSelf and oState.m_Attacker != oListener.m_ID:
                    continue
                if iFromSameItem and dEventInfo['ItemID'] != oState.m_Item:
                    continue
                oState.AddCount(oTarget, iAddCount, iFrame)
            
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if oState:
            oState.AddCount(oTarget, iAddCount, iFrame)
    


def EventCBDoneEvent(oListener, oEventCB, iMsg, iSub):
    cl_msgcenter.DoneEvent(oListener, iMsg, GetCommonEventKey(oEventCB.GetCBEventInfo()), iSub)


def EventCBRemoveRelic(oListener, oEventCB, iRelic, iNotify = 0):
    oListener.m_RelicCon.RemoveRelic(iRelic, 'eventRemoveRelic', 1)
    if iNotify:
        lstPlayer = [
            oListener.m_PlayerID]
        sName = cl_perform.GetPerformClassAttr(iRelic, 'm_Name')
        cl_notify.SendCommonNotify(oListener.m_Game, lstPlayer, 2418, {
            '$name': sName })


def EventCBChangeRelicShareStatus(oListener, oEventCB, iShare):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'StaticInfo' not in dMsgInfo or 'Share' not in dMsgInfo['StaticInfo']:
        return None
    dMsgInfo['StaticInfo']['Share'] = iShare


def EventCBTargetDeath(oListener, oEventCB, iExecuteType):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if not oTarget.QueryBitAttr('LogicKey') & FIGHT3_KEY_IGNELBEEXECUTED:
            oTarget.AddExecuteType(iExecuteType)
    


def EventCBImmuneDamageByType(oListener, oEventCB, iImmuneDamType, iShowType = IMMUNITY_SHOWCAST):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sDamKey in ('MainDam', 'FlowDam'):
        if sDamKey not in dMsgInfo:
            continue
        lstNewDam = []
        for iDam, oReason in dMsgInfo[sDamKey]:
            iDamType = oReason.Query('DamType', 0)
            if iDamType & DAM_MASK_ELEMENT & iImmuneDamType == 0:
                lstNewDam.append((iDam, oReason))
        
        dMsgInfo[sDamKey] = lstNewDam
    
    dMsgInfo['ShowType'] = iShowType


def GetExtInfoKey(oEventCB, sKey):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    return '%s-%s' % (oLifeCycle.Key(), sKey)


def EventCBRecordMoveDis(oListener, oEventCB, sBaseKey, iObjectType = 0, iAddExtInfo = 0):
    if iObjectType is None:
        iObjectType = 0
    oWarrior = oListener.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    sKey = 'MoveDis%s' % sBaseKey
    if iAddExtInfo:
        sKey = GetExtInfoKey(oEventCB, sKey)
    vNow = oWarrior.GetPos()
    tLast = oWarrior.Query(sKey, None)
    if tLast:
        (vLast, fLastDis) = tLast
        fNewDis = cl_math.CalDistance(vLast, vNow) + fLastDis
    else:
        fNewDis = 0
    oWarrior.Set(sKey, (vNow, fNewDis))


def EventCBUpdateMovePos(oListener, oEventCB, sBaseKey, iObjectType = 0, iAddExtInfo = 0):
    oWarrior = oListener.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    sKey = 'MoveDis%s' % sBaseKey
    if iAddExtInfo:
        sKey = GetExtInfoKey(oEventCB, sKey)
    vNow = oWarrior.GetPos()
    tLast = oWarrior.Query(sKey, None)
    if tLast:
        (_, fLastDis) = tLast
    else:
        fLastDis = 0
    oWarrior.Set(sKey, (vNow, fLastDis))


def EventCBResetMoveDis(oListener, oEventCB, sBaseKey, iObjectType = 0, iInitValue = 0, iAddExtInfo = 0):
    if iObjectType is None:
        iObjectType = 0
        iInitValue = 0
    oWarrior = oListener.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    sKey = 'MoveDis%s' % sBaseKey
    if iAddExtInfo:
        sKey = GetExtInfoKey(oEventCB, sKey)
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iInitValue = cl_formula.GetResultByData(oListener, iInitValue, dEventInfo, dMsgInfo)
    oWarrior.Set(sKey, (oWarrior.GetPos(), iInitValue))


def EventCBGetMoveDis(oListener, oEventCB, sBaseKey, iObjectType, iAddExtInfo = 0):
    oWarrior = oListener.GetOwnObject(iObjectType)
    if not oWarrior:
        return 0
    sKey = 'MoveDis%s' % sBaseKey
    if iAddExtInfo:
        sKey = GetExtInfoKey(oEventCB, sKey)
    (_, fDis) = oWarrior.Query(sKey, (0, 0))
    return int(fDis)


def EventCBRecordCurPos(oListener, oEventCB, sBaseKey):
    sKey = 'CurPos%s' % sBaseKey
    oListener.Set(sKey, oListener.GetPos())


def EventCBGetRecordPos(oListener, oEventCB, sBaseKey):
    sKey = 'CurPos%s' % sBaseKey
    return oListener.Query(sKey, None)


def EventCBGetDistance(oListener, oEventCB, sBaseKey):
    sKey = 'CurPos%s' % sBaseKey
    vTargetPos = oListener.Query(sKey, None)
    if vTargetPos:
        return round(cl_math.CalDistance(vTargetPos, oListener.GetPos()))
    return 0


def EventCBGetTargetPos(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return (0, 0, 0)
    lstTar = dTrans['TargetList']
    if lstTar:
        iTarget = lstTar[0]
        oTarget = oListener.m_Game.GetObject(iTarget)
        if oTarget:
            return oTarget.GetPos()
    return (0, 0, 0)


def EventCBGetCurPos(oListener, oEventCB):
    return oListener.GetPos()


def EventCBChangePerformDamType(oListener, oEventCB, iPerform, iDamType):
    
    def ClearChangePerformDamType(oListener, oCommonObj):
        oChangePerform = oListener.GetPerform(iPerform)
        if not oChangePerform:
            return None
        sKey = oLifeCycle.Key()
        oChangePerform.m_ElementTypeObj.RemoveSetModify(sKey)

    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    oChangePerform = oListener.GetPerform(iPerform)
    if not oChangePerform:
        return None
    oChangePerform.m_ElementTypeObj.SetModify(sKey, iDamType)
    oLifeCycle.AddDisableFunc(ClearChangePerformDamType)


def EventCBAddSceneEvent(oListener, oEventCB, iTime, iShape, dEffArgs, iYOffset, iEnterGroup, iLeaveGroup, iIsDisableClear):
    
    def ClearSceneEvt(oGame, iScene):
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oScene.RemoveSceneEvent(iSceneEvtID)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEvent = oEventCB.GetCBEventInfo()
    for sAttr, oValue in dEffArgs.items():
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iValue = cl_formula.GetResultByData(oListener, oValue, oEventCB.GetCBEventInfo(), dMsgInfo)
        dEffArgs[sAttr] = iValue
    
    dData = {
        'AID': oListener.m_ID }
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        dData['RS'] = oSkill.m_Base['RS']
        dData.update(oSkill.m_Cache)
    else:
        dData['RS'] = dEvent['RS']
    dTrans = oEventCB.GetCBTransInfo()
    vEPFPos = dTrans['EPFPos'] if 'EPFPos' in dTrans else oListener.GetPos()
    (x, y, z) = vEPFPos
    y += iYOffset
    if iShape == SCENE_EVT_SHAPE_SPHERE:
        lstArgs = [
            (x, y, z),
            dEffArgs['Radius']]
    elif iShape == SCENE_EVT_SHAPE_RECTANGLE:
        lstArgs = [
            (x, y, z),
            (dEffArgs['HalfX'], dEffArgs['HalfY'], dEffArgs['HalfZ'])]
    else:
        return None
    oGame = oListener.m_Game
    iScene = oListener.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    (enterfunc, leavefunc) = (None, None)
    if iEnterGroup:
        enterfunc = Functor(cl_action.CommmonEventCBFunc, oEventCB, iEnterGroup, dEvent)
    if iLeaveGroup:
        leavefunc = Functor(cl_action.CommmonEventCBFunc, oEventCB, iLeaveGroup, dEvent)
    iSceneEvtID = oScene.AddSceneEvent(oListener, enterfunc, leavefunc, iShape, lstArgs, dData)
    if iTime:
        oGame.m_Timer.Call_Out(Functor(ClearSceneEvt, oGame, iScene), Time2Frame(iTime), 'EventCBClearSceneEvt')
    oLifeCycle = dEvent['LifeCycle']
    if iIsDisableClear:
        oLifeCycle.AddDisableType(DISABLE_TYPE_SCENEEVENT, iScene, iSceneEvtID)


def EventCBAddEvent(oListener, oEventCB, iTime, iShape, dEffArgs, iEnterGroup, iLeaveGroup, iIsDisableClear, iLayer = PXLAYER_EBULLET):
    
    def ClearFunc(oEvent, oListener, oLifeCycle):
        oListener.Delete(sKey)
        oEvent.Unstall()

    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEvent = oEventCB.GetCBEventInfo()
    oGame = oListener.m_Game
    for sAttr, oValue in dEffArgs.items():
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iValue = cl_formula.GetResultByData(oListener, oValue, oEventCB.GetCBEventInfo(), dMsgInfo)
        dEffArgs[sAttr] = iValue
    
    if iShape == SCENE_EVT_SHAPE_SPHERE:
        dArgs = {
            'Shape': MODEL_TYPE_SPHERE,
            'Radius': dEffArgs['Radius'] }
    elif iShape == SCENE_EVT_SHAPE_RECTANGLE:
        dArgs = {
            'Shape': MODEL_TYPE_BOX,
            'HalfExt': (dEffArgs['HalfX'], dEffArgs['HalfY'], dEffArgs['HalfZ']) }
    else:
        return None
    (enterfunc, leavefunc) = (None, None)
    if iEnterGroup is not None:
        enterfunc = Functor(cl_action.CommmonEventCBFunc, oEventCB, iEnterGroup, dEvent)
    if iLeaveGroup is not None:
        leavefunc = Functor(cl_action.CommmonEventCBFunc, oEventCB, iLeaveGroup, dEvent)
    oEvent = cl_engphyobj.CreateTraceEvent(oGame, oListener, {
        'TraceIdx': oEventCB.Key(),
        'PassID': oListener.m_ID }, iLayer, dArgs, (enterfunc, leavefunc))
    sKey = 'AreaEvent-%s' % oEventCB.m_Key
    oOldEvent = oListener.Query(sKey, None)
    if oOldEvent:
        oOldEvent.Unstall()
    oListener.Set(sKey, oEvent)
    oLifeCycle = dEvent['LifeCycle']
    if iTime:
        oGame.m_Timer.Call_Out(Functor(ClearFunc, oEvent, oListener, oLifeCycle), Time2Frame(iTime), 'EventCBClearEvt')
    if iIsDisableClear:
        oFunc = Functor(ClearFunc, oEvent)
        oLifeCycle.AddDisableFunc(oFunc)


def EventCBAddUnlockProgress(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'UnlockProgress' not in dEventInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oListener.m_UnlockProgressCon.AddProgress(dEventInfo['UnlockProgress'], iAdd, dMsgInfo)


def EventCBAddGSCashByCash(oListener, oEventCB, iThreshold, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Cash' not in dMsgInfo:
        return None
    iCash = dMsgInfo['Cash']
    if iCash <= 0:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'pfid' in dEventInfo:
        sKey = 'gscashbycash%d' % dEventInfo['pfid']
    elif 'StateSID' in dEventInfo:
        sKey = 'gscashbycash%d' % dEventInfo['StateSID']
    else:
        return None
    iLastUnSettled = oListener.QuerySavedData(sKey, 0)
    iAll = iLastUnSettled + iCash
    iAmount = iAll // iThreshold
    iUnSettled = iAll - iAmount * iThreshold
    oListener.SetSavedData(sKey, iUnSettled)
    oListener.AddGSCash(iAmount * iAdd, sKey)


def EventCBSummonAreaMonster(oListener, oEventCB, iGroup, dAreaWeight, dNumWeight, iDelay, iLimitExtAmount = -1):
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLineNode = oLevelCtrl.GetLineNode(oListener.m_LineIdx)
    if not oLineNode:
        return None
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    tParam = (iGroup, dAreaWeight, dNumWeight, iDelay, iLimitExtAmount)
    oMonsterCtrl.AddSpawnInfo(tParam)
    oMonsterCtrl.StartSpawn(tParam, Owner = oListener.m_ID)


def EventCBAppointSummonAreaMonster(oListener, oEventCB, iGroup, dAreaWeight, iNum, iDelay, iLimitExtAmount, iIsolate):
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLineNode = oLevelCtrl.GetLineNode(oListener.m_LineIdx)
    if not oLineNode:
        return None
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, oEventCB.GetCBEventInfo(), dMsgInfo)
    if iIsolate:
        lstArea = ChooseMulKeys(oGame, dAreaWeight, iNum)
        for iArea in lstArea:
            tParam = (iGroup, {
                iArea: 10 }, {
                1: 10 }, iDelay, iLimitExtAmount)
            oMonsterCtrl.AddSpawnInfo(tParam)
            oMonsterCtrl.StartSpawn(tParam, Owner = oListener.m_ID)
        
    else:
        tParam = (iGroup, dAreaWeight, {
            iNum: 10 }, iDelay, iLimitExtAmount)
        oMonsterCtrl.AddSpawnInfo(tParam)
        oMonsterCtrl.StartSpawn(tParam, Owner = oListener.m_ID)


def EventCBStartClientSkill(oListener, oEventCB, iPerform, sKey = '', iTriggerHitPos = 0, iIgnoreItem = 0, dArgInfo = None):
    oGame = oListener.m_Game
    iWeapon = 0
    dEventInfo = oEventCB.GetCBEventInfo()
    if not iIgnoreItem:
        if 'ItemID' in dEventInfo:
            iWeapon = dEventInfo['ItemID']
        elif 'RS' in dEventInfo:
            iWeapon = dEventInfo['RS'].Query('Item')
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iPerform = cl_formula.GetResultByData(oListener, iPerform, dEventInfo, dMsgInfo)
    oPerform = oListener.GetPerform(iPerform, iWeapon)
    if not oPerform or oPerform.m_PFType != PF_TYPE_TRIGGERCLIENT or not (oPerform.m_Enable):
        return None
    if iTriggerHitPos:
        if 'CurVID' not in dMsgInfo:
            return None
        iVictim = dMsgInfo['CurVID']
        if 'CurHitPos' in dMsgInfo:
            vStart = dMsgInfo['CurHitPos']
        elif 'CurVID' in dMsgInfo:
            oVictim = oGame.GetObject(dMsgInfo['CurVID'])
            if not oVictim:
                return None
            vStart = oVictim.GetPos()
        else:
            return None
        dArgs = {
            'StartX': int(vStart[0] * 100),
            'StartY': int(vStart[1] * 100),
            'StartZ': int(vStart[2] * 100),
            'Target': iVictim }
    else:
        dArgs = { }
    if sKey:
        if 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        if 'ItemID' not in oSkill.m_Cache:
            return None
        dArgs[sKey] = oSkill.m_Cache['ItemID']
    if dArgInfo:
        dArgInfo = cl_formula.CalArgsFormula(oListener, dArgInfo, dEventInfo, dMsgInfo)
        dArgs.update(dArgInfo)
    oPerform.AddCanUseCount()
    cl_snetwar.GS2CNotifyStartSkill(oGame, oListener.m_PlayerID, iPerform, oPerform.m_ID, iWeapon, dArgs)


def EventCBStartThrowSkill(oListener, oEventCB, iPerform, iUseTarget = 0, dCustomData = None):
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.AddCanUseCount()
    dArgs = { }
    if iUseTarget:
        dTrans = oEventCB.GetCBTransInfo()
        if 'TargetList' not in dTrans or not dTrans['TargetList']:
            SendAlert('err', '%s事件回调未设置目标或目标为空' % oEventCB.m_Key)
            return None
        dArgs['Target'] = dTrans['TargetList'][0]
    if dCustomData:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        dEventInfo = oEventCB.GetCBEventInfo()
        for skey, iVal in dCustomData.items():
            iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
            dArgs[skey] = iVal
        
    cl_snetwar.GS2CNotifyStartSkill(oListener.m_Game, oListener.m_PlayerID, iPerform, oPerform.m_ID, 0, dArgs)


def EventCBAddSourceWeaponPFBullet(oListener, oEventCB, iPerform, iAdd, iMaxBulletSync = 0, iCalRecoverMul = 1):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'ItemID' in dEventInfo:
        iWeapon = dEventInfo['ItemID']
    elif 'RS' in dEventInfo:
        iWeapon = dEventInfo['RS'].Query('Item')
    else:
        return None
    oPerform = oListener.GetPerform(iPerform, iWeapon)
    if oPerform and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iAddCount = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
        oPerform.AddPFBullet(iAddCount, iMaxBulletSync = iMaxBulletSync, iCalRecoverMul = iCalRecoverMul)


def EventCBCostSourceWeaponPFBullet(oListener, oEventCB, iPerform, iCost):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'ItemID' in dEventInfo:
        iWeapon = dEventInfo['ItemID']
    elif 'RS' in dEventInfo:
        iWeapon = dEventInfo['RS'].Query('Item')
    else:
        return None
    oPerform = oListener.GetPerform(iPerform, iWeapon)
    if oPerform:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iCost = cl_formula.GetResultByData(oListener, iCost, dEventInfo, dMsgInfo)
        oPerform.CostPFBullet(iCost)


def EventCBSetSourceWeaponPFBullet(oListener, oEventCB, iPerform, iValue):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'ItemID' in dEventInfo:
        iWeapon = dEventInfo['ItemID']
    elif 'RS' in dEventInfo:
        iWeapon = dEventInfo['RS'].Query('Item')
    else:
        return None
    oPerform = oListener.GetPerform(iPerform, iWeapon)
    if oPerform and oPerform.m_PFType in (PF_TYPE_SHOOT, PF_TYPE_CONSHOOT, PF_TYPE_CHARGE):
        dMsgInfo = oEventCB.GetCBMsgInfo()
        oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
        dOtherArgs = {
            'Weapon': oWeapon }
        iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo, dOtherArgs)
        iMax = oPerform.MaxPFBullet()
        if iValue > iMax:
            iValue = iMax
        oPerform.m_CurPFBullet = iValue
        oPerform.RefreshCurPFBullet()


def EventCBReturnSourceWeaponPFBullet(oListener, oEventCB, iPointNum = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'pfid' not in dMsgInfo or 'ItemID' not in dMsgInfo:
        SendAlert('err', '%s技能专属子弹返还失败，需要监听消耗专属子弹消息' % oEventCB.m_Key)
        return None
    iWeapon = dMsgInfo['ItemID']
    oPerform = oListener.GetPerform(dMsgInfo['pfid'], iWeapon)
    if not oPerform:
        return None
    if not iPointNum:
        iReturn = dMsgInfo['RealCost'] if 'RealCost' in dMsgInfo else 0
    else:
        dEventInfo = oEventCB.GetCBEventInfo()
        iReturn = cl_formula.GetResultByData(oListener, iPointNum, dEventInfo, dMsgInfo)
    if iReturn:
        oPerform.AddPFBullet(iReturn)


def EventCBAddEventWeaponPFBullet(oListener, oEventCB, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    else:
        iWeapon = 0
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oPerform = oWeapon.GetPFBulletPerform()
    if oPerform:
        dEventInfo = oEventCB.GetCBEventInfo()
        iAddCount = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
        oPerform.AddPFBullet(iAddCount)


def EventCBCostEventWeaponPFBullet(oListener, oEventCB, iCost):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    else:
        iWeapon = 0
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oPerform = oWeapon.GetPFBulletPerform()
    if oPerform:
        dEventInfo = oEventCB.GetCBEventInfo()
        iCostCount = cl_formula.GetResultByData(oListener, iCost, dEventInfo, dMsgInfo)
        oPerform.CostPFBullet(iCostCount)


def EventCBAddWeaponPFBulletByHoldType(oListener, oEventCB, iHoldType, iAdd, iPercent = 0):
    lstWeapon = oListener.m_WieldCon.GetWeapons(iHoldType)
    if not lstWeapon:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for oWeapon in lstWeapon:
        oPerform = oWeapon.GetPFBulletPerform()
        if oPerform:
            iAddCount = 0
            if iAdd:
                iAddCount += cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
            if iPercent:
                iAddCount += oPerform.MaxPFBullet() * iPercent // 100
            oPerform.AddPFBullet(iAddCount)
    


def EventCBSetCanAddPFBulletByHoldType(oListener, oEventCB, iHoldType, iCanAdd):
    
    def ClearFunc(oListener, oLifeCycle):
        for iWeapon in lstClear:
            oItem = oListener.m_WieldCon.GetItemByID(iWeapon)
            if not oItem:
                continue
            oPerform = oItem.GetPFBulletPerform()
            if oPerform:
                oPerform.SetCanAddPFBullet(iOldValue)
        

    lstItem = oListener.m_WieldCon.GetWeapons(iHoldType)
    if not lstItem:
        return None
    lstClear = []
    for oItem in lstItem:
        oPerform = oItem.GetPFBulletPerform()
        if oPerform:
            dEventInfo = oEventCB.GetCBEventInfo()
            dMsgInfo = oEventCB.GetCBMsgInfo()
            iOldValue = oPerform.GetCanAddPFBullet()
            lstClear.append(oItem.m_ID)
            iCanAdd = cl_formula.GetResultByData(oListener, iCanAdd, dEventInfo, dMsgInfo)
            oPerform.SetCanAddPFBullet(iCanAdd)
            oLifeCycle = dEventInfo['LifeCycle']
            oLifeCycle.AddDisableFunc(ClearFunc)
    


def EventCBAddHoldWeaponComBullet(oListener, oEventCB, iAmount, iFlag):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstAdd = oListener.m_WieldCon.GetWeapons(iFlag)
    for oWeapon in lstAdd:
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        iTrueAmount = cl_formula.GetResultByData(oListener, iAmount, dEventInfo, dMsgInfo, {
            'Weapon': oWeapon })
        oBulletCom.BulletModify(iTrueAmount, 1)
    


def EventTargetAddHoldWeaponComBullet(oListener, oEventCB, iAmount, iFlag):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not (oTarget.m_FightType & WARRIOR_HERO):
            continue
        EventCBAddHoldWeaponComBullet(oTarget, oEventCB, iAmount, iFlag)
    


def EventCBAddHoldWeaponBagBullet(oListener, oEventCB, iAmount, iFlag):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstAdd = oListener.m_WieldCon.GetWeapons(iFlag)
    sKey = GetCommonEventKey(dEventInfo)
    for oWeapon in lstAdd:
        iAddAmount = cl_formula.GetResultByData(oListener, iAmount, dEventInfo, dMsgInfo, {
            'Weapon': oWeapon })
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return None
        iBulletSID = oBulletCom.BulletType()
        oListener.m_BulletCon.BulletModify(iBulletSID, iAddAmount, sKey)
    


def EventTargetAddHoldWeaponBagBullet(oListener, oEventCB, iAmount, iFlag):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget or not (oTarget.m_FightType & WARRIOR_HERO):
            continue
        EventCBAddHoldWeaponBagBullet(oTarget, oEventCB, iAmount, iFlag)
    


def EventCBPullTargetToPos(oListener, oEventCB, fSpeed, fMaxDis):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    oGame = oListener.m_Game
    vEnd = dTrans['EPFPos'] if 'EPFPos' in dTrans else oListener.GetPos()
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget or not (oTarget.m_MoveCtrl):
            continue
        vTar = oTarget.GetPos()
        fCurDis = cl_math.CalDistance3D(vTar, vEnd)
        fDis = min(fCurDis, fMaxDis)
        fSecondOut = fDis / fSpeed
        vDir = cl_math.Vec3Minus(vEnd, vTar)
        if oTarget.m_FightType & WARRIOR_MONSTER:
            oTarget.m_MoveCtrl.PushMove(oTarget, vDir, fSpeed, fSecondOut)
            continue
        oTarget.m_MoveCtrl.PushMove(oTarget, vDir, fSpeed, fSecondOut, 0, 9.8)
    


def EventCBTargetRecordInjureListener(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        dAll = oTarget.Query('Injured', { })
        dAll[oListener.m_ID] = 1
        oTarget.Set('Injured', dAll)
    


def EventCBSelfStop(oListener, oEventCB):
    if not oListener.m_MoveCtrl:
        return None
    if oListener.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
        oListener.m_MoveCtrl.Stop(oListener, oEventCB.m_Key)
    else:
        oListener.m_MoveCtrl.Stop(oListener)


def GetCommonEventKey(dEventInfo):
    sKey = ''
    if 'StateKey' in dEventInfo:
        sKey = dEventInfo['StateKey']
    elif 'PFKey' in dEventInfo:
        sKey = dEventInfo['PFKey']
    elif 'ItemKey' in dEventInfo:
        sKey = dEventInfo['ItemKey']
    return sKey


def CheckWeaponType2(oWeapon, iType):
    if 15 & iType:
        if oWeapon.m_Type == iType:
            return 1
        return 0
    if oWeapon.m_Type & iType == iType:
        return 1
    return 0


def EventCBChangeElementAttr(oListener, oEventCB, iPerform):
    
    def ClearChangePerformDamType(oListener, oCommonObj):
        oChangePerform = oListener.GetPerform(iPerform)
        if not oChangePerform:
            return None
        sKey = oLifeCycle.Key()
        oChangePerform.m_ElementTypeObj.RemoveSetModify(sKey)

    oChangePerform = oListener.GetPerform(iPerform)
    if not oChangePerform:
        return None
    oWeapon = oListener.m_WieldCon.GetCurWeapon()
    if not oWeapon:
        return None
    iDamType = oWeapon.m_ElementTypeObj.GetValue()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    oChangePerform.m_ElementTypeObj.SetModify(sKey, iDamType)
    oLifeCycle.AddDisableFunc(ClearChangePerformDamType)


def CommonCBSetMonsterDis(oListener, oEventCB, sBaseKey):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    iRecent = 99999
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        iDis = cl_math.CalDistance3D(oListener.GetPos(), oTarget.GetPos())
        if iDis < iRecent:
            iRecent = iDis
    
    sKey = f'''RecentDis{sBaseKey}'''
    oListener.Set(sKey, iRecent)
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddDisableType(DISABLE_TYPE_KEY, sKey)


def EventCBDropBeadByHP(oListener, oEventCB, iCnt, iTime):
    if not iCnt or iCnt <= 0:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TotalDam' not in dMsgInfo:
        return None
    if 'CurVID' not in dMsgInfo:
        return None
    if 'AID' not in dMsgInfo:
        return None
    oGame = oListener.m_Game
    iTotalDam = sum(dMsgInfo['TotalDam'])
    iOldDam = oListener.Query('OldDam', 0)
    iTotalDam += iOldDam
    iMaxHP = oListener.QueryAttr('HPMax')
    iShieldMax = oListener.QueryAttr('ShieldMax')
    iArmorMax = oListener.QueryAttr('ArmorMax')
    iTotalHP = iMaxHP + iShieldMax + iArmorMax
    iPer = min(iTotalDam * 100 // iTotalHP, 100)
    if iPer < iCnt:
        oListener.Set('OldDam', iTotalDam)
        return None
    iOverDam = iTotalDam % iCnt * iTotalHP // 100
    oListener.Set('OldDam', iOverDam)
    oVictim = oListener.m_Game.GetObject(dMsgInfo['CurVID'])
    oAttack = oListener.m_Game.GetObject(dMsgInfo['AID'])
    if not oAttack or not (oAttack.m_Scene):
        return None
    for i in range(iPer // iCnt):
        if oVictim.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            vBasePos = cl_reward.GetDropBasePos(oVictim)
            vFace = cl_math.Vec3Minus(oAttack.GetPos(), vBasePos)
            vPos = oGame.Scene_RandomPointSectorInMesh(oAttack.m_Scene, oAttack.GetPos(), vFace, 4, 12, 0, 180)
            if not vPos:
                continue
            vPos = (vPos[0], vBasePos[1], vPos[2])
        else:
            vPos = oVictim.GetPos()
            iX = oGame.Random(10) - 5
            iZ = oGame.Random(10) - 5
            vPos = (vPos[0] + iX, vPos[1], vPos[2] + iZ)
        lstDropInfo = [
            {
                'Hero': oAttack,
                'DropPos': vPos,
                'Delaytime': iTime }]
        oVictim.m_Game.GetResMgr().CreateDrop(oVictim.m_Scene, NWARRIOR_DROP_TREASURE_DEAD, vPos, lstDropInfo, {
            'Abandoner': oVictim.m_ID })
    


def CommonCBDropCash(oListener, oEventCB, iCnt, iInterval):
    if not iCnt or iCnt <= 0:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TotalDam' not in dMsgInfo:
        return None
    sKey = oEventCB.m_Key + 'DropTime'
    iCurFrame = oListener.m_Game.GetFrameNum()
    iOldFrame = oListener.Query(sKey, 0)
    iInterval = Time2Frame(iInterval)
    if iCurFrame - iOldFrame < iInterval:
        return None
    oListener.Set(sKey, iCurFrame)
    iTotalDam = sum(dMsgInfo['TotalDam'])
    iMaxHP = oListener.QueryAttr('HPMax')
    iPer = max(iTotalDam * 100 // iMaxHP, 1)
    if iPer > 100:
        dFactorInfo = { }
        dForceSetInfo = { }
        if oListener.HasAttr('HPMax'):
            oAttr = oListener.GetAttr('HPMax')
            dFactorInfo = oAttr.m_FactorInfo
            dForceSetInfo = oAttr.m_ForceSetInfo
        SendAlert('err', '%s 回调每损失百分之一血量掉落金币 异常：%d %s %s' % (oEventCB.m_Key, iPer, dFactorInfo, dForceSetInfo))
        iPer = 100
    for i in range(iPer * iCnt):
        dCash = {
            'Cash': 1 }
        oListener.m_Game.GetResMgr().CreateDrop(oListener.m_Scene, NWARRIOR_DROP_CASH, oListener.GetPos(), [
            dCash], { })
    
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddDisableType(DISABLE_TYPE_KEY, sKey)


def CommonCBDropReward(oListener, oEventCB, dDropCnt, dProbability, iDelay, iSource = MG_SOURCE_KILLMONSTER, iOnlyRewardAttack = 0, iRepeatReward = 0):
    
    def DelayCommonCBDropReward(oListener, iAttack, dDropCnt, dProbability):
        dReward = { }
        for ID in dDropCnt:
            if ID in dProbability:
                dReward[ID] = (dProbability[ID], dDropCnt[ID])
        
        dExtInfo = {
            'CalOffset': 0,
            'CheckGoldenCup': 1,
            'OnlyRewardAttack': iOnlyRewardAttack,
            'Abandoner': oListener.m_ID,
            'RepeatReward': iRepeatReward }
        cl_reward.RewardItemByMiniGame(oListener, iAttack, dReward, sKey, iSource, dExtInfo)

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for k, v in dDropCnt.items():
        iCnt = cl_formula.GetResultByData(oListener, v, dEventInfo, dMsgInfo)
        dDropCnt[k] = iCnt
    
    iAttack = dEventInfo['AID']
    sKey = oEventCB.m_Key + 'DropReward'
    if not iDelay:
        DelayCommonCBDropReward(oListener, iAttack, dDropCnt, dProbability)
        return None
    func = Functor(DelayCommonCBDropReward, oListener, iAttack, dDropCnt, dProbability)
    oListener.Call_Out(func, Time2Frame(iDelay), sKey)


def CommonCBSetRefreshMonsterTime(oListener, oEventCB):
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    sKey = oEventCB.m_Key + 'MonsterTime'
    oListener.Set(sKey, oListener.m_Game.GetFrameNum())
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddDisableType(DISABLE_TYPE_KEY, sKey)


def CommonCBAddPerform(oListener, oEventCB, iPerform):
    oListener.AddPerform(iPerform, 1)


def EventCBTargetAddPerform(oListener, oEventCB, iPerform, iLevel):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iLevel = cl_formula.GetResultByData(oListener, iLevel, dEventInfo, dMsgInfo, dEventInfo)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if oTarget:
            oTarget.AddPerform(iPerform, iLevel)
    


def EventCBTargetRemovePerform(oListener, oEventCB, iPerform):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if oTarget and oTarget.m_Perform:
            oTarget.m_Perform.RemovePerform(oTarget, iPerform)
    


def CommonCBTargetDropReward(oListener, oEventCB, dDropCnt, dProbability, iDelay, iSource = MG_SOURCE_KILLMONSTER, iOnlyRewardAttack = 0, iRepeatReward = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        CommonCBDropReward(oTarget, oEventCB, dDropCnt, dProbability, iDelay, iSource, iOnlyRewardAttack, iRepeatReward)
    


def EventCBChangeAllWeaponAttr(oListener, oEventCB, sAttr, iAdd, iMul, iType):
    dEventInfo = oEventCB.GetCBEventInfo()
    lstAdd = []
    if iType:
        lstItem = oListener.m_WieldCon.GetAllItem()
        for oItem in lstItem:
            if CheckWeaponType2(oItem, iType):
                lstAdd.append(oItem)
        
    else:
        lstAdd = oListener.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo, dEventInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo, dEventInfo)
    for oWeapon in lstAdd:
        if iMul or iAdd:
            oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
            oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
            continue
        if (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
            oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
        oWeapon.AttrClear(sAttr, sKey)
    


def EventCBChangeOwnerAllWeaponAttr(oListener, oEventCB, sAttr, iAdd, iMul, iType):
    
    def ClearFunc(oTarget, oLifeCycle):
        oOwner = oListener.GetOwner()
        if not oOwner:
            return None
        lstAdd = []
        if iType:
            lstItem = oOwner.m_WieldCon.GetAllItem()
            for oItem in lstItem:
                if CheckWeaponType2(oItem, iType):
                    lstAdd.append(oItem)
            
        else:
            lstAdd = oOwner.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
        for oWeapon in lstAdd:
            oWeapon.AttrClear(sAttr, sKey)
        

    dEventInfo = oEventCB.GetCBEventInfo()
    oOwner = oListener.GetOwner()
    lstAdd = []
    if iType:
        lstItem = oOwner.m_WieldCon.GetAllItem()
        for oItem in lstItem:
            if CheckWeaponType2(oItem, iType):
                lstAdd.append(oItem)
        
    else:
        lstAdd = oOwner.m_WieldCon.GetAllItemByMask(itemdef.EQUIP_MASK_WEAPON)
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iMul or iAdd:
        for oWeapon in lstAdd:
            oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
        
        sUniqueKey = 'ChangeAllWeaponAttr-%s' % sAttr
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)
    else:
        for oWeapon in lstAdd:
            oWeapon.AttrClear(sAttr, sKey)
        


def EventCBChangeWeaponAttr(oListener, oEventCB, sAttr, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    oWeapon = oListener.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
    if not oWeapon:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo, dEventInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo, dEventInfo)
    if iMul or iAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
        oLifeCycle.m_ItemApply[(oWeapon.m_ID, sAttr)] = 1
    elif (oWeapon.m_ID, sAttr) in oLifeCycle.m_ItemApply:
        oLifeCycle.m_ItemApply.pop((oWeapon.m_ID, sAttr))
    oWeapon.AttrClear(sAttr, sKey)


def EventCBChangeOwnerWeaponAttr(oListener, oEventCB, sAttr, iAdd, iMul):
    
    def ClearFunc(oTarget, oLifeCycle):
        oOwner = oListener.GetOwner()
        if not oOwner:
            return None
        oWeapon = oOwner.m_WieldCon.GetItemByID(iItem)
        if not oWeapon:
            return None
        oWeapon.AttrClear(sAttr, sKey)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    oOwner = oListener.GetOwner()
    iItem = dMsgInfo['ItemID']
    oWeapon = oOwner.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iMul or iAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
        sUniqueKey = 'ChangeOwnerWeaponAttr-%s-%s' % (iItem, sAttr)
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)
    else:
        oWeapon.AttrClear(sAttr, sKey)


def EventCBChangeHPDamType(oListener, oEventCB, iRatio):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    setHPDamTypeReason = oListener.Query('ChangeHPDamTypeReason', None)
    if setHPDamTypeReason:
        if 'CacheHPDamTypeReason' not in dMsgInfo:
            SendAlert('err', '%s no cache reason ' % oEventCB.m_Key)
            return None
        setReason = dMsgInfo['CacheHPDamTypeReason']
        if setReason == setHPDamTypeReason or 'CacheHPDamTypeRatio' in dMsgInfo:
            iRatio += dMsgInfo['CacheHPDamTypeRatio']
        elif 'CacheHPDamTypeRatio' in dMsgInfo:
            dMsgInfo['CacheHPDamTypeRatio'] += iRatio
        else:
            dMsgInfo['CacheHPDamTypeRatio'] = iRatio
        return None
    iRatio = min(iRatio, 1)
    if iRatio <= 0:
        return None
    lNewDam = []
    for idx, (iDam, oReason) in enumerate(dMsgInfo['MainDam']):
        iDamType = oReason.Query('DamType', 0)
        iNewDam = int(iDam * iRatio)
        iDam -= iNewDam
        iNewDamType = iDamType & ~DAM_USE_ALL | DAM_USE_HP
        oNewReason = oReason.ExtInfo({
            'DamType': iNewDamType })
        dMsgInfo['MainDam'][idx] = [
            iDam,
            oReason]
        lNewDam.append([
            iNewDam,
            oNewReason])
    
    if lNewDam:
        dMsgInfo['MainDam'].extend(lNewDam)


def EventCBAddHPDamTypeReason(oListener, oEventCB, iReason = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CacheHPDamTypeReason' in dMsgInfo:
        dMsgInfo['CacheHPDamTypeReason'].add(iReason)
    else:
        dMsgInfo['CacheHPDamTypeReason'] = {
            iReason}


def EventCBAddDamType(oListener, oEventCB, iTarDamType, iAddUseType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    for idx, (iDam, oReason) in enumerate(dMsgInfo['MainDam']):
        iDamType = oReason.Query('DamType', 0)
        if iDamType & DAM_USE_ALL == iTarDamType:
            iNewDamType = iDamType | iAddUseType
            oNewReason = oReason.ExtInfo({
                'DamType': iNewDamType })
            dMsgInfo['MainDam'][idx] = [
                iDam,
                oNewReason]
    


def EventCBDoEnableFunc(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'LifeCycle' not in dEventInfo:
        return None
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.CallFunc('Enable', oListener)


def EventCBChangeRelicValidRemove(oListener, oEventCB, iValid, iNotClear = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        sKey = 'ChangeSigal%s' % oLifeCycle.Key()
        dRelic = oTarget.Query(sKey, { })
        oTarget.Set(sKey, { })
        oRelicCon = oTarget.m_RelicCon
        oRelicCon.DelRelicTempRemove(dRelic)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' in dMsgInfo:
        iRelic = dMsgInfo['iPerform']
    elif 'Relic' in dMsgInfo:
        iRelic = dMsgInfo['Relic']
    else:
        return None
    oRelicCon = oListener.m_RelicCon
    oRelic = oRelicCon.GetPerform(iRelic)
    if not oRelic:
        return None
    iValidRemove = oRelic.ValidRemove()
    if iValid == iValidRemove:
        return None
    oRelicCon.SetRelicTempRemoveType({
        iRelic: iValid })
    if iNotClear:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = 'ChangeSigal%s' % oLifeCycle.Key()
    dRelic = oListener.Query(sKey, { })
    dRelic[iRelic] = iValidRemove
    oListener.Set(sKey, dRelic)
    oLifeCycle.AddDisableFunc(ClearFunc)


def EventCBSetRelicArgValue(oListener, oEventCB, sKey, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' not in dMsgInfo or not dMsgInfo['iPerform']:
        return None
    iRelic = dMsgInfo['iPerform']
    oRelic = oListener.m_RelicCon.GetPerform(iRelic)
    if not oRelic:
        return None
    iVal = cl_formula.GetResultByData(oListener, iVal, oEventCB.GetCBEventInfo(), dMsgInfo)
    oRelic.SetArgValue(sKey, iVal)


def EventCBHaltFlow(oLisetner, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['Halt'] = 1


def EventCBHaltPriMsg(oLisetner, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['HaltPriMsg'] = 1


def EventCBAddEventInfoFlag(oLisetner, oEventCB, sFlag):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo[sFlag] = 1


def EventCBGetStateStatistics(oListener, oEventCB, iStateSID, sAttr):
    dMsgInfo = oEventCB.GetCBEventInfo()
    iAttack = dMsgInfo['AID']
    oAttacker = oListener.m_Game.GetObject(iAttack)
    if not oAttacker:
        return 0
    oStateCon = oAttacker.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return 0
    if sAttr not in oState.m_Data:
        return 0
    return oState.m_Data[sAttr]


def EventCBGetStateStatisticsByID(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBEventInfo()
    iAttack = dMsgInfo['AID']
    iStateID = dMsgInfo['StateID']
    oAttacker = oListener.m_Game.GetObject(iAttack)
    if not oAttacker:
        return 0
    oStateCon = oAttacker.m_State
    oState = oStateCon.GetItem(iStateID)
    if not oState:
        return 0
    if sAttr not in oState.m_Data:
        return 0
    return oState.m_Data[sAttr]


def EventCBAddStateStatistics(oListener, oEventCB, iValue, iStateSID, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    iValue = cl_formula.GetResultByData(oListener, iValue, oEventCB.GetCBEventInfo(), dMsgInfo)
    if sAttr in oState.m_Data:
        oState.m_Data[sAttr] += iValue
    else:
        oState.m_Data[sAttr] = iValue


def EventCBAddTargetFromSameItemStateStatistics(oListener, oEventCB, iValue, iStateSID, sAttr):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iItemID = dEventInfo['ItemID']
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstState = oTarget.m_State.GetItems(iStateSID)
        for oState in lstState:
            if oState.m_Item != iItemID:
                continue
            if sAttr in oState.m_Data:
                oState.m_Data[sAttr] += iValue
                continue
            oState.m_Data[sAttr] = iValue
        
    


def EventCBSetStateStatistics(oListener, oEventCB, iValue, iStateSID, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    iValue = cl_formula.GetResultByData(oListener, iValue, oEventCB.GetCBEventInfo(), dMsgInfo)
    oState.m_Data[sAttr] = iValue


def EventCBSetStateStatisticsByOrderAndAddType(oListener, oEventCB, iValue, iStateSID, sAttr, iOrder, iAddType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oStateCon = oListener.m_State
    iIndex = 0
    if iOrder:
        iIndex = -1
    elif iAddType:
        clsState = cl_state.GetStateClass(iStateSID)
        if clsState.m_AddType == STATE_ADD_SYNC:
            iIndex = -1
    oState = oStateCon.GetItemBySIDWithIndex(iStateSID, iIndex)
    iValue = cl_formula.GetResultByData(oListener, iValue, oEventCB.GetCBEventInfo(), dMsgInfo)
    oState.m_Data[sAttr] = iValue


def EventCBSetCartoonUpdateValue(oListener, oEventCB, sKey, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dCurCartoon = oSkill.GetCurCartoon()
    if not dCurCartoon:
        return None
    dData = oSkill.m_Update.setdefault('EventCartoonValue', { })
    dData[(dCurCartoon['ID'], sKey)] = iValue


def EventCBGetCartoonUpdateValue(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    dCurCartoon = oSkill.GetCurCartoon()
    if not dCurCartoon:
        return 0
    dData = oSkill.m_Update['EventCartoonValue'] if 'EventCartoonValue' in oSkill.m_Update else { }
    tKey = (dCurCartoon['ID'], sKey)
    if tKey in dData:
        return dData[tKey]
    return 0


def EventCBAddSourceWeaponBagBullet(oListener, oEventCB, iAmount):
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = GetCommonEventKey(dEventInfo)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SID' in dMsgInfo:
        iBulletSID = dMsgInfo['SID']
        iAddAmount = cl_formula.GetResultByData(oListener, iAmount, dEventInfo, dMsgInfo)
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    else:
        return None
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon or oWeapon.IsInitWeapon():
        return None
    iAddAmount = cl_formula.GetResultByData(oListener, iAmount, dEventInfo, dMsgInfo, {
        'Weapon': oWeapon })
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iBulletSID = oBulletCom.BulletType()
    oListener.m_BulletCon.BulletModify(iBulletSID, iAddAmount, sKey)


def EventCBUsePerform(oListener, oEventCB, iPerform, iIsVid = 0, dCustom = None):
    dTransInfo = oEventCB.GetCBTransInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if not oListener.GetPerform(iPerform):
        oListener.AddPerform(iPerform, 1)
    oPerform = oListener.GetPerform(iPerform)
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        lstLockTarget = []
        if not oTarget:
            continue
        lstLockTarget.append(oTarget.m_ID)
        tPos = oTarget.GetPos()
        dData = { }
        dData['Custom'] = { }
        if 'VID' in dMsgInfo:
            dData['VID'] = dMsgInfo['VID']
        if 'CurVID' in dMsgInfo:
            dData['VID'] = dMsgInfo['CurVID']
        if iIsVid and 'VID' in dMsgInfo:
            iVictim = dMsgInfo['VID']
            oVictim = oGame.GetObject(iVictim)
            if not oVictim:
                continue
            tPos = oVictim.GetPos()
            dData['Custom']['vStart'] = tPos
            dData['VID'] = iTarget
        tPos = [
            tPos[0],
            tPos[1] + oTarget.m_ModelHeight * 0.5,
            tPos[2]]
        dData['vStart'] = tPos
        dData['Custom']['LockTarget'] = lstLockTarget
        if 'StateInfo' in dEventInfo and 'pfid' in dEventInfo['StateInfo']:
            dData['Custom']['pfid'] = dEventInfo['StateInfo']['pfid']
        if 'pfid' in dEventInfo:
            dData['Custom']['pfid'] = dEventInfo['pfid']
        if 'Skill' in dMsgInfo:
            dData['Custom']['TriggerPerfrom'] = dMsgInfo['Skill'].m_Base['pfid']
        if dCustom:
            dCustomData = { }
            for sKey, tData in dCustom.items():
                iValue = cl_formula.GetResultByData(oListener, tData, dEventInfo, dMsgInfo)
                dCustomData[sKey] = iValue
            
            dData['Custom'].update(dCustomData)
        cl_war.UsePerform(oListener, oPerform, dData)
    


def EventCBNonLockEnemyTarget(oListener, oEventCB):
    lstTarget = []
    iLockEnemy = 0
    if oListener.m_Agent:
        oLockEnemy = oListener.m_Agent.GetLockEnemy()
        iLockEnemy = oLockEnemy.m_ID
    oScene = oListener.m_Game.m_SceneMgr.GetScene(oListener.m_Scene)
    lstSceneHero = oScene.GetHeros() if oScene else []
    for iHero in lstSceneHero:
        if iLockEnemy and iLockEnemy == iHero:
            continue
        lstTarget.append(iHero)
    
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTarget


def EventCBTargetUsePerform(oListener, oEventCB, iTargetCnt, dPerform):
    
    def DelayUsePerformOnTargetList(oWarrior, lstTarget, iPerform):
        pfobj = oWarrior.GetPerformIfNoThenNew(iPerform)
        for iTarget in lstTarget:
            cl_war.UsePerform(oListener, pfobj, {
                'VID': iTarget })
        

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTargetCnt = cl_formula.GetResultByData(oListener, iTargetCnt, dEventInfo, dMsgInfo)
    if not iTargetCnt:
        return None
    oGame = oListener.m_Game
    sKey = GetCommonEventKey(dEventInfo)
    lstTarget = ShufferList(oGame, dTransInfo['TargetList'], iTargetCnt)
    dCallKey = { }
    for idx, (iPerform, iDelayTime) in enumerate(dPerform.items()):
        iDelayFrame = Time2Frame(iDelayTime)
        if iDelayFrame:
            sCallKey = '%s-%s' % (sKey, idx)
            dCallKey[sCallKey] = 1
            oListener.Remove_Call_Out(sCallKey)
            oListener.Call_Out(Functor(DelayUsePerformOnTargetList, oListener, lstTarget, iPerform), iDelayFrame, sCallKey)
            continue
        DelayUsePerformOnTargetList(oListener, lstTarget, iPerform)
    
    oLifeCycle = dEventInfo['LifeCycle']
    if dCallKey:
        oLifeCycle.AddDisableType(DISABLE_TYPE_CALL, dCallKey)


def EventCBTarget2ListenerUsePerform(oListener, oEventCB, iPerform, fDis):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    vFace = oListener.GetFacing()
    vPos = cl_math.Vec3DisplaceDir(oListener.GetPos(), (vFace[0], 0, vFace[1]), fDis)
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oPerform = oTarget.GetPerformIfNoThenNew(iPerform)
        if not oPerform:
            continue
        dPerform = {
            'Custom': {
                'vStart': vPos } }
        cl_war.UsePerform(oTarget, oPerform, dPerform)
    


def PassiveCBGetSceneData(oListener, oEventCB, sAttr):
    if not oListener.m_Scene:
        SendAlert('err', f'''{oEventCB.m_Key}事件场景不存在:{oListener.m_Scene}''')
        return 0
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return 0
    if sAttr in oScene.m_CustomData:
        return oScene.m_CustomData[sAttr]
    return 0


def PassiveCBChangeSceneData(oListener, oEventCB, sAttr, iAdd, iSet):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    if not oListener.m_Scene:
        SendAlert('err', f'''{oEventCB.m_Key}事件场景不存在:{oListener.m_Scene}''')
        return None
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    if iSet:
        iSet = cl_formula.GetResultByData(oListener, iSet, dEventInfo, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iOldData = oScene.m_CustomData[sAttr] if sAttr in oScene.m_CustomData else 0
    if iSet:
        iNewData = iSet + iAdd
    else:
        iNewData = iOldData + iAdd
    oScene.m_CustomData[sAttr] = iNewData


def EventCBSetTargetConnectionInfo(oListener, oEventCB, iState):
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = 'TargetList%d' % iState
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    lstTarget = []
    if sKey not in oScene.m_CustomData:
        lstTarget.append(oListener.m_ID)
        oScene.m_CustomData[sKey] = lstTarget
    else:
        lstTarget = oScene.m_CustomData[sKey]
        if oListener.m_ID not in lstTarget:
            lstTarget.append(oListener.m_ID)


def EventGetTargetByConnectionInfo(oListener, oEventCB, iState):
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = 'TargetList%d' % iState
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTarget = []
    lstNewTarget = []
    if sKey not in oScene.m_CustomData:
        return None
    for iTarget in oScene.m_CustomData[sKey]:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        lstNewTarget.append(iTarget)
        if iTarget != iVictim:
            lstTarget.append(iTarget)
    
    dTransInfo['TargetList'] = lstTarget
    oScene.m_CustomData[sKey] = lstNewTarget


def EventFullCareerPerformColdTime(oListener, oEventCB):
    pfobj = oListener.GetCareerPerform()
    if not pfobj:
        return None
    iPerform = pfobj.m_SID
    iColdTimeFrame = oListener.m_Perform.GetNowCoverRemainTime(iPerform)
    if not iColdTimeFrame:
        return None
    iMaxColdTimeFrame = oListener.m_Perform.GetMaxColdTime(iPerform)
    oListener.m_Perform.ModifyColdTime(iPerform, iMaxColdTimeFrame - iColdTimeFrame)


def EventGetTargetBySkillVlst(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    oGame = oListener.m_Game
    dTransInfo['TargetList'] = []
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if 'lstVLST' not in oSkill.m_Collect:
        return None
    for iTarget in oSkill.m_Collect['lstVLST']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        dTransInfo['TargetList'].append(iTarget)
    


def EventGetTargetBySummonType(oListener, oEventCB, iSummonType):
    dTransInfo = oEventCB.GetCBTransInfo()
    oGame = oListener.m_Game
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstNewTar = []
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        for iSummon in oTarget.m_SummonDict:
            oSummon = oGame.GetObject(iSummon)
            if oSummon and oSummon.m_FightType & iSummonType == iSummonType:
                lstNewTar.append(iSummon)
                dTransInfo['EPFPos'] = oSummon.GetPos()
        
    
    dTransInfo['TargetList'] = lstNewTar


def EventGetEnergyCost(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'EnergyCost' in dMsgInfo:
        return dMsgInfo['EnergyCost']
    return 0


def EventSetEnergyCost(oListener, oEventCB, iEnergyCost):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iEnergyCost = cl_formula.GetResultByData(oListener, iEnergyCost, dEventInfo, dMsgInfo)
    dMsgInfo['EnergyCost'] = iEnergyCost


def EventCBGetPerformAttr(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        SendAlert('err', '%s事件回调未设置技能' % oEventCB.m_Key)
        return None
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return 0
    return oPerform.CalAttr(sAttr)


def EventGetTargetByMsgInfoSummonID(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstNewTar = []
    oSummon = oListener.m_Game.GetObject(dMsgInfo['summonId'])
    if oSummon:
        lstNewTar.append(dMsgInfo['summonId'])
        dTransInfo['EPFPos'] = oSummon.GetPos()
    dTransInfo['TargetList'] = lstNewTar


def EventGetTotalDamage(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo:
        return 0
    return sum(dMsgInfo['PredictChange'])


def EventCBDropBulletInTarget(oListener, oEventCB, dAmount, iAssignBulletType, iRewardTarget = 0, iUseMsgPos = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    oGame = oListener.m_Game
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iAssignBulletType = cl_formula.GetResultByData(oListener, iAssignBulletType, dEventInfo, dMsgInfo)
    if iAssignBulletType:
        dAmount = {
            iAssignBulletType: dAmount.get(iAssignBulletType, 0) }
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if iUseMsgPos and 'CurHitPos' in dMsgInfo:
            vPos = dMsgInfo['CurHitPos']
        else:
            vPos = oTarget.GetPos()
        sKey = GetCommonEventKey(dEventInfo)
        lstDropInfo = [
            dAmount]
        dReward = {
            'item': VIRTUAL_ITEM_DROP,
            'info': {
                'DropType': NWARRIOR_DROP_BULLET,
                'DropInfo': lstDropInfo,
                'DropPos': vPos } }
        tobj = oTarget if iRewardTarget else oListener
        cl_reward.RewardItem(oListener.m_Game, tobj, [
            dReward], sKey, {
            'Player': tobj.m_ID })
    


def EventChangeMinorPerformEnergyCost(oListener, oEventCB, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iFormulaValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    iEnergyCost = oListener.Query('EnergyCost', 0)
    iChange = iEnergyCost + iFormulaValue
    oListener.Set('EnergyCost', iChange)
    oListener.GS2CPropChange('EnergyCost', iChange)


def EventGetTMinorPerformEnergyCost(oListener, oEventCB):
    return oListener.Query('EnergyCost', 0)


def EventGetTargetMaskMonsterAsTarget(oListener, oEventCB, sMask, iDirectGet = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstNewTar = []
    oGame = oListener.m_Game
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if iDirectGet:
            lstNewTar.extend(oTarget.Query(sMask, []))
            continue
        dMaskMonster = oTarget.Query(sMask, { })
        if sMask in dMaskMonster:
            lstNewTar.extend(dMaskMonster[sMask])
    
    dTransInfo['TargetList'] = lstNewTar


def EventGetTargetMonsterRelicNumByQuality(oListener, oEventCB, iQuality):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget or not (oTarget.m_FightType & WARRIOR_MONSTER):
        return 0
    oMonsterRelicElement = oTarget.m_Game.m_WarMgr.GetComponent('MonsterRelicElement')
    if not iQuality:
        return oMonsterRelicElement.GetMonsterRelicNum(oTarget)
    return oMonsterRelicElement.GetMonsterRelicNumByQuality(oTarget, iQuality)


def EventGetStateEffectiveCnt(oListener, oEventCB):
    oGame = oListener.m_Game
    dMsgInfo = oEventCB.GetCBEventInfo()
    iStateID = dMsgInfo['StateID']
    oStateCon = oListener.m_State
    oState = oStateCon.GetItem(iStateID)
    if not oState:
        return 0
    iEffectiveCnt = 0
    iCurFrame = oGame.GetFrameNum()
    dEffective = { }
    if 'EffectiveTimeInfo' in oState.m_Data:
        for iFrame, iCount in oState.m_Data['EffectiveTimeInfo'].items():
            if iFrame > iCurFrame:
                iEffectiveCnt += iCount
                dEffective[iFrame] = iCount
        
    oState.m_Data['EffectiveTimeInfo'] = dEffective
    iNowCount = oState.GetCount()
    iAddCount = iEffectiveCnt - iNowCount
    oState.AddCount(oListener, iAddCount)
    return iEffectiveCnt


def EventCBAddTargetStateCountAndEffectiveTime(oListener, oEventCB, iStateSID, iAdd, iTime, iFromAdder):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iAddCount = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iEffectiveFrame = Time2Frame(iTime)
    iCurFrame = oGame.GetFrameNum()
    iTotalFrame = iCurFrame + iEffectiveFrame
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iFromAdder:
            iAttacker = dEventInfo['StateInfo']['AID'] if 'StateInfo' in dEventInfo else dEventInfo.get('AID', 0)
            lstState = oTarget.m_State.GetItems(iStateSID)
            for oState in lstState:
                if oState.m_Attacker != iAttacker:
                    continue
                oState.AddCount(oTarget, iAddCount)
                dInfo = oState.m_Data.setdefault('EffectiveTimeInfo', { })
                oState.m_Data['EffectiveTimeInfo'][iTotalFrame] = (dInfo[iTotalFrame] if iTotalFrame in dInfo else 0) + iAddCount
            
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if oState:
            oState.AddCount(oTarget, iAddCount)
            dInfo = oState.m_Data.setdefault('EffectiveTimeInfo', { })
        oState.m_Data['EffectiveTimeInfo'][iTotalFrame] = (dInfo[iTotalFrame] if iTotalFrame in dInfo else 0) + iAddCount
    


def EventCBAddTargetStateAllCountEffectiveTime(oListener, oEventCB, iStateSID, iTime):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iEffectiveFrame = Time2Frame(iTime)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if not oState or 'EffectiveTimeInfo' not in oState.m_Data:
            continue
        dEffectiveTimeInfo = oState.m_Data['EffectiveTimeInfo']
        dNewEffectiveTimeInfo = { }
        for iFrame in dEffectiveTimeInfo:
            iNewFrame = iFrame + iEffectiveFrame
            dNewEffectiveTimeInfo[iNewFrame] = dEffectiveTimeInfo[iFrame]
        
        oState.m_Data['EffectiveTimeInfo'] = dNewEffectiveTimeInfo
    


def EventClearTargetStateEffectiveTimeInfo(oListener, oEventCB, iStateSID, iFromSelf):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if not iFromSelf:
            oState = oTarget.m_State.GetItemBySID(iStateSID)
            if not oState:
                continue
            oState.m_Data['EffectiveTimeInfo'] = { }
            continue
        lstState = oTarget.m_State.GetItems(iStateSID)
        for oState in lstState:
            if oState.m_Attacker != oListener.m_ID:
                continue
            oState.m_Data['EffectiveTimeInfo'] = { }
        
    


def EventReduceTargetStateEffectiveCount(oListener, oEventCB, iStateSID, iReduce):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iReduce = cl_formula.GetResultByData(oListener, iReduce, dEventInfo, dMsgInfo)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if not oState:
            continue
        iEffectiveCnt = 0
        iCurFrame = oGame.GetFrameNum()
        lstCount = []
        if 'EffectiveTimeInfo' in oState.m_Data:
            for iFrame, iCount in oState.m_Data['EffectiveTimeInfo'].items():
                if iFrame > iCurFrame:
                    lstCount.append(iFrame)
                    iEffectiveCnt += iCount
            
        if iEffectiveCnt <= iReduce:
            oState.m_Data['EffectiveTimeInfo'] = { }
            continue
        lstCount.sort()
        for iFrame in lstCount:
            if iReduce <= 0:
                break
            if oState.m_Data['EffectiveTimeInfo'][iFrame] <= iReduce:
                iReduce -= oState.m_Data['EffectiveTimeInfo'][iFrame]
                oState.m_Data['EffectiveTimeInfo'].pop(iFrame)
                continue
            iRemainCount = oState.m_Data['EffectiveTimeInfo'][iFrame] - iReduce
            oState.m_Data['EffectiveTimeInfo'][iFrame] = iRemainCount
        
    


def EventSetTargetMark(oListener, oEventCB, sMark, iNotAddDefaultKey = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iSelf = oListener.m_ID
    oGame = oListener.m_Game
    sKey = oEventCB.m_Key
    if iNotAddDefaultKey:
        sFinalMark = sMark
    else:
        sPreFix = sKey.split('-', 1)[0]
        sFinalMark = '%s-%s' % (sPreFix, sMark)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstMaskTarget = oTarget.Query(sFinalMark, [])
        if iSelf not in lstMaskTarget:
            lstMaskTarget.append(iSelf)
        oTarget.Set(sFinalMark, lstMaskTarget)
    


def EventClearTargetMark(oListener, oEventCB, sMark, iJustClearSelf = 0, iNotAddDefaultKey = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    sKey = oEventCB.m_Key
    iSelf = oListener.m_ID
    if iNotAddDefaultKey:
        sFinalMark = sMark
    else:
        sPreFix = sKey.split('-', 1)[0]
        sFinalMark = '%s-%s' % (sPreFix, sMark)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstMaskTarget = oTarget.Query(sFinalMark)
        if not lstMaskTarget:
            continue
        if iJustClearSelf:
            if iSelf in lstMaskTarget:
                lstMaskTarget.remove(iSelf)
            if not lstMaskTarget:
                oTarget.Delete(sFinalMark)
                continue
        oTarget.Delete(sFinalMark)
    


def EventSetSkillHitDamageInfo(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo or 'CurVID' not in dMsgInfo or 'MainDam' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iCurVID = dMsgInfo['CurVID']
    iDamage = 0
    for lstDam in dMsgInfo['MainDam']:
        iDamage += lstDam[0]
    
    sKey = oEventCB.m_Key
    if sKey not in oSkill.m_Collect:
        oSkill.m_Collect[sKey] = { }
    dInfo = oSkill.m_Collect[sKey]
    if iCurVID not in dInfo:
        if 'CurHitPos' in dMsgInfo:
            tPos = dMsgInfo['CurHitPos']
        else:
            tPos = oListener.m_Game.GetObject(dMsgInfo['CurVID']).GetPos()
        dInfo[iCurVID] = {
            'Pos': tPos,
            'Damage': iDamage }
    else:
        dInfo[iCurVID]['Damage'] += iDamage


def EventSetSkillFirstHitFinalDamageInfo(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo or 'CurVID' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iCurVID = dMsgInfo['CurVID']
    sKey = oEventCB.m_Key
    if sKey not in oSkill.m_Collect:
        oSkill.m_Collect[sKey] = { }
    dInfo = oSkill.m_Collect[sKey]
    if iCurVID in dInfo:
        return None
    iDamage = 0
    if 'TrueChange' in dMsgInfo:
        for lstDam in dMsgInfo['TrueChange']:
            iDamage += lstDam[0]
        
    if 'ExcessChange' in dMsgInfo:
        for lstDam in dMsgInfo['ExcessChange']:
            iDamage += lstDam[0]
        
    dInfo[iCurVID] = iDamage


def EventSetSkillHitInfo(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    if 'CurVID' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iCurVID = dMsgInfo['CurVID']
    if 'lstAllVID' not in oSkill.m_Collect:
        lstTarget = [
            iCurVID]
        oSkill.m_Collect['lstAllVID'] = lstTarget
    else:
        oSkill.m_Collect['lstAllVID'].append(iCurVID)


def EventGetTargetSkillHitInfo(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oGame = oListener.m_Game
    if 'lstAllVID' not in oSkill.m_Collect:
        return None
    lstTarget = oSkill.m_Collect['lstAllVID']
    for iTarget in lstTarget:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        lstTar.append(iTarget)
    


def EventRandomTargetExecCBFuncAction(oListener, oEventCB, iCount, iBanRepeat = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oGame = oListener.m_Game
    lstTar = dTransInfo['TargetList']
    iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    lstNewTarget = []
    if lstTar:
        for _ in range(iCount):
            iRandom = oGame.Random(len(lstTar))
            iTarget = lstTar[iRandom]
            lstNewTarget.append(iTarget)
            if iBanRepeat:
                del lstTar[iRandom]
                if not lstTar:
                    break
        
    dTransInfo['TargetList'] = lstNewTarget


def EventCBGetTargetStateRemainingTime(oListener, oEventCB, iState, iFromSelf):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    if not iFromSelf:
        oState = oTarget.m_State.GetItemBySID(iState)
        if not oState:
            return 0
        return Frame2Time(oState.GetRemainTime())
    lstState = oTarget.m_State.GetItems(iState)
    for oState in lstState:
        if oState.m_Attacker != oListener.m_ID:
            continue
        return Frame2Time(oState.GetRemainTime())
    
    return 0


def EventCBSetDamShowTipsType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oSkill.m_Collect['ExShowTips'] = iType


def EventCBAddShowTipsEffect(oTarget, oEventCB, iShopTipsEffect):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    for _, oReason in dMsgInfo['MainDam']:
        iExInfo = oReason.Query('ExInfo', 0) | iShopTipsEffect
        oReason.SetInfo('ExInfo', iExInfo)
    


def EventGetGscashChangeValue(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Cash' in dMsgInfo:
        return dMsgInfo['Cash']
    return 0


def EventCBAddWeaponEnhanceCnt(oListener, oEventCB, iCnt, sReason):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo.setdefault('Enhance', 0)
    dMsgInfo.setdefault('Reason', '')
    dMsgInfo['Enhance'] += iCnt
    dMsgInfo['Reason'] += sReason + ';'


def EventSetRelicDropLevel(oListener, oEventCB, iLevel):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Relic' not in dMsgInfo:
        return None
    clsPerform = cl_perform.GetPerformModule(dMsgInfo['Relic'])
    if clsPerform.m_MaxLevel >= iLevel:
        dMsgInfo['RelicDropLevel'] = iLevel


def EventGetTargetNum(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    return len(lstTar)


def EventAddHitTargetCnt(oListener, oEventCB, iCnt):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    for iTarget in dTrans['TargetList']:
        sKey = 'HitCnt%d' % iTarget
        iOldCnt = oListener.Query(sKey)
        oListener.Set(sKey, iOldCnt + iCnt)
    


def EventSetExSuperMonsterRatio(oListener, oEventCB, iRatio):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iRatio = cl_formula.GetResultByData(oListener, iRatio, dEventInfo, dMsgInfo)
    oGame = oListener.m_Game
    oMonsterSuper = oGame.m_WarMgr.GetComponent('MonsterSuper')
    oMonsterSuper.m_ExChooseRatio[oEventCB.m_Key] = iRatio


def EventSetExSuperMonsterNum(oListener, oEventCB, iCount):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    oGame = oListener.m_Game
    oMonsterSuper = oGame.m_WarMgr.GetComponent('MonsterSuper')
    oMonsterSuper.m_ExSuperNum[oEventCB.m_Key] = iCount


def EventCBGetTargetStateRemainingEffectiveTime(oListener, oEventCB, iState, iFromSelf):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return 0
    oGame = oListener.m_Game
    iCurFrame = oGame.GetFrameNum()
    iEffectiveTime = 0
    oStateCon = oTarget.m_State
    oTargetState = oStateCon.GetItemBySource(iState, oListener.m_ID) if iFromSelf else oStateCon.GetItemBySID(iState)
    if not oTargetState:
        return 0
    iStateCnt = oTargetState.GetCount()
    dInfo = oTargetState.m_Data.setdefault('EffectiveTimeInfo', { })
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


def EventCBUsePerformEvtTarget(oListener, oEventCB, iPerform, dData, iOnlyServer = 0):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sKey, lstFormula in dData.items():
        if isinstance(lstFormula, dict):
            dData[sKey] = lstFormula
            continue
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = dTransInfo['TargetList']
    if not lstTarget:
        return None
    oPerform = oListener.GetPerformIfNoThenNew(iPerform)
    if not oPerform:
        return None
    dPerform = {
        'Custom': dData }
    dData['LockTarget'] = lstTarget
    if 'StateInfo' in dEventInfo and 'pfid' in dEventInfo['StateInfo']:
        dPerform['Custom']['pfid'] = dEventInfo['StateInfo']['pfid']
    if 'Skill' in dMsgInfo and dMsgInfo['Skill']:
        oSkill = dMsgInfo['Skill']
        dPerform['Custom']['TriggerPerfromActNum'] = oSkill.m_Base['ActNum']
        dPerform['Custom']['TriggerPerfrom'] = oSkill.m_Base['pfid']
        if 'Inherit' in dData and dData['Inherit']:
            dPerform['Custom']['dCache'] = dict(oSkill.m_Cache)
        elif 'pfid' in dEventInfo:
            dPerform['Custom']['TriggerPerfrom'] = dEventInfo['pfid']
    if None:
        dPerform['VID'] = lstTarget[0]
        dData['LockTrigger'] = lstTarget[0]
    if not iOnlyServer:
        cl_war.UsePerform(oListener, oPerform, dPerform)
    else:
        cl_war.UseOnlyServerPerform(oListener, oPerform, dPerform)


def EventCBChangeItemPickCnt(oListener, oEventCB, iMul, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    dItem = dMsgInfo['Item']
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    for iSID, iCnt in dItem.items():
        dItem[iSID] = iCnt * iMul + iAdd if iMul else iCnt + iAdd
    


def EventCBAddHeroBuyBenedRule(oListener, oEventCB, iRule, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    dMsgInfo.setdefault('RuleInfo', [])
    dMsgInfo['RuleInfo'].append((iRule, iValue))


def EventCBGetTargetByBelongs(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = [
        oListener.m_Owner] if oListener.m_Owner else []


def EventCBGetTargetBySelfAndOwner(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = [
        oListener.m_Owner,
        oListener.m_ID] if oListener.m_Owner else [
        oListener.m_ID]


def EventCBReducePredictDam(oListener, oEventCB, iAdd, iCalExcess = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo and 'RS' not in dMsgInfo:
        SendAlert('err', '%s事件回调预测伤害不存在' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iCalExcess and 'ExcessChange' in dMsgInfo:
        iExcessChange = dMsgInfo['ExcessChange']
        iAdd -= iExcessChange
        if iAdd <= 0:
            dMsgInfo['ExcessChange'] = -iAdd
            return None
    lstPredictChange = dMsgInfo['PredictChange']
    oReason = dMsgInfo['RS'] if 'RS' in dMsgInfo else None
    iDamType = oReason.Query('DamType', 0) if oReason else 0
    for idx, sAttr, iUseType in reversed(cl_formula.g_DamTypeSequence):
        iChange = iAdd if lstPredictChange[idx] and iDamType & iUseType or lstPredictChange[idx] >= iAdd else lstPredictChange[idx]
        iAdd -= iChange
        lstPredictChange[idx] -= iChange
        if iAdd <= 0:
            break
    


def EventCBRecoverDam(oListener, oEventCB, iAdd, iDamgType):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TotalDam' not in dMsgInfo:
        return None
    lstTotalDam = dMsgInfo['TotalDam']
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    for idx, sAttr, iUseType in reversed(cl_formula.g_DamTypeSequence):
        iChange = lstTotalDam[idx] if iAdd >= lstTotalDam[idx] else iAdd
        iAdd -= iChange
        EventChangeDefValue(oListener, oEventCB, iChange, iUseType)
        if iAdd <= 0:
            break
    
    if iAdd > 0:
        EventChangeDefValue(oListener, oEventCB, iAdd, iDamgType)


def EventCBAddRatioToNoMaxHate(oListener, oEventCB, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oAgent = oListener.m_Agent
    if not oAgent:
        return None
    iRatio = oAgent.GetData('NoMaxHateRatio', 0)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iRatio += iAdd
    if iRatio > 100:
        iRatio = 100
    if iRatio < 0:
        iRatio = 0
    oAgent.SetData('NoMaxHateRatio', iRatio)


def EventCBEnableTargetBulletChangeRule(oListener, oEventCB, iPerform, iLevel):
    
    def ClearFunc(oTarget, oListener, oLifeCycle):
        pfobj = oLifeCycle.GetObject()
        iOwnPfid = pfobj.m_ID
        oClearPerform = oTarget.GetPerform(iPerform, 0, iOwnPfid)
        if not oClearPerform:
            return None
        oClearPerform.Disable(oTarget)

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        pfobj = oLifeCycle.GetObject()
        iOwnPfid = pfobj.m_ID
        oTarget.m_BulletChangeCon.AddPerform(oTarget, iOwnPfid, iPerform, iLevel, 1, 0)
        oFunc = Functor(ClearFunc, oTarget)
        oLifeCycle.AddDisableFunc(oFunc)
    


def EventCBConvertFamageToPoinType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo and 'FlowDam' not in dMsgInfo:
        return None
    for sDamKey in ('MainDam', 'FlowDam'):
        lNewDam = []
        if sDamKey not in dMsgInfo:
            continue
        for idx, (iDam, oReason) in enumerate(dMsgInfo[sDamKey]):
            iDamType = oReason.Query('DamType', 0)
            iNewDamType = iDamType & ~DAM_USE_ALL | iType
            oNewReason = oReason.ExtInfo({
                'DamType': iNewDamType })
            dMsgInfo[sDamKey][idx] = [
                0,
                oReason]
            lNewDam.append([
                iDam,
                oNewReason])
        
        if lNewDam:
            dMsgInfo[sDamKey].extend(lNewDam)
    


def EventCBRecordVictim(oListener, oEventCB, sMark):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    sKey = oEventCB.m_Key
    sPre = sKey.split('-', 1)[0]
    sMark = '%s-%s' % (sPre, sMark)
    iVictim = 0
    if 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    dVictim = oListener.Query(sMark, { })
    dVictim[iVictim] = 1
    oListener.Set(sMark, dVictim)


def EventCBCreatePart(oListener, oEventCB, iPartSID, iPartDiePhase):
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    oGame = oListener.m_Game
    oPart = oGame.m_ResMgr.CreateMonster(oListener.m_Scene, iPartSID, (0, 0, 0), (0, 0, 0), iSide = oListener.m_Side, iGrade = oListener.m_AddGrade, tLineIdx = oListener.m_LineIdx, dExtInfo = {
        'Owner': oListener.m_ID })
    if (not oPart or oPart.m_FightType != WARRIOR_ELIPART) and oPart.m_FightType != WARRIOR_NORPART:
        SendAlert('err', f'''{oEventCB.m_Key}事件回调创建客体失败{iPartSID}''')
        return None
    if oPart.m_Agent:
        oPart.m_Agent.Release()
        oPart.m_Agent = None
    oPart.m_DiePhase = iPartDiePhase
    oListener.m_Part = oPart.m_ID


def EventCBTransAttach(oListener, oEventCB, dAttr):
    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    if not oListener.m_Part:
        return None
    oPart = oListener.m_Game.GetObject(oListener.m_Part)
    if not oPart or oPart.IsDead():
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oReason = dEventInfo['RS']
    for sAttr in dAttr:
        if sAttr not in cl_formula.g_PartTransAttr:
            continue
        iType = cl_formula.g_PartTransAttr[sAttr]
        if iType == cl_formula.OTHER_TRANS:
            if sAttr == 'HP':
                iPartHP = oPart.HP()
                oPart.HPDirectModify('HP', oListener.m_ID, -iPartHP, oReason)
                oAttr = oPart.GetAttr('HPMax')
                iValue = oAttr.GetBaseAttr()
                oListener.SetAttr('HPMax', iValue, BASEATTR_REFRESH)
                oListener.HPDirectModify('HP', oPart.m_ID, iPartHP, oReason)
            elif sAttr == 'MoveSpeed':
                oAttr = oPart.GetAttr(sAttr)
                iValue = oAttr.GetBaseAttr()
                oAgent = oListener.m_Agent
                if oAgent:
                    oAgent.SetActionSMPatrol(oAgent)
                    oListener.SetAttr(sAttr, iValue * 100, BASEATTR_REFRESH)
                    continue
                continue
        if iType == cl_formula.ATTR_TRANS:
            Attr = getattr(oPart, sAttr)
            if not Attr:
                continue
            setattr(oListener, sAttr, Attr)
            continue
        if iType == cl_formula.QUERY_TRANS:
            oAttr = oPart.GetAttr(sAttr)
            iValue = oAttr.GetBaseAttr()
            oListener.SetAttr(sAttr, iValue, BASEATTR_REFRESH)
    


def EventCBRecallRider(oListener, oEventCB):
    
    def ResetBaseAttr(oTarget, sAttr):
        if iRound not in clsData.m_BaseAttrInfo:
            return None
        if sAttr not in clsData.m_BaseAttrInfo[iRound]:
            return None
        iVal = clsData.m_BaseAttrInfo[iRound][sAttr]
        iVal = cl_formula.GetFormulaResultByLV(oTarget, iVal, iGrade)
        oTarget.SetAttr(sAttr, iVal, BASEATTR_REFRESH)

    if oListener.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
        return None
    if not oListener.m_Part:
        return None
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    oReason = dEventInfo['RS']
    oPart = oListener.m_Game.GetObject(oListener.m_Part)
    iDataSID = oListener.m_SID
    clsData = oGame.m_WarData.GetMonsterData(iDataSID)
    iRound = oGame.m_WarMgr.m_Round
    iGrade = oListener.m_Grade
    for sAttr, iType in cl_formula.g_PartTransAttr.items():
        if iType == cl_formula.OTHER_TRANS:
            if sAttr == 'HP':
                dReason = {
                    'Type': TYPE_RELIFE_PASSIVE }
                dRelifeInfo = {
                    'HP': oListener.HP(),
                    'Shield': 0,
                    'Armor': 0 }
                oPart.Relife(dReason, dRelifeInfo)
                ResetBaseAttr(oListener, 'HPMax')
                oListener.HPDirectModify('HP', oListener.m_ID, oListener.QueryAttr('HPMax'), oReason)
            elif sAttr == 'MoveSpeed':
                oAttr = oListener.GetAttr(sAttr)
                iValue = oAttr.GetBaseAttr()
                oPart.SetAttr(sAttr, iValue * 100, BASEATTR_REFRESH)
                ResetBaseAttr(oListener, 'MoveSpeed')
                continue
        if iType == cl_formula.ATTR_TRANS:
            Attr = getattr(oListener, sAttr)
            if not Attr:
                continue
            setattr(oPart, sAttr, Attr)
            Attr = getattr(clsData, sAttr)
            if not Attr:
                continue
            setattr(oListener, sAttr, Attr)
            continue
        if iType == cl_formula.QUERY_TRANS:
            oAttr = oListener.GetAttr(sAttr)
            iValue = oAttr.GetBaseAttr()
            oPart.SetAttr(sAttr, iValue, BASEATTR_REFRESH)
            ResetBaseAttr(oListener, sAttr)
    
    oListener.SetPhase(1)


def EventCBDropRrlifeDrop(oListener, oEventCB, iPerformID = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo:
        return None
    oVictim = oListener.m_Game.GetObject(dMsgInfo['VID'])
    if not oVictim:
        return None
    vPos = cl_reward.GetDropBasePos(oVictim)
    oVictim.m_Game.GetResMgr().CreateDrop(oVictim.m_Scene, NWARRIOR_DROP_RELIFE, vPos, [
        {
            'PerformID': iPerformID }], { })


def EventReplaceRelicReward(oListener, oEventCB, dRelic, iCanRepeat = 0, iUseOldLevel = 0, iForceReplace = 0):
    setUnlock = oListener.Query('Illus')['Relic']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Relic' in dMsgInfo:
        clsRelic = cl_perform.GetPerformModule(dMsgInfo['Relic'])
        if clsRelic and clsRelic.m_RelicType == RELIC_TYPE_CURSE:
            return None
        lstRelicInfo = []
        for iRelic, iLevel in dRelic.items():
            if not iForceReplace and iRelic not in setUnlock:
                SendAlert('err', f'''{oEventCB.Key()} 回调将当前遗物替换为指定遗物 添加了未解锁遗物 {iRelic} ，请检查''')
                continue
            clsPerform = cl_perform.GetPerformModule(iRelic)
            if clsPerform.m_MaxLevel >= iLevel:
                lstRelicInfo.append((iRelic, iLevel))
                continue
            SendAlert('err', '%s替换秘卷%s时等级异常' % (oEventCB.m_Key, iRelic))
            return None
        
        if lstRelicInfo:
            dMsgInfo['ReplaceRelicInfo'] = lstRelicInfo
            dMsgInfo['RelicCanRepeat'] = iCanRepeat
            dMsgInfo['RelicUseOldLevel'] = iUseOldLevel


def EventSetChooseRelicCnt(oListener, oEventCB, iCnt):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['ChooseCnt'] = iCnt


def EventCBSetMaxLuckyHit(oListener, oEventCB, iMax):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LuckyHit' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iMax = cl_formula.GetResultByData(oListener, iMax, dEventInfo, dMsgInfo)
    if 'MaxLuckyHit' in dMsgInfo and iMax > dMsgInfo['MaxLuckyHit']:
        return None
    dMsgInfo['MaxLuckyHit'] = iMax


def EventCBAddWeaponUpgradeLevel(oListener, oEventCB, iLevel):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Args' not in dMsgInfo:
        return None
    dArgs = dMsgInfo['Args']
    if 'UpgradeLevel' not in dArgs:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iLevel = cl_formula.GetResultByData(oListener, iLevel, dEventInfo, dMsgInfo)
    dArgs['UpgradeLevel'] += iLevel


def EventRemoveFactorForFlowDam(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'FlowDam' not in dMsgInfo:
        return None
    lstFlowDam = dMsgInfo['FlowDam']
    lstDam = []
    for iDam, oReason in lstFlowDam:
        oReason2 = oReason.ExtInfo({
            'ThunderStrike': 1 })
        lstDam.append((iDam, oReason2))
    
    dMsgInfo['FlowDam'] = lstDam


def EventCBSetDamageRatio(oListener, oEventCB, iRatio, iPartRatio):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iRatio > 10000 or iRatio < 0:
        iRatio = 10000
        SendAlert('err', '%s回调设置骑乘怪伤害比例主体异常' % oEventCB.m_Key)
    if iPartRatio > 10000 or iPartRatio < 0:
        iPartRatio = 10000
        SendAlert('err', '%s回调设置骑乘怪伤害比例部位异常' % oEventCB.m_Key)
    dMsgInfo['PartRatio'] = iPartRatio
    dMsgInfo['BodyRatio'] = iRatio


def EventCBRemoveItem(oListener, oEventCB, iItem):
    oItem = oListener.m_ItemCon.GetItemBySID(iItem)
    if not oItem:
        return None
    oListener.m_ItemCon.RemoveItem(oItem, 'eventRemoveItem')


def EventCBNextFrameUpdateAI(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    oGame = oListener.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oAgent = oTarget.m_Agent
        if oAgent:
            oAgent.m_GameSpace.CallDelayUpdate(oAgent, 1)
    


def EventCBConvertPredictDamToPoinType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PredictChange' not in dMsgInfo:
        return None
    lstPredictChange = dMsgInfo['PredictChange']
    iTotalDam = 0
    index = 0
    for idx, sAttr, iUseType in reversed(cl_formula.g_DamTypeSequence):
        if lstPredictChange[idx]:
            iTotalDam += lstPredictChange[idx]
            lstPredictChange[idx] = 0
        if iUseType == iType:
            index = idx
    
    lstPredictChange[index] = iTotalDam


def EventCBTriggerDropBullet(oListener, oEventCB, dNumber, dWeight, iTime, iUseCartoonPos, dOffset):
    oGame = oListener.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    lstHero = oGame.m_WarMgr.GetLiveHero()
    vListenerPos = oListener.GetPos()
    for _ in range(iTime):
        iBullet = ChooseKey(oGame, dWeight)
        dInfo = {
            iBullet: dNumber[iBullet] }
        for iHero in lstHero:
            oTarget = oGame.GetObject(iHero)
            if not oTarget:
                continue
            if iUseCartoonPos and 'Cartoon' in dMsgInfo:
                vPos = dMsgInfo['Cartoon'].get('CurPos', vListenerPos)
            else:
                vPos = vListenerPos
            if dOffset:
                iAngle = oGame.Random(dOffset['angle'])
                iAngle = iAngle if oGame.Random(2) else -iAngle
                vDir = cl_math.RotateAroundVector(oListener.GetFacing(), (0, 1, 0), iAngle)
                if not cl_math.IsZero(vDir):
                    iLen = oGame.Random(dOffset['random']) + dOffset['min']
                    vPos = cl_math.Vec3DisplaceDir(vPos, vDir, iLen)
            sKey = GetCommonEventKey(dEventInfo)
            lstDropInfo = [
                dInfo]
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_BULLET,
                    'DropInfo': lstDropInfo,
                    'DropPos': vPos } }
            cl_reward.RewardItem(oListener.m_Game, oTarget, [
                dReward], sKey, {
                'Player': oTarget.m_ID,
                'Scene': oListener.m_Scene })
        
    


def EventCBTriggerKillEffect(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    oAttack = oGame.GetObject(dMsgInfo['AID'])
    oVictim = oGame.GetObject(dMsgInfo['VID'])
    if not oVictim or not oAttack:
        return None
    oVictim.SendKillMsg(oAttack, dMsgInfo)


def EventCBSetCurseRelicValidRemove(oListener, oEventCB):
    
    def ClearFunc(oListener, oLifeCycle):
        oListener.SetRemoveCurseRelicValid(0)

    oListener.SetRemoveCurseRelicValid(1)
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddDisableFunc(ClearFunc)


def EventCBShieldAndArmor2HP(oListener, oEventCB, iAddTip = True):
    
    def ClearFunc(oTarget, oLifeCycle):
        dDefend2HP = oListener.Query('Defend2HP', { })
        if sKey in dDefend2HP:
            dDefend2HP.pop(sKey)

    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    iHPMaxAdd = 0
    if oListener.m_DefendTrend & DEFEND_TREND_SHIELD:
        oAttr = oListener.GetAttr('ShieldMax')
        iHPMaxAdd += oAttr.GetExcludeValue()
    if oListener.m_DefendTrend & DEFEND_TREND_ARMOR:
        oAttr = oListener.GetAttr('ArmorMax')
        iHPMaxAdd += oAttr.GetExcludeValue()
    sKey = oLifeCycle.Key()
    sAttr = 'HPMax'
    oLifeCycle.m_Apply[sAttr] = 1
    oListener.AttrChange(sAttr, 0, iHPMaxAdd, sKey)
    if iAddTip:
        dDefend2HP = oListener.Query('Defend2HP', { })
        dDefend2HP[sKey] = 1
        oListener.Set('Defend2HP', dDefend2HP)
        sUniqueKey = 'EventCBShieldAndArmor2HP'
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def EventCBExcessShieldAndArmor2HP(oListener, oEventCB):
    
    def ClearFunc(oTarget, oLifeCycle):
        iBaseVal = oTarget.m_ExcessHP
        oTarget.TrueModifyExcessAttr('HP', -iBaseVal)
        fRatio = oTarget.m_ExcessHPRatio
        iVal = int(iBaseVal / fRatio) if fRatio else iBaseVal
        if oListener.m_DefendTrend & DEFEND_TREND_SHIELD:
            oTarget.TrueModifyExcessAttr('Shield', iVal)
        if oListener.m_DefendTrend & DEFEND_TREND_ARMOR:
            oTarget.TrueModifyExcessAttr('Armor', iVal)

    if oListener.m_ExcessShield > 0:
        iAdd = oListener.m_ExcessShield
        oListener.TrueModifyExcessAttr('Shield', -iAdd)
    elif oListener.m_ExcessArmor > 0:
        iAdd = oListener.m_ExcessArmor
        oListener.TrueModifyExcessAttr('Armor', -iAdd)
    else:
        return None
    oListener.AddExcessAttr('HP', iAdd)
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sUniqueKey = '%s-ExcessShieldAndArmor2HP' % oEventCB.m_Key
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def EventCBChangeGSCashShopGoods(oListener, oEventCB):
    
    def ClearFunc(oListener, oLifeCycle):
        oListener.Set('ChangeGSCashShopGoods', 0)

    oListener.Set('ChangeGSCashShopGoods', 1)
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddDisableFunc(ClearFunc)


def EventCBChangeShopGoods(oListener, oEventCB, iPos, iSID, iCash, iCashType, iBuyNum, iHide, iExcGoodsType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo or 'GoodsMenu' not in dMsgInfo:
        return False
    iShopNpc = dMsgInfo['ShopNpc']
    oShopNpc = oListener.m_Game.GetObject(iShopNpc)
    if not oShopNpc:
        return False
    dGoods = dMsgInfo['GoodsMenu']
    if iExcGoodsType and iPos in dGoods and dGoods[iPos].m_GoodsType == iExcGoodsType:
        return False
    iCash = cl_formula.GetFormulaResult(oListener, iCash, {
        'Npc': iShopNpc })
    oGood = cl_shop.CreateGoodsByConfig(iSID, iCash, iCashType, iBuyNum, iHide)
    if not oGood:
        return False
    dGoods[iPos] = oGood
    return True


def EventCBChangeShopPosGoodsByMiniGameSID(oListener, oEventCB, iPos, iMiniGame, iMiniGameType, iCash, iCashType, iBuyNum, iHide, iPlus):
    oGame = oListener.m_Game
    clsMiniGame = oGame.m_WarData.GetMiniGameData(iMiniGame)
    if clsMiniGame.m_Type != iMiniGameType:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo or 'GoodsMenu' not in dMsgInfo:
        return None
    iShopNpc = dMsgInfo['ShopNpc']
    oShopNpc = oGame.GetObject(iShopNpc)
    if not oShopNpc:
        return None
    dGoodsMenu = dMsgInfo['GoodsMenu']
    if not oShopNpc.CanReplace(oListener, iPos, dGoodsMenu[iPos]):
        return None
    oGood = None
    if iMiniGameType == MG_EQUIP:
        oGood = GetEquipGood(oListener, iPos, clsMiniGame, iCash, iCashType, iBuyNum, iHide, dGoodsMenu, iPlus)
    elif iMiniGameType == MG_RELIC:
        oGood = GetRelicGood(oListener, iPos, clsMiniGame, iCash, iCashType, iBuyNum, iHide, dGoodsMenu, iPlus)
    if not oGood:
        return None
    dGoodsMenu[iPos] = oGood


def GetEquipGood(oListener, iPos, clsMiniGame, iCash, iCashType, iBuyNum, iHide, dGoodsMenu, iPlus):
    oGame = oListener.m_Game
    lstWeapon = list(clsMiniGame.GetChooseWeight(oListener))
    lstAllUnlockItem = oListener.Query('Illus')['Weapon']
    lstAllCanSellItem = cl_item.GetAllCanSellWeapon(oGame)
    lstAllItem = list(set(lstAllUnlockItem) & set(lstAllCanSellItem) & set(lstWeapon))
    for oGoods in dGoodsMenu.values():
        if oGoods.m_SID in lstAllItem and oGoods.m_GoodsType == VIRTUAL_ITEM_EQUIP and iPos != oGoods.m_Pos:
            lstAllItem.remove(oGoods.m_SID)
    
    if not lstAllItem:
        return None
    iReward = oGame.m_RandomMgr.ChooseKey('weapon%d' % oListener.m_ID, {
        'Select': lstAllItem })
    iGrade = cl_reward.GetWeaponRewardGrade(oGame)
    oEquip = cl_item.CreateEquip(oGame, iReward, iGrade, oOwner = oListener, iSource = ITEM_SOURCE_GOOD)
    if not oEquip:
        return None
    if oEquip.Type() & cl_item.EQUIP_TYPE_MAINWEAPON:
        oBulletcom = oEquip.GetComponent('Bullet')
        if oBulletcom:
            oBulletcom.BulletModify(oBulletcom.MaxBullet())
    if iPlus:
        oEquip.AddEnhance(1, 'shop')
    iCash = cl_formula.GetFormulaResult(oListener, iCash, { })
    dGoods = {
        'item': VIRTUAL_ITEM_EQUIP,
        'info': {
            'sid': oEquip.m_SID,
            'item': oEquip,
            'data': { } } }
    return cl_shop.CreateGoodsByData(oEquip.m_SID, VIRTUAL_ITEM_EQUIP, iCash, iCashType, iBuyNum, [
        dGoods], iHide)


def GetRelicGood(oListener, iPos, clsMiniGame, iCash, iCashType, iBuyNum, iHide, dGoodsMenu, iPlus):
    oGame = oListener.m_Game
    if not iPlus:
        iLevel = 1
    else:
        iLevel = 2
    setRelic = set(clsMiniGame.m_ChooseWeight)
    setAllUnlockRelic = oListener.Query('Illus')['Relic']
    lstAllCanSellRelic = cl_perform.GetAllCanSellRelic(oGame)
    lstAllRelic = list(setAllUnlockRelic & set(lstAllCanSellRelic) & setRelic)
    oRelicCon = oListener.m_RelicCon
    dFilterRelic = oRelicCon.GetFilterRelic()
    for oRelic in oRelicCon.m_PosPerform.values():
        if oRelic.m_SID in dFilterRelic and iLevel <= oRelic.m_Level and oRelic.m_SID in lstAllRelic:
            lstAllRelic.remove(oRelic.m_SID)
    
    for oGoods in dGoodsMenu.values():
        if oGoods.m_SID in lstAllRelic and iPos != oGoods.m_Pos:
            lstAllRelic.remove(oGoods.m_SID)
    
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    oChoosePool = oScene.m_ScenePreLoad.GetSceneChoosePool(oListener.m_ID)
    if oChoosePool:
        dRelic = oChoosePool.m_PreLoadData['Relic']
        for iRelic in dRelic:
            if iRelic in lstAllRelic:
                lstAllRelic.remove(iRelic)
        
    if not lstAllRelic:
        return None
    iReward = oGame.m_RandomMgr.ChooseKey('relic%d' % oListener.m_ID, {
        'Select': lstAllRelic })
    clsRelic = cl_perform.GetPerformModule(iReward)
    if not clsRelic:
        return None
    iQuality = clsRelic.m_Quality
    dArgs = {
        'RelicSID': iReward,
        'QualityCoff': QUALITY_FACTOR[iQuality] }
    iCash = cl_formula.GetFormulaResult(oListener, iCash, dArgs)
    dGoods = {
        'item': VIRTUAL_ITEM_RELIC,
        'info': {
            'sid': iReward,
            'data': { },
            'level': iLevel } }
    dMsgInfo = {
        'Relic': iReward }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oListener, dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_GOOD)
    if 'RelicDropLevel' in dMsgInfo:
        dGoods['info']['level'] = dMsgInfo['RelicDropLevel']
        iLevel = dMsgInfo['RelicDropLevel']
    if 'ReplaceRelicInfo' in dMsgInfo:
        iCanRepeat = dMsgInfo['RelicCanRepeat']
        iUseOldLevel = dMsgInfo['RelicUseOldLevel']
        setRelic = set()
        for oGoods in dGoodsMenu.values():
            if oGoods.m_GoodsType != VIRTUAL_ITEM_RELIC:
                continue
            setRelic.add(oGoods.m_SID)
        
        for iReplaceRelic, iReplaceLevel in dMsgInfo['ReplaceRelicInfo']:
            if not iCanRepeat and iReplaceRelic in setRelic:
                continue
            dGoods['info']['sid'] = iReplaceRelic
            dGoods['info']['level'] = iReplaceLevel
            if iUseOldLevel:
                clsPerform = cl_perform.GetPerformModule(iReplaceRelic)
                if clsPerform.m_MaxLevel >= iLevel:
                    dGoods['info']['level'] = iLevel
            iReward = iReplaceRelic
        
    return cl_shop.CreateGoodsByData(iReward, VIRTUAL_ITEM_RELIC, iCash, iCashType, iBuyNum, [
        dGoods], iHide)


def EventCBDelCurWeaponAllBeaconSummon(oListener, oEventCB):
    oCurWeapon = oListener.m_WieldCon.GetCurWeapon()
    lstSummon = list(oListener.m_SummonDict)
    if not lstSummon or not oCurWeapon:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo and dMsgInfo['ItemID'] != oCurWeapon.m_ID:
        return None
    oGame = oListener.m_Game
    for iCurSummon in lstSummon:
        oCurSummon = oGame.GetObject(iCurSummon)
        if not oCurSummon:
            continue
        if oCurSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
            continue
        if oCurSummon.m_SrcWeapon != oCurWeapon.m_ID:
            continue
        oCurSummon.Remove('ChangeWeapon')
    


def EventCBChangeSummonModel(oListener, oEventCB, iScale = 100):
    
    def ClearFunc(oListener, oLifeCycle):
        oListener.SetAttr('Scale', 100, BASEATTR_CLIENT)
        oListener.ClearSkillCheckArgs()

    if not iScale or oListener.m_FightType & WARRIOR_SUMMON != WARRIOR_SUMMON:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddDisableFunc(ClearFunc)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iScale = cl_formula.GetResultByData(oListener, iScale, dEventInfo, dMsgInfo)
    oListener.SetAttr('Scale', iScale, BASEATTR_CLIENT)
    fScale = iScale / 100
    tSkillCheckArgs = (oListener.SkillCheckArgs[0] * fScale, oListener.SkillCheckArgs[1] * fScale)
    oListener.SetSkillCheckArgs(tSkillCheckArgs[0], tSkillCheckArgs[1])


def EventCBChangeCostPierceByBeaconSummon(oListener, oEventCB):
    
    def ClearFunc(oListener, oLifeCycle):
        oSrcWeapon.Set('NoCostPierce', 0)
        lstSummon = list(oListener.m_SummonDict)
        if not lstSummon:
            return None
        oGame = oListener.m_Game
        for iCurSummon in lstSummon:
            oCurSummon = oGame.GetObject(iCurSummon)
            if not oCurSummon:
                continue
            if oCurSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
                continue
            if oCurSummon.m_SrcWeapon != oSrcWeapon.m_ID:
                continue
            oCurSummon.Remove('NoInscription')
        

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    oSrcWeapon = oListener.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
    if not oSrcWeapon:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oGame = oListener.m_Game
    iSummon = dMsgInfo['Summon'] if 'Summon' in dMsgInfo else dMsgInfo['summonId']
    oSummon = oGame.GetObject(iSummon)
    if iSummon in oListener.m_SummonDict:
        if not oSummon or oSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
            return None
        oSrcWeapon.Set('NoCostPierce', 1)
    elif not oSummon or oSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
        return None
    lstSummon = list(oListener.m_SummonDict)
    if not lstSummon:
        oSrcWeapon.Set('NoCostPierce', 0)
        oLifeCycle.AddDisableFunc(ClearFunc)
        return None
    for iCurSummon in lstSummon:
        oCurSummon = oGame.GetObject(iCurSummon)
        if not oCurSummon:
            continue
        if oCurSummon.m_FightType & WARRIOR_BEACON != WARRIOR_BEACON:
            continue
        if oCurSummon.m_SrcWeapon == oSrcWeapon.m_ID:
            oSrcWeapon.Set('NoCostPierce', 1)
            oLifeCycle.AddDisableFunc(ClearFunc)
            return None
    
    oSrcWeapon.Set('NoCostPierce', 0)
    oLifeCycle.AddDisableFunc(ClearFunc)


def DropRandomWeaponWithType(oWarrior, oEventCB, iType, iBulletType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oWarrior.m_Game
    dValid = oWarrior.Query('Illus')['Weapon']
    lstAllWeapon = []
    for iweapon in dValid:
        clsWeapon = cl_item.GetItemCls(iweapon)
        if iType and clsWeapon.m_Type != iType:
            continue
        if iBulletType and clsWeapon.GetBulletType() != iBulletType:
            continue
        lstAllWeapon.append(iweapon)
    
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        iWeapon = oGame.m_RandomMgr.ChooseKey('weapon%d' % oWarrior.m_ID, {
            'Select': lstAllWeapon })
        if not iWeapon:
            continue
        iGrade = cl_reward.GetWeaponRewardGrade(oGame)
        iNewInscriptionNum = 0
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.m_CurNode
        if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
            oWarData = oGame.m_WarData
            iLayer = oLevelCtrl.m_LayerNum + 1
            iGrade = oWarData.GetWeaponGrade(iLayer, 1, oGame)
            iNewInscriptionNum = oWarData.GetInscriptionNum(iLayer, 1, oLevelCtrl)
        oWeapon = cl_item.CreateEquip(oGame, iWeapon, iGrade, oOwner = oWarrior, iSource = ITEM_SOURCE_DROP)
        dMsgInfo = { }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEDROPWEAPON, oWarrior, dMsgInfo)
        if 'Enhance' in dMsgInfo:
            oWeapon.AddEnhance(dMsgInfo['Enhance'], dMsgInfo['Reason'])
        oInscriptionCom = oWeapon.GetComponent('Inscription')
        if oInscriptionCom and iNewInscriptionNum:
            oInscriptionCom.m_InscriptionNum = iNewInscriptionNum
            oInscriptionCom.AddInscription()
        lstDropData = [
            oWeapon]
        vDropPos = cl_reward.GetDropBasePos(oTarget)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPWEAPON, oWarrior, {
            'lstWeapon': lstDropData })
        oGame.GetResMgr().CreateDrop(oWarrior.m_Scene, NWARRIOR_DROP_EQUIP, vDropPos, lstDropData, { }, {
            'DropSource': oWarrior.m_PlayerID }, oWarrior.m_ID)
    


def EventCBDisableSealInscription(oWarrior, oEventCB, iLevel):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
    if not oWeapon:
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    oInscriptionCom.DisableSealedInscription(iLevel)


def EventCBEnableSealInscription(oWarrior, oEventCB, iLevel):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
    if not oWeapon:
        return None
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if not oInscriptionCom:
        return None
    oInscriptionCom.EnableSealedInscription(iLevel)


def EventCBChangeWeaponExtGrade(oListener, oEventCB, iGroup, iGrade):
    
    def ClearExtGrade(oTarget, oLifeCycle):
        sKey = oLifeCycle.Key()
        oWeapon = oTarget.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oWeapon.ClearExtGrade(sKey)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    elif 'ID' in dMsgInfo:
        iWeapon = dMsgInfo['ID']
    elif 'ReplaceID' in dMsgInfo:
        iWeapon = dMsgInfo['ReplaceID']
    else:
        SendAlert('err', '%s事件没有武器信息' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iGrade = cl_formula.GetResultByData(oListener, iGrade, dEventInfo, dMsgInfo)
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    oWeapon.AddExtGrade(sKey, iGroup, iGrade)
    oLifeCycle.AddDisableFunc(ClearExtGrade)


def EventCBChangeItemGradeBySource(oListener, oEventCB, iGrade, dSource):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Grade' not in dMsgInfo or 'Source' not in dMsgInfo:
        return None
    if dMsgInfo['Source'] not in dSource:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iOldGrade = dMsgInfo['Grade']
    iGrade = cl_formula.GetResultByData(oListener, iGrade, dEventInfo, dMsgInfo)
    iNewGrade = iOldGrade + iGrade
    dMsgInfo['Grade'] = iNewGrade


def EventCBChangeWeaponInscriptionNumBySource(oListener, oEventCB, iInscriptionType, iNum, dSource, iSubType = None):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Weapon' not in dMsgInfo or 'Source' not in dMsgInfo:
        return None
    if dMsgInfo['Source'] not in dSource:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    oInscriptionCom = dMsgInfo['Weapon'].GetComponent('Inscription')
    oInscriptionCom.ResetInscriptionByType(iInscriptionType, iNum)
    if iSubType and iSubType != INSCRIPTION_TYPE_GEMINI:
        iTargetTypeNum = oInscriptionCom.m_Type2Num[iInscriptionType] if iInscriptionType in oInscriptionCom.m_Type2Num else 0
        if iTargetTypeNum < iNum:
            iGeminiNum = oInscriptionCom.m_Type2Num[INSCRIPTION_TYPE_GEMINI] if INSCRIPTION_TYPE_GEMINI in oInscriptionCom.m_Type2Num else 0
            iReplaceNum = oInscriptionCom.m_InscriptionNum - iGeminiNum - iTargetTypeNum
            if iReplaceNum:
                oInscriptionCom.ResetInscriptionByType(iSubType, iReplaceNum, iKeepType = iInscriptionType)


def EventCBRandomAddWeaponEnhanceCntBySource(oListener, oEventCB, iRange, iProb, iCnt, dSource):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    iRange = cl_formula.GetResultByData(oListener, iRange, dEventInfo, dMsgInfo)
    iProb = cl_formula.GetResultByData(oListener, iProb, dEventInfo, dMsgInfo)
    if oListener.m_Game.Random(iRange) + 1 <= iProb:
        if 'Weapon' not in dMsgInfo or 'Source' not in dMsgInfo:
            return None
        if dMsgInfo['Source'] not in dSource:
            return None
        oWeapon = dMsgInfo['Weapon']
        oWeapon.AddEnhance(iCnt, '%s-EventCBEnhance' % sKey)


def EventCBAddWeaponIntentionType(oListener, oEventCB, iType):
    dType = oListener.Query('WeaponIntentionType', { })
    if iType not in dType:
        dType[iType] = 1
        oListener.Set('WeaponIntentionType', dType)


def EventCBTempChangeWeaponInsNumUpperLimit(oListener, oEventCB, iNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ExtraAttr' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    dMsgInfo['ExtraAttr']['TempInsNumUpperLimit'] = iNum


def EventCBRemoveTempWeaponInsNumUpperLimit(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'lstWeapon' not in dMsgInfo:
        return None
    lstWeapon = dMsgInfo['lstWeapon']
    for oWeapon in lstWeapon:
        oWeapon.RemoveTmp('TempInsNumUpperLimit')
    


def EventCBTempOpenWeaponExclusiveIns(oListener, oEventCB, iNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ExtraAttr' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    dMsgInfo['ExtraAttr']['TempExclusiveInscription'] = iNum


def EventCBRemoveTempOpenWeaponExclusiveIns(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'lstWeapon' not in dMsgInfo:
        return None
    lstWeapon = dMsgInfo['lstWeapon']
    for oWeapon in lstWeapon:
        oWeapon.RemoveTmp('TempExclusiveInscription')
    


def EventCBTempAddWeaponInsPropByType(oListener, oEventCB, iType, iAddProp):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ExtraAttr' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    sKey = oEventCB.m_Key
    iAddProp = cl_formula.GetResultByData(oListener, iAddProp, dEventInfo, dMsgInfo)
    if 'PropAddByType' in dMsgInfo['ExtraAttr'] and iType in dMsgInfo['ExtraAttr']['PropAddByType']:
        dMsgInfo['ExtraAttr']['PropAddByType'][iType][sKey] = iAddProp
    else:
        dMsgInfo['ExtraAttr']['PropAddByType'] = {
            iType: {
                sKey: iAddProp } }


def EventCBAddInscriptionByType(oListener, oEventCB, iNum, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Weapon' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    oInscriptionCom = dMsgInfo['Weapon'].GetComponent('Inscription')
    oInscriptionCom.m_InscriptionNum += iNum
    oInscriptionCom.ChooseInscriptionByType(iType, iNum)


def EventCBRandomAddInscriptionByExcType(oListener, oEventCB, iNum, dExcType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Weapon' not in dMsgInfo:
        return None
    dWeight = { }
    dAll = GetInscriptionLib()
    for iType in dAll:
        if iType in dExcType:
            continue
        dWeight[iType] = 1
    
    iChooseType = ChooseKey(oListener.m_Game, dWeight)
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    oInscriptionCom = dMsgInfo['Weapon'].GetComponent('Inscription')
    oInscriptionCom.m_InscriptionNum += iNum
    oInscriptionCom.ChooseInscriptionByType(iChooseType, iNum)


def EventCBChangeRandomElement(oListener, oEventCB, iPerform):
    
    def ClearPerformElementType(oListener, oLifeCycle):
        oPerform = oListener.GetPerform(iPerform)
        if not oPerform:
            return None
        sKey = oLifeCycle.Key()
        oPerform.m_ElementTypeObj.RemoveSetModify(sKey)

    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    lstElementType = list(cl_abnormalconf.g_AbnormalCheck.keys())
    oGame = oListener.m_Game
    iElementType = lstElementType[oGame.Random(len(lstElementType))]
    oPerform.m_ElementTypeObj.SetModify(sKey, iElementType)
    oLifeCycle.AddDisableFunc(ClearPerformElementType)


def EventGetTargetByStateAdder(oListener, oEventCB, iState):
    lstAdder = []
    dTransInfo = oEventCB.GetCBTransInfo()
    lstState = oListener.m_State.GetItems(iState)
    for oState in lstState:
        iAttack = oState.m_Attacker
        if iAttack not in lstAdder:
            lstAdder.append(iAttack)
    
    dTransInfo['TargetList'] = lstAdder


def EventCBGetRandomCurseRelic(oListener, oEventCB, iCnt = 1):
    dCurse = oListener.m_RelicCon.GetChooseCurseRelic()
    if not dCurse:
        return None
    if not iCnt or iCnt <= 1:
        iRelic = ChooseKey(oListener.m_Game, dCurse)
        lstReward = [
            {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iRelic,
                    'level': 1 } }]
    else:
        lstRelic = ChooseMulKeys(oListener.m_Game, dCurse, iCnt)
        lstReward = []
        for iRelic in lstRelic:
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iRelic,
                    'level': 1 } }
            lstReward.append(dReward)
        
    sReason = oEventCB.m_Key
    cl_reward.RewardItem(oListener.m_Game, oListener, lstReward, sReason)


def EventCBRemoveRandomCurseRelic(oListener, oEventCB, iNotify = 0):
    lstCurse = oListener.m_RelicCon.GetAllRelicByType(RELIC_TYPE_CURSE)
    if not lstCurse:
        return None
    oGame = oListener.m_Game
    oRelic = lstCurse[oGame.Random(len(lstCurse))]
    oListener.m_RelicCon.RemoveRelic(oRelic.m_SID, 'eventRemoveRelic', 1)
    lstPlayer = [
        oListener.m_PlayerID]
    if iNotify:
        cl_notify.SendCommonNotify(oListener.m_Game, lstPlayer, 2418, {
            '$name': oRelic.m_Name })


def EventCBSubTargetCareerPerformColdTime(oListener, oEventCB, iTime, iPercent):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        pfobj = oTarget.GetCareerPerform()
        if not pfobj:
            continue
        iPerform = pfobj.m_SID
        iColdTimeFrame = oTarget.m_Perform.GetTotalColdTime(iPerform)
        if not iColdTimeFrame:
            continue
        iTime = cl_formula.GetResultByData(oTarget, iTime, dEventInfo, dMsgInfo)
        iFrame = Time2Frame(iTime)
        iPercent = cl_formula.GetResultByData(oTarget, iPercent, dEventInfo, dMsgInfo)
        if iPercent > 0:
            iMaxColdTimeFrame = oTarget.m_Perform.GetMaxColdTime(iPerform)
            iFrame += iMaxColdTimeFrame * iPercent // 100
        oTarget.m_Perform.ModifyColdTime(iPerform, -iFrame)
    


def EventCBSubTargetPerformColdTime(oListener, oEventCB, iPerform, iTime, iPercent):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            continue
        iColdTimeFrame = oTarget.m_Perform.GetTotalColdTime(iPerform)
        if not iColdTimeFrame:
            continue
        iTime = cl_formula.GetResultByData(oTarget, iTime, dEventInfo, dMsgInfo)
        iFrame = Time2Frame(iTime)
        iPercent = cl_formula.GetResultByData(oTarget, iPercent, dEventInfo, dMsgInfo)
        if iPercent > 0:
            iMaxColdTimeFrame = oTarget.m_Perform.GetMaxColdTime(iPerform)
            iFrame += iMaxColdTimeFrame * iPercent // 100
        oTarget.m_Perform.ModifyColdTime(iPerform, -iFrame)
    


def EventCBSubEventPerformColdTime(oListener, oEventCB, iTime, iPercent):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        oTarget = oSkill.GetAttack()
        if not oTarget:
            return None
        iPerform = oSkill.m_Base['pfid']
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            return None
        iColdTimeFrame = oTarget.m_Perform.GetTotalColdTime(iPerform)
        if not iColdTimeFrame:
            return None
        iTime = cl_formula.GetResultByData(oTarget, iTime, dEventInfo, dMsgInfo)
        iFrame = Time2Frame(iTime)
        iPercent = cl_formula.GetResultByData(oTarget, iPercent, dEventInfo, dMsgInfo)
        if iPercent > 0:
            iMaxColdTimeFrame = oTarget.m_Perform.GetMaxColdTime(iPerform)
            iFrame += iMaxColdTimeFrame * iPercent // 100
        oTarget.m_Perform.ModifyColdTime(iPerform, -iFrame)
    elif 'Perform' in dMsgInfo and 'Owner' in dMsgInfo:
        iPerform = dMsgInfo['Perform']
        iOwner = dMsgInfo['Owner']
        oGame = oListener.m_Game
        oTarget = oGame.GetObject(iOwner)
        if not oTarget:
            return None
        oPerform = oTarget.GetPerform(iPerform)
        if not oPerform:
            return None
        iTime = cl_formula.GetResultByData(oTarget, iTime, dEventInfo, dMsgInfo)
        iFrame = Time2Frame(iTime)
        iPercent = cl_formula.GetResultByData(oTarget, iPercent, dEventInfo, dMsgInfo)
        if iPercent > 0:
            iMaxColdTimeFrame = oPerform.m_Container.GetColdTime(iPerform)
            iFrame += iMaxColdTimeFrame * iPercent // 100
        oPerform.ModifyColdTime(oTarget, -iFrame)


def EventCBSubSelfColdTime(oListener, oEventCB, iCDTime):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    if not pfobj.InColdTime():
        return None
    iTime = cl_formula.GetResultByData(oListener, iCDTime, dEventInfo, dMsgInfo)
    iFrame = Time2Frame(iTime)
    if iFrame > 0:
        pfobj.ModifyColdTime(oListener, -iFrame)


def EventCBRemoveMonsterfromTargetList(oListener, oEventCB, iFightType, iExculueKey = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    lstTarget = []
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_FightType & iFightType == iFightType:
            continue
        if oTarget.QueryBitAttr('SpecialKey') & iExculueKey:
            continue
        lstTarget.append(iTarget)
    
    dTrans['TargetList'] = lstTarget


def EventCBCreateRandomNumMonster(oListener, oEventCB, iDivedeNum, dNumPivot, iIgnoreOwner, iAf, iPlus, iUseCurCategory, dExcMonster = None, dMonsterRelicInfo = None, dAttrChange = None, iReward = 1, iLimit = 0):
    if not oListener.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
        return None
    if not oListener.m_LineIdx:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iDivedeNum = cl_formula.GetResultByData(oListener, iDivedeNum, dEventInfo, dMsgInfo)
    oGame = oListener.m_Game
    iScene = oListener.m_Scene
    vCenterPos = oListener.GetPos()
    fModelRadius = oListener.m_ModelRadius
    fSize = fModelRadius * 2 + 0.2
    iCenterIndex = (iDivedeNum - 1) // 2
    (px, py, pz) = vCenterPos
    tLine = oListener.m_LineIdx
    lstPos = []
    for iRow in range(iDivedeNum):
        x = px + (iRow - iCenterIndex) * fSize
        for iCol in range(iDivedeNum):
            if iIgnoreOwner and iRow == iCenterIndex and iCol == iCenterIndex:
                continue
            z = pz + (iCol - iCenterIndex) * fSize
            vTmpPos = (x, py, z)
            (iRet, vBoxPos) = oGame.Scene_GetSpace(iScene, vTmpPos)
            if not iRet:
                continue
            if abs(vBoxPos[0] - x) > 0.1 or abs(vBoxPos[2] - z) > 0.1:
                continue
            vRetPos = oGame.Scene_NavMeshRayCast(iScene, vCenterPos, vBoxPos)
            if vRetPos != vBoxPos:
                continue
            lstPos.append(vRetPos)
        
    
    iChooseNum = ChooseKey(oGame, dNumPivot)
    if iLimit:
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        iCurCnt = 0
        iLimit = cl_formula.GetResultByData(oListener, iLimit, dEventInfo, dMsgInfo)
        lstMonster = oScene.GetObjectsByType('Monster')
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if oMonster and oMonster.Query('CreatedMonster', 0):
                iCurCnt += 1
        
        if iCurCnt >= iLimit - iChooseNum:
            iChooseNum = iLimit - iCurCnt
    if not lstPos or not iChooseNum:
        return None
    iLen = len(lstPos)
    if iLen <= iChooseNum:
        lstChoosePos = lstPos
    else:
        for _ in range(iChooseNum):
            iRandIndex = oGame.Random(iLen)
            lstPos[iRandIndex] = lstPos[iLen - 1]
            lstPos[iLen - 1] = lstPos[iRandIndex]
            iLen -= 1
        
        lstChoosePos = lstPos[-iChooseNum:]
    dAI = {
        'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
        'AIMethod': MONSTERAI_TYPE_DEFAULT }
    dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
    dAI.update(dHateSearchAI)
    tFace = oListener.GetFacing()
    iAddGrade = oListener.m_AddGrade
    dExtInfo = { }
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    if iAf:
        iSuperLevel = 0
        oMonsterSuper = oGame.m_WarMgr.GetComponent('MonsterSuper')
        if oMonsterSuper:
            iSuperLevel = oMonsterSuper.GetMonsterSuperLevel(oLevelNode.m_LevelType)
        else:
            iSuperLevel = oLevelCtrl.m_LayerNum
        dExtInfo = {
            'DefaultSuper': (iSuperLevel, iPlus, iAf) }
    dChoosePool = GetChoosePool(oGame, oListener, oLevelNode, dExcMonster) if iUseCurCategory else { }
    vFixDropPos = oListener.Query('FixDropPos')
    dCheckDropInfo = oListener.Query('CheckDropInfo')
    lstDisableRelic = list(dMonsterRelicInfo['Disable']) if 'Disable' in dMonsterRelicInfo else []
    dMonsterRelic = dMonsterRelicInfo['Enable'] if 'Enable' in dMonsterRelicInfo else { }
    oMonsterRelicElement = oGame.m_WarMgr.GetComponent('MonsterRelicElement') if lstDisableRelic else None
    for vPos in lstChoosePos:
        iMonster = ChooseKey(oGame, dChoosePool) if dChoosePool else oListener.m_SID
        oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonster, vPos, tFace, SIDE_TYPE_MONSTER, iAddGrade, dAI, tLine, dExtInfo)
        if not oMonster:
            continue
        oMonster.Set('CreatedMonster', 1)
        if not iReward:
            oMonster.m_Reward = { }
        if iUseCurCategory:
            tSuperInfo = oListener.Query('MonsterSuper')
            if tSuperInfo:
                oMonsterSuper = oGame.m_WarMgr.GetComponent('MonsterSuper')
                iSuperLevel = oListener.SuperLevel()
                iLevelType = oLevelNode.m_LevelType
                (iAfPF, iPlusPF) = oMonsterSuper.RandomMonsterSuperInfo(oMonster, None, iLevelType)
                if iAfPF and iPlusPF:
                    oMonster.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)
        for sAttr, dOp in dAttrChange.items():
            iMul = cl_formula.GetResultByData(oListener, dOp['Mul'], dEventInfo, dMsgInfo) if 'Mul' in dOp else 0
            iAdd = cl_formula.GetResultByData(oListener, dOp['Add'], dEventInfo, dMsgInfo) if 'Add' in dOp else 0
            if sAttr == 'HP':
                oMonster.m_HP = (oMonster.m_HP + iAdd) * (10000 + iMul) // 10000
            if sAttr == 'Shield':
                oMonster.m_Shield = (oMonster.m_Shield + iAdd) * (10000 + iMul) // 10000
            if sAttr == 'Armor':
                oMonster.m_Armor = (oMonster.m_Armor + iAdd) * (10000 + iMul) // 10000
            oMonster.GS2CPropChange(sAttr)
        
        if vFixDropPos:
            oMonster.Set('FixDropPos', vFixDropPos)
        if dCheckDropInfo:
            oMonster.Set('CheckDropInfo', dCheckDropInfo)
        for iRelic, iLevel in dMonsterRelic.items():
            clsRelic = cl_perform.GetPerformModule(iRelic)
            if not clsRelic or clsRelic.m_PFType != PF_TYPE_RELIC:
                continue
            if oMonster.m_Perform.GetPerform(iRelic):
                continue
            oMonster.AddPerform(iRelic, iLevel)
        
        if oMonsterRelicElement:
            oMonsterRelicElement.MonsterDisableRelicList(oMonster, lstDisableRelic)
    


def GetChoosePool(oGame, oListener, oLevelNode, dExcMonster):
    dChoosePool = { }
    iTargetFightType = 0
    for iFightType in (WARRIOR_NORMAL, WARRIOR_ELITE):
        if oListener.m_FightType & iFightType == iFightType:
            iTargetFightType = iFightType
            break
    
    if not iTargetFightType:
        return None
    for lstLine in oLevelNode.m_RoomList:
        for oLine in lstLine:
            for _, dGroup in oLine.m_MonsterCtrl.m_GroupInfo.items():
                ChooseFromWaitMonsters(dGroup['Wait'], iTargetFightType, dExcMonster, dChoosePool)
            
        
    
    return dChoosePool


def ChooseFromWaitMonsters(dWait, iFightType, dExcMonster, dChoosePool):
    for _, lstInfo in dWait.items():
        for dInfo in lstInfo:
            iMonsterSID = dInfo.get('MonsterSID', 0)
            if iMonsterSID not in dChoosePool and iMonsterSID not in dExcMonster:
                iCategory = dInfo.get('BaseSID', 0)
                clsData = GetMonsterConfig(iCategory)
                if clsData and iFightType and clsData.m_FightType & iFightType == iFightType:
                    dChoosePool[iMonsterSID] = 1
        
    


def EventCBRefreshStateArgs(oListener, oEventCB, iState, dArgs):
    lstState = oListener.m_State.GetItems(iState)
    if not lstState:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'pfid' not in dEventInfo:
        return None
    iPerform = dEventInfo['pfid']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dArgs = cl_formula.CalArgsFormula(oListener, dArgs, dEventInfo, dMsgInfo)
    for oState in lstState:
        if not oState.m_Enable:
            continue
        oReason = oState.m_Reason
        if oReason.m_Type != REASON_TYPE_PERFORM:
            continue
        if oReason.m_Perform != iPerform:
            continue
        oState.UpdateStateInfo(dArgs)
        oState.m_LifeCycle.CallFunc('Enable', oListener)
    


def EventCBRemoveSummonBySummonOwner(oListener, oEventCB, iSummonSID):
    if oListener.m_FightType & WARRIOR_SUMMON != WARRIOR_SUMMON:
        return None
    oGame = oListener.m_Game
    oOwner = oGame.GetObject(oListener.m_Owner)
    if not oOwner:
        return None
    oReason = cl_object.reason.CStrReason(oEventCB.m_Key, None, {
        'DamType': DAM_TYPE_SCENE | DAM_USE_HP })
    for iSummonID in list(oOwner.m_SummonDict):
        oSummon = oGame.GetObject(iSummonID, PY_FLAG_DEAD)
        if not oSummon or oSummon.m_SID != iSummonSID:
            continue
        oSummon.HPModifyDam(oListener.m_ID, [
            [
                oSummon.HP(),
                oReason]])
    


def EventCBBreakTargetProtection(oListener, oEventCB, iDamUse, bNoBoss, bNoElite):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        iFightType = oTarget.m_FightType
        if bNoBoss and iFightType & WARRIOR_BOSS == WARRIOR_BOSS:
            continue
        if bNoElite and iFightType & WARRIOR_ELITE == WARRIOR_ELITE:
            continue
        oReason = dEventInfo['RS'].ExtInfo({
            'ShowTips': 0,
            'DamType': DAM_TYPE_TRUE | iDamUse })
        iVal = 0
        if iDamUse & DAM_USE_SHIELD == DAM_USE_SHIELD:
            iVal += oTarget.Shield()
        if iDamUse & DAM_USE_ARMOR == DAM_USE_ARMOR:
            iVal += oTarget.Armor()
        if iDamUse & DAM_USE_HP == DAM_USE_HP:
            iVal += oTarget.HP()
        lstChange = [
            (iVal, oReason)]
        oTarget.HPModifyDam(oTarget.m_ID, lstChange)
    


def EventCBChangeMainDamage(oListener, oEventCB, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    for idx, (iDam, oReason) in enumerate(dMsgInfo['MainDam']):
        iDam = iDam * (10000 + iMul) // 10000 + iAdd
        dMsgInfo['MainDam'][idx] = [
            iDam,
            oReason]
    


def EventCBAddTargetCDByMark(oListener, oEventCB, sMark, iTime, iUseOwner = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    sKey = sMark + 'CDMark'
    iNowFrame = oListener.m_Game.GetFrameNum()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iFrame = Time2Frame(iTime)
    if iUseOwner and oListener.m_Owner:
        iRecodeID = oListener.m_Owner
    else:
        iRecodeID = oListener.m_ID
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        dMarkCDInfo = oTarget.Query(sKey, { })
        dMarkCDInfo[iRecodeID] = (iNowFrame, iFrame)
        oTarget.Set(sKey, dMarkCDInfo)
    


def EventCBSubTargetCDByMark(oListener, oEventCB, sMark, iTime):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    sKey = sMark + 'CDMark'
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iFrame = Time2Frame(iTime)
    iListener = oListener.m_ID
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        dMarkCDInfo = oTarget.Query(sKey, { })
        if iListener in dMarkCDInfo:
            (iStartFrame, iOldFrame) = dMarkCDInfo[oListener.m_ID]
            dMarkCDInfo[oListener.m_ID] = (iStartFrame, iOldFrame - iFrame)
            oTarget.Set(sKey, dMarkCDInfo)
    


def EventCBAddTargetNoSourceCDByMark(oListener, oEventCB, sMark, iTime):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    sKey = sMark + 'NoSourceCDMark'
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iTimeoutFrame = oListener.m_Game.GetFrameNum() + Time2Frame(iTime)
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        oTarget.Set(sKey, iTimeoutFrame)
    


def EventCBGetRandomRelic(oListener, oEventCB, dExcludeRelic):
    setUnlockRelic = oListener.Query('Illus')['Relic']
    lstHasRelic = oListener.m_RelicCon.GetAllPerformSID()
    dChooseRelic = { }
    for iRelic in setUnlockRelic:
        if iRelic in dExcludeRelic:
            continue
        if iRelic in lstHasRelic:
            continue
        dChooseRelic[iRelic] = 1
    
    if not dChooseRelic:
        return None
    iRelic = ChooseKey(oListener.m_Game, dChooseRelic)
    sReason = oEventCB.m_Key
    dReward = {
        'item': VIRTUAL_ITEM_RELIC,
        'info': {
            'sid': iRelic,
            'level': 1 } }
    cl_reward.RewardItem(oListener.m_Game, oListener, [
        dReward], sReason)


def EventCBCopyRelic(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iRelic = dMsgInfo['iPerform'] if 'iPerform' in dMsgInfo else 0
    if iRelic and iRelic not in oListener.m_RelicCon.m_Perform:
        iLevel = dMsgInfo['Level'] if 'Level' in dMsgInfo else 1
        clsPerform = cl_perform.GetPerformModule(iRelic)
        iLevel = iLevel if iLevel <= clsPerform.m_MaxLevel else clsPerform.m_MaxLevel
        sReason = oEventCB.m_Key
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iRelic,
                'level': iLevel } }
        cl_reward.RewardItem(oListener.m_Game, oListener, [
            dReward], sReason)


def EventCBRandomReplaceRelicBySourceRelic(oListener, oEventCB, dExcludeRelic, iChat = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' not in dMsgInfo or 'Level' not in dMsgInfo:
        return None
    iSourceRelic = dMsgInfo['iPerform']
    iLevel = dMsgInfo['Level']
    clsSourcePerform = cl_perform.GetPerformModule(iSourceRelic)
    setUnlockRelic = oListener.Query('Illus')['Relic']
    lstHasRelic = oListener.m_RelicCon.GetAllRelicSID()
    dChooseRelic = { }
    oGame = oListener.m_Game
    for iRelic in setUnlockRelic:
        if iRelic in dExcludeRelic:
            continue
        if iRelic in lstHasRelic:
            continue
        clsPerform = cl_perform.GetPerformModule(iRelic)
        if clsSourcePerform.m_Quality != clsPerform.m_Quality:
            continue
        if clsPerform.m_MaxLevel < iLevel:
            continue
        dChooseRelic[iRelic] = 1
    
    if dChooseRelic:
        iRelic = ChooseKey(oGame, dChooseRelic)
        if iChat:
            clsRelic = cl_perform.GetPerformModule(iRelic)
            cl_notify.SendCommonNotify(oGame, [
                oListener.m_PlayerID], iChat, {
                '$name': clsRelic.m_Name })
        else:
            iRelic = iSourceRelic
    dMsgInfo['iPerform'] = None


def EventCBUpdateTargetCDByMark(oListener, oEventCB, sMark, iTime):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    sKey = sMark + 'CDMark'
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iFrame = Time2Frame(iTime)
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        dMarkCDInfo = oTarget.Query(sKey, { })
        if not dMarkCDInfo:
            continue
        if oListener.m_ID in dMarkCDInfo:
            (iStartCDFrame, iRecordCDFrame) = dMarkCDInfo[oListener.m_ID]
            dMarkCDInfo[oListener.m_ID] = (iStartCDFrame, iFrame)
        oTarget.Set(sKey, dMarkCDInfo)
    


def EventCBRemoveTarget(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if oTarget:
            oTarget.DieClearEffect()
            oTarget.Remove(oLifeCycle.Key())
    


def EventCBWeaponClientBehavior(oListener, oEventCB, iBehavior, iStop):
    iItemID = 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        iItemID = dMsgInfo['ItemID']
    oGame = oListener.m_Game
    cl_snetwar.GS2CTriggerBehavior(oGame, oListener.m_ID, iBehavior, [
        oListener.m_PlayerID], iStop, iItemID)


def EventCBSetPerformActNumInfo(oListener, oEventCB, iValue, iTime):
    
    def ClearFunc(oListener, oLifeCycle, iActNum):
        dPerformInfo = oListener.Query(sKey, { })
        if iActNum in dPerformInfo:
            dPerformInfo.pop(iActNum)
            oListener.Set(sKey, dPerformInfo)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    iActNum = oSkill.m_Base['ActNum']
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key() + 'ParentActNum'
    dPerformInfo = oListener.Query(sKey, { })
    dPerformInfo[iActNum] = iValue
    oListener.Set(sKey, dPerformInfo)
    oListener.Call_Out(Functor(ClearFunc, oListener, oLifeCycle, iActNum), Time2Frame(iTime), 'ClearParentActNum')


def EventCBGetPerformActNumInfo(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    iPerentActNum = cl_perform.skillcache.GetSkillCacheByIndex(oSkill, SKILLCACHE_PARENTACTNUM)
    if not iPerentActNum:
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key() + 'ParentActNum'
    dPerformInfo = oListener.Query(sKey, { })
    if iPerentActNum not in dPerformInfo:
        return 0
    return dPerformInfo[iPerentActNum]


def EventCBGetHasStateTargetNum(oListener, oEventCB, iState):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    iTargetCnt = 0
    lstTar = dTransInfo['TargetList']
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if oTarget and oTarget.m_State.HasState(iState):
            iTargetCnt += 1
    
    return iTargetCnt


def EventCBGetTargetByDyingHero(oListener, oEventCB, iRange, iCount):
    oGame = oListener.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    lstDyingHero = []
    for iHero in oScene.GetHeros():
        if iHero == oListener.m_ID:
            continue
        oHero = oGame.GetObject(iHero)
        if not oHero or not oHero.IsDying():
            continue
        lstDyingHero.append(iHero)
    
    lstTar = []
    if lstDyingHero:
        dTarget = oGame.Scene_GetTargetDisMap(oListener.m_ID, lstDyingHero)
        dInTarget = { }
        for iTarget, iDis in dTarget.items():
            if iDis <= iRange:
                dInTarget[iTarget] = iDis
        
        lstSort = sorted(dInTarget.items(), key = (lambda x: x[1]))
        lstTar = [ x[0] for x in lstSort ]
    dTransInfo['TargetList'] = lstTar[:iCount] if iCount <= len(lstTar) else lstTar


def EventCBRelifeDyingTarget(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oRescueElement = oListener.m_Game.m_WarMgr.GetComponent('RescueElement')
    if not oRescueElement:
        return None
    oScene = oListener.m_Game.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    lstHero = oScene.GetHeros()
    for iTarget in dTrans['TargetList']:
        if iTarget not in lstHero:
            continue
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        if not oTarget.IsDying():
            continue
        oRescueElement.RescueRelife(oListener, iTarget)
    


def EventCBChangeCure(oListener, oEventCB, iChangeCureType, iMul, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainCure' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    if iMul:
        iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    for idx, lstCure in enumerate(dMsgInfo['MainCure']):
        (iCure, oReason) = lstCure
        if iChangeCureType and not (iChangeCureType & oReason.Query('DamType', 0)):
            continue
        iCure = iCure * (10000 + iMul) // 10000 + iAdd
        dMsgInfo['MainCure'][idx][0] = iCure
    


def EventCBChangeCureLimit(oListener, oEventCB, iChangeCureType, iLimitCure):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainCure' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iLimitCure = cl_formula.GetResultByData(oListener, iLimitCure, dEventInfo, dMsgInfo)
    for idx, lstCure in enumerate(dMsgInfo['MainCure']):
        (iCure, oReason) = lstCure
        if oReason.Query('DamType', 0) & iChangeCureType or iLimitCure < iCure:
            iCure = iLimitCure
        dMsgInfo['MainCure'][idx][0] = iCure
    


def EventCBAddAttackPFBullet(oTarget, oEventCB, pfid, iCnt):
    dEventInfo = oEventCB.GetCBEventInfo()
    iWeapon = 0
    if 'ItemID' in dEventInfo:
        iWeapon = dEventInfo['ItemID']
    elif 'RS' in dEventInfo:
        iWeapon = dEventInfo['RS'].Query('Item')
    oAttack = oTarget.m_Game.GetObject(dEventInfo['AID'])
    if not oAttack:
        return None
    oPerform = oAttack.GetPerform(pfid, iWeapon)
    if oPerform:
        oPerform.AddPFBullet(iCnt)


def EventCBAddHitPart(oTarget, oEventCB, iAddHitPart):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DamType' not in dMsgInfo:
        return None
    dMsgInfo['DamType'] = dMsgInfo['DamType'] | iAddHitPart


def EventCBModifyComb(oTarget, oEventCB, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Comb' not in dMsgInfo:
        return None
    dMsgInfo['Comb'] = iVal


def EventCBRemainQuality(oTarget, oEventCB, iAssignQuality, iNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iRemainQuality = dMsgInfo['RemainQuality']
    if iRemainQuality and iRemainQuality != iAssignQuality:
        SendAlert('err', f'''{oEventCB.m_Key}事件指定品质失败,已存在 {iRemainQuality}.''')
        return None
    dMsgInfo['RemainQuality'] = iAssignQuality
    dMsgInfo['RemainCnt'] = dMsgInfo['RemainCnt'] + iNum


def EventCBMonsterUseExtraRelic(oTarget, oEventCB, iMonsterRelic, iCount):
    oWarMgr = oTarget.m_Game.m_WarMgr
    oElement = oWarMgr.GetComponent('MonsterRelicElement')
    if not oElement:
        return None
    oElement.MonsterUseExtraRelic(oTarget, iMonsterRelic, iCount)


def EventCBUpdateShareWeaponInscription(oTarget, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    if pfobj.m_PFType != PF_TYPE_INSCRIPTION or pfobj.m_InscriptionType != INSCRIPTION_TYPE_GEMINI:
        return None
    oWeapon = pfobj.GetMyItem()
    if not oWeapon or not (oWeapon.Type() & itemdef.EQUIP_MASK_WEAPON):
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iItemID = dMsgInfo['ItemID']
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if iItemID == oWeapon.m_ID:
        oInscriptionCom.UpdateShareInscriptionEffect()
        return None
    oCon = oTarget.m_WieldCon
    oOtherWeapon = oCon.GetItemByID(iItemID)
    if not oOtherWeapon:
        return None
    iInscription = dMsgInfo['SID']
    if iAdd:
        lstHas = oInscriptionCom.m_Inscription
        clsPerform = cl_perform.GetPerformModule(iInscription)
        if not clsPerform.CheckValidItem(oWeapon, lstHas):
            return None
        oInscriptionCom.AddShareInscription(iInscription)
    else:
        oInscriptionCom.RemoveShareInscription([
            iInscription])


def EventCBChangeMonsterReward(oListener, oEventCB, iType, iTargetMG, iProbability):
    if not oListener.m_Reward:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    iRound = oGame.m_WarMgr.m_Round
    dReward = oListener.m_Reward
    if iRound not in dReward:
        iRound = sorted(dReward)[0]
    dReward = dReward[iRound]
    oWarData = oGame.m_WarData
    iAttack = dMsgInfo['AID']
    oAttack = oGame.GetObject(iAttack)
    iTransMG = 0
    for iMiniGame in dReward:
        clsMiniGame = oWarData.GetMiniGameData(iMiniGame)
        if clsMiniGame.m_Type != iType:
            continue
        iTransMG = iMiniGame
    
    if not iTransMG:
        return None
    (iRatio, iTimes) = dReward[iTransMG]
    iTimes = cl_minigame.GetMiniGameTimes(oGame, iRatio, iTimes, oListener, oAttack, iTransMG, MG_SOURCE_KILLMONSTER)
    iChange = 0
    for _ in range(iTimes):
        if oGame.Random(100) < iProbability:
            iChange += 1
    
    if iChange:
        dNewReward = dict(dReward)
        dNewReward[iTargetMG] = (iRatio, iChange)
        iRemain = iTimes - iChange
        if iRemain:
            dNewReward[iTransMG] = (iRatio, iRemain)
        else:
            dNewReward.pop(iTransMG)
        oListener.m_Reward[iRound] = dNewReward


def EventCBRemoveMonsterReward(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Monster' not in dMsgInfo:
        return None
    oMonster = oListener.m_Game.GetObject(dMsgInfo['Monster'])
    if not oMonster:
        return None
    oMonster.m_Reward = { }


def EventCBCostBagBulletByType(oListener, oEventCB, iType, iCost):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    iCost = cl_formula.GetResultByData(oListener, iCost, oEventCB.GetCBEventInfo())
    oListener.m_BulletCon.BulletModify(iType, -iCost, oEventCB.m_Key)
    dCollect = dMsgInfo['Skill'].m_Collect
    if 'OtherBulletUse' not in dCollect:
        dCollect['OtherBulletUse'] = {
            iType: iCost }
    elif iType not in dCollect['OtherBulletUse']:
        dCollect['OtherBulletUse'][iType] = iCost
    else:
        dCollect['OtherBulletUse'][iType] += iCost


def CalTeamSameWeaponInfo(oListener, oEventCB, iCalBulletType):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        return None
    lstWeapon = oListener.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
    dType = { }
    dWeaponSID = { }
    dBulletType = { }
    for oWeapon in lstWeapon:
        dType[oWeapon.m_Type] = 1
        dWeaponSID[oWeapon.m_SID] = 1
        if iCalBulletType:
            oBulletCom = oWeapon.GetComponent('Bullet')
            if oBulletCom:
                dBulletType[oBulletCom.BulletType()] = 1
    
    if 'Hero' not in dMsgInfo or dMsgInfo['Hero'] == oListener.m_ID:
        dSampleWeaponInfo = { }
    else:
        dSampleWeaponInfo = pfobj.GetArgValue('SampleWeaponInfo')
    if not dSampleWeaponInfo:
        dSampleWeaponInfo = { }
        lstRoomHero = oGame.m_WarMgr.GetRoomHero()
        lstHeros = []
        for iHero in lstRoomHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if oHero.IsDead():
                continue
            if oHero.m_ID == oListener.m_ID:
                continue
            lstHeros.append(iHero)
        
    else:
        lstHeros = [
            dMsgInfo['Hero']]
    (iSameType, iSameBulletType, iSameWeaponSID) = (0, 0, 0)
    for iHero in lstHeros:
        oHero = oGame.GetObject(iHero)
        lstWeapon = oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
        dTypeSign = { }
        dBulletTypeSign = { }
        dSIDSign = { }
        for oMateWeapon in lstWeapon:
            if oMateWeapon.m_Type not in dTypeSign and oMateWeapon.m_Type in dType:
                dTypeSign[oMateWeapon.m_Type] = 1
                iSameType += 1
            if oMateWeapon.m_SID not in dSIDSign and oMateWeapon.m_SID in dWeaponSID:
                dSIDSign[oMateWeapon.m_SID] = 1
                iSameWeaponSID += 1
            if iCalBulletType:
                oBulletCom = oMateWeapon.GetComponent('Bullet')
                if oBulletCom:
                    iBulletType = oBulletCom.BulletType()
                    if iBulletType not in dBulletTypeSign and iBulletType in dBulletType:
                        dBulletTypeSign[iBulletType] = 1
                        iSameBulletType += 1
        
        dSampleWeaponInfo[iHero] = [
            iSameType,
            iSameBulletType,
            iSameWeaponSID]
    
    pfobj.SetArgValue('SampleWeaponInfo', dSampleWeaponInfo)


def RemoveTeamSameWeaponInfo(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    pfobj = oLifeCycle.GetObject()
    if not pfobj:
        return None
    dSampleWeaponInfo = pfobj.GetArgValue('SampleWeaponInfo')
    if not dSampleWeaponInfo:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Hero' in dMsgInfo and dMsgInfo['Hero'] in dSampleWeaponInfo:
        dSampleWeaponInfo.pop(dMsgInfo['Hero'])


def EventTargetShareDamage(oListener, oEventCB, iShare, iUseDam, iShowTips, iDamType, iToDeath = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if not dTransInfo['TargetList']:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RS' not in dMsgInfo or dMsgInfo['RS'].Query('DamShare'):
        return None
    if 'Skill' not in dMsgInfo:
        return None
    if 'CurVID' in dMsgInfo:
        oMainCur = oListener.m_Game.GetObject(dMsgInfo['CurVID'])
    elif 'VID' in dMsgInfo:
        oMainCur = oListener.m_Game.GetObject(dMsgInfo['VID'])
    if not oMainCur:
        return None
    if 'DamFactor' in dMsgInfo:
        dTempDamFactor = dMsgInfo['DamFactor']
    elif 'Skill' in dMsgInfo and not iUseDam:
        oSkill = dMsgInfo['Skill']
        iVictim = oSkill.m_Update['CurVID']
        dVictim = oSkill.m_Update[iVictim]
        dTempDamFactor = dVictim['DamFactor']
    else:
        dTempDamFactor = {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } }
    iMainCurExtTotalHP = oMainCur.HP() + oMainCur.Armor() + oMainCur.Shield()
    lstMainDam = []
    iShareNums = len(dTransInfo['TargetList'])
    iShare = cl_formula.GetResultByData(oListener, iShare, oEventCB.GetCBEventInfo(), dMsgInfo)
    if 'MainDam' in dMsgInfo:
        for lstDam in dMsgInfo['MainDam']:
            (iDam, oReason) = lstDam
            iDam = min(iDam, iMainCurExtTotalHP) * iShare // 10000 // iShareNums
            lstMainDam.append([
                iDam,
                oReason])
        
    elif iUseDam and 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iUseDam = cl_formula.GetResultByData(oListener, iUseDam, oEventCB.GetCBEventInfo(), dMsgInfo)
        iDam = iUseDam * iShare // 10000 // iShareNums
        lstMainDam.append([
            iDam,
            oReason])
    elif 'RS' in dMsgInfo:
        oReason = dMsgInfo['RS']
        iDam = oReason.Query('InitDam')
        if iDam:
            iDam = min(iDam, iMainCurExtTotalHP) * iShare // 10000 // iShareNums
        lstMainDam.append([
            iDam,
            oReason])
    dTempDamage = {
        'AID': dMsgInfo['AID'],
        'CrazyEff': 0,
        'LuckyHit': 0,
        'RS': dMsgInfo['RS'].ExtInfo({
            'DamShare': {
                'Share': iShare } }),
        'FlowDam': dMsgInfo['FlowDam'] if 'FlowDam' in dMsgInfo else [],
        'LuckyHitEff': 0,
        'Skill': dMsgInfo['Skill'] }
    dExtInfo = {
        'DamShare': {
            'Share': iShare },
        'ShowTips': iShowTips }
    for iTarget in dTransInfo['TargetList']:
        oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        iTargetExtTotalHP = oTarget.HP() + oTarget.Armor() + oTarget.Shield()
        iDam = 0
        lstTempDam = []
        for lstDam in lstMainDam:
            iDam = min(lstDam[0], iTargetExtTotalHP - 100) if not iToDeath else lstDam[0]
            oReason = lstDam[1]
            if iDamType:
                iOldDamType = oReason.Query('DamType')
                dExtInfo['DamType'] = iOldDamType ^ iOldDamType & DAM_MASK_ELEMENT | iDamType
            lstTempDam.append([
                iDam,
                oReason.ExtInfo(dExtInfo)])
        
        if iDam < 100:
            continue
        dShareDamage = dTempDamage
        dShareDamage['MainDam'] = lstTempDam
        dShareDamage['DamFactor'] = DeepCopy(dTempDamFactor)
        dShareDamage['CurVID'] = iTarget
        oTarget.ReceiveDamage(dShareDamage['AID'], dShareDamage)
    


def EventCBSetNumTalentGen(oListener, oEventCB, iNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Num' not in dMsgInfo:
        return None
    dMsgInfo['Num'] = iNum


def EventAddCBNumTalentGen(oListener, oEventCB, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Num' not in dMsgInfo:
        return None
    iChangeNum = dMsgInfo['Num'] + iAdd
    if iChangeNum < 1:
        dMsgInfo['Num'] = 1
    elif iChangeNum > 3:
        dMsgInfo['Num'] = 3
    else:
        dMsgInfo['Num'] = iChangeNum


def EventCBSetSavedData(oListener, oEventCB, sFlag, iVal, iUseFormula):
    if iUseFormula:
        dEventInfo = oEventCB.GetCBEventInfo()
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    oListener.SetSavedData('save.' + sFlag, iVal)


def EventCBAddSavedData(oListener, oEventCB, sFlag, iAdd, iUseFormula):
    if iUseFormula:
        dEventInfo = oEventCB.GetCBEventInfo()
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oListener.AddSavedData('save.' + sFlag, iAdd)


def EventCBAddComb(oListener, oEventCB, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iComb = 0
    if 'Comb' in dMsgInfo and dMsgInfo['Comb']:
        iComb = dMsgInfo['Comb']
    elif oListener.m_SID == GAMBLER_HERO:
        iComb = oListener.m_GamblerCon.GetComb()
    dMsgInfo['Comb'] = min(iComb + iVal, 5)


def EventCBMonsterRelicCreateMonster(oListener, oEventCB, iRelic, iSummonLimit, iRoomSummonLimit, iEffectPf, iCDState, iRadius1, iRadius2, iAngle1, iAngle2, lstExcRelic):
    tPosArgs = (iRadius1, iRadius2, iAngle1, iAngle2)
    oElement = oListener.m_Game.m_WarMgr.GetComponent('MonsterRelicElement')
    if not oElement:
        return None
    iRoomCount = cl_formula.GetResultByData(oListener, iRoomSummonLimit, { })
    dInfo = {
        'Relic': iRelic,
        'SummonLimit': iSummonLimit,
        'RoomSummonLimit': iRoomCount,
        'EffectPf': iEffectPf,
        'CDState': iCDState,
        'PosArgs': tPosArgs,
        'ExcRelic': lstExcRelic }
    oElement.RelicCreateSummon(oListener, dInfo)


def EventCBAddMessageInfo(oListener, oEventCB, sKey, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    dMsgInfo[sKey] = iVal


def EventCbSetBallisticType(oListener, oEventCB, iType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oSkill.m_CacheData.SetBallisticType(iType)


def EventCbSaveCurTargetInStateData(oListener, oEventCB, iStateSID, iAddSelf, iCover = 1, iUpdateAlive = 0):
    oState = oListener.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList'][:]
    if iAddSelf and oListener.m_ID not in lstTar:
        lstTar.append(oListener.m_ID)
    if iCover or 'TargetData' not in oState.m_Data:
        oState.m_Data['TargetData'] = lstTar
    else:
        oState.m_Data['TargetData'].extend(lstTar)
    if iUpdateAlive:
        lstAlive = []
        oGame = oListener.m_Game
        for iTarget in oState.m_Data['TargetData']:
            oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
            if not oTarget:
                continue
            lstAlive.append(iTarget)
        
        oState.m_Data['TargetData'] = lstAlive


def EventCbGetTargetByStateTargetData(oListener, oEventCB, iStateSID):
    dTransInfo = oEventCB.GetCBTransInfo()
    lstTar = []
    dTransInfo['TargetList'] = lstTar
    oState = oListener.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    if 'TargetData' in oState.m_Data:
        lstTar.extend(oState.m_Data['TargetData'])


def EventCbUseSelfUpdateStateTargetData(oListener, oEventCB, iStateSID, iAdd):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if not oState:
            continue
        if ('TargetData' in oState.m_Data or not iAdd) and oListener.m_ID in oState.m_Data['TargetData']:
            oState.m_Data['TargetData'].remove(oListener.m_ID)
            continue
        if iAdd and oListener.m_ID not in oState.m_Data['TargetData']:
            oState.m_Data['TargetData'].append(oListener.m_ID)
    


def EventCBKillMonsterGroup(oListener, oEventCB, iGroup):
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLineNode = oLevelCtrl.GetLineNode(oListener.m_LineIdx)
    if not oLineNode:
        return None
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    if iGroup not in oMonsterCtrl.m_GroupInfo:
        return None
    dGroup = oMonsterCtrl.m_GroupInfo[iGroup]
    if not dGroup['Live']:
        return None
    oReason = cl_object.reason.CStrReason(f'''KillGroup-{iGroup}-{oEventCB.m_Key}''')
    sReason = oReason.GetStrReason()
    lstMonster = list(dGroup['Live'])
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        oMonster.Set('RelifeInfo', { })
        oMonster.SetDiePriority(DIE_PRIORITY_KILL, sReason)
        oMonster.HPDirectModify('HP', oListener.m_ID, -(oMonster.m_HP), oReason)
    


def EventCBGetTargetByMonsterGroup(oListener, oEventCB, iGroup):
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLineNode = oLevelCtrl.GetLineNode(oListener.m_LineIdx)
    if not oLineNode:
        return None
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    if iGroup not in oMonsterCtrl.m_GroupInfo:
        return None
    dGroup = oMonsterCtrl.m_GroupInfo[iGroup]
    if not dGroup['Live']:
        return None
    dTransInfo['TargetList'] = list(dGroup['Live'])


def EventCBMonsterHaltPFGroup(oListener, oEventCB):
    if not oListener.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
        return None
    oAgent = oListener.m_Agent
    if not oAgent:
        return None
    oAgent.UsePerformGroupEnd()


def EventGetTargetByMsgInfoSummon(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo['TargetList'] = []
    if 'Summon' not in dMsgInfo:
        return None
    dTransInfo['TargetList'].append(dMsgInfo['Summon'])


def EventCBRemoveMonsterGroupReward(oListener, oEventCB, iGroup, iSave):
    oGame = oListener.m_Game
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLineNode = oLevelCtrl.GetLineNode(oListener.m_LineIdx)
    if not oLineNode:
        return None
    oMonsterCtrl = oLineNode.m_MonsterCtrl
    if iGroup not in oMonsterCtrl.m_GroupInfo:
        return None
    dGroup = oMonsterCtrl.m_GroupInfo[iGroup]
    if not dGroup['Live']:
        return None
    if iSave:
        lstSaveMonster = []
        for iMonster in ShufferList(oGame, dGroup['Live']):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster or not (oMonster.m_Reward):
                continue
            if len(lstSaveMonster) != iSave:
                lstSaveMonster.append(iMonster)
                continue
            oMonster.m_Reward = { }
        
        LevelLog.Debug('%s %s map:%s level:%s group:%s savegroupreward %s' % (oGame.m_ID, oEventCB.Key(), oLineNode.m_LevelNode.m_Map, oLineNode.m_LevelNode.m_Level, iGroup, lstSaveMonster))
    else:
        for iMonster in dGroup['Live']:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            oMonster.m_Reward = { }
        


def EventCBGetTargetByEventMonster(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Monster' not in dMsgInfo:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = [
        dMsgInfo['Monster']]


def EventCBSetTargetRelifeInfo(oListener, oEventCB, iType, iTime, iTimes, iPriority, iHpRatio, iShieldRatio, iArmorRatio, iRelifeOnly = 0, dHatchRatio = None):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if iType not in TYPE_RELIFE_ALL:
        return None
    oLifeCycle = oEventCB.GetCBLifeCycle()
    sKey = oLifeCycle.GetStableKey()
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iTimes = cl_formula.GetResultByData(oListener, iTimes, dEventInfo)
    lstTar = dTransInfo['TargetList']
    dRatio = {
        'HPRatio': iHpRatio,
        'ShieldRatio': iShieldRatio,
        'ArmorRatio': iArmorRatio }
    iOwnerSID = oLifeCycle.GetObject().m_SID
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iRelifeOnly:
            iMaxHpRatio = GetTargetMaxRelifeHPRatio(oTarget)
            if not iMaxHpRatio:
                oTarget.AddRelifeInfo(iType, sKey, iTime, iTimes, iPriority, dRatio)
            if iMaxHpRatio < iHpRatio:
                dRelifeInfo = {
                    iType: {
                        sKey: [
                            iTime,
                            iTimes,
                            iTimes,
                            iPriority] } }
                oTarget.Set('RelifeInfo', dRelifeInfo)
                oTarget.Set('RelifeRatio', {
                    (iType, sKey): dRatio })
            else:
                oTarget.AddRelifeInfo(iType, sKey, iTime, iTimes, iPriority, dRatio)
        if None.m_FightType & WARRIOR_MONSTER:
            oTarget.AddHatchRatio(iOwnerSID, iType, sKey, dHatchRatio)
    


def GetTargetMaxRelifeHPRatio(oTarget):
    dRelifeInfo = oTarget.Query('RelifeInfo', { })
    if not dRelifeInfo:
        return 0
    iMaxHpRatio = 0
    dRelifeRatio = oTarget.Query('RelifeRatio', { })
    for iType, dType in dRelifeInfo.items():
        for sKey, (_, iTimes, _, _) in dType.items():
            if iTimes <= 0:
                continue
            tRelifeExtInfoKey = (iType, sKey)
            if tRelifeExtInfoKey not in dRelifeRatio:
                iMaxHpRatio = 100
                break
            iCurRelifeHpRatio = dRelifeRatio[tRelifeExtInfoKey]['HPRatio']
            if iMaxHpRatio < iCurRelifeHpRatio:
                iMaxHpRatio = iCurRelifeHpRatio
        
    
    return iMaxHpRatio


def EventCBReturnCost(oListener, oEventCB, iSendMsg):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Cost' not in dMsgInfo:
        return None
    iCost = dMsgInfo['Cost']
    if iCost:
        oListener.AddCash(iCost, oEventCB.m_Key, iSendMsg)


def EventCBGetUnLockedPosByDir(oListener, oEventCB, iDirect, iTargetPos):
    if not oListener.m_FightType & WARRIOR_HERO:
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo:
        return 0
    iShopNpc = dMsgInfo['ShopNpc']
    oShopNpc = oListener.m_Game.GetObject(iShopNpc)
    if not oShopNpc:
        return 0
    iTargetPos = cl_formula.GetResultByData(oListener, iTargetPos, oEventCB.GetCBEventInfo())
    dGoods = oShopNpc.m_GoodsData.get(oListener.m_ID, { })
    if iTargetPos not in dGoods:
        SendAlert('err', '%s目标位置为%s，下标应为商品列表中的有效位置' % (oEventCB.m_Key, iTargetPos))
        return 0
    lstGoods = list(dGoods)
    lstGoods.sort()
    iTargetIndex = lstGoods.index(iTargetPos)
    if iDirect:
        lstGoods = lstGoods[iTargetIndex:]
    else:
        lstGoods = lstGoods[:iTargetIndex + 1]
        lstGoods.reverse()
    dLockGoods = oShopNpc.m_LockGoods.get(oListener.m_ID, { })
    for iPos in lstGoods:
        if iPos not in dLockGoods:
            return iPos
    
    iMaxPos = max(dGoods)
    return iMaxPos + 1


def EventCBSetCustomData(oListener, oEventCB, sKey, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    oListener.Set(sKey, iVal)


def EventCBGetCustomData(oListener, oEventCB, sKey):
    return oListener.Query(sKey)


def EventCBAddCustomData(oListener, oEventCB, sKey, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    oListener.Add(sKey, iVal)


def EventCBAddTargetCustomData(oListener, oEventCB, sKey, iVal):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oTarget.Add(sKey, iVal)
    


def EventCBAddListenerTargetCustomData(oListener, oEventCB, sKey, iVal, iMax, iPassLevelClear):
    
    def ClearFunc(oListener, oLifeCycle):
        oListener.DelPassLayerClearKey(sKey)

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    iMax = cl_formula.GetResultByData(oListener, iMax, dEventInfo, dMsgInfo)
    dCustom = oListener.SetDefault(sKey, { })
    for iTarget in lstTar:
        if iTarget in dCustom:
            dCustom[iTarget] += iVal
        else:
            dCustom[iTarget] = iVal
        if dCustom[iTarget] > iMax:
            dCustom[iTarget] = iMax
    
    if iPassLevelClear:
        oListener.AddPassLayerClearKey(sKey)
        oLifeCycle = oEventCB.GetCBLifeCycle()
        oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def EventCBAddTargetListenerCustomData(oListener, oEventCB, sKey, iVal):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    iListener = oListener.m_ID
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        dCustom = oTarget.SetDefault(sKey, { })
        if iListener in dCustom:
            dCustom[iListener] += iVal
            continue
        dCustom[iListener] = iVal
    


def EventCBClearTargetListenerCustomData(oListener, oEventCB, sKey):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    iListener = oListener.m_ID
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        dCustom = oTarget.Query(sKey, { })
        dCustom.pop(iListener, None)
    


def EventCBDelTargetCustomData(oListener, oEventCB, sKey):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oTarget.Delete(sKey)
    


def EventCBAddTargetTimeLimitCustomData(oListener, oEventCB, sKey, iVal, iTime, iAppendListener = 0, iAppendSkillActNum = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    oGame = oListener.m_Game
    iLastFrame = oGame.GetFrameNum() + Time2Frame(iTime)
    if iAppendListener:
        sKey = '%s-%d' % (sKey, oListener.m_ID)
    if iAppendSkillActNum and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iActNum = oSkill.m_Base['ActNum']
        sKey = sKey + '-%d' % iActNum
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        dCustomData = oTarget.SetDefault(sKey, { })
        dCustomData[iVal] = iLastFrame
    


def EventCBGetTargetCustomDataByEnableTime(oListener, oEventCB, sKey, iDeOrder = 0, iAppendListener = 0, iAppendSkillActNum = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(lstTar[0])
    if not oTarget:
        return 0
    if iAppendListener:
        sKey = '%s-%d' % (sKey, oListener.m_ID)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iAppendSkillActNum and 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iActNum = oSkill.m_Base['ActNum']
        sKey = sKey + '-%d' % iActNum
    dCustomData = oTarget.Query(sKey, { })
    iCurFrame = oGame.GetFrameNum()
    iMax = None
    iMin = None
    bChange = False
    dCustom = { }
    for iVal, iLastFrame in dCustomData.items():
        if iLastFrame < iCurFrame:
            bChange = True
            continue
        dCustom[iVal] = iLastFrame
        if iDeOrder:
            if iMax is None or iMax < iVal:
                iMax = iVal
                continue
        if not iMin is None:
            if iMin > iVal:
                iMin = iVal
                continue
    
    if bChange:
        oTarget.Set(sKey, dCustom)
    if iMax is None and iMin is None:
        return 0
    if iDeOrder:
        return iMax
    return iMin


def EventCBGetTargetCustomDataNumByEnableTime(oListener, oEventCB, sKey):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(lstTar[0])
    if not oTarget:
        return 0
    iCurFrame = oGame.GetFrameNum()
    dCustom = { }
    for iVal, iLastFrame in oTarget.Query(sKey, { }).items():
        if iLastFrame < iCurFrame:
            continue
        dCustom[iVal] = iLastFrame
    
    oTarget.Set(sKey, dCustom)
    return len(dCustom)


def EventCBEnQueueByTarget(oListener, oEventCB, iTime, iResetTime = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    sKey = oEventCB.m_Key
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    if iTime:
        iLastFrame = Time2Frame(iTime) + oListener.m_Game.GetFrameNum()
    else:
        iLastFrame = 0
    dRecordQueue = oListener.SetDefault('%sRecordQueue' % sKey, { })
    if iResetTime:
        for iTarget in dRecordQueue:
            dRecordQueue[iTarget] = iLastFrame
        
    for iTarget in lstTar:
        dRecordQueue[iTarget] = iLastFrame
    


def EventCBClearQueue(oListener, oEventCB):
    oListener.Delete('%sRecordQueue' % oEventCB.m_Key)


def EventCBAddTargetFlawAddition(oListener, oEventCB, sAttr, iAdd, iMul, iCover, iAddMax = 0, iMulMax = 0):
    
    def ClearFunc(oTarget, oLifeCycle, setTar):
        for iTarget in setTar:
            oTarget.m_FlawCon.RemoveMonsterAddition(iTarget, sAttr, sKey)
        

    dTransInfo = oEventCB.GetCBTransInfo()
    sKey = oEventCB.m_Key + sAttr
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    if oListener.m_SID != EXECUTOR_HERO:
        return None
    oGame = oListener.m_Game
    oFlawCon = oListener.m_FlawCon
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        iAdd = cl_formula.GetResultByData(oTarget, iAdd, dEventInfo, dMsgInfo)
        iMul = cl_formula.GetResultByData(oTarget, iMul, dEventInfo, dMsgInfo)
        oFlawCon.AddMonsterAddition(iTarget, sAttr, sKey, iAdd, iMul, iCover, iAddMax, iMulMax)
    
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddDisableType(DISABLE_TYPE_TARGETSET, sKey, set(lstTar), ClearFunc)


def EventCBBreakFlaw(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['BreakFlaw'] = 1


def EventCBAddEventUnbalanceProb(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dMsgInfo['AddUnbalanceProb'] = iAdd


def EventCBAddSceneEventForState(oListener, oEventCB, iTime, iShape, dEffArgs, iYOffset, iState, iStateTime, iLeaveRemoveState = 1, iFightType = WARRIOR_MONSTER, iLeaveSetTime = -1):
    
    def ClearSceneEvt(oGame, iScene):
        for iTriggerObj in lstInScene[:]:
            SceneLeaveFunc(None, {
                'VID': iTriggerObj })
        
        dAllState.clear()
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oScene.RemoveSceneEvent(iSceneEvtID)

    
    def SceneEnterFunc(oListener, dMsgInfo):
        iTriggerObj = dMsgInfo['VID']
        obj = oGame.GetObject(iTriggerObj)
        if obj.m_FightType & iFightType != iFightType:
            return None
        lstInScene.append(iTriggerObj)
        oState = cl_state.AddState(obj, iState, iStateTimeType, Time2Frame(iStateTime), dStateArgs)
        if oState:
            lstStateID = dAllState.setdefault(iTriggerObj, [])
            lstStateID.append(oState.m_ID)
            oState.Enable(obj)

    
    def SceneLeaveFunc(oListener, dMsgInfo):
        iTriggerObj = dMsgInfo['VID']
        obj = oGame.GetObject(iTriggerObj)
        if not obj:
            return None
        if iTriggerObj in lstInScene:
            lstInScene.remove(iTriggerObj)
            lstStateID = dAllState.get(iTriggerObj, [])
            if iLeaveRemoveState:
                for iStateID in lstStateID:
                    obj.m_State.RemoveItem(iStateID)
                
                dAllState.pop(iTriggerObj, None)
            elif iLeaveSetTime >= 0:
                for iStateID in lstStateID:
                    oState = obj.m_State.GetItem(iStateID)
                    if oState:
                        oState.SetTime(obj, Time2Frame(iLeaveSetTime), 0)
                

    oGame = oListener.m_Game
    dTrans = oEventCB.GetCBTransInfo()
    vEPFPos = dTrans['EPFPos'] if 'EPFPos' in dTrans else oListener.GetPos()
    (x, y, z) = vEPFPos
    vPos = (x, y + iYOffset, z)
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sAttr, oValue in dEffArgs.items():
        iValue = cl_formula.GetResultByData(oListener, oValue, dEventInfo, dMsgInfo)
        dEffArgs[sAttr] = iValue
    
    if iShape == SCENE_EVT_SHAPE_SPHERE:
        lstArgs = [
            vPos,
            dEffArgs['Radius']]
    elif iShape == SCENE_EVT_SHAPE_RECTANGLE:
        lstArgs = [
            vPos,
            (dEffArgs['HalfX'], dEffArgs['HalfY'], dEffArgs['HalfZ'])]
    else:
        return None
    iScene = oListener.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    lstInScene = []
    dAllState = { }
    enterfunc = SceneEnterFunc
    leavefunc = SceneLeaveFunc
    iSceneEvtID = oScene.AddSceneEvent(oListener, enterfunc, leavefunc, iShape, lstArgs, { })
    iStateTimeType = STATE_TIME_LIMIT if iStateTime else STATE_TIME_FOREVER
    iPFItem = dEventInfo['ItemID']
    iPerform = dEventInfo['pfid']
    dData = {
        'Item': iPFItem } if iPFItem else { }
    oReason = cl_object.reason.CPerformReason(iPerform, oListener.m_ID, oListener.m_SID, oListener.m_FightType, None, dData)
    oReason = oReason.ExtInfo({
        'ActNum': 0 })
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    dStateArgs = {
        'AID': oListener.m_ID,
        'RS': oReason,
        'arg': {
            'Pos': vPos } }
    oGame.m_Timer.Call_Out(Functor(ClearSceneEvt, oGame, iScene), Time2Frame(iTime), 'AddSceneClearSceneEvt')


def EventCBSetTargetBySkillHit(oListener, oEventCB, iSuffix):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    sSuffix = oEventCB.m_Key if iSuffix else ''
    dHitTarget = oSkill.GetHitTarget(sSuffix)
    lstHitTarget = list(dHitTarget)
    dTransInfo = oEventCB.GetCBTransInfo()
    if lstHitTarget:
        dTransInfo['TargetList'] = lstHitTarget
        return None
    iTarget = 0
    if 'CurVID' in dMsgInfo:
        iTarget = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iTarget = dMsgInfo['VID']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iTarget = oSkill.m_Base['VID']
        if not iTarget and 'CurVID' in oSkill.m_Update:
            iTarget = oSkill.m_Update['CurVID']
    dTransInfo['TargetList'] = [
        iTarget] if iTarget else []


def EventCBRecordHitTarget(oListener, oEventCB, iSuffix):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    sSuffix = oEventCB.m_Key if iSuffix else ''
    oSkill.RecordHitTarget(sSuffix)


def EventCBSetTargetByVictim(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'Skill' not in dMsgInfo:
        dTransInfo['TargetList'] = []
        return None
    oSkill = dMsgInfo['Skill']
    if 'LastVLST' not in oSkill.m_Update:
        dTransInfo['TargetList'] = []
        return None
    dTransInfo['TargetList'] = oSkill.m_Update['LastVLST']


def EventCBAddTargetStateTime(oListener, oEventCB, iStateSID, iTime, iMaxTime):
    oState = oListener.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iMaxTime = cl_formula.GetResultByData(oListener, iMaxTime, dEventInfo, dMsgInfo)
    cl_state.AddTime(oState, oListener, Time2Frame(iTime), Time2Frame(iMaxTime))


def EventCBSetSkillCustomInfo(oWarrior, oEventCB, sArgs, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oWarrior, iValue, dEventInfo, dMsgInfo)
    oSkill.m_Custom[sArgs] = iValue


def EventCBChangeStateDelayTime(oListener, oEventCB, iAdd, iMul, bEventTarget = False):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'StateID' not in dMsgInfo:
        return None
    iStateID = dMsgInfo['StateID']
    if bEventTarget:
        oTarget = oListener.m_Game.GetObject(dMsgInfo['VID'])
        oState = oTarget.m_State.GetItem(iStateID)
    else:
        oState = oListener.m_State.GetItem(iStateID)
    if not oState:
        return None
    dTempDelayAction = oState.m_DelayAction
    if not dTempDelayAction:
        return None
    dDelayAction = { }
    dDelayAction.update(dTempDelayAction)
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    dDelayAction['delay'] = (dDelayAction['delay'] + iAdd) * (10000 + iMul) // 10000
    oState.m_DelayAction = dDelayAction


def EventCBSetPerformAttr(oTarget, oEventCB, sAttr, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iVal = cl_formula.GetResultByData(oTarget, iVal, dEventInfo, dMsgInfo)
    sKey = oEventCB.Key()
    if sAttr not in oPerform.m_Attr:
        oPerform.SetAttr(sAttr, 0, 1)
        oPerform.AttrChange(sAttr, sKey, 0, iVal)
    else:
        oPerform.AttrChange(sAttr, sKey, 0, iVal)
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1


def EventGetTargeIDtByType(oListener, oEventCB, iTargetType):
    iTarget = 0
    if iTargetType == OBJ_ATTACK:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        if 'AID' in dMsgInfo:
            iTarget = dMsgInfo['AID']
        elif 'Skill' in dMsgInfo:
            iTarget = dMsgInfo['Skill'].m_Base['AID']
        elif iTargetType == OBJ_VICTIM:
            dMsgInfo = oEventCB.GetCBMsgInfo()
            if 'CurVID' in dMsgInfo:
                iTarget = dMsgInfo['CurVID']
            elif 'VID' in dMsgInfo:
                iTarget = dMsgInfo['VID']
            elif 'Skill' in dMsgInfo:
                oSkill = dMsgInfo['Skill']
                iTarget = oSkill.m_Base['VID']
                if not iTarget and 'CurVID' in oSkill.m_Update:
                    iTarget = oSkill.m_Update['CurVID']
                elif iTargetType == OBJ_SELF:
                    iTarget = oListener.m_ID


def EventGetTargeID(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    return lstTar[0]


def EventCBSetSmithExtraUpgradeCost(oListener, oEventCB, iCost):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NpcID' in dMsgInfo:
        iNpcID = dMsgInfo['NpcID']
        dEventInfo = oEventCB.GetCBEventInfo()
        iCost = cl_formula.GetResultByData(oListener, iCost, dEventInfo, dMsgInfo)
        dCost = oListener.SetDefault('WeaponExtraUpgradeCost', { })
        dCost.setdefault(iNpcID, 0)
        dCost[iNpcID] += iCost


def EventCBSetSmithExtraUpgradeCostEnable(oListener, oEventCB, iEnable):
    oListener.Set('WeaponExtraUpgradeCostEnable', iEnable)


def GetTargetStateCountSum(oListener, oEventCB, iState, iFromAttack, iAttack):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    if iAttack:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        dEventInfo = oEventCB.GetCBEventInfo()
        iAttack = cl_formula.GetResultByData(oListener, iAttack, dEventInfo, dMsgInfo)
    elif iFromAttack:
        iAttack = oListener.m_ID
    iCount = 0
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        lstState = oTarget.m_State.GetItems(iState)
        for oState in lstState:
            if iAttack and oState.m_Attacker != iAttack:
                continue
            iCount += oState.GetCount()
        
    
    return iCount


def EventCBChangeDeviceEnergy(oListener, oEventCB, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Alter' not in dMsgInfo:
        return None
    iChange = dMsgInfo['Alter']
    dEventInfo = oEventCB.GetCBEventInfo()
    if iAdd:
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
        iChange += iAdd
    if iMul:
        iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
        iChange += iChange * iMul // 10000
    dMsgInfo['Alter'] = iChange


def EventCBAddTargetToxicStateCount(oListener, oEventCB, dCustomData):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    oGame = oListener.m_Game
    iAttack = oListener.GetDeviceID()
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        CommonAddToxicCount(oTarget, iAttack, dCustomData)
    


def EventCBUnitUsePerformByPosType(oListener, oEventCB, iPerform, iUnit, iPosType, dCustomData):
    if not oListener.m_FightType & WARRIOR_HERO:
        return None
    if iUnit == DEVICE_UNIT_TYPE:
        oUnit = oListener.GetDevice()
    else:
        return None
    if not oUnit:
        return None
    oPerform = oUnit.GetPerform(iPerform)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iPosType == DEVICE_USEPERFORM_POSTYPE_OWNER:
        vCurPos = oListener.GetPos()
    elif iPosType == DEVICE_USEPERFORM_POSTYPE_ENDPOS:
        if 'Skill' not in dMsgInfo:
            SendAlert('err', '%s监听消息使用错误，请检查！' % oEventCB.m_Key)
            return None
        oSkill = dMsgInfo['Skill']
        if 'EndPos' not in oSkill.m_Collect:
            SendAlert('err', '%s %s %s %s技能未写入EndPos，请程序检查！' % (oEventCB.m_Key, iUnit, oSkill, oSkill.m_Collect))
            return None
        vCurPos = oSkill.m_Collect['EndPos']
    elif iPosType == DEVICE_USEPERFORM_POSTYPE_SERVANT:
        oServant = oListener.m_Game.GetObject(oListener.m_Servant, PY_FLAG_DIED)
        if not oServant:
            return None
        vCurPos = oServant.GetPos()
    else:
        vCurPos = oUnit.GetPos()
    dEventInfo = oEventCB.GetCBEventInfo()
    dCustom = {
        'PosType': iPosType,
        'vEnd': vCurPos }
    for sKey, lstFormula in dCustomData.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dCustom[sKey] = iRet
    
    dData = {
        'Custom': dCustom }
    cl_war.UsePerform(oUnit, oPerform, dData)


def EventCBRemoveStateFromOwn(oListener, oEventCB, iStateSID, iObjectType):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    oGame = oListener.m_Game
    iCheckID = oListener.GetOwnObjectID(iObjectType)
    for iTarget in lstTar:
        oVictim = oGame.GetObject(iTarget)
        if not oVictim:
            continue
        oVictim.m_State.RemoveItemBySource(iStateSID, iCheckID)
    


def EventCBDeviceUsePerformEvtTarget(oListener, oEventCB, iPerform, dData, iLockPos = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    oDevice = oListener.GetDevice()
    if not oDevice:
        return None
    oPerform = oDevice.GetPerform(iPerform)
    if not oPerform:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sKey, lstFormula in dData.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    dPerform = {
        'Custom': dData }
    dData['LockTarget'] = lstTar
    iVictim = lstTar[0]
    dPerform['VID'] = iVictim
    dData['LockTrigger'] = iVictim
    if iLockPos:
        vCurPos = None
        if 'Skill' in dMsgInfo:
            oSkill = dMsgInfo['Skill']
            if 'DirectHitCurPos' in oSkill.m_Collect:
                vCurPos = oSkill.m_Collect['DirectHitCurPos']
            elif 'CurHitPos' in oSkill.m_Update:
                vCurPos = oSkill.m_Update['CurHitPos']
            else:
                dCartoon = oSkill.GetCurCartoon()
                if 'CurPos' in dCartoon:
                    vCurPos = dCartoon['CurPos']
        if not vCurPos:
            oVictim = oListener.m_Game.GetObject(iVictim)
            if oVictim:
                vCurPos = oVictim.GetPos()
        if not vCurPos:
            return None
        dData['LockPos'] = vCurPos
    cl_war.UsePerform(oDevice, oPerform, dPerform)


def EventChangeDeviceEnergy(oListener, oEventCB, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dData = {
        'LifeCycle': oEventCB.GetCBLifeCycle() }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dData, dMsgInfo)
    if iMul:
        iMul = cl_formula.GetResultByData(oListener, iMul, dData, dMsgInfo)
        iAdd += oListener.QueryAttr('MaxDeviceEnergy') * iMul // 10000
    oListener.DeviceEnergyModify(iAdd)


def EventChangeInkBeadReward(oListener, oEventCB, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'InkBeadReward' not in dMsgInfo:
        return None
    dData = {
        'LifeCycle': oEventCB.GetCBLifeCycle() }
    if iAdd:
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dData, dMsgInfo)
    if iMul:
        iMul = cl_formula.GetResultByData(oListener, iMul, dData, dMsgInfo)
    dMsgInfo['InkBeadReward'] = dMsgInfo['InkBeadReward'] * (10000 + iMul) // 10000 + iAdd


def EventCBChangeModifyInkValue(oListener, oEventCB, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Modify' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iModify = dMsgInfo['Modify']
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iModify += iModify * iMul // 10000 + iAdd
    dMsgInfo['Modify'] = iModify


def EventCBGetLockEnemy(oListener, oEventCB, iObjectType, iChooseLockEnemy, iChooseTargetRule, iMethodType, dArgs):
    if iObjectType:
        oTarget = oListener.GetOwnObject(iObjectType)
    else:
        oTarget = oListener
    if oTarget and oTarget.m_Scene and oTarget.m_Agent:
        oAgent = oTarget.m_Agent
        oLockEnemy = oAgent.GetLockEnemy()
        if not oLockEnemy and iChooseLockEnemy:
            dMsgInfo = oEventCB.GetCBMsgInfo()
            dEventInfo = oEventCB.GetCBEventInfo()
            for sKey, lstFormula in dArgs.items():
                iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
                dArgs[sKey] = iRet
            
            if iChooseTargetRule == SERVANTAGENT_CHOOSE_TARGET_SEE_ENEMY:
                oAgent.ChooseSeeEnemy(iMethodType, dArgs['Range'], oAgent)
                oLockEnemy = oAgent.GetLockEnemy()
        iLockEnemy = oLockEnemy.m_ID if oLockEnemy else 0
    else:
        iLockEnemy = 0
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = [
        iLockEnemy] if iLockEnemy else []


def EventCBGetCurPet(oListener, oEventCB):
    lstTar = []
    if not oListener.m_PetCon:
        return None
    if oListener.m_FightType & WARRIOR_HERO:
        oCurPet = oListener.m_PetCon.GetCurPet()
        if oCurPet:
            lstTar = [
                oCurPet.m_ID]
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTar


def EventCBGetEventPet(oListener, oEventCB):
    lstTar = []
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TargetPet' in dMsgInfo and dMsgInfo['TargetPet']:
        lstTar = [
            dMsgInfo['TargetPet']]
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTar


def EventCBGetFusePet(oListener, oEventCB, iUseMain):
    lstTar = []
    if iUseMain:
        sPet = 'MainPet'
    else:
        sPet = 'DeputyPet'
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if sPet in dMsgInfo and dMsgInfo[sPet]:
        lstTar = [
            dMsgInfo[sPet]]
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTar


def EventCBGetConPet(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    oPetCon = oListener.m_PetCon
    for iPetID in list(oPetCon.m_Pet):
        oPet = oListener.m_Game.GetObject(iPetID)
        if not oPet:
            continue
        dTransInfo['TargetList'].append(oPet.m_ID)
    


def EventCBGetEventMiniClone(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ClonePet' not in dMsgInfo or not dMsgInfo['ClonePet']:
        lstTar = []
    else:
        lstTar = [
            dMsgInfo['ClonePet']]
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTar


def EventCBGetOwnerPet(oListener, oEventCB):
    lstTar = []
    if oListener.m_FightType in (WARRIOR_PET_MINI, WARRIOR_PET_MINICLONE):
        if oListener.m_FightType == WARRIOR_PET_MINI:
            lstTar = [
                oListener.m_ID]
        else:
            oOwnerPet = oListener.m_Game.GetObject(oListener.m_OwnerPet)
            if oOwnerPet:
                lstTar = [
                    oOwnerPet.m_ID]
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTar


def EventCBGetClonePet(oListener, oEventCB):
    if oListener.m_FightType == WARRIOR_PET_MINICLONE:
        oOwnerPet = oListener.m_Game.GetObject(oListener.m_OwnerPet)
    elif oListener.m_FightType == WARRIOR_PET_MINI:
        oOwnerPet = oListener
    elif oListener.m_FightType & WARRIOR_HERO:
        oCurPet = oListener.m_PetCon.GetCurPet()
        oOwnerPet = oCurPet if oCurPet and oCurPet.m_FightType == WARRIOR_PET_MINI else None
    else:
        oOwnerPet = None
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = list(oOwnerPet.m_Clone) if oOwnerPet else []


def EventCBGetTentacleOwnerAndOtherTentacle(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    iTentacleOwner = oListener.Query('TentacleOwner', 0)
    oTentacleOwner = oListener.m_Game.GetObject(iTentacleOwner, PY_FLAG_DEAD)
    if oTentacleOwner:
        lstTar = [
            iTentacleOwner]
        iTentacleSID = oListener.m_SID
        iListener = oListener.m_ID
        for iSummonID, iSummonSID in oTentacleOwner.m_MonsterSummon.items():
            if iTentacleSID == iSummonSID and iListener != iSummonID:
                lstTar.append(iSummonID)
        
    else:
        lstTar = []
    dTransInfo['TargetList'] = lstTar


def EventCBGetSkillSummonCreate(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo['TargetList'] = []
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if 'SummonCreate' in oSkill.m_Collect:
        dTransInfo['TargetList'] = oSkill.m_Collect['SummonCreate']


def EventCBGetOwnerConquerCount(oListener, oEventCB):
    oConquerElement = oListener.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        return 0
    oOwner = oListener.GetOwner()
    return oConquerElement.m_ConquerchallengeMgr.GetHeroConquerCount(oOwner.m_PlayerID)


def EventCBGetTeamConquerCount(oListener, oEventCB):
    oConquerElement = oListener.m_Game.m_WarMgr.GetComponent('ConquerElement')
    if not oConquerElement:
        return 0
    return oConquerElement.m_ConquerchallengeMgr.GetSuccessConquerCount()


def EventGetFaceVictimSectorHateTarget(oListener, oEventCB, iObjectType, iHateMethod, iAngle):
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    oWarrior = oListener.GetOwnObject(iObjectType)
    if not oWarrior:
        return None
    oAgent = oWarrior.m_Agent
    if not oAgent:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iVictim = oSkill.m_Base['VID']
        if not iVictim and 'CurVID' in oSkill.m_Update:
            iVictim = oSkill.m_Update['CurVID']
        else:
            return None
    oGame = oListener.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return None
    oAgent.UpdateHate(iHateMethod)
    dHateData = oAgent.GetData('HateData', { })
    if not dHateData:
        return None
    iMaxHateTarget = 0
    vStart = oWarrior.GetPos()
    vDir = cl_math.Vec3Minus(oVictim.GetPos(), vStart)
    for iTarget, _ in sorted(dHateData.items(), key = (lambda x: x[1]['Hate'][0]), reverse = True):
        if iTarget == iVictim:
            continue
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        disp = cl_math.Vec3Minus(oTarget.GetPos(), vStart)
        if cl_math.CheckVector2Angle(disp, vDir, iAngle):
            continue
        if not oAgent.IsEnemyInSight(oListener, oTarget, iAngle = 180, iUsePerform = 1):
            continue
        iMaxHateTarget = iTarget
    
    if iMaxHateTarget:
        dTransInfo['TargetList'] = [
            iMaxHateTarget]


def EventCBAddDamSign(oListener, oEventCB, sSign, iSkillSign):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iSkillSign:
        if 'Skill' not in dMsgInfo:
            return None
        dCollect = dMsgInfo['Skill'].m_Collect
        if 'DamSign' not in dCollect:
            dCollect['DamSign'] = { }
        dCollect['DamSign'][sSign] = 1
    elif 'MainDam' not in dMsgInfo:
        return None
    for _, oReason in dMsgInfo['MainDam']:
        dDamSign = oReason.Query('DamSign', { })
        dDamSign[sSign] = 1
        oReason.SetInfo('DamSign', dDamSign)
    


def EventCBAddCustomInfo(oListener, oEventCB, sKey, iVal):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    if 'Custom' not in dMsgInfo:
        dMsgInfo['Custom'] = { }
    dMsgInfo['Custom'][sKey] = iVal


def EventCBSetTargetPhase(oListener, oEventCB, iPhase):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    iPhase = cl_formula.GetResultByData(oListener, iPhase, {
        'LifeCycle': oEventCB.GetCBLifeCycle() })
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        oTarget.SetPhase(iPhase)
    


def EventCBGetEventInkAreaSquare(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'EventID' not in dMsgInfo or oListener.m_SID != INKMASTER_HERO:
        return 0
    oInkCon = oListener.m_InkCon
    return oInkCon.GetInkAreaSquareByEventID(dMsgInfo['EventID'])


def EventCBReduceTargetFlawCD(oListener, oEventCB, iReduce, iMul):
    if oListener.m_SID != EXECUTOR_HERO:
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iReduce = cl_formula.GetResultByData(oListener, iReduce, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iReduce = Time2Frame(iReduce)
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        oListener.m_FlawCon.ReduceTargetCurFlawCD(oTarget, iReduce, iMul)
    


def EventCBSetTargetStateStatistics(oListener, oEventCB, iState, sAttr, iValue, iFromSelf, iFromSameItem, iCloseClear):
    
    def ClearFunc(oTarget, oLifeCycle):
        if not oState:
            return None
        oState.m_Data[sAttr] = 0

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAttack = oListener.m_ID if iFromSelf else 0
    iItem = dEventInfo['ItemID'] if iFromSameItem else 0
    oState = oTarget.m_State.GetStateBySource(iState, iAttack, iItem)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    oState.m_Data[sAttr] = iValue
    if iCloseClear:
        sUniqueKey = 'SetTargetStateStatistics-%s-%s-%s' % (iTarget, iState, sAttr)
        oLifeCycle = dEventInfo['LifeCycle']
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def EventCBGetEventItemKey(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'ItemKey' in oSkill.m_Cache:
            return oSkill.m_Cache['ItemKey']
    if 'ItemKey' in dMsgInfo:
        return dMsgInfo['ItemKey']
    if 'ItemID' in dMsgInfo:
        iItemID = dMsgInfo['ItemID']
        oItem = oListener.m_WieldCon.GetItemByID(iItemID)
        if oItem:
            return oItem.Key()
    return ''


def EventCBSetLuckyHitEff(oListener, oEventCB, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LuckyHitEff' not in dMsgInfo:
        return None
    dMsgInfo['LuckyHitEff'] = iValue


def EventCBSetTargetConquerStatus(oListener, oEventCB, iValue):
    oListener.Set('ConquerStatus', iValue)
    oListener.GS2CPropChange('ConquerStatus', iValue)


def EventCBSetTargetMaxAttr(oListener, oEventCB, sAttr, iValue, iTime):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    oTarget.SetMaxAttr(sAttr)
    oTarget.AddMaxAttr(sAttr, oEventCB.m_Key, iValue, Time2Frame(iTime))


def EventCBListenTargetMsgCallBack(oListener, oEventCB, iMsg, iSub, iGroup, iTime):
    
    def CallBackFunc(oEventCB, iGroup, dEvent, oListener, oTarget, dMsgInfo):
        dListen = oListener.Query(sEventListen, { })
        if not dListen or tKey not in dListen:
            cl_msgcenter.DoneAttention(oListener, iTarget, iMsg, sEventKey, iSub)
            return None
        iExpireFrameNum = dListen[tKey]
        if iExpireFrameNum and oListener.m_Game.GetFrameNum() > iExpireFrameNum:
            cl_msgcenter.DoneAttention(oListener, iTarget, iMsg, sEventKey, iSub)
            dListen.pop(tKey, { })
            return None
        oEventCB.CBFuncAction(oListener, iGroup, dEvent, dMsgInfo)

    
    def ClearFunc(oTarget, oLifeCycle):
        dListen = oListener.Query(sEventListen, { })
        oListener.Delete(sEventListen)
        for iListenTarget, iListenMsg, iListenSubMsg in dListen:
            cl_msgcenter.DoneAttention(oListener, iListenTarget, iListenMsg, sEventKey, iListenSubMsg)
        

    sEventKey = oEventCB.m_Key
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sEventKey)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    sEventListen = 'EventListen-%s' % sEventKey
    dListen = oListener.SetDefault(sEventListen, { })
    tKey = (iTarget, iMsg, iSub)
    if tKey in dListen:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    dEvent = oLifeCycle.AttrCache()
    dEvent['LifeCycle'] = oLifeCycle
    if iTime:
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
        iExpireFrameNum = Time2Frame(iTime) + oListener.m_Game.GetFrameNum()
    else:
        iExpireFrameNum = 0
    dListen[tKey] = iExpireFrameNum
    func = Functor(CallBackFunc, oEventCB, iGroup, dEvent)
    cl_msgcenter.AddAttentionFunc(oListener, iTarget, iMsg, func, sEventKey, iSub)
    oLifeCycle.AddUniqueDisableFunc(sEventKey, ClearFunc, 0)


def EventCBRemoveTargetList(oListener, oEventCB, iState, iRemoveDevilMonster):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    lstTarget = []
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if iRemoveDevilMonster and oTarget.Query('Demon'):
            continue
        if iState and oTarget.m_State.HasState(iState):
            continue
        lstTarget.append(iTarget)
    
    dTrans['TargetList'] = lstTarget


def EventCBDirectEventCBFuncByInterval(oListener, oEventCB, iNum, dInterval, iRepetition):
    
    def ClearFunc(oTarget, oLifeCycle):
        oLifeCycleOwner.DelArgValue('LastIntervalGroup')

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    iGroup = 0
    oLifeCycleOwner = oLifeCycle.GetObject()
    dLastGroup = oLifeCycleOwner.GetArgValue('LastIntervalGroup', { })
    for iLeft in dInterval:
        if iNum <= iLeft:
            break
        iGroup = dInterval[iLeft]
    
    sKey = oEventCB.m_Key
    if sKey in dLastGroup:
        iLastGroup = dLastGroup[sKey]
    else:
        iLastGroup = 0
    if iGroup == iLastGroup and not iRepetition:
        return None
    dLastGroup[sKey] = iGroup
    oLifeCycleOwner.SetArgValue('LastIntervalGroup', dLastGroup)
    oEventCB.CBFuncAction(oListener, iGroup, dEventInfo, dMsgInfo)
    sEventKey = 'LastIntervalGroup-%s' % sKey
    oLifeCycle.AddUniqueDisableFunc(sEventKey, ClearFunc, 0)


def EventCBRefreshTargetPerformColdTime(oListener, oEventCB, iPerform):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    oTarget = oListener.m_Game.GetObject(lstTar[0])
    if not oTarget:
        return None
    oPerformCon = oTarget.m_Perform
    if not oPerformCon:
        return None
    iPerform = cl_formula.GetResultByData(oTarget, iPerform, { })
    if not iPerform:
        return None
    pfobj = oPerformCon.GetPerform(iPerform)
    if not pfobj:
        return None
    oPerformCon.DelCoverColdTime(iPerform)


def EventCBRecordAllHPLoss(oListener, oEventCB, iRecordTime, iDamUse):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'IsDam' not in dMsgInfo:
        return None
    if not dMsgInfo['IsDam']:
        return None
    if 'TotalDam' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycleOwner = oLifeCycle.GetObject()
    iNowFrame = oListener.m_Game.GetFrameNum()
    lstTotalDam = dMsgInfo['TotalDam']
    iChange = 0
    if iDamUse & DAM_USE_SHIELD == DAM_USE_SHIELD:
        iIndex = cl_formula.g_HpTypeIndex['Shield']
        iChange += lstTotalDam[iIndex]
    if iDamUse & DAM_USE_ARMOR == DAM_USE_ARMOR:
        iIndex = cl_formula.g_HpTypeIndex['Armor']
        iChange += lstTotalDam[iIndex]
    if iDamUse & DAM_USE_HP == DAM_USE_HP:
        iIndex = cl_formula.g_HpTypeIndex['HP']
        iChange += lstTotalDam[iIndex]
    dLossInfo = oLifeCycleOwner.GetArgValue('AllHPLossInfo', { })
    if iNowFrame in dLossInfo:
        dLossInfo[iNowFrame] = dLossInfo[iNowFrame] + iChange
    else:
        dLossInfo[iNowFrame] = iChange
    if not iRecordTime:
        oLifeCycleOwner.SetArgValue('AllHPLossInfo', dLossInfo)
        return None
    iFrame = Time2Frame(iRecordTime)
    iClearFrame = iNowFrame - iFrame
    dNewLossInfo = { iToatlDam: iHPChangeFrame for iHPChangeFrame, iToatlDam in dLossInfo.items() if iHPChangeFrame >= iClearFrame }
    oLifeCycleOwner.SetArgValue('AllHPLossInfo', dNewLossInfo)


def EventCBSetStateTime(oListener, oEventCB, iStateSID, iTime, iRefreshDelay):
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    if iTime:
        cl_state.SetTime(oState, oListener, Time2Frame(iTime), iRefreshDelay)
    else:
        oState.SetForever(oListener)


def EventCBTriggerGroupByTargetAssistantWeaponElementType(oListener, oEventCB, dGroup):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    oTarget = oListener.m_Game.GetObject(lstTar[0])
    if not oTarget or not (oTarget.m_FightType & WARRIOR_HERO):
        return None
    oWeapon = oTarget.m_WieldCon.GetAssistantWeapon()
    if not oWeapon:
        return None
    iElementType = oWeapon.m_ElementType
    if iElementType not in dGroup:
        return None
    iGroup = dGroup[iElementType]
    if iGroup not in oEventCB.m_CBFuncAction:
        return None
    func = oEventCB.m_CBFuncAction[iGroup]
    func(oEventCB, oListener)


def EventCBTargetAddThrowBagBullet(oListener, oEventCB, iAmount):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for iTarget in dTrans['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oPerform = oTarget.GetThrowPerform()
        if not oPerform:
            continue
        iBullet = oPerform.CalAttr('BulletSID')
        iAmount = cl_formula.GetResultByData(oTarget, iAmount, dEventInfo, dMsgInfo)
        if iAmount < 0:
            iHasBullet = oTarget.m_BulletCon.Bullet(iBullet)
            if iHasBullet + iAmount < 0:
                iAmount = 0 - iHasBullet
        oTarget.m_BulletCon.BulletModify(iBullet, iAmount, oEventCB.m_Key)
    


def EventCBQueryTargetAttr(oListener, oEventCB, sAttr):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    oTarget = oListener.m_Game.GetObject(lstTar[0])
    if not oTarget:
        return 0
    return cl_newformula.GetWarriorAttr(sAttr, oTarget)


def EventCBChangeTargetPerformAttr(oListener, oEventCB, iPerform, sAttr, iMul, iAdd, iCalByTarget):
    
    def ClearTargetPerformAttr(oTarget, oLifeCycle):
        oChangeTarget = oTarget.m_Game.GetObject(iTarget)
        if not oChangeTarget:
            return None
        oChangePerform = oChangeTarget.GetPerform(iPerform)
        if not oChangePerform:
            return None
        oChangePerform.AttrClear(sAttr, sKey, iRefresh = 1)

    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iPerform = cl_formula.GetResultByData(oTarget, iPerform, dEventInfo, dMsgInfo)
    oChangePerform = oTarget.GetPerform(iPerform)
    if not oChangePerform:
        return None
    if iCalByTarget:
        oCalTarget = oTarget
    else:
        oCalTarget = oListener
    if iMul:
        iMul = cl_formula.GetResultByData(oCalTarget, iMul, dEventInfo, dMsgInfo)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oCalTarget, iAdd, dEventInfo, dMsgInfo)
        iAdd = cl_object.AttrUnitConversion(sAttr, iAdd)
    sKey = oEventCB.m_Key
    oChangePerform.AttrChange(sAttr, sKey, iMul, iAdd)
    sUniqueKey = 'ChangeTargetPerformAttr-%s-%s' % (iTarget, sAttr)
    dEventInfo['LifeCycle'].AddUniqueDisableFunc(sUniqueKey, ClearTargetPerformAttr, iCover = 0)


def EventCBUseCommonSpell(oListener, oEventCB, iCount):
    if oListener.IsDead():
        return None
    oGame = oListener.m_Game
    oPerformCon = oListener.m_AbilityCon
    dChoose = GetCommonSpell()
    dAddPerform = { }
    for _ in range(iCount):
        iPerform = ChooseKey(oGame, dChoose)
        oPerform = oListener.GetPerform(iPerform)
        if oPerform:
            iTotalCDTime = oPerformCon.GetTotalColdTime(iPerform)
            if iTotalCDTime > 0:
                oPerform.DelCDTime(oListener)
                oPerform.SetCDTime(oListener, iTotalCDTime)
                continue
        oPerform = oPerformCon.AddPerform(oListener, iPerform, iLevel = 1, iEnable = 1, iItem = 0)
        if not oPerform:
            SendAlert('err', '%s使用通用法术%s失败' % (oEventCB.m_Key, iPerform))
            continue
        dAddPerform[iPerform] = 1
        oPerform.DelCDTime(oListener)
    
    for iPerform in dAddPerform:
        oPerformCon.RemovePerform(oListener, iPerform)
    


def EventCBUseEnableSpell(oListener, oEventCB, iCount, iExcludeSelf = 1):
    if oListener.IsDead():
        return None
    oGame = oListener.m_Game
    lstAllSpell = oListener.GetEnableSpell()
    if oListener.m_FightType == WARRIOR_PET_MINICLONE:
        oMainPet = oGame.GetObject(oListener.m_OwnerPet)
        if not oMainPet:
            return None
        setShareSpell = oListener.m_ShareSpell
    else:
        oMainPet = None
        setShareSpell = set()
    for iPerform in lstAllSpell[:]:
        oPerform = oListener.GetPerform(iPerform)
        if oPerform.m_PFType == PF_TYPE_PETACTIVE and oPerform.m_ExtCover:
            lstAllSpell.remove(iPerform)
        if iPerform in setShareSpell:
            oMainPetPerform = oMainPet.GetPerform(iPerform)
            if not not oMainPetPerform:
                if oMainPetPerform.GetArgValue('CloneTrigger') == oGame.GetFrameNum():
                    lstAllSpell.remove(iPerform)
                    continue
    
    if iExcludeSelf:
        iSelfSpell = 0
        dEventInfo = oEventCB.GetCBEventInfo()
        if 'pfid' in dEventInfo:
            iSelfSpell = dEventInfo['pfid']
        elif 'StateInfo' in dEventInfo and 'pfid' in dEventInfo['StateInfo']:
            iSelfSpell = dEventInfo['StateInfo']['pfid']
        if iSelfSpell in lstAllSpell:
            lstAllSpell.remove(iSelfSpell)
    if not lstAllSpell:
        return None
    iSpellLen = len(lstAllSpell)
    for _ in range(iCount):
        idx = oGame.Random(iSpellLen)
        iPerform = lstAllSpell[idx]
        if iPerform in setShareSpell:
            lstAllSpell.remove(iPerform)
            oMainPetPerform = oMainPet.GetPerform(iPerform)
            oMainPetPerform.SetArgValue('CloneTrigger', oGame.GetFrameNum())
            iTotalCDTime = oMainPetPerform.m_Container.GetTotalColdTime(iPerform)
            oMainPetPerform.DelCDTime(oMainPet)
            if iTotalCDTime > 0:
                oMainPetPerform.SetCDTime(oMainPet, iTotalCDTime)
            if not lstAllSpell:
                break
            iSpellLen = len(lstAllSpell)
            continue
        oPerform = oListener.GetPerform(iPerform)
        if oPerform.m_PFType == PF_TYPE_PETABILITY:
            if oPerform.m_NeedLockTarget:
                if not (oListener.m_Agent) or not oListener.m_Agent.GetLockEnemy():
                    oPerform.AddExtCover()
                else:
                    iTotalCDTime = oPerform.m_Container.GetTotalColdTime(iPerform)
                    oPerform.DelCDTime(oListener)
                    if iTotalCDTime > 0:
                        oPerform.SetCDTime(oListener, iTotalCDTime)
                        continue
        oPerform.AddExtCover()
    


def EventCBTriggerMinorByHeroSID(oWarrior, oEventCB, iUseOwner, dInfo):
    if iUseOwner:
        iOwner = oWarrior.m_Owner
        if not iOwner:
            return None
        oOwner = oWarrior.m_Game.GetObject(iOwner)
        if not oOwner:
            return None
        oUser = oOwner
    else:
        oUser = oWarrior
    iHeroSID = oUser.m_SID
    if iHeroSID in HERO_TRIGGER_FUNC:
        dInfo['Perform'] = HERO_TRIGGER_FUNC[iHeroSID][1]
        HERO_TRIGGER_FUNC[iHeroSID][0](oUser, oEventCB, dInfo)


def HeroUsePointPerform(oUser, oEventCB, dInfo):
    iHeroSID = oUser.m_SID
    iAssignEndPos = 0
    dCustomData = { }
    if 'CommonCustomData' in dInfo:
        dCustomData = dInfo['CommonCustomData']
    if 'AssignEndPos' in dInfo and iHeroSID in dInfo['AssignEndPos']:
        iAssignEndPos = 1
    if 'CustomData' in dInfo and iHeroSID in dInfo['CustomData']:
        dCustomData.update(dInfo['CustomData'][iHeroSID])
    if 'HalfHeight' in dInfo and iHeroSID in dInfo['HalfHeight']:
        dCustomData['HalfHeight'] = 1
    dCustomData['ThrowMsg'] = 1
    PassiveCBUsePerform2EvtTarget(oUser, oEventCB, dInfo['Perform'], iAssignEndPos, dCustomData)


def Hero207Trigger(oUser, oEventCB, dInfo):
    iPerform = dInfo['Perform']
    oPerform = oUser.GetPerform(iPerform)
    if not oPerform:
        oUser.AddPerform(iPerform, 1)
    iTriggerOrigin = dInfo['CommonCustomData']['TriggerOrigin'] if 'CommonCustomData' in dInfo and 'TriggerOrigin' in dInfo['CommonCustomData'] else 0
    EventCBStartThrowSkill(oUser, oEventCB, iPerform, 0, {
        'ThrowMsg': 1,
        'TriggerOrigin': iTriggerOrigin })


def Hero214Trigger(oUser, oEventCB, dInfo):
    iPerform = dInfo['Perform']
    oPerform = oUser.GetPerformIfNoThenNew(iPerform)
    oGame = oUser.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' in dTrans and dTrans['TargetList']:
        iCurVID = dTrans['TargetList'][0]
        oVictim = oGame.GetObject(iCurVID)
        if not oVictim:
            return None
        vCurPos = oVictim.GetPos()
    elif 'VID' in dMsgInfo and 'CurHitPos' in dMsgInfo:
        iCurVID = dMsgInfo['VID']
        vCurPos = dMsgInfo['CurHitPos']
    elif 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if 'CurVID' not in oSkill.m_Update:
        return None
    iCurVID = oSkill.m_Update['CurVID']
    if 'DirectHitCurPos' in oSkill.m_Collect:
        vCurPos = oSkill.m_Collect['DirectHitCurPos']
    elif 'CurHitPos' in oSkill.m_Update:
        vCurPos = oSkill.m_Update['CurHitPos']
    else:
        return None
    oVictim = oGame.GetObject(iCurVID)
    if not oVictim:
        return None
    vEndPos = oVictim.GetPos()
    oPerform.AddCanUseCount()
    dEventInfo = oEventCB.GetCBEventInfo()
    iTriggerOrigin = dInfo['CommonCustomData']['TriggerOrigin'] if 'CommonCustomData' in dInfo and 'TriggerOrigin' in dInfo['CommonCustomData'] else 0
    iTriggerOrigin = cl_formula.GetResultByData(oUser, iTriggerOrigin, dEventInfo, dMsgInfo)
    dArgs = {
        'SX': int(vCurPos[0] * 100),
        'SY': int(vCurPos[1] * 100),
        'SZ': int(vCurPos[2] * 100),
        'EX': int(vEndPos[0] * 100),
        'EY': int((vEndPos[1] + oVictim.m_ModelHeight / 2) * 100),
        'EZ': int(vEndPos[2] * 100),
        'ThrowMsg': 1,
        'TriggerOrigin': iTriggerOrigin }
    cl_snetwar.GS2CNotifyStartSkill(oGame, oUser.m_PlayerID, iPerform, oPerform.m_ID, 0, dArgs)


def Hero216Trigger(oUser, oEventCB, dInfo):
    iPerform = dInfo['Perform']
    oPerform = oUser.GetPerformIfNoThenNew(iPerform)
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oPerform.AddCanUseCount()
    iAssignQuality = oUser.m_GamblerCon.GetCurCombQuality()
    iQualityNum = cl_formula.GetResultByData(oUser, dInfo['QualityNum'], dEventInfo, dMsgInfo)
    iQuality = oUser.m_GamblerCon.TryAppendQuality(iAssignQuality, GAMBLER_CHOOSE_EQUITY, True, iQualityNum)
    iTriggerOrigin = dInfo['CommonCustomData']['TriggerOrigin'] if 'CommonCustomData' in dInfo and 'TriggerOrigin' in dInfo['CommonCustomData'] else 0
    iTriggerOrigin = cl_formula.GetResultByData(oUser, iTriggerOrigin, dEventInfo, dMsgInfo)
    dArgs = {
        'CardNum': dInfo['CardNum'],
        'Quality': iQuality,
        'ThrowMsg': 1,
        'TriggerOrigin': iTriggerOrigin }
    cl_snetwar.GS2CNotifyStartSkill(oUser.m_Game, oUser.m_PlayerID, iPerform, oPerform.m_ID, 0, dArgs)


def Hero219Trigger(oUser, oEventCB, dInfo):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' in dTrans and dTrans['TargetList']:
        iCurVID = dTrans['TargetList'][0]
        iPerform = dInfo['Perform']
        oPerform = oUser.GetPerformIfNoThenNew(iPerform)
        oPerform.AddCanUseCount()
        dEventInfo = oEventCB.GetCBEventInfo()
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iTriggerOrigin = dInfo['CommonCustomData']['TriggerOrigin'] if 'CommonCustomData' in dInfo and 'TriggerOrigin' in dInfo['CommonCustomData'] else 0
        iTriggerOrigin = cl_formula.GetResultByData(oUser, iTriggerOrigin, dEventInfo, dMsgInfo)
        cl_snetwar.GS2CNotifyStartSkill(oUser.m_Game, oUser.m_PlayerID, iPerform, oPerform.m_ID, 0, {
            'Target': iCurVID,
            'ThrowMsg': 1,
            'FromTargetDistance': 1,
            'TriggerOrigin': iTriggerOrigin })


def Hero220Trigger(oUser, oEventCB, dInfo):
    (iBigLionThrow, iSmallLionThrow) = dInfo['Perform']
    if oUser.m_State.GetItemBySID(BIG_LION_STATE):
        oPerform = oUser.GetPerformIfNoThenNew(iBigLionThrow)
        dEventInfo = oEventCB.GetCBEventInfo()
        dMsgInfo = oEventCB.GetCBMsgInfo()
        iTriggerOrigin = dInfo['CommonCustomData']['TriggerOrigin'] if 'CommonCustomData' in dInfo and 'TriggerOrigin' in dInfo['CommonCustomData'] else 0
        iTriggerOrigin = cl_formula.GetResultByData(oUser, iTriggerOrigin, dEventInfo, dMsgInfo)
        dCustom = {
            'TriggerOrigin': iTriggerOrigin,
            'ThrowMsg': 1 }
        dData = {
            'Custom': dCustom }
        cl_war.UsePerform(oUser, oPerform, dData)
    else:
        dInfo['Perform'] = iSmallLionThrow
        HeroUsePointPerform(oUser, oEventCB, dInfo)

HERO_TRIGGER_FUNC = {
    201: (HeroUsePointPerform, 8011),
    205: (HeroUsePointPerform, 8001),
    206: (HeroUsePointPerform, 8012),
    207: (Hero207Trigger, 1413),
    212: (HeroUsePointPerform, 8013),
    213: (HeroUsePointPerform, 8014),
    214: (Hero214Trigger, 1430),
    215: (HeroUsePointPerform, 8007),
    216: (Hero216Trigger, 12008),
    217: (HeroUsePointPerform, 8009),
    218: (HeroUsePointPerform, 8010),
    219: (Hero219Trigger, 12030),
    220: (Hero220Trigger, (8021, 8022)),
    221: (HeroUsePointPerform, 8019) }

def GetVictimIDByMsgInfo(dMsgInfo):
    if 'CurVID' in dMsgInfo:
        iCurVID = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iCurVID = dMsgInfo['VID']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iCurVID = oSkill.m_Base['VID']
    else:
        iCurVID = 0
    return iCurVID


def EventCBRecordMasterImmobilizeMonsterNum(oListener, oEventCB):
    
    def ClearFunc(oTarget, oLifeCycle):
        oLifeCycleOwner.DelArgValue('ImmobilizeMonsterNum')
        oLifeCycleOwner.DelArgValue('ImmobilizeMonster')

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycleOwner = oLifeCycle.GetObject()
    dImmobilizeMonster = oLifeCycleOwner.GetArgValue('ImmobilizeMonster', { })
    iVictim = dMsgInfo['VID']
    sKey = dMsgInfo['Key']
    if dMsgInfo['Immobilize']:
        if iVictim not in dImmobilizeMonster:
            dImmobilizeMonster[iVictim] = { }
        if sKey not in dImmobilizeMonster[iVictim]:
            dImmobilizeMonster[iVictim][sKey] = 1
        elif iVictim not in dImmobilizeMonster:
            return None
    if None not in dImmobilizeMonster[iVictim]:
        return None
    dImmobilizeMonster[iVictim].pop(sKey)
    if not dImmobilizeMonster[iVictim]:
        dImmobilizeMonster.pop(iVictim)
    oLifeCycleOwner.SetArgValue('ImmobilizeMonsterNum', len(dImmobilizeMonster))
    oLifeCycleOwner.SetArgValue('ImmobilizeMonster', dImmobilizeMonster)
    sEventKey = 'ImmobilizeMonster-%s' % sKey
    oLifeCycle.AddUniqueDisableFunc(sEventKey, ClearFunc, 0)


def EventCBGetTargetAbnormalNum(oListener, oEventCB, iRemove = 0, iCheckType = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTrans['TargetList']
    if not lstTar:
        return 0
    iNum = 0
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        for iState in g_AllAbnormalStateSID:
            lstState = oTarget.m_State.GetItems(iState)
            if not lstState:
                continue
            if iCheckType:
                iNum += 1
            else:
                iNum += len(lstState)
            if iRemove:
                for oTarState in lstState:
                    oTarget.m_State.RemoveItem(oTarState.m_ID)
                
        
    
    return iNum


def EventCBChooseAbilityByQuality(oListener, oEventCB, iQuality, iNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Pet' not in dMsgInfo or 'Count' not in dMsgInfo or not dMsgInfo['Count']:
        return None
    sKey = oEventCB.m_Key
    oGame = oListener.m_Game
    oPet = oGame.GetObject(dMsgInfo['Pet'])
    if not oPet or oPet.Query(sKey, 0):
        return None
    oPet.Set(sKey, 1)
    iCount = dMsgInfo['Count']
    if iCount < iNum:
        iNum = iCount
    dMsgInfo['Count'] -= iNum
    if 'TotalCount' in dMsgInfo:
        dMsgInfo['TotalCount'] -= iNum
    oPerformCon = oPet.m_AbilityCon
    for _ in range(iNum):
        if not oPerformCon.ChooseAbilityByQuality(oPet, iQuality, sReason = sKey):
            dMsgInfo['Count'] += 1
            if 'TotalCount' in dMsgInfo:
                dMsgInfo['TotalCount'] += 1
    


def EventCBChooseParentAbilityByQuality(oListener, oEventCB, iQuality, iNum, iAddition):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Pet' not in dMsgInfo or 'Count' not in dMsgInfo or not dMsgInfo['Count'] or 'ParentAbilityWeight' not in dMsgInfo:
        return None
    sKey = oEventCB.m_Key
    oGame = oListener.m_Game
    oPet = oGame.GetObject(dMsgInfo['Pet'])
    if not oPet or oPet.Query(sKey, 0):
        return None
    dAbilityByQuality = cl_platformdata.GetPetAbilityByQuality(iQuality)
    if not dAbilityByQuality:
        return None
    dTargetFromParentAbility = { }
    for iAbility, iWeight in dMsgInfo['ParentAbilityWeight'].items():
        if iAbility not in dAbilityByQuality:
            continue
        dTargetFromParentAbility[iAbility] = iWeight
    
    if not dTargetFromParentAbility:
        if iAddition:
            EventCBChooseAbilityByQuality(oListener, oEventCB, iQuality, iNum)
        return None
    oPet.Set(sKey, 1)
    iCount = dMsgInfo['Count']
    if iCount < iNum:
        iNum = iCount
    dMsgInfo['Count'] -= iNum
    dMsgInfo['TotalCount'] -= iNum
    oPerformCon = oPet.m_AbilityCon
    for _ in range(iNum):
        if not oPerformCon.ChooseParentAbility(dTargetFromParentAbility, sReason = sKey):
            dMsgInfo['Count'] += 1
            dMsgInfo['TotalCount'] += 1
    


def EventCBAddSourceWeaponSpecialAttrBase(oListener, oEventCB, sAttr, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    if iAdd:
        iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
        oWeapon.AddSpecialAttrBase(sAttr, iAdd)


def EventCBChangeTargetBaseDamRatio(oListener, oEventCB, iMul, iAdd, iMask):
    
    def ClearFunc(oListener, oLifeCycle):
        oTarget = oGame.GetObject(iTarget)
        if not oTarget or oTarget.m_ReleaseFlag:
            return None
        sKey = oLifeCycle.Key()
        oTarget.ClearBaseDamRatioByKey(sKey)

    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    sKey = 'ChangeTargetDam-%s-%s' % (iTarget, oEventCB.m_Key)
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oTarget, iMul, dEventInfo, dMsgInfo)
    if iAdd or iMul:
        oTarget.ChangeBaseDamRatio(sKey, iAdd, iMul, iMask)
        oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)
    else:
        oTarget.ClearBaseDamRatioByKey(sKey)


def EventCBHitUnbalance(oListener, oEventCB, iProb):
    if oListener.m_SID != EXECUTOR_HERO:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'CurVID' not in dMsgInfo:
        return None
    oMonster = oListener.m_Game.GetObject(dMsgInfo['CurVID'], PY_FLAG_DEAD)
    if not oMonster:
        return None
    oListener.m_FlawCon.HitUnbalance(oMonster, dMsgInfo, iProb)


def CBChangeOwnerWeaponAttr(oListener, oEventCB, iHoldType, sAttr, iAdd, iMul):
    
    def ClearFunc(oListener, oLifeCycle):
        oOwner = oListener.GetOwner()
        if not oOwner:
            return None
        oWeapon = oOwner.m_WieldCon.GetItemByID(iItem)
        if not oWeapon:
            return None
        oWeapon.AttrClear(sAttr, sKey)

    oOwner = oListener.GetOwner()
    oWeapon = oOwner.m_WieldCon.GetCurWeapon(iHoldType)
    if not oWeapon:
        return None
    iItem = oWeapon.m_ID
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iMul or iAdd:
        oWeapon.AttrChange(sAttr, iMul, iAdd, sKey, iRemoveClear = 1)
        sUniqueKey = 'CBChangeOwnerWeaponAttr-%s-%s' % (iItem, sAttr)
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)
    else:
        oWeapon.AttrClear(sAttr, sKey)


def EventCBChangeTargetStateDelayTime(oListener, oEventCB, iStateSID, iAdd, iMul):
    
    def ClearFunc(oListener, oEventCB):
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            return None
        oState = oTarget.m_State.GetItemBySID(iStateSID)
        if not oState:
            return None
        dDelayAction = oState.m_DelayAction
        if not dDelayAction:
            return None
        dArg = oState.GetArgValue(sSTKey, None)
        if not dArg:
            return None
        dArg['Add'].pop(sKey, 0)
        dArg['Mul'].pop(sKey, 0)
        iBaseValue = oState.GetArgValue('BaseValue', 0)
        dDelayAction['delay'] = CalStateDelayTime(iBaseValue, dArg)

    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    oState = oTarget.m_State.GetItemBySID(iStateSID)
    if not oState:
        return None
    dTempDelayAction = oState.m_DelayAction
    if not dTempDelayAction:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dDelayAction = { }
    dDelayAction.update(dTempDelayAction)
    iAdd = cl_formula.GetResultByData(oTarget, iAdd, dEventInfo)
    iMul = cl_formula.GetResultByData(oTarget, iMul, dEventInfo)
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = 'EventCBChangeTargetStateDelayTime-' + oLifeCycle.Key()
    sSTKey = 'EventCBChangeTargetStateDelayTime-' + oState.Key()
    iBaseValue = oState.GetArgValue('BaseValue', 0)
    if not iBaseValue:
        iBaseValue = dTempDelayAction['delay']
        oState.UpdateArgValue({
            'BaseValue': iBaseValue })
    dArg = oState.GetArgValue(sSTKey, {
        'Add': { },
        'Mul': { } })
    dArg['Add'][sKey] = iAdd
    dArg['Mul'][sKey] = iMul
    oState.UpdateArgValue({
        sSTKey: dArg })
    dDelayAction['delay'] = CalStateDelayTime(iBaseValue, dArg)
    oState.m_DelayAction = dDelayAction
    oLifeCycle.AddDisableFunc(ClearFunc)


def CalStateDelayTime(iBaseValue, dArg):
    iAdd = 0
    iMul = 10000
    for _iAdd, _iMul in zip(dArg['Add'].values(), dArg['Mul'].values()):
        iAdd += _iAdd
        if _iMul < -10000:
            _iMul = -10000
        iMul = iMul * (10000 + _iMul) // 10000
    
    iBaseValue = (iBaseValue + iAdd) * iMul // 10000
    if iBaseValue < 0:
        return 0
    return iBaseValue


def EventCBGetPFTransDamFactor(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'TransDamFactor' in dMsgInfo:
        return dMsgInfo['TransDamFactor']
    if 'Skill' not in dMsgInfo:
        return { }
    oSkill = dMsgInfo['Skill']
    if 'TransDamFactor' in oSkill.m_Custom:
        return oSkill.m_Custom['TransDamFactor']
    return { }


def EventSetStateStatistics(oListener, oEventCB, sKey, iVal):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iStateOwner = dMsgInfo['VID']
    iStateID = dMsgInfo['StateID']
    oStateOwner = oListener.m_Game.GetObject(iStateOwner)
    if not oStateOwner:
        return None
    oStateCon = oStateOwner.m_State
    oState = oStateCon.GetItem(iStateID)
    if not oState:
        return None
    oState.m_Data[sKey] = iVal


def EventCBGetRelicName(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NewRelic' in dMsgInfo:
        iRelic = dMsgInfo['NewRelic']
    elif 'iPerform' in dMsgInfo:
        iRelic = dMsgInfo['iPerform']
    else:
        return ''
    clsRelic = cl_perform.GetPerformModule(iRelic)
    if not clsRelic:
        return ''
    if 'Level' in dMsgInfo and dMsgInfo['Level'] == 2:
        return '强化·' + clsRelic.m_Name
    return clsRelic.m_Name


def EventAddDemonReward(oListener, oEventCB, iDropType, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Reward' not in dMsgInfo or not dMsgInfo['Reward']:
        return None
    (_, lstReward, _) = dMsgInfo['Reward'][0]
    dInfo['Group'] = oListener.m_Game.m_WarMgr.AddDropGroup()
    dReward = {
        'item': VIRTUAL_ITEM_DROP,
        'info': {
            'DropType': iDropType,
            'DropInfo': [
                dInfo] } }
    lstReward.append(dReward)


def EventCBSendEmote(oListener, oEventCB, dHeroEmote, iSendAll = 0):
    import cl_signal.net
    oGame = oListener.m_Game
    iScene = oListener.m_Scene
    oScene = oListener.m_Game.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iHeroSID = oListener.m_SID
    dEmote = dHeroEmote[iHeroSID] if iHeroSID in dHeroEmote else dHeroEmote[0]
    iEmote = ChooseKey(oGame, dEmote)
    if iEmote < 1000:
        iEmote = cl_platformdata.GetHeroEmotion(iHeroSID, iEmote)
    if iEmote <= 0:
        return None
    iEmote = cl_formula.GetResultByData(oListener, iEmote, dEventInfo)
    if iSendAll:
        dPlayer = oGame.m_WarMgr.GetRoomPlayer()
    else:
        dPlayer = oScene.GetPlayers()
    cl_signal.net.GS2CSignInfo(oGame, dPlayer, oListener.m_ID, iEmote)


def EventCBChangeEventPerformDamType(oListener, oEventCB, iDamType):
    
    def ClearChangeEventPerformDamType(oListener, oEventCB):
        oChangePerform = oListener.GetPerform(iChangePerform)
        if not oChangePerform:
            return None
        oChangePerform.m_ElementTypeObj.RemoveSetModify(sKey)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    iChangePerform = dMsgInfo['Skill'].m_Base['pfid']
    oChangePerform = oListener.GetPerform(iChangePerform)
    if not oChangePerform:
        return None
    iDamType = cl_formula.GetResultByData(oListener, iDamType, {
        'LifeCycle': oLifeCycle })
    oChangePerform.m_ElementTypeObj.SetModify(sKey, iDamType)
    oLifeCycle.AddDisableFunc(ClearChangeEventPerformDamType)


def EventCBRemoveBulletDropMiniGameBySID(oListener, oEventCB, dSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstNoChoose = dMsgInfo['NoChoose'] if 'NoChoose' in dMsgInfo else []
    for iSID in dSID:
        if iSID not in lstNoChoose:
            lstNoChoose.append(iSID)
    
    dMsgInfo['NoChoose'] = lstNoChoose


def EventCBChangeBulletDropMiniGameChooseWeight(oListener, oEventCB, iBulletType, iMul, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dChooseWeight = dMsgInfo['ChooseWeight'] if 'ChooseWeight' in dMsgInfo else { }
    if not dChooseWeight:
        return None
    dBulletBag = dMsgInfo['BulletBag'] if 'BulletBag' in dMsgInfo else { }
    if not dBulletBag:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo)
    for index, dDrop in dBulletBag.items():
        if iBulletType in dDrop:
            dChooseWeight[index] = dChooseWeight[index] * iMul // 10000 + iAdd
    


def EventCBAddEventStateTime(oListener, oEventCB, iTime, iMaxTime):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iState = dMsgInfo['StateSID'] if 'StateSID' in dMsgInfo else 0
    if not iState:
        SendAlert('err', '%s事件回调没有状态信息,请检查监听消息是否正确' % oEventCB.m_Key)
        return None
    oState = oListener.m_State.GetItemBySID(iState)
    if not oState:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iMaxTime = cl_formula.GetResultByData(oListener, iMaxTime, dEventInfo, dMsgInfo)
    cl_state.AddTime(oState, oListener, Time2Frame(iTime), Time2Frame(iMaxTime))


def EventCBSetCurDamMustElementRestraint(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sDamKey in ('MainDam', 'FlowDam'):
        if sDamKey not in dMsgInfo:
            continue
        for idx, (iDam, oReason) in enumerate(dMsgInfo[sDamKey]):
            oNewReason = oReason.ExtInfo({
                'MustElementRestraint': 1 })
            dMsgInfo[sDamKey][idx] = [
                iDam,
                oNewReason]
        
    


def EventCBSetCurDamImmuneElementRestraint(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sDamKey in ('MainDam', 'FlowDam'):
        if sDamKey not in dMsgInfo:
            continue
        for idx, (iDam, oReason) in enumerate(dMsgInfo[sDamKey]):
            oNewReason = oReason.ExtInfo({
                'ImmuneElementRestraint': 1 })
            dMsgInfo[sDamKey][idx] = [
                iDam,
                oNewReason]
        
    


def EventCBCreateClonePetAtDiePos(oListener, oEventCB):
    if not oListener.m_EnterBattle:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DiePos' not in dMsgInfo or not dMsgInfo['DiePos']:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    oListener.CreateClone(dMsgInfo['DiePos'], sKey)


def EventCBTargetAddShareSpell(oListener, oEventCB, iSpell):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if oTarget and oTarget.m_FightType == WARRIOR_PET_MINICLONE:
            oTarget.AddShareSpell(iSpell)
    


def EventCBSetPetBronPos(oTarget, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Pet' not in dMsgInfo or 'Pos' not in dMsgInfo:
        return None
    oPet = oTarget.m_Game.GetObject(dMsgInfo['Pet'])
    if not oPet:
        return None
    oPet.Set('PetBornPos', dMsgInfo['Pos'])


def EventCBSendNotify(oTarget, oEventCB, bToSelf, iChat, dReplaceInfo):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oLifeCycle.Key()
    if not iChat:
        SendAlert('err', '%s对白编号未指定，请对照通用对白表中对白编号填写' % sKey)
        return None
    oGame = oTarget.m_Game
    if bToSelf:
        if not oTarget.m_FightType & WARRIOR_HERO:
            SendAlert('err', '%s目标类型为%s，非玩家无法进行提示' % (sKey, oTarget.m_Type))
            return None
        dPlayers = {
            oTarget.m_PlayerID: 1 }
    else:
        oScene = oGame.m_SceneMgr.GetScene(oTarget.m_Scene)
        if not oScene:
            return None
        dPlayers = oScene.GetPlayers()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if dReplaceInfo:
        for key, value in dReplaceInfo.items():
            if callable(value):
                value = cl_formula.GetResultByData(oTarget, value, dEventInfo, dMsgInfo)
            dReplaceInfo[key] = str(value)
        
    cl_notify.SendCommonNotify(oGame, dPlayers, iChat, dReplaceInfo)


def EventCBEnableTempRelic(oTarget, oEventCB, iMaxNum, iTempLevel):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    lstReceive = dMsgInfo['Result']
    iReceiveNum = len(lstReceive)
    if iReceiveNum != iMaxNum:
        if iReceiveNum > iMaxNum:
            lstReceive = lstReceive[:iMaxNum]
        if iReceiveNum < iMaxNum:
            lstReceive = lstReceive + [
                0] * (iMaxNum - iReceiveNum)
    oRelicCon = oTarget.m_RelicCon
    lstNowRelic = oTarget.QuerySavedData('SeasonSuit_NowRelic', [])
    dBanRelic = oTarget.QuerySavedData('SeasonSuit_BanRelic', { })
    for iNowRelic in lstNowRelic:
        if iNowRelic not in lstReceive:
            oPerform = oRelicCon.GetPerform(iNowRelic)
            if not oPerform:
                continue
            oPerform.RemoveOtherLifeCycle(oTarget, RELIC_LIFECYCLE_TEMPLEVEL)
    
    lstAnwer = []
    dInfo = {
        'TempLevel': iTempLevel }
    for iRelic in lstReceive:
        oPerform = oRelicCon.GetPerform(iRelic)
        if not oPerform or iRelic in dBanRelic:
            lstAnwer.append(0)
            continue
        oPerform.SetOtherLifeCycle(oTarget, RELIC_LIFECYCLE_TEMPLEVEL, dInfo)
        lstAnwer.append(iRelic)
    
    oTarget.SetSavedData('SeasonSuit_NowRelic', lstAnwer)
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_INTENSIFY, lstAnwer, oTarget.m_Game, oTarget, iSendAll = 1)


def EventCBUpdateTempRelic(oTarget, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'iPerform' not in dMsgInfo:
        return None
    iRelic = dMsgInfo['iPerform']
    lstNowRelic = oTarget.SetDefaultSavedData('SeasonSuit_NowRelic', [])
    if iRelic not in lstNowRelic:
        return None
    lstNowRelic[lstNowRelic.index(iRelic)] = 0
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_INTENSIFY, lstNowRelic, oTarget.m_Game, oTarget, iSendAll = 1)


def EventSetTargetMustElementRestraint(oTarget, oEventCB):
    
    def ClearFunc(oTarget, oEventCB):
        oGame = oTarget.m_Game
        for iTarget in lstTar:
            oTarget = oGame.GetObject(iTarget)
            if not oTarget:
                continue
            oTarget.ClearMustElementRestraint(sKey)
        

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    if not dTransInfo['TargetList']:
        return None
    oLifeCycle = oEventCB.GetCBLifeCycle()
    sKey = oLifeCycle.m_Key
    oGame = oTarget.m_Game
    lstTar = []
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        lstTar.append(oTarget.m_ID)
        oTarget.SetMustElementRestraint(sKey)
    
    oLifeCycle.AddDisableFunc(ClearFunc)


def EventCBUpdateTempRelicByCoreRelic(oTarget, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'RelicSID' not in dMsgInfo:
        return None
    iRelic = dMsgInfo['RelicSID']
    oRelicCon = oTarget.m_RelicCon
    lstNowRelic = oTarget.SetDefaultSavedData('SeasonSuit_NowRelic', [])
    dBanRelic = oTarget.SetDefaultSavedData('SeasonSuit_BanRelic', { })
    if 'IsSet' in dMsgInfo:
        dBanRelic[iRelic] = 1
        if iRelic in lstNowRelic:
            oPerform = oRelicCon.GetPerform(iRelic)
            if oPerform:
                oPerform.RemoveOtherLifeCycle(oTarget, RELIC_LIFECYCLE_TEMPLEVEL)
            lstNowRelic[lstNowRelic.index(iRelic)] = 0
    if iRelic in dBanRelic and 'IsRemove' in dMsgInfo:
        dBanRelic.pop(iRelic)
    lstBanRelic = list(dBanRelic.keys())
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_BANRELIC, lstBanRelic, oTarget.m_Game, oTarget)
    cl_snetwar.GS2CSeasonSuitOptionInfo(SUIT_HANDLE_INTENSIFY, lstNowRelic, oTarget.m_Game, oTarget, iSendAll = 1)


def CBSetProbTimesInfo(oTarget, oEventCB, iLimit, iRatio, iMaxCnt, iExtraRatio, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iLimit = cl_formula.GetResultByData(oTarget, iLimit, dEventInfo, dMsgInfo)
    iRatio = cl_formula.GetResultByData(oTarget, iRatio, dEventInfo, dMsgInfo)
    iExtraRatio = cl_formula.GetResultByData(oTarget, iExtraRatio, dEventInfo, dMsgInfo)
    oGame = oTarget.m_Game
    iTimes = 0
    for iCnt in range(iMaxCnt):
        iRealRatio = iRatio + iCnt * iExtraRatio
        if oGame.Random(iLimit) < iRealRatio:
            iTimes += 1
        else:
            break
        if iTimes > iMaxCnt:
            break
    
    oSkill.m_Collect[sKey] = iTimes


def EventCBDirectEventCBFuncByNum(oListener, oEventCB, iNum, dGroup):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    if iNum not in dGroup:
        return None
    oEventCB.CBFuncAction(oListener, dGroup[iNum], dEventInfo, dMsgInfo)


def EventCBTargetDie(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    sKey = oEventCB.m_Key
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oReason = cl_object.reason.CStrReason(sKey, None, {
            'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
        oTarget.Set('RelifeInfo', { })
        oTarget.SetDiePriority(DIE_PRIORITY_KILL, sKey)
        oTarget.HPDirectModify('HP', 0, -(oTarget.m_HP), oReason)
    


def EventTriggerTargetEleAbnormal(oListener, oEventCB, iDam):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    if 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    else:
        iVictim = dMsgInfo['Skill'].m_Base['VID']
    oVictim = oListener.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim:
        return None
    oSkill = dMsgInfo['Skill']
    dEventInfo = oEventCB.GetCBEventInfo()
    iDam = cl_formula.GetResultByData(oListener, iDam, dEventInfo, dMsgInfo)
    iElementType = oSkill.m_Cache['ElementType'] if 'ElementType' in oSkill.m_Cache else DAM_TYPE_NORMAL
    oReason = oSkill.m_Base['RS'].ExtInfo({
        'DamType': iElementType })
    oVictim.m_EleAbnormal.TryTriggerEleAbnormal(oSkill, iDam, oReason)


def EventCBSetEventPerformAttr(oListener, oEventCB, sAttr, iMul, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iPerform = oSkill.m_Base['pfid']
    elif 'Perform' in dMsgInfo:
        iPerform = dMsgInfo['Perform']
    else:
        return None
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.AttrChange(sAttr, oEventCB.Key(), iMul, iAdd)
    oLifeCycle = oEventCB.GetCBLifeCycle()
    oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1


def EventCBCalCountByMonsterFightType(oListener, oEventCB, dTypeCount):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    iCount = 0
    oGame = oListener.m_Game
    dCount = {
        'Normal': 0,
        'Elite': 0,
        'Boss': 0 }
    dCount.update(dTypeCount)
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_FightType & WARRIOR_NORMAL == WARRIOR_NORMAL:
            iCount += dCount['Normal']
            continue
        if oTarget.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            iCount += dCount['Elite']
            continue
        if oTarget.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            iCount += dCount['Boss']
    
    return iCount


def EventCBSetTargetByID(oListener, oEventCB, iTargetID):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    iTargetID = cl_formula.GetResultByData(oListener, iTargetID, dEventInfo, dMsgInfo)
    dTransInfo['TargetList'] = [
        iTargetID]


def EventCBChangeShowShopRelic(oListener, oEventCB, iRelic, iMaxNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'GoodsMenu' not in dMsgInfo or 'ShopNpc' not in dMsgInfo:
        return 0
    oShopNpc = oListener.m_Game.GetObject(dMsgInfo['ShopNpc'])
    if not oShopNpc or oShopNpc.m_FightType not in (NWARRIOR_NPC_SHOP, NWARRIOR_NPC_GSCASHSHOP):
        return 0
    dEventInfo = oEventCB.GetCBEventInfo()
    iMaxNum = cl_formula.GetResultByData(oListener, iMaxNum, dEventInfo, dMsgInfo)
    dGoodsMenu = dMsgInfo['GoodsMenu']
    oBuyMgr = oListener.m_BuyMgr
    iNum = 0
    for iPos, oGoods in dGoodsMenu.items():
        if iNum >= iMaxNum:
            break
        if oGoods.m_GoodsType != VIRTUAL_ITEM_RELIC or oBuyMgr.IsHidden(iPos, oGoods) or not oShopNpc.CanReplace(oListener, iPos, oGoods):
            continue
        lstGoods = DeepCopy(oGoods.m_Items)
        for dGoods in lstGoods:
            dGoods['info']['sid'] = iRelic
        
        oNewGoods = cl_shop.CreateGoodsByData(iRelic, VIRTUAL_ITEM_RELIC, oGoods.m_Cash, oGoods.m_CashType, oGoods.m_CanBuy, lstGoods, oGoods.m_Hidden)
        dGoodsMenu[iPos] = oNewGoods
        iNum += 1
    
    return iNum


def EventCBClearPerformDamType(oListener, oEventCB, iObjectType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Perform' not in dMsgInfo:
        return None
    iPerform = dMsgInfo['Perform']
    oTarget = oListener.GetOwnObject(iObjectType)
    if not oTarget:
        return None
    oPerform = oTarget.GetPerform(iPerform)
    if not oPerform:
        return None
    oPerform.m_ElementTypeObj.RemoveSetModify(oEventCB.Key())


def EventCBSetUsePerformData(oListener, oEventCB, sKey, value, iCustom, iCheckValue):
    if iCheckValue and not value:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if iCustom:
        sTransKey = 'CustomPerformData'
    else:
        sTransKey = 'PerformData'
    dTransData = dTransInfo.setdefault(sTransKey, { })
    dTransData[sKey] = value


def EventCBCustomUsePerform(oListener, oEventCB, iPerform, dData, dCustom, iItem = 0):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iPerform = cl_formula.GetResultByData(oListener, iPerform, dEventInfo, dMsgInfo)
    iItem = cl_formula.GetResultByData(oListener, iItem, dEventInfo, dMsgInfo)
    oPerform = oListener.GetPerform(iPerform, iItem)
    if not oPerform:
        return None
    dData = cl_formula.CalArgsFormula(oListener, dData, dEventInfo, dMsgInfo)
    dCustom = cl_formula.CalArgsFormula(oListener, dCustom, dEventInfo, dMsgInfo)
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'CustomPerformData' in dTransInfo:
        dCustom.update(dTransInfo['CustomPerformData'])
    if 'PerformData' in dTransInfo:
        dData.update(dTransInfo['PerformData'])
    dData['Custom'] = dCustom
    cl_war.UsePerform(oListener, oPerform, dData)


def EventCBGetDirAwayAttack(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AID' not in dMsgInfo:
        return None
    oAttack = oListener.m_Game.GetObject(dMsgInfo['AID'])
    if not oAttack:
        return None
    return cl_math.Vec3Minus(oListener.GetPos(), oAttack.GetPos())


def EventCBGetHitPos(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTarget = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'DirectHitCurPos' in oSkill.m_Collect:
            return oSkill.m_Collect['DirectHitCurPos']
        if 'CurHitPos' in oSkill.m_Update:
            return oSkill.m_Update['CurHitPos']
        iTarget = oSkill.m_Update['CurVID'] if 'CurVID' in oSkill.m_Update else oSkill.m_Base['VID']
    elif 'CurVID' in dMsgInfo:
        iTarget = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iTarget = dMsgInfo['VID']
    if not iTarget:
        ErrLog.TraceAlert('%d %d %d get hit pos err %s' % (oListener.m_Game.m_ID, oListener.m_ID, oListener.m_PlayerID, dMsgInfo))
        return (0, 0, 0)
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        ErrLog.TraceAlert('%d %d %d get hit pos err %d %s' % (oListener.m_Game.m_ID, oListener.m_ID, oListener.m_PlayerID, iTarget, dMsgInfo))
        return (0, 0, 0)
    return oTarget.GetCenter()


def EventCBLimitNPCChooseTask(oListener, oEventCB, iChooseNum, dQuality):
    if iChooseNum > 3 and iChooseNum < 0:
        SendAlert('err', '%s数值异常 %s' % (oEventCB.m_Key, iChooseNum))
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NpcID' in dMsgInfo:
        iNpcID = dMsgInfo['NpcID']
        oNpc = oListener.m_Game.GetObject(iNpcID)
        dLimitTaskInfo = { }
        lstQuality = []
        if dQuality:
            lstQuality = list(dQuality)
        dLimitTaskInfo[oListener.m_ID] = {
            'ChooseNum': iChooseNum,
            'Quality': lstQuality }
        oNpc.SetArgValue('LimitTaskInfo', dLimitTaskInfo)


def EventCBAddDeadPunishmentTimes(oListener, oEventCB, iTimes):
    if not iTimes:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iTimes = cl_formula.GetResultByData(oListener, iTimes, dEventInfo, dMsgInfo)
    sKey = oEventCB.m_Key
    lstTarget = dTransInfo['TargetList']
    for iTarget in lstTarget:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        oTarget.AddDeadPunishmentTimes(iTimes, sReason = sKey)
    


def EventCBAddExcessAttr(oListener, oEventCB, sAttr, iAdd, iCalMul, iHPModify = 1):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iCalMul:
        oListener.AddExcessAttr(sAttr, iAdd, iHPModify)
    else:
        oListener.TrueModifyExcessAttr(sAttr, iAdd, iHPModify)


def EventCBCostSourceWeaponBullet(oListener, oEventCB, iNum, iCostBagBullet = 0):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    iItemID = dMsgInfo['ItemID']
    oWeapon = oListener.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    iCurBullet = oBulletCom.m_CurBullet
    iRemainBullet = iCurBullet - iNum
    if iRemainBullet >= 0:
        oBulletCom.BulletModify(-iNum)
    elif iCostBagBullet:
        if iCurBullet > 0:
            iNum = iNum - iCurBullet
            oBulletCom.BulletModify(-iCurBullet)
        sKey = oEventCB.m_Key
        iBulletSID = oBulletCom.m_BulletType
        iBagBullet = oListener.m_BulletCon.m_Bullet[iBulletSID]
        if iBagBullet >= iNum:
            oListener.m_BulletCon.BulletModify(iBulletSID, -iNum, sKey)
        elif iBagBullet > 0:
            oListener.m_BulletCon.BulletModify(iBulletSID, -iBagBullet, sKey)


def EventCBCostSourceWeaponBagBullet(oListener, oEventCB, iNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SID' not in dMsgInfo:
        return None
    iBulletSID = dMsgInfo['SID']
    oBulletCon = oListener.m_BulletCon
    if iBulletSID not in oBulletCon.m_Bullet:
        return None
    iBullet = oBulletCon.m_Bullet[iBulletSID]
    sKey = oEventCB.m_Key
    if iBullet >= iNum:
        oBulletCon.BulletModify(iBulletSID, -iNum, sKey)
    elif iBullet > 0:
        oBulletCon.BulletModify(iBulletSID, -iBullet, sKey)


def EventCBRewardTalent(oTarget, oEventCB, iTalent, iExcludeTalent, iUseLib, iExcludeCurTalent):
    oGame = oTarget.m_Game
    oTalentCon = oTarget.m_TalentCon
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iTalent = cl_formula.GetResultByData(oTarget, iTalent, dEventInfo, dMsgInfo)
    iExcludeTalent = cl_formula.GetResultByData(oTarget, iExcludeTalent, dEventInfo, dMsgInfo)
    if iTalent == 0:
        dTalent = oTalentCon.GetAllValidTalent(iUseLib, iExcludeCurTalent)
        if iExcludeTalent in dTalent:
            dTalent.pop(iExcludeTalent)
        if not dTalent:
            return None
        iTalent = ChooseKey(oGame, dTalent)
    dReward = {
        'info': {
            'sid': iTalent } }
    cl_reward.RewardTalent(oGame, oTarget, dReward, oEventCB.Key(), { })


def EventCBReduceTalentLevel(oTarget, oEventCB, iTalent, iLevel):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iTalent = cl_formula.GetResultByData(oTarget, iTalent, dEventInfo, dMsgInfo)
    oTalentCon = oTarget.m_TalentCon
    oTalentCon.DeGradeTalent(iTalent, iLevel, oEventCB.Key())


def EventCBTempEnhanceWeapon(oListener, oEventCB, iWeaponType, sPrefixKey, iMaxAttr = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        dKeyData = oTarget.Query(sPrefixKey, { })
        dKeyData.pop(sEvKey)
        oTarget.Set(sPrefixKey, dKeyData)
        oWeapon = oTarget.m_WieldCon.GetCurWeapon(iWeaponType)
        if not oWeapon:
            return None
        if oWeapon.IsInitWeapon():
            return None
        sKey = 'TempEnhanceWeapon-%s-%s' % (sPrefixKey, oWeapon.m_ID)
        oEnhanceCom = oWeapon.GetComponent('Enhance')
        if dKeyData:
            if iMaxAttrFlag in dKeyData.values():
                oEnhanceCom.AddTempEnhance(sKey, iMaxAttrFlag)
            else:
                oEnhanceCom.AddTempEnhance(sKey)
            return None
        oEnhanceCom.ClearTempEnhance(sKey)

    oWeapon = oListener.m_WieldCon.GetCurWeapon(iWeaponType)
    if not oWeapon:
        return None
    if oWeapon.IsInitWeapon():
        return None
    sEvKey = oEventCB.Key()
    if not sPrefixKey:
        sPrefixKey = sEvKey
    sKey = 'TempEnhanceWeapon-%s-%s' % (sPrefixKey, oWeapon.m_ID)
    oEnhanceCom = oWeapon.GetComponent('Enhance')
    if not oEnhanceCom:
        return None
    dKeyData = oListener.SetDefault(sPrefixKey, { })
    dKeyData[sEvKey] = iMaxAttr
    iMaxAttrFlag = 1
    if iMaxAttrFlag in dKeyData.values():
        oEnhanceCom.AddTempEnhance(sKey, iMaxAttrFlag)
    else:
        oEnhanceCom.AddTempEnhance(sKey, iMaxAttr)
    oLifeCycle = oEventCB.GetCBLifeCycle()
    sUniqueKey = 'ClearTempEnhance'
    oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 1)


def EventCBSetPlusRandom(oListener, oEventCB, iPlusRandom):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PlusRandom' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iPlusRandom = cl_formula.GetResultByData(oListener, iPlusRandom, dEventInfo, dMsgInfo)
    dMsgInfo['PlusRandom'] = iPlusRandom


def EventCBRemoveWeaponTempEnhance(oListener, oEventCB, sPrefixKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oWeapon = None
    if 'oItem' in dMsgInfo:
        oWeapon = dMsgInfo['oItem']
    elif 'ItemID' in dMsgInfo:
        iWeaponID = dMsgInfo['ItemID']
        oWeapon = oListener.m_WieldCon.GetItemByID(iWeaponID)
    if oWeapon is None:
        return None
    if oWeapon.IsInitWeapon():
        return None
    if not sPrefixKey:
        sPrefixKey = oEventCB.Key()
    sKey = 'TempEnhanceWeapon-%s-%s' % (sPrefixKey, oWeapon.m_ID)
    oEnhanceCom = oWeapon.GetComponent('Enhance')
    if not oEnhanceCom:
        return None
    oEnhanceCom.ClearTempEnhance(sKey)


def EventCBRecordValueToInfoList(oListener, oEventCB, sKey, iValue):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return None
    lstInfo = oLifeCycleOwner.SetArgValueDefault(sKey, [])
    lstInfo.append(iValue)


def EventCBReplaceCreateNpc(oListener, oEventCB, iNpcSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    if 'Scene' not in dMsgInfo:
        WarnpcLog.TraceAlert('%s %s %s replacenpc fail %d' % (oGame.m_ID, oListener.m_PlayerID, oEventCB.m_Key, iNpcSID))
        return None
    if iNpcSID == dMsgInfo['NPC']:
        return None
    dNpcInfo = dMsgInfo['NPCInfo']
    dVisiblePlayer = dNpcInfo['VisiblePlayer'] if 'VisiblePlayer' in dNpcInfo else { }
    if not dVisiblePlayer:
        lstHero = oGame.m_WarMgr.GetRoomHero()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            dVisiblePlayer[oHero.m_PlayerID] = 1
        
    if oListener.m_PlayerID not in dVisiblePlayer:
        return None
    dVisiblePlayer[oListener.m_PlayerID] = 0
    dNpcInfo['VisiblePlayer'] = dVisiblePlayer
    dExtInfo = { }
    if 'Pos' in dNpcInfo:
        dExtInfo['Pos'] = dNpcInfo['Pos']
    if 'Facing' in dNpcInfo:
        dExtInfo['Facing'] = dNpcInfo['Facing']
    if 'Abandoner' in dNpcInfo:
        dExtInfo['Abandoner'] = dNpcInfo['Abandoner']
    dExtInfo['Scene'] = dMsgInfo['Scene']
    cl_action.CommonCreateNpc(oListener, oEventCB.GetCBLifeCycle(), iNpcSID, 1, dExtInfo)


def EventCBGetTargetName(oListener, oEventCB, iTargetType):
    if iTargetType == OBJ_SELF:
        oTarget = oListener
    else:
        iTarget = 0
        if iTargetType == OBJ_ATTACK:
            dMsgInfo = oEventCB.GetCBMsgInfo()
            if 'AID' in dMsgInfo:
                iTarget = dMsgInfo['AID']
            elif 'Skill' in dMsgInfo:
                iTarget = dMsgInfo['Skill'].m_Base['AID']
            else:
                dMsgInfo = oEventCB.GetCBMsgInfo()
                if 'CurVID' in dMsgInfo:
                    iTarget = dMsgInfo['CurVID']
                elif 'VID' in dMsgInfo:
                    iTarget = dMsgInfo['VID']
                elif 'Skill' in dMsgInfo:
                    oSkill = dMsgInfo['Skill']
                    iTarget = oSkill.m_Base['VID']
                    if not iTarget and 'CurVID' in oSkill.m_Update:
                        iTarget = oSkill.m_Update['CurVID']
        oTarget = None.m_Game.GetObject(iTarget)
    if not oTarget:
        return ''
    return oTarget.Name()


def EventCBCloseRelifeNotify(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['CloseNotify'] = 1


def EventCBSetAttackTargetBySceneAureoleOwner(oListener, oEventCB, sKey):
    oGame = oListener.m_Game
    iScene = oListener.m_Scene
    dAttTar = { }
    for iWarrior in oGame.m_AureoleMgr.GetAureoleOwner(sKey):
        oWarrior = oGame.GetObject(iWarrior, PY_FLAG_DEAD)
        if not oWarrior or oWarrior.m_Scene != iScene:
            continue
        dAttTar[iWarrior] = 1
    
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['AttackTarget'] = dAttTar


def EventCBTriggerGroupByAttackTarget(oListener, oEventCB, iGroup):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'AttackTarget' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置事件执行目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for iAttackTarget in dTransInfo['AttackTarget']:
        dMsgInfo['AID'] = iAttackTarget
        oEventCB.CBFuncAction(oListener, iGroup, dEventInfo, dMsgInfo)
    


def EventCBModifyExtraLotteryCnt(oListener, oEventCB, iCnt):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Npc' not in dMsgInfo:
        return None
    oNpc = oListener.m_Game.GetObject(dMsgInfo['Npc'])
    if not oNpc or oNpc.m_FightType != NWARRIOR_NPC_RELICLOTTERY:
        return None
    oNpc.ModifyExtraLotteryCnt(oListener, iCnt)


def EventCBModifyInputRelicLotteryQuality(oListener, oEventCB, iQuality):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Quality' not in dMsgInfo:
        return None
    dMsgInfo['Quality'] = iQuality


def EventSetStateStatisticsData(oListener, oEventCB, iStateSID, sDictKey, iKey):
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iKey = cl_formula.GetResultByData(oListener, iKey, dEventInfo, dMsgInfo)
    if 'arg' not in oState.m_StateInfo:
        oState.m_StateInfo['arg'] = { }
    dArg = oState.m_StateInfo['arg']
    if sDictKey not in dArg:
        dArg[sDictKey] = { }
    dArg[sDictKey][iKey] = 1


def EventCBGetTargetByAIFollowTarget(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    oElement = oListener.m_Game.m_WarMgr.GetComponent('TeammateAI')
    dTransInfo['TargetList'] = []
    if oElement:
        oTarget = oElement.GetFollowTarget(oListener.m_ID)
        if oTarget:
            dTransInfo['TargetList'] = [
                oTarget.m_ID]


def EventCBGetTargetPositiveFactorAttr(oListener, oEventCB, sAttr):
    sKey = oEventCB.m_Key
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    lstTarget = dTransInfo['TargetList']
    if not lstTarget:
        return None
    oTarget = oListener.m_Game.GetObject(lstTarget[0])
    if not oTarget:
        return None
    oAttr = oTarget.GetAttr(sAttr)
    (iTotalMul, iTotalAdd) = (0, 0)
    for iMul, iAdd in oAttr.m_FactorInfo.values():
        if iMul > 0:
            iTotalMul += iMul
        if iAdd > 0:
            iTotalAdd += iAdd
    
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.m_Apply[sAttr] = 1
    oListener.AttrChange(sAttr, iTotalMul, iTotalAdd, sKey)


def EventCBSetMiniGameChooseCnt(oListener, oEventCB, iCount):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ChooseCnt' not in dMsgInfo:
        return None
    dMsgInfo['ChooseCnt'] = iCount


def EventTargetListSortBySelfDis(oListener, oEventCB, iTargetMinNum):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGame = oListener.m_Game
    dDis = oGame.Scene_GetTargetDisMap(oListener.m_ID, list(dTransInfo['TargetList']))
    lstTargetList = sorted(dDis, key = dDis.get)
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTargetMinNum = cl_formula.GetResultByData(oListener, iTargetMinNum, dEventInfo, dMsgInfo)
    iLackNum = iTargetMinNum - len(lstTargetList)
    if iLackNum > 0:
        iLen = len(lstTargetList)
        if iLackNum <= iLen:
            lstLackTarget = ChooseMulKeys(oListener.m_Game, dict.fromkeys(lstTargetList, 1), iLackNum)
        else:
            lstLackTarget = lstTargetList * (iLackNum // iLen)
            lstLackTarget.extend(lstTargetList[:iLackNum % iLen])
        lstTargetList.extend(lstLackTarget)
    dTransInfo['TargetList'] = lstTargetList


def EventGetSkillActNum(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return 0
    oSkill = dMsgInfo['Skill']
    return oSkill.m_Base['ActNum']


def EventCBSetWeaponRepeatInfo(oListener, oEventCB, iRepeatCnt, iRepeatCold):
    
    def ClearFunc(oTarget, oLifeCycle):
        oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
        if not oWeapon:
            return None
        oWeapon.RemoveRepeatInfo(sKey)

    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    elif 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    else:
        return None
    if not iWeapon:
        return None
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    sKey = oEventCB.Key()
    dEventInfo = oEventCB.GetCBEventInfo()
    iRepeatCnt = cl_formula.GetResultByData(oListener, iRepeatCnt, dEventInfo, dMsgInfo)
    iRepeatCold = cl_formula.GetResultByData(oListener, iRepeatCold, dEventInfo, dMsgInfo)
    oWeapon.SetRepeatInfo(sKey, iRepeatCnt, iRepeatCold)
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddUniqueDisableFunc('%s-%s' % (oEventCB.Key(), oWeapon.m_ID), ClearFunc, 0)


def EventCBUseTargetAsSourceWeaponFlag(oListener, oEventCB, sFlag):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTrans['TargetList']
    if not lstTar:
        return None
    dFlagTarget = oWeapon.SetDefaultTmp(sFlag, { })
    for iTarget in lstTar:
        dFlagTarget[iTarget] = 1
    


def EventCBAddWandCount(oListener, oEventCB, iCount):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oListener.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
    if not oWand:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    oWand.AddWandCount(iCount)


def EventCBSetWandCount(oListener, oEventCB, iCount):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oListener.m_WandCon.GetWandByID(oLifeCycleOwner.m_Item)
    if not oWand:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iCount = cl_formula.GetResultByData(oListener, iCount, dEventInfo, dMsgInfo)
    oWand.SetWandCount(iCount)


def EventCBSetWeaponPerformColdTime(oListener, oEventCB, iTime):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if 'ItemID' not in oSkill.m_Cache:
        return None
    iPerform = oSkill.m_Base['pfid']
    oPerform = oListener.GetPerform(iPerform, oSkill.m_Cache['ItemID'])
    if not oPerform:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iFrame = Time2Frame(iTime)
    iColdTimeFrame = oPerform.m_Container.GetColdTime(iPerform)
    iChangeFrame = iFrame - iColdTimeFrame
    oPerform.ModifyColdTime(iPerform, iChangeFrame)
    oPerform.ModifyNextAttackFrame(iChangeFrame)


def EventCBRandTriggerWandAction(oListener, oEventCB, iNum):
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, oEventCB.GetCBMsgInfo())
    if not iNum:
        return None
    oWand.RandomTriggerActionComp(iNum)


def EventCBReplaceGoodsToRandomByType(oListener, oEventCB, iNum, dReplaceType, iNewGoodSID, iReverse, iCash, iCashType):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if not iNum or 'ShopNpc' not in dMsgInfo:
        return None
    clsNewGood = cl_shop.goodsdata.GetGoodsData(iNewGoodSID)
    if not clsNewGood:
        SendAlert('err', '%s未定义的商品编号 %d' % (oEventCB.m_Key, iNewGoodSID))
        return None
    dGoodsMenu = dMsgInfo['GoodsMenu']
    oBuyMgr = oListener.m_BuyMgr
    lstReplace = []
    lstReplaceType = sorted(dReplaceType, key = dReplaceType.get, reverse = True)
    if iReverse:
        lstGoodsMenus = list(reversed(list(dGoodsMenu)))
    else:
        lstGoodsMenus = list(dGoodsMenu)
    for iType in lstReplaceType:
        for iPos in lstGoodsMenus:
            oGoods = dGoodsMenu[iPos]
            if not oBuyMgr.IsHidden(iPos, oGoods) and oGoods.m_GoodsType == iType:
                lstReplace.append(iPos)
                if len(lstReplace) >= iNum:
                    break
        
        if len(lstReplace) >= iNum:
            break
    
    iNewGoodType = clsNewGood.m_GoodsType
    for iPos in lstReplace:
        if iNewGoodType == VIRTUAL_ITEM_RANDOM:
            oGood = cl_shop.CreateRandGoods(iNewGoodSID, iCash, iCashType, 1, 0)
        elif iNewGoodType in (VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_AUTOPERFORM, VIRTUAL_ITEM_EQUIP, VIRTUAL_ITEM_RELIC):
            oGood = cl_shop.CreateGoodsByConfig(iNewGoodSID, iCash, iCashType, 1, 0)
        else:
            SendAlert('err', '%s 随机商品替换未支持的商品类型 %d %d %d' % (oEventCB.m_Key, iNewGoodSID, iNewGoodType, iPos))
        if oGood:
            dGoodsMenu[iPos] = oGood
            oGood.m_Pos = iPos
    
    WarnpcLog.Debug('%d %d %s rplranditem %d %d %d %s %s' % (oListener.m_Game.m_ID, oListener.m_PlayerID, oEventCB.m_Key, iNum, iNewGoodSID, iReverse, dReplaceType, lstReplace))


def EventCBSaveMonsterStatePolicy(oListener, oEventCB, sName):
    oEventSource = oEventCB.GetObject()
    if not oEventSource:
        return None
    if not oListener.m_Agent:
        return None
    sKey = 'StatePolicy%s' % sName
    dPolicy = oListener.m_Agent.GetData(sKey, { })
    if not dPolicy:
        return None
    oEventSource.SetArgValue(sKey, dPolicy)


def EventCBRecoverMonsterStatePolicy(oListener, oEventCB, sName):
    oEventSource = oEventCB.GetObject()
    if not oEventSource:
        return None
    sKey = 'StatePolicy%s' % sName
    dPolicy = oEventSource.PopArgValue(sKey, { })
    if not dPolicy:
        return None
    if not oListener.m_Agent:
        return None
    oListener.m_Agent.SetData(sKey, dPolicy)


def EventCBSetWandExtActionCompNum(oListener, oEventCB, iNum, iNotyfiy):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Wand' not in dMsgInfo:
        return None
    oWand = oListener.m_WandCon.GetWandByID(dMsgInfo['Wand'])
    if not oWand:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, oEventCB.GetCBMsgInfo())
    oWand.SetExtActionComp(oEventCB.Key(), iNum, iNotyfiy)


def EventCBSetShopNpcMaxRelic(oListener, oEventCB, iNum):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'NPC' in dMsgInfo:
        iNPCID = dMsgInfo['NPC']
    elif 'NpcID' in dMsgInfo:
        iNPCID = dMsgInfo['NpcID']
    elif 'ShopNpc' in dMsgInfo:
        iNPCID = dMsgInfo['ShopNpc']
    else:
        return None
    oNpc = oListener.m_Game.GetObject(iNPCID)
    if not oNpc or oNpc.m_FightType != NWARRIOR_NPC_SHOP:
        return None
    iNum = cl_formula.GetResultByData(oListener, iNum, oEventCB.GetCBEventInfo(), dMsgInfo)
    oNpc.SetMaxRelicGoodsNum(oListener.m_ID, iNum)


def EventCBCreateSeed(oListener, oEventCB, iCheckPos, iNum = 1, iCheckID = 0):
    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo)
    iCheckID = cl_formula.GetResultByData(oListener, iCheckID, dEventInfo)
    if iCheckID:
        oListener = oGame.GetObject(iCheckID)
    if oListener.m_SID != GARDENER_HERO:
        SendAlert('err', '%s园丁才可以创建种子' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetPos' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置位置' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return None
    vTargetPos = dTransInfo['TargetPos']
    oListener.m_GardenerCon.CreateSeed(vTargetPos, oEventCB.m_Key, iCheckPos, iNum)


def EventCBCreatePlantInPos(oListener, oEventCB, iCheckPos, iFieldCenterPos, fDetectArea = 0, fCollisionFactor = 1):
    if oListener.m_SID != GARDENER_HERO:
        SendAlert('err', '%s园丁才可以创建植物' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return None
    if iFieldCenterPos:
        vTargetPos = oListener.Query('FieldCenterPos', ())
        if not vTargetPos:
            return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetPos' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置位置' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return None
    vTargetPos = dTransInfo['TargetPos']
    oListener.m_GardenerCon.CreatePlant(vTargetPos, PLANT_PHASE_NORMAL, iCheckPos, fDetectArea = fDetectArea, fCollisionFactor = fCollisionFactor, sReason = oEventCB.m_Key)


def EventCBWandItemInBag(oListener, oEventCB, iSID, iLevel, iNum, iItemType):
    sKey = oEventCB.m_Key
    if iNum <= 0:
        SendAlert('err', '%s奖励数量异常:%d' % (sKey, iNum))
        return None
    if iItemType == VIRTUAL_ITEM_WAND:
        dAllWand = GetAllWand()
        if iSID not in dAllWand:
            SendAlert('err', '%s不存在该法杖SID:%d' % (sKey, iSID))
            return None
        sReason = '%sRewardWand' % sKey
        for _ in range(iNum):
            oListener.m_WandCon.RewardWand(iSID, iLevel, sReason)
        
    elif iItemType == VIRTUAL_ITEM_WANDCOMP:
        dAllWandComp = GetAllWandComp()
        if iSID not in dAllWandComp:
            SendAlert('err', '%s不存在该法杖模块SID:%d' % (sKey, iSID))
            return None
        sReason = '%sRewardWandComp' % sKey
        oListener.m_WandCon.AddBagComp(iSID, iLevel, iNum, sReason)


def EventCBSetInteractHitFlag(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'OriginID' not in dMsgInfo or 'TriggerFrame' not in dMsgInfo:
        return None
    iOriginID = dMsgInfo['OriginID']
    iTriggerFrame = dMsgInfo['TriggerFrame']
    tHitFlag = (iOriginID, iTriggerFrame)
    lstHitFlag = oListener.Query(sKey, [])
    if tHitFlag in lstHitFlag:
        return None
    lstHitFlag.append(tHitFlag)
    oListener.Set(sKey, lstHitFlag)


def EventCBHatchSeed(oListener, oEventCB):
    if oListener.m_SID != GARDENER_HERO:
        SendAlert('err', '%s园丁才可以孵化种子' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SeedID' not in dMsgInfo:
        return None
    oListener.m_GardenerCon.HatchSeed(dMsgInfo['SeedID'], oEventCB.Key())


def EventCBTriggerSeedShoot(oListener, oEventCB, iCheckPos):
    if oListener.m_SID != GARDENER_HERO:
        SendAlert('err', '%s园丁才可以触发种子射击' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetPos' not in dTransInfo:
        SendAlert('err', '%s种子射击回调未设置位置' % oEventCB.GetStableKey(oEventCB.GetCBEventInfo()))
        return None
    oListener.m_GardenerCon.TriggerSeedShoot(dTransInfo['TargetPos'], iCheckPos, oEventCB.m_Key)


def EventCBRecordSkill(oListener, oEventCB, sKey):
    oEventSource = oEventCB.GetObject()
    if not oEventSource:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iActNum = oSkill.m_Base['ActNum']
    dInfo = oEventSource.SetArgValueDefault(sKey, { })
    dInfo[iActNum] = 1


def EventCBDelRecordSkill(oListener, oEventCB, sKey):
    oEventSource = oEventCB.GetObject()
    if not oEventSource:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    iActNum = oSkill.m_Base['ActNum']
    dInfo = oEventSource.GetArgValue(sKey, { })
    dInfo.pop(iActNum, 0)


def EventCBAddRecordSkillDamFactor(oListener, oEventCB, sRecordKey, iAdd, iMul, iMask, iTransmit, iClearTransmit = 0):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearTransFactorInState(tStateUseTransFactor, sKey)

    oEventSource = oEventCB.GetObject()
    if not oEventSource:
        return None
    oGame = oListener.m_Game
    iAttack = oListener.m_ID
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    dActNum = oEventSource.GetArgValue(sRecordKey, { })
    sKey = oEventCB.m_Key
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    for iActNum in list(dActNum):
        oSkill = oGame.m_SkillMgr.GetSkill(iAttack, iActNum)
        if not oSkill:
            dActNum.pop(iActNum)
            continue
        dFactor = oSkill.m_Collect['DamFactor'] if 'DamFactor' in oSkill.m_Collect else { }
        if sKey in dFactor:
            (iOldAdd, iOldMul, _) = dFactor[sKey]
            dFactor[sKey] = (iOldAdd + iAdd, iOldMul + iMul, iMask)
        else:
            dFactor[sKey] = (iAdd, iMul, iMask)
        oSkill.m_Collect['DamFactor'] = dFactor
        dTransFactor = oSkill.m_Custom['TransDamFactor'] if iTransmit == 1 or 'TransDamFactor' in oSkill.m_Custom else { }
        dTransFactor[sKey] = dFactor[sKey]
        oSkill.m_Custom['TransDamFactor'] = dTransFactor
        if iClearTransmit == 1:
            tStateUseTransFactor = oListener.GetStateUseTransFactor()
            if not tStateUseTransFactor:
                return None
            oLifeCycle = dEventInfo['LifeCycle']
            oLifeCycle.AddUniqueDisableFunc('EventCBAddRecordSkillDamFactor', ClearFunc, iCover = 0)
    


def EventCBAdditionDamage(oListener, oEventCB, iDam):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' not in dMsgInfo or 'PredictChange' not in dMsgInfo or 'ExcessChange' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iDam = cl_formula.GetResultByData(oListener, iDam, dEventInfo, dMsgInfo)
    if iDam <= 0:
        return None
    if dMsgInfo['ExcessChange'] > 0:
        dMsgInfo['ExcessChange'] += iDam
        return None
    oVictim = oListener.m_Game.GetObject(dMsgInfo['VID'])
    if not oVictim:
        return None
    lstHasValue = [
        oVictim.Shield(),
        oVictim.Armor(),
        oVictim.HP()]
    lstPredictChange = dMsgInfo['PredictChange']
    for idx in range(3):
        if lstHasValue[idx] > lstPredictChange[idx]:
            iRemain = lstHasValue[idx] - lstPredictChange[idx]
            if iRemain >= iDam:
                lstPredictChange[idx] += iDam
                return None
            lstPredictChange[idx] += lstHasValue[idx]
            iDam -= lstHasValue[idx]
    
    if iDam > 0:
        dMsgInfo['ExcessChange'] += iDam


def EventCBClearExtGrade(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        iItem = dMsgInfo['ItemID']
    elif 'Weapon' in dMsgInfo:
        iItem = dMsgInfo['Weapon']
    else:
        return None
    oWeapon = oListener.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    sKey = oEventCB.m_Key
    oWeapon.ClearExtGrade(sKey)


def EventCBCreatePlantByTargetPos(oListener, oEventCB, dShifInfo, iHpRatio, iCheckBossLevel = 0, iPhase = PLANT_PHASE_NORMAL, iGrade = 1, iChangeTarget = 0):
    if oListener.m_SID != GARDENER_HERO:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    oGame = oListener.m_Game
    sKey = oEventCB.m_Key
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    iTarget = dTransInfo['TargetList'][0]
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    vPos = oTarget.GetPos()
    oScene = oGame.m_SceneMgr.GetScene(oListener.m_Scene)
    if not oScene:
        return None
    oGardenerCon = oListener.m_GardenerCon
    iCheckPos = 1
    iLevel = oScene.m_Level
    if iCheckBossLevel and oGardenerCon.CheckUseBossLevelCreatePos(iLevel):
        (iRet, vTarget) = oGardenerCon.GetBossLevelAutoCreatePos(iLevel)
        if not iRet:
            return None
        iCheckPos = 0
    elif dShifInfo:
        iShiftDis = dShifInfo['Dis']
        tShiftDir = dShifInfo['Dir']
        vTarget = cl_math.Vec3DisplaceDir(vPos, tShiftDir, iShiftDis)
        vTarget = oListener.m_Game.Scene_NavMeshRayCast(oListener.m_Scene, vPos, vTarget)
    else:
        vTarget = vPos
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iGrade = cl_formula.GetResultByData(oTarget, iGrade, dEventInfo, dMsgInfo)
    iHpRatio = cl_formula.GetResultByData(oTarget, iHpRatio, dEventInfo, dMsgInfo)
    oPlant = oGardenerCon.CreatePlant(vTarget, iPhase, iCheckPos, sReason = sKey, iGrade = iGrade, iInitHPRatio = iHpRatio)
    if iChangeTarget:
        if not oPlant:
            dTransInfo['TargetList'] = []
        else:
            dTransInfo['TargetList'] = [
                oPlant.m_ID]


def EventCBRecordLimitedTimeInfo(oListener, oEventCB, iKey, iVal):
    oLifeCycle = oEventCB.GetCBLifeCycle()
    oLifeCycleOwner = oLifeCycle.GetObject()
    if not oLifeCycleOwner:
        return None
    dLimitedTimeInfo = oLifeCycleOwner.SetArgValueDefault('LimitedTimeInfo', { })
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iKey = cl_formula.GetResultByData(oListener, iKey, dEventInfo, dMsgInfo)
    iVal = cl_formula.GetResultByData(oListener, iVal, dEventInfo, dMsgInfo)
    dInfo = dLimitedTimeInfo.setdefault(iKey, { })
    iNowFrame = oListener.m_Game.GetFrameNum()
    if iNowFrame in dInfo:
        dInfo[iNowFrame] += iVal
    else:
        dInfo[iNowFrame] = iVal


def EventCBSetTransInfo(oListener, oEventCB, sKey, iVal):
    dTransInfo = oEventCB.GetCBTransInfo()
    iVal = cl_formula.GetResultByData(oListener, iVal, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    dTransInfo[sKey] = iVal


def EventCBSetStateArgVal(oListener, oEventCB, iStateSID, sKey, iSet):
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iSet = cl_formula.GetResultByData(oListener, iSet, dEventInfo, dMsgInfo)
    oState.SetArgValue(sKey, iSet)


def EventCBAddStateArgVal(oListener, oEventCB, iStateSID, sKey, iAdd):
    oStateCon = oListener.m_State
    oState = oStateCon.GetItemBySID(iStateSID)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oState.AddArgValue(sKey, iAdd)


def EventCBGetTargetAsTargetOwner(oListener, oEventCB):
    sKey = oEventCB.m_Key
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    lstTarget = dTransInfo['TargetList']
    if not lstTarget:
        return None
    iTarget = lstTarget[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    dTransInfo['TargetList'] = [
        oTarget.m_Owner] if oTarget.m_Owner else []


def EventCBMustEleAbnormal(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    lstMainDam = dMsgInfo['MainDam']
    for _, oReason in lstMainDam:
        oReason.SetInfo('MustEleAbnormal', 1)
    


def EventCBCannotEleAbnormal(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'MainDam' not in dMsgInfo:
        return None
    lstMainDam = dMsgInfo['MainDam']
    for _, oReason in lstMainDam:
        oReason.SetInfo('BanEleAbnormal', 1)
    


def EventCBCostPointSkillPFBullet(oListener, oEventCB, iPerform, iCost):
    oPerform = oListener.GetPerform(iPerform)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iCostCount = cl_formula.GetResultByData(oListener, iCost, dEventInfo, dMsgInfo)
    oPerform.CostPFBullet(iCostCount)


def EventCBAddDiceCanRollTimes(oListener, oEventCB, iTime = 1):
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Dice' not in dMsgInfo:
        return None
    iDice = dMsgInfo['Dice']
    oDice = oDiceCon.GetDiceByID(iDice)
    if not oDice:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    sReason = dMsgInfo.get('RS', 'AddDiceCanRollTimes')
    oDice.AddCanRollTimes(iTime, sReason)


def EventCBAddUpQualityDice(oListener, oEventCB, iQuality, iRandom, iChat):
    oDiceCon = oListener.m_DiceCon
    oGame = oListener.m_Game
    iPlayerID = oListener.m_PlayerID
    if not oDiceCon:
        DiceLog.Debug('%s %s eventadddice conerr' % (oGame.m_ID, iPlayerID))
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'DiceSID' not in dMsgInfo or 'QL' not in dMsgInfo:
        DiceLog.Debug('%s %s eventadddice key err' % (oGame.m_ID, iPlayerID))
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iQuality = cl_formula.GetResultByData(oListener, iQuality, dEventInfo, dMsgInfo)
    iNewQuality = dMsgInfo['QL'] + iQuality
    iQualityMax = max(DICE_QUALITY_ALL)
    iQualityMin = min(DICE_QUALITY_ALL)
    if iNewQuality > iQualityMax:
        iNewQuality = iQualityMax
    elif iNewQuality < iQualityMin:
        iNewQuality = iQualityMin
    if iRandom:
        oWarMgr = oGame.m_WarMgr
        oDiceElement = oWarMgr.GetDiceElement()
        if not oDiceElement:
            DiceLog.Debug('%s %s eventadddice elementerr' % (oGame.m_ID, iPlayerID))
            return None
        dAllDice = oDiceElement.GetAllUnLockDice(iPlayerID)
        dChooseWeight = { }
        for iDice in dAllDice:
            if iDice in GetExcludeDiceQuality(iNewQuality):
                continue
            dChooseWeight[iDice] = 1
        
        iDiceSID = ChooseKey(oGame, dChooseWeight)
        if not iDiceSID:
            DiceLog.Debug('%s %s eventadddice chooseerr %s %s' % (oGame.m_ID, oListener.m_PlayerID, iNewQuality, dChooseWeight))
            return None
    iDiceSID = dMsgInfo['DiceSID']
    dNewDiceInfo = oDiceCon.GetDiceInfo(iDiceSID, iNewQuality)
    oDiceCon.RewardDice(dNewDiceInfo, sReason = oEventCB.m_Key)
    if iChat:
        clsPerform = cl_perform.GetPerformModule(iDiceSID)
        if clsPerform:
            iPoint = dMsgInfo['Point'] if 'Point' in dMsgInfo else 0
            cl_notify.SendCommonNotify(oGame, {
                iPlayerID: 1 }, iChat, {
                '$name': clsPerform.m_Name,
                '$point': str(iPoint) })


def EventCBTargetPosDropRelic(oListener, oEventCB, dInfo):
    sKey = oEventCB.m_Key
    if not dInfo:
        SendAlert('err', '%s未配置关键信息' % sKey)
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    iTarget = dTransInfo['TargetList'][0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    vPos = cl_reward.GetDropBasePos(oTarget)
    lstReward = []
    dExtInfo = {
        'Player': oListener.m_ID,
        'DropReason': DROP_REASON_NORMAL }
    dInfo = cl_formula.CalArgsFormula(oListener, dInfo, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    for iRelic, iLevel in dInfo.items():
        dReward = {
            'item': VIRTUAL_ITEM_DROP,
            'info': {
                'DropType': NWARRIOR_DROP_RELIC,
                'DropInfo': [
                    iRelic],
                'DropPos': vPos,
                'DropLevel': iLevel } }
        lstReward.append(dReward)
    
    cl_reward.RewardItem(oGame, oListener, lstReward, sKey, dExtInfo)


def EventCBGetTargetBySkillCustomData(oListener, oEventCB, sKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = []
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if sKey not in oSkill.m_Custom:
        return None
    oGame = oListener.m_Game
    for iTarget in oSkill.m_Custom[sKey]:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        dTransInfo['TargetList'].append(iTarget)
    


def EventCBGetTargeList(oListener, oEventCB):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return []
    return dTrans['TargetList']


def EventCBDisableLinkCopyAbility(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'AbilitySID' not in dMsgInfo or 'AbilityQuality' not in dMsgInfo:
        return None
    oDiceCon = oListener.m_DiceCon
    if not oDiceCon:
        return None
    oDiceCon.DisableLinkCopyAbility(dMsgInfo['AbilitySID'], dMsgInfo['AbilityQuality'])


def EventCBUseDiceShopNpcSpecialItem(oListener, oEventCB, iSpecialItemID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo:
        return None
    iShopNpcID = dMsgInfo['ShopNpc']
    oListener.m_DiceCon.UseSpecialItem(oListener, iSpecialItemID, [], dInfo = {
        'ShopNpc': iShopNpcID })


def EventCBAddCurWandConditionCount(oListener, oEventCB, iAddRatio, iUseRemainCount, dExcludePos, dExcludeSID):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Wand' not in dMsgInfo:
        return None
    oWand = oListener.m_WandCon.GetWandByID(dMsgInfo['Wand'])
    if not oWand or not (oWand.m_Enable):
        return None
    dComp = oWand.m_Comp[WAND_COMP_TYPE_CONDITION]
    iAddRatio = cl_formula.GetResultByData(oListener, iAddRatio, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    for iPos, oConditionComp in dComp.items():
        if iPos in dExcludePos or oConditionComp.m_SID in dExcludeSID or oConditionComp.CheckFinish():
            continue
        iOldConditionCount = oConditionComp.m_ConditionCount
        iFinishCount = oConditionComp.m_FinishConditionCount
        if iUseRemainCount:
            iAdd = max(0, (iFinishCount - iOldConditionCount) * iAddRatio // 100)
        else:
            iAdd = iFinishCount * iAddRatio // 100
        oConditionComp.AddConditionCount(iAdd)
    


def EventCBCareerPFAddValue(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dMsgInfo['RealAddCount'] = iAdd


def EventCBChangeTargetCareerPFBullet(oListener, oEventCB, iPerform, iValue, iAdd):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iTarget = dTransInfo['TargetList'][0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    oPerform = oTarget.GetPerform(iPerform)
    if oPerform and oPerform.m_PFType == PF_TYPE_CAREERPF:
        iValue = cl_formula.GetResultByData(oListener, iValue, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
        if iAdd:
            oPerform.AddPFBullet(iValue)
        else:
            oPerform.CostPFBullet(iValue)


def EventCBChangeWeaponAttPerformAttr(oListener, oEventCB, sAttr, iAdd, iMul):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' not in dMsgInfo:
        return None
    oWeapon = oListener.m_WieldCon.GetItemByID(dMsgInfo['ItemID'])
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    sKey = oEventCB.m_Key
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo, dEventInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo, dEventInfo)
    lstPerform = oPerformCom.GetPerformSIDByType(PF_TYPE_ATTACK)
    for iPerform in lstPerform:
        oPerform = oPerformCom.GetPerform(iPerform)
        if sAttr not in oPerform.m_Attr:
            continue
        oLifeCycle.m_PerformApply[(oPerform.m_Item, iPerform, sAttr)] = 1
        oPerform.AttrChange(sAttr, sKey, iMul, iAdd)
    


def EventCBGetArgDataInCache(oListener, oEventCB, sKey):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'ArgData' not in dEventInfo:
        return 0
    dArgData = dEventInfo['ArgData']
    if sKey not in dArgData:
        return 0
    return dArgData[sKey]


def EventCBAddTargetStateStatistics(oListener, oEventCB, iStateSID, sKey, iAdd, iFromSelf = 0):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAttack = oListener.m_ID if iFromSelf else 0
    oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, 0)
    if not oState:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if sKey not in oState.m_Data:
        oState.m_Data[sKey] = iAdd
    else:
        oState.m_Data[sKey] += iAdd


def EventCBIgnoreStateEff(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['IgnoreStateEff'] = 1


def EventCBAddRecycleReward(oListener, oEventCB, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Reward' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dMsgInfo['Reward'] += iAdd


def EventCBChangeRelifTimes(oListener, oEventCB, iType, iChange):
    if not oListener.m_FightType & WARRIOR_HERO:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iChange = cl_formula.GetResultByData(oListener, iChange, dEventInfo, dMsgInfo)
    sStableKey = oEventCB.GetStableKey(dEventInfo)
    oListener.ModifyRelifeCnt(iType, sStableKey, iChange)


def EventCBModifySubCDPerformColdTime(oListener, oEventCB, iTime, iExcludeEventPF, iDelayTime):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if iExcludeEventPF:
        iPerform = dMsgInfo['pfid']
        iItem = dMsgInfo['Item']
        dExcludeiPerform = {
            (iPerform, iItem): 1 }
    else:
        dExcludeiPerform = { }
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    iFrame = Time2Frame(iTime)
    iDelayFrame = Time2Frame(iDelayTime)
    cl_action.ModifySubCDPerformColdTime(oListener, iFrame, dExcludeiPerform, iDelayFrame)


def EventCBAddLionLockStateToTarget(oListener, oEventCB, iStateTime, iEnhance, dArgs):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    iStateTime = cl_formula.GetResultByData(oListener, iStateTime, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    for iTarget in lstTar:
        TargetAddLionLockState(oListener, iTarget, iStateTime, iEnhance, oEventCB.Key(), dArgs)
    


def EventCBAddBulletCost(oListener, oEventCB, iAdd):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Amount' not in dMsgInfo:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dMsgInfo['Amount'] -= iAdd


def EventCBLionLockStateSearchEnemy(oListener, oEventCB, fRadius, iUseTarget, iNum, iCheckCanSee, iCheckFly, iCheckLockStateFromSelf, dExcludeEnemy, iIgnWudi = 0):
    oGame = oListener.m_Game
    dTransInfo = oEventCB.GetCBTransInfo()
    if iUseTarget:
        if 'TargetList' not in dTransInfo:
            SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
            dTransInfo['TargetList'] = []
            return None
        lstTar = dTransInfo['TargetList']
        if not lstTar:
            return None
        oCenterTarget = oGame.GetObject(lstTar[0])
        if not oCenterTarget:
            dTransInfo['TargetList'] = []
            return None
    oCenterTarget = oListener
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iNum = cl_formula.GetResultByData(oListener, iNum, dEventInfo, dMsgInfo)
    vCenterPos = oCenterTarget.GetPos()
    dTransInfo['TargetList'] = LionLockStateSearchEnemy(oListener, fRadius, vCenterPos, iNum, iCheckCanSee, iCheckFly, iCheckLockStateFromSelf, dExcludeEnemy, iIgnWudi)


def TargetAddLionLockState(oAttack, iTarget, iStateTime, iEnhance, sReason, dArgs = None, dRSInfo = None):
    if oAttack.m_SID != LION_HERO:
        return None
    oTarget = oAttack.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    iFrame = Time2Frame(iStateTime)
    if iFrame < 1:
        iFrame = 1
        SendAlert('err', '狮子添加缚影印持续时间过低 %s' % sReason)
    if iEnhance:
        iLockState = LION_MONSTER_ENHANCELOCK_STATE
        iLockPerform = LION_SMALL_ENHANCE_THROW
    else:
        iLockState = LION_MONSTER_LOCK_STATE
        iLockPerform = LION_SMALL_NOR_THROW
    oLockPerform = oAttack.GetPerform(iLockPerform)
    if not oLockPerform:
        return None
    if not dArgs:
        dArgs = { }
    dArgs['LockRadius'] = oLockPerform.CalAttr('BulletVerticalAcc')
    dStateArgs = {
        'AID': oAttack.m_ID,
        'RS': cl_object.reason.CStrReason(sReason, dData = dRSInfo),
        'arg': dArgs if dArgs else { } }
    oState = cl_state.AddState(oTarget, iLockState, STATE_TIME_LIMIT, iFrame, dStateArgs)
    if oState:
        oState.Enable(oTarget)


def LionLockStateSearchEnemy(oAttack, fRadius, vCenterPos, iNum = 1, iCheckCanSee = 0, iCheckFly = 0, iCheckLockStateFromSelf = 0, dExcludeEnemy = None, iIgnWudi = 0):
    if oAttack.m_SID != LION_HERO:
        return []
    oGame = oAttack.m_Game
    lstArgs = [
        vCenterPos,
        fRadius]
    lstVLST = cl_math.GetAttackTargetList(oGame, oAttack.m_Scene, ATT_SHAPE_SPHERE, lstArgs, {
        'Mask': PXMASK_MONSTER,
        'BlockMask': 0 })
    dTargetPriority = { }
    iAttack = oAttack.m_ID
    vAttackPos = oAttack.GetPos()
    vAttackFacing = oAttack.GetFacing()
    if not dExcludeEnemy:
        dExcludeEnemy = { }
    for iTarget in lstVLST:
        if iTarget in dExcludeEnemy:
            continue
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if iIgnWudi and oTarget.IsWudi():
            continue
        vTargetPos = oTarget.GetPos()
        lstCurTargetPriority = [
            0,
            1,
            1,
            1,
            fRadius]
        lstMarkHero = oTarget.Query('WeakLock', [])
        if oAttack.m_ID in lstMarkHero:
            lstCurTargetPriority[0] = 1
        if iCheckFly and not oTarget.m_State.GetItemBySID(LION_MONSTER_FLY_STATE) and not oTarget.m_State.GetItemBySID(LION_MONSTER_FALL_STATE):
            lstCurTargetPriority[1] = 0
        if iCheckLockStateFromSelf and not oTarget.m_State.GetStateBySource(LION_MONSTER_LOCK_STATE, iAttack, 0) and not oTarget.m_State.GetStateBySource(LION_MONSTER_ENHANCELOCK_STATE, iAttack, 0):
            lstCurTargetPriority[2] = 0
        if iCheckCanSee:
            vDir = cl_math.Vec3Minus(vTargetPos, vAttackPos)
            if not cl_math.CheckVector2Angle(vDir, vAttackFacing, 60):
                lstCurTargetPriority[3] = 0
        lstCurTargetPriority[4] = cl_math.CalDistance(vCenterPos, vTargetPos)
        dTargetPriority[iTarget] = lstCurTargetPriority
    
    lstSorted = sorted(dTargetPriority.keys(), key = (lambda key: dTargetPriority[key]))
    return lstSorted[:iNum]


def EventCBAddTargetParasiticState(oListener, oEventCB, iCount):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGardenerCon = GetGardenerCon(oListener)
    if not oGardenerCon:
        return None
    sReason = oEventCB.m_Key
    for iTarget in dTransInfo['TargetList']:
        oGardenerCon.AddParasiticState(iTarget, sReason, iCount)
    


def EventCBCauseParasiticDam(oListener, oEventCB, iParasiticCount, iMul):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    oGardenerCon = GetGardenerCon(oListener)
    if not oGardenerCon:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iParasiticCount = cl_formula.GetResultByData(oListener, iParasiticCount, None, dMsgInfo)
    for iTarget in dTransInfo['TargetList']:
        oGardenerCon.CauseParasiticDam(iTarget, iMul, iParasiticCount, { })
    


def GetGardenerCon(oListener):
    if oListener.m_SID == GARDENER_HERO:
        return oListener.m_GardenerCon
    if oListener.m_FightType & WARRIOR_PLANT == WARRIOR_PLANT:
        oOwner = oListener.GetOwner()
        if oOwner:
            return oOwner.m_GardenerCon


def EventCBSetTargetStateArgVal(oListener, oEventCB, iStateSID, sKey, iValue, iFromSelf):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
    oGame = oListener.m_Game
    for iTarget in dTransInfo['TargetList']:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        oStateCon = oTarget.m_State
        oState = oStateCon.GetItemBySource(iStateSID, oListener.m_ID) if iFromSelf else oStateCon.GetItemBySID(iStateSID)
        if not oState:
            continue
        oState.SetArgValue(sKey, iValue)
    


def EventCBClearWeaponPFAttrChange(oListener, oEventCB, sAttr):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ItemID' in dMsgInfo:
        iWeapon = dMsgInfo['ItemID']
    elif 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iWeapon = oSkill.m_Cache['ItemID'] if 'ItemID' in oSkill.m_Cache else 0
    else:
        iWeapon = 0
    if not iWeapon:
        return None
    oWeapon = oListener.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oPerform = oWeapon.GetPFBulletPerform()
    if not oPerform or sAttr not in oPerform.m_Attr:
        return None
    sKey = oEventCB.m_Key
    oPerform.AttrClear(sAttr, sKey)


def EventCBCopySkillCustom(oListener, oEventCB, dExcludeKey):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    if not oSkill:
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    sTransKey = 'CustomPerformData'
    dTransData = dTransInfo.setdefault(sTransKey, { })
    for sKey, iValue in oSkill.m_Custom.items():
        if sKey in dExcludeKey:
            continue
        dTransData[sKey] = iValue
    


def EventCBAddWeaponPFBulletChangeNum(oListener, oEventCB, iAdd):
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    dMsgInfo['BulletNum'] += iAdd


def EventCBChangeTargetModel(oListener, oEventCB, iScale = 100):
    
    def ClearFunc(oListener, oLifeCycle):
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            return None
        oTarget.SetAttr('Scale', 100, BASEATTR_REFRESH | BASEATTR_CLIENT)
        oTargetModel = oTarget.m_ModelData
        if not oTargetModel:
            return None
        ChangeTargetModelDataWithScale(oTarget, oTargetModel, 1)
        oTarget.ClearSkillCheckArgs()

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iTarget = dTransInfo['TargetList'][0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not iScale or not oTarget or not (oTarget.m_ModelData):
        return None
    oTargetModel = oTarget.m_ModelData
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iScale = cl_formula.GetResultByData(oListener, iScale, dEventInfo, dMsgInfo)
    oTarget.SetAttr('Scale', iScale, BASEATTR_REFRESH | BASEATTR_CLIENT)
    fScale = iScale / 100
    tSkillCheckArgs = (oTarget.SkillCheckArgs[0] * fScale, oTarget.SkillCheckArgs[1] * fScale)
    ChangeTargetModelDataWithScale(oTarget, oTargetModel, fScale)
    oTarget.SetSkillCheckArgs(tSkillCheckArgs[0], tSkillCheckArgs[1])
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddUniqueDisableFunc('ClearSummonModelChange', ClearFunc, iCover = 1)


def ChangeTargetModelDataWithScale(oTarget, oTargetModel, fScale):
    if oTarget.m_FightType == WARRIOR_MECH and fScale > 3:
        fScale = 3
    iModelShape = oTargetModel.m_ModelShape
    if iModelShape in (MODEL_TYPE_SPHERE, MODEL_TYPE_CAPSULE, MODEL_TYPE_BOX):
        dParam = {
            'Shape': oTargetModel.m_ModelShape,
            'Angle': oTargetModel.m_ModelAngle,
            'Center': oTargetModel.m_ModelCenter,
            'Scale': (fScale, fScale, fScale),
            'Size': oTargetModel.m_ModelSize }
    elif iModelShape == MODEL_TYPE_SCALECTRLAGENT:
        dParam = {
            'ObjShape': oTarget.m_Shape,
            'Shape': iModelShape,
            'Scale': fScale }
    else:
        SendAlert('err', 'ChangeTargetModelDataWithScale 暂未支持该模型,请联系程序支持')
        return None
    oTarget.m_ModelData = cl_modeldata.GetModel(dParam)
    oTarget.m_ModelRadius = oTarget.m_ModelData.GetModelRadius()
    oTarget.m_ModelHeight = oTarget.m_ModelData.GetModelHeight()
    if oTarget.m_PhyModel:
        (iPaType, iNavType, iLayer, dParam) = oTarget.GetModelAttr()
        oTarget.m_PhyModel.E_Unstall()
        oTarget.m_PhyModel = cl_engphyobj.CreatePhyModel(oTarget, iPaType, iLayer, dParam)


def EventCBRemoveFromTargetList(oListener, oEventCB, iRemoveTarget):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTarget = dTrans['TargetList']
    iRemoveTarget = cl_formula.GetResultByData(oListener, iRemoveTarget, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    if iRemoveTarget in lstTarget:
        lstTarget.remove(iRemoveTarget)


def EventGetTargetByPlants(oListener, oEventCB):
    if oListener.m_SID != GARDENER_HERO:
        return None
    lstPlant = list(oListener.m_GardenerCon.m_PlantDict.keys())
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstPlant


def EventCBAddDicePacketGood(oListener, oEventCB, iSellOut, dPackageGoods):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo:
        return None
    iNpcID = dMsgInfo['ShopNpc']
    oNpc = oListener.m_Game.GetObject(iNpcID)
    if not oNpc or oNpc.m_FightType != NWARRIOR_NPC_DICESHOP:
        return None
    oNpc.AddDicePacketGood(oListener, iSellOut, dPackageGoods)


def EventCBNonaSearchEnemy(oListener, oEventCB, fRadius, fHalfHeight, iAngle, iLimit):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oListener.m_Game
    oAttack = oGame.GetObject(dMsgInfo['AID'])
    CurVID = dMsgInfo['CurVID']
    if not oAttack:
        return None
    vPos = _GetHitPos(oListener, oEventCB)
    if not vPos:
        return None
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        vStart = oSkill.m_Base['vStart']
    else:
        vStart = oListener.GetPos()
    vDir = cl_math.Vec3Minus((vPos[0], 0, vPos[2]), (vStart[0], 0, vStart[2]))
    dTransInfo = oEventCB.GetCBTransInfo()
    iLimit = cl_formula.GetResultByData(oListener, iLimit, oEventCB.GetCBEventInfo(), oEventCB.GetCBMsgInfo())
    TargetList = _GetNonaSearchEnemy(oAttack, CurVID, vPos, vDir, fRadius, fHalfHeight, iAngle, iLimit)
    dTransInfo['TargetList'] = TargetList


def EventCBGetTargetHitPos(oListener, oEventCB):
    return _GetHitPos(oListener, oEventCB)


def _GetNonaSearchEnemy(oAttack, CurVID, vPos, vDir, fRadius, fHalfHeight, iAngle, iLimit):
    if oAttack.m_SID != NONA_HERO:
        return []
    oGame = oAttack.m_Game
    lstArgs = [
        vPos,
        vDir,
        fRadius,
        fHalfHeight,
        iAngle]
    lstTarget = cl_math.GetAttackTargetList(oGame, oAttack.m_Scene, ATT_SHAPE_SECTOR, lstArgs, {
        'Mask': PXMASK_MONSTER,
        'BlockMask': 1 })
    dTargetPriority = { }
    vAttackPos = oAttack.GetPos()
    for iTarget in lstTarget:
        if iTarget == CurVID:
            continue
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        if oTarget.IsPetrochemical():
            continue
        lstCurTargetPriority = [
            0,
            0,
            0]
        lstCurTargetPriority[0] = 1 if oTarget.IsWudi() else 0
        lstCurTargetPriority[1] = oTarget.m_HP
        vTargetPos = oTarget.GetPos()
        lstCurTargetPriority[2] = cl_math.CalDistance(vAttackPos, vTargetPos)
        dTargetPriority[iTarget] = lstCurTargetPriority
    
    lstSorted = sorted(dTargetPriority.keys(), key = (lambda key: dTargetPriority[key]))
    return lstSorted[:iLimit]


def _GetHitPos(oListener, oEventCB):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iTarget = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iTarget = oSkill.m_Base['VID']
        if not iTarget and 'CurVID' in oSkill.m_Update:
            iTarget = oSkill.m_Update['CurVID']
        elif 'CurVID' in dMsgInfo:
            iTarget = dMsgInfo['CurVID']
        elif 'VID' in dMsgInfo:
            iTarget = dMsgInfo['VID']
    if not None:
        return None
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    return oTarget.GetCenter()


def EventGetAllSummonAsTarget(oListener, oEventCB):
    lstTarget = []
    iServant = oListener.GetOwnObjectID(OBJECT_SERVANT)
    if iServant:
        lstTarget.append(iServant)
    if oListener.m_PetCon:
        iPet = oListener.GetOwnObjectID(OBJECT_CURPET)
        if iPet:
            lstTarget.append(iPet)
    if oListener.m_SID == GARDENER_HERO:
        lstPlant = list(oListener.m_GardenerCon.m_PlantDict.keys())
        lstTarget.extend(lstPlant)
    if oListener.m_HeroSidePetCon:
        lstTarget.extend(list(oListener.m_HeroSidePetCon.m_HeroSidePet.keys()))
    dTransInfo = oEventCB.GetCBTransInfo()
    dTransInfo['TargetList'] = lstTarget


def EventChangeTargetAttr(oListener, oEventCB, sAttr, iAdd, iMul, iCalByTarget = 0):
    
    def ClearChangeAttr(oListener, oLifeCycle):
        obj = oListener.m_Game.GetObject(iTarget)
        if obj and not (obj.m_ReleaseFlag):
            obj.AttrClear(sAttr, sKey)

    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    dData = {
        'LifeCycle': oLifeCycle }
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    obj = oListener.m_Game.GetObject(iTarget)
    if not obj:
        return None
    oCalTarget = obj if iCalByTarget else oListener
    if iMul:
        iMul = cl_formula.GetResultByData(oCalTarget, iMul, dData)
    if iAdd:
        iAdd = cl_formula.GetResultByData(oCalTarget, iAdd, dData)
    sKey = oLifeCycle.Key()
    if iMul or iAdd or obj.HasAttr(sAttr):
        obj.AttrChange(sAttr, iMul, iAdd, sKey)
        sUniqueKey = 'ChangeTargetAttr-%s-%s' % (sAttr, iTarget)
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearChangeAttr, iCover = 0)
    else:
        obj.AttrClear(sAttr, sKey)


def EventCBCreateSummon(oListener, oEventCB, iSummonSID, iLifeTime, vPos, iAddSrcPerform, iClearRemove = 1):
    
    def ClearFunc(oWarrior, oLifeCycle):
        dSummon = oWarrior.Query(sKey, { })
        if not dSummon:
            return None
        oGame = oWarrior.m_Game
        for iSummon in dSummon:
            oSummon = oGame.GetObject(iSummon)
            if not oSummon:
                continue
            oSummon.Remove(sKey)
        

    oGame = oListener.m_Game
    dEventInfo = oEventCB.GetCBEventInfo()
    dAddInfo = {
        'Side': oListener.m_Side,
        'Origin': vPos,
        'Owner': oListener.m_ID }
    if iAddSrcPerform:
        if 'StateInfo' in dEventInfo and 'pfid' in dEventInfo['StateInfo']:
            dAddInfo['SrcPerform'] = dEventInfo['StateInfo']['pfid']
        elif 'pfid' in dEventInfo:
            dAddInfo['SrcPerform'] = dEventInfo['pfid']
        else:
            SendAlert('err', '%s无来源技能' % oEventCB.m_Key)
            return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oSummon = oGame.m_ResMgr.CreateSummon(oListener.m_Scene, iSummonSID, dAddInfo)
    if not oSummon:
        return None
    iLifeTime = cl_formula.GetResultByData(oListener, iLifeTime, dEventInfo, dMsgInfo)
    if iLifeTime:
        oSummon.SetLifeFrame(Time2Frame(iLifeTime))
    if iClearRemove:
        sKey = 'EventCreateSummon-%s' % oEventCB.m_Key
        dSummon = oListener.SetDefault(sKey, { })
        dSummon[oSummon.m_ID] = 1
        sUniqueKey = 'EventCreateSummon-%s' % iSummonSID
        oLifeCycle.AddUniqueDisableFunc(sUniqueKey, ClearFunc, iCover = 0)


def EventCBSetCrystalPacketInfo(oListener, oEventCB, dPackageInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo:
        return None
    iNpcID = dMsgInfo['ShopNpc']
    oNpc = oListener.m_Game.GetObject(iNpcID)
    if not oNpc or oNpc.m_FightType != NWARRIOR_NPC_S7SHOP:
        return None
    oNpc.SetCrystalPacketPlayerInfo(oListener, dPackageInfo)


def EventCBS7RandomAddExtraPoint(oListener, oEventCB, sKey, iRandNum, iAddPoint, iSave):
    
    def ClearFunc(oWarrior, oLifeCycle):
        if not oListener.m_OnGame:
            return None
        if oListener.m_Game.m_WarMgr.IsAIHero(oListener.m_ID):
            return None
        oBackpackCon = oWarrior.m_BackpackCon
        if not oBackpackCon:
            return None
        oBackpackCon.ClearExtraPoint(sKey)

    oBackpackCon = oListener.m_BackpackCon
    if not oBackpackCon:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    if iSave:
        dS7ExtraPoint = oListener.SetDefaultSavedData('S7ExtraPoint', { })
        if sKey in dS7ExtraPoint and dS7ExtraPoint[sKey]:
            oBackpackCon.AddExtraPoint(sKey, dS7ExtraPoint[sKey])
        else:
            dS7ExtraPoint[sKey] = oBackpackCon.RandomAddExtraPoint(sKey, iRandNum, iAddPoint)
    else:
        oBackpackCon.RandomAddExtraPoint(sKey, iRandNum, iAddPoint)
    oLifeCycle.AddUniqueDisableFunc(sKey, ClearFunc, iCover = 0)


def EventCBAddSkillEndTriggerGroup(oListener, oEventCB, iGroup):
    
    def SkillEndTriggerGroup(oTarget, oLifeCycle, dEventInfo, dMsgInfo, oSkill):
        if not oLifeCycle or not (oLifeCycle.m_Owner):
            return None
        oLifeCycleOwner = oLifeCycle.GetObject()
        if not oLifeCycleOwner or not (oLifeCycleOwner.m_EventCB):
            return None
        oLifeCycleOwner.m_EventCB.CBFuncAction(oTarget, iGroup, dEventInfo, dMsgInfo)

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oLifeCycle = dEventInfo['LifeCycle']
    func = Functor(SkillEndTriggerGroup, oListener, oLifeCycle, dEventInfo, dMsgInfo)
    oSkill.AddEndFunc(func)


def EventCBTargetHateTarget(oListener, oEventCB):
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return 0
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return 0
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget or not (oTarget.m_Agent):
        return 0
    oAgent = oTarget.m_Agent
    oEnemy = oAgent.GetLockEnemy()
    if not oEnemy:
        return 0
    return oEnemy.m_ID


def EventCBHateTarget(oListener, oEventCB):
    if not oListener or not (oListener.m_Agent):
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    lstTar = dTransInfo['TargetList']
    if not lstTar:
        return None
    iTarget = lstTar[0]
    oTarget = oListener.m_Game.GetObject(iTarget)
    if not oTarget:
        return None
    oAgent = oListener.m_Agent
    dHateData = oAgent.GetData('HateData', { })
    iCurFrame = oListener.m_Game.GetFrameNum()
    if iTarget not in dHateData:
        dHateData[iTarget] = {
            'Dam': { },
            'Hate': [
                0,
                iCurFrame],
            'Immutable': 0 }
    oAgent.SetLockEnemy(iTarget)
    oAgent.SetData('HateData', dHateData)


def EventCBTarget2UsePerform(oListener, oEventCB, iPerform, dData):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for sKey, lstFormula in dData.items():
        iRet = cl_formula.GetResultByData(oListener, lstFormula, dEventInfo, dMsgInfo)
        dData[sKey] = iRet
    
    lstTar = dTrans['TargetList']
    oGame = oListener.m_Game
    for iTarget in lstTar:
        oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            continue
        oPerform = oTarget.GetPerformIfNoThenNew(iPerform)
        if not oPerform:
            continue
        dPerform = {
            'Custom': dData }
        cl_war.UsePerform(oTarget, oPerform, dPerform)
    


def EventCBAddS7CrystalPoint(oListener, oEventCB, iAddPoint, iBeneMark):
    oBackpackCon = oListener.m_BackpackCon
    if not oBackpackCon:
        return None
    iCrystal = 0
    if iBeneMark:
        iCrystal = oBackpackCon.GetBeneCrystal()
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAddPoint = cl_formula.GetResultByData(oListener, iAddPoint, dEventInfo, dMsgInfo)
    oBackpackCon.AddCrystalPoint(iCrystal, iAddPoint, { }, iRandomDir = 1)


def EventCBAddS7CrystalExtPoint(oListener, oEventCB, sKey, iAddPoint, iItemID, iMaxPoint):
    oBackpackCon = oListener.m_BackpackCon
    if not oBackpackCon:
        return None
    
    def ClearFunc(oListener, oLifeCycle):
        oBackpackCon = oListener.m_BackpackCon
        oBackpackCon.ClearExtPoint(sKey, 0, 0)

    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iAddPoint = cl_formula.GetResultByData(oListener, iAddPoint, dEventInfo, dMsgInfo)
    iItemID = cl_formula.GetResultByData(oListener, iItemID, dEventInfo, dMsgInfo)
    oBackpackCon.AddCrystalExtPoint(sKey, iItemID, iAddPoint, iMaxPoint)
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycle.AddUniqueDisableFunc('AddCrystalExtPoint', ClearFunc, iCover = 0)


def EventCBReEnableS7CrystalExtPointEffect(oListener, oEventCB, sKey):
    oBackpackCon = oListener.m_BackpackCon
    if not oBackpackCon:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oCrystal = dMsgInfo['Item']
    oCrystal.ReEnableExtPointEffect(sKey, oListener)


def EventCBAddS7CrystalShopExtPoint(oListener, oEventCB, sKey, iTotalPoint, iMaxPoint):
    oBackpackCon = oListener.m_BackpackCon
    if not oBackpackCon:
        return None
    if not iTotalPoint:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dCrystal = dMsgInfo['CrystalInfo']
    SetS7CrystalExtInfo(oListener.m_Game, oListener.m_PlayerID, dCrystal, sKey, iTotalPoint, iMaxPoint)


def SetS7CrystalExtInfo(oGame, pid, dCrystal, sKey, iTotalPoint, iMaxPoint):
    dPoint = dCrystal['PI']
    dExtPoint = { }
    lstGrid2 = []
    for tPos in dPoint.keys():
        if tPos == (0, 0):
            continue
        (_, iPointMax) = clseason7.GetCrystalPointRange(dCrystal['SID'], tPos)
        if iPointMax:
            iPointMax = max(iPointMax, iMaxPoint)
        if dPoint[tPos] >= iPointMax:
            continue
        lstGrid2.append((tPos, iPointMax))
    
    for _ in range(iTotalPoint):
        if not lstGrid2 or not iTotalPoint:
            break
        (tRandomPos, iPointMax) = lstGrid2[oGame.Random(len(lstGrid2))]
        iTotalPoint -= 1
        dPoint[tRandomPos] += 1
        dExtPoint[tRandomPos] = dExtPoint.setdefault(tRandomPos, 0) + 1
        if dPoint[tRandomPos] >= iPointMax:
            lstGrid2.remove((tRandomPos, iPointMax))
    
    dCrystal['EP'] = {
        pid: {
            sKey: dExtPoint } }


def EventCBTriggerTargetStateRefresh(oListener, oEventCB, iState, dArgs, iFromSameItem = 0, iFromSelf = 0):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iAttack = oListener.m_ID if iFromSelf else 0
    dEventInfo = oEventCB.GetCBEventInfo()
    if iFromSameItem:
        iItem = dEventInfo['ItemID'] if 'ItemID' in dEventInfo else 0
    else:
        iItem = 0
    lstTar = dTrans['TargetList']
    dArgs = cl_formula.CalArgsFormula(oListener, dArgs, dEventInfo, oEventCB.GetCBMsgInfo())
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetStateBySource(iState, iAttack, iItem)
        if not oState or not (oState.m_Enable):
            return None
        if 'arg' in oState.m_StateInfo:
            dStateInfoArgs = oState.m_StateInfo['arg']
            dStateInfoArgs.update(dArgs)
        else:
            oState.m_StateInfo.update({
                'arg': dArgs })
        oState.m_LifeCycle.CallFunc('Refresh', oTarget)
    


def EventCBUpdateStateArgsDict(oListener, oEventCB, iStateSID, sArgs, iValue, iFromSelf, iFromSameItem):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iAttack = oListener.m_ID if iFromSelf else 0
    dEventInfo = oEventCB.GetCBEventInfo()
    if iFromSameItem:
        iItem = dEventInfo['ItemID'] if 'ItemID' in dEventInfo else 0
    else:
        iItem = 0
    lstTar = dTrans['TargetList']
    dMsgInfo = oEventCB.GetCBMsgInfo()
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
        if not oState:
            return None
        iValue = cl_formula.GetResultByData(oListener, iValue, dEventInfo, dMsgInfo)
        dArgs = oState.SetArgValueDefault(sArgs, { })
        dArgs[oEventCB.m_Key] = iValue
    


def EventCBRemoveStateArgsDict(oListener, oEventCB, iStateSID, sArgs, iFromSelf, iFromSameItem):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件回调未设置目标' % oEventCB.m_Key)
        return None
    iAttack = oListener.m_ID if iFromSelf else 0
    dEventInfo = oEventCB.GetCBEventInfo()
    if iFromSameItem:
        iItem = dEventInfo['ItemID'] if 'ItemID' in dEventInfo else 0
    else:
        iItem = 0
    lstTar = dTrans['TargetList']
    for iTarget in lstTar:
        oTarget = oListener.m_Game.GetObject(iTarget)
        if not oTarget:
            continue
        oState = oTarget.m_State.GetStateBySource(iStateSID, iAttack, iItem)
        if not oState:
            return None
        dArgs = oState.SetArgValueDefault(sArgs, { })
        dArgs.pop(oEventCB.m_Key, None)
    


def EventCBModifyS8ThirdItemEnergy(oListener, oEventCB, iAdd):
    oS8Con = oListener.m_S8Con
    if not oS8Con:
        return None
    oEquipThirdItem = oS8Con.GetEquipThirdItem()
    if not oEquipThirdItem:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    oEquipThirdItem.ChangeEnergy(iAdd)


def EventCBModifyS8ThirdItemAttr(oListener, oEventCB, sAttr, iMul, iAdd):
    
    def ClearFunc(oListener, oLifeCycle):
        oS8Con = oListener.m_S8Con
        if not oS8Con:
            return None
        oS8Con.ClearThirdGrooveAttr(sKey, sAttr)

    oS8Con = oListener.m_S8Con
    if not oS8Con:
        return None
    sKey = oEventCB.m_Key
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    iMul = cl_formula.GetResultByData(oListener, iMul, dEventInfo, dMsgInfo)
    iAdd = cl_formula.GetResultByData(oListener, iAdd, dEventInfo, dMsgInfo)
    if iMul or iAdd:
        oS8Con.AddThirdGrooveAttr(sKey, sAttr, iMul, iAdd)
    else:
        oS8Con.ClearThirdGrooveAttr(sKey, sAttr)
    oLifeCycle.AddUniqueDisableFunc(sKey + sAttr, ClearFunc, iCover = 0)


def EventCBTargetPosSummonSoul(oListener, oEventCB, dInfo):
    if not oListener.m_FightType & WARRIOR_HERO:
        return None
    sKey = oEventCB.m_Key
    if not dInfo:
        SendAlert('err', '%s未配置关键信息' % sKey)
        return None
    dTransInfo = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTransInfo:
        SendAlert('err', '%s事件回调未设置目标' % sKey)
        return None
    if not dTransInfo['TargetList']:
        return None
    iTarget = dTransInfo['TargetList'][0]
    oGame = oListener.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    iScene = oTarget.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    oLifeCycle = dEventInfo['LifeCycle']
    oLifeCycleOwner = oLifeCycle.GetObject()
    oItem = oLifeCycleOwner.GetMyItem()
    if not oItem:
        return None
    vDropPos = cl_reward.GetDropBasePos(oTarget)
    dInfo.update({
        'Item': oItem.m_ID })
    dExtraInfo = {
        'Abandoner': iTarget }
    lstDropData = [
        dInfo]
    oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_SUMMONSOUL, vDropPos, lstDropData, dExtraInfo, {
        'DropSource': oListener.m_PlayerID }, oListener.m_ID)


def EventCBSetTimeLimitCustomData(oListener, oEventCB, sKey, iSuffix, iVal, iTime):
    if iSuffix:
        sKey = sKey + '-%s' % oEventCB.m_Key
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dEventInfo = oEventCB.GetCBEventInfo()
    iTime = cl_formula.GetResultByData(oListener, iTime, dEventInfo, dMsgInfo)
    oGame = oListener.m_Game
    iLastFrame = oGame.GetFrameNum() + Time2Frame(iTime)
    dCustomData = oListener.SetDefault(sKey, { })
    dCustomData[iVal] = iLastFrame


def EventCBDeleteCustomData(oListener, oEventCB, sKey, iSuffix):
    if iSuffix:
        sKey = sKey + '-%s' % oEventCB.m_Key
    oListener.Delete(sKey)

