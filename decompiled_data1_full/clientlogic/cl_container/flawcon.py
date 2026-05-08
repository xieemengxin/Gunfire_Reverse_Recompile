# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/flawcon.pyc
# RelativePath: clientlogic/cl_container/flawcon.pyc
# Source Generated with Decompyle++
# File: flawcon.pyc (Python 3.6)

from cl_only import WeakProxy, Time2Frame, Frame2Time, Functor, PY_FLAG_DEAD, ChooseKey, PY_FLAG_DIED
from cl_commondefines import MODEL_TYPE_SPHERE, WARRIOR_MONSTER, STATE_TIME_LIMIT, ATTACKERSUBMSG_NORMAL, FLAW_COLDTIME, FLAW_KILLLINE, FLAW_UNBALANCE_KILLLINE, FLAW_MAXCOUNT, FLAW_EFFECTTIME, FLAW_HITTIMES, FLAW_UNBALANCE_PROB, FLAW_UNBALANCE_EFFECTTIME, FLAW_SIZE, FLAW_UNBALANCE_EFFECTTIME, FLAW_ISWEAKNESS, FLAW_SPAWNFRAME, FLAW_UNBALANCE_COLDTIME, FLAW_UNBALANCE_STARTFRAME, FLAW_LOCKMAXCOUNT, FLAW_CURHITTIMES
from cl_commondefines import STATE_TIME_FOREVER, STATE_PETROCHEMICAL_DISSOLVE, FLAW_MAXKILLLINE, WUDI_START, WUDI_END, WARRIOR_BOSS, EXECUTOR_HERO, DAM_TYPE_WEAPON, REASON_HITFLAW, STATE_UNBALANCE, STATE_EXECUTE_UNBALANCE, CRT_CHECK_CLIENT, MONSTER_PART_FLAW, FIGHT_KEY_IGNOREEXECTORCHOOSE
from cl_pxlayer import PXLAYER_TRIDSTEVENT
from cl_object.logging import WarobjLog
import cl_engphyobj
import cl_msgcenter
import cl_platformdata
import cl_state
import cl_object.reason
import cl_snetwar as net
import cl_formula
RANGE_INFINITE = 99
ADDITION_HERO = 1
ADDITION_MONSTER = 2
COMMON_FLAG = 'CommonFlawCon'

