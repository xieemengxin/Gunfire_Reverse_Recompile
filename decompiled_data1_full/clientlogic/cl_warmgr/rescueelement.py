# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/rescueelement.pyc
# RelativePath: clientlogic/cl_warmgr/rescueelement.pyc
# Source Generated with Decompyle++
# File: rescueelement.pyc (Python 3.6)

from cl_commondefines import STATE_DYING, TYPE_RELIFE_RESCUE, STATE_TIME_LIMIT, STATE_TIME_FOREVER, RESCUE_SUBMSG_START, RESCUE_SUBMSG_HALT, RESCUE_SUBMSG_END, RESCUE_SUBMSG_SUCCESS, WARRIOR_HERO, STATE_BEINGRESCUED, FORBID_SAVE, WARRIOR_SERVANT, WARRIOR_PET, FIGHT_KEY_RERESCUEINTENSIFY, FIGHT_KEY_TIEYIRERESCUEINTENSIFY
from cl_commondefines import TAG_RESCUE_NORMAL, TAG_RESCUE_REMOTE, TAG_RESCUE_MECHREMOTE
from cl_warmgr.mobject import CBaseElement
from cl_object.logging import WarobjLog
from cl_only import Functor, Time2Frame
import cl_math
import cl_notify
import cl_msgcenter
import cl_object
import cl_state
import cl_snetwar
CANRESCUE_FIGHTTYPE = WARRIOR_HERO | WARRIOR_SERVANT

class CRescueElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super().__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_HaltInfo = self.m_Data.m_Config.get('m_HaltInfo', { })
        self.m_IgnoreHalt = self.m_Data.m_Config.get('m_IgnoreHalt', ())
        self.m_RescueCache = { }
        self.m_RescueDistance = 6

    
    def CanRescue(self, oWarrior, oTarget):
        if oWarrior.IsDead():
            return False
        if not oTarget or not oTarget.IsDying() or not (oTarget.m_FightType & CANRESCUE_FIGHTTYPE):
            return False
        if oWarrior.m_ID == oTarget.m_ID:
            return False
        if oWarrior.m_ID in self.m_RescueCache:
            return False
        if oWarrior.IsForbid(FORBID_SAVE):
            return False
        dRescuing = oTarget.Query('Rescuing', { })
        if dRescuing and oWarrior.m_ID in dRescuing:
            return False
        if oWarrior.m_Scene != oTarget.m_Scene:
            return False
        vAttPos = oWarrior.GetPos()
        vTarPos = oTarget.GetPos()
        if not oWarrior.CheckSpecialKey(FIGHT_KEY_RERESCUEINTENSIFY) and not cl_math.CheckDistance(vAttPos, vTarPos, self.m_RescueDistance):
            if not oWarrior.CheckSpecialKey(FIGHT_KEY_TIEYIRERESCUEINTENSIFY) or oTarget.m_ID != oWarrior.m_Servant:
                return False
        return True

    
    def GetRescuedHero(self, oWarrior):
        if oWarrior.m_ID not in self.m_RescueCache:
            return None
        iTarget = self.m_RescueCache[oWarrior.m_ID]
        return self.m_Game.GetObject(iTarget)

    
    def IsRescuing(self, oWarrior, iTarget):
        return iTarget == self.m_RescueCache.get(oWarrior.m_ID, 0)

    
    def GetRescuingTarget(self, oWarrior):
        return self.m_RescueCache.get(oWarrior.m_ID, 0)

    
    def GetRemainRescueFrame(self, oWarrior):
        iEndRescueFrame = oWarrior.Query('EndRescueFrame', 0)
        if not iEndRescueFrame:
            return 0
        iCurFrame = self.m_Game.GetFrameNum()
        return iEndRescueFrame - iCurFrame

    
    def CheckRescueDis(self, oWarrior):
        if oWarrior.m_ID not in self.m_RescueCache:
            return 0
        iTarget = self.m_RescueCache[oWarrior.m_ID]
        oTarget = self.m_Game.GetObject(iTarget)
        vAttPos = oWarrior.GetPos()
        vTarPos = oTarget.GetPos()
        if not cl_math.CheckDistance3D(vAttPos, vTarPos, self.m_RescueDistance):
            self.HaltRescue(oWarrior, { })
            return 0
        return 1

    
    def StartRescue(self, oWarrior, iTarget):
        oTarget = self.m_Game.GetObject(iTarget)
        if not self.CanRescue(oWarrior, oTarget):
            return False
        dRescuing = oTarget.Query('Rescuing', { })
        dRescuing[oWarrior.m_ID] = 1
        oTarget.Set('Rescuing', dRescuing)
        self.m_RescueCache[oWarrior.m_ID] = iTarget
        oState = oTarget.m_State.GetItemBySID(STATE_DYING)
        oState.StopCount(oTarget)
        iRescueFrame = Time2Frame(oWarrior.QueryAttr('SaveTime'))
        iCurFrame = self.m_Game.GetFrameNum()
        oWarrior.Set('EndRescueFrame', iRescueFrame + iCurFrame)
        if iRescueFrame:
            iTimeType = STATE_TIME_LIMIT
        else:
            iTimeType = STATE_TIME_FOREVER
        dArgs = {
            'AID': oTarget.m_ID,
            'RS': cl_object.reason.CStrReason('救助'),
            'arg': { } }
        oState = cl_state.AddState(oTarget, STATE_BEINGRESCUED, iTimeType, iRescueFrame, dArgs)
        if oState:
            oState.Enable(oTarget)
        iRescueIntensify = oWarrior.CheckSpecialKey(FIGHT_KEY_RERESCUEINTENSIFY)
        if not iRescueIntensify:
            if oWarrior.m_FightType & (WARRIOR_SERVANT | WARRIOR_PET):
                cl_notify.SendCommonNotify(self.m_Game, self.m_Game.GetRealPlayers(), 2363, {
                    '$name': oWarrior.Name(),
                    '$$playername': oTarget.Name() })
            elif oTarget.m_FightType & WARRIOR_SERVANT:
                cl_notify.SendCommonNotify(self.m_Game, self.m_Game.GetRealPlayers(), 2364, {
                    '$$playername': oWarrior.Name(),
                    '$name': oTarget.Name() })
            else:
                cl_notify.SendCommonNotify(self.m_Game, self.m_Game.GetRealPlayers(), 2103, {
                    '$$playername1': oWarrior.Name(),
                    '$$playername2': oTarget.Name() })
        cl_msgcenter.AddAttentionFunc(oWarrior, iTarget, cl_msgcenter.MSG_WAR_DIEDIST, self.StopRescue, 'SaveRealDie')
        cl_msgcenter.AddAttentionFunc(oWarrior, iTarget, cl_msgcenter.MSG_WAR_RELIFE, self.StopRescue, 'SaveRelife')
        cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_DIE, self.HaltRescue, 'SaveMasterDie')
        cl_snetwar.GS2CStartRescue(oWarrior, oTarget, oWarrior.QueryAttr('SaveTime'), self.m_Game.GetFrameNum(), self.m_Game.GetRealPlayers())
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RESCUE, oWarrior, { }, iSub = RESCUE_SUBMSG_START)
        WarobjLog.Info(f'''start Rescue {oWarrior.m_PlayerID} {oWarrior.m_ID} {oTarget.m_PlayerID} {oTarget.m_ID}''')
        if iRescueIntensify:
            self.RescueRelife(oWarrior, oTarget.m_ID, iTag = TAG_RESCUE_REMOTE)
        elif oWarrior.CheckSpecialKey(FIGHT_KEY_TIEYIRERESCUEINTENSIFY) and iTarget == oWarrior.m_Servant:
            self.RescueRelife(oWarrior, oTarget.m_ID, iTag = TAG_RESCUE_MECHREMOTE)
        else:
            oWarrior.Call_Out(Functor(self.RescueRelife, oWarrior, oTarget.m_ID), iRescueFrame, 'Rescue')
        return True

    
    def StopRescue(self, oWarrior, oTarget, dInfo):
        if oWarrior.m_ID not in self.m_RescueCache:
            return None
        cl_snetwar.GS2CStopRescue(oWarrior, oTarget, self.m_Game.GetRealPlayers())
        self.EndRescue(oWarrior, self.m_RescueCache[oWarrior.m_ID])

    
    def HaltRescue(self, oWarrior, dInfo):
        if oWarrior.m_ID not in self.m_RescueCache:
            return None
        oTarget = self.GetRescuedHero(oWarrior)
        if not oTarget:
            return None
        cl_snetwar.GS2CBreakRescue(oWarrior, oTarget, self.m_Game.GetRealPlayers())
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RESCUE, oWarrior, { }, iSub = RESCUE_SUBMSG_HALT)
        WarobjLog.Info(f'''break Rescue {oWarrior.m_PlayerID} {oWarrior.m_ID} {oTarget.m_PlayerID} {oTarget.m_ID}''')
        self.EndRescue(oWarrior, self.m_RescueCache[oWarrior.m_ID])

    
    def RescueRelife(self, oWarrior, iTarget, iTag = TAG_RESCUE_NORMAL):
        oTarget = self.m_Game.GetObject(iTarget)
        if not oTarget:
            return None
        dReason = {
            'Type': TYPE_RELIFE_RESCUE,
            'AID': oWarrior.m_ID,
            'Tag': iTag }
        if oTarget.m_FightType & WARRIOR_SERVANT or oWarrior.CheckSpecialKey(FIGHT_KEY_RERESCUEINTENSIFY):
            dRelifeInfo = None
        else:
            dRelifeInfo = {
                'HP': max(100, oTarget.QueryAttr('HPMax') // 10),
                'Shield': 0,
                'Armor': 0 }
        dRescuing = oTarget.Query('Rescuing', { })
        for iSaverID in dRescuing:
            oSaver = self.m_Game.GetObject(iSaverID)
            if not oSaver:
                continue
            dInfo = {
                'VID': oTarget.m_ID }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RESCUE, oSaver, dInfo, iSub = RESCUE_SUBMSG_SUCCESS)
            if 'CloseNotify' in dInfo:
                dReason['CloseNotify'] = 1
        
        oDieElement = self.m_WarMgr.GetComponent('PVEDieElement')
        if oDieElement:
            oDieElement.DirectHeroRelife(oTarget, dReason, dRelifeInfo)
        else:
            oTarget.Relife(dReason, dRelifeInfo)

    
    def EndRescue(self, oWarrior, iTarget):
        oTarget = self.m_Game.GetObject(iTarget)
        if not oTarget:
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_RESCUE, oWarrior, { }, iSub = RESCUE_SUBMSG_END)
        dRescuing = oTarget.Query('Rescuing', { })
        dRescuing.pop(oWarrior.m_ID, 0)
        self.m_RescueCache.pop(oWarrior.m_ID, 0)
        oWarrior.Delete('EndRescueFrame')
        oWarrior.Remove_Call_Out('Rescue')
        iSaved = 1
        if not dRescuing:
            oState = oTarget.m_State.GetItemBySID(STATE_DYING)
            if oState:
                oState.StartCount(oTarget)
                iSaved = 0
            oState = oTarget.m_State.GetItemBySID(1006)
            if oState:
                oTarget.m_State.RemoveItem(oState.m_ID)
        cl_msgcenter.DoneAttention(oWarrior, iTarget, cl_msgcenter.MSG_WAR_DIEDIST, 'SaveRealDie')
        cl_msgcenter.DoneAttention(oWarrior, iTarget, cl_msgcenter.MSG_WAR_RELIFE, 'SaveRelife')
        cl_msgcenter.DoneEvent(oWarrior, cl_msgcenter.MSG_WAR_DIE, 'SaveMasterDie')
        WarobjLog.Info(f'''end Rescue {oWarrior.m_PlayerID} {oWarrior.m_ID} {oTarget.m_PlayerID} {oTarget.m_ID} {iSaved}''')



def GetComponentClass(oMgrManager):
    return CRescueElement

