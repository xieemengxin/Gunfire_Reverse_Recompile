# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_minigame/cnet.pyc
# RelativePath: clientlogic/cl_minigame/cnet.pyc
# Source Generated with Decompyle++
# File: cnet.pyc (Python 3.6)

from cl_object.logging import WarrewardLog

def C2GSMiniGameOP(who, iMiniGame, iSubOp, iAnswer):
    oGame = who.m_Game
    WarrewardLog.Debug(f'''{oGame.m_ID} c2gsminigameop {iMiniGame} {iSubOp} {iAnswer}''')
    oMiniGame = oGame.m_MiniGameMgr.GetMiniGame(iMiniGame)
    if not oMiniGame:
        return None
    oMiniGame.C2GSGameOP(who, iSubOp, iAnswer)

