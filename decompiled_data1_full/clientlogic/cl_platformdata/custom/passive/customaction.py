# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/passive/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/passive/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import DAM_TYPE_TRUE, SCENE_EVT_SHAPE_RECTANGLE, WARRIOR_HERO, STATE_TIME_LIMIT, STATE_LUOHOU_WEAKER0, STATE_TIME_FOREVER, MONSTER_LUOHOU_WEAKER0, MONSTER_LUOHOU_PHASE1, STATE_TIME_FOREVER, PF_TYPE_CONSHOOT, NWARRIOR_DROP_EQUIP, LEVEL_TYPE_BOSS, DAM_TYPE_FIRE, DAM_TYPE_CORRISION, FIGHT_KEY_IGNOREDAMAGE
from cl_commondefines import WARRIOR_BOSSDM, FIGHT_KEY_WUDI, DAM_TYPE_NORMAL, DAM_TYPE_PERFORM, DAM_USE_ALL, DEVICE_USEPERFORM_POSTYPE_OWNER, INKMASTER_HERO, PARAM_LEVEL_MEDIUM_HIGH, MONSTERAI_TYPE_DEFAULT, MONSTERAI_TYPE_HATESEARCH, SIDE_TYPE_MONSTER
from cl_commondefines import BLOCK_BY_BARRIER, OBJ_ATTACK, OBJ_VICTIM, GAMBLER_CHOOSE_EQUITY, PF_TYPE_PETACTIVE, FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE, HERO_CHASED_STATE, SHARK_CHASE_STATE, SHARK_CHASECD_STATE, WAND_COMP_TYPE_ACTION, COPY_COMP, GARDENER_AREA, GARDENER_HERO, WARRIOR_MONSTER
from cl_commondefines import ATT_SHAPE_SPHERE, STATE_TIME_LIMIT, WARRIOR_MONSTER, ATTACKERSUBMSG_NORMAL, S7_FOGPOISON_STATE, WARRIOR_BOSS, WARRIOR_BOSSCANNON, BASEATTR_REFRESH, BASEATTR_CLIENT
from cl_commondefines import STATUS_STOP, NWARRIOR_DROP_AXE, S7_SIMULATE_MODULE_SID
from cl_newformula import GetWarriorAttr
from cl_only import SendAlert, Functor, PY_FLAG_DEAD, ShufferList, Time2Frame, PY_FLAG_SERVANTTARGET, ChooseRange
from cl_perform.cartoon.crt_raycasttimer import RaycastTimerCartoon
from cl_perform.cartoon.crt_delegatewhirling import DelegateWhirlingCartoon
from cl_item.defines import EQUIP_SNIPER, EQUIP_TYPE_FUNDAMENTALWEAPON, EQUIP_TYPE_AMULET
from cl_cscommondef.cs_itemdef import ITEM_SOURCE_TALENT
from cl_cscommondef import ITEM_SOURCE_TALENT, INSCRIPTION_TYPE_EXCLUSIVE
from cl_platformdata import GetSeasonSuitSub2Main, GetSeasonSuitCls, GetMinorSeasonSuit, GetWandCompIconColor
from cl_warmgr.seasonsuitelement import EXCLUDE_FUSESUIT
from cl_npc import net
from cl_commondefines import NPC_CB_VALUE, NPC_CB_REFRESH
from cl_object.logging import WarobjLog, WarrewardLog
from cl_resmgr.aitempparam import GetAIConfParam
from cl_evcon import CheckRandom
from cl_item.component.cominscription import GetMaxInscriptionNum
from cl_pxlayer import PXMASK_MONSTER
from cl_platformdata.custom.seasonpassive.customaction import AddFogPoisonState
from cl_container.backpackcon import BACKPACKCON_EMPTY_POS
import cl_object
import cl_state
import cl_msgcenter
import cl_math
import cl_snetwar
import cl_evact
import cl_reward
import cl_item
import cl_perform
import cl_action
import cl_war
import cl_formula
MAXDAM = 999999900
CHECK_SUITGRADE = 1
REPEAT_WAND_PURPLE_ABILITY = 1
REPEAT_WAND_GOLDEN_ABILITY = 2

def IgnorePainInjuryDataCollection(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oReason = dMsgInfo['RS']
    iDamType = oReason.Query('DamType', 0)
    if iDamType & DAM_TYPE_TRUE == DAM_TYPE_TRUE:
        return None
    oState = oWarrior.m_State.GetItemBySID(dInfo['StateSID'])
    if not oState:
        return None
    iDam = sum(dMsgInfo['PredictChange']) + dMsgInfo['ExcessChange']
    iOriginalDam = iDam * 10000 // (10000 + dInfo['DamReduce'])
    iStoreDam = iOriginalDam - iDam
    sStoryRemainKey = dInfo['StoreRemainKey']
    sStoryTotalKey = dInfo['StoreTotalKey']
    iOldStoreDam = oState.m_Data[sStoryRemainKey] if sStoryRemainKey in oState.m_Data else 0
    iFinalStoreDam = iOldStoreDam + iStoreDam
    iMaxDam = dInfo['MaxDam'] if 'MaxDam' in dInfo else MAXDAM
    oState.m_Data[sStoryRemainKey] = iFinalStoreDam if iFinalStoreDam < iMaxDam else iMaxDam
    oState.m_Data[sStoryTotalKey] = oState.m_Data[sStoryRemainKey]


def CustomAction4282(oWarrior, oLifeCycle, dInfo):
    pfobj = oLifeCycle.GetObject()
    pfobj.SetAttr('DistanceFactor', 10000, 0)


def CustomAction4297(oWarrior, oEventCB, dInfo):
    dTrans = oEventCB.GetCBTransInfo()
    if 'TargetList' not in dTrans:
        SendAlert('err', '%s事件自定义回调未设置目标' % oEventCB.m_Key)
        return None
    iTrigger = dTrans['TargetList'][0]
    oTrigger = oWarrior.m_Game.GetObject(iTrigger)
    if not oTrigger or oTrigger.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['SkillCustom'] = {
        'TriggerPid': oTrigger.m_PlayerID }


def CustomAction4305(oWarrior, oLifeCycle, dInfo):
    oGame = oWarrior.m_Game
    iStateSID = dInfo['StateSID']
    oReason = cl_object.reason.CStrReason('customaction4305')
    for iHero in oGame.m_WarMgr.GetAllHero():
        oState = cl_state.AddState(oWarrior, iStateSID, STATE_TIME_FOREVER, 0, {
            'AID': iHero,
            'RS': oReason })
        if oState:
            oState.Enable(oWarrior)
    


def CustomAction4309(oWarrior, oLifeCycle, dInfo):
    
    def SceneEnterFunc(oListener, dMsgInfo):
        iTriggerObj = dMsgInfo['VID']
        obj = oGame.GetObject(iTriggerObj)
        if obj.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        oState = cl_state.AddState(obj, dInfo['NoAttractSID'], STATE_TIME_FOREVER, 0, dStateArgs)
        if oState:
            dInScene[iTriggerObj] = oState.m_ID
            oState.Enable(obj)

    
    def SceneLeaveFunc(oListener, dMsgInfo):
        iTriggerObj = dMsgInfo['VID']
        obj = oGame.GetObject(iTriggerObj)
        if not obj:
            return None
        if obj.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        oAttack = oGame.GetObject(iAttack)
        if not oAttack:
            return None
        oState = oAttack.m_State.GetItemBySID(dInfo['UsePerformStateSID'])
        if oState:
            oAttractState = cl_state.AddState(obj, dInfo['AttractSID'], STATE_TIME_LIMIT, oState.GetRemainTime(), dStateArgs)
            if oAttractState:
                oAttractState.Enable(obj)
        iStateID = dInScene.pop(iTriggerObj, 0)
        if iStateID:
            obj.m_State.RemoveItem(iStateID)

    
    def OnBuildRemove(oGame, iScene, iSceneEvtID, oBuild, dInfo):
        for iTriggerObj in list(dInScene):
            SceneLeaveFunc(None, {
                'VID': iTriggerObj })
        
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        oScene.RemoveSceneEvent(iSceneEvtID)

    iScene = oWarrior.m_Scene
    oGame = oWarrior.m_Game
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    vCenterPos = dInfo['SceneCenter']
    vBuildPos = oWarrior.GetPos()
    vPos = cl_math.Vec3DisplaceDir(vBuildPos, cl_math.Vec3Minus(vBuildPos, vCenterPos), dInfo['Dis'])
    iShape = SCENE_EVT_SHAPE_RECTANGLE
    lstArgs = [
        (vPos[0], vPos[1] + dInfo['Size'][1] / 2, vPos[2]),
        (dInfo['Size'][0] / 2, dInfo['Size'][1] / 2, dInfo['Size'][2] / 2)]
    dInScene = { }
    iSceneEvtID = oScene.AddSceneEvent(oWarrior, SceneEnterFunc, SceneLeaveFunc, iShape, lstArgs, { })
    oReason = cl_object.reason.CStrReason('customaction4309')
    iAttack = oWarrior.m_Owner
    dStateArgs = {
        'AID': iAttack,
        'RS': oReason }
    cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_REMOVEOBJ, Functor(OnBuildRemove, oGame, iScene, iSceneEvtID), 'customaction4309')


def CustomAction4308(oWarrior, oEventCB, dInfo):
    oLifeCycle = oEventCB.GetCBLifeCycle()
    pfobj = oLifeCycle.GetObject()
    sKey = pfobj.Key()
    vOriPos = oWarrior.GetPos()
    iMonsterSID1 = dInfo['MosterSID1']
    iMonsterNum1 = dInfo['MonsterNum1']
    iMonsterSID2 = dInfo['MosterSID2']
    iMonsterNum2 = dInfo['MonsterNum2']
    iScene = oWarrior.m_Scene
    oGame = oWarrior.m_Game
    vFace = oWarrior.GetFacing()
    lstMonsterID = []
    iPriority = 100
    vFixDropPos = None
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    tLineIdx = oWarrior.m_LineIdx
    if tLineIdx:
        oLevelNode = oLevelCtrl.GetLevelNode(tLineIdx)
        lstPos = oLevelNode.GetSceneConfigPos('bossreward', 1, False)
        if lstPos:
            vFixDropPos = tuple(lstPos[0]['Pos'])
    for idx in range(iMonsterNum1 + iMonsterNum2):
        if idx < iMonsterNum1:
            iMonsterSID = iMonsterSID1
        else:
            iMonsterSID = iMonsterSID2
        oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, vOriPos, vFace, oWarrior.m_Side, oWarrior.m_Grade, dExtInfo = {
            'Owner': oWarrior.m_ID })
        if not oMonster:
            SendAlert('err', '%s create affiliate monster fail' % sKey)
            continue
        oMonster.Set('FixDropPos', vFixDropPos)
        oMonster.Set('39021_Priority', iPriority)
        iPriority -= 1
        iMonster = oMonster.m_ID
        cl_msgcenter.AddAttentionFunc(oWarrior, iMonster, cl_msgcenter.MSG_WAR_DIE, OnMonsterDie, sKey)
        oMonster.SetSkillCheckArgs(*dInfo['WeaknessCheck'])
        lstMonsterID.append(iMonster)
    
    oWarrior.Set('Luohou_Weaker', lstMonsterID[0])
    oWarrior.Set('39021_Priority', iPriority)
    oWarrior.Set('AffiliateMonster', lstMonsterID)
    oWarrior.Set('AffiliateLiveMonster', lstMonsterID[1:])
    SyncAffiliateID(oWarrior, { })
    oWarrior.AddExtPacket('SyncAffiliateID', SyncAffiliateID)


