# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/levelline/leveltrigger.pyc
# RelativePath: clientlogic/cl_warmgr/levelline/leveltrigger.pyc
# Source Generated with Decompyle++
# File: leveltrigger.pyc (Python 3.6)

from cl_commondefines import WARRIOR_MONSTER, TRIGGER_CLIENTBUTTON, ARMOR_RADIO_SUB, TRIGGER_GROUPREST, TRIGGER_SCEVTTOPOLOGY, TRIGGER_BUILDINTERACT, TRIGGER_ROOMGOAL, TRIGGER_NPCSCENEEVT, TRIGGER_KILLPETROCHEMICALGROUP, TRIGGER_ROOMCHALLENGE, TRIGGER_MIXTHRESHOLD, TRIGGER_WARSERIAL, TRIGGER_PICKITEM, TRIGGER_LEVELFINISH, TRIGGER_LEVELGOAL, TRIGGER_NPCINTERACT, TRIGGER_BULLETCHANGE, TRIGGER_DUALWIELD, TRIGGER_HPTHRESHOLD, TRIGGER_SCEVTHOLD, TRIGGER_KILLGROUP, TRIGGER_KILLMONSTER, TRIGGER_SCENEEVT, HP_RADIO_SUB, WARRIOR_PROTEGE_NORMAL, HP_TYPE_NORMAL, HP_TYPE_ARMOR, TRIGGER_INIT, STATE_PETROCHEMICAL, NWARRIOR_NPC_CAR, HP_TYPE_SHIELD, SHIELD_RADIO_SUB, SCENE_EVT_ENTER, WARRIOR_HERO, SCENE_EVT_LEAVE, TRIGGER_TYPE_DEFAULT, TRIGGER_TYPE_LINE, TRIGGER_TYPE_SCENE, TRIGGER_BUILDALIVE, SURVIVOR_TRIGGER_PHASESTART, SURVIVOR_TRIGGER_OCCUPYPROCESS, PHASE_CHALLENGE_SINGLEPOINTOCCUPY, SURVIVOR_TRIGGER_HPTHRESHOLD, SURVIVOR_TRIGGER_KILLMONSTERGROUPNUM, SURVIVOR_TRIGGER_KILLGROUP, PLAYMODE_NEWSURVIVOR, TRIGGER_JUDGECYCLE, JUDGE_LOGIC_GREATER, JUDGE_LOGIC_LESS, JUDGE_LOGIC_EQUAL, JUDGE_LOGIC_GREATER_EQUAL, JUDGE_LOGIC_LESS_EQUAL, JUDGE_LOGIC_NO_EQUAL
from cl_only import Functor, WeakProxy, SendAlert, PY_FLAG_DEAD
import cl_msgcenter
import cl_formula
ONCE_TRIGGER = 1
HOLD_TRIGGER = 2

class CLevelTriggerMgr(object):
    
    def __init__(self, oLevelCtrlMgr):
        self.m_LevelCtrl = oLevelCtrlMgr
        self.m_Game = oLevelCtrlMgr.m_Game
        self.m_RuleComponent = { }
        dRuleClass = { }
        dRuleClass.update(g_RuleClass)
        if self.m_Game.m_WarMgr.m_PlayMode == PLAYMODE_NEWSURVIVOR:
            dRuleClass.update(g_SurvivorRuleClass)
        for iRule, cls in dRuleClass.items():
            self.m_RuleComponent[iRule] = cls(self)
        
        self.m_MultiTrigger = { }
        self.m_HoldRuleIdx = 0

    
    def Release(self):
        self.m_MultiTrigger = []
        for oTrigger in self.m_RuleComponent.values():
            oTrigger.Release()
        
        self.m_LevelCtrl = None
        self.m_Game = None

    
    def NewHoldRuleIdx(self):
        self.m_HoldRuleIdx += 1
        return self.m_HoldRuleIdx

    
    def _HoldTriggerOver(self, cbfunc, iRule, lstArgs, *args, **kwargs):
        cbfunc(*args, **kwargs)
        oTrigger = self.m_RuleComponent[iRule]
        oTrigger.UnRegister(*lstArgs)

    
    def SingleAttention(self, cbFunc, iRule, *args):
        oTrigger = self.m_RuleComponent[iRule]
        if oTrigger.m_TriggerType == HOLD_TRIGGER:
            iNewIdx = self.NewHoldRuleIdx()
            args = list(args) + [
                iNewIdx]
            cbFunc = Functor(self._HoldTriggerOver, cbFunc, iRule, args)
        oTrigger.Register(cbFunc, *args)

    
    def MultiAttention(self, cbFunc, lstRule, iScene, dArgs = None):
        oTrigger = CMultiTrigger(self, Functor(self._MultiAttentionOver, iScene, cbFunc), lstRule, dArgs)
        lstMulti = self.m_MultiTrigger.setdefault(iScene, [])
        lstMulti.append(oTrigger)

    
    def _MultiAttentionOver(self, iScene, cbFunc, oTarget, oTrigger):
        oTrigger.Release()
        self.m_MultiTrigger[iScene].remove(oTrigger)
        cbFunc(oTarget)

    
    def AttentionArgChange(self, iRule, tParam, dArgs):
        if iRule in TRIGGER_TYPE_SCENE:
            return [
                dArgs['Scene']] + list(tParam)
        if iRule in TRIGGER_TYPE_LINE:
            return [
                dArgs['LineIdx']] + list(tParam)
        if iRule in TRIGGER_TYPE_DEFAULT:
            return list(tParam)
        SendAlert('err', '未区分的触发类型%d' % iRule)

    
    def LineAttention(self, cbFunc, oLineNode, oCondition):
        iScene = oLineNode.m_LevelNode.m_Scene
        dArgs = {
            'Scene': iScene,
            'LineIdx': oLineNode.GetLineIdx() }
        if isinstance(oCondition, dict):
            tParam = self.AttentionArgChange(oCondition['rule'], oCondition['param'], dArgs)
            self.SingleAttention(cbFunc, oCondition['rule'], *tParam)
        else:
            self.MultiAttention(cbFunc, oCondition, iScene, dArgs)

    
    def LevelAttention(self, cbFunc, oLevelNode, oCondition):
        iScene = oLevelNode.m_Scene
        dArgs = {
            'Scene': iScene }
        if isinstance(oCondition, dict):
            tParam = self.AttentionArgChange(oCondition['rule'], oCondition['param'], dArgs)
            self.SingleAttention(cbFunc, oCondition['rule'], *tParam)
        else:
            self.MultiAttention(cbFunc, oCondition, iScene, dArgs)

    
    def ClearLevel(self, iScene, lstLineIdx):
        if iScene in self.m_MultiTrigger:
            for oTrigger in self.m_MultiTrigger.pop(iScene):
                oTrigger.Release()
            
        for oTrigger in self.m_RuleComponent.values():
            oTrigger.Clear(iScene, lstLineIdx)
        



