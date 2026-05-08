# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_duonet/__init__.pyc
# RelativePath: clientlogic/cl_duonet/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

__version__ = '1.0.0'
__all__ = [
    'Receive',
    'GetProcessedProtoSet']
from importlib import import_module
from . import duonetdata
from . import netfunc
if 'g_NetModule' not in globals():
    g_NetModule = { }
    g_RcvFunc = { }
SUBPROTO_LONG = 1

def Receive(cmd, linkname, obj):
    protoNoList = UnpackMultiSub(cmd, linkname)
    c2sdict = duonetdata.g_C2FS
    (moduleName, oneProto, subProtoDict) = c2sdict[protoNoList]
    subProtoNo = None
    if not oneProto:
        subProtoNo = netfunc.UnpackInt(SUBPROTO_LONG)
    if subProtoNo not in subProtoDict:
        return None
    subProtoName = subProtoDict[subProtoNo]
    tKey = (moduleName, subProtoName)
    if tKey not in g_RcvFunc:
        if moduleName not in g_NetModule:
            g_NetModule[moduleName] = import_module('cl_duonet.%s' % moduleName.replace('.', '_'))
        g_RcvFunc[tKey] = getattr(g_NetModule[moduleName], subProtoName)
    g_RcvFunc[tKey](obj)


def UnpackMultiSub(cmd, linkname):
    subNo = [
        cmd]
    multisubdict = duonetdata.g_MultiSubC2FS
    subDict = multisubdict[cmd]
    while True:
        if not subDict:
            break
        subNo.append(netfunc.UnpackInt(SUBPROTO_LONG))
        subDict = subDict[subNo[-1]]
    return tuple(subNo)


def GetProcessedProtoSet(linkname):
    return getattr(duonetdata, 'g_ProcessedProtoSet%s' % linkname)

