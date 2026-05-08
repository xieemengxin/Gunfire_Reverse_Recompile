# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/eventnpcaction.pyc
# RelativePath: clientlogic/cl_npc/eventnpcaction.pyc
# Source Generated with Decompyle++
# File: eventnpcaction.pyc (Python 3.6)

from cl_commondefines import RELIC_TYPE_CURSE, CAL_BY_CURSE_RELIC, INSCRIPTION_TYPE_EXCLUSIVE, STATE_TIME_FOREVER, STATE_TIME_LIMIT, DAM_USE_HP, MG_EQUIP, VIRTUAL_ITEM_EQUIP, NWARRIOR_DROP_EQUIP, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP, VIRTUAL_ITEM_GOLDENCUP, NWARRIOR_DROP_RELIC, DROP_REASON_NPCREWARD, DEFEND_TREND_ARMOR, VIRTUAL_ITEM_ATTR, VIRTUAL_ITEM_WARCASH, NWARRIOR_DROP_CASH, VIRTUAL_ITEM_DROP, VIRTUAL_ITEM_RELIC, NPC_CB_VALUELIST, DEFAULT_DROP_RADIUS
from cl_cscommondef import EQUIP_TYPE_MAINWEAPON, WEAPON_ACTION_UPGRADE, ITEM_SOURCE_NPCREWARD, VIRTUAL_ITEM_MAGICPOWER
from cl_perform.load import GetInscriptionLib
from cl_only import ChooseKey, Functor, Time2Frame
from cl_object.logging import WarnpcLog
from cl_item.weapon import CHECK_WEAPON_ACTION, WEAPON_ACTION
import math
import cl_formula
import cl_reward
import cl_item
import cl_object.reason
import cl_math
import cl_notify
import cl_state
import cl_msgcenter
import cl_netattr
import cl_perform
from . import net
EVENT_TYPE_REMOVE_RELIC = 0
EVENT_TYPE_REMOVE_LEVELRELIC = 1
EVENT_TYPE_UPGRADE_RELIC = 2
EVENT_TYPE_DISABLE_CURSE_RELIC = 3

def InitWarCashCost(oOption, oHero, iCashArg):
    
    def ValidCostFunc(oNpc, oFuncHero):
        return oFuncHero.m_WarCash >= iCash

    
    def CostFunc(oNpc, oFuncHero):
        iCost = iCash
        if iCost == 0:
            iCost = oFuncHero.m_WarCash
        oNpc.CostLog(oFuncHero, 'warcash %d' % iCost)
        oFuncHero.AddCash(-iCost, oNpc.ActionKey(tOp))
        return 1

    tOp = oOption.m_ID
    dInfo = oOption.m_LimitInfo
    iCash = cl_formula.GetFormulaResult(oHero, iCashArg, dInfo)
    oOption.m_CostFunc[oHero.m_ID] = (ValidCostFunc, CostFunc)
    oOption.m_CostData[oHero.m_ID] = {
        'Amount': iCash }


def InitGSCashCost(oOption, oHero, iCashArg):
    
    def ValidCostFunc(oNpc, oFuncHero):
        return oFuncHero.m_WarGSCash >= iCash

    
    def CostFunc(oNpc, oFuncHero):
        iCost = iCash
        oNpc.CostLog(oFuncHero, 'gscash %d' % iCost)
        oFuncHero.ConsumeGSCash(iCost, oNpc.ActionKey(tOp))
        return 1

    tOp = oOption.m_ID
    dInfo = oOption.m_LimitInfo
    iCash = cl_formula.GetFormulaResult(oHero, iCashArg, dInfo)
    oOption.m_CostFunc[oHero.m_ID] = (ValidCostFunc, CostFunc)
    oOption.m_CostData[oHero.m_ID] = {
        'Amount': iCash }


