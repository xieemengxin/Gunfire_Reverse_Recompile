# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_bullet.pyc
# RelativePath: clientlogic/cl_minigame/mg_bullet.pyc
# Source Generated with Decompyle++
# File: mg_bullet.pyc (Python 3.6)

from cl_only import ChooseKey, DeepCopy
from cl_commondefines import NWARRIOR_DROP_BULLET, VIRTUAL_ITEM_DROP, MG_BULLET
import cl_msgcenter
from .mobject import CDropGame, CBaseGameData

class CDropBulletGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_BULLET
    m_BulletBag = { }
    m_ChooseWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_BulletBag = cls.m_BulletBag
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropBulletGame

    GetGameClass = classmethod(GetGameClass)


class CDropBulletGame(CDropGame):
    m_BulletBag = { }
    
    def GetRewardInfo(self):
        iTime = self.Query('Times', 1)
        lstReward = []
        dData = {
            'ChooseWeight': self.m_ChooseWeight,
            'Source': self.m_Source,
            'BulletBag': self.m_BulletBag }
        oOwner = self.m_Game.GetObject(self.m_Owner)
        oPlayer = self.m_Game.GetObject(self.m_Player)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BULLETDROP, oOwner, dData)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BULLETDROP_PLAYER, oPlayer, dData)
        lstNoChoose = dData['NoChoose'] if 'NoChoose' in dData else []
        for _ in range(iTime):
            iLevel = ChooseKey(self.m_Game, dData['ChooseWeight'])
            dBullet = self.m_BulletBag[iLevel]
            dChooseReward = { }
            for iKey, iCnt in dBullet.items():
                if iKey not in lstNoChoose:
                    dChooseReward[iKey] = iCnt
            
            if dChooseReward:
                lstDropInfo = [
                    dChooseReward]
                vPos = self.GetDropBasePos()
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_BULLET,
                        'DropInfo': lstDropInfo,
                        'DropPos': vPos } }
                lstReward.append(dReward)
        
        return lstReward

    
    def GetChooseData(self):
        dData = {
            'ChooseWeight': self.m_ChooseWeight,
            'MiniGameType': self.m_Type,
            'ExtInfo': self.m_BulletBag }
        return dData


