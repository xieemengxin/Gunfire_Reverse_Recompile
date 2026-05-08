# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_behavior/debug/parseragent.pyc
# RelativePath: clientlogic/cl_behavior/debug/parseragent.pyc
# Source Generated with Decompyle++
# File: parseragent.pyc (Python 3.6)

from __future__ import absolute_import
import os
import sys
import importlib
from .. import GetTools

class CParserAgent(object):
    
    def __init__(self):
        (sAgentDir, sExportDir) = GetTools().GetParserAgentDir()
        self.m_ProjectAgentPath = sAgentDir.replace('\\', '/')
        self.m_ProjectExportPath = sExportDir.replace('\\', '/')
        self.m_dTempInfo = {
            'append_path': None,
            'append_module': [] }
        self.m_ExportClass = []

    
    def Start(self):
        if not os.path.exists(self.m_ProjectExportPath):
            os.makedirs(self.m_ProjectExportPath)
            with open(os.path.join(self.m_ProjectExportPath, '__init__.py'), 'w') as f:
                pass
        lstMoudle = self.WalkPath()
        for sName, moudle in lstMoudle:
            self.m_ExportClass = []
            self.Trans(sName, moudle)
        
        self.ClearTempInfo()

    
    def ClearTempInfo(self):
        for s in self.m_dTempInfo['append_module']:
            if s in sys.modules:
                sys.modules.pop(s)
        
        if self.m_dTempInfo['append_path'] is not None and self.m_dTempInfo['append_path'] in sys.path:
            sys.path.remove(self.m_dTempInfo['append_path'])
        self.m_dTempInfo = {
            'append_path': None,
            'append_module': [] }

    
    def WalkPath(self):
        if os.path.isabs(self.m_ProjectAgentPath) or self.m_ProjectAgentPath not in sys.path:
            sys.path.append(self.m_ProjectAgentPath)
            self.m_dTempInfo['append_path'] = self.m_ProjectAgentPath
        else:
            sAppendPath = os.path.join(os.getcwd(), self.m_ProjectAgentPath)
            if sAppendPath not in sys.path:
                sys.path.append(sAppendPath)
                self.m_dTempInfo['append_path'] = self.m_ProjectAgentPath
        lstMoudle = []
        for root, _, files in os.walk(self.m_ProjectAgentPath):
            for sFile in files:
                lstFileName = sFile.split('.')
                if len(lstFileName) != 2 or lstFileName[1] != 'py' or 'agent' not in lstFileName[0]:
                    continue
                sAbsPath = os.path.join(root, lstFileName[0]).replace('\\', '/')
                sModuleName = sAbsPath.replace(self.m_ProjectAgentPath + '/', '').replace('/', '.')
                if sModuleName not in sys.modules:
                    self.m_dTempInfo['append_module'].append(sModuleName)
                moudle = importlib.import_module(sModuleName)
                lstMoudle.append(('%s.py' % sModuleName.replace('.', '/'), moudle))
            
        
        return lstMoudle

    
    def Trans(self, sName, moudle):
        import codecs
        from .. import agent
        if 'CAgent' not in moudle.__dict__:
            GetTools().Print('%s No Class CAgent' % sName)
            return None
        sDoc = "'''%s\n'''\n" % moudle.__doc__ if moudle.__doc__ else ''
        lstWrite = [
            '# -*- coding: utf-8 -*-\n',
            sDoc,
            'import typing',
            "status=typing.TypeVar('status')\n\n"]
        cls = moudle.__dict__['CAgent']
        oParent = cls.__bases__[0]
        sParent = oParent.__module__
        lParent = sParent.split('.')
        while True:
            if '' in lParent:
                lParent.remove('')
                continue
        if 'agent' in sParent and oParent != agent.CAgent:
            if len(lParent) <= 1:
                sImport = 'import %s\n' % lParent[-1]
            else:
                sImport = 'from %s import %s\n' % ('.'.join(lParent[:-1]), lParent[-1])
            sClass = 'class CAgent(%s.CAgent):' % lParent[-1]
            lstWrite.append(sImport)
            lstWrite.append(sClass)
        else:
            sClass = 'class CAgent(object):'
            lstWrite.append(sClass)
        for sKey in ('m_EventKey', 'm_ConfigKey', 'm_DataKey', 'm_CacheKey'):
            lstWrite.extend(self.ParserDict(sKey, cls.__dict__.get(sKey, { })))
        
        lstWrite.append('\n\tdef GetData(self, sKey):\n\t\tpass\n\n\tdef GetConfig(self, sKey):\n\t\tpass\n\n\tdef GetChache(self, sKey):\n\t\tpass\n')
        for sFunc in sorted(cls.__dict__):
            if isinstance(cls.__dict__[sFunc], staticmethod):
                lstWrite.extend(self.ParserFunc(sFunc, cls.__dict__[sFunc]))
        
        dImport = { }
        dHasEnum = { }
        for expCls in self.m_ExportClass:
            sParentModule = expCls.__bases__[0].__module__
            if sParentModule == 'enum':
                dImport[sParentModule] = 1
                if expCls.__name__ in dHasEnum:
                    continue
                sClass = 'class %s(enum.Enum):' % expCls.__name__
                dHasEnum[expCls.__name__] = 1
                sMember = ''
                for sKey, val in expCls.__members__.items():
                    sMember += '\t%s = %s\n' % (sKey, val.value)
                
            lstWrite.insert(3, sClass)
            lstWrite.insert(4, sMember)
        
        sImport = ''
        for sModule in dImport:
            sImport += 'import %s\n' % sModule
        
        lstWrite.insert(3, sImport)
        sWrite = '\n'.join(lstWrite)
        sWrite = sWrite.replace('\r\n', '\n')
        sFinalPath = os.path.join(self.m_ProjectExportPath, sName)
        sDirName = os.path.dirname(sFinalPath)
        if not os.path.exists(sDirName):
            os.makedirs(sDirName)
            with codecs.open(os.path.join(sDirName, '__init__.py'), 'w', encoding = 'utf8') as f:
                pass
        with codecs.open(sFinalPath, 'w', encoding = 'utf8') as f:
            if sys.version_info.major == 3:
                f.write(sWrite)
            else:
                
                try:
                    f.write(sWrite.decode('utf8'))
                except:
                    f.write(sWrite.decode('gbk'))


    
    def ParserDict(self, sName, dDict):
        lstRes = []
        lstRes.append('\t%s = {' % sName)
        for sKey, value in sorted(dDict.items()):
            lstRes.append('\t\t"%s": "%s",' % (sKey, value))
        
        lstRes.append('\t}')
        return lstRes

    
    def ParserFunc(self, sFunc, obj):
        lstRes = []
        lstRes.append('\t@staticmethod')
        func = obj.__func__
        iArgs = func.__code__.co_argcount
        lstArgs = []
        for s in func.__code__.co_varnames[:iArgs]:
            if sys.version_info[:2] >= (3, 5) and s in func.__annotations__:
                cls = func.__annotations__[s]
                lstArgs.append('%s:%s' % (s, cls.__name__))
                self.m_ExportClass.append(cls)
                continue
            if s[0] == 'i':
                lstArgs.append('%s:int' % s)
                continue
            if s[0] == 'f':
                lstArgs.append('%s:float' % s)
                continue
            if s[0] == 's':
                lstArgs.append('%s:str' % s)
                continue
            if s[0] == 'b':
                lstArgs.append('%s:bool' % s)
                continue
            lstArgs.append(s)
        
        if sys.version_info[:2] >= (3, 5):
            if 'return' in func.__annotations__:
                sRetClass = ' -> %s' % func.__annotations__['return'].__name__
            else:
                sRetClass = ''
        else:
            sRetClass = ''
        lstRes.append('\tdef %s(%s)%s:' % (sFunc, ', '.join(lstArgs), sRetClass))
        sDoc = func.__doc__ if func.__doc__ else '\n\t\t'
        lstRes.append('\t\t"""%s"""' % sDoc)
        lstRes.append('\t\tpass')
        lstRes.append('')
        return lstRes


