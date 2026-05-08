# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3002/minigame.pyc
# RelativePath: clientlogic/cl_wardata/w3002/minigame.pyc
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
            4503: 40,
            4508: 1,
            4502: 80 },
        3: {
            4508: 2 } }
    m_ChooseWeight = {
        2: 30,
        3: 20 }


class CMiniGameData202(CDropBulletGameData):
    m_SID = 202
    m_BulletBag = {
        1: {
            4508: 3 } }
    m_ChooseWeight = {
        1: 10 }


class CMiniGameData203(CDropBulletGameData):
    m_SID = 203
    m_BulletBag = {
        1: {
            4502: 1 } }
    m_ChooseWeight = {
        1: 100 }


class CMiniGameData204(CDropBulletGameData):
    m_SID = 204
    m_BulletBag = {
        1: {
            4503: 1 } }
    m_ChooseWeight = {
        1: 100 }


class CMiniGameData205(CDropBulletGameData):
    m_SID = 205
    m_BulletBag = {
        1: {
            4504: 1 } }
    m_ChooseWeight = {
        1: 100 }


class CMiniGameData206(CDropBulletGameData):
    m_SID = 206
    m_BulletBag = {
        1: {
            4508: 1 } }
    m_ChooseWeight = {
        1: 100 }


class CMiniGameData1001(CDropEquipGameData):
    m_SID = 1001
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 5
    m_FlagDifferBullet = 0


class CMiniGameData1002(CDropEquipGameData):
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

