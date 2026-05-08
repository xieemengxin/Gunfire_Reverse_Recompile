# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_resmgr/atom.pyc
# RelativePath: clientlogic/cl_resmgr/atom.pyc
# Source Generated with Decompyle++
# File: atom.pyc (Python 3.6)

from cl_only import ShufferList

class CAtom(object):
    m_Scene = 1001
    m_FirstTime = 0
    m_RefreshCD = 0
    m_ShufferPos = 0
    m_PosList = []
    m_ObjList = []
    
    def __init__(self):
        self.m_Info = []
        for idx, iDataSID in enumerate(self.m_ObjList):
            tPos = self.m_PosList[idx]
            self.m_Info.append((tPos, iDataSID))
        

    
    def GetInfo(self):
        return self.m_Info

    
    def GetFirstTime(self):
        return self.m_FirstTime

    
    def GetRefreshCD(self):
        return self.m_RefreshCD



class CMonsterAtom(CAtom):
    m_Leader = 0
    
    def GetLeader(self):
        return self.m_Leader


