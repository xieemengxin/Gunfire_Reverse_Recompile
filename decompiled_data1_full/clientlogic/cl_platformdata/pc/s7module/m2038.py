# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2038.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2038.pyc
# Source Generated with Decompyle++
# File: m2038.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2038
    m_Name = '移速-速度优势'
    m_EquipNumMax = 2
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51578, 1),
            4: (51578, 2),
            6: (51578, 3),
            8: (51578, 4) } }
    m_PointMax = {
        QUALITY_NORMAL: 8 }

