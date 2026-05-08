# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/mobject.pyc
# RelativePath: clientlogic/cl_monster/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import MG_SOURCE_KILLMONSTER, STATE_PETROCHEMICAL, FIGHT3_KEY_IGNORETHUMP, FIGHT3_KEY_IGNOREKNOCKBACK, MOVE_TYPE_JUMP, MONSTER_PART_SHIELD, MONSTER_PART_UNTAGGED, FORBID_MOVE, GetGlobalHitPartToType, WARRIOR_HERO, WARRIOR_ELITE, PATHMODE_STAYSTATUS, MONSTER_CLASSIFY_PETROCHEMICAL, STATE_TIME_LIMIT, STATE_MONSTERBORN, DEFEND_TREND_NONE, MODEL_BOX, MONSTER_CLASSIFY_MASK, STATE_MONSTER_HATCH, WARRIOR_NORMAL, HATCH_FLAG_NO, HATCH_FLAG_RUNNING, HATCH_FLAG_SUCCESS, HATCH_FLAG_FAIL, MONSTER_MAX_SUPERLEVEL, FIGHT3_KEY_IGNOREPOISON, STATUS_DEFAULT, FIGHT_KEY_UNBALANCE, WARRIOR_BOSS, HP_RADIO_SUB, MODEL_TYPE_SCALECTRLAGENT, WARRIOR_NORLARGESUMMON, THUMP_TYPE_NORMAL, THUMP_TYPE_TRAP, PLAYMODE_ROGUELIKE, STATE_KNOCKER_AIR
from cl_commondefines import WARRIOR_NORFLY
from cl_object.reason import CStrReason
from cl_only import GAME_FRAME, Time2Frame, TraceMsg, Functor, SendAlert
from cl_object.logging import WarobjLog, SceneLog, BehaviorLog
import cl_warrior
import cl_netattr
import cl_msgcenter
import cl_monster.monsterstatus
import cl_facectrl
import cl_snetwar
import cl_math
import cl_modeldefine
import cl_betree.monsteragent as monsteragent
import cl_reward
import cl_perform
import cl_state
import cl_notify
import cl_warmgr.levelline.linespawnaction as linespawnaction
import cl_action
import cl_forbid
import cl_modeldata
import cl_engphyobj
import cllib.lib_flag
import cl_object.dielog
from . import monsterattradjust, monsterrewardadjust

