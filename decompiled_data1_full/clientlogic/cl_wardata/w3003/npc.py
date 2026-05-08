# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3003/npc.pyc
# RelativePath: clientlogic/cl_wardata/w3003/npc.pyc
# Source Generated with Decompyle++
# File: npc.pyc (Python 3.6)

from cl_resmgr.resdata import CNpcData as CCustom
import cl_wardata.npcaction as npcaction
import cl_resmgr.npcconfig as baseconfig
from cl_commondefines import NPC_ACTION_ITEMBOX, NPC_ACTION_MAPCHOOSE, NPC_ACTION_SETTLELEVEL, NPC_ACTION_SHOP, OBTAIN_GOLD, OBTAIN_WARCASH
from cl_item.defines import QUALITY_TYPE_HIGH, QUALITY_TYPE_LOW, QUALITY_TYPE_NORMAL
from cl_newformula import Func16, Func201, Func202, Func203

def NpcAction1001(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)


def NpcAction1002(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1003(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            1001: {
                'Prop': 10000,
                'Times': 1 } },
        2: {
            1001: {
                'Prop': 10000,
                'Times': 1 } } }, 130)


def NpcAction1004(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)


def NpcAction1005(oNpc, who):
    npcaction.NpcGoodsConfig(oNpc, who, 0, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 10 + Func202(*a) * 2), 1007, None, { })
    npcaction.NpcGoodsConfig(oNpc, who, 1, 100, 1, OBTAIN_WARCASH, (lambda *a: 0 + Func201(*a) * 10 + Func202(*a) * 2), 1001, None, { })
    npcaction.NpcGoodsEquip(oNpc, who, 2, 100, 1, {
        QUALITY_TYPE_HIGH: (lambda *a: 10 + Func201(*a) * 5 + Func202(*a) * 1),
        QUALITY_TYPE_NORMAL: (lambda *a: 50 + Func201(*a) * -8 + Func202(*a) * -1),
        QUALITY_TYPE_LOW: (lambda *a: 30 + Func201(*a) * -10 + Func202(*a) * -0.5) }, {
        1: 1001,
        2: 1001 }, None, None, None, { })
    npcaction.NpcGoodsEquip(oNpc, who, 3, 100, 1, {
        QUALITY_TYPE_HIGH: (lambda *a: 10 + Func201(*a) * 5 + Func202(*a) * 1),
        QUALITY_TYPE_NORMAL: (lambda *a: 50 + Func201(*a) * -8 + Func202(*a) * -1),
        QUALITY_TYPE_LOW: (lambda *a: 30 + Func201(*a) * -10 + Func202(*a) * -0.5) }, {
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
    npcaction.NpcGoodsConfig(oNpc, who, 6, 100, 3, OBTAIN_GOLD, 10, 1002, None, { })


def NpcAction1016(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            1001: {
                'Prop': 10000,
                'Times': 1 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } },
        2: {
            1001: {
                'Prop': 10000,
                'Times': 1 },
            201: {
                'Prop': 10000,
                'Times': 3 },
            2001: {
                'Prop': 10000,
                'Times': 2 } } }, 130)


def NpcAction1017(oNpc, who):
    npcaction.NpcTransferHideLevel(oNpc, who)


def NpcAction1019(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


class CNpcData1001(baseconfig.CNpcData1001):
    m_SID = 1001
    m_Name = ''
    m_Info = {
        'Action': NpcAction1001,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1002(baseconfig.CNpcData1002):
    m_SID = 1002
    m_Name = ''
    m_Info = {
        'Action': NpcAction1002,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1003(baseconfig.CNpcData1003):
    m_SID = 1003
    m_Name = ''
    m_Info = {
        'Action': NpcAction1003,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1004(baseconfig.CNpcData1004):
    m_SID = 1004
    m_Name = ''
    m_Info = {
        'Action': NpcAction1004,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1005(baseconfig.CNpcData1005):
    m_SID = 1005
    m_Name = ''
    m_Info = {
        'Action': NpcAction1005,
        'ActionType': NPC_ACTION_SHOP }


class CNpcData1016(baseconfig.CNpcData1006):
    m_SID = 1016
    m_Name = ''
    m_Info = {
        'Action': NpcAction1016,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1017(baseconfig.CNpcData1012):
    m_SID = 1017
    m_Name = ''
    m_Info = {
        'Action': NpcAction1017,
        'ActionType': NPC_ACTION_SETTLELEVEL }


class CNpcData1018(baseconfig.CNpcData1013):
    m_SID = 1018
    m_Name = ''
    m_Info = { }


class CNpcData1019(baseconfig.CNpcData1014):
    m_SID = 1019
    m_Name = ''
    m_Info = {
        'Action': NpcAction1019,
        'ActionType': NPC_ACTION_MAPCHOOSE }

