# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cli_init.pyc
# RelativePath: clientlogic/clinterface/cli_init.pyc
# Source Generated with Decompyle++
# File: cli_init.pyc (Python 3.6)

import C_frgame
import C_customnet
import cllib.lib_flag

def ServerInit():
    import cl_only
    import cl_interface
    
    try:
        C_frgame.InitGameCtrl(cl_only.GAME_FRAME_SECOND)
        print('old gamectrl')
    except:
        C_frgame.InitGameCtrl(cl_only.GAME_FRAME_SECOND, 8)

    cl_interface.SetResourcePath('map')
    CommonInit()
    ServerInit1()


def ServerInit1():
    import C_frscene
    import C_game
    import server
    import cl_wardata.levelconf.load as mapload
    import ctrlcenter
    if server.IsFightServer() and not C_game.GetOSPlatForm() and not ctrlcenter.IsServerGroup('devcloud'):
        lstAllMap = mapload.GetAllMapList()
        ret = C_frscene.LoadHotSceneRes(lstAllMap)
        print('scene res loaded [%d %d]' % (ret, len(lstAllMap)))


def ClientInit():
    import C_logic
    import site
    import sys
    import re
    import cl_only
    for path in sys.path:
        if ('data2' in path or cllib.lib_flag.g_IsMobile) and cllib.lib_flag.g_IsInternalRun:
            sCond = '(\\S+mobilegame)\\/(data2.fls)'
            m = re.search(sCond, path)
            if m:
                sGmPath = '%s/gamegm.fls' % m.group(1)
                sys.path.append(sGmPath)
        site.addsitedir(path + '/site-packages')
    
    ClientInit1()
    if not hasattr(C_logic, 'GameInit'):
        print('outdated dll found, please update it.')
        return -1
    
    try:
        C_frgame.InitGameCtrl(cl_only.GAME_FRAME_SECOND)
        print('old gamectrl')
    except:
        C_frgame.InitGameCtrl(cl_only.GAME_FRAME_SECOND, 1)

    
    try:
        tFlag = ('encrypt', 'doublehash')
        sFlag = '-'.join(filter((lambda x: x in sys.version), tFlag))
        print('pyversion: ' + sFlag if sFlag else 'null')
    except:
        'pyversion: ' + sFlag
        print
        print('pyversion: unknown')

    
    try:
        tBuildInfo = C_logic.GetBuildInfo()
        print('logic build: %s %s' % tBuildInfo)
    except:
        'pyversion: ' + sFlag
        print
        print('logic build: unknown')

    
    try:
        copyright = C_logic.GetCopyright()
        scopyright = cl_only.GetCopyright()
        if copyright == scopyright:
            print('copyright: %s *' % (copyright,))
        else:
            print('copyright: %s %s' % (copyright, scopyright))
    except:
        'pyversion: ' + sFlag
        print
        print('copyright: unknown')

    if cllib.lib_flag.g_IsInternalRun:
        print('flags: ', dict(filter((lambda x: x[0].startswith('g_')), cllib.lib_flag.__dict__.items())))
    print('g_UseNewRectangle', cllib.lib_flag.g_UseNewRectangle)
    ClientInit2()
    CommonInit()
    return 0


def ClientInit1():
    import C_logic
    import sys
    
    class CStdOut(object):
        
        def __init__(self):
            self.m_MsgList = []

        
        def write(self, msg):
            if msg != '\n':
                self.m_MsgList.append(msg)
            else:
                self.flush()

        
        def flush(self):
            C_logic.Message(1, ''.join(self.m_MsgList))
            self.m_MsgList.clear()


    
    class CStdErr(object):
        
        def __init__(self):
            self.m_MsgList = []

        
        def write(self, msg):
            if msg != '\n':
                self.m_MsgList.append(msg)
            else:
                self.flush()

        
        def flush(self):
            C_logic.Message(2, ''.join(self.m_MsgList))
            self.m_MsgList.clear()


    sys.stdout = CStdOut()
    sys.stderr = CStdErr()

PYLGCB_LCCMD = 0
PYLGCB_ENTRY = 2

def ClientInit2():
    import C_logic
    import clclient.clc_cmd
    import clclient.clc_entry
    import clclient.clc_pyerror
    clclient.clc_cmd.SetLogicFunction()
    clclient.clc_cmd.SetFightFunction()
    C_logic.InitPyCallInfo(PYLGCB_LCCMD, clclient.clc_cmd.OnLogicCommand)
    C_logic.InitPyCallInfo(PYLGCB_ENTRY, clclient.clc_entry.OnLogin)
    C_logic.SetErrorCallback(clclient.clc_pyerror.ExtExceptionCallBack)


def ClientRelease():
    import cl_interface
    cl_interface.ReleaseAllGame()


def CommonInit():
    import cl_pxlayer
    import cl_betree
    import cl_putdata
    C_frgame.SetGameTimeoutLimit(1, 50)
    C_frgame.SetGameTimeoutLimit(3, 4)
    C_frgame.SetGameTimeoutLimit(4, 100)
    C_frgame.SetGameTimeoutLimit(5, 50)
    C_frgame.SetGameTimeoutLimit(6, 50)
    C_frgame.SetGameTimeoutLimit(7, 10)
    C_frgame.SetGameTimeoutLimit(8, 50)
    C_frgame.SetGameTimeoutLimit(9, 50)
    C_frgame.SetGameTimeoutLimit(10, 50)
    
    try:
        C_frgame.SetGameTimeoutLimit(11, 100)
    except:
        print('SetGameTimeoutLimit 11 Failed')

    
    try:
        C_frgame.SetGameTimeoutLimit(12, 50)
        C_frgame.SetGameTimeoutLimit(13, 50)
    except:
        print('SetGameTimeoutLimit 12/13 Failed')

    C_customnet.SetFloatPacketPrecision(1, 100)
    C_customnet.SetFloatPacketPrecision(2, 100)
    C_customnet.SetFloatPacketPrecision(3, 100000)
    cl_pxlayer.InitPxLayer()
    cl_betree.MyInit()
    cl_putdata.Init()
    InitCXXErrorAlert()


def InitCXXErrorAlert():
    import re
    dReplace = {
        re.compile('PAERROR: pascene .* event .* not exist'): {
            'PAERROR: pascene': '场景:',
            'event': '事件区域:',
            'not exist': '不存在' },
        re.compile('PAERROR: pxsceneres .* area .* not exist'): {
            'PAERROR: pxsceneres': '资源:',
            'area': '区域:',
            'not exist': '不存在' } }
    dIgnore = { }
    
    def CXXErrorAlert(msg):
        import cl_only
        import cllib.lib_flag
        for r in dIgnore.keys():
            if r.search(msg):
                return None
        
        if not cllib.lib_flag.g_IsLogicLayer:
            for r, dMap in dReplace.items():
                if r.search(msg):
                    for sSrc, sRpl in dMap.items():
                        msg = msg.replace(sSrc, sRpl)
                    
            
        cl_only.SendAlert('cxxerr', msg)

    C_frgame.SetCXXErrorCallback(CXXErrorAlert)

