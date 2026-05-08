# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/mg_keyitem.pyc
# RelativePath: clientlogic/cl_minigame/mg_keyitem.pyc
# Source Generated with Decompyle++
# File: mg_keyitem.pyc (Python 3.6)

from cl_only import ChooseKey
from cl_commondefines import NWARRIOR_DROP_KEYITEM, VIRTUAL_ITEM_DROP, MG_KEYITEM
from .mobject import CDropGame, CBaseGameData
import cl_item

class CDropKeyItemGameData(CBaseGameData):
    m_SID = 0
    m_Type = MG_KEYITEM
    m_ChooseWeight = { }
    m_Item = { }
    
    def InitMiniGame(cls, oMiniGame):
        oMiniGame.m_ChooseWeight = cls.m_ChooseWeight
        oMiniGame.m_Item = cls.m_Item

    InitMiniGame = classmethod(InitMiniGame)
    
    def GetGameClass(cls):
        return CDropKeyItemGame

    GetGameClass = classmethod(GetGameClass)


class CDropKeyItemGame(CDropGame):
    
    def OnInit(self):
        super().OnInit()
        self.Set('DropOwner', 0)

    
    def GetRewardInfo(self):
        iTime = self.Query('Times', 1)
        lstReward = []
        for _ in range(iTime):
            iGroup = ChooseKey(self.m_Game, self.m_ChooseWeight)
            if iGroup not in self.m_Item:
                continue
            for iItemSID, iAmount in self.m_Item[iGroup].items():
                oItem = cl_item.GetTemp(iItemSID)
                if not oItem:
                    continue
                oItem.AddAmount(iAmount, 'DropGame')
                lstDropInfo = [
                    oItem]
                vPos = self.GetDropBasePos()
                dReward = {
                    'item': VIRTUAL_ITEM_DROP,
                    'info': {
                        'DropType': NWARRIOR_DROP_KEYITEM,
                        'DropInfo': lstDropInfo,
                        'DropPos': vPos } }
                lstReward.append(dReward)
            
        
        return lstReward


