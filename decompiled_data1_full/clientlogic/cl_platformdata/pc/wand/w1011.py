# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wand/w1011.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wand/w1011.pyc
# Source Generated with Decompyle++
# File: w1011.pyc (Python 3.6)

from cl_wand.mobject import CWandData
from cl_commondefines import WANDTAG_DAMAGE

class CItem(CWandData):
    m_SID = 1011
    m_Name = '流星令牌'
    m_Tag = (WANDTAG_DAMAGE,)
    m_LevelInfo = {
        1: (1, (), 4, ((2027, 1, 1),), (51210,), {
            'ColdTime': 400 }),
        2: (1, (), 5, ((2027, 2, 1),), (51210,), {
            'ColdTime': 400 }),
        3: (1, (), 6, ((2027, 3, 1),), (51210,), {
            'ColdTime': 400 }) }
    m_SendWandCnt = True

