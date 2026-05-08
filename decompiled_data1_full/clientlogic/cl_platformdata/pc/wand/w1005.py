# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wand/w1005.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wand/w1005.pyc
# Source Generated with Decompyle++
# File: w1005.pyc (Python 3.6)

from cl_wand.mobject import CWandData
from cl_commondefines import WANDTAG_DAMAGE, WANDTAG_WEAPON

class CItem(CWandData):
    m_SID = 1005
    m_Name = '电弧令牌'
    m_Tag = (WANDTAG_WEAPON, WANDTAG_DAMAGE)
    m_LevelInfo = {
        1: (1, ((1010, 2, 0),), 3, ((2022, 1, 0),), (51202,), {
            'ColdTime': 300 }),
        2: (1, ((1010, 2, 0),), 3, ((2022, 2, 0),), (51202,), {
            'ColdTime': 300 }),
        3: (1, ((1010, 2, 0),), 4, ((2022, 3, 0),), (51202,), {
            'ColdTime': 300 }) }
    m_SendWandCnt = True

