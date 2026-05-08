# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_reward.pyc
# RelativePath: clientlogic/cl_reward.pyc
# Source Generated with Decompyle++
# File: cl_reward.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_NPC_RAREGOLDENCUP, NWARRIOR_DROP_EXPERIENCE, MG_EXPERIENCE, NWARRIOR_DROP_DEMON, VIRTUAL_ITEM_SHOPGOODSWEIGHT, VIRTUAL_ITEM_GSCASHRELIFE, VIRTUAL_ITEM_INSCRIPTIONPROP, VIRTUAL_ITEM_GEMINI, VIRTUAL_ITEM_EXCLUSINSCRIPTION, VIRTUAL_ITEM_WEAPONUPGRADE, VIRTUAL_ITEM_HIDESHOPGOODS, VIRTUAL_ITEM_EXTGSCASHDROP, VIRTUAL_ITEM_TALENT, VIRTUAL_UNLOCK_INITWEAPONDROP, VIRTUAL_ITEM_WARCASH, VIRTUAL_ITEM_PASSIVE, VIRTUAL_ITEM_KEY, VIRTUAL_ITEM_SHOPREFRESH, VIRTUAL_ITEM_AUTOPERFORM, VIRTUAL_ITEM_ATTR, VIRTUAL_ITEM_RELIC, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, NWARRIOR_DROP_GSCASH, VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_EQUIP, STATE_NODRUG, NWARRIOR_DROP_TRIGGER, STATE_NOBULLET, NWARRIOR_DROP_CASH, MG_GOLDENCUP, STATE_NOWARCASH, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_BULLET, VIRTUAL_ITEM_DROP, WARRIOR_HERO, VIRTUAL_ITEM_GOLDENCUP, DEFAULT_DROP_RADIUS, WARRIOR_BOSS, MG_TRIGGER, MG_RELIC, MG_EQUIP, MG_AUTOPERFORM, MG_TALENT, MG_KEYITEM, NWARRIOR_DROP_RELIC, VIRTUAL_ITEM_TALENTWEIGHT, DROP_REASON_NORMAL, RELIC_SUBMSG_GENERATE_DROP, ADJUST_RELIC, NWARRIOR_DROP_RAREITEM, VIRTUAL_ITEM_RAREITEM, MG_RAREITEM, MG_TASK, VIRTUAL_ITEM_MAGICPOWER, NWARRIOR_DROP_MAGIC_POWER, VIRTUAL_ITEM_DEVICECOMP, NWARRIOR_DROP_DEVICECOMP, VIRTUAL_ITEM_PET, VIRTUAL_ITEM_WANDCARDPACK, VIRTUAL_ITEM_WAND, VIRTUAL_ITEM_WANDCOMP, WANDPUT_SHOPBUY, MG_WAND, VIRTUAL_ITEM_DICE, MG_DICESELECT, VIRTUAL_ITEM_S7CRYSTAL, VIRTUAL_ITEM_S7MODULE, VIRTUAL_ITEM_S7CRYSTALPACKET, VIRTUAL_ITEM_S8GEMITEM, VIRTUAL_ITEM_S8THIRDPERFORM
from cl_object.logging import WarrewardLog
from cl_item.defines import EQUIP_MASK_WEAPON, BULLET_GRENADER
import cl_wand
import cl_war
import cl_minigame
import cl_msgcenter
import cl_math
ONCE_MG_TYPE = (MG_GOLDENCUP, MG_KEYITEM, MG_TALENT, MG_AUTOPERFORM, MG_EXPERIENCE, MG_RAREITEM, MG_TASK)
SORTED_MG_TYPE = (MG_EQUIP, MG_RELIC, MG_TRIGGER, MG_GOLDENCUP, MG_WAND, MG_DICESELECT)
NOTRECORD_DROPLOG = (NWARRIOR_DROP_CASH, NWARRIOR_DROP_BULLET, NWARRIOR_DROP_GSCASH, NWARRIOR_DROP_EXPERIENCE, NWARRIOR_DROP_TRIGGER)

def NeedCheckGoldenCup(clsMiniGame, dExtInfo):
    iCheck = dExtInfo['CheckGoldenCup'] if 'CheckGoldenCup' in dExtInfo else 1
    if not iCheck:
        return 0
    if clsMiniGame.m_Type != MG_GOLDENCUP:
        return 0
    return 1


def ValidExtraGoldenCup(oGame, dExtInfo = None):
    dLimitInfo = oGame.m_WarData.GetGoldenCupLimit()
    if 'Limit' not in dLimitInfo:
        return 1
    if dExtInfo and 'NPC' in dExtInfo and 'LimitNPC' in dLimitInfo:
        iNPC = dExtInfo['NPC']
        if iNPC not in dLimitInfo['LimitNPC']:
            return 1
    iLimit = dLimitInfo['Limit']
    iNowCount = oGame.m_WarMgr.Query('GoldenCupLimit', 0)
    if iLimit != -1 and iNowCount < iLimit:
        return 1
    return 0


def AddExtraGoldenCup(oGame):
    iNowCount = oGame.m_WarMgr.Query('GoldenCupLimit', 0)
    iNowCount += 1
    oGame.m_WarMgr.Set('GoldenCupLimit', iNowCount)


def IsPointInOBB(dCheckDropInfo, vPos):
    vCenter = dCheckDropInfo['Pos']
    lstSize = dCheckDropInfo['Size']
    tEuler = dCheckDropInfo['Euler'] if 'Euler' in dCheckDropInfo else (0, 0, 0)
    return cl_math.PosInOBB(vCenter, (0, 0, 0), lstSize, (1, 1, 1), (int(tEuler[0]), int(tEuler[1]), int(tEuler[2])), vPos)


