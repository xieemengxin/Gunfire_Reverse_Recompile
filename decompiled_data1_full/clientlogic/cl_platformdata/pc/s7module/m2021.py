# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2021.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2021.pyc
# Source Generated with Decompyle++
# File: m2021.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2021
    m_Name = '次要技能-灵力回复'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51561, 1),
            4: (51561, 2),
            6: (51561, 3),
            8: (51561, 4) } }
    m_PointMax = {
        QUALITY_NORMAL: 8 }