class CFlawContainer(object):
    
    def __init__(self, oGame, oWarrior, dData):
        self.m_Game = oGame
        self.m_Owner = WeakProxy(oWarrior)
        self.m_Flag = 'FlawCon-%s' % oWarrior.m_PlayerID
        self.m_FlawRange = cl_platformdata.GetMonsterFlawRange()
        self.m_FlawData = cl_platformdata.GetMonsterFlaw()
        self.m_WeaknessFlawMonster = cl_platformdata.GetWeaknessFlawMonster()
        self.m_ShareCountMonster = cl_platformdata.GetShareFlawCountMonster()
        self.m_ImmuneExecuteMonster = cl_platformdata.GetImmuneExecuteMonster()
        iWarNo = oGame.m_WarMgr.m_SID
        self.m_MonsterState = dData['MonsterState'] if 'MonsterState' in dData else { }
        if 'PlayModeAddition' in dData and iWarNo in dData['PlayModeAddition']:
            self.m_PlayModeAddition = dData['PlayModeAddition'][iWarNo]
        else:
            self.m_PlayModeAddition = { }
        if 'FlawMaxCnt' in dData and iWarNo in dData['FlawMaxCnt']:
            self.m_FlawMaxCnt = dData['FlawMaxCnt'][iWarNo]
        else:
            self.m_FlawMaxCnt = 0
        self.m_Trigger = { }
        self.m_Flaw = { }
        self.m_NewFlawID = { }
        self.m_WeaknessProb = { }
        self.m_CurWeaknessProb = 0
        self.m_FlawAddition = { }
        self.m_CurFlawAddition = { }
        self.m_MonsterAddition = { }
        self.m_CurMonsterAddition = { }
        self.m_CallOut = { }
        self.m_NextCallOutFrameNum = 0
        self.m_ShareFlaw = { }
        self.m_ShareFlawStandBy = { }
        self.m_FlawCD = { }
        self.m_DelaySpawnFlaw = { }
        self.m_Pause = { }
        self.m_CntLimitStandBy = { }
        self.InitTrigger()
        self.InitEvent()

    
    def Save(self):
        return { }

    
    def Load(self, dData):
        pass

    
    def InitEvent(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, self.m_Flag, iSub = ATTACKERSUBMSG_NORMAL, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.OnMapLoadOK, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, self.OnDiedist, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(self.m_Owner, cl_msgcenter.MSG_WAR_RELIFE, self.OnRelife, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateMonster, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CG_START, self.OnCGStart, self.m_Flag, iOnce = 0)
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_CG_END, self.OnCGEnd, self.m_Flag, iOnce = 0)

    
    def InitTrigger(self):
        for iRange in self.m_FlawRange:
            self.SetRangeTrigger(iRange)
        

    
    def SetRangeTrigger(self, iRange):
        if iRange in self.m_Trigger or iRange == RANGE_INFINITE:
            return None
        dShape = {
            'Shape': MODEL_TYPE_SPHERE,
            'Center': (0, 0, 0),
            'Radius': iRange }
        func = Functor(self.OnTrigger, iRange)
        oTrigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, self.m_Owner, PXLAYER_TRIDSTEVENT, dShape, func)
        oTrigger.rigidbody.E_SetKinematic(1)
        self.m_Trigger[iRange] = oTrigger

    
    def AddRangeFlaw(self, oMonster, iFlawSID, iRange):
        lstFlaw = self.m_FlawRange.setdefault(iRange, [])
        if iFlawSID not in lstFlaw:
            lstFlaw.append(iFlawSID)
        if iRange == RANGE_INFINITE:
            self.StartSpawnFlaw(oMonster)
        else:
            self.SetRangeTrigger(iRange)

    
    def Release(self):
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_ATTACK, self.m_Flag, iSub = ATTACKERSUBMSG_NORMAL)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, self.m_Flag)
        cl_msgcenter.DoneEvent(self.m_Owner, cl_msgcenter.MSG_WAR_RELIFE, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CG_START, self.m_Flag)
        cl_msgcenter.DoneEvent(oWarMgr, cl_msgcenter.MSG_WARMGR_CG_END, self.m_Flag)
        for iRange, oTrigger in self.m_Trigger.items():
            oTrigger.Unstall()
            self.m_Trigger[iRange] = None
        
        for dCall in self.m_CallOut.values():
            dCall.clear()
        
        self.m_Trigger = { }
        self.m_CallOut = { }
        self.m_Flaw = { }
        self.m_Owner = None
        self.m_Game = None

    
    def StartSpawnFlaw(self, oMonster):
        iMonster = oMonster.m_ID
        self.m_Flaw[iMonster] = { }
        if self.CheckShareFlaw(oMonster):
            dStandBy = self.m_ShareFlawStandBy.setdefault(oMonster.m_FlawSID, { })
            dStandBy[iMonster] = 0
        self.SpawnFlaw(iMonster)

    
    def GetFlaw(self, iMonster):
        if iMonster not in self.m_Flaw:
            return None
        return self.m_Flaw[iMonster]

    
    def ClearFlaw(self, oMonster, iSync = 1, iPop = 1):
        iMonster = oMonster.m_ID
        if iMonster in self.m_Flaw:
            iCnt = len(self.m_Flaw[iMonster])
            self.m_CntLimitStandBy.pop(iMonster, 0)
            self.TryFillFlawCount(iCnt)
            if iPop:
                self.m_Flaw.pop(iMonster, 0)
            else:
                self.m_Flaw[iMonster].clear()
            self.ClearTargetCallOut(iMonster)
            if iSync:
                net.GS2CMonsterClearFlaw(self.m_Owner.m_PlayerID, iMonster)
        if self.CheckShareFlaw(oMonster):
            iSID = oMonster.m_FlawSID
            if iSID in self.m_ShareFlaw:
                self.m_ShareFlaw[iSID].pop(iMonster, 0)
            if iSID in self.m_ShareFlawStandBy:
                self.m_ShareFlawStandBy[iSID].pop(iMonster, 0)
            else:
                self.m_FlawCD.pop(oMonster.m_ID, 0)

    
    def ClearAllFlaw(self):
        dFlaw = { }
        oGame = self.m_Game
        for iMonster, dFlaw in self.m_Flaw.items():
            dFlaw.clear()
            self.ClearTargetCallOut(iMonster)
            net.GS2CMonsterClearFlaw(self.m_Owner.m_PlayerID, iMonster)
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if oMonster and self.CheckShareFlaw(oMonster):
                iSID = oMonster.m_FlawSID
                if iSID in self.m_ShareFlaw:
                    self.m_ShareFlaw[iSID].pop(iMonster, 0)
                if iSID in self.m_ShareFlawStandBy:
                    self.m_ShareFlawStandBy[iSID][iMonster] = 0
                    continue
            self.m_FlawCD.pop(iMonster, 0)
        

    
    def OnCreateMonster(self, oWarMgr, dInfo):
        iMonster = dInfo['Monster']
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            return None
        self.PrepareMonsterKillLine(oMonster)
        if oMonster.m_FlawSID in self.m_MonsterState:
            iState = self.m_MonsterState[oMonster.m_FlawSID]
            dArgs = {
                'AID': oMonster.m_ID,
                'RS': cl_object.reason.CStrReason(self.m_Flag),
                'arg': { } }
            oState = cl_state.AddState(oMonster, iState, STATE_TIME_FOREVER, 0, dArgs)
            if oState:
                oState.Enable(oMonster)
        cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_DIE, OnMonsterDie, COMMON_FLAG, iOnce = 1)
        cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_HATCH, OnMonsterHatch, COMMON_FLAG, iOnce = 0)
        if oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_WUDI, OnMonsterWudiStart, COMMON_FLAG, iSub = WUDI_START, iOnce = 0)
        if oMonster.IsPetrochemical():
            MonsterForbidSpawnFlaw(oMonster, 'Petrochemical')
            cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, OnCustomStateEnd, COMMON_FLAG, iOnce = 0)
        if oMonster.m_FlawSID in self.m_FlawRange[RANGE_INFINITE]:
            self.StartSpawnFlaw(oMonster)

    
    def PrepareMonsterKillLine(self, oMonster):
        iBaseKillLine = self.GetFlawAttr(oMonster, FLAW_KILLLINE, iCalAddition = 0)
        iUnbalanceKillLine = self.GetFlawAttr(oMonster, FLAW_UNBALANCE_KILLLINE, iCalAddition = 0)
        iMaxKillLine = self.GetFlawAttr(oMonster, FLAW_MAXKILLLINE, iCalAddition = 0)
        net.GS2CMonsterKillLine(self.m_Owner.m_PlayerID, [
            [
                oMonster.m_ID,
                iBaseKillLine,
                iUnbalanceKillLine,
                iMaxKillLine]])

    
    def SyncHeroKillLine(self):
        if FLAW_KILLLINE not in self.m_CurFlawAddition and FLAW_UNBALANCE_KILLLINE not in self.m_CurFlawAddition:
            return None
        iBaseKillLine = self.m_CurFlawAddition.get(FLAW_KILLLINE, 100000000)
        iUnbalanceKillLine = self.m_CurFlawAddition.get(FLAW_UNBALANCE_KILLLINE, 100000000)
        net.GS2CHeroKillLine(self.m_Owner.m_PlayerID, iBaseKillLine, iUnbalanceKillLine)

    
    def SyncMonsterKillLineAddition(self, iMonster):
        dAddition = self.m_CurMonsterAddition.get(iMonster, { })
        if FLAW_KILLLINE not in dAddition:
            return None
        iKillLineAddition = dAddition.get(FLAW_KILLLINE, 100000000)
        net.GS2CMonsterKillLineAddition(self.m_Owner.m_PlayerID, iMonster, iKillLineAddition)

    
    def ResumeSpawnFlaw(self, oMonster):
        if not self.CheckInFlaw(oMonster.m_ID):
            return None
        self.StartSpawnFlaw(oMonster)

    
    def OnTrigger(self, iRange, obj, iLeave):
        if not obj.m_FightType & WARRIOR_MONSTER:
            return None
        if iRange not in self.m_FlawRange or obj.m_FlawSID not in self.m_FlawRange[iRange]:
            return None
        iMonster = obj.m_ID
        if obj.IsPetrochemical():
            if iLeave:
                self.m_Flaw.pop(iMonster, 0)
            else:
                self.m_Flaw[iMonster] = { }
            return None
        if iLeave:
            self.ClearFlaw(obj, iSync = 1, iPop = 1)
        elif iMonster not in self.m_Flaw:
            self.StartSpawnFlaw(obj)

    
    def CheckSpawnFlaw(self, oMonster):
        if self.m_Pause:
            return None
        iMonster = oMonster.m_ID
        dFlaw = self.GetFlaw(iMonster)
        if dFlaw is None:
            return 0
        if self.GetSpawnFlawCD(oMonster):
            return 0
        if self.CheckShareFlaw(oMonster):
            dShareFlaw = self.m_ShareFlaw.get(oMonster.m_FlawSID, { })
            if iMonster in dShareFlaw:
                return 0
            iFlawCount = len(dShareFlaw)
        else:
            iFlawCount = len(dFlaw)
        iMaxFlawCount = self.GetFlawMaxCount(oMonster)
        if iFlawCount >= iMaxFlawCount:
            return 0
        if oMonster.Query('ForbidSpawnFlaw', { }):
            return 0
        if oMonster.m_Scene != self.m_Owner.m_Scene:
            return 0
        return 1

    
    def GetSpawnFlawCD(self, oMonster):
        iKey = self.GetKey(oMonster)
        if iKey in self.m_FlawCD:
            iCurFrame = self.m_Game.GetFrameNum()
            if iCurFrame < self.m_FlawCD[iKey]:
                return self.m_FlawCD[iKey] - iCurFrame
        return 0

    
    def ReduceTargetCurFlawCD(self, oTarget, iReduce, iMul):
        iKey = self.GetKey(oTarget)
        if iKey not in self.m_FlawCD:
            return None
        iCurFrame = self.m_Game.GetFrameNum()
        iCDFrame = self.m_FlawCD[iKey]
        if iCDFrame <= iCurFrame:
            return None
        iNewCDFrame = iCDFrame - iCurFrame
        if iMul:
            iNewCDFrame = iNewCDFrame * (100 - iMul) // 100
        iNewCDFrame -= iReduce
        if iNewCDFrame < 0:
            iNewCDFrame = 0
        self.m_FlawCD[iKey] = iCurFrame + iNewCDFrame
        if iNewCDFrame == 0:
            if iKey in self.m_ShareFlaw:
                self.RandomSpawnShareFlaw(iKey)
            else:
                self.SpawnFlaw(iKey)
        elif iKey in self.m_ShareFlaw:
            func = Functor(self.RandomSpawnShareFlaw, iKey)
        else:
            func = Functor(self.SpawnFlaw, iKey)
        self.m_DelaySpawnFlaw[iKey] = 1
        self.Call_Out(iKey, iNewCDFrame + 1, func)

    
    def ReduceAllCurFlawCD(self, iReduce, iMul):
        iCurFrame = self.m_Game.GetFrameNum()
        dFlawCD = self.m_FlawCD
        dSpawnFlaw = { }
        for iKey, iCDFrame in dFlawCD.items():
            if iCDFrame <= iCurFrame:
                continue
            iNewCDFrame = iCDFrame - iCurFrame
            if iMul:
                iNewCDFrame = iNewCDFrame * (100 - iMul) // 100
            iNewCDFrame -= iReduce
            if iNewCDFrame < 0:
                iNewCDFrame = 0
            dFlawCD[iKey] = iCurFrame + iNewCDFrame
            if iNewCDFrame == 0:
                dSpawnFlaw[iKey] = 1
                continue
            if iKey in self.m_ShareFlaw:
                func = Functor(self.RandomSpawnShareFlaw, iKey)
            else:
                func = Functor(self.SpawnFlaw, iKey)
            self.m_DelaySpawnFlaw[iKey] = 1
            self.Call_Out(iKey, iNewCDFrame + 1, func)
        
        for iKey in dSpawnFlaw:
            if iKey in self.m_ShareFlaw:
                self.RandomSpawnShareFlaw(iKey)
                continue
            self.SpawnFlaw(iKey)
        

    
    def NewFlawID(self, iMonster):
        if iMonster not in self.m_NewFlawID or self.m_NewFlawID[iMonster] > 255:
            self.m_NewFlawID[iMonster] = 0
        self.m_NewFlawID[iMonster] += 1
        return self.m_NewFlawID[iMonster]

    
    def SpawnFlaw(self, iMonster):
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            return None
        iKey = self.GetKey(oMonster)
        self.m_DelaySpawnFlaw[iKey] = 0
        if not self.CheckSpawnFlaw(oMonster):
            return None
        iCurFlawCnt = self.RefreshAndGetFlawCnt()
        if self.m_FlawMaxCnt and iCurFlawCnt >= self.m_FlawMaxCnt:
            self.m_CntLimitStandBy[iMonster] = 1
            return None
        iFlaw = self.NewFlawID(iMonster)
        iEffectTime = self.GetFlawAttr(oMonster, FLAW_EFFECTTIME)
        iHitTimes = self.GetFlawAttr(oMonster, FLAW_HITTIMES)
        iUnbalanceEffectTime = self.GetFlawAttr(oMonster, FLAW_UNBALANCE_EFFECTTIME)
        iFlawColdTime = self.GetFlawAttr(oMonster, FLAW_COLDTIME)
        iSize = self.GetFlawAttr(oMonster, FLAW_SIZE)
        iIsWeakness = self.RandomWeaknessFlaw(oMonster)
        iCurFrame = self.m_Game.GetFrameNum()
        dFlaw = self.GetFlaw(iMonster)
        dFlaw[iFlaw] = {
            FLAW_SPAWNFRAME: iCurFrame,
            FLAW_ISWEAKNESS: iIsWeakness,
            FLAW_SIZE: iSize,
            FLAW_UNBALANCE_EFFECTTIME: Time2Frame(iUnbalanceEffectTime),
            FLAW_CURHITTIMES: 0,
            FLAW_HITTIMES: iHitTimes,
            FLAW_EFFECTTIME: iEffectTime }
        lstFlaw = [
            [
                iMonster,
                iFlaw,
                iEffectTime,
                iHitTimes,
                iSize,
                iIsWeakness]]
        net.GS2CMonsterSpawnFlaw(self.m_Owner.m_PlayerID, lstFlaw)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SPAWNFLAW, self.m_Owner, {
            'VID': iMonster,
            'Flaw': iFlaw })
        iCDFrame = Time2Frame(iFlawColdTime)
        self.m_FlawCD[iKey] = iCurFrame + iCDFrame
        iEffectFrame = Time2Frame(iEffectTime)
        self.Call_Out(iMonster, iEffectFrame + 1, Functor(self.RemoveFlaw, iMonster, iFlaw))
        if self.CheckShareFlaw(oMonster):
            iSID = oMonster.m_FlawSID
            dShareFlaw = self.m_ShareFlaw.setdefault(iSID, { })
            dShareFlaw[iMonster] = iFlaw
            dStandBy = self.m_ShareFlawStandBy.setdefault(iSID, { })
            dStandBy[iMonster] = iCurFrame
            iCount = len(dShareFlaw)
            func = Functor(self.RandomSpawnShareFlaw, iSID)
        else:
            iCount = len(dFlaw)
            func = Functor(self.SpawnFlaw, iMonster)
        iMaxFlawCount = self.GetFlawMaxCount(oMonster)
        if iCount < iMaxFlawCount:
            self.m_DelaySpawnFlaw[iKey] = 1
            self.Call_Out(iKey, iCDFrame + 1, func)

    
    def RemoveFlaw(self, iMonster, iFlaw, iEffect = 0):
        dFlaw = self.GetFlaw(iMonster)
        if not dFlaw or iFlaw not in dFlaw:
            return None
        dFlaw.pop(iFlaw)
        net.GS2CMonsterRemoveFlaw(self.m_Owner.m_PlayerID, iMonster, iFlaw, iEffect)
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            return None
        iKey = self.GetKey(oMonster)
        func = None
        if self.CheckShareFlaw(oMonster):
            dShareFlaw = self.m_ShareFlaw.get(iKey, { })
            dShareFlaw.pop(iMonster, 0)
            func = Functor(self.RandomSpawnShareFlaw, iKey)
        elif iKey not in self.m_DelaySpawnFlaw or not self.m_DelaySpawnFlaw[iKey]:
            iCount = len(dFlaw)
            iMaxFlawCount = self.GetFlawMaxCount(oMonster)
            if iCount < iMaxFlawCount:
                func = Functor(self.SpawnFlaw, iMonster)
        if func:
            self.m_DelaySpawnFlaw[iKey] = 1
            iCDFrame = self.GetSpawnFlawCD(oMonster)
            if iCDFrame:
                self.Call_Out(iKey, iCDFrame + 1, func)
            else:
                func()
        self.TryFillFlawCount(1)

    
    def TryFillFlawCount(self, iCount):
        if not self.m_CntLimitStandBy:
            return None
        oGame = self.m_Game
        if not self.m_Owner.m_Scene:
            return None
        dDis = oGame.Scene_GetTargetDisMap(self.m_Owner.m_ID, list(self.m_CntLimitStandBy))
        lstSortDis = sorted(dDis.items(), key = (lambda item: item[1]))
        for iMonster, _ in lstSortDis[:iCount]:
            self.SpawnFlaw(iMonster)
        

    
    def GetSkillHitFlaw(self, oSkill, iMonster):
        if 'Flaw' in oSkill.m_Update:
            return oSkill.m_Update['Flaw']
        if not oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return []
        dCartoon = oSkill.GetCurCartoon()
        if not dCartoon or 'ID' not in dCartoon or dCartoon['ID'] not in oSkill.m_NetReceive:
            return []
        dClient = oSkill.m_NetReceive[dCartoon['ID']]
        if 'Flaw' not in dClient or not dClient['Flaw']:
            return []
        idx = 0
        iHitFlaw = 0
        lstFlaw = dClient['Flaw']
        for dInfo in oSkill.m_Update['HitInfo']:
            if dInfo['HitArea'] != MONSTER_PART_FLAW:
                continue
            if dInfo['Victim'] == iMonster:
                if len(lstFlaw) > idx:
                    iHitFlaw = lstFlaw[idx]
                break
            idx += 1
        
        if iHitFlaw:
            return [
                iHitFlaw]
        return []

    
    def OnDealTotalDam(self, oHero, dMsgInfo):
        if 'Skill' not in dMsgInfo:
            return None
        oSkill = dMsgInfo['Skill']
        if not oSkill:
            return None
        if 'CurHitArea' not in oSkill.m_Update or oSkill.m_Update['CurHitArea'] != MONSTER_PART_FLAW:
            return None
        iMonster = dMsgInfo['CurVID']
        lstFlaw = self.GetSkillHitFlaw(oSkill, iMonster)
        if not lstFlaw:
            return None
        oMonster = self.m_Game.GetObject(iMonster, PY_FLAG_DEAD)
        if not oMonster:
            return None
        iBreakFlaw = oSkill.m_Update.pop('BreakFlaw', 0)
        dFlaw = self.GetFlaw(iMonster)
        for iFlaw in lstFlaw:
            if not dFlaw or iFlaw not in dFlaw:
                net.GS2CMonsterRemoveFlaw(self.m_Owner.m_PlayerID, iMonster, iFlaw, 0)
                continue
            dHitFlaw = dFlaw[iFlaw]
            dHitFlaw[FLAW_CURHITTIMES] += 1
            iCurHitTimes = dHitFlaw[FLAW_CURHITTIMES]
            dMsgInfo['FlawHitTimes'] = iCurHitTimes
            if iBreakFlaw or iCurHitTimes >= dHitFlaw[FLAW_HITTIMES] or dMsgInfo['DieData']:
                dMsgInfo['BreakFlaw'] = 1
            else:
                dMsgInfo['BreakFlaw'] = 0
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HIT_FLAW_BEFORE, oHero, dMsgInfo)
            if 'BreakFlaw' in dMsgInfo and dMsgInfo['BreakFlaw']:
                self.RemoveFlaw(iMonster, iFlaw, iEffect = 1)
            if not dMsgInfo['RS'].Query('DamType', 0) & DAM_TYPE_WEAPON:
                continue
            self.HitUnbalance(oMonster, dMsgInfo)
        

    
    def HitUnbalance(self, oMonster, dMsgInfo, iUnbalanceProb = 0):
        if not oMonster or not (oMonster.m_FightType & WARRIOR_MONSTER):
            return None
        if oMonster.IsUnbalance():
            return None
        if not self.CanHitUnbalance(oMonster):
            return None
        if not iUnbalanceProb:
            iUnbalanceProb = self.GetFlawAttr(oMonster, FLAW_UNBALANCE_PROB, dMsgInfo = dMsgInfo)
            if 'AddUnbalanceProb' in dMsgInfo:
                iUnbalanceProb += dMsgInfo['AddUnbalanceProb']
        iRandmon = self.m_Game.Random(10000)
        if iUnbalanceProb > iRandmon:
            iAttack = dMsgInfo['AID']
            dArgs = {
                'AID': iAttack,
                'RS': cl_object.reason.CStrReason(REASON_HITFLAW),
                'arg': { } }
            iUnbalanceEffectFrame = Time2Frame(self.GetFlawAttr(oMonster, FLAW_UNBALANCE_EFFECTTIME))
            oState = cl_state.AddState(oMonster, STATE_UNBALANCE, STATE_TIME_LIMIT, iUnbalanceEffectFrame, dArgs)
            if oState:
                oState.Enable(oMonster)

    
    def OnMapLoadOK(self, oHero, dInfo):
        self.SyncHeroKillLine()
        oGame = self.m_Game
        oScene = oGame.m_SceneMgr.GetScene(oHero.m_Scene)
        lstKillLine = []
        lstFlaw = []
        iCurFrame = oGame.GetFrameNum()
        dSceneFlaw = { }
        for iMonster in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            dSceneFlaw[iMonster] = 1
            self.SyncMonsterKillLineAddition(iMonster)
            iBaseKillLine = self.GetFlawAttr(oMonster, FLAW_KILLLINE, iCalAddition = 0)
            iUnbalanceKillLine = self.GetFlawAttr(oMonster, FLAW_UNBALANCE_KILLLINE, iCalAddition = 0)
            iMaxKillLine = self.GetFlawAttr(oMonster, FLAW_MAXKILLLINE, iCalAddition = 0)
            lstKillLine.append([
                iMonster,
                iBaseKillLine,
                iUnbalanceKillLine,
                iMaxKillLine])
            dFlaw = self.GetFlaw(iMonster)
            if not dFlaw:
                if oMonster.m_FlawSID in self.m_FlawRange[RANGE_INFINITE]:
                    self.StartSpawnFlaw(oMonster)
                    continue
            for iFlaw, dFlawInfo in dFlaw.items():
                iEffectTime = dFlawInfo[FLAW_EFFECTTIME]
                iSpawnFrame = dFlawInfo[FLAW_SPAWNFRAME]
                iEffectTime = iEffectTime - Frame2Time(iCurFrame - iSpawnFrame)
                if iEffectTime <= 0:
                    continue
                iHitTimes = dFlawInfo[FLAW_HITTIMES]
                iSize = dFlawInfo[FLAW_SIZE]
                iIsWeakness = dFlawInfo[FLAW_ISWEAKNESS]
                lstFlaw.append([
                    iMonster,
                    iFlaw,
                    iEffectTime,
                    iHitTimes,
                    iSize,
                    iIsWeakness])
            
        
        dClearFlaw = { }
        for iMonster in self.m_Flaw:
            if iMonster in dSceneFlaw:
                continue
            dClearFlaw[iMonster] = 1
        
        for iMonster in dClearFlaw:
            oMonster = oGame.GetObject(iMonster)
            if not oMonster:
                self.m_Flaw.pop(iMonster, 0)
                continue
            self.ClearFlaw(oMonster, iSync = 0, iPop = 1)
        
        if lstKillLine:
            net.GS2CMonsterKillLine(self.m_Owner.m_PlayerID, lstKillLine)
        if lstFlaw:
            net.GS2CMonsterSpawnFlaw(self.m_Owner.m_PlayerID, lstFlaw)

    
    def AddWeaknessFlawProb(self, sKey, iPriority):
        self.m_WeaknessProb[sKey] = iPriority
        self.RefreshWeaknessFlawProb()

    
    def DisableWeaknessFlawProb(self, sKey):
        self.m_WeaknessProb.pop(sKey, 0)
        self.RefreshWeaknessFlawProb()

    
    def RefreshWeaknessFlawProb(self):
        self.m_CurWeaknessProb = sum(self.m_WeaknessProb.values())

    
    def RandomWeaknessFlaw(self, oMonster):
        dFlaw = self.GetFlaw(oMonster.m_ID)
        if dFlaw:
            for dInfo in dFlaw.values():
                if dInfo[FLAW_ISWEAKNESS] == 1:
                    return 0
            
        if oMonster.m_FlawSID not in self.m_WeaknessFlawMonster:
            return 0
        if not self.m_CurWeaknessProb:
            return 0
        if self.m_Game.Random(10000) < self.m_CurWeaknessProb:
            return 1
        return 0

    
    def AddFlawAddition(self, sAttr, sKey, iAdd, iMul, iCover):
        dAddition = self.m_FlawAddition.setdefault(sAttr, { })
        if not iCover and sKey in dAddition:
            (iOldAdd, iOldMul) = dAddition[sKey]
            iAdd += iOldAdd
            iMul += iOldMul
        dAddition[sKey] = (iAdd, iMul)
        self.RefreshFlawAddition(sAttr)

    
    def RemoveFlawAddition(self, sAttr, sKey):
        if sAttr not in self.m_FlawAddition or sKey not in self.m_FlawAddition[sAttr]:
            return None
        self.m_FlawAddition[sAttr].pop(sKey)
        self.RefreshFlawAddition(sAttr)

    
    def RefreshFlawAddition(self, sAttr):
        self.RefreshAddition(sAttr, ADDITION_HERO, None)
        if sAttr in [
            FLAW_KILLLINE,
            FLAW_UNBALANCE_KILLLINE]:
            self.SyncHeroKillLine()

    
    def AddMonsterAddition(self, iMonster, sAttr, sKey, iAdd, iMul, iCover, iAddMax = 0, iMulMax = 0):
        dAddition = self.m_MonsterAddition.setdefault(iMonster, { })
        dAttrAddition = dAddition.setdefault(sAttr, { })
        if not iCover and sKey in dAttrAddition:
            (iOldAdd, iOldMul) = dAttrAddition[sKey]
            iAdd += iOldAdd
            iMul += iOldMul
        if iAddMax and iAdd > iAddMax:
            iAdd = iAddMax
        if iMulMax and iMul > iMulMax:
            iMul = iMulMax
        dAttrAddition[sKey] = (iAdd, iMul)
        self.RefreshMonsterAddition(iMonster, sAttr)

    
    def RemoveMonsterAddition(self, iMonster, sAttr, sKey):
        if iMonster not in self.m_MonsterAddition or sAttr not in self.m_MonsterAddition[iMonster] or sKey not in self.m_MonsterAddition[iMonster][sAttr]:
            return None
        self.m_MonsterAddition[iMonster][sAttr].pop(sKey)
        self.RefreshMonsterAddition(iMonster, sAttr)

    
    def RefreshMonsterAddition(self, iMonster, sAttr):
        oMonster = self.m_Game.GetObject(iMonster)
        if not oMonster:
            return None
        self.RefreshAddition(sAttr, ADDITION_MONSTER, iMonster)
        if sAttr in [
            FLAW_KILLLINE]:
            self.SyncMonsterKillLineAddition(iMonster)

    
    def RefreshAddition(self, sAttr, iType, iTarget):
        if iType == ADDITION_HERO:
            dAddition = self.m_FlawAddition
            dCurAddition = self.m_CurFlawAddition
        elif iType == ADDITION_MONSTER:
            dAddition = self.m_MonsterAddition.setdefault(iTarget, { })
            dCurAddition = self.m_CurMonsterAddition.setdefault(iTarget, { })
        else:
            return None
        if sAttr not in dAddition or not dAddition[sAttr]:
            dCurAddition.pop(sAttr, 0)
            return None
        iAdd = 10000
        iMul = 10000
        iAccuracy = 10000
        for _Add, _Mul in dAddition[sAttr].values():
            iAdd += _Add
            if _Mul < -iAccuracy:
                _Mul = -iAccuracy
            iMul = iMul * (iAccuracy + _Mul) // iAccuracy
        
        if iAdd < 0:
            iAdd = 0
        iAttr = iAdd * iMul
        dCurAddition[sAttr] = iAttr

    
    def GetFlawAttr(self, oMonster, sAttr, iCalAddition = 1, dMsgInfo = None):
        if not oMonster or not (oMonster.m_FightType & WARRIOR_MONSTER) or oMonster.m_FlawSID not in self.m_FlawData:
            return 0
        dFlawData = self.m_FlawData[oMonster.m_FlawSID]
        if sAttr not in dFlawData:
            return 0
        if sAttr in [
            FLAW_UNBALANCE_PROB]:
            obj = self.m_Owner
        else:
            obj = oMonster
        iAttr = cl_formula.GetResultByData(obj, dFlawData[sAttr], {
            'FlawCon': self }, dMsgInfo)
        if sAttr in self.m_PlayModeAddition:
            iAttr += self.m_PlayModeAddition[sAttr]
        if iCalAddition:
            iAccuracy = 100000000
            if sAttr in self.m_CurFlawAddition:
                iAttr = iAttr * self.m_CurFlawAddition[sAttr] // iAccuracy
            iMonster = oMonster.m_ID
            if iMonster in self.m_CurMonsterAddition and sAttr in self.m_CurMonsterAddition[iMonster]:
                iAttr = iAttr * self.m_CurMonsterAddition[iMonster][sAttr] // iAccuracy
        return iAttr

    
    def GetFlawMaxCount(self, oMonster):
        dFlawData = self.m_FlawData[oMonster.m_FlawSID]
        iCalAddition = 0 if dFlawData[FLAW_LOCKMAXCOUNT] else 1
        iMaxCount = self.GetFlawAttr(oMonster, FLAW_MAXCOUNT, iCalAddition)
        if self.CheckShareFlaw(oMonster):
            iStandBy = len(self.m_ShareFlawStandBy.get(oMonster.m_FlawSID, { }))
            iMaxCount = min(iStandBy, iMaxCount)
        return iMaxCount

    
    def CanHitUnbalance(self, oMonster):
        iStartFrame = oMonster.Query(FLAW_UNBALANCE_STARTFRAME, 0)
        if not iStartFrame:
            return True
        iUnbalanceCD = Time2Frame(self.GetFlawAttr(oMonster, FLAW_UNBALANCE_COLDTIME))
        return iUnbalanceCD < self.m_Game.GetFrameNum() - iStartFrame

    
    def GetKillLine(self, oMonster, iUnbalance = 0):
        if iUnbalance or oMonster.IsUnbalance():
            iKillLine = self.GetFlawAttr(oMonster, FLAW_UNBALANCE_KILLLINE)
        else:
            iKillLine = self.GetFlawAttr(oMonster, FLAW_KILLLINE)
        iMaxKillLine = self.GetFlawAttr(oMonster, FLAW_MAXKILLLINE)
        if iKillLine > iMaxKillLine:
            iKillLine = iMaxKillLine
        return iKillLine

    
    def CheckMonsterBeExecuted(self, oMonster):
        if not (oMonster.m_FightType & WARRIOR_MONSTER) or oMonster.CheckSpecialKey(FIGHT_KEY_IGNOREEXECTORCHOOSE):
            return False
        if oMonster.IsWudi() and oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            return False
        if oMonster.m_DataSID in self.m_ImmuneExecuteMonster:
            return False
        iTentacleOwner = oMonster.Query('TentacleOwner', 0)
        if iTentacleOwner:
            oTentacleOwner = oMonster.m_Game.GetObject(iTentacleOwner)
            if oTentacleOwner:
                oMonster = oTentacleOwner
        if self.m_Owner.m_State.GetItemBySID(STATE_EXECUTE_UNBALANCE):
            iUnbalance = 1
        else:
            iUnbalance = 0
        iKillLine = self.GetKillLine(oMonster, iUnbalance)
        iRatio = (oMonster.HP() + oMonster.Shield() + oMonster.Armor()) * 10000 // (oMonster.QueryAttr('HPMax') + oMonster.QueryAttr('ShieldMax') + oMonster.QueryAttr('ArmorMax'))
        return iRatio <= iKillLine

    
    def Call_Out(self, iKey, iFrame, func):
        iCallFrame = self.m_Game.GetFrameNum() + iFrame
        if iCallFrame not in self.m_CallOut:
            self.m_CallOut[iCallFrame] = { }
        lstFunc = self.m_CallOut[iCallFrame].setdefault(iKey, [])
        lstFunc.append(func)
        if not (self.m_NextCallOutFrameNum) or iCallFrame < self.m_NextCallOutFrameNum:
            self.m_NextCallOutFrameNum = iCallFrame
            self.m_Owner.Remove_Call_Out(self.m_Flag)
            self.m_Owner.Call_Out(self.CallBack, iFrame, self.m_Flag)

    
    def CallBack(self):
        self.m_NextCallOutFrameNum = 0
        iCurFrame = self.m_Game.GetFrameNum()
        if iCurFrame in self.m_CallOut:
            dCallOut = self.m_CallOut.pop(iCurFrame)
            for lstFunc in dCallOut.values():
                for func in lstFunc:
                    func()
                
            
            dCallOut.clear()
        if self.m_CallOut:
            iNextFrameNum = min(self.m_CallOut)
            self.m_NextCallOutFrameNum = iNextFrameNum
            self.m_Owner.Call_Out(self.CallBack, iNextFrameNum - iCurFrame, self.m_Flag)

    
    def ClearTargetCallOut(self, iKey):
        dEmptyCall = { }
        for iCallFrame, dCall in self.m_CallOut.items():
            dCall.pop(iKey, { })
            if not dCall:
                dEmptyCall[iCallFrame] = 1
        
        for iCallFrame in dEmptyCall:
            self.m_CallOut.pop(iCallFrame)
        

    
    def CheckShareFlaw(self, oMonster):
        return oMonster.m_FlawSID in self.m_ShareCountMonster

    
    def RandomSpawnShareFlaw(self, iSID):
        self.m_FlawCD.pop(iSID, 0)
        oGame = self.m_Game
        iCurFrame = oGame.GetFrameNum()
        dWeight = { }
        dStandBy = self.m_ShareFlawStandBy.setdefault(iSID, { })
        dShare = self.m_ShareFlaw.get(iSID, { })
        dRemove = { }
        for iMonster, iFrame in dStandBy.items():
            oMonster = oGame.GetObject(iMonster)
            if not oMonster:
                dRemove[iMonster] = 1
                continue
            if iMonster in dShare:
                continue
            dWeight[iMonster] = iCurFrame - iFrame
        
        for iMonster in dRemove:
            dStandBy.pop(iMonster, 0)
            dShare.pop(iMonster, 0)
        
        iMonster = ChooseKey(oGame, dWeight)
        if not iMonster:
            return None
        self.SpawnFlaw(iMonster)

    
    def GetKey(self, oMonster):
        if not oMonster.m_FightType & WARRIOR_MONSTER:
            return 0
        if self.CheckShareFlaw(oMonster):
            return oMonster.m_FlawSID
        return oMonster.m_ID

    
    def CheckInFlaw(self, iMonster):
        return iMonster in self.m_Flaw

    
    def PauseCon(self, sReason):
        WarobjLog.Debug('%s pauseflaw %s %s' % (self.m_Game.m_ID, sReason, self.m_Pause))
        self.m_Pause[sReason] = 1

    
    def ResumeCon(self, sReason):
        if sReason not in self.m_Pause:
            return None
        WarobjLog.Debug('%s resumeflaw %s %s' % (self.m_Game.m_ID, sReason, self.m_Pause))
        self.m_Pause.pop(sReason, 0)
        if self.m_Pause:
            return None
        oGame = self.m_Game
        for iMonster in self.m_Flaw:
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            self.StartSpawnFlaw(oMonster)
        

    
    def OnCGStart(self, oWarMgr, dInfo):
        self.PauseCon('CG-%d' % dInfo['Behavior'])

    
    def OnCGEnd(self, oWarMgr, dInfo):
        self.ResumeCon('CG-%d' % dInfo['Behavior'])

    
    def SetFlawData(self, iFlawSID, dData):
        self.m_FlawData[iFlawSID] = dData

    
    def AddWeaknessFlawMonster(self, iFlawSID):
        if iFlawSID not in self.m_WeaknessFlawMonster:
            self.m_WeaknessFlawMonster.append(iFlawSID)

    
    def AddShareFlawMonster(self, iFlawSID):
        if iFlawSID not in self.m_ShareCountMonster:
            self.m_ShareCountMonster.append(iFlawSID)

    
    def OnDiedist(self, oOwner, dMsgInfo):
        self.PauseCon('Die')
        self.ClearAllFlaw()

    
    def OnRelife(self, oOwner, dMsgInfo):
        self.ResumeCon('Die')

    
    def CheckPreBreakFlaw(self, dMsgInfo):
        if 'Skill' not in dMsgInfo or 'CurVID' not in dMsgInfo:
            return False
        oSkill = dMsgInfo['Skill']
        iMonster = dMsgInfo['CurVID']
        lstFlaw = self.GetSkillHitFlaw(oSkill, iMonster)
        if not lstFlaw:
            return False
        dFlaw = self.GetFlaw(iMonster)
        if not dFlaw:
            return False
        if 'BreakFlaw' in oSkill.m_Update and oSkill.m_Update['BreakFlaw']:
            return True
        for iFlaw in lstFlaw:
            if iFlaw not in dFlaw:
                continue
            dHitFlaw = dFlaw[iFlaw]
            if dHitFlaw[FLAW_CURHITTIMES] + 1 >= dHitFlaw[FLAW_HITTIMES]:
                return True
        
        return False

    
    def RefreshAndGetFlawCnt(self):
        iCnt = 0
        oGame = self.m_Game
        dNewFlaw = { }
        for iMonster, dFlaw in self.m_Flaw.items():
            oMonster = oGame.GetObject(iMonster, PY_FLAG_DEAD)
            if not oMonster:
                continue
            iCnt += len(dFlaw)
            dNewFlaw[iMonster] = dFlaw
        
        self.m_Flaw = dNewFlaw
        return iCnt



