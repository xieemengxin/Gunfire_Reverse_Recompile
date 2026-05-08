# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_gscash.pyc
# RelativePath: clientlogic/cl_minigame/mg_gscash.pyc
# Source Generated with Decompyle++
# File: mg_gscash.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_DROP_GSCASH, WARRIOR_MONSTER, MONSTER_TYPE_MASK, VIRTUAL_ITEM_DROP, WARRIOR_HERO, MG_GSCASH
from .mobject import CDropGame, CBaseGameData

class CDropGSCashGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_GSCASH
    m_TypeBase = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_TypeBase = cls.m_TypeBase

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropGSCashGame

    GetGameClass = classmethod(GetGameClass)


class CDropGSCashGame(CDropGame):
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if oOwner.m_FightType & WARRIOR_MONSTER:
            iType = oOwner.m_FightType & MONSTER_TYPE_MASK
        else:
            iType = oOwner.m_FightType
        if iType not in self.m_TypeBase:
            return []
        iBase = self.m_TypeBase[iType]
        oPlayer = oGame.GetObject(self.m_Player)
        if not oPlayer or not (oPlayer.m_FightType & WARRIOR_HERO):
            return []
        dAllRatio = oPlayer.Query('ExtraGSCashDropRatio', { })
        iTotalRatio = 0
        for iFightType, iRatio in dAllRatio.items():
            if iFightType & iType == iFightType:
                iTotalRatio += iRatio
        
        iGSCash = iBase * (100 + iTotalRatio) // 100
        iTime = self.Query('Times', 1)
        lstReward = []
        for _ in range(iTime):
            vPos = self.GetDropBasePos()
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_GSCASH,
                    'DropInfo': [
                        {
                            'GSCash': iGSCash }],
                    'DropPos': vPos } }
            lstReward.append(dReward)
        
        return lstReward


