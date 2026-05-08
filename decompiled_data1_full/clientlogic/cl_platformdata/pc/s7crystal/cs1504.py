# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7crystal/cs1504.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7crystal/cs1504.pyc
# Source Generated with Decompyle++
# File: cs1504.pyc (Python 3.6)

from cl_seasonplay.season7.crystal import CCrystalData
from cl_commondefines import CRTSTAL_NORMAL

class CCrystal(CCrystalData):
    m_SID = 1504
    m_Name = '测试-周围加成'
    m_CrystalType = CRTSTAL_NORMAL
    m_CanRotate = False
    m_MaxPoint = 12
    m_CanChoosePoint = { }
    m_GridConfig = {
        (1, 1): (0, 1),
        (0, 1): (0, 2),
        (-1, 1): (0, 1),
        (-1, 0): (0, 2),
        (-1, -1): (0, 1),
        (0, -1): (0, 2),
        (1, -1): (0, 1),
        (1, 0): (0, 2) }

