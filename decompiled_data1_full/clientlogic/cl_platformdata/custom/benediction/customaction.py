# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/custom/benediction/customaction.pyc
# RelativePath: clientlogic/cl_platformdata/custom/benediction/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_commondefines import SUIT_RELIC, VIRTUAL_ITEM_RELIC, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_RELIC, WARRIOR_MONSTER, WARRIOR_SUMMON, WARRIOR_SUMMON_STELE, WARRIOR_BUILD, SIDE_TYPE_MONSTER, INKMASTER_HERO, NWARRIOR_NPC_S7SHOP, VIRTUAL_ITEM_S7CRYSTALPACKET
from cl_only import ShufferList, ChooseMulKeys, PY_FLAG_SERVANTTARGET
from cl_platformdata import GetIgnoreBeTarget
import cl_reward
import cl_action
import cl_snetwar
import cl_evact

def CustomAction13723(oWarrior, oLifeCycle, dInfo):
    oGame = oWarrior.m_Game
    oSuitElement = oGame.m_WarMgr.GetComponent('SuitElement')
    if not oSuitElement:
        return None
    if oWarrior.Query('Loading', 0):
        return None
    sKey = oLifeCycle.m_Key
    if oWarrior.Query(sKey, 0):
        return None
    oWarrior.Set(sKey, 1)
    lstChoose = dInfo['ChooseList'].split('|') if dInfo['ChooseList'] else []
    for i in range(len(lstChoose)):
        lstChoose[i] = int(lstChoose[i])
    
    lstChoose = ShufferList(oGame, lstChoose)
    setUnlock = oWarrior.Query('Illus')['Relic']
    iNum = dInfo['Num']
    iLevel = dInfo['RewardLevel']
    dCondition = oSuitElement.m_SuitCon
    dCurReward = {
        'ChooseRelic': { },
        'OwnedRelic': { } }
    oRelicCon = oWarrior.m_RelicCon
    for iSuit in lstChoose:
        if iSuit not in dCondition:
            continue
        dRelic = {
            'ChooseRelic': { },
            'OwnedRelic': { } }
        for iType, iSID in dCondition[iSuit].values():
            if iType != SUIT_RELIC:
                continue
            if iSID not in setUnlock:
                continue
            pfobj = oRelicCon.GetPerform(iSID)
            if pfobj and pfobj.m_Level == iLevel:
                dRelic['OwnedRelic'][iSID] = 10
                continue
            dRelic['ChooseRelic'][iSID] = 10
        
        iCount = len(dRelic['ChooseRelic'])
        if iCount < iNum:
            iCurRewardNum = len(dCurReward['ChooseRelic'])
            if iCount > iCurRewardNum:
                dCurReward = dRelic
            else:
                dCurReward = dRelic
                break
        if not None['ChooseRelic'] and not dCurReward['OwnedRelic']:
            dCurReward = dRelic
    
    dChooseReward = dCurReward['ChooseRelic']
    iCurRewardNum = len(dChooseReward)
    if iCurRewardNum == iNum:
        lstReward = list(dChooseReward)
    elif iCurRewardNum < iNum:
        iDropRewardNum = iNum - iCurRewardNum
        lstDropReward = ChooseMulKeys(oGame, dCurReward['OwnedRelic'], iDropRewardNum)
        vDropPos = oWarrior.GetPos()
        for iSID in lstDropReward:
            dInfo = {
                'DropType': NWARRIOR_DROP_RELIC,
                'DropPos': vDropPos,
                'DropLevel': iLevel,
                'DropInfo': [
                    iSID] }
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': dInfo }
            cl_reward.RewardItem(oGame, oWarrior, [
                dReward], sKey, {
                'Player': oWarrior.m_ID })
        
        if iCurRewardNum == 0:
            return None
        lstReward = list(dChooseReward)
    else:
        lstReward = ChooseMulKeys(oGame, dChooseReward, iNum)
    for iSID in lstReward:
        oWarrior.m_RelicCon.AddFilterRelic(iSID, sKey)
    
    for iSID in lstReward:
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iSID,
                'level': iLevel } }
        cl_reward.RewardItem(oGame, oWarrior, [
            dReward], sKey)
        oWarrior.m_RelicCon.DelFilterRelic(iSID, sKey)
    