def GetDropBasePos(oOwner):
    if not oOwner:
        return (0, 0, 0)
    dPosCache = oOwner.SetDefault('BaseDropPos', { })
    iNowFrame = oOwner.m_Game.GetFrameNum()
    if iNowFrame in dPosCache:
        return dPosCache[iNowFrame]
    vPos = _GetDropBasePos(oOwner)
    dPosCache[iNowFrame] = vPos
    return vPos


def _GetDropBasePos(oOwner):
    vFixDropPos = oOwner.Query('FixDropPos', None)
    dCheckDropInfo = oOwner.Query('CheckDropInfo', None)
    if vFixDropPos:
        if not dCheckDropInfo:
            return vFixDropPos
        vOwner = oOwner.GetPos()
        if IsPointInOBB(dCheckDropInfo, vOwner):
            return vFixDropPos
    tLineIdx = oOwner.m_LineIdx
    oGame = oOwner.m_Game
    if oOwner.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS and tLineIdx:
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        oLevelNode = oLevelCtrl.GetLevelNode(tLineIdx)
        lstPos = oLevelNode.GetSceneConfigPos('bossreward', 1, False)
        if lstPos:
            dPosData = lstPos[0]
            vPos = dPosData['Pos']
            if 'RangeX' in dPosData:
                fOffsetX = (oGame.Random(int(dPosData['RangeX'] * 100)) / 100) * (1 if oGame.Random(2) == 0 else -1)
                fOffsetZ = (oGame.Random(int(dPosData['RangeZ'] * 100)) / 100) * (1 if oGame.Random(2) == 0 else -1)
                vPos = cl_math.Vec3Add(vPos, (fOffsetX, 0, fOffsetZ))
            return vPos
        for iHero in oGame.m_WarMgr.GetLiveHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            WarrewardLog.Alert('%d boss %d droppos err %s %s' % (oGame.m_ID, oOwner.m_SID, oOwner.GetPos(), oHero.GetPos()))
            return oHero.GetPos()
        
    return oOwner.GetPos()


def GetDropFixPos(oGame, oOwner, iScene, vPos, iAbandoner):
    if not iScene:
        return vPos
    (bRet, vFixPos) = oGame.Scene_GetSpace(iScene, vPos)
    oAbandoner = oGame.GetObject(iAbandoner)
    if bRet:
        vPos = vFixPos
        if oAbandoner:
            vFixDropPos = oAbandoner.Query('FixDropPos', None)
            dCheckDropInfo = oAbandoner.Query('CheckDropInfo', None)
            if vFixDropPos and dCheckDropInfo and IsPointInOBB(dCheckDropInfo, vPos):
                vPos = vFixDropPos
            elif oAbandoner:
                vFixDropPos = oAbandoner.Query('FixDropPos')
                if vFixDropPos:
                    vPos = vFixDropPos
                else:
                    vPos = oAbandoner.GetPos()
            else:
                vPos = oOwner.GetPos()


def GetMiniGameForEach(oGame, oOwner, oTarget, dMiniGame, iSource, dExtInfo):
    dEachMiniGame = { }
    dOnceMiniGame = { }
    for iMiniGame, dInfo in dMiniGame.items():
        if 'UseOriTimes' in dExtInfo:
            iTimes = dInfo[1]
        else:
            iTimes = cl_minigame.GetMiniGameTimes(oGame, dInfo[0], dInfo[1], oOwner, oTarget, iMiniGame, iSource)
        if not iTimes:
            continue
        clsData = oGame.m_WarData.GetMiniGameData(iMiniGame)
        if not clsData:
            continue
        if NeedCheckGoldenCup(clsData, dExtInfo):
            if ValidExtraGoldenCup(oGame, dExtInfo):
                AddExtraGoldenCup(oGame)
            
        iType = clsData.m_Type
        dData = dict(dExtInfo)
        if 'CalOffset' in dExtInfo and dExtInfo['CalOffset'] and iType in SORTED_MG_TYPE:
            dData.update({
                'Scene': oOwner.m_Scene,
                'Times': iTimes,
                'AutoReward': 0 })
        else:
            dData.update({
                'Scene': oOwner.m_Scene,
                'Times': iTimes })
        if clsData.m_Type in ONCE_MG_TYPE:
            dOnceMiniGame[iMiniGame] = dData
            continue
        if dExtInfo.get('OnlyRewardAttack', 0):
            dOnceMiniGame[iMiniGame] = dData
            continue
        dEachMiniGame[iMiniGame] = dData
    
    return (dEachMiniGame, dOnceMiniGame)


def StartMiniGame(oGame, iMiniGame, iOwner, iTarget, iSource, dData, dHeroReward, lstMiniGame, dMGInfo):
    oMiniGame = cl_minigame.NewMiniGame(oGame, iMiniGame, iOwner, iTarget, dData, iSource)
    if not oMiniGame:
        return None
    oMiniGame.Start()
    if oMiniGame.Query('AutoReward', 1):
        return None
    lstReward = dHeroReward.setdefault(iTarget, [])
    lstMGReward = oMiniGame.Query('Reward', [])
    lstReward.extend(lstMGReward)
    lstMiniGame.append(oMiniGame)
    if oMiniGame.Query('CanReward', 1):
        return None
    dHeroMGInfo = dMGInfo.setdefault(iTarget, { })
    dHeroMGInfo[oMiniGame.m_ID] = (iMiniGame, lstMGReward, oMiniGame.m_Data)


