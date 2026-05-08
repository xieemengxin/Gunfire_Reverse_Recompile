# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2005.pyc
# Source Generated with Decompyle++
# File: m2005.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2005
    m_Name = '快速换弹'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            1: (51521, 1),
            3: (51522, 1),
            5: (51523, 1),
            7: (51524, 1),
            8: (51525, 1) } }
    m_PointMax = {
        QUALITY_NORMAL: 3 }

