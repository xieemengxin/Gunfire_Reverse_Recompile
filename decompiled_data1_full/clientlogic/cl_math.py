# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_math.pyc
# RelativePath: clientlogic/cl_math.pyc
# Source Generated with Decompyle++
# File: cl_math.pyc (Python 3.6)

from C_frgame import IntSqrt, CalDistance, CalDistance3D, CheckDistance, CheckDistance3D, CalJumpPath
from cl_commondefines import g_SideTypeEnemy, g_SideTypeTeammate, SCENEOBJ_TYPE, OBJ_ENEMY_DEF, OBJ_TEAMMATE_DEF, OBJ_SELF_DEF, ATT_SHAPE_RECTANGLE, ATT_SHAPE_SPHERICALSHELL, ATT_SHAPE_SECTOR, ATT_SHAPE_SPHERE, ATT_SHAPE_CYLINDER, OBJ_ALL_PLAYER
import cllib.lib_flag as lib_flag
import math
if 'g_fSinAngle' not in globals():
    g_fSinAngle = { }
    g_TanAngle = { }
    g_SinAngle1000 = { }
    g_TanAngle1000 = { }

def InitTrigTable():
    for i in range(360):
        g_fSinAngle[i] = math.sin(i * g_InvRa)
    


def UseCMath():
    
    def _UseCMath(func):
        import C_math
        from cl_object.logging import OtherLog
        sFunc = func.__name__
        cFunc = getattr(C_math, sFunc, None)
        if not cFunc:
            OtherLog.Debug('cmath pass %s' % sFunc)
            return func
        return cFunc

    return _UseCMath

g_InvRa = math.pi / 180
InitTrigTable()

def fSinAngle(iAngle):
    return g_fSinAngle[iAngle % 360]

fSinAngle = UseCMath()(fSinAngle)

def fCosAngle(iAngle):
    return g_fSinAngle[(iAngle + 90) % 360]

fCosAngle = UseCMath()(fCosAngle)

def CosAngle1000(iAngle):
    iAngle = (iAngle + 90) % 360
    if iAngle not in g_SinAngle1000:
        g_SinAngle1000[iAngle] = int(fSinAngle(iAngle) * 1000)
    return g_SinAngle1000[iAngle]


def TanAngle1000(iAngle):
    if iAngle not in g_TanAngle1000:
        iCos = CosAngle1000(iAngle)
        if not iCos:
            iCos = 1
        g_TanAngle1000[iAngle] = CosAngle1000(iAngle - 90) * 1000 // iCos
    return g_TanAngle1000[iAngle]


def SinAngle(fAngle):
    fRadian = math.radians(fAngle)
    return math.sin(fRadian)

SinAngle = UseCMath()(SinAngle)

def CosAngle(fAngle):
    fRadian = math.radians(fAngle)
    return math.cos(fRadian)

CosAngle = UseCMath()(CosAngle)

def TanAngle(fAngle):
    fRadian = math.radians(fAngle)
    return math.tan(fRadian)

TanAngle = UseCMath()(TanAngle)

def CotAngle(fAngle):
    fRadian = math.radians(fAngle)
    return 1 / math.tan(fRadian)

CotAngle = UseCMath()(CotAngle)

def IsZero(v):
    if abs(v[0]) > 1e-06 or abs(v[1]) > 1e-06 or abs(v[2]) > 1e-06:
        return False
    return True

IsZero = UseCMath()(IsZero)

def IsPlaneZero(v):
    if abs(v[0]) > 1e-06 or abs(v[2]) > 1e-06:
        return False
    return True

IsPlaneZero = UseCMath()(IsPlaneZero)

def IsPlaneEqual(v, w):
    if v[0] == w[0] and v[2] == w[2]:
        return True
    return False


def IsEqual(v, w):
    if v[0] == w[0] and v[1] == w[1] and v[2] == w[2]:
        return True
    return False


def Vec3Add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

Vec3Add = UseCMath()(Vec3Add)

