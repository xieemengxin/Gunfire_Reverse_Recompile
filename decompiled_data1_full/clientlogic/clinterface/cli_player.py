# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cli_player.pyc
# RelativePath: clientlogic/clinterface/cli_player.pyc
# Source Generated with Decompyle++
# File: cli_player.pyc (Python 3.6)

import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    import C_logic
    
    def GetPlayer(pid, iGameID = 0):
        return C_logic.GetLObject(pid)

else:
    import C_object
    
    def GetPlayer(pid, iGameID = 0):
        oPlayer = C_object.GetObject(pid)
        if not oPlayer:
            return None
        if iGameID and oPlayer.m_GameID != iGameID:
            return None
        return oPlayer

