# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_summon/mobject.pyc
# RelativePath: clientlogic/cl_summon/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from __future__ import absolute_import
from cl_commondefines import WARRIOR_SUMMON, TURN_SPEED_BASE, SIDE_TYPE_OBSTACLE
from cl_only import Functor, GAME_FRAME, PY_FLAG_DIED
import cl_warrior
import cl_netattr
import cl_msgcenter
import cl_facectrl

class CBaseSummon(cl_warrior.CWarrior):
    m_SID = 0
    m_Name = ''
    m_Type = 'Summon'
    m_Shape = 0
    m_AttDis = 5
    m_Delete = 1
    m_RemoveDelay = 0
    m_FightType = WARRIOR_SUMMON
    m_DieAction = None
    m_RemoveAction = None
    m_ClientSummonID = 0
    m_ScenesRemoveDelayFrame = 1
    m_AddGrade = 0
    
    def __init__(self, oGame, nid):
        super(CBaseSummon, self).__init__(oGame, nid)
        self.m_Data = { }
        self.m_PlayerID = 0
        self.m_LifeFrame = 0
        self.m_LifeStart = 0
        self.m_Prefab = 0
        self.m_RecoredSceneEvt = { }
        self.m_Collider = None
        self.m_ClientOwner = 0
        self.m_Owner = 0
        self.m_BodyPart = ()
        self.m_SrcWeapon = 0
        self.m_SrcPerform = 0
        self.m_AttachTarget = 0
        self.m_TurnSpeed = TURN_SPEED_BASE
        self.m_FaceCtrl = cl_facectrl.CFaceStatusMgr(self)

    
    def InitSummon(self, clsData, dAddData):
        clsData.InitSummonData(self, dAddData)
        self.m_SrcWeapon = dAddData['Weapon'] if 'Weapon' in dAddData else self.m_ID
        self.m_SrcPerform = dAddData['SrcPerform'] if 'SrcPerform' in dAddData else self.m_ID
        self.OnInitAttr(clsData, dAddData)
        func = clsData.m_Action
        if func:
            func(self)
        self.InitWarValue()
        if self.m_Owner:
            oOwner = self.GetOwner()
            self.m_OwnerPlayerID = oOwner.m_PlayerID
            oOwner.AddSummon(self.m_ID)
            dMsg = {
                'ItemID': self.m_SrcWeapon,
                'pfid': self.m_SrcPerform,
                'Summon': self.m_ID,
                'VID': self.m_AttachTarget }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CREATESUMMON, oOwner, dMsg, oGame = self.m_Game)

    
    def OnInitAttr(self, clsData, dAddData):
        pass

    
    def OnInitToScene(self, tPos):
        super(CBaseSummon, self).OnInitToScene(tPos)
        if self.m_DieAction:
            cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DIE, self.OnSummonDie, 'SummonDieAction')

    
    def Name(self):
        return self.m_Name

    
    def TurnSpeed(self):
        return self.m_TurnSpeed

    
    def SetLifeFrame(self, iFrame):
        self.Remove_Call_Out('Remove')
        self.m_LifeStart = self.m_Game.GetFrameNum()
        self.m_LifeFrame = iFrame
        self.DelayRemove('到时删除')

    
    def DelayRemove(self, sReason):
        self.Call_Out(Functor(self.Remove, sReason), self.m_LifeFrame, 'Remove')

    
    def LifeTime(self):
        return (self.m_LifeFrame // GAME_FRAME) * 100

    
    def LifeFrame(self):
        return self.m_LifeFrame

    
    def RemainFrame(self):
        iRemainFrame = 0
        if self.m_LifeFrame:
            iRemainFrame = self.m_LifeStart + self.m_LifeFrame - self.m_Game.GetFrameNum()
            if iRemainFrame < 0:
                iRemainFrame = 0
        return iRemainFrame

    
    def Remove(self, sReason):
        self.Remove_Call_Out('Remove')
        oOwner = self.GetOwner()
        if oOwner:
            if self.m_ID in oOwner.m_SummonDict:
                oOwner.m_SummonDict.pop(self.m_ID)
            dMsg = {
                'ItemID': self.m_SrcWeapon,
                'pfid': self.m_SrcPerform,
                'summonId': self.m_ID }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_REMOVESUMMON, oOwner, dMsg, oGame = self.m_Game)
            if self.m_RemoveAction:
                self.m_RemoveAction(self)
                self.m_RemoveAction = None
        super(CBaseSummon, self).Remove(sReason)

    
    def HeartBeat(self):
        pass

    
    def MapSendPacket(self, dPlayer):
        cl_netattr.MakeSummonAddPacket(self, dPlayer)

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def TriggerSummon(self, dTrigger):
        pass

    
    def OnSummonDie(self, oSummon, dMsgInfo):
        if not self.m_DieAction:
            return None
        iAttack = dMsgInfo['AID']
        oKiller = self.m_Game.GetObject(iAttack)
        if oKiller and oKiller.m_Owner:
            oKiller = self.m_Game.GetObject(oKiller.m_Owner)
        func = self.m_DieAction
        self.m_DieAction = None
        func(self, oKiller)

    
    def GetScenesRemoveDelayFrame(self):
        return self.m_ScenesRemoveDelayFrame

    
    def ScenesRemoveDelay(self, sReason):
        self.m_Game.SetPyFlag(self.m_ID, PY_FLAG_DIED, 1)
        self.LeaveScene(0)
        self.RemoveFromScene()
        self.Call_Out(Functor(self.Remove, sReason), self.m_ScenesRemoveDelayFrame, sReason)


