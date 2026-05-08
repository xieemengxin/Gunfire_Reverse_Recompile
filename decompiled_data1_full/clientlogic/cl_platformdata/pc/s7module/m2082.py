# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/s7module/m2082.pyc
# RelativePath: clientlogic/cl_platformdata/pc/s7module/m2082.pyc
# Source Generated with Decompyle++
# File: m2082.pyc (Python 3.6)

from cl_seasonplay.season7.module import CModuleData
from cl_commondefines import QUALITY_NORMAL

class CModule(CModuleData):
    m_SID = 2082
    m_Name = '武器-火力升级'
    m_EquipNumMax = 3
    m_QualityConfig = {
        QUALITY_NORMAL: {
            2: (51625, 1),
            4: (51625, 2),
            6: (51625, 3) } }
    m_PointMax = {
        QUALITY_NORMAL: 6 }

