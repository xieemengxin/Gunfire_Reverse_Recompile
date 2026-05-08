# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/debug/net.pyc
# RelativePath: clientlogic/cl_behavior/debug/net.pyc
# Source Generated with Decompyle++
# File: net.pyc (Python 3.6)

from __future__ import absolute_import
from C_net import *
from pubnet import *
from only import Functor, log_file, PacketAddSL, GetOnlinePlayer, UnpackString, UnpackBinaryString, UnpackInt, PythonError, PacketSend, PacketAddI, PacketAddI, PacketPrepare, SendAlert
import os
import cllib.lib_flag
import tools.checkcode
from . import linkmanager
from .. import GetTools
from myutil.alertmerge import SendPersonIMMsg

def Log(sLog):
    log_file('debug/behavior', sLog)


def GetRpcModule():
    sModule = __name__.split('.')[0]
    sModule += '.debug'
    return sModule


def PacketPrepareEditor(iSub):
    PacketPrepare(GS2C_GAME_PUBLIC)
    PacketAddI(GS2C_SUB_EDITOR_BEHAVIOR, 1)
    PacketAddI(iSub, 1)


def GS2CLinkConnect(uid, iRet):
    PacketPrepareEditor(1)
    PacketAddI(iRet, 1)
    PacketSend(uid)


def GS2CSendBTVerion(uid, dVer):
    PacketPrepareEditor(2)
    PacketAddI(len(dVer), 1)
    for sName, iVer in dVer.items():
        PacketAddSL(sName, 1)
        PacketAddI(iVer, 2)
    
    PacketSend(uid)


def R_NodeResult(resfunc, pid, sAgentName, sRootPath, iNodeID, iAction, iResult):
    oLink = GetLink(pid)
    if not oLink:
        return None
    GS2CNodeResult(oLink.m_ID, sAgentName, sRootPath, iNodeID, iAction, iResult)


def R_BreakPointResult(resfunc, pid, sRootPath, iNodeID, iAction, iHit):
    oLink = GetLink(pid)
    if not oLink:
        return None
    PacketPrepareEditor(6)
    PacketAddSL(sRootPath, 1)
    PacketAddI(iNodeID, 2)
    PacketAddI(iAction, 1)
    PacketAddI(iHit, 1)
    PacketSend(oLink.m_ID)


def GS2CNodeResult(uid, sAgentName, sRootPath, iNodeID, iAction, iResult):
    PacketPrepareEditor(3)
    PacketAddSL(sAgentName, 1)
    PacketAddSL(sRootPath, 1)
    PacketAddI(iNodeID, 2)
    PacketAddI(iAction, 1)
    PacketAddI(iResult, 1)
    PacketSend(uid)


def R_SendGameEnd(resfunc, pid):
    Log('%d sendgameend' % pid)
    oLink = GetLink(pid)
    if not oLink:
        return None
    GS2CSendGameEnd(oLink.m_ID)


def GS2CSendGameEnd(uid):
    PacketPrepareEditor(4)
    PacketSend(uid)


def R_NotifyMsg(resfunc, pid, sMsg):
    GetTools().Notify(pid, sMsg)


def RES_LinkConnect(pid, iRet):
    Log('%d linkconnect %d' % (pid, iRet))
    oLink = GetLink(pid)
    if not oLink:
        return None
    GS2CLinkConnect(oLink.m_ID, iRet)


def RES_SendBTVersion(pid, dVer):
    Log('%d sendbtversion %s' % (pid, dVer))
    oLink = GetLink(pid)
    if not oLink:
        return None
    GS2CSendBTVerion(oLink.m_ID, dVer)


def C2GSLinkConnect(oLink):
    oTools = GetTools()
    if not oTools.IsDaoBiaoServer():
        GS2CLinkConnect(oLink.m_ID, 4)
        return None
    pid = UnpackInt(4)
    if cllib.lib_flag.g_IsMobile:
        import rpc
        oTools.m_ResCB = { }
        oLink.m_EditorPlayer = pid
        oMgr = linkmanager.GetBehaviorLinkMgr()
        oMgr.AddLink(oLink)
        for iServer in (4700105, 4700106):
            resfunc = rpc.RPC_Functor(Res_GetPlayerInfo, T_GetPlayerInfo, pid, iServer)
            rpc.CallFunc(iServer, 'serviceallot.allotmgr.R_GetPlayerInfo', [
                pid], resfunc)
        
        return None
    (iRet, iServer) = oTools.QueryPlayerGameServer(pid)
    oLink.m_EditorPlayer = pid
    if iRet == 1:
        oMgr = linkmanager.GetBehaviorLinkMgr()
        oMgr.AddLink(oLink)
        cbfunc = Functor(RES_LinkConnect, pid)
        oTools.RpcCallFunc(iServer, GetRpcModule() + '.R_SetDebug', cbfunc, pid)
    else:
        GS2CLinkConnect(oLink.m_ID, iRet)


