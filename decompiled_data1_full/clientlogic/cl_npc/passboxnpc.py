# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/passboxnpc.pyc
# RelativePath: clientlogic/cl_npc/passboxnpc.pyc
# Source Generated with Decompyle++
# File: passboxnpc.pyc (Python 3.6)

from cl_commondefines import INTERACT_TYPE_FORBID, INTERACT_RULE_LEVELGOAL, INTERACT_TYPE_ALLOW
from . import magicbox

class CLevelGoalBoxNpc(magicbox.CBoxNPC):
    
    def __init__(self, *args):
        super(CLevelGoalBoxNpc, self).__init__(*args)
        self.AddExtraInteractRule(INTERACT_RULE_LEVELGOAL, { })
        self.SetInitInteract(INTERACT_TYPE_FORBID)

    
    def OnInteract(self, oHero):
        lstPlayer = self.m_Game.m_WarMgr.GetAllPlayer()
        for pid in lstPlayer:
            self.SetHeroInteractStatus(pid, 0)
            self.BoxModelOpen(pid)
        
        self.SetPlayerInteractType(INTERACT_TYPE_FORBID, lstPlayer)



class CRoomChallengeNpc(magicbox.CBoxNPC):
    
    def __init__(self, *args):
        super(CRoomChallengeNpc, self).__init__(*args)
        self.SetInitInteract(INTERACT_TYPE_FORBID)

    
    def SetPlayerInteractType(self, iInteractType, lstPlayer):
        if iInteractType != INTERACT_TYPE_ALLOW:
            return None
        if not self.m_ActionFunc:
            return None
        func = self.m_ActionFunc
        self.m_ActionFunc = None
        oWarMgr = self.m_Game.m_WarMgr
        for pid in lstPlayer:
            oHero = oWarMgr.GetHeroByPlayer(pid)
            if not oHero:
                continue
            func(self, oHero)
        


