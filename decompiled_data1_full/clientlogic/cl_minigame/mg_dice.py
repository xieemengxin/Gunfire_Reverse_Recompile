# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_dice.pyc
# RelativePath: clientlogic/cl_minigame/mg_dice.pyc
# Source Generated with Decompyle++
# File: mg_dice.pyc (Python 3.6)

from cl_commondefines import MG_DICE, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_DICE
from cl_only import ChooseKey, DeepCopy
from .mobject import CDropGame, CBaseGameData
from cl_platformdata import GetExcludeDiceQuality
from cl_object.logging import DiceLog
import cl_dice
import cl_perform

class CDiceGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_DICE
    m_ChooseQualityWeight = { }
    m_ChoosePutOutPoolWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseQualityWeight = DeepCopy(cls.m_ChooseQualityWeight)
        oMiniGame.m_ChoosePutOutPoolWeight = DeepCopy(cls.m_ChoosePutOutPoolWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDiceGame

    GetGameClass = classmethod(GetGameClass)


class CDiceGame(CDropGame):
    m_ChooseQualityWeight = { }
    m_ChoosePutOutPoolWeight = { }
    
    def GetRewardInfo(self):
        lstReward = []
        oGame = self.m_Game
        oTarget = oGame.GetObject(self.m_Player)
        if not oTarget:
            DiceLog.Debug('%s %s dicegame targeterr' % (oGame.m_ID, self.m_Player))
            return lstReward
        oWarMgr = oGame.m_WarMgr
        oDiceElement = oWarMgr.GetDiceElement()
        if not oDiceElement:
            DiceLog.Debug('%s %s dicegame elementerr' % (oGame.m_ID, oTarget.m_PlayerID))
            return lstReward
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iMaxLayer = max(self.m_ChooseQualityWeight)
        iLayer = min(iMaxLayer, oLevelCtrl.m_LayerNum)
        dDiceQuality = self.m_ChooseQualityWeight[iLayer]
        iDiceQuality = ChooseKey(oGame, dDiceQuality)
        if not iDiceQuality:
            DiceLog.Debug('%s %s dicegame chooseerr %s %s' % (oGame.m_ID, oTarget.m_PlayerID, iLayer, self.m_ChooseQualityWeight))
            return lstReward
        dAllDice = oDiceElement.GetAllUnLockDice(oTarget.m_PlayerID)
        dChooseWeight = { }
        for iDice in dAllDice:
            if iDice in GetExcludeDiceQuality(iDiceQuality):
                continue
            clsPerform = cl_perform.GetPerformModule(iDice)
            if not clsPerform:
                continue
            iPutOutPoolType = clsPerform.m_PutOutPoolType
            if iPutOutPoolType not in dChooseWeight:
                dChooseWeight[iPutOutPoolType] = {
                    iDice: 1 }
                continue
            dChooseWeight[iPutOutPoolType][iDice] = 1
        
        if not dChooseWeight:
            DiceLog.Debug('%s %s dicegame chooseerr %s' % (oGame.m_ID, oTarget.m_PlayerID, dAllDice))
            return lstReward
        dDicePoolTypeWeight = { }
        for iDicePoolType, iWeight in self.m_ChoosePutOutPoolWeight.items():
            if iDicePoolType in dChooseWeight:
                dDicePoolTypeWeight[iDicePoolType] = iWeight
        
        if not dDicePoolTypeWeight:
            return lstReward
        iTimes = self.Query('Times', 1)
        tPos = self.GetDropBasePos()
        for _ in range(iTimes):
            iDicePoolType = ChooseKey(oGame, dDicePoolTypeWeight)
            dChooseWeightByPoolType = dChooseWeight.get(iDicePoolType, { })
            if not dChooseWeightByPoolType:
                DiceLog.Debug('%s %s dicegame pooltypeerr %s %s' % (oGame.m_ID, oTarget.m_PlayerID, iDicePoolType, dChooseWeight))
                continue
            iDice = ChooseKey(oGame, dChooseWeightByPoolType)
            dDiceInfo = {
                'SID': iDice,
                'QL': iDiceQuality,
                'PR': oDiceElement.GetTempPointRangeByQuality(iDiceQuality) }
            oDice = cl_dice.CreateDice(oGame, oDiceCon = None, dDiceInfo = dDiceInfo)
            if not oDice:
                DiceLog.Debug('%s %s dicegame diceerr %s' % (oGame.m_ID, oTarget.m_PlayerID, iDice))
                continue
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_DICE,
                    'DropInfo': [
                        oDice],
                    'DropPos': tPos } }
            lstReward.append(dReward)
        
        return lstReward


