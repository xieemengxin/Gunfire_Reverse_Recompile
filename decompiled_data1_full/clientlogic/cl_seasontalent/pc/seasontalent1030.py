# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_seasontalent/pc/seasontalent1030.pyc
# RelativePath: clientlogic/cl_seasontalent/pc/seasontalent1030.pyc
# Source Generated with Decompyle++
# File: seasontalent1030.pyc (Python 3.6)

from cl_commondefines import DICE_PUTOUT_POLL_ONE, VIRTUAL_ITEM_PASSIVE, WAR_UNLOCK_DICEPRESETTEMP, WAR_UNLOCK_DICEPUT

class CSeasonTalent(object):
    m_SID = 1030
    m_Reward = [
        {
            'item': WAR_UNLOCK_DICEPUT,
            'info': {
                'diceinfo': { },
                'speciteminfo': {
                    1001: 1,
                    1017: 1 },
                'dicepool': DICE_PUTOUT_POLL_ONE } },
        {
            'item': WAR_UNLOCK_DICEPRESETTEMP,
            'info': {
                'dicetempinfo': {
                    1001: 1,
                    1002: 1 } } }]
    m_WarReward = ({
        'item': VIRTUAL_ITEM_PASSIVE,
        'info': {
            'sid': 6621,
            'data': { } } },)

