# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3005/minigame.pyc
# RelativePath: clientlogic/cl_wardata/w3005/minigame.pyc
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
from cl_minigame.mg_gscash import CDropGSCashGameData
from cl_minigame.mg_keyitem import CDropKeyItemGameData
from cl_minigame.mg_autoperform import CAutoPerformGameData
from cl_commondefines import NWARRIOR_NPC_LOCKEDBOX, NWARRIOR_NPC_PASSBOX, WARRIOR_BOSS, WARRIOR_ELITE, WARRIOR_NORMAL, WARRIOR_OBSTACLE_NORMAL
from cl_newformula import Func201, Func202, Func205
from cl_item.defines import QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL

class CMiniGameData101(CDropCashGameData):
    m_SID = 101
    m_TypeBase = {
        WARRIOR_BOSS: 6,
        NWARRIOR_NPC_LOCKEDBOX: 80,
        NWARRIOR_NPC_PASSBOX: 40,
        WARRIOR_NORMAL: 6 }


class CMiniGameData102(CDropCashGameData):
    m_SID = 102
    m_TypeBase = {
        WARRIOR_OBSTACLE_NORMAL: 1 }


class CMiniGameData104(CDropCashGameData):
    m_SID = 104
    m_TypeBase = {
        WARRIOR_BOSS: 1,
        WARRIOR_ELITE: 1,
        WARRIOR_NORMAL: 1 }


class CMiniGameData201(CDropBulletGameData):
    m_SID = 201
    m_BulletBag = {
        1: {
            4502: 90 },
        2: {
            4503: 25 },
        3: {
            4504: 8 },
        4: {
            4508: 1 } }
    m_ChooseWeight = {
        1: 15,
        2: 15,
        3: 15,
        4: 10 }


class CMiniGameData202(CDropBulletGameData):
    m_SID = 202
    m_BulletBag = {
        1: {
            4508: 2 } }
    m_ChooseWeight = {
        1: 10 }


class CMiniGameData203(CDropBulletGameData):
    m_SID = 203
    m_BulletBag = {
        1: {
            4508: 1 } }
    m_ChooseWeight = {
        1: 10 }


class CMiniGameData204(CDropBulletGameData):
    m_SID = 204
    m_BulletBag = {
        1: {
            4502: 30 },
        2: {
            4503: 6 },
        3: {
            4504: 2 },
        4: {
            4508: 1 } }
    m_ChooseWeight = {
        1: 15,
        2: 15,
        3: 15,
        4: 25 }


class CMiniGameData205(CDropBulletGameData):
    m_SID = 205
    m_BulletBag = {
        1: {
            4502: 90 },
        2: {
            4503: 25 },
        3: {
            4504: 8 } }
    m_ChooseWeight = {
        1: 15,
        2: 15,
        3: 15 }


class CMiniGameData1001(CDropEquipGameData):
    m_SID = 1001
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 3
    m_FlagDifferBullet = 1


class CMiniGameData1002(CRewardChooseEquipGameData):
    m_SID = 1002
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 0
    m_FlagDifferBullet = 1


class CMiniGameData1003(CRewardChooseInitWeaponGameData):
    m_SID = 1003
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 1
    m_FlagDifferBullet = 1


class CMiniGameData1004(CDropEquipGameData):
    m_SID = 1004
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 1
    m_FlagDifferBullet = 0


class CMiniGameData1005(CDropEquipGameData):
    m_SID = 1005
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 1
    m_FlagDifferBullet = 0


class CMiniGameData1006(CDropEquipGameData):
    m_SID = 1006
    m_ChooseWeight = { }
    m_FilterList = []
    m_PreChooseLen = 3
    m_FlagDifferBullet = 1


class CMiniGameData2104(CDropRelicGameData):
    m_SID = 2104
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5701: 10,
        5704: 10,
        5706: 10,
        5708: 10,
        5709: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5715: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5759: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5767: 10,
        5768: 10,
        5769: 10,
        5776: 10,
        5785: 10,
        5789: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5803: 10,
        5801: 10,
        5804: 10,
        5809: 10,
        5810: 10,
        5821: 10,
        5819: 10,
        5817: 10,
        5824: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = -1


class CMiniGameData2108(CDropRelicGameData):
    m_SID = 2108
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5703: 10,
        5705: 10,
        5707: 10,
        5713: 10,
        5753: 10,
        5716: 10,
        5719: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5732: 10,
        5735: 10,
        5736: 10,
        5740: 10,
        5743: 10,
        5744: 10,
        5745: 10,
        5746: 10,
        5747: 10,
        5748: 10,
        5751: 10,
        5755: 10,
        5756: 10,
        5763: 10,
        5765: 10,
        5766: 10,
        5771: 10,
        5774: 10,
        5775: 8,
        5777: 10,
        5778: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5786: 10,
        5791: 10,
        5792: 10,
        5793: 10,
        5798: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5814: 10,
        5813: 10,
        5811: 10,
        5815: 10,
        5816: 10,
        5820: 10,
        5818: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = -1


