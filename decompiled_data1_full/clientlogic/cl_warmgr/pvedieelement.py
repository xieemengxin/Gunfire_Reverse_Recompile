# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/pvedieelement.pyc
# RelativePath: clientlogic/cl_warmgr/pvedieelement.pyc
# Source Generated with Decompyle++
# File: pvedieelement.pyc (Python 3.6)

from cl_only import Functor, Time2Frame, DeepCopy, ShufferList
from cl_commondefines import WARRIOR_HERO, WARRIOR_MONSTER, WARRIOR_BOSS, BOSS_DONOT_COUNT, TYPE_RELIFE_RELIC, TYPE_RELIFE_GSCASH, TYPE_RELIFE_PASS, TYPE_RELIFE_KILLBOSS, TYPE_RELIFE_PASSIVE, LEVEL_TYPE_HIDE, DEAD_REAL_DELAYTIME, WARRIOR_SERVANT, WARRIOR_PET, WARRIOR_MECH, WARRIOR_PLANT, TYPE_RELIFE_DICE, WARRIOR_PET_HEROSIDE
from cl_warmgr.mobject import CBaseElement
from cl_wardata.relifeinfo import GetRelifeInfo
from cl_object.logging import WarobjLog
import cl_msgcenter
import cl_snetwar
import cl_formula
import cl_math

class CPVEDieElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CPVEDieElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_CallFlag = 'WarMgr.PVEDieElement'
        self.m_RelifeIdx = 0
        self.m_RelifeData = self.m_Data.m_Config.get('RelifeData', 1001)
        self.m_InitDyingSecond = self.m_Data.m_Config.get('InitDyingSecond', 20)
        self.m_MinDyingSecond = self.m_Data.m_Config.get('MinDyingSecond', 5)
        self.m_TimesSubSecond = 2
        self.m_SavedData = { }
        self.m_HallRelife = []
        self.m_OpenRescue = 1
        self.m_OpenRescueSource = {
            'InitOpen': 1 }
        self.m_Relifed = { }
        self.InitTimeSubSecond()

    
    def Init(self):
        self.AddAttention()

    
    def InitTimeSubSecond(self):
        iRound = self.m_WarMgr.m_Round
        iCycle = self.m_WarMgr.m_Cycle
        dTimesSubSecond = self.m_Data.m_Config.get('TimesSubSecond', {
            (0, 0): 2 })
        if (iRound, iCycle) in dTimesSubSecond:
            self.m_TimesSubSecond = dTimesSubSecond[(iRound, iCycle)]
        elif (0, 0) in dTimesSubSecond:
            self.m_TimesSubSecond = dTimesSubSecond[(0, 0)]
        else:
            WarobjLog.Error('pvedieelement timessubsecond setting err')

    
    def Release(self):
        oWarMgr = self.m_WarMgr
        oGame = self.m_Game
        oGame.DoneGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, 'PlayerReady' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, 'AddAllPlayer' + self.m_CallFlag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'NodeGoalOK' + self.m_CallFlag)
        self.m_WarMgr = None
        self.Remove_Call_Out('RelifeDelayCall')
        self.m_SavedData = { }
        super(CPVEDieElement, self).Release()

    
    def AddAttention(self):
        oWarMgr = self.m_WarMgr
        oGame = self.m_Game
        oGame.AddGlobalAttention(oWarMgr.m_ID, cl_msgcenter.MSG_WAR_PLAYERONREADY, PlayerReady, 'PlayerReady' + self.m_CallFlag)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, InitPlayer, 'AddAllPlayer' + self.m_CallFlag, -1, 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, NodeGoalOK, 'NodeGoalOK' + self.m_CallFlag, -1, 0)

    
    def Save(self, iHero):
        dData = { }
        oHero = self.m_Game.GetObject(iHero)
        if oHero:
            dData = DeepCopy(oHero.Query('RelifeInfo', { }))
        return dData

    
    def Load(self, iHero, dData):
        self.m_SavedData[iHero] = dData

    
    def GetRelifeTimes(self, oHero):
        dInfo = GetRelifeInfo(self.m_RelifeData)
        if self.m_WarMgr.IsSingleGame():
            iBase = dInfo['SingleRelifeTimes']
        else:
            iBase = dInfo['TeamRelifeTimes']
        iTotal = iBase + oHero.Query('AdditionalGSCashRelife', 0)
        return iTotal

    
    def GetDyingSecond(self):
        return self.m_InitDyingSecond

    
    def WarRelifeSetInfo(self):
        return (TYPE_RELIFE_GSCASH, 'WarInit', 0)

    
    def GetRelifeGSCashCost(self, oHero):
        dInfo = GetRelifeInfo(self.m_RelifeData)
        iGSCashRelifeTimes = oHero.QuerySavedData('GSCashRelifeTimes', 0) + 1
        sKey = 'SingleRelifeCost' if self.m_WarMgr.IsSingleGame() else 'TeamRelifeCost'
        iCost = 0
        if sKey not in dInfo:
            return iCost
        if iGSCashRelifeTimes in dInfo[sKey]:
            iCost = dInfo[sKey][iGSCashRelifeTimes]
        else:
            lstRelifeTimes = sorted(dInfo[sKey], reverse = True)
            for iTimes in lstRelifeTimes:
                if iGSCashRelifeTimes >= iTimes:
                    iCost = dInfo[sKey][iTimes]
                    break
            
        iCost = cl_formula.GetFormulaResult(oHero, iCost)
        if iCost < 0:
            iCost = 0
        return iCost

    
    def InitPlayer(self, dInfo):
        oWarMgr = self.m_WarMgr
        lstHero = oWarMgr.GetAllHero()
        oGame = self.m_Game
        if oGame.m_WarMgr.IsSingleGame():
            oHero = self.m_Game.GetObject(lstHero[0])
            if not oHero or not oHero.Query('SingleRescue'):
                self.m_OpenRescue = 0
                self.m_OpenRescueSource = { }
        iDyingSecond = self.GetDyingSecond()
        for iHero in lstHero:
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if iHero in self.m_SavedData:
                oHero.SetRelifeInfo(self.m_SavedData[iHero])
            else:
                iRelifeTimes = self.GetRelifeTimes(oHero)
                if iRelifeTimes > 0:
                    (iType, sKey, iRemainTime) = self.WarRelifeSetInfo()
                    oHero.AddRelifeInfo(iType, sKey, iRemainTime, iRelifeTimes, 0)
                oHero.InitDyingSecond(iDyingSecond)
            cl_msgcenter.AddAttentionFunc(oWarMgr, iHero, cl_msgcenter.MSG_WAR_RELIFE, OnHeroRelife, 'OnHeroRelife' + self.m_CallFlag)
        

    
    def CheckAllHeroDead(self):
        for iTarget in self.m_WarMgr.GetAllHero():
            oTarget = self.m_Game.GetObject(iTarget)
            if not oTarget:
                continue
            if not oTarget.IsDead():
                return False
            if oTarget.IsRealDied():
                continue
            if oTarget.Query('DelayRealDie'):
                return False
            if oTarget.Query('SingleRescue'):
                return False
            (iType, _, _) = oTarget.GetFirstRelifeInfo()
            if iType != 0:
                return False
        
        return True

    
    def AllDyingHeroDie(self):
        for iTarget in self.m_WarMgr.GetAllHero():
            oTarget = self.m_Game.GetObject(iTarget)
            if not oTarget:
                continue
            if not oTarget.IsDying():
                continue
            self.RealHeroDie(oTarget)
        

    
    def HeroEnterDie(self, oHero, iAttack, oReason):
        if oHero.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        (iType, _, _) = oHero.GetFirstRelifeInfo()
        if self.ValidHeroDying(oHero, iType):
            self.HeroDying(oHero, iAttack, oReason)
            if not oHero.IsDead():
                return None
            if not self.m_WarMgr.IsSingleGame(bExcludeAIMember = True) and self.CheckAllHeroDead():
                self.AllDyingHeroDie()
                return None
        oHero.Die(iAttack, oReason)
        if not oHero.IsDead():
            return None
        if iType not in (TYPE_RELIFE_RELIC, TYPE_RELIFE_PASSIVE):
            if self.m_OpenRescue:
                self.RealHeroDie(oHero)
                return None
            if iType not in (TYPE_RELIFE_GSCASH, TYPE_RELIFE_DICE):
                cl_snetwar.GS2CRelifeConfirm(self.m_Game, oHero.m_PlayerID, iRelifeIdx = 0, iLeftTimes = 0, iMaxTimes = 0, iType = 0, iRemainTime = 0, iCost = 0)
                self.Call_Out(Functor(self.DelayRealHeroDie, oHero.m_ID), Time2Frame(DEAD_REAL_DELAYTIME), 'DelayRealHeroDie')
                return None
        self.HeroRelife(oHero)

    
    def MonsterEnterDie(self, oMonster, iAttack, oReason):
        if oMonster.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        (iType, sKey, iTime) = oMonster.GetFirstRelifeInfo()
        if oReason.GetStrReason() == 'FollowDie' or oMonster.Query('NoRelife', 0) or not iType:
            if oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS and oMonster.m_FightType not in BOSS_DONOT_COUNT:
                self.RelifeRealDied()
            oMonster.Die(iAttack, oReason)
            return None
        oMonster.CostRelifeTimes(iType, sKey)
        if oMonster.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS or oMonster.m_FightType in BOSS_DONOT_COUNT:
            oMonster.DieClearEffect()
        dRelifeRatio = oMonster.Query('RelifeRatio', { })
        dRelifeInfo = None
        if dRelifeRatio:
            tRelifeExtInfoKey = (iType, sKey)
            if tRelifeExtInfoKey in dRelifeRatio:
                dRatio = dRelifeRatio[tRelifeExtInfoKey]
                dRelifeInfo = oMonster.GetHpInfoByRatio(dRatio)
        iRatio = oMonster.Query('HatchRatio', { })[(iType, sKey)]
        dHatchInfo = {
            'Ratio': iRatio,
            'Time': iTime,
            'RelifeInfo': dRelifeInfo }
        oMonster.Hatch({
            'Type': iType }, dHatchInfo)

    
    def ServantEnterDie(self, oServant, iAttack, oReason):
        if not oServant.m_FightType & WARRIOR_SERVANT:
            return None
        if not self.ValidServantDying(oServant, oReason):
            oServant.Die(iAttack, oReason)
            oServant.RealDie(oReason)
            return None
        oServant.Dying(iAttack, oReason, {
            'StateCount': oServant.GetRestDyingSecond() })

    
    def PetEnterDie(self, oPet, iAttack, oReason):
        if not oPet.m_FightType & WARRIOR_PET:
            return None
        oPet.Die(iAttack, oReason)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_PET_DIE, oPet, {
            'Pet': oPet.m_ID,
            'Pos': oPet.GetPos() })
        if oPet.m_FightType & WARRIOR_PET_HEROSIDE == WARRIOR_PET_HEROSIDE:
            oPet.RealDie(oReason)

    
    def RealServantDie(self, oServant):
        if oServant.IsRealDied():
            return None
        oServant.RealDie()

    
    def DelayRealHeroDie(self, iHero):
        self.Remove_Call_Out('DelayRealHeroDie')
        oHero = self.m_Game.GetObject(iHero)
        if not oHero or not oHero.IsDead():
            return None
        self.RealHeroDie(oHero)

    
    def RealHeroDie(self, oHero):
        if not oHero.IsDead():
            return None
        if oHero.IsRealDied() or oHero.Query('DelayRealDie'):
            return None
        WarobjLog.Info('game: %d pid: %d realdie' % (self.m_Game.m_ID, oHero.m_PlayerID))
        if hasattr(oHero, 'm_RelifeCache'):
            delattr(oHero, 'm_RelifeCache')
        oHero.RealDie()
        self.m_Game.m_WarMgr.OnPlayerDead(oHero)

    
    def ValidHeroDying(self, oHero, iFirstRelifeType):
        if iFirstRelifeType in (TYPE_RELIFE_RELIC, TYPE_RELIFE_PASSIVE):
            return False
        if not self.m_OpenRescue:
            return False
        iLeftSecond = oHero.GetRestDyingSecond()
        if iLeftSecond <= 0:
            return False
        return True

    
    def ValidServantDying(self, oServant, oReason):
        if oServant.m_FightType & WARRIOR_PLANT == WARRIOR_PLANT:
            return False
        if oServant.m_FightType & WARRIOR_MECH == WARRIOR_MECH and oServant.Query('CanExplosion', 0):
            return False
        oOwner = oServant.GetOwner()
        if not oOwner or oOwner.IsRealDied():
            return False
        return True

    
    def HeroDying(self, oHero, iAttack, oReason):
        iLeftSecond = oHero.GetRestDyingSecond()
        oHero.CostDyingTimes()
        oHero.Dying(iAttack, oReason, {
            'StateCount': iLeftSecond })

    
    def HeroRelife(self, oHero):
        if not oHero.IsDead():
            return None
        (iType, sKey, iRemainTime) = oHero.GetFirstRelifeInfo()
        if iType == 0:
            (iType, sKey, iRemainTime) = self.WarRelifeSetInfo()
        iCost = self.GetRelifeGSCashCost(oHero) if iType == TYPE_RELIFE_GSCASH else 0
        self.m_RelifeIdx += 1
        idx = self.m_RelifeIdx
        oHero.m_RelifeCache = (idx, iType, sKey, iRemainTime, iCost)
        if iType in (TYPE_RELIFE_RELIC, TYPE_RELIFE_PASSIVE):
            self.Call_Out(Functor(self.HeroRelifeDelay, idx, oHero.m_ID), Time2Frame(iRemainTime), 'RelifeDelayCall')
        (iLeftTimes, iMaxTimes) = oHero.GetRelifeTimesAndMaxTimesByType(iType)
        cl_snetwar.GS2CRelifeConfirm(self.m_Game, oHero.m_PlayerID, idx, iLeftTimes, iMaxTimes, iType, iRemainTime, iCost)
        if self.IsDirectDie(iType, oHero):
            self.Call_Out(Functor(self.DelayRealHeroDie, oHero.m_ID), Time2Frame(DEAD_REAL_DELAYTIME), 'DelayRealHeroDie')

    
    def IsDirectDie(self, iType, oHero):
        if not (self.m_OpenRescue) and iType == TYPE_RELIFE_GSCASH:
            pass
        return oHero.m_WarGSCash < self.GetRelifeGSCashCost(oHero)

    
    def HeroRelifeDelay(self, idx, iHeroID):
        oHero = self.m_Game.GetObject(iHeroID)
        if not oHero or not oHero.IsDied():
            return None
        if not hasattr(oHero, 'm_RelifeCache') or oHero.m_RelifeCache[0] != idx:
            self.RealHeroDie(oHero)
            return None
        iType = oHero.m_RelifeCache[1]
        sKey = oHero.m_RelifeCache[2]
        iCost = oHero.m_RelifeCache[4]
        delattr(oHero, 'm_RelifeCache')
        if not self.ValidHeroRelife(oHero, iType, sKey):
            self.RealHeroDie(oHero)
            return None
        self.RealHeroRelife(oHero, idx, iType, sKey, iCost)

    
    def ValidHeroRelife(self, oHero, iType, sKey):
        iLeftTimes = oHero.GetRelifeTimes(iType, sKey)
        if iLeftTimes <= 0:
            return False
        if iType != TYPE_RELIFE_RELIC and not self.m_WarMgr.IsSingleGame() and not oHero.IsDying():
            return False
        return True

    
    def RealHeroRelife(self, oHero, idx, iType, sKey, iCost):
        WarobjLog.Info('game: %d hero %d pid: %d relife %d type %d key %s' % (self.m_Game.m_ID, oHero.m_ID, oHero.m_PlayerID, idx, iType, sKey))
        oHero.CostRelifeTimes(iType, sKey)
        dReason = {
            'Type': iType,
            'Cost': iCost }
        oHero.Relife(dReason)

    
    def StartPayRelife(self, oHero, iRelifeIdx):
        if iRelifeIdx != oHero.m_RelifeCache[0]:
            return None
        iType = oHero.m_RelifeCache[1]
        sKey = oHero.m_RelifeCache[2]
        iCost = oHero.m_RelifeCache[4]
        if not self.ValidHeroRelife(oHero, iType, sKey):
            self.RealHeroDie(oHero)
            return None
        WarobjLog.Debug('game: %d hero %d pid: %d gscash %d need %d' % (self.m_Game.m_ID, oHero.m_ID, oHero.m_PlayerID, oHero.m_WarGSCash, iCost))
        if oHero.m_WarGSCash < iCost:
            self.RealHeroDie(oHero)
            return None
        sReason = 'relife'
        iNewGSCashRelifeTimes = oHero.QuerySavedData('GSCashRelifeTimes', 0) + 1
        oHero.SetSavedData('GSCashRelifeTimes', iNewGSCashRelifeTimes)
        WarobjLog.Info('game: %d hero %d pid: %d pay gscash %d %s %d' % (self.m_Game.m_ID, oHero.m_ID, oHero.m_PlayerID, iCost, sReason, iNewGSCashRelifeTimes))
        oHero.ConsumeGSCash(iCost, sReason)
        delattr(oHero, 'm_RelifeCache')
        self.RealHeroRelife(oHero, iRelifeIdx, iType, sKey, iCost)

    
    def AnswerRelife(self, oHero, iRelifeIdx, iAnswer):
        if not oHero.IsDied() and not oHero.IsDying():
            return None
        WarobjLog.Debug('game: %d hero %s pid: %d answerrelife %d ' % (self.m_Game.m_ID, oHero.m_ID, oHero.m_PlayerID, iAnswer))
        if iAnswer:
            if not hasattr(oHero, 'm_RelifeCache'):
                return None
            idx = oHero.m_RelifeCache[0]
            iType = oHero.m_RelifeCache[1]
            if idx != iRelifeIdx or iType not in (TYPE_RELIFE_GSCASH, TYPE_RELIFE_DICE):
                return None
            self.StartPayRelife(oHero, idx)
        elif self.Find_Call_Out('DelayRealHeroDie'):
            self.Remove_Call_Out('DelayRealHeroDie')
        self.RealHeroDie(oHero)

    
    def DirectHeroRelife(self, oHero, dReason, dRelifeInfo = None):
        if not oHero.IsDied() and not oHero.IsDying():
            return None
        oHero.Relife(dReason, dRelifeInfo)

    
    def WatcherRelife(self, oHero, iType, iAttack, dRelifeInfo = None):
        WarobjLog.Info('game: %d pid: %d realrelife type %d' % (self.m_Game.m_ID, oHero.m_PlayerID, iType))
        dReason = {
            'Type': iType,
            'AID': iAttack }
        oHero.Relife(dReason, dRelifeInfo)
        cl_snetwar.GS2CTriggerBehavior(self.m_Game, oHero.m_ID, 11, self.m_Game.GetRealPlayers())
        self.m_Game.m_WarMgr.AddLivePlayer(oHero.m_PlayerID)

    
    def OnPlayerReEnter(self, oHero):
        if not hasattr(oHero, 'm_RelifeCache'):
            return None
        if oHero.m_RelifeCache[1] != TYPE_RELIFE_GSCASH:
            return None
        (idx, iType, _sKey, iRemainTime, iCost) = oHero.m_RelifeCache
        (iLeftTimes, iMaxTimes) = oHero.GetRelifeTimesAndMaxTimesByType(iType)
        cl_snetwar.GS2CRelifeConfirm(self.m_Game, oHero.m_PlayerID, idx, iLeftTimes, iMaxTimes, iType, iRemainTime, iCost)

    
    def NodeGoalOK(self, dMsgInfo):
        if 'PassLevel' in dMsgInfo and dMsgInfo['PassLevel'] is False:
            return None
        if 'LevelType' not in dMsgInfo:
            return None
        self.RelifeDead(dMsgInfo)

    
    def RelifeDead(self, dMsgInfo):
        if dMsgInfo['LevelType'] == LEVEL_TYPE_HIDE:
            return None
        oGame = self.m_Game
        for iHero in self.m_WarMgr.GetRoomHero():
            oHero = oGame.GetObject(iHero)
            if not oHero:
                continue
            if not oHero.IsDying():
                if oHero.IsDied():
                    dReason = {
                        'Type': TYPE_RELIFE_PASS }
                    dInfo = {
                        'HP': max(100, oHero.QueryAttr('HPMax') // 10),
                        'Shield': 0,
                        'Armor': 0 }
                    oHero.Relife(dReason, dInfo)
                    self.m_Relifed[iHero] = 1
                    continue
        
        dMsgInfo['Relifed'] = self.m_Relifed

    
    def OnHeroRelife(self, oHero, dInfo):
        if hasattr(oHero, 'm_RelifeCache'):
            delattr(oHero, 'm_RelifeCache')

    
    def RelifeRealDied(self):
        oWatch = self.m_WarMgr.GetComponent('WatchElement')
        self.m_Relifed = { }
        for iTarget in self.m_WarMgr.GetRoomHero():
            oTarget = self.m_Game.GetObject(iTarget)
            if not oTarget or not oTarget.IsRealDied():
                continue
            self.m_Relifed[oTarget.m_ID] = 1
            dRelifeInfo = {
                'HP': max(100, oTarget.QueryAttr('HPMax') * 20 // 100),
                'Shield': oTarget.QueryAttr('ShieldMax'),
                'Armor': oTarget.QueryAttr('ArmorMax') }
            oFocus = oWatch.GetFocus(iTarget)
            oWatch.RelifeWatch(oTarget)
            self.WatcherRelife(oTarget, TYPE_RELIFE_KILLBOSS, oTarget.m_ID, dRelifeInfo)
            if oFocus or oTarget.m_Scene == oFocus.m_Scene:
                oTarget.WalkTo(oFocus.GetPos())
                oTarget.Stop()
                continue
            oTarget.Goto(oFocus.m_Scene, oFocus.GetPos(), oFocus.GetFacing())
        

    
    def OpenRescue(self, sKey):
        self.m_OpenRescueSource[sKey] = 1
        if not self.m_OpenRescue:
            self.m_OpenRescue = 1

    
    def CloseRescue(self, sKey):
        if sKey in self.m_OpenRescueSource:
            self.m_OpenRescueSource.pop(sKey)
        if not self.m_OpenRescueSource:
            self.m_OpenRescue = 0



def InitPlayer(oWarMgr, dInfo):
    oDieElement = oWarMgr.GetComponent('PVEDieElement')
    oDieElement.InitPlayer(dInfo)


def PlayerReady(oWarMgr, oWarrior, dInfo):
    if oWarrior.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
        oDieElement = oWarMgr.GetComponent('PVEDieElement')
        oDieElement.OnPlayerReEnter(oWarrior)


def NodeGoalOK(oWarMgr, dMsgInfo):
    oDieElement = oWarMgr.GetComponent('PVEDieElement')
    if oDieElement.Find_Call_Out('DelayRealHeroDie'):
        oDieElement.Remove_Call_Out('DelayRealHeroDie')
    oDieElement.NodeGoalOK(dMsgInfo)


def OnHeroRelife(oWarMgr, oHero, dInfo):
    oDieElement = oWarMgr.GetComponent('PVEDieElement')
    oDieElement.OnHeroRelife(oHero, dInfo)


def GetComponentClass(oMgrManager):
    return CPVEDieElement

