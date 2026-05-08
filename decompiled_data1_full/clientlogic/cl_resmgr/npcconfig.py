# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_resmgr/npcconfig.pyc
# RelativePath: clientlogic/cl_resmgr/npcconfig.pyc
# Source Generated with Decompyle++
# File: npcconfig.pyc (Python 3.6)

from cl_resmgr.resdata import CNpcData as CCustom
from cl_commondefines import DICE_QUALITY_NORMAL, DICE_QUALITY_RARE, DICE_QUALITY_TALE, INTERACT_RULE_CDTIME, INTERACT_RULE_CHALLENGE, INTERACT_RULE_ENDLESSTIME, INTERACT_RULE_INITWEAPON, INTERACT_RULE_LEVELGOAL, LEVEL_TYPE_BOSS, LEVEL_TYPE_FIGHT, NPC_CON_ALWAYSFALSE, NPC_CON_CHECKENDLESS, NPC_CON_CHECKENDLESSELEMENT, NPC_CON_CHECKHERO, NPC_CON_CHECKLAYERBOSS, NPC_CON_CHECKMODE, NPC_CON_CHECKREGROUPRELICELEMENT, NPC_CON_CYCLEWAR, NPC_CON_UNLOCK4LAYER, NPC_REFRESH_COST_GSCASH, NPC_REFRESH_COST_WARCASH, NWARRIOR_NPC_BENEDICTION, NWARRIOR_NPC_BONFIRE, NWARRIOR_NPC_CANNON, NWARRIOR_NPC_CAR, NWARRIOR_NPC_CONNECTTRANSFER, NWARRIOR_NPC_DICESHOP, NWARRIOR_NPC_ELEVATOR, NWARRIOR_NPC_EVENT, NWARRIOR_NPC_EXCHANGEGOLDENCUP, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_GSCASHSHOP, NWARRIOR_NPC_HOOKROPE, NWARRIOR_NPC_INITBOX, NWARRIOR_NPC_ITEMBOX, NWARRIOR_NPC_LIMITGOLDENCUP, NWARRIOR_NPC_LOCKEDBOX, NWARRIOR_NPC_MAGICBOX, NWARRIOR_NPC_PASSBOX, NWARRIOR_NPC_PETSHOP, NWARRIOR_NPC_PHASEGOLDENCUP, NWARRIOR_NPC_PHASESHOP, NWARRIOR_NPC_PHASESMITH, NWARRIOR_NPC_RAREGOLDENCUP, NWARRIOR_NPC_REFRESH, NWARRIOR_NPC_RELIC, NWARRIOR_NPC_RELICLOTTERY, NWARRIOR_NPC_RELICROLLBOX, NWARRIOR_NPC_ROOMCHALLENGE, NWARRIOR_NPC_S7SHOP, NWARRIOR_NPC_S8SHOP, NWARRIOR_NPC_SHOP, NWARRIOR_NPC_SMITH, NWARRIOR_NPC_TASKNPC, NWARRIOR_NPC_TRANSFER, NWARRIOR_NPC_TRANSFERPOS, NWARRIOR_NPC_WANDSHOP, NWARRIOR_NPC_WEAPONSTORE, PET_QUALITY_NORMAL, PET_QUALITY_RARE, TRANSFER_DIRTO_LAYER, TRANSFER_DIRTO_PASS, VIRTUAL_ITEM_KEY, VIRTUAL_ITEM_KEYITEM, VIRTUAL_ITEM_WARCASH
from math import ceil
from cl_newformula import Func16, Func201, Func202, Func203, Func211, Func212, Func441, Func518, Func678, Func734, Func740
import cl_wardata.npcaction as npcaction

def NpcInitAction1007(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKLAYERBOSS, {
        'Layer': {
            1: 1 },
        'Check': 1 })


def NpcInitAction1009(oNpc):
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_KEY, {
        3101: 1 }, 0)


def NpcInitAction1010(oNpc):
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_KEY, {
        3101: 2 }, 0)


def NpcInitAction1011(oNpc):
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_KEY, {
        3101: 3 }, 0)


def NpcInitAction1018(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_INITWEAPON, { })
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESS, {
        'Check': 0 })


def NpcInitAction1021(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKLAYERBOSS, {
        'Layer': {
            2: 1 },
        'Check': 1 })


def NpcInitAction1023(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_CHALLENGE, { })


def NpcInitAction1024(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_LEVELGOAL, { })


def NpcInitAction1027(oNpc):
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_KEYITEM, {
        6001: 1 }, 0)


def NpcInitAction1028(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_CDTIME, {
        'Time': 1300 })


def NpcInitAction1029(oNpc):
    npcaction.NpcSetTriggerRadius(oNpc, 8)
    npcaction.NpcSetSpeed(oNpc, 2)


def NpcInitAction1031(oNpc):
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_PASS, {
        3: 1 }, 4)
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKLAYERBOSS, {
        'Layer': {
            3: 1 },
        'Check': 1 })


def NpcInitAction1032(oNpc):
    npcaction.NpcSetRefreshFormula(oNpc, 300)
    npcaction.NpcSetInitRefreshFormula(oNpc, 400, NPC_REFRESH_COST_WARCASH)
    npcaction.NpcSetRefreshWarMG(oNpc, {
        1: {
            3001: 30012012 },
        2: {
            3001: 30012012 } })


def NpcInitAction1033(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_LEVELGOAL, { })


def NpcInitAction1034(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_CHALLENGE, { })


def NpcInitAction1036(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKLAYERBOSS, {
        'Layer': {
            1: 1 },
        'Check': 1 })