def InitAttrCost(oOption, oHero, sAttr, iMul, iAdd):
    
    def ValidCostFunc(oNpc, oFuncHero):
        oAttr = oFuncHero.GetAttr(sRealAttr)
        if not oAttr:
            return 0
        iPreview = oAttr.PreviewChange(-iMul, -iAdd)
        if sRealAttr in ('ShieldMax', 'ArmorMax') and iPreview < 0:
            return 0
        if iPreview <= 0:
            return 0
        return 1

    
    def CostFunc(oNpc, oFuncHero):
        oNpc.CostLog(oFuncHero, 'attr %s %d %d' % (sRealAttr, iMul, iAdd))
        sKey = oNpc.ActionKey(tOp)
        oFuncHero.AttrChange(sRealAttr, -iMul, -iAdd, sKey, iSave = 1)
        return 1

    tOp = oOption.m_ID
    if oHero.m_DefendTrend & DEFEND_TREND_ARMOR and sAttr == 'ShieldMax':
        sRealAttr = 'ArmorMax'
    else:
        sRealAttr = sAttr
    oOption.m_CostFunc[oHero.m_ID] = (ValidCostFunc, CostFunc)
    oOption.m_CostData[oHero.m_ID] = {
        'Amount': (iMul if iMul else iAdd) // 100 }


def InitHPCost(oOption, oHero, iRatio, iValue):
    
    def ValidCostFunc(oNpc, oFuncHero):
        iHP = math.ceil(oFuncHero.HP() / 100) * 100
        if iRatio and iHP * (100 - iRatio) // 100 < 100:
            return 0
        if iValue and iHP - iValue < 100:
            return 0
        return 1

    
    def CostFunc(oNpc, oFuncHero):
        iChange = iValue
        if iRatio:
            iChange = math.ceil(math.ceil(oFuncHero.HP() / 100) * iRatio / 100) * 100
        oNpc.CostLog(oFuncHero, 'hp %d' % iChange)
        oReason = cl_object.reason.CStrReason(oNpc.ActionKey(tOp), None, {
            'DamType': DAM_USE_HP })
        oFuncHero.HPDirectModify('HP', oNpc.m_ID, -iChange, oReason)
        return 1

    tOp = oOption.m_ID
    iRatio = min(iRatio, 99)
    oOption.m_CostFunc[oHero.m_ID] = (ValidCostFunc, CostFunc)
    oOption.m_CostData[oHero.m_ID] = {
        'Amount': iRatio if iRatio else iValue // 100 }


def InitRelicCost(oOption, oHero, iType, iExtraTips = 0):
    
    def ValidCostFunc(oNpc, oFuncHero):
        if iRelic and not oFuncHero.m_RelicCon.GetPerform(iRelic):
            return 0
        if not iRelic and not oFuncHero.m_RelicCon.GetAllPerformSID():
            return 0
        return 1

    
    def CostFunc(oNpc, oFuncHero):
        iCostRelic = iRelic
        if not iCostRelic:
            lstHasRelic = oFuncHero.m_RelicCon.GetAllPerformSID()
            iCostRelic = lstHasRelic[oFuncHero.m_Game.Random(len(lstHasRelic))]
        oNpc.CostLog(oFuncHero, 'relic %d' % iCostRelic)
        oFuncHero.m_RelicCon.RemoveRelic(iCostRelic, 'npcCostRelic', iForce = 1)
        if iExtraTips:
            oFuncHero.m_RelicCon.GS2CRandomRemoveRelic(iCostRelic)
        oOption.m_CostData[oFuncHero.m_ID]['SID'] = iCostRelic
        return 1

    lstHasRelic = oHero.m_RelicCon.GetAllPerformSID()
    if lstHasRelic and iType == 1:
        iRelic = lstHasRelic[oHero.m_Game.Random(len(lstHasRelic))]
        oOption.AddCostRelic(oHero.m_ID, iRelic)
    else:
        iRelic = 0
    oOption.m_CostFunc[oHero.m_ID] = (ValidCostFunc, CostFunc)
    oOption.m_CostData[oHero.m_ID] = {
        'SID': iRelic }


def InitSelectedRelicCost(oOption, oHero, iRelicType, iQuality, iCount, iLevel):
    if not iLevel:
        iLevel = 0
    
    def ValidCostFunc(oNpc, oFuncHero):
        iHas = 0
        for oRelic in oFuncHero.m_RelicCon.GetAllPerform():
            if not oRelic.m_RelicType & iRelicType:
                continue
            if not oRelic.m_Quality & iQuality:
                continue
            if iLevel and oRelic.m_Level != iLevel:
                continue
            iHas += 1
        
        if iHas >= iCount:
            return 1
        return 0

    
    def CostFunc(oNpc, oFuncHero):
        dChooseData = oOption.GetChooseData(oHero.m_ID, iChooseIdx)
        if 'SelectedRelicCost' not in dChooseData:
            return 0
        lstRelic = dChooseData['SelectedRelicCost']
        if len(lstRelic) < iCount:
            return 0
        lstRelic = lstRelic[:iCount]
        oNpc.CostLog(oFuncHero, 'selectrelic %s' % lstRelic)
        oRelicCon = oFuncHero.m_RelicCon
        for iMixSID in lstRelic:
            if not oRelicCon.IsExistRelicByMixSID(iMixSID):
                return 0
        
        for iMixSID in lstRelic:
            oRelicCon.RemoveRelicByMixSID(iMixSID, 'npcSelectedRelicCost', iForce = 1)
            iRelic = oRelicCon.GetRelicSIDByMixSID(iMixSID)
            oOption.AddCostRelic(oHero.m_ID, iRelic)
        
        return 1

    
    def ChooseFunc(oNpc, oFuncHero):
        lstRelic = []
        oRelicCon = oFuncHero.m_RelicCon
        for iMixSID, oRelic in oRelicCon.GetAllRelicByMixSID().items():
            if not oRelic.m_RelicType & iRelicType:
                continue
            if not oRelic.m_Quality & iQuality:
                continue
            if iLevel and oRelic.m_Level != iLevel:
                continue
            lstRelic.append(iMixSID)
        
        if iLevel > 1:
            iEventType = EVENT_TYPE_REMOVE_LEVELRELIC
        else:
            iEventType = EVENT_TYPE_REMOVE_RELIC
        net.GS2CNPCEventChoose(oFuncHero, VIRTUAL_ITEM_RELIC, iCount, lstRelic, iEventType)
        net.SetNpcUICallBackFunction(oFuncHero, NPC_CB_VALUELIST, Functor(CBChooseFunc, iChooseIdx, oNpc.m_ID, oOption.m_ID, 'SelectedRelicCost', lstRelic), oNpc)

    oOption.m_CostFunc[oHero.m_ID] = (ValidCostFunc, CostFunc)
    oOption.m_CostData[oHero.m_ID] = { }
    iChooseIdx = oOption.AddChooseFunc(oHero.m_ID, ChooseFunc)


def CBChooseFunc(iChooseIdx, iNpc, tOption, sKey, lstPreChoose, oHero, lstAnswer):
    oNpc = oHero.m_Game.GetObject(iNpc)
    if not oNpc:
        return None
    oOption = oNpc.GetOption(tOption)
    if not oOption:
        return None
    if not lstAnswer:
        oNpc.RefreshStage(oHero)
        return None
    if lstPreChoose and not (set(lstAnswer) <= set(lstPreChoose)):
        return None
    dData = {
        sKey: lstAnswer }
    oOption.AddChooseData(oHero.m_ID, iChooseIdx, dData)
    oOption.ChooseOption(oNpc, oHero)


def ChooseCurseRelic(oHero):
    dCurse = oHero.m_RelicCon.GetChooseCurseRelic()
    if not dCurse:
        return 0
    iRelic = ChooseKey(oHero.m_Game, dCurse)
    return iRelic


def InitCurseRelicCost(oOption, oHero, iType):
    
    def ValidCostFunc(oNpc, oFuncHero):
        iTrueRelic = iRelic
        lstHasRelic = oFuncHero.m_RelicCon.GetAllPerformSID()
        if iTrueRelic in lstHasRelic:
            return 0
        return 1

    
    def CostFunc(oNpc, oFuncHero):
        iTrueRelic = iRelic
        if not iTrueRelic:
            iTrueRelic = ChooseCurseRelic(oFuncHero)
        oNpc.CostLog(oFuncHero, 'curserelic %d' % iTrueRelic)
        if not iTrueRelic:
            return 1
        dReward = {
            'item': VIRTUAL_ITEM_RELIC,
            'info': {
                'sid': iTrueRelic,
                'amount': 1 } }
        cl_reward.RewardItem(oNpc.m_Game, oFuncHero, [
            dReward], oNpc.ActionKey(tOp))
        oOption.m_CostData[oFuncHero.m_ID]['SID'] = iTrueRelic
        return 1

    tOp = oOption.m_ID
    if iType == 1:
        iRelic = ChooseCurseRelic(oHero)
    else:
        iRelic = 0
    oOption.m_CostFunc[oHero.m_ID] = (ValidCostFunc, CostFunc)
    oOption.m_CostData[oHero.m_ID] = {
        'SID': iRelic }


def InitWarCashReward(oOption, oHero, iCashArg, iDrop = 0, iRule = 0):
    
    def RewardFunc(oNpc, oFuncHero):
        dInfo = oOption.m_LimitInfo
        iTrueCash = cl_formula.GetFormulaResult(oHero, iCash, dInfo)
        if iTrueCash < 0 and iTrueCash + oHero.m_WarCash < 0:
            iTrueCash = -(oHero.m_WarCash)
        if iDrop:
            vDropPos = oNpc.GetPos()
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_CASH,
                    'DropInfo': [
                        {
                            'Cash': iTrueCash }],
                    'DropPos': vDropPos } }
            dExtInfo = {
                'Player': oFuncHero.m_ID }
        else:
            dReward = {
                'item': VIRTUAL_ITEM_WARCASH,
                'info': {
                    'amount': iTrueCash } }
            dExtInfo = { }
        iDelay = oOption.m_RewardDelay
        sKey = oNpc.ActionKey(tOp)
        if iDelay:
            dExtInfo['Scene'] = oNpc.m_Scene
            oNpc.Call_Out(Functor(DelayReward, oNpc, oFuncHero.m_ID, [
                dReward], sKey, dExtInfo), iDelay, sKey)
        else:
            cl_reward.RewardItem(oNpc.m_Game, oFuncHero, [
                dReward], sKey, dExtInfo)

    
    def ValidRewardFunc(oNpc, oFuncHero):
        if iRule == CAL_BY_CURSE_RELIC and len(oFuncHero.m_RelicCon.GetAllRelicSIDByType(RELIC_TYPE_CURSE)) == 0:
            return 0
        return 1

    tOp = oOption.m_ID
    if iRule in (CAL_BY_CURSE_RELIC,):
        iCash = iCashArg
    else:
        dInfo = oOption.m_LimitInfo
        iCash = cl_formula.GetFormulaResult(oHero, iCashArg, dInfo)
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.m_RewardData[oHero.m_ID] = {
        'Amount': iCash }
    oOption.AddConditionFunc(oHero.m_ID, ValidRewardFunc)


