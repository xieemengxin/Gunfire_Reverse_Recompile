# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_npc/transfernpc.pyc
# RelativePath: clientlogic/cl_npc/transfernpc.pyc
# Source Generated with Decompyle++
# File: transfernpc.pyc (Python 3.6)

from cl_commondefines import INTERACT_STATUS_PEND, INTERACT_STATUS_DONE, TRANSFER_DIRTO_NULL
from . import mobject

class CTransferNPC(mobject.CNPC):
    
    def __init__(self, *args):
        super(CTransferNPC, self).__init__(*args)
        self.m_Ready = { }
        self.m_TransferDir = TRANSFER_DIRTO_NULL

    
    def OnInteract(self, oHero):
        pass

    
    def SetHeroInteractStatus(self, pid, iNotify = 1):
        dPlayerStat = self.m_PlayerInteractStatus
        if dPlayerStat[pid] == INTERACT_STATUS_PEND:
            dPlayerStat[pid] = INTERACT_STATUS_DONE
        elif dPlayerStat[pid] == INTERACT_STATUS_DONE:
            dPlayerStat[pid] = INTERACT_STATUS_PEND
        if iNotify:
            self.NotifyInteractInfo(pid)