def RewardItemByMiniGame(oOwner, iTarget, dMiniGame, sKey, iSource, dExtInfo):
    if oOwner.Query(sKey):
        return None
    iRepeat = dExtInfo['RepeatReward'] if 'RepeatReward' in dExtInfo else 0
    if not iRepeat:
        oOwner.Set(sKey, 1)
    oGame = oOwner.m_Game
    oTarget = oGame.GetObject(iTarget)
    (dEachMiniGame, dOnceMiniGame) = GetMiniGameForEach(oGame, oOwner, oTarget, dMiniGame, iSource, dExtInfo)
    dHeroReward = { }
    lstMiniGame = []
    dMGInfo = { }
    for iMiniGame, dData in dOnceMiniGame.items():
        StartMiniGame(oGame, iMiniGame, oOwner.m_ID, iTarget, iSource, dData, dHeroReward, lstMiniGame, dMGInfo)
    
    lstHero = oOwner.m_Game.m_WarMgr.GetLiveHero()
    for iHero in lstHero:
        for iMiniGame, dData in dEachMiniGame.items():
            StartMiniGame(oGame, iMiniGame, oOwner.m_ID, iHero, iSource, dData, dHeroReward, lstMiniGame, dMGInfo)
        
    
    vFace = oOwner.GetFacing()
    vVertical = (-vFace[2], 0, vFace[0])
    fInterval = DEFAULT_DROP_RADIUS * 2
    vPos = GetDropBasePos(oOwner)
    for iHero, lstReward in dHeroReward.items():
        if dMGInfo:
            break
        iTotalIdx = len(lstReward)
        idx = 0
        for dReward in lstReward:
            if dReward['item'] == VIRTUAL_ITEM_GOLDENCUP:
                continue
            vDropPos = cl_math.Vec3DisplaceDir(vPos, vVertical, fInterval * (idx - (iTotalIdx - 1) / 2))
            dReward['info']['DropPos'] = vDropPos
            idx += 1
        
    
    for oMiniGame in lstMiniGame:
        if oMiniGame.Query('CanReward', 1):
            oMiniGame.SendReward()
            continue
        oMiniGame.Set('Reward', [])
        oMiniGame.End()
    
    bUrgentDrop = dExtInfo['UrgentDrop'] if 'UrgentDrop' in dExtInfo else 1
    if bUrgentDrop:
        CheckUrgentBulletSupplement(oOwner, iTarget)
    return dMGInfo


def CheckUrgentBulletSupplement(oOwner, iTarget):
    oGame = oOwner.m_Game
    oTarget = oGame.GetObject(iTarget)
    if not oTarget or oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    dUrgentData = oGame.m_WarData.GetUrgentBulletConf()
    lstCheckSID = [
        BULLET_GRENADER]
    for oWeapon in oTarget.m_WieldCon.GetAllItemByMask(EQUIP_MASK_WEAPON):
        if not oWeapon or oWeapon.IsInitWeapon():
            continue
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            continue
        lstCheckSID.append(oBulletCom.BulletType())
    
    vPos = GetDropBasePos(oOwner)
    for iBulletSID in lstCheckSID:
        if iBulletSID not in dUrgentData:
            continue
        dData = dUrgentData[iBulletSID]
        iHas = oTarget.m_BulletCon.Bullet(iBulletSID) * 100 // oTarget.m_BulletCon.GetMaxBullet(iBulletSID)
        if iHas > dData['Threshold']:
            continue
        iProb = dData['Prob'] if 'Prob' in dData else 0
        if oGame.Random(100) > iProb:
            continue
        lstDropInfo = [
            {
                iBulletSID: dData['Count'] }]
        dReward = {
            'item': VIRTUAL_ITEM_DROP,
            'info': {
                'Scene': oOwner.m_Scene,
                'DropType': NWARRIOR_DROP_BULLET,
                'DropInfo': lstDropInfo,
                'DropPos': vPos } }
        RewardItem(oGame, oTarget, [
            dReward], 'UrgentBullet', {
            'Player': iTarget })
    


def CreateDemon(oGame, iTarget, dReward, sReason = '', dStaticInfo = None):
    if not dReward:
        return None
    oTarget = oGame.GetObject(iTarget)
    if not oTarget:
        return None
    if dStaticInfo is None:
        dStaticInfo = { }
    oResMgr = oGame.GetResMgr()
    vDropPos = GetDropBasePos(oTarget)
    WarrewardLog.Debug('%d createdemon reward %s %s' % (oGame.m_ID, list(dReward), vDropPos))
    for iHero, dInfo in dReward.items():
        for iMiniGame, lstInfo in dInfo.items():
            (iSID, lstReward, dExtInfo) = lstInfo
            lstCopyReward = lstReward[:]
            for dReward in lstCopyReward:
                iRewardItem = dReward['item'] if 'item' in dReward else 0
                if iRewardItem == VIRTUAL_ITEM_GOLDENCUP:
                    lstReward.remove(dReward)
                    RewardItem(oGame, oTarget, [
                        dReward], 'MiniGame%s-%s' % (iSID, iMiniGame), dExtInfo)
            
        
        dMsgInfo = {
            'Reward': dInfo,
            'Reason': sReason }
        oHero = oGame.GetObject(iHero)
        if oHero:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFORECREATEDEMON, oHero, dMsgInfo)
        dInfo = dMsgInfo['Reward']
        for _, lstReward, _ in dInfo.values():
            if lstReward:
                oResMgr.CreateDrop(oTarget.m_Scene, NWARRIOR_DROP_DEMON, vDropPos, [
                    dInfo], { }, dStaticInfo = dStaticInfo, iOwner = iHero)
                break
        
    


def LogReward(oGame, iScene, sLog):
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    iLevelNode = 0
    if oScene:
        iLevelNode = oScene.m_Level
    WarrewardLog.Debug('%d %d %s' % (oGame.m_ID, iLevelNode, sLog))


