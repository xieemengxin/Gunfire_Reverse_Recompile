# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/warcondition.pyc
# RelativePath: clientlogic/cl_warmgr/warcondition.pyc
# Source Generated with Decompyle++
# File: warcondition.pyc (Python 3.6)

from cl_commondefines import KILLHISTORY_COMPATIBY

def WarCheckHistoryKillBoss(oWarMgr, iLevel, dMonsterSID, iCount):
    for iHero in oWarMgr.GetRoomHero(iCalAI = 0):
        oHero = oWarMgr.m_Game.GetObject(iHero)
        dMonster = oHero.Query('Monster', { })
        if 'KillBoss' not in dMonster:
            continue
        iKill = 0
        for iMonsterSID in dMonsterSID:
            iKill += dMonster['KillBoss'].get(iMonsterSID, 0)
        
        iKill += dMonster['KillBoss'].get(KILLHISTORY_COMPATIBY, 0)
        if iKill >= iCount:
            return True
    
    return False


def WarCheckForceLevel(oWarMgr, iLevel, dMonsterSID, iCount):
    bKillBoss = WarCheckHistoryKillBoss(oWarMgr, iLevel, dMonsterSID, iCount)
    if not bKillBoss:
        return False
    for iHero in oWarMgr.GetRoomHero(iCalAI = 0):
        oHero = oWarMgr.m_Game.GetObject(iHero)
        lstLevel = oHero.Query('LevelRecord', [])
        if iLevel not in lstLevel:
            return True
    
    return False


def WarCheckSpecifcMode(oWarMgr, iLevel, iMode):
    if iMode in oWarMgr.m_ModeType:
        return True
    return False


def WarCheckCycle(oWarMgr, iLevel, iCycle):
    return oWarMgr.m_Cycle == iCycle


def WarCheckNewVerLayer(oWarMgr, iLevel):
    return oWarMgr.GetNewVerLayer()

