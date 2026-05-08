# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_packetsender.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_packetsender.pyc
# Source Generated with Decompyle++
# File: clc_packetsender.pyc (Python 3.6)

from cl_object.logging import PacketLog
from cli_player import GetPlayer
import marshal
import time
import cllib.lib_server

class CPacketSender(object):
    m_SendIntervalTime = 1
    m_CheckResendTime = 1000
    m_LimitSize = 300
    
    def __init__(self, pid):
        self.m_Owner = pid
        self.m_Packet = { }
        self.m_PacketID = 0
        self.m_CurID = 0
        self.m_AckID = 0
        self.m_LastSendTime = 0
        self.m_Sending = False
        self.m_Key = ''

    
    def Init(self, sKey):
        self.m_Key = sKey
        oOwner = GetPlayer(self.m_Owner)
        oOwner.Call_Out(self.CheckResend, self.m_CheckResendTime, 'CheckReSend')

    
    def NewPacketID(self):
        if self.m_PacketID > 0xFFFFFFFF:
            self.m_PacketID = 0
        self.m_PacketID += 1
        return self.m_PacketID

    
    def CheckResend(self):
        oOwner = GetPlayer(self.m_Owner)
        oOwner.Remove_Call_Out('CheckReSend')
        oOwner.Call_Out(self.CheckResend, self.m_CheckResendTime, 'CheckReSend')
        if self.m_LastSendTime and self.m_LastSendTime + self.m_CheckResendTime < int(time.time() * 100) and self.m_AckID < self.m_CurID:
            self.TryResend()

    
    def TryResend(self):
        if self.m_Sending:
            oOwner = GetPlayer(self.m_Owner)
            oOwner.Remove_Call_Out('SendPacket')
            self.m_Sending = False
        PacketLog.Info('%d %d %d resend start' % (self.m_Owner, self.m_CurID, self.m_AckID))
        self.m_CurID = self.m_AckID
        self.TrySend()

    
    def AddPacket(self, dPacket):
        if not self.m_Sending:
            oOwner = GetPlayer(self.m_Owner)
            oOwner.Call_Out(self.TrySend, self.m_SendIntervalTime, 'TrySend')
        dAdd = dict(dPacket)
        iPacketID = self.NewPacketID()
        dAdd['Data'] = marshal.dumps(dPacket['Data'])
        dAdd['PacketID'] = iPacketID
        self.m_Packet[iPacketID] = dAdd
        PacketLog.Info('%d add %d %s' % (self.m_Owner, iPacketID, dPacket))

    
    def TrySend(self):
        if not self.m_Key:
            return None
        if self.m_CurID >= self.m_PacketID or self.m_Sending:
            return None
        self.m_Sending = True
        self.m_CurID += 1
        dPacket = self.m_Packet[self.m_CurID]
        dPacket['Send'] = dPacket['Data']
        PacketLog.Info('%s %s %s send start' % (self.m_Owner, self.m_Key, self.m_CurID))
        dPacket['StartFunc'](self.m_Key, self.m_CurID)
        self.SendPacket()

    
    def SendPacket(self):
        if not self.m_Sending:
            return None
        dPacket = self.m_Packet[self.m_CurID]
        oOwner = GetPlayer(self.m_Owner)
        oOwner.Remove_Call_Out('SendPacket%d' % self.m_Owner)
        sData = dPacket['Send']
        sSend = sData[:self.m_LimitSize]
        sLeft = sData[self.m_LimitSize:]
        pid = dPacket['pid']
        iLGS = dPacket['LGS']
        sKey = self.m_Key
        iPacketID = dPacket['PacketID']
        cllib.lib_server.L2SPacketContent(iLGS, pid, sKey, dPacket['PacketID'], sSend)
        if not sLeft:
            cllib.lib_server.L2SPacketEnd(iLGS, pid, sKey, iPacketID)
            PacketLog.Info('%s %s %s send end' % (self.m_Owner, sKey, iPacketID))
            self.m_Sending = False
            self.m_LastSendTime = int(time.time() * 100)
            oOwner.Call_Out(self.TrySend, self.m_SendIntervalTime, 'TrySend%d' % self.m_Owner)
        else:
            dPacket['Send'] = sLeft
            oOwner.Call_Out(self.SendPacket, self.m_SendIntervalTime, 'SendPacket%d' % self.m_Owner)

    
    def ResPacketEnd(self, sKey, iPacketID):
        PacketLog.Info('%d %s res packet end' % (iPacketID, sKey))
        if self.m_AckID + 1 == iPacketID:
            self.m_AckID = iPacketID


