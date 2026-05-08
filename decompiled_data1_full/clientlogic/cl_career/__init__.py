# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_career/__init__.pyc
# RelativePath: clientlogic/cl_career/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_only import PythonError
import importlib

class CBaseCareerData(object):
    m_SID = 150
    m_CareerName = ''
    m_PerformList = ()
    m_ChoosePerform = ()
    
    def InitBaseAttr(self, oHero):
        oHero.m_CareerName = self.m_CareerName

    
    def InitCareerPerform(self, oHero):
        oHero.m_CareerPerform = self.m_PerformList

    
    def InitChoosePerform(self, oHero):
        oHero.m_ChoosePerformSet.update(self.m_ChoosePerform)


if 'g_CareerMoudleObj' not in globals():
    g_CareerMoudleObj = { }

def GetCareerData(iCareerSID):
    if iCareerSID not in g_CareerMoudleObj:
        
        try:
            mod = importlib.import_module('cl_career.c%d' % iCareerSID)
            g_CareerMoudleObj[iCareerSID] = mod.CCareerData()
        except:
            PythonError()
            return None

    return g_CareerMoudleObj[iCareerSID]

