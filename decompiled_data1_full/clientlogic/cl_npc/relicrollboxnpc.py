# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/relicrollboxnpc.pyc
# RelativePath: clientlogic/cl_npc/relicrollboxnpc.pyc
# Source Generated with Decompyle++
# File: relicrollboxnpc.pyc (Python 3.6)

from cl_commondefines import LEVEL_TYPE_BOSS, PF_TYPE_RELIC, INTERACT_TYPE_FORBID, INTERACT_TYPE_ALLOW
from cl_cscommondef import QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL, QUALITY_TYPE_HIGH, QUALITY_TYPE_CURSE, BLANKRELIC
from cl_platformdata import GetSeasonSuitCls
from cl_object.logging import WarrelicLog
from . import magicbox
from . import net
import cl_msgcenter
import cl_notify
CHECK_FUSE_POINT = 2
FUSEREDUCE_NUM = 1
INITFUSE_TIMES = 1

class CRelicRollBoxNPC(magicbox.CBoxNPC):
    m_FusePointByType = {
        QUALITY_TYPE_HIGH: 3,
        QUALITY_TYPE_NORMAL: 2,
        QUALITY_TYPE_LOW: 1,
        BLANKRELIC: 1 }
    
    def __init__(self, *args):
        super(CRelicRollBoxNPC, self).__init__(*args)
        self.m_HeroFuseTimes = { }
        self.m_HeroCheckFusePoint = { }
        self.SetInitInteract(INTERACT_TYPE_FORBID)

    
    def OnGoto(self):
        super().OnGoto()
        oGame = self.m_Game
        oWarMgr = oGame.m_WarMgr
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        oScene = oGame.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return None
        oLevelNode = oLevelCtrl.GetLevelNode(oScene.m_Level)
        bBossLevel = False
        if oLevelNode and oLevelNode.m_LevelType == LEVEL_TYPE_BOSS:
            bBossLevel = True
        bFirstHall = False
        if oLevelCtrl.CheckFirstHall():
            bFirstHall = True
        for iPlayer in oWarMgr.GetAllPlayer():
            oHero = oWarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                continue
            iHero = oHero.m_ID
            self.m_HeroFuseTimes[iHero] = INITFUSE_TIMES
            self.SetPlayerInteractType(INTERACT_TYPE_ALLOW, [
                iPlayer])
            self.m_HeroCheckFusePoint[iHero] = CHECK_FUSE_POINT
            if bBossLevel:
                self.m_HeroFuseTimes[iHero] += oHero.QuerySavedData('save.BossFuseTimes', 0)
            if not bFirstHall:
                self.m_HeroFuseTimes[iHero] += oHero.QuerySavedData('save.ExtraFuseTimes', 0)
                self.m_HeroCheckFusePoint[iHero] -= oHero.QuerySavedData('save.ReduceFusePoint', 0)
        

    
    def ValidInteract(self, oHero):
        oRegroupRelicElement = self.m_Game.m_WarMgr.GetComponent('RegroupRelicElement')
        if not oRegroupRelicElement:
            return False
        return super(CRelicRollBoxNPC, self).ValidInteract(oHero)

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        self.SetHeroInteractStatus(oHero.m_PlayerID)
        self.SyncData(oHero)

    
    def SyncData(self, oHero):
        self.SyncHeroFuseTimes(oHero)
        if oHero.m_ID in self.m_HeroCheckFusePoint:
            net.GS2CCheckFusePoint(oHero, self.m_ID, self.m_HeroCheckFusePoint[oHero.m_ID])

    
    def SyncHeroFuseTimes(self, oHero):
        if oHero.m_ID in self.m_HeroFuseTimes:
            net.GS2CSyncFuseCount(oHero, self.m_ID, self.m_HeroFuseTimes[oHero.m_ID])

    
    def FuseBySubMode(self, oHero, lstMixRelic, iSuit):
        if not lstMixRelic:
            return None
        iHero = oHero.m_ID
        if iHero not in self.m_HeroFuseTimes or self.m_HeroFuseTimes[iHero] <= 0:
            return None
        clsSuit = GetSeasonSuitCls(iSuit)
        if not clsSuit:
            WarrelicLog.Alert('%d %d fuserelic no suit %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iSuit))
            return None
        self.FuseSuitCondiReduce(oHero, clsSuit, lstMixRelic)

    
    def FuseSuitCondiReduce(self, oHero, clsSuit, lstMixRelic):
        oSuitElement = self.m_Game.m_WarMgr.GetSeasonSuitElement()
        if not oSuitElement:
            return None
        iSuit = clsSuit.m_SID
        if not oSuitElement.CheckCondiReduce(oHero.m_ID, iSuit):
            WarrelicLog.Alert('%d %d fuse reduceerr %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iSuit))
            return None
        oRelicCon = oHero.m_RelicCon
        if not self.CheckFusePointAndReturnBlankRelic(oHero, oRelicCon, lstMixRelic):
            return None
        WarrelicLog.Debug('%d %d fusesuit %s choose: %s' % (self.m_Game.m_ID, oHero.m_PlayerID, clsSuit.m_SID, lstMixRelic))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_FUSEDRELIC, oHero, {
            'SeasonSuit': iSuit,
            'CostRelic': lstMixRelic })
        sReason = 'FuseSuitCondiReduce'
        self.FuseCost(oHero, oRelicCon, lstMixRelic, sReason)
        oSuitElement.SuitCondiReduce(oHero, clsSuit, FUSEREDUCE_NUM, sReason)
        cl_notify.SendCommonNotify(self.m_Game, {
            oHero.m_PlayerID: 1 }, 9659, { })

    
    def CheckFusePointAndReturnBlankRelic(self, oHero, oRelicCon, lstMixRelic):
        iPointResult = 0
        for iMixSID in lstMixRelic:
            if iMixSID == BLANKRELIC:
                iPointResult += self.m_FusePointByType[BLANKRELIC]
                continue
            oPerform = oHero.m_RelicCon.GetRelicByMixSID(iMixSID)
            if not oPerform or oPerform.m_PFType != PF_TYPE_RELIC:
                continue
            iQuality = oPerform.m_Quality
            if iQuality == QUALITY_TYPE_CURSE:
                WarrelicLog.Alert('%d %d fuserelic input curse relic %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iMixSID))
                return False
            if iQuality in self.m_FusePointByType:
                iPointResult += self.m_FusePointByType[iQuality]
        
        if oHero.m_ID not in self.m_HeroCheckFusePoint:
            return False
        iCheckFusePoint = self.m_HeroCheckFusePoint[oHero.m_ID]
        if iPointResult < iCheckFusePoint:
            WarrelicLog.Alert('%d %d fuserelic point require %s but %s' % (self.m_Game.m_ID, oHero.m_PlayerID, iCheckFusePoint, iPointResult))
            return False
        if iPointResult > iCheckFusePoint:
            iReturnNum = iPointResult - iCheckFusePoint
            oRelicCon.ChangeBlankRelicNum(iReturnNum, 'FusePointReturn')
        return True

    
    def FuseCost(self, oHero, oRelicCon, lstCostRelic, sFuseReason):
        iHero = oHero.m_ID
        self.m_HeroFuseTimes[iHero] -= 1
        self.SyncHeroFuseTimes(oHero)
        for iCostRelic in lstCostRelic:
            oRelicCon.RemoveRelicByMixSID(iCostRelic, sFuseReason, iForce = 1)
        

    
    def AddFuseTimes(self, oHero, iTimes):
        dData = self.m_HeroFuseTimes
        iHero = oHero.m_ID
        if iHero not in dData:
            dData[iHero] = iTimes
        else:
            dData[iHero] += iTimes
        if dData[iHero] > 0:
            self.SetPlayerInteractType(INTERACT_TYPE_ALLOW, [
                oHero.m_PlayerID])


