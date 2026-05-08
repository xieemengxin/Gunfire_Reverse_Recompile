# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_trigger.pyc
# RelativePath: clientlogic/cl_minigame/mg_trigger.pyc
# Source Generated with Decompyle++
# File: mg_trigger.pyc (Python 3.6)

from cl_only import ChooseKey, DeepCopy
from cl_commondefines import NWARRIOR_DROP_TRIGGER, VIRTUAL_ITEM_DROP, MG_TRIGGER
from .mobject import CDropGame, CBaseGameData

class CDropTriggerGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_TRIGGER
    m_ChooseWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropTriggerGame

    GetGameClass = classmethod(GetGameClass)


class CDropTriggerGame(CDropGame):
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if not oOwner:
            return []
        iTime = self.Query('Times', 1)
        lstReward = []
        if not self.m_ChooseWeight:
            return []
        for _ in range(iTime):
            iPerform = ChooseKey(self.m_Game, self.m_ChooseWeight)
            dDropInfo = { }
            dDropInfo[iPerform] = 1
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_TRIGGER,
                    'DropInfo': [
                        dDropInfo],
                    'DropPos': self.GetDropBasePos() } }
            lstReward.append(dReward)
        
        return lstReward


