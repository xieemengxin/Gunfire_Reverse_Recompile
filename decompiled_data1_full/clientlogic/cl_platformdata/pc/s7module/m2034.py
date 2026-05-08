# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2034.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2034.pyc
# Source Generated with Decompyle++
# File: m2034.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2034
    m_Name = '移速-弹射骰子'
    m_EquipNumMax = 1
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51574, 1),
            4: (51574, 2),
            6: (51574, 3),
            8: (51574, 4),
            10: (51574, 5) } }
    m_PointMax = {
        QUALITY_NORMAL: 10 }