def OnMonsterDie(oListener, oSender, dInfo):
    if oSender.m_SID == MONSTER_LUOHOU_WEAKER0:
        cl_state.RemoveState(oListener, STATE_LUOHOU_WEAKER0)
    elif oSender.m_SID == MONSTER_LUOHOU_PHASE1:
        lstMonster = oListener.Query('AffiliateLiveMonster', [])
        if oSender.m_ID in lstMonster:
            lstMonster.remove(oSender.m_ID)
        oListener.Set('AffiliateLiveMonster', lstMonster)
        if len(lstMonster) == 0 and oListener.Phase() == 1:
            oListener.SetPhase(2)


def SyncAffiliateID(oWarrior, dPlayer):
    if oWarrior.IsDead():
        return None
    oGame = oWarrior.m_Game
    lstMonsterID = oWarrior.Query('AffiliateMonster')
    if not lstMonsterID:
        SendAlert('err', 'query affiliatemonster err')
        return None
    cl_snetwar.GS2CMonsterAdditionInfo(oGame, oWarrior, lstMonsterID)


def CustomAction4109(oWarrior, oLifeCycle, dInfo):
    oGame = oWarrior.m_Game
    lstMonsterID = oWarrior.Query('AffiliateMonster', [])
    for iMonster in lstMonsterID:
        oMonster = oGame.GetObject(iMonster)
        if oMonster and oMonster.m_SID == dInfo['MonsterSID']:
            oReason = cl_object.reason.CStrReason(oLifeCycle.Key())
            oMonster.HPDirectModify('HP', oWarrior.m_ID, -oMonster.HP(), oReason)
    


