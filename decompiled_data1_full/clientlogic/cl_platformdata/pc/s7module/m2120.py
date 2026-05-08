# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2120.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2120.pyc
# Source Generated with Decompyle++
# File: m2120.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2120
    m_Name = '通用-双生模仿'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51665, 1),
            4: (51665, 2),
            6: (51665, 3) } }
    m_PointMax = {
        QUALITY_NORMAL: 6 }
    m_DefaultPoint = 4