class CMultiTrigger(object):
    
    def __init__(self, oParent, cbFunc, lstRule, dArgs):
        self.m_Parent = WeakProxy(oParent)
        self.m_cbFunc = cbFunc
        self.m_Trigger = [
            0,
            0]
        self.m_Child = [
            None,
            None]
        self.m_Rule = [
            None,
            None]
        (tLeft, self.m_Type, tRight) = lstRule
        for idx, oRule in enumerate((tLeft, tRight)):
            childFunc = Functor(self.Trigger, idx)
            if isinstance(oRule, dict):
                iRule = oRule['rule']
                tParam = oRule['param']
                if dArgs:
                    tParam = oParent.AttentionArgChange(iRule, tParam, dArgs)
                oTrigger = oParent.m_RuleComponent[iRule]
                if oTrigger.m_TriggerType == HOLD_TRIGGER:
                    iHoldIdx = oParent.NewHoldRuleIdx()
                    self.m_Rule[idx] = (iRule, tParam, iHoldIdx)
                    oTrigger.Register(childFunc, *tParam, iHoldIdx)
                else:
                    oTrigger.Register(childFunc, *tParam)
            self.m_Child[idx] = CMultiTrigger(oParent, childFunc, oRule, dArgs)
        

    
    def Release(self):
        for tRule in self.m_Rule:
            if not tRule:
                continue
            (iRule, tParam, iHoldIdx) = tRule
            self.m_Parent.m_RuleComponent[iRule].UnRegister(*tParam, iHoldIdx)
        
        self.m_Parent = None
        self.m_cbFunc = None
        for oChild in self.m_Child:
            if oChild:
                oChild.Release()
        
        self.m_Child = None

    
    def Trigger(self, idx, oTarget, oChild = None):
        if not self.m_cbFunc:
            return None
        self.m_Trigger[idx] = 1
        if self.IsTrigger():
            self.m_cbFunc(oTarget, self)

    
    def IsTrigger(self):
        iCnt = 0
        for idx in (0, 1):
            if self.m_Child[idx]:
                iCnt += self.m_Child[idx].IsTrigger()
                continue
            if self.m_Rule[idx]:
                (iRule, tParam, _) = self.m_Rule[idx]
                oTrigger = self.m_Parent.m_RuleComponent[iRule]
                iCnt += oTrigger.IsTrigger(*tParam)
                continue
            iCnt += self.m_Trigger[idx]
        
        if self.m_Type == 'and' and iCnt == 2:
            return 1
        if self.m_Type == 'or' and iCnt:
            return 1
        return 0



class CBaseTriggerRule(object):
    m_TriggerType = ONCE_TRIGGER
    
    def __init__(self, oParent):
        self.m_Parent = WeakProxy(oParent)
        self.m_TriggerFunc = { }
        self.OnInit()

    
    def OnInit(self):
        pass

    
    def Release(self):
        self.OnRelease()
        self.m_TriggerFunc = { }
        self.m_Parent = None

    
    def OnRelease(self):
        pass

    
    def Clear(self, iScene, lstLineIdx):
        if iScene in self.m_TriggerFunc:
            self.m_TriggerFunc.pop(iScene)
        for tLineIdx in lstLineIdx:
            if tLineIdx in self.m_TriggerFunc:
                self.m_TriggerFunc.pop(tLineIdx)
        



class CInitTrigger(CBaseTriggerRule):
    
    def Register(self, cbFunc):
        cbFunc(None)



class CSceneEvtTrigger(CBaseTriggerRule):
    
    def Register(self, cbFunc, iScene, iEvent, iEnterType):
        oScene = self.m_Parent.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        dSceneTrigger = self.m_TriggerFunc.setdefault(iScene, { })
        dEvtCallBack = dSceneTrigger.setdefault(iEvent, {
            SCENE_EVT_LEAVE: [],
            SCENE_EVT_ENTER: [] })
        dEvtCallBack[iEnterType].append(cbFunc)
        oListener = self.m_Parent.m_LevelCtrl
        enterfunc = Functor(self.OnSceneEvent, SCENE_EVT_ENTER)
        leavefunc = Functor(self.OnSceneEvent, SCENE_EVT_LEAVE)
        oScene.BindSceneEvent(oListener, iEvent, enterfunc, leavefunc)

    
    def Trigger(self, oTarget, iScene, iEvent, iEnterType):
        if iScene not in self.m_TriggerFunc:
            return None
        dSceneTrigger = self.m_TriggerFunc[iScene]
        if iEvent not in dSceneTrigger:
            return None
        dEvtCallBack = dSceneTrigger[iEvent]
        lstFunc = dEvtCallBack[iEnterType]
        iOtherType = SCENE_EVT_LEAVE if iEnterType == SCENE_EVT_ENTER else SCENE_EVT_ENTER
        if dEvtCallBack[iOtherType]:
            dEvtCallBack[iEnterType] = []
        else:
            self.m_TriggerFunc[iScene].pop(iEvent)
            oScene = self.m_Parent.m_Game.m_SceneMgr.GetScene(iScene)
            oScene.UnBindSceneEvent(iEvent)
        for func in lstFunc:
            func(oTarget)
        

    
    def OnSceneEvent(self, iEnterType, oLevelCtrl, dMsgInfo):
        oGame = oLevelCtrl.m_Game
        oTarget = oGame.GetObject(dMsgInfo['VID'])
        if not oTarget or oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        self.Trigger(oTarget, dMsgInfo['Scene'], dMsgInfo['Event'], iEnterType)



class CKillMonsterTrigger(CBaseTriggerRule):
    
    def __init__(self, oParent):
        super(CKillMonsterTrigger, self).__init__(oParent)
        oGame = oParent.m_Game
        oGame.AddGlobalAttention(oParent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnWarriorDie, 'KillMonsterTrigger')

    
    def OnRelease(self):
        oGame = self.m_Parent.m_Game
        oGame.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, 'KillMonsterTrigger')

    
    def Register(self, cbFunc, tLineIdx, iGroup, iPerfab, iNum):
        iNum = cl_formula.GetFormulaResult(self.m_Parent, iNum)
        dSceneTrigger = self.m_TriggerFunc.setdefault(tLineIdx, { })
        (lstKillTrigger, _) = dSceneTrigger.setdefault((iGroup, iPerfab), ([], 0))
        lstKillTrigger.append((iNum, cbFunc))

    
    def Trigger(self, oTarget, tLineIdx, iGroup, iPerfab):
        if tLineIdx not in self.m_TriggerFunc:
            return None
        dSceneTrigger = self.m_TriggerFunc[tLineIdx]
        tKey = (iGroup, iPerfab)
        if tKey not in dSceneTrigger:
            return None
        (lstKillTrigger, iKillCnt) = dSceneTrigger[tKey]
        iKillCnt += 1
        lstNew = []
        lstFunc = []
        for iTrigger, func in lstKillTrigger:
            if iKillCnt >= iTrigger:
                lstFunc.append(func)
                continue
            lstNew.append((iTrigger, func))
        
        if lstNew:
            dSceneTrigger[tKey] = (lstNew, iKillCnt)
        else:
            dSceneTrigger.pop(tKey)
        for func in lstFunc:
            func(oTarget)
        

    
    def OnWarriorDie(self, oLevelCtrl, oWarrior, dMsgInfo):
        if not oWarrior or not (oWarrior.m_LineIdx):
            return None
        oLineNode = oLevelCtrl.GetLineNode(oWarrior.m_LineIdx)
        if not oLineNode:
            oGame = self.m_Parent.m_Game
            iGameID = oGame.m_ID
            iPlayer = 0
            if 'AID' in dMsgInfo:
                oAttacker = oGame.GetObject(dMsgInfo['AID'])
                if oAttacker and oAttacker.m_FightType & WARRIOR_HERO:
                    iPlayer = oAttacker.m_PlayerID
            SendAlert('err', 'no linenode %s %s %s %s %s' % (iGameID, oWarrior.m_SID, oWarrior.m_LineIdx, iPlayer, oWarrior.m_Owner))
            return None
        (iGroup, iPerfab) = oLineNode.m_MonsterCtrl.GetMonsterBelong(oWarrior)
        if not iGroup:
            return None
        self.Trigger(oWarrior, oWarrior.m_LineIdx, iGroup, iPerfab)
        self.Trigger(oWarrior, oWarrior.m_LineIdx, iGroup, 0)
        oLineNode.m_MonsterCtrl.OnWarriorDie(dMsgInfo)



