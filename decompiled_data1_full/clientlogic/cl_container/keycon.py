# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/keycon.pyc
# RelativePath: clientlogic/cl_container/keycon.pyc
# Source Generated with Decompyle++
# File: keycon.pyc (Python 3.6)

from cl_item.load import GetAllKeyType
from cl_only import SendAlert, log_file
import cl_duonet.dn_cl_item_cnet

def GS2CRefreshKey(oGame, oHero, dKey):
    lstKey = []
    for iKeySID, iNum in dKey.items():
        lstKey.append((iKeySID, iNum))
    
    netData = {
        'lstKey': lstKey,
        'iWarrior': oHero.m_ID,
        'pid': oHero.m_PlayerID,
        'oGame': oGame }
    cl_duonet.dn_cl_item_cnet.DN_GS2CRefreshKey(netData)


class CKeyContainer(object):
    
    def __init__(self, oGame, iOwner):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_Keys = { }

    
    def Release(self):
        self.m_Game = None

    
    def AddKey(self, dKey, sReason):
        log_file('warkey', '%d %d add %s %s' % (self.m_Game.m_ID, self.m_Owner, dKey, sReason))
        dAllKey = GetAllKeyType()
        for iKey, iNum in dKey.items():
            if iKey not in dAllKey:
                SendAlert('err', '尝试添加不存在钥匙%d %s' % (iKey, sReason))
                continue
            if iNum <= 0:
                SendAlert('err', '尝试添加非正数钥匙%d %s' % (iKey, sReason))
                continue
            iMax = dAllKey[iKey]
            iCurNum = self.m_Keys[iKey] if iKey in self.m_Keys else 0
            self.m_Keys[iKey] = min(iCurNum + iNum, iMax)
        
        self.Refresh()

    
    def CostKey(self, dKey, sReason):
        log_file('warkey', '%d %d cost %s %s' % (self.m_Game.m_ID, self.m_Owner, dKey, sReason))
        for iKey, iNum in dKey.items():
            self.m_Keys[iKey] -= iNum
        
        self.Refresh()

    
    def ValidCostKey(self, dKey):
        for iKey, iNum in dKey.items():
            if iKey not in self.m_Keys:
                return 0
            if not iNum <= 0:
                if self.m_Keys[iKey] < iNum:
                    return 0
        
        return 1

    
    def Refresh(self, oHero = None):
        oGame = self.m_Game
        if oHero:
            GS2CRefreshKey(oGame, oHero, self.m_Keys)
        else:
            for iHero in oGame.m_WarMgr.GetAllHero():
                oHero = oGame.GetObject(iHero)
                GS2CRefreshKey(oGame, oHero, self.m_Keys)
            


