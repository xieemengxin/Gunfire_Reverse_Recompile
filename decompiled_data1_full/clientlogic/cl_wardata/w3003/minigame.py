# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3003/minigame.pyc
# RelativePath: clientlogic/cl_wardata/w3003/minigame.pyc
# Source Generated with Decompyle++
# File: minigame.pyc (Python 3.6)

from cl_minigame.mg_cash import CDropCashGameData
from cl_minigame.mg_bullet import CDropBulletGameData
from cl_minigame.mg_equip import CDropEquipGameData, CRewardChooseEquipGameData, CRewardChooseInitWeaponGameData, CUpgradeChooseWeaponGameData, CRewardSurvivorInitWeaponGameData
from cl_minigame.mg_relic import CDropRelicGameData, CRelicGameData, CRewardChooseRelicGameData, CUpgradeChooseRelicGameData
from cl_item.defines import QUALITY_TYPE_HIGH, QUALITY_TYPE_NORMAL, QUALITY_TYPE_LOW
from cl_minigame.mg_trigger import CDropTriggerGameData
from cl_commondefines import WARRIOR_NORMAL, WARRIOR_OBSTACLE

class CMiniGameData101(CDropCashGameData):
    m_SID = 101
    m_TypeBase = {
        WARRIOR_OBSTACLE: 10,
        WARRIOR_NORMAL: 10 }


class CMiniGameData201(CDropBulletGameData):
    m_SID = 201
    m_BulletBag = {
        2: {
            4503: 300,
            4508: 3,
            4502: 300,
            4504: 300 } }
    m_ChooseWeight = {
        2: 30 }


class CMiniGameData1001(CDropEquipGameData):
    m_SID = 1001
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 5
    m_FlagDifferBullet = 0


class CMiniGameData2001(CDropRelicGameData):
    m_SID = 2001
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5701: 10,
        5709: 10,
        5715: 10,
        5718: 10,
        5728: 10,
        5731: 10,
        5741: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 5
    m_ValidRemove = 0


class CMiniGameData401(CDropTriggerGameData):
    m_SID = 401
    m_ChooseWeight = {
        1604: 10 }

