# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3002/npc.pyc
# RelativePath: clientlogic/cl_wardata/w3002/npc.pyc
# Source Generated with Decompyle++
# File: npc.pyc (Python 3.6)

from cl_resmgr.resdata import CNpcData as CCustom
import cl_wardata.npcaction as npcaction
import cl_resmgr.npcconfig as baseconfig
from cl_commondefines import NPC_ACTION_ITEMBOX, NPC_ACTION_MAPCHOOSE, NPC_ACTION_SETTLELEVEL, NPC_ACTION_SHOP, OBTAIN_CASH, OBTAIN_WARCASH
from cl_newformula import Func16, Func201, Func202, Func203

def NpcAction1001(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)


def NpcAction1002(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)


def NpcAction1003(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101 }, 130, {
        'OffsetY': 1.5 })


def NpcAction1004(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1005(oNpc, who):
    npcaction.NpcGoodsConfig(oNpc, who, 0, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 50 + Func202(*a) * 5), 1007, None, { })
    npcaction.NpcGoodsConfig(oNpc, who, 1, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 50 + Func202(*a) * 5), 1001, None, { })
    npcaction.NpcGoodsConfig(oNpc, who, 2, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 50 + Func202(*a) * 5), 1008, None, { })
    npcaction.NpcGoodsEquip(oNpc, who, 3, 100, 1, (lambda *a: 0 + Func201(*a) * 150 + Func202(*a) * 30), {
        1: 1001,
        2: 1001 }, None, None, None, { })
    npcaction.NpcGoodsEquip(oNpc, who, 4, 100, 1, (lambda *a: 0 + Func201(*a) * 150 + Func202(*a) * 30), {
        1: 1001,
        2: 1001 }, None, None, None, { })
    npcaction.NpcGoodsRelic(oNpc, who, 5, 100, 1, OBTAIN_WARCASH, (lambda *a: (Func201(*a) * 150 + Func202(*a) * 30) * Func203(*a) * Func16(*a, **{
'a': 0.9,
'b': 1 })), {
        1: 2001,
        2: 2001 }, None, None, { }, None)
    npcaction.NpcGoodsConfig(oNpc, who, 6, 100, 3, OBTAIN_CASH, 100, 1002, None, { })


def NpcAction1006(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101 }, 130, {
        'OffsetY': 1.5 })


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
                'Times': 1 } } }, 142)


def NpcAction1011(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            1001: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 6 },
            401: {
                'Prop': 10000,
                'Times': 3 },
            201: {
                'Prop': 10000,
                'Times': 6 } },
        2: {
            1001: {
                'Prop': 10000,
                'Times': 2 },
            2001: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 6 },
            401: {
                'Prop': 10000,
                'Times': 3 },
            201: {
                'Prop': 10000,
                'Times': 6 } } }, 130)
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101 }, 130, {
        'OffsetY': 1.5 })


def NpcAction1012(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1013(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 3001,
        2: 3001 }, None, { })


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
                'Times': 3 } } }, 130)


def NpcAction1017(oNpc, who):
    npcaction.NpcTransferHideLevel(oNpc, who)


def NpcAction1019(oNpc, who):
    npcaction.NpcGoodsConfig(oNpc, who, 0, 100, 1, OBTAIN_CASH, (lambda *a: 0 + Func201(*a) * 50 + Func202(*a) * 5), 1007, None, { })
    npcaction.NpcGoodsConfig(oNpc, who, 1, 100, 1, OBTAIN_CASH, (lambda *a: 0 + Func201(*a) * 50 + Func202(*a) * 5), 1001, None, { })
    npcaction.NpcGoodsConfig(oNpc, who, 2, 100, 1, OBTAIN_CASH, (lambda *a: 0 + Func201(*a) * 50 + Func202(*a) * 5), 1008, None, { })


def NpcAction1020(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1021(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            2001: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            2001: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1023(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 1002,
        2: 1002 }, 0, {
        3: 100 }, 150)


def NpcAction1024(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 2002,
        2: 2002 }, 0, {
        3: 100 }, 150)


def NpcAction1025(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 1003,
        2: 1003 }, 0, {
        3: 100 }, 150)


def NpcAction1026(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            401: {
                'Prop': 3000,
                'Times': 1 },
            2001: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 5 } },
        2: {
            401: {
                'Prop': 3000,
                'Times': 1 },
            2001: {
                'Prop': 10000,
                'Times': 1 },
            101: {
                'Prop': 10000,
                'Times': 5 } } }, 130)


def NpcAction1027(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4001,
        2: 4001 }, 0, { })


def NpcAction1028(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4001,
        2: 4001 }, 0, {
        'OnlyCore': 1 })


def NpcAction1029(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101 }, 130, {
        'OffsetY': 1.5 })


def NpcAction1099(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)


def NpcAction1201(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)


def NpcAction1202(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


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
    m_Name = '掉落普通天赋金爵的宝箱'
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
    m_Name = '掉落天赋金爵的宝箱'
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
        'ActionType': NPC_ACTION_MAPCHOOSE }


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


class CNpcData1019(baseconfig.CNpcData1005):
    m_SID = 1019
    m_Name = '精魄商店'
    m_Info = {
        'Action': NpcAction1019,
        'ActionType': NPC_ACTION_SHOP }


class CNpcData1020(baseconfig.CNpcData1014):
    m_SID = 1020
    m_Name = '出隐藏关传送门'
    m_Info = {
        'Action': NpcAction1020,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1021(baseconfig.CNpcData1006):
    m_SID = 1021
    m_Name = '隐藏关内宝箱'
    m_Info = {
        'Action': NpcAction1021,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1023(baseconfig.CNpcData1017):
    m_SID = 1023
    m_Name = '武器魔盒3选1'
    m_Info = {
        'Action': NpcAction1023,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1024(baseconfig.CNpcData1017):
    m_SID = 1024
    m_Name = '遗物魔盒3选1'
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
    m_Name = '挑战触发宝箱'
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


class CNpcData1029(baseconfig.CNpcData1006):
    m_SID = 1029
    m_Name = '掉落普通天赋金爵的宝箱'
    m_Info = {
        'Action': NpcAction1029,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1099(baseconfig.CNpcData1015):
    m_SID = 1099
    m_Name = '美术测试门'
    m_Info = {
        'Action': NpcAction1099,
        'ActionType': NPC_ACTION_SETTLELEVEL }


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