def InitAttrReward(oOption, oHero, sAttr, iMul, iAdd):
    
    def RewardFunc(oNpc, oFuncHero):
        dReward = {
            'item': VIRTUAL_ITEM_ATTR,
            'info': {
                'attr': sRealAttr,
                'mul': iMul,
                'add': iAdd } }
        sReason = oNpc.ActionKey(tOp)
        cl_reward.RewardItem(oNpc.m_Game, oFuncHero, [
            dReward], sReason)

    tOp = oOption.m_ID
    if oHero.m_DefendTrend & DEFEND_TREND_ARMOR and sAttr == 'ShieldMax':
        sRealAttr = 'ArmorMax'
    else:
        sRealAttr = sAttr
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.m_RewardData[oHero.m_ID] = {
        'Amount': (iMul if iMul else iAdd) // 100 }


def GetValidRelic(oHero, dWeight, dRoundMiniGame, iLevel):
    dValid = { }
    setAvailableRelic = oHero.m_RelicCon.GetAvailableRelic()
    oGame = oHero.m_Game
    if dRoundMiniGame:
        iRound = oGame.m_WarMgr.m_Round
        iWarNo = oGame.m_WarMgr.m_SID
        if iRound in dRoundMiniGame:
            iWarMiniGame = dRoundMiniGame[iRound]
            if isinstance(iWarMiniGame, dict):
                dMiniGame = iWarMiniGame
                if iWarNo not in dMiniGame:
                    return dValid
                dWarMiniGame = dict(dMiniGame[iWarNo])
                for _ in range(len(dWarMiniGame)):
                    iWarMiniGame = ChooseKey(oGame, dWarMiniGame)
                    dValid = GetValidRelicByMG(oGame, iWarMiniGame, setAvailableRelic)
                    if dValid:
                        break
                    dWarMiniGame.pop(iWarMiniGame)
                
            else:
                dValid = GetValidRelicByMG(oGame, iWarMiniGame, setAvailableRelic)
        elif dWeight:
            for iSID, iWeight in dWeight.items():
                if iSID in setAvailableRelic:
                    dValid[iSID] = iWeight
            
    if iLevel:
        lstInValid = []
        for iSID in dValid:
            clsRelic = cl_perform.GetPerformModule(iSID)
            if not not clsRelic:
                if clsRelic.m_MaxLevel < iLevel:
                    lstInValid.append(iSID)
                    continue
        
        for iSID in lstInValid:
            dValid.pop(iSID)
        
    return dValid


def GetValidRelicByMG(oGame, iWarMiniGame, setAvailableRelic):
    dValid = { }
    dCheck = { }
    iWarNo = iWarMiniGame // 10000
    if iWarNo == oGame.m_WarMgr.m_SID:
        iMiniGame = iWarMiniGame % 10000
        clsData = oGame.m_WarData.GetMiniGameData(iMiniGame)
        if clsData:
            dCheck = dict(clsData.m_ChooseWeight)
    for iSID, iWeight in dCheck.items():
        if iSID in setAvailableRelic:
            dValid[iSID] = iWeight
    
    return dValid


def InitRelicReward(oOption, oHero, iType, dWeight, iDrop = 0, dRoundMiniGame = None, iLevel = 0):
    
    def RewardFunc(oNpc, oFuncHero):
        iTrueRelic = iRelic
        if not iTrueRelic:
            dValid = GetValidRelic(oFuncHero, dWeight, dRoundMiniGame, iLevel)
            if oHero.m_ID in oOption.m_CostRelic.keys():
                iTrueRelic = ChooseRelic(oOption.m_CostRelic[oHero.m_ID], oGame, dValid, oHero)
                oOption.m_CostRelic.pop(oHero.m_ID)
            else:
                iTrueRelic = oGame.m_RandomMgr.ChooseKey('relic%d' % oHero.m_ID, {
                    'Select': dValid })
            if not iTrueRelic:
                WarnpcLog.Alert('%s no relic %s %s %s %s' % (oNpc.m_SID, iType, dWeight, dRoundMiniGame, dValid))
                return None
        dMsgInfo = {
            'Relic': iTrueRelic,
            'Level': iLevel }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EVENTNPC_REWARD_RELIC, oHero, dMsgInfo)
        if iDrop:
            vDropPos = CalOffsetCoodinates(oNpc, oHero)
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RELIC,
                    'DropInfo': [
                        iTrueRelic],
                    'DropPos': vDropPos,
                    'DropLevel': iLevel } }
            dExtInfo = {
                'Player': oFuncHero.m_ID,
                'DropReason': DROP_REASON_NPCREWARD }
        else:
            dReward = {
                'item': VIRTUAL_ITEM_RELIC,
                'info': {
                    'sid': iTrueRelic,
                    'amount': 1,
                    'level': iLevel } }
            dExtInfo = { }
        if 'ReplaceRelicInfo' in dMsgInfo:
            (iReplaceRelic, iReplaceLevel) = dMsgInfo['ReplaceRelicInfo'][0]
            iTrueRelic = iReplaceRelic
            dReward['info']['ShowedBeforDrop'] = 1
            if 'RelicUseOldLevel' in dMsgInfo and not dMsgInfo['RelicUseOldLevel']:
                dReward['info']['DropLevel'] = iReplaceLevel
            if dReward['item'] == VIRTUAL_ITEM_DROP:
                dReward['info']['DropInfo'][0] = iTrueRelic
            elif dReward['item'] == VIRTUAL_ITEM_RELIC:
                dReward['info']['sid'] = iTrueRelic
        iDelay = oOption.m_RewardDelay
        sKey = oNpc.ActionKey(tOp)
        if iDelay:
            dExtInfo['Scene'] = oNpc.m_Scene
            oNpc.Call_Out(Functor(DelayReward, oNpc, oFuncHero.m_ID, [
                dReward], sKey, dExtInfo), iDelay, sKey)
        else:
            cl_reward.RewardItem(oNpc.m_Game, oFuncHero, [
                dReward], sKey, dExtInfo)
        oOption.m_RewardData[oFuncHero.m_ID]['SID'] = iTrueRelic

    
    def ValidRewardFunc(oNpc, oFuncHero):
        if not GetValidRelic(oFuncHero, dWeight, dRoundMiniGame, iLevel):
            return 0
        return 1

    
    def ChooseRelic(iCostRelic, oGame, dValid, oHero):
        if iCostRelic in dValid:
            dValid.pop(iCostRelic)
        if len(dValid) == 0:
            return iCostRelic
        iRelic = oGame.m_RandomMgr.ChooseKey('relic%d' % oHero.m_ID, {
            'Select': dValid })
        return iRelic

    tOp = oOption.m_ID
    oGame = oHero.m_Game
    if iType == 1:
        dValid = GetValidRelic(oHero, dWeight, dRoundMiniGame, iLevel)
        if oHero.m_ID in oOption.m_CostRelic:
            iRelic = ChooseRelic(oOption.m_CostRelic[oHero.m_ID], oGame, dValid, oHero)
            oOption.m_CostRelic.pop(oHero.m_ID)
        else:
            iRelic = ChooseRelic(0, oGame, dValid, oHero)
    else:
        iRelic = 0
    if not iLevel:
        iLevel = 1
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    dMsgInfo = {
        'Relic': iRelic }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EVENTNPC_CHOOSE_RELIC, oHero, dMsgInfo)
    if 'ReplaceRelicInfo' in dMsgInfo:
        for iReplaceRelic, _ in dMsgInfo['ReplaceRelicInfo']:
            iRelic = iReplaceRelic
        
    oOption.m_RewardData[oHero.m_ID] = {
        'SID': iRelic if iRelic else 0 }
    oOption.AddConditionFunc(oHero.m_ID, ValidRewardFunc)