def GetWeaponRewardGrade(oGame):
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if oLevelCtrl:
        iGrade = oLevelCtrl.GetWeaponRewardGrade()
    else:
        iGrade = 1
    return iGrade


def RewardItemDrop(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    lstDropData = dInfo['DropInfo']
    iDropType = dInfo['DropType']
    if iDropType == NWARRIOR_DROP_EQUIP:
        lstDropLog = [ oEquip.m_SID for oEquip in lstDropData ]
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPWEAPON, tobj, {
            'lstWeapon': lstDropData })
    elif iDropType == NWARRIOR_DROP_RAREITEM:
        lstDropLog = [ oRareItem.m_SID for oRareItem in lstDropData ]
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPRAREITEM, tobj, {
            'lstRareItem': lstDropData })
    else:
        lstDropLog = lstDropData
    iHero = dExtInfo['Player']
    if 'Scene' in dExtInfo and dExtInfo['Scene']:
        iScene = dExtInfo['Scene']
    elif 'Scene' in dInfo and dInfo['Scene']:
        iScene = dInfo['Scene']
    else:
        iScene = tobj.m_Scene
    oHero = oGame.GetObject(iHero)
    iPlayer = oHero.m_PlayerID if oHero else iHero
    if oHero:
        if not iDropType == NWARRIOR_DROP_CASH or oHero.m_State.GetItemBySID(STATE_NOWARCASH):
            if (iDropType == NWARRIOR_DROP_BULLET or oHero.m_State.GetItemBySID(STATE_NOBULLET) or iDropType == NWARRIOR_DROP_TRIGGER) and oHero.m_State.GetItemBySID(STATE_NODRUG):
                LogReward(oGame, iScene, '%d nodrop %d %s %s' % (iPlayer, iDropType, lstDropLog, sReason))
                return None
    if iDropType not in NOTRECORD_DROPLOG:
        LogReward(oGame, iScene, '%d drop %d %s %s' % (iPlayer, iDropType, lstDropLog, sReason))
    oResMgr = oGame.GetResMgr()
    vPos = dInfo['DropPos'] if 'DropPos' in dInfo else tobj.GetPos()
    iDropReason = dExtInfo['DropReason'] if 'DropReason' in dExtInfo else 0
    iAbandoner = dExtInfo['Abandoner'] if 'Abandoner' in dExtInfo else 0
    if iDropType != NWARRIOR_NPC_GOLDENCUP and iDropReason == DROP_REASON_NORMAL:
        vPos = GetDropFixPos(oGame, tobj, iScene, vPos, iAbandoner)
    iDropOwner = dExtInfo['DropOwner'] if 'DropOwner' in dExtInfo else iHero
    dShare = { }
    if iDropType == NWARRIOR_DROP_RELIC:
        dMsgInfo = {
            'Relic': dReward['info']['DropInfo'][0],
            'StaticInfo': {
                'Share': 1 },
            'Level': dInfo['DropLevel'] if 'DropLevel' in dInfo else 1 }
        if 'NPC' in dExtInfo:
            dMsgInfo['NPC'] = dExtInfo['NPC']
        if 'DropReason' in dExtInfo:
            dMsgInfo['DropReason'] = dExtInfo['DropReason']
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC_BEFORE, oHero, dMsgInfo, iSub = RELIC_SUBMSG_GENERATE_DROP)
        dShare = dMsgInfo['StaticInfo']
        if 'ShowedBeforDrop' not in dInfo:
            if 'RelicDropLevel' in dMsgInfo:
                dReward['info']['DropLevel'] = dMsgInfo['RelicDropLevel']
            if 'ReplaceRelicInfo' in dMsgInfo:
                (iReplaceRelic, iReplaceLevel) = dMsgInfo['ReplaceRelicInfo'][0]
                dReward['info']['DropInfo'][0] = iReplaceRelic
                if 'RelicUseOldLevel' in dMsgInfo and not dMsgInfo['RelicUseOldLevel']:
                    dReward['info']['DropLevel'] = iReplaceLevel
        iRelic = dReward['info']['DropInfo'][0]
        iTrueRelic = oGame.m_WarData.GetTruePassive(ADJUST_RELIC, iRelic)
        if iTrueRelic != iRelic:
            WarrewardLog.Alert('%d %d relic %d!=%d reason %s' % (oGame.m_ID, iPlayer, iRelic, iTrueRelic, sReason))
            if not iTrueRelic:
                return None
            dReward['info']['DropInfo'][0] = iTrueRelic
        elif iDropType == NWARRIOR_DROP_TRIGGER:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPTRIGGER, tobj, {
                'Player': tobj.m_PlayerID,
                'TriggerItem': lstDropData,
                'DropType': iDropType })
        elif iDropType == NWARRIOR_DROP_DEVICECOMP:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_DEVICECOMP, tobj, {
                'DropInfo': lstDropData })
    iLevel = dInfo['DropLevel'] if dInfo['DropLevel'] in dInfo else 1
    dStaticInfo = {
        'DropLevel': iLevel,
        'DropSource': iPlayer }
    if 'ExtStaticInfo' in dExtInfo:
        dStaticInfo.update(dExtInfo['ExtStaticInfo'])
    if iDropType == NWARRIOR_DROP_RELIC:
        dStaticInfo.update(dShare)
    dExtraInfo = {
        'Abandoner': iAbandoner,
        'DropReason': iDropReason }
    if 'ExtraInfo' in dExtInfo:
        dExtraInfo.update(dExtInfo['ExtraInfo'])
    oResMgr.CreateDrop(iScene, iDropType, vPos, lstDropData, dExtraInfo, dStaticInfo, iDropOwner, iSplit = 1)