def NpcInitAction1037(oNpc):
    npcaction.NpcSetGoldenCupTimes(oNpc, 3)


def NpcInitAction1038(oNpc):
    npcaction.NpcSetEventData(oNpc, 1023)


def NpcInitAction1039(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_CHALLENGE, { })


def NpcInitAction1040(oNpc):
    npcaction.NpcSetEventData(oNpc, 1024)


def NpcInitAction1041(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CYCLEWAR, { })
    npcaction.NpcSetRefreshLayer(oNpc, 1, 99, (lambda *a: ceil(min(60, int((10 + Func211(*a) * 10) * Func678(*a) / 100)))))
    npcaction.NpcSetBuyCostFactor(oNpc, (lambda *a: Func678(*a)))


def NpcInitAction1042(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CYCLEWAR, { })


def NpcInitAction1046(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_UNLOCK4LAYER, { })
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_LAYER, {
        3: 1 }, 4)
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKLAYERBOSS, {
        'Layer': {
            3: 1 },
        'Check': 1 })


def NpcInitAction1047(oNpc):
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_PASS, {
        4: 1 }, 4)


def NpcInitAction1048(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_ALWAYSFALSE, { })
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_PASS, {
        4: 1 }, 4)


def NpcInitAction1049(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CYCLEWAR, { })
    npcaction.NpcSetRefreshLayer(oNpc, 1, 99, (lambda *a: ceil((10 + Func211(*a) * 10) * Func678(*a) / 100)))
    npcaction.NpcSetBuyCostFactor(oNpc, (lambda *a: Func678(*a)))


def NpcInitAction1053(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKHERO, {
        'AssignHero': 216 })


def NpcInitAction1054(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_LEVELGOAL, { })
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKMODE, {
        'Mode': 1005 })
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKLAYERBOSS, {
        'Layer': {
            1: 1,
            2: 1,
            3: 1 },
        'Check': 0 })


def NpcInitAction1059(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESS, {
        'Check': 1 })


def NpcInitAction1061(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESS, {
        'Check': 1 })
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_LAYER, {
        1: 1 }, 4)
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_ENDLESSTIME, { })


def NpcInitAction1062(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESS, {
        'Check': 1 })
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_LAYER, {
        1: 1 }, 4)
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_ENDLESSTIME, { })


def NpcInitAction1063(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESS, {
        'Check': 1 })
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_LAYER, {
        2: 1 }, 4)
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_ENDLESSTIME, { })


def NpcInitAction1064(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESS, {
        'Check': 1 })
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_LAYER, {
        1: 1,
        2: 1,
        3: 1,
        4: 1 }, 4)
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_ENDLESSTIME, { })


def NpcInitAction1065(oNpc):
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_PASS, {
        3: 1,
        1: 1,
        2: 1,
        4: 1 }, 4)
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESSELEMENT, {
        'Check': 1 })
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKLAYERBOSS, {
        'Layer': {
            1: 1,
            2: 1,
            3: 1 },
        'Check': 0 })


def NpcInitAction1066(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKENDLESSELEMENT, {
        'Check': 1 })
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_LAYER, {
        4: 1 }, 4)
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_ENDLESSTIME, { })


def NpcInitAction1067(oNpc):
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_LAYER, {
        4: 1 }, 4)
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_ALWAYSFALSE, { })
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_ENDLESSTIME, { })


def NpcInitAction1068(oNpc):
    npcaction.NpcSetSellPrice(oNpc, (lambda *a: min(700, Func201(*a) * 120 + Func202(*a) * 30 + 40) * Func203(*a) * Func16(*a, **{
'a': 0.45,
'b': 0.5 })), {
        PET_QUALITY_RARE: 150,
        PET_QUALITY_NORMAL: 100 })


def NpcInitAction1069(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKREGROUPRELICELEMENT, { })


def NpcInitAction1071(oNpc):
    npcaction.NpcSetVisibleCondition(oNpc, NPC_CON_CHECKREGROUPRELICELEMENT, { })
    npcaction.NpcSetRelicLotteryInitData(oNpc, {
        1: 60,
        2: 40,
        3: 0 }, {
        1: 30,
        2: 60,
        3: 10 }, {
        1: 15,
        2: 45,
        3: 40 }, {
        1: 5,
        2: 25,
        3: 70 }, (lambda *a: 100 - (80 + Func518(*a, **{
'sAttr': 'AntiLotteryClose' })) / 2 ** (Func734(*a) - 1 - Func740(*a))), 2405)


def NpcInitAction1072(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 4,
        'MaxLevel': 5 })


def NpcInitAction1073(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 4,
        'MaxLevel': 5 })
    npcaction.NpcSetDiceShopNpcInitData(oNpc, 4, {
        'Init': {
            DICE_QUALITY_TALE: 12,
            DICE_QUALITY_RARE: 6,
            DICE_QUALITY_NORMAL: 4 },
        'Ratio': {
            DICE_QUALITY_TALE: {
                1: 20,
                2: 60 },
            DICE_QUALITY_RARE: {
                1: 20,
                2: 60 },
            DICE_QUALITY_NORMAL: {
                1: 20,
                2: 60 } },
        'Threshold': {
            DICE_QUALITY_TALE: 2,
            DICE_QUALITY_RARE: 2,
            DICE_QUALITY_NORMAL: 2 } }, {
        1: {
            LEVEL_TYPE_FIGHT: {
                1: 4 },
            LEVEL_TYPE_BOSS: {
                2: 2,
                1: 2 } },
        2: {
            LEVEL_TYPE_FIGHT: {
                2: 4 },
            LEVEL_TYPE_BOSS: {
                3: 2,
                2: 2 } },
        3: {
            LEVEL_TYPE_FIGHT: {
                3: 2,
                2: 2 },
            LEVEL_TYPE_BOSS: {
                3: 4 } },
        4: {
            LEVEL_TYPE_FIGHT: {
                3: 4 },
            LEVEL_TYPE_BOSS: {
                3: 4 } } }, 0, {
        1: {
            1: DICE_QUALITY_NORMAL },
        2: {
            1: DICE_QUALITY_RARE },
        3: {
            1: DICE_QUALITY_TALE },
        4: {
            1: DICE_QUALITY_TALE } }, {
        1: {
            1: DICE_QUALITY_RARE },
        2: {
            1: DICE_QUALITY_TALE },
        3: {
            1: DICE_QUALITY_TALE },
        4: {
            1: DICE_QUALITY_TALE } }, { })


