# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/seasonshopnpc.pyc
# RelativePath: clientlogic/cl_npc/seasonshopnpc.pyc
# Source Generated with Decompyle++
# File: seasonshopnpc.pyc (Python 3.6)

from cl_commondefines import SEASONSHOP_INITGOODSBEFORE
import cl_msgcenter
from . import mobject

class CSeasonShopNPC(mobject.CNPC):
    m_Season = 0
    m_RefreshKey = 'SeasonShopRefreshTimes'
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_GoodsData = { }
        self.m_FormulaLimit = { }
        self.m_RefreshTimes = { }

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        self.SetHeroInteractStatus(pid)
        self.InitHeroGoods(oHero)
        self.RefreshShopUI(oHero)

    
    def InitHeroGoods(self, oHero):
        if oHero.m_ID in self.m_GoodsData:
            return None
        if self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SEASONSHOP, oHero, {
            'ShopNpc': self.m_ID }, iSub = SEASONSHOP_INITGOODSBEFORE)
        self.InitGoodsInfo(oHero)

    
    def InitGoodsInfo(self, oHero):
        pass

    
    def CheckRefreshTimes(self, oHero, sKey):
        return False

    
    def RefreshShopUI(self, oHero):
        if self.CheckRefreshTimes(oHero, self.m_RefreshKey):
            self.SetNpcRefreshCallBackFunction(oHero)

    
    def Release(self):
        if self.m_ReleaseFlag:
            return None
        for dGoodsMenu in self.m_GoodsData.values():
            for oGoods in dGoodsMenu.values():
                oGoods.Disable()
            
        
        self.m_GoodsData = { }
        super().Release()

    
    def SetFormulaArgsLimit(self, dArgs):
        self.m_FormulaLimit = dArgs

    
    def CanBuy(self, oHero, oGoods):
        if not oGoods.CanBuy():
            return False
        if not (oGoods.m_CanBuy) or oGoods.m_HasBuy >= oGoods.m_CanBuy:
            return False
        if oGoods.IsHidden():
            return False
        if oHero.m_WarCash < oGoods.GetCash():
            return False
        return True

    
    def CanReplace(self, oGoods):
        if not oGoods.CanBuy():
            return False
        if not (oGoods.m_CanBuy) or oGoods.m_HasBuy >= oGoods.m_CanBuy:
            return False
        return True

    
    def SetRefreshTime(self, oHero, iPos, iMaxCount):
        iHero = oHero.m_ID
        if iHero not in self.m_RefreshTimes:
            self.m_RefreshTimes[iHero] = { }
        if iPos in self.m_RefreshTimes[iHero]:
            return None
        self.m_RefreshTimes[iHero][iPos] = {
            'MaxCount': iMaxCount,
            'NowCount': iMaxCount }

    
    def UpdateRefreshTimes(self, oHero, iPos, iNum):
        iHero = oHero.m_ID
        if iHero not in self.m_RefreshTimes:
            return False
        if iPos not in self.m_RefreshTimes[iHero]:
            return False
        dPosInfo = self.m_RefreshTimes[iHero][iPos]
        iMaxCount = dPosInfo['MaxCount']
        iNowCount = dPosInfo['NowCount']
        iResult = iNowCount + iNum
        if iResult > iMaxCount or iResult < 0:
            return False
        dPosInfo['NowCount'] = iResult
        return True

    
    def GetRefreshTimes(self, oHero, iPos):
        iHero = oHero.m_ID
        if iHero not in self.m_RefreshTimes:
            return (0, 0)
        if iPos not in self.m_RefreshTimes[iHero]:
            return (0, 0)
        dPosInfo = self.m_RefreshTimes[iHero][iPos]
        return (dPosInfo['NowCount'], dPosInfo['MaxCount'])