def RewardEquip(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    oItem = dInfo['item']
    iSID = oItem.m_SID
    if 'Owner' in dInfo:
        iNpcID = dInfo['Owner']
    else:
        iNpcID = 0
    iReplacePos = dExtInfo['iReplacePos'] if dExtInfo and 'iReplacePos' in dExtInfo else 0
    LogReward(oGame, tobj.m_Scene, '%d equip %d %s' % (tobj.m_PlayerID, iSID, sReason))
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DROPWEAPON, tobj, {
        'lstWeapon': [
            oItem],
        'NpcID': iNpcID,
        'Weapon': oItem })
    lstContainer = oItem.GetTargetContainer(tobj)
    if not oItem.PutToContainer(lstContainer, sReason, iReplacePos):
        WarrewardLog.Error('reward equip fail %s' % iSID)


def RewardBullet(oGame, tobj, dReward, sReason, dExtInfo):
    dBullet = dReward['info']
    dInfo = dBullet['bullet']
    oBulletCon = tobj.m_BulletCon
    for iBulletSID, iCnt in dInfo.items():
        oBulletCon.BulletModify(iBulletSID, iCnt, sReason)
    


def RewardRelic(oGame, tobj, dReward, sReason, dExtInfo):
    dRelic = dReward['info']
    iSID = dRelic['sid']
    iLevel = dRelic['level'] if 'level' in dRelic else 1
    if dExtInfo is None:
        dExtInfo = { }
    if 'remove' in dRelic:
        dExtInfo['ValidRemove'] = dRelic['remove']
    LogReward(oGame, tobj.m_Scene, '%d relic %s %s %s' % (tobj.m_PlayerID, iSID, iLevel, sReason))
    iTrueRelic = oGame.m_WarData.GetTruePassive(ADJUST_RELIC, iSID)
    if iTrueRelic != iSID:
        WarrewardLog.Alert('%d %d relic %d!=%d reason %s' % (oGame.m_ID, tobj.m_PlayerID, iSID, iTrueRelic, sReason))
        if not iTrueRelic:
            return None
        iSID = iTrueRelic
    oRelicCon = tobj.m_RelicCon
    if 'NoSendCreateRelicMsg' not in dExtInfo:
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_RELIC, tobj, {
            'Relic': [
                iSID] })
    bExtend = dExtInfo['ExtendBag'] if 'ExtendBag' in dExtInfo else False
    bTempRelic = dExtInfo['TempRelic'] if 'TempRelic' in dExtInfo else False
    if bExtend:
        oRelicCon.AddExtendRelic(iSID, sReason, iLevel, dExtInfo, iSource = tobj.m_PlayerID)
    elif bTempRelic or 'GamePlayType' in dExtInfo:
        iGamePlayType = dExtInfo['GamePlayType']
        oRelicCon.AddTempRemoveRelic(iGamePlayType, iSID, sReason, iLevel, dExtInfo, tobj.m_PlayerID, iSendClient = 1)
    else:
        oRelicCon.AddRelic(iSID, sReason, iLevel, dExtInfo, iSource = tobj.m_PlayerID)


def RewardAttr(oGame, tobj, dReward, sReason, dExtInfo):
    dAttr = dReward['info']
    sAttr = dAttr['attr']
    oAttr = tobj.GetAttr(sAttr)
    if not oAttr:
        WarrewardLog.Error('reward no attr %s %s %s' % (tobj.Type(), sAttr, sReason))
        return None
    LogReward(oGame, tobj.m_Scene, '%d attr %s %s' % (tobj.m_PlayerID, dAttr, sReason))
    (iMul, iAdd) = oAttr.GetKeyFactorInfo(sReason)
    iMul += dAttr['mul']
    iAdd += dAttr['add']
    oAttr.AddValue(tobj, iMul, iAdd, sReason, iSave = 1)


def RewardAutoPerform(oGame, tobj, dReward, sReason, dExtInfo):
    dPerform = dReward['info']
    iPerform = dPerform['sid']
    oPerform = tobj.GetPerformIfNoThenNew(iPerform)
    dData = {
        'VID': tobj.m_ID }
    dData.update(dPerform['data'])
    cl_war.UsePerform(tobj, oPerform, dData)
    tobj.RemovePerform(iPerform)


def RewardShopRefresh(oGame, tobj, dReward, sReason, dExtInfo):
    (_, iNpc, _) = tobj.m_NpcUICallBack
    LogReward(oGame, tobj.m_Scene, '%d shoprefresh %d %s' % (tobj.m_PlayerID, iNpc, sReason))
    oNpc = oGame.GetObject(iNpc)
    oNpc.ShopRefresh(tobj)


