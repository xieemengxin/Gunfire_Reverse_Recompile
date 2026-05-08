# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_cash.pyc
# RelativePath: clientlogic/cl_minigame/mg_cash.pyc
# Source Generated with Decompyle++
# File: mg_cash.pyc (Python 3.6)

from cl_commondefines import NWARRIOR_DROP_CASH, WARRIOR_MONSTER, MONSTER_TYPE_MASK, VIRTUAL_ITEM_DROP, WARRIOR_HERO, MG_CASH
from .mobject import CDropGame, CBaseGameData
import cl_msgcenter
import cl_formula

class CDropCashGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_CASH
    m_TypeBase = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_TypeBase = cls.m_TypeBase

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropCashGame

    GetGameClass = classmethod(GetGameClass)


class CDropCashGame(CDropGame):
    m_TypeBase = { }
    
    def GetRewardInfo(self):
        oGame = self.m_Game
        oOwner = oGame.GetObject(self.m_Owner)
        if oOwner.m_FightType & WARRIOR_MONSTER:
            iType = oOwner.m_FightType & MONSTER_TYPE_MASK
        else:
            iType = oOwner.m_FightType
        if iType not in self.m_TypeBase or not self.m_TypeBase[iType]:
            return []
        oPlayer = oGame.GetObject(self.m_Player)
        if not oPlayer or not (oPlayer.m_FightType & WARRIOR_HERO):
            return []
        self.m_Data['LogReward'] = 0
        iCash = self.m_TypeBase[iType]
        iTimes = self.Query('Times', 1)
        lstCash = [ cl_formula.GetResultByData(oOwner, iCash, { }) for _ in range(iTimes) ]
        dMsgInfo = {
            'CashList': lstCash }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BEFOREDROPCASH, oPlayer, dMsgInfo)
        if 'Reward' in dMsgInfo:
            return dMsgInfo['Reward']
        lstReward = []
        for iBase in lstCash:
            vPos = self.GetDropBasePos()
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_CASH,
                    'DropInfo': [
                        {
                            'Cash': iBase }],
                    'DropPos': vPos } }
            lstReward.append(dReward)
        
        return lstReward


