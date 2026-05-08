# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_only.pyc
# RelativePath: clientlogic/cl_only.pyc
# Source Generated with Decompyle++
# File: cl_only.pyc (Python 3.6)

from _functools import partial
from cllib.lib_only import *
from cl_rplstr import CRplStr
from types import MappingProxyType
import re
import traceback
import weakref
import marshal
import cllib.lib_flag
import math
GAME_FRAME = 25
GAME_FRAME_TIME = 100 // GAME_FRAME
GAME_FRAME_SECOND = 1 / GAME_FRAME
GAME_GRAVITY = -18
GAME_FRAME_INF = 360000000
HALF_GAME_FRAME = GAME_FRAME // 2
CELL_SPACESIZE = 100
CELL_REC = 0.01

def Time2Frame(iTime):
    return iTime // GAME_FRAME_TIME


def Second2Frame(iSecond):
    return int(iSecond * GAME_FRAME)


def Frame2Time(iFrame):
    return iFrame * GAME_FRAME_TIME


def PerSecond2PerFrame(iValue):
    return iValue // GAME_FRAME


def PosNet2Float(pos):
    return (pos[0] * CELL_REC, pos[1] * CELL_REC, pos[2] * CELL_REC)


def PosFloat2Net(pos):
    return (int(pos[0] * CELL_SPACESIZE), int(pos[1] * CELL_SPACESIZE), int(pos[2] * CELL_SPACESIZE))


def Float2Net(val):
    return int(val * CELL_SPACESIZE)


def Net2Float(val):
    return val * CELL_REC


def OutputPos(vector):
    return '(%s)' % ', '.join([ '%.3f' % v for v in vector ])

PY_FLAG_NONE = 0
PY_FLAG_DIED = 1
PY_FLAG_DYING = 2
PY_FLAG_DEAD = PY_FLAG_DIED | PY_FLAG_DYING
PY_FLAG_IGNORESCENEEVT = 4
PY_FLAG_NOWALKCEHCK = 8
PY_FLAG_EXCLUDEHATE = 16
PY_FLAG_EXCLUDEMONSTERHATE = 32
PY_FLAG_EXCLUDEPRIORITYHATE = 64
PY_FLAG_SERVANTTARGET = PY_FLAG_DIED | PY_FLAG_EXCLUDEHATE
PY_FLAG_SERVANTCHOOSETARGET = PY_FLAG_SERVANTTARGET | PY_FLAG_EXCLUDEPRIORITYHATE
PY_FLAG_MONSTERTARGET = PY_FLAG_DEAD | PY_FLAG_EXCLUDEMONSTERHATE
CTRL_FLAG_SIM = 1
CTRL_FLAG_QUERY = 2
CTRL_FLAG_CCTFT = 4
CTRL_FLAG_FOR_DEAD = CTRL_FLAG_SIM | CTRL_FLAG_QUERY | CTRL_FLAG_CCTFT
CTRL_FLAG_FOR_ALL = CTRL_FLAG_SIM | CTRL_FLAG_QUERY | CTRL_FLAG_CCTFT
CTRL_FLAG_HERO_DYING = CTRL_FLAG_QUERY | CTRL_FLAG_CCTFT
LEAVE_NAVMESH = 0
ENTER_NAVMESH = 1
PX_COMBINE_MODE_AVERAGE = 0
PX_COMBINE_MODE_MIN = 1
PX_COMBINE_MODE_MULTIPLY = 2
PX_COMBINE_MODE_MAX = 3
PLATFORM_ANDROID = 1
PLATFORM_IOS = 2
PLATFORM_WIN = 3
PLATFORM_XBOX = 4
PLATFORM_PSX = 5
DEAD_FLAG_DIED = 1
DEAD_FLAG_DYING = 2
DEAD_FLAG_REAL = 3
RE_PATTERN = re.compile('^[a-z](\\d|[a-z_])*(/[a-z](\\d|[a-z_])*)*$')

class Functor(partial):
    
    def __getattr__(self, sAttr):
        if sAttr == 'm_Type':
            return None
        raise AttributeError("'Functor object has no attribute '%s'" % sAttr)

    
    def Type(self):
        return self.m_Type

    
    def SetType(self, a):
        self.m_Type = a

    
    def __str__(self):
        return 'functor%s' % self.func

    
    def __repr__(self):
        return 'functor%s' % self.func


if cllib.lib_flag.g_IsStableRun:
    
    def DeepCopy(data):
        sData = marshal.dumps(data)
        return marshal.loads(sData)

else:
    
    def DeepCopy(data):
        sData = marshal.dumps(TransReadOnly(data))
        return marshal.loads(sData)


def RplFormat(sFormat, *Args):
    return sFormat % Args


def ChooseKey(oGame, dInfo, iTotal = 0):
    if iTotal == 0:
        for v in dInfo.values():
            iTotal += v
        
    i = oGame.Random(iTotal)
    t = 0
    for k, v in dInfo.items():
        t += v
        if i < t:
            return k
    