def RewardKey(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    dKey = dInfo['key']
    LogReward(oGame, tobj.m_Scene, '%d key %s %s' % (tobj.m_PlayerID, dKey, sReason))
    tobj.AddKey(dKey, sReason)


def RewardPassive(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iPerform = dInfo['sid']
    dData = dInfo['data']
    if 'level' in dData:
        iLevel = dData['level']
    elif dExtInfo and 'SourceLevel' in dExtInfo:
        iLevel = dExtInfo['SourceLevel']
    else:
        iLevel = 1
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d rewardpassive %s level%s %s' % (tobj.m_PlayerID, iPerform, iLevel, sReason))
    tobj.AddPerform(iPerform, iLevel)


def RewardWarCash(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iAmount = dInfo['amount']
    iSendMsg = dInfo.get('sendmsg', 1)
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d rewardwarcash %s %s' % (tobj.m_PlayerID, iAmount, sReason))
    tobj.AddCash(iAmount, sReason, iSendMsg)


def RewardInitWeaponDrop(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iBulletType = dInfo['bullettype']
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d rewardinitweapondrop %s %s' % (tobj.m_PlayerID, iBulletType, sReason))
    dInitWeaponDrop = tobj.Query('InitWeaponDrop', { })
    dInitWeaponDrop[iBulletType] = 1
    tobj.Set('InitWeaponDrop', dInitWeaponDrop)


def RewardTalent(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iTalent = dInfo['sid']
    LogReward(oGame, tobj.m_Scene, '%d rewardtalent %s %s' % (tobj.m_PlayerID, iTalent, sReason))
    oTalentCon = tobj.m_TalentCon
    oTalent = oTalentCon.GetPerform(iTalent)
    if not oTalent:
        iLevel = 1
    else:
        iLevel = oTalent.Level() + 1
    if not tobj.m_TalentCon.AddTalent(iTalent, iLevel, sReason, dExtInfo):
        WarrewardLog.Error('reward talent fail %s' % iTalent)


def RewardGoldenCup(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iNpc = dInfo['sid']
    clsNpcData = oGame.GetWarData().GetNpcData(iNpc)
    if not clsNpcData or clsNpcData.m_FightType not in [
        NWARRIOR_NPC_GOLDENCUP,
        NWARRIOR_NPC_LIMITGOLDENCUP,
        NWARRIOR_NPC_RAREGOLDENCUP,
        NWARRIOR_NPC_EXCHANGEGOLDENCUP]:
        return None
    iScene = dInfo['Scene'] if 'Scene' in dInfo else tobj.m_Scene
    vPos = dInfo['DropPos'] if 'DropPos' in dInfo else tobj.GetPos()
    iLogID = 0
    if tobj and tobj.m_PlayerID:
        iLogID = tobj.m_PlayerID
    elif 'Player' in dExtInfo:
        oHero = oGame.GetObject(dExtInfo['Player'])
        iLogID = oHero.m_PlayerID if oHero else 0
    if not iLogID and tobj:
        iLogID = tobj.m_ID
    LogReward(oGame, iScene, '%d rewardgoldencup %s %s %s %s' % (iLogID, iNpc, iScene, vPos, sReason))
    dAddInfo = {
        'Pos': vPos,
        'VisiblePlayer': dInfo['VisiblePlayer'] if 'VisiblePlayer' in dInfo else { },
        'Abandoner': dExtInfo['Abandoner'] if 'Abandoner' in dExtInfo else 0,
        'Share': dInfo['Share'] if 'Share' in dInfo else 1,
        'SetInfo': dInfo['SetInfo'] if 'SetInfo' in dInfo else { } }
    if 'DropReason' in dExtInfo:
        dAddInfo['DropSource'] = dExtInfo['DropReason']
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    oLevelNode = oLevelCtrl.m_CurNode
    dMsgInfo = {
        'NPC': iNpc,
        'LevelNode': oLevelNode,
        'ExtInfo': dExtInfo,
        'Abandoner': dAddInfo['Abandoner'],
        'NPCInfo': dAddInfo,
        'Scene': iScene }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_LEVEL_CREATENPC_PRE, oLevelNode.m_CtrlMgr, dMsgInfo)
    if not dMsgInfo['NPC']:
        return None
    oNpc = oGame.m_ResMgr.CreateNpc(iScene, dMsgInfo['NPC'], dAddInfo)
    if oNpc and 'RecordData' in dInfo:
        oNpc.Load(dInfo['RecordData'])


def RewardExtGSCashDropRatio(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    (iType, iAdd) = dInfo['ratio']
    dAll = tobj.Query('ExtraGSCashDropRatio', { })
    iCurRatio = dAll.get(iType, 0)
    iNewRatio = iCurRatio + iAdd
    LogReward(oGame, tobj.m_Scene, '%d extgscashdropratio %s %s %s %s' % (tobj.m_PlayerID, iType, iAdd, iNewRatio, sReason))
    dAll[iType] = iNewRatio
    tobj.Set('ExtraGSCashDropRatio', dAll)


def RewardShowShopHiddenGoods(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iPos = dInfo['pos']
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d shophiddenpos %s %s' % (tobj.m_PlayerID, iPos, sReason))
    tobj.m_BuyMgr.ShowHiddenGoods(iPos)


def RewardAdditionalWeaponUpgradeTimes(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iAdd = dInfo['add']
    iCur = tobj.Query('AdditionalWeaponUpgrade', 0)
    iNew = iCur + iAdd
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d weaponupgradetimes %s %s %s' % (tobj.m_PlayerID, iAdd, iNew, sReason))
    tobj.Set('AdditionalWeaponUpgrade', iNew)


def RewardOpenExclusiveInscription(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iNew = dInfo['new']
    iOld = oGame.m_WarMgr.Query('ExclusiveInscription', 0)
    if iOld >= iNew:
        return None
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d exclusiveinscription %s' % (tobj.m_PlayerID, sReason))
    oGame.m_WarMgr.Set('ExclusiveInscription', iNew)


def RewardAdditionalGeminiInscription(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iNew = dInfo['new']
    iOld = oGame.m_WarMgr.Query('AdditionalGemini', 0)
    if iOld >= iNew:
        return None
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d addgemini %s %s %s' % (tobj.m_PlayerID, iNew - iOld, iNew, sReason))
    oGame.m_WarMgr.Set('AdditionalGemini', iNew)


def RewardAddInscriptionProp(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iType = dInfo['type']
    iNew = dInfo['new']
    dAll = oGame.m_WarMgr.Query('AdditionalInscriptionProp', { })
    iOld = dAll[iType] if iType in dAll else 0
    if iOld >= iNew:
        return None
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d inscriptionprop %s %s %s %s' % (tobj.m_PlayerID, iType, iNew - iOld, iNew, sReason))
    dAll[iType] = iNew
    oGame.m_WarMgr.Set('AdditionalInscriptionProp', dAll)


def RewardAddGSCashRelife(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iAdd = dInfo['add']
    iOld = tobj.Query('AdditionalGSCashRelife', 0)
    iNew = iOld + iAdd
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d gscashrelife %s %s %s' % (tobj.m_PlayerID, iNew - iOld, iNew, sReason))
    tobj.Set('AdditionalGSCashRelife', iNew)


def RewardAdditionalShopGoodsWeight(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iType = dInfo['type']
    iWeight = dInfo['weight']
    dWeight = tobj.Query('AddtionalGoodsWeight', { })
    if iType in dWeight:
        dWeight[iType] += iWeight
    else:
        dWeight[iType] = iWeight
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d shopgoodsextraweight %s %s %s' % (tobj.m_PlayerID, iType, iWeight, sReason))
    tobj.Set('AddtionalGoodsWeight', dWeight)


def RewardModifyTalentWeight(oGame, tobj, dReward, sReason, dExtInfo):
    dWeight = tobj.Query('ModifyTalentWeight', { })
    dInfo = dReward['info']
    iTalent = dInfo['talent']
    iModify = dInfo['modify']
    if iTalent not in dWeight:
        dWeight[iTalent] = { }
    dWeight[iTalent][sReason] = iModify
    iLogReward = dExtInfo['LogReward'] if dExtInfo and 'LogReward' in dExtInfo else 1
    if iLogReward:
        LogReward(oGame, tobj.m_Scene, '%d talent weight %s %s %s' % (tobj.m_PlayerID, iTalent, iModify, sReason))
    tobj.Set('ModifyTalentWeight', dWeight)


def RewardRareItem(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    oItem = dInfo['item']
    iSID = oItem.m_SID
    LogReward(oGame, tobj.m_Scene, '%d rareitem %d %s' % (tobj.m_PlayerID, iSID, sReason))
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REWARDRAREITEM, tobj, {
        'Item': oItem })
    lstContainer = oItem.GetTargetContainer(tobj)
    if not oItem.PutToContainer(lstContainer, sReason):
        WarrewardLog.Error('%d rareitem fail %s %s' % (tobj.m_PlayerID, iSID, sReason))


def RewardMagicPower(oGame, tobj, dReward, sReason, dExtInfo):
    oWarMgr = oGame.m_WarMgr
    oRelicTalentElement = oWarMgr.GetComponent('RelicTalentElement')
    if not oRelicTalentElement or not (oRelicTalentElement.m_Enable):
        return None
    dInfo = dReward['info']
    iOption = dInfo['Option']
    iMagicPower = dInfo['MagicPower']
    vPos = dInfo['DropPos']
    iScene = dInfo['Scene']
    LogReward(oGame, tobj.m_Scene, '%d magicpower %d %d %s' % (tobj.m_PlayerID, iOption, iMagicPower, sReason))
    dDrop = {
        'Option': iOption,
        'MagicPower': iMagicPower,
        'Notify': oRelicTalentElement.m_MagicNotify }
    if 'Group' in dInfo:
        dDrop['Group'] = dInfo['Group']
    if iOption in oRelicTalentElement.m_MagicDrop:
        dDrop['SID'] = oRelicTalentElement.m_MagicDrop[iOption]
    oResMgr = oGame.m_ResMgr
    oResMgr.CreateDrop(iScene, NWARRIOR_DROP_MAGIC_POWER, vPos, [
        dDrop], dExtInfo, { }, tobj.m_ID, iSplit = 1)


def RewardDeviceComp(oGame, tobj, dReward, sReason, dExtInfo):
    oWarMgr = oGame.m_WarMgr
    oDeviceElement = oWarMgr.GetComponent('DeviceElement')
    if not oDeviceElement or not (oDeviceElement.m_Enable):
        return None
    dInfo = dReward['info']
    iSID = dInfo['SID']
    LogReward(oGame, tobj.m_Scene, '%d devicecomp %d %s' % (tobj.m_PlayerID, iSID, sReason))
    tobj.m_DevicePerformCon.PickComponent(iSID, sReason)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GENERATE_DEVICECOMP, tobj, { })


def RewardPet(oGame, tobj, dReward, sReason, dExtInfo):
    iPet = dReward['info']['item']
    oPet = oGame.GetObject(iPet)
    if not oPet:
        return None
    iSID = oPet.m_SID
    LogReward(oGame, tobj.m_Scene, '%s pet %s-%s %s' % (tobj.m_PlayerID, oPet.m_ID, iSID, sReason))
    tobj.m_PetCon.AddPet(oPet)


def RewardWandCardPack(oGame, tobj, dReward, sReason, dExtInfo):
    oWandElement = tobj.m_Game.m_WarMgr.GetWandElement()
    if not oWandElement:
        return None
    dInfo = dReward['info']
    iLevel = dInfo['level']
    dShopWand = oWandElement.GetWandPutWithFilter(tobj.m_PlayerID, WANDPUT_SHOPBUY)
    if not dShopWand:
        return None
    lstWand = []
    iPos = 0
    for iWand in dShopWand:
        iRewardLevel = cl_wand.FixWandLevel(iWand, iLevel)
        lstWand.append((iPos, iWand, iRewardLevel))
        iPos += 1
    
    LogReward(oGame, tobj.m_Scene, '%s wandcardpack %s %s' % (tobj.m_PlayerID, lstWand, sReason))
    oWandElement.RewardWandCardPack(tobj, dInfo['Npc'], sReason, lstWand)


def RewardWand(oGame, tobj, dReward, sReason, dExtInfo):
    oWandElement = tobj.m_Game.m_WarMgr.GetWandElement()
    if not oWandElement:
        return None
    dInfo = dReward['info']
    iWand = dInfo['sid']
    iLevel = dInfo['level']
    LogReward(oGame, tobj.m_Scene, '%s wand %s %s %s' % (tobj.m_PlayerID, iWand, iLevel, sReason))
    oWandElement.AddShopBuyWandRecord(tobj, iWand)
    oWandElement.TrueRewardWand(tobj, iWand, iLevel, sReason)


def RewardWandComp(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    iComp = dInfo['sid']
    iLevel = dInfo['level']
    LogReward(oGame, tobj.m_Scene, '%s wandcomp %s %s %s' % (tobj.m_PlayerID, iComp, iLevel, sReason))
    tobj.m_WandCon.AddBagComp(iComp, iLevel, 1, sReason)


def RewardDice(oGame, tobj, dReward, sReason, dExtInfo):
    LogReward(oGame, tobj.m_Scene, '%s dice %s %s' % (tobj.m_PlayerID, dReward['info'], sReason))
    tobj.m_DiceCon.RewardDice(dReward['info'], sReason, bAccumulatedRollPoint = True)


def RewardS7Crystal(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    LogReward(oGame, tobj.m_Scene, '%s s7crystal %s %s' % (tobj.m_PlayerID, dInfo, sReason))
    tobj.m_BackpackCon.RewardCrystal(dInfo, sReason, dExtInfo = dExtInfo)


def RewardS7Module(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    LogReward(oGame, tobj.m_Scene, '%s s7module %s %s' % (tobj.m_PlayerID, dInfo, sReason))
    tobj.m_BackpackCon.RewardModule(dInfo, sReason)


def RewardS8ThirdPerform(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    LogReward(oGame, tobj.m_Scene, '%s s8thirdperform %s %s' % (tobj.m_PlayerID, dInfo, sReason))
    tobj.m_S8Con.RewardThirdItem(dInfo, sReason)


def RewardS8Gem(oGame, tobj, dReward, sReason, dExtInfo):
    dInfo = dReward['info']
    LogReward(oGame, tobj.m_Scene, '%s s8gem %s %s' % (tobj.m_PlayerID, dInfo, sReason))
    tobj.m_S8Con.RewardGemItem(dInfo, sReason)

REWARD_FUNC = {
    VIRTUAL_ITEM_S8GEMITEM: RewardS8Gem,
    VIRTUAL_ITEM_S8THIRDPERFORM: RewardS8ThirdPerform,
    VIRTUAL_ITEM_S7CRYSTALPACKET: RewardS7Crystal,
    VIRTUAL_ITEM_S7MODULE: RewardS7Module,
    VIRTUAL_ITEM_S7CRYSTAL: RewardS7Crystal,
    VIRTUAL_ITEM_DICE: RewardDice,
    VIRTUAL_ITEM_WANDCOMP: RewardWandComp,
    VIRTUAL_ITEM_WAND: RewardWand,
    VIRTUAL_ITEM_WANDCARDPACK: RewardWandCardPack,
    VIRTUAL_ITEM_PET: RewardPet,
    VIRTUAL_ITEM_DEVICECOMP: RewardDeviceComp,
    VIRTUAL_ITEM_MAGICPOWER: RewardMagicPower,
    VIRTUAL_ITEM_RAREITEM: RewardRareItem,
    VIRTUAL_ITEM_TALENTWEIGHT: RewardModifyTalentWeight,
    VIRTUAL_ITEM_SHOPGOODSWEIGHT: RewardAdditionalShopGoodsWeight,
    VIRTUAL_ITEM_GSCASHRELIFE: RewardAddGSCashRelife,
    VIRTUAL_ITEM_INSCRIPTIONPROP: RewardAddInscriptionProp,
    VIRTUAL_ITEM_GEMINI: RewardAdditionalGeminiInscription,
    VIRTUAL_ITEM_EXCLUSINSCRIPTION: RewardOpenExclusiveInscription,
    VIRTUAL_ITEM_WEAPONUPGRADE: RewardAdditionalWeaponUpgradeTimes,
    VIRTUAL_ITEM_HIDESHOPGOODS: RewardShowShopHiddenGoods,
    VIRTUAL_ITEM_EXTGSCASHDROP: RewardExtGSCashDropRatio,
    VIRTUAL_ITEM_GOLDENCUP: RewardGoldenCup,
    VIRTUAL_ITEM_TALENT: RewardTalent,
    VIRTUAL_UNLOCK_INITWEAPONDROP: RewardInitWeaponDrop,
    VIRTUAL_ITEM_WARCASH: RewardWarCash,
    VIRTUAL_ITEM_PASSIVE: RewardPassive,
    VIRTUAL_ITEM_KEY: RewardKey,
    VIRTUAL_ITEM_SHOPREFRESH: RewardShopRefresh,
    VIRTUAL_ITEM_AUTOPERFORM: RewardAutoPerform,
    VIRTUAL_ITEM_ATTR: RewardAttr,
    VIRTUAL_ITEM_RELIC: RewardRelic,
    VIRTUAL_ITEM_BULLET: RewardBullet,
    VIRTUAL_ITEM_EQUIP: RewardEquip,
    VIRTUAL_ITEM_DROP: RewardItemDrop }

def RewardItem(oGame, tobj, lstReward, sReason, dExtInfo = None):
    for dReward in lstReward:
        iType = dReward['item']
        func = REWARD_FUNC[iType]
        func(oGame, tobj, dReward, sReason, dExtInfo)
    