def NpcInitAction1074(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 4,
        'MaxLevel': 3 })
    npcaction.NpcSetS7ShopNpcInitData(oNpc, 1, (lambda *a: ((Func201(*a) - 1) * 50 + Func202(*a) * 10) * Func16(*a, **{
'a': 0.9,
'b': 1 })), 1, (lambda *a: ((Func201(*a) - 1) * 50 + Func202(*a) * 10) * Func16(*a, **{
'a': 0.9,
'b': 1 })), 3, 1, 1, (lambda *a: ((Func201(*a) - 1) * 50 + Func202(*a) * 10) * Func16(*a, **{
'a': 0.9,
'b': 1 })), {
        3: {
            1050: 100 },
        4: {
            1050: 100 } }, {
        1: {
            0: {
                1200: 100 },
            1: {
                1201: 100 },
            5: {
                1211: 100 },
            2: {
                1201: 100 },
            3: {
                1201: 100 },
            4: {
                1201: 100 } },
        2: {
            1: {
                1202: 100 },
            4: {
                1214: 100 },
            2: {
                1202: 100 },
            3: {
                1202: 100 } },
        3: {
            1: {
                1203: 100 },
            4: {
                1215: 10 },
            2: {
                1203: 100 },
            3: {
                1203: 100 } },
        4: {
            1: {
                1204: 100 },
            3: {
                1216: 100 },
            2: {
                1204: 100 } } }, {
        1: {
            0: {
                1001: 100 },
            1: {
                1002: 100 },
            2: {
                1002: 100 },
            3: {
                1002: 100 },
            4: {
                1002: 100 },
            5: {
                1003: 100 } },
        2: {
            1: {
                1002: 100 },
            2: {
                1002: 100 },
            3: {
                1002: 100 },
            4: {
                1003: 100 } },
        3: {
            1: {
                1002: 100 },
            2: {
                1002: 100 },
            3: {
                1002: 100 },
            4: {
                1003: 100 } },
        4: {
            1: {
                1002: 100 },
            2: {
                1002: 100 },
            3: {
                1003: 100 } } })


def NpcInitAction1075(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 4,
        'MaxLevel': 5 })
    npcaction.NpcSetS8ShopNpcInitData(oNpc, 0, 0, {
        1: {
            (0, 1): {
                1001: 100 },
            (5, 1): {
                1002: 100 } },
        2: {
            (4, 1): {
                1003: 100 } },
        3: {
            (4, 1): {
                1003: 100 } },
        4: {
            (3, 1): {
                1003: 100 } } }, {
        1: {
            (0, 1): {
                1051: 100 },
            (5, 1): {
                1051: 100 },
            (4, 1): {
                1051: 100 },
            (3, 1): {
                1051: 100 },
            (2, 1): {
                1051: 100 },
            (1, 1): {
                1051: 100 } },
        2: {
            (0, 1): {
                1051: 100 },
            (4, 1): {
                1051: 100 },
            (3, 1): {
                1051: 100 },
            (2, 1): {
                1051: 100 },
            (1, 1): {
                1051: 100 } },
        3: {
            (0, 1): {
                1051: 100 },
            (4, 1): {
                1051: 100 },
            (3, 1): {
                1051: 100 },
            (2, 1): {
                1051: 100 },
            (1, 1): {
                1051: 100 } },
        4: {
            (0, 1): {
                1051: 100 },
            (3, 1): {
                1051: 100 },
            (2, 1): {
                1051: 100 },
            (1, 1): {
                1051: 100 } } })


def NpcInitAction1101(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1101)


def NpcInitAction1102(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1102)


def NpcInitAction1103(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1103)


def NpcInitAction1104(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1104)


def NpcInitAction1105(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1105)


def NpcInitAction1106(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1106)


def NpcInitAction1107(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1107)


def NpcInitAction1108(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1108)


def NpcInitAction1109(oNpc):
    npcaction.NpcSetEventData(oNpc, 1109)


def NpcInitAction1110(oNpc):
    npcaction.NpcSetEventData(oNpc, 1110)


def NpcInitAction1111(oNpc):
    npcaction.NpcSetEventData(oNpc, 1111)


def NpcInitAction1112(oNpc):
    npcaction.NpcSetEventData(oNpc, 1112)


def NpcInitAction1113(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 1113)


def NpcInitAction2001(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2001)


def NpcInitAction2002(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2002)


def NpcInitAction2003(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2003)


def NpcInitAction2004(oNpc):
    npcaction.NpcSetEventData(oNpc, 2004)


def NpcInitAction2005(oNpc):
    npcaction.NpcSetEventData(oNpc, 2005)


