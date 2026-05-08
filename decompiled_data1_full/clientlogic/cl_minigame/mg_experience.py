# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_experience.pyc
# RelativePath: clientlogic/cl_minigame/mg_experience.pyc
# Source Generated with Decompyle++
# File: mg_experience.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_DROP, NWARRIOR_DROP_EXPERIENCE, MG_EXPERIENCE
from .mobject import CDropGame, CBaseGameData

class CDropExperienceGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_EXPERIENCE
    m_ExperienceValue = 0
    m_DropModel = 0
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ExperienceValue = cls.m_ExperienceValue
        oMiniGame.m_DropModel = cls.m_DropModel

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropExperienceGame

    GetGameClass = classmethod(GetGameClass)


class CDropExperienceGame(CDropGame):
    
    def OnInit(self):
        super().OnInit()
        self.Set('DropOwner', 0)

    
    def GetRewardInfo(self):
        iTime = self.Query('Times', 1)
        lstReward = []
        vPos = self.GetDropBasePos()
        for _ in range(iTime):
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_EXPERIENCE,
                    'DropInfo': [
                        {
                            'Experience': int(self.m_ExperienceValue),
                            'DropModel': self.m_DropModel }],
                    'DropPos': vPos } }
            lstReward.append(dReward)
        
        return lstReward