def ChooseRange(oGame, iMin, iMax):
    if iMax == iMin:
        return iMax
    iTmax = max(iMin, iMax)
    iTmin = min(iMin, iMax)
    iOff = oGame.Random((iTmax - iTmin) + 1)
    return iOff + iMin


def ChooseMulKeys(oGame, dSource, iCount):
    dInfo = { v: k for k, v in dSource.items() if v > 0 }
    iTotal = 0
    for v in dInfo.values():
        iTotal += v
    
    if iCount >= len(dInfo):
        return list(dInfo.keys())
    lstKey = []
    for _ in range(iCount):
        i = oGame.Random(iTotal)
        t = 0
        for k, v in dInfo.items():
            t += v
            if i < t:
                lstKey.append(k)
                break
        
        iTotal -= dInfo[k]
        dInfo.pop(k)
    
    return lstKey


def ChooseTotalKey(oGame, dInfo, iTotal, iMax):
    i = oGame.Random(iTotal)
    t = 0
    for k, v in dInfo.items():
        t += v
        if i < t and v <= iMax:
            return k
    


def GetRandomCard(oGame, iSize, iMax, get_off = None):
    lstRet = []
    for i in range(iMax):
        lstRet.append(i)
    
    if get_off:
        for i in get_off:
            if i in lstRet:
                lstRet.remove(i)
                iMax -= 1
        
    for i in range(iMax):
        if i >= iSize:
            break
        iPos = i + oGame.Random(iMax - i)
        if i != iPos:
            tmp = lstRet[i]
            lstRet[i] = lstRet[iPos]
            lstRet[iPos] = tmp
    
    return lstRet[:iSize]


def ShufferList(oGame, lstInfo, iNum = 0):
    result = []
    iSize = len(lstInfo)
    if iNum == 0:
        iNum = iSize
    for iPos in GetRandomCard(oGame, iNum, iSize):
        result.append(lstInfo[iPos])
    
    return result


def RandomFloat2Int(oGame, fNum):
    iBase = int(fNum)
    iLimit = int((fNum - iBase) * 100)
    if iLimit <= 0:
        return iBase
    iRand = oGame.Random(100)
    if iRand > iLimit:
        return iBase
    return iBase + 1


def ReduceDict(Dict):
    lstRet = []
    for key, value in Dict.items():
        if not isinstance(value, list) and not isinstance(value, tuple) or value not in lstRet:
            lstRet.append(value)
            continue
        for v in value:
            if v not in lstRet:
                lstRet.append(v)
        
    
    return lstRet


def CeilDivide(iNum1, iNum2):
    iResult = iNum1 // iNum2
    if iNum1 % iNum2:
        iResult += 1
    return iResult


def RoundDivide(iNum1, iNum2):
    iResult = iNum1 // iNum2
    if iNum1 % iNum2 >= iNum2 // 2:
        iResult += 1
    return iResult

if cllib.lib_flag.g_IsAuthorityRun:
    
    class CUniqueDict(dict):
        
        def __setitem__(self, k, v):
            if k in self:
                raise Exception('unique dict duplicate')
            dict.__setitem__(self, k, v)


else:
    CUniqueDict = dict

def RaiseError(sMsg):
    log_file('err', '%s' % sMsg)
    TraceWarning()


def TraceWarning():
    iLen = 5
    lstTrace = traceback.extract_stack()
    if len(lstTrace) < iLen:
        iLen = len(lstTrace)
    if iLen < 1:
        log_file('err', 'TraceWarning Err')
        InstantWarning('TraceWarning Err')
        return None
    lstTrace = lstTrace[-iLen:]
    log_file('err', 'TraceWarning Begin:')
    for iPos in range(iLen):
        sInfo = lstTrace[iPos]
        sWarning = str(sInfo[:3])
        log_file('err', '%s' % sWarning)
        if iPos < iLen - 1:
            PrintWarning(sWarning)
            continue
        InstantWarning(sWarning)
    
    log_file('err', 'TraceWarning End')


def WeakProxy(obj):
    if isinstance(obj, weakref.ProxyType):
        return obj
    return weakref.proxy(obj)


def WeakProxyBool(obj):
    
    try:
        return bool(obj)
    except ReferenceError:
        return False



def ReadOnly(obj):
    if cllib.lib_flag.g_IsStableRun:
        return obj
    if isinstance(obj, dict):
        dDict = { ReadOnly(v): k for k, v in obj.items() }
        return MappingProxyType(dDict)
    if isinstance(obj, list):
        return tuple(obj)
    if isinstance(obj, set):
        return frozenset(obj)
    return obj


def TransReadOnly(obj):
    if isinstance(obj, MappingProxyType):
        return { TransReadOnly(v): k for k, v in obj.items() }
    if isinstance(obj, tuple):
        return [ TransReadOnly(v) for v in obj ]
    if isinstance(obj, frozenset):
        return { TransReadOnly(v) for v in obj }
    return obj

