# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3004/npc.pyc
# RelativePath: clientlogic/cl_wardata/w3004/npc.pyc
# Source Generated with Decompyle++
# File: npc.pyc (Python 3.6)

from cl_resmgr.resdata import CNpcData as CCustom
import cl_wardata.npcaction as npcaction
import cl_resmgr.npcconfig as baseconfig
from cl_commondefines import NPC_ACTION_ITEMBOX, NPC_ACTION_MAPCHOOSE, NPC_ACTION_SETTLELEVEL, NPC_ACTION_SHOP, OBTAIN_CASH, OBTAIN_WARCASH
from cl_newformula import Func16, Func201, Func202, Func203

def NpcAction1001(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1002(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 4 },
            1001: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 4 },
            1001: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } } }, 130)


def NpcAction1003(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 4 },
            1001: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 4 },
            1001: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } } }, 130)


def NpcAction1004(oNpc, who):
    npcaction.NpcGoodsConfig(oNpc, who, 0, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 10 + Func202(*a) * 2), 1007, None, { })
    npcaction.NpcGoodsConfig(oNpc, who, 1, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 10 + Func202(*a) * 2), 1001, None, { })
    npcaction.NpcGoodsEquip(oNpc, who, 2, 100, 1, (lambda *a: 0 + Func201(*a) * 150 + Func202(*a) * 20), {
        1: 1001,
        2: 1001 }, None, None, None, { })
    npcaction.NpcGoodsEquip(oNpc, who, 3, 100, 1, (lambda *a: 0 + Func201(*a) * 150 + Func202(*a) * 20), {
        1: 1001,
        2: 1001 }, None, None, None, { })
    npcaction.NpcGoodsRelic(oNpc, who, 4, 100, 1, OBTAIN_WARCASH, (lambda *a: (Func201(*a) * 50 + Func202(*a) * 100) * Func203(*a) * Func16(*a, **{
'a': 0.9,
'b': 1 })), {
        1: 2001,
        2: 2001 }, None, None, { }, None)
    npcaction.NpcGoodsRelic(oNpc, who, 5, 100, 1, OBTAIN_WARCASH, (lambda *a: (Func201(*a) * 50 + Func202(*a) * 100) * Func203(*a) * Func16(*a, **{
'a': 0.9,
'b': 1 })), {
        1: 2001,
        2: 2001 }, None, None, { }, None)
    npcaction.NpcGoodsConfig(oNpc, who, 6, 100, 3, OBTAIN_CASH, 10, 1002, None, { })


def NpcAction1005(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 3001,
        2: 3001 }, None, { })


def NpcAction1006(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 10 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 10 } } }, 130)


def NpcAction1008(oNpc, who):
    npcaction.NpcTransferHideLevel(oNpc, who)


def NpcAction1009(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4001,
        2: 4001 }, 0, { })


def NpcAction1010(oNpc, who):
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4001,
        2: 4001 }, 0, {
        'OnlyCore': 1 })


def NpcAction1011(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 4 },
            1001: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 4 },
            1001: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } } }, 130)
    npcaction.NpcStartMiniGame(oNpc, who, {
        1: 4101,
        2: 4101 }, 130, {
        'OffsetY': 1.5 })


def NpcAction1019(oNpc, who):
    npcaction.NpcTransferHideLevel(oNpc, who)


def NpcAction1020(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1021(oNpc, who):
    npcaction.NpcTriggerChooseItem(oNpc, who, {
        1: 1002,
        2: 1002 }, 1, {
        3: 100,
        2: 100 }, 150)


def NpcAction1022(oNpc, who):
    npcaction.NpcAddTargetState(oNpc, who, 1165, 100)


def NpcAction1023(oNpc, who):
    npcaction.NpcTriggerClientBehavior(oNpc, who, 39, 0, 1)


class CNpcData1001(baseconfig.CNpcData1002):
    m_SID = 1001
    m_Name = '结算传送门'
    m_Info = {
        'Action': NpcAction1001,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1002(baseconfig.CNpcData1006):
    m_SID = 1002
    m_Name = '通用宝箱'
    m_Info = {
        'Action': NpcAction1002,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1003(baseconfig.CNpcData1006):
    m_SID = 1003
    m_Name = '通用宝箱'
    m_Info = {
        'Action': NpcAction1003,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1004(baseconfig.CNpcData1005):
    m_SID = 1004
    m_Name = '商店'
    m_Info = {
        'Action': NpcAction1004,
        'ActionType': NPC_ACTION_SHOP }


class CNpcData1005(baseconfig.CNpcData1008):
    m_SID = 1005
    m_Name = '属性卷轴'
    m_Info = {
        'Action': NpcAction1005,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1006(baseconfig.CNpcData1006):
    m_SID = 1006
    m_Name = '通用宝箱'
    m_Info = {
        'Action': NpcAction1006,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1007(baseconfig.CNpcData1013):
    m_SID = 1007
    m_Name = '工匠'
    m_Info = { }


class CNpcData1008(baseconfig.CNpcData1012):
    m_SID = 1008
    m_Name = '进隐藏关传送门'
    m_Info = {
        'Action': NpcAction1008,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1009(baseconfig.CNpcData1008):
    m_SID = 1009
    m_Name = '测试普通天赋金爵'
    m_Info = {
        'Action': NpcAction1009,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1010(baseconfig.CNpcData1008):
    m_SID = 1010
    m_Name = '测试核心天赋金爵'
    m_Info = {
        'Action': NpcAction1010,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1011(baseconfig.CNpcData1006):
    m_SID = 1011
    m_Name = '测试生成金爵宝箱'
    m_Info = {
        'Action': NpcAction1011,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1019(baseconfig.CNpcData1019):
    m_SID = 1019
    m_Name = '进二幕隐藏关传送门'
    m_Info = {
        'Action': NpcAction1019,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1020(baseconfig.CNpcData1014):
    m_SID = 1020
    m_Name = '出隐藏关传送门'
    m_Info = {
        'Action': NpcAction1020,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1021(baseconfig.CNpcData1017):
    m_SID = 1021
    m_Name = '魔盒'
    m_Info = {
        'Action': NpcAction1021,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1022(baseconfig.CNpcData1025):
    m_SID = 1022
    m_Name = '篝火'
    m_Info = {
        'Action': NpcAction1022,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1023(baseconfig.CNpcData1028):
    m_SID = 1023
    m_Name = '电梯'
    m_Info = {
        'Action': NpcAction1023,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1101(baseconfig.CNpcData1101):
    m_SID = 1101
    m_Name = '关卡NPC测试'
    m_Info = { }