class CMonster(cl_warrior.CWarrior):
    m_Type = 'Monster'
    m_Delete = 1
    m_ModelType = MODEL_BOX
    m_Reward = { }
    m_DefaultPhase = 0
    m_PhasePF = { }
    m_PhaseHitPartToType = { }
    m_AttrPlusPF = ()
    m_DefendTrend = DEFEND_TREND_NONE
    m_RemoveDelay = 10 * GAME_FRAME
    m_CombatForce = 0
    m_RunSpeedUpMul = 0
    m_SprintSpeedUpMul = 0
    m_BornActionInfo = { }
    m_BornActionEndFrame = 0
    m_AccuracyFactor = 0
    m_MissingDisType = { }
    m_AttachCtrl = None
    m_DodgeCDFrame = 0
    m_AddGrade = 0
    m_DemonReward = 0
    m_SurvivorGSCash = 0
    m_ExtraPerform = { }
    m_Hatch = HATCH_FLAG_NO
    m_AreaIndex = 0
    
    def __init__(self, oGame, nid):
        super(CMonster, self).__init__(oGame, nid)
        self.m_DataSID = 0
        self.m_AttrAdjust = monsterattradjust.CBaseAttrAdjust()
        self.m_RewardAdjust = monsterrewardadjust.CBaseRewardAdjust()
        self.m_MonsterSummon = { }
        self.m_Phase = 0
        self.m_SuperLevel = 0
        self.m_NeedLockHeroEnemyNotify = True
        self.m_ReceivedDamInfo = { }
        self.m_CurveCompute = None
        self.m_UseFlyNav = 0
        self.m_DieLogMgr = None

    
    def InitMonster(self, clsData, dAddData):
        clsData.InitMonsterData(self, dAddData)
        self.Set('Scale', 100)
        self.InitWarValue()
        self.InitPhasePerform()
        self.InitExtraPerform()
        self.m_MoveStatusMgr = cl_monster.monsterstatus.CMoveStatusMgr(self)
        self.m_FightStatusMgr = cl_monster.monsterstatus.CFightStatusMgr(self)
        (self.m_PreDodgeTime, self.m_DodgeTime, self.m_PostDodgeTime) = cl_modeldefine.GetModelDefine(self.m_Shape, 'Dodge')
        if self.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            WarobjLog.Debug('%d initboss %d' % (self.m_Game.m_ID, self.m_SID))
            self.m_DieLogMgr = cl_object.dielog.CDieLogMgr(self.m_Game, self.m_ID)
        if self.m_FightType == WARRIOR_NORFLY:
            if cllib.lib_flag.g_UseFlyNav:
                self.m_UseFlyNav = 1
            else:
                self.m_FightType = WARRIOR_NORMAL

    
    def OnInitToScene(self, tPos):
        super(CMonster, self).OnInitToScene(tPos)
        self.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(self)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DIE, OnMonsterDie, 'MonsterReward')

    
    def Release(self):
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_REVTOTALDAM, 'AddDamStats')
        oPart = self.m_Game.GetObject(self.m_Part)
        if oPart:
            oPart.Remove('DieRemove')
        if self.m_DieLogMgr:
            self.m_DieLogMgr.Release()
        super().Release()

    
    def EnterScene(self, iOldScene):
        super(CMonster, self).EnterScene(iOldScene)
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        iLevelID = oScene.m_Level
        self.m_AttrAdjust.SetLevelID(iLevelID)
        self.m_AttrAdjust.DoneAllAttrAdjust(self)
        self.m_RewardAdjust.DoneAllRewardAdjust(self)
        self.SetPhase(self.m_DefaultPhase)
        if self.m_BornActionInfo:
            lstAction = list(self.m_BornActionInfo.keys())
            iRandIndex = self.m_Game.Random(len(lstAction))
            sAction = lstAction[iRandIndex]
            cl_snetwar.GS2CMonsterActionSM(self, 1, sAction, 0)
            iFrame = Time2Frame(self.m_BornActionInfo[sAction])
            oState = cl_state.AddState(self, STATE_MONSTERBORN, STATE_TIME_LIMIT, iFrame, {
                'AID': self.m_ID,
                'RS': CStrReason('Born') })
            oState.Enable(self)
            self.m_BornActionEndFrame = self.m_Game.GetFrameNum() + iFrame
        if self.m_FightType & MONSTER_CLASSIFY_MASK == MONSTER_CLASSIFY_PETROCHEMICAL:
            self.m_MoveCtrl.SetPathMode('Petrochemical', PATHMODE_STAYSTATUS)

    
    def LeaveScene(self, iNewScene):
        super(CMonster, self).LeaveScene(iNewScene)
        self.m_AttrAdjust.ClearAllAttrAdjust(self)
        self.m_AttrAdjust.SetLevelID(0)
        self.m_FaceCtrl.Release()
        self.m_AttachCtrl = None

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeMonsterAddPacket(self, dPlayer)

    
    def NetAddTo(self, dPlayer):
        super(CMonster, self).NetAddTo(dPlayer)
        tSuperInfo = self.Query('MonsterSuper')
        if tSuperInfo:
            (iPlusPF, iAfPF) = tSuperInfo
            cl_snetwar.GS2CMonsterSuperInfo(self.m_Game, iAfPF, iPlusPF, self.m_ID, dPlayer)
        oPart = self.m_Game.GetObject(self.m_Part)
        if oPart:
            oPart.PartNetAddTo(dPlayer)

    
    def WalkTo(self, tPos, sReason = ''):
        if self.m_SID in (21641, 21651, 22831, 32831):
            (ret, tPos) = self.m_Game.Scene_GetSpace(self.m_Scene, tPos)
            if not ret:
                iScene = self.m_Scene
                oScene = self.m_Game.m_SceneMgr.GetScene(iScene)
                iLevel = oScene.m_Level if oScene else 0
                tCur = self.GetPos()
                WarobjLog.Alert(f'''walk to errpos {iLevel} {tCur} {tPos}''')
                if cllib.lib_flag.g_IsInternalRun:
                    TraceMsg()
                return None
        super(CMonster, self).WalkTo(tPos, sReason)

    
    def OnStartMove(self, dInfo):
        if self.m_Agent:
            (dx, dz) = dInfo['MoveDir']
            self.m_Agent.OnNextPath(self, dx, dz)

    
    def SetCtrlModelData(self, iScale = 100):
        dParam = {
            'ObjShape': self.m_Shape,
            'Shape': MODEL_TYPE_SCALECTRLAGENT,
            'Scale': iScale / 100 }
        self.m_ModelData = cl_modeldata.GetModel(dParam)

    
    def SetModelScale(self, iScale, iChangeClientMode = 1):
        if iChangeClientMode:
            self.Set('Scale', iScale)
            cl_netattr.GS2CPropChange(self, 'Scale', iScale)
        self.SetCtrlModelData(iScale)
        self.m_ModelRadius = self.m_ModelData.GetModelRadius()
        self.m_ModelHeight = self.m_ModelData.GetModelHeight()
        if self.m_PhyModel:
            self.m_PhyModel.E_Unstall()
            (iPaType, iNavType, iLayer, dParam) = self.GetModelAttr()
            self.m_PhyModel = cl_engphyobj.CreatePhyModel(self, iPaType, iLayer, dParam)

    
    def MoveStatus(self):
        return self.m_MoveStatusMgr.GetCurStatus()

    
    def FightStatus(self):
        return self.m_FightStatusMgr.GetCurStatus()

    
    def LockEnemy(self):
        return self.Query('LockEnemy', 0)

    
    def SetLockEnemy(self, iTarget):
        iOldTarget = self.Query('LockEnemy')
        if iOldTarget == 0 or iTarget != 0:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MONSTER_START_HATE, self, {
                'LockEnemy': iTarget })
        elif iTarget == 0:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MONSTER_END_HATE, self, {
                'OldTarget': iOldTarget })
        elif iOldTarget != iTarget:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MONSTER_UPDATE_HATE, self, {
                'OldTarget': iOldTarget,
                'LockEnemy': iTarget })
        self.Set('LockEnemy', iTarget)
        self.GS2CPropChange('LockEnemy', iTarget)
        if self.m_NeedLockHeroEnemyNotify and self.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            oGame = self.m_Game
            oTarget = oGame.GetObject(iTarget)
            if oTarget and oTarget.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
                lstPlayer = oGame.GetRealPlayers()
                cl_notify.SendCommonNotify(oGame, lstPlayer, 2222, {
                    '$$player': oTarget.m_OwnerName,
                    '$monster': self.m_Name })
                self.m_NeedLockHeroEnemyNotify = False

    
    def AttrCache(self):
        dData = super().AttrCache()
        dData['Phase'] = self.m_Phase
        return dData

    
    def GetDieReward(self):
        if not self.m_Reward:
            return { }
        iRound = self.m_Game.m_WarMgr.m_Round
        dReward = self.m_Reward
        if iRound not in dReward:
            iRound = sorted(dReward)[0]
        return dReward[iRound]

    
    def OnForbid(self, iRule, dForbid, sReason):
        super(CMonster, self).OnForbid(iRule, dForbid, sReason)
        if FORBID_MOVE in dForbid:
            if self.m_MoveCtrl:
                self.m_MoveCtrl.OverArrive(self, iFail = 1, iCallBack = 1)
            self.Stop()

    
    def Phase(self):
        return self.m_Phase

    
    def InitPhasePerform(self):
        for iPerform in self.m_PhasePF.values():
            self.AddPerform(iPerform, 1, iItem = 0, iEnable = 0)
        

    
    def SetPhase(self, iPhase):
        if iPhase == self.m_Phase:
            return None
        if self.m_Phase in self.m_PhasePF:
            oPerform = self.m_Perform.GetPerform(self.m_PhasePF[self.m_Phase])
            if oPerform:
                oPerform.Disable(self)
        iOldPhase = self.m_Phase
        if self.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS:
            WarobjLog.Debug('%d setphase %d %d %d %d' % (self.m_Game.m_ID, self.m_SID, self.m_Phase, iPhase, self.m_HP))
        self.m_Phase = iPhase
        self.GS2CPropChange('Phase')
        if self.m_Phase in self.m_PhasePF:
            oPerform = self.GetPerform(self.m_PhasePF[self.m_Phase])
            if oPerform:
                oPerform.Enable(self)
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SWITCH_PHASE, self, {
                    'OldPhase': iOldPhase,
                    'NewPhase': self.m_Phase })

    
    def InitExtraPerform(self):
        if not self.m_ExtraPerform:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        iRound = oWarMgr.m_Round
        iCycle = oWarMgr.m_Cycle
        dExcludePassive = self.GetExcludePassive(iRound, iCycle)
        for iCurRound in range(1, iRound + 1):
            for iCurCycle in range(0, iCycle + 1):
                tRoundKey = (iCurRound, iCurCycle)
                if tRoundKey in self.m_ExtraPerform['Round']:
                    for iPerform in self.m_ExtraPerform['Round'][tRoundKey]:
                        if iPerform in dExcludePassive:
                            continue
                        self.AddPerform(iPerform, 1)
                    
            
        
        for iModeType in oWarMgr.m_ModeType:
            if iModeType in self.m_ExtraPerform['Mode']:
                for iPerform in self.m_ExtraPerform['Mode'][iModeType]:
                    self.AddPerform(iPerform, 1)
                
        

    
    def GetExcludePassive(self, iRound, iCycle):
        dExcludePassive = { }
        dAllMonsterExcludePassive = self.m_Game.m_WarData.GetMonsterExcludePassive()
        if self.m_SID in dAllMonsterExcludePassive and (iRound, iCycle) in dAllMonsterExcludePassive[self.m_SID]:
            dExcludePassive = dAllMonsterExcludePassive[self.m_SID][(iRound, iCycle)]
        return dExcludePassive

    
    def SuperLevel(self):
        return self.m_SuperLevel

    
    def MonsterSuper(self, iSuperLevel, iPlusPF, iAfPF):
        if self.m_SuperLevel > 0:
            return None
        if iSuperLevel <= 0:
            return None
        if iSuperLevel > MONSTER_MAX_SUPERLEVEL:
            iSuperLevel = MONSTER_MAX_SUPERLEVEL
        self.m_SuperLevel = iSuperLevel
        oGame = self.m_Game
        oPart = oGame.GetObject(self.m_Part)
        dMsgInfo = {
            'PlusPFEnable': 1,
            'AfPFEnable': 1,
            'AfPF': iAfPF }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MONSTER_SUPER_BEFORE, self, dMsgInfo)
        iPlusPFEnable = dMsgInfo['PlusPFEnable']
        iAfPFEnable = dMsgInfo['AfPFEnable']
        iAfPF = dMsgInfo['AfPF']
        if iPlusPF and iPlusPF in self.m_AttrPlusPF:
            self.AddPerform(iPlusPF, 1, iEnable = iPlusPFEnable)
            if oPart:
                oPart.AddPerform(iPlusPF, 1, iEnable = iPlusPFEnable)
        if iAfPF:
            cls = cl_perform.GetPerformModule(iAfPF)
            iLevel = min(self.m_SuperLevel, cls.m_MaxLevel)
            self.AddPerform(iAfPF, iLevel, iEnable = iAfPFEnable)
            if oPart:
                oPart.AddPerform(iAfPF, iLevel, iEnable = iAfPFEnable)
        self.Set('MonsterSuper', (iPlusPF, iAfPF))
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MONSTER_SUPER, self, { })
        WarobjLog.Debug('monstersuperinfo: %s %s %s %s %s %s %s %s' % (oGame.m_ID, self.m_SID, self.m_Owner, iSuperLevel, iPlusPF, iPlusPFEnable, iAfPF, iAfPFEnable))
        self.NotifySuperInfo()
        lstArgs = self.m_Game.m_WarMgr.Query('DebugMonster', ())
        if 'strengthen' in lstArgs:
            import cl_gamegm
            cl_gamegm.SendMonsterDebugInfo(self)

    
    def ClearMonsterSuper(self):
        tSuperInfo = self.Query('MonsterSuper')
        if not tSuperInfo:
            return None
        (iPlusPF, iAfPF) = tSuperInfo
        if not iPlusPF and not iAfPF:
            return None
        self.m_SuperLevel = 0
        self.RemovePerform(iPlusPF)
        self.RemovePerform(iAfPF)
        oGame = self.m_Game
        oPart = oGame.GetObject(self.m_Part)
        if oPart:
            oPart.RemovePerform(iPlusPF)
            oPart.RemovePerform(iAfPF)
        self.Set('MonsterSuper', (0, 0))
        WarobjLog.Debug('clearmonstersuper: %s %s %s %s %s' % (oGame.m_ID, self.m_SID, self.m_Owner, iPlusPF, iAfPF))
        self.NotifySuperInfo()
        self.Delete('MonsterSuper')

    
    def NotifySuperInfo(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        if not oScene:
            return None
        self.GS2CPropChange('SuperLevel')
        tSuperInfo = self.Query('MonsterSuper')
        (iPlusPF, iAfPF) = tSuperInfo
        dPlayer = oScene.GetPlayers()
        cl_snetwar.GS2CMonsterSuperInfo(self.m_Game, iAfPF, iPlusPF, self.m_ID, dPlayer)

    
    def GetDamTypeByPart(self, iHitPart):
        iDamType = 0
        dHitPartToType = GetGlobalHitPartToType()
        if iHitPart in dHitPartToType:
            iDamType = dHitPartToType[iHitPart]
        if self.m_Phase in self.m_PhaseHitPartToType:
            dHitPartToType = self.m_PhaseHitPartToType[self.m_Phase]
            if iHitPart in dHitPartToType:
                iDamType = dHitPartToType[iHitPart]
        return iDamType

    
    def SetDemonReward(self, iReward):
        self.m_DemonReward = iReward

    
    def IsDemonReward(self):
        return self.m_DemonReward

    
    def GetThumped(self, dData, iProb = 0, iClient = 1):
        iCurFrame = self.m_Game.GetFrameNum()
        sKey = 'Struck'
        if (iCurFrame < self.Query('ActionFrame') or 'IgnoreStruckCD' not in dData) and iCurFrame < self.Query(sKey, (0, 0))[0]:
            return 0
        iHitPart = MONSTER_PART_UNTAGGED
        if 'Skill' in dData and 'CurHitArea' in dData['Skill'].m_Update:
            iHitPart = dData['Skill'].m_Update['CurHitArea']
            if iHitPart == MONSTER_PART_SHIELD:
                return 0
        if self.CheckThump(dData, iProb):
            if self.CheckThumpInfo(dData):
                return 0
            if 'ThumpFrame' in dData:
                iActionFrame = dData['ThumpFrame']
            else:
                iActionFrame = self.QueryAttr('ThumpFrame')
            if not iActionFrame:
                BehaviorLog.Alert('怪物%d %s重击动作时长为0, %s' % (self.m_SID, sKey, dData.get('RS', '')))
                iActionFrame = 1
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_THUMPED, self, dData, oGame = self.m_Game)
            iActionFrame = self.GetChangeSpeedDelayFrame(iActionFrame)
            iStruckIgnoreFrame = self.QueryAttr('StruckIgnoreFrame')
            iActionEndFrame = iActionFrame + iCurFrame
            self.Set(sKey, (iActionEndFrame + iStruckIgnoreFrame, iStruckIgnoreFrame))
            self.Set('ActionFrame', iActionEndFrame)
            monsteragent.Struck(self, sKey, iActionFrame)
            if iClient:
                cl_snetwar.GS2CStruckMonster(self, THUMP_TYPE_NORMAL, iHitPart)
            (fMoveSecond, fMaxDis) = cl_modeldefine.GetModelDefine(self.m_Shape, 'Thump')
            if fMoveSecond and fMaxDis and 'Skill' in dData:
                fSpeed = fMaxDis / fMoveSecond
                oSkill = dData['Skill']
                dCartoon = oSkill.GetCurCartoon()
                if 'cls' in dCartoon:
                    vStart = dCartoon['cls'].GetPushStart(oSkill, dCartoon)
                else:
                    vStart = oSkill.m_Base['vStart']
                vDir = cl_math.Vec3Minus(self.m_Pos, vStart)
                if self.m_MoveCtrl:
                    self.m_MoveCtrl.PushMove(self, vDir, fSpeed, fMoveSecond, iClientAni = 0)
            return 1
        return 0

    
    def CheckThumpInfo(self, dData):
        if 'Skill' not in dData:
            return 0
        oSkill = dData['Skill']
        if 'IsThump' in oSkill.m_Cache and oSkill.m_Cache['IsThump'] == 1:
            return 1
        if 'ThumpInfo' not in oSkill.m_Cache:
            return 0
        dThump = oSkill.m_Cache['ThumpInfo']
        if self.m_ID not in dThump:
            return 0
        if dThump[self.m_ID] == 0:
            dThump[self.m_ID] = 1
            return 0
        return 1

    
    def GetKnockedBack(self, dData, iProb):
        iCurFrame = self.m_Game.GetFrameNum()
        if iCurFrame < self.Query('Struck', (0, 0))[0]:
            return 0
        if self.CheckKnockBack(iProb):
            iActionFrame = self.QueryAttr('KnockBackFrame')
            iActionFrame = self.GetChangeSpeedDelayFrame(iActionFrame)
            if not iActionFrame:
                WarobjLog.Alert('怪物%d击退动作时长为0 请检查小怪表属性配置' % self.m_SID)
                iActionFrame = 1
            monsteragent.KnockedBack(self, iActionFrame)
            return 1
        return 0

    
    def CheckKnockBack(self, iBasicProb):
        if not iBasicProb:
            return 0
        if self.m_MoveMode == MOVE_TYPE_JUMP:
            return 0
        if self.CheckLogicKey(FIGHT3_KEY_IGNOREKNOCKBACK):
            return 0
        iDef = self.QueryAttr('DefKnockBack')
        if not self.Query('ForceKnock', 0) and self.m_Game.Random(10000) >= iBasicProb - iDef:
            return 0
        return 1

    
    def CheckThump(self, dData, iBasicProb):
        if self.m_MoveMode == MOVE_TYPE_JUMP:
            return 0
        if self.CheckLogicKey(FIGHT3_KEY_IGNORETHUMP):
            return 0
        if 'Skill' in dData:
            iBasicProb += dData['Skill'].m_Cache.get('ThumpProb', 0)
        if not iBasicProb:
            return 0
        iDef = self.QueryAttr('DefThump')
        if self.m_Game.Random(10000) >= iBasicProb - iDef:
            return 0
        return 1

    
    def StruckChangeSpeed(self, sOldKey, dFrameShaft):
        monsteragent.StruckChangeSpeed(self, sOldKey, dFrameShaft)

    
    def IsPetrochemical(self):
        lstState = self.m_State.GetItems(STATE_PETROCHEMICAL)
        if lstState:
            return True
        return False

    
    def GetTrapThumped(self):
        iCurFrame = self.m_Game.GetFrameNum()
        sKey = 'TrapThump'
        if iCurFrame < self.Query('TrapThump') or iCurFrame < self.Query('ActionFrame'):
            return 0
        iActionFrame = self.QueryAttr('ThumpFrame')
        iActionEndFrame = iCurFrame + iActionFrame
        self.Set('ActionFrame', iActionEndFrame)
        self.Set(sKey, iActionEndFrame)
        monsteragent.Struck(self, sKey, iActionFrame)
        cl_snetwar.GS2CStruckMonster(self, THUMP_TYPE_TRAP, MONSTER_PART_UNTAGGED)
        return 1

    
    def Unbalance(self, iSourceTarget):
        if self.IsDead():
            return None
        sKey = 'Unbalance'
        self.AddBitAttr('SpecialKey', sKey, FIGHT_KEY_UNBALANCE, bSync = False)
        if self.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            monsteragent.Unbalance(self)
            sResetState = self.Query('UnbalanceResetState', 'reset')
            cl_snetwar.GS2CMonsterActionSM(self, 1, sResetState, 0)
            self.Set('OldMoveState', self.m_MoveStatusMgr.GetCurStatus())
            self.m_MoveStatusMgr.ChangeStatus(self, STATUS_DEFAULT)
            self.AttrForceSet('MoveSpeed', 0, sKey)
        self.SetImmobilize(sKey, iSourceTarget)

    
    def ClearUnbalance(self, iSourceTarget):
        sKey = 'Unbalance'
        self.ClearBitAttr('SpecialKey', sKey, FIGHT_KEY_UNBALANCE, bSync = False)
        self.ClearImmobilize(sKey, iSourceTarget)
        if self.m_FightType & WARRIOR_BOSS != WARRIOR_BOSS:
            iOldMoveState = self.Query('OldMoveState', 0)
            if iOldMoveState:
                self.Delete('OldMoveState')
                self.m_MoveStatusMgr.ChangeStatus(self, iOldMoveState)
            if 'MoveSpeed' in self.m_PrivateAttr:
                self.AttrForceClear('MoveSpeed', sKey)
            if not self.IsDead():
                sResetState = self.Query('UnbalanceResetState', 'reset')
                cl_snetwar.GS2CMonsterActionSM(self, 1, sResetState, 0)

    
    def EnterDie(self, iAttack, oReason):
        if self.IsHatching():
            self.SetHatchFlag(HATCH_FLAG_FAIL, iHatchTime = 0)
        super().EnterDie(iAttack, oReason)

    
    def SetHatchFlag(self, iFlag, iHatchTime):
        self.m_Hatch = iFlag
        cl_snetwar.GS2CHatch(self, iFlag, iHatchTime)

    
    def IsHatching(self):
        return self.m_Hatch == HATCH_FLAG_RUNNING

    
    def Hatch(self, dReason, dHatchInfo):
        iHPMax = (self.QueryAttr('HPMax') + self.QueryAttr('ShieldMax') + self.QueryAttr('ArmorMax')) * dHatchInfo['Ratio'] // 100
        dArg = {
            'HPMax': iHPMax,
            'ShieldMax': 0,
            'ArmorMax': 0 }
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        iTime = 0
        if oLevelCtrl:
            iLayerNum = oLevelCtrl.m_LayerNum
            iTime = int(self.m_Game.GetWarData().GetMonsterRelifeTime().get(iLayerNum, 0))
        if not iTime:
            iTime = dHatchInfo['Time']
        iFrame = Time2Frame(iTime)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_HATCH, self, { })
        self.ResetByDie()
        self.HatchClearEffect()
        self.SetHatchFlag(HATCH_FLAG_RUNNING, iHatchTime = iTime)
        oState = cl_state.AddState(self, STATE_MONSTER_HATCH, STATE_TIME_LIMIT, iFrame, {
            'AID': self.m_ID,
            'RS': CStrReason('孵化'),
            'arg': dArg })
        if oState:
            oState.Enable(self)
        self.TrueModify('HP', None, self.QueryAttr('HPMax') - self.m_HP)
        self.Remove_Call_Out('HatchRelife')
        self.Call_Out(Functor(self.HatchOver, dReason, dHatchInfo['RelifeInfo']), iFrame, 'HatchRelife')

    
    def OnHatch(self):
        pass

    
    def HatchOver(self, dReason, dRelifeInfo = None):
        if self.IsDead():
            return None
        self.SetHatchFlag(HATCH_FLAG_SUCCESS, iHatchTime = 0)
        self.Relife(dReason, dRelifeInfo)
        self.UnForbid(cl_forbid.HATCH_RULE, '孵化禁止')

    
    def HatchClearEffect(self):
        cl_action.HaltAllCasting(self, 'Hatch')
        self.Forbid(cl_forbid.HATCH_RULE, '孵化禁止')

    
    def AddHatchRatio(self, iOwnerSID, iType, sKey, dHatchRatio):
        if not dHatchRatio:
            SendAlert('err', '怪物复活属性: 孵化血量比例未配置 被动: %d' % iOwnerSID)
            return None
        if self.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
            self._AddHatchRatio(iType, sKey, dHatchRatio['Elite'])
        elif self.m_FightType & WARRIOR_NORMAL == WARRIOR_NORMAL:
            self._AddHatchRatio(iType, sKey, dHatchRatio['Normal'])
        else:
            SendAlert('err', 'Boss%d 设置了复活属性 被动: %d' % (self.m_SID, iOwnerSID))

    
    def _AddHatchRatio(self, iType, sKey, iRatio):
        dHatchRatio = self.SetDefault('HatchRatio', { })
        dHatchRatio[(iType, sKey)] = iRatio

    
    def AddDamRecord(self, iIgnorePosion):
        iStatus = self.Query('DebugStatus', 0)
        if iStatus:
            if iIgnorePosion:
                self.AddBitAttr('LogicKey', 'gm', FIGHT3_KEY_IGNOREPOISON)
            cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_REVTOTALDAM, self.ReceivedDamRecord, 'AddDamStats', -1, 0)
            self.AddHPThreshold(1, HP_RADIO_SUB, 'AddDamStats', self.DebugHPThreshold)
            cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_REMOVEOBJ, self.DebugClearHPThreshold, 'AddDamStats', -1, 0)

    
    def InitReceivedDamRecord(self):
        self.DebugHPModifyCureFull()
        iNowFrame = self.m_Game.GetFrameNum()
        self.m_ReceivedDamInfo = {
            'TotalDam': 0,
            'Dps': 0,
            'MaxDam': 0,
            'StartFrame': iNowFrame,
            'LastFrame': iNowFrame }

    
    def ReceivedDamRecord(self, oOwner, dMsgInfo):
        if not self.m_ReceivedDamInfo:
            self.InitReceivedDamRecord()
        iNowFrame = self.m_Game.GetFrameNum()
        iDelayFrame = iNowFrame - self.m_ReceivedDamInfo['LastFrame']
        if iDelayFrame > Time2Frame(1200):
            self.InitReceivedDamRecord()
        dInfo = self.m_ReceivedDamInfo
        iDam = 0
        for iTrueChange, _ in dMsgInfo['TrueChange']:
            iDam += iTrueChange
        
        for iExcessChange, _ in dMsgInfo['ExcessChange']:
            iDam += iExcessChange
        
        dInfo['TotalDam'] += iDam
        iFrame = iNowFrame - dInfo['StartFrame']
        if iFrame == 0:
            iFrame = 1
        dInfo['Dps'] = dInfo['TotalDam'] * GAME_FRAME // iFrame
        if iDam > dInfo['MaxDam']:
            dInfo['MaxDam'] = iDam
        dInfo['LastFrame'] = iNowFrame
        cl_snetwar.GS2CReceivedDamRecord(self.m_Game, self, dInfo)

    
    def DebugHPThreshold(self, oOwner, dMsgInfo):
        self.DebugHPModifyCureFull()

    
    def DebugClearHPThreshold(self, oOwner, dInfo):
        self.ClearHPThresholdByKey(HP_RADIO_SUB, 'AddDamStats')



