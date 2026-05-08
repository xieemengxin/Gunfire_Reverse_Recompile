# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_flag.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_flag.pyc
# Source Generated with Decompyle++
# File: lib_flag.pyc (Python 3.6)

g_IsLogicLayer = 0
g_IsTradition = 0
g_IsStandalone = 0
g_IsMobile = 0
g_IsConsole = 0
g_IsStandaloneClient = 0
g_IsPCRunFight = 0
g_IsMobileRun = 0
g_IsInternalRun = 0
g_IsAuthorityRun = 0
g_IsStableRun = 0
g_GameGate = ''
g_PCChannel = 0
g_MobileChannel = 0
g_MobileEnvironment = -1
g_IsMobileShenHeRun = 0
g_IsPrivyRun = 0
g_OpenAsyncLoad = 0
g_UseCBehavior = 0
g_AutoDelMapRes = 0
g_AutoDelBetree = 0
g_UseSkillID = 1
g_OpenAggrAlert = 1
g_OpenWarFrameCheck = 0
g_UseAnima = 1
g_OpenCompressLog = 0
g_OpenSeason = 0
g_UseNewRectangle = 1
g_UseFlyNav = 1

try:
    import C_logic
    g_IsLogicLayer = 1
except:
    pass

if g_IsLogicLayer:
    import C_logic
    
    def GetRunMaskShift(iShift, iBit):
        return C_logic.GetRunMask() >> iShift & (1 << iBit) - 1

    g_IsInternalRun = GetRunMaskShift(0, 1)
    g_IsTradition = int(GetRunMaskShift(2, 3) == 1)
    g_IsStandalone = int(GetRunMaskShift(2, 3) == 2)
    g_IsMobile = int(GetRunMaskShift(2, 3) == 3)
    g_IsConsole = int(GetRunMaskShift(2, 3) == 4)
    if g_IsStandalone or g_IsConsole:
        g_IsStandaloneClient = 1
    iIsExtRunFlag = GetRunMaskShift(5, 1)
    iIsConsoleTest = 0
    if g_IsTradition:
        g_IsMobileRun = iIsExtRunFlag
    elif g_IsMobile:
        g_IsMobileRun = 1
    elif g_IsConsole:
        iIsConsoleTest = iIsExtRunFlag
    del iIsExtRunFlag
    iIsChinaArea = GetRunMaskShift(6, 1) & 1
    if g_IsTradition:
        g_GameGate = 'm2m1'
    elif g_IsStandalone:
        g_GameGate = 'p2m1' if iIsChinaArea else 'p3m1us'
    elif g_IsMobile:
        g_GameGate = 'm2m1m' if iIsChinaArea else 'm3m1mus'
    elif g_IsConsole:
        g_GameGate = 'console'
    else:
        g_GameGate = 'unknown'
    del iIsChinaArea
    g_PCChannel = GetRunMaskShift(7, 2)
    g_MobileChannel = GetRunMaskShift(7, 2)
    if g_IsMobile:
        g_MobileEnvironment = int(GetRunMaskShift(10, 2))
    g_IsStableRun = GetRunMaskShift(11, 1)
    g_OpenAsyncLoad = 0
    g_UseCBehavior = 0
    g_AutoDelMapRes = 1 if g_IsMobileRun else 0
    g_AutoDelBetree = 1 if g_IsMobileRun else 0
    g_OpenAggrAlert = 0
    g_OpenCompressLog = 1 if g_IsStandalone else 0
    g_OpenSeason = 1 if g_IsTradition or g_IsStandalone or g_IsMobile else 0
    if g_GameGate == 'm2m1m' and g_MobileChannel == 1:
        g_UseNewRectangle = 0
    
    try:
        iDevices = C_logic.GetDevices()
    except:
        'p2m1'
        iDevices = 0

    if g_IsTradition:
        pass
    if g_IsConsole:
        pass
    devicesInfo = {
        0: (1,),
        1: (g_IsMobileRun, g_IsMobile),
        2: (g_IsTradition, g_IsStandalone, iIsConsoleTest),
        3: (g_IsConsole,) }
    if iDevices not in devicesInfo or not any(devicesInfo[iDevices]):
        raise Exception('devices[%d] logic not match.' % (iDevices,))
    del iIsConsoleTest
    del iDevices
    del devicesInfo
else:
    import only
    import server
    import ctrlcenter
    g_GameGate = only.GetGameFlag()
    g_IsTradition = int(g_GameGate in ('m2m1',))
    g_IsStandalone = int(g_GameGate in ('p2m1', 'p3m1us'))
    g_IsMobile = int(g_GameGate in ('m2m1m', 'm3m1mus'))
    g_IsPCRunFight = int(g_GameGate in ('p2m1', 'p3m1us'))
    g_IsConsole = 0
    g_IsMobileRun = ctrlcenter.RunMobileData()
    g_IsInternalRun = server.IsInternalNetServer()
    g_IsAuthorityRun = server.IsAuthorityServer()
    g_IsPrivyRun = server.IsPrivyDevelop()
    g_IsStableRun = server.IsStableServer()
    g_PCChannel = 0
    g_MobileChannel = 0
    if g_IsMobileRun:
        g_OpenAggrAlert = 0
    g_OpenAsyncLoad = 1
    g_AutoDelMapRes = 0
    g_AutoDelBetree = 0
    g_OpenWarFrameCheck = 1
    if g_IsTradition or g_IsStandalone or g_IsMobile:
        g_OpenSeason = 1