def C2GSLinkHeartBeat(oLink):
    if not GetTools().IsDaoBiaoServer():
        GS2CLinkConnect(oLink.m_ID, 4)
        return None
    oMgr = linkmanager.GetBehaviorLinkMgr()
    oMgr.AddHeartBeat(oLink.m_ID)


def C2GSGetBTVersion(oLink):
    oTools = GetTools()
    if not oTools.IsDaoBiaoServer():
        GS2CLinkConnect(oLink.m_ID, 4)
        return None
    lstNames = []
    iNum = UnpackInt(1)
    for _ in range(iNum):
        iLen = UnpackInt(1)
        sName = UnpackString(iLen)
        lstNames.append(sName)
    
    pid = oLink.m_EditorPlayer
    if cllib.lib_flag.g_IsMobile:
        (iRet, iServer) = QueryGameServer(oLink)
    else:
        (iRet, iServer) = oTools.QueryPlayerGameServer(pid)
    if iRet == 1:
        Log('%d getbtversion %s' % (pid, lstNames))
        cbfunc = Functor(RES_SendBTVersion, pid)
        oTools.RpcCallFunc(iServer, GetRpcModule() + '.R_GetBTVersion', cbfunc, pid, lstNames)


def C2GSUpdateBT(oLink):
    if not GetTools().IsDaoBiaoServer():
        GS2CLinkConnect(oLink.m_ID, 4)
        return None
    iLen = UnpackInt(1)
    sBTName = UnpackString(iLen)
    oLink.m_EditorCallBack = Functor(UpdateBT, oLink, sBTName)


def UpdateBT(oLink, sBTName, sCode):
    oTools = GetTools()
    pid = oLink.m_EditorPlayer
    if sBTName.find(' ') != -1:
        oTools.Notify(pid, '%s 行为树命名有空格，无法更新' % sBTName)
        return None
    if cllib.lib_flag.g_IsMobile:
        (iRet, iServer) = QueryGameServer(oLink)
    else:
        (iRet, iServer) = oTools.QueryPlayerGameServer(pid)
    if iRet == 1:
        Log('%d updatebt %s' % (pid, sBTName))
        oTools.RpcCallFunc(iServer, GetRpcModule() + '.R_UpdateTree', None, pid, sBTName, sCode)


def R_SaveBT(resfunc, pid, sIM, tCommitInfo, sRelativePath, sCode):
    oTools = GetTools()
    if not oTools.IsDaoBiaoServer():
        return None
    Log('%d savebt %s' % (pid, sRelativePath))
    dData = {
        'pid': pid,
        'sub_path': '',
        'relative_path': sRelativePath,
        'code': sCode,
        'retry': 3,
        'IM': sIM,
        'CommitInfo': tCommitInfo }
    tools.checkcode.UpdateAndExec('trunk', Functor(TryCommit, dData, True, 'parser'))


def TryCommit(dData, bUpdate, sReason, iSvnVer, lstSvnLog):
    import tools.commitcode
    pid = dData['pid']
    sRelativePath = dData['relative_path']
    sCode = dData['code']
    Log('%d commitbt %s %s' % (pid, sRelativePath, sReason))
    oTools = GetTools()
    sFileName = sRelativePath.replace('.', '/')
    filename = '%s/%s.py' % (oTools.GetProjectScriptTreePath(), sFileName)
    filepath = os.path.abspath(filename)
    fobj = open(filepath, 'w+', encoding = __import__('C_game').GetDefaultEncoding(), newline = '\n')
    fobj.write(sCode)
    fobj.close()
    if bUpdate and not UpdateBt(dData, iSvnVer, lstSvnLog):
        sIM = dData['IM']
        if sIM:
            SendPersonIMMsg(sIM, '%s行为树导出发生错误，无法提交' % sRelativePath)
        return None
    (sDescription, sTaskID, sName) = dData['CommitInfo']
    sDesc = f'''parserbehavior#r{sName}_#{sDescription}_%{sTaskID}'''
    tools.commitcode.CommitAndExec(dData['sub_path'], Functor(CommitDone, dData), sDesc)


def UpdateBt(dData, iSvnVer, lstSvnLog):
    import gamegm.mynewremote
    oTools = GetTools()
    pid = dData['pid']
    who = gamegm.mynewremote.CreateMaster(pid, {
        'Auth': 99 })
    sRelativePath = dData['relative_path']
    sUpdatePath = '%s.%s' % (oTools.GetProjectTreePath(), sRelativePath)
    
    try:
        modname = sUpdatePath.replace('/', '.')
        oTools.UpdateAll(who, modname)
    except:
        PythonError()
        return False

    return True


