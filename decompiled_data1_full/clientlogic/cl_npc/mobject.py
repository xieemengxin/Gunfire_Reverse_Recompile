# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/mobject.pyc
# RelativePath: clientlogic/cl_npc/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_commondefines import NPC_CB_REFRESH, INTERACT_STATUS_DONE, INTERACT_TYPE_FORBID, INTERACT_STATUS_PEND, INTERACT_TYPE_ALLOW, NPC_ACTION_NONE, NWARRIOR_NPC, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP
from cl_only import SendAlert
from cl_object.logging import WarnpcLog
import cl_world
import cl_netattr
import cl_math
import cl_msgcenter
import cl_notify
import cl_snetwar
from . import net
from . import npcinteractrule

class CNPC(cl_world.CSceneObject):
    m_Type = 'NPC'
    m_Delete = 1
    m_FightType = NWARRIOR_NPC
    m_InteractDis = 5
    m_CheckInteractDistance = True
    m_CheckInteractScene = True
    
    def __init__(self, *args):
        super(CNPC, self).__init__(*args)
        self.m_Enable = 1
        self.m_GlobalPrefab = 0
        self.m_ActionFunc = None
        self.m_ActionType = NPC_ACTION_NONE
        self.m_PlayerInteractStatus = { }
        self.m_PlayerInteractType = { }
        self.m_PlayerAssignInteractType = { }
        self.SetInitInteract(INTERACT_TYPE_ALLOW)
        self.m_VisiblePlayer = { }
        self.m_VisibleCondition = []
        self.m_ExtraInteractRule = { }
        self.m_ArgData = { }
        self.m_RefreshCost = 0
        self.m_TriCenter = []
        self.m_TriHalfExt = []
        self.m_TriType = None
        self.m_Share = 1
        self.m_FormulaLimit = { }

    
    def GetArgValue(self, sArgs, default = 0):
        if sArgs not in self.m_ArgData:
            return default
        return self.m_ArgData[sArgs]

    
    def SetArgValue(self, sArgs, val):
        self.m_ArgData[sArgs] = val

    
    def DelArgValue(self, sArgs):
        if sArgs in self.m_ArgData:
            self.m_ArgData.pop(sArgs)

    
    def Remove(self, sReason):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVENPC, self, { })
        super().Remove(sReason)

    
    def Release(self):
        for _, oRule in self.m_ExtraInteractRule.items():
            oRule.Release()
        
        self.m_ExtraInteractRule = { }
        self.m_ActionFunc = None
        super(CNPC, self).Release()

    
    def SetInitInteract(self, iType):
        oWarMgr = self.m_Game.m_WarMgr
        for pid in oWarMgr.GetAllPlayer():
            self.m_PlayerInteractStatus[pid] = INTERACT_STATUS_PEND
            self.m_PlayerInteractType[pid] = iType
            self.m_PlayerAssignInteractType[pid] = NPC_ACTION_NONE
        

    
    def SetInteractDis(self, fDis):
        self.m_InteractDis = fDis
        self.GS2CPropChange('InteractDis', fDis)

    
    def ValidShare(self):
        return self.m_Share

    
    def SetShare(self, iShare):
        self.m_Share = iShare
        self.GS2CPropChange('Share', iShare)

    
    def SetFormulaArgsLimit(self, dArgs):
        self.m_FormulaLimit = dArgs

    
    def ActionType(self):
        if not self.m_Enable:
            return 0
        return self.m_ActionType

    
    def Enable(self):
        if self.m_Enable:
            return None
        self.m_Enable = 1

    
    def Disable(self):
        if not self.m_Enable:
            return None
        self.m_Enable = 0

    
    def InitCustomAttr(self, clsData, dAddData):
        clsData.InitNPCData(self, dAddData)

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeNpcAddPacket(self, dPlayer)

    
    def AddVisibleCondition(self, oConditionFunc):
        self.m_VisibleCondition.append(oConditionFunc)

    
    def ClearVisibleCondition(self):
        self.m_VisibleCondition = []

    
    def AddExtraInteractRule(self, iType, dParam):
        oRule = npcinteractrule.GetInteractRule(iType, self, dParam)
        if oRule:
            self.m_ExtraInteractRule[iType] = oRule

    
    def GetExtraInteractRule(self, iType):
        if iType not in self.m_ExtraInteractRule:
            return None
        return self.m_ExtraInteractRule[iType]

    
    def ValidInteract(self, oHero):
        if self.m_CheckInteractScene and self.m_Scene != oHero.m_Scene:
            return False
        if self.m_CheckInteractDistance and not cl_math.CheckDistance3D(oHero.GetPos(), self.GetPos(), self.m_InteractDis):
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, 'NPC距离过远')
            return False
        iStatus = self.m_PlayerInteractType[oHero.m_PlayerID]
        if iStatus & INTERACT_TYPE_ALLOW != INTERACT_TYPE_ALLOW:
            cl_notify.GS2CDebugMsg(self.m_Game, oHero.m_PlayerID, 'NPC不可交互')
            return False
        if not self.IsVisibleTo(oHero.m_PlayerID):
            return False
        for _, oRule in self.m_ExtraInteractRule.items():
            if not oRule.ValidInteract(oHero):
                oRule.SendValidInteractMsg(oHero)
                return False
        
        return True

    
    def SendInteractMsg(self, oHero):
        iInteractType = self.m_PlayerInteractType[oHero.m_PlayerID]
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_NPCINTERACT, self, {
            'pid': oHero.m_PlayerID,
            'Hero': oHero.m_ID,
            'Type': iInteractType,
            'NPC': self.m_ID,
            'NpcType': self.m_FightType })

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        pid = oHero.m_PlayerID
        self.OnInteract(oHero)
        self.SetHeroInteractStatus(pid)
        self.SendInteractMsg(oHero)
        net.GS2CNpcRefreshInfo(self, oHero)
        if self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)

    
    def StopInteract(self, oHero):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_NPCSTOPINTERACT, self, {
            'Hero': oHero.m_ID })
        self.OnStopInteract(oHero)

    
    def OnStopInteract(self, oHero):
        pass

    
    def OnInteract(self, oHero):
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, [
            oHero.m_PlayerID])

    
    def GetHeroInteractStatus(self, pid):
        if pid not in self.m_PlayerInteractStatus:
            return 0
        return self.m_PlayerInteractStatus[pid]

    
    def SetHeroInteractStatus(self, pid, iNotify = 1):
        if self.m_PlayerInteractStatus[pid] == INTERACT_STATUS_DONE:
            return None
        self.m_PlayerInteractStatus[pid] = INTERACT_STATUS_DONE
        if iNotify:
            self.NotifyInteractInfo(pid)

    
    def GetPlayerInteractType(self, pid):
        if pid not in self.m_PlayerInteractType:
            return 0
        return self.m_PlayerInteractType[pid]

    
    def SetPlayerInteractType(self, iInteractType, lstPlayer):
        if iInteractType not in (INTERACT_TYPE_FORBID, INTERACT_TYPE_ALLOW):
            return None
        for pid in lstPlayer:
            iOldType = self.m_PlayerInteractType.get(pid, -1)
            if iOldType == iInteractType:
                continue
            self.m_PlayerInteractType[pid] = iInteractType
            self.NotifyInteractInfo(pid)
        

    
    def GetPlayerAssignInteractType(self, pid):
        if pid not in self.m_PlayerAssignInteractType:
            return NPC_ACTION_NONE
        return self.m_PlayerAssignInteractType[pid]

    
    def NotifyInteractInfo(self, pid):
        net.GS2CNpcInteractState(self, pid)

    
    def SetInVisiblePlayer(self, iPlayer):
        oGame = self.m_Game
        if not self.m_VisiblePlayer:
            lstHero = oGame.m_WarMgr.GetRoomHero()
            for iHero in lstHero:
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                self.m_VisiblePlayer[oHero.m_PlayerID] = 1
            
        self.m_VisiblePlayer[iPlayer] = 0

    
    def IsVisibleTo(self, iPlayer):
        if self.m_VisiblePlayer:
            if iPlayer not in self.m_VisiblePlayer or not self.m_VisiblePlayer[iPlayer]:
                return 0
        if self.m_VisibleCondition:
            oHero = self.m_Game.m_WarMgr.GetHeroByPlayer(iPlayer)
            if not oHero:
                return 0
            for oConditionFunc in self.m_VisibleCondition:
                if not oConditionFunc(self, oHero):
                    return 0
            
        return 1

    
    def SendMsgToPlayer(self, iMsg, dMsgInfo, iCalAI):
        oWarMgr = self.m_Game.m_WarMgr
        dPlayer = oWarMgr.GetRoomPlayer(iCalAI)
        for iPlayerID in dPlayer:
            oHero = oWarMgr.GetHeroByPlayer(iPlayerID)
            if not oHero:
                continue
            if not self.IsVisibleTo(iPlayerID):
                continue
            cl_msgcenter.SendMsg(iMsg, oHero, dMsgInfo)
        

    
    def NetAddTo(self, dPlayer):
        dVisible = { }
        for iPlayer in dPlayer:
            if self.IsVisibleTo(iPlayer):
                dVisible[iPlayer] = 1
        
        if self.m_FightType in (NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_EXCHANGEGOLDENCUP):
            WarnpcLog.Debug('goldcup player:%s visible:%s' % (dPlayer, dVisible))
        super().NetAddTo(dVisible)
        for iPlayer in dVisible:
            net.GS2CNpcInteractState(self, iPlayer)
        
        if self.m_TriCenter and self.m_TriHalfExt and self.m_TriType:
            cl_snetwar.GS2CTriggerArea(self.m_Game, self.m_ID, self.m_TriType, self.m_TriCenter, self.m_TriHalfExt, dPlayer)

    
    def SetActionFunc(self, oFunc):
        self.m_ActionFunc = oFunc

    
    def MiniGameEnd(self, oMiniGame, iHero):
        pass

    
    def SetOpenCost(self, dCost, iReset):
        SendAlert('err', '%d战场 NPC%d无法设置开启消耗 请检查NPC类型' % (self.m_Game.GetWarMgr().m_SID, self.m_SID))

    
    def Refresh(self, oHero):
        pass

    
    def GetRefreshInfo(self, oHero):
        return (0, 0)

    
    def GetRefreshCost(self, oHero):
        return 0

    
    def GetChooseAllInfo(self, oHero):
        return (0, 0)

    
    def GetCreateSource(self):
        return -1

    
    def UseChooseAllTimes(self, oHero):
        pass

    
    def OnChooseOne(self, oHero, iAnswer):
        pass

    
    def OnChooseAll(self, oHero):
        pass

    
    def ValidAction(self, oHero, dInfo):
        return True

    
    def SetNpcRefreshCallBackFunction(self, oHero):
        net.SetNpcUICallBackFunction(oHero, NPC_CB_REFRESH, self.Refresh, self)

    
    def CanSharedByAI(self, oHero):
        return self.IsVisibleTo(oHero.m_PlayerID)



def SendNpcRefreshMsg(oHero, oNpc, iStage, lstAllOption):
    if iStage == 2:
        return None
    dInfo = {
        'pid': oHero.m_PlayerID,
        'Hero': oHero.m_ID,
        'NPC': oNpc.m_ID,
        'Stage': iStage,
        'AllOption': lstAllOption }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EVENTNPC_REFRESH, oNpc, dInfo)


def SendNpcChooseMsg(oHero, oNpc, iOption):
    dInfo = {
        'pid': oHero.m_PlayerID,
        'Hero': oHero.m_ID,
        'NPC': oNpc.m_ID,
        'Option': iOption }
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EVENTNPC_CHOOSE, oNpc, dInfo)
    cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_EVENTNPC_CHOOSE, oHero, dInfo)