def InitGoldenCupReward(oOption, oHero, dCupSID):
    
    def RewardFunc(oNpc, oFuncHero):
        vPos = oNpc.GetPos()
        vCupPos = cl_math.Vec3Add(vPos, (0, oNpc.m_ModelHeight + 0.1, 0))
        dReward = {
            'item': VIRTUAL_ITEM_GOLDENCUP,
            'info': {
                'sid': iGoldenCupSID,
                'DropPos': vCupPos,
                'scene': oNpc.m_Scene,
                'VisiblePlayer': {
                    oFuncHero.m_PlayerID: 1 } } }
        iDelay = oOption.m_RewardDelay
        sKey = oNpc.ActionKey(tOp)
        if iDelay:
            oNpc.Call_Out(Functor(DelayReward, oNpc, oFuncHero.m_ID, [
                dReward], sKey, { }), iDelay, sKey)
        else:
            cl_reward.RewardItem(oNpc.m_Game, oFuncHero, [
                dReward], sKey)

    
    def ValidRewardFunc(oNpc, oFuncHero):
        clsNpcData = oNpc.m_Game.GetWarData().GetNpcData(iGoldenCupSID)
        if not clsNpcData or clsNpcData.m_FightType not in [
            NWARRIOR_NPC_LIMITGOLDENCUP,
            NWARRIOR_NPC_GOLDENCUP,
            NWARRIOR_NPC_EXCHANGEGOLDENCUP]:
            iWarNo = oFuncHero.m_Game.m_WarMgr.m_SID
            WarnpcLog.Alert('warno%d eventnpc%d no goldencupnpc' % (iWarNo, oNpc.m_SID))
            return 0
        return 1

    tOp = oOption.m_ID
    oGame = oHero.m_Game
    iWarNo = oGame.m_WarMgr.m_SID
    iGoldenCupSID = dCupSID.get(iWarNo, 0) % 10000
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.AddConditionFunc(oHero.m_ID, ValidRewardFunc)


