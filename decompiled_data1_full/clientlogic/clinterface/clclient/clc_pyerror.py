# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/clclient/clc_pyerror.pyc
# RelativePath: clientlogic/clinterface/clclient/clc_pyerror.pyc
# Source Generated with Decompyle++
# File: clc_pyerror.pyc (Python 3.6)

import C_logic
import os
import re
import math
import traceback
import cllib.lib_flag
from cl_object.logging import EvidenceLog, ErrLog
AddressRE = re.compile('\\<(\\S+)\\s.+at.+\\>')

class CPyError(object):
    m_ErrorObjAttr = ('m_ID', 'm_TaskID', 'm_SID', 'm_Players', 'm_Owner')
    m_Collected = False
    m_Busted = False
    m_CheatList = [
        'cheatengine',
        'flingtrainer']
    m_TmpMsg = ''
    
    def GetFunccode(self, func):
        if hasattr(func, '__func__'):
            return func.__func__.__code__
        if hasattr(func, '__code__'):
            return func.__code__

    
    def FindFunc(self, tb):
        frame = tb.tb_frame
        funcname = frame.f_code.co_name
        for dict in (frame.f_locals, frame.f_globals):
            for att in dict:
                v = dict[att]
                funccode = None
                if att == funcname:
                    funccode = self.GetFunccode(v)
                elif hasattr(v, funcname):
                    v = getattr(v, funcname)
                    funccode = self.GetFunccode(v)
                
                if funccode == frame.f_code:
                    return v
            
        

    
    def ExtErrorInfo(self, tb, exceptionType, exceptionReason):
        lstOutPut = []
        if self.m_Collected:
            lstOutPut.append('存在前置报错 请注意确认')
        if not self.m_Collected:
            self.ColletEvidence()
        obj = None
        if self.m_Busted:
            lstOutPut.append('Busted')
        lasttb = None
        while True:
            if tb:
                lasttb = tb
                tb = tb.tb_next
                continue
        if not lasttb:
            return ''
        func = self.FindFunc(lasttb)
        if func and hasattr(func, '__self__'):
            obj = func.__self__
            if hasattr(func.__self__, '__class__'):
                lstOutPut.append('类:%s' % func.__self__.__class__)
        if not obj and 'self' in lasttb.tb_frame.f_locals:
            obj = lasttb.tb_frame.f_locals['self']
        if obj:
            for sAttr in self.m_ErrorObjAttr:
                if not hasattr(obj, sAttr):
                    continue
                sAttrName = getattr(obj, sAttr)
                lstOutPut.append('实例%s:%s' % (sAttr, sAttrName))
            
            if hasattr(obj, 'Name'):
                
                try:
                    sName = obj.Name()
                except:
                    sName = getattr(obj, 'm_Name', '')

                if sName:
                    lstOutPut.append('实例名:%s' % sName)
            if hasattr(obj, 'm_Container') and hasattr(obj.m_Container, 'm_Owner'):
                lstOutPut.append('容器主人ID:%s' % obj.m_Container.m_Owner)
        dShortInfo = { }
        
        try:
            for k, v in lasttb.tb_frame.f_locals.items():
                dShortInfo[k] = self.ShortInfo(v)
            
        except:
            dShortInfo = lasttb.tb_frame.f_locals

        sLocals = '局部变量:%s\n' % str(dShortInfo)
        if len(sLocals) > 1000:
            sLocals = '%s...(略)\n' % sLocals[:1000]
        lstOutPut.append(sLocals)
        for filename, lineno, name, _ in traceback.extract_stack()[:-3]:
            lstOutPut.append('  File "%s", line %d ,in %s' % (filename, lineno, name))
        
        lstOutPut.append('')
        return '\n'.join(lstOutPut)

    
    def ShortInfo(self, value):
        ret = None
        if isinstance(value, dict):
            dRet = { }
            for k, v in value.items():
                dRet[k] = self.ShortInfo(v)
            
            ret = dRet
        elif isinstance(value, (list, tuple)):
            lstRet = []
            for v in value:
                lstRet.append(self.ShortInfo(v))
            
            ret = lstRet
        elif isinstance(value, float):
            ret = round(value, 2)
        else:
            sValue = str(value)
            oMatch = AddressRE.match(sValue)
            if oMatch:
                value = oMatch.group(1)
            ret = value
        return ret

    
    def ColletEvidence(self):
        if cllib.lib_flag.g_IsMobileRun:
            return None
        lstPName = []
        
        try:
            lstLines = os.popen('tasklist /fo csv').readlines()
            lstLines = lstLines[1:]
        except:
            lstLines = []

        
        try:
            RE = re.compile('\\"(.+?)\\",.+')
            self.CheckCheat(lstLines)
            for sLine in lstLines:
                oMatch = RE.match(sLine)
                if oMatch:
                    sName = oMatch.group(1)
                    sName = sName.rstrip('.exe')
                    if sName not in lstPName:
                        lstPName.append(sName)
            
            lstPName = sorted(lstPName)
            self.m_Collected = True
        except:
            lstPName = []
            self.m_Collected = False

        iMax = 100
        if not lstPName:
            lstPName = lstLines
            iMax = 20
        iSplit = math.ceil(len(lstPName) / iMax)
        for _ in range(iSplit):
            EvidenceLog.Info(lstPName[:iMax])
            lstPName = lstPName[iMax:]
            if not lstPName:
                break
        

    
    def CheckCheat(self, sTasks):
        for sLine in sTasks:
            sLower = sLine.lower()
            for sCheat in self.m_CheatList:
                if sCheat in sLower:
                    self.m_Busted = True
                    return None
            
        



def ExtExceptionCallBack(tb, exceptionType, exceptionReason):
    
    try:
        res = g_PyError.ExtErrorInfo(tb, exceptionType, exceptionReason)
        ErrLog.Debug('%s %s %s' % (exceptionType, exceptionReason, res))
        if g_PyError.m_TmpMsg:
            res += '\n请查看本行提示: %s\n' % g_PyError.m_TmpMsg
            g_PyError.m_TmpMsg = ''
    except:
        res = 'py自定义报错异常\n'

    return res

if 'g_PyError' not in globals():
    g_PyError = CPyError()