class CKillGroupTrigger(CBaseTriggerRule):
    
    def __init__(self, oParent):
        super(CKillGroupTrigger, self).__init__(oParent)
        oGame = oParent.m_Game
        oGame.AddGlobalAttention(oParent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.OnKillGroup, 'KillGroupTrigger')

    
    def OnRelease(self):
        oGame = self.m_Parent.m_Game
        oGame.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, 'KillGroupTrigger')

    
    def Register(self, cbFunc, tLineIdx, tGroup):
        lstKillTrigger = self.m_TriggerFunc.setdefault(tLineIdx, [])
        lstKillTrigger.append((list(tGroup), cbFunc))

    
    def Trigger(self, oTarget, tLineIdx, iGroup):
        if tLineIdx not in self.m_TriggerFunc:
            return None
        lstExecute = []
        lstKillTrigger = []
        for lstGroup, cbFunc in self.m_TriggerFunc[tLineIdx]:
            if iGroup in lstGroup:
                lstGroup.remove(iGroup)
            if not lstGroup:
                lstExecute.append(cbFunc)
                continue
            lstKillTrigger.append((lstGroup, cbFunc))
        
        self.m_TriggerFunc[tLineIdx] = lstKillTrigger
        for func in lstExecute:
            func(oTarget)
        

    
    def OnKillGroup(self, oLevelCtrl, oWarMgr, dMsgInfo):
        iVictim = dMsgInfo['VID']
        iGroup = dMsgInfo['GroupID']
        tLineIdx = dMsgInfo['LineIdx']
        oVictim = oWarMgr.m_Game.GetObject(iVictim)
        self.Trigger(oVictim, tLineIdx, iGroup)



class CGroupRestMonsterTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        oGame = self.m_Parent.m_Game
        oGame.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, 'GroupRestTrigger')
        oGame.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, 'GroupRestTrigger')

    
    def Register(self, cbFunc, tLineIdx, iGroup, iTargetNum):
        if not self.m_TriggerFunc:
            oGame = self.m_Parent.m_Game
            oGame.AddGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_KILLMONSTERGROUP, self.OnKillGroup, 'GroupRestTrigger')
            oGame.AddGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnWarriorDie, 'GroupRestTrigger')
        lstTrigger = self.m_TriggerFunc.setdefault(tLineIdx, [])
        lstTrigger.append((iGroup, iTargetNum, cbFunc))

    
    def Trigger(self, oTarget, tLineIdx, iDieGroup, iRest):
        if tLineIdx not in self.m_TriggerFunc:
            return None
        lstExecute = []
        lstTrigger = []
        lstAllFunc = self.m_TriggerFunc.pop(tLineIdx)
        for iGroup, iTargetNum, cbFunc in lstAllFunc:
            if iGroup == iDieGroup and iRest <= iTargetNum:
                lstExecute.append(cbFunc)
                continue
            lstTrigger.append((iGroup, iTargetNum, cbFunc))
        
        for func in lstExecute:
            func(oTarget)
        
        if lstTrigger:
            self.m_TriggerFunc[tLineIdx] = lstTrigger
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def OnKillGroup(self, oLevelCtrl, oWarMgr, dMsgInfo):
        iVictim = dMsgInfo['VID']
        iGroup = dMsgInfo['GroupID']
        tLineIdx = dMsgInfo['LineIdx']
        oVictim = oWarMgr.m_Game.GetObject(iVictim)
        self.Trigger(oVictim, tLineIdx, iGroup, iRest = 0)

    
    def OnWarriorDie(self, oLevelCtrl, oWarrior, dMsgInfo):
        if not oWarrior or not (oWarrior.m_LineIdx):
            return None
        oLineNode = oLevelCtrl.GetLineNode(oWarrior.m_LineIdx)
        (iGroup, _iPerfab) = oLineNode.m_MonsterCtrl.GetMonsterBelong(oWarrior)
        if not iGroup:
            return None
        iRest = oLineNode.m_MonsterCtrl.GetGroupRemainCount(iGroup)
        self.Trigger(oWarrior, oWarrior.m_LineIdx, iGroup, iRest)



class CSceneEvtHoldTrigger(CBaseTriggerRule):
    m_TriggerType = HOLD_TRIGGER
    
    def Register(self, cbFunc, iScene, iEvent, iRuleIdx):
        oScene = self.m_Parent.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        dSceneTrigger = self.m_TriggerFunc.setdefault(iScene, { })
        (dCallBack, lstTarget) = dSceneTrigger.setdefault(iEvent, ({ }, []))
        dCallBack[iRuleIdx] = cbFunc
        oListener = self.m_Parent.m_LevelCtrl
        enterfunc = Functor(self.OnSceneEvent, SCENE_EVT_ENTER)
        leavefunc = Functor(self.OnSceneEvent, SCENE_EVT_LEAVE)
        oScene.BindSceneEvent(oListener, iEvent, enterfunc, leavefunc, 'EvtHoldTrigger')

    
    def UnRegister(self, iScene, iEvent, iRuleIdx):
        if iScene not in self.m_TriggerFunc:
            return None
        dSceneTrigger = self.m_TriggerFunc[iScene]
        if iEvent not in dSceneTrigger:
            return None
        (dCallBack, _) = dSceneTrigger[iEvent]
        if iRuleIdx in dCallBack:
            dCallBack.pop(iRuleIdx)
        if not dCallBack:
            dSceneTrigger.pop(iEvent)
            oScene = self.m_Parent.m_Game.m_SceneMgr.GetScene(iScene)
            if oScene:
                oScene.UnBindSceneEvent(iEvent, 'EvtHoldTrigger')

    
    def Trigger(self, oTarget, iScene, iEvent, iEnterType):
        if iScene not in self.m_TriggerFunc:
            return None
        if iEvent not in self.m_TriggerFunc[iScene]:
            return None
        (dCallBack, lstTarget) = self.m_TriggerFunc[iScene][iEvent]
        if iEnterType == SCENE_EVT_ENTER:
            lstTarget.append(oTarget.m_ID)
            if len(lstTarget) == 1:
                for func in list(dCallBack.values()):
                    func(oTarget)
                
            elif oTarget.m_ID in lstTarget:
                lstTarget.remove(oTarget.m_ID)

    
    def IsTrigger(self, iScene, iEvent):
        if iScene not in self.m_TriggerFunc:
            return 0
        if iEvent not in self.m_TriggerFunc[iScene]:
            return 0
        (_, lstTarget) = self.m_TriggerFunc[iScene][iEvent]
        if lstTarget:
            return 1
        return 0

    
    def OnSceneEvent(self, iEnterType, oLevelCtrl, dMsgInfo):
        oGame = oLevelCtrl.m_Game
        oTarget = oGame.GetObject(dMsgInfo['VID'])
        if not oTarget or oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        self.Trigger(oTarget, dMsgInfo['Scene'], dMsgInfo['Event'], iEnterType)



