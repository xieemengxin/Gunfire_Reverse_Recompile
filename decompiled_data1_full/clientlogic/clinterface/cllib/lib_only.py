# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_only.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_only.pyc
# Source Generated with Decompyle++
# File: lib_only.pyc (Python 3.6)

import time
import weakref
import cllib.lib_flag
import sys
import linecache
import tokenize
import io
import types
MAX_USER_ID = 268435455
PRODUCT_MIN_CSUMMON_ID = 268436455
PRODUCT_MIN_NPC_ID = 268437455
CHANNEL_STEAM = 1
CHANNEL_ZHANMENG = 2
CHANNEL_WEGAME = 3

def ShortParam(oVal, bRoot = True):
    if type(oVal) == dict:
        if bRoot:
            dVal = { }
            for k, v in oVal.items():
                dVal[k] = ShortParam(v, False)
            
            return dVal
        sVal = str(oVal)
        iLen = len(sVal)
        if iLen > 120:
            return sVal[:50] + f'''...略({iLen})'''
    if type(oVal) == list:
        lstVal = []
        for v in oVal:
            lstVal.append(ShortParam(v, False))
        
        return lstVal
    if type(oVal) == tuple:
        lstVal = []
        for v in oVal:
            lstVal.append(ShortParam(v, False))
        
        return tuple(lstVal)
    return oVal


def GetFrameText(lstFrame, bLineInfo = False):
    
    def GetCodeLine(frame, lineno):
        sFileName = frame.f_code.co_filename
        linecache.checkcache(sFileName)
        line = linecache.getline(sFileName, lineno, frame.f_globals)
        return line.strip()

    lstLine = []
    for frame, lineno in lstFrame:
        lstText = []
        if bLineInfo:
            line = "File '%s', line %s, in '%s'" % (frame.f_code.co_filename, lineno, frame.f_code.co_name)
            lstText.append(line)
        line = GetCodeLine(frame, lineno)
        if line:
            lstText.append(' ' + line)
            dParams = { }
            dLocals = frame.f_locals
            dGlobals = frame.f_globals
            oVal = None
            bIsAttr = False
            sLastKey = ''
            for token in tokenize.tokenize(io.BytesIO(line.encode('utf-8')).readline):
                if token.type == tokenize.NAME:
                    sKey = token.string
                    if sKey in dLocals:
                        oVal = dLocals[sKey]
                    elif sKey in dGlobals:
                        oVal = dGlobals[sKey]
                    elif bIsAttr and hasattr(oVal, sKey):
                        oVal = getattr(oVal, sKey)
                        sKey = f'''{sLastKey}.{sKey}'''
                    
                    sLastKey = sKey
                    if type(oVal) == types.ModuleType:
                        continue
                    if type(oVal) in (types.FunctionType, types.MethodType) and oVal.__name__ == token.string:
                        continue
                    if sKey in dParams:
                        del dParams[sKey]
                    dParams[sKey] = oVal
                if token.type == tokenize.OP and token.string == '.':
                    bIsAttr = True
                    continue
                bIsAttr = False
            
            iLastIdx = len(dParams) - 1
            idx = 0
            for sKey, oVal in dParams.items():
                sSymbol = '└' if idx == iLastIdx else '├'
                line = f'''  {sSymbol} {sKey}: {ShortParam(oVal)}'''
                lstText.append(line)
                idx += 1
            
        if lstText:
            lstLine.append(lstText)
    
    return lstLine


def TraceArg(*args):
    lstFrame = []
    frame = sys._getframe().f_back
    while True:
        if frame:
            lstFrame.insert(0, (frame, frame.f_lineno))
            frame = frame.f_back
            continue
    lstLine = GetFrameText(lstFrame, bLineInfo = True)
    print('----------------')
    for lstText in lstLine:
        print('\n'.join(lstText))
    

