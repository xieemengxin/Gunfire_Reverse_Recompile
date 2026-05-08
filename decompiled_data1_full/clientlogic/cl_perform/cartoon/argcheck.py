# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/argcheck.pyc
# RelativePath: clientlogic/cl_perform/cartoon/argcheck.pyc
# Source Generated with Decompyle++
# File: argcheck.pyc (Python 3.6)


def PosAroundCheck(oSkill, vClient, vServer, iPlane = 4, iHeight = 2):
    (xc, yc, zc) = vClient
    (xs, ys, zs) = vServer
    iPlaneDelta = 2
    iHeightDelta = 2.5
    if abs(xc - xs) + abs(zc - zs) < iPlane + iPlaneDelta and yc > ys - iHeightDelta and yc < ys + iHeight + iHeightDelta:
        return True
    return False

