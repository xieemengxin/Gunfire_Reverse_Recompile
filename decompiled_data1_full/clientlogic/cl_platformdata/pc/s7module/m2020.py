# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2020.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2020.pyc
# Source Generated with Decompyle++
# File: m2020.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2020
    m_Name = '次要技能-灵力膨胀'
    m_EquipNumMax = 2
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51560, 1),
            4: (51560, 2),
            6: (51560, 3) } }
    m_PointMax = {
        QUALITY_NORMAL: 6 }

