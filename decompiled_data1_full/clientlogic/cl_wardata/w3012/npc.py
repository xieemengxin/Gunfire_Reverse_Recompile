# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3012/npc.pyc
# RelativePath: clientlogic/cl_wardata/w3012/npc.pyc
# Source Generated with Decompyle++
# File: npc.pyc (Python 3.6)

from cl_resmgr.resdata import CNpcData as CCustom
import cl_wardata.npcaction as npcaction
import cl_resmgr.npcconfig as baseconfig
from cl_commondefines import NPC_ACTION_ITEMBOX, NPC_ACTION_MAPCHOOSE, NPC_ACTION_SETTLELEVEL, NPC_ACTION_SHOP, OBTAIN_CASH, OBTAIN_WARCASH, VIRTUAL_ITEM_WARCASH
from cl_newformula import Func16, Func201, Func202, Func203, Func204, Func205, Func212, Func219

def NpcAction1001(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1002(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1003(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101,
        3: 4101 }, 150, {
        'OffsetY': 1.5 })
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 5 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 5 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            101: {
                'Prop': 10000,
                'Times': 5 },
            201: {
                'Prop': 10000,
                'Times': 3 } } }, 142)


def NpcAction1004(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1005(oNpc, who):
    npcaction.NpcGoodsConfig(oNpc, who, 0, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 50 + Func202(*a) * 5), 1007, 0, { })
    npcaction.NpcGoodsConfig(oNpc, who, 1, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 60 + Func202(*a) * 5), 1001, 0, { })
    npcaction.NpcGoodsConfig(oNpc, who, 2, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 60 + Func202(*a) * 5), 1008, 0, { })
    npcaction.NpcGoodsEquip(oNpc, who, 3, 100, 1, (lambda *a: 40 + Func201(*a) * 120 + Func202(*a) * 30), {
        1: 1001,
        2: 1001,
        3: 1001 }, 0, OBTAIN_WARCASH, 0, { })
    npcaction.NpcGoodsEquip(oNpc, who, 4, 100, 1, (lambda *a: 40 + Func201(*a) * 120 + Func202(*a) * 30), {
        1: 1001,
        2: 1001,
        3: 1001 }, 0, OBTAIN_WARCASH, 0, { })
    npcaction.NpcGoodsRelic(oNpc, who, 5, 0, 1, OBTAIN_WARCASH, (lambda *a: (Func201(*a) * 120 + Func202(*a) * 30 + 40) * Func203(*a) * Func16(*a, **{
'a': 0.9,
'b': 1 })), {
        1: 2401,
        2: 2401,
        3: 2401 }, 0, 1, { }, None)
    npcaction.NpcGoodsEquip(oNpc, who, 5, 100, 1, (lambda *a: 40 + Func201(*a) * 120 + Func202(*a) * 30), {
        1: 1001,
        2: 1001,
        3: 1001 }, 0, OBTAIN_WARCASH, 0, { })
    npcaction.NpcGoodsConfig(oNpc, who, 6, 100, 0, OBTAIN_CASH, 0, 1002, 0, { })
    npcaction.NpcGoodsEquip(oNpc, who, 7, 100, 1, (lambda *a: 40 + Func201(*a) * 120 + Func202(*a) * 30), {
        1: 1001,
        2: 1001,
        3: 1001 }, 1, OBTAIN_WARCASH, 0, { })
    npcaction.NpcGoodsRelic(oNpc, who, 8, 100, 1, OBTAIN_WARCASH, (lambda *a: (Func201(*a) * 120 + Func202(*a) * 30 + 40) * Func203(*a) * Func16(*a, **{
'a': 0.9,
'b': 1 })), {
        1: 2401,
        2: 2401,
        3: 2401 }, 1, 1, { }, None)
    npcaction.NpcGoodsEquip(oNpc, who, 8, 100, 1, (lambda *a: 40 + Func201(*a) * 120 + Func202(*a) * 30), {
        1: 1001,
        2: 1001,
        3: 1001 }, 1, OBTAIN_WARCASH, 0, { })
    npcaction.NpcGoodsRelife(oNpc, who, 9, 100, 1, OBTAIN_WARCASH, (lambda *a: 150 * (1 + (Func201(*a) - 1) * 1.6 + (Func202(*a) - 1) * 0.25) * (1 + (Func204(*a) - 1) * 0.1) * (1 + (Func205(*a) - 1) * 0.15)))
    npcaction.NpcGoodsRelife(oNpc, who, 10, 100, 1, OBTAIN_WARCASH, (lambda *a: 150 * (1 + (Func201(*a) - 1) * 1.6 + (Func202(*a) - 1) * 0.25) * (1 + (Func204(*a) - 1) * 0.1) * (1 + (Func205(*a) - 1) * 0.15)))
    npcaction.NpcGoodsRelife(oNpc, who, 11, 100, 1, OBTAIN_WARCASH, (lambda *a: 150 * (1 + (Func201(*a) - 1) * 1.6 + (Func202(*a) - 1) * 0.25) * (1 + (Func204(*a) - 1) * 0.1) * (1 + (Func205(*a) - 1) * 0.15)))