def GetMonsterSceneExecutor(oMonster):
    oGame = oMonster.m_Game
    oScene = oGame.m_SceneMgr.GetScene(oMonster.m_Scene)
    if not oScene:
        return { }
    dHero = { }
    for iHero in oScene.GetHeros():
        oHero = oGame.GetObject(iHero, PY_FLAG_DIED)
        if not oHero or oHero.m_SID != EXECUTOR_HERO:
            continue
        dHero[oHero] = 1
    
    return dHero


def OnMonsterDie(oMonster, dMsgInfo):
    for oHero in GetMonsterSceneExecutor(oMonster):
        oFlawCon = oHero.m_FlawCon
        oFlawCon.ClearFlaw(oMonster, iSync = 0, iPop = 1)
        cl_msgcenter.DoneEvent(oMonster, cl_msgcenter.MSG_WAR_HATCH, COMMON_FLAG)
        if oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            cl_msgcenter.DoneEvent(oMonster, cl_msgcenter.MSG_WAR_WUDI, COMMON_FLAG, iSub = WUDI_START)
            cl_msgcenter.DoneEvent(oMonster, cl_msgcenter.MSG_WAR_WUDI, COMMON_FLAG, iSub = WUDI_END)
    


def MonsterForbidSpawnFlaw(oMonster, sKey):
    dForbid = oMonster.SetDefault('ForbidSpawnFlaw', { })
    if sKey in dForbid:
        return None
    dForbid[sKey] = 1
    if len(dForbid) > 1:
        return None
    for oHero in GetMonsterSceneExecutor(oMonster):
        oHero.m_FlawCon.ClearFlaw(oMonster, iSync = 1, iPop = 0)
    


