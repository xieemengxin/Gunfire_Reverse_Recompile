# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_hero/linerandom.pyc
# RelativePath: clientlogic/cl_hero/linerandom.pyc
# Source Generated with Decompyle++
# File: linerandom.pyc (Python 3.6)


class CLinearRandom(object):
    
    def __init__(self, iSeed):
        self.m_Rand = int(iSeed)
        self.m_Cnt = 0

    
    def Random(self, iMax):
        if iMax <= 0:
            return 0
        iRandN = self.m_Rand
        iRandN = (iRandN * 61 + 7) % 10000
        self.m_Rand = iRandN % iMax
        self.m_Cnt += 1
        return self.m_Rand

    
    def GetSeed(self):
        return self.m_Rand

    
    def GetRandomCnt(self):
        return self.m_Cnt


