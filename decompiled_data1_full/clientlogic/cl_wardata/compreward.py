# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_wardata/compreward.pyc
# RelativePath: clientlogic/cl_wardata/compreward.pyc
# Source Generated with Decompyle++
# File: compreward.pyc (Python 3.6)

g_CompRewardConfig = { }
from cl_commondefines import DEVICECOMP_TYPE_COMMON, DEVICECOMP_TYPE_DEVICE, DEVICECOMP_TYPE_HERO
g_CompRewardConfig = {
    1001: {
        'RoomChallenge': {
            'Weight': {
                DEVICECOMP_TYPE_DEVICE: 100 },
            'Num': 1,
            'ForceNum': { } },
        'Boss': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 15,
                DEVICECOMP_TYPE_DEVICE: 85 },
            'Num': 2,
            'ForceNum': {
                DEVICECOMP_TYPE_DEVICE: 1 } },
        'PassBox': {
            'Weight': {
                DEVICECOMP_TYPE_DEVICE: 30,
                DEVICECOMP_TYPE_COMMON: 70 },
            'Num': 1,
            'ForceNum': { } },
        'DeviceChallenge': {
            'Weight': {
                DEVICECOMP_TYPE_DEVICE: 70,
                DEVICECOMP_TYPE_COMMON: 30 },
            'Num': 1,
            'ForceNum': { } } },
    1002: {
        'RoomChallenge': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 25,
                DEVICECOMP_TYPE_DEVICE: 75 },
            'Num': 1,
            'ForceNum': { } },
        'Boss': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 25,
                DEVICECOMP_TYPE_DEVICE: 75 },
            'Num': 2,
            'ForceNum': {
                DEVICECOMP_TYPE_DEVICE: 1 } },
        'PassBox': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 5,
                DEVICECOMP_TYPE_DEVICE: 25,
                DEVICECOMP_TYPE_COMMON: 70 },
            'Num': 1,
            'ForceNum': { } },
        'DeviceChallenge': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 20,
                DEVICECOMP_TYPE_DEVICE: 40,
                DEVICECOMP_TYPE_COMMON: 30 },
            'Num': 1,
            'ForceNum': { } } },
    1003: {
        'RoomChallenge': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 25,
                DEVICECOMP_TYPE_DEVICE: 75 },
            'Num': 1,
            'ForceNum': { } },
        'Boss': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 25,
                DEVICECOMP_TYPE_DEVICE: 75 },
            'Num': 2,
            'ForceNum': {
                DEVICECOMP_TYPE_DEVICE: 1 } },
        'PassBox': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 10,
                DEVICECOMP_TYPE_DEVICE: 30,
                DEVICECOMP_TYPE_COMMON: 70 },
            'Num': 1,
            'ForceNum': { } },
        'DeviceChallenge': {
            'Weight': {
                DEVICECOMP_TYPE_HERO: 15,
                DEVICECOMP_TYPE_DEVICE: 70,
                DEVICECOMP_TYPE_COMMON: 30 },
            'Num': 1,
            'ForceNum': { } } } }

def GetCompRewardConfig(iSID):
    if iSID in g_CompRewardConfig:
        return g_CompRewardConfig[iSID]
    return { }

