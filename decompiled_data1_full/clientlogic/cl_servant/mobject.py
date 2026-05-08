# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_servant/mobject.pyc
# RelativePath: clientlogic/cl_servant/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import GARDENER_PLANT_SID, DEFEND_TREND_NONE, DAM_TYPE_SCENE, DAM_TYPE_TRUE, DAM_USE_HP, BASEATTR_REFRESH, BASEATTR_CLIENT, LEVEL_TYPE_HIDE, PF_TYPE_MONSTERACT, PF_SUBMSG_SERVANT, MOVE_TYPE_JUMP, MOVE_TYPE_NORMAL, MAIN_DEBUFF, MINOR_DEBUFF, WARRIOR_SERVANT, LINK_QUIT, LINK_DISCONNECT, PF_SUBMSG_CAREERPF, EXECUTETYPE_PLANT, OBJ_ATTACK, STATE_TIME_LIMIT, STATE_TIME_FOREVER, CURE_TYPE_PERFORM, DAM_USE_ALL, MODEL_TYPE_SCALECTRLAGENT
from cl_only import GAME_FRAME, Functor, SendAlert, TraceLog, Time2Frame
from cl_object.logging import GardenerLog
import cl_warrior
import cl_facectrl
import cl_msgcenter
import cl_netattr
import cl_object.reason
import cl_formula
import cl_state
import cl_platformdata
import cl_modeldata

