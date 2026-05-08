# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_rareitem.pyc
# RelativePath: clientlogic/cl_minigame/mg_rareitem.pyc
# Source Generated with Decompyle++
# File: mg_rareitem.pyc (Python 3.6)

from cl_only import DeepCopy, ChooseKey
from cl_commondefines import VIRTUAL_ITEM_DROP, NWARRIOR_DROP_RAREITEM, MG_RAREITEM
from cl_platformdata import GetRareItmeLimitPlayType
from .mobject import CDropGame, CBaseGameData
import cl_item

class CDropRareItemGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_RAREITEM
    m_ChooseWeight = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = DeepCopy(cls.m_ChooseWeight)

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropRareItemGame

    GetGameClass = classmethod(GetGameClass)


class CDropRareItemGame(CDropGame):
    
    def GetRewardInfo(self):
        lstReward = []
        dChooseWeight = { }
        iTime = self.Query('Times', 1)
        oWarMgr = self.m_Game.GetWarMgr()
        dExcludeRareItem = self.Query('ExcludeRareItem', { })
        dRareItmeLimit = GetRareItmeLimitPlayType(oWarMgr.GetPlayType())
        for iRareItem in dExcludeRareItem:
            self.m_ChooseWeight.pop(iRareItem, 0)
        
        for iRareItem, iWeight in self.m_ChooseWeight.items():
            if iRareItem not in dRareItmeLimit:
                continue
            dChooseWeight[iRareItem] = iWeight
        
        for _ in range(iTime):
            iRareItem = ChooseKey(self.m_Game, dChooseWeight)
            vPos = self.GetDropBasePos()
            oItem = cl_item.CreateRareItem(self.m_Game, iRareItem)
            if not oItem:
                continue
            lstDropInfo = [
                oItem]
            dReward = {
                'item': VIRTUAL_ITEM_DROP,
                'info': {
                    'DropType': NWARRIOR_DROP_RAREITEM,
                    'DropInfo': lstDropInfo,
                    'DropPos': vPos } }
            lstReward.append(dReward)
        
        return lstReward


