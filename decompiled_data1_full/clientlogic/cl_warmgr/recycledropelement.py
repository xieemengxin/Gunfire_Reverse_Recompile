# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/recycledropelement.pyc
# RelativePath: clientlogic/cl_warmgr/recycledropelement.pyc
# Source Generated with Decompyle++
# File: recycledropelement.pyc (Python 3.6)

from cl_commondefines import PF_TYPE_RELIC, NWARRIOR_DROP_RELIC, NWARRIOR_DROP_EQUIP, FORBID_RECYCLE, PLAYMODE_SURVIVOR, PLAYMODE_ROGUELIKE, PLAYMODE_DAYLY_TRIAL, RECYCLE_RELIC, RECYCLE_DROP, RECYCLE_UNDROP, NWARRIOR_DROP_RELIC_CURSE, RECYCLE_EXTEND_RELIC, NWARRIOR_DROP_RELIC_MYSTERY, CURRENCY_CASH
from cl_cscommondef.cs_itemdef import QUALITY_FACTOR
from cl_warmgr.mobject import CBaseElement
from cl_object.logging import WarrewardLog
import cl_msgcenter
import cl_formula
import cl_perform
import cl_snetwar
RECYCLE_TYPE_ACTIVE = 0
RECYCLE_TYPE_AUTO = 1
NOTGETSID_FIGHTTYPE = (NWARRIOR_DROP_RELIC,)

class CRecycleDropElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CRecycleDropElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_CustomRecycleRule = { }

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnPlayerMapLoadOK, 'RecycleDropInit')
        cl_msgcenter.AddFunction(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.OnLevelNodeFinish, 'RecycleDropLevelFinish', -1, 0)

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_ID, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, 'RecycleDropInit')
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'RecycleDropLevelFinish')
        self.m_WarMgr = None
        self.m_CustomRecycleRule = { }
        super(CRecycleDropElement, self).Release()

    
    def OnPlayerMapLoadOK(self, oListener, oHero, dInfo):
        self.RefreshRecycleDropInfo(oHero)

    
    def RefreshRecycleDropInfo(self, oHero):
        dPrice = oHero.Query('RecycleDropPrice', { })
        if not dPrice:
            return None
        lstDropType = dPrice.keys()
        cl_snetwar.GS2CRecycleDropInfo(oHero, lstDropType)

    
    def OnLevelNodeFinish(self, oWarMgr, dInfo):
        if oWarMgr.m_PlayMode not in (PLAYMODE_ROGUELIKE, PLAYMODE_DAYLY_TRIAL):
            return None
        oGame = self.m_Game
        oLevelCtrl = oWarMgr.GetComponent('LevelCtrl')
        for oNode in oLevelCtrl.m_LevelNodeLib.values():
            iScene = oNode.m_Scene
            oScene = oGame.m_SceneMgr.GetScene(iScene)
            if not oScene:
                return None
            lstDrop = oScene.GetObjectsByType('Drop')
            for iHero in oWarMgr.GetAllHero():
                oHero = self.m_Game.GetObject(iHero)
                if not oHero:
                    continue
                for iDrop in lstDrop:
                    oDrop = oGame.GetObject(iDrop)
                    if not oDrop:
                        continue
                    iDropType = oDrop.m_FightType
                    if iDropType in self.m_CustomRecycleRule:
                        func = self.m_CustomRecycleRule[iDropType]
                        func(oWarMgr, oHero, oDrop, 'AutoRecycleDrop')
                        continue
                    self.RecycleDrop(oHero, iDrop, RECYCLE_TYPE_AUTO)
                
            
        

    
    def RecycleDrop(self, oHero, iDrop, iType = RECYCLE_TYPE_ACTIVE):
        iResult = self.ValidRecycle(oHero, iDrop, iType)
        iPrice = self.CalDropPrice(oHero, iDrop, iResult)
        if iResult:
            oDrop = self.m_Game.GetObject(iDrop)
            iFightType = oDrop.m_FightType
            if iFightType in NOTGETSID_FIGHTTYPE:
                iDropSID = oDrop.m_DropInfo[0]
            else:
                iDropSID = oDrop.m_SID
            WarrewardLog.Debug(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} recycledrop {iDropSID} {iPrice} {iType}''')
            oDrop.SetReleaseFlag(1)
            iPrice = oHero.AddCash(iPrice, 'RecycleDrop')
            dMsgInfo = {
                'RecycleDrop': iDrop,
                'Cash': iPrice,
                'RecycleDropType': iFightType,
                'RecycleType': RECYCLE_DROP }
            if iFightType in (NWARRIOR_DROP_RELIC, NWARRIOR_DROP_RELIC_MYSTERY):
                dMsgInfo['Relic'] = oDrop.m_DropInfo[0]
                dMsgInfo['RecycleDropType'] = NWARRIOR_DROP_RELIC
                if iType == RECYCLE_TYPE_AUTO:
                    dMsgInfo['AutoRecycle'] = 1
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEDROP, oHero, dMsgInfo, iSub = RECYCLE_DROP)
        if iType == RECYCLE_TYPE_ACTIVE:
            cl_snetwar.GS2CRecycleDropResult(self.m_Game, iDrop, oHero.m_ID, iResult, CURRENCY_CASH, iPrice, self.m_Game.GetRealPlayers())
        if iResult:
            self.RemoveDrop(iDrop)

    
    def RecycleUnDrop(self, oHero, iRecycleType, iSID):
        iResult = self.ValidRecycleUnDrop(oHero, iRecycleType, iSID)
        if iResult:
            iPrice = self.CalUnDropPrice(oHero, iRecycleType, iSID)
            WarrewardLog.Info(f'''{self.m_Game.m_ID} {oHero.m_PlayerID} recyclerelic {iSID} {iPrice}''')
            oRelicCon = oHero.m_RelicCon
            if iRecycleType == RECYCLE_RELIC:
                oRelicCon.RemoveRelic(iSID, 'RecycleUnDropRelic', 1)
            else:
                oRelicCon.RemoveExtendRelic(iSID, 'RecycleUnDropRelic')
            iPrice = oHero.AddCash(iPrice, 'RecycleDrop')
            dMsgInfo = {
                'Cash': iPrice,
                'RecycleDropType': NWARRIOR_DROP_RELIC,
                'Relic': iSID,
                'RecycleType': RECYCLE_UNDROP }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RECYCLEDROP, oHero, dMsgInfo, iSub = RECYCLE_UNDROP)
            cl_snetwar.GS2CRecycleDropResult(self.m_Game, 0, oHero.m_ID, iResult, CURRENCY_CASH, iPrice, {
                oHero.m_PlayerID: 1 })

    
    def ValidRecycleUnDrop(self, oHero, iRecycleType, iSID):
        if iRecycleType == RECYCLE_RELIC:
            return self.ValidRecycleRelic(oHero, iSID)
        if iRecycleType == RECYCLE_EXTEND_RELIC:
            return self.ValidRecycleExtendRelic(oHero, iSID)
        return 0

    
    def ValidRecycleRelic(self, oHero, iSID):
        oPerform = oHero.m_RelicCon.GetPerform(iSID)
        if not oPerform:
            return 0
        if oPerform.m_PFType != PF_TYPE_RELIC:
            return 0
        if not oPerform.ValidRemove():
            return 0
        dPrice = oHero.Query('RecycleDropPrice', { })
        if NWARRIOR_DROP_RELIC not in dPrice:
            return 0
        if oPerform.m_Source != oHero.m_PlayerID and self.m_WarMgr.Query('RecycleSelf', 1):
            return 0
        return 1

    
    def ValidRecycleExtendRelic(self, oHero, iSID):
        oPerform = oHero.m_RelicCon.GetExtendRelic(iSID)
        if not oPerform:
            return 0
        dPrice = oHero.Query('RecycleDropPrice', { })
        if NWARRIOR_DROP_RELIC not in dPrice:
            return 0
        if oPerform.m_Source != oHero.m_PlayerID and self.m_WarMgr.Query('RecycleSelf', 1):
            return 0
        return 1

    
    def CalUnDropPrice(self, oHero, iRecycleType, iPerformSID):
        iPrice = 0
        dPrice = oHero.Query('RecycleDropPrice', { })
        if iRecycleType in (RECYCLE_RELIC, RECYCLE_EXTEND_RELIC):
            iPrice = self.CalRelicPrice(oHero, iPerformSID, dPrice[NWARRIOR_DROP_RELIC][0])
        else:
            WarrewardLog.Alert('%s %s recycletype %s %s err' % (oHero.m_Game.m_ID, oHero.m_ID, iRecycleType, iPerformSID))
        return iPrice

    
    def CalRelicPrice(self, oHero, iPerformSID, iPrice):
        clsPerform = cl_perform.GetPerformModule(iPerformSID)
        if not clsPerform:
            return 0
        iQuality = clsPerform.m_Quality
        return cl_formula.GetResultByData(oHero, iPrice, {
            'QualityCoff': QUALITY_FACTOR[iQuality],
            'RelicSID': iPerformSID })

    
    def CalDropPrice(self, oHero, iDrop, iResult):
        iPrice = 0
        if iResult:
            dArgs = { }
            oDrop = self.m_Game.GetObject(iDrop)
            dPrice = oHero.Query('RecycleDropPrice')
            iPrice = dPrice[oDrop.m_FightType][0]
            if self.m_WarMgr.m_PlayMode == PLAYMODE_SURVIVOR:
                if oDrop.m_FightType == NWARRIOR_DROP_EQUIP:
                    oEquip = oDrop.m_DropInfo[0]
                    oDrop.Set('SurvivorPhase', oEquip.Query('SurvivorPhase'))
                dArgs['Drop'] = iDrop
            if oDrop.m_FightType == NWARRIOR_DROP_RELIC:
                iPerformSID = oDrop.m_DropInfo[0]
                return self.CalRelicPrice(oHero, iPerformSID, iPrice)
            iPrice = cl_formula.GetResultByData(oHero, iPrice, dArgs)
        return iPrice

    
    def ValidRecycle(self, oHero, iDrop, iType):
        oDrop = self.m_Game.GetObject(iDrop)
        if not oDrop:
            return 0
        iHero = oHero.m_ID
        dPrice = oHero.Query('RecycleDropPrice', { })
        if not dPrice:
            return 0
        if oDrop.m_FightType not in dPrice:
            return 0
        if oDrop.m_FightType == NWARRIOR_DROP_EQUIP:
            oWeapon = oDrop.m_DropInfo[0]
            if oWeapon.Query('UnWarWeapon', 0):
                return 0
            if oHero.IsForbid(FORBID_RECYCLE):
                return 0
            if oWeapon.Query('InjectOwner', 0):
                return 0
        if oDrop.m_FightType == NWARRIOR_DROP_RELIC or self.m_WarMgr.IsAIHero(iHero):
            return 0
        if oDrop.m_FightType == NWARRIOR_DROP_RELIC_CURSE:
            WarrewardLog.Alert('%s recycle curserelic %s' % (self.m_Game, oDrop))
            return 0
        if oDrop.m_Owner and oDrop.m_Owner != iHero:
            return 0
        if oDrop.m_Pick and oDrop.m_Pick != iHero:
            return 0
        if iType == RECYCLE_TYPE_ACTIVE and oDrop.m_Scene != oHero.m_Scene:
            return 0
        if oDrop.m_Source != oHero.m_PlayerID and self.m_WarMgr.Query('RecycleSelf', 1):
            return 0
        if oDrop.m_ReleaseFlag:
            return 0
        if oHero.IsDead():
            return 0
        return 1

    
    def RemoveDrop(self, iDrop):
        oDrop = self.m_Game.GetObject(iDrop)
        if not oDrop:
            return None
        oDrop.SetReleaseFlag(0)
        oDrop.Remove('RecycleDrop')

    
    def AddCustomRecycleRule(self, iType, func):
        if iType in self.m_CustomRecycleRule:
            return None
        self.m_CustomRecycleRule[iType] = func



def GetComponentClass(oMgrManager):
    return CRecycleDropElement