class CServant(cl_warrior.CWarrior):
    m_Type = 'Servant'
    m_Delete = 0
    m_DefendTrend = DEFEND_TREND_NONE
    m_Phase = 0
    m_DefaultPhase = 0
    m_PhasePF = { }
    m_AttrInfo = { }
    m_EnterDelay = GAME_FRAME
    m_RemoveDelay = 10 * GAME_FRAME
    m_FightType = WARRIOR_SERVANT
    m_HateDisEff = { }
    
    def InitServant(self, clsData, dAddData):
        clsData.InitServantData(self, dAddData)
        self.InitWarValue()
        self.InitPhasePerform()
        if 'Phase' not in dAddData:
            self.SetPhase(self.m_DefaultPhase)
        else:
            self.SetPhase(dAddData['Phase'])
        self.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(self)
        self.InitAttention()
        self.m_TransferHistory = []
        if self.m_Owner:
            oOwner = self.m_Game.GetObject(self.m_Owner)
            self.m_OwnerPlayerID = oOwner.m_PlayerID
        self.AddExtPacket('InitScaleAttr', InitScaleAttr)

    
    def Release(self):
        self.Remove_Call_Out('DelayEnterScene')
        self.ReleaseAttention()
        super(CServant, self).Release()

    
    def InitAttention(self):
        if not self.m_Owner:
            return None
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_RECEIVEDAM, Functor(SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_RECEIVEDAM), 'OnReceiveDam', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_KILL, SendKillMsg2Owner, 'OnKill', iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_PERFORM, Functor(SendOwnerMsgByVictimSub, cl_msgcenter.MSG_WAR_PERFORM), 'OnPerformDamage', iSub = self.m_SubAttackMsg, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DEALTOTALDAM, self.OnDealTotalDam, 'OnDealTotalDam', iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OwnerLeaveScene, 'OwnerLeaveScene')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, self.OwnerDieDist, 'OwnerDieDist')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, self.OnLinkStatusChange, 'OnLinkStatusChange')

    
    def ReleaseAttention(self):
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_RECEIVEDAM, 'OnReceiveDam')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_KILL, 'OnKill')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_PERFORM, 'OnPerformDamage')
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_DEALTOTALDAM, 'OnDealTotalDam')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, 'OwnerLeaveScene')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_DIEDIST, 'OwnerDieDist')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_CHANGE_PLAYER_LINKSTATUS, 'OnLinkStatusChange')

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def AddPerform(self, iPerform, iLevel, iItem = 0, iEnable = 1):
        oPerform = super().AddPerform(iPerform, iLevel, iItem, iEnable)
        if oPerform and oPerform.m_PFType == PF_TYPE_MONSTERACT:
            oPerform.m_SubMsg = PF_SUBMSG_SERVANT
        return oPerform

    
    def ResetByDie(self):
        if self.m_MoveMode != MOVE_TYPE_NORMAL:
            if self.m_MoveMode == MOVE_TYPE_JUMP:
                self.WalkTo(self.m_MoveCtrl.m_JumpStart, 'resetbydie')
            self.m_MoveMode = MOVE_TYPE_NORMAL
        super().ResetByDie()

    
    def ResetAttr(self, oServant, oHero, dMsgInfo):
        cl_formula.ResetGradeFormulaAttr(oServant, self.m_AttrInfo, self.m_Grade, BASEATTR_REFRESH)

    
    def WalkTo(self, vPos, sReason = ''):
        self.m_MoveCtrl.StopJump()
        self.OnTransfer(vPos, sReason)
        super().WalkTo(vPos, sReason)

    
    def OnTransfer(self, vPos, sReason):
        self.m_TransferHistory.append((self.m_Pos, vPos, sReason))
        if len(self.m_TransferHistory) > 10:
            self.m_TransferHistory = self.m_TransferHistory[-10:]

    
    def OnDealTotalDam(self, _oServant, dMsgInfo):
        oGame = self.m_Game
        iAttack = self.m_Owner
        oAttack = oGame.GetObject(iAttack)
        if not oAttack:
            return None
        oVictim = oGame.GetObject(dMsgInfo['CurVID'])
        if not oVictim:
            return None
        iCurFrame = oGame.GetFrameNum()
        oVictim.Set('Injured%d' % iAttack, iCurFrame)
        dInfo = { }
        dInfo.update(dMsgInfo)
        dInfo['AID'] = iAttack
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_DEALTOTALDAM, oAttack, dInfo, iSub = oVictim.m_SubAttackMsg, oGame = oGame)

    
    def OwnerLeaveScene(self, oServant, oOwner, dMsgInfo):
        self.Remove_Call_Out('DelayEnterScene')
        if self.IsDying():
            self.RealDie()
        iNewScene = dMsgInfo['NewScene']
        self.LeaveScene(iNewScene)

    
    def OwnerDieDist(self, _oServant, _oOwner, _dMsgInfo):
        oReason = cl_object.reason.CStrReason('FollowDie', None, {
            'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
        self.HPModifyDam(0, [
            [
                self.HP(),
                oReason]])

    
    def OnLinkStatusChange(self, _oServant, oOwner, _dMsgInfo):
        oAgent = self.m_Agent
        if not oAgent:
            return None
        if oOwner.Online() in (LINK_QUIT, LINK_DISCONNECT):
            oAgent.PauseAgent('LinkStatusChange')
        else:
            oAgent.ResumeAgent('LinkStatusChange')

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeServantAddPacket(self, dPlayer)

    
    def AttrCache(self):
        dData = super().AttrCache()
        dData['Phase'] = self.m_Phase
        return dData

    
    def GotoBornPos(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        iScene = oOwner.m_Scene
        if not iScene:
            return None
        tOwnerPos = oOwner.GetPos()
        tInfo = self.Query('BronPosInfo', None)
        if not tInfo:
            return None
        (fMinRadius, fMaxRadius, iMinAngle, iMaxAngle) = tInfo
        tDir = oOwner.GetFacing()
        tPos = self.m_Game.Scene_RandomPointSectorInMesh(iScene, tOwnerPos, tDir, fMinRadius, fMaxRadius, iMinAngle, iMaxAngle)
        if not tPos:
            for _ in range(5):
                fMaxRadius += 1
                tPos = self.m_Game.Scene_RandomPointSectorInMesh(iScene, tOwnerPos, tDir, fMinRadius, fMaxRadius, iMinAngle, iMaxAngle)
                if tPos:
                    break
            else:
                (ret, tPos) = self.m_Game.Scene_GetSpace(iScene, tOwnerPos)
                if not ret:
                    tPos = tOwnerPos
        self.OnTransfer(tPos, 'bornpos')
        self.Goto(iScene, tPos)

    
    def LockEnemy(self):
        return self.Query('LockEnemy', 0)

    
    def SetLockEnemy(self, iTarget):
        if iTarget == self.Query('LockEnemy', 0):
            return None
        self.Set('LockEnemy', iTarget)
        self.GS2CPropChange('LockEnemy', iTarget)

    
    def LeaveScene(self, iNewScene):
        super(CServant, self).LeaveScene(iNewScene)
        self.m_Game.m_SkillMgr.AttackLeaveScene(self.m_ID)
        if self.m_Scene:
            self.RemoveFromScene()

    
    def SetCtrlModelData(self, iScale = 100):
        dParam = {
            'ObjShape': self.m_Shape,
            'Shape': MODEL_TYPE_SCALECTRLAGENT,
            'Scale': iScale / 100 }
        self.m_ModelData = cl_modeldata.GetModel(dParam)

    
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
        self.m_Phase = iPhase
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_SWITCH_PHASE, self, {
            'OldPhase': iOldPhase,
            'NewPhase': iPhase })
        self.GS2CPropChange('Phase')
        if self.m_Phase in self.m_PhasePF:
            oPerform = self.GetPerformIfNoThenNew(self.m_PhasePF[self.m_Phase])
            if oPerform:
                oPerform.Enable(self)

    
    def HPModifyDam(self, iAttack, lstChange):
        if iAttack and iAttack != self.m_ID and iAttack != self.m_Owner:
            oAttack = self.m_Game.GetObject(iAttack)
            if oAttack and oAttack.m_OwnerPlayerID and self.CheckDamTraceCD():
                sText = f'''{self.m_Game.m_ID} servant {self.m_SID} recvdam from {oAttack.m_SID} {oAttack.m_OwnerPlayerID}'''
                SendAlert('err', sText)
                TraceLog('err', sText)
                return ([
                    0,
                    0,
                    0], [], [])
        return super().HPModifyDam(iAttack, lstChange)

    
    def Relife(self, dReason, dRelifeInfo = None):
        oOwner = self.GetOwner()
        if not oOwner or oOwner.IsRealDied():
            return None
        if 'RelifePos' in dReason:
            self.Goto(self.m_Scene, dReason['RelifePos'])
        elif not self.IsDying():
            self.GotoBornPos()
        super().Relife(dReason, dRelifeInfo = dRelifeInfo)
        self.m_MoveCtrl.E_Enable()
        oAgent = self.m_Agent
        if oAgent:
            oAgent.ResumeAgent('Die')
            oCurrentBt = oAgent.m_CurrentBT
            if oCurrentBt:
                oCurrentBt.Reset(oAgent)

    
    def InitDyingSecond(self, iSecond):
        iMaxDyingSecond = self.QuerySavedData('MaxDyingSecond')
        if iSecond > iMaxDyingSecond:
            self.SetSavedData('MaxDyingSecond', iSecond)
        self.SetDyingSecond(iSecond)

    
    def SetDyingSecond(self, iSecond):
        self.SetSavedData('RestDyingSecond', iSecond)
        self.GS2CPropChange('RestDyingSecond', iSecond)

    
    def GetRestDyingSecond(self):
        return self.QuerySavedData('RestDyingSecond')



def SendOwnerMsg(iMsg, iSub, oServant, dMsgInfo):
    oOwner = oServant.GetOwner()
    dInfo = { }
    dInfo.update(dMsgInfo)
    dInfo['AID'] = oOwner.m_ID
    if oOwner:
        cl_msgcenter.SendMsg(iMsg, oOwner, dInfo, iSub = iSub)


def SendOwnerMsgByVictimSub(iMsg, oServant, dMsgInfo):
    if 'VID' in dMsgInfo:
        iVictim = dMsgInfo['VID']
    elif 'CurVID' in dMsgInfo:
        iVictim = dMsgInfo['CurVID']
    else:
        return None
    oGame = oServant.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return None
    oAttack = oServant.GetOwner()
    if not oAttack:
        return None
    dInfo = { }
    dInfo.update(dMsgInfo)
    dInfo['OriginalAID'] = dInfo['AID']
    dInfo['AID'] = oAttack.m_ID
    cl_msgcenter.SendMsg(iMsg, oAttack, dInfo, iSub = oVictim.m_SubAttackMsg, oGame = oGame)
    if iMsg == cl_msgcenter.MSG_WAR_RECEIVEDAM:
        if 'Skill' not in dMsgInfo:
            return None
        dMsgInfo['DamFactor'][OBJ_ATTACK].update(oAttack.GetBaseDamRatio())


def SendKillMsg2Owner(oServant, dMsgInfo):
    if 'VID' not in dMsgInfo:
        return None
    iVictim = dMsgInfo['VID']
    if iVictim == oServant.m_ID:
        return None
    oGame = oServant.m_Game
    oVictim = oGame.GetObject(iVictim)
    if not oVictim:
        return None
    oAttack = oServant.GetOwner()
    if not oAttack:
        return None
    dInfo = { }
    dInfo.update(dMsgInfo)
    dInfo['OriginalAID'] = dInfo['AID']
    dInfo['AID'] = oAttack.m_ID
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_KILL, oAttack, dInfo, iSub = oVictim.m_SubAttackMsg, oGame = oGame)


class CMechServant(CServant):
    
    def InitAttention(self):
        super(CMechServant, self).InitAttention()
        if not self.m_Owner:
            return None
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF), 'OnCauseDebuff', iSub = MAIN_DEBUFF, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MINOR_DEBUFF), 'OnCauseMinorDebuff', iSub = MINOR_DEBUFF, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1), 'OnCausedFinalDebuff', iOnce = 0)
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_ADDTALENT, self.ResetAttr, 'OwnerAddTalent')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, self.ResetAttr, 'OwnerRemoveTalent')
        cl_msgcenter.AddAttentionFunc(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, self.OnLevelNodeInit, 'OnLevelNodeInit')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OwnerEnterScene, 'OwnerEnterScene')

    
    def ReleaseAttention(self):
        super(CMechServant, self).ReleaseAttention()
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, 'OnCauseDebuff', iSub = MAIN_DEBUFF)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, 'OnCauseMinorDebuff', iSub = MINOR_DEBUFF)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, 'OnCausedFinalDebuff')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_ADDTALENT, 'OwnerAddTalent')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_AFTERREMOVETALENT, 'OwnerRemoveTalent')
        cl_msgcenter.DoneAttention(self, self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEINIT, 'OnLevelNodeInit')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, 'OwnerEnterScene')

    
    def OwnerEnterScene(self, _oServant, _oOwner, _dMsgInfo):
        if not self.IsDead():
            self.Remove_Call_Out('DelayEnterScene')
            self.Call_Out(self.GotoBornPos, self.m_EnterDelay, 'DelayEnterScene')

    
    def OnLevelNodeInit(self, oServant, oWarMgr, dMsgInfo):
        if dMsgInfo['LevelType'] != LEVEL_TYPE_HIDE:
            cl_formula.ResetGradeFormulaAttr(oServant, self.m_AttrInfo, self.m_Grade, BASEATTR_REFRESH)



