# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betree/producttools.pyc
# RelativePath: clientlogic/cl_betree/producttools.pyc
# Source Generated with Decompyle++
# File: producttools.pyc (Python 3.6)

from cl_only import Functor
from cli_player import GetPlayer
import cllib.lib_flag
import cl_framegame
import cl_notify
import cl_behavior

class CProductFunc(cl_behavior.GetProductFuncClass()):
    
    def Functor(self, *args):
        return Functor(*args)

    
    def Print(self, *args):
        print(args)

    
    def CanHotReload(self):
        return True

    
    def GetProjectTreePath(self):
        return 'cl_betreedata'

    
    def GetProjectScriptTreePath(self):
        return 'script/clientlogic/cl_betreedata'

    
    def GetParserAgentDir(self):
        return ('script/clientlogic/cl_betree', 'script/jqdescParser')

    
    def QueryPlayerGameServer(self, iPlayer):
        oPlayer = GetPlayer(iPlayer)
        iRet = 1
        iServer = 0
        if not oPlayer:
            iRet = 2
            return (iRet, iServer)
        if not oPlayer.m_RoomKey:
            iRet = 3
            return (iRet, iServer)
        (_, iServer) = oPlayer.m_RoomKey
        return (iRet, iServer)

    
    def RpcCallFunc(self, iServer, sFunc, resfunc, *args):
        import rpc
        if resfunc:
            func = rpc.RPC_Functor(resfunc, None)
        else:
            func = None
        rpc.CallFunc(iServer, sFunc, args, func)

    
    def GetGameSpace(self, pid):
        who = GetPlayer(pid)
        if not who:
            return None
        oGame = cl_framegame.GetGame(who.m_GameID)
        if not oGame:
            return None
        oGameSpace = oGame.m_Betree
        return oGameSpace

    
    def Notify(self, pid, sMsg):
        if cllib.lib_flag.g_IsLogicLayer:
            who = GetPlayer(pid)
            if not who:
                return None
            oGame = cl_framegame.GetGame(who.m_GameID)
            cl_notify.GS2CDebugMsg(oGame, pid, sMsg)
        else:
            import notify
            notify.GS2CMessage(pid, sMsg)
            notify.GS2CGMNotify(pid, sMsg)

    
    def IsDaoBiaoServer(self):
        if cllib.lib_flag.g_IsLogicLayer:
            return None
        import mkparser
        import ctrlcenter
        if ctrlcenter.GetServerNum() in (4430101,):
            return True
        if mkparser.GetEditor().IsDaoBiaoServer():
            pass
        return ctrlcenter.GetServerGroup() != 'mobile'

    
    def IsInternalNetServer(self):
        return cllib.lib_flag.g_IsInternalRun

    
    def CheckPythonSyntax(self, sCode):
        
        try:
            compile(sCode, '', 'exec')
            return ''
        except SyntaxError as err:
            
            try:
                return err.text
            finally:
                err = None
                del err



    
    def CheckGMIdentity(self, oLink):
        import gamegm.net
        gamegm.net.CheckGMIdentity(oLink)
        if hasattr(oLink, 'm_DevelopName'):
            return True
        return False

    
    def UpdateAll(self, who, modname):
        import gamegm.c_admin
        import pubgmcenter
        pubgmcenter.SetAdmin(who.m_ID)
        gamegm.c_admin.updateall(who, modname)
        pubgmcenter.SetAdmin(0)


