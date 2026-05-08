# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/lockedboxnpc.pyc
# RelativePath: clientlogic/cl_npc/lockedboxnpc.pyc
# Source Generated with Decompyle++
# File: lockedboxnpc.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_ITEM_WARCASH, VIRTUAL_ITEM_BULLET, VIRTUAL_ITEM_KEYITEM, VIRTUAL_ITEM_KEY, INTERACT_TYPE_ALLOW
import cl_formula
import cl_notify
import cl_npc.net
from . import magicbox

class CLockedBoxNpc(magicbox.CBoxNPC):
    
    def __init__(self, *args):
        super(CLockedBoxNpc, self).__init__(*args)
        self.SetInitInteract(INTERACT_TYPE_ALLOW)
        self.m_OpenCost = { }

    
    def NetAddTo(self, dPlayer):
        super(CLockedBoxNpc, self).NetAddTo(dPlayer)
        for pid in dPlayer:
            oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
            cl_npc.net.GS2CNpcOpenCost(oHero, self, self.m_OpenCost)
        

    
    def ValidInteract(self, oHero):
        if not self.CheckValidCost(oHero, self.m_OpenCost):
            return False
        return super(CLockedBoxNpc, self).ValidInteract(oHero)

    
    def OnInteract(self, oHero):
        self.CostItem(oHero)
        self.BoxModelOpen(oHero.m_PlayerID)

    
    def SetOpenCost(self, dCost, iReset):
        for _, dInfo in dCost.items():
            for iSID, tCost in dInfo.items():
                iCost = cl_formula.GetFormulaResult(self, tCost)
                dInfo[iSID] = iCost
            
        
        if iReset:
            self.m_OpenCost = dCost
        else:
            self.m_OpenCost.update(dCost)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return None
        for pid in oScene.GetPlayers():
            oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(pid)
            cl_npc.net.GS2CNpcOpenCost(oHero, self, self.m_OpenCost)
        

    
    def CheckValidCost(self, oHero, dOpenCost):
        for iType, dInfo in dOpenCost.items():
            if not iType == VIRTUAL_ITEM_KEY or oHero.ValidCostKey(dInfo):
                return False
            if iType == VIRTUAL_ITEM_KEYITEM:
                for iSid, iCost in dInfo.items():
                    if oHero.m_ItemCon.GetItemAmountBySID(iSid) < iCost:
                        return False
                
            if iType == VIRTUAL_ITEM_BULLET:
                for iSid, iCost in dInfo.items():
                    if oHero.m_BulletCon.Bullet(iSid) < iCost:
                        return False
                
            if iType == VIRTUAL_ITEM_WARCASH:
                for iSid, iCost in dInfo.items():
                    if oHero.m_WarCash < iCost:
                        return False
                
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, '未识别的消耗类型%s' % iType)
        
        return True

    
    def CostItem(self, oHero):
        for iType, dInfo in self.m_OpenCost.items():
            if iType == VIRTUAL_ITEM_KEY:
                oHero.CostKey(dInfo, 'NPC')
                continue
            if iType == VIRTUAL_ITEM_KEYITEM:
                for iSID, iCnt in dInfo.items():
                    oHero.m_ItemCon.SubItemAmountBySID(iSID, iCnt, 'NPC')
                
            if iType == VIRTUAL_ITEM_BULLET:
                for iSid, iCost in dInfo.items():
                    oHero.m_BulletCon.BulletModify(iSid, -iCost, 'LockedBox')
                
            if iType == VIRTUAL_ITEM_WARCASH:
                for iSid, iCost in dInfo.items():
                    oHero.AddCash(-iCost, 'lockbox-%d' % self.m_SID)
                
        


