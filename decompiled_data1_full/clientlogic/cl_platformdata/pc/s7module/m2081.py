# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2081.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2081.pyc
# Source Generated with Decompyle++
# File: m2081.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2081
    m_Name = '武器-等级增幅'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51624, 1),
            4: (51624, 2),
            6: (51624, 3),
            8: (51624, 4),
            10: (51624, 5) } }
    m_PointMax = {
        QUALITY_NORMAL: 10 }

