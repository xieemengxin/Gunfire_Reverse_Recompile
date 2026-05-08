# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2040.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2040.pyc
# Source Generated with Decompyle++
# File: m2040.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2040
    m_Name = '武器-等级增幅'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51580, 1),
            4: (51580, 2),
            6: (51580, 3),
            8: (51580, 4),
            10: (51580, 5) } }
    m_PointMax = {
        QUALITY_NORMAL: 10 }

