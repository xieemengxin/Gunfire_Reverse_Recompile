# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasonplay/season8/__init__.pyc
# RelativePath: clientlogic/cl_seasonplay/season8/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_platformdata import ImportdMod, IsRunPCData, GetS8GemItem, GetS8ThirdItem
if 'g_S8GemItemCls' not in globals():
    g_S8GemItemCls = { }
    g_S8ThirdItemCls = { }

def GetS8GemItemDataCls(iSID):
    if iSID not in GetS8GemItem():
        return None
    if iSID not in g_S8GemItemCls:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 's8gemitem', 'gem%4d' % iSID)
        if not mod:
            return None
        g_S8GemItemCls[iSID] = mod.CS8GemItem
    return g_S8GemItemCls[iSID]


def GetS8ThirdItemCls(iSID):
    if iSID not in GetS8ThirdItem():
        return None
    if iSID not in g_S8ThirdItemCls:
        if IsRunPCData():
            sPlatform = 'pc'
        else:
            sPlatform = 'mobile'
        mod = ImportdMod(sPlatform, 's8thirditem', 'td%4d' % iSID)
        if not mod:
            return None
        g_S8ThirdItemCls[iSID] = mod.CS8ThirdItem
    return g_S8ThirdItemCls[iSID]


def CreateS8GemItem(oGame, iSID, iQuality, dItemData):
    clsItem = GetS8GemItemDataCls(iSID)
    if not clsItem:
        return None
    dItemData['SID'] = iSID
    dItemData['QL'] = iQuality
    return clsItem.Create(oGame, dItemData, iPointID = 0, dTmp = { })


def CreateS8ThirdItem(oGame, iSID, iQuality, dItemData):
    clsItem = GetS8ThirdItemCls(iSID)
    if not clsItem:
        return None
    dItemData['SID'] = iSID
    dItemData['QL'] = iQuality
    return clsItem.Create(oGame, dItemData, iPointID = 0, dTmp = { })