def CustomAction4316(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    pfid = oSkill.m_Base['pfid']
    if 'IgnoreSkill' in dInfo and pfid in dInfo['IgnoreSkill']:
        return None
    if 'LastVLST' in oSkill.m_Update:
        oGame = oWarrior.m_Game
        lstVLST = oSkill.m_Update['LastVLST']
        iTarget = 0
        tMonsterGroup = dInfo['MonsterGroup']
        lstIgnoreIdx = []
        iMaxPriority = -1
        for idx, iVictim in enumerate(lstVLST):
            if not iVictim:
                continue
            oVictim = oGame.GetObject(iVictim)
            if not oVictim:
                continue
            if oVictim.m_SID not in tMonsterGroup:
                lstIgnoreIdx.append(idx)
            iPriority = oVictim.Query('39021_Priority')
            iIgnoreDam = oVictim.QueryBitAttr('SpecialKey') & FIGHT_KEY_IGNOREDAMAGE
            if iPriority > iMaxPriority and not iIgnoreDam:
                iMaxPriority = iPriority
                iTarget = oVictim.m_ID
        
        iCurVID = oSkill.m_Update['CurVID']
        for idx, iVictim in enumerate(lstVLST):
            if iVictim != iTarget and idx not in lstIgnoreIdx:
                lstVLST[idx] = 0
        
        oSkill.m_Update['LastVLST'] = lstVLST
        if iTarget != iCurVID:
            cl_evact.EventCBHaltFlow(oWarrior, oEventCB)
            return None
    dCartoon = oSkill.GetCurCartoon()
    if not dCartoon:
        return None
    if oSkill.m_Base['PFType'] in (PF_TYPE_CONSHOOT, PF_TYPE_PETACTIVE) or issubclass(dCartoon['cls'], RaycastTimerCartoon) or issubclass(dCartoon['cls'], DelegateWhirlingCartoon):
        return None
    sKey = dInfo['Key']
    if pfid in dInfo['OnlyPerform']:
        dValid = oSkill.m_Collect.setdefault('ValidCartoon', { })
        if sKey not in dValid:
            dValid[sKey] = dCartoon['ID']
        else:
            CheckCartoonHalt(oWarrior, oEventCB, dCartoon)
    elif pfid in dInfo['OnlyObject']:
        dValid = oSkill.m_Collect.setdefault('ValidObjectCartoon', { })
        iCurVID = oSkill.m_Update['CurVID']
        sNewKey = '{0}-{1}'.format(sKey, dCartoon['ID'])
        if sNewKey not in dValid:
            dValid[sNewKey] = iCurVID
        elif dValid[sNewKey] != iCurVID:
            CheckCartoonHalt(oWarrior, oEventCB, dCartoon)
        else:
            dValid = oSkill.m_Collect.setdefault('ValidSingleCartoon', { })
            if sKey not in dValid or dCartoon['ID'] not in dValid[sKey]:
                lstCartoonID = dValid.setdefault(sKey, [])
                lstCartoonID.append(dCartoon['ID'])
            else:
                CheckCartoonHalt(oWarrior, oEventCB, dCartoon)


def CheckCartoonHalt(oWarrior, oEventCB, dCartoon):
    if 'MultipleExplodeCnt' not in dCartoon:
        cl_evact.EventCBHaltFlow(oWarrior, oEventCB)


def CustomActionUsePerform1714(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iItem = 0
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        iItem = oSkill.m_Base['Weapon']
    else:
        dEventInfo = oEventCB.GetCBEventInfo()
        iItem = dEventInfo['ItemID'] if 'ItemID' in dEventInfo else 0
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iItem)
    if not oWeapon:
        return None
    oComPerform = oWeapon.GetComponent('Perform')
    oPerform = oComPerform.GetPerform(dInfo['perform'])
    if not oPerform:
        oPerform = oComPerform.AddPerform(dInfo['perform'], 1)
        if not oPerform:
            return None
    oPerform.AddCanUseCount()
    iCurVID = 0
    if 'CurVID' in dMsgInfo:
        iCurVID = dMsgInfo['CurVID']
    elif 'VID' in dMsgInfo:
        iCurVID = dMsgInfo['VID']
    oVictim = oWarrior.m_Game.GetObject(iCurVID)
    if not oVictim:
        return None
    iCount = oVictim.m_State.GetStateCountByAttacker(dInfo['state'], oWarrior.m_ID)
    iAttRatio = (iCount // dInfo['count']) * 100 if iCount else 100
    vPos = oVictim.GetPos()
    dArgs = {
        'CurVID': iCurVID,
        'AttRatio': iAttRatio,
        'ExtraDam': 1 if 'ExtraDam' in dInfo else 0,
        'X': int(vPos[0] * 100),
        'Y': int((vPos[1] + oVictim.m_ModelHeight / 2) * 100),
        'Z': int(vPos[2] * 100) }
    cl_snetwar.GS2CNotifyStartSkill(oWarrior.m_Game, oWarrior.m_PlayerID, dInfo['perform'], oPerform.m_ID, oWeapon.m_ID, dArgs)


def CustomAction4348(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    iWeapon = oSkill.m_Base['Weapon']
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    if 'Clear' in dInfo:
        oWeapon.Set('AnnulusEnergyInfo', [])
        return None
    iVID = oSkill.m_Update['CurVID']
    lstFisrtHitHight = oSkill.m_Collect['AnnulusTriggerFisrtHitHight']
    if iVID in lstFisrtHitHight:
        return None
    lstAnnulusEnergyInfo = oWeapon.Query('AnnulusEnergyInfo', [])
    if iVID in lstAnnulusEnergyInfo:
        return None
    lstAnnulusEnergyInfo.append(iVID)
    oWeapon.Set('AnnulusEnergyInfo', lstAnnulusEnergyInfo)
    iState = dInfo['State']
    iAdd = dInfo['Add']
    oState = oWarrior.m_State.GetItemBySID(iState)
    if oState:
        oState.AddCount(oWarrior, iAdd)


def CustomAction5367(oSummon, oLifeCycle, dInfo):
    iScene = oSummon.m_Scene
    if not iScene:
        return None
    oHero = oSummon.GetOwner()
    if not oHero:
        return None
    iHeroID = oHero.m_ID
    oGame = oSummon.m_Game
    iRangeRadius = oSummon.GetCurRangeRadius()
    if not (oSummon.m_FollowTarget) or oSummon.m_FollowTarget == iHeroID or not oGame.GetObject(oSummon.m_FollowTarget, PY_FLAG_SERVANTTARGET):
        iRange = dInfo['SearchRange']
        bSearch = True
    else:
        iRange = iRangeRadius
        bSearch = False
    dMask = {
        'Mask': PXMASK_MONSTER,
        'BlockMask': 0,
        'ExcludeFlag': PY_FLAG_SERVANTTARGET }
    lstArgs = [
        oSummon.GetPos(),
        iRange]
    lstMonster = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    sKey = oLifeCycle.Key()
    i3d = 1
    vSummonPos = oSummon.GetPos()
    iRandomDeviation = dInfo['RandomDeviation']
    if bSearch:
        vHeroPos = oHero.GetPos()
        if not lstMonster and cl_math.CalDistance3D(vHeroPos, vSummonPos) > iRange:
            oSummon.WalkTo(vHeroPos, sKey)
            vSummonPos = vHeroPos
            lstMonster = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, [
                vHeroPos,
                iRangeRadius], dMask)
        if not lstMonster:
            iRandomDeviation = dInfo['FollowHeroRandomDeviation']
            oSummon.SetFollowTarget(iHeroID)
            cl_msgcenter.AddAttentionFunc(oSummon, iHeroID, cl_msgcenter.MSG_WAR_RECEIVEDAM, Functor(OnDam, sKey), sKey, ATTACKERSUBMSG_NORMAL)
        else:
            dDis = oGame.Scene_GetTargetDisMap(oSummon.m_ID, list(lstMonster), i3d)
            iFollowMonster = 0
            for iMonster in dDis:
                iFollowMonster = iMonster
            
            oSummon.SetFollowTarget(iFollowMonster)
    iAddFrame = Time2Frame(dInfo['AddTime'])
    iFogRange = iRangeRadius
    bAddPoisonState = False
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        if bSearch and cl_math.CalDistance3D(oMonster.GetPos(), vSummonPos) > iFogRange:
            continue
        FogAddPoisonState(oHero, oMonster, oLifeCycle, iAddFrame)
        bAddPoisonState = True
    
    oSummon.Set('MonsterInPoison', lstMonster)
    AddEffectAudio(bAddPoisonState, oSummon, dInfo['Behavior'], oHero.m_PlayerID)
    iIntervalTime = 100
    oSummon.UpdateFollowPos(iIntervalTime, iRandomDeviation)


def CustomAction5367_2(oSummon, oLifeCycle, dInfo):
    iScene = oSummon.m_Scene
    if not iScene:
        return None
    oHero = oSummon.GetOwner()
    if not oHero:
        return None
    oGame = oSummon.m_Game
    iBoss = oSummon.Query('PF5367Boss')
    iBehavior = dInfo['Behavior']
    oBoss = None
    if not iBoss:
        oScene = oGame.m_SceneMgr.GetScene(oSummon.m_Scene)
        lstMonster = oScene.GetObjectsByType('Monster')
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster or not (oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS):
                continue
            oBoss = oMonster
        
        oSummon.Set('PF5367Boss', iBoss)
    else:
        oBoss = oGame.GetObject(iBoss, PY_FLAG_DEAD)
    if not oBoss:
        oSummon.SetFollowTarget(oHero.m_ID)
        oSummon.UpdateFollowPos(iIntervalTime = 100, iRandomDeviation = dInfo['FollowHeroRandomDeviation'])
        AddEffectAudio(False, oSummon, iBehavior, oHero.m_PlayerID)
        return None
    vMove = (dInfo['BossX'], dInfo['BossY'], dInfo['BossZ'])
    oSummon.UpdateMovePos(vMove, iRandomDeviation = dInfo['RandomDeviation'])
    vSummonPos = oSummon.GetPos()
    iFogRange = oSummon.GetCurRangeRadius()
    if cl_math.CalDistance3D(vMove, vSummonPos) > iFogRange:
        AddEffectAudio(False, oSummon, iBehavior, oHero.m_PlayerID)
        return None
    AddEffectAudio(True, oSummon, iBehavior, oHero.m_PlayerID)
    FogAddPoisonState(oHero, oBoss, oLifeCycle, Time2Frame(dInfo['AddTime']))
    oSummon.Set('MonsterInPoison', [
        oBoss.m_ID])


def CustomAction5367_3(oSummon, oLifeCycle, dInfo):
    iScene = oSummon.m_Scene
    if not iScene:
        return None
    oHero = oSummon.GetOwner()
    if not oHero:
        return None
    oGame = oSummon.m_Game
    oBoss = oGame.GetObject(oSummon.Query('PF5367Boss'), PY_FLAG_SERVANTTARGET)
    iBehavior = dInfo['Behavior']
    if not oBoss:
        i3d = 3
        oScene = oGame.m_SceneMgr.GetScene(oSummon.m_Scene)
        lstMonster = oScene.GetObjectsByType('Monster')
        lstBoss = []
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_SERVANTTARGET)
            if not oMonster or not (oMonster.m_FightType == WARRIOR_BOSSCANNON):
                continue
            lstBoss.append(iMonster)
        
        if lstBoss:
            dDis = oGame.Scene_GetTargetDisMap(oSummon.m_ID, list(lstBoss), i3d)
            for iMonster in dDis:
                oSummon.Set('PF5367Boss', iMonster)
            
    iBoss = oSummon.Query('PF5367Boss')
    if not iBoss:
        oSummon.SetFollowTarget(oHero.m_ID)
        oSummon.UpdateFollowPos(iIntervalTime = 100, iRandomDeviation = dInfo['FollowHeroRandomDeviation'])
        AddEffectAudio(False, oSummon, iBehavior, oHero.m_PlayerID)
        return None
    oSummon.SetFollowTarget(iBoss)
    dMask = {
        'Mask': PXMASK_MONSTER,
        'BlockMask': 0,
        'ExcludeFlag': PY_FLAG_SERVANTTARGET }
    lstArgs = [
        oSummon.GetPos(),
        oSummon.GetCurRangeRadius() + dInfo['ExtraRadius']]
    lstMonster = cl_math.GetAttackTargetList(oGame, iScene, ATT_SHAPE_SPHERE, lstArgs, dMask)
    iAddFrame = Time2Frame(dInfo['AddTime'])
    bEffectAudio = False
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        FogAddPoisonState(oHero, oMonster, oLifeCycle, iAddFrame)
        bEffectAudio = True
    
    oSummon.Set('MonsterInPoison', lstMonster)
    AddEffectAudio(bEffectAudio, oSummon, iBehavior, oHero.m_PlayerID)
    oSummon.UpdateFollowPos(iIntervalTime = 100, iRandomDeviation = dInfo['RandomDeviation'])


def CustomAction5367_4(oSummon, oLifeCycle, dInfo):
    iScene = oSummon.m_Scene
    if not iScene:
        return None
    oHero = oSummon.GetOwner()
    if not oHero:
        return None
    oGame = oSummon.m_Game
    iBoss = oSummon.Query('PF5367Boss')
    oBoss = None
    iBehavior = dInfo['Behavior']
    if not iBoss:
        oScene = oGame.m_SceneMgr.GetScene(oSummon.m_Scene)
        lstMonster = oScene.GetObjectsByType('Monster')
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster or not (oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS):
                continue
            oBoss = oMonster
        
        oSummon.Set('PF5367Boss', iBoss)
    else:
        oBoss = oGame.GetObject(iBoss, PY_FLAG_DEAD)
    if not oBoss:
        oSummon.SetFollowTarget(oHero.m_ID)
        oSummon.UpdateFollowPos(iIntervalTime = 100, iRandomDeviation = dInfo['FollowHeroRandomDeviation'])
        AddEffectAudio(False, oSummon, iBehavior, oHero.m_PlayerID)
        return None
    vBossPos = oBoss.GetPos()
    vCenter = (vBossPos[0], dInfo['BossY'], vBossPos[2])
    vHeroPos = oHero.GetPos()
    iFogRange = oSummon.GetCurRangeRadius()
    vDir = (vHeroPos[0] - vCenter[0], 0, vHeroPos[2] - vCenter[2])
    iShiftAngle = oGame.Random(dInfo['Angle']) - dInfo['Angle'] // 2
    vMovePos = cl_math.Vec3DestPosDirPlane(vCenter, vDir, oBoss.m_ModelRadius, iShiftAngle)
    oSummon.UpdateMovePos(vMovePos, iIntervalTime = 100, iRandomDeviation = 0)
    vSummonPos = oSummon.GetPos()
    if cl_math.CalDistance3D(vCenter, vSummonPos) > oBoss.m_ModelRadius + iFogRange:
        AddEffectAudio(False, oSummon, iBehavior, oHero.m_PlayerID)
        return None
    AddEffectAudio(True, oSummon, iBehavior, oHero.m_PlayerID)
    FogAddPoisonState(oHero, oBoss, oLifeCycle, Time2Frame(dInfo['AddTime']))
    oSummon.Set('MonsterInPoison', [
        oBoss.m_ID])


def FogAddPoisonState(oHero, oMonster, oLifeCycle, iAddFrame):
    oState = oMonster.m_State.GetItemBySource(S7_FOGPOISON_STATE, oHero.m_ID)
    if not oState:
        oPerform = oLifeCycle.GetObject()
        iPerformSid = oPerform.m_SID
        oState = AddFogPoisonState(oHero, oMonster, iPerformSid, iAddFrame, sReason = oHero.AttReason(oPerform, 0))
        if not oState:
            return None
    oState.AddCount(oMonster, 1, iAddFrame)
    if oState.m_LifeCycle and oState.IsCountFull():
        oState.m_LifeCycle.CallFunc('Refresh', oMonster)


def OnDam(sKey, oSummon, oHero, dInfo):
    if 'CurVID' not in dInfo:
        return None
    iVID = dInfo['CurVID']
    oGame = oSummon.m_Game
    oVictim = oGame.GetObject(iVID, PY_FLAG_SERVANTTARGET)
    if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER):
        return None
    cl_msgcenter.DoneAttention(oSummon, oHero.m_ID, cl_msgcenter.MSG_WAR_RECEIVEDAM, sKey, ATTACKERSUBMSG_NORMAL)
    oSummon.SetFollowTarget(iVID)


def AddEffectAudio(bEffectAudio, oFog, iBehavior, iPlayerID):
    if bEffectAudio and not oFog.Query('PF5367_InEffectAudio'):
        oFog.Set('PF5367_InEffectAudio', 1)
        cl_snetwar.GS2CTriggerBehavior(oFog.m_Game, oFog.m_ID, iBehavior, {
            iPlayerID: 1 }, iStop = 0)
        return None
    if not bEffectAudio and oFog.Query('PF5367_InEffectAudio'):
        oFog.Set('PF5367_InEffectAudio', 0)
        cl_snetwar.GS2CTriggerBehavior(oFog.m_Game, oFog.m_ID, iBehavior, {
            iPlayerID: 1 }, iStop = 1)
        return None


def RefreshEffectAudio(oFog, oLifeCycle, dInfo):
    if not oFog.Query('PF5367_InEffectAudio'):
        return None
    oHero = oFog.GetOwner()
    if not oHero:
        return None
    cl_snetwar.GS2CTriggerBehavior(oFog.m_Game, oFog.m_ID, dInfo['Behavior'], {
        oHero.m_PlayerID: 1 }, iStop = 0)