def NpcInitAction2006(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2006)


def NpcInitAction2007(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2007)


def NpcInitAction2008(oNpc):
    npcaction.NpcSetEventData(oNpc, 2008)


def NpcInitAction2009(oNpc):
    npcaction.NpcSetEventData(oNpc, 2009)


def NpcInitAction2010(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2010)


def NpcInitAction2011(oNpc):
    npcaction.NpcSetEventData(oNpc, 2011)


def NpcInitAction2012(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2012)


def NpcInitAction2013(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2013)


def NpcInitAction2014(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2014)


def NpcInitAction2015(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2015)


def NpcInitAction2101(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2101)


def NpcInitAction2102(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2102)


def NpcInitAction2103(oNpc):
    npcaction.NpcSetEventData(oNpc, 2103)


def NpcInitAction2104(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2104)


def NpcInitAction2105(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2105)


def NpcInitAction2106(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2106)


def NpcInitAction2107(oNpc):
    npcaction.NpcSetEventData(oNpc, 2107)


def NpcInitAction2108(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2108)


def NpcInitAction2109(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetRefreshFormula(oNpc, (lambda *a: 20 * 1.3 ** Func211(*a) + 40))
    npcaction.NpcSetInitRefreshFormula(oNpc, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 75 })), NPC_REFRESH_COST_WARCASH)
    npcaction.NpcSetArgValue(oNpc, 'RewardDelay', 150)
    npcaction.NpcSetRefreshWarMG(oNpc, {
        1: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3010: 30102401,
            3012: 30122401 },
        2: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401 },
        3: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401 } })


def NpcInitAction2110(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2110)


def NpcInitAction2111(oNpc):
    npcaction.NpcSetArgValue(oNpc, 'RefreshTimes', 0)
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_WARCASH, {
        0: (lambda *a: 20 * 1.1 ** Func212(*a, **{
'sAttr': 'RefreshTimes' }) + 50) }, 1)


def NpcInitAction2112(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2112)


def NpcInitAction2113(oNpc):
    npcaction.NpcSetEventData(oNpc, 2113)


def NpcInitAction2114(oNpc):
    npcaction.NpcSetEventData(oNpc, 2114)


def NpcInitAction2115(oNpc):
    npcaction.NpcSetEventData(oNpc, 2115)


def NpcInitAction2116(oNpc):
    npcaction.NpcSetEventData(oNpc, 2116)


def NpcInitAction2117(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2117)


def NpcInitAction2118(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2118)


def NpcInitAction2119(oNpc):
    npcaction.NpcSetEventData(oNpc, 2119)


def NpcInitAction2120(oNpc):
    npcaction.NpcSetEventData(oNpc, 2120)


def NpcInitAction2121(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2121)


def NpcInitAction2122(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2122)


def NpcInitAction2123(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2123)


def NpcInitAction2201(oNpc):
    npcaction.NpcSetEventData(oNpc, 2201)


def NpcInitAction2202(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2202)


def NpcInitAction2203(oNpc):
    npcaction.NpcSetRefreshFormula(oNpc, (lambda *a: ceil((Func678(*a) / 100) * (20 * 1.3 ** Func211(*a) + 14))))
    npcaction.NpcSetInitRefreshFormula(oNpc, (lambda *a: ceil((1 + Func201(*a) * 0 + Func202(*a) * 0) * Func16(*a, **{
'a': 60,
'b': 80 }) * Func678(*a) / 100)), NPC_REFRESH_COST_GSCASH)
    npcaction.NpcSetArgValue(oNpc, 'RewardDelay', 150)
    npcaction.NpcSetArgValue(oNpc, 'RelicLevel', 2)
    npcaction.NpcSetRefreshWarMG(oNpc, {
        1: {
            3001: 30012407,
            3007: 30072407,
            3020: 30202407 },
        2: {
            3001: 30012407,
            3007: 30072407,
            3020: 30202407 },
        3: {
            3001: 30012407,
            3007: 30072407,
            3020: 30202407 } })
    npcaction.NpcSetArgValue(oNpc, 'RefreshCnt', 15)


def NpcInitAction2204(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2204)


def NpcInitAction2205(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2205)


def NpcInitAction2206(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2206)


def NpcInitAction2207(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetEventData(oNpc, 2201)


def NpcInitAction2301(oNpc):
    npcaction.NpcSetEventData(oNpc, 2301)


def NpcInitAction2302(oNpc):
    npcaction.NpcSetEventData(oNpc, 2302)


def NpcInitAction3001(oNpc):
    npcaction.NpcSetFormulaArgsLimit(oNpc, {
        'MaxLayer': 6,
        'MaxLevel': 4 })
    npcaction.NpcSetRefreshFormula(oNpc, (lambda *a: 20 * 1.3 ** Func211(*a) + 40))
    npcaction.NpcSetInitRefreshFormula(oNpc, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 75 })), NPC_REFRESH_COST_WARCASH)
    npcaction.NpcSetArgValue(oNpc, 'RewardDelay', 150)
    npcaction.NpcSetRefreshWarMG(oNpc, {
        1: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3010: 30102401,
            3012: 30122401 },
        2: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401 },
        3: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401 } })


def NpcInitAction3101(oNpc):
    npcaction.NpcSetEventData(oNpc, 3101)


def NpcInitAction3102(oNpc):
    npcaction.NpcSetEventData(oNpc, 3102)


def NpcInitAction3103(oNpc):
    npcaction.NpcSetEventData(oNpc, 3103)


def NpcInitAction3105(oNpc):
    npcaction.NpcSetEventData(oNpc, 3105)