def GetValidWeapon(oHero, dWeight, dInscription):
    lstAllUnlockItem = oHero.Query('Illus')['Weapon']
    dValid = { }
    dIns = GetInscriptionLib()[INSCRIPTION_TYPE_EXCLUSIVE]
    for iSID in lstAllUnlockItem:
        if iSID in dWeight or INSCRIPTION_TYPE_EXCLUSIVE in dInscription:
            clsEquip = cl_item.GetItemCls(iSID)
            for iPerform in dIns:
                clsPerform = cl_perform.GetPerformModule(iPerform)
                if clsPerform.CheckValidItem(clsEquip, []):
                    break
            
        dValid[iSID] = dWeight[iSID]
    
    return dValid


def InitWeaponReward(oOption, oHero, iType, dMinigameSID, iDrop = 0, iPointGrade = 0, dInscription = None, iEnhance = 0):
    
    def RewardFunc(oNpc, oFuncHero):
        iTrueWeapon = iWeapon
        if not iTrueWeapon:
            dValid = GetValidWeapon(oFuncHero, dWeight, dInscription)
            iTrueWeapon = oGame.m_RandomMgr.ChooseKey('weapon%d' % oFuncHero.m_ID, {
                'Select': dValid })
            iGrade = iPointGrade + cl_reward.GetWeaponRewardGrade(oGame)
            oWeapon = cl_item.CreateEquip(oGame, iTrueWeapon, iGrade, oOwner = oHero, iSource = ITEM_SOURCE_NPCREWARD)
        else:
            oWeapon = oOption.m_RewardData[oFuncHero.m_ID]['Item']
        if not oWeapon:
            return None
        if iDrop:
            vDropPos = CalOffsetCoodinates(oNpc, oHero)
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_EQUIP,
                    'DropInfo': [
                        oWeapon],
                    'DropPos': vDropPos } }
            dExtInfo = {
                'Player': oFuncHero.m_ID,
                'DropReason': DROP_REASON_NPCREWARD }
        else:
            dReward = {
                'item': VIRTUAL_ITEM_EQUIP,
                'info': {
                    'sid': iTrueWeapon,
                    'item': oWeapon,
                    'data': { } } }
            dExtInfo = { }
        if oWeapon.Type() & EQUIP_TYPE_MAINWEAPON == EQUIP_TYPE_MAINWEAPON:
            oBulletcom = oWeapon.GetComponent('Bullet')
            if oBulletcom:
                oBulletcom.BulletModify(oBulletcom.MaxBullet())
        if dInscription:
            oInscriptionCom = oWeapon.GetComponent('Inscription')
            for iType, iCnt in dInscription.items():
                oInscriptionCom.ResetInscriptionByType(iType, iCnt)
            
        sKey = oNpc.ActionKey(tOp)
        if iEnhance:
            oWeapon.AddEnhance(iEnhance, sKey)
        iDelay = oOption.m_RewardDelay
        if iDelay:
            dExtInfo['Scene'] = oNpc.m_Scene
            oNpc.Call_Out(Functor(DelayReward, oNpc, oFuncHero.m_ID, [
                dReward], sKey, dExtInfo), iDelay, sKey)
        else:
            cl_reward.RewardItem(oGame, oFuncHero, [
                dReward], sKey, dExtInfo)
        oOption.m_RewardData[oFuncHero.m_ID]['SID'] = iTrueWeapon

    
    def ValidRewardFunc(oNpc, oFuncHero):
        if not GetValidWeapon(oFuncHero, dWeight, dInscription):
            iWarNo = oGame.m_WarMgr.m_SID
            WarnpcLog.Alert('warno%d eventnpc%d no enough weapon' % (iWarNo, oNpc.m_SID))
            return 0
        if dInscription and INSCRIPTION_TYPE_EXCLUSIVE in dInscription:
            if not oGame.m_WarMgr.Query('ExclusiveInscription', 0):
                return 0
            oWeapon = oOption.m_RewardData[oFuncHero.m_ID]['Item']
            if oWeapon and not oWeapon.m_TmpData.get('TempExclusiveInscription', 0):
                return 0
        return 1

    tOp = oOption.m_ID
    oGame = oHero.m_Game
    iWarNo = oGame.m_WarMgr.m_SID
    iMinigameSID = dMinigameSID.get(iWarNo, 0) % 10000
    clsData = oGame.m_WarData.GetMiniGameData(iMinigameSID)
    dWeight = clsData.GetChooseWeight(oHero) if clsData and clsData.m_Type == MG_EQUIP else { }
    iWeapon = 0
    oWeapon = None
    iPointGrade = cl_formula.GetFormulaResult(oHero, iPointGrade) if iPointGrade is not None else 0
    if iType == 1:
        dValid = GetValidWeapon(oHero, dWeight, dInscription)
        iWeapon = oGame.m_RandomMgr.ChooseKey('weapon%d' % oHero.m_ID, {
            'Select': dValid })
        if iWeapon:
            iGrade = iPointGrade + cl_reward.GetWeaponRewardGrade(oGame)
            oWeapon = cl_item.CreateEquip(oGame, iWeapon, iGrade, oOwner = oHero, iSource = ITEM_SOURCE_NPCREWARD)
            iWeapon = oWeapon.m_SID
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.m_RewardData[oHero.m_ID] = {
        'SID': iWeapon if iWeapon else 0,
        'Item': oWeapon }
    oOption.AddConditionFunc(oHero.m_ID, ValidRewardFunc)


