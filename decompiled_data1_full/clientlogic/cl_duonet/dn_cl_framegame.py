# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_framegame.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_framegame.pyc
# Source Generated with Decompyle++
# File: dn_cl_framegame.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_framegame

def DN_GS2CFightLoop(iFrame, dPlayer):
    cl_duonet.netfunc.PacketPrepare(47)
    cl_duonet.netfunc.PacketVarInt(iFrame)
    cl_duonet.netfunc.SendToPlayers(dPlayer)

