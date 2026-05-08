# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_pyextend.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_pyextend.pyc
# Source Generated with Decompyle++
# File: clc_pyextend.pyc (Python 3.6)

from cl_object.logging import PyextendLog
from cl_only import PythonError
import os
import sys
import types
import marshal
import base64
import pkgutil

class CExtendPackageMgr(object):
    
    def __init__(self):
        self.m_dPackData = { }

    
    def AcceptData(self, sPath, sCode, iFinish):
        PyextendLog.Info('accept data: %s' % sPath)
        sPath = self.AdjustPath(sPath)
        self.SaveInfo(sPath, sCode)
        self.DynamicCreate(sPath, iFinish)

    
    def SaveInfo(self, sPath, sCode):
        self.m_dPackData[sPath] = sCode

    
    def AdjustPath(self, sPath):
        if sPath.endswith('/__init__.py'):
            sPath = sPath[:-12]
        return sPath

    
    def IsModuleExists(self, sPath):
        for _, sModuleName, _ in pkgutil.iter_modules():
            if sModuleName == sPath:
                return True
        
        return False

    
    def DynamicCreate(self, sPath, iFinish):
        lPath = sPath.split('/')
        sFrontPath = ''
        for sComponent in lPath:
            if sFrontPath:
                sFrontPath += '/' + sComponent
            else:
                sFrontPath = sComponent
            if not self.IsModuleExists(sFrontPath.replace('/', '.')):
                sScrRootPath = self.GetScrRootPath(sFrontPath)
                if not sys.modules.get(sScrRootPath.replace('/', '.'), None):
                    PyextendLog.Info('dynamic create: %s' % sScrRootPath)
                    if sComponent.endswith('.py'):
                        self.CreateModule(sScrRootPath, sComponent)
                        continue
                    self.CreatePackage(sScrRootPath, sComponent)
        
        if iFinish:
            self.RunCode()

    
    def GetScrRootPath(self, sFrontPath):
        lFrontPath = sFrontPath.split('/')
        if len(lFrontPath) <= 1:
            return sFrontPath
        sScrRootPath = ''
        for sComponent in lFrontPath:
            if sys.modules.get(sComponent, None):
                iIndex = lFrontPath.index(sComponent)
                sScrRootPath = '/'.join(lFrontPath[iIndex:])
                break
        
        if not sScrRootPath:
            return lFrontPath[-1]
        return sScrRootPath

    
    def RunCode(self):
        PyextendLog.Info('runcode start')
        lLeafNodes = self.m_dPackData.keys()
        self.ExcetLeafCode(lLeafNodes)
        self.Clear()
        PyextendLog.Info('runcode end')

    
    def ExcetLeafCode(self, lLeafNodes):
        lNotExec = []
        for sTargetPath in lLeafNodes:
            sCode = self.m_dPackData.get(sTargetPath, None)
            if sCode:
                sScrRootPath = self.GetScrRootPath(sTargetPath)
                if sScrRootPath.endswith('.py'):
                    sScrRootPath = sScrRootPath[:-3]
                oModule = sys.modules.get(sScrRootPath.replace('/', '.'), None)
                if oModule:
                    sCode = base64.b64decode(sCode)
                    sCode = marshal.loads(sCode)
                    
                    try:
                        exec(sCode, oModule.__dict__)
                    except:
                        PythonError()
                        lNotExec.append(sTargetPath)

        
        if lNotExec and len(lNotExec) == len(lLeafNodes):
            PyextendLog.Error('leafcode err:%s' % lLeafNodes)
            return None
        if not lNotExec:
            PyextendLog.Info('excet leafcode end')
        else:
            self.ExcetLeafCode(lNotExec)

    
    def CreatePackage(self, sPath, sName):
        if sPath != sName:
            sParentPath = os.path.dirname(sPath).replace('/', '.')
            sPath = sPath.replace('/', '.')
            oPackage = types.ModuleType(sName)
            sys.modules[sPath] = oPackage
            oPackage.__package__ = sPath
            oParent = sys.modules.get(sParentPath, None)
            if not oParent:
                oParent = __import__(sParentPath)
                for sComponent in sParentPath.split('.'):
                    oParent = getattr(oParent, sComponent)
                
            setattr(oParent, sName, oPackage)
        else:
            oPackage = types.ModuleType(sName)
            sys.modules[sName] = oPackage
            oPackage.__package__ = sName

    
    def CreateModule(self, sPath, sName):
        if sPath != sName:
            sPath = sPath[:-3]
            sName = sName[:-3]
            sParentPath = os.path.dirname(sPath).replace('/', '.')
            sPath = sPath.replace('/', '.')
            oModule = types.ModuleType(sName)
            sys.modules[sPath] = oModule
            oModule.__package__ = sParentPath
            oParent = sys.modules.get(sParentPath, None)
            if not oParent:
                oParent = __import__(sParentPath)
                for sComponent in sParentPath.split('.'):
                    oParent = getattr(oParent, sComponent)
                
            setattr(oParent, sName, oModule)
        else:
            sName = sName[:-3]
            oModule = types.ModuleType(sName)
            sys.modules[sName] = oModule

    
    def Clear(self):
        self.m_dPackData = { }


if 'g_ExtendPackageMgr' not in globals():
    g_ExtendPackageMgr = CExtendPackageMgr()

def AcceptExtendData(sPath, sCode, iFinish):
    g_ExtendPackageMgr.AcceptData(sPath, sCode, iFinish)