def InitHPReward(oOption, oHero, iRatio, iValue):
    
    def RewardFunc(oNpc, oFuncHero):
        iChange = iValue
        if iRatio:
            iChange = oFuncHero.HP() * iRatio // 100
        oReason = cl_object.reason.CStrReason(oNpc.ActionKey(tOp), None, {
            'DamType': DAM_USE_HP })
        oFuncHero.HPDirectModify('HP', oNpc.m_ID, iChange, oReason)

    tOp = oOption.m_ID
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.m_RewardData[oHero.m_ID] = {
        'Amount': iRatio if iRatio else iValue // 100 }


def DelayReward(oNpc, iHero, lstReward, sKey, dExtInfo):
    oGame = oNpc.m_Game
    oHero = oGame.GetObject(iHero)
    if oHero:
        dExtInfo['NPC'] = oNpc.m_ID
        cl_reward.RewardItem(oGame, oHero, lstReward, sKey, dExtInfo)


def InitState(oOption, oHero, dRoundState, tTime, dArgs):
    
    def RewardFunc(oNpc, oFuncHero):
        iTime = cl_formula.GetFormulaResult(oFuncHero, tTime)
        iTimeType = STATE_TIME_LIMIT if iTime else STATE_TIME_FOREVER
        oReason = cl_object.reason.CStrReason(oNpc.ActionKey(tOp))
        dRet = cl_formula.CalArgsFormula(oFuncHero, dArgs, oHero.AttrCache())
        dStateArgs = {
            'AID': oFuncHero.m_ID,
            'RS': oReason,
            'arg': dRet }
        oState = cl_state.AddState(oHero, iState, iTimeType, Time2Frame(iTime), dStateArgs)
        if oState:
            oState.Enable(oHero)

    if not dRoundState:
        return None
    iRound = oHero.m_Game.m_WarMgr.m_Round
    if iRound not in dRoundState:
        cl_notify.GS2CDebugMsg(oHero.m_Game, oHero.m_PlayerID, '未配置战场周目%d状态奖励' % iRound)
        iRound = sorted(dRoundState)[0]
    dState = dRoundState[iRound]
    iState = ChooseKey(oHero.m_Game, dState)
    if not iState:
        return None
    tOp = oOption.m_ID
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.m_RewardData[oHero.m_ID] = {
        'SID': iState }


def InitWeaponAction(oOption, oHero, iPos, iActionType, dArgs):
    
    def ValidRewardFunc(oNpc, oFuncHero):
        if iActionType not in CHECK_WEAPON_ACTION:
            return 0
        lstWeapon = oFuncHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
        if not lstWeapon:
            return 0
        for oWeapon in lstWeapon:
            if CHECK_WEAPON_ACTION[iActionType](oWeapon, dArgs):
                return 1
        
        return 0

    
    def RewardFunc(oNpc, oFuncHero):
        dChooseData = oOption.GetChooseData(oFuncHero.m_ID, iChooseIdx)
        if 'SelectedWeaponPos' not in dChooseData:
            return None
        lstPos = dChooseData['SelectedWeaponPos']
        oWeapon = oFuncHero.m_WieldCon.GetItemByPos(lstPos[0])
        if not oWeapon or not CHECK_WEAPON_ACTION[iActionType](oWeapon, dArgs):
            return None
        WEAPON_ACTION[iActionType](oWeapon, dArgs)

    
    def ChooseFunc(oNpc, oFuncHero):
        lstInfo = [
            (GetWeaponData(oFuncHero, iActionType, dArgs), iUpgradeLevel)]
        net.GS2CNPCEventWeaponAction(oFuncHero, iActionType, oNpc.m_FightType, lstInfo)
        net.SetNpcUICallBackFunction(oFuncHero, NPC_CB_VALUELIST, Functor(CBChooseFunc, iChooseIdx, oNpc.m_ID, oOption.m_ID, 'SelectedWeaponPos', []), oNpc)

    iUpgradeLevel = dArgs.get('WeaponUpgradeLevel', 0)
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.AddConditionFunc(oHero.m_ID, ValidRewardFunc)
    oOption.m_RewardData[oHero.m_ID] = {
        'Pos': iPos,
        'Amount': iUpgradeLevel }
    iChooseIdx = oOption.AddChooseFunc(oHero.m_ID, ChooseFunc)


def GetWeaponData(oHero, iActionType, dArgs):
    lstWeapon = []
    for oWeapon in oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON):
        if not oWeapon:
            continue
        lstAttr = []
        dAttr = {
            'Attr': lstAttr }
        iPos = oWeapon.m_Pos
        if iActionType == WEAPON_ACTION_UPGRADE:
            iUpgradeLevel = dArgs['WeaponUpgradeLevel'] if 'WeaponUpgradeLevel' in dArgs else 0
            iGrade = oWeapon.m_Grade + iUpgradeLevel
            for sAttr in cl_netattr.INFO_OBJECT_INIT[cl_netattr.PROP_DROPITEM_MAINWEAPON]:
                if sAttr not in ('Att',):
                    continue
                (iIdx, _, iType, iLen, _) = cl_netattr.INFO_PROP_NAME[sAttr]
                iValue = oWeapon.GetAttrValueByGrade(sAttr, iGrade)
                if iValue is None:
                    continue
                lstAttr.append((iIdx, iType, iLen, iValue))
            
        iValid = 0
        if CHECK_WEAPON_ACTION[iActionType](oWeapon, dArgs):
            iValid = 1
        lstWeapon.append((oWeapon.m_ID, iPos, iValid, dAttr))
    
    return lstWeapon


