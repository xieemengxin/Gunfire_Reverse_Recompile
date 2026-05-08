# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/leveltransfernpc.pyc
# RelativePath: clientlogic/cl_npc/leveltransfernpc.pyc
# Source Generated with Decompyle++
# File: leveltransfernpc.pyc (Python 3.6)

from cl_commondefines import INTERACT_TYPE_ALLOW, INTERACT_TYPE_FORBID, INTERACT_STATUS_PEND, INTERACT_STATUS_PEND2, INTERACT_STATUS_DONE, TRANSFER_DIRTO_NULL, INTERACT_RULE_CDNOTIFY, TRANSFER_DIRTO_HIDE, TRANSFER_DIRTO_MAIN
import cl_msgcenter
from . import mobject
from . import net
DELAYCD_FRAME = 750

class CLevelTransferNPC(mobject.CNPC):
    m_Type = 'Transfer'
    
    def __init__(self, *args):
        super(CLevelTransferNPC, self).__init__(*args)
        self.m_TransferDir = TRANSFER_DIRTO_NULL
        self.SetInitInteract(INTERACT_TYPE_FORBID)

    
    def InitCustomAttr(self, clsData, dAddData):
        clsData.InitNPCData(self, dAddData)
        if not self.m_TransferDir:
            self.m_TransferDir = dAddData.get('TransferDir', TRANSFER_DIRTO_NULL)
        if self.m_TransferDir in (TRANSFER_DIRTO_HIDE, TRANSFER_DIRTO_MAIN):
            self.SetInitInteract(INTERACT_TYPE_ALLOW)
            if self.m_TransferDir == TRANSFER_DIRTO_HIDE:
                self.OnHideTransferInit(dAddData)
            else:
                oWarMgr = self.m_Game.m_WarMgr
                cl_msgcenter.AddAttentionFunc(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoalTransfer, 'LevelGoalTransfer')

    
    def OnInteract(self, oHero):
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WARMGR_INTERACTTRANSFER, oHero, {
            'TransferDir': self.m_TransferDir })

    
    def SetHeroInteractStatus(self, pid, iNotify = 1):
        dPlayerStat = self.m_PlayerInteractStatus
        if dPlayerStat[pid] == INTERACT_STATUS_PEND:
            dPlayerStat[pid] = INTERACT_STATUS_DONE
        elif dPlayerStat[pid] == INTERACT_STATUS_DONE:
            dPlayerStat[pid] = INTERACT_STATUS_PEND
        if iNotify:
            self.NotifyInteractInfo(pid)

    
    def SetHeroInteractStatusDone(self, pid, iNotify = 1):
        self.m_PlayerInteractStatus[pid] = INTERACT_STATUS_PEND2
        self.m_PlayerInteractType[pid] = INTERACT_TYPE_FORBID
        if iNotify:
            self.NotifyInteractInfo(pid)

    
    def OnLevelGoalTransfer(self, oNpc, oOwner, dMsgInfo):
        iLevel = dMsgInfo['LevelID']
        tLineIdx = self.m_LineIdx
        if not tLineIdx or tLineIdx[0] != iLevel:
            return None
        oWarMgr = self.m_Game.m_WarMgr
        lstPlayer = oWarMgr.GetAllPlayer()
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'LevelGoalTransfer')
        self.SetPlayerInteractType(INTERACT_TYPE_ALLOW, lstPlayer)

    
    def Release(self):
        super(CLevelTransferNPC, self).Release()
        oWarMgr = self.m_Game.m_WarMgr
        cl_msgcenter.DoneAttention(self, oWarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'LevelGoalTransfer')

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        iHideType = 0
        iHideLevel = 0
        if self.m_TransferDir == TRANSFER_DIRTO_HIDE:
            oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
            iHideLevel = self.Query('HideLevel')
            iHideType = oLevelCtrl.m_HideLevelLib.get(iHideLevel, 0)
        net.GS2CTransferDir(self.m_Game, dPlayer, self.m_ID, self.m_TransferDir, iHideType, iHideLevel)
        dParam = self.m_ModelData.GetClientData()
        if not dParam['Scale'] == (100, 100, 100):
            net.GS2CTransferScale(self.m_Game, dPlayer, self, dParam['Scale'])

    
    def SetTransferDir(self, iDir):
        self.m_TransferDir = iDir
        net.GS2CTransferDir(self.m_Game, self.m_Game.GetRealPlayers(), self.m_ID, self.m_TransferDir, iHideType = 0, iHideLevel = 0)

    
    def OnHideTransferInit(self, dAddData):
        iLevel = dAddData['HideLevel']
        oLevelCtrl = self.m_Game.m_WarMgr.GetComponent('LevelCtrl')
        oLevelConfData = oLevelCtrl.m_LevelConfData
        iEnterEffect = oLevelConfData.GetLevelConfig(iLevel, 'EnterEffect', default = 0)
        if iEnterEffect:
            self.m_Shape = iEnterEffect
        self.AddExtraInteractRule(INTERACT_RULE_CDNOTIFY, {
            'Time': 3000,
            'Notify': 2231 })
        self.Set('HideLevel', dAddData['HideLevel'])
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.SetPlayerInteractType(INTERACT_TYPE_ALLOW, lstPlayer)

    
    def CheckTransferLevel(self, oHero):
        oGame = self.m_Game
        oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
        dReady = oLevelCtrl.GetReadyTransferPlayer()
        lstPlayer = oGame.m_WarMgr.GetLivePlayer()
        for iPlayer in lstPlayer:
            if iPlayer not in dReady:
                break
        else:
            return False
        return True