class CMiniGameData2112(CDropRelicGameData):
    m_SID = 2112
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5702: 10,
        5717: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5733: 10,
        5734: 10,
        5738: 10,
        5739: 10,
        5741: 10,
        5742: 10,
        5749: 10,
        5750: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5770: 10,
        5772: 10,
        5773: 10,
        5779: 10,
        5780: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5802: 10,
        5812: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = -1


class CMiniGameData2117(CDropRelicGameData):
    m_SID = 2117
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5948: 10,
        5946: 10,
        5939: 10,
        5935: 10,
        5929: 10,
        5928: 10,
        5920: 10,
        5915: 10,
        5909: 10,
        5906: 10,
        5949: 10,
        5950: 10,
        5951: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = -1


class CMiniGameData2401(CDropRelicGameData):
    m_SID = 2401
    m_ChooseQuality = {
        QUALITY_TYPE_HIGH: (lambda *a: 5 + Func201(*a) * 6 + Func202(*a) * 0 + Func205(*a) * 20),
        QUALITY_TYPE_NORMAL: (lambda *a: 130 + Func201(*a) * 2 + Func202(*a) * 0 + Func205(*a) * 11),
        QUALITY_TYPE_LOW: (lambda *a: 180 + Func201(*a) * -7 + Func202(*a) * -0.5 + Func205(*a) * 0) }
    m_ChooseWeight = {
        5701: 10,
        5708: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5753: 10,
        5767: 10,
        5768: 10,
        5785: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5704: 10,
        5769: 10,
        5706: 10,
        5709: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5776: 10,
        5789: 10,
        5713: 10,
        5715: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5740: 10,
        5744: 10,
        5745: 10,
        5748: 10,
        5755: 10,
        5756: 10,
        5759: 10,
        5766: 10,
        5771: 10,
        5786: 10,
        5791: 10,
        5703: 10,
        5732: 10,
        5743: 10,
        5746: 10,
        5765: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5798: 10,
        5705: 10,
        5707: 10,
        5716: 10,
        5719: 10,
        5735: 10,
        5736: 10,
        5747: 10,
        5751: 10,
        5763: 10,
        5774: 10,
        5777: 10,
        5778: 10,
        5792: 10,
        5793: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5738: 10,
        5739: 10,
        5770: 10,
        5772: 10,
        5702: 10,
        5733: 10,
        5734: 10,
        5749: 10,
        5750: 10,
        5773: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5717: 10,
        5741: 10,
        5742: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5775: 10,
        5779: 10,
        5780: 10,
        5801: 10,
        5802: 10,
        5803: 10,
        5804: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5809: 10,
        5810: 10,
        5811: 10,
        5812: 10,
        5813: 10,
        5814: 10,
        5815: 10,
        5816: 10,
        5817: 10,
        5818: 10,
        5819: 10,
        5820: 10,
        5821: 10,
        5824: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = -1


class CMiniGameData2402(CRewardChooseRelicGameData):
    m_SID = 2402
    m_ChooseQuality = {
        QUALITY_TYPE_HIGH: (lambda *a: 5 + Func201(*a) * 6 + Func202(*a) * 0 + Func205(*a) * 20),
        QUALITY_TYPE_NORMAL: (lambda *a: 130 + Func201(*a) * 2 + Func202(*a) * 0 + Func205(*a) * 11),
        QUALITY_TYPE_LOW: (lambda *a: 180 + Func201(*a) * -7 + Func202(*a) * -0.5 + Func205(*a) * 0) }
    m_ChooseWeight = {
        5701: 10,
        5708: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5753: 10,
        5767: 10,
        5768: 10,
        5785: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5704: 10,
        5769: 10,
        5706: 10,
        5709: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5776: 10,
        5789: 10,
        5713: 10,
        5715: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5740: 10,
        5744: 10,
        5745: 10,
        5748: 10,
        5755: 10,
        5756: 10,
        5759: 10,
        5766: 10,
        5771: 10,
        5786: 10,
        5791: 10,
        5703: 10,
        5732: 10,
        5743: 10,
        5746: 10,
        5765: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5798: 10,
        5705: 10,
        5707: 10,
        5716: 10,
        5719: 10,
        5735: 10,
        5736: 10,
        5747: 10,
        5751: 10,
        5763: 10,
        5774: 10,
        5777: 10,
        5778: 10,
        5792: 10,
        5793: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5738: 10,
        5739: 10,
        5770: 10,
        5772: 10,
        5702: 10,
        5733: 10,
        5734: 10,
        5749: 10,
        5750: 10,
        5773: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5717: 10,
        5741: 10,
        5742: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5775: 10,
        5779: 10,
        5780: 10,
        5801: 10,
        5802: 10,
        5803: 10,
        5804: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5809: 10,
        5810: 10,
        5811: 10,
        5812: 10,
        5813: 10,
        5814: 10,
        5815: 10,
        5816: 10,
        5817: 10,
        5818: 10,
        5819: 10,
        5820: 10,
        5821: 10,
        5824: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 4
    m_ValidRemove = -1


class CMiniGameData2403(CRewardChooseRelicGameData):
    m_SID = 2403
    m_ChooseQuality = {
        QUALITY_TYPE_HIGH: (lambda *a: 1 + Func201(*a) * 3 + Func202(*a) * 0 + Func205(*a) * 2),
        QUALITY_TYPE_NORMAL: (lambda *a: 60 + Func201(*a) * 0 + Func202(*a) * 0 + Func205(*a) * 1) }
    m_ChooseWeight = {
        5701: 10,
        5708: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5753: 10,
        5767: 10,
        5768: 10,
        5785: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5704: 10,
        5769: 10,
        5706: 10,
        5709: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5776: 10,
        5789: 10,
        5713: 10,
        5715: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5740: 10,
        5744: 10,
        5745: 10,
        5748: 10,
        5755: 10,
        5756: 10,
        5759: 10,
        5766: 10,
        5771: 10,
        5786: 10,
        5791: 10,
        5703: 10,
        5732: 10,
        5743: 10,
        5746: 10,
        5765: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5798: 10,
        5705: 10,
        5707: 10,
        5716: 10,
        5719: 10,
        5735: 10,
        5736: 10,
        5747: 10,
        5751: 10,
        5763: 10,
        5774: 10,
        5777: 10,
        5778: 10,
        5792: 10,
        5793: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5738: 10,
        5739: 10,
        5770: 10,
        5772: 10,
        5702: 10,
        5733: 10,
        5734: 10,
        5749: 10,
        5750: 10,
        5773: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5717: 10,
        5741: 10,
        5742: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5775: 10,
        5779: 10,
        5780: 10,
        5801: 10,
        5802: 10,
        5803: 10,
        5804: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5809: 10,
        5810: 10,
        5811: 10,
        5812: 10,
        5813: 10,
        5814: 10,
        5815: 10,
        5816: 10,
        5817: 10,
        5818: 10,
        5819: 10,
        5820: 10,
        5821: 10,
        5824: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 4
    m_ValidRemove = -1


class CMiniGameData2404(CDropRelicGameData):
    m_SID = 2404
    m_ChooseQuality = {
        QUALITY_TYPE_LOW: 0,
        QUALITY_TYPE_NORMAL: 0,
        QUALITY_TYPE_HIGH: 100 }
    m_ChooseWeight = {
        5701: 10,
        5708: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5753: 10,
        5767: 10,
        5768: 10,
        5785: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5704: 10,
        5769: 10,
        5706: 10,
        5709: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5776: 10,
        5789: 10,
        5713: 10,
        5715: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5740: 10,
        5744: 10,
        5745: 10,
        5748: 10,
        5755: 10,
        5756: 10,
        5759: 10,
        5766: 10,
        5771: 10,
        5786: 10,
        5791: 10,
        5703: 10,
        5732: 10,
        5743: 10,
        5746: 10,
        5765: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5798: 10,
        5705: 10,
        5707: 10,
        5716: 10,
        5719: 10,
        5735: 10,
        5736: 10,
        5747: 10,
        5751: 10,
        5763: 10,
        5774: 10,
        5777: 10,
        5778: 10,
        5792: 10,
        5793: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5738: 10,
        5739: 10,
        5770: 10,
        5772: 10,
        5702: 10,
        5733: 10,
        5734: 10,
        5749: 10,
        5750: 10,
        5773: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5717: 10,
        5741: 10,
        5742: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5775: 10,
        5779: 10,
        5780: 10,
        5801: 10,
        5802: 10,
        5803: 10,
        5804: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5809: 10,
        5810: 10,
        5811: 10,
        5812: 10,
        5813: 10,
        5814: 10,
        5815: 10,
        5816: 10,
        5817: 10,
        5818: 10,
        5819: 10,
        5820: 10,
        5821: 10,
        5824: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = {
        5701: 10,
        5708: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5753: 10,
        5767: 10,
        5768: 10,
        5785: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5704: 10,
        5769: 10,
        5706: 10,
        5709: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5776: 10,
        5789: 10,
        5713: 10,
        5715: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5740: 10,
        5744: 10,
        5745: 10,
        5748: 10,
        5755: 10,
        5756: 10,
        5759: 10,
        5766: 10,
        5771: 10,
        5786: 10,
        5791: 10,
        5703: 10,
        5732: 10,
        5743: 10,
        5746: 10,
        5765: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5798: 10,
        5705: 10,
        5707: 10,
        5716: 10,
        5719: 10,
        5735: 10,
        5736: 10,
        5747: 10,
        5751: 10,
        5763: 10,
        5774: 10,
        5777: 10,
        5778: 10,
        5792: 10,
        5793: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5738: 10,
        5739: 10,
        5770: 10,
        5772: 10,
        5702: 10,
        5733: 10,
        5734: 10,
        5749: 10,
        5750: 10,
        5773: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5717: 10,
        5741: 10,
        5742: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5775: 10,
        5779: 10,
        5780: 10,
        5801: 10,
        5802: 10,
        5803: 10,
        5804: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5809: 10,
        5810: 10,
        5811: 10,
        5812: 10,
        5813: 10,
        5814: 10,
        5815: 10,
        5816: 10 }
    m_PreChooseLen = 5
    m_ValidRemove = -1


class CMiniGameData2407(CDropRelicGameData):
    m_SID = 2407
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5708: 10,
        5711: 10,
        5716: 10,
        5812: 10,
        5720: 10,
        5723: 10,
        5738: 10,
        5744: 10,
        5747: 10,
        5757: 10,
        5765: 10,
        5777: 10,
        5784: 10,
        5786: 10,
        5798: 10,
        5755: 10,
        5745: 10,
        5802: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = -1


class CMiniGameData2408(CRelicGameData):
    m_SID = 2408
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5701: 10,
        5708: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5753: 10,
        5767: 10,
        5768: 10,
        5785: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5704: 10,
        5769: 10,
        5706: 10,
        5709: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5776: 10,
        5789: 10,
        5713: 10,
        5715: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5740: 10,
        5744: 10,
        5745: 10,
        5748: 10,
        5755: 10,
        5756: 10,
        5759: 10,
        5766: 10,
        5771: 10,
        5786: 10,
        5791: 10,
        5703: 10,
        5732: 10,
        5743: 10,
        5746: 10,
        5765: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5798: 10,
        5705: 10,
        5707: 10,
        5716: 10,
        5719: 10,
        5735: 10,
        5736: 10,
        5747: 10,
        5751: 10,
        5763: 10,
        5774: 10,
        5777: 10,
        5778: 10,
        5792: 10,
        5793: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5738: 10,
        5739: 10,
        5770: 10,
        5772: 10,
        5702: 10,
        5733: 10,
        5734: 10,
        5749: 10,
        5750: 10,
        5773: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5717: 10,
        5741: 10,
        5742: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5775: 10,
        5779: 10,
        5780: 10,
        5801: 10,
        5802: 10,
        5803: 10,
        5804: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5808: 10,
        5809: 10,
        5810: 10,
        5811: 10,
        5812: 10,
        5813: 10,
        5814: 10,
        5815: 10,
        5816: 10,
        5817: 10,
        5818: 10,
        5819: 10,
        5820: 10,
        5821: 10,
        5824: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = 0


class CMiniGameData2409(CRelicGameData):
    m_SID = 2409
    m_ChooseQuality = { }
    m_ChooseWeight = {
        5701: 10,
        5708: 10,
        5710: 10,
        5711: 10,
        5712: 10,
        5753: 10,
        5767: 10,
        5768: 10,
        5785: 10,
        5790: 10,
        5795: 10,
        5796: 10,
        5797: 10,
        5799: 10,
        5704: 10,
        5769: 10,
        5706: 10,
        5709: 10,
        5714: 10,
        5718: 10,
        5727: 10,
        5728: 10,
        5729: 10,
        5754: 10,
        5760: 10,
        5761: 10,
        5762: 10,
        5764: 10,
        5776: 10,
        5789: 10,
        5713: 10,
        5715: 10,
        5723: 10,
        5725: 10,
        5730: 10,
        5731: 10,
        5740: 10,
        5744: 10,
        5745: 10,
        5748: 10,
        5755: 10,
        5756: 10,
        5759: 10,
        5766: 10,
        5771: 10,
        5786: 10,
        5791: 10,
        5703: 10,
        5732: 10,
        5743: 10,
        5746: 10,
        5765: 10,
        5781: 10,
        5782: 10,
        5783: 10,
        5798: 10,
        5705: 10,
        5707: 10,
        5716: 10,
        5719: 10,
        5735: 10,
        5736: 10,
        5747: 10,
        5751: 10,
        5763: 10,
        5774: 10,
        5777: 10,
        5778: 10,
        5792: 10,
        5793: 10,
        5720: 10,
        5724: 10,
        5726: 10,
        5738: 10,
        5739: 10,
        5770: 10,
        5772: 10,
        5702: 10,
        5733: 10,
        5734: 10,
        5749: 10,
        5750: 10,
        5773: 10,
        5784: 10,
        5787: 10,
        5788: 10,
        5794: 10,
        5717: 10,
        5741: 10,
        5742: 10,
        5752: 10,
        5757: 10,
        5758: 10,
        5775: 10,
        5779: 10,
        5780: 10,
        5801: 10,
        5802: 10,
        5803: 10,
        5804: 10,
        5805: 10,
        5806: 10,
        5807: 10,
        5808: 10,
        5809: 10,
        5810: 10,
        5811: 10,
        5812: 10,
        5813: 10,
        5814: 10,
        5815: 10,
        5816: 10,
        5817: 10,
        5818: 10,
        5819: 10,
        5820: 10,
        5821: 10,
        5824: 10,
        5906: 10,
        5909: 10,
        5915: 10,
        5920: 10,
        5928: 10,
        5929: 10,
        5935: 10,
        5939: 10,
        5946: 10,
        5948: 10,
        5949: 10,
        5950: 10,
        5951: 10 }
    m_FilterList = []
    m_ChooseWeightStandby = { }
    m_PreChooseLen = 1
    m_ValidRemove = -1


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
        3101: 1 }


class CMiniGameData3102(CDropKeyGameData):
    m_SID = 3102
    m_KeyBag = {
        3102: 1 }


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
                2225: 10 } },
        104: {
            1: {
                2307: 10,
                2308: 10,
                2309: 10,
                2310: 10,
                2311: 10,
                2312: 10 },
            3: {
                2301: 10,
                2302: 10,
                2303: 10,
                2304: 10,
                2305: 10,
                2306: 10 },
            2: {
                2313: 10,
                2314: 10,
                2315: 10,
                2316: 10,
                2317: 10,
                2318: 10 } },
        105: {
            1: {
                2418: 10,
                2402: 10,
                2403: 10,
                2404: 10,
                2405: 10,
                2406: 10 },
            2: {
                2401: 10,
                2413: 10,
                2414: 10,
                2415: 10,
                2416: 10,
                2417: 10 },
            3: {
                2407: 10,
                2408: 10,
                2409: 10,
                2410: 10,
                2411: 10,
                2412: 10 } },
        108: {
            1: {
                2801: 10,
                2802: 10,
                2803: 10,
                2804: 10,
                2805: 10,
                2806: 10 },
            2: {
                2807: 10,
                2808: 10,
                2809: 10,
                2810: 10,
                2811: 10,
                2812: 10 },
            3: {
                2813: 10,
                2814: 10,
                2815: 10,
                2816: 10,
                2817: 10,
                2818: 10 } },
        109: {
            1: {
                2713: 10,
                2714: 10,
                2715: 10,
                2716: 10,
                2717: 10,
                2718: 10 },
            2: {
                2701: 10,
                2702: 10,
                2703: 10,
                2704: 10,
                2705: 10,
                2706: 10 },
            3: {
                2707: 10,
                2708: 10,
                2709: 10,
                2710: 10,
                2711: 10,
                2712: 10 } } }


class CMiniGameData4101(CRewardGoldenCupGameData):
    m_SID = 4101
    m_ChooseWeight = {
        1027: 10 }


class CMiniGameData4102(CRewardGoldenCupGameData):
    m_SID = 4102
    m_ChooseWeight = {
        1028: 10 }


class CMiniGameData501(CDropGSCashGameData):
    m_SID = 501
    m_TypeBase = {
        WARRIOR_BOSS: 3,
        WARRIOR_ELITE: 2,
        WARRIOR_NORMAL: 1 }


class CMiniGameData6001(CDropKeyItemGameData):
    m_SID = 6001
    m_ChooseWeight = {
        1001: 100 }
    m_Item = {
        1001: {
            6001: 1 } }


class CMiniGameData7001(CAutoPerformGameData):
    m_SID = 7001
    m_ChooseWeight = {
        1630: 100 }