class CPlantServant(CServant):
    m_Delete = 1
    m_RemoveDelay = 2 * GAME_FRAME
    
    def __init__(self, oGame, nid):
        super(CPlantServant, self).__init__(oGame, nid)
        self.m_CanTransferState = { }
        self.m_Reason = ''

    
    def MapSendPacket(self, dPlayer):
        if self.m_OwnerPlayerID not in dPlayer:
            return None
        dPlayer = {
            self.m_OwnerPlayerID: 1 }
        cl_netattr.MakeServantAddPacket(self, dPlayer)

    
    def InitAttention(self):
        super(CPlantServant, self).InitAttention()
        if not self.m_Owner:
            return None
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_PERFORM_START, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_CAREERPF), 'OnCareepfStart', iSub = PF_SUBMSG_CAREERPF, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MAIN_DEBUFF), 'OnCauseDebuff', iSub = MAIN_DEBUFF, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, MINOR_DEBUFF), 'OnCauseMinorDebuff', iSub = MINOR_DEBUFF, iOnce = 0)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, Functor(SendOwnerMsg, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, -1), 'OnCausedFinalDebuff', iOnce = 0)

    
    def ReleaseAttention(self):
        super(CPlantServant, self).ReleaseAttention()
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_PERFORM_START, 'OnCareepfStart', iSub = PF_SUBMSG_CAREERPF)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, 'OnCauseDebuff', iSub = MAIN_DEBUFF)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, 'OnCauseMinorDebuff', iSub = MINOR_DEBUFF)
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, 'OnCausedFinalDebuff')

    
    def InitServant(self, clsData, dAddData):
        super().InitServant(clsData, dAddData)
        if 'InitHPRatio' in dAddData:
            self.m_HP = int(self.QueryAttr('HPMax') * dAddData['InitHPRatio'] / 100)
        oLifeTime = self.GetAttr('LifeTime')
        iLifeTime = oLifeTime.GetBaseAttr()
        if iLifeTime:
            self.SetLifeFrame(Time2Frame(iLifeTime))
        self.m_Reason = dAddData['Reason']
        self.SetDebuffInfo()

    
    def Reason(self):
        return self.m_Reason

    
    def LeaveScene(self, iNewScene):
        super().LeaveScene(iNewScene)
        self.RemoveConPlant('LeaveScene')

    
    def DieRemove(self):
        super().DieRemove()
        sReason = self.m_DeadReason.GetStrReason() if self.m_DeadReason else 'DieRemove'
        self.RemoveConPlant(sReason)

    
    def RemoveConPlant(self, sReason):
        oOwner = self.GetOwner()
        if not oOwner or not (oOwner.m_GardenerCon):
            return None
        oOwner.m_GardenerCon.RemovePlant(self.m_ID, sReason)

    
    def OwnerLeaveScene(self, oServant, oOwner, dMsgInfo):
        self.Remove('OwnerLeaveScene')

    
    def SetLifeFrame(self, iFrame):
        self.Call_Out(self.DelayDie, iFrame, 'DelayDie')

    
    def DelayDie(self):
        self.Remove_Call_Out('DelayDie')
        self.ExecuteSelf('DelayDie')

    
    def ExecuteSelf(self, sReason):
        oReason = cl_object.reason.CStrReason(sReason, None, {
            'DamType': DAM_TYPE_SCENE | DAM_TYPE_TRUE | DAM_USE_HP })
        self.Die(0, oReason)

    
    def SetCanTransferState(self, dState):
        self.m_CanTransferState.update(dState)

    
    def GetTransferState(self):
        dResult = { }
        oStateCon = self.m_State
        for iState in self.m_CanTransferState:
            lstState = oStateCon.GetItems(iState)
            if not lstState:
                continue
            if iState not in dResult:
                dResult[iState] = []
            for oState in lstState:
                dResult[iState].append([
                    oState.GetRemainTime(),
                    oState.GetCount(),
                    oState.GetArg()])
            
        
        return dResult

    
    def AddTransferState(self, dState):
        iPlantID = self.m_ID
        for iStateSID, lstStateInfo in dState.items():
            for iTime, iCount, dArg in lstStateInfo:
                iTimeType = STATE_TIME_LIMIT if iTime else STATE_TIME_FOREVER
                dArgs = {
                    'AID': iPlantID,
                    'RS': cl_object.reason.CStrReason('Transfer'),
                    'arg': dArg }
                oState = cl_state.AddState(self, iStateSID, iTimeType, iTime, dArgs)
                if not oState:
                    continue
                oState.Enable(self)
                oState.SetCount(self, iCount)
            
        

    
    def AttrCache(self):
        dData = super().AttrCache()
        oOwner = self.GetOwner()
        if oOwner:
            dData['DebuffPeriod'] = oOwner.QueryAttr('DebuffPeriod')
            dData['DebuffFactor'] = oOwner.QueryAttr('DebuffFactor')
            dData['FireAbnormalFactor'] = oOwner.QueryAttr('FireAbnormalFactor')
            dData['ThunderAbnormalFactor'] = oOwner.QueryAttr('ThunderAbnormalFactor')
            dData['CorrisionAbnormalFactor'] = oOwner.QueryAttr('CorrisionAbnormalFactor')
        return dData

    
    def SetDebuffInfo(self):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        self.m_PositiveElementFactorValue = oOwner.m_PositiveElementFactorValue
        self.m_PositiveElementFactorValueByType.update(oOwner.m_PositiveElementFactorValueByType)
        self.m_PositiveElementFactor.update(oOwner.m_PositiveElementFactor)
        self.m_PositiveElementFactorByType.update(oOwner.m_PositiveElementFactorByType)
        self.m_MustElementRestrainted.update(oOwner.m_MustElementRestrainted)
        self.m_ImmuneElementRestrainted.update(oOwner.m_ImmuneElementRestrainted)

    
    def InitPhasePerform(self):
        pass

    
    def OnSetPlantPhase(self):
        clsServantData = cl_platformdata.GetServantConfig(GARDENER_PLANT_SID)
        if not clsServantData:
            return None
        oGame = self.m_Game
        iRound = oGame.m_WarMgr.m_Round
        dBaseAttr = { }
        dClsBaseAttrInfo = clsServantData.m_BaseAttrInfo
        dBaseAttrInfo = { }
        iPhase = self.m_Phase
        if iRound in dClsBaseAttrInfo:
            dBaseAttrInfo = dClsBaseAttrInfo[iRound]
        elif dClsBaseAttrInfo:
            iCurRound = max(dClsBaseAttrInfo)
            dBaseAttrInfo = dClsBaseAttrInfo[iCurRound]
        if dBaseAttrInfo:
            if iPhase not in dBaseAttrInfo:
                iPhase = self.m_DefaultPhase
            dBaseAttr.update(dBaseAttrInfo[iPhase])
        cl_formula.ResetGradeFormulaAttr(self, dBaseAttr, self.m_Grade, BASEATTR_REFRESH)
        oReason = cl_object.reason.CStrReason('SetPlantPhase', None, {
            'DamType': CURE_TYPE_PERFORM | DAM_USE_ALL })
        iCure = self.QueryAttr('HPMax')
        dCure = {
            'MainCure': [
                [
                    iCure,
                    oReason]],
            'FlowCure': [],
            'RS': oReason }
        self.ReceiveCure(self.m_ID, dCure, iSendMsg = 0)



def InitScaleAttr(oServant, dPlayer = { }):
    if not oServant:
        return None
    if oServant.HasAttr('Scale'):
        iScale = oServant.QueryAttr('Scale')
    else:
        iScale = 100
        oServant.SetAttr('Scale', iScale, BASEATTR_REFRESH | BASEATTR_CLIENT)
    cl_netattr.GS2CPropChange(oServant, 'Scale', iScale)

