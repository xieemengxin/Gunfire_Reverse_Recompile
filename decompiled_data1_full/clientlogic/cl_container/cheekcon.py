# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/cheekcon.pyc
# RelativePath: clientlogic/cl_container/cheekcon.pyc
# Source Generated with Decompyle++
# File: cheekcon.pyc (Python 3.6)

from cl_commondefines import PROGRESSUNLOCK_CHEEK
from cl_object.logging import CheekLog
import cl_notify

class CCheekContainer(object):
    
    def __init__(self, oGame, iOwner, iPlayerID):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayerID
        self.m_Unlock = []

    
    def AddCheek(self, iCheek, sReason):
        if iCheek in self.m_Unlock:
            return None
        CheekLog.Info(f'''{self.m_Game.m_ID} {self.m_PlayerID} addcheek {iCheek} {sReason}''')
        self.m_Unlock.append(iCheek)
        cl_notify.SendUnlockNotify(self.m_Game, self.m_PlayerID, 0, iCheek, PROGRESSUNLOCK_CHEEK)

    
    def GetAddCheek(self):
        return self.m_Unlock