def NpcInitAction3109(oNpc):
    npcaction.NpcSetRefreshFormula(oNpc, (lambda *a: 15 * 1.3 ** Func211(*a) + 15))
    npcaction.NpcSetInitRefreshFormula(oNpc, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 35,
'b': 45 })), NPC_REFRESH_COST_WARCASH)
    npcaction.NpcSetArgValue(oNpc, 'RewardDelay', 150)
    npcaction.NpcSetRefreshWarMG(oNpc, {
        1: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3010: 30102401,
            3012: 30122401,
            3020: 30202401,
            3030: 30302401 },
        2: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401,
            3020: 30202401,
            3030: 30302401 },
        3: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401,
            3020: 30202401,
            3030: 30302401 } })


def NpcInitAction3112(oNpc):
    npcaction.NpcSetEventData(oNpc, 3112)


def NpcInitAction3113(oNpc):
    npcaction.NpcSetEventData(oNpc, 3113)


def NpcInitAction3115(oNpc):
    npcaction.NpcSetEventData(oNpc, 3115)


def NpcInitAction3116(oNpc):
    npcaction.NpcSetEventData(oNpc, 3116)


def NpcInitAction3117(oNpc):
    npcaction.NpcSetEventData(oNpc, 3117)


def NpcInitAction3118(oNpc):
    npcaction.NpcSetEventData(oNpc, 3118)


def NpcInitAction3119(oNpc):
    npcaction.NpcSetEventData(oNpc, 3119)


def NpcInitAction3121(oNpc):
    npcaction.NpcSetEventData(oNpc, 3121)


def NpcInitAction3122(oNpc):
    npcaction.NpcSetEventData(oNpc, 3122)


def NpcInitAction3201(oNpc):
    npcaction.NpcSetEventData(oNpc, 3201)


def NpcInitAction3202(oNpc):
    npcaction.NpcSetEventData(oNpc, 3202)


def NpcInitAction3203(oNpc):
    npcaction.NpcSetEventData(oNpc, 3203)


def NpcInitAction3205(oNpc):
    npcaction.NpcSetEventData(oNpc, 3205)


def NpcInitAction3209(oNpc):
    npcaction.NpcSetRefreshFormula(oNpc, (lambda *a: 15 * 1.3 ** Func211(*a) + 15))
    npcaction.NpcSetInitRefreshFormula(oNpc, (lambda *a: (1.5 + Func441(*a) * 0.2) * Func16(*a, **{
'a': 35,
'b': 45 })), NPC_REFRESH_COST_WARCASH)
    npcaction.NpcSetArgValue(oNpc, 'RewardDelay', 150)
    npcaction.NpcSetRefreshWarMG(oNpc, {
        1: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3010: 30102401,
            3012: 30122401,
            3020: 30202401,
            3030: 30302401 },
        2: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401,
            3020: 30202401,
            3030: 30302401 },
        3: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401,
            3012: 30122401,
            3020: 30202401,
            3030: 30302401 } })


def NpcInitAction3212(oNpc):
    npcaction.NpcSetEventData(oNpc, 3212)


def NpcInitAction3213(oNpc):
    npcaction.NpcSetEventData(oNpc, 3213)


def NpcInitAction3215(oNpc):
    npcaction.NpcSetEventData(oNpc, 3215)


def NpcInitAction3216(oNpc):
    npcaction.NpcSetEventData(oNpc, 3216)


def NpcInitAction3217(oNpc):
    npcaction.NpcSetEventData(oNpc, 3217)


def NpcInitAction3218(oNpc):
    npcaction.NpcSetEventData(oNpc, 3218)


def NpcInitAction3221(oNpc):
    npcaction.NpcSetEventData(oNpc, 3223)


def NpcInitAction3222(oNpc):
    npcaction.NpcSetEventData(oNpc, 3222)


def NpcInitAction3223(oNpc):
    npcaction.NpcSetEventData(oNpc, 3223)


def NpcInitAction3224(oNpc):
    npcaction.NpcSetEventData(oNpc, 3224)


def NpcInitAction4001(oNpc):
    npcaction.NpcSetEventData(oNpc, 4001)


def NpcInitAction4002(oNpc):
    npcaction.NpcSetEventData(oNpc, 4002)


def NpcInitAction4003(oNpc):
    npcaction.NpcSetEventData(oNpc, 4003)


def NpcInitAction4004(oNpc):
    npcaction.NpcSetEventData(oNpc, 4004)


def NpcInitAction4005(oNpc):
    npcaction.NpcSetEventData(oNpc, 4005)


def NpcInitAction4006(oNpc):
    npcaction.NpcSetEventData(oNpc, 4006)


def NpcInitAction4007(oNpc):
    npcaction.NpcSetEventData(oNpc, 4007)


def NpcInitAction4008(oNpc):
    npcaction.NpcSetEventData(oNpc, 4008)


def NpcInitAction4009(oNpc):
    npcaction.NpcSetRefreshFormula(oNpc, (lambda *a: -20 * 1.3 ** Func211(*a) - 40))
    npcaction.NpcSetInitRefreshFormula(oNpc, (lambda *a: (0.1 + Func201(*a) * 1.5 + Func202(*a) * 0.3) * Func16(*a, **{
'a': 65,
'b': 75 }) * -1), NPC_REFRESH_COST_WARCASH)
    npcaction.NpcSetArgValue(oNpc, 'RewardDelay', 150)
    npcaction.NpcSetRefreshWarMG(oNpc, {
        1: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401 },
        2: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401 },
        3: {
            3001: 30012401,
            3005: 30052401,
            3008: 30082401,
            3007: 30072401,
            3009: 30092401 } })


