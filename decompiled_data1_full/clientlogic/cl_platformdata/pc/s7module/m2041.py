# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2041.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2041.pyc
# Source Generated with Decompyle++
# File: m2041.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2041
    m_Name = '武器-武器等级'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51581, 1),
            4: (51581, 2),
            6: (51581, 3),
            8: (51581, 4) } }
    m_PointMax = {
        QUALITY_NORMAL: 8 }