class CTopologySceneEvtTrigger(CBaseTriggerRule):
    
    def Register(self, cbFunc, iScene, lstPreEvent, iEvent):
        oScene = self.m_Parent.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return None
        dSceneTrigger = self.m_TriggerFunc.setdefault(iScene, { })
        lstTarget = []
        oListener = self.m_Parent.m_LevelCtrl
        for evtid in set(lstPreEvent):
            enterfunc = Functor(self.OnSceneEvent, SCENE_EVT_ENTER)
            leavefunc = None
            lstTarget.append(evtid)
            oScene.BindSceneEvent(oListener, evtid, enterfunc, leavefunc, 'EvtPreTrigger%d' % evtid)
        
        oScene.BindSceneEvent(oListener, iEvent, Functor(self.OnSceneEvent, SCENE_EVT_ENTER), None, 'EvtTopologyTrigger')
        dSceneTrigger[iEvent] = (lstTarget, [], cbFunc)

    
    def Clear(self, iScene, lstLineIdx):
        super(CTopologySceneEvtTrigger, self).Clear(iScene, lstLineIdx)
        oScene = self.m_Parent.m_Game.m_SceneMgr.GetScene(iScene)
        if not oScene or iScene not in self.m_TriggerFunc:
            return None
        for iEvent in self.m_TriggerFunc[iScene].keys():
            self.ClearEvent(iScene, iEvent)
        
        self.m_TriggerFunc.pop(iScene)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def ClearEvent(self, iScene, iEvent):
        oScene = self.m_Parent.m_Game.m_SceneMgr.GetScene(iScene)
        oScene.UnBindSceneEvent(iEvent, 'EvtHoldTrigger')
        (lstTarget, _, _) = self.m_TriggerFunc[iScene][iEvent]
        for iEvent in lstTarget:
            oScene.UnBindSceneEvent(iEvent, 'EvtPreTrigger%d' % iEvent)
        

    
    def Trigger(self, oTarget, iScene, iEvent):
        if iScene not in self.m_TriggerFunc:
            return None
        for lstTarget, lstCur, _ in self.m_TriggerFunc[iScene].values():
            if iEvent in lstTarget and iEvent not in lstCur:
                lstCur.append(iEvent)
        
        if iEvent not in self.m_TriggerFunc[iScene]:
            return None
        (lstTarget, lstCur, func) = self.m_TriggerFunc[iScene][iEvent]
        if len(lstTarget) == len(lstCur):
            func(oTarget)
            self.ClearEvent(iScene, iEvent)

    
    def OnSceneEvent(self, iEnterType, oLevelCtrl, dMsgInfo):
        oGame = oLevelCtrl.m_Game
        oTarget = oGame.GetObject(dMsgInfo['VID'])
        if not oTarget or oTarget.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        if iEnterType != SCENE_EVT_ENTER:
            return None
        self.Trigger(oTarget, dMsgInfo['Scene'], dMsgInfo['Event'])



class CThresholdMonsterTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_Parent.m_LevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, 'ThresholdTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CThresholdMonsterTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbFunc, tLineIdx, iMonsterNo, iThreshold):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.OnCreateMonster, 'ThresholdTrigger', -1, 0)
        dLineTrigger = self.m_TriggerFunc.setdefault(tLineIdx, { })
        dCBFunc = dLineTrigger.setdefault(iMonsterNo, { })
        lstCBFunc = dCBFunc.setdefault(iThreshold, [])
        lstCBFunc.append(cbFunc)
        if len(lstCBFunc) != 1:
            return None
        oLineNode = self.m_Parent.m_LevelCtrl.GetLineNode(tLineIdx)
        lstMonster = oLineNode.m_MonsterCtrl.GetMonsterByNo(iMonsterNo)
        oGame = self.m_Parent.m_Game
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster)
            oMonster.AddHPThreshold(iThreshold, HP_RADIO_SUB, 'HPLevelTrigger', self.Trigger)
        

    
    def Trigger(self, oMonster, dInfo):
        iThreshold = dInfo['Threshold']
        oMonster.ClearHPThreshold(iThreshold, HP_RADIO_SUB, 'HPLevelTrigger')
        tLineIdx = oMonster.m_LineIdx
        if tLineIdx not in self.m_TriggerFunc:
            return None
        iMonsterNo = oMonster.Query('MonsterNo')
        dLineTrigger = self.m_TriggerFunc[tLineIdx]
        if iMonsterNo not in dLineTrigger:
            return None
        dCBFunc = dLineTrigger[iMonsterNo]
        if iThreshold not in dCBFunc:
            return None
        lstFunc = dCBFunc[iThreshold]
        dCBFunc[iThreshold] = []
        for func in lstFunc:
            func(oMonster)
        
        if not dCBFunc:
            dLineTrigger.pop(iMonsterNo)
        if not dLineTrigger:
            self.m_TriggerFunc.pop(tLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        iMonster = dMsgInfo['Monster']
        tLineIdx = dMsgInfo['LineIdx']
        iMonsterNo = dMsgInfo['MonsterNo']
        if tLineIdx not in self.m_TriggerFunc:
            return None
        if iMonsterNo not in self.m_TriggerFunc[tLineIdx]:
            return None
        oMonster = self.m_Parent.m_Game.GetObject(iMonster)
        for iThreshold in self.m_TriggerFunc[tLineIdx][iMonsterNo].keys():
            oMonster.AddHPThreshold(iThreshold, HP_RADIO_SUB, 'HPLevelTrigger', self.Trigger)
        



class CDualWieldTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        self.m_Parent.m_Game.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_WIELDWEAPON, 'DualWieldTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CDualWieldTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbFunc, iScene):
        lstCallBack = self.m_TriggerFunc.setdefault(iScene, [])
        lstCallBack.append(cbFunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_WIELDWEAPON, self.Trigger, 'DualWieldTrigger')

    
    def Trigger(self, oLevelCtrl, oHero, dInfo):
        if oHero.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        if oHero.m_Scene not in self.m_TriggerFunc:
            return None
        if not oHero.ValidOpenDualWield():
            return None
        lstFunc = self.m_TriggerFunc.pop(oHero.m_Scene)
        for func in lstFunc:
            func(oHero)
        
        if not self.m_TriggerFunc:
            self.OnRelease()



class CBulletChangeTrigger(CBaseTriggerRule):
    
    def OnInit(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_BULLETCHANGE, self.Trigger, 'BulletChangeTrigger')

    
    def OnRelease(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_Parent.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_BULLETCHANGE, 'BulletChangeTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CBulletChangeTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, iScene, iBulletSID):
        dSceneTrigger = self.m_TriggerFunc.setdefault(iScene, { })
        lstCBFunc = dSceneTrigger.setdefault(iBulletSID, [])
        lstCBFunc.append(cbfunc)

    
    def Trigger(self, oLevelCtrl, oHero, dInfo):
        if oHero.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        iScene = oHero.m_Scene
        iBulletSID = dInfo['SID']
        if iScene not in self.m_TriggerFunc:
            return None
        if iBulletSID not in self.m_TriggerFunc[iScene]:
            return None
        lstFunc = self.m_TriggerFunc[iScene].pop(iBulletSID)
        for func in lstFunc:
            func(oHero)
        
        if not self.m_TriggerFunc[iScene]:
            self.m_TriggerFunc.pop(iScene)



class CNPCInteractTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        self.m_Parent.m_Game.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, 'NPCInteractTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CNPCInteractTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, iScene, iNPC, iStatus):
        dSceneTrigger = self.m_TriggerFunc.setdefault(iScene, { })
        dNPCFunc = dSceneTrigger.setdefault(iNPC, { })
        lstCBFunc = dNPCFunc.setdefault(iStatus, [])
        lstCBFunc.append(cbfunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_NPCINTERACT, self.Trigger, 'NPCInteractTrigger')

    
    def Trigger(self, oLevelCtrl, oNPC, dInfo):
        pass



class CBuildInteractTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        self.m_Parent.m_Game.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_BUILD_STOP_INTERACT, 'NPCInteractTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CBuildInteractTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, iScene, iBuild):
        dSceneTrigger = self.m_TriggerFunc.setdefault(iScene, { })
        lstCBFunc = dSceneTrigger.setdefault(iBuild, [])
        lstCBFunc.append(cbfunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_BUILD_STOP_INTERACT, self.Trigger, 'BuildInteractTrigger')

    
    def Trigger(self, oLevelCtrl, oBuild, dInfo):
        if oBuild.m_FightType & WARRIOR_PROTEGE_NORMAL != WARRIOR_PROTEGE_NORMAL:
            return None
        iScene = oBuild.m_Scene
        iBuild = oBuild.m_SID
        if iScene not in self.m_TriggerFunc:
            return None
        if iBuild not in self.m_TriggerFunc[iScene]:
            return None
        lstFunc = self.m_TriggerFunc[iScene].pop(iBuild)
        for func in lstFunc:
            func(oBuild)
        
        if not self.m_TriggerFunc[iScene]:
            self.m_TriggerFunc.pop(iScene)



class CLevelGoalTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        cl_msgcenter.DoneAttention(self.m_Parent.m_LevelCtrl, self.m_Parent.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'LevelGoalTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CLevelGoalTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, iScene):
        lstCBFunc = self.m_TriggerFunc.setdefault(iScene, [])
        lstCBFunc.append(cbfunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddAttentionFunc(oLevelCtrl, self.m_Parent.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.Trigger, 'LevelGoalTrigger')

    
    def Trigger(self, oLevelCtrl, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iScene = oLevelNode.m_Scene
        if iScene not in self.m_TriggerFunc:
            return None
        lstFunc = self.m_TriggerFunc.pop(iScene)
        for func in lstFunc:
            func(oLevelCtrl)
        
        if not self.m_TriggerFunc:
            self.OnRelease()



class CBuildAliveTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        cl_msgcenter.DoneAttention(self.m_Parent.m_LevelCtrl, self.m_Parent.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'BuildAliveTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        self.OnRelease()
        self.m_TriggerFunc = { }

    
    def Register(self, cbfunc, _iScene, lstPlayMode, iBuildSID, iAliveNum):
        oGame = self.m_Parent.m_Game
        oWarMgr = oGame.m_WarMgr
        if not isinstance(lstPlayMode, list):
            lstPlayMode = [
                lstPlayMode]
        if oWarMgr.m_PlayMode not in lstPlayMode:
            return None
        tKey = (iBuildSID, iAliveNum)
        lstCBFunc = self.m_TriggerFunc.setdefault(tKey, [])
        lstCBFunc.append(cbfunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddAttentionFunc(oLevelCtrl, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.Trigger, 'BuildAliveTrigger')

    
    def Trigger(self, oLevelCtrl, oWarMgr, dInfo):
        iScene = dInfo['Scene']
        oGame = self.m_Parent.m_Game
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        lstBuild = oScene.GetObjectsByTypes([
            'Build',
            'Obstacle',
            'Trap',
            'GateControl',
            'Protege'])
        dAlive = { }
        for iBuild in lstBuild:
            oBuild = oGame.GetObject(iBuild, PY_FLAG_DEAD)
            if not oBuild:
                continue
            dAlive[oBuild.m_SID] = dAlive.get(oBuild.m_SID, 0) + 1
        
        lstTriggerKey = []
        for tKey in self.m_TriggerFunc:
            (iBuildSID, iTargetAliveNum) = tKey
            if dAlive.get(iBuildSID, 0) >= iTargetAliveNum:
                lstTriggerKey.append(tKey)
        
        for tKey in lstTriggerKey:
            lstFunc = self.m_TriggerFunc.pop(tKey)
            for func in lstFunc:
                func(oLevelCtrl)
            
        
        if not self.m_TriggerFunc:
            self.OnRelease()



class CLevelFinishTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        cl_msgcenter.DoneAttention(self.m_Parent.m_LevelCtrl, self.m_Parent.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, 'LevelFinishTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CLevelFinishTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, iScene):
        lstCBFunc = self.m_TriggerFunc.setdefault(iScene, [])
        lstCBFunc.append(cbfunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddAttentionFunc(oLevelCtrl, self.m_Parent.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEFINISH, self.Trigger, 'LevelFinishTrigger')

    
    def Trigger(self, oLevelCtrl, oWarMgr, dInfo):
        iLevel = dInfo['LevelID']
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iScene = oLevelNode.m_Scene
        if iScene not in self.m_TriggerFunc:
            return None
        lstFunc = self.m_TriggerFunc.pop(iScene)
        for func in lstFunc:
            func(oLevelCtrl)
        
        if not self.m_TriggerFunc:
            self.OnRelease()



class CPickItemTrigger(CBaseTriggerRule):
    
    def OnInit(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PICK, self.Trigger, 'PickTrigger')

    
    def OnRelease(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        self.m_Parent.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_PICK, 'PickTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CPickItemTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, iScene, iFightType, iCnt):
        dSceneTrigger = self.m_TriggerFunc.setdefault(iScene, { })
        (lstPickTrigger, _) = dSceneTrigger.setdefault(iFightType, ([], 0))
        lstPickTrigger.append((iCnt, cbfunc))

    
    def Trigger(self, oLevelCtrl, oHero, dInfo):
        iScene = oHero.m_Scene
        if iScene not in self.m_TriggerFunc:
            return None
        iFightType = dInfo['Type']
        dPickTrigger = self.m_TriggerFunc[iScene]
        if iFightType not in dPickTrigger:
            return None
        (lstPickTrigger, iPick) = dPickTrigger.pop(iFightType)
        iPick += 1
        lstNew = []
        lstFunc = []
        for iTrigger, func in lstPickTrigger:
            if iTrigger <= iPick:
                lstFunc.append(func)
                continue
            lstNew.append((iTrigger, func))
        
        for func in lstFunc:
            func(oLevelCtrl)
        
        if lstNew:
            dPickTrigger[iFightType] = (lstNew, iPick)
        if not self.m_TriggerFunc[iScene]:
            self.m_TriggerFunc.pop(iScene)



class CWarSerialTrigger(CBaseTriggerRule):
    
    def Register(self, cbFunc, iWarNo):
        oGame = self.m_Parent.m_Game
        oWarMgr = oGame.m_WarMgr
        if oWarMgr.m_SID == iWarNo:
            cbFunc(None)



class CMixThresHoldMonsterTrigger(CBaseTriggerRule):
    m_HPThresholdTrigger = {
        HP_TYPE_SHIELD: SHIELD_RADIO_SUB,
        HP_TYPE_ARMOR: ARMOR_RADIO_SUB,
        HP_TYPE_NORMAL: HP_RADIO_SUB }
    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_Parent.m_LevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, 'MixThresHoldLevelTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CMixThresHoldMonsterTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbFunc, tLineIdx, iMonsterNo, iHPType, iThreshold):
        iDirect = 0
        for iType, iVal in self.m_HPThresholdTrigger.items():
            if iType & iHPType == iType:
                iDirect |= iVal
        
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        cl_msgcenter.AddFunction(oLevelCtrl, cl_msgcenter.MSG_LEVEL_CREATEMONSTER, self.OnCreateMonster, 'MixThresHoldLevelTrigger', -1, 0)
        dLineTrigger = self.m_TriggerFunc.setdefault(tLineIdx, { })
        dCBFunc = dLineTrigger.setdefault(iMonsterNo, { })
        lstCBFunc = dCBFunc.setdefault((iDirect, iThreshold), [])
        lstCBFunc.append(cbFunc)
        if len(lstCBFunc) != 1:
            return None
        oLineNode = self.m_Parent.m_LevelCtrl.GetLineNode(tLineIdx)
        lstMonster = oLineNode.m_MonsterCtrl.GetMonsterByNo(iMonsterNo)
        oGame = self.m_Parent.m_Game
        for iMonster in lstMonster:
            oMonster = oGame.GetObject(iMonster)
            oMonster.AddHPThreshold(iThreshold, iDirect, 'MixThresHold', self.Trigger)
        

    
    def Trigger(self, oMonster, dInfo):
        iThreshold = dInfo['Threshold']
        iDirect = dInfo['Direct']
        tKey = (iDirect, iThreshold)
        oMonster.ClearHPThreshold(iThreshold, iDirect, 'MixThresHold')
        tLineIdx = oMonster.m_LineIdx
        if tLineIdx not in self.m_TriggerFunc:
            return None
        iMonsterNo = oMonster.Query('MonsterNo')
        dLineTrigger = self.m_TriggerFunc[tLineIdx]
        if iMonsterNo not in dLineTrigger:
            return None
        dCBFunc = dLineTrigger[iMonsterNo]
        if tKey not in dCBFunc:
            return None
        lstFunc = dCBFunc[tKey]
        dCBFunc[tKey] = []
        for func in lstFunc:
            func(oMonster)
        
        if not dCBFunc:
            dLineTrigger.pop(iMonsterNo)
        if not dLineTrigger:
            self.m_TriggerFunc.pop(tLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def OnCreateMonster(self, oLevelCtrl, dMsgInfo):
        iMonster = dMsgInfo['Monster']
        tLineIdx = dMsgInfo['LineIdx']
        iMonsterNo = dMsgInfo['MonsterNo']
        if tLineIdx not in self.m_TriggerFunc:
            return None
        if iMonsterNo not in self.m_TriggerFunc[tLineIdx]:
            return None
        oMonster = self.m_Parent.m_Game.GetObject(iMonster)
        for iDirect, iThreshold in self.m_TriggerFunc[tLineIdx][iMonsterNo].keys():
            oMonster.AddHPThreshold(iThreshold, iDirect, 'MixThresHold', self.Trigger)
        



class CRoomGoalTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, 'RoomGoalTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CRoomGoalTrigger, self).Clear(iScene, lstLineIdx)
        for tLineIdx in lstLineIdx:
            iLevel = tLineIdx[0]
            if iLevel in self.m_TriggerFunc:
                self.m_TriggerFunc.pop(iLevel)
        
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, iScene, iLevel, iRoomPos):
        dLevelTrigger = self.m_TriggerFunc.setdefault(iLevel, { })
        lstCBFunc = dLevelTrigger.setdefault(iRoomPos, [])
        lstCBFunc.append(cbfunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMGOAL, self.Trigger, 'RoomGoalTrigger')

    
    def Trigger(self, oLevelCtrl, oWarMgr, dInfo):
        iRoomPos = dInfo['Room']
        iLevel = dInfo['Level']
        if iLevel not in self.m_TriggerFunc:
            return None
        dLevelTrigger = self.m_TriggerFunc[iLevel]
        if iRoomPos not in dLevelTrigger:
            return None
        lstFunc = dLevelTrigger.pop(iRoomPos)
        for func in lstFunc:
            func(oLevelCtrl)
        
        if not dLevelTrigger:
            self.m_TriggerFunc.pop(iLevel)
        if not self.m_TriggerFunc:
            self.OnRelease()



class CRoomChallengeTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.DoneGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, 'RoomChallengeTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CRoomChallengeTrigger, self).Clear(iScene, lstLineIdx)
        for tLineIdx in lstLineIdx:
            iLevel = tLineIdx[0]
            if iLevel in self.m_TriggerFunc:
                self.m_TriggerFunc.pop(iLevel)
        
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbfunc, tLineIdx):
        (iLevel, iRoomPos, _) = tLineIdx
        dLevelTrigger = self.m_TriggerFunc.setdefault(iLevel, { })
        lstCBFunc = dLevelTrigger.setdefault(iRoomPos, [])
        lstCBFunc.append(cbfunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_LEVEL_ROOMCHALLENGE, self.Trigger, 'RoomChallengeTrigger')

    
    def Trigger(self, oLevelCtrl, oWarMgr, dInfo):
        if not dInfo['Rlt']:
            return None
        iRoomPos = dInfo['Room']
        iLevel = dInfo['LevelID']
        if iLevel not in self.m_TriggerFunc:
            return None
        dLevelTrigger = self.m_TriggerFunc[iLevel]
        if iRoomPos not in dLevelTrigger:
            return None
        lstFunc = dLevelTrigger.pop(iRoomPos)
        for func in lstFunc:
            func(oLevelCtrl)
        
        if not dLevelTrigger:
            self.m_TriggerFunc.pop(iLevel)
        if not self.m_TriggerFunc:
            self.OnRelease()



class CNPCSceneEvtTrigger(CSceneEvtTrigger):
    
    def OnSceneEvent(self, iEnterType, oLevelCtrl, dMsgInfo):
        oGame = oLevelCtrl.m_Game
        oTarget = oGame.GetObject(dMsgInfo['VID'])
        if not oTarget or oTarget.m_FightType != NWARRIOR_NPC_CAR:
            return None
        self.Trigger(oTarget, dMsgInfo['Scene'], dMsgInfo['Event'], iEnterType)



class CKillPetrochemicalGroupTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        oGame = self.m_Parent.m_Game
        oGame.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, 'KillPetrochemicalGroupTrigger')

    
    def Register(self, cbFunc, tLineIdx, tGroup):
        oGame = self.m_Parent.m_Game
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        lstCBFunc = self.m_TriggerFunc.setdefault(tLineIdx, [])
        lstCBFunc.append((tGroup, cbFunc))
        oGame.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.Trigger, 'KillPetrochemicalGroupTrigger')

    
    def IsExsitUnPetrochemical(self, oWarrior):
        oGame = self.m_Parent.m_Game
        iScene = oWarrior.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if not oScene:
            return False
        for mid in oScene.GetObjectsByType('Monster'):
            oMonster = oGame.GetObject(mid, PY_FLAG_DEAD)
            if not oMonster:
                continue
            lstStatePetrochemical = oMonster.m_State.GetItems(STATE_PETROCHEMICAL)
            if not lstStatePetrochemical:
                return True
        
        return False

    
    def Trigger(self, oLevelCtrl, oWarrior, dMsgInfo):
        if not oWarrior or not (oWarrior.m_LineIdx):
            return None
        if oWarrior.m_FightType & WARRIOR_MONSTER != WARRIOR_MONSTER:
            return None
        tLineIdx = oWarrior.m_LineIdx
        if tLineIdx not in self.m_TriggerFunc:
            return None
        if self.IsExsitUnPetrochemical(oWarrior):
            return None
        lstExcuetFunc = []
        lstTrigger = []
        for lstGroup, cbFunc in self.m_TriggerFunc[tLineIdx]:
            if not lstGroup:
                lstExcuetFunc.append(cbFunc)
                continue
            for iGroup in lstGroup:
                oLineNode = oLevelCtrl.GetLineNode(tLineIdx)
                lstAlive = oLineNode.m_MonsterCtrl.GetGroupRemainCount(iGroup)
                if lstAlive:
                    lstTrigger.append((lstGroup, cbFunc))
                    break
            
        
        if lstTrigger:
            self.m_TriggerFunc[tLineIdx] = lstTrigger
        for func in lstExcuetFunc:
            func(oLevelCtrl)
        
        if not self.m_TriggerFunc:
            self.OnRelease()



class CClientButtonTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        self.m_Parent.m_Game.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_UNSEND_CLIENTBUTTON, 'ClientButton')

    
    def Clear(self, iScene, lstLineIdx):
        super(CClientButtonTrigger, self).Clear(iScene, lstLineIdx)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Register(self, cbFunc, iScene, lstKey):
        if isinstance(lstKey, int):
            lstKey = [
                lstKey]
        iKey = 0
        for iButton in lstKey:
            iKey |= iButton
        
        dCallBack = self.m_TriggerFunc.setdefault(iScene, { })
        if iKey not in dCallBack:
            dCallBack[iKey] = []
        dCallBack[iKey].append(cbFunc)
        oLevelCtrl = self.m_Parent.m_LevelCtrl
        oLevelCtrl.m_Game.AddGlobalAttention(oLevelCtrl.m_ID, cl_msgcenter.MSG_UNSEND_CLIENTBUTTON, self.Trigger, 'ClientButton')

    
    def Trigger(self, oLevelCtrl, oHero, dInfo):
        if oHero.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
            return None
        if oHero.m_Scene not in self.m_TriggerFunc:
            return None
        if 'lstClientKey' not in dInfo:
            return None
        iClientKey = 0
        dCallBack = self.m_TriggerFunc[oHero.m_Scene]
        for iButton in dInfo.get('lstClientKey', []):
            iClientKey |= iButton
        
        if iClientKey not in dCallBack.keys():
            return None
        for func in dCallBack[iClientKey]:
            func(oHero)
        
        self.m_TriggerFunc[oHero.m_Scene].pop(iClientKey)
        if not self.m_TriggerFunc[oHero.m_Scene]:
            self.m_TriggerFunc.pop(oHero.m_Scene)
        if not self.m_TriggerFunc:
            self.OnRelease()



class CPhaseStartTrigger(CBaseTriggerRule):
    
    def Register(self, cbFunc):
        cbFunc(None)



class COccupyProcessTrigger(CBaseTriggerRule):
    
    def Register(self, cbFunc, iProcess):
        oSurvivor = self.m_Parent.m_Game.m_WarMgr.GetComponent('NewSurvivorElement')
        if oSurvivor.m_Phase not in oSurvivor.m_PhaseChallengeMgr.m_Challenge:
            return None
        oChallenge = oSurvivor.m_PhaseChallengeMgr.m_Challenge[oSurvivor.m_Phase]
        if oChallenge.m_Type != PHASE_CHALLENGE_SINGLEPOINTOCCUPY:
            return None
        (lstFunc, _) = self.m_TriggerFunc.setdefault(iProcess, ([], []))
        lstFunc.append(cbFunc)
        func = Functor(self.Trigger, oChallenge, iProcess)
        oChallenge.AddProcessCbFun(iProcess, func)

    
    def Trigger(self, oChallenge, iProcess):
        oChallenge.RemoveProcessCbFun(iProcess)
        if iProcess not in self.m_TriggerFunc:
            return None
        (lstFunc, lstResult) = self.m_TriggerFunc[iProcess]
        if not lstResult:
            lstResult.append(iProcess)
        for func in lstFunc:
            func()
        
        for iRegisterProcess in list(self.m_TriggerFunc):
            if iRegisterProcess < iProcess:
                self.m_TriggerFunc.pop(iRegisterProcess)
        

    
    def IsTrigger(self, iProcess):
        if iProcess not in self.m_TriggerFunc:
            return 0
        (_, lstResult) = self.m_TriggerFunc[iProcess]
        if lstResult:
            return 1
        return 0

    
    def Clear(self, iScene, lstLineIdx):
        self.m_TriggerFunc = { }



class CHPThresholdMonsterTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        cl_msgcenter.DoneEvent(self.m_Parent.m_Game.m_WarMgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, 'PHThresholdMonsterTrigger')

    
    def Clear(self, iScene, lstLineIdx):
        super(CHPThresholdMonsterTrigger, self).Clear(iScene, lstLineIdx)
        self.m_TriggerFunc = { }
        self.OnRelease()

    
    def Register(self, cbFunc, iMonsterSID, iThreshold):
        oWarmgr = self.m_Parent.m_Game.m_WarMgr
        cl_msgcenter.AddFunction(oWarmgr, cl_msgcenter.MSG_WARMGR_CREATEMONSTER, self.OnCreateWarMonster, 'PHThresholdMonsterTrigger', -1, 0)
        dCBFunc = self.m_TriggerFunc.setdefault(iMonsterSID, { })
        lstCBFunc = dCBFunc.setdefault(iThreshold, [])
        lstCBFunc.append(cbFunc)

    
    def Trigger(self, oMonster, dInfo):
        iThreshold = dInfo['Threshold']
        oMonster.ClearHPThreshold(iThreshold, HP_RADIO_SUB, 'SurvivorHPThresholdTrigger')
        iMonsterSID = oMonster.m_SID
        if iMonsterSID not in self.m_TriggerFunc:
            return None
        dCBFunc = self.m_TriggerFunc[iMonsterSID]
        if iThreshold not in dCBFunc:
            return None
        lstFunc = dCBFunc.pop(iThreshold)
        for func in lstFunc:
            func(oMonster)
        
        if not dCBFunc:
            self.m_TriggerFunc.pop(iMonsterSID)
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def OnCreateWarMonster(self, oLevelCtrl, dMsgInfo):
        iMonster = dMsgInfo['Monster']
        oMonster = self.m_Parent.m_Game.GetObject(iMonster)
        if not oMonster:
            return None
        if oMonster.m_SID not in self.m_TriggerFunc:
            return None
        for iThreshold in self.m_TriggerFunc[oMonster.m_SID]:
            oMonster.AddHPThreshold(iThreshold, HP_RADIO_SUB, 'SurvivorHPThresholdTrigger', self.Trigger)
        



class CKillMonsterGroupNumTrigger(CBaseTriggerRule):
    
    def OnRelease(self):
        oGame = self.m_Parent.m_Game
        oGame.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, 'KillMonsterGroupNumTrigger')

    
    def Register(self, cbFunc, iSpawnGroup, iNum):
        oGame = self.m_Parent.m_Game
        oGame.AddGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnMonsterDie, 'KillMonsterGroupNumTrigger')
        (lstSpawnGroup, _) = self.m_TriggerFunc.setdefault(iSpawnGroup, ([], 0))
        lstSpawnGroup.append((iNum, cbFunc))

    
    def Trigger(self, oTarget, iSpawnGroup):
        if iSpawnGroup not in self.m_TriggerFunc:
            return None
        (lstSpawnGroup, iKillCnt) = self.m_TriggerFunc[iSpawnGroup]
        iKillCnt += 1
        lstNew = []
        lstFunc = []
        for iTrigger, func in lstSpawnGroup:
            if iKillCnt >= iTrigger:
                lstFunc.append(func)
                continue
            lstNew.append((iTrigger, func))
        
        if lstNew:
            self.m_TriggerFunc[iSpawnGroup] = (lstNew, iKillCnt)
        else:
            self.m_TriggerFunc.pop(iSpawnGroup)
        for func in lstFunc:
            func(oTarget)
        
        if not self.m_TriggerFunc:
            self.OnRelease()

    
    def Clear(self, iScene, lstLineIdx):
        super(CKillMonsterGroupNumTrigger, self).Clear(iScene, lstLineIdx)
        self.m_TriggerFunc = { }
        self.OnRelease()

    
    def OnMonsterDie(self, oLevelCtrl, oWarrior, dMsgInfo):
        if not oWarrior:
            return None
        iSpawnGroup = oWarrior.Query('SpawnGroup', 0)
        if not iSpawnGroup:
            return None
        self.Trigger(oWarrior, iSpawnGroup)



class CSurvivorKillGroup(CBaseTriggerRule):
    
    def __init__(self, oParent):
        super(CSurvivorKillGroup, self).__init__(oParent)
        oGame = oParent.m_Game
        oGame.AddGlobalAttention(oParent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, self.OnWarriorDie, 'SurvivorKillGroup')

    
    def OnRelease(self):
        oGame = self.m_Parent.m_Game
        oGame.DoneGlobalAttention(self.m_Parent.m_LevelCtrl.m_ID, cl_msgcenter.MSG_WAR_DIE, 'SurvivorKillGroup')

    
    def Register(self, cbFunc, tLineIdx, tGroup):
        lstKillTrigger = self.m_TriggerFunc.setdefault(tLineIdx, [])
        lstKillTrigger.append((list(tGroup), cbFunc))

    
    def Trigger(self, oTarget, tLineIdx, iGroup):
        lstExecute = []
        lstKillTrigger = []
        for lstGroup, cbFunc in self.m_TriggerFunc[tLineIdx]:
            if iGroup in lstGroup:
                lstGroup.remove(iGroup)
            if not lstGroup:
                lstExecute.append(cbFunc)
                continue
            lstKillTrigger.append((lstGroup, cbFunc))
        
        self.m_TriggerFunc[tLineIdx] = lstKillTrigger
        for func in lstExecute:
            func(oTarget)
        

    
    def OnWarriorDie(self, oLevelCtrl, oWarrior, dMsgInfo):
        if not oWarrior or not (oWarrior.m_LineIdx):
            return None
        if oWarrior.m_LineIdx not in self.m_TriggerFunc:
            return None
        iSpawnGroup = oWarrior.Query('SpawnGroup', 0)
        if not iSpawnGroup:
            return None
        oLineNode = oLevelCtrl.GetLineNode(oWarrior.m_LineIdx)
        if not oLineNode:
            return None
        iRes = oLineNode.m_MonsterCtrl.CheckGroupAllDie(oWarrior.m_ID, iSpawnGroup)
        if iRes:
            self.Trigger(oWarrior, oWarrior.m_LineIdx, iSpawnGroup)



class CJudgeCycle(CBaseTriggerRule):
    
    def Register(self, cbFunc, iCycle, iJudge):
        if not iJudge == JUDGE_LOGIC_GREATER or self.m_Parent.m_Game.m_WarMgr.m_Cycle > iCycle:
            return None
        if not iJudge == JUDGE_LOGIC_LESS or self.m_Parent.m_Game.m_WarMgr.m_Cycle < iCycle:
            return None
        if not iJudge == JUDGE_LOGIC_EQUAL or self.m_Parent.m_Game.m_WarMgr.m_Cycle == iCycle:
            return None
        if not iJudge == JUDGE_LOGIC_GREATER_EQUAL or self.m_Parent.m_Game.m_WarMgr.m_Cycle >= iCycle:
            return None
        if not iJudge == JUDGE_LOGIC_LESS_EQUAL or self.m_Parent.m_Game.m_WarMgr.m_Cycle <= iCycle:
            return None
        if not iJudge == JUDGE_LOGIC_NO_EQUAL or self.m_Parent.m_Game.m_WarMgr.m_Cycle != iCycle:
            return None
        return None


g_RuleClass = {
    TRIGGER_JUDGECYCLE: CJudgeCycle,
    TRIGGER_BUILDALIVE: CBuildAliveTrigger,
    TRIGGER_CLIENTBUTTON: CClientButtonTrigger,
    TRIGGER_BUILDINTERACT: CBuildInteractTrigger,
    TRIGGER_SCEVTTOPOLOGY: CTopologySceneEvtTrigger,
    TRIGGER_GROUPREST: CGroupRestMonsterTrigger,
    TRIGGER_KILLPETROCHEMICALGROUP: CKillPetrochemicalGroupTrigger,
    TRIGGER_NPCSCENEEVT: CNPCSceneEvtTrigger,
    TRIGGER_ROOMCHALLENGE: CRoomChallengeTrigger,
    TRIGGER_ROOMGOAL: CRoomGoalTrigger,
    TRIGGER_MIXTHRESHOLD: CMixThresHoldMonsterTrigger,
    TRIGGER_WARSERIAL: CWarSerialTrigger,
    TRIGGER_PICKITEM: CPickItemTrigger,
    TRIGGER_LEVELFINISH: CLevelFinishTrigger,
    TRIGGER_LEVELGOAL: CLevelGoalTrigger,
    TRIGGER_NPCINTERACT: CNPCInteractTrigger,
    TRIGGER_BULLETCHANGE: CBulletChangeTrigger,
    TRIGGER_DUALWIELD: CDualWieldTrigger,
    TRIGGER_HPTHRESHOLD: CThresholdMonsterTrigger,
    TRIGGER_SCEVTHOLD: CSceneEvtHoldTrigger,
    TRIGGER_KILLMONSTER: CKillMonsterTrigger,
    TRIGGER_KILLGROUP: CKillGroupTrigger,
    TRIGGER_SCENEEVT: CSceneEvtTrigger,
    TRIGGER_INIT: CInitTrigger }
g_SurvivorRuleClass = {
    SURVIVOR_TRIGGER_KILLGROUP: CSurvivorKillGroup,
    SURVIVOR_TRIGGER_KILLMONSTERGROUPNUM: CKillMonsterGroupNumTrigger,
    SURVIVOR_TRIGGER_HPTHRESHOLD: CHPThresholdMonsterTrigger,
    SURVIVOR_TRIGGER_OCCUPYPROCESS: COccupyProcessTrigger,
    SURVIVOR_TRIGGER_PHASESTART: CPhaseStartTrigger }
