# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_wand.pyc
# RelativePath: clientlogic/cl_minigame/mg_wand.pyc
# Source Generated with Decompyle++
# File: mg_wand.pyc (Python 3.6)

from cl_commondefines import MG_WAND, VIRTUAL_ITEM_DROP, WANDPUT_MAX_LAYER, NWARRIOR_DROP_MAGIC_WAND, WANDPUT_SHOPBUY, S5_ITEM_TYPE_WAND
from cl_only import ChooseKey, DeepCopy
from .mobject import CDropGame, CBaseGameData
import cl_wand
EXTRA_CHOOSEWEIGHT = 4

class CWandGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_WAND
    m_ChooseLevelWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseLevelWeight = DeepCopy(cls.m_ChooseLevelWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CWandGame

    GetGameClass = classmethod(GetGameClass)


class CWandGame(CDropGame):
    m_ChooseLevelWeight = { }
    
    def GetRewardInfo(self):
        lstReward = []
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oWandElement = oWarMgr.GetWandElement()
        if not oWandElement:
            return lstReward
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return lstReward
        oTarget = oGame.GetObject(self.m_Player)
        if not oTarget:
            return lstReward
        oWandCon = oTarget.m_WandCon
        if not oWandCon:
            return lstReward
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iLayer = min(WANDPUT_MAX_LAYER, oLevelCtrl.m_LayerNum)
        iLevel = self.m_ChooseLevelWeight.get(iLayer, 1)
        dChooseWeight = DeepCopy(oWandElement.GetWandPutWithFilter(oTarget.m_PlayerID, WANDPUT_SHOPBUY))
        dExtraChoose = oWandElement.GetShopBuyWandRecord(oTarget.m_PlayerID)
        lstPlayerSign = oWandCon.GetSignByItemType(S5_ITEM_TYPE_WAND)
        if lstPlayerSign:
            dPlayerSign = dict.fromkeys(lstPlayerSign, 1)
            dExtraChoose.update(dPlayerSign)
        for iWand in dExtraChoose:
            if iWand in dChooseWeight:
                dChooseWeight[iWand] *= EXTRA_CHOOSEWEIGHT
        
        iTime = self.Query('Times', 1)
        for _ in range(iTime):
            iChooseWand = ChooseKey(oGame, dChooseWeight)
            iRewardLevel = cl_wand.FixWandLevel(iChooseWand, iLevel)
            oWand = cl_wand.CreateWand(oGame, oWandCon, iChooseWand, iRewardLevel, { }, dTmp = {
                'NoInitComp': 1,
                'MGDrop': 1 })
            if not oWand:
                continue
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_MAGIC_WAND,
                    'DropInfo': [
                        oWand],
                    'DropPos': self.GetDropBasePos() } }
            lstReward.append(dReward)
        
        return lstReward


