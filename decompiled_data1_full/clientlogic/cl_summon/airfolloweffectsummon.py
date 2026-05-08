# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/airfolloweffectsummon.pyc
# RelativePath: clientlogic/cl_summon/airfolloweffectsummon.pyc
# Source Generated with Decompyle++
# File: airfolloweffectsummon.pyc (Python 3.6)

from cl_commondefines import WARRIOR_SUMMON_AIRFOLLOWEFFECT
from cl_only import PY_FLAG_DEAD, GAME_FRAME
from . import mobject
import cl_movectrl.net as movenet
import cl_msgcenter
import cl_math
import cl_netattr

class CAirFollowEffectSummon(mobject.CBaseSummon):
    m_FightType = WARRIOR_SUMMON_AIRFOLLOWEFFECT
    
    def __init__(self, oGame, nid):
        super().__init__(oGame, nid)
        self.m_AllLifeFrame = 0
        self.m_FollowTarget = 0
        self.m_BaseRangeRadius = 4
        self.m_BaseScale = 100
        self.m_ScaleFactor = { }

    
    def MapSendPacket(self, dPlayer):
        oOwner = self.GetOwner()
        if not oOwner:
            return None
        if oOwner.m_PlayerID not in dPlayer:
            return None
        dPlayer = {
            oOwner.m_PlayerID: 1 }
        cl_netattr.MakeSummonAddPacket(self, dPlayer)
        self.GS2CSyncLifeTime()

    
    def OnInitAttr(self, clsData, dAddData):
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, self.OwnerEnterScene, 'OwnerEnterScene')
        cl_msgcenter.AddAttentionFunc(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, self.OwnerLeaveScene, 'OwnerLeaveScene')

    
    def Remove(self, sReason):
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_ENTERSCENE, 'OwnerEnterScene')
        cl_msgcenter.DoneAttention(self, self.m_Owner, cl_msgcenter.MSG_WAR_LEAVESCENE, 'OwnerLeaveScene')
        super().Remove(sReason)

    
    def SetFollowTarget(self, iTarget):
        self.m_FollowTarget = iTarget

    
    def UpdateFollowPos(self, iIntervalTime = 100, iRandomDeviation = 0):
        iTarget = self.m_FollowTarget
        oTarget = self.m_Game.GetObject(iTarget, PY_FLAG_DEAD)
        if not oTarget:
            self.m_FollowTarget = 0
            return None
        self.UpdateMovePos(oTarget.GetPos(), iIntervalTime, iRandomDeviation)

    
    def UpdateMovePos(self, vMovePos, iIntervalTime = 100, iRandomDeviation = 0):
        if not self.m_Scene:
            return None
        fSpeed = self.MoveSpeed()
        fStepDis = fSpeed * (iIntervalTime / 100)
        vStart = self.GetPos()
        fDis = cl_math.CalDistance3D(vStart, vMovePos)
        if fDis > fStepDis:
            vMovePos = cl_math.Vec3DisplacePos(vStart, vMovePos, fStepDis)
        elif iRandomDeviation:
            vMovePos = cl_math.GetPointInCircle(self.m_Game, vMovePos, iRandomDeviation)
        fDis = cl_math.CalDistance3D(vStart, vMovePos)
        fSpeed = min(fSpeed, fDis / iIntervalTime / 100)
        movenet.GS2CMapAirTrack(self, fSpeed, vStart, vMovePos)
        self.m_Game.Scene_Walk(self.m_ID, vMovePos)
        self.RefreshPos()

    
    def OwnerEnterScene(self, oSummon, oHero, dMsgInfo):
        iScene = oHero.m_Scene
        tPos = oHero.GetPos()
        if iScene == self.m_Scene:
            self.WalkTo(tPos)
        else:
            self.Goto(iScene, tPos)

    
    def OwnerLeaveScene(self, oSummon, oHero, dMsgInfo):
        self.LeaveScene(dMsgInfo['NewScene'])
        if self.m_Scene:
            self.RemoveFromScene()

    
    def SetScaleFactor(self, sKey, iValue):
        self.m_ScaleFactor[sKey] = iValue

    
    def ClearScaleFactor(self, sKey):
        self.m_ScaleFactor.pop(sKey, 0)

    
    def GetCurScale(self):
        iCurScale = self.m_BaseScale + sum(self.m_ScaleFactor.values())
        return iCurScale

    
    def GetCurRangeRadius(self):
        iScale = self.GetCurScale()
        return int(iScale * self.m_BaseRangeRadius / 100)

    
    def SetLifeFrame(self, iFrame):
        iRemainFrame = self.RemainFrame()
        self.m_AllLifeFrame = (self.m_AllLifeFrame - iRemainFrame) + iFrame
        super().SetLifeFrame(iFrame)
        self.GS2CSyncLifeTime()

    
    def AllLifeTime(self):
        return (self.m_AllLifeFrame // GAME_FRAME) * 100

    
    def GS2CSyncLifeTime(self):
        self.GS2CPropChange('LifeTime')
        self.GS2CPropChange('AllLifeTime')