def CommitDone(dData, bError):
    sRelativePath = dData['relative_path']
    sIM = dData['IM']
    if bError:
        if dData['retry'] <= 0:
            sText = '%s行为树多次提交SVN失败，请联系程序处理' % sRelativePath
            SendAlert('behavior', sText)
            tools.checkcode.UpdateAndExec('trunk', Functor(UpdateBt, dData))
        else:
            dData['retry'] -= 1
            sText = '%s行为树提交SVN失败, 正在尝试重新提交' % sRelativePath
            tools.checkcode.UpdateAndExec('trunk', Functor(TryCommit, dData, False, 'retry'))
    else:
        Log('%s commit done' % dData['relative_path'])
        sText = '%s导出【成功】 请提交【btjson】' % sRelativePath
    if sIM:
        SendPersonIMMsg(sIM, sText)


def C2GSTextOP(oLink):
    iSub = UnpackInt(1)
    if iSub == 1:
        oLink.m_TextBuffer = b''
    elif iSub == 2 or hasattr(oLink, 'm_TextBuffer'):
        iLen = UnpackInt(1)
        sStr = UnpackBinaryString(iLen)
        oLink.m_TextBuffer += sStr
    elif iSub == 3:
        if not hasattr(oLink, 'm_TextBuffer'):
            return None
        sText = oLink.m_TextBuffer.decode(__import__('C_game').GetDefaultEncoding())
        del oLink.m_TextBuffer
        if not oLink.m_EditorCallBack:
            return None
        func = oLink.m_EditorCallBack
        func(sText)
        oLink.m_EditorCallBack = None


def C2GSSetBreakPoint(oLink):
    pass


def C2GSNextStep(oLink):
    pass


def C2GSSaveBT(oLink):
    oTools = GetTools()
    if not oTools.IsDaoBiaoServer():
        GS2CLinkConnect(oLink.m_ID, 4)
        return None
    lstNames = []
    iNum = UnpackInt(1)
    for _ in range(iNum):
        iLen = UnpackInt(1)
        sBTName = UnpackString(iLen)
        lstNames.append(sBTName)
    
    sDescription = UnpackString(UnpackInt(1))
    sTaskID = UnpackString(UnpackInt(1))
    pid = oLink.m_EditorPlayer
    if cllib.lib_flag.g_IsMobile:
        (iRet, iServer) = QueryGameServer(oLink)
    else:
        (iRet, iServer) = oTools.QueryPlayerGameServer(pid)
    if iRet == 1:
        oTools.RpcCallFunc(iServer, GetRpcModule() + '.R_SaveTree', None, pid, lstNames, sDescription, sTaskID)


def Res_GetPlayerInfo(pid, iCbServer, iFightServer, iGameID):
    oLink = GetLink(pid)
    if not oLink:
        return None
    oTools = GetTools()
    oTools.m_ResCB[iCbServer] = 0
    if iFightServer and iGameID:
        oLink.m_FightData = {
            'Fight': iFightServer,
            'GameID': iGameID }
        oTools.m_ResCB[iCbServer] = 1
        cbfunc = Functor(RES_LinkConnect, pid)
        oTools.RpcCallFunc(iFightServer, GetRpcModule() + '.R_SetDebug', cbfunc, pid)
    elif not CheckConnect(oTools.m_ResCB):
        GS2CLinkConnect(oLink.m_ID, 3)


def T_GetPlayerInfo(pid, iCbServer):
    oTools = GetTools()
    oTools.m_ResCB[iCbServer] = 0
    if not CheckConnect(oTools.m_ResCB):
        GS2CLinkConnect(pid, 3)


def CheckConnect(dResInfo):
    if not dResInfo.get(4700105, 0):
        pass
    if not dResInfo.get(4700106, 0) and len(dResInfo) == 2:
        return 0
    return 1


def QueryGameServer(oLink):
    iFightServer = oLink.m_FightData.get('Fight', 0)
    iGameID = oLink.m_FightData.get('GameID', 0)
    (iRet, iServer) = (0, 0)
    if iFightServer and iGameID:
        iRet = 1
        iServer = iFightServer
    return (iRet, iServer)

g_Cmd = {
    1: C2GSLinkConnect,
    2: C2GSLinkHeartBeat,
    3: C2GSGetBTVersion,
    4: C2GSUpdateBT,
    5: C2GSSaveBT,
    6: C2GSTextOP,
    7: C2GSSetBreakPoint }

def C2GSBehaviorCmd(oLink):
    iSub = UnpackInt(1)
    if iSub not in g_Cmd:
        return None
    func = g_Cmd[iSub]
    func(oLink)


def GetLink(pid):
    oMgr = linkmanager.GetBehaviorLinkMgr()
    oLink = oMgr.GetLink(pid)
    if not oLink and pid in oMgr.m_DebugPlayer:
        oMgr.m_DebugPlayer.remove(pid)
        GetTools().Notify(pid, '行为树编辑器连接已断开,请重连')
        if cllib.lib_flag.g_IsMobile:
            (iRet, iServer) = QueryGameServer(oLink)
        else:
            (iRet, iServer) = GetTools().QueryPlayerGameServer(pid)
        if iRet == 1:
            GetTools().RpcCallFunc(iServer, GetRpcModule() + '.R_ReleaseDebug', None, pid)
    return oLink

