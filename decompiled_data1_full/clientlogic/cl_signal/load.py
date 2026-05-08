# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_signal/load.pyc
# RelativePath: clientlogic/cl_signal/load.pyc
# Source Generated with Decompyle++
# File: load.pyc (Python 3.6)

import importlib
import importlib.util
g_TxtSignal = {
    1001: {
        'Weight': {
            1: 10,
            2: 10,
            3: 10 },
        'Info': {
            1: {
                131: 2243,
                132: 9136,
                133: 9161,
                134: 9186 },
            2: {
                131: 2244,
                132: 9137,
                133: 9162,
                134: 9187 },
            3: {
                131: 2245,
                132: 9138,
                133: 9163,
                134: 9188 } } },
    1002: {
        'Weight': {
            1: 10,
            2: 10,
            3: 10 },
        'Info': {
            1: {
                131: 2246,
                132: 9139,
                133: 9164,
                134: 9189 },
            2: {
                131: 2247,
                132: 9140,
                133: 9165,
                134: 9190 },
            3: {
                131: 2248,
                132: 9141,
                133: 9166,
                134: 9191 } } },
    1003: {
        'Weight': {
            1: 10,
            2: 10,
            3: 10 },
        'Info': {
            1: {
                131: 2249,
                132: 9143,
                133: 9167,
                134: 9192 },
            2: {
                131: 2250,
                132: 9144,
                133: 9168,
                134: 9193 },
            3: {
                131: 2277,
                132: 9142,
                133: 9169,
                134: 9194 } } } }
from cl_commondefines import NWARRIOR_DROP_DICE, NWARRIOR_DROP_EQUIP, NWARRIOR_DROP_MAGIC_WAND, NWARRIOR_DROP_RELIC, NWARRIOR_DROP_RELIC_MYSTERY, NWARRIOR_DROP_S7CRYSTAL, NWARRIOR_DROP_S7MODULE, NWARRIOR_DROP_WANDCOMP, NWARRIOR_NPC_DICESHOP, NWARRIOR_NPC_EVENT, NWARRIOR_NPC_GOLDENCUP, NWARRIOR_NPC_GSCASHSHOP, NWARRIOR_NPC_ITEMBOX, NWARRIOR_NPC_LOCKEDBOX, NWARRIOR_NPC_PETSHOP, NWARRIOR_NPC_REFRESH, NWARRIOR_NPC_RELICLOTTERY, NWARRIOR_NPC_RELICROLLBOX, NWARRIOR_NPC_S7SHOP, NWARRIOR_NPC_SHOP, NWARRIOR_NPC_SMITH, NWARRIOR_NPC_TASKNPC, NWARRIOR_NPC_TRANSFER, NWARRIOR_NPC_WANDSHOP
g_FightType2Signal = {
    NWARRIOR_DROP_S7CRYSTAL: 1235,
    NWARRIOR_DROP_S7MODULE: 1234,
    NWARRIOR_NPC_S7SHOP: 1233,
    NWARRIOR_DROP_DICE: 1232,
    NWARRIOR_NPC_DICESHOP: 1231,
    NWARRIOR_NPC_WANDSHOP: 1230,
    NWARRIOR_DROP_WANDCOMP: 1229,
    NWARRIOR_DROP_MAGIC_WAND: 1228,
    NWARRIOR_DROP_RELIC_MYSTERY: 1227,
    NWARRIOR_NPC_RELICLOTTERY: 1225,
    NWARRIOR_NPC_RELICROLLBOX: 1224,
    NWARRIOR_NPC_PETSHOP: 1222,
    NWARRIOR_NPC_TASKNPC: 1218,
    NWARRIOR_NPC_GSCASHSHOP: 1213,
    NWARRIOR_NPC_REFRESH: 1211,
    NWARRIOR_NPC_LOCKEDBOX: 1210,
    NWARRIOR_NPC_ITEMBOX: 1209,
    NWARRIOR_NPC_EVENT: 1207,
    NWARRIOR_NPC_SMITH: 1204,
    NWARRIOR_NPC_SHOP: 1203,
    NWARRIOR_NPC_TRANSFER: 1202,
    NWARRIOR_NPC_GOLDENCUP: 1103,
    NWARRIOR_DROP_RELIC: 1102,
    NWARRIOR_DROP_EQUIP: 1101 }
if 'g_SignalCls' not in globals():
    g_SignalCls = { }

def GetSignalCls(sid):
    if sid not in g_SignalCls:
        sMode = 'cl_signal.s%04d' % sid
        spec = importlib.util.find_spec(sMode)
        if spec is None:
            return None
        mod = importlib.import_module(sMode)
        clsSignal = mod.CSignal
        g_SignalCls[sid] = clsSignal
    return g_SignalCls[sid]


def GetTxtSignal(sid):
    if sid not in g_TxtSignal:
        return { }
    return g_TxtSignal[sid]


def GetFightType2Signal(iFightType):
    if iFightType not in g_FightType2Signal:
        return 0
    return g_FightType2Signal[iFightType]


def GetAIShareSignalFightType():
    return list(g_FightType2Signal)

