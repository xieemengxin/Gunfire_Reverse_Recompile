# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_load.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_load.pyc
# Source Generated with Decompyle++
# File: lib_load.pyc (Python 3.6)

from . import lib_json
import cllib.lib_flag
if 'g_ResourcePath' not in globals():
    g_ResourcePath = ''
if cllib.lib_flag.g_IsLogicLayer:
    if 'g_TestResourcePath' not in globals():
        g_TestResourcePath = False
    import os
    import C_logic
    import C_frscene
    
    def SetResourcePathTest(sPath):
        global g_ResourcePath, g_TestResourcePath
        g_ResourcePath = sPath
        g_TestResourcePath = True
        C_frscene.SetMapResPath(sPath)

    
    def ClearResourceTest():
        C_logic.ClearResourceCache('map')

    
    def SetResourcePath(sPath):
        global g_ResourcePath
        g_ResourcePath = sPath
        C_frscene.SetMapResPath(sPath)
        dResPackage = {
            'residx.txt': 'data0' }
        C_logic.SetResourcePackage(dResPackage)
        dResourceMap = LoadResource('', 'residx', 'json')
        for k, v in dResourceMap.items():
            fileK = k.replace('/', '.')
            if 'json' in fileK:
                fileK = fileK.replace('json', 'txt')
            dResPackage[fileK] = v
        
        C_logic.SetResourcePackage(dResPackage)

    
    def LoadResource(sResource, sFile, sSuffix):
        if not g_TestResourcePath and sSuffix == 'json':
            sRealFile = '%s.txt' % (sFile,)
        else:
            sRealFile = '%s.%s' % (sFile, sSuffix)
        
        try:
            sLoadRes = C_frscene.ReadFile(sRealFile, sResource)
            if sSuffix == 'json':
                sLoadRes = lib_json.loads(sLoadRes)
        except:
            import cllib.lib_only
            cllib.lib_only.PythonError()
            raise Exception('resourcefail %s %s' % (sResource, sRealFile))

        return sLoadRes

else:
    import os
    import C_debug
    import C_frscene
    
    def SetResourcePath(sPath):
        global g_ResourcePath
        g_ResourcePath = sPath
        C_frscene.SetMapResPath(sPath)

    
    def LoadResource0(sResource, sFile, sSuffix):
        
        try:
            if not sResource:
                sRes = '%s/%s.%s' % (g_ResourcePath, sFile, sSuffix)
            else:
                sRes = '%s/%s/%s.%s' % (g_ResourcePath, sResource, sFile, sSuffix)
            sPath = os.path.abspath(sRes)
            with open(sPath) as ofile:
                dData = lib_json.loads(ofile.read())
        except:
            C_debug.PythonError()
            dData = { }

        return dData

    
    def LoadResource(sResource, sFile, sSuffix):
        sRealFile = '%s.%s' % (sFile, sSuffix)
        
        try:
            sLoadRes = C_frscene.ReadFile(sRealFile, sResource)
            if sSuffix == 'json':
                sLoadRes = lib_json.loads(sLoadRes)
        except:
            C_debug.PythonError()
            raise Exception('resourcefail %s %s' % (sResource, sRealFile))

        return sLoadRes