def MonsterResumeSpawnFlaw(oMonster, sKey):
    dForbid = oMonster.Query('ForbidSpawnFlaw', { })
    if sKey not in dForbid:
        return None
    dForbid.pop(sKey, None)
    if dForbid:
        return None
    for oHero in GetMonsterSceneExecutor(oMonster):
        oHero.m_FlawCon.ResumeSpawnFlaw(oMonster)
    


def OnMonsterHatch(oMonster, dMsgInfo):
    MonsterForbidSpawnFlaw(oMonster, 'Hatch')
    cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_RELIFE, OnMonsterRelife, COMMON_FLAG, iOnce = 1)


def OnMonsterRelife(oMonster, dMsgInfo):
    MonsterResumeSpawnFlaw(oMonster, 'Hatch')


def OnMonsterWudiStart(oMonster, dMsgInfo):
    MonsterForbidSpawnFlaw(oMonster, 'Wudi')
    cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_WUDI, OnMonsterWudiEnd, COMMON_FLAG, iSub = WUDI_END, iOnce = 1)


def OnMonsterWudiEnd(oMonster, dMsgInfo):
    MonsterResumeSpawnFlaw(oMonster, 'Wudi')


def OnCustomStateEnd(oMonster, dMsgInfo):
    if dMsgInfo['StateSID'] != STATE_PETROCHEMICAL_DISSOLVE:
        return None
    cl_msgcenter.DoneEvent(oMonster, cl_msgcenter.MSG_WAR_CUSTOMSTATEEND, COMMON_FLAG)
    MonsterResumeSpawnFlaw(oMonster, 'Petrochemical')


def NewTargetFlowSID(oMonster):
    oMonster.m_FlawSID = oMonster.m_FlawSID + 10000
    return oMonster.m_FlawSID

