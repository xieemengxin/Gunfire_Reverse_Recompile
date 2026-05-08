# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3011/minigame.pyc
# RelativePath: clientlogic/cl_wardata/w3011/minigame.pyc
# Source Generated with Decompyle++
# File: minigame.pyc (Python 3.6)

from cl_minigame.mg_cash import CDropCashGameData
from cl_minigame.mg_bullet import CDropBulletGameData
from cl_minigame.mg_equip import CDropEquipGameData, CRewardChooseEquipGameData, CRewardChooseInitWeaponGameData, CUpgradeChooseWeaponGameData, CRewardSurvivorInitWeaponGameData
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
        1: {
            4503: 20,
            4508: 1,
            4502: 60,
            4504: 10 } }
    m_ChooseWeight = {
        1: 100 }


class CMiniGameData202(CDropBulletGameData):
    m_SID = 202
    m_BulletBag = {
        1: {
            4502: 60 } }
    m_ChooseWeight = {
        1: 100 }


class CMiniGameData1001(CDropEquipGameData):
    m_SID = 1001
    m_ChooseWeight = {
        1002: 1 }
    m_FilterList = []
    m_PreChooseLen = 5
    m_FlagDifferBullet = 0


class CMiniGameData1002(CDropEquipGameData):
    m_SID = 1002
    m_ChooseWeight = {
        1002: 1 }
    m_FilterList = []
    m_PreChooseLen = 5
    m_FlagDifferBullet = 0


class CMiniGameData1003(CDropEquipGameData):
    m_SID = 1003
    m_ChooseWeight = {
        1002: 1 }
    m_FilterList = []
    m_PreChooseLen = 5
    m_FlagDifferBullet = 0


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