def InitSelectedRelicReward(oOption, oHero, iRelicType, iQuality, iCount):
    
    def ValidCostFunc(oNpc, oFuncHero):
        iHas = 0
        for oRelic in oFuncHero.m_RelicCon.GetAllPerform():
            if not oRelic.m_RelicType & iRelicType:
                continue
            if not oRelic.m_Quality & iQuality:
                continue
            iHas += 1
        
        if iHas >= iCount:
            return 1
        return 0

    
    def CostFunc(oNpc, oFuncHero):
        dChooseData = oOption.GetChooseData(oHero.m_ID, iChooseIdx)
        if 'SelectedRelicCost' not in dChooseData:
            return 0
        lstRelic = dChooseData['SelectedRelicCost']
        if len(lstRelic) < iCount:
            return 0
        lstRelic = lstRelic[:iCount]
        oNpc.CostLog(oFuncHero, 'selectrelic %s' % lstRelic)
        oRelicCon = oFuncHero.m_RelicCon
        for iMixSID in lstRelic:
            if not oRelicCon.IsExistRelicByMixSID(iMixSID):
                return 0
        
        lstReward = []
        for iMixSID in lstRelic:
            oRelicCon.RemoveRelicByMixSID(iMixSID, 'npcSelectedRelicReward', iForce = 1)
            iRelic = oRelicCon.GetRelicSIDByMixSID(iMixSID)
            oOption.AddCostRelic(oHero.m_ID, iRelic)
            lstReward.append(iRelic)
        
        oOption.m_RewardData[oFuncHero.m_ID]['SID'] = lstReward
        return 1

    
    def ChooseFunc(oNpc, oFuncHero):
        lstRelic = []
        oRelicCon = oFuncHero.m_RelicCon
        for iMixSID, oRelic in oRelicCon.GetAllRelicByMixSID().items():
            if not oRelic.m_RelicType & iRelicType:
                continue
            if not oRelic.m_Quality & iQuality:
                continue
            lstRelic.append(iMixSID)
        
        net.GS2CNPCEventChoose(oFuncHero, VIRTUAL_ITEM_RELIC, iCount, lstRelic, EVENT_TYPE_REMOVE_RELIC)
        net.SetNpcUICallBackFunction(oFuncHero, NPC_CB_VALUELIST, Functor(CBChooseFunc, iChooseIdx, oNpc.m_ID, oOption.m_ID, 'SelectedRelicCost', lstRelic), oNpc)

    oOption.m_RewardFunc[oHero.m_ID] = CostFunc
    oOption.m_RewardData[oHero.m_ID] = { }
    oOption.AddConditionFunc(oHero.m_ID, ValidCostFunc)
    iChooseIdx = oOption.AddChooseFunc(oHero.m_ID, ChooseFunc)