def Vec3Sum(lstV):
    (x, y, z) = (0, 0, 0)
    for _x, _y, _z in lstV:
        x += _x
        y += _y
        z += _z
    
    return (x, y, z)

Vec3Sum = UseCMath()(Vec3Sum)

def Vec3Minus(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])

Vec3Minus = UseCMath()(Vec3Minus)

def Vec3MulF(v, f):
    return (f * v[0], f * v[1], f * v[2])

Vec3MulF = UseCMath()(Vec3MulF)

def Vec3MulV(v1, v2):
    return (v1[0] * v2[0], v1[1] * v2[1], v1[2] * v2[2])

Vec3MulV = UseCMath()(Vec3MulV)

def Vec3Mad(v, d, f):
    return (v[0] + d[0] * f, v[1] + d[1] * f, v[2] + d[2] * f)

Vec3Mad = UseCMath()(Vec3Mad)

def Vec3Normalize(v):
    dis = CalDistance3D(v, (0, 0, 0))
    if not dis:
        return (0, 0, 0)
    disf = 1 / dis
    return (disf * v[0], disf * v[1], disf * v[2])

Vec3Normalize = UseCMath()(Vec3Normalize)

def Vec3NormalizeByPython(v):
    dis = (v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** 0.5
    if not dis:
        return (0, 0, 0)
    disf = 1 / dis
    return (disf * v[0], disf * v[1], disf * v[2])


def VectorDot2D(v1, v2):
    return v1[0] * v2[0] + v1[2] * v2[2]

VectorDot2D = UseCMath()(VectorDot2D)

def VectorDot3D(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

VectorDot3D = UseCMath()(VectorDot3D)

def VectorCross2D(v1, v2):
    return v1[0] * v2[2] - v2[0] * v1[2]

VectorCross2D = UseCMath()(VectorCross2D)

def VectorCross3D(v1, v2):
    return (v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0])

VectorCross3D = UseCMath()(VectorCross3D)

def CheckVector2Angle(v, w, iAngle):
    x1 = v[0]
    z1 = v[2]
    x2 = w[0]
    z2 = w[2]
    if (x1 == 0 or z1 == 0 or x2 == 0) and z2 == 0:
        return 0
    fVDot = x1 * x2 + z1 * z2
    fCos = CosAngle(iAngle)
    if fVDot > 0 or fCos <= 0:
        return 0
    if fVDot < 0 or fCos >= 0:
        return 1
    if fCos > 0:
        return 1
    return 0

CheckVector2Angle = UseCMath()(CheckVector2Angle)

def RotateAroundVector(tTar, tAxis, iAngle):
    (x, y, z) = tAxis
    if x * x + y * y + z * z != 1:
        (x, y, z) = Vec3Normalize(tAxis)
    c = CosAngle(iAngle)
    a = 1 - CosAngle(iAngle)
    b = SinAngle(iAngle)
    m = [
        [
            a * x * x + c,
            a * x * y + b * z,
            a * x * z - b * y],
        [
            a * x * y - b * z,
            a * y * y + c,
            a * y * z + b * x],
        [
            a * x * z + b * y,
            a * y * z - b * x,
            a * z * z + c]]
    lstNew = [
        0,
        0,
        0]
    for i in range(3):
        lstNew[i] = m[0][i] * tTar[0] + m[1][i] * tTar[1] + m[2][i] * tTar[2]
    
    return tuple(lstNew)

RotateAroundVector = UseCMath()(RotateAroundVector)

def RotateByEuler(v, Euler):
    (iAngleX, iAngleY, iAngleZ) = Euler
    v = RotateAroundVector(v, (1, 0, 0), iAngleX)
    v = RotateAroundVector(v, (0, 1, 0), iAngleY)
    v = RotateAroundVector(v, (0, 0, 1), iAngleZ)
    return v

RotateByEuler = UseCMath()(RotateByEuler)

def CalAngle2D(v1, v2):
    (x1, _, z1) = v1
    (x2, _, z2) = v2
    l1 = CalDistance((0, 0, 0), v1)
    l2 = CalDistance((0, 0, 0), v2)
    if not l1 or not l2:
        return 0
    cos = (x1 * x2 + z1 * z2) / l1 / l2
    if cos > 1:
        cos = 1
    elif cos < -1:
        cos = -1
    fAngle = math.acos(cos) * 180 / math.pi
    return int(fAngle)

CalAngle2D = UseCMath()(CalAngle2D)

def CalAngle3D(v1, v2):
    (x1, y1, z1) = v1
    (x2, y2, z2) = v2
    l1 = CalDistance3D((0, 0, 0), v1)
    l2 = CalDistance3D((0, 0, 0), v2)
    if not l1 or not l2:
        return 0
    cos = (x1 * x2 + y1 * y2 + z1 * z2) / l1 / l2
    if cos > 1:
        cos = 1
    elif cos < -1:
        cos = -1
    fAngle = math.acos(cos) * 180 / math.pi
    return int(fAngle)

CalAngle3D = UseCMath()(CalAngle3D)

def CheckManhattanDis(v1, v2, iDis):
    if abs(v1[0] - v2[0]) + abs(v1[1] - v2[1]) + abs(v1[2] - v2[2]) < iDis:
        return 1
    return 0


def CheckMahhattanDis2D(v1, v2, iDis):
    if abs(v1[0] - v2[0]) + abs(v1[2] - v2[2]) < iDis:
        return 1
    return 0


def CalRotate2D(vFace):
    (x, _, z) = vFace
    ln = CalDistance((0, 0, 0), vFace)
    if not ln:
        return 0
    cos = z / ln
    if cos > 1:
        cos = 1
    elif cos < -1:
        cos = -1
    radiany = math.acos(cos) * 180 / math.pi
    if x < 0:
        radiany *= -1
    return int(radiany)

CalRotate2D = UseCMath()(CalRotate2D)

def Vec2DisplaceDir(v, d, fMoveDis):
    dis = fMoveDis / math.sqrt(d[0] * d[0] + d[1] * d[1])
    x = v[0] + d[0] * dis
    z = v[1] + d[1] * dis
    return (x, z)

Vec2DisplaceDir = UseCMath()(Vec2DisplaceDir)

def Vec3DisplacePos(v, w, fMoveDis):
    fDis = CalDistance3D(v, w)
    if not fDis:
        return v
    dis = fMoveDis / fDis
    x = v[0] + (w[0] - v[0]) * dis
    y = v[1] + (w[1] - v[1]) * dis
    z = v[2] + (w[2] - v[2]) * dis
    return (x, y, z)

Vec3DisplacePos = UseCMath()(Vec3DisplacePos)

def Vec3DisplaceDir(v, d, fMoveDis):
    fDis = CalDistance3D((0, 0, 0), d)
    if not fDis:
        return v
    dis = fMoveDis / fDis
    x = v[0] + d[0] * dis
    y = v[1] + d[1] * dis
    z = v[2] + d[2] * dis
    return (x, y, z)

Vec3DisplaceDir = UseCMath()(Vec3DisplaceDir)

def Vec3HorizonDisplacePos(v, w, fMoveDis):
    fDis = CalDistance(v, w)
    if not fDis:
        return v
    dis = fMoveDis / fDis
    x = v[0] + (w[0] - v[0]) * dis
    y = v[1]
    z = v[2] + (w[2] - v[2]) * dis
    return (x, y, z)

Vec3HorizonDisplacePos = UseCMath()(Vec3HorizonDisplacePos)

def Vec3HorizonDisplaceDir(v, d, fMoveDis):
    fDis = CalDistance((0, 0, 0), d)
    if not fDis:
        return v
    dis = fMoveDis / fDis
    x = v[0] + d[0] * dis
    y = v[1]
    z = v[2] + d[2] * dis
    return (x, y, z)

Vec3HorizonDisplaceDir = UseCMath()(Vec3HorizonDisplaceDir)

def Vec3DisplacePosEdge(oGame, iScene, v, w, fMoveDis):
    vNew = Vec3DisplacePos(v, w, fMoveDis)
    vNew = oGame.Scene_GetSafePos(iScene, vNew)
    return vNew


def Vec2DestPosDir(v, d, fDis, iShiftAngle):
    dx = d[0] * CosAngle(iShiftAngle) - d[1] * SinAngle(iShiftAngle)
    dz = d[0] * SinAngle(iShiftAngle) + d[1] * CosAngle(iShiftAngle)
    if dx == 0 and dz == 0:
        return v
    return Vec2DisplaceDir(v, (dx, dz), fDis)

Vec2DestPosDir = UseCMath()(Vec2DestPosDir)

def Vec3DestPosDirPlane(v, d, fDis, iShiftAngle):
    dx = d[0] * CosAngle(iShiftAngle) - d[2] * SinAngle(iShiftAngle)
    dz = d[0] * SinAngle(iShiftAngle) + d[2] * CosAngle(iShiftAngle)
    if dx == 0 and dz == 0:
        return v
    return Vec3DisplaceDir(v, (dx, 0, dz), fDis)

Vec3DestPosDirPlane = UseCMath()(Vec3DestPosDirPlane)

def Vec3DestPosDir(v, d, fDis, iShiftAngle):
    dx = d[0] * CosAngle(iShiftAngle) - d[2] * SinAngle(iShiftAngle)
    dz = d[0] * SinAngle(iShiftAngle) + d[2] * CosAngle(iShiftAngle)
    dy = d[1]
    if dx == 0 and dz == 0 and dy == 0:
        return v
    return Vec3DisplaceDir(v, (dx, dy, dz), fDis)

Vec3DestPosDir = UseCMath()(Vec3DestPosDir)

def Vec3MoveDirDisp(d, fMoveDis):
    dis = fMoveDis / CalDistance3D((0, 0, 0), d)
    x = d[0] * dis
    y = d[1] * dis
    z = d[2] * dis
    return (x, y, z)

Vec3MoveDirDisp = UseCMath()(Vec3MoveDirDisp)

def GetRandomPointInCircle(oGame, ox, oz, r):
    if not r:
        return (ox, oz)
    a = oGame.Random(360)
    u = oGame.Random(r * r)
    u = math.sqrt(u)
    return (ox + u * CosAngle(a), oz + u * SinAngle(a))


def Rotate2DPointByPoint(lstOriPoint, lstRatPoint, iAngle):
    (ox, oy) = lstOriPoint
    (x, y) = lstRatPoint
    c = CosAngle(iAngle)
    s = SinAngle(iAngle)
    iRx = int((c * x - s * y) + (1 - c) * ox + s * oy)
    iRy = int(s * x + c * y + (1 - c) * oy - s * ox)
    return [
        iRx,
        iRy]


def Rotate2DPointByPoint2(lstOriPoint, lstRatPoint, iAngle):
    (ox, oy) = lstOriPoint
    (x, y) = lstRatPoint
    c = CosAngle(iAngle)
    s = SinAngle(iAngle)
    fRx = (c * x - s * y) + (1 - c) * ox + s * oy
    fRy = s * x + c * y + (1 - c) * oy - s * ox
    return [
        fRx,
        fRy]


def GetRandomPointOnRect(oGame, x, y):
    iType = oGame.Random(2)
    if iType:
        return (oGame.Random(x), oGame.Random(2) * y)
    return (oGame.Random(2) * x, oGame.Random(y))


def GetCenterWorldPos(vOrigin, vCenter, vScale, vAngle):
    vAngle = (int(vAngle[0]), int(vAngle[1]), int(vAngle[2]))
    return Vec3Add(vOrigin, RotateByEuler(Vec3MulV(vCenter, vScale), vAngle))


def Angle2Radians(vAngle):
    return (vAngle[0] * g_InvRa, vAngle[1] * g_InvRa, vAngle[2] * g_InvRa)


def Radians2Angle(vRadians):
    return (int(vRadians[0] / g_InvRa), int(vRadians[1] / g_InvRa), int(vRadians[2] / g_InvRa))

Radians2Angle = UseCMath()(Radians2Angle)

def Dir2Radians(vDir):
    if vDir[1]:
        vDir = Vec3NormalizeByPython(vDir)
    return (math.asin(-vDir[1]), math.atan2(vDir[0], vDir[2]), 0)


def GetFootPoint(x0, y0, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return (x1, y1)
    if x1 == x2:
        return (x1, y0)
    if y1 == y2:
        return (x0, y1)
    x01 = x0 - x1
    x21 = x2 - x1
    y01 = y0 - y1
    y21 = y2 - y1
    uk = x01 * x21 + y01 * y21
    dk = x21 * x21 + y21 * y21
    x = x1 + uk * x21 / dk
    y = y1 + uk * y21 / dk
    return (x, y)


def GetLinePointDis(x0, y0, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return CalDistance((x1, 0, y1), (x0, 0, y0))
    if x1 == x2:
        if x0 > x1:
            return x0 - x1
        return x1 - x0
    if y1 == y2:
        if y0 > y1:
            return y0 - y1
        return y1 - y0
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    D = A * x0 + B * y0 + C
    fDis = math.sqrt(D * D / (A * A + B * B))
    return fDis

GetLinePointDis = UseCMath()(GetLinePointDis)

def GetPointInTriangle(oGame, v1, v2, v3):
    if len(v1) == 3:
        v1 = (v1[0], v1[2])
        v2 = (v2[0], v2[2])
        v3 = (v3[0], v3[2])
    tVector1 = (v2[0] - v1[0], v2[1] - v1[1])
    tVector2 = (v3[0] - v1[0], v3[1] - v1[1])
    t1 = (oGame.Random(100) + 1) / 100
    t2 = (oGame.Random(100) + 1) / 100
    if t1 + t2 > 1:
        t1 = 1 - t1
        t2 = 1 - t2
    tPoint = (t1 * tVector1[0] + t2 * tVector2[0] + v1[0], t1 * tVector1[1] + t2 * tVector2[1] + v1[1])
    return tPoint


def GetPointInCircle(oGame, vCenter, fRadius):
    (x, y, z) = vCenter
    fRandRadius = (oGame.Random(int(fRadius * 100)) + 1) / 100
    iRandAngle = oGame.Random(360)
    x = x + fRandRadius * CosAngle(iRandAngle)
    z = z + fRandRadius * SinAngle(iRandAngle)
    return (x, y, z)


def PNPoly(lstVertices, v):
    for i, vPos in enumerate(lstVertices):
        if len(vPos) == 3:
            lstVertices[i] = (vPos[0], vPos[2])
            continue
    
    bRet = False
    j = len(lstVertices) - 1
    for i, v1 in enumerate(lstVertices):
        v2 = lstVertices[j]
        if (v1[1] > v[1]) != (v2[1] > v[1]) and v[0] < (v2[0] - v1[0] * (v[1] - v1[1]) / (v2[1] - v1[1])) + v1[0]:
            bRet = not bRet
        j = i
    
    return bRet


def PosInOBB(vOri, vOffset, vSize, vScale, vAngle, vPos):
    vDiffAngle = (-1 * vAngle[0], -1 * vAngle[1], -1 * vAngle[2])
    vNewPos = Vec3Minus(vPos, vOri)
    vNewPos = RotateByEuler(vNewPos, vDiffAngle)
    vCenter = Vec3MulV(vOffset, vScale)
    vHalf = Vec3MulF(vSize, 0.5)
    vHalf = Vec3MulV(vHalf, vScale)
    for i in range(3):
        if not vNewPos[i] < vCenter[i] - vHalf[i]:
            if vNewPos[i] > vCenter[i] + vHalf[i]:
                return False
    
    return True

PosInOBB = UseCMath()(PosInOBB)

def RemoveDuplicates(func):
    
    def _RemoveDuplicates(*args):
        return list(set(func(*args)))

    if lib_flag.g_IsLogicLayer and lib_flag.g_IsMobile:
        return _RemoveDuplicates
    return func


def GetAttackTargetList(oGame, iScene, iAttShape, lstArgs, dQArgs, bIsOffset = True):
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    if not oScene:
        return set()
    if iAttShape == ATT_SHAPE_SPHERE:
        (vPos, fRadius) = lstArgs
        lstTarget = oGame.Scene_GetSphereObjects(iScene, vPos, fRadius, dQArgs['Mask'], dQArgs)
    elif iAttShape == ATT_SHAPE_SECTOR:
        (vPos, vDir, fRadius, fHeight, iAngle) = lstArgs
        fHalfHeight = fHeight / 2
        vPos = [
            vPos[0],
            vPos[1] + fHalfHeight,
            vPos[2]]
        lstTarget = oGame.Scene_GetSectorObjects(iScene, vPos, vDir, fRadius, fHalfHeight, iAngle, dQArgs['Mask'], dQArgs)
    elif iAttShape == ATT_SHAPE_RECTANGLE:
        (vPos, vDir, fLength, fWidth, fHeight) = lstArgs
        fHalfLength = fLength / 2
        fHalfWidth = fWidth / 2
        fHalfHeight = fHeight / 2
        if lib_flag.g_UseNewRectangle:
            lstTarget = oGame.Scene_GetRectangleObjects(iScene, vPos, vDir, (fHalfWidth, fHalfHeight, fHalfLength), dQArgs['Mask'], dQArgs)
        else:
            iUseEular = dQArgs.get('UseEuler', 0)
            if not iUseEular:
                if vDir[1] < 0.1:
                    if not IsZero(vDir) and bIsOffset:
                        vPos = Vec3DisplaceDir(vPos, vDir, fHalfLength)
                    vPos = (vPos[0], vPos[1] + fHalfHeight, vPos[2])
                else:
                    vPoint1 = Vec3DisplaceDir(vPos, vDir, fHalfLength)
                    vPoint2 = Vec3DestPosDirPlane(vPos, vDir, 1, 90)
                    vNormal = VectorCross3D(Vec3Minus(vPos, vPoint2), Vec3Minus(vPos, vPoint1))
                    if IsZero(vNormal):
                        vPos = (vPos[0], vPos[1] + fHalfHeight, vPos[2])
                    elif bIsOffset:
                        vPos = Vec3DisplaceDir(vPoint1, vNormal, fHalfHeight)
                    else:
                        vPos = Vec3DisplaceDir(vPos, vNormal, fHalfHeight)
            else:
                vEuler = vDir
                vPos = GetOffsetWorldPos2(vPos, (0, 0, fHalfLength), vEuler)
            if bIsOffset:
                lstTarget = oGame.Scene_GetRectangleObjects(iScene, vPos, vDir, (fHalfWidth, fHalfHeight, fHalfLength), dQArgs['Mask'], dQArgs)
            else:
                lstTarget = oGame.Scene_GetRectangleObjects(iScene, vPos, vDir, (fHalfWidth, fHalfHeight, fLength), dQArgs['Mask'], dQArgs)
    elif iAttShape == ATT_SHAPE_CYLINDER:
        (vPos, fRadius, fHalfHeight) = lstArgs
        lstTarget = oGame.Scene_GetCylinderObjects(iScene, vPos, fRadius, fHalfHeight, dQArgs['Mask'], dQArgs)
    elif iAttShape == ATT_SHAPE_SPHERICALSHELL:
        (vPos, fMaxRadius, fMinRadius) = lstArgs
        lstOuterTarget = oGame.Scene_GetSphereObjects(iScene, vPos, fMaxRadius, dQArgs['Mask'], dQArgs)
        lstInnerTarget = oGame.Scene_GetSphereObjects(iScene, vPos, fMinRadius, dQArgs['Mask'], dQArgs)
        lstCheckInnerTarget = set()
        for iTarget in lstInnerTarget:
            oTarget = oGame.GetObject(iTarget)
            if not oTarget:
                continue
            vTargetPos = oTarget.GetPos()
            vTargetCenterPos = (vTargetPos[0], vTargetPos[1] + oTarget.m_ModelHeight / 2, vTargetPos[2])
            if CheckDistance3D(vTargetCenterPos, vPos, fMinRadius):
                lstCheckInnerTarget.add(iTarget)
        
        lstTarget = lstOuterTarget - lstCheckInnerTarget
    else:
        lstTarget = set()
    return lstTarget

GetAttackTargetList = RemoveDuplicates(GetAttackTargetList)

def CheckTargetType(_oGame, oTarget, iAttack, iSide, iTargetType):
    iFlag = 0
    if iAttack == oTarget.m_ID:
        if iTargetType & OBJ_SELF_DEF:
            iFlag = 1
        else:
            return 0
    if not iFlag:
        if iTargetType & OBJ_TEAMMATE_DEF and g_SideTypeTeammate[iSide] & oTarget.m_Side:
            iFlag = 1
        elif iTargetType & OBJ_ENEMY_DEF and g_SideTypeEnemy[iSide] & oTarget.m_Side:
            iFlag = 1
        elif iTargetType == OBJ_ALL_PLAYER:
            iFlag = 1
    if iFlag and iTargetType & SCENEOBJ_TYPE & oTarget.m_FightType:
        return 1
    return 0


def Get2DPoly6(ox, oz, iEdgeDis):
    VERT_POLY6 = [
        (0, 100),
        (87, 50),
        (87, -50),
        (0, -100),
        (-87, -50),
        (-87, 50)]
    lstVert = []
    for dx, dz in VERT_POLY6:
        dx = iEdgeDis * dx // 100
        dz = iEdgeDis * dz // 100
        tPos = (ox + dx, oz + dz)
        lstVert.append(tPos)
    
    return lstVert


def GetOffsetWorldPos(tOrigin, tOffset, tAngle):
    (ox, oy, oz) = tOffset
    (ax, ay, az) = tAngle
    sinx = SinAngle(ax)
    cosx = CosAngle(ax)
    siny = SinAngle(ay)
    cosy = CosAngle(ay)
    sinz = SinAngle(az)
    cosz = CosAngle(az)
    r11 = cosy * cosz + sinx * siny * sinz
    r12 = cosz * sinx * siny - cosy * sinz
    r13 = siny * cosx
    r21 = cosx * sinz
    r22 = cosx * cosz
    r23 = -sinx
    r31 = cosy * sinx * sinz - siny * cosz
    r32 = siny * sinz + cosy * cosx * cosz
    r33 = cosx * cosy
    tx = r11 * ox + r12 * oy + r13 * oz + tOrigin[0]
    ty = r21 * ox + r22 * oy + r23 * oz + tOrigin[1]
    tz = r31 * ox + r32 * oy + r33 * oz + tOrigin[2]
    return (tx, ty, tz)


def GetOffsetWorldPos2(tOrigin, tOffset, tRadians):
    (ox, oy, oz) = tOffset
    (rx, ry, rz) = tRadians
    sinx = math.sin(rx)
    cosx = math.cos(rx)
    siny = math.sin(ry)
    cosy = math.cos(ry)
    sinz = math.sin(rz)
    cosz = math.cos(rz)
    r11 = cosy * cosz + sinx * siny * sinz
    r12 = cosz * sinx * siny - cosy * sinz
    r13 = siny * cosx
    r21 = cosx * sinz
    r22 = cosx * cosz
    r23 = -sinx
    r31 = cosy * sinx * sinz - siny * cosz
    r32 = siny * sinz + cosy * cosx * cosz
    r33 = cosx * cosy
    tx = r11 * ox + r12 * oy + r13 * oz + tOrigin[0]
    ty = r21 * ox + r22 * oy + r23 * oz + tOrigin[1]
    tz = r31 * ox + r32 * oy + r33 * oz + tOrigin[2]
    return (tx, ty, tz)

