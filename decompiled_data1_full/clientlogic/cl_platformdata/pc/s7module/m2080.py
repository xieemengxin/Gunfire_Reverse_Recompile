# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2080.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2080.pyc
# Source Generated with Decompyle++
# File: m2080.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2080
    m_Name = '次要技能-次要消耗'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51622, 1),
            4: (51622, 2),
            6: (51622, 3),
            8: (51622, 4) } }
    m_PointMax = {
        QUALITY_NORMAL: 8 }

