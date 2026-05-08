# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_cscommondef/cs_notify.pyc
# RelativePath: clientlogic/cl_cscommondef/cs_notify.pyc
# Source Generated with Decompyle++
# File: cs_notify.pyc (Python 3.6)

NOTIFY_STYLE_LEVELNORMAL = 101
NOTIFY_STYLE_LEVELPREPARE = 102
NOTIFY_STYLE_LEVELBOSS = 103
NOTIFY_ICON_LEVEL = {
    1: 10205,
    2: 10206,
    3: 10207,
    4: 10208,
    5: 10209,
    'boss': 10210 }
NUM_CN = {
    0: '零',
    1: '一',
    2: '二',
    3: '三',
    4: '四',
    5: '五',
    6: '六',
    7: '七',
    8: '八',
    9: '九' }
ROUND_CN = {
    1: '普通',
    2: '精英',
    3: '噩梦' }
CYCLE_CN = {
    1: '轮回第一层',
    2: '轮回第二层',
    3: '轮回第三层',
    4: '轮回第四层',
    5: '轮回第五层',
    6: '轮回第六层',
    7: '轮回第七层',
    8: '轮回第八层' }

def GetNumCN(iNum):
    if iNum in NUM_CN:
        return NUM_CN[iNum]
    return ''


def GetRoundInfoCN(iRound, iCycle):
    if iCycle > 0:
        return CYCLE_CN.get(iCycle, '')
    if iRound in ROUND_CN:
        return ROUND_CN[iRound]
    return ''

