# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/magicbox.pyc
# RelativePath: clientlogic/cl_npc/magicbox.pyc
# Source Generated with Decompyle++
# File: magicbox.pyc (Python 3.6)

from cl_commondefines import ANIMATOR_BOXOPEN, ANIMATOR_BOXCLOSE, INTERACT_TYPE_FORBID
import cl_minigame.mobject
from . import mobject
from . import net

class CBoxNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super(CBoxNPC, self).__init__(*args)

    
    def OnInteract(self, oHero):
        super().OnInteract(oHero)
        self.BoxModelOpen(oHero.m_PlayerID)

    
    def InitCustomAttr(self, clsData, dAddData):
        super().InitCustomAttr(clsData, dAddData)
        self.InitBoxModelClose()

    
    def InitBoxModelClose(self):
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.Set('Animator', { }.fromkeys(lstPlayer, ANIMATOR_BOXCLOSE))
        self.AddExtPacket('Animator', CBoxNPC.GS2CAnimator)

    
    def BoxModelOpen(self, iPlayer):
        dPlayerAnimator = self.SetDefault('Animator', { })
        dPlayerAnimator[iPlayer] = ANIMATOR_BOXOPEN
        self.GS2CAnimator(iPlayer)

    
    def BoxModelClose(self, iPlayer):
        dPlayerAnimator = self.SetDefault('Animator', { })
        dPlayerAnimator[iPlayer] = ANIMATOR_BOXCLOSE
        self.GS2CAnimator(iPlayer)

    
    def GS2CAnimator(self, dPlayer):
        if isinstance(dPlayer, int):
            dPlayer = {
                dPlayer: 1 }
        dPlayerAnimator = self.SetDefault('Animator', { })
        for pid in dPlayer:
            if pid not in dPlayerAnimator:
                dPlayerAnimator[pid] = ANIMATOR_BOXOPEN
            net.GS2CNpcAnimator(self, pid, dPlayerAnimator[pid])
        

    
    def MiniGameEnd(self, oMiniGame, iHero):
        oHero = self.m_Game.GetObject(iHero)
        if not oHero:
            return None
        if isinstance(oMiniGame, cl_minigame.mobject.CRewardChooseGame):
            self.BoxModelClose(oHero.m_PlayerID)



class CItemBoxNPC(CBoxNPC):
    
    def BoxModelOpen(self, iPlayer):
        dPlayerAnimator = self.SetDefault('Animator', { })
        dPlayer = { }
        for iPlayer in dPlayerAnimator:
            dPlayerAnimator[iPlayer] = ANIMATOR_BOXOPEN
            dPlayer[iPlayer] = 1
        
        self.GS2CAnimator(dPlayer)

    
    def OnInteract(self, oHero):
        super().OnInteract(oHero)
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)



class CMagicBoxNPC(CBoxNPC):
    pass

