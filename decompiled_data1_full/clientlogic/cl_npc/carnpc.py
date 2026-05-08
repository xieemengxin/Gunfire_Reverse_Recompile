# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/carnpc.pyc
# RelativePath: clientlogic/cl_npc/carnpc.pyc
# Source Generated with Decompyle++
# File: carnpc.pyc (Python 3.6)

from cl_commondefines import WARRIOR_HERO, WARRIOR_MONSTER, MODEL_TYPE_SPHERE, INTERACT_TYPE_FORBID, TURN_SPEED_BASE, NPC_CAT_PHASE_INIT, NPC_CAT_PHASE_ING, NPC_CAT_PHASE_SUC, NPC_CAT_PHASE_FAIL
from cl_pxlayer import PXLAYER_EBULLET
import cl_engphyobj
import cl_facectrl
import cl_snetwar
import cl_math
from . import mobject

class CCarNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super().__init__(*args)
        self.m_Path = []
        self.m_Trigger = None
        self.m_TriggerRadius = 1
        self.m_Area = {
            'Monster': { },
            'Hero': { } }
        self.m_TurnSpeed = TURN_SPEED_BASE
        self.m_Moving = False
        self.m_CurPathIndex = 0
        self.m_Phase = NPC_CAT_PHASE_INIT

    
    def GetPathInfo(self):
        return (self.m_CurPathIndex, self.m_Path)

    
    def TurnSpeed(self):
        return self.m_TurnSpeed

    
    def SetTriggerRadius(self, fRadius):
        self.m_TriggerRadius = fRadius

    
    def OnInteract(self, oHero):
        pass

    
    def Release(self):
        if self.m_Trigger:
            self.m_Trigger.Unstall()
            self.m_Trigger = None
        super().Release()

    
    def OnStopInteract(self, oHero):
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, self.m_Game.m_WarMgr.GetRoomPlayer())

    
    def SetPhase(self, iPhase):
        if iPhase != self.m_Phase:
            self.m_Phase = iPhase
            self.GS2CPropChange('Phase')

    
    def SetPath(self, iPath):
        lstPath = self.Query('Paths', [])
        if iPath >= len(lstPath):
            return None
        self.m_Path = [
            self.GetPos()] + lstPath[iPath]
        self.m_CurPathIndex = 1
        self.CheckTriggerMove()

    
    def OnInitToScene(self, tPos):
        super().OnInitToScene(tPos)
        dShape = {
            'Shape': MODEL_TYPE_SPHERE,
            'Center': self.GetCenterPosition(),
            'Radius': self.m_TriggerRadius }
        self.m_Trigger = cl_engphyobj.CreateAttachEventObject(self.m_Game, self, PXLAYER_EBULLET, dShape, self.OnTrigger)
        self.m_Trigger.rigidbody.E_SetKinematic(1)
        self.m_Trigger.Disable()
        self.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(self)

    
    def StartConvoy(self):
        self.m_Trigger.Enable()
        self.SetPhase(NPC_CAT_PHASE_ING)

    
    def EndConvoy(self, iSuc):
        self.m_Trigger.Disable()
        if iSuc:
            self.SetPhase(NPC_CAT_PHASE_SUC)
        else:
            self.SetPhase(NPC_CAT_PHASE_FAIL)

    
    def OnTrigger(self, obj, iLeave):
        if not obj:
            return None
        if obj.m_FightType & WARRIOR_HERO == WARRIOR_HERO:
            dCount = self.m_Area['Hero']
        elif obj.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
            dCount = self.m_Area['Monster']
        else:
            return None
        if not iLeave:
            dCount[obj.m_ID] = 1
        else:
            dCount.pop(obj.m_ID, 0)
        self.CheckTriggerMove()

    
    def MoveEndCB(self, oOwner, vPos, iFail):
        vCurPos = self.GetPos()
        if self.m_Path and cl_math.CheckDistance(vCurPos, self.m_Path[self.m_CurPathIndex], 0.5):
            self.m_CurPathIndex += 1
        self.CheckTriggerMove()

    
    def CheckTriggerMove(self):
        if self.m_Area['Hero'] and not self.m_Area['Monster'] and self.m_Path and self.m_CurPathIndex < len(self.m_Path):
            self.m_Moving = True
            self.m_FaceCtrl.FacePos(self, self.m_Path[self.m_CurPathIndex], 'TriggerMove')
            self.m_MoveCtrl.SeekPath(self, self.m_Path[self.m_CurPathIndex], self.MoveEndCB)
            cl_snetwar.GS2CMonsterActionSM(self, 2, 'Patrol', 1)
        elif self.m_Moving:
            self.m_Moving = False
            self.m_MoveCtrl.Stop(self)
            cl_snetwar.GS2CMonsterActionSM(self, 2, 'Patrol', 0)


