# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/survivor/connecttransfernpcctrl.pyc
# RelativePath: clientlogic/cl_warmgr/survivor/connecttransfernpcctrl.pyc
# Source Generated with Decompyle++
# File: connecttransfernpcctrl.pyc (Python 3.6)

from cl_only import SendAlert
import cl_msgcenter

class CConnectTransferNpcCtrl(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_TransferNpc = { }
        self.m_GroupCDFrame = { }
        self.m_HeroLastUesdFrame = { }
        self.Init()

    
    def Init(self):
        self.m_Game.AddGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, self.OnLevelGoal, 'ConnectTransfer')

    
    def Release(self):
        self.m_Game.DoneGlobalAttention(self.m_Game.m_WarMgr.m_ID, cl_msgcenter.MSG_WARMGR_LEVELNODEGOALOK, 'ConnectTransfer')
        self.m_Game = None
        self.m_TransferNpc = { }
        self.m_GroupCDFrame = { }
        self.m_HeroLastUesdFrame = { }

    
    def Clear(self):
        self.m_TransferNpc = { }
        self.m_GroupCDFrame = { }
        self.m_HeroLastUesdFrame = { }

    
    def OnLevelGoal(self, oWarMgr, oTarget, dInfo):
        for lstTransferNpc in self.m_TransferNpc.values():
            for iNpc in lstTransferNpc:
                oNpc = self.m_Game.GetObject(iNpc)
                if oNpc:
                    oNpc.OnLevelGoal()
            
        

    
    def AddTransferNpc(self, sGroup, iTransferNpc):
        if sGroup not in self.m_TransferNpc:
            self.m_TransferNpc[sGroup] = []
        if len(self.m_TransferNpc[sGroup]) > 1:
            return None
        self.m_TransferNpc[sGroup].append(iTransferNpc)

    
    def RefreshTransferInfo(self):
        oGame = self.m_Game
        for sGroup in self.m_TransferNpc.keys():
            lstTransferID = self.m_TransferNpc[sGroup]
            if len(lstTransferID) != 2:
                oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
                oLevelNode = oLevelCtrl.m_CurNode
                SendAlert('关卡%s 传送门组%s 配置信息有误，请检查' % (oLevelNode.m_Level, sGroup))
                continue
            (iTransferNpc1, iTransferNpc2) = lstTransferID
            oTransferNpc1 = oGame.GetObject(iTransferNpc1)
            oTransferNpc2 = oGame.GetObject(iTransferNpc2)
            if not oTransferNpc1 or not oTransferNpc2:
                return None
            oTransferNpc1.SetTransInfoByTargetNpc(oTransferNpc2)
            oTransferNpc2.SetTransInfoByTargetNpc(oTransferNpc1)
        

    
    def SetGroupCDFrame(self, sGroup, iFrame):
        self.m_GroupCDFrame[sGroup] = iFrame

    
    def RecordHeroLastUsedFrame(self, sGroup, iHero):
        if sGroup not in self.m_HeroLastUesdFrame:
            self.m_HeroLastUesdFrame[sGroup] = { }
        self.m_HeroLastUesdFrame[sGroup][iHero] = self.m_Game.GetFrameNum()

    
    def ValidHeroTransfer(self, sGroup, iHero):
        if sGroup not in self.m_HeroLastUesdFrame:
            return True
        if iHero not in self.m_HeroLastUesdFrame[sGroup]:
            return True
        if self.m_HeroLastUesdFrame[sGroup][iHero] + self.m_GroupCDFrame[sGroup] < self.m_Game.GetFrameNum():
            return True
        return False

    
    def ValidTransfer(self, sGroup, iTransferNpc, iHero):
        if sGroup not in self.m_TransferNpc:
            return False
        if iTransferNpc not in self.m_TransferNpc[sGroup]:
            return False
        if not self.ValidHeroTransfer(sGroup, iHero):
            return False
        return True



def NewConnectTransferNpcCtrl(oGame):
    return CConnectTransferNpcCtrl(oGame)

