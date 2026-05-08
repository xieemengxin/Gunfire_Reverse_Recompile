# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_diceselection.pyc
# RelativePath: clientlogic/cl_minigame/mg_diceselection.pyc
# Source Generated with Decompyle++
# File: mg_diceselection.pyc (Python 3.6)

from cl_commondefines import MG_DICESELECT, VIRTUAL_ITEM_DROP, NWARRIOR_DROP_DICESELECTIONPACKET
from .mobject import CDropGame, CBaseGameData

class CDiceSelectionGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_DICESELECT
    m_LayerMaxDropNum = 0
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_LayerMaxDropNum = cls.m_LayerMaxDropNum

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDiceSelectionGame

    GetGameClass = classmethod(GetGameClass)


class CDiceSelectionGame(CDropGame):
    m_LayerMaxDropNum = 0
    
    def GetRewardInfo(self):
        lstReward = []
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oDiceElement = oWarMgr.GetDiceElement()
        if not oDiceElement:
            return lstReward
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        iCurLayer = oLevelCtrl.m_LayerNum
        if not oDiceElement.CheckPacketValidDrop(iCurLayer, self.m_LayerMaxDropNum):
            return lstReward
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return lstReward
        oTarget = oGame.GetObject(self.m_Player)
        if not oTarget:
            return lstReward
        dLayerDropInfo = oDiceElement.GetPacketChallengeDropInfo()
        if not dLayerDropInfo:
            return lstReward
        oDiceElement.AddPacketDropTimes(iCurLayer)
        iPacketLayer = min(iCurLayer, max(dLayerDropInfo))
        iQuality = dLayerDropInfo[iPacketLayer]
        iDrop = oDiceElement.GetSelectionPacketDrop(iQuality)
        iTime = self.Query('Times', 1)
        for _ in range(iTime):
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_DICESELECTIONPACKET,
                    'DropInfo': [
                        {
                            'SID': iDrop,
                            'Quality': iQuality }],
                    'DropPos': self.GetDropBasePos() } }
            lstReward.append(dReward)
        
        return lstReward


