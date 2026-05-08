# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/connecttransfernpc.pyc
# RelativePath: clientlogic/cl_npc/connecttransfernpc.pyc
# Source Generated with Decompyle++
# File: connecttransfernpc.pyc (Python 3.6)

from cl_commondefines import SCENE_EVT_SHAPE_RECTANGLE, SIDE_TYPE_HERO, MINIMAPPT_SHOW_HIGHLIGHT, MINIMAPPT_OPER_SHOW, MINIMAPPT_OPER_HIDE, TRIGGER_AREA_INTERACT, MINIMAPPT_TYPE_CONNECTTRANS
from cl_pxlayer import PXMASK_SKILLBLK
from cl_only import Functor, GAME_FRAME
import cl_npc.net as npcnet
import cl_math
import cl_msgcenter
import cl_snetwar
from . import mobject

class CConnectTransferNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super(CConnectTransferNPC, self).__init__(*args)
        self.m_Group = None
        self.m_TransPos = None
        self.m_TransFacing = None
        self.m_TriShape = None
        self.m_TriDir = None
        self.m_TipCenter = None
        self.m_TipHalfExt = None
        self.m_TriEvent = None
        self.m_TipEvent = None
        self.m_SelfPt = None
        self.m_TransPt = None
        self.m_DelayTransTip = { }
        self.m_LevelGoal = False
        self.m_Target = None

    
    def OnLevelGoal(self):
        self.m_LevelGoal = True
        if not (self.m_SelfPt) or not (self.m_TransPt):
            return None
        lstPlayer = self.m_Game.m_WarMgr.GetLivePlayer()
        self.SetMiniMapTips([
            self.m_SelfPt,
            self.m_TransPt], MINIMAPPT_OPER_HIDE, lstPlayer)

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            return None
        self.Transfer(oHero.m_ID)
        self.DoAction(oHero)

    
    def DoAction(self, oHero):
        if self.m_ActionFunc:
            self.m_ActionFunc(self, oHero)

    
    def ValidInteract(self, oHero):
        if not self.TryTransfer(oHero.m_ID):
            return False
        return super(CConnectTransferNPC, self).ValidInteract(oHero)

    
    def Release(self):
        self.DestoryTriggerArea()
        super(CConnectTransferNPC, self).Release()

    
    def InitCustomAttr(self, clsData, dAddData):
        super(CConnectTransferNPC, self).InitCustomAttr(clsData, dAddData)
        sGroup = dAddData['Group']
        self.m_Group = sGroup
        self.m_TriCenter = dAddData['Center']
        self.m_TriShape = SCENE_EVT_SHAPE_RECTANGLE
        self.m_TriType = TRIGGER_AREA_INTERACT
        self.m_TriHalfExt = dAddData['HalfExt']
        self.m_TriDir = dAddData['Facing']
        self.m_TipCenter = dAddData['TipCenter']
        self.m_TipHalfExt = dAddData['TipHalfExt']

    
    def OnGoto(self):
        super().OnGoto()
        self.SetTipEvent()

    
    def SetTransEvent(self):
        if not (self.m_TriCenter) or not (self.m_TriHalfExt):
            return None
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        (iLevel, _, _) = self.m_LineIdx
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        oScene = self.m_Game.m_SceneMgr.GetScene(oLevelNode.m_Scene)
        enterfunc = OnHeroTriggerTransfer
        leavefunc = None
        self.m_TriEvent = oScene.AddSceneEvent(self, enterfunc, leavefunc, self.m_TriShape, (self.m_TriCenter, self.m_TriHalfExt), {
            'Dir': self.m_TriDir }, False)

    
    def SetTransInfoByTargetNpc(self, oTarget):
        if not (self.m_TriCenter) or not (self.m_TriHalfExt):
            return None
        self.m_Target = oTarget.m_ID
        vTransferPos = oTarget.GetPos()
        vTransFacing = oTarget.GetFacing()
        fMoveDis = 1
        vTransferPos = cl_math.Vec3DisplaceDir(vTransferPos, vTransFacing, fMoveDis)
        fGroundDis = self.m_Game.Scene_GroundDistance(oTarget.m_Scene, vTransferPos, 5, PXMASK_SKILLBLK)
        self.m_TransPos = (vTransferPos[0], vTransferPos[1] - fGroundDis, vTransferPos[2])
        self.m_TransFacing = vTransFacing
        self.InitMiniMapPt()

    
    def GetTarget(self):
        if self.m_Target:
            return self.m_Game.GetObject(self.m_Target)

    
    def Transfer(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        if not (self.m_TransPos) or not (self.m_TransFacing):
            return None
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_INTERACTTRANSFER, oHero, {
            'TransferDir': self.m_TriDir })
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
        oTransferCtrl = oSurvivorElement.m_TransferCtrl
        oTransferCtrl.RecordHeroLastUsedFrame(self.m_Group, iHero)
        oHero.Stop()
        oHero.WalkTo(self.m_TransPos)
        vFacing = self.m_TransFacing
        vFacing = (int(vFacing[0] * 127) + 128, int(vFacing[1] * 127) + 128, int(vFacing[2] * 127) + 128)
        self.m_DelayTransTip[iHero] = 1
        npcnet.GS2CTransferFace(self, vFacing, oHero.m_PlayerID)
        oTarget = self.GetTarget()
        if oTarget:
            oTarget.DoAction(oHero)

    
    def TryTransfer(self, iHero):
        oSurvivorElement = self.m_Game.m_WarMgr.GetComponent('SurvivorElement')
        if not oSurvivorElement:
            return False
        oTransferCtrl = oSurvivorElement.m_TransferCtrl
        if not oTransferCtrl.ValidTransfer(self.m_Group, self.m_ID, iHero):
            return False
        return True

    
    def SetTipEvent(self):
        if not (self.m_TipCenter) or not (self.m_TipHalfExt):
            return None
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        (iLevel, _, _) = self.m_LineIdx
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        oScene = self.m_Game.m_SceneMgr.GetScene(oLevelNode.m_Scene)
        enterfunc = OnHeroApproachTransfer
        leavefunc = OnHeroDepartTransfer
        self.m_TipEvent = oScene.AddSceneEvent(self, enterfunc, leavefunc, self.m_TriShape, (self.m_TipCenter, self.m_TipHalfExt), {
            'Dir': self.m_TriDir }, False)

    
    def InitMiniMapPt(self):
        if not (self.m_TipCenter) or not (self.m_TipHalfExt):
            return None
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        (iLevel, _, _) = self.m_LineIdx
        oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
        iShowMode = MINIMAPPT_SHOW_HIGHLIGHT
        iType = MINIMAPPT_TYPE_CONNECTTRANS
        iSelfPt = oMiniMap.NewPtID()
        self.m_SelfPt = (iSelfPt, iType, iShowMode, self.GetPos())
        iTransPt = oMiniMap.NewPtID()
        self.m_TransPt = (iTransPt, iType, iShowMode, self.m_TransPos)

    
    def SetMiniMapTips(self, lstPt, iOperate, lstPlayer):
        (iLevel, _, _) = self.m_LineIdx
        cl_snetwar.GS2CUpdateMiniMapPos(self, iLevel, iOperate, lstPt, lstPlayer)

    
    def OnApproach(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        self.SetMiniMapTips([
            self.m_SelfPt,
            self.m_TransPt], MINIMAPPT_OPER_SHOW, [
            oHero.m_PlayerID])

    
    def OnDepart(self, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        if iHero in self.m_DelayTransTip and self.m_DelayTransTip[iHero]:
            self.m_DelayTransTip[iHero] = 0
            func = Functor(self.OnDepart, iHero)
            self.Call_Out(func, GAME_FRAME, 'transfertips')
        else:
            self.Remove_Call_Out('transfertips')
            self.SetMiniMapTips([
                self.m_SelfPt,
                self.m_TransPt], MINIMAPPT_OPER_HIDE, [
                oHero.m_PlayerID])

    
    def DestoryTriggerArea(self):
        oGame = self.m_Game
        iScene = self.m_Scene
        oScene = oGame.m_SceneMgr.GetScene(iScene)
        if self.m_TriEvent:
            oScene.RemoveSceneEvent(self.m_TriEvent)
            self.m_TriEvent = None
        if self.m_TipEvent:
            oScene.RemoveSceneEvent(self.m_TipEvent)
            self.m_SelfPt = None
            self.m_TransPt = None
            self.m_TipEvent = None



def ValidTrigger(oListener, dMsgInfo):
    if not oListener:
        return False
    iTriggerObj = dMsgInfo['VID']
    oTrigger = oListener.m_Game.GetObject(iTriggerObj)
    if not oTrigger:
        return False
    if oTrigger.m_Side != SIDE_TYPE_HERO:
        return False
    return True


def OnHeroTriggerTransfer(oListener, dMsgInfo):
    if not ValidTrigger(oListener, dMsgInfo):
        return None
    oTrigger = oListener.m_Game.GetObject(dMsgInfo['VID'])
    oListener.TryTransfer(oTrigger.m_ID)


def OnHeroApproachTransfer(oListener, dMsgInfo):
    if not ValidTrigger(oListener, dMsgInfo):
        return None
    oTrigger = oListener.m_Game.GetObject(dMsgInfo['VID'])
    oListener.OnApproach(oTrigger.m_ID)


def OnHeroDepartTransfer(oListener, dMsgInfo):
    if not ValidTrigger(oListener, dMsgInfo):
        return None
    oTrigger = oListener.m_Game.GetObject(dMsgInfo['VID'])
    oListener.OnDepart(oTrigger.m_ID)

