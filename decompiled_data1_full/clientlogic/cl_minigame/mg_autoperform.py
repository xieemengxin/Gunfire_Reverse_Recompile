# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_autoperform.pyc
# RelativePath: clientlogic/cl_minigame/mg_autoperform.pyc
# Source Generated with Decompyle++
# File: mg_autoperform.pyc (Python 3.6)

from cl_only import ChooseKey, DeepCopy
from cl_commondefines import VIRTUAL_ITEM_AUTOPERFORM, MG_AUTOPERFORM
from .mobject import CDropGame, CBaseGameData

class CAutoPerformGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_AUTOPERFORM
    m_ChooseWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CAutoPerformGame

    GetGameClass = classmethod(GetGameClass)


class CAutoPerformGame(CDropGame):
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return []
        iTime = self.Query('Times', 1)
        lstReward = []
        for _ in range(iTime):
            iPerform = ChooseKey(self.m_Game, self.m_ChooseWeight)
            dReward = {
                'item': VIRTUAL_ITEM_AUTOPERFORM,
                'info': {
                    'sid': iPerform,
                    'data': {
                        'vStart': oOwner.GetPos() } } }
            lstReward.append(dReward)
        
        return lstReward


