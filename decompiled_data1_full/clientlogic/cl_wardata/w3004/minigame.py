# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3004/minigame.pyc
# RelativePath: clientlogic/cl_wardata/w3004/minigame.pyc
# Source Generated with Decompyle++
# File: minigame.pyc (Python 3.6)

from cl_minigame.mg_cash import CDropCashGameData
from cl_minigame.mg_bullet import CDropBulletGameData
from cl_minigame.mg_equip import CDropEquipGameData, CRewardChooseEquipGameData, CRewardChooseInitWeaponGameData, CUpgradeChooseWeaponGameData, CRewardSurvivorInitWeaponGameData
from cl_minigame.mg_relic import CDropRelicGameData, CRelicGameData, CRewardChooseRelicGameData, CUpgradeChooseRelicGameData
from cl_item.defines import QUALITY_TYPE_HIGH, QUALITY_TYPE_NORMAL, QUALITY_TYPE_LOW
from cl_minigame.mg_trigger import CDropTriggerGameData
from cl_minigame.mg_key import CDropKeyGameData
from cl_minigame.mg_talent import CRewardChooseTalentGameData, CUpgradeChooseTalentGameData, CPhaseChooseTalentGameData, CRewardChooseRareTalentGameData, CDirectRewardRandomTalentGameData
from cl_minigame.mg_goldencup import CRewardGoldenCupGameData
from cl_commondefines import NWARRIOR_NPC_ITEMBOX, NWARRIOR_NPC_LOCKEDBOX, NWARRIOR_NPC_PASSBOX, WARRIOR_NORMAL, WARRIOR_OBSTACLE

class CMiniGameData101(CDropCashGameData):
    m_SID = 101
    m_TypeBase = {
        NWARRIOR_NPC_LOCKEDBOX: 10000,
        NWARRIOR_NPC_PASSBOX: 10000,
        NWARRIOR_NPC_ITEMBOX: 10000,
        WARRIOR_OBSTACLE: 10000,
        WARRIOR_NORMAL: 10000 }


class CMiniGameData201(CDropBulletGameData):
    m_SID = 201
    m_BulletBag = {
        1: {
            4503: 10,
            4504: 10,
            4502: 4 },
        2: {
            4503: 20,
            4504: 20,
            4508: 1,
            4502: 8 } }
    m_ChooseWeight = {
        1: 70,
        2: 30 }


class CMiniGameData1001(CDropEquipGameData):
    m_SID = 1001
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 5
    m_FlagDifferBullet = 0


class CMiniGameData1002(CRewardChooseEquipGameData):
    m_SID = 1002
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 5
    m_FlagDifferBullet = 0


class CMiniGameData2001(CDropRelicGameData):
    m_SID = 2001
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5701: 10,
        5702: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 5
    m_ValidRemove = 0


class CMiniGameData2002(CRewardChooseRelicGameData):
    m_SID = 2002
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5701: 10,
        5702: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 5
    m_ValidRemove = 0


class CMiniGameData401(CDropTriggerGameData):
    m_SID = 401
    m_ChooseWeight = {
        1801: 10 }


class CMiniGameData402(CDropTriggerGameData):
    m_SID = 402
    m_ChooseWeight = {
        1802: 10 }


class CMiniGameData403(CDropTriggerGameData):
    m_SID = 403
    m_ChooseWeight = {
        1803: 10 }


class CMiniGameData404(CDropTriggerGameData):
    m_SID = 404
    m_ChooseWeight = {
        1804: 10 }


class CMiniGameData405(CDropTriggerGameData):
    m_SID = 405
    m_ChooseWeight = {
        1805: 10 }


class CMiniGameData406(CDropTriggerGameData):
    m_SID = 406
    m_ChooseWeight = {
        1806: 10 }


class CMiniGameData407(CDropTriggerGameData):
    m_SID = 407
    m_ChooseWeight = {
        1807: 10 }


class CMiniGameData408(CDropTriggerGameData):
    m_SID = 408
    m_ChooseWeight = {
        1808: 10 }


class CMiniGameData3101(CDropKeyGameData):
    m_SID = 3101
    m_KeyBag = {
        3101: 5 }


class CMiniGameData4001(CRewardChooseTalentGameData):
    m_SID = 4001
    m_ChooseWeight = {
        101: {
            1: {
                2025: 10,
                2026: 10,
                2028: 10,
                2035: 10,
                2036: 10,
                2041: 10 },
            3: {
                2037: 10,
                2038: 10,
                2039: 10,
                2042: 10,
                2043: 10,
                2044: 10 },
            2: {
                2030: 10,
                2031: 10,
                2029: 10,
                2032: 10,
                2033: 10,
                2034: 10 } },
        102: {
            1: {
                2125: 10,
                2126: 10,
                2109: 10,
                2127: 10,
                2111: 10,
                2129: 10 },
            3: {
                2102: 10,
                2103: 10,
                2105: 10,
                2106: 10,
                2104: 10,
                2123: 10 },
            2: {
                2113: 10,
                2130: 10,
                2119: 10,
                2120: 10,
                2116: 10,
                2124: 10 } },
        103: {
            1: {
                2220: 10,
                2202: 10,
                2203: 10,
                2221: 10,
                2205: 10,
                2223: 10 },
            3: {
                2207: 10,
                2208: 10,
                2226: 10,
                2210: 10,
                2227: 10,
                2212: 10 },
            2: {
                2224: 10,
                2214: 10,
                2228: 10,
                2216: 10,
                2222: 10,
                2225: 10 } } }


class CMiniGameData4101(CRewardGoldenCupGameData):
    m_SID = 4101
    m_ChooseWeight = {
        1009: 10 }


class CMiniGameData4102(CRewardGoldenCupGameData):
    m_SID = 4102
    m_ChooseWeight = {
        1010: 10 }