if cllib.lib_flag.g_IsLogicLayer:
    from C_logic import PythonError, DoCommand
    from C_logic import GetLogicFrameTime as GetFrameTime
    import C_logic
    MIN_NPC_ID = MAX_USER_ID + 1000
    
    def log_file(filename, sText):
        C_logic.OutputWithTime(filename, sText)

    
    def log_file_debug(sLogName, sLogText):
        log_file('debug/%s' % sLogName, sLogText)

    
    def log_file_long(filename, sText):
        C_logic.OutputWithTime(filename, sText)

    
    def PrintWarning(sText):
        print(sText)

    
    def InstantWarning(txt):
        print(txt)

    
    def IsNpcObjectID(pid):
        return pid > MAX_USER_ID

    
    def GetOSPlatForm():
        if C_logic.GetPlatform() == 3:
            return 1
        return 0

    
    def GetServerIndex():
        return 0

    
    def CheckNetSize(sContent, sReason = ''):
        pass

    
    def GetGameFlag():
        return cllib.lib_flag.g_GameGate

    
    def GetServerGroup():
        return ''

    
    def RunMobileData():
        if cllib.lib_flag.g_IsMobileRun:
            return True
        return False

    
    def GetCopyright():
        (a, b) = (188, 222)
        c = a << 8 | b
        copyright = [
            58820,
            51732,
            50063,
            49666,
            48247,
            52886,
            56221,
            56990,
            56279]
        return ''.join([ chr(x ^ c) for x in copyright ])

    
    def CopyList(srclist):
        return srclist[:]

    
    def CopyTuple(srctuple):
        return srctuple[:]

    
    def CopyDict(srcdict):
        dNewDict = { }
        dNewDict.update(srcdict)
        return dNewDict

    
    class LFunctor(object):
        
        def __init__(self, func, *args, **kwargs):
            self._func = func.__func__
            self._object = weakref.ref(func.__self__)
            self._args = args
            self._kwargs = kwargs

        
        def __call__(self, *args, **kwargs):
            obj = self._object()
            if obj is None:
                raise Exception('LFunctor: dead weakref!')
            self._kwargs.update(kwargs)
            return self._func(obj, *self._args + args, **self._kwargs)

        
        def object(self):
            return self._object()


    
    class WFunctor(object):
        
        def __init__(self, func, *args, **kwargs):
            self._func = func.__func__
            self._object = weakref.ref(func.__self__)
            self._args = args
            self._kwargs = kwargs

        
        def __call__(self, *args, **kwargs):
            obj = self._object()
            if obj is None:
                return None
            self._kwargs.update(kwargs)
            return self._func(obj, *self._args + args, **self._kwargs)

        
        def object(self):
            return self._object()


    
    class Functor:
        
        def __init__(self, fn, *args):
            self._fn = fn
            self._args = args
            self.m_Type = ''

        
        def __call__(self, *args):
            return self._fn(*self._args + args)

        
        def Type(self):
            return self.m_Type

        
        def SetType(self, a):
            self.m_Type = a


    
    def GetTraceText(*args):
        import traceback
        txtlist = []
        txtlist.append('----------------')
        stack = traceback.extract_stack()
        for filename, lineno, name, line in stack[:-1]:
            txt = " File '%s', line %s, in '%s'" % (filename, lineno, name)
            txtlist.append(txt)
        
        if args:
            txt = '其它信息:'
            for s in args:
                txt = '%s%s,' % (txt, s)
            
            txt = txt[:-1]
            txtlist.append(txt)
        return txtlist

    
    def TraceMsg(*args):
        txtlist = GetTraceText(*args)
        for txt in txtlist:
            print(txt)
        

    
    def TraceLog(sLogName, *args):
        txtlist = GetTraceText(*args)
        for txt in txtlist:
            log_file('err', txt)
        

    
    def GetIP(iIP):
        sIP = ''
        for i in range(4):
            if len(sIP):
                sIP += '.'
            sIP += '%d' % iIP % 256
            iIP //= 256
        
        return sIP

    
    def GetIntIP(sIP):
        iIP = 0
        sList = sIP.split('.')
        for i in range(4):
            iIP += int(sList[i]) << i * 8
        
        if iIP > 2147483647:
            iIP = iIP - 0x100000000
        return iIP

    
    def TimeStr(ti = 0, sFormat = '%Y-%m-%d %H:%M:%S'):
        if ti:
            t = time.localtime(ti)
        else:
            t = time.localtime()
        return time.strftime(sFormat, t)

    
    def SendAlert(sMode, sMsg):
        import cl_object.logging
        cl_object.logging.LogicwarningLog.Info('%s %s' % (sMode, sMsg))
        if cllib.lib_flag.g_IsAuthorityRun:
            from clclient.clc_pyerror import g_PyError
            
            try:
                g_PyError.m_TmpMsg = sMsg
                d = { }
                d[sMsg] += 1
            except:
                PythonError()


    
    def TimeString(ti):
        if ti < 60:
            return '%d秒'.format(ti)
        iMin = ti // 60
        iHour = iMin // 60
        iDay = iHour // 24
        if iDay and iHour % 24 and iMin % 60:
            return '%d天%d小时%d分钟'.format(iDay, iHour % 24, iMin % 60)
        if iDay and iHour % 24:
            return '%d天%d小时'.format(iDay, iHour % 24)
        if iDay and iMin % 60:
            return '%d天%d分钟'.format(iDay, iMin % 60)
        if iHour % 24 and iMin % 60:
            return '%d小时%d分钟'.format(iHour % 24, iMin % 60)
        if iDay:
            return '%d天'.format(iDay)
        if iHour % 24:
            return '%d小时'.format(iHour % 24)
        if iMin % 60:
            return '%d分钟'.format(iMin % 60)

    
    def SetGlobalManager(sFlag, oManager, bLimitReplace = True):
        oldobj = g_GlobalManagerDict.get(sFlag, None)
        if oldobj and g_GManagerLimit[sFlag]:
            InstantWarning('限制替换的全局管理实例被替换:%s %s' % (oldobj, oManager))
        g_GlobalManagerDict[sFlag] = oManager
        g_GManagerLimit[sFlag] = bLimitReplace
        if oldobj and hasattr(oManager, 'OnReplaced'):
            oManager.OnReplaced(oldobj)

    
    def DelGlobalManager(sFlag):
        if sFlag in g_GlobalManagerDict:
            del g_GlobalManagerDict[sFlag]
        if sFlag in g_GManagerLimit:
            del g_GManagerLimit[sFlag]

    
    def GetGlobalManager(sFlag):
        if sFlag in g_GlobalManagerDict:
            return g_GlobalManagerDict[sFlag]

    if 'g_GlobalManagerDict' not in globals():
        g_GlobalManagerDict = { }
        g_GManagerLimit = { }
    
    def GetCommandMode():
        import clclient.clc_cmd
        return clclient.clc_cmd

    
    def GetCommandKey():
        return 'set_command'

else:
    from only import *
    from C_debug import PythonError
    from ctrlcenter import GetServerGroup, RunMobileData
    
    def GetCommandMode():
        import netcommand
        return netcommand

    
    def GetCommandKey():
        return 'set_commond'

