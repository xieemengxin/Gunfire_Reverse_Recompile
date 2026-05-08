# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/wand/__init__.pyc
# RelativePath: clientlogic/cl_platformdata/pc/wand/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import WANDPUT_INITIAL, WANDPUT_SHOPBUY
g_AllWand = { }
g_WandPut = { }
from cl_commondefines import WANDTAG_DAMAGE, WANDTAG_FUNCTION, WANDTAG_PERFORM, WANDTAG_WEAPON
g_AllWand = {
    1001: 1,
    1002: 1,
    1003: 1,
    1005: 1,
    1006: 1,
    1007: 1,
    1008: 1,
    1009: 1,
    1010: 1,
    1011: 1,
    1012: 1,
    1013: 1,
    1015: 1,
    1016: 1,
    1018: 1,
    1019: 1,
    1020: 1,
    1021: 1,
    1022: 1 }
g_WandHasPut = {
    1001: 1,
    1003: 1,
    1005: 1,
    1006: 1,
    1007: 1,
    1008: 1,
    1009: 1,
    1011: 1,
    1012: 1,
    1013: 1,
    1015: 1,
    1016: 1,
    1018: 1,
    1019: 1,
    1020: 1,
    1021: 1,
    1022: 1 }
g_WandPut = {
    WANDPUT_SHOPBUY: {
        1003: 1,
        1005: 1,
        1006: 1,
        1007: 1,
        1008: 1,
        1009: 1,
        1011: 1,
        1012: 1,
        1013: 1,
        1015: 1,
        1016: 1,
        1018: 1,
        1019: 1,
        1020: 1,
        1021: 1,
        1022: 1 },
    WANDPUT_INITIAL: {
        1001: 1 } }
g_WandTag = {
    WANDTAG_PERFORM: [
        1007],
    WANDTAG_DAMAGE: [
        1005,
        1006,
        1011],
    WANDTAG_WEAPON: [
        1005,
        1013,
        1018],
    WANDTAG_FUNCTION: [
        1002,
        1003,
        1008,
        1009,
        1010,
        1012,
        1015,
        1016,
        1019,
        1020,
        1021,
        1022] }
g_WandDrop = {
    1001: 0,
    1002: 1,
    1003: 1,
    1005: 1,
    1006: 1,
    1007: 1,
    1008: 1,
    1009: 1,
    1010: 1,
    1011: 1,
    1012: 1,
    1013: 1,
    1015: 1,
    1016: 1,
    1018: 1,
    1019: 1,
    1020: 1,
    1021: 1,
    1022: 1 }
g_WandRecycle = {
    1001: 0,
    1002: 1,
    1003: 1,
    1005: 1,
    1006: 1,
    1007: 1,
    1008: 1,
    1009: 1,
    1010: 1,
    1011: 1,
    1012: 1,
    1013: 1,
    1015: 1,
    1016: 1,
    1018: 1,
    1019: 1,
    1020: 1,
    1021: 1,
    1022: 1 }

def GetAllWand():
    return g_AllWand


def GetAllPutWand():
    return g_WandHasPut


def GetWandPut(iPutSource):
    if iPutSource not in g_WandPut:
        return { }
    return g_WandPut[iPutSource]


def GetWandByTag(iTag):
    if iTag in g_WandTag:
        return g_WandTag[iTag]
    return []


def GetWandDropInfo(iWand):
    if iWand in g_WandDrop:
        return g_WandDrop[iWand]
    return 0


def GetWandRecycleInfo(iWand):
    if iWand in g_WandRecycle:
        return g_WandRecycle[iWand]
    return 0

from cl_commondefines import WAND_CARDPACK
g_CardPack = {
    WAND_CARDPACK: {
        1999: None } }

def GetWandCardPack():
    return g_CardPack

g_WandPresetTemp = { }

def GetAllWandPresetTemp():
    return g_WandPresetTemp