def CustomAction6018(oWarrior, oEventCB, dArgs):
    oGame = oWarrior.m_Game
    dValid = oWarrior.Query('Illus')['Weapon']
    lstAllWeapon = []
    for iweapon in dValid:
        oWeapon = cl_item.GetItemCls(iweapon)
        if oWeapon.m_Type == EQUIP_SNIPER:
            lstAllWeapon.append(iweapon)
    
    iWeapon = oGame.m_RandomMgr.ChooseKey('weapon%d' % oWarrior.m_ID, {
        'Select': lstAllWeapon })
    if not iWeapon:
        return None
    iGrade = cl_reward.GetWeaponRewardGrade(oGame)
    iNewInscriptionNum = 0
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
        oWarData = oGame.m_WarData
        iLayer = oLevelCtrl.m_LayerNum + 1
        iGrade = oWarData.GetWeaponGrade(iLayer, 1, oGame)
        iNewInscriptionNum = oWarData.GetInscriptionNum(iLayer, 1, oLevelCtrl)
    oWeapon = cl_item.CreateEquip(oGame, iWeapon, iGrade, oOwner = oGame.GetObject(oWarrior.m_ID), iSource = ITEM_SOURCE_TALENT)
    dMsgInfo = { }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEDROPWEAPON, oWarrior, dMsgInfo)
    if 'Enhance' in dMsgInfo:
        oWeapon.AddEnhance(dMsgInfo['Enhance'], dMsgInfo['Reason'])
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if oInscriptionCom and iNewInscriptionNum:
        oInscriptionCom.m_InscriptionNum = iNewInscriptionNum
        oInscriptionCom.AddInscription()
    oResMgr = oGame.GetResMgr()
    dFlyInfo = {
        'Abandoner': oWarrior.m_ID }
    lstDropData = [
        oWeapon]
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPWEAPON, oWarrior, {
        'lstWeapon': lstDropData })
    oResMgr.CreateDrop(oWarrior.m_Scene, NWARRIOR_DROP_EQUIP, oWarrior.GetPos(), lstDropData, dFlyInfo, {
        'DropSource': oWarrior.m_PlayerID }, oWarrior.m_ID)


def CustomAction6087(oWarrior, oEventCB, dInfo):
    oGame = oWarrior.m_Game
    dValid = oWarrior.Query('Illus')['Weapon']
    lstAllWeapon = []
    for iWeapon in dValid:
        oWeapon = cl_item.GetItemCls(iWeapon)
        if dInfo['ElementTag'] in oWeapon.m_ClassifyTag and oWeapon.m_ElementType != DAM_TYPE_FIRE:
            continue
        if oWeapon.m_Type == EQUIP_TYPE_FUNDAMENTALWEAPON:
            continue
        lstAllWeapon.append(iWeapon)
    
    iWeapon = oGame.m_RandomMgr.ChooseKey('weapon%d' % oWarrior.m_ID, {
        'Select': lstAllWeapon })
    if not iWeapon:
        return None
    iGrade = cl_reward.GetWeaponRewardGrade(oGame)
    iNewInscriptionNum = 0
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
        oWarData = oGame.m_WarData
        iLayer = oLevelCtrl.m_LayerNum + 1
        iGrade = oWarData.GetWeaponGrade(iLayer, 1, oGame)
        iNewInscriptionNum = oWarData.GetInscriptionNum(iLayer, 1, oLevelCtrl)
    oWeapon = cl_item.CreateEquip(oGame, iWeapon, iGrade, oOwner = oGame.GetObject(oWarrior.m_ID), iSource = ITEM_SOURCE_TALENT)
    dMsgInfo = { }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEDROPWEAPON, oWarrior, dMsgInfo)
    if 'Enhance' in dMsgInfo:
        oWeapon.AddEnhance(dMsgInfo['Enhance'], dMsgInfo['Reason'])
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if iNewInscriptionNum:
        oInscriptionCom.m_InscriptionNum = iNewInscriptionNum
    if oWeapon.m_ElementType != DAM_TYPE_FIRE:
        for iSID in oInscriptionCom.m_Inscription[:]:
            clsPerform = cl_perform.GetPerformModule(iSID)
            if clsPerform.m_InscriptionType == INSCRIPTION_TYPE_EXCLUSIVE:
                continue
            oInscriptionCom.RemoveInscription(iSID)
        
        oInscriptionCom.AppendInscription(dInfo['FireInscription'])
    if oInscriptionCom.m_InscriptionNum > len(oInscriptionCom.m_Inscription):
        oInscriptionCom.AddInscription()
    oResMgr = oGame.GetResMgr()
    dFlyInfo = {
        'Abandoner': oWarrior.m_ID }
    lstDropData = [
        oWeapon]
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPWEAPON, oWarrior, {
        'lstWeapon': lstDropData })
    iPlayerID = oWarrior.m_PlayerID
    WarrewardLog.Debug('%d %d heropf reward %s %s %s' % (oGame.m_ID, iPlayerID, oEventCB.GetStableKey(oEventCB.GetCBEventInfo()), oWeapon.m_SID, oInscriptionCom.m_Inscription[:]))
    oResMgr.CreateDrop(oWarrior.m_Scene, NWARRIOR_DROP_EQUIP, oWarrior.GetPos(), lstDropData, dFlyInfo, {
        'DropSource': iPlayerID }, oWarrior.m_ID)


def CustomAction4331(oWarrior, oEventCB, dInfo):
    oGame = oWarrior.m_Game
    iServant = oWarrior.m_Servant
    oServant = oGame.GetObject(iServant)
    if not oServant:
        return None
    oMoveSpeedAttr = oWarrior.m_PrivateAttr['MoveSpeed']
    (iTotalMul, iTotalAdd) = (0, 0)
    for iMul, iAdd in oMoveSpeedAttr.m_FactorInfo.values():
        if iMul > 0:
            iTotalMul += iMul
        if iAdd > 0:
            iTotalAdd += iAdd
    
    sKey = oEventCB.Key()
    oServant.AttrChange('MoveSpeed', iTotalMul, iTotalAdd, sKey)


def CustomAction4089(oWarrior, oLifeCycle, dInfo):
    if oWarrior.m_FightType != WARRIOR_BOSSDM:
        return None
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI)
    oGame = oWarrior.m_Game
    lstMonster = oWarrior.Query('CannonList', [])
    for iMonster in lstMonster:
        oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            continue
        cl_action.CommonAddSpecialKey(oMonster, oLifeCycle, FIGHT_KEY_WUDI)
    


def CustomAction6017(oWarrior, oLifeCycle, dInfo):
    cbFun = Functor(SendReward, dInfo)
    oWarrior.AddMapLoadOKCbFun('heropf6017', cbFun, iOnce = 1)


def SendReward(dInfo, oWarrior, dMsgInfo):
    iRandomRewardFlag = oWarrior.QuerySavedData('RandomRewardFlag', 0)
    if iRandomRewardFlag:
        if iRandomRewardFlag == dInfo['Oncepf']:
            return 1
        oPerform = oWarrior.m_Perform.GetPerform(iRandomRewardFlag)
        if not oPerform:
            oWarrior.AddPerform(iRandomRewardFlag, 1)
            oWarrior.m_State.Load(oWarrior.Query('STA', { }))
        return 1
    lstDefensepf = list(dInfo['Defensepf'].keys())
    lstWeaponpf = list(dInfo['Weaponpf'].keys())
    lstSkillpf = list(dInfo['Skillpf'].keys())
    oGame = oWarrior.m_Game
    dPFInfo = {
        'Defensepf': (ShufferList(oGame, lstDefensepf), 0),
        'Weaponpf': (ShufferList(oGame, lstWeaponpf), 0),
        'Skillpf': (ShufferList(oGame, lstSkillpf), 0) }
    lstRewardpf = oWarrior.QuerySavedData('lstRewardpf', [])
    if lstRewardpf:
        WarobjLog.Debug('%d %d customaction6017 sendreward answer %s' % (oWarrior.m_Game.m_ID, oWarrior.m_PlayerID, lstRewardpf))
        net.GS2CRandomRewardpf(oWarrior, lstRewardpf)
        for skey, (lstTypepf, _) in dPFInfo.items():
            if lstTypepf[0] in lstRewardpf:
                iRandom = oGame.Random(len(lstTypepf) - 1) + 1
                lstTypepf[0] = lstTypepf[iRandom]
                lstTypepf[iRandom] = lstTypepf[0]
            dPFInfo[skey] = (lstTypepf, 0)
        
        net.SetNpcUICallBackFunction(oWarrior, NPC_CB_VALUE, Choose)
        net.SetNpcUICallBackFunction(oWarrior, NPC_CB_REFRESH, Functor(Refresh, dPFInfo))
    else:
        Refresh(dPFInfo, oWarrior)
    return 0


def Choose(oWarrior, iAnswer):
    WarobjLog.Debug('%d %d Choose answer %s' % (oWarrior.m_Game.m_ID, oWarrior.m_PlayerID, iAnswer))
    if oWarrior.QuerySavedData('RandomRewardFlag', 0):
        return None
    oWarrior.SetSavedData('RandomRewardFlag', iAnswer)
    if iAnswer not in oWarrior.QuerySavedData('lstRewardpf', []):
        oWarrior.DoNextMapLoadOKCbFun()
        return None
    oWarrior.AddPerform(iAnswer, 1)
    oWarrior.DoNextMapLoadOKCbFun()


def Refresh(dPFInfo, oWarrior):
    WarobjLog.Debug('%d %d customaction6017 refresh answer %s' % (oWarrior.m_Game.m_ID, oWarrior.m_PlayerID, dPFInfo))
    lstRewardpf = []
    oGame = oWarrior.m_Game
    for skey, (lstTypepf, iIndex) in dPFInfo.items():
        iLen = len(lstTypepf)
        iChoosepf = lstTypepf[iIndex]
        lstRewardpf.append(iChoosepf)
        iIndex += 1
        if iIndex >= iLen:
            iIndex = 0
            lstTypepf = ShufferList(oGame, lstTypepf)
            if lstTypepf[0] == iChoosepf:
                iRandom = oGame.Random(iLen - 1) + 1
                lstTypepf[0] = lstTypepf[iRandom]
                lstTypepf[iRandom] = lstTypepf[0]
        dPFInfo[skey] = (lstTypepf, iIndex)
    
    oWarrior.SetSavedData('lstRewardpf', lstRewardpf)
    net.GS2CRandomRewardpf(oWarrior, lstRewardpf)
    net.SetNpcUICallBackFunction(oWarrior, NPC_CB_VALUE, Choose)
    net.SetNpcUICallBackFunction(oWarrior, NPC_CB_REFRESH, Functor(Refresh, dPFInfo))