def NpcInitAction4010(oNpc):
    npcaction.NpcSetEventData(oNpc, 4010)


def NpcInitAction4011(oNpc):
    npcaction.NpcSetEventData(oNpc, 4011)


def NpcInitAction4012(oNpc):
    npcaction.NpcSetEventData(oNpc, 4012)


def NpcInitAction4013(oNpc):
    npcaction.NpcSetEventData(oNpc, 4013)


def NpcInitAction4014(oNpc):
    npcaction.NpcSetEventData(oNpc, 4014)


def NpcInitAction4015(oNpc):
    npcaction.NpcSetEventData(oNpc, 4015)


def NpcInitAction4101(oNpc):
    npcaction.NpcSetEventData(oNpc, 4101)


def NpcInitAction4102(oNpc):
    npcaction.NpcSetEventData(oNpc, 4102)


def NpcInitAction4103(oNpc):
    npcaction.NpcSetEventData(oNpc, 4103)


def NpcInitAction4104(oNpc):
    npcaction.NpcSetEventData(oNpc, 4104)


def NpcInitAction4105(oNpc):
    npcaction.NpcSetEventData(oNpc, 4105)


def NpcInitAction5001(oNpc):
    npcaction.NpcSetArgValue(oNpc, 'RefreshTimes', 0)
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_WARCASH, {
        0: (lambda *a: 20 * 1.1 ** Func212(*a, **{
'sAttr': 'RefreshTimes' }) + 50) }, 1)


def NpcInitAction5002(oNpc):
    npcaction.AddExtraInteractRule(oNpc, INTERACT_RULE_CHALLENGE, { })


def NpcInitAction5003(oNpc):
    npcaction.NpcSetArgValue(oNpc, 'RefreshTimes', 0)
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_WARCASH, {
        0: (lambda *a: 20 * 1.1 ** Func212(*a, **{
'sAttr': 'RefreshTimes' }) + 50) }, 1)


def NpcInitAction6003(oNpc):
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_PASS, { }, 4)


def NpcInitAction6006(oNpc):
    npcaction.NpcSetTransferDir(oNpc, TRANSFER_DIRTO_PASS, { }, 4)


def NpcInitAction9001(oNpc):
    npcaction.NpcSetEventData(oNpc, 9001)


def NpcInitAction9002(oNpc):
    npcaction.NpcSetEventData(oNpc, 9002)


def NpcInitAction9003(oNpc):
    npcaction.NpcSetEventData(oNpc, 9003)


def NpcInitAction9004(oNpc):
    npcaction.NpcSetEventData(oNpc, 9004)


def NpcInitAction9005(oNpc):
    npcaction.NpcSetEventData(oNpc, 9005)


def NpcInitAction9006(oNpc):
    npcaction.NpcSetEventData(oNpc, 9006)


class CNpcData1001(CCustom):
    m_Shape = 4001
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1002(CCustom):
    m_Shape = 4001
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1003(CCustom):
    m_Shape = 4002
    m_FightType = NWARRIOR_NPC_PASSBOX
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1004(CCustom):
    m_Shape = 4007
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 20
    m_InitFunc = None


class CNpcData1005(CCustom):
    m_Shape = 4003
    m_FightType = NWARRIOR_NPC_SHOP
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1006(CCustom):
    m_Shape = 4002
    m_FightType = NWARRIOR_NPC_ITEMBOX
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1007(CCustom):
    m_Shape = 4010
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = NpcInitAction1007


class CNpcData1008(CCustom):
    m_Shape = 4005
    m_FightType = NWARRIOR_NPC_GOLDENCUP
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1009(CCustom):
    m_Shape = 4002
    m_FightType = NWARRIOR_NPC_LOCKEDBOX
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1009


class CNpcData1010(CCustom):
    m_Shape = 4002
    m_FightType = NWARRIOR_NPC_LOCKEDBOX
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1010


class CNpcData1011(CCustom):
    m_Shape = 4002
    m_FightType = NWARRIOR_NPC_LOCKEDBOX
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1011


