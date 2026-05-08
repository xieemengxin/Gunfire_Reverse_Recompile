# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_chatinfo.pyc
# RelativePath: clientlogic/cl_chatinfo.pyc
# Source Generated with Decompyle++
# File: cl_chatinfo.pyc (Python 3.6)

from cl_only import RplFormat, SendAlert
import re
import cl_notify
import cllib.lib_flag
g_ChatTable = { }

def GS2CPlayerShowText(oGame, iChat, pid, iType = 0, *Args):
    ShowText(oGame, iChat, pid, iType, *Args)


def GS2CShowText(oGame, iChat, iType = 0, *Args):
    ShowText(oGame, iChat, 0, iType, *Args)


def ShowText(oGame, iChat, pid, iType, *Args):
    sMsg = GetChat(iChat, *Args)
    iFuncType = g_ChatTable[iChat][0]
    if iFuncType == 1:
        cl_notify.GS2CCenterTopFloatMsg(oGame, iType, sMsg, pid)
    elif iFuncType == 2:
        cl_notify.GS2CLeftMidScrollMsg(oGame, iType, sMsg, pid)
    elif iFuncType == 3:
        cl_notify.GS2CCenterBtmFloatMsg(oGame, iType, sMsg, pid)
    elif iFuncType == 4:
        cl_notify.GS2CCenterMidScrollMsg(oGame, sMsg, pid)


def GetChat(iChat, *Args):
    sChat = ''
    if iChat in g_ChatTable:
        sChat = g_ChatTable[iChat][2]
        for i in range(0, len(Args), 2):
            sChat = sChat.replace(Args[i], Args[i + 1])
        
    if cllib.lib_flag.g_IsInternalRun:
        if re.search('\\$[A-Za-z]', sChat):
            ErrChat(iChat, 1)
        elif not sChat:
            ErrChat(iChat, 2)
    return sChat


def ErrChat(iChat, iType):
    sChatInfo = ChatInfo(iChat)
    if iType == 1:
        SendAlert('exception', 'chat error 1: %s not trans' % sChatInfo)
    elif iType == 2:
        SendAlert('exception', 'chat error 2: %s not exist' % sChatInfo)


def ChatInfo(iChat):
    return RplFormat('D战场对白_%d', iChat)