def CustomAction6952(oWarrior, oEventCB, dInfo):
    if 'Perform' not in dInfo:
        return None
    if not oWarrior.m_FightType & WARRIOR_HERO:
        return None
    if not oWarrior.m_Agent:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'ShopNpc' not in dMsgInfo:
        return None
    iShopNpc = dMsgInfo['ShopNpc']
    dShopRecover = oWarrior.Query('ShopRecover', { })
    if iShopNpc not in dShopRecover:
        dShopRecover[iShopNpc] = 1
        oWarrior.Set('ShopRecover', dShopRecover)
        iPerform = dInfo['Perform']
        oPerform = oWarrior.GetPerformIfNoThenNew(iPerform)
        if not oPerform:
            return None
        cl_war.UsePerform(oWarrior, oPerform, { })
        oWarrior.RemovePerform(iPerform)


def CustomAction7006(oWarrior, oEventCB, dInfo):
    iPerform = dInfo['PF']
    oPerform = oWarrior.m_Perform.GetPerform(iPerform)
    if not oPerform:
        return None
    oGame = oWarrior.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' in dMsgInfo and 'CurHitPos' in dMsgInfo:
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
    vEndPos = oVictim.GetPos()
    oPerform.AddCanUseCount()
    dArgs = {
        'SX': int(vCurPos[0] * 100),
        'SY': int(vCurPos[1] * 100),
        'SZ': int(vCurPos[2] * 100),
        'EX': int(vEndPos[0] * 100),
        'EY': int((vEndPos[1] + oVictim.m_ModelHeight / 2) * 100),
        'EZ': int(vEndPos[2] * 100) }
    cl_snetwar.GS2CNotifyStartSkill(oGame, oWarrior.m_PlayerID, iPerform, oPerform.m_ID, 0, dArgs)


def CustomAction4380(oWarrior, oEventCB, dInfo):
    iWeakerID = oWarrior.Query('Luohou_Weaker', 0)
    if not iWeakerID:
        return None
    oGame = oWarrior.m_Game
    oMonster = oGame.GetObject(iWeakerID, PY_FLAG_DEAD)
    if oMonster:
        oLifeCycle = oEventCB.GetCBLifeCycle()
        oReason = cl_object.reason.CStrReason(oLifeCycle.Key())
        oMonster.HPDirectModify('HP', oWarrior.m_ID, -oMonster.HP(), oReason)


def CustomAction4234(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    sReason = dMsgInfo['RS'] if 'RS' in dMsgInfo else ''
    WarobjLog.Debug('%d demonking beexecuted %d %s' % (oWarrior.m_Game.m_ID, oWarrior.m_Phase, sReason))


def CustomAction50100(oWarrior, oEventCB, dInfo):
    oDevice = oWarrior.GetDevice()
    if not oDevice:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, dInfo['CDTime'])
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
    oTarget = oWarrior.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return None
    dReason = {
        'ShowTips': 1,
        'DamType': DAM_TYPE_PERFORM | DAM_TYPE_NORMAL | DAM_USE_ALL,
        'ExInfo': 0 }
    if 'Skill' in dMsgInfo:
        dReason['FromActNum'] = dMsgInfo['Skill'].m_Base['ActNum']
    dEventInfo = oEventCB.GetCBEventInfo()
    oReason = dEventInfo['RS'].ExtInfo(dReason)
    iDamage = cl_formula.GetResultByData(oDevice, dInfo['Dam'], dEventInfo, dMsgInfo)
    iDeviceID = oDevice.m_ID
    dDamage = {
        'AID': iDeviceID,
        'CurVID': iTarget,
        'MainDam': [
            (iDamage, oReason)],
        'FlowDam': [],
        'RS': oReason,
        'DamFactor': {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } } }
    oTarget.ReceiveDamage(iDeviceID, dDamage, iSendMsg = 1)