class CNpcData1012(CCustom):
    m_Shape = 4009
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1013(CCustom):
    m_Shape = 5519
    m_FightType = NWARRIOR_NPC_SMITH
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1014(CCustom):
    m_Shape = 4025
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1015(CCustom):
    m_Shape = 4012
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1016(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_ITEMBOX
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1017(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_MAGICBOX
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1018(CCustom):
    m_Shape = 4011
    m_FightType = NWARRIOR_NPC_INITBOX
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1018


class CNpcData1019(CCustom):
    m_Shape = 4016
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1020(CCustom):
    m_Shape = 4026
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1021(CCustom):
    m_Shape = 4021
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = NpcInitAction1021


class CNpcData1022(CCustom):
    m_Shape = 4022
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 15
    m_InitFunc = None


class CNpcData1023(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_MAGICBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1023


class CNpcData1024(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_MAGICBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1024


class CNpcData1025(CCustom):
    m_Shape = 5528
    m_FightType = NWARRIOR_NPC_BONFIRE
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1026(CCustom):
    m_Shape = 4015
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1027(CCustom):
    m_Shape = 4023
    m_FightType = NWARRIOR_NPC_CANNON
    m_InteractDis = 10
    m_InitFunc = NpcInitAction1027


class CNpcData1028(CCustom):
    m_Shape = 4024
    m_FightType = NWARRIOR_NPC_ELEVATOR
    m_InteractDis = 10
    m_InitFunc = NpcInitAction1028


class CNpcData1029(CCustom):
    m_Shape = 5529
    m_FightType = NWARRIOR_NPC_CAR
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1029


class CNpcData1030(CCustom):
    m_Shape = 4017
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1031(CCustom):
    m_Shape = 4018
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1031


class CNpcData1032(CCustom):
    m_Shape = 4003
    m_FightType = NWARRIOR_NPC_REFRESH
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1032


class CNpcData1033(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_MAGICBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1033


class CNpcData1034(CCustom):
    m_Shape = 4002
    m_FightType = NWARRIOR_NPC_ITEMBOX
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1034


class CNpcData1035(CCustom):
    m_Shape = 4019
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1036(CCustom):
    m_Shape = 4020
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 10
    m_InitFunc = NpcInitAction1036


class CNpcData1037(CCustom):
    m_Shape = 4005
    m_FightType = NWARRIOR_NPC_GOLDENCUP
    m_InteractDis = 4
    m_InitFunc = NpcInitAction1037


class CNpcData1038(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1038


class CNpcData1039(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_MAGICBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1039


class CNpcData1040(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1040


class CNpcData1041(CCustom):
    m_Shape = 4027
    m_FightType = NWARRIOR_NPC_BENEDICTION
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1041


class CNpcData1042(CCustom):
    m_Shape = 4028
    m_FightType = NWARRIOR_NPC_GSCASHSHOP
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1042


class CNpcData1043(CCustom):
    m_Shape = 4031
    m_FightType = NWARRIOR_NPC_TRANSFERPOS
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1044(CCustom):
    m_Shape = 4029
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = None


class CNpcData1045(CCustom):
    m_Shape = 4030
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1046(CCustom):
    m_Shape = 4032
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1046


class CNpcData1047(CCustom):
    m_Shape = 4030
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1047


class CNpcData1048(CCustom):
    m_Shape = 4030
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1048


class CNpcData1049(CCustom):
    m_Shape = 4033
    m_FightType = NWARRIOR_NPC_BENEDICTION
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1049


class CNpcData1050(CCustom):
    m_Shape = 4034
    m_FightType = NWARRIOR_NPC_LIMITGOLDENCUP
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1051(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_MAGICBOX
    m_InteractDis = 8
    m_InitFunc = None


class CNpcData1052(CCustom):
    m_Shape = 4035
    m_FightType = NWARRIOR_NPC_RAREGOLDENCUP
    m_InteractDis = 4
    m_InitFunc = None


class CNpcData1053(CCustom):
    m_Shape = 4036
    m_FightType = NWARRIOR_NPC_RELIC
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1053


class CNpcData1054(CCustom):
    m_Shape = 4037
    m_FightType = NWARRIOR_NPC_WEAPONSTORE
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1054


class CNpcData1055(CCustom):
    m_Shape = 4038
    m_FightType = NWARRIOR_NPC_TASKNPC
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1056(CCustom):
    m_Shape = 4003
    m_FightType = NWARRIOR_NPC_PHASESHOP
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1057(CCustom):
    m_Shape = 5519
    m_FightType = NWARRIOR_NPC_PHASESMITH
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1058(CCustom):
    m_Shape = 4005
    m_FightType = NWARRIOR_NPC_PHASEGOLDENCUP
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1059(CCustom):
    m_Shape = 5546
    m_FightType = NWARRIOR_NPC_BONFIRE
    m_InteractDis = 6
    m_InitFunc = NpcInitAction1059


class CNpcData1060(CCustom):
    m_Shape = 7003
    m_FightType = NWARRIOR_NPC_EXCHANGEGOLDENCUP
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData1061(CCustom):
    m_Shape = 4020
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 10
    m_InitFunc = NpcInitAction1061


class CNpcData1062(CCustom):
    m_Shape = 4010
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = NpcInitAction1062


class CNpcData1063(CCustom):
    m_Shape = 4021
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 6
    m_InitFunc = NpcInitAction1063


class CNpcData1064(CCustom):
    m_Shape = 4018
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1064


class CNpcData1065(CCustom):
    m_Shape = 4030
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction1065


class CNpcData1066(CCustom):
    m_Shape = 4018
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 10
    m_InitFunc = NpcInitAction1066


class CNpcData1067(CCustom):
    m_Shape = 4018
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 10
    m_InitFunc = NpcInitAction1067


class CNpcData1068(CCustom):
    m_Shape = 4041
    m_FightType = NWARRIOR_NPC_PETSHOP
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1068


class CNpcData1069(CCustom):
    m_Shape = 4042
    m_FightType = NWARRIOR_NPC_RELICROLLBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1069


class CNpcData1071(CCustom):
    m_Shape = 4042
    m_FightType = NWARRIOR_NPC_RELICLOTTERY
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1071


class CNpcData1072(CCustom):
    m_Shape = 4043
    m_FightType = NWARRIOR_NPC_WANDSHOP
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1072


class CNpcData1073(CCustom):
    m_Shape = 4044
    m_FightType = NWARRIOR_NPC_DICESHOP
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1073


class CNpcData1074(CCustom):
    m_Shape = 4045
    m_FightType = NWARRIOR_NPC_S7SHOP
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1074


class CNpcData1075(CCustom):
    m_Shape = 4045
    m_FightType = NWARRIOR_NPC_S8SHOP
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1075


class CNpcData1101(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1101


class CNpcData1102(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1102


class CNpcData1103(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1103


class CNpcData1104(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1104


class CNpcData1105(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1105


class CNpcData1106(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1106


class CNpcData1107(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1107


class CNpcData1108(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1108


class CNpcData1109(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1109


class CNpcData1110(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1110


class CNpcData1111(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1111


class CNpcData1112(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1112


class CNpcData1113(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction1113


class CNpcData2001(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2001


class CNpcData2002(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2002


class CNpcData2003(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2003


class CNpcData2004(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2004


class CNpcData2005(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2005


class CNpcData2006(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2006


class CNpcData2007(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2007


class CNpcData2008(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2008


class CNpcData2009(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2009


class CNpcData2010(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2010


class CNpcData2011(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2011


class CNpcData2012(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2012


class CNpcData2013(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2013


class CNpcData2014(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2014


class CNpcData2015(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2015


class CNpcData2101(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2101


class CNpcData2102(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2102


class CNpcData2103(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2103


class CNpcData2104(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2104


class CNpcData2105(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2105


class CNpcData2106(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2106


class CNpcData2107(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2107


class CNpcData2108(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2108


class CNpcData2109(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_REFRESH
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2109


class CNpcData2110(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2110


class CNpcData2111(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_LOCKEDBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2111


class CNpcData2112(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2112


class CNpcData2113(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2113


class CNpcData2114(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2114


class CNpcData2115(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2115


class CNpcData2116(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2116


class CNpcData2117(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2117


class CNpcData2118(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2118


class CNpcData2119(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2119


class CNpcData2120(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2120


class CNpcData2121(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2121


class CNpcData2122(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2122


class CNpcData2123(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2123


class CNpcData2201(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2201


class CNpcData2202(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2202


class CNpcData2203(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_REFRESH
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2203


class CNpcData2204(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2204


class CNpcData2205(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2205


class CNpcData2206(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2206


class CNpcData2207(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2207


class CNpcData2301(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2301


class CNpcData2302(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction2302


class CNpcData3001(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_REFRESH
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3001


class CNpcData3101(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3101


class CNpcData3102(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3102


class CNpcData3103(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3103


class CNpcData3105(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3105


class CNpcData3109(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_REFRESH
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3109


class CNpcData3112(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3112


class CNpcData3113(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3113


class CNpcData3115(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3115


class CNpcData3116(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3116


class CNpcData3117(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3117


class CNpcData3118(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3118


class CNpcData3119(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3119


class CNpcData3121(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3121


class CNpcData3122(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3122


class CNpcData3201(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3201


class CNpcData3202(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3202


class CNpcData3203(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3203


class CNpcData3205(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3205


class CNpcData3209(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_REFRESH
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3209


class CNpcData3212(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3212


class CNpcData3213(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3213


class CNpcData3215(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3215


class CNpcData3216(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3216


class CNpcData3217(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3217


class CNpcData3218(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3218


class CNpcData3221(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3221


class CNpcData3222(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3222


class CNpcData3223(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3223


class CNpcData3224(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction3224


class CNpcData4001(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4001


class CNpcData4002(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4002


class CNpcData4003(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4003


class CNpcData4004(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4004


class CNpcData4005(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4005


class CNpcData4006(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4006


class CNpcData4007(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4007


class CNpcData4008(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4008


class CNpcData4009(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_REFRESH
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4009


class CNpcData4010(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4010


class CNpcData4011(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4011


class CNpcData4012(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4012


class CNpcData4013(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4013


class CNpcData4014(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4014


class CNpcData4015(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4015


class CNpcData4101(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4101


class CNpcData4102(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4102


class CNpcData4103(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4103


class CNpcData4104(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4104


class CNpcData4105(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction4105


class CNpcData5001(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_LOCKEDBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction5001


class CNpcData5002(CCustom):
    m_Shape = 4002
    m_FightType = NWARRIOR_NPC_ROOMCHALLENGE
    m_InteractDis = 5
    m_InitFunc = NpcInitAction5002


class CNpcData5003(CCustom):
    m_Shape = 4004
    m_FightType = NWARRIOR_NPC_LOCKEDBOX
    m_InteractDis = 5
    m_InitFunc = NpcInitAction5003


class CNpcData6001(CCustom):
    m_Shape = 6967
    m_FightType = NWARRIOR_NPC_CONNECTTRANSFER
    m_InteractDis = 50
    m_InitFunc = None


class CNpcData6002(CCustom):
    m_Shape = 6968
    m_FightType = NWARRIOR_NPC_CONNECTTRANSFER
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData6003(CCustom):
    m_Shape = 7000
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction6003


class CNpcData6004(CCustom):
    m_Shape = 6981
    m_FightType = NWARRIOR_NPC_CONNECTTRANSFER
    m_InteractDis = 50
    m_InitFunc = None


class CNpcData6005(CCustom):
    m_Shape = 6982
    m_FightType = NWARRIOR_NPC_CONNECTTRANSFER
    m_InteractDis = 5
    m_InitFunc = None


class CNpcData6006(CCustom):
    m_Shape = 7002
    m_FightType = NWARRIOR_NPC_TRANSFER
    m_InteractDis = 8
    m_InitFunc = NpcInitAction6006


class CNpcData7001(CCustom):
    m_Shape = 4040
    m_FightType = NWARRIOR_NPC_HOOKROPE
    m_InteractDis = 99
    m_InitFunc = None


class CNpcData9001(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction9001


class CNpcData9002(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction9002


class CNpcData9003(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction9003


class CNpcData9004(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction9004


class CNpcData9005(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction9005


class CNpcData9006(CCustom):
    m_Shape = 4014
    m_FightType = NWARRIOR_NPC_EVENT
    m_InteractDis = 5
    m_InitFunc = NpcInitAction9006

