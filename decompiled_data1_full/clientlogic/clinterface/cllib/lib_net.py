# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_net.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_net.pyc
# Source Generated with Decompyle++
# File: lib_net.pyc (Python 3.6)

import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    from C_logic import PacketPrepare
    from C_logic import PacketAddBinaryS
    from C_logic import PacketAddI
    from C_logic import PacketAddLong
    from C_logic import PacketAddS
    from C_logic import PacketAddSL
    from C_logic import GetPacketData
    from C_logic import SetPacketData
    from C_logic import GetCPacketData
    from C_logic import SetPacketDataForUnpack
    from C_logic import UnpackBinaryString
    from C_logic import UnpackInt
    from C_logic import UnpackLong
    from C_logic import UnpackString
    from C_logic import LocalSend
    from C_logic import PacketSend
    from C_logic import SendToPlayers
    from C_logic import WorldBroadcast
    from C_customnet import UnpackVarInt
    from C_customnet import PacketVarInt
    from C_customnet import UnpackVarLong
    from C_customnet import PacketVarLong
    from C_customnet import UnpackPosInt
    from C_customnet import PacketPosInt
    from C_customnet import UnpackPosFloat
    from C_customnet import PacketPosFloat
    from C_customnet import PacketFloat
    from C_customnet import UnpackFloat
    
    def ClearCmdFlag():
        pass

else:
    from C_net import PacketPrepare
    from C_net import PacketAddBinaryS
    from C_net import PacketAddI
    from C_net import PacketAddL
    from C_net import PacketAddS
    from C_net import PacketAddSL
    from C_net import GetPacketData
    from C_net import SetPacketData
    from C_net import GetCPacketData
    from C_net import SetPacketDataForUnpack
    from C_net import UnpackBinaryString
    from C_net import UnpackInt
    from C_net import UnpackLong
    from C_net import UnpackString
    from C_net import PacketSend
    from C_net import SendToPlayers
    from C_net import ClearCmdFlag
    from C_object import WorldBroadcast
    from C_customnet import UnpackVarInt
    from C_customnet import PacketVarInt
    from C_customnet import UnpackVarLong
    from C_customnet import PacketVarLong
    from C_customnet import UnpackPosInt
    from C_customnet import PacketPosInt
    from C_customnet import UnpackPosFloat
    from C_customnet import PacketPosFloat
    from C_customnet import PacketFloat
    from C_customnet import UnpackFloat
    PacketAddLong = PacketAddL
    
    def LocalSend():
        raise Exception('err call localsend')