def CustomAction50101(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dCustom = oSkill.m_Custom
    dCustom['PosType'] = DEVICE_USEPERFORM_POSTYPE_OWNER
    dCustom['PF50101'] = 1
    dCustom['vEnd'] = oWarrior.GetPos()


def CustomAction50220(oWarrior, oEventCB, dInfo):
    oDevice = oWarrior.GetDevice()
    if not oDevice:
        return None
    oDevice.m_Phase = dInfo['Phase']
    oDevice.GS2CPropChange('Phase', oDevice.m_Phase)


def CustomAction50102(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oPassiveObj = oEventCB.GetObject()
    if 'AddToxicNumInfo' not in oPassiveObj.m_ArgData:
        oPassiveObj.m_ArgData['AddToxicNumInfo'] = { }
    dNumInfo = oPassiveObj.m_ArgData['AddToxicNumInfo']
    iVID = dMsgInfo['VID']
    iAddCount = dMsgInfo['AddCount']
    if iVID not in dNumInfo:
        dNumInfo[iVID] = iAddCount
    else:
        dNumInfo[iVID] += iAddCount
    iTriggerNum = dInfo['TriggerNum']
    if dNumInfo[iVID] < iTriggerNum:
        return None
    iRepeat = dNumInfo[iVID] // iTriggerNum
    dNumInfo[iVID] = dNumInfo[iVID] % iTriggerNum
    for _ in range(iRepeat):
        oEventCB.CBFuncAction(oWarrior, 1, oEventCB.GetCBEventInfo(), dMsgInfo)
    


def ClearAddToxicNumInfo(oWarrior, oEventCB, dInfo):
    oPassiveObj = oEventCB.GetObject()
    oPassiveObj.m_ArgData['AddToxicNumInfo'] = { }


def CustomAction50110(oWarrior, oEventCB, dInfo):
    pfobj = oWarrior.GetPerform(dInfo['Perform'])
    if not pfobj:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iVID = dMsgInfo['VID']
    oVictim = oWarrior.m_Game.GetObject(iVID)
    if not oVictim:
        return None
    dInfo['vEnd'] = dMsgInfo['CurHitPos']
    dPerform = {
        'Custom': dInfo }
    cl_war.UsePerform(oWarrior, pfobj, dPerform)


def CustomAction50255(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oOwner = oWarrior.GetOwner()
    dInfo['Skill'] = dMsgInfo['Skill']
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BARRIER_BLOCK, oOwner, dInfo, iSub = BLOCK_BY_BARRIER)


def CustomAction5301(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo or oWarrior.m_SID != INKMASTER_HERO:
        return None
    oSkill = dMsgInfo['Skill']
    if not oSkill:
        return None
    fHalfLength = oSkill.m_Collect['InkAreaCheckLength'] / 2
    fHalfHeight = oSkill.m_Collect['InkAreaCheckHeight'] / 2
    vHorizontalDir = oSkill.m_Collect['HorizontalDir']
    vHighestPoint = oSkill.m_Collect['HighestPoint']
    vCenter = cl_math.Vec3DisplaceDir(oWarrior.GetPos(), vHorizontalDir, fHalfLength)
    if fHalfHeight > dInfo['HalfY']:
        vCenter = (vCenter[0], vHighestPoint[1] - fHalfHeight, vCenter[2])
        dInfo['HalfY'] = fHalfHeight
    oLifeCycle = oEventCB.GetCBLifeCycle()
    dInfo['HalfX'] = cl_formula.GetResultByData(oWarrior, dInfo['FullX'], {
        'LifeCycle': oLifeCycle }) / 2
    dExtInfo = {
        'HalfZ': fHalfLength,
        'Pos': vCenter,
        'Dir': vHorizontalDir,
        'Key': oEventCB.Key(),
        'RSPerform': oSkill.m_Base['pfid'],
        'LifeCycle': oLifeCycle }
    dInfo.update(dExtInfo)
    oInkCon = oWarrior.m_InkCon
    oInkCon.CreateRectangleInkArea(oWarrior, dInfo)


def CustomAction7010(oWarrior, oEventCB, dInfo):
    if 'Ratio' not in dInfo or 'MinMoveSpeed' not in dInfo:
        return None
    oDevice = oWarrior.GetDevice()
    if not oDevice:
        return None
    iRatio = dInfo['Ratio']
    fMoveSpeed = oWarrior.QueryAttr('MoveSpeed')
    fNewMoveSpeed = fMoveSpeed * iRatio * 100
    fMinMoveSpeed = dInfo['MinMoveSpeed']
    if fNewMoveSpeed < fMinMoveSpeed:
        fNewMoveSpeed = fMinMoveSpeed
    oDevice.AttrForceSet('MoveSpeed', fNewMoveSpeed, oEventCB.Key())


def CustomAction50228(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    dMsgInfo['AddCount'] += dInfo['AddValues']


def CustomAction50201(oWarrior, oEventCB, dInfo):
    oDevice = oWarrior.GetDevice()
    if not oDevice:
        return None
    iPerform = dInfo['Perform']
    oPerform = oDevice.GetPerform(iPerform)
    if not oPerform:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' in dMsgInfo:
        oSkill = dMsgInfo['Skill']
        if 'DirectHitCurPos' in oSkill.m_Collect:
            vCurPos = oSkill.m_Collect['DirectHitCurPos']
        elif 'CurHitPos' in oSkill.m_Update:
            vCurPos = oSkill.m_Update['CurHitPos']
        else:
            dCartoon = oSkill.GetCurCartoon()
            vCurPos = dCartoon['CurPos']
    else:
        iCurVID = dMsgInfo['CurVID']
        oVictim = oWarrior.m_Game.GetObject(iCurVID)
        if not oVictim:
            return None
        vCurPos = oVictim.GetPos()
    dData = {
        'vEnd': vCurPos }
    cl_war.UsePerform(oDevice, oPerform, dData)


def CustomAction50708(oWarrior, oEventCB, dInfo):
    iOwner = oWarrior.m_Owner
    if not iOwner:
        return None
    oOwner = oWarrior.m_Game.GetObject(iOwner)
    if not oOwner:
        return None
    iPerform = dInfo['Perform']
    oPerform = oOwner.m_Perform.GetPerform(iPerform)
    if not oPerform:
        oPerform = oOwner.AddPerform(iPerform, 1)
    oGame = oOwner.m_Game
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'VID' in dMsgInfo and 'CurHitPos' in dMsgInfo:
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
    vEndPos = oVictim.GetPos()
    oPerform.AddCanUseCount()
    dArgs = {
        'SX': int(vCurPos[0] * 100),
        'SY': int(vCurPos[1] * 100),
        'SZ': int(vCurPos[2] * 100),
        'EX': int(vEndPos[0] * 100),
        'EY': int((vEndPos[1] + oVictim.m_ModelHeight / 2) * 100),
        'EZ': int(vEndPos[2] * 100) }
    cl_snetwar.GS2CNotifyStartSkill(oGame, oOwner.m_PlayerID, iPerform, oPerform.m_ID, 0, dArgs)


def CustomAction50713(oWarrior, oEventCB, dInfo):
    iOwner = oWarrior.m_Owner
    if not iOwner:
        return None
    oOwner = oWarrior.m_Game.GetObject(iOwner)
    if not oOwner:
        return None
    iPerform = dInfo['Perform']
    oPerform = oOwner.GetPerform(iPerform, 0)
    if not oPerform:
        return None
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oPerform.AddCanUseCount()
    iAssignQuality = oOwner.m_GamblerCon.GetCurCombQuality()
    iQualityNum = cl_formula.GetResultByData(oOwner, dInfo['QualityNum'], dEventInfo, dMsgInfo)
    iQuality = oOwner.m_GamblerCon.TryAppendQuality(iAssignQuality, GAMBLER_CHOOSE_EQUITY, True, iQualityNum)
    dArgs = {
        'CardNum': dInfo['CardNum'],
        'Quality': iQuality }
    cl_snetwar.GS2CNotifyStartSkill(oOwner.m_Game, oOwner.m_PlayerID, dInfo['Perform'], oPerform.m_ID, 0, dArgs)


def CustomAction6966(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'PF6966.Check' in dMsgInfo:
        return None
    oGame = oWarrior.m_Game
    dMsgInfo['PF6966.Check'] = 1
    sTag = dInfo['Tag']
    iDelayFrame = Time2Frame(dInfo['Time'])
    iCount = dInfo['Count']
    if sTag == 'HeroDie':
        bSameScene = True
        oHero = oGame.GetObject(dMsgInfo['VID'])
    else:
        bSameScene = False
        oHero = oGame.m_WarMgr.GetHeroByPlayer(dMsgInfo['Adder'])
    sKey = 'Cnt6966' + sTag
    lstCount = oHero.Query(sKey, [])
    iTotal = 1
    lstNew = []
    iCurFrame = oGame.GetFrameNum()
    for iFrame in lstCount:
        if iFrame < iCurFrame:
            continue
        iTotal += 1
        lstNew.append(iFrame)
    
    if iTotal >= iCount:
        oHero.Set(sKey, [])
        iRatio = dInfo['Ratio']
        if oGame.Random(100) < iRatio:
            if sTag == 'AISignal':
                oPerform = oEventCB.GetCBLifeCycle().GetObject()
                oPerform.SetArgValue('SendEmotion', 1)
            else:
                lstPerform = []
                for iHero in oGame.m_WarMgr.GetAllAIHero():
                    oAIHero = oGame.GetObject(iHero)
                    if not oAIHero:
                        continue
                    if bSameScene and oHero.m_Scene != oAIHero.m_Scene:
                        continue
                    oPerform = oAIHero.GetPerform(6966)
                    if not oPerform:
                        continue
                    if oPerform.CheckLiteCD():
                        continue
                    lstPerform.append(oPerform)
                
                if lstPerform:
                    iIndex = oGame.Random(len(lstPerform))
                    oPerform = lstPerform[iIndex]
                    oPerform.SetArgValue('SendEmotion', 1)
                else:
                    lstNew.append(iCurFrame + iDelayFrame)
                    oHero.Set(sKey, lstNew)


def CustomAction50903(oWarrior, oEventCB, dInfo):
    oPassiveObj = oEventCB.GetObject()
    if not oPassiveObj:
        return None
    oSuitElement = oWarrior.m_Game.m_WarMgr.GetSeasonSuitElement()
    if not oSuitElement:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SeasonSuit' not in dMsgInfo:
        return None
    iEventSuit = dMsgInfo['SeasonSuit']
    dSeasonSuitSub2Main = GetSeasonSuitSub2Main()
    if iEventSuit in dSeasonSuitSub2Main:
        iTargetSuit = dSeasonSuitSub2Main[iEventSuit]
    else:
        iTargetSuit = iEventSuit
    dArgs = oPassiveObj.SetArgValueDefault('ActiveSuit', { })
    if iTargetSuit not in dArgs:
        dArgs[iTargetSuit] = 1
        cl_action.CommonAddModeTimes(oWarrior, oEventCB.GetCBLifeCycle(), FUNCMODE_TYPE_S4CARDPACKSUITCHOOSE, 1)
    dMinorSuit = GetMinorSeasonSuit()
    if iEventSuit not in EXCLUDE_FUSESUIT and iEventSuit in dMinorSuit:
        clsSuit = GetSeasonSuitCls(iEventSuit)
        if not clsSuit:
            return None
        iNum = clsSuit.m_GradeInfo.get(CHECK_SUITGRADE, 0)
        if not iNum:
            return None
        dEventInfo = oEventCB.GetCBEventInfo()
        oLifeCycle = dEventInfo['LifeCycle']
        oSuitElement.SuitCondiReduce(oWarrior, clsSuit, iNum, oLifeCycle.Key())


def CustomAction6951(oWarrior, oEventCB, dInfo):
    oDieLogMgr = oWarrior.m_DieLogMgr
    if not oDieLogMgr:
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oDieLogMgr.AddDieLogData([], dMsgInfo['RS'], [], [])


def CustomAction14307(oWarrior, oEventCB, dInfo):
    oGame = oWarrior.m_Game
    iScene = oWarrior.m_Scene
    tFace = oWarrior.GetFacing()
    vPos = oWarrior.GetPos()
    tLine = oWarrior.m_LineIdx
    iGrade = oWarrior.m_AddGrade
    dAI = {
        'AIParamLv': PARAM_LEVEL_MEDIUM_HIGH,
        'AIMethod': MONSTERAI_TYPE_DEFAULT }
    dHateSearchAI = GetAIConfParam(MONSTERAI_TYPE_HATESEARCH, PARAM_LEVEL_MEDIUM_HIGH)
    dAI.update(dHateSearchAI)
    iWarriorSID = dInfo['MonsterSID']
    vFinalPos = None
    for _ in range(dInfo['TryTimes']):
        vFinalPos = oGame.Scene_RandomPointSectorInMesh(iScene, vPos, tFace, dInfo['Radius1'], dInfo['Radius2'], dInfo['Angle1'], dInfo['Angle2'])
        if vFinalPos:
            break
    
    if not vFinalPos:
        vFinalPos = vPos
    oMonster = oGame.m_ResMgr.CreateMonster(iScene, iWarriorSID, vFinalPos, tFace, SIDE_TYPE_MONSTER, iGrade, dAI, tLine, {
        'Owner': oWarrior.m_ID,
        'NoEnemyNotify': True })
    if not oMonster:
        return None
    oWarrior.m_MonsterSummon[oMonster.m_ID] = iWarriorSID
    oWarrior.m_FollowDieObjs[oMonster.m_ID] = 1
    iSuperLevel = oWarrior.SuperLevel()
    if iSuperLevel:
        (iPlusPF, iAfPF) = oWarrior.Query('MonsterSuper', (0, 0))
        oMonster.MonsterSuper(iSuperLevel, iPlusPF, iAfPF)


def CheckSharkCanChase(oShark, IsLowHPChase):
    if oShark.m_State.GetItemBySID(SHARK_CHASE_STATE):
        return False
    if IsLowHPChase and oShark.m_State.GetItemBySID(SHARK_CHASECD_STATE):
        return False
    return True


def GetCanChaseSharkNum(oShark, oHero):
    oChasedState = oHero.m_State.GetItemBySID(HERO_CHASED_STATE)
    if not oChasedState:
        if oHero.m_Game.m_WarMgr.m_Cycle >= 9:
            return oShark.Query('HighCycleCanChaseSharkNum')
        return oShark.Query('DefaultCanChaseSharkNum')
    return oChasedState.m_MaxCount - oChasedState.GetCount()


def CheckHeroCanBeChase(oShark, oHero, IsLowHPChase):
    if GetCanChaseSharkNum(oShark, oHero) <= 0:
        return False
    if IsLowHPChase:
        iTotalHP = oHero.HP() + oHero.Shield() + oHero.Armor()
        iTotalHPMax = oHero.QueryAttr('HPMax') + oHero.QueryAttr('ShieldMax') + oHero.QueryAttr('ArmorMax')
        if iTotalHP >= iTotalHPMax * oShark.Query('SharkChaseHPLimit') / 100:
            return False
    return True


def CustomAction5328(oWarrior, oEventCB, dInfo):
    bIsLowHPChase = True
    if not CheckSharkCanChase(oWarrior, bIsLowHPChase):
        return None
    oGame = oWarrior.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oWarrior.m_Scene)
    lstMonster = oScene.GetObjectsByType('Monster')
    lstHero = oScene.GetHeros()
    for iHero in lstHero:
        oHero = oGame.GetObject(iHero, PY_FLAG_DEAD)
        if not oHero:
            continue
        if not CheckHeroCanBeChase(oWarrior, oHero, bIsLowHPChase):
            continue
        dShark = { }
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster or oMonster.m_SID != oWarrior.m_SID:
                continue
            if not CheckSharkCanChase(oMonster, bIsLowHPChase):
                continue
            dShark[iMonster] = cl_math.CalDistance3D(oMonster.GetPos(), oHero.GetPos())
        
        if not dShark:
            return None
        iCanChaseSharkNum = GetCanChaseSharkNum(oWarrior, oHero)
        lstShark = sorted(dShark, key = dShark.get)
        lstShark = lstShark[:iCanChaseSharkNum]
        oChasedState = oHero.m_State.GetItemBySID(HERO_CHASED_STATE)
        if not oChasedState:
            dChasedInfo = {
                'AID': oWarrior.m_ID,
                'RS': cl_object.reason.CStrReason('CustomAction5828') }
            oChasedState = cl_state.AddState(oHero, HERO_CHASED_STATE, STATE_TIME_FOREVER, 0, dChasedInfo)
            if oChasedState:
                oChasedState.Enable(oHero)
        for iShark in lstShark:
            oShark = oGame.GetObject(iShark, PY_FLAG_DEAD)
            if not oShark:
                continue
            dSharkChaseInfo = {
                'AID': iShark,
                'RS': cl_object.reason.CStrReason('CustomAction5828'),
                'ChaseTarget': oHero.m_ID }
            oSharkChaseState = cl_state.AddState(oShark, SHARK_CHASE_STATE, STATE_TIME_FOREVER, 0, dSharkChaseInfo)
            if oSharkChaseState:
                oSharkChaseState.m_Data['ChaseTarget'] = oHero.m_ID
                oSharkChaseState.Enable(oShark)
            oChasedState.AddCount(oHero, 1)
            if 'ChaseShark' not in oChasedState.m_Data:
                oChasedState.m_Data['ChaseShark'] = { }
            oChasedState.m_Data['ChaseShark'][iShark] = 1
        
    


def CustomAction3711(oWarrior, oEventCB, dInfo):
    tKey = oWarrior.Query('PF3711_UsingKey', None)
    if tKey:
        skillMgr = oWarrior.m_Game.m_SkillMgr
        if tKey in skillMgr.m_Using:
            oOldSkill = skillMgr.m_Using[tKey]
            oOldSkill.Halt()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oSkill = dMsgInfo['Skill']
    oWarrior.Set('PF3711_UsingKey', (oWarrior.m_ID, oSkill.m_Base['ActNum']))


def CustomAction51223(oWarrior, oEventCB, dInfo):
    oLifeCycle = oEventCB.GetCBLifeCycle()
    oLifeCycleOwner = oLifeCycle.GetObject()
    oWand = oLifeCycleOwner.GetMyItem()
    if not oWand:
        return None
    dComp = oWand.m_Comp[WAND_COMP_TYPE_ACTION]
    if not dComp:
        return None
    dExtraCallTimes = { }
    dColorExtCallTimes = { }
    iActionCompNum = oWand.m_GrooveNum[WAND_COMP_TYPE_ACTION]
    sKey = oEventCB.m_Key
    iMergeSameColors = dInfo['MergeSameColors'] if 'MergeSameColors' in dInfo else 0
    dWandCompColor = GetWandCompIconColor() if iMergeSameColors else { }
    for iPos in range(iActionCompNum):
        if iPos not in dComp:
            continue
        oComp = dComp[iPos]
        iSID = oComp.m_SID
        if iSID in COPY_COMP:
            iSID = oComp.GetKeepValue('CopyTargetSID', 0)
            if not iSID:
                if dWandCompColor and oComp.m_SID in dWandCompColor:
                    iColor = dWandCompColor[oComp.m_SID]
                    dColorExtCallTimes.setdefault(iColor, 0)
                    dColorExtCallTimes[iColor] += 1
                oComp.SetShowCallTimes(0)
                oComp.SetCallTimesInfo(sKey, 0)
                continue
            continue
        if dWandCompColor and iSID in dWandCompColor:
            iColor = dWandCompColor[iSID]
            iColorExtCallTimes = dColorExtCallTimes.setdefault(iColor, 0)
            dColorExtCallTimes[iColor] += 1
        else:
            iColorExtCallTimes = 0
        iCallTimes = dExtraCallTimes.setdefault(iSID, 0)
        if iMergeSameColors == REPEAT_WAND_GOLDEN_ABILITY:
            iCallTimes = max(iCallTimes, iColorExtCallTimes)
        elif iMergeSameColors == REPEAT_WAND_PURPLE_ABILITY and iColorExtCallTimes > iCallTimes:
            iCallTimes += 1
        dExtraCallTimes[iSID] += 1
        iMaxCallTimes = dInfo['MaxCallTimes']
        iCallTimes = min(iCallTimes, iMaxCallTimes)
        oComp.SetCallTimesInfo(sKey, iCallTimes)
        oComp.SetShowCallTimes(iCallTimes)
    


def CustomAction32659(oWarrior, oEventCB, dInfo):
    oGame = oWarrior.m_Game
    dValid = oWarrior.Query('Illus')['Weapon']
    lstAllWeapon = []
    for iWeapon in dValid:
        oWeapon = cl_item.GetItemCls(iWeapon)
        if oWeapon.m_Type == EQUIP_TYPE_AMULET:
            lstAllWeapon.append(iWeapon)
    
    iWeapon = oGame.m_RandomMgr.ChooseKey('weapon%d' % oWarrior.m_ID, {
        'Select': lstAllWeapon })
    if not iWeapon:
        return None
    iGrade = cl_reward.GetWeaponRewardGrade(oGame)
    iNewInscriptionNum = 0
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    if oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
        oWarData = oGame.m_WarData
        iLayer = oLevelCtrl.m_LayerNum + 1
        iGrade = oWarData.GetWeaponGrade(iLayer, 1, oGame)
        iNewInscriptionNum = oWarData.GetInscriptionNum(iLayer, 1, oLevelCtrl)
    oWeapon = cl_item.CreateEquip(oGame, iWeapon, iGrade, oOwner = oGame.GetObject(oWarrior.m_ID), iSource = ITEM_SOURCE_TALENT)
    dMsgInfo = { }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GREATEDROPWEAPON, oWarrior, dMsgInfo)
    if 'Enhance' in dMsgInfo:
        oWeapon.AddEnhance(dMsgInfo['Enhance'], dMsgInfo['Reason'])
    oInscriptionCom = oWeapon.GetComponent('Inscription')
    if iNewInscriptionNum:
        oInscriptionCom.m_InscriptionNum = iNewInscriptionNum
    if oInscriptionCom.m_InscriptionNum < GetMaxInscriptionNum() and oInscriptionCom.ValidAddInscription(dInfo['CorrisionInscription']) and CheckRandom(oWarrior, oEventCB, 100, dInfo['Proba']):
        oInscriptionCom.m_InscriptionNum += 1
        oInscriptionCom.AppendInscription(dInfo['CorrisionInscription'])
    if oInscriptionCom.m_InscriptionNum > len(oInscriptionCom.m_Inscription):
        oInscriptionCom.AddInscription()
    oResMgr = oGame.GetResMgr()
    dFlyInfo = {
        'Abandoner': oWarrior.m_ID }
    lstDropData = [
        oWeapon]
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPWEAPON, oWarrior, {
        'lstWeapon': lstDropData })
    iPlayerID = oWarrior.m_PlayerID
    WarrewardLog.Debug('%d %d heropf reward %s %s %s' % (oGame.m_ID, iPlayerID, oEventCB.GetStableKey(oEventCB.GetCBEventInfo()), oWeapon.m_SID, oInscriptionCom.m_Inscription[:]))
    oResMgr.CreateDrop(oWarrior.m_Scene, NWARRIOR_DROP_EQUIP, oWarrior.GetPos(), lstDropData, dFlyInfo, {
        'DropSource': iPlayerID }, oWarrior.m_ID)


def CustomAction6968(oWarrior, oEventCB, dInfo):
    oAgent = oWarrior.m_Agent
    if not oAgent:
        return None
    oPerform = oWarrior.m_Perform.GetPerform(dInfo['Perform'])
    if not oPerform:
        return None
    iAddFrame = Time2Frame(oPerform.GetArgValue('PerformCD'))
    iCurFrame = oWarrior.m_Game.GetFrameNum()
    oAgent.SetData('TurnFrame', iCurFrame + iAddFrame)


def CustomActionInitChoosePF(oWarrior, oEventCB, dInfo):
    oAgent = oWarrior.m_Agent
    if not oAgent:
        return None
    oLevelCtrl = oWarrior.m_Game.m_WarMgr.GetComponent('LevelCtrl')
    dType = dInfo['OtherLayer'] if oLevelCtrl.m_LayerNum > dInfo['Layer'] else dInfo['FristLayer']
    oBenediction = oWarrior.m_BenedictionCon.GetPerform(dInfo['Benediction'])
    if oBenediction:
        dType.update(dInfo['BenedictionType'])
    oAgent.SetData('CanUsePerformType', dType)


def CustomAction6969(oWarrior, oLifeCycle, dInfo):
    if oWarrior.m_SID != GARDENER_HERO:
        return None
    oSkillMgr = oWarrior.m_Game.m_SkillMgr
    iHeroID = oWarrior.m_ID
    lstSkill = oSkillMgr.GetSkillBySID(GARDENER_AREA)
    for oHaltSkill in lstSkill:
        if oHaltSkill.m_Base['AID'] != iHeroID:
            continue
        oHaltSkill.Halt()
    
    oWarrior.m_GardenerCon.ClearOtherInfo()


def CustomAction50724_1(oWarrior, oEventCB, dInfo):
    oAgent = oWarrior.m_Agent
    if not oAgent or not (oAgent.m_SceneData) or oAgent.GetHateTarget():
        return None
    dMsgInfo = oEventCB.GetCBMsgInfo()
    oGame = oWarrior.m_Game
    if not oGame:
        return None
    if 'CurVID' not in dMsgInfo:
        return None
    iVictim = dMsgInfo['CurVID']
    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
    if not oVictim or not (oVictim.m_FightType & WARRIOR_MONSTER) or oWarrior.m_Scene != oVictim.m_Scene:
        return None
    oAgent.AddForceHateTarget(iVictim)


def CustomAction50724_2(oWarrior, oEventCB, dInfo):
    oAgent = oWarrior.m_Agent
    if not oAgent:
        return None
    oAgent.ClearForceHateTarget()


def CustomAction5317InitAttr(oWarrior, oLifeCycle, dInfo):
    iPerform = dInfo['Perform'] if 'Perform' in dInfo else 9020
    iMaxCount = dInfo['MaxCount'] if 'MaxCount' in dInfo else 10
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return None
    dInitAttr = {
        'TriggerTimes': 0,
        'CommonMaxCount': iMaxCount }
    sKey = oLifeCycle.Key()
    for sAttr, iInitValue in dInitAttr.items():
        if sAttr not in oPerform.m_Attr:
            oPerform.SetAttr(sAttr, 0, BASEATTR_REFRESH | BASEATTR_CLIENT)
            oPerform.AttrChange(sAttr, sKey, 0, iInitValue)
            continue
        oAttr = oPerform.m_Attr[sAttr]
        if oAttr.m_Flag != BASEATTR_REFRESH | BASEATTR_CLIENT:
            oAttr.m_Flag = BASEATTR_REFRESH | BASEATTR_CLIENT
        oPerform.AttrChange(sAttr, sKey, 0, iInitValue)
    


def CustomAction5317ChangeCount(oWarrior, oLifeCycle, dInfo):
    iPerform = dInfo['Perform'] if 'Perform' in dInfo else 9020
    oWeapon = oLifeCycle.GetOwnerSourceWeapon()
    if not oWeapon:
        return None
    oPerformCom = oWeapon.GetComponent('Perform')
    if not oPerformCom:
        return None
    oPerform = oPerformCom.GetPerform(iPerform)
    if not oPerform:
        return None
    if 'TriggerTimes' not in oPerform.m_Attr or 'CommonMaxCount' not in oPerform.m_Attr:
        return None
    sKey = oLifeCycle.Key()
    if 'ClearCount' in dInfo:
        oPerform.AttrChange('TriggerTimes', sKey, 0, 0)
    else:
        iCurCount = oPerform.CalAttr('TriggerTimes')
        iMaxCount = oPerform.CalAttr('CommonMaxCount')
        if iCurCount < iMaxCount:
            iCurCount += 1
            oPerform.AttrChange('TriggerTimes', sKey, 0, iCurCount)


def CustomAction4330(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    iVictim = oSkill.m_Update['CurVID']
    oVictim = oGame.GetObject(iVictim)
    if not oVictim or oVictim.IsWudi():
        return None
    dInfo = cl_formula.CalArgsFormula(oWarrior, dInfo, {
        'LifeCycle': oEventCB.GetCBLifeCycle() })
    vVictimPos = oVictim.GetPos()
    vPosStart = oAttack.GetPos()
    iScene = oSkill.m_Base['Scene']
    vDropPos = vPosStart
    if oAttack.m_MoveCtrl.m_CurStatus != STATUS_STOP and oSkill.m_Collect['MoveDir'] and not cl_math.IsZero(oSkill.m_Collect['MoveDir']):
        fDistance = cl_math.CalDistance(vPosStart, vVictimPos)
        fFlyDistance = GetWarriorAttr('MoveSpeed', oAttack) * dInfo['DistanceParam1'] * 0.01 + dInfo['DistanceParam2']
        if fDistance <= fFlyDistance and not cl_math.CheckVector2Angle(cl_math.Vec3Minus(vVictimPos, vPosStart), oSkill.m_Collect['MoveDir'], dInfo['Angle']):
            fFlyDistance = fDistance - 2
        fShiftRadius = dInfo['ShiftRadius']
        fCenterDistance = fFlyDistance - fShiftRadius
        iShiftAngle = ChooseRange(oGame, -90, 90)
        vPosCenter = cl_math.Vec3DisplaceDir(vPosStart, oSkill.m_Collect['MoveDir'], fCenterDistance)
        vPosEnd = cl_math.Vec3DestPosDir(vPosCenter, oSkill.m_Collect['MoveDir'], fShiftRadius, iShiftAngle)
        vPosEnd = oGame.Scene_NavMeshRayCast(iScene, vPosStart, vPosEnd)
        if oVictim.m_SID == dInfo['BossStoneSID'] and abs(vPosEnd[2] - vVictimPos[2]) < dInfo['AirWallLen']:
            vDropPos = vPosStart
        else:
            vDropPos = vPosEnd
    iFlyTime = CalcFlyTime(dInfo['MinFlyTime'], dInfo['MaxFlyTime'], dInfo['MinFlyDis'], dInfo['MaxFlyDis'], vVictimPos, vDropPos)
    dInfo['ExtTime'] += iFlyTime
    dInfo['Item'] = oSkill.m_Base['Weapon']
    dExtraInfo = {
        'Abandoner': iVictim }
    lstDropData = [
        dInfo]
    oGame.m_ResMgr.CreateDrop(iScene, NWARRIOR_DROP_AXE, vDropPos, lstDropData, dExtraInfo, {
        'DropSource': oAttack.m_PlayerID }, oAttack.m_ID)


def CalcFlyTime(iMinTime, iMaxTime, iMinDis, iMaxDis, vStart, vEnd):
    fDistance = cl_math.CalDistance(vStart, vEnd)
    if fDistance >= iMaxDis:
        return iMaxTime
    if fDistance <= iMinDis:
        return iMinTime
    return int(iMinTime + (iMaxTime - iMinTime) * (fDistance - iMinDis) / (iMaxDis - iMinDis))


def CustomAction51226(oWarrior, oEventCB, dInfo):
    iPerform = dInfo['PerformSID']
    oGame = oWarrior.m_Game
    if not oGame:
        return None
    oSkillMgr = oGame.m_SkillMgr
    oSkill = oSkillMgr.GetSkillBySource(iPerform, oWarrior.m_ID, iItem = 0)
    if not oSkill:
        return None
    iActNum = oSkill.m_Base['ActNum']
    cl_action.HaltCasting(oWarrior, iActNum, oEventCB.m_Key)


def GetLastModule(oWarrior, iTargetPoint):
    oGame = oWarrior.m_Game
    if not oGame:
        return None
    oBackPackCon = oWarrior.m_BackpackCon
    if not oBackPackCon:
        return None
    oTarModule = None
    iMinPoint = 999
    for iItem, _ in oBackPackCon.m_Item2Pos.items():
        if iItem not in oBackPackCon.m_Module:
            continue
        oModule = oBackPackCon.m_Module[iItem]
        if oModule.m_SID == S7_SIMULATE_MODULE_SID:
            continue
        if oModule.m_PointMax[oModule.m_Quality] != iTargetPoint:
            continue
        iPoint = oBackPackCon.GetModulePoint(iItem)
        if iPoint > iMinPoint:
            continue
        iMinPoint = iPoint
        oTarModule = oModule
    
    return oTarModule


def CustomAction51665_1(oWarrior, oEventCB, dInfo):
    
    def ClearSimulatePF(oWarrior, oLifeCycle):
        oPf = oLifeCycle.m_Owner
        oBackPackCon = oWarrior.m_BackpackCon
        if not oBackPackCon:
            return None
        dModulePf = oBackPackCon.m_Perform.get(oPf.m_Item, { })
        for iPerform in list(dModulePf):
            if iPerform == oPf.m_SID:
                continue
            oBackPackCon.DisableSimPerform(oPf.m_Item, iPerform)
        
        oModule = oBackPackCon.GetModule(oPf.m_Item)
        if oModule:
            oModule.Set('SimPos', BACKPACKCON_EMPTY_POS)

    oLifeCycle = oEventCB.GetCBEventInfo()['LifeCycle']
    oPf = oLifeCycle.m_Owner
    oBackPackCon = oWarrior.m_BackpackCon
    oModule = oBackPackCon.GetModule(oPf.m_Item)
    tOldPos = oModule.Query('SimPos', BACKPACKCON_EMPTY_POS)
    iTarModule = oBackPackCon.m_EquipMap.get(tOldPos, 0)
    oTarModule = oBackPackCon.GetItemByID(iTarModule)
    if not oTarModule:
        oTarModule = GetLastModule(oWarrior, dInfo['TarPoint'])
    if oTarModule:
        oModule.Set('SimPos', oBackPackCon.m_Item2Pos[oTarModule.m_ID])
        iPoint = oBackPackCon.GetModulePoint(oPf.m_Item)
        dAbility = oTarModule.GetAbilityByPoint(iPoint)
        for iPerform, iLv in dAbility.items():
            oBackPackCon.EnableSimPerform(oPf.m_Item, oTarModule.m_ID, iPerform, iLv)
        
    else:
        oModule.Set('SimPos', BACKPACKCON_EMPTY_POS)
    oLifeCycle.AddDisableFunc(ClearSimulatePF)


def CustomAction51665_2(oWarrior, oEventCB, dInfo):
    oLifeCycle = oEventCB.GetCBEventInfo()['LifeCycle']
    oPf = oLifeCycle.m_Owner
    if oEventCB.GetCBMsgInfo()['S7Item'] == oPf.m_Item:
        return None
    oBackPackCon = oWarrior.m_BackpackCon
    if not oBackPackCon:
        return None
    oModule = oBackPackCon.GetModule(oPf.m_Item)
    if not oModule or not oBackPackCon.IsEquip(oPf.m_Item):
        return None
    oTarModule = GetLastModule(oWarrior, dInfo['TarPoint'])
    tOldPos = oModule.Query('SimPos', BACKPACKCON_EMPTY_POS)
    tNewPos = oBackPackCon.GetPos(oTarModule.m_ID) if oTarModule else BACKPACKCON_EMPTY_POS
    if tOldPos == tNewPos and oBackPackCon.m_SimulateInfo[1] == (oTarModule.m_ID if oTarModule else 0):
        return None
    oModule.Set('SimPos', tNewPos)
    if tOldPos != BACKPACKCON_EMPTY_POS:
        dModulePf = oBackPackCon.m_Perform.get(oPf.m_Item, { })
        for iPerform in list(dModulePf):
            if iPerform == oPf.m_SID:
                continue
            oBackPackCon.DisableSimPerform(oPf.m_Item, iPerform)
        
    if tNewPos != BACKPACKCON_EMPTY_POS:
        iPoint = oBackPackCon.GetModulePoint(oPf.m_Item)
        dAbility = oTarModule.GetAbilityByPoint(iPoint)
        for iPerform, iLv in dAbility.items():
            oBackPackCon.EnableSimPerform(oPf.m_Item, oTarModule.m_ID, iPerform, iLv)
        


def CustomAction51679(oWarrior, oEventCB, dData):
    oBulletContainer = oWarrior.m_BulletCon
    iTempBulletSId = 0
    iTempPst = 0
    iTempMaxBullet = 0
    iCostRatio = dData['CostRatio']
    iTime = dData['Time']
    iSpeedAddRatio = dData['SpeedAddRatio']
    iStateId = dData['StateId']
    tupleBullet = dData['TupleBullet']
    dEventInfo = oEventCB.GetCBEventInfo()
    dMsgInfo = oEventCB.GetCBMsgInfo()
    iCostRatio = cl_formula.GetResultByData(oWarrior, iCostRatio, dEventInfo, dMsgInfo)
    for iBulletSID in tupleBullet:
        iMaxBullet = oBulletContainer.GetMaxBullet(iBulletSID)
        iCurBullet = oBulletContainer.Bullet(iBulletSID)
        iCurPst = iCurBullet * 100 // iMaxBullet
        if iCurPst < iCostRatio:
            continue
        if iCurPst > iTempPst:
            iTempBulletSId = iBulletSID
            iTempPst = iCurPst
            iTempMaxBullet = iMaxBullet
    
    if not iTempBulletSId:
        return None
    cl_action.CommonAddBagBullet(oWarrior, oEventCB.GetCBLifeCycle(), iTempBulletSId, -iTempMaxBullet * iCostRatio // 100, 0)
    cl_evact.PassiveCBAddState(oWarrior, oEventCB, iStateId, iTime, {
        'SpeedAddRatio': iSpeedAddRatio }, 1, 0, 0)

