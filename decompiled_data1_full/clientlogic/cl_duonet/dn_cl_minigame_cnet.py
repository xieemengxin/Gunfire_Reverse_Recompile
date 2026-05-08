# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/dn_cl_minigame_cnet.pyc
# RelativePath: clientlogic/cl_duonet/dn_cl_minigame_cnet.pyc
# Source Generated with Decompyle++
# File: dn_cl_minigame_cnet.pyc (Python 3.6)

import cl_duonet.netfunc
import cl_minigame.cnet

def DN_C2GSMiniGameOP(who):
    iMiniGame = cl_duonet.netfunc.UnpackInt(4)
    iSubOp = cl_duonet.netfunc.UnpackInt(1)
    iAnswer = cl_duonet.netfunc.UnpackInt(2)
    cl_minigame.cnet.C2GSMiniGameOP(who, iMiniGame, iSubOp, iAnswer)

