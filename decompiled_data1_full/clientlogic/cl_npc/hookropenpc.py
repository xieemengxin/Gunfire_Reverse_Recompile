# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/hookropenpc.pyc
# RelativePath: clientlogic/cl_npc/hookropenpc.pyc
# Source Generated with Decompyle++
# File: hookropenpc.pyc (Python 3.6)

from cl_cscommondef import STATUS_HOOKROPE
from . import mobject

class CHookRopeNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super(CHookRopeNPC, self).__init__(*args)
        self.m_AttachTarget = 0

    
    def InitCustomAttr(self, clsData, dAddData):
        super(CHookRopeNPC, self).InitCustomAttr(clsData, dAddData)
        self.m_BornPos = dAddData['BornPos']

    
    def NetAddTo(self, dPlayer):
        super().NetAddTo(dPlayer)
        oGame = self.m_Game
        oTargetNpc = oGame.GetObject(self.m_AttachTarget)
        if not oTargetNpc:
            return None
        vBornPos = oTargetNpc.GetBornPos()
        for iPlayer in dPlayer:
            oHero = oGame.m_WarMgr.GetHeroByPlayer(iPlayer)
            if oHero and oHero.Query('CurHookRopeNpc') == self.m_ID:
                oHero.WalkTo(vBornPos)
        

    
    def ValidInteract(self, oHero):
        if not self.m_AttachTarget:
            return False
        if oHero.Query('CurHookRopeNpc'):
            return False
        return super().ValidInteract(oHero)

    
    def Interact(self, oHero, iType = 0):
        if not self.ValidInteract(oHero):
            oHero.m_MoveCtrl.Stop(oHero, 'InValidInteract')
            return None
        self.OnInteract(oHero)
        self.SendInteractMsg(oHero)

    
    def OnInteract(self, oHero):
        oStatus = oHero.m_MoveCtrl.GetStatus(STATUS_HOOKROPE)
        oStatus.SetHookRopeID(self.m_ID)

    
    def BindTargetHookRopeNpc(self, oTarget):
        self.m_AttachTarget = oTarget.m_ID
        self.GS2CPropChange('AttachTarget', self.m_AttachTarget)

    
    def GetTargetHookRopeNpcID(self):
        return self.m_AttachTarget

    
    def GetBornPos(self):
        return self.m_BornPos