def NpcAction1006(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101,
        3: 4101 }, 150, {
        'OffsetY': 1.5 })
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 7 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 7 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            101: {
                'Prop': 10000,
                'Times': 7 },
            201: {
                'Prop': 10000,
                'Times': 3 } } }, 142)


def NpcAction1007(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 3 },
            401: {
                'Prop': 10000,
                'Times': 1 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 3 },
            401: {
                'Prop': 10000,
                'Times': 1 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            101: {
                'Prop': 10000,
                'Times': 3 },
            401: {
                'Prop': 10000,
                'Times': 1 },
            201: {
                'Prop': 10000,
                'Times': 3 } } }, 130)


def NpcAction1008(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 4 },
            401: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 4 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 4 },
            401: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 4 } },
        3: {
            101: {
                'Prop': 10000,
                'Times': 4 },
            401: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 4 } } }, 130)


def NpcAction1009(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 5 },
            401: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 5 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 5 },
            401: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 5 } },
        3: {
            101: {
                'Prop': 10000,
                'Times': 5 },
            401: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 5 } } }, 130)


def NpcAction1010(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2001: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2001: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2001: {
                'Prop': 10000,
                'Times': 1 } } }, 142)


def NpcAction1011(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2009: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 3 },
            4101: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2010: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 3 },
            4101: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2010: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 3 },
            4101: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1012(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1013(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 3001,
        2: 3001,
        3: 3001 }, None, { })


def NpcAction1014(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } } }, 130)


def NpcAction1015(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 8000,
                'Times': 1 },
            1001: {
                'Prop': 8000,
                'Times': 1 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 8000,
                'Times': 1 },
            1001: {
                'Prop': 8000,
                'Times': 1 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 8000,
                'Times': 1 },
            1001: {
                'Prop': 8000,
                'Times': 1 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } } }, 130)


def NpcAction1016(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 10000,
                'Times': 1 },
            1001: {
                'Prop': 10000,
                'Times': 2 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 10000,
                'Times': 1 },
            1001: {
                'Prop': 10000,
                'Times': 2 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            401: {
                'Prop': 3000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            101: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 10000,
                'Times': 1 },
            1001: {
                'Prop': 10000,
                'Times': 2 },
            202: {
                'Prop': 10000,
                'Times': 3 },
            203: {
                'Prop': 10000,
                'Times': 3 },
            204: {
                'Prop': 10000,
                'Times': 3 },
            205: {
                'Prop': 10000,
                'Times': 3 } } }, 130)


def NpcAction1017(oNpc, who):
    npcaction.NpcTransferHideLevel(oNpc, who)


def NpcAction1019(oNpc, who):
    npcaction.NpcTransferHideLevel(oNpc, who)


def NpcAction1020(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1021(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2009: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2010: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2010: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1022(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1023(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 1002,
        2: 1002,
        3: 1002 }, 0, {
        3: 100 }, 150)


def NpcAction1024(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2006,
        2: 2007,
        3: 2007 }, 0, {
        3: 100 }, 150)


def NpcAction1025(oNpc, who):
    npcaction.NpcSetInteractDone(oNpc, who, 0, 1, 0)
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 1003,
        2: 1003,
        3: 1003 }, 0, {
        3: 100 }, 150)


def NpcAction1026(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            401: {
                'Prop': 3000,
                'Times': 1 },
            2009: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 5 } },
        2: {
            401: {
                'Prop': 3000,
                'Times': 1 },
            2010: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 5 } },
        3: {
            401: {
                'Prop': 3000,
                'Times': 1 },
            2010: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 5 } } }, 130)


def NpcAction1027(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4001,
        2: 4001,
        3: 4001 }, 0, { })


