# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_key.pyc
# RelativePath: clientlogic/cl_minigame/mg_key.pyc
# Source Generated with Decompyle++
# File: mg_key.pyc (Python 3.6)

from cl_only import CopyDict, DeepCopy
from cl_commondefines import NWARRIOR_DROP_KEY, VIRTUAL_ITEM_DROP, MG_KEY
from .mobject import CDropGame, CBaseGameData

class CDropKeyGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_KEY
    m_ChooseWeight = { }
    m_KeyBag = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_KeyBag = cls.m_KeyBag
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropKeyGame

    GetGameClass = classmethod(GetGameClass)


class CDropKeyGame(CDropGame):
    
    def GetRewardInfo(self):
        iTime = self.Query('Times', 1)
        lstReward = []
        for _ in range(iTime):
            lstDropInfo = [
                CopyDict(self.m_KeyBag)]
            vPos = self.GetDropBasePos()
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_KEY,
                    'DropInfo': lstDropInfo,
                    'DropPos': vPos } }
            lstReward.append(dReward)
        
        return lstReward