def CustomAction13556(oWarrior, oEventCB, dInfo):
    if oWarrior.m_SID != INKMASTER_HERO:
        return None
    iScene = oWarrior.m_Scene
    if not iScene:
        return None
    oGame = oWarrior.m_Game
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return None
    lstTarget = []
    lstSortedDis = []
    for sType in ('Monster', 'Summon', 'Protege'):
        lstTarget.extend(oScene.GetObjectsByType(sType))
    
    dDis = oGame.Scene_GetTargetDisMap(oWarrior.m_ID, lstTarget, 1)
    lstSortedDis = sorted(dDis.items(), key = (lambda x: x[1]))
    for iTarget, fDis in lstSortedDis:
        if fDis > dInfo['Dis']:
            break
        oTarget = oGame.GetObject(iTarget, PY_FLAG_SERVANTTARGET)
        if not oTarget:
            continue
        if not ValidTarget(oTarget, dInfo):
            continue
        iPerform = dInfo['Perform']
        oPerform = oWarrior.GetPerformIfNoThenNew(iPerform)
        oPerform.AddCanUseCount()
        cl_snetwar.GS2CNotifyStartSkill(oGame, oWarrior.m_PlayerID, iPerform, oPerform.m_ID, 0, {
            'Target': oTarget.m_ID,
            'Enhance': 1,
            'ThrowMsg': 1 })
        oLifeCycle = oEventCB.GetCBLifeCycle()
        oInkCon = oWarrior.m_InkCon
        oInkCon.ModifyInkValue(-dInfo['CostInkValue'], oLifeCycle.Key())
        cl_action.PassiveAddState(oWarrior, oLifeCycle, dInfo['State'], dInfo['StateTime'], { }, 1)
    


def CustomAction13734(oTarget, oLifeCycle, dInfo):
    
    def ClearFunc(oTarget, oLifeCycle):
        oTarget.ClearBaseDamRatioByKey(sKey)

    sKey = oLifeCycle.Key()
    oBackpackCon = oTarget.m_BackpackCon
    if not oBackpackCon:
        return None
    dOverflowPoint = { }
    for oModule in oBackpackCon.CustomGetModule(iCheckEquip = 1):
        iOverflowPoint = oBackpackCon.GetModuleOverflowPoint(oModule.m_ID)
        if not iOverflowPoint:
            continue
        for iPerOverflowPoint in range(1, iOverflowPoint + 1):
            if iPerOverflowPoint not in dOverflowPoint:
                dOverflowPoint[iPerOverflowPoint] = 0
            dOverflowPoint[iPerOverflowPoint] += 1
        
    
    if not dOverflowPoint:
        oTarget.ClearBaseDamRatioByKey(sKey)
        return None
    iMul = 0
    iOriginalDamMul = dInfo['OriginalDamMul']
    iEachOverflowDecrease = dInfo['EachOverflowDecrease']
    iMinimumDamMul = dInfo['MinimumDamMul']
    for iOverflowPoint, iCnt in dOverflowPoint.items():
        iMul += max(iOriginalDamMul - (iOverflowPoint - 1) * iEachOverflowDecrease, iMinimumDamMul) * iCnt
    
    oTarget.ChangeBaseDamRatio(sKey, iAdd = 0, iMul = iMul)
    oLifeCycle.AddUniqueDisableFunc('benediction13734ChangeBaseDamRatio', ClearFunc, iCover = 0)


def CustomAction13734_1(oTarget, oLifeCycle, dInfo):
    oPerform = oLifeCycle.GetObject()
    if not oPerform:
        return None
    dPerform = { }
    dPerform[oPerform.m_SID] = dInfo
    cl_snetwar.GS2CCustomPerformData(dPerform, oTarget.m_PlayerID)


def ValidTarget(oTarget, dInfo):
    if oTarget.m_FightType & WARRIOR_MONSTER:
        return 1
    if oTarget.m_FightType & WARRIOR_BUILD and oTarget.m_SID in dInfo['TargetBuild']:
        return 1
    if oTarget.m_FightType == WARRIOR_SUMMON_STELE:
        return 1
    if oTarget.m_FightType & WARRIOR_SUMMON and oTarget.m_Side == SIDE_TYPE_MONSTER and oTarget.m_SID not in GetIgnoreBeTarget():
        return 1
    return 0


def CustomAction13735(oWarrior, oEventCB, dInfo):
    oGame = oWarrior.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oWarrior.m_Scene)
    if not oScene:
        return None
    lstNPC = oScene.GetObjectsByType('NPC')
    for iTarget in lstNPC:
        oTarget = oGame.GetObject(iTarget)
        if not oTarget:
            continue
        if oTarget.m_FightType != NWARRIOR_NPC_S7SHOP:
            continue
        if oWarrior.m_ID not in oTarget.m_GoodsData:
            continue
        dGoods = oTarget.m_GoodsData[oWarrior.m_ID]
        for oGoods in dGoods.values():
            if oGoods.m_GoodsType != VIRTUAL_ITEM_S7CRYSTALPACKET:
                continue
            for dCrystal in oGoods.m_Items:
                cl_evact.SetS7CrystalExtInfo(oGame, oWarrior.m_PlayerID, dCrystal['info'], dInfo['Key'], dInfo['TotalPoint'], dInfo['MaxPoint'])
            
            dShowInfo = oGoods.GetShowInfo()
            dShowInfo['MaxPoint'] += dInfo['TotalPoint']
            oGoods.SetShowInfo(dShowInfo)
            oTarget.UpdateShowInfo(oWarrior, oGoods, 'CrystalPacket')
        
    