def NpcAction1028(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4001,
        2: 4001,
        3: 4001 }, 0, {
        'OnlyCore': 1 })


def NpcAction1029(oNpc, who):
    npcaction.NpcSetInteractDone(oNpc, who, 0, 1, 1)
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101,
        3: 4101 }, 142, {
        'OffsetY': 1.5 })


def NpcAction1030(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2006,
        2: 2007,
        3: 2007 }, 0, {
        3: 100 }, 150)


def NpcAction1031(oNpc, who):
    npcaction.NpcSetInteractDone(oNpc, who, 0, 1, 1)
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101,
        3: 4101 }, 130, {
        'OffsetY': 1.5 })


def NpcAction1032(oNpc, who):
    npcaction.NpcSetInteractDone(oNpc, who, 0, 1, 1)
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2009: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2010: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2010: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1033(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1034(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2006,
        2: 2007,
        3: 2007 }, 0, {
        3: 100 }, 150)


def NpcAction1035(oNpc, who):
    npcaction.NpcSetInteractDone(oNpc, who, 0, 1, 1)
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101,
        3: 4101 }, 142, {
        'OffsetY': 1.5 })


def NpcAction1036(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1037(oNpc, who):
    npcaction.NpcTriggerClientBehavior(oNpc, who, 51, 0, 1)
    npcaction.NpcDisableSceneMonsterPassive(oNpc, who, 39051, 4089, 40)


def NpcAction1038(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            1001: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            1001: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            1001: {
                'Prop': 10000,
                'Times': 2 },
            201: {
                'Prop': 10000,
                'Times': 3 } } }, 130)


def NpcAction1039(oNpc, who):
    npcaction.NpcTriggerClientBehavior(oNpc, who, 49, 0, 1)


def NpcAction1040(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1041(oNpc, who):
    npcaction.NpcTriggerClientBehavior(oNpc, who, 39, 0, 1)


def NpcAction1042(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1043(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101,
        3: 4101 }, 200, {
        'OffsetY': 1.5 })
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 3 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 3 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            101: {
                'Prop': 10000,
                'Times': 3 },
            201: {
                'Prop': 10000,
                'Times': 3 } } }, 142)


def NpcAction1044(oNpc, who):
    npcaction.NpcTransferHideLevel(oNpc, who)


def NpcAction1045(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1046(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1047(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4001,
        2: 4001,
        3: 4001 }, 0, { })


def NpcAction1048(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4103,
        2: 4103,
        3: 4103 }, 142, { })


def NpcAction1050(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101,
        3: 4101 }, 150, {
        'OffsetY': 1.5 })
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 12 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 12 },
            201: {
                'Prop': 10000,
                'Times': 3 } },
        3: {
            101: {
                'Prop': 10000,
                'Times': 12 },
            201: {
                'Prop': 10000,
                'Times': 3 } } }, 142)


def NpcAction1054(oNpc, who):
    npcaction.NpcGoodsEquip(oNpc, who, 0, 100, 1, (lambda *a: Func201(*a) * 20 + Func202(*a) * 5), {
        3: 1006 }, 0, OBTAIN_CASH, 1, { })
    npcaction.NpcGoodsEquip(oNpc, who, 1, 100, 1, (lambda *a: Func201(*a) * 20 + Func202(*a) * 5), {
        3: 1006 }, 0, OBTAIN_CASH, 1, { })
    npcaction.NpcGoodsRelic(oNpc, who, 2, 100, 1, OBTAIN_CASH, (lambda *a: Func219(*a)), {
        3: 2407 }, 0, 2, { }, None)
    npcaction.NpcGoodsRelic(oNpc, who, 3, 100, 1, OBTAIN_CASH, (lambda *a: Func219(*a)), {
        3: 2407 }, 0, 2, { }, None)


