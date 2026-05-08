# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_bezier.pyc
# RelativePath: clientlogic/cl_bezier.pyc
# Source Generated with Decompyle++
# File: cl_bezier.pyc (Python 3.6)

import cl_math

def GetQuadraticPowerBezierCurve(lstInitPos, lstExtraPos, bRing):
    iLength = len(lstInitPos)
    lstRes = []
    iCnt = iLength if bRing else iLength - 1
    for index in range(0, iCnt):
        iNext = index + 1 if index < iLength - 1 else 0
        iCount = int((cl_math.CalDistance3D(lstInitPos[index], lstExtraPos[index]) + cl_math.CalDistance3D(lstExtraPos[index], lstInitPos[iNext])) / 0.2)
        for iRatio in range(1, iCount):
            t = iRatio / iCount
            vTemp = cl_math.Vec3Add(cl_math.Vec3MulF(lstInitPos[index], (1 - t) * (1 - t)), cl_math.Vec3MulF(lstExtraPos[index], 2 * t * (1 - t)))
            vPos = cl_math.Vec3Add(vTemp, cl_math.Vec3MulF(lstInitPos[iNext], t * t))
            lstRes.append(vPos)
        
    
    if not bRing:
        lstTemp = lstRes[1:-1]
        lstTemp.reverse()
        lstRes.extend(lstTemp)
    return lstRes


def GetLinearBezierCurve(lstInitPos):
    iLength = len(lstInitPos)
    lstRes = []
    for index in range(0, iLength - 1):
        iCount = int(cl_math.CalDistance3D(lstInitPos[index], lstInitPos[index + 1]) / 0.2)
        for iRatio in range(1, iCount):
            t = iRatio / iCount
            vPos = cl_math.Vec3Add(cl_math.Vec3MulF(lstInitPos[index], 1 - t), cl_math.Vec3MulF(lstInitPos[index + 1], t))
            lstRes.append(vPos)
        
    
    lstTemp = lstRes[1:-1]
    lstTemp.reverse()
    lstRes.extend(lstTemp)
    return lstRes


class SecondBeizer(object):
    
    def __init__(self, vStart, vMid, vEnd):
        self.m_Start = vStart
        self.m_Mid = vMid
        self.m_End = vEnd
        self.InitConstant()

    
    def GetBezierLength(self):
        fLength = 0
        iCount = int((cl_math.CalDistance3D(self.m_Start, self.m_Mid) + cl_math.CalDistance3D(self.m_Mid, self.m_End)) / 2)
        vLastPos = self.m_Start
        for i in range(iCount):
            iRatio = (i + 1) / iCount
            vTemp = self.GetPos(iRatio)
            fLength += cl_math.CalDistance3D(vLastPos, vTemp)
            vLastPos = vTemp
        
        return fLength

    
    def InitConstant(self):
        bx = 2 * (self.m_Mid[0] - self.m_Start[0])
        ax = self.m_End[0] - bx - self.m_Start[0]
        by = 2 * (self.m_Mid[1] - self.m_Start[1])
        ay = self.m_End[1] - by - self.m_Start[1]
        bz = 2 * (self.m_Mid[2] - self.m_Start[2])
        az = self.m_End[2] - bz - self.m_Start[2]
        self.m_A = (ax, ay, az)
        self.m_B = (bx, by, bz)

    
    def GetPos(self, fTime):
        fTime2 = fTime * fTime
        vTemp = cl_math.Vec3Add(cl_math.Vec3MulF(self.m_A, fTime2), cl_math.Vec3MulF(self.m_B, fTime))
        vPos = cl_math.Vec3Add(self.m_Start, vTemp)
        return vPos