def OnMonsterDie(oTarget, dMsgInfo):
    oGame = oTarget.m_Game
    iMonsterSID = oTarget.m_SID
    dBehavior = oGame.m_WarMgr.Query('OneTimeClientBehavior', { })
    if iMonsterSID in dBehavior:
        linespawnaction.TriggerOneTimeClientBehavior(oGame, dBehavior[iMonsterSID])
    if not oTarget.m_Reward:
        return None
    dReward = oTarget.m_Reward
    oTarget.m_Reward = { }
    if not dReward:
        return None
    iAttack = dMsgInfo['AID']
    iRound = oGame.m_WarMgr.m_Round
    if iRound not in dReward:
        cl_notify.GS2CDebugMsg(oGame, iAttack, '未配置战场%d小怪%s周目%d掉落' % (oGame.m_WarMgr.m_SID, oTarget.m_SID, iRound))
        iRound = sorted(dReward)[0]
    dReward = dReward[iRound]
    iFlag = 0 if oTarget.IsDemonReward() else 1
    dExtInfo = {
        'CalOffset': 0,
        'CheckGoldenCup': 1,
        'Abandoner': oTarget.m_ID,
        'CanReward': iFlag,
        'AutoReward': iFlag }
    dMGInfo = cl_reward.RewardItemByMiniGame(oTarget, iAttack, dReward, 'MonsterReward%d' % iAttack, MG_SOURCE_KILLMONSTER, dExtInfo)
    cl_reward.CreateDemon(oGame, oTarget.m_ID, dMGInfo)