def NpcAction1099(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1201(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1202(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1203(oNpc, who):
    npcaction.NpcAddTargetState(oNpc, who, 1165, 100)


def NpcAction1301(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1302(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)
    npcaction.NpcCancelCheckDistance(oNpc, who, 1)


def NpcAction1405(oNpc, who):
    npcaction.NpcVoteNextLayer(oNpc, who, 1, 3000, 500)


def NpcAction1501(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2103: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2103: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2103: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1502(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2101: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2101: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2101: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1503(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2102: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2102: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2102: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1504(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2107: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2107: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2107: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1505(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2105: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2105: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2105: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1506(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2106: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2106: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2106: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1507(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2101: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2101: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2101: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1508(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2102: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2102: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2102: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1509(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2208,
        2: 2208,
        3: 2208 }, 0, {
        3: 100 }, 150)


def NpcAction1510(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2208,
        2: 2208,
        3: 2208 }, 0, {
        3: 100 }, 150)


def NpcAction1511(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2204,
        2: 2204,
        3: 2204 }, 0, {
        3: 100 }, 150)


def NpcAction1512(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2212,
        2: 2212,
        3: 2212 }, 0, {
        3: 100 }, 150)


def NpcAction1513(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2105: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2105: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2105: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1514(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2401: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2401: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2401: {
                'Prop': 10000,
                'Times': 1 } } }, 150)


def NpcAction1515(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2401: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2401: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2401: {
                'Prop': 10000,
                'Times': 1 } } }, 150)


def NpcAction1516(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2402,
        2: 2402,
        3: 2402 }, 0, {
        3: 100 }, 150)


def NpcAction1517(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2402,
        2: 2402,
        3: 2402 }, 0, {
        3: 100 }, 150)


def NpcAction1518(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2403,
        2: 2403,
        3: 2403 }, 0, {
        3: 100 }, 150)


def NpcAction5001(oNpc, who):
    npcaction.NpcWeightRewardGroup(oNpc, who, {
        1: 1001,
        2: 1002,
        3: 1003 }, 0, {
        'RepeatReward': 1 })
    npcaction.NpcSetArgValue(oNpc, 'RefreshTimes', npcaction.NpcGetArgValue(oNpc, 'RefreshTimes') + 1)
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_WARCASH, {
        0: (lambda *a: 20 * 1.1 ** Func212(*a, **{
'sAttr': 'RefreshTimes' }) + 50) }, 1)


def NpcAction5002(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2401: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 5 },
            1001: {
                'Prop': 500,
                'Times': 1 } },
        2: {
            2401: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 5 },
            1001: {
                'Prop': 500,
                'Times': 1 } },
        3: {
            2401: {
                'Prop': 10000,
                'Times': 1 } } }, 200)


def NpcAction5003(oNpc, who):
    npcaction.NpcWeightRewardGroup(oNpc, who, {
        1: 1004 }, 0, {
        'RepeatReward': 1 })
    npcaction.NpcSetArgValue(oNpc, 'RefreshTimes', npcaction.NpcGetArgValue(oNpc, 'RefreshTimes') + 1)
    npcaction.NpcSetOpenCost(oNpc, VIRTUAL_ITEM_WARCASH, {
        0: (lambda *a: 20 * 1.1 ** Func212(*a, **{
'sAttr': 'RefreshTimes' }) + 50) }, 1)


def NpcAction9100(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2401: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2401: {
                'Prop': 10000,
                'Times': 1 } },
        3: {
            2401: {
                'Prop': 10000,
                'Times': 1 } } }, 150)


def NpcAction9101(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2402,
        2: 2402,
        3: 2402 }, 0, {
        3: 100 }, 150)