def InitUpgradeRelicReward(oOption, oHero, iQuality, iCount, iDrop = 0):
    
    def ValidRewardFunc(oNpc, oFuncHero):
        iHas = 0
        for oRelic in oFuncHero.m_RelicCon.GetAllPerform():
            if oRelic.m_RelicType == RELIC_TYPE_CURSE:
                continue
            if not oRelic.m_Quality & iQuality:
                continue
            if oRelic.m_MaxLevel < 2 or oRelic.m_Level != 1:
                continue
            iHas += 1
        
        if iHas >= iCount:
            return 1
        return 0

    
    def RewardFunc(oNpc, oFuncHero):
        dChooseData = oOption.GetChooseData(oHero.m_ID, iChooseIdx)
        if 'UpgradeRelic' not in dChooseData:
            return 0
        lstRelic = dChooseData['UpgradeRelic']
        if len(lstRelic) < iCount:
            return 0
        lstRelic = lstRelic[:iCount]
        oNpc.CostLog(oFuncHero, 'selectrelic %s' % lstRelic)
        oRelicCon = oFuncHero.m_RelicCon
        for iMixSID in lstRelic:
            if not oRelicCon.IsExistRelicByMixSID(iMixSID):
                return 0
        
        iHero = oFuncHero.m_ID
        iDelay = oOption.m_RewardDelay
        sKey = oNpc.ActionKey(tOp)
        vPos = CalOffsetCoodinates(oNpc, oHero)
        lstReward = []
        for iMixSID in lstRelic:
            oRelicCon.RemoveRelicByMixSID(iMixSID, 'npcUpgradeRelicReward', iForce = 1)
            iRelic = oRelicCon.GetRelicSIDByMixSID(iMixSID)
            if iDrop:
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_RELIC,
                        'DropInfo': [
                            iRelic],
                        'DropPos': vPos,
                        'DropLevel': 2 } }
                dExtInfo = {
                    'Player': iHero,
                    'DropReason': DROP_REASON_NPCREWARD }
            else:
                dReward = {
                    'item': VIRTUAL_ITEM_RELIC,
                    'info': {
                        'sid': iRelic,
                        'amount': 1,
                        'level': 2 } }
                dExtInfo = { }
            dReward['info']['ShowedBeforDrop'] = 1
            if iDelay:
                dExtInfo['Scene'] = oNpc.m_Scene
                oNpc.Call_Out(Functor(DelayReward, oNpc, iHero, [
                    dReward], sKey, dExtInfo), iDelay, sKey)
            else:
                cl_reward.RewardItem(oNpc.m_Game, oFuncHero, [
                    dReward], sKey, dExtInfo)
            lstReward.append(iRelic)
        
        oOption.m_RewardData[iHero]['SID'] = lstReward
        return 1

    
    def ChooseFunc(oNpc, oFuncHero):
        lstRelic = []
        oRelicCon = oFuncHero.m_RelicCon
        for iMixSID, oRelic in oRelicCon.GetAllRelicByMixSID().items():
            if oRelic.m_RelicType == RELIC_TYPE_CURSE:
                continue
            if not oRelic.m_Quality & iQuality:
                continue
            if oRelic.m_MaxLevel < 2 or oRelic.m_Level != 1:
                continue
            lstRelic.append(iMixSID)
        
        net.GS2CNPCEventChoose(oFuncHero, VIRTUAL_ITEM_RELIC, iCount, lstRelic, EVENT_TYPE_UPGRADE_RELIC)
        net.SetNpcUICallBackFunction(oFuncHero, NPC_CB_VALUELIST, Functor(CBChooseFunc, iChooseIdx, oNpc.m_ID, oOption.m_ID, 'UpgradeRelic', lstRelic), oNpc)

    tOp = oOption.m_ID
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.m_RewardData[oHero.m_ID] = { }
    oOption.AddConditionFunc(oHero.m_ID, ValidRewardFunc)
    iChooseIdx = oOption.AddChooseFunc(oHero.m_ID, ChooseFunc)


def InitMagicPowerReward(oOption, oHero, iOption, iMagicPower):
    
    def RewardFunc(oNpc, oFuncHero):
        sKey = oNpc.ActionKey(tOp)
        vDropPos = CalOffsetCoodinates(oNpc, oHero)
        dReward = {
            'item': VIRTUAL_ITEM_MAGICPOWER,
            'info': {
                'Option': iOption,
                'MagicPower': iMagicPower,
                'DropPos': vDropPos,
                'Scene': oNpc.m_Scene } }
        iDelay = oOption.m_RewardDelay
        if iDelay:
            oNpc.Call_Out(Functor(DelayReward, oNpc, oFuncHero.m_ID, [
                dReward], sKey, {
                'DropReason': DROP_REASON_NPCREWARD }), iDelay, sKey)
        else:
            cl_reward.RewardItem(oNpc.m_Game, oFuncHero, [
                dReward], sKey, {
                'DropReason': DROP_REASON_NPCREWARD })

    
    def ValidRewardFunc(oNpc, oFuncHero):
        if not iOption and not iMagicPower:
            return 0
        oWarMgr = oNpc.m_Game.m_WarMgr
        oRelicTalentElement = oWarMgr.GetComponent('RelicTalentElement')
        if not oRelicTalentElement or not (oRelicTalentElement.m_Enable):
            return 0
        if oWarMgr.IsEndless():
            return 0
        return 1

    tOp = oOption.m_ID
    oOption.m_RewardFunc[oHero.m_ID] = RewardFunc
    oOption.m_RewardData[oHero.m_ID] = {
        'Option': iOption,
        'MagicPower': iMagicPower }
    oOption.AddConditionFunc(oHero.m_ID, ValidRewardFunc)


def CalOffsetCoodinates(oNpc, oHero):
    vPos = oNpc.GetPos()
    iNoLimit = oHero.Query('NpcInteractChooseNoLimit', 0)
    if not iNoLimit:
        return vPos
    iChooseCnt = oNpc.m_InteractChooseCnt.get(oHero.m_ID, 0)
    return CalOffsetCoodinates2(oNpc, iChooseCnt)


def CalOffsetCoodinates2(oNpc, iChooseCnt):
    vPos = oNpc.GetPos()
    if not iChooseCnt:
        return vPos
    vFace = oNpc.GetFacing()
    vVertical = (-vFace[2], 0, vFace[0])
    fInterval = DEFAULT_DROP_RADIUS
    iOffset = -(iChooseCnt + 1) // 2 if iChooseCnt % 2 else iChooseCnt // 2
    vPos = cl_math.Vec3DisplaceDir(vPos, vVertical, fInterval * iOffset)
    return vPos

