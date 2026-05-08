# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/tools.pyc
# RelativePath: clientlogic/cl_behavior/tools.pyc
# Source Generated with Decompyle++
# File: tools.pyc (Python 3.6)


class CProductFunc(object):
    
    def Functor(self, *args):
        pass

    
    def Print(self, *args):
        print(*args)

    
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



    
    def IsInternalNetSever(self):
        return False

    
    def GetProjectTreePath(self):
        return ''

    
    def CanHotReload(self):
        return False

    
    def GetParserAgentDir(self):
        return ('', '')

    
    def QueryPlayerGameServer(self, iPlayer):
        (iRet, iServer) = (1, 4430301)
        return (iRet, iServer)

    
    def RpcCallFunc(self, iServer, sFunc, resfunc, *args):
        pass

    
    def GetProjectScriptTreePath(self):
        return ''

    
    def GetGameSpace(self, pid):
        pass

    
    def Notify(self, pid, sMsg):
        pass

    
    def IsDaoBiaoServer(self):
        return False

    
    def CheckGMIdentity(self, oLink):
        return False

    
    def UpdateAll(self, who, modname):
        pass


if 'g_Tools' not in globals():
    g_Tools = None

def SetProductFunc(obj):
    global g_Tools
    g_Tools = obj


def GetTools():
    return g_Tools