class CNpcData1001(baseconfig.CNpcData1001):
    m_SID = 1001
    m_Name = '关卡传送门'
    m_Info = {
        'Action': NpcAction1001,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1002(baseconfig.CNpcData1002):
    m_SID = 1002
    m_Name = '结算传送门'
    m_Info = {
        'Action': NpcAction1002,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1003(baseconfig.CNpcData1003):
    m_SID = 1003
    m_Name = '【第一幕】通关金爵宝箱'
    m_Info = {
        'Action': NpcAction1003,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1004(baseconfig.CNpcData1004):
    m_SID = 1004
    m_Name = '大厅传送门'
    m_Info = {
        'Action': NpcAction1004,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1005(baseconfig.CNpcData1005):
    m_SID = 1005
    m_Name = '商店'
    m_Info = {
        'Action': NpcAction1005,
        'ActionType': NPC_ACTION_SHOP }


class CNpcData1006(baseconfig.CNpcData1003):
    m_SID = 1006
    m_Name = '【第二幕】通关金爵宝箱'
    m_Info = {
        'Action': NpcAction1006,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1007(baseconfig.CNpcData1003):
    m_SID = 1007
    m_Name = '1-3宝箱'
    m_Info = {
        'Action': NpcAction1007,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1008(baseconfig.CNpcData1003):
    m_SID = 1008
    m_Name = '1-4宝箱'
    m_Info = {
        'Action': NpcAction1008,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1009(baseconfig.CNpcData1003):
    m_SID = 1009
    m_Name = '1-5宝箱'
    m_Info = {
        'Action': NpcAction1009,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1010(baseconfig.CNpcData1006):
    m_SID = 1010
    m_Name = '通用宝箱'
    m_Info = {
        'Action': NpcAction1010,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1011(baseconfig.CNpcData1003):
    m_SID = 1011
    m_Name = '1-6宝箱'
    m_Info = {
        'Action': NpcAction1011,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1012(baseconfig.CNpcData1007):
    m_SID = 1012
    m_Name = 'BOSS关传送门'
    m_Info = {
        'Action': NpcAction1012,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1013(baseconfig.CNpcData1008):
    m_SID = 1013
    m_Name = '属性卷轴'
    m_Info = {
        'Action': NpcAction1013,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1014(baseconfig.CNpcData1009):
    m_SID = 1014
    m_Name = '铜宝箱'
    m_Info = {
        'Action': NpcAction1014,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1015(baseconfig.CNpcData1010):
    m_SID = 1015
    m_Name = '银宝箱'
    m_Info = {
        'Action': NpcAction1015,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1016(baseconfig.CNpcData1011):
    m_SID = 1016
    m_Name = '金宝箱'
    m_Info = {
        'Action': NpcAction1016,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1017(baseconfig.CNpcData1012):
    m_SID = 1017
    m_Name = '进隐藏关传送门'
    m_Info = {
        'Action': NpcAction1017,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1018(baseconfig.CNpcData1013):
    m_SID = 1018
    m_Name = '工匠'
    m_Info = { }


class CNpcData1019(baseconfig.CNpcData1019):
    m_SID = 1019
    m_Name = '进二幕隐藏关传送门'
    m_Info = {
        'Action': NpcAction1019,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1020(baseconfig.CNpcData1020):
    m_SID = 1020
    m_Name = '出隐藏关传送门'
    m_Info = {
        'Action': NpcAction1020,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1021(baseconfig.CNpcData1006):
    m_SID = 1021
    m_Name = '隐藏关-通用宝箱'
    m_Info = {
        'Action': NpcAction1021,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1022(baseconfig.CNpcData1021):
    m_SID = 1022
    m_Name = '二幕出隐藏关传送门'
    m_Info = {
        'Action': NpcAction1022,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1023(baseconfig.CNpcData1017):
    m_SID = 1023
    m_Name = '武器魔盒3选1'
    m_Info = {
        'Action': NpcAction1023,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1024(baseconfig.CNpcData1024):
    m_SID = 1024
    m_Name = '隐藏关-遗物魔盒3选1'
    m_Info = {
        'Action': NpcAction1024,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1025(baseconfig.CNpcData1018):
    m_SID = 1025
    m_Name = '初始武器魔盒'
    m_Info = {
        'Action': NpcAction1025,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1026(baseconfig.CNpcData1023):
    m_SID = 1026
    m_Name = '隐藏关-挑战触发宝箱'
    m_Info = {
        'Action': NpcAction1026,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1027(baseconfig.CNpcData1008):
    m_SID = 1027
    m_Name = '普通天赋金爵'
    m_Info = {
        'Action': NpcAction1027,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1028(baseconfig.CNpcData1008):
    m_SID = 1028
    m_Name = '核心天赋金爵'
    m_Info = {
        'Action': NpcAction1028,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1029(baseconfig.CNpcData1003):
    m_SID = 1029
    m_Name = '掉落普通天赋金爵的宝箱'
    m_Info = {
        'Action': NpcAction1029,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1030(baseconfig.CNpcData1023):
    m_SID = 1030
    m_Name = '挑战关三选一宝箱'
    m_Info = {
        'Action': NpcAction1030,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1031(baseconfig.CNpcData1023):
    m_SID = 1031
    m_Name = '挑战关金爵宝箱'
    m_Info = {
        'Action': NpcAction1031,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1032(baseconfig.CNpcData1006):
    m_SID = 1032
    m_Name = '低级遗物通关宝箱'
    m_Info = {
        'Action': NpcAction1032,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1033(baseconfig.CNpcData1026):
    m_SID = 1033
    m_Name = '1-5关卡传送门'
    m_Info = {
        'Action': NpcAction1033,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1034(baseconfig.CNpcData1017):
    m_SID = 1034
    m_Name = '隐藏关-通用遗物魔盒3选1'
    m_Info = {
        'Action': NpcAction1034,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1035(baseconfig.CNpcData1006):
    m_SID = 1035
    m_Name = '掉落普通天赋金爵的宝箱'
    m_Info = {
        'Action': NpcAction1035,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1036(baseconfig.CNpcData1019):
    m_SID = 1036
    m_Name = '出二幕隐藏关传送门'
    m_Info = {
        'Action': NpcAction1036,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1037(baseconfig.CNpcData1027):
    m_SID = 1037
    m_Name = '三幕BOSS破盾NPC'
    m_Info = {
        'Action': NpcAction1037,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1038(baseconfig.CNpcData1003):
    m_SID = 1038
    m_Name = '1-6宝箱2'
    m_Info = {
        'Action': NpcAction1038,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1039(baseconfig.CNpcData1029):
    m_SID = 1039
    m_Name = '护送目标'
    m_Info = {
        'Action': NpcAction1039,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1040(baseconfig.CNpcData1030):
    m_SID = 1040
    m_Name = '组队关传送门'
    m_Info = {
        'Action': NpcAction1040,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1041(baseconfig.CNpcData1028):
    m_SID = 1041
    m_Name = '电梯'
    m_Info = {
        'Action': NpcAction1041,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1042(baseconfig.CNpcData1014):
    m_SID = 1042
    m_Name = '出隐藏关传送门'
    m_Info = {
        'Action': NpcAction1042,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1043(baseconfig.CNpcData1034):
    m_SID = 1043
    m_Name = '护送关—挑战宝箱'
    m_Info = {
        'Action': NpcAction1043,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1044(baseconfig.CNpcData1035):
    m_SID = 1044
    m_Name = '三幕隐藏关传送门'
    m_Info = {
        'Action': NpcAction1044,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1045(baseconfig.CNpcData1035):
    m_SID = 1045
    m_Name = '三幕出隐藏关传送门'
    m_Info = {
        'Action': NpcAction1045,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1046(baseconfig.CNpcData1036):
    m_SID = 1046
    m_Name = '陆吾关-新传送门'
    m_Info = {
        'Action': NpcAction1046,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1047(baseconfig.CNpcData1037):
    m_SID = 1047
    m_Name = '每日试炼金爵'
    m_Info = {
        'Action': NpcAction1047,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1048(baseconfig.CNpcData1006):
    m_SID = 1048
    m_Name = '每日试炼金爵宝箱'
    m_Info = {
        'Action': NpcAction1048,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1049(baseconfig.CNpcData1038):
    m_SID = 1049
    m_Name = '瞄准关武器宝箱'
    m_Info = { }


class CNpcData1050(baseconfig.CNpcData1003):
    m_SID = 1050
    m_Name = '【第三幕】通关金爵宝箱'
    m_Info = {
        'Action': NpcAction1050,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1053(baseconfig.CNpcData1041):
    m_SID = 1053
    m_Name = '祝福使者'
    m_Info = { }


class CNpcData1054(baseconfig.CNpcData1042):
    m_SID = 1054
    m_Name = '精魄商人'
    m_Info = {
        'Action': NpcAction1054,
        'ActionType': NPC_ACTION_SHOP }


class CNpcData1099(baseconfig.CNpcData1015):
    m_SID = 1099
    m_Name = '美术测试门'
    m_Info = {
        'Action': NpcAction1099,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1101(baseconfig.CNpcData1101):
    m_SID = 1101
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1102(baseconfig.CNpcData1102):
    m_SID = 1102
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1103(baseconfig.CNpcData1103):
    m_SID = 1103
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1104(baseconfig.CNpcData1104):
    m_SID = 1104
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1105(baseconfig.CNpcData1105):
    m_SID = 1105
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1106(baseconfig.CNpcData1106):
    m_SID = 1106
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1107(baseconfig.CNpcData1107):
    m_SID = 1107
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1108(baseconfig.CNpcData1108):
    m_SID = 1108
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1109(baseconfig.CNpcData1109):
    m_SID = 1109
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1110(baseconfig.CNpcData1110):
    m_SID = 1110
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1111(baseconfig.CNpcData1111):
    m_SID = 1111
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1112(baseconfig.CNpcData1112):
    m_SID = 1112
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1113(baseconfig.CNpcData1113):
    m_SID = 1113
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData1201(baseconfig.CNpcData1021):
    m_SID = 1201
    m_Name = '二幕通关传送门'
    m_Info = {
        'Action': NpcAction1201,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1202(baseconfig.CNpcData1022):
    m_SID = 1202
    m_Name = '二幕入口传送门'
    m_Info = {
        'Action': NpcAction1202,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1203(baseconfig.CNpcData1025):
    m_SID = 1203
    m_Name = '篝火'
    m_Info = {
        'Action': NpcAction1203,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1301(baseconfig.CNpcData1031):
    m_SID = 1301
    m_Name = '三幕通关传送门'
    m_Info = {
        'Action': NpcAction1301,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1302(baseconfig.CNpcData1031):
    m_SID = 1302
    m_Name = '三幕入口传送门'
    m_Info = {
        'Action': NpcAction1302,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1405(baseconfig.CNpcData1046):
    m_SID = 1405
    m_Name = '四幕通关传送门'
    m_Info = {
        'Action': NpcAction1405,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1501(baseconfig.CNpcData1034):
    m_SID = 1501
    m_Name = '隐藏-普通2103-挑战'
    m_Info = {
        'Action': NpcAction1501,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1502(baseconfig.CNpcData1003):
    m_SID = 1502
    m_Name = '隐藏-普通2101-通关'
    m_Info = {
        'Action': NpcAction1502,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1503(baseconfig.CNpcData1003):
    m_SID = 1503
    m_Name = '隐藏-普通2102-通关'
    m_Info = {
        'Action': NpcAction1503,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1504(baseconfig.CNpcData1034):
    m_SID = 1504
    m_Name = '隐藏-普通2107-挑战'
    m_Info = {
        'Action': NpcAction1504,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1505(baseconfig.CNpcData1003):
    m_SID = 1505
    m_Name = '隐藏-普通2105-通关'
    m_Info = {
        'Action': NpcAction1505,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1506(baseconfig.CNpcData1003):
    m_SID = 1506
    m_Name = '隐藏-普通2106-通关'
    m_Info = {
        'Action': NpcAction1506,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1507(baseconfig.CNpcData1006):
    m_SID = 1507
    m_Name = '隐藏-普通2101-无条件'
    m_Info = {
        'Action': NpcAction1507,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1508(baseconfig.CNpcData1006):
    m_SID = 1508
    m_Name = '隐藏-普通2102-无条件'
    m_Info = {
        'Action': NpcAction1508,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1509(baseconfig.CNpcData1024):
    m_SID = 1509
    m_Name = '隐藏-魔盒2208-通关'
    m_Info = {
        'Action': NpcAction1509,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1510(baseconfig.CNpcData1023):
    m_SID = 1510
    m_Name = '隐藏-魔盒2208-挑战'
    m_Info = {
        'Action': NpcAction1510,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1511(baseconfig.CNpcData1023):
    m_SID = 1511
    m_Name = '隐藏-魔盒2204-通关'
    m_Info = {
        'Action': NpcAction1511,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1512(baseconfig.CNpcData1023):
    m_SID = 1512
    m_Name = '隐藏-魔盒2212-通关'
    m_Info = {
        'Action': NpcAction1512,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1513(baseconfig.CNpcData1006):
    m_SID = 1513
    m_Name = '隐藏-普通2105-无条件'
    m_Info = {
        'Action': NpcAction1513,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1514(baseconfig.CNpcData1006):
    m_SID = 1514
    m_Name = '隐藏-普通-无条件'
    m_Info = {
        'Action': NpcAction1514,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1515(baseconfig.CNpcData1003):
    m_SID = 1515
    m_Name = '隐藏-普通-通关'
    m_Info = {
        'Action': NpcAction1515,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1516(baseconfig.CNpcData1023):
    m_SID = 1516
    m_Name = '隐藏-普通-挑战'
    m_Info = {
        'Action': NpcAction1516,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1517(baseconfig.CNpcData1024):
    m_SID = 1517
    m_Name = '隐藏-普通-通关三选一'
    m_Info = {
        'Action': NpcAction1517,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1518(baseconfig.CNpcData1023):
    m_SID = 1518
    m_Name = '隐藏-普通-困难挑战'
    m_Info = {
        'Action': NpcAction1518,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData2001(baseconfig.CNpcData2001):
    m_SID = 2001
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2002(baseconfig.CNpcData2002):
    m_SID = 2002
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2003(baseconfig.CNpcData2003):
    m_SID = 2003
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2004(baseconfig.CNpcData2004):
    m_SID = 2004
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2005(baseconfig.CNpcData2005):
    m_SID = 2005
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2006(baseconfig.CNpcData2006):
    m_SID = 2006
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2007(baseconfig.CNpcData2007):
    m_SID = 2007
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2008(baseconfig.CNpcData2008):
    m_SID = 2008
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2009(baseconfig.CNpcData2009):
    m_SID = 2009
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2010(baseconfig.CNpcData2010):
    m_SID = 2010
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2011(baseconfig.CNpcData2011):
    m_SID = 2011
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2012(baseconfig.CNpcData2012):
    m_SID = 2012
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2013(baseconfig.CNpcData2013):
    m_SID = 2013
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2014(baseconfig.CNpcData2014):
    m_SID = 2014
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2015(baseconfig.CNpcData2015):
    m_SID = 2015
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData2017(baseconfig.CNpcData1032):
    m_SID = 2017
    m_Name = '测试刷新'
    m_Info = { }


class CNpcData2101(baseconfig.CNpcData2101):
    m_SID = 2101
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2102(baseconfig.CNpcData2102):
    m_SID = 2102
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2103(baseconfig.CNpcData2103):
    m_SID = 2103
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2104(baseconfig.CNpcData2104):
    m_SID = 2104
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2105(baseconfig.CNpcData2105):
    m_SID = 2105
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2106(baseconfig.CNpcData2106):
    m_SID = 2106
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2107(baseconfig.CNpcData2107):
    m_SID = 2107
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2108(baseconfig.CNpcData2108):
    m_SID = 2108
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2109(baseconfig.CNpcData2109):
    m_SID = 2109
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2110(baseconfig.CNpcData2110):
    m_SID = 2110
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2111(baseconfig.CNpcData2111):
    m_SID = 2111
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2112(baseconfig.CNpcData2112):
    m_SID = 2112
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2113(baseconfig.CNpcData2113):
    m_SID = 2113
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2114(baseconfig.CNpcData2114):
    m_SID = 2114
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2115(baseconfig.CNpcData2115):
    m_SID = 2115
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2116(baseconfig.CNpcData2116):
    m_SID = 2116
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2117(baseconfig.CNpcData2117):
    m_SID = 2117
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2118(baseconfig.CNpcData2118):
    m_SID = 2118
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2119(baseconfig.CNpcData2119):
    m_SID = 2119
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2120(baseconfig.CNpcData2120):
    m_SID = 2120
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2121(baseconfig.CNpcData2121):
    m_SID = 2121
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2122(baseconfig.CNpcData2122):
    m_SID = 2122
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData2123(baseconfig.CNpcData2123):
    m_SID = 2123
    m_Name = '事件NPC'
    m_Info = { }


class CNpcData3001(baseconfig.CNpcData3001):
    m_SID = 3001
    m_Name = '刷新npc'
    m_Info = { }


class CNpcData5001(baseconfig.CNpcData5001):
    m_SID = 5001
    m_Name = '神秘宝箱'
    m_Info = {
        'Action': NpcAction5001,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData5002(baseconfig.CNpcData5002):
    m_SID = 5002
    m_Name = '挑战奖励NPC'
    m_Info = {
        'Action': NpcAction5002,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData5003(baseconfig.CNpcData5003):
    m_SID = 5003
    m_Name = '测试npc'
    m_Info = {
        'Action': NpcAction5003,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData9001(baseconfig.CNpcData9001):
    m_SID = 9001
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData9002(baseconfig.CNpcData9002):
    m_SID = 9002
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData9003(baseconfig.CNpcData9003):
    m_SID = 9003
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData9004(baseconfig.CNpcData9004):
    m_SID = 9004
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData9005(baseconfig.CNpcData9005):
    m_SID = 9005
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData9006(baseconfig.CNpcData9006):
    m_SID = 9006
    m_Name = '关卡NPC测试'
    m_Info = { }


class CNpcData9100(baseconfig.CNpcData1006):
    m_SID = 9100
    m_Name = '测试-普通-无条件'
    m_Info = {
        'Action': NpcAction9100,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData9101(baseconfig.CNpcData1006):
    m_SID = 9101
    m_Name = '测试-三选一-无条件'
    m_Info = {
        'Action': NpcAction9101,
        'ActionType': NPC_ACTION_ITEMBOX }

