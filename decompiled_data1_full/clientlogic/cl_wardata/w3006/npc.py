# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/w3006/npc.pyc
# RelativePath: clientlogic/cl_wardata/w3006/npc.pyc
# Source Generated with Decompyle++
# File: npc.pyc (Python 3.6)

from cl_resmgr.resdata import CNpcData as CCustom
import cl_wardata.npcaction as npcaction
import cl_resmgr.npcconfig as baseconfig
from cl_commondefines import NPC_ACTION_ITEMBOX, NPC_ACTION_MAPCHOOSE, NPC_ACTION_SETTLELEVEL

def NpcAction1001(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1002(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1003(oNpc, who):
    npcaction.NpcRewardItemList(oNpc, who, {
        1: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 6 },
            1001: {
                'Prop': 10000,
                'Times': 2 } },
        2: {
            101: {
                'Prop': 10000,
                'Times': 10 },
            201: {
                'Prop': 10000,
                'Times': 6 },
            1001: {
                'Prop': 10000,
                'Times': 2 } } }, 130)


def NpcAction1004(oNpc, who):
    npcaction.NpcTransferLevel(oNpc, who)


def NpcAction1099(oNpc, who):
    npcaction.NpcDelayTransferLevel(oNpc, who, 3000)


class CNpcData1001(baseconfig.CNpcData1012):
    m_SID = 1001
    m_Name = ''
    m_Info = {
        'Action': NpcAction1001,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1002(baseconfig.CNpcData1002):
    m_SID = 1002
    m_Name = ''
    m_Info = {
        'Action': NpcAction1002,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1003(baseconfig.CNpcData1006):
    m_SID = 1003
    m_Name = ''
    m_Info = {
        'Action': NpcAction1003,
        'ActionType': NPC_ACTION_ITEMBOX }


class CNpcData1004(baseconfig.CNpcData1015):
    m_SID = 1004
    m_Name = ''
    m_Info = {
        'Action': NpcAction1004,
        'ActionType': NPC_ACTION_MAPCHOOSE }


class CNpcData1099(baseconfig.CNpcData1015):
    m_SID = 1099
    m_Name = '美术测试门'
    m_Info = {
        'Action': NpcAction1099,
        'ActionType': NPC_ACTION_SETTLELEVEL }

